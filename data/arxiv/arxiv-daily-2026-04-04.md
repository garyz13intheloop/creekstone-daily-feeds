# arXiv AI 论文日报 | 2026-04-04

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (9 篇)
- [cs.LG](#csLG) (7 篇)

---

## cs.AI

## [1. Beyond the Assistant Turn: User Turn Generation as a Probe of Interaction Awareness in Language Models](https://arxiv.org/abs/2604.02315v1)

**作者**：Sarath Shekkizhar, Romain Cosentino, Adam Earle  
**分类**：cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Standard LLM benchmarks evaluate the assistant turn: the model generates a response to an input, a verifier scores correctness, and the analysis ends. This paradigm leaves unmeasured whether the LLM encodes any awareness of what follows the assistant response. We propose user-turn generation as a probe of this gap: given a conversation context of user query and assistant response, we let a model generate under the user role. If the model's weights encode interaction awareness, the generated user turn will be a grounded follow-up that reacts to the preceding context. Through experiments across $11$ open-weight LLMs (Qwen3.5, gpt-oss, GLM) and $5$ datasets (math reasoning, instruction following, conversation), we show that interaction awareness is decoupled from task accuracy. In particular, within the Qwen3.5 family, GSM8K accuracy scales from $41\%$ ($0.8$B) to $96.8\%$ ($397$B-A$17$B), yet genuine follow-up rates under deterministic generation remain near zero. In contrast, higher temperature sampling reveals interaction awareness is latent with follow up rates reaching $22\%$. Controlled perturbations validate that the proposed probe measures a real property of the model, and collaboration-oriented post-training on Qwen3.5-2B demonstrates an increase in follow-up rates. Our results show that user-turn generation captures a dimension of LLM behavior, interaction awareness, that is unexplored and invisible with current assistant-only benchmarks.

### 🤖 AI 总结

**一句话总结**：论文提出用“生成下一轮用户发言（user turn）”来探测大语言模型是否具备对对话后续走向的“交互感知”，并发现它与常规任务正确率并不一致。

**研究动机**：现有LLM评测几乎只看助手回合的答案对不对，忽略模型是否理解自己回答后用户会如何接续互动。作者希望测量这一“对后续交互的意识/建模能力”，补足assistant-only基准看不见的行为维度。

**核心方法**：给定“用户问题+助手回答”的对话上下文，让模型在“用户角色”下生成下一句用户跟进，并以其是否为贴合上下文的真实追问/反馈来衡量交互感知。作者在11个开源权重模型与5类数据集上对比不同解码策略（确定性/高温采样），并通过受控扰动与面向协作的后训练验证该指标确实在测量模型属性且可被提升。

**主要结论**：交互感知与任务准确率解耦：例如Qwen3.5系列GSM8K准确率大幅提升，但确定性生成下真实跟进率几乎为零。高温采样显示交互感知可能以“潜在能力”存在（跟进率可到22%），且通过协作导向的后训练可以显著提高该能力，说明用户回合生成能揭示现有基准忽视的新维度。

**关键词**：交互感知, 跟进问题生成, 评测探针, 助手轮次基准, 温度采样, 确定性解码, 任务准确率解耦, 协作式后训练

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02315v1) | [下载PDF](https://arxiv.org/pdf/2604.02315v1.pdf)

---

## [2. Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency](https://arxiv.org/abs/2604.02280v1)

**作者**：Payal Fofadiya, Sunil Tiwari  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Long-horizon conversational agents require persistent memory for coherent reasoning, yet uncontrolled accumulation causes temporal decay and false memory propagation. Benchmarks such as LOCOMO and LOCCO report performance degradation from 0.455 to 0.05 across stages, while MultiWOZ shows 78.2% accuracy with 6.8% false memory rate under persistent retention. This work introduces an adaptive budgeted forgetting framework that regulates memory through relevanceguided scoring and bounded optimization. The approach integrates recency, frequency, and semantic alignment to maintain stability under constrained context. Comparative analysis demonstrates improved long-horizon F1 beyond 0.583 baseline levels, higher retention consistency, and reduced false memory behavior without increasing context usage. These findings confirm that structured forgetting preserves reasoning performance while preventing unbounded memory growth in extended conversational settings.

### 🤖 AI 总结

**一句话总结**：论文提出一种自适应“预算化遗忘”机制，通过相关性评分与约束优化在长对话中控制记忆增长并降低错误记忆。

**研究动机**：长程对话代理需要持久记忆以保持推理连贯，但记忆无限累积会导致时间衰减与错误记忆传播，进而显著拉低基准表现。

**核心方法**：构建自适应预算遗忘框架，在固定上下文预算下用“新近性、频次、语义对齐”等指标进行相关性引导打分，并用有界优化策略选择保留/遗忘的记忆条目以维持稳定性与效率。

**主要结论**：相较基线（如长程F1约0.583），该方法在不增加上下文使用的前提下提升长程表现与保留一致性，并降低错误记忆行为，验证结构化遗忘能平衡相关性与计算/上下文效率。

**关键词**：持久化记忆, 自适应遗忘, 预算约束记忆, 相关性评分, 有界优化, 时间新近性, 访问频率, 语义对齐, 虚假记忆抑制, 长程对话评测基准

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02280v1) | [下载PDF](https://arxiv.org/pdf/2604.02280v1.pdf)

---

## [3. The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management](https://arxiv.org/abs/2604.02279v1)

**作者**：Andrew Ang, Nazym Azimbayev, Andrey Kim  
**分类**：cs.AI, cs.MA, q-fin.GN, q-fin.PM  
**发布时间**：2026-04-02

### 📄 论文摘要

Agentic AI shifts the investor's role from analytical execution to oversight. We present an agentic strategic asset allocation pipeline in which approximately 50 specialized agents produce capital market assumptions, construct portfolios using over 20 competing methods, and critique and vote on each other's output. A researcher agent proposes new portfolio construction methods not yet represented, and a meta-agent compares past forecasts against realized returns and rewrites agent code and prompts to improve future performance. The entire pipeline is governed by the Investment Policy Statement--the same document that guides human portfolio managers can now constrain and direct autonomous agents.

### 🤖 AI 总结

**一句话总结**：论文提出“自驾投资组合”式的多智能体资产配置架构，让AI在投资政策声明（IPS）约束下生成、评审并迭代优化机构级组合方案。

**研究动机**：传统机构资产配置高度依赖人工分析与经验，流程复杂且难以持续自我改进。作者希望用多智能体把投资者角色从“执行分析”转为“监督治理”，同时提升方法多样性与适应性。

**核心方法**：构建约50个专职智能体的战略资产配置流水线：生成资本市场假设、用20+组合构建方法并行产出方案、互相批判与投票择优；另设研究员智能体提出新方法，元智能体对比历史预测与实现收益并改写代码/提示以自我迭代，整体由IPS进行约束与对齐。

**主要结论**：该架构表明IPS可作为可执行的治理层，驱动多智能体实现端到端的机构资产配置与持续改进。通过方法竞赛、互评投票与基于回测/实现表现的自我修正，系统有望比单一模型或静态流程更稳健地生成并优化组合建议。

**关键词**：多智能体架构, 机构资产管理, 战略资产配置, 资本市场假设, 组合构建方法, 智能体互评投票, 研究员智能体, 回测与预测校准, 投资政策声明约束, 组合优化

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02279v1) | [下载PDF](https://arxiv.org/pdf/2604.02279v1.pdf)

---

## [4. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules](https://arxiv.org/abs/2604.02276v1)

**作者**：Keerat Guliani, Deepkamal Gill, David Landsman 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of source documents into structured Markdown; LLM-driven semantic decomposition into structured rule units; multi-criteria LLM-as-a-judge evaluation across 19 dimensions spanning metadata, definitions, and rule semantics; and iterative repair of low-scoring extractions within a bounded regeneration budget, where upstream components are repaired before rule units are evaluated. We evaluate De Jure across four models on three regulatory corpora spanning finance, healthcare, and AI governance. On the finance domain, De Jure yields consistent and monotonic improvement in extraction quality, reaching peak performance within three judge-guided iterations. De Jure generalizes effectively to healthcare and AI governance, maintaining high performance across both open- and closed-source models. In a downstream compliance question-answering evaluation via RAG, responses grounded in De Jure extracted rules are preferred over prior work in 73.8% of cases at single-rule retrieval depth, rising to 84.0% under broader retrieval, confirming that extraction fidelity translates directly into downstream utility. These results demonstrate that explicit, interpretable evaluation criteria can substitute for human annotation in complex regulatory domains, offering a scalable and auditable path toward regulation-grounded LLM alignment.

### 🤖 AI 总结

**一句话总结**：De Jure 提出一种无需人工标注的迭代式LLM自我修复流水线，将监管法规原文自动抽取为可机读的结构化规则，并显著提升下游合规问答效果。

**研究动机**：监管文件结构复杂且法律约束强，传统把法规转成规则的流程昂贵且依赖专家。作者希望用可解释的自动评测标准替代人工标注，实现跨领域、可审计的规则抽取与对齐。

**核心方法**：流水线包含四步：将文档规范化为结构化Markdown、用LLM做语义分解生成规则单元、由“LLM裁判”按19个维度对元数据/定义/规则语义进行多指标评分、在有限迭代预算内优先修复上游组件并对低分抽取进行迭代再生成。

**主要结论**：在金融、医疗与AI治理三类语料和多种开闭源模型上，De Jure 的抽取质量随迭代单调提升且通常三轮达峰；在RAG合规问答中，基于其规则的回答更常被偏好（单规则检索73.8%，更宽检索84.0%），表明自动可解释评测能有效替代人工标注并带来实际下游收益。

**关键词**：监管规则抽取, 结构化规则单元, 文档规范化, 语义分解, 多维度评测, 无标注抽取, 合规问答RAG, 可解释评估标准

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02276v1) | [下载PDF](https://arxiv.org/pdf/2604.02276v1.pdf)

---

## [5. Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models](https://arxiv.org/abs/2604.02236v1)

**作者**：Minda Zhao, Yutong Yang, Chufei Peng 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Emotional tone is pervasive in human communication, yet its influence on large language model (LLM) behaviour remains unclear. Here, we examine how first-person emotional framing in user-side queries affect LLM performance across six benchmark domains, including mathematical reasoning, medical question answering, reading comprehension, commonsense reasoning and social inference. Across models and tasks, static emotional prefixes usually produce only small changes in accuracy, suggesting that affective phrasing is typically a mild perturbation rather than a reliable general-purpose intervention. This stability is not uniform: effects are more variable in socially grounded tasks, where emotional context more plausibly interacts with interpersonal reasoning. Additional analyses show that stronger emotional wording induces only modest extra change, and that human-written prefixes reproduce the same qualitative pattern as LLM-generated ones. We then introduce EmotionRL, an adaptive emotional prompting framework that selects emotional framing adaptively for each query. Although no single emotion is consistently beneficial, adaptive selection yields more reliable gains than fixed emotional prompting. Together, these findings show that emotional tone is neither a dominant driver of LLM performance nor irrelevant noise, but a weak and input-dependent signal that can be exploited through adaptive control.

### 🤖 AI 总结

**一句话总结**：论文发现：在多数任务上，提示词的情绪化第一人称前缀对LLM准确率影响很小且不稳定，但通过对每个问题自适应选择情绪框架可获得更可靠的小幅提升。

**研究动机**：人类交流普遍带情绪色彩，但LLM是否会因用户提问的情绪语气而显著改变推理与回答质量仍缺乏系统证据，需要量化其影响边界与可用性。

**核心方法**：在六类基准任务（如数学推理、医学问答、阅读理解、常识推理、社会推断等）上，对多种模型注入固定的第一人称情绪前缀，比较不同情绪与强度、以及人写/模型生成前缀对性能的影响；并提出EmotionRL框架，用强化学习式的自适应策略为每个输入选择最合适的情绪提示。

**主要结论**：固定情绪前缀通常只带来轻微的准确率变化，且社会性/人际推断类任务更易受情绪语境影响；增强情绪强度也仅带来有限额外变化，而自适应选择情绪（EmotionRL）比固定情绪更可能获得稳定收益，说明情绪是“弱但可利用”的输入依赖信号。

**关键词**：情感提示, 情绪框架, 第一人称前缀, LLM行为影响, 跨任务评测, 数学推理, 医学问答, 常识推理, 自适应提示

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02236v1) | [下载PDF](https://arxiv.org/pdf/2604.02236v1.pdf)

---

## [6. Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](https://arxiv.org/abs/2604.02230v1)

**作者**：Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

For Large Language Models (LLMs) to be reliably deployed, models must effectively know when not to answer: abstain. Reasoning models, in particular, have gained attention for impressive performance on complex tasks. However, reasoning models have been shown to have worse abstention abilities. Taking the vulnerabilities of reasoning models into account, we propose our Query Misalignment Framework. Hallucinations resulting in failed abstention can be reinterpreted as LLMs answering the wrong question (rather than answering a question incorrectly). Based on this framework, we develop a new class of state-of-the-art abstention methods called Trace Inversion. First, we generate the reasoning trace of a model. Based on only the trace, we then reconstruct the most likely query that the model responded to. Finally, we compare the initial query with the reconstructed query. Low similarity score between the initial query and reconstructed query suggests that the model likely answered the question incorrectly and is flagged to abstain. Extensive experiments demonstrate that Trace Inversion effectively boosts abstention performance in four frontier LLMs across nine abstention QA datasets, beating competitive baselines in 33 out of 36 settings.

### 🤖 AI 总结

**一句话总结**：提出“推理轨迹反演（Trace Inversion）”来检测模型是否在“回答错问题”，以此提升LLM在不确定时的弃答（abstention）能力。

**研究动机**：推理型LLM虽然解题能力强，但在该弃答时更容易胡编，导致可靠性不足。作者将失败的弃答视为“问题-回答发生错位（misalignment）”，即模型实际上在回应一个被其误解的查询。

**核心方法**：先生成模型的推理轨迹，仅基于该轨迹反推出模型最可能在回答的“重构问题”。再将原始问题与重构问题做相似度比较，相似度低则判定模型可能答非所问并触发弃答。

**主要结论**：在四个前沿LLM与九个弃答QA数据集上，Trace Inversion显著提升弃答性能，并在36种设置中的33种优于强基线方法，验证了“问题错位检测”对减少幻觉与提升可靠性有效。

**关键词**：拒答评测, 推理模型, 幻觉检测, 查询错位, 推理轨迹, 轨迹反演, 查询重构, 相似度评分, 错误问题回答

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02230v1) | [下载PDF](https://arxiv.org/pdf/2604.02230v1.pdf)

---

## [7. When to ASK: Uncertainty-Gated Language Assistance for Reinforcement Learning](https://arxiv.org/abs/2604.02226v1)

**作者**：Juarez Monteiro, Nathan Gavenski, Gianlucca Zuin 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

Reinforcement learning (RL) agents often struggle with out-of-distribution (OOD) scenarios, leading to high uncertainty and random behavior. While language models (LMs) contain valuable world knowledge, larger ones incur high computational costs, hindering real-time use, and exhibit limitations in autonomous planning. We introduce Adaptive Safety through Knowledge (ASK), which combines smaller LMs with trained RL policies to enhance OOD generalization without retraining. ASK employs Monte Carlo Dropout to assess uncertainty and queries the LM for action suggestions only when uncertainty exceeds a set threshold. This selective use preserves the efficiency of existing policies while leveraging the language model's reasoning in uncertain situations. In experiments on the FrozenLake environment, ASK shows no improvement in-domain, but demonstrates robust navigation in transfer tasks, achieving a reward of 0.95. Our findings indicate that effective neuro-symbolic integration requires careful orchestration rather than simple combination, highlighting the need for sufficient model scale and effective hybridization mechanisms for successful OOD generalization.

### 🤖 AI 总结

**一句话总结**：ASK 通过“不确定性门控”在强化学习策略遇到高不确定性时才向语言模型求助，从而在无需重训的情况下提升分布外（OOD）任务表现。

**研究动机**：RL 智能体在 OOD 场景常因不确定性高而出现随机行为；直接引入大语言模型虽有知识优势但计算开销大且自主规划能力有限，难以实时使用。

**核心方法**：用 Monte Carlo Dropout 估计当前策略的不确定性，并设置阈值：仅当不确定性超过阈值时查询小型语言模型获取动作建议，否则沿用原有 RL 策略以保持效率与稳定性。

**主要结论**：在 FrozenLake 域内任务上几乎无提升，但在迁移/OOD 任务中显著更稳健（最高回报约 0.95）；结果表明神经-符号/LM-RL 的有效结合需要精心的协同机制而非简单拼接，并提示模型规模与混合策略设计对 OOD 泛化至关重要。

**关键词**：强化学习, 分布外泛化, 不确定性估计, 不确定性门控, 语言模型辅助决策, 动作建议, 神经符号融合, 迁移任务评测

**评分**：57

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02226v1) | [下载PDF](https://arxiv.org/pdf/2604.02226v1.pdf)

---

## [8. Blinded Radiologist and LLM-Based Evaluation of LLM-Generated Japanese Translations of Chest CT Reports: Comparative Study](https://arxiv.org/abs/2604.02207v1)

**作者**：Yosuke Yamagishi, Atsushi Takamatsu, Yasunori Hamaguchi 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-02

### 📄 论文摘要

Background: Accurate translation of radiology reports is important for multilingual research, clinical communication, and radiology education, but the validity of LLM-based evaluation remains unclear. Objective: To evaluate the educational suitability of LLM-generated Japanese translations of chest CT reports and compare radiologist assessments with LLM-as-a-judge evaluations. Methods: We analyzed 150 chest CT reports from the CT-RATE-JPN validation set. For each English report, a human-edited Japanese translation was compared with an LLM-generated translation by DeepSeek-V3.2. A board-certified radiologist and a radiology resident independently performed blinded pairwise evaluations across 4 criteria: terminology accuracy, readability, overall quality, and radiologist-style authenticity. In parallel, 3 LLM judges (DeepSeek-V3.2, Mistral Large 3, and GPT-5) evaluated the same pairs. Agreement was assessed using QWK and percentage agreement. Results: Agreement between radiologists and LLM judges was near zero (QWK=-0.04 to 0.15). Agreement between the 2 radiologists was also poor (QWK=0.01 to 0.06). Radiologist 1 rated terminology as equivalent in 59% of cases and favored the LLM translation for readability (51%) and overall quality (51%). Radiologist 2 rated readability as equivalent in 75% of cases and favored the human-edited translation for overall quality (40% vs 21%). All 3 LLM judges strongly favored the LLM translation across all criteria (70%-99%) and rated it as more radiologist-like in >93% of cases. Conclusions: LLM-generated translations were often judged natural and fluent, but the 2 radiologists differed substantially. LLM-as-a-judge showed strong preference for LLM output and negligible agreement with radiologists. For educational use of translated radiology reports, automated LLM-based evaluation alone is insufficient; expert radiologist review remains important.

### 🤖 AI 总结

**一句话总结**：研究发现：LLM生成的日文胸部CT报告翻译在流畅度上常被认为不错，但“LLM评审”几乎不与放射科医生一致且明显偏向LLM输出，教育用途不能只靠自动评估。

**研究动机**：放射学报告跨语言翻译对科研、临床沟通与教学重要，但用“LLM作为裁判”来验证翻译质量是否可靠仍缺乏证据。

**核心方法**：选取CT-RATE-JPN验证集150份英文胸部CT报告，将“人工润色日译”与DeepSeek-V3.2生成日译进行盲法两两对比；两名放射科医生（主治与住院医）按术语准确性、可读性、整体质量、放射科风格四维度评估，并由3个LLM裁判（DeepSeek-V3.2、Mistral Large 3、GPT-5）并行评审，用QWK与一致率衡量一致性。

**主要结论**：放射科医生与LLM裁判的一致性接近于零（QWK≈-0.04到0.15），两位放射科医生之间一致性也很差；而3个LLM裁判在各指标上强烈偏好LLM翻译（70%-99%）并认为其更“像放射科写法”（>93%），因此自动化LLM评估不足以替代专家审阅。

**关键词**：放射学报告翻译, 日语医学翻译, 胸部CT报告, LLM生成翻译, 盲法成对比较, 放射科专家评审, 评审一致性分析, 术语准确性评估, 可读性评估, 文风真实性评估

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02207v1) | [下载PDF](https://arxiv.org/pdf/2604.02207v1.pdf)

---

## [9. From High-Dimensional Spaces to Verifiable ODD Coverage for Safety-Critical AI-based Systems](https://arxiv.org/abs/2604.02198v1)

**作者**：Thomas Stefani, Johann Maximilian Christensen, Elena Hoemann 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

While Artificial Intelligence (AI) offers transformative potential for operational performance, its deployment in safety-critical domains such as aviation requires strict adherence to rigorous certification standards. Current EASA guidelines mandate demonstrating complete coverage of the AI/ML constituent's Operational Design Domain (ODD) -- a requirement that demands proof that no critical gaps exist within defined operational boundaries. However, as systems operate within high-dimensional parameter spaces, existing methods struggle to provide the scalability and formal grounding necessary to satisfy the completeness criterion. Currently, no standardized engineering method exists to bridge the gap between abstract ODD definitions and verifiable evidence. This paper addresses this void by proposing a method that integrates parameter discretization, constraint-based filtering, and criticality-based dimension reduction into a structured, multi-step ODD coverage verification process. Grounded in gathered simulation data from prior research on AI-based mid-air collision avoidance research, this work demonstrates a systematic engineering approach to defining and achieving coverage metrics that satisfy EASA's demand for completeness. Ultimately, this method enables the validation of ODD coverage in higher dimensions, advancing a Safety-by-Design approach while complying with EASA's standards.

### 🤖 AI 总结

**一句话总结**：论文提出一套面向航空等安全关键AI系统的可验证ODD覆盖工程方法，通过离散化、约束过滤与关键性降维在高维空间中构造满足EASA“完备性”要求的覆盖证据。

**研究动机**：EASA要求证明AI/ML组成部分在其ODD内“完全覆盖且无关键空白”，但ODD往往处于高维参数空间，现有方法难以规模化并缺乏形式化可验证依据。工程上也缺少将抽象ODD定义转化为可审计覆盖证据的标准化流程。

**核心方法**：方法将ODD覆盖验证拆成多步流程：先对参数空间进行离散化生成候选场景，再用约束/规则进行可行性过滤，最后基于风险/关键性对维度进行缩减以聚焦关键变量并定义覆盖度量。并利用既有的AI空中防撞（mid-air collision avoidance）仿真数据展示如何计算与论证覆盖指标。

**主要结论**：该流程在更高维ODD中仍能系统化地产生覆盖度量与证据链，支持“Safety-by-Design”并更贴合EASA对ODD完备覆盖的合规审查需求。论文用防撞仿真数据示例说明该方法可落地地桥接ODD定义与可验证覆盖证明。

**关键词**：ODD覆盖验证, 高维参数空间, 参数离散化, 约束求解过滤, 关键性驱动降维, 覆盖度量指标, 安全关键认证, 航空运行场景, 仿真数据验证, 中空防撞系统, 安全性设计

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02198v1) | [下载PDF](https://arxiv.org/pdf/2604.02198v1.pdf)

---

## cs.CL

## [10. No Single Best Model for Diversity: Learning a Router for Sample Diversity](https://arxiv.org/abs/2604.02319v1)

**作者**：Yuhan Liu, Fangyuan Xu, Vishakh Padmakumar 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-02

### 📄 论文摘要

When posed with prompts that permit a large number of valid answers, comprehensively generating them is the first step towards satisfying a wide range of users. In this paper, we study methods to elicit a comprehensive set of valid responses. To evaluate this, we introduce \textbf{diversity coverage}, a metric that measures the total quality scores assigned to each \textbf{unique} answer in the predicted answer set relative to the best possible answer set with the same number of answers. Using this metric, we evaluate 18 LLMs, finding no single model dominates at generating diverse responses to a wide range of open-ended prompts. Yet, per each prompt, there exists a model that outperforms all other models significantly at generating a diverse answer set. Motivated by this finding, we introduce a router that predicts the best model for each query. On NB-Wildchat, our trained router outperforms the single best model baseline (26.3% vs $23.8%). We further show generalization to an out-of-domain dataset (NB-Curated) as well as different answer-generation prompting strategies. Our work lays foundation for studying generating comprehensive answers when we have access to a suite of models.

### 🤖 AI 总结

**一句话总结**：论文提出“多样性覆盖度”指标衡量开放式问题的答案多样性，并训练一个路由器为每个查询选择最能产出多样答案的LLM，从而优于单一最佳模型。

**研究动机**：开放式提示往往存在大量合理答案，想要“全面覆盖”就需要高质量且互不重复的答案集合；但不同LLM在不同提示上的多样性表现不稳定，难以用单一模型通吃。

**核心方法**：提出diversity coverage指标：在固定答案数量下，比较预测答案集中“唯一答案”的质量总和与最优可达集合的相对表现；评测18个LLM后训练一个router为每个query预测应调用的最佳模型，并验证其在不同数据集与不同生成提示策略下的泛化。

**主要结论**：不存在在各类开放式提示上都最擅长生成多样答案的单一模型，但对每个具体提示通常存在显著最优的模型；基于此的路由器在NB-Wildchat上超过单一最佳模型基线（26.3% vs 23.8%），并能迁移到域外数据与不同生成策略。

**关键词**：开放式生成, 回答集覆盖, 多样性覆盖指标, 答案去重, 质量打分, LLM对比评测, 模型路由, 查询级模型选择, 多模型集成, 多样性提示策略, 跨域泛化

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02319v1) | [下载PDF](https://arxiv.org/pdf/2604.02319v1.pdf)

---

## [11. CV-18 NER: Augmented Common Voice for Named Entity Recognition from Arabic Speech](https://arxiv.org/abs/2604.02209v1)

**作者**：Youssef Saidi, Haroun Elleuch, Fethi Bougares  
**分类**：cs.CL  
**发布时间**：2026-04-02

### 📄 论文摘要

End-to-end speech Named Entity Recognition (NER) aims to directly extract entities from speech. Prior work has shown that end-to-end (E2E) approaches can outperform cascaded pipelines for English, French, and Chinese, but Arabic remains under-explored due to its morphological complexity, the absence of short vowels, and limited annotated resources. We introduce CV-18 NER, the first publicly available dataset for NER from Arabic speech, created by augmenting the Arabic Common Voice 18 corpus with manual NER annotations following the fine-grained Wojood schema (21 entity types). We benchmark both pipeline systems (ASR + text NER) and E2E models based on Whisper and AraBEST-RQ. E2E systems substantially outperform the best pipeline configuration on the test set, reaching 37.0% CoER (AraBEST-RQ 300M) and 38.0% CVER (Whisper-medium). Further analysis shows that Arabic-specific self-supervised pretraining yields strong ASR performance, while multilingual weak supervision transfers more effectively to joint speech-to-entity learning, and that larger models may be harder to adapt in this low-resource setting. Our dataset and models are publicly released, providing the first open benchmark for end-to-end named entity recognition from Arabic speech https://huggingface.co/datasets/Elyadata/CV18-NER.

### 🤖 AI 总结

**一句话总结**：本文发布并基准测试了首个公开的阿拉伯语语音端到端命名实体识别数据集 CV-18 NER，证明端到端模型在该任务上显著优于“ASR+文本NER”的流水线方案。

**研究动机**：阿拉伯语因形态复杂、缺少短元音且标注资源稀缺，使得语音到实体的NER研究不足，亟需公开数据集与可复现实验基准来推动进展。

**核心方法**：在 Arabic Common Voice 18 上依据细粒度 Wojood 标注体系（21类实体）进行人工NER标注构建 CV-18 NER，并对比评测流水线（ASR→文本NER）与基于 Whisper、AraBEST-RQ 的端到端语音到实体模型。

**主要结论**：端到端系统在测试集上明显优于最佳流水线配置（如 AraBEST-RQ 300M 达到 37.0% CoER、Whisper-medium 达到 38.0% CVER）；分析还表明阿语自监督预训练更利于ASR，而多语弱监督更利于联合“语音→实体”学习，且低资源下更大模型可能更难适配。

**关键词**：端到端语音实体识别, 阿拉伯语语音NER, 语音到实体抽取, 低资源语音标注数据集, Wojood 实体类型体系, 级联系统（ASR+文本NER）, 自监督语音预训练, 多语种弱监督迁移

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02209v1) | [下载PDF](https://arxiv.org/pdf/2604.02209v1.pdf)

---

## [12. Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Language Model](https://arxiv.org/abs/2604.02194v1)

**作者**：Jaemin Kim, Jae O Lee, Sumyeong Ahn 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Retrieval-Augmented Language Models (RALMs) have demonstrated significant potential in knowledge-intensive tasks; however, they remain vulnerable to performance degradation when presented with irrelevant or noisy retrieved contexts. Existing approaches to enhance robustness typically operate via coarse-grained parameter updates at the layer or module level, often overlooking the inherent neuron-level sparsity of Large Language Models (LLMs). To address this limitation, we propose Neuro-RIT (Neuron-guided Robust Instruction Tuning), a novel framework that shifts the paradigm from dense adaptation to precision-driven neuron alignment. Our method explicitly disentangles neurons that are responsible for processing relevant versus irrelevant contexts using attribution-based neuron mining. Subsequently, we introduce a two-stage instruction tuning strategy that enforces a dual capability for noise robustness: achieving direct noise suppression by functionally deactivating neurons exclusive to irrelevant contexts, while simultaneously optimizing targeted layers for evidence distillation. Extensive experiments across diverse QA benchmarks demonstrate that Neuro-RIT consistently outperforms strong baselines and robustness-enhancing methods.

### 🤖 AI 总结

**一句话总结**：Neuro-RIT 通过在神经元粒度上识别并抑制“处理无关检索信息”的神经元，同时强化证据蒸馏能力，从而提升 RAG 语言模型在噪声检索下的鲁棒性。

**研究动机**：现有增强 RALM 鲁棒性的方法多在层/模块级进行粗粒度更新，忽视了 LLM 天生的神经元稀疏与功能分化，导致面对无关或噪声检索上下文时仍易性能退化。

**核心方法**：先用基于归因(Attribution)的神经元挖掘区分“负责相关证据处理”和“倾向无关上下文”的神经元；再采用两阶段指令微调：一方面功能性停用仅与无关上下文相关的神经元以实现噪声抑制，另一方面对目标层进行优化以提升证据提炼/蒸馏能力。

**主要结论**：在多种 QA 基准上，Neuro-RIT 相比强基线与既有鲁棒性方法取得更稳定、更高的表现，证明神经元级对齐与双阶段调优能有效缓解检索噪声带来的性能下降。

**关键词**：检索增强语言模型, RAG 鲁棒性, 噪声检索上下文, 神经元级稀疏性, 归因分析, 神经元挖掘, 神经元对齐, 指令微调, 神经元功能失活, 证据蒸馏, 问答基准评测

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02194v1) | [下载PDF](https://arxiv.org/pdf/2604.02194v1.pdf)

---

## cs.CV

## [13. EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors](https://arxiv.org/abs/2604.02331v1)

**作者**：Luca Bartolomei, Fabio Tosi, Matteo Poggi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

We propose EventHub, a novel framework for training deep-event stereo networks without ground truth annotations from costly active sensors, relying instead on standard color images. From these images, we derive either proxy annotations and proxy events through state-of-the-art novel view synthesis techniques, or simply proxy annotations when images are already paired with event data. Using the training set generated by our data factory, we repurpose state-of-the-art stereo models from RGB literature to process event data, obtaining new event stereo models with unprecedented generalization capabilities. Experiments on widely used event stereo datasets support the effectiveness of EventHub and show how the same data distillation mechanism can improve the accuracy of RGB stereo foundation models in challenging conditions such as nighttime scenes.

### 🤖 AI 总结

**一句话总结**：EventHub通过从普通彩色图像生成“代理事件/代理标注”来训练事件相机双目网络，从而无需昂贵的主动传感器真值也能获得更强泛化能力的事件双目模型。

**研究动机**：事件双目深度估计通常依赖激光雷达/结构光等主动传感器提供真值标注，成本高且数据覆盖受限，导致模型泛化不足。作者希望仅用更易获取的RGB数据（以及可选的事件数据）构建可扩展的训练数据管线。

**核心方法**：提出数据工厂EventHub：利用新视角合成等技术从RGB图像蒸馏出视差/深度等代理标注，并可进一步生成代理事件（若原始数据无事件）；若已有图像+事件对，则只需生成代理标注。随后将RGB双目领域的SOTA立体匹配网络“改造/迁移”到事件输入上，用蒸馏数据进行训练以获得新的事件双目模型。

**主要结论**：在多种事件双目基准上，EventHub训练出的模型表现出更好的准确性与前所未有的泛化能力；同样的数据蒸馏机制也能提升RGB双目基础模型在夜间等困难场景下的效果。

**关键词**：事件相机立体匹配, 事件立体深度估计, 无真值训练, 代理标注, 代理事件生成, 新视角合成, 数据蒸馏, RGB到事件域迁移, 立体网络泛化, 夜间立体视觉

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02331v1) | [下载PDF](https://arxiv.org/pdf/2604.02331v1.pdf)

---

## [14. Modulate-and-Map: Crossmodal Feature Mapping with Cross-View Modulation for 3D Anomaly Detection](https://arxiv.org/abs/2604.02328v1)

**作者**：Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

We present ModMap, a natively multiview and multimodal framework for 3D anomaly detection and segmentation. Unlike existing methods that process views independently, our method draws inspiration from the crossmodal feature mapping paradigm to learn to map features across both modalities and views, while explicitly modelling view-dependent relationships through feature-wise modulation. We introduce a cross-view training strategy that leverages all possible view combinations, enabling effective anomaly scoring through multiview ensembling and aggregation. To process high-resolution 3D data, we train and publicly release a foundational depth encoder tailored to industrial datasets. Experiments on SiM3D, a recent benchmark that introduces the first multiview and multimodal setup for 3D anomaly detection and segmentation, demonstrate that ModMap attains state-of-the-art performance by surpassing previous methods by wide margins.

### 🤖 AI 总结

**一句话总结**：ModMap提出一种原生多视角+多模态的3D异常检测框架，通过跨模态特征映射与跨视角调制建模视角关系，在SiM3D上取得显著SOTA。

**研究动机**：现有3D异常检测方法往往将不同视角独立处理，难以充分利用多视角间的互补信息与视角相关差异。为提升多视角多模态场景下的异常评分与分割效果，需要显式学习跨模态/跨视角的对齐与融合机制。

**核心方法**：方法基于“跨模态特征映射”学习在不同模态与不同视角间进行特征映射，同时通过特征级调制（modulation）显式建模视角依赖关系。训练上采用跨视角组合策略利用所有视角配对，并在推理时进行多视角集成与聚合；同时训练并开源适配工业数据的基础深度编码器以处理高分辨率3D数据。

**主要结论**：在SiM3D这一多视角多模态3D异常检测与分割基准上，ModMap以大幅优势超过以往方法，达到当前最优表现，验证了跨模态映射与跨视角调制/训练策略的有效性。

**关键词**：3D异常检测, 3D异常分割, 多视角学习, 多模态融合, 跨模态特征映射, 跨视角调制, 视角依赖建模, 跨视角训练, 多视角集成, 深度编码器, 工业视觉检测

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02328v1) | [下载PDF](https://arxiv.org/pdf/2604.02328v1.pdf)

---

## [15. Steerable Visual Representations](https://arxiv.org/abs/2604.02327v1)

**作者**：Jona Ruthardt, Manu Gaur, Deva Ramanan 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Pretrained Vision Transformers (ViTs) such as DINOv2 and MAE provide generic image features that can be applied to a variety of downstream tasks such as retrieval, classification, and segmentation. However, such representations tend to focus on the most salient visual cues in the image, with no way to direct them toward less prominent concepts of interest. In contrast, Multimodal LLMs can be guided with textual prompts, but the resulting representations tend to be language-centric and lose their effectiveness for generic visual tasks. To address this, we introduce Steerable Visual Representations, a new class of visual representations, whose global and local features can be steered with natural language. While most vision-language models (e.g., CLIP) fuse text with visual features after encoding (late fusion), we inject text directly into the layers of the visual encoder (early fusion) via lightweight cross-attention. We introduce benchmarks for measuring representational steerability, and demonstrate that our steerable visual features can focus on any desired objects in an image while preserving the underlying representation quality. Our method also matches or outperforms dedicated approaches on anomaly detection and personalized object discrimination, exhibiting zero-shot generalization to out-of-distribution tasks.

### 🤖 AI 总结

**一句话总结**：提出一种可被自然语言“引导/转向”的视觉表征方法，使预训练ViT的全局与局部特征能按提示聚焦任意目标，同时保持通用视觉表征能力。

**研究动机**：现有预训练ViT特征往往只关注图像中最显著线索，难以让表示转向不显眼但用户关心的概念；而多模态LLM虽可用文本引导，但得到的表示偏语言中心，做通用视觉任务时效果会下降。

**核心方法**：在视觉编码器内部进行“早期融合”，通过轻量级跨注意力将文本注入ViT各层，从而让全局/局部视觉特征可被提示词可控地重加权与聚焦；同时提出衡量表征“可引导性”的基准来评测该能力与表征质量保持情况。

**主要结论**：实验表明该可引导视觉特征能根据文本提示聚焦任意期望对象且不损害底层表征质量，并在异常检测与个性化目标区分等任务上达到或超过专用方法，同时具备零样本的分布外泛化能力。

**关键词**：视觉表征可控性, 早期融合, 跨注意力, 视觉-语言引导, 可提示视觉特征, 全局-局部特征, 表征可控性评测基准, 零样本泛化, 异常检测, 个性化目标区分

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02327v1) | [下载PDF](https://arxiv.org/pdf/2604.02327v1.pdf)

---

## [16. Beyond Referring Expressions: Scenario Comprehension Visual Grounding](https://arxiv.org/abs/2604.02323v1)

**作者**：Ruozhen He, Nisarg A. Shah, Qihua Dong 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Existing visual grounding benchmarks primarily evaluate alignment between image regions and literal referring expressions, where models can often succeed by matching a prominent named category. We explore a complementary and more challenging setting of scenario-based visual grounding, where the target must be inferred from roles, intentions, and relational context rather than explicit naming. We introduce Referring Scenario Comprehension (RSC), a benchmark designed for this setting. The queries in this benchmark are paragraph-length texts that describe object roles, user goals, and contextual cues, including deliberate references to distractor objects that often require deep understanding to resolve. Each instance is annotated with interpretable difficulty tags for uniqueness, clutter, size, overlap, and position which expose distinct failure modes and support fine-grained analysis. RSC contains approximately 31k training examples, 4k in-domain test examples, and a 3k out-of-distribution split with unseen object categories. We further propose ScenGround, a curriculum reasoning method serving as a reference point for this setting, combining supervised warm-starting with difficulty-aware reinforcement learning. Experiments show that scenario-based queries expose systematic failures in current models that standard benchmarks do not reveal, and that curriculum training improves performance on challenging slices and transfers to standard benchmarks.

### 🤖 AI 总结

**一句话总结**：论文提出“场景理解式视觉指代”(RSC)基准，用段落级场景描述来定位目标物体，并给出课程化训练方法ScenGround以提升在复杂推理型视觉定位任务上的表现。

**研究动机**：现有视觉定位基准多依赖“字面指代表达+显著类别匹配”，模型可能通过关键词/类别捷径取得高分，难以衡量对角色、意图与关系上下文的真实理解能力。

**核心方法**：构建RSC数据集：查询为包含角色、目标、上下文及干扰项的段落文本，并为每个样本标注可解释难度标签（唯一性、拥挤、大小、重叠、位置）以及提供域内/域外（未见类别）测试划分；提出ScenGround：先监督预热，再进行难度感知的强化学习课程训练以逐步攻克更难样本。

**主要结论**：实验表明，场景式查询能揭示现有模型在标准基准中不易暴露的系统性失败模式；采用课程化训练可显著改善高难度切片表现，并对传统视觉指代基准具有一定迁移增益。

**关键词**：视觉定位, 情景式视觉定位, 角色意图推理, 关系上下文推理, 长文本指代表达, 干扰物消解, 难度标注标签, 分布外泛化, 课程学习, 难度感知强化学习

**评分**：82

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02323v1) | [下载PDF](https://arxiv.org/pdf/2604.02323v1.pdf)

---

## [17. Large-scale Codec Avatars: The Unreasonable Effectiveness of Large-scale Avatar Pretraining](https://arxiv.org/abs/2604.02320v1)

**作者**：Junxuan Li, Rawal Khirodkar, Chengan He 等 40 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-04-02

### 📄 论文摘要

High-quality 3D avatar modeling faces a critical trade-off between fidelity and generalization. On the one hand, multi-view studio data enables high-fidelity modeling of humans with precise control over expressions and poses, but it struggles to generalize to real-world data due to limited scale and the domain gap between the studio environment and the real world. On the other hand, recent large-scale avatar models trained on millions of in-the-wild samples show promise for generalization across a wide range of identities, yet the resulting avatars are often of low-quality due to inherent 3D ambiguities. To address this, we present Large-Scale Codec Avatars (LCA), a high-fidelity, full-body 3D avatar model that generalizes to world-scale populations in a feedforward manner, enabling efficient inference. Inspired by the success of large language models and vision foundation models, we present, for the first time, a pre/post-training paradigm for 3D avatar modeling at scale: we pretrain on 1M in-the-wild videos to learn broad priors over appearance and geometry, then post-train on high-quality curated data to enhance expressivity and fidelity. LCA generalizes across hair styles, clothing, and demographics while providing precise, fine-grained facial expressions and finger-level articulation control, with strong identity preservation. Notably, we observe emergent generalization to relightability and loose garment support to unconstrained inputs, and zero-shot robustness to stylized imagery, despite the absence of direct supervision.

### 🤖 AI 总结

**一句话总结**：提出LCA：通过“百万级野外视频预训练 + 高质量数据后训练”的范式，实现兼具高保真与强泛化的全身3D头像，并可前馈高效推理与精细表情/手指控制。

**研究动机**：现有高保真多视角棚拍方法难以泛化到真实世界，而大规模野外数据训练的模型虽泛化强却因3D歧义导致质量偏低；因此需要一种同时兼顾质量与泛化、且推理高效的3D头像建模方案。

**核心方法**：提出大规模3D头像的预训练/后训练流程：先在1M野外视频上学习外观与几何的通用先验，再用高质量精修数据进行后训练以提升表现力与细节保真，并以feedforward方式生成可控的全身头像（含面部细粒度表情与手指级关节控制）。

**主要结论**：LCA在发型、服装与人群属性上具备世界规模泛化，同时保持强身份一致性与高质量细节；并出现无需直接监督的涌现能力，如对非受控输入的可重光照、宽松衣物支持，以及对风格化图像的零样本鲁棒性。

**关键词**：3D虚拟人建模, 全身头像, 大规模预训练, 预训练-后训练范式, 野外视频数据, 高保真重建, 前馈式推理, 表情驱动控制, 手指级关节控制, 可重光照, 宽松服装建模

**评分**：84

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02320v1) | [下载PDF](https://arxiv.org/pdf/2604.02320v1.pdf)

---

## [18. A Simple Baseline for Streaming Video Understanding](https://arxiv.org/abs/2604.02317v1)

**作者**：Yujiao Shen, Shulin Tian, Jingkang Yang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Recent streaming video understanding methods increasingly rely on complex memory mechanisms to handle long video streams. We challenge this trend with a simple finding: a sliding-window baseline that feeds only the most recent N frames to an off-the-shelf VLM already matches or surpasses published streaming models. We formalize this baseline as SimpleStream and evaluate it against 13 major offline and online video LLM baselines on OVO-Bench and StreamingBench. Despite its simplicity, SimpleStream delivers consistently strong performance. With only 4 recent frames, it reaches 67.7% average accuracy on OVO-Bench and 80.59% on StreamingBench. Controlled ablations further show that the value of longer context is backbone-dependent rather than uniformly increasing with model scale, and reveal a consistent perception-memory trade-off: adding more historical context can improve recall, but often weakens real-time perception. This suggests that stronger memory, retrieval, or compression modules should not be taken as evidence of progress unless they clearly outperform SimpleStream under the same protocol. We therefore argue that future streaming benchmarks should separate recent-scene perception from long-range memory, so that performance improvements from added complexity can be evaluated more clearly.

### 🤖 AI 总结

**一句话总结**：作者提出并验证了一个极简的流式视频理解基线：仅用滑动窗口输入最近N帧给现成VLM/Video-LLM，就能匹敌甚至超过许多带复杂记忆模块的流式方法。

**研究动机**：现有流式视频理解方法往往引入复杂记忆/检索/压缩机制来处理长视频，但其收益是否真实、是否优于简单强基线并不明确。作者希望用一个清晰、强力且易复现的基线，重新校准“复杂度=进步”的默认假设。

**核心方法**：提出SimpleStream：对视频流采用滑动窗口，仅保留并输入最近N帧（如4帧）到现成视觉语言模型进行理解，不使用额外显式记忆模块。并在OVO-Bench与StreamingBench上与13个主流离线/在线Video-LLM基线对比，同时做受控消融分析上下文长度与骨干模型的关系及感知-记忆权衡。

**主要结论**：SimpleStream在多个基准上表现稳定强劲（例如仅4帧即达OVO-Bench 67.7%、StreamingBench 80.59%），表明复杂记忆机制并非必然带来提升。更长历史上下文的价值依赖于骨干模型且存在“记忆增强可能削弱实时感知”的权衡，因此未来评测应区分近期场景感知与长程记忆，并要求复杂模块在同协议下明确超过SimpleStream。

**关键词**：滑动窗口, 视觉语言模型（VLM）, 视频LLM基线, 长时记忆机制, 上下文长度消融, 感知-记忆权衡, Simple, Baseline

**评分**：59

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02317v1) | [下载PDF](https://arxiv.org/pdf/2604.02317v1.pdf)

---

## [19. VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)

**作者**：Saman Motamed, William Harvey, Benjamin Klein 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Existing video object removal methods excel at inpainting content "behind" the object and correcting appearance-level artifacts such as shadows and reflections. However, when the removed object has more significant interactions, such as collisions with other objects, current models fail to correct them and produce implausible results. We present VOID, a video object removal framework designed to perform physically-plausible inpainting in these complex scenarios. To train the model, we generate a new paired dataset of counterfactual object removals using Kubric and HUMOTO, where removing an object requires altering downstream physical interactions. During inference, a vision-language model identifies regions of the scene affected by the removed object. These regions are then used to guide a video diffusion model that generates physically consistent counterfactual outcomes. Experiments on both synthetic and real data show that our approach better preserves consistent scene dynamics after object removal compared to prior video object removal methods. We hope this framework sheds light on how to make video editing models better simulators of the world through high-level causal reasoning.

### 🤖 AI 总结

**一句话总结**：VOID 提出一种面向“物体移除后连锁物理交互也要合理改变”的视频修复框架，使删除物体后的场景运动与因果结果更符合真实物理。

**研究动机**：现有视频物体移除多擅长补全被遮挡背景与外观伪影（阴影/反射），但当被删物体与其他物体发生碰撞等强交互时，后续运动仍沿用原轨迹而显得不可信。为此需要能在“反事实”层面改写下游动态的模型与数据。

**核心方法**：训练阶段用 Kubric 与 HUMOTO 合成成对“反事实移除”数据：移除某物体同时要求改变后续物理交互与运动结果。推理阶段用视觉-语言模型定位受该物体影响的区域，再以这些区域作为引导输入视频扩散模型，生成物理一致的反事实视频结果。

**主要结论**：在合成与真实数据实验中，VOID 相比既有方法能更好地保持删除物体后场景动力学的时序一致性与合理性，尤其在碰撞等复杂交互场景下更自然；作者强调该方向体现了通过高层因果推理提升视频编辑模型“世界模拟能力”的潜力。

**关键词**：视频目标移除, 交互感知修复, 物理一致性补全, 反事实视频生成, 视频扩散模型, 视觉-语言模型, 因果推理, 碰撞交互建模, 受影响区域定位, 合成配对数据集, 场景动力学一致性

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02296v1) | [下载PDF](https://arxiv.org/pdf/2604.02296v1.pdf)

---

## [20. Modular Energy Steering for Safe Text-to-Image Generation with Foundation Models](https://arxiv.org/abs/2604.02265v1)

**作者**：Yaoteng Tan, Zikui Cai, M. Salman Asif  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Controlling the behavior of text-to-image generative models is critical for safe and practical deployment. Existing safety approaches typically rely on model fine-tuning or curated datasets, which can degrade generation quality or limit scalability. We propose an inference-time steering framework that leverages gradient feedback from frozen pretrained foundation models to guide the generation process without modifying the underlying generator. Our key observation is that vision-language foundation models encode rich semantic representations that can be repurposed as off-the-shelf supervisory signals during generation. By injecting such feedback through clean latent estimates at each sampling step, our method formulates safety steering as an energy-based sampling problem. This design enables modular, training-free safety control that is compatible with both diffusion and flow-matching models and can generalize across diverse visual concepts. Experiments demonstrate state-of-the-art robustness against NSFW red-teaming benchmarks and effective multi-target steering, while preserving high generation quality on benign non-targeted prompts. Our framework provides a principled approach for utilizing foundation models as semantic energy estimators, enabling reliable and scalable safety control for text-to-image generation.

### 🤖 AI 总结

**一句话总结**：提出一种无需训练、在推理阶段利用冻结的视觉-语言基础模型梯度反馈来“能量引导”文本到图像生成，从而提升安全性且尽量不损伤画质。

**研究动机**：现有文生图安全控制多依赖微调或数据集筛选，往往带来生成质量下降、维护成本高或难以扩展到新概念的问题。作者希望用可复用的基础模型语义能力，在不改动生成器参数的前提下实现可扩展的安全控制。

**核心方法**：将视觉-语言基础模型视作语义“能量/监督信号”估计器，在每个采样步对“干净潜变量”注入由梯度反馈得到的引导，从而把安全约束转化为能量基采样的 steering 问题。该模块化框架训练-free，兼容扩散与flow-matching，并支持多目标/多概念同时引导。

**主要结论**：实验显示在NSFW红队基准上具备更强鲁棒性，并能实现有效的多目标安全引导，同时在非目标良性提示上保持较高生成质量，证明基础模型可作为可靠的语义能量估计器用于可扩展安全控制。

**关键词**：文本到图像安全, 推理时引导, 能量模型采样, 梯度反馈引导, 视觉语言基础模型, 语义能量估计, 干净潜变量估计, 扩散模型兼容, 流匹配模型, 多目标引导

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02265v1) | [下载PDF](https://arxiv.org/pdf/2604.02265v1.pdf)

---

## [21. SPAR: Single-Pass Any-Resolution ViT for Open-vocabulary Segmentation](https://arxiv.org/abs/2604.02252v1)

**作者**：Naomi Kombol, Ivan Martinović, Siniša Šegvić 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Foundational Vision Transformers (ViTs) have limited effectiveness in tasks requiring fine-grained spatial understanding, due to their fixed pre-training resolution and inherently coarse patch-level representations. These challenges are especially pronounced in dense prediction scenarios, such as open-vocabulary segmentation with ViT-based vision-language models, where high-resolution inputs are essential for accurate pixel-level reasoning. Existing approaches typically process large-resolution images using a sliding-window strategy at the pre-training resolution. While this improves accuracy through finer strides, it comes at a significant computational cost. We introduce SPAR: Single-Pass Any-Resolution ViT, a resolution-agnostic dense feature extractor designed for efficient high-resolution inference. We distill the spatial reasoning capabilities of a finely-strided, sliding-window teacher into a single-pass student using a feature regression loss, without requiring architectural changes or pixel-level supervision. Applied to open-vocabulary segmentation, SPAR improves single-pass baselines by up to 10.5 mIoU and even surpasses the teacher, demonstrating effectiveness in efficient, high-resolution reasoning. Code: https://github.com/naomikombol/SPAR

### 🤖 AI 总结

**一句话总结**：SPAR通过知识蒸馏把滑窗高分辨率推理的空间细粒度能力压缩到单次前向的ViT中，实现任意分辨率下高效开放词汇分割并显著提升精度。

**研究动机**：ViT受限于固定预训练分辨率与粗粒度patch表示，在像素级密集预测（如开放词汇分割）中高分辨率推理困难；现有滑窗策略虽提升精度但计算开销巨大。

**核心方法**：构建“细步长滑窗教师”在预训练分辨率上进行高质量密集特征提取，并用特征回归蒸馏损失将其空间推理能力迁移到“单次前向学生”ViT；无需改动架构，也不需要像素级监督即可在任意分辨率直接输出密集特征用于分割。

**主要结论**：在开放词汇分割任务上，SPAR相对单次前向基线最高提升10.5 mIoU，且在效率更高的同时可达到甚至超过滑窗教师的效果，证明其具备高效高分辨率空间推理能力。

**关键词**：开放词汇分割, 单次前向推理, 任意分辨率 ViT, 高分辨率推理, 稠密特征提取, 滑窗推理, 知识蒸馏, 特征回归损失, 视觉语言模型, 像素级推理

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02252v1) | [下载PDF](https://arxiv.org/pdf/2604.02252v1.pdf)

---

## [22. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models](https://arxiv.org/abs/2604.02241v1)

**作者**：Qiyao Zhang, Shuhua Zheng, Jianli Sun 等 9 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-02

### 📄 论文摘要

Embodied visual tracking is crucial for Unmanned Aerial Vehicles (UAVs) executing complex real-world tasks. In dynamic urban scenarios with complex semantic requirements, Vision-Language-Action (VLA) models show great promise due to their cross-modal fusion and continuous action generation capabilities. To benchmark multimodal tracking in such environments, we construct a dedicated evaluation benchmark and a large-scale dataset encompassing over 890K frames, 176 tasks, and 85 diverse objects. Furthermore, to address temporal feature redundancy and the lack of spatial geometric priors in existing VLA models, we propose an improved VLA tracking model, UAV-Track VLA. Built upon the $π_{0.5}$ architecture, our model introduces a temporal compression net to efficiently capture inter-frame dynamics. Additionally, a parallel dual-branch decoder comprising a spatial-aware auxiliary grounding head and a flow matching action expert is designed to decouple cross-modal features and generate fine-grained continuous actions. Systematic experiments in the CARLA simulator validate the superior end-to-end performance of our method. Notably, in challenging long-distance pedestrian tracking tasks, UAV-Track VLA achieves a 61.76\% success rate and 269.65 average tracking frames, significantly outperforming existing baselines. Furthermore, it demonstrates robust zero-shot generalization in unseen environments and reduces single-step inference latency by 33.4\% (to 0.0571s) compared to the original $π_{0.5}$, enabling highly efficient, real-time UAV control. Data samples and demonstration videos are available at: https://github.com/Hub-Tian/UAV-Track\_VLA.

### 🤖 AI 总结

**一句话总结**：本文提出面向复杂城市场景的无人机具身视觉跟踪VLA模型UAV-Track VLA，并构建大规模多模态跟踪数据集与基准，在CARLA中实现更高成功率与更低实时控制延迟。

**研究动机**：现有VLA跟踪在长时序视频中存在时间特征冗余、且缺乏空间几何先验，导致跨模态跟踪与连续动作控制在动态城市环境中表现受限；同时也缺少专门评测多模态无人机跟踪的统一基准与数据集。

**核心方法**：构建包含约890K帧、176个任务、85类对象的评测基准与数据集；在π_{0.5}架构上加入时间压缩网络以高效建模帧间动态，并设计并行双分支解码器：空间感知的辅助grounding头提供几何/定位先验，flow-matching动作专家生成细粒度连续控制，从而解耦跨模态特征并提升端到端控制效果。

**主要结论**：在CARLA系统实验中，UAV-Track VLA显著优于现有基线，长距离行人跟踪达到61.76%成功率与269.65平均跟踪帧数；同时具备未见环境的零样本泛化能力，并将单步推理延迟较原π_{0.5}降低33.4%至0.0571秒，支持更高效的实时无人机控制。

**关键词**：无人机视觉跟踪, 具身智能, 视觉-语言-动作模型（VLA）, 多模态跟踪基准, 大规模跟踪数据集, 时间特征压缩, 双分支解码器, 流匹配动作生成, 连续控制动作, 零样本泛化

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02241v1) | [下载PDF](https://arxiv.org/pdf/2604.02241v1.pdf)

---

## [23. SCALE: Semantic- and Confidence-Aware Conditional Variational Autoencoder for Zero-shot Skeleton-based Action Recognition](https://arxiv.org/abs/2604.02222v1)

**作者**：Soroush Oraki, Feng Ding, Jie Liang  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Zero-shot skeleton-based action recognition (ZSAR) aims to recognize action classes without any training skeletons from those classes, relying instead on auxiliary semantics from text. Existing approaches frequently depend on explicit skeleton-text alignment, which can be brittle when action names underspecify fine-grained dynamics and when unseen classes are semantically confusable. We propose SCALE, a lightweight and deterministic Semantic- and Confidence-Aware Listwise Energy-based framework that formulates ZSAR as class-conditional energy ranking. SCALE builds a text-conditioned Conditional Variational Autoencoder where frozen text representations parameterize both the latent prior and the decoder, enabling likelihood-based evaluation for unseen classes without generating samples at test time. To separate competing hypotheses, we introduce a semantic- and confidence-aware listwise energy loss that emphasizes semantically similar hard negatives and incorporates posterior uncertainty to adapt decision margins and reweight ambiguous training instances. Additionally, we utilize a latent prototype contrast objective to align posterior means with text-derived latent prototypes, improving semantic organization and class separability without direct feature matching. Experiments on NTU-60 and NTU-120 datasets show that SCALE consistently improves over prior VAE- and alignment-based baselines while remaining competitive with diffusion-based methods.

### 🤖 AI 总结

**一句话总结**：SCALE通过文本条件的CVAE与语义/置信度感知的listwise能量排序损失，在无需显式骨架-文本对齐和无需测试时生成样本的情况下提升零样本骨架动作识别性能。

**研究动机**：现有ZSAR方法常依赖显式骨架-文本对齐，但动作名称往往难以覆盖细粒度运动差异且未见类语义易混淆，导致对齐脆弱、判别边界不稳。作者希望用更稳健的似然/能量排名机制，并显式处理“相似类别难负样本”和“不确定样本”。

**核心方法**：构建文本条件CVAE：冻结的文本表征同时参数化潜变量先验与解码器，从而可对每个候选类别计算条件似然/能量并进行排名（测试时不采样）。提出语义与置信度感知的listwise能量损失，强化语义相近的hard negatives，并利用后验不确定性自适应调整间隔与重加权；再用潜空间原型对比目标将后验均值对齐到由文本生成的潜原型，以提升语义结构与类间可分性而非直接特征匹配。

**主要结论**：在NTU-60与NTU-120上，SCALE相较以VAE或对齐为主的基线取得稳定提升，并在性能上与扩散模型方法保持竞争力，同时保持框架轻量且推理确定性强。其结果表明：将ZSAR表述为条件能量/似然排名并结合语义相似度与不确定性建模，能显著缓解语义混淆与对齐脆弱问题。

**关键词**：零样本动作识别, 骨架动作识别, 文本语义条件, 条件变分自编码器, 类条件能量排序, 似然评估, 语义硬负样本, 后验不确定性, 潜变量原型对比学习, 文本编码冻结

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02222v1) | [下载PDF](https://arxiv.org/pdf/2604.02222v1.pdf)

---

## cs.LG

## [24. go-$m$HC: Direct Parameterization of Manifold-Constrained Hyper-Connections via Generalized Orthostochastic Matrices](https://arxiv.org/abs/2604.02309v1)

**作者**：Torque Dandachi, Sophia Diggs-Galligan  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-04-02

### 📄 论文摘要

Doubly stochastic matrices enable learned mixing across residual streams, but parameterizing the set of doubly stochastic matrices (the Birkhoff polytope) exactly and efficiently remains an open challenge. Existing exact methods scale factorially with the number of streams ($d$), while Kronecker-factorized approaches are efficient but expressivity-limited. We introduce a novel exact parameterization grounded in the theory of generalized orthostochastic matrices, which scales as $\mathcal{O}(d^3)$ and exposes a single hyperparameter $s$ which continuously interpolates between a computationally efficient boundary and the fully expressive Birkhoff polytope. Building on Manifold-Constrained Hyper-Connections ($m$HC), a framework for learned dynamic layer connectivity, we instantiate this parameterization in go-$m$HC. Our method composes naturally with Kronecker-factorized methods, substantially recovering expressivity at similar FLOP costs. Spectral analysis indicates that go-$m$HC fills the Birkhoff polytope far more completely than Kronecker-factorized baselines. On synthetic stream-mixing tasks, go-$m$HC achieves the minimum theoretical loss while converging up to $10\times$ faster. We validate our approach in a 30M parameter GPT-style language model. The expressivity, efficiency, and exactness of go-$m$HC offer a practical avenue for scaling $d$ as a new dimension of model capacity.

### 🤖 AI 总结

**一句话总结**：提出 go-$m$HC：用广义正交随机矩阵对双随机矩阵进行一种精确且高效的直接参数化，从而在近似相同计算成本下显著提升残差流混合/超连接的表达能力与训练效率。

**研究动机**：双随机矩阵可用于在多残差流之间学习混合，但对 Birkhoff 多面体（所有双随机矩阵集合）的“精确且可扩展”参数化仍困难：现有精确法随流数 $d$ 呈阶乘增长，而高效的 Kronecker 分解法又受表达力限制。

**核心方法**：基于“广义正交随机矩阵”理论给出一种精确参数化，复杂度为 $\mathcal{O}(d^3)$，并引入单一超参数 $s$ 在计算友好的边界与完全表达的 Birkhoff 多面体之间连续插值；将其嵌入 Manifold-Constrained Hyper-Connections 框架得到 go-$m$HC，并可与 Kronecker 因式分解自然组合以在相近 FLOPs 下补回表达力。

**主要结论**：谱分析表明 go-$m$HC 比 Kronecker 基线更充分覆盖 Birkhoff 多面体；在合成流混合任务上达到理论最小损失且收敛最高快约 10 倍，并在 30M 参数 GPT 风格语言模型上验证了其实用性，显示其可作为扩展流数 $d$ 这一容量维度的有效途径。

**关键词**：双随机矩阵, 精确参数化, 广义正交随机矩阵, 残差流混合, 流连接超连接, 流形约束超连接, 动态层连接, 谱分析, GPT 风格语言模型

**评分**：84

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02309v1) | [下载PDF](https://arxiv.org/pdf/2604.02309v1.pdf)

---

## [25. Taming the Exponential: A Fast Softmax Surrogate for Integer-Native Edge Inference](https://arxiv.org/abs/2604.02292v1)

**作者**：Dimitrios Danopoulos, Enrico Lupi, Michael Kagan 等 4 位作者  
**分类**：cs.LG, cs.AR  
**发布时间**：2026-04-02

### 📄 论文摘要

Softmax can become a computational bottleneck in the Transformer model's Multi-Head Attention (MHA) block, particularly in small models under low-precision inference, where exponentiation and normalization incur significant overhead. As such, we suggest using Head-Calibrated Clipped-Linear Softmax (HCCS), a bounded, monotone surrogate to the exponential softmax function, which uses a clipped linear mapping of the max centered attention logits. This approximation produces a stable probability distribution, maintains the ordering of the original logits and has non-negative values. HCCS differs from previous softmax surrogates as it includes a set of lightweight calibration parameters that are optimized offline based on a representative dataset and calibrated for each individual attention head to preserve the statistical properties of the individual heads. We describe a hardware-motivated implementation of HCCS for high-throughput scenarios targeting the AMD Versal AI Engines. The current reference implementations from AMD for this platform rely upon either bfloat16 arithmetic or LUTs to perform the exponential operation, which might limit the throughput of the platform and fail to utilize the high-throughput integer vector processing units of the AI Engine. In contrast, HCCS provides a natural mapping to the AI Engines' int8 multiply accumulate (MAC) units. To the best of our knowledge, this is the first int8 optimized softmax surrogate for AMD AI engines that significantly exceeds the speed performance of other reference implementations while maintaining competitive task accuracy on small or heavily quantized MHA workloads after quantization-aware retraining.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向整数推理的Softmax近似HCCS，用截断线性映射替代指数运算，在AMD Versal AI Engines上显著加速注意力计算并保持精度竞争力。

**研究动机**：在小模型与低精度（尤其int8）边缘推理中，Softmax的指数与归一化开销会成为MHA瓶颈，现有bfloat16或LUT实现限制吞吐且难以充分利用整数向量MAC单元。

**核心方法**：提出Head-Calibrated Clipped-Linear Softmax（HCCS）：对max-centered的attention logits做有界单调的“截断线性”映射生成非负权重，并为每个注意力头引入轻量校准参数，利用代表性数据离线优化以匹配各头统计特性；同时给出面向AMD AI Engines的硬件友好int8实现，并通过量化感知再训练保持任务精度。

**主要结论**：HCCS在AMD Versal AI Engines上能自然映射到int8 MAC实现，较AMD参考Softmax方案实现显著更高吞吐/速度，同时在小模型或重度量化的MHA场景中经过QAT后仍能维持具有竞争力的准确率。

**关键词**：截断线性映射, 注意力机制, 多头注意力, 低精度推理, int8 量化, 离线校准, 逐头校准, 高吞吐边缘推理, 量化感知训练

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02292v1) | [下载PDF](https://arxiv.org/pdf/2604.02292v1.pdf)

---

## [26. Model-Based Reinforcement Learning for Control under Time-Varying Dynamics](https://arxiv.org/abs/2604.02260v1)

**作者**：Klemens Iten, Bruce Lee, Chenhao Li 等 6 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-04-02

### 📄 论文摘要

Learning-based control methods typically assume stationary system dynamics, an assumption often violated in real-world systems due to drift, wear, or changing operating conditions. We study reinforcement learning for control under time-varying dynamics. We consider a continual model-based reinforcement learning setting in which an agent repeatedly learns and controls a dynamical system whose transition dynamics evolve across episodes. We analyze the problem using Gaussian process dynamics models under frequentist variation-budget assumptions. Our analysis shows that persistent non-stationarity requires explicitly limiting the influence of outdated data to maintain calibrated uncertainty and meaningful dynamic regret guarantees. Motivated by these insights, we propose a practical optimistic model-based reinforcement learning algorithm with adaptive data buffer mechanisms and demonstrate improved performance on continuous control benchmarks with non-stationary dynamics.

### 🤖 AI 总结

**一句话总结**：本文研究在系统动力学随时间变化的情况下，如何通过持续的模型式强化学习在控制中获得可靠不确定性估计与有意义的动态遗憾（regret）保证，并提出带自适应数据缓冲的乐观算法。

**研究动机**：许多学习控制方法默认动力学平稳，但现实系统常因漂移、磨损或工况变化而非平稳，导致旧数据误导模型与不确定性评估失准。作者希望在这种持续变化的环境中仍能得到理论上校准的不确定性与性能保证。

**核心方法**：在“跨episode演化”的持续模型式RL设定下，使用高斯过程（GP）动力学模型，并在频率学派的变动预算（variation-budget）假设下进行理论分析。基于分析结论，设计一种乐观的模型式RL算法，通过自适应数据缓冲/窗口机制限制过时数据影响，以维持不确定性校准并改进决策。

**主要结论**：理论表明持续非平稳性下必须显式削弱旧数据权重，否则会破坏不确定性校准并使动态regret保证失效。实验在非平稳连续控制基准上验证：带自适应缓冲的数据管理策略能显著提升性能。

**关键词**：时变动力学, 非平稳控制, 基于模型强化学习, 持续强化学习, 高斯过程动力学模型, 变动预算假设, 动态遗憾, 不确定性校准, 乐观探索, 自适应数据缓冲区, 连续控制基准

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02260v1) | [下载PDF](https://arxiv.org/pdf/2604.02260v1.pdf)

---

## [27. Smoothing the Landscape: Causal Structure Learning via Diffusion Denoising Objectives](https://arxiv.org/abs/2604.02250v1)

**作者**：Hao Zhu, Di Zhou, Donna Slonim  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-04-02

### 📄 论文摘要

Understanding causal dependencies in observational data is critical for informing decision-making. These relationships are often modeled as Bayesian Networks (BNs) and Directed Acyclic Graphs (DAGs). Existing methods, such as NOTEARS and DAG-GNN, often face issues with scalability and stability in high-dimensional data, especially when there is a feature-sample imbalance. Here, we show that the denoising score matching objective of diffusion models could smooth the gradients for faster, more stable convergence. We also propose an adaptive k-hop acyclicity constraint that improves runtime over existing solutions that require matrix inversion. We name this framework Denoising Diffusion Causal Discovery (DDCD). Unlike generative diffusion models, DDCD utilizes the reverse denoising process to infer a parameterized causal structure rather than to generate data. We demonstrate the competitive performance of DDCDs on synthetic benchmarking data. We also show that our methods are practically useful by conducting qualitative analyses on two real-world examples. Code is available at this url: https://github.com/haozhu233/ddcd.

### 🤖 AI 总结

**一句话总结**：提出DDCD框架，将扩散模型的去噪得分匹配目标用于因果结构学习，以获得更平滑的优化过程并提升高维DAG发现的稳定性与效率。

**研究动机**：现有DAG学习方法（如NOTEARS、DAG-GNN）在高维、样本-特征不平衡场景下常出现可扩展性差与训练不稳定的问题，需要更稳定且更快的优化目标与约束实现。

**核心方法**：利用扩散模型的反向去噪过程与denoising score matching目标来学习参数化因果结构，从而“平滑”梯度并加速收敛；同时提出自适应k-hop无环性（acyclicity）约束，避免依赖矩阵求逆以降低运行开销。

**主要结论**：在合成基准数据上DDCD表现具有竞争力，并在两个真实世界案例中展示了定性分析效果；总体上该方法能在高维因果发现中带来更稳定的训练与更好的运行效率。

**关键词**：因果结构学习, 贝叶斯网络, 观测数据因果推断, 扩散去噪, 去噪评分匹配, 反向去噪推断, 梯度平滑, 自适应k跳无环约束, 高维小样本, 可扩展稳定优化

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02250v1) | [下载PDF](https://arxiv.org/pdf/2604.02250v1.pdf)

---

## [28. Universal Hypernetworks for Arbitrary Models](https://arxiv.org/abs/2604.02215v1)

**作者**：Xuanfeng Zhou  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Conventional hypernetworks are typically engineered around a specific base-model parameterization, so changing the target architecture often entails redesigning the hypernetwork and retraining it from scratch. We introduce the \emph{Universal Hypernetwork} (UHN), a fixed-architecture generator that predicts weights from deterministic parameter, architecture, and task descriptors. This descriptor-based formulation decouples the generator architecture from target-network parameterization, so one generator can instantiate heterogeneous models across the tested architecture and task families. Our empirical claims are threefold: (1) one fixed UHN remains competitive with direct training across vision, graph, text, and formula-regression benchmarks; (2) the same UHN supports both multi-model generalization within a family and multi-task learning across heterogeneous models; and (3) UHN enables stable recursive generation with up to three intermediate generated UHNs before the final base model. Our code is available at https://github.com/Xuanfeng-Zhou/UHN.

### 🤖 AI 总结

**一句话总结**：提出通用超网络UHN，用固定生成器通过“描述符”预测权重，从而在不同架构与任务上实例化异构模型且性能接近直接训练。

**研究动机**：传统超网络往往与特定目标模型参数化强耦合，一旦更换架构就需要重设计并从头训练，难以在多模型/多任务场景复用。

**核心方法**：UHN使用确定性的参数、架构与任务描述符作为输入来生成目标网络权重，以描述符驱动的方式将生成器结构与目标网络参数化解耦，使同一个固定UHN可生成多种模型并支持跨任务训练。

**主要结论**：在视觉、图、文本与公式回归等基准上，一个固定UHN可与直接训练竞争；同一UHN同时支持家族内多模型泛化与跨异构模型的多任务学习，并能稳定进行最多三层的递归生成（先生成中间UHN再生成最终基模型）。

**关键词**：超网络, 权重生成, 参数描述符, 架构描述符, 任务描述符, 异构模型实例化, 跨模型泛化, 多任务学习, 递归生成, 公式回归, 跨模态基准评测

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02215v1) | [下载PDF](https://arxiv.org/pdf/2604.02215v1.pdf)

---

## [29. LEO: Graph Attention Network based Hybrid Multi Sensor Extended Object Fusion and Tracking for Autonomous Driving Applications](https://arxiv.org/abs/2604.02206v1)

**作者**：Mayank Mayank, Bharanidhar Duraisamy, Florian Geiss  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Accurate shape and trajectory estimation of dynamic objects is essential for reliable automated driving. Classical Bayesian extended-object models offer theoretical robustness and efficiency but depend on completeness of a-priori and update-likelihood functions, while deep learning methods bring adaptability at the cost of dense annotations and high compute. We bridge these strengths with LEO (Learned Extension of Objects), a spatio-temporal Graph Attention Network that fuses multi-modal production-grade sensor tracks to learn adaptive fusion weights, ensure temporal consistency, and represent multi-scale shapes. Using a task-specific parallelogram ground-truth formulation, LEO models complex geometries (e.g. articulated trucks and trailers) and generalizes across sensor types, configurations, object classes, and regions, remaining robust for challenging and long-range targets. Evaluations on the Mercedes-Benz DRIVE PILOT SAE L3 dataset demonstrate real-time computational efficiency suitable for production systems; additional validation on public datasets such as View of Delft (VoD) further confirms cross-dataset generalization.

### 🤖 AI 总结

**一句话总结**：LEO 使用时空图注意力网络对多传感器目标轨迹进行自适应融合，实现动态目标的高精度形状与轨迹联合估计，并具备实时性与跨数据集泛化能力。

**研究动机**：传统贝叶斯扩展目标模型虽稳健高效但依赖完备的先验与似然建模，而纯深度学习方法适应性强却需要密集标注且算力开销大；自动驾驶需要在复杂形状、远距离与多传感器配置下兼顾鲁棒性与工程可部署性。

**核心方法**：提出 LEO（Learned Extension of Objects），以多模态“传感器轨迹/track”为节点构建时空图，通过 Graph Attention 学习自适应融合权重并约束时间一致性，同时用多尺度形状表示与任务特定的平行四边形真值标注来刻画如卡车+挂车等复杂几何。

**主要结论**：在 Mercedes-Benz DRIVE PILOT SAE L3 数据集上，LEO 达到适合量产系统的实时计算效率并提升对挑战场景与长距离目标的鲁棒性；在 VoD 等公开数据集上的验证表明其能跨传感器类型、配置、类别与区域实现良好泛化。

**关键词**：扩展目标跟踪, 多传感器融合, 图注意力网络, 时空图神经网络, 自适应融合权重, 轨迹与形状估计, 多尺度形状表示, 平行四边形标注, 自动驾驶感知, 实时推理, 跨数据集泛化

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02206v1) | [下载PDF](https://arxiv.org/pdf/2604.02206v1.pdf)

---

## [30. On the Role of Depth in the Expressivity of RNNs](https://arxiv.org/abs/2604.02201v1)

**作者**：Maude Lizaire, Michael Rizvi-Martel, Éric Dupuis 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

The benefits of depth in feedforward neural networks are well known: composing multiple layers of linear transformations with nonlinear activations enables complex computations. While similar effects are expected in recurrent neural networks (RNNs), it remains unclear how depth interacts with recurrence to shape expressive power. Here, we formally show that depth increases RNNs' memory capacity efficiently with respect to the number of parameters, thus enhancing expressivity both by enabling more complex input transformations and improving the retention of past information. We broaden our analysis to 2RNNs, a generalization of RNNs with multiplicative interactions between inputs and hidden states. Unlike RNNs, which remain linear without nonlinear activations, 2RNNs perform polynomial transformations whose maximal degree grows with depth. We further show that multiplicative interactions cannot, in general, be replaced by layerwise nonlinearities. Finally, we validate these insights empirically on synthetic and real-world tasks.

### 🤖 AI 总结

**一句话总结**：论文从理论上证明增加深度能更高效（按参数量计）提升RNN的记忆容量与表达能力，并分析2RNN中深度如何提升多项式变换的阶数且乘法交互不可简单用逐层非线性替代。

**研究动机**：尽管深层前馈网络的表达优势已较清楚，但“深度”在RNN中如何与“递归记忆”共同作用、以及是否能以更少参数提升记忆与表达仍缺乏严格刻画。

**核心方法**：作者对深层RNN的记忆容量/表达性进行形式化分析，证明深度在参数效率上提升对历史信息的保留能力；并将分析扩展到含输入-隐状态乘法交互的2RNN，刻画其随深度增长的多项式变换最高次数，同时给出乘法交互不可一般性被层间非线性替代的论证，最后在合成与真实任务上做实验验证。

**主要结论**：深度不仅带来更复杂的输入变换，也能以更少参数显著提升RNN的记忆容量从而增强表达性；对2RNN而言，深度使其可实现的多项式变换次数上界随深度增长，且乘法交互提供了非线性层难以等价替代的表达增益，实验结果与理论结论一致。

**关键词**：表达能力, 记忆容量, 参数效率, 递归结构, 乘性交互, 多项式变换, 多项式阶数, 非线性激活替代性, 合成任务评测, 真实任务验证

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02201v1) | [下载PDF](https://arxiv.org/pdf/2604.02201v1.pdf)

---

