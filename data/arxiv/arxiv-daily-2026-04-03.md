# arXiv AI 论文日报 | 2026-04-03

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

**一句话总结**：论文提出用“生成下一轮用户发言（user-turn generation）”来探测LLM是否具备对对话后续走向的“交互感知”，并发现该能力与传统任务准确率并不同步。

**研究动机**：现有基准多只评估助手回合的正确性，忽略模型是否理解其回答会如何影响用户的下一步反应与对话进程，因此需要一个能衡量“回答之后会发生什么”的新探针。

**核心方法**：给定“用户提问+助手回答”的上下文，让模型以“用户角色”生成下一轮用户发言，并用“是否产生有根据的跟进（grounded follow-up）”作为交互感知指标；在多模型多数据集上比较确定性生成与高温采样，并通过受控扰动与针对性后训练验证指标有效性与可提升性。

**主要结论**：交互感知与任务准确率解耦：例如Qwen3.5在GSM8K准确率随规模显著提升，但确定性生成下真实跟进率接近零；高温采样显示该能力可能以潜在形式存在（跟进率可到22%），且通过协作导向的后训练可进一步提高跟进率，说明该维度在助手式基准中长期被忽视。

**关键词**：交互感知, 评测探针, 助手回合基准局限, 采样温度, 确定性解码, 开放权重LLM评测, 扰动验证, 协作式后训练, 任务准确率解耦

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

**一句话总结**：本文提出一种自适应、预算约束的“结构化遗忘”机制，在不增加上下文开销的前提下提升长对话智能体的记忆可靠性并降低虚假记忆。

**研究动机**：长时程对话需要持久记忆以保持推理连贯，但记忆无限累积会导致信息过时、性能退化与虚假记忆传播（基准中表现显著下降）。因此需要一种能在有限上下文中动态控制记忆规模且保持相关性的遗忘策略。

**核心方法**：提出自适应预算化遗忘框架：对记忆条目进行相关性引导评分，综合考虑新近性（recency）、频次（frequency）与语义对齐（semantic alignment），并通过有界优化在固定记忆预算下选择保留/遗忘内容，以维持稳定与效率。

**主要结论**：实验对比显示该方法在长时程任务上将F1提升到超过0.583的基线水平，同时提高保留一致性并降低虚假记忆率，且不需要增加上下文使用量，表明结构化遗忘能在扩展对话中兼顾性能与可控记忆增长。

**关键词**：持久记忆管理, 自适应遗忘, 预算约束记忆, 相关性评分, 有界优化, 时间新近性, 访问频率, 语义对齐, 虚假记忆抑制

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02280v1) | [下载PDF](https://arxiv.org/pdf/2604.02280v1.pdf)

---

## [3. The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management](https://arxiv.org/abs/2604.02279v1)

**作者**：Andrew Ang, Nazym Azimbayev, Andrey Kim  
**分类**：cs.AI, cs.MA, q-fin.GN, q-fin.PM  
**发布时间**：2026-04-02

### 📄 论文摘要

Agentic AI shifts the investor's role from analytical execution to oversight. We present an agentic strategic asset allocation pipeline in which approximately 50 specialized agents produce capital market assumptions, construct portfolios using over 20 competing methods, and critique and vote on each other's output. A researcher agent proposes new portfolio construction methods not yet represented, and a meta-agent compares past forecasts against realized returns and rewrites agent code and prompts to improve future performance. The entire pipeline is governed by the Investment Policy Statement--the same document that guides human portfolio managers can now constrain and direct autonomous agents.

### 🤖 AI 总结

**一句话总结**：Agentic AI shifts the investor's role from analytical execution to oversight. We present an agentic strategic asset allocation pipeline in which approximately 50 specialized agents produce capital mar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：机构资产管理, 战略资产配置, 多智能体架构, 资本市场假设预测, 组合构建方法集成, 智能体互评投票, 研究智能体生成新方法, 预测回测评估, 投资政策声明约束, 自主投资决策管线

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02279v1) | [下载PDF](https://arxiv.org/pdf/2604.02279v1.pdf)

---

## [4. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules](https://arxiv.org/abs/2604.02276v1)

**作者**：Keerat Guliani, Deepkamal Gill, David Landsman 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of source documents into structured Markdown; LLM-driven semantic decomposition into structured rule units; multi-criteria LLM-as-a-judge evaluation across 19 dimensions spanning metadata, definitions, and rule semantics; and iterative repair of low-scoring extractions within a bounded regeneration budget, where upstream components are repaired before rule units are evaluated. We evaluate De Jure across four models on three regulatory corpora spanning finance, healthcare, and AI governance. On the finance domain, De Jure yields consistent and monotonic improvement in extraction quality, reaching peak performance within three judge-guided iterations. De Jure generalizes effectively to healthcare and AI governance, maintaining high performance across both open- and closed-source models. In a downstream compliance question-answering evaluation via RAG, responses grounded in De Jure extracted rules are preferred over prior work in 73.8% of cases at single-rule retrieval depth, rising to 84.0% under broader retrieval, confirming that extraction fidelity translates directly into downstream utility. These results demonstrate that explicit, interpretable evaluation criteria can substitute for human annotation in complex regulatory domains, offering a scalable and auditable path toward regulation-grounded LLM alignment.

### 🤖 AI 总结

**一句话总结**：Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, ex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：监管规则抽取, 结构化规则表示, 法律文本解析, 多维度评价指标, 语义分解, 迭代修复, 文档规范化, 零标注抽取, 合规问答 RAG, 可审计对齐

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02276v1) | [下载PDF](https://arxiv.org/pdf/2604.02276v1.pdf)

---

## [5. Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models](https://arxiv.org/abs/2604.02236v1)

**作者**：Minda Zhao, Yutong Yang, Chufei Peng 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Emotional tone is pervasive in human communication, yet its influence on large language model (LLM) behaviour remains unclear. Here, we examine how first-person emotional framing in user-side queries affect LLM performance across six benchmark domains, including mathematical reasoning, medical question answering, reading comprehension, commonsense reasoning and social inference. Across models and tasks, static emotional prefixes usually produce only small changes in accuracy, suggesting that affective phrasing is typically a mild perturbation rather than a reliable general-purpose intervention. This stability is not uniform: effects are more variable in socially grounded tasks, where emotional context more plausibly interacts with interpersonal reasoning. Additional analyses show that stronger emotional wording induces only modest extra change, and that human-written prefixes reproduce the same qualitative pattern as LLM-generated ones. We then introduce EmotionRL, an adaptive emotional prompting framework that selects emotional framing adaptively for each query. Although no single emotion is consistently beneficial, adaptive selection yields more reliable gains than fixed emotional prompting. Together, these findings show that emotional tone is neither a dominant driver of LLM performance nor irrelevant noise, but a weak and input-dependent signal that can be exploited through adaptive control.

### 🤖 AI 总结

**一句话总结**：情绪化提示语通常只会对LLM在多类基准任务上的表现产生轻微且不稳定的影响，但通过按输入自适应选择情绪框架可获得更可靠的小幅收益。

**研究动机**：人类交流中情绪语气普遍存在，但其是否能稳定地提升或削弱LLM能力仍缺乏系统证据与跨任务验证。

**核心方法**：在数学推理、医学问答、阅读理解、常识推理、社会推断等六类基准上，对多种LLM施加第一人称情绪前缀（不同情绪与不同强度、含人写/模型写），评估准确率变化，并提出EmotionRL对每个查询自适应选择情绪提示。

**主要结论**：固定情绪前缀总体只是“温和扰动”，多数任务准确率变化很小；社会性更强的任务波动更大且更可能受情绪语境影响；更强烈措辞只带来有限增量，而自适应的EmotionRL比固定情绪提示更可能带来稳定的整体提升。

**关键词**：情感提示, 情感框架, 提示前缀, LLM 性能评估, 基准测试, 数学推理, 医学问答, 常识推理, 自适应提示

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02236v1) | [下载PDF](https://arxiv.org/pdf/2604.02236v1.pdf)

---

## [6. Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](https://arxiv.org/abs/2604.02230v1)

**作者**：Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

For Large Language Models (LLMs) to be reliably deployed, models must effectively know when not to answer: abstain. Reasoning models, in particular, have gained attention for impressive performance on complex tasks. However, reasoning models have been shown to have worse abstention abilities. Taking the vulnerabilities of reasoning models into account, we propose our Query Misalignment Framework. Hallucinations resulting in failed abstention can be reinterpreted as LLMs answering the wrong question (rather than answering a question incorrectly). Based on this framework, we develop a new class of state-of-the-art abstention methods called Trace Inversion. First, we generate the reasoning trace of a model. Based on only the trace, we then reconstruct the most likely query that the model responded to. Finally, we compare the initial query with the reconstructed query. Low similarity score between the initial query and reconstructed query suggests that the model likely answered the question incorrectly and is flagged to abstain. Extensive experiments demonstrate that Trace Inversion effectively boosts abstention performance in four frontier LLMs across nine abstention QA datasets, beating competitive baselines in 33 out of 36 settings.

### 🤖 AI 总结

**一句话总结**：提出“推理轨迹反演（Trace Inversion）”方法，通过比较原始问题与由推理轨迹反推的问题是否一致来判断模型应否弃答，从而显著提升LLM的abstention能力。

**研究动机**：推理型LLM在复杂任务上表现强，但在“不该回答时选择弃答”方面更脆弱，容易产生幻觉与错误自信。作者将这类失败重释为模型“答对了自己理解的另一个问题”（查询错位），从而寻找可检测的信号。

**核心方法**：先让模型生成其推理轨迹，再仅基于该轨迹重建模型最可能在回答的“隐含问题”，并与用户原始问题计算相似度。若相似度低则判定发生查询错位、触发弃答，从而形成一类新的弃答检测方法Trace Inversion。

**主要结论**：在四个前沿LLM与九个abstention QA数据集上，Trace Inversion整体显著提升弃答性能，并在36种设置中的33种超过具有竞争力的基线方法，表明“轨迹→问题反演+相似度”是有效的弃答判别信号。

**关键词**：拒答评测, 推理模型, 推理轨迹, 轨迹反演, 查询错位框架, 问题重构, 相似度检测, 幻觉检测, 问答数据集

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02230v1) | [下载PDF](https://arxiv.org/pdf/2604.02230v1.pdf)

---

## [7. When to ASK: Uncertainty-Gated Language Assistance for Reinforcement Learning](https://arxiv.org/abs/2604.02226v1)

**作者**：Juarez Monteiro, Nathan Gavenski, Gianlucca Zuin 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

Reinforcement learning (RL) agents often struggle with out-of-distribution (OOD) scenarios, leading to high uncertainty and random behavior. While language models (LMs) contain valuable world knowledge, larger ones incur high computational costs, hindering real-time use, and exhibit limitations in autonomous planning. We introduce Adaptive Safety through Knowledge (ASK), which combines smaller LMs with trained RL policies to enhance OOD generalization without retraining. ASK employs Monte Carlo Dropout to assess uncertainty and queries the LM for action suggestions only when uncertainty exceeds a set threshold. This selective use preserves the efficiency of existing policies while leveraging the language model's reasoning in uncertain situations. In experiments on the FrozenLake environment, ASK shows no improvement in-domain, but demonstrates robust navigation in transfer tasks, achieving a reward of 0.95. Our findings indicate that effective neuro-symbolic integration requires careful orchestration rather than simple combination, highlighting the need for sufficient model scale and effective hybridization mechanisms for successful OOD generalization.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) agents often struggle with out-of-distribution (OOD) scenarios, leading to high uncertainty and random behavior. While language models (LMs) contain valuable world knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：分布外泛化, 不确定性估计, 不确定性门控, 语言模型辅助, 强化学习策略, 动作建议, 选择性查询, 无需再训练, 迁移任务评测, 神经符号融合

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02226v1) | [下载PDF](https://arxiv.org/pdf/2604.02226v1.pdf)

---

## [8. Blinded Radiologist and LLM-Based Evaluation of LLM-Generated Japanese Translations of Chest CT Reports: Comparative Study](https://arxiv.org/abs/2604.02207v1)

**作者**：Yosuke Yamagishi, Atsushi Takamatsu, Yasunori Hamaguchi 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-02

### 📄 论文摘要

Background: Accurate translation of radiology reports is important for multilingual research, clinical communication, and radiology education, but the validity of LLM-based evaluation remains unclear. Objective: To evaluate the educational suitability of LLM-generated Japanese translations of chest CT reports and compare radiologist assessments with LLM-as-a-judge evaluations. Methods: We analyzed 150 chest CT reports from the CT-RATE-JPN validation set. For each English report, a human-edited Japanese translation was compared with an LLM-generated translation by DeepSeek-V3.2. A board-certified radiologist and a radiology resident independently performed blinded pairwise evaluations across 4 criteria: terminology accuracy, readability, overall quality, and radiologist-style authenticity. In parallel, 3 LLM judges (DeepSeek-V3.2, Mistral Large 3, and GPT-5) evaluated the same pairs. Agreement was assessed using QWK and percentage agreement. Results: Agreement between radiologists and LLM judges was near zero (QWK=-0.04 to 0.15). Agreement between the 2 radiologists was also poor (QWK=0.01 to 0.06). Radiologist 1 rated terminology as equivalent in 59% of cases and favored the LLM translation for readability (51%) and overall quality (51%). Radiologist 2 rated readability as equivalent in 75% of cases and favored the human-edited translation for overall quality (40% vs 21%). All 3 LLM judges strongly favored the LLM translation across all criteria (70%-99%) and rated it as more radiologist-like in >93% of cases. Conclusions: LLM-generated translations were often judged natural and fluent, but the 2 radiologists differed substantially. LLM-as-a-judge showed strong preference for LLM output and negligible agreement with radiologists. For educational use of translated radiology reports, automated LLM-based evaluation alone is insufficient; expert radiologist review remains important.

### 🤖 AI 总结

**一句话总结**：在胸部CT英文报告的日文翻译任务中，LLM评审与放射科医生评审几乎不一致且LLM评审显著偏向LLM译文，说明仅靠自动化LLM评测不适合教育用途的质量把关。

**研究动机**：放射学报告的准确翻译对多语言科研、临床沟通与教学很关键，但“用LLM当裁判”来评估翻译质量是否可信仍不清楚。

**核心方法**：选取CT-RATE-JPN验证集150份英文胸部CT报告，将人工润色日文译文与DeepSeek-V3.2生成译文配对盲评；两位放射科医师（主治+住院医）按术语准确性、可读性、总体质量、放射科风格四项进行两两比较，同时由DeepSeek-V3.2、Mistral Large 3、GPT-5三种LLM裁判对同样样本评估，并用QWK与一致率衡量一致性。

**主要结论**：放射科医师之间一致性也较差，而LLM裁判与放射科医师一致性接近于零且三种LLM裁判几乎全面偏好LLM译文（尤其认为更“放射科风格”）；因此，LLM译文虽常更自然流畅，但教育场景下不能仅依赖LLM自动评测，仍需专家审核。

**关键词**：放射学报告翻译, 胸部CT报告, 日英医学翻译, LLM翻译评测, 盲法配对比较, 放射科专家评审, 术语准确性, 可读性评估, 整体质量评估, 一致性检验（QWK）, 评测偏置

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02207v1) | [下载PDF](https://arxiv.org/pdf/2604.02207v1.pdf)

---

## [9. From High-Dimensional Spaces to Verifiable ODD Coverage for Safety-Critical AI-based Systems](https://arxiv.org/abs/2604.02198v1)

**作者**：Thomas Stefani, Johann Maximilian Christensen, Elena Hoemann 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

While Artificial Intelligence (AI) offers transformative potential for operational performance, its deployment in safety-critical domains such as aviation requires strict adherence to rigorous certification standards. Current EASA guidelines mandate demonstrating complete coverage of the AI/ML constituent's Operational Design Domain (ODD) -- a requirement that demands proof that no critical gaps exist within defined operational boundaries. However, as systems operate within high-dimensional parameter spaces, existing methods struggle to provide the scalability and formal grounding necessary to satisfy the completeness criterion. Currently, no standardized engineering method exists to bridge the gap between abstract ODD definitions and verifiable evidence. This paper addresses this void by proposing a method that integrates parameter discretization, constraint-based filtering, and criticality-based dimension reduction into a structured, multi-step ODD coverage verification process. Grounded in gathered simulation data from prior research on AI-based mid-air collision avoidance research, this work demonstrates a systematic engineering approach to defining and achieving coverage metrics that satisfy EASA's demand for completeness. Ultimately, this method enables the validation of ODD coverage in higher dimensions, advancing a Safety-by-Design approach while complying with EASA's standards.

### 🤖 AI 总结

**一句话总结**：论文提出一种面向航空等安全关键AI系统的可验证ODD覆盖验证流程，以在高维参数空间中满足EASA对“完整覆盖”的认证要求。

**研究动机**：EASA指南要求证明AI/ML构件的ODD在定义边界内不存在关键覆盖空洞，但高维运行参数空间使现有方法难以规模化且缺乏形式化依据。工程上也缺少将抽象ODD定义转化为可审计、可验证覆盖证据的标准化方法。

**核心方法**：方法将ODD参数离散化生成候选场景网格，再通过约束条件过滤剔除不可行/无效组合，并基于关键性（criticality）进行维度缩减以聚焦安全相关的子空间。随后形成结构化多步骤流程与覆盖度量，并利用既有的基于仿真的空中防撞AI研究数据进行验证与示例化。

**主要结论**：该流程在更高维度下仍能系统化地产生并验证ODD覆盖指标，为“无关键空洞”的完整性主张提供更可审计的证据。结果表明该方法有助于推进Safety-by-Design并更贴近EASA认证对ODD完整覆盖的要求。

**关键词**：ODD覆盖验证, 安全关键航空, 高维参数空间, 参数离散化, 约束过滤, 关键性驱动降维, 覆盖度量, 形式化完备性, 仿真数据驱动验证, 中空防撞避碰

**评分**：74

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

**一句话总结**：提出“多样性覆盖度（diversity coverage）”来衡量开放式问题的答案集合质量，并训练一个路由器为每个问题选择最擅长产出多样答案的LLM，从而整体优于单一最佳模型。

**研究动机**：开放式提示往往存在大量同样合理的答案，用户需求差异使“尽可能全面地产生多种有效回答”变得重要。实验发现不同模型在不同提示上各有优势、没有单一模型在多样性生成上全面占优，因此需要按问题动态选模型。

**核心方法**：定义diversity coverage指标：在固定生成答案数量下，比较预测答案集合中“唯一答案”的总质量得分与同规模最优答案集合的相对表现。评测18个LLM后，训练一个查询级路由器（router）预测每个prompt应调用哪个模型，并验证其在不同数据集与不同生成提示策略下的泛化。

**主要结论**：在NB-Wildchat上，路由器相较“单一最佳模型”基线提升多样性覆盖度（26.3% vs 23.8%），且能迁移到域外数据集NB-Curated与不同生成策略。结果表明：面向多样性与全面覆盖，模型集成+路由选择比追求一个“万能模型”更有效。

**关键词**：开放式问答, 样本多样性, 多样性覆盖度, 答案集合生成, 模型路由, 查询级模型选择, 多模型集成, 泛化评测, 提示策略鲁棒性

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

**一句话总结**：本文发布并基准测试了首个公开的阿拉伯语语音端到端命名实体识别数据集CV-18 NER，结果显示端到端模型显著优于传统ASR+文本NER流水线。

**研究动机**：阿拉伯语因形态复杂、短元音缺失且标注资源稀缺，使语音NER研究明显滞后于英语等语言，需要一个公开基准与可复现评测来推动端到端方法发展。

**核心方法**：在Arabic Common Voice 18上人工补充细粒度Wojood方案（21类实体）的NER标注，构建CV-18 NER；并对比评测流水线系统（ASR+文本NER）与基于Whisper、AraBEST-RQ的端到端语音到实体模型。

**主要结论**：端到端系统在测试集上显著超过最佳流水线配置（如AraBEST-RQ 300M达37.0% CoER、Whisper-medium达38.0% CVER）；分析表明阿语自监督预训练更利于ASR，而多语弱监督更利于联合语音到实体学习，且在低资源场景更大模型可能更难适配。

**关键词**：阿拉伯语语音命名实体识别, 端到端语音NER, 级联流水线（ASR+文本NER）, 低资源学习, 细粒度实体标注, 自监督语音预训练, 多语种弱监督迁移, CV-18

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02209v1) | [下载PDF](https://arxiv.org/pdf/2604.02209v1.pdf)

---

## [12. Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Language Model](https://arxiv.org/abs/2604.02194v1)

**作者**：Jaemin Kim, Jae O Lee, Sumyeong Ahn 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Retrieval-Augmented Language Models (RALMs) have demonstrated significant potential in knowledge-intensive tasks; however, they remain vulnerable to performance degradation when presented with irrelevant or noisy retrieved contexts. Existing approaches to enhance robustness typically operate via coarse-grained parameter updates at the layer or module level, often overlooking the inherent neuron-level sparsity of Large Language Models (LLMs). To address this limitation, we propose Neuro-RIT (Neuron-guided Robust Instruction Tuning), a novel framework that shifts the paradigm from dense adaptation to precision-driven neuron alignment. Our method explicitly disentangles neurons that are responsible for processing relevant versus irrelevant contexts using attribution-based neuron mining. Subsequently, we introduce a two-stage instruction tuning strategy that enforces a dual capability for noise robustness: achieving direct noise suppression by functionally deactivating neurons exclusive to irrelevant contexts, while simultaneously optimizing targeted layers for evidence distillation. Extensive experiments across diverse QA benchmarks demonstrate that Neuro-RIT consistently outperforms strong baselines and robustness-enhancing methods.

### 🤖 AI 总结

**一句话总结**：Neuro-RIT通过在神经元层面区分并抑制处理无关检索内容的神经元，同时强化证据蒸馏能力，从而提升RAG语言模型在噪声检索下的鲁棒性。

**研究动机**：现有提升RAG鲁棒性的方案多在层/模块级进行粗粒度更新，忽视了LLM神经元激活的稀疏性，导致对无关或噪声检索上下文仍易性能退化。

**核心方法**：先用基于归因(attribution)的神经元挖掘，将“处理相关证据”和“受无关上下文影响”的神经元显式解耦；再采用两阶段指令微调：一方面功能性“停用/抑制”仅在无关上下文中起作用的神经元以直接降噪，另一方面对目标层进行优化以提升证据提炼与利用。

**主要结论**：在多种QA基准上，Neuro-RIT在面对无关/噪声检索上下文时较强基线与既有鲁棒性方法表现更稳定且总体效果更优，验证了神经元级对齐与双阶段调优的有效性。

**关键词**：检索增强语言模型, 噪声检索鲁棒性, 神经元级对齐, 归因分析, 神经元挖掘, 神经元去激活, 指令微调, 两阶段训练, 证据蒸馏, 问答基准评测

**评分**：69

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

**一句话总结**：We propose EventHub, a novel framework for training deep-event stereo networks without ground truth annotations from costly active sensors, relying instead on standard color images. From these images,...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：事件相机立体视觉, 事件立体匹配, 无真值监督训练, 代理标注, 代理事件生成, 新视角合成, 数据蒸馏, RGB到事件域迁移, 立体深度估计, 泛化评测, 夜间场景鲁棒性

**评分**：80

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02331v1) | [下载PDF](https://arxiv.org/pdf/2604.02331v1.pdf)

---

## [14. Modulate-and-Map: Crossmodal Feature Mapping with Cross-View Modulation for 3D Anomaly Detection](https://arxiv.org/abs/2604.02328v1)

**作者**：Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

We present ModMap, a natively multiview and multimodal framework for 3D anomaly detection and segmentation. Unlike existing methods that process views independently, our method draws inspiration from the crossmodal feature mapping paradigm to learn to map features across both modalities and views, while explicitly modelling view-dependent relationships through feature-wise modulation. We introduce a cross-view training strategy that leverages all possible view combinations, enabling effective anomaly scoring through multiview ensembling and aggregation. To process high-resolution 3D data, we train and publicly release a foundational depth encoder tailored to industrial datasets. Experiments on SiM3D, a recent benchmark that introduces the first multiview and multimodal setup for 3D anomaly detection and segmentation, demonstrate that ModMap attains state-of-the-art performance by surpassing previous methods by wide margins.

### 🤖 AI 总结

**一句话总结**：We present ModMap, a natively multiview and multimodal framework for 3D anomaly detection and segmentation. Unlike existing methods that process views independently, our method draws inspiration from ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：三维异常检测, 异常分割, 多视角学习, 多模态融合, 跨模态特征映射, 跨视角调制, 特征级调制, 多视角集成, 异常评分聚合, 深度编码器, 工业视觉数据集

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02328v1) | [下载PDF](https://arxiv.org/pdf/2604.02328v1.pdf)

---

## [15. Steerable Visual Representations](https://arxiv.org/abs/2604.02327v1)

**作者**：Jona Ruthardt, Manu Gaur, Deva Ramanan 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Pretrained Vision Transformers (ViTs) such as DINOv2 and MAE provide generic image features that can be applied to a variety of downstream tasks such as retrieval, classification, and segmentation. However, such representations tend to focus on the most salient visual cues in the image, with no way to direct them toward less prominent concepts of interest. In contrast, Multimodal LLMs can be guided with textual prompts, but the resulting representations tend to be language-centric and lose their effectiveness for generic visual tasks. To address this, we introduce Steerable Visual Representations, a new class of visual representations, whose global and local features can be steered with natural language. While most vision-language models (e.g., CLIP) fuse text with visual features after encoding (late fusion), we inject text directly into the layers of the visual encoder (early fusion) via lightweight cross-attention. We introduce benchmarks for measuring representational steerability, and demonstrate that our steerable visual features can focus on any desired objects in an image while preserving the underlying representation quality. Our method also matches or outperforms dedicated approaches on anomaly detection and personalized object discrimination, exhibiting zero-shot generalization to out-of-distribution tasks.

### 🤖 AI 总结

**一句话总结**：提出一种可用自然语言“引导/转向”的视觉表征，通过在视觉编码器内部注入文本信息，使特征能关注用户指定概念且保持通用视觉任务性能。

**研究动机**：现有预训练ViT表征往往只捕捉图像中最显著线索，难以按需关注不显眼但重要的概念；而多模态LLM虽可用提示词引导，但得到的表征偏语言中心，通用视觉表征能力下降。

**核心方法**：提出Steerable Visual Representations：采用“早期融合”，在视觉编码器层内加入轻量级跨注意力将文本直接注入，从而同时对全局与局部特征进行语言可控的引导；并构建衡量“表征可引导性(steerability)”的新基准进行评测。

**主要结论**：实验表明该方法能在零样本条件下让特征聚焦任意指定目标，同时维持底层表示质量；在异常检测与个性化目标区分等任务上达到或超过专门方法，并能泛化到分布外任务。

**关键词**：可控视觉表征, 早期融合, 跨注意力, 自然语言引导, 提示驱动特征, 表征可控性评测, 零样本泛化, 异常检测, 个性化目标区分, 局部特征对齐, 视觉-语言表征

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02327v1) | [下载PDF](https://arxiv.org/pdf/2604.02327v1.pdf)

---

## [16. Beyond Referring Expressions: Scenario Comprehension Visual Grounding](https://arxiv.org/abs/2604.02323v1)

**作者**：Ruozhen He, Nisarg A. Shah, Qihua Dong 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Existing visual grounding benchmarks primarily evaluate alignment between image regions and literal referring expressions, where models can often succeed by matching a prominent named category. We explore a complementary and more challenging setting of scenario-based visual grounding, where the target must be inferred from roles, intentions, and relational context rather than explicit naming. We introduce Referring Scenario Comprehension (RSC), a benchmark designed for this setting. The queries in this benchmark are paragraph-length texts that describe object roles, user goals, and contextual cues, including deliberate references to distractor objects that often require deep understanding to resolve. Each instance is annotated with interpretable difficulty tags for uniqueness, clutter, size, overlap, and position which expose distinct failure modes and support fine-grained analysis. RSC contains approximately 31k training examples, 4k in-domain test examples, and a 3k out-of-distribution split with unseen object categories. We further propose ScenGround, a curriculum reasoning method serving as a reference point for this setting, combining supervised warm-starting with difficulty-aware reinforcement learning. Experiments show that scenario-based queries expose systematic failures in current models that standard benchmarks do not reveal, and that curriculum training improves performance on challenging slices and transfers to standard benchmarks.

### 🤖 AI 总结

**一句话总结**：论文提出面向“场景理解”的视觉指代新基准RSC与课程式训练方法ScenGround，要求模型根据角色/意图/关系上下文推断目标，从而暴露并缓解传统指代表达基准难以发现的系统性失败。

**研究动机**：现有视觉定位/指代基准多依赖字面类别匹配（如显著物体名称），模型可用浅层线索“投机取巧”而非真正理解情境。作者希望评测并推动模型在包含目标意图、角色关系、干扰物等更贴近真实任务的“场景叙述式查询”上的定位能力。

**核心方法**：构建Referring Scenario Comprehension（RSC）数据集：以段落级文本描述目标的角色、用户目标与上下文线索，并刻意加入干扰物；同时为每个样例标注可解释难度标签（唯一性、拥挤度、尺寸、重叠、位置）并提供域内与OOD（未见类别）划分。提出ScenGround训练范式：先监督预热（warm-start），再进行难度感知的课程式强化学习以提升困难切片表现与泛化。

**主要结论**：场景式查询能显著揭示当前视觉指代模型在深层理解与关系推断上的系统性短板，这是标准基准难以暴露的。采用难度驱动的课程训练可提升在困难样例与OOD设置下的表现，并且对传统视觉指代基准具有一定迁移增益。

**关键词**：视觉定位, 情境式查询, 角色意图推理, 关系推理, 长文本指代表达, 难度标签标注, 分布外泛化, 课程学习, 强化学习训练

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02323v1) | [下载PDF](https://arxiv.org/pdf/2604.02323v1.pdf)

---

## [17. Large-scale Codec Avatars: The Unreasonable Effectiveness of Large-scale Avatar Pretraining](https://arxiv.org/abs/2604.02320v1)

**作者**：Junxuan Li, Rawal Khirodkar, Chengan He 等 40 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-04-02

### 📄 论文摘要

High-quality 3D avatar modeling faces a critical trade-off between fidelity and generalization. On the one hand, multi-view studio data enables high-fidelity modeling of humans with precise control over expressions and poses, but it struggles to generalize to real-world data due to limited scale and the domain gap between the studio environment and the real world. On the other hand, recent large-scale avatar models trained on millions of in-the-wild samples show promise for generalization across a wide range of identities, yet the resulting avatars are often of low-quality due to inherent 3D ambiguities. To address this, we present Large-Scale Codec Avatars (LCA), a high-fidelity, full-body 3D avatar model that generalizes to world-scale populations in a feedforward manner, enabling efficient inference. Inspired by the success of large language models and vision foundation models, we present, for the first time, a pre/post-training paradigm for 3D avatar modeling at scale: we pretrain on 1M in-the-wild videos to learn broad priors over appearance and geometry, then post-train on high-quality curated data to enhance expressivity and fidelity. LCA generalizes across hair styles, clothing, and demographics while providing precise, fine-grained facial expressions and finger-level articulation control, with strong identity preservation. Notably, we observe emergent generalization to relightability and loose garment support to unconstrained inputs, and zero-shot robustness to stylized imagery, despite the absence of direct supervision.

### 🤖 AI 总结

**一句话总结**：LCA提出一种“海量野外视频预训练 + 高质量棚拍数据后训练”的范式，实现兼具高保真与强泛化的全身3D头像，并可前馈高效推理。

**研究动机**：现有方法在“棚拍多视角高质量但泛化弱”与“野外大规模泛化强但3D质量低”之间难以兼得，需要一种既能吸收大规模先验又能保证细节与可控性的训练策略。

**核心方法**：先在100万野外视频上进行预训练以学习外观与几何的广泛先验（覆盖发型、服装、人群分布等），再用高质量精标/棚拍数据进行后训练以提升面部表情、手指级关节与身份保持等精细控制与保真度，并保持前馈式生成以提升推理效率。

**主要结论**：该范式使模型在多样身份与外观上具备强泛化的同时获得高质量细节与精确控制；此外还出现了对重光照、宽松衣物与风格化输入的零样本鲁棒性等涌现能力，即便没有直接监督。

**关键词**：3D虚拟人建模, 全身头像重建, 大规模预训练, 预训练-后训练范式, 野外视频数据, 高保真重建, 前馈推理, 身份保持, 表情控制, 手指级关节控制, 可重光照, 宽松服装建模

**评分**：81

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02320v1) | [下载PDF](https://arxiv.org/pdf/2604.02320v1.pdf)

---

## [18. A Simple Baseline for Streaming Video Understanding](https://arxiv.org/abs/2604.02317v1)

**作者**：Yujiao Shen, Shulin Tian, Jingkang Yang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Recent streaming video understanding methods increasingly rely on complex memory mechanisms to handle long video streams. We challenge this trend with a simple finding: a sliding-window baseline that feeds only the most recent N frames to an off-the-shelf VLM already matches or surpasses published streaming models. We formalize this baseline as SimpleStream and evaluate it against 13 major offline and online video LLM baselines on OVO-Bench and StreamingBench. Despite its simplicity, SimpleStream delivers consistently strong performance. With only 4 recent frames, it reaches 67.7% average accuracy on OVO-Bench and 80.59% on StreamingBench. Controlled ablations further show that the value of longer context is backbone-dependent rather than uniformly increasing with model scale, and reveal a consistent perception-memory trade-off: adding more historical context can improve recall, but often weakens real-time perception. This suggests that stronger memory, retrieval, or compression modules should not be taken as evidence of progress unless they clearly outperform SimpleStream under the same protocol. We therefore argue that future streaming benchmarks should separate recent-scene perception from long-range memory, so that performance improvements from added complexity can be evaluated more clearly.

### 🤖 AI 总结

**一句话总结**：论文提出并验证了一个仅使用最近N帧的滑动窗口基线SimpleStream，在多个流式视频理解基准上即可匹敌或超过更复杂的记忆机制方法。

**研究动机**：现有流式视频理解研究常引入复杂记忆/检索/压缩模块以应对长视频流，但这些复杂性是否真正带来稳定收益缺乏与强基线的公平对比。作者希望用一个极简、可复现的设置检验“长上下文+复杂记忆”是否必然优于“只看最近帧”。

**核心方法**：SimpleStream将流式视频按时间滑动窗口截取，仅把最近N帧输入现成的视觉语言模型(VLM)进行理解与回答，不引入额外记忆网络。作者在OVO-Bench与StreamingBench上对比13种离线/在线视频LLM基线，并做上下文长度与骨干模型相关的消融分析。

**主要结论**：仅4帧的SimpleStream就取得OVO-Bench 67.7%与StreamingBench 80.59%的平均准确率，整体表现稳定且常超过已有流式方法；同时发现更长历史上下文的收益依赖于骨干而非随规模单调提升，并存在“感知-记忆”权衡（历史更长可能提升回忆但削弱实时感知）。因此作者建议：新增记忆/检索模块的进步应在同协议下显著超越SimpleStream，并且未来基准应区分近期场景感知与长程记忆能力。

**关键词**：滑动窗口, 视觉语言模型（VLM）, 长视频上下文, 记忆机制, 感知-记忆权衡, 上下文长度消融, Simple, Baseline

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02317v1) | [下载PDF](https://arxiv.org/pdf/2604.02317v1.pdf)

---

## [19. VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)

**作者**：Saman Motamed, William Harvey, Benjamin Klein 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Existing video object removal methods excel at inpainting content "behind" the object and correcting appearance-level artifacts such as shadows and reflections. However, when the removed object has more significant interactions, such as collisions with other objects, current models fail to correct them and produce implausible results. We present VOID, a video object removal framework designed to perform physically-plausible inpainting in these complex scenarios. To train the model, we generate a new paired dataset of counterfactual object removals using Kubric and HUMOTO, where removing an object requires altering downstream physical interactions. During inference, a vision-language model identifies regions of the scene affected by the removed object. These regions are then used to guide a video diffusion model that generates physically consistent counterfactual outcomes. Experiments on both synthetic and real data show that our approach better preserves consistent scene dynamics after object removal compared to prior video object removal methods. We hope this framework sheds light on how to make video editing models better simulators of the world through high-level causal reasoning.

### 🤖 AI 总结

**一句话总结**：VOID 提出一种面向“反事实”视频对象删除的框架，在移除物体后能同步修正其引发的碰撞等物理交互，从而生成更符合物理一致性的结果。

**研究动机**：现有视频去物体方法主要擅长补全被遮挡背景与处理阴影/反射等外观伪影，但当被删除物体与环境存在碰撞、推动等显著交互时，会留下不合理的后续运动与状态。作者希望让视频编辑模型具备更高层的因果推理能力，生成“如果该物体从未出现过”的合理动态演化。

**核心方法**：训练阶段：用 Kubric 与 HUMOTO 合成配对数据，构建“移除物体会改变后续物理交互”的反事实样本以监督学习。推理阶段：先用视觉-语言模型定位受被删物体影响的区域，再用这些区域作为引导条件驱动视频扩散模型生成物理一致的反事实视频结果。

**主要结论**：在合成与真实数据实验中，VOID 相比既有视频对象移除方法更能保持场景动力学的一致性与可信度，尤其在存在碰撞等复杂交互时表现更好；该工作表明引入高层因果/物理一致性约束可显著提升视频编辑的真实性。

**关键词**：视频目标移除, 物理一致性补全, 交互效应修正, 反事实视频生成, 因果推理, 视频扩散模型, 视觉-语言模型, 影响区域定位, 物理仿真数据生成, 合成-真实评测

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02296v1) | [下载PDF](https://arxiv.org/pdf/2604.02296v1.pdf)

---

## [20. Modular Energy Steering for Safe Text-to-Image Generation with Foundation Models](https://arxiv.org/abs/2604.02265v1)

**作者**：Yaoteng Tan, Zikui Cai, M. Salman Asif  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Controlling the behavior of text-to-image generative models is critical for safe and practical deployment. Existing safety approaches typically rely on model fine-tuning or curated datasets, which can degrade generation quality or limit scalability. We propose an inference-time steering framework that leverages gradient feedback from frozen pretrained foundation models to guide the generation process without modifying the underlying generator. Our key observation is that vision-language foundation models encode rich semantic representations that can be repurposed as off-the-shelf supervisory signals during generation. By injecting such feedback through clean latent estimates at each sampling step, our method formulates safety steering as an energy-based sampling problem. This design enables modular, training-free safety control that is compatible with both diffusion and flow-matching models and can generalize across diverse visual concepts. Experiments demonstrate state-of-the-art robustness against NSFW red-teaming benchmarks and effective multi-target steering, while preserving high generation quality on benign non-targeted prompts. Our framework provides a principled approach for utilizing foundation models as semantic energy estimators, enabling reliable and scalable safety control for text-to-image generation.

### 🤖 AI 总结

**一句话总结**：Controlling the behavior of text-to-image generative models is critical for safe and practical deployment. Existing safety approaches typically rely on model fine-tuning or curated datasets, which can...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：文本到图像安全, 推理时引导, 能量模型采样, 梯度反馈, 视觉语言模型, 冻结基础模型, Diffusion, 流匹配模型, 干净潜变量估计, 多目标引导, 训练免控制

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02265v1) | [下载PDF](https://arxiv.org/pdf/2604.02265v1.pdf)

---

## [21. SPAR: Single-Pass Any-Resolution ViT for Open-vocabulary Segmentation](https://arxiv.org/abs/2604.02252v1)

**作者**：Naomi Kombol, Ivan Martinović, Siniša Šegvić 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Foundational Vision Transformers (ViTs) have limited effectiveness in tasks requiring fine-grained spatial understanding, due to their fixed pre-training resolution and inherently coarse patch-level representations. These challenges are especially pronounced in dense prediction scenarios, such as open-vocabulary segmentation with ViT-based vision-language models, where high-resolution inputs are essential for accurate pixel-level reasoning. Existing approaches typically process large-resolution images using a sliding-window strategy at the pre-training resolution. While this improves accuracy through finer strides, it comes at a significant computational cost. We introduce SPAR: Single-Pass Any-Resolution ViT, a resolution-agnostic dense feature extractor designed for efficient high-resolution inference. We distill the spatial reasoning capabilities of a finely-strided, sliding-window teacher into a single-pass student using a feature regression loss, without requiring architectural changes or pixel-level supervision. Applied to open-vocabulary segmentation, SPAR improves single-pass baselines by up to 10.5 mIoU and even surpasses the teacher, demonstrating effectiveness in efficient, high-resolution reasoning. Code: https://github.com/naomikombol/SPAR

### 🤖 AI 总结

**一句话总结**：SPAR通过特征蒸馏把滑窗高分辨率ViT的细粒度空间能力压缩到一次前向的任意分辨率ViT中，在开放词汇分割上显著提升精度且更高效。

**研究动机**：基础ViT受限于固定预训练分辨率与粗粒度patch表征，做像素级密集预测（如开放词汇分割）时高分辨率推理很关键但滑窗策略计算成本极高。

**核心方法**：以“细步长滑窗教师”在高分辨率下产生的密集特征为目标，用特征回归损失将其空间推理能力蒸馏到“单次前向学生”中，实现分辨率无关的密集特征提取；全程不改网络结构，也不需要像素级标注监督。

**主要结论**：在开放词汇分割任务上，SPAR相对单次前向基线最高提升约10.5 mIoU，并且在某些设置下甚至超过滑窗教师，证明其能以更低计算开销实现有效的高分辨率像素级推理。

**关键词**：开放词汇分割, 任意分辨率 ViT, 单次前向推理, 高分辨率密集预测, 滑窗推理, 知识蒸馏, 特征回归损失, 空间推理, 视觉语言模型, 密集特征提取

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02252v1) | [下载PDF](https://arxiv.org/pdf/2604.02252v1.pdf)

---

## [22. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models](https://arxiv.org/abs/2604.02241v1)

**作者**：Qiyao Zhang, Shuhua Zheng, Jianli Sun 等 9 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-02

### 📄 论文摘要

Embodied visual tracking is crucial for Unmanned Aerial Vehicles (UAVs) executing complex real-world tasks. In dynamic urban scenarios with complex semantic requirements, Vision-Language-Action (VLA) models show great promise due to their cross-modal fusion and continuous action generation capabilities. To benchmark multimodal tracking in such environments, we construct a dedicated evaluation benchmark and a large-scale dataset encompassing over 890K frames, 176 tasks, and 85 diverse objects. Furthermore, to address temporal feature redundancy and the lack of spatial geometric priors in existing VLA models, we propose an improved VLA tracking model, UAV-Track VLA. Built upon the $π_{0.5}$ architecture, our model introduces a temporal compression net to efficiently capture inter-frame dynamics. Additionally, a parallel dual-branch decoder comprising a spatial-aware auxiliary grounding head and a flow matching action expert is designed to decouple cross-modal features and generate fine-grained continuous actions. Systematic experiments in the CARLA simulator validate the superior end-to-end performance of our method. Notably, in challenging long-distance pedestrian tracking tasks, UAV-Track VLA achieves a 61.76\% success rate and 269.65 average tracking frames, significantly outperforming existing baselines. Furthermore, it demonstrates robust zero-shot generalization in unseen environments and reduces single-step inference latency by 33.4\% (to 0.0571s) compared to the original $π_{0.5}$, enabling highly efficient, real-time UAV control. Data samples and demonstration videos are available at: https://github.com/Hub-Tian/UAV-Track\_VLA.

### 🤖 AI 总结

**一句话总结**：本文提出UAV-Track VLA及其大规模基准数据集，用视觉-语言-动作模型实现更高效、更鲁棒的端到端无人机目标跟踪。

**研究动机**：现有VLA在动态城市场景的无人机跟踪中存在时间特征冗余、缺少空间几何先验的问题，同时缺乏面向“语义要求复杂”的多模态跟踪评测基准。

**核心方法**：构建包含约89万帧、176类任务、85种对象的评测基准与数据集，并在π_{0.5}架构上加入时间压缩网络以提炼跨帧动态；设计并行双分支解码器（空间感知的辅助grounding头+基于flow matching的动作专家）以解耦跨模态特征并生成细粒度连续控制动作。

**主要结论**：在CARLA仿真中，UAV-Track VLA在长距离行人跟踪等任务上显著优于基线（成功率61.76%、平均跟踪269.65帧），具备未见环境的零样本泛化能力，并将单步推理延迟较原π_{0.5}降低33.4%至0.0571秒，支持更实时的无人机控制。

**关键词**：无人机视觉跟踪, 具身视觉跟踪, 视觉-语言-动作模型, 多模态跟踪基准, 大规模跟踪数据集, 时序特征压缩, 双分支解码器, 流匹配动作生成, 零样本泛化, 实时无人机控制

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02241v1) | [下载PDF](https://arxiv.org/pdf/2604.02241v1.pdf)

---

## [23. SCALE: Semantic- and Confidence-Aware Conditional Variational Autoencoder for Zero-shot Skeleton-based Action Recognition](https://arxiv.org/abs/2604.02222v1)

**作者**：Soroush Oraki, Feng Ding, Jie Liang  
**分类**：cs.CV  
**发布时间**：2026-04-02

### 📄 论文摘要

Zero-shot skeleton-based action recognition (ZSAR) aims to recognize action classes without any training skeletons from those classes, relying instead on auxiliary semantics from text. Existing approaches frequently depend on explicit skeleton-text alignment, which can be brittle when action names underspecify fine-grained dynamics and when unseen classes are semantically confusable. We propose SCALE, a lightweight and deterministic Semantic- and Confidence-Aware Listwise Energy-based framework that formulates ZSAR as class-conditional energy ranking. SCALE builds a text-conditioned Conditional Variational Autoencoder where frozen text representations parameterize both the latent prior and the decoder, enabling likelihood-based evaluation for unseen classes without generating samples at test time. To separate competing hypotheses, we introduce a semantic- and confidence-aware listwise energy loss that emphasizes semantically similar hard negatives and incorporates posterior uncertainty to adapt decision margins and reweight ambiguous training instances. Additionally, we utilize a latent prototype contrast objective to align posterior means with text-derived latent prototypes, improving semantic organization and class separability without direct feature matching. Experiments on NTU-60 and NTU-120 datasets show that SCALE consistently improves over prior VAE- and alignment-based baselines while remaining competitive with diffusion-based methods.

### 🤖 AI 总结

**一句话总结**：SCALE通过文本条件CVAE的似然评估与语义/置信度感知的listwise能量排序损失，实现更稳健的零样本骨架动作识别。

**研究动机**：现有ZSAR常依赖显式骨架-文本对齐，但当动作名称难以刻画细粒度动态、且未见类语义相近易混淆时，对齐会变得脆弱并导致误判。

**核心方法**：提出文本条件CVAE：冻结的文本表示同时参数化潜变量先验与解码器，从而可对每个候选类别计算条件似然并以“能量排序”决策、测试时无需采样；同时设计语义与置信度感知的listwise能量损失，强化相似难负样本并用后验不确定性自适应边界/重权重歧义样本，另加潜空间原型对比将后验均值对齐到文本导出的潜原型以提升可分性。

**主要结论**：在NTU-60与NTU-120上，SCALE相较VAE类与对齐类基线持续提升，并在保持轻量与确定性推理的同时，性能可与扩散模型方法竞争。

**关键词**：零样本骨架动作识别, 骨架序列建模, 文本语义条件, 条件变分自编码器, 类条件似然评估, 能量排序模型, 列表式能量损失, 不确定性感知学习, 语义硬负样本挖掘, 潜变量原型对比学习, 未见类泛化

**评分**：78

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

**一句话总结**：go-$m$HC 提出一种基于广义正交随机矩阵的精确双随机矩阵参数化，以更高效且更具表达力地学习残差流/层间的动态混合连接，并在合成任务与GPT式语言模型中验证有效。

**研究动机**：双随机矩阵可用于在多条残差流之间进行可学习的“混合”，但对 Birkhoff 多面体进行“精确且高效”的参数化一直很难：现有精确方法随流数 $d$ 呈阶乘级增长，而Kronecker分解虽高效但表达力受限。

**核心方法**：作者用广义正交随机（generalized orthostochastic）矩阵理论给出一个精确参数化，计算复杂度约为 $\mathcal{O}(d^3)$，并引入单一超参数 $s$ 在“高效边界”和“完全表达的Birkhoff多面体”之间连续插值；将其嵌入 Manifold-Constrained Hyper-Connections 框架形成 go-$m$HC，且可与Kronecker分解自然组合以在相近FLOPs下恢复表达力。

**主要结论**：谱分析显示 go-$m$HC 相比Kronecker基线能更充分覆盖Birkhoff多面体；在合成流混合任务上达到理论最小损失并最高加速约 $10\times$ 收敛，同时在约30M参数的GPT风格语言模型中验证了其表达力-效率-精确性兼顾，并提出将流数 $d$ 作为可扩展的新容量维度。

**关键词**：双随机矩阵, 精确参数化, 广义正交随机矩阵, 流混合, 残差流, 流形约束超连接（mHC）, 动态层连接, 谱分析, 计算复杂度 O(d^3, GPT 语言模型

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02309v1) | [下载PDF](https://arxiv.org/pdf/2604.02309v1.pdf)

---

## [25. Taming the Exponential: A Fast Softmax Surrogate for Integer-Native Edge Inference](https://arxiv.org/abs/2604.02292v1)

**作者**：Dimitrios Danopoulos, Enrico Lupi, Michael Kagan 等 4 位作者  
**分类**：cs.LG, cs.AR  
**发布时间**：2026-04-02

### 📄 论文摘要

Softmax can become a computational bottleneck in the Transformer model's Multi-Head Attention (MHA) block, particularly in small models under low-precision inference, where exponentiation and normalization incur significant overhead. As such, we suggest using Head-Calibrated Clipped-Linear Softmax (HCCS), a bounded, monotone surrogate to the exponential softmax function, which uses a clipped linear mapping of the max centered attention logits. This approximation produces a stable probability distribution, maintains the ordering of the original logits and has non-negative values. HCCS differs from previous softmax surrogates as it includes a set of lightweight calibration parameters that are optimized offline based on a representative dataset and calibrated for each individual attention head to preserve the statistical properties of the individual heads. We describe a hardware-motivated implementation of HCCS for high-throughput scenarios targeting the AMD Versal AI Engines. The current reference implementations from AMD for this platform rely upon either bfloat16 arithmetic or LUTs to perform the exponential operation, which might limit the throughput of the platform and fail to utilize the high-throughput integer vector processing units of the AI Engine. In contrast, HCCS provides a natural mapping to the AI Engines' int8 multiply accumulate (MAC) units. To the best of our knowledge, this is the first int8 optimized softmax surrogate for AMD AI engines that significantly exceeds the speed performance of other reference implementations while maintaining competitive task accuracy on small or heavily quantized MHA workloads after quantization-aware retraining.

### 🤖 AI 总结

**一句话总结**：论文提出HCCS（Head-Calibrated Clipped-Linear Softmax）作为softmax的int8友好近似，在边缘低精度Transformer注意力中显著加速并保持接近的任务精度。

**研究动机**：在小模型与低精度推理场景下，softmax中的指数运算与归一化会成为MHA的主要计算瓶颈，且现有实现常依赖bfloat16或LUT导致吞吐受限。作者希望用可映射到整数向量MAC单元的替代方案来充分利用AMD Versal AI Engines的高吞吐int8能力。

**核心方法**：HCCS用对“减去最大值”的attention logits做截断线性映射来近似exp-softmax，保证单调、有界、非负并保留logits排序，从而形成稳定的概率分布。其关键是为每个注意力头引入轻量校准参数，基于代表性数据离线优化以匹配各头统计特性，并给出面向AMD Versal AI Engines的int8实现与量化感知再训练流程。

**主要结论**：在AMD Versal AI Engines上，HCCS相比依赖bfloat16或LUT指数的参考实现获得显著更高的softmax吞吐/速度，同时在小模型或重度量化的MHA任务中经QAT后保持具有竞争力的准确率。作者声称这是首个面向该平台、显著超越参考实现性能的int8优化softmax替代方案。

**关键词**：多头注意力, 整数推理, 边缘推理, 低精度量化, 逐头校准, 裁剪线性映射, 量化感知训练, 高吞吐硬件实现

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02292v1) | [下载PDF](https://arxiv.org/pdf/2604.02292v1.pdf)

---

## [26. Model-Based Reinforcement Learning for Control under Time-Varying Dynamics](https://arxiv.org/abs/2604.02260v1)

**作者**：Klemens Iten, Bruce Lee, Chenhao Li 等 6 位作者  
**分类**：cs.LG, cs.RO  
**发布时间**：2026-04-02

### 📄 论文摘要

Learning-based control methods typically assume stationary system dynamics, an assumption often violated in real-world systems due to drift, wear, or changing operating conditions. We study reinforcement learning for control under time-varying dynamics. We consider a continual model-based reinforcement learning setting in which an agent repeatedly learns and controls a dynamical system whose transition dynamics evolve across episodes. We analyze the problem using Gaussian process dynamics models under frequentist variation-budget assumptions. Our analysis shows that persistent non-stationarity requires explicitly limiting the influence of outdated data to maintain calibrated uncertainty and meaningful dynamic regret guarantees. Motivated by these insights, we propose a practical optimistic model-based reinforcement learning algorithm with adaptive data buffer mechanisms and demonstrate improved performance on continuous control benchmarks with non-stationary dynamics.

### 🤖 AI 总结

**一句话总结**：本文研究在系统动力学随时间变化的情况下，如何用持续的模型式强化学习实现稳健控制，并提出通过限制旧数据影响来获得更可靠的不确定性与动态后悔界。

**研究动机**：现实控制系统常因磨损、漂移或工况变化而呈现非平稳动力学，使得假设动力学不变的学习控制方法容易失效或过度自信。作者希望在持续学习场景下，对这种时间变化建立可分析的理论保证与有效算法。

**核心方法**：采用高斯过程（GP）作为动力学模型，并在“频率学派的变化预算（variation budget）”假设下分析跨episode动力学漂移对不确定性校准与动态遗憾（dynamic regret）的影响。基于分析结论，提出一种乐观的模型式RL算法，配合自适应数据缓冲区/滑动窗口机制以降低过时数据的权重。

**主要结论**：理论分析表明，持续非平稳时若不显式削弱旧数据影响，将导致不确定性失真并破坏有意义的动态遗憾保证；采用自适应缓冲机制可维持校准不确定性并改善后悔界。实验在具有非平稳动力学的连续控制基准上验证了该方法优于常规做法的性能。

**关键词**：时变动力学, 非平稳强化学习, 持续学习控制, 模型式强化学习, 高斯过程动力学模型, 变化预算假设, 动态遗憾界, 不确定性校准, 乐观探索, 自适应数据缓冲, 连续控制基准

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02260v1) | [下载PDF](https://arxiv.org/pdf/2604.02260v1.pdf)

---

## [27. Smoothing the Landscape: Causal Structure Learning via Diffusion Denoising Objectives](https://arxiv.org/abs/2604.02250v1)

**作者**：Hao Zhu, Di Zhou, Donna Slonim  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-04-02

### 📄 论文摘要

Understanding causal dependencies in observational data is critical for informing decision-making. These relationships are often modeled as Bayesian Networks (BNs) and Directed Acyclic Graphs (DAGs). Existing methods, such as NOTEARS and DAG-GNN, often face issues with scalability and stability in high-dimensional data, especially when there is a feature-sample imbalance. Here, we show that the denoising score matching objective of diffusion models could smooth the gradients for faster, more stable convergence. We also propose an adaptive k-hop acyclicity constraint that improves runtime over existing solutions that require matrix inversion. We name this framework Denoising Diffusion Causal Discovery (DDCD). Unlike generative diffusion models, DDCD utilizes the reverse denoising process to infer a parameterized causal structure rather than to generate data. We demonstrate the competitive performance of DDCDs on synthetic benchmarking data. We also show that our methods are practically useful by conducting qualitative analyses on two real-world examples. Code is available at this url: https://github.com/haozhu233/ddcd.

### 🤖 AI 总结

**一句话总结**：Understanding causal dependencies in observational data is critical for informing decision-making. These relationships are often modeled as Bayesian Networks (BNs) and Directed Acyclic Graphs (DAGs). ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：因果结构学习, 贝叶斯网络, Diffusion, 去噪评分匹配, 反向去噪推断, 梯度平滑, 高维小样本, k-hop 无环约束, 可扩展性与稳定性, 合成基准评测

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02250v1) | [下载PDF](https://arxiv.org/pdf/2604.02250v1.pdf)

---

## [28. Universal Hypernetworks for Arbitrary Models](https://arxiv.org/abs/2604.02215v1)

**作者**：Xuanfeng Zhou  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Conventional hypernetworks are typically engineered around a specific base-model parameterization, so changing the target architecture often entails redesigning the hypernetwork and retraining it from scratch. We introduce the \emph{Universal Hypernetwork} (UHN), a fixed-architecture generator that predicts weights from deterministic parameter, architecture, and task descriptors. This descriptor-based formulation decouples the generator architecture from target-network parameterization, so one generator can instantiate heterogeneous models across the tested architecture and task families. Our empirical claims are threefold: (1) one fixed UHN remains competitive with direct training across vision, graph, text, and formula-regression benchmarks; (2) the same UHN supports both multi-model generalization within a family and multi-task learning across heterogeneous models; and (3) UHN enables stable recursive generation with up to three intermediate generated UHNs before the final base model. Our code is available at https://github.com/Xuanfeng-Zhou/UHN.

### 🤖 AI 总结

**一句话总结**：提出通用超网络UHN：用固定生成器通过“描述符”预测任意目标模型权重，从而在多架构多任务上复用同一个超网络并保持竞争性能。

**研究动机**：传统超网络往往与特定目标网络的参数化强耦合，一旦更换架构就需要重设计并从头训练，难以跨模型与跨任务复用。

**核心方法**：UHN采用基于描述符的权重生成：输入由确定性的参数描述、架构描述和任务描述组成，生成器架构固定且与目标网络参数化解耦，从而能实例化异构的视觉/图/文本/回归等模型；并探索递归生成（生成UHN再生成模型）以验证稳定性。

**主要结论**：单个固定UHN在多种基准上可与直接训练的模型性能相当，并同时支持同族模型泛化与跨异构模型的多任务学习；此外还能稳定进行最多三层中间UHN的递归生成。

**关键词**：权重生成, 描述符条件化, 架构描述符, 任务描述符, 参数描述符, 异构模型实例化, 多模型泛化, 多任务学习, 递归生成

**评分**：75

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02215v1) | [下载PDF](https://arxiv.org/pdf/2604.02215v1.pdf)

---

## [29. LEO: Graph Attention Network based Hybrid Multi Sensor Extended Object Fusion and Tracking for Autonomous Driving Applications](https://arxiv.org/abs/2604.02206v1)

**作者**：Mayank Mayank, Bharanidhar Duraisamy, Florian Geiss  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-02

### 📄 论文摘要

Accurate shape and trajectory estimation of dynamic objects is essential for reliable automated driving. Classical Bayesian extended-object models offer theoretical robustness and efficiency but depend on completeness of a-priori and update-likelihood functions, while deep learning methods bring adaptability at the cost of dense annotations and high compute. We bridge these strengths with LEO (Learned Extension of Objects), a spatio-temporal Graph Attention Network that fuses multi-modal production-grade sensor tracks to learn adaptive fusion weights, ensure temporal consistency, and represent multi-scale shapes. Using a task-specific parallelogram ground-truth formulation, LEO models complex geometries (e.g. articulated trucks and trailers) and generalizes across sensor types, configurations, object classes, and regions, remaining robust for challenging and long-range targets. Evaluations on the Mercedes-Benz DRIVE PILOT SAE L3 dataset demonstrate real-time computational efficiency suitable for production systems; additional validation on public datasets such as View of Delft (VoD) further confirms cross-dataset generalization.

### 🤖 AI 总结

**一句话总结**：Accurate shape and trajectory estimation of dynamic objects is essential for reliable automated driving. Classical Bayesian extended-object models offer theoretical robustness and efficiency but depen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：自动驾驶目标跟踪, 扩展目标融合, 多传感器轨迹融合, 时空图注意力网络, 图注意力网络（GAT）, 自适应融合权重, 时间一致性建模, 多尺度形状表示, 复杂几何建模, 平行四边形标注, 实时推理效率

**评分**：80

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02206v1) | [下载PDF](https://arxiv.org/pdf/2604.02206v1.pdf)

---

## [30. On the Role of Depth in the Expressivity of RNNs](https://arxiv.org/abs/2604.02201v1)

**作者**：Maude Lizaire, Michael Rizvi-Martel, Éric Dupuis 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-02

### 📄 论文摘要

The benefits of depth in feedforward neural networks are well known: composing multiple layers of linear transformations with nonlinear activations enables complex computations. While similar effects are expected in recurrent neural networks (RNNs), it remains unclear how depth interacts with recurrence to shape expressive power. Here, we formally show that depth increases RNNs' memory capacity efficiently with respect to the number of parameters, thus enhancing expressivity both by enabling more complex input transformations and improving the retention of past information. We broaden our analysis to 2RNNs, a generalization of RNNs with multiplicative interactions between inputs and hidden states. Unlike RNNs, which remain linear without nonlinear activations, 2RNNs perform polynomial transformations whose maximal degree grows with depth. We further show that multiplicative interactions cannot, in general, be replaced by layerwise nonlinearities. Finally, we validate these insights empirically on synthetic and real-world tasks.

### 🤖 AI 总结

**一句话总结**：论文从理论上证明：增加深度能以更高参数效率提升RNN的记忆容量与表达能力；对含乘性交互的2RNN而言，深度还能提升其可表示多项式变换的最高阶数，且乘性交互一般无法用逐层非线性完全替代。

**研究动机**：尽管前馈网络“深度提升表达力”已较清晰，但在RNN中深度与递归如何共同影响记忆与表达能力仍缺乏形式化理解，尤其是与乘性交互结构（2RNN）的差异。

**核心方法**：作者对不同深度的RNN与2RNN进行表达能力与记忆容量的形式化分析，比较参数效率下的记忆提升、以及2RNN可实现的多项式变换阶数随深度增长的规律，并论证乘性交互不可一般性地被层间非线性替代；最后通过合成与真实任务实验验证理论结论。

**主要结论**：深度能更高效（相对参数数量）地提升RNN的记忆容量，从而同时增强输入变换复杂度与历史信息保留能力；对2RNN，深度使其多项式表达的最大次数增长并带来更强表达力，而且乘性交互提供的能力通常无法用单纯加深并叠加非线性来等价替换，实验结果与理论一致。

**关键词**：表达能力, 记忆容量, 参数效率, 乘法交互, 多项式变换, 多项式次数增长, 非线性激活不可替代性, 序列建模, 合成任务评测, 真实世界任务实验

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.02201v1) | [下载PDF](https://arxiv.org/pdf/2604.02201v1.pdf)

---

