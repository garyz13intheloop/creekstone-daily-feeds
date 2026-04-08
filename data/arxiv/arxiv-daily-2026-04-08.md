# arXiv AI 论文日报 | 2026-04-08

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (8 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (9 篇)
- [cs.AI](#csAI) (6 篇)

---

## cs.AI

## [1. Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents](https://arxiv.org/abs/2604.06132v1)

**作者**：Bowen Ye, Rang Li, Qibin Yang 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Large language models are increasingly deployed as autonomous agents executing multi-step workflows in real-world software environments. However, existing agent benchmarks suffer from three critical limitations: (1) trajectory-opaque grading that checks only final outputs, (2) underspecified safety and robustness evaluation, and (3) narrow modality coverage and interaction paradigms. We introduce Claw-Eval, an end-to-end evaluation suite addressing all three gaps. It comprises 300 human-verified tasks spanning 9 categories across three groups (general service orchestration, multimodal perception and generation, and multi-turn professional dialogue). Every agent action is recorded through three independent evidence channels (execution traces, audit logs, and environment snapshots), enabling trajectory-aware grading over 2,159 fine-grained rubric items. The scoring protocol evaluates Completion, Safety, and Robustness, reporting Average Score, Pass@k, and Pass^k across three trials to distinguish genuine capability from lucky outcomes. Experiments on 14 frontier models reveal that: (1) trajectory-opaque evaluation is systematically unreliable, missing 44% of safety violations and 13% of robustness failures that our hybrid pipeline catches; (2) controlled error injection primarily degrades consistency rather than peak capability, with Pass^3 dropping up to 24% while Pass@3 remains stable; (3) multimodal performance varies sharply, with most models performing poorer on video than on document or image, and no single model dominating across all modalities. Beyond benchmarking, Claw-Eval highlights actionable directions for agent development, shedding light on what it takes to build agents that are not only capable but reliably deployable.

### 🤖 AI 总结

**一句话总结**：Claw-Eval 提供一个面向自主智能体的端到端评测套件，用轨迹可追溯证据对完成度、安全性与鲁棒性进行更可信的综合评分。

**研究动机**：现有智能体基准多只看最终结果、缺少系统的安全/鲁棒评估，并且覆盖的模态与交互范式较窄，导致评测容易失真、难以支撑真实部署。

**核心方法**：构建包含300个经人工核验任务的评测集，覆盖9类任务与三大场景，并通过执行轨迹、审计日志、环境快照三路证据记录每步动作，以2,159条细粒度rubric做轨迹感知打分；同时用三次试验与Average Score、Pass@k、Pass^k指标分别衡量能力上限与一致性，并加入受控错误注入检验鲁棒性。

**主要结论**：在14个前沿模型上的实验表明，仅看最终输出的“轨迹不透明”评测会系统性漏检问题（漏掉44%安全违规与13%鲁棒失败）；错误注入主要损伤一致性而非峰值能力（Pass^3最多降24%而Pass@3较稳定）；多模态上视频任务普遍更难且不存在单一模型全模态领先。

**关键词**：自主智能体评测, 端到端基准, 轨迹感知评分, 执行轨迹, 审计日志, 环境快照, 细粒度评分量表, 安全评估, 鲁棒性评估, 多模态任务, 多轮专业对话

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06132v1) | [下载PDF](https://arxiv.org/pdf/2604.06132v1.pdf)

---

## [2. ACE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments](https://arxiv.org/abs/2604.06111v1)

**作者**：Wang Yang, Chaoda Song, Xinpeng Li 等 10 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

Existing Agent benchmarks suffer from two critical limitations: high environment interaction overhead (up to 41\% of total evaluation time) and imbalanced task horizon and difficulty distributions that make aggregate scores unreliable. To address these issues, we propose ACE-Bench built around a unified grid-based planning task, where agents must fill hidden slots in a partially completed schedule subject to both local slot constraints and global constraints. Our benchmark offers fine-grained control through two orthogonal axes: Scalable Horizons, controlled by the number of hidden slots $H$, and Controllable Difficulty, governed by a decoy budget $B$ that determines the number of globally misleading decoy candidates. Crucially, all tool calls are resolved via static JSON files under a Lightweight Environment design, eliminating setup overhead and enabling fast, reproducible evaluation suitable for training-time validation. We first validate that H and B provide reliable control over task horizon and difficulty, and that ACE-Bench exhibits strong domain consistency and model discriminability. We then conduct comprehensive experiments across 13 models of diverse sizes and families over 6 domains, revealing significant cross-model performance variation and confirming that ACE-Bench provides interpretable and controllable evaluation of agent reasoning.

### 🤖 AI 总结

**一句话总结**：Existing Agent benchmarks suffer from two critical limitations: high environment interaction overhead (up to 41\% of total evaluation time) and imbalanced task horizon and difficulty distributions tha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：可控任务视界, 可控难度, 轻量环境, 网格规划任务, 部分可观测排程, 全局约束推理, 诱饵候选, 可复现实验, 训练时验证, 模型可区分性

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06111v1) | [下载PDF](https://arxiv.org/pdf/2604.06111v1.pdf)

---

## [3. Artificial Intelligence and the Structure of Mathematics](https://arxiv.org/abs/2604.06107v1)

**作者**：Maissam Barkeshli, Michael R. Douglas, Michael H. Freedman  
**分类**：cs.AI, math.HO, math.LO  
**发布时间**：2026-04-07

### 📄 论文摘要

Recent progress in artificial intelligence (AI) is unlocking transformative capabilities for mathematics. There is great hope that AI will help solve major open problems and autonomously discover new mathematical concepts. In this essay, we further consider how AI may open a grand perspective on mathematics by forging a new route, complementary to mathematical\textbf{ logic,} to understanding the global structure of formal \textbf{proof}\textbf{s}. We begin by providing a sketch of the formal structure of mathematics in terms of universal proof and structural hypergraphs and discuss questions this raises about the foundational structure of mathematics. We then outline the main ingredients and provide a set of criteria to be satisfied for AI models capable of automated mathematical discovery. As we send AI agents to traverse Platonic mathematical worlds, we expect they will teach us about the nature of mathematics: both as a whole, and the small ribbons conducive to human understanding. Perhaps they will shed light on the old question: "Is mathematics discovered or invented?" Can we grok the terrain of these \textbf{Platonic worlds}?

### 🤖 AI 总结

**一句话总结**：论文探讨AI如何通过分析形式化证明的全局结构（如证明网络/超图）来辅助乃至推动数学概念发现与开放问题求解，从而提供一条不同于传统数理逻辑的“理解数学整体结构”的新路径。

**研究动机**：尽管AI在数学上展现出强大潜力，但目前对“数学作为一个整体的结构”缺乏可操作的全局视角；作者希望AI能补充数理逻辑，从宏观层面理解与导航庞大的形式化证明空间。

**核心方法**：提出用“通用证明（universal proof）”与“结构性超图（structural hypergraphs）”来刻画形式数学的组织方式，并据此提出面向自动数学发现的AI系统应满足的关键要素与评估标准（如能在证明空间中探索、提出新概念并形成可验证的证明链）。

**主要结论**：作者认为AI代理有望在“柏拉图式数学世界”中进行系统探索，既帮助解决重大未解问题，也可能揭示哪些结构更利于人类理解，并推动关于“数学是被发现还是被发明”的哲学讨论。

**关键词**：形式化证明, 证明结构分析, 结构超图, 数学基础, 数学逻辑, 自动化定理证明, 柏拉图式数学世界, Artificial

**评分**：54

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06107v1) | [下载PDF](https://arxiv.org/pdf/2604.06107v1.pdf)

---

## [4. How LLMs Follow Instructions: Skillful Coordination, Not a Universal Mechanism](https://arxiv.org/abs/2604.06015v1)

**作者**：Elisabetta Rocchetti, Alfio Ferrara  
**分类**：cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Instruction tuning is commonly assumed to endow language models with a domain-general ability to follow instructions, yet the underlying mechanism remains poorly understood. Does instruction-following rely on a universal mechanism or compositional skill deployment? We investigate this through diagnostic probing across nine diverse tasks in three instruction-tuned models.   Our analysis provides converging evidence against a universal mechanism. First, general probes trained across all tasks consistently underperform task-specific specialists, indicating limited representational sharing. Second, cross-task transfer is weak and clustered by skill similarity. Third, causal ablation reveals sparse asymmetric dependencies rather than shared representations. Tasks also stratify by complexity across layers, with structural constraints emerging early and semantic tasks emerging late. Finally, temporal analysis shows constraint satisfaction operates as dynamic monitoring during generation rather than pre-generation planning.   These findings indicate that instruction-following is better characterized as skillful coordination of diverse linguistic capabilities rather than deployment of a single abstract constraint-checking process.

### 🤖 AI 总结

**一句话总结**：论文认为指令微调后的LLM并非依靠单一“通用指令遵循机制”，而是通过协调多种可分解的语言技能来完成不同指令任务。

**研究动机**：尽管指令微调被普遍视为赋予模型跨领域遵循指令的通用能力，但其内部机理不清楚；作者希望检验这是否源于统一机制，还是由多种技能按需组合实现。

**核心方法**：在三种指令微调模型上覆盖九类多样任务进行诊断探测：比较跨任务通用探针与任务专用探针、评估跨任务迁移与聚类相似性，并结合因果消融、层级表征与生成过程的时间动态分析来定位机制。

**主要结论**：跨任务通用探针显著弱于专用探针、迁移能力弱且按技能相似性成簇，消融呈现稀疏且不对称的依赖关系，均反对“共享的通用机制”；同时不同任务在网络层间呈复杂度分层（结构约束更早、语义更晚），并且约束满足更像生成时的动态监控而非生成前规划，支持“技能协同”解释。

**关键词**：指令微调, 指令跟随机制, 诊断探针, 任务特定表征, 跨任务迁移, 技能协调, 因果消融, 层级表征分析, 结构约束, 语义任务, 生成时监控, 约束满足

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06015v1) | [下载PDF](https://arxiv.org/pdf/2604.06015v1.pdf)

---

## [5. Epistemic Blinding: An Inference-Time Protocol for Auditing Prior Contamination in LLM-Assisted Analysis](https://arxiv.org/abs/2604.06013v1)

**作者**：Michael Cuccarese  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

This paper presents epistemic blinding in the context of an agentic system that uses large language models to reason across multiple biological datasets for drug target prioritization. During development, it became apparent that LLM outputs silently blend data-driven inference with memorized priors about named entities - and the blend is invisible: there is no way to determine, from a single output, how much came from the data on the page and how much came from the model's training memory. Epistemic blinding is a simple inference-time protocol that replaces entity identifiers with anonymous codes before prompting, then compares outputs against an unblinded control. The protocol does not make LLM reasoning deterministic, but it restores one critical axis of auditability: measuring how much of an output came from the supplied data versus the model's parametric knowledge. The complete target identification system is described - including LLM-guided evolutionary optimization of scoring functions and blinded agentic reasoning for target rationalization - with demonstration that both stages operate without access to entity identity. In oncology drug target prioritization across four cancer types, blinding changes 16% of top-20 predictions while preserving identical recovery of validated targets. The contamination problem is shown to generalize beyond biology: in S&P 500 equity screening, brand-recognition bias reshapes 30-40% of top-20 rankings across five random seeds. To lower the barrier to adoption, the protocol is released as an open-source tool and as a Claude Code skill that enables one-command epistemic blinding within agentic workflows. The claim is not that blinded analysis produces better results, but that without blinding, there is no way to know to what degree the agent is adhering to the analytical process the researcher designed.

### 🤖 AI 总结

**一句话总结**：提出“认知盲化（epistemic blinding）”推理时协议，通过匿名化实体名称并与未盲化输出对照，审计LLM分析中“训练记忆先验”对结论的污染程度。

**研究动机**：LLM在基于数据集进行推理时会将页面数据与对已知实体的记忆先验无声混合，单次输出无法判断结论究竟来自提供的数据还是模型记忆，从而削弱可审计性与研究流程的可信度。

**核心方法**：在提示前将实体标识符（如基因/公司名）替换为匿名代码进行“盲化”分析，再与保留原名的“未盲化”对照运行比较差异，以量化输出对实体身份先验的依赖；并在药物靶点优选系统中展示LLM引导的打分函数进化优化与盲化的agentic推理都可在不访问实体身份的情况下工作。

**主要结论**：在四种癌症的肿瘤靶点优选中，盲化会改变16%的Top-20预测但对已验证靶点的召回保持不变；在标普500选股中品牌识别偏差会重塑30–40%的Top-20排名，说明该污染问题可泛化，且盲化提供了关键的审计维度（而非声称一定提升效果）。

**关键词**：认知盲化, 推理时审计, 先验污染, 实体匿名化, 数据驱动推理, 参数记忆知识, 药物靶点优先级, 评分函数进化优化, 排名偏差评测, 品牌识别偏差, 多数据集推理

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06013v1) | [下载PDF](https://arxiv.org/pdf/2604.06013v1.pdf)

---

## [6. Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains](https://arxiv.org/abs/2604.05987v1)

**作者**：Eranga Bandara, Ross Gore, Sachin Shetty 等 18 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Retail supply chain operations in supermarket chains involve continuous, high-volume manual workflows spanning demand forecasting, procurement, supplier coordination, and inventory replenishment, processes that are repetitive, decision-intensive, and difficult to scale without significant human effort. Despite growing investment in data analytics, the decision-making and coordination layers of these workflows remain predominantly manual, reactive, and fragmented across outlets, distribution centers, and supplier networks. This paper introduces Flowr, a novel agentic AI framework for automating end-to-end retail supply chain workflows in large-scale supermarket operations. Flowr systematically decomposes manual supply chain operations into specialized AI agents, each responsible for a clearly defined cognitive role, enabling automation of processes previously dependent on continuous human coordination. To ensure task accuracy and adherence to responsible AI principles, the framework employs a consortium of fine-tuned, domain-specialized large language models coordinated by a central reasoning LLM. Central to the framework is a human-in-the-loop orchestration model in which supply chain managers supervise and intervene across workflow stages via a Model Context Protocol (MCP)-enabled interface, preserving accountability and organizational control. Evaluation demonstrates that Flowr significantly reduces manual coordination overhead, improves demand-supply alignment, and enables proactive exception handling at a scale unachievable through manual processes. The framework was validated in collaboration with a large-scale supermarket chain and is domain-independent, offering a generalizable blueprint for agentic AI-driven supply chain automation across large-scale enterprise settings.

### 🤖 AI 总结

**一句话总结**：Flowr 通过“多智能体+中心推理LLM+人类在环”的框架，将大型连锁超市供应链的端到端人工协同流程自动化，从而提升效率与供需匹配并强化异常处理能力。

**研究动机**：大型超市供应链涉及预测、采购、供应商协同与补货等高频、重复且决策密集的流程，长期依赖人工协调导致反应式、碎片化且难以规模化。现有数据分析虽普及，但关键的决策与跨节点协同层仍未被有效自动化。

**核心方法**：提出Flowr：把供应链操作拆解为多个具明确“认知角色”的专用AI智能体，并用中心推理LLM协调一组经过领域微调的LLM以提升准确性与合规性。通过支持MCP的界面引入人类在环编排机制，让管理者在各阶段监督与介入以保留问责与组织控制。

**主要结论**：实验评估显示Flowr显著降低人工协调开销、改善供需对齐，并实现更主动的异常处置与规模化运行能力。该框架已与大型超市链合作验证，且具有领域无关性，可作为企业级智能体自动化供应链的通用蓝图。

**关键词**：零售供应链自动化, 多智能体工作流, 需求预测, 采购决策, 供应商协同, 库存补货, 人机协同（HITL）, MCP 协议接口, 领域微调 LLM, 异常处理与预警, 需求-供给对齐

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2604.05987v1) | [下载PDF](https://arxiv.org/pdf/2604.05987v1.pdf)

---

## cs.CL

## [7. Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework](https://arxiv.org/abs/2604.06170v1)

**作者**：Komal Kumar, Aman Chadha, Salman Khan 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

The rapid growth of scientific literature has made it increasingly difficult for researchers to efficiently discover, evaluate, and synthesize relevant work. Recent advances in multi-agent large language models (LLMs) have demonstrated strong potential for understanding user intent and are being trained to utilize various tools. In this paper, we introduce Paper Circle, a multi-agent research discovery and analysis system designed to reduce the effort required to find, assess, organize, and understand academic literature. The system comprises two complementary pipelines: (1) a Discovery Pipeline that integrates offline and online retrieval from multiple sources, multi-criteria scoring, diversity-aware ranking, and structured outputs; and (2) an Analysis Pipeline that transforms individual papers into structured knowledge graphs with typed nodes such as concepts, methods, experiments, and figures, enabling graph-aware question answering and coverage verification. Both pipelines are implemented within a coder LLM-based multi-agent orchestration framework and produce fully reproducible, synchronized outputs including JSON, CSV, BibTeX, Markdown, and HTML at each agent step. This paper describes the system architecture, agent roles, retrieval and scoring methods, knowledge graph schema, and evaluation interfaces that together form the Paper Circle research workflow. We benchmark Paper Circle on both paper retrieval and paper review generation, reporting hit rate, MRR, and Recall at K. Results show consistent improvements with stronger agent models. We have publicly released the website at https://papercircle.vercel.app/ and the code at https://github.com/MAXNORM8650/papercircle.

### 🤖 AI 总结

**一句话总结**：Paper Circle 是一个开源的多智能体科研发现与论文分析框架，通过“检索发现+结构化知识图谱分析”两条流水线来提升找文献与写综述的效率与可复现性。

**研究动机**：科学文献增长过快导致研究者难以高效发现、评估与综合相关工作；作者希望利用多智能体LLM的意图理解与工具调用能力，降低检索、筛选、组织和理解论文的成本。

**核心方法**：系统包含两条互补流水线：Discovery Pipeline 融合多源离线/在线检索、多指标评分、兼顾多样性的排序与结构化输出；Analysis Pipeline 将单篇论文解析为带类型节点（概念、方法、实验、图表等）的知识图谱，用于图谱感知问答与覆盖性核查，并在多智能体编排下输出可复现的 JSON/CSV/BibTeX/Markdown/HTML 过程产物。

**主要结论**：在论文检索与论文评述生成基准上，Paper Circle 以 hit rate、MRR、Recall@K 等指标评测显示：更强的代理模型带来稳定性能提升；系统代码与网站已开源发布以支持复现与使用。

**关键词**：多智能体编排, 文献检索, 多指标评分, 多样性排序, 结构化输出, 论文知识图谱, 图谱问答, 覆盖度验证, 检索评测指标

**评分**：62

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06170v1) | [下载PDF](https://arxiv.org/pdf/2604.06170v1.pdf)

---

## [8. Exclusive Unlearning](https://arxiv.org/abs/2604.06154v1)

**作者**：Mutsumi Sasaki, Kouta Nakayama, Yusuke Miyao 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

When introducing Large Language Models (LLMs) into industrial applications, such as healthcare and education, the risk of generating harmful content becomes a significant challenge. While existing machine unlearning methods can erase specific harmful knowledge and expressions, diverse harmful content makes comprehensive removal difficult. In this study, instead of individually listing targets for forgetting, we propose Exclusive Unlearning (EU), which aims for broad harm removal by extensively forgetting everything except for the knowledge and expressions we wish to retain. We demonstrate that through Exclusive Unlearning, it is possible to obtain a model that ensures safety against a wide range of inputs, including jailbreaks, while maintaining the ability to respond to diverse instructions related to specific domains such as medicine and mathematics.

### 🤖 AI 总结

**一句话总结**：提出“独占式遗忘（Exclusive Unlearning）”，通过“只保留指定知识、遗忘其余内容”来实现更广谱的有害内容清除，并在保持特定领域能力的同时增强对越狱等攻击的安全性。

**研究动机**：工业场景中LLM容易生成多样化的有害内容，而逐条列举并“定点删除”有害知识的传统遗忘方法难以覆盖长尾与变体（包括jailbreak）。因此需要一种不依赖枚举有害目标、但能实现广泛安全约束的遗忘思路。

**核心方法**：将遗忘目标从“删除某些坏知识”反转为“除保留集合外全部遗忘”：训练模型强化对特定保留域（如医学、数学）的知识与表达，同时系统性抑制/忘却其余内容与潜在有害表达，从而形成更安全的输出分布。

**主要结论**：实验证明独占式遗忘可在广泛输入（含越狱提示）下提升安全性，同时仍能对保留领域的多样指令保持可用的响应能力，实现“更强安全+特定能力保留”的折中。

**关键词**：模型遗忘, LLM安全对齐, 有害内容抑制, 越狱防护, 保留知识子集, 指令跟随保持, 医疗问答, 数学推理

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06154v1) | [下载PDF](https://arxiv.org/pdf/2604.06154v1.pdf)

---

## [9. Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives](https://arxiv.org/abs/2604.06091v1)

**作者**：Changgeon Ko, Jisu Shin, Hoyun Song 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.MA  
**发布时间**：2026-04-07

### 📄 论文摘要

Large language model (LLM) agents are increasingly acting as human delegates in multi-agent environments, where a representative agent integrates diverse peer perspectives to make a final decision. Drawing inspiration from social psychology, we investigate how the reliability of this representative agent is undermined by the social context of its network. We define four key phenomena-social conformity, perceived expertise, dominant speaker effect, and rhetorical persuasion-and systematically manipulate the number of adversaries, relative intelligence, argument length, and argumentative styles. Our experiments demonstrate that the representative agent's accuracy consistently declines as social pressure increases: larger adversarial groups, more capable peers, and longer arguments all lead to significant performance degradation. Furthermore, rhetorical strategies emphasizing credibility or logic can further sway the agent's judgment, depending on the context. These findings reveal that multi-agent systems are sensitive not only to individual reasoning but also to the social dynamics of their configuration, highlighting critical vulnerabilities in AI delegates that mirror the psychological biases observed in human group decision-making.

### 🤖 AI 总结

**一句话总结**：论文指出：在多智能体LLM集体决策中，代表智能体会因“社会压力/群体动态”而系统性偏离客观判断，导致准确率显著下降。

**研究动机**：随着LLM代理在多智能体环境中充当“人类代表/决策整合者”，其决策可靠性可能像人类群体一样受从众、权威与话术影响；作者希望量化这些社会心理机制对LLM集体决策的脆弱性。

**核心方法**：基于社会心理学构建四类效应（社会从众、感知专家性、强势发言者效应、修辞说服），并在多代理设置中系统操控对抗者数量、同伴相对能力、论证长度与论证风格（如强调可信度或逻辑）来测试代表代理的决策准确性变化。

**主要结论**：实验表明社会压力越强代表代理越不准确：更多对抗者、更“聪明”的同伴、更长的论证都会显著拉低表现；此外，强调可信度或逻辑的修辞策略会在不同情境下进一步左右其判断，揭示多智能体系统存在类似人类群体偏差的关键安全/可靠性漏洞。

**关键词**：多智能体 LLM, 代表智能体, 群体决策, 感知专家性, 主导发言效应, 修辞说服, 论证长度, 相对智能水平

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06091v1) | [下载PDF](https://arxiv.org/pdf/2604.06091v1.pdf)

---

## [10. LAG-XAI: A Lie-Inspired Affine Geometric Framework for Interpretable Paraphrasing in Transformer Latent Spaces](https://arxiv.org/abs/2604.06086v1)

**作者**：Olexander Mazurets, Olexander Barmak, Leonid Bedratyuk 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Modern Transformer-based language models achieve strong performance in natural language processing tasks, yet their latent semantic spaces remain largely uninterpretable black boxes. This paper introduces LAG-XAI (Lie Affine Geometry for Explainable AI), a novel geometric framework that models paraphrasing not as discrete word substitutions, but as a structured affine transformation within the embedding space. By conceptualizing paraphrasing as a continuous geometric flow on a semantic manifold, we propose a computationally efficient mean-field approximation, inspired by local Lie group actions. This allows us to decompose paraphrase transitions into geometrically interpretable components: rotation, deformation, and translation. Experiments on the noisy PIT-2015 Twitter corpus, encoded with Sentence-BERT, reveal a "linear transparency" phenomenon. The proposed affine operator achieves an AUC of 0.7713. By normalizing against random chance (AUC 0.5), the model captures approximately 80% of the non-linear baseline's effective classification capacity (AUC 0.8405), offering explicit parametric interpretability in exchange for a marginal drop in absolute accuracy. The model identifies fundamental geometric invariants, including a stable matrix reconfiguration angle (~27.84°) and near-zero deformation, indicating local isometry. Cross-domain generalization is confirmed via direct cross-corpus validation on an independent TURL dataset. Furthermore, the practical utility of LAG-XAI is demonstrated in LLM hallucination detection: using a "cheap geometric check," the model automatically detected 95.3% of factual distortions on the HaluEval dataset by registering deviations beyond the permissible semantic corridor. This approach provides a mathematically grounded, resource-efficient path toward the mechanistic interpretability of Transformers.

### 🤖 AI 总结

**一句话总结**：LAG-XAI将“释义”建模为Transformer嵌入空间中的可解释仿射几何流（旋转/形变/平移），在较小精度损失下获得可参数化解释并可用于幻觉检测。

**研究动机**：尽管Transformer模型效果强，但其潜在语义空间难以解释，释义等语义变化通常被视为离散替换而缺乏机制层面的可解释性与可验证性。

**核心方法**：提出受局部李群作用启发的均值场近似，把释义转移表示为嵌入空间上的仿射算子，并将其分解为旋转、形变与平移等几何分量；在Sentence-BERT编码的语料上训练/验证，并用几何偏离作为“廉价检查”检测LLM事实扭曲。

**主要结论**：在PIT-2015上仿射模型AUC=0.7713，约保留非线性基线（AUC=0.8405）有效能力的80%且提供显式可解释参数；发现稳定旋转角约27.84°且形变近零（局部近等距），跨语料（TURL）泛化成立，并在HaluEval上以几何走廊偏离检测到95.3%的事实失真。

**关键词**：可解释性语义嵌入, 释义检测, 仿射变换, 几何流, 语义流形, 均值场近似, 旋转-形变-平移分解, 局部等距不变量, 跨语料泛化, LLM 幻觉检测

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06086v1) | [下载PDF](https://arxiv.org/pdf/2604.06086v1.pdf)

---

## [11. Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles](https://arxiv.org/abs/2604.06071v1)

**作者**：Ben Wigler, Maria Tsfasman, Tiffany Matej Hrkalovic  
**分类**：cs.CL, cs.AI, cs.HC  
**发布时间**：2026-04-07

### 📄 论文摘要

Personality traits are richly encoded in natural language, and large language models (LLMs) trained on human text can simulate personality when conditioned on persona descriptions. However, existing evaluations rely predominantly on questionnaire self-report by the conditioned model, are limited in architectural diversity, and rarely use real human psychometric data. Without addressing these limitations, it remains unclear whether personality conditioning produces psychometrically informative representations of individual differences or merely superficial alignment with trait descriptors. To test how robustly LLMs can encode personality into extended text, we condition LLMs on real psychometric profiles from 290 participants to generate first-person life story narratives, and then task independent LLMs to recover personality scores from those narratives alone. We show that personality scores can be recovered from the generated narratives at levels approaching human test-retest reliability (mean r = 0.750, 85% of the human ceiling), and that recovery is robust across 10 LLM narrative generators and 3 LLM personality scorers spanning 6 providers. Decomposing systematic biases reveals that scoring models achieve their accuracy while counteracting alignment-induced defaults. Content analysis of the generated narratives shows that personality conditioning produces behaviourally differentiated text: nine of ten coded features correlate significantly with the same features in participants' real conversations, and personality-driven emotional reactivity patterns in narratives replicate in real conversational data. These findings provide evidence that the personality-language relationship captured during pretraining supports robust encoding and decoding of individual differences, including characteristic emotional variability patterns that replicate in real human behaviour.

### 🤖 AI 总结

**一句话总结**：Personality traits are richly encoded in natural language, and large language models (LLMs) trained on human text can simulate personality when conditioned on persona descriptions. However, existing e...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：人格特质编码, 人格条件生成, 心理测量画像, 人生故事叙事生成, 回环评测, 人格分数反推, 跨模型鲁棒性, 内容特征对齐, 情绪反应性模式

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06071v1) | [下载PDF](https://arxiv.org/pdf/2604.06071v1.pdf)

---

## [12. From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection](https://arxiv.org/abs/2604.06066v1)

**作者**：Hongxu Zhou  
**分类**：cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

Intrinsic self-correction in Large Language Models (LLMs) frequently fails in open-ended reasoning tasks due to ``hallucination snowballing,'' a phenomenon in which models recursively justify early errors during free-text reflection. While structured feedback can mitigate this issue, existing approaches often rely on externally trained critics or symbolic tools, reducing agent autonomy. This study investigates whether enforcing structured reflection purely through Outlines-based constrained decoding can disrupt error propagation without additional training. Evaluating an 8-billion-parameter model (Qwen3-8B), we show that simply imposing structural constraints does not improve self-correction performance. Instead, it triggers a new failure mode termed ``structure snowballing.'' We find that the cognitive load required to satisfy strict formatting rules pushes the model into formatting traps. This observation helps explain why the agent achieves near-perfect superficial syntactic alignment yet fails to detect or resolve deeper semantic errors. These findings expose an ``alignment tax'' inherent to constrained decoding, highlighting a tension between structural granularity and internal model capacity in autonomous workflows. Code and raw logs are available in the GitHub repository: https://github.com/hongxuzhou/agentic_llm_structured_self_critique.

### 🤖 AI 总结

**一句话总结**：论文发现：仅靠Outlines式受约束解码强制结构化反思并不能提升LLM自我纠错，反而会引发“结构雪崩”导致语义错误被持续放大。

**研究动机**：LLM在开放式反思中常出现“幻觉雪崩”，早期错误会被递归自洽地论证；现有缓解方法多依赖外部critic或符号工具，削弱了自主性，因此作者探究能否仅用解码层面的结构约束来抑制错误传播。

**核心方法**：在Qwen3-8B上使用基于Outlines的constrained decoding强制模型按严格格式进行反思/自检，不引入额外训练或外部评估器，并对比其自我纠错表现与失败模式。

**主要结论**：结构约束未带来更好的自我纠错，反而因满足格式规则的“认知负载”使模型陷入格式陷阱，产生“结构雪崩”：表层语法对齐几乎完美但深层语义错误难以被发现与修复，揭示了受约束解码存在内在的“对齐税”。

**关键词**：反思推理, 幻觉滚雪球, 结构化反思, 约束解码, 结构滚雪球, 格式陷阱, 语法对齐, 语义错误检测

**评分**：57

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06066v1) | [下载PDF](https://arxiv.org/pdf/2604.06066v1.pdf)

---

## [13. A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models](https://arxiv.org/abs/2604.06028v1)

**作者**：Maria Mahbub, Gregory M. Dams, Josh Arnold 等 12 位作者  
**分类**：cs.CL, cs.AI, cs.IR  
**发布时间**：2026-04-07

### 📄 论文摘要

Large language models (LLMs) show promise for extracting clinically meaningful information from unstructured health records, yet their translation into real-world settings is constrained by the lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily on annotation-intensive reference standards or incomplete structured data, limiting feasibility at population scale. We propose a multi-stage validation framework for LLM-based clinical information extraction that enables rigorous assessment under weak supervision. The framework integrates prompt calibration, rule-based plausibility filtering, semantic grounding assessment, targeted confirmatory evaluation using an independent higher-capacity judge LLM, selective expert review, and external predictive validity analysis to quantify uncertainty and characterize error modes without exhaustive manual annotation. We applied this framework to extraction of substance use disorder (SUD) diagnoses across 11 substance categories from 919,783 clinical notes. Rule-based filtering and semantic grounding removed 14.59% of LLM-positive extractions that were unsupported, irrelevant, or structurally implausible. For high-uncertainty cases, the judge LLM's assessments showed substantial agreement with subject matter expert review (Gwet's AC1=0.80). Using judge-evaluated outputs as references, the primary LLM achieved an F1 score of 0.80 under relaxed matching criteria. LLM-extracted SUD diagnoses also predicted subsequent engagement in SUD specialty care more accurately than structured-data baselines (AUC=0.80). These findings demonstrate that scalable, trustworthy deployment of LLM-based clinical information extraction is feasible without annotation-intensive evaluation.

### 🤖 AI 总结

**一句话总结**：论文提出一种多阶段弱监督验证框架，用于在无需大规模人工标注的情况下，对LLM从海量临床文本中抽取诊断信息进行可扩展且可信的评估与部署。

**研究动机**：LLM可从非结构化病历中提取临床关键信息，但传统评估依赖高成本人工金标准或不完整结构化数据，难以在人群规模上实现可靠验证与风险量化。

**核心方法**：框架依次结合提示校准、规则/结构合理性过滤、语义支撑（grounding）检查、对高不确定样本用更强的“裁判LLM”做确认性评估、少量专家复核，以及用外部预测效度（如下游就医行为）检验抽取结果的有效性。

**主要结论**：在近92万条临床笔记的SUD诊断抽取任务上，规则过滤与语义校验剔除约14.59%的不支持/不相关结果；裁判LLM与专家一致性较高（AC1=0.80），主LLM在其参照下F1达0.80，且抽取的诊断对后续SUD专科就诊预测优于结构化基线（AUC=0.80），表明无需密集标注也可实现可扩展的可信验证。

**关键词**：临床信息抽取, 多阶段验证框架, 弱监督评测, 提示校准, 规则可置信性过滤, 语义溯源评估, 选择性专家复核, 不确定性量化, 外部预测效度分析

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06028v1) | [下载PDF](https://arxiv.org/pdf/2604.06028v1.pdf)

---

## [14. The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models](https://arxiv.org/abs/2604.05995v1)

**作者**：Xiaojie Gu, Ziying Huang, Weicong Hong 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-07

### 📄 论文摘要

Large Language Models (LLMs) internalize vast world knowledge as parametric memory, yet inevitably inherit the staleness and errors of their source corpora. Consequently, ensuring the reliability and malleability of these internal representations is imperative for trustworthy real-world deployment. Knowledge editing offers a pivotal paradigm for surgically modifying memory without retraining. However, while recent editors demonstrate high success rates on standard benchmarks, it remains questionable whether current evaluation frameworks that rely on assessing output under specific prompting conditions can reliably authenticate genuine memory modification. In this work, we introduce a simple diagnostic framework that subjects models to discriminative self-assessment under in-context learning (ICL) settings that better reflect real-world application environments, specifically designed to scrutinize the subtle behavioral nuances induced by memory modifications. This probing reveals a pervasive phenomenon of Surface Compliance, where editors achieve high benchmark scores by merely mimicking target outputs without structurally overwriting internal beliefs. Moreover, we find that recursive modifications accumulate representational residues, triggering cognitive instability and permanently diminishing the reversibility of the model's memory state. These insights underscore the risks of current editing paradigms and highlight the pivotal role of robust memory modification in building trustworthy, long-term sustainable LLM systems. Code is available at https://github.com/XiaojieGu/SA-MCQ.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) internalize vast world knowledge as parametric memory, yet inevitably inherit the staleness and errors of their source corpora. Consequently, ensuring the reliability and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：知识编辑, 参数化记忆, 编辑评测框架, ICL 自评诊断, 判别式自评, 表层服从, 信念覆盖失败, 递归编辑, 表征残留, 记忆可逆性退化, 认知不稳定性

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2604.05995v1) | [下载PDF](https://arxiv.org/pdf/2604.05995v1.pdf)

---

## cs.CV

## [15. DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models](https://arxiv.org/abs/2604.06161v1)

**作者**：Zhengming Yu, Li Ma, Mingming He 等 14 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-04-07

### 📄 论文摘要

Most digital videos are stored in 8-bit low dynamic range (LDR) formats, where much of the original high dynamic range (HDR) scene radiance is lost due to saturation and quantization. This loss of highlight and shadow detail precludes mapping accurate luminance to HDR displays and limits meaningful re-exposure in post-production workflows. Although techniques have been proposed to convert LDR images to HDR through dynamic range expansion, they struggle to restore realistic detail in the over- and underexposed regions. To address this, we present DiffHDR, a framework that formulates LDR-to-HDR conversion as a generative radiance inpainting task within the latent space of a video diffusion model. By operating in Log-Gamma color space, DiffHDR leverages spatio-temporal generative priors from a pretrained video diffusion model to synthesize plausible HDR radiance in over- and underexposed regions while recovering the continuous scene radiance of the quantized pixels. Our framework further enables controllable LDR-to-HDR video conversion guided by text prompts or reference images. To address the scarcity of paired HDR video data, we develop a pipeline that synthesizes high-quality HDR video training data from static HDRI maps. Extensive experiments demonstrate that DiffHDR significantly outperforms state-of-the-art approaches in radiance fidelity and temporal stability, producing realistic HDR videos with considerable latitude for re-exposure.

### 🤖 AI 总结

**一句话总结**：DiffHDR 将LDR视频转HDR建模为视频扩散模型潜空间中的“辐射度修复/补全”生成任务，以合成过曝与欠曝区域的合理HDR细节并支持可控重曝光。

**研究动机**：常见8-bit LDR视频因饱和与量化丢失高光/暗部细节，导致HDR显示映射不准且后期重曝光空间很小；现有动态范围扩展方法难以在过曝/欠曝区域恢复真实细节与时序一致性。

**核心方法**：在Log-Gamma色彩空间中，利用预训练视频扩散模型的时空生成先验，在潜空间对过曝/欠曝与量化像素进行辐射度“生成式修复”，并可用文本提示或参考图实现可控转换；同时提出从静态HDRI贴图合成高质量HDR视频的数据管线以缓解成对HDR视频数据稀缺。

**主要结论**：实验表明DiffHDR在辐射度保真度与时间稳定性上显著优于现有方法，能生成更真实的HDR视频并提供更大的后期重曝光余量。

**关键词**：HDR视频重建, 视频扩散模型, 潜空间生成修复, 辐射度补全, 时空生成先验, 可控生成, 文本提示引导, 参考图像引导, HDR训练数据合成, 时间一致性

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06161v1) | [下载PDF](https://arxiv.org/pdf/2604.06161v1.pdf)

---

## [16. The Character Error Vector: Decomposable errors for page-level OCR evaluation](https://arxiv.org/abs/2604.06160v1)

**作者**：Jonathan Bourne, Mwiza Simbeye, Joseph Nockels  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-07

### 📄 论文摘要

The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often not the case. Under page-parsing errors, CER becomes undefined, limiting its use as a metric and making evaluating page-level OCR challenging, particularly when using data that do not share a labelling schema. We introduce the Character Error Vector (CEV), a bag-of-characters evaluator for OCR. The CEV can be decomposed into parsing and OCR, and interaction error components. This decomposability allows practitioners to focus on the part of the Document Understanding pipeline that will have the greatest impact on overall text extraction quality. The CEV can be implemented using a variety of methods, of which we demonstrate SpACER (Spatially Aware Character Error Rate) and a Character distribution method using the Jensen-Shannon Distance. We validate the CEV's performance against other metrics: first, the relationship with CER; then, parse quality; and finally, as a direct measure of page-level OCR quality. The validation process shows that the CEV is a valuable bridge between parsing metrics and local metrics like CER. We analyse a dataset of archival newspapers made of degraded images with complex layouts and find that state-of-the-art end-to-end models are outperformed by more traditional pipeline approaches. Whilst the CEV requires character-level positioning for optimal triage, thresholding on easily available values can predict the main error source with an F1 of 0.91. We provide the CEV as part of a Python library to support Document understanding research.

### 🤖 AI 总结

**一句话总结**：The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often not t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：字符错误向量（CEV）, 字符错误率（CER）, 页面级OCR评测, 版面解析错误, 可分解误差分析, 字符级位置对齐, 端到端OCR模型, 传统OCR流水线

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06160v1) | [下载PDF](https://arxiv.org/pdf/2604.06160v1.pdf)

---

## [17. MMEmb-R1: Reasoning-Enhanced Multimodal Embedding with Pair-Aware Selection and Adaptive Control](https://arxiv.org/abs/2604.06156v1)

**作者**：Yuchi Wang, Haiyang Yu, Weikang Bian 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

MLLMs have been successfully applied to multimodal embedding tasks, yet their generative reasoning capabilities remain underutilized. Directly incorporating chain-of-thought reasoning into embedding learning introduces two fundamental challenges. First, structural misalignment between instance-level reasoning and pairwise contrastive supervision may lead to shortcut behavior, where the model merely learns the superficial format of reasoning. Second, reasoning is not universally beneficial for embedding tasks. Enforcing reasoning for all inputs may introduce unnecessary computation and latency, and can even obscure salient semantic signals for simple cases. To address these issues, we propose MMEmb-R1, an adaptive reasoning-based multimodal embedding framework. We formulate reasoning as a latent variable and introduce pair-aware reasoning selection that employs counterfactual intervention to identify reasoning paths beneficial for query-target alignment. Furthermore, we adopt reinforcement learning to selectively invoke reasoning only when necessary. Experiments on the MMEB-V2 benchmark demonstrate that our model achieves a score of 71.2 with only 4B parameters, establishing a new state-of-the-art while significantly reducing reasoning overhead and inference latency.

### 🤖 AI 总结

**一句话总结**：MMEmb-R1通过“按需推理+成对感知选择”将推理作为可控潜变量引入多模态嵌入学习，在降低推理开销的同时提升检索对齐效果并刷新MMEB-V2 SOTA。

**研究动机**：直接把链式推理用于嵌入学习会与成对对比监督结构不匹配，导致模型学到推理“格式捷径”而非真实语义对齐；同时推理并非对所有样本都有益，强制推理会带来额外延迟并可能掩盖简单样本的关键信号。

**核心方法**：提出将推理建模为潜变量，并用“pair-aware reasoning selection”结合反事实干预挑选对query-target对齐真正有帮助的推理路径；再用强化学习学习自适应控制策略，仅在必要时触发推理以兼顾效果与计算/时延。

**主要结论**：在MMEB-V2上，MMEmb-R1以4B参数取得71.2分的新SOTA，并且通过选择性推理显著减少推理开销与推理延迟，验证了按需推理对多模态嵌入任务更有效且更经济。

**关键词**：多模态嵌入, 推理增强, 链式思维, 成对感知选择, 反事实干预, 潜变量推理, 强化学习, 查询-目标对齐, 推理开销控制, MMEB-V2 基准

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06156v1) | [下载PDF](https://arxiv.org/pdf/2604.06156v1.pdf)

---

## [18. Lightweight Multimodal Adaptation of Vision Language Models for Species Recognition and Habitat Context Interpretation in Drone Thermal Imagery](https://arxiv.org/abs/2604.06124v1)

**作者**：Hao Chen, Fang Qiu, Fangchao Dong 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

This study proposes a lightweight multimodal adaptation framework to bridge the representation gap between RGB-pretrained VLMs and thermal infrared imagery, and demonstrates its practical utility using a real drone-collected dataset. A thermal dataset was developed from drone-collected imagery and was used to fine-tune VLMs through multimodal projector alignment, enabling the transfer of information from RGB-based visual representations to thermal radiometric inputs. Three representative models, including InternVL3-8B-Instruct, Qwen2.5-VL-7B-Instruct, and Qwen3-VL-8B-Instruct, were benchmarked under both closed-set and open-set prompting conditions for species recognition and instance enumeration. Among the tested models, Qwen3-VL-8B-Instruct with open-set prompting achieved the best overall performance, with F1 scores of 0.935 for deer, 0.915 for rhino, and 0.968 for elephant, and within-1 enumeration accuracies of 0.779, 0.982, and 1.000, respectively. In addition, combining thermal imagery with simultaneously collected RGB imagery enabled the model to generate habitat-context information, including land-cover characteristics, key landscape features, and visible human disturbance. Overall, the findings demonstrate that lightweight projector-based adaptation provides an effective and practical route for transferring RGB-pretrained VLMs to thermal drone imagery, expanding their utility from object-level recognition to habitat-context interpretation in ecological monitoring.

### 🤖 AI 总结

**一句话总结**：提出一种轻量级多模态投影器对齐方法，将RGB预训练视觉语言模型有效迁移到无人机热红外影像，实现物种识别、数量估计并可生成栖息地语境解读。

**研究动机**：现有VLM多在RGB图像上预训练，直接用于热红外会因表征差异导致性能下降；生态监测中无人机热成像常用但缺乏高效可迁移的多模态方法与数据支撑。

**核心方法**：构建真实无人机采集的热红外数据集，通过“多模态投影器对齐”进行轻量微调，桥接RGB视觉特征与热辐射输入；在闭集/开集提示条件下评测InternVL3与Qwen系列模型的物种识别与实例计数，并探索与同步RGB融合以输出栖息地上下文描述。

**主要结论**：Qwen3-VL-8B-Instruct在开集提示下总体最佳（如鹿/犀牛/大象F1分别达0.935/0.915/0.968，计数within-1准确率达0.779/0.982/1.000）；轻量投影器适配能实用地把RGB预训练VLM迁移到热红外无人机影像，并将能力扩展到栖息地语境解释与人类扰动识别等生态监测任务。

**关键词**：热红外图像, 无人机热成像, 视觉语言模型适配, 轻量化微调, 多模态投影器对齐, 跨模态表示迁移, 物种识别, 开放集提示, 实例计数, RGB-热红外融合, 栖息地语境解读, 生态监测

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06124v1) | [下载PDF](https://arxiv.org/pdf/2604.06124v1.pdf)

---

## [19. SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)

**作者**：Hiba Dahmani, Nathan Piasco, Moussab Bennehar 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-07

### 📄 论文摘要

Scalable generation of outdoor driving scenes requires 3D representations that remain consistent across multiple viewpoints and scale to large areas. Existing solutions either rely on image or video generative models distilled to 3D space, harming the geometric coherence and restricting the rendering to training views, or are limited to small-scale 3D scene or object-centric generation. In this work, we propose a 3D generative framework based on $Σ$-Voxfield grid, a discrete representation where each occupied voxel stores a fixed number of colorized surface samples. To generate this representation, we train a semantic-conditioned diffusion model that operates on local voxel neighborhoods and uses 3D positional encodings to capture spatial structure. We scale to large scenes via progressive spatial outpainting over overlapping regions. Finally, we render the generated $Σ$-Voxfield grid with a deferred rendering module to obtain photorealistic images, enabling large-scale multiview-consistent 3D scene generation without per-scene optimization. Extensive experiments show that our approach can generate diverse large-scale urban outdoor scenes, renderable into photorealistic images with various sensor configurations and camera trajectories while maintaining moderate computation cost compared to existing approaches.

### 🤖 AI 总结

**一句话总结**：提出SEM-ROVER：用语义条件扩散在Σ‑Voxfield体素表面采样网格上生成大尺度驾驶场景，并通过渐进式空间外延生成与延迟渲染实现多视角一致的逼真图像输出。

**研究动机**：现有将2D生成模型蒸馏到3D的方法常牺牲几何一致性且受限于训练视角，而纯3D生成多局限于小场景或物体级；因此需要一种可扩展到城市级、跨视角一致且无需逐场景优化的3D生成框架。

**核心方法**：使用Σ‑Voxfield离散3D表示（每个占据体素存固定数量的带颜色表面采样），训练一个在局部体素邻域上运行、结合3D位置编码的语义条件扩散模型；通过重叠区域的渐进式空间outpainting扩展到大范围，并用延迟渲染模块将生成网格渲染为可适配不同传感器与轨迹的写实图像。

**主要结论**：实验表明该方法能以相对适中的计算成本生成多样的大规模城市场景，并在不同相机配置与轨迹下保持较好的多视角一致性与照片级渲染质量，同时避免逐场景优化带来的开销。

**关键词**：自动驾驶场景生成, 大规模3D场景生成, 多视角一致性, 语义条件扩散模型, 体素网格表示, 局部体素邻域建模, 3D位置编码, 渐进式空间外延生成, 重叠区域拼接, 延迟渲染

**评分**：79

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06113v1) | [下载PDF](https://arxiv.org/pdf/2604.06113v1.pdf)

---

## [20. Scientific Graphics Program Synthesis via Dual Self-Consistency Reinforcement Learning](https://arxiv.org/abs/2604.06079v1)

**作者**：Juekai Lin, Yun Zhu, Honglin Lin 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Graphics Program Synthesis is pivotal for interpreting and editing visual data, effectively facilitating the reverse-engineering of static visuals into editable TikZ code. While TikZ is the de facto standard for scientific schematics due to its programmatic flexibility, its requirement for rigorous spatial precision presents a significant challenge for Multimodal Large Language Models. Progress is currently stifled by two primary gaps: (1) Data Quality Gap: existing image-TikZ corpora often lack strict executability and reliable visual alignment; (2) Evaluation Gap: a lack of benchmarks for both structural and visual fidelity. To address these, we present a closed-loop framework featuring: SciTikZ-230K, a large-scale, high-quality dataset from our Execution-Centric Data Engine covering 11 diverse scientific disciplines; SciTikZ-Bench, a multifaceted benchmark spanning from basic geometric constructs to intricate hierarchical schematics to evaluate both visual fidelity and structural logic. To further broaden the scope of visual-code optimization methodology, we introduce a novel Dual Self-Consistency Reinforcement Learning optimization paradigm, which utilizes Round-Trip Verification to penalize degenerate code and boost overall self-consistency. Empowered by these, our trained model SciTikZer-8B achieves state-of-the-art performance, consistently outperforming proprietary giants like Gemini-2.5-Pro and massive models like Qwen3-VL-235B-A22B-Instruct.

### 🤖 AI 总结

**一句话总结**：论文提出面向科学示意图的高质量图像→TikZ代码生成闭环体系（数据集+基准+强化学习优化），并训练出在结构与视觉一致性上显著领先的SciTikZer-8B模型。

**研究动机**：现有图像-TikZ数据集常存在代码不可执行、渲染与原图不对齐等问题，导致模型学到“退化代码”。同时缺少同时衡量结构逻辑与视觉保真度的统一评测基准，限制了方法迭代与公平比较。

**核心方法**：构建Execution-Centric数据引擎生成并验证SciTikZ-230K高质量数据，并提出SciTikZ-Bench覆盖从基础几何到复杂层级示意图的多维评测。训练上引入Dual Self-Consistency Reinforcement Learning：通过Round-Trip Verification（代码渲染回图再对齐验证）来惩罚退化/不一致程序、提升自一致性与可执行性。

**主要结论**：在新数据与新评测下，SciTikZer-8B在视觉对齐与结构正确性方面达到SOTA，表现稳定优于Gemini-2.5-Pro等闭源大模型以及更大规模的Qwen3-VL-235B-A22B-Instruct。结果表明“执行验证+回环一致性强化学习”对科学图形程序合成具有显著增益。

**关键词**：图形程序合成, 科学示意图解析, 执行一致性验证, 视觉-代码对齐, 结构与视觉保真评测, 基准测试套件, 双重自一致强化学习, Scientific

**评分**：80

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06079v1) | [下载PDF](https://arxiv.org/pdf/2604.06079v1.pdf)

---

## [21. Toward Aristotelian Medical Representations: Backpropagation-Free Layer-wise Analysis for Interpretable Generalized Metric Learning on MedMNIST](https://arxiv.org/abs/2604.06017v1)

**作者**：Michael Karnes, Alper Yilmaz  
**分类**：cs.CV  
**发布时间**：2026-04-07

### 📄 论文摘要

While deep learning has achieved remarkable success in medical imaging, the "black-box" nature of backpropagation-based models remains a significant barrier to clinical adoption. To bridge this gap, we propose Aristotelian Rapid Object Modeling (A-ROM), a framework built upon the Platonic Representation Hypothesis (PRH). This hypothesis posits that models trained on vast, diverse datasets converge toward a universal and objective representation of reality. By leveraging the generalizable metric space of pretrained Vision Transformers (ViTs), A-ROM enables the rapid modeling of novel medical concepts without the computational burden or opacity of further gradient-based fine-tuning. We replace traditional, opaque decision layers with a human-readable concept dictionary and a k-Nearest Neighbors (kNN) classifier to ensure the model's logic remains interpretable. Experiments on the MedMNIST v2 suite demonstrate that A-ROM delivers performance competitive with standard benchmarks while providing a simple and scalable, "few-shot" solution that meets the rigorous transparency demands of modern clinical environments.

### 🤖 AI 总结

**一句话总结**：A-ROM 利用预训练 ViT 的可泛化度量空间，通过概念字典+kNN 在无需反向传播微调的情况下，实现对新医疗概念的少样本、可解释建模，并在 MedMNIST v2 上达到有竞争力的性能。

**研究动机**：医疗影像深度模型虽准确但常依赖反向传播微调且难解释，阻碍临床落地；作者希望在保持性能的同时，用透明、低成本的方式快速适配新任务与新概念。

**核心方法**：基于“Platonic Representation Hypothesis”，直接复用预训练 ViT 的表示/度量空间，将传统不透明的分类头替换为人类可读的概念词典，并用 kNN 在该嵌入空间进行分类与概念匹配，从而实现层级/逐层的无反传分析与快速建模。

**主要结论**：在 MedMNIST v2 基准上，A-ROM 的表现与标准方法相当，同时提供更强的可解释性与可扩展的 few-shot 方案，满足临床对透明度和部署成本的要求。

**关键词**：医学影像可解释性, 免反向传播, 层级分析, 广义度量学习, k 近邻分类, 概念词典, 少样本学习, 表示空间对齐

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06017v1) | [下载PDF](https://arxiv.org/pdf/2604.06017v1.pdf)

---

## [22. OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)

**作者**：Yukun Wang, Ruihuang Li, Jiale Tao 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-07

### 📄 论文摘要

Video fundamentally intertwines two crucial axes: the dynamic content of a scene and the camera motion through which it is observed. However, existing generation models often entangle these factors, limiting independent control. In this work, we introduce OmniCamera, a unified framework designed to explicitly disentangle and command these two dimensions. This compositional approach enables flexible video generation by allowing arbitrary pairings of camera and content conditions, unlocking unprecedented creative control. To overcome the fundamental challenges of modality conflict and data scarcity inherent in such a system, we present two key innovations. First, we construct OmniCAM, a novel hybrid dataset combining curated real-world videos with synthetic data that provides diverse paired examples for robust multi-task learning. Second, we propose a Dual-level Curriculum Co-Training strategy that mitigates modality interference and synergistically learns from diverse data sources. This strategy operates on two levels: first, it progressively introduces control modalities by difficulties (condition-level), and second, trains for precise control on synthetic data before adapting to real data for photorealism (data-level). As a result, OmniCamera achieves state-of-the-art performance, enabling flexible control for complex camera movements while maintaining superior visual quality.

### 🤖 AI 总结

**一句话总结**：Video fundamentally intertwines two crucial axes: the dynamic content of a scene and the camera motion through which it is observed. However, existing generation models often entangle these factors, l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：多任务视频生成, 任意相机控制, 内容-相机解耦, 组合式条件生成, 相机运动建模, 混合数据集, 真实-合成数据融合, 课程学习联合训练, 模态冲突抑制, 合成到真实域适配

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06010v1) | [下载PDF](https://arxiv.org/pdf/2604.06010v1.pdf)

---

## [23. Is CLIP Cross-Eyed? Revealing and Mitigating Center Bias in the CLIP Family](https://arxiv.org/abs/2604.05971v1)

**作者**：Oscar Chew, Hsiao-Ying Huang, Kunal Jain 等 6 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-04-07

### 📄 论文摘要

Recent research has shown that contrastive vision-language models such as CLIP often lack fine-grained understanding of visual content. While a growing body of work has sought to address this limitation, we identify a distinct failure mode in the CLIP family, which we term center bias, that persists even in recent model variants. Specifically, CLIP tends to disproportionately focus on the central region of an image, overlooking important objects located near the boundaries. This limitation is fundamental as failure to recognize relevant objects makes it difficult to perform any sophisticated tasks that depend on those objects. To understand the underlying causes of the limitation, we conduct analyses from both representation and attention perspectives. Using interpretability methods, i.e., embedding decomposition and attention map analysis, we find that relevant concepts especially those associated with off-center objects vanish from the model's embedding in the final representation due to information loss during the aggregation of visual embeddings, particularly the reliance on pooling mechanisms. Finally, we show that this bias can be alleviated with training-free strategies such as visual prompting and attention redistribution by redirecting models' attention to off-center regions.

### 🤖 AI 总结

**一句话总结**：论文揭示CLIP系列模型存在“中心偏置”，更关注图像中心而忽略边缘重要目标，并提出无需训练的注意力重分配等方法缓解该问题。

**研究动机**：现有研究多聚焦CLIP缺乏细粒度理解，但作者发现一个更基础的失效模式：对非中心目标识别不足会直接影响依赖这些目标的下游复杂任务。

**核心方法**：从表示与注意力两条线分析：用embedding分解与注意力图可解释性手段定位信息丢失来源，指出视觉特征在聚合/池化过程中使离中心相关概念在最终表示中“消失”。同时提出训练免（training-free）的缓解策略，如视觉提示（visual prompting）和注意力重分配以引导模型关注边缘区域。

**主要结论**：CLIP的中心偏置在新版本中仍然存在，根因与视觉embedding聚合（尤其池化）导致的表征信息损失相关；通过不训练的提示与注意力引导可在一定程度上减轻对边缘目标的忽视。

**关键词**：中心偏置, 边缘目标识别, 视觉表征聚合, 池化信息损失, 嵌入分解, 注意力图分析, 可解释性分析, 视觉提示, 注意力重分配

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.05971v1) | [下载PDF](https://arxiv.org/pdf/2604.05971v1.pdf)

---

## cs.LG

## [24. Topological Characterization of Churn Flow and Unsupervised Correction to the Wu Flow-Regime Map in Small-Diameter Vertical Pipes](https://arxiv.org/abs/2604.06167v1)

**作者**：Brady Koenig, Sushovan Majhi, Atish Mitra 等 5 位作者  
**分类**：cs.LG, math.AT  
**发布时间**：2026-04-07

### 📄 论文摘要

Churn flow-the chaotic, oscillatory regime in vertical two-phase flow-has lacked a quantitative mathematical definition for over $40$ years. We introduce the first topology-based characterization using Euler Characteristic Surfaces (ECS). We formulate unsupervised regime discovery as Multiple Kernel Learning (MKL), blending two complementary ECS-derived kernels-temporal alignment ($L^1$ distance on the $χ(s,t)$ surface) and amplitude statistics (scale-wise mean, standard deviation, max, min)-with gas velocity. Applied to $37$ unlabeled air-water trials from Montana Tech, the self-calibrating framework learns weights $β_{ECS}=0.14$, $β_{amp}=0.50$, $β_{ugs}=0.36$, placing $64\%$ of total weight on topology-derived features ($β_{ECS} + β_{amp}$). The ECS-inferred slug/churn transition lies $+3.81$ m/s above Wu et al.'s (2017) prediction in $2$-in. tubing, quantifying reports that existing models under-predict slug persistence in small-diameter pipes where interfacial tension and wall-to-wall interactions dominate flow. Cross-facility validation on $947$ Texas A&M University images confirms $1.9\times$ higher topological complexity in churn vs. slug ($p < 10^{-5}$). Applied to $45$ TAMU pseudo-trials, the same unsupervised framework achieves $95.6\%$ $4$-class accuracy and $100\%$ churn recall-without any labeled training data-matching or exceeding supervised baselines that require thousands of annotated examples. This work provides the first mathematical definition of churn flow and demonstrates that unsupervised topological descriptors can challenge and correct widely adopted mechanistic models.

### 🤖 AI 总结

**一句话总结**：论文用拓扑数据分析（Euler Characteristic Surfaces, ECS）给出了竖直小管径两相流中“搅动流（churn flow）”的首个数学化定义，并以无监督方式修正了Wu流型图对段塞/搅动转捩的预测。

**研究动机**：搅动流长期缺乏可量化的严格定义，导致流型判别与机理模型（如Wu 2017流型图）在小管径条件下常出现系统性偏差（如低估段塞持续范围）。作者希望用无需标注数据的数学特征来自动发现流型并校正现有模型。

**核心方法**：将无监督流型发现表述为多核学习（MKL），融合两类ECS拓扑核（基于χ(s,t)曲面的L1时序对齐距离与多尺度幅值统计）以及气相表观速度等信息，通过学习核权重实现自校准聚类/分类与转捩边界推断。并在Montana Tech无标签试验上学习权重、在TAMU大规模图像数据上做跨设施验证与伪试验评测。

**主要结论**：学习到的权重显示拓扑相关特征占主要贡献（约64%），且ECS推断的段塞→搅动转捩气速比Wu(2017)在2英寸管中高3.81 m/s，定量证明传统模型在小管径下低估段塞持久性；跨设施数据验证搅动流的拓扑复杂度显著高于段塞（约1.9倍，p<1e-5）。在无任何标注训练数据下，方法在TAMU伪试验上达到95.6%四分类准确率与100%搅动召回，表现可匹配或超过依赖大量标注的监督基线。

**关键词**：垂直两相流, 流型识别, 段塞流-翻腾流转捩, 翻腾流定义, 拓扑数据分析, 欧拉示性数曲面（ECS）, 多核学习（MKL）, 无监督聚类, 核距离度量, 流型图修正, 跨设施验证

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06167v1) | [下载PDF](https://arxiv.org/pdf/2604.06167v1.pdf)

---

## [25. Target Policy Optimization](https://arxiv.org/abs/2604.06159v1)

**作者**：Jean Kaddour  
**分类**：cs.LG  
**发布时间**：2026-04-07

### 📄 论文摘要

In RL, given a prompt, we sample a group of completions from a model and score them. Two questions follow: which completions should gain probability mass, and how should the parameters move to realize that change? Standard policy-gradient methods answer both at once, so the update can overshoot or undershoot depending on the learning rate, clipping, and other optimizer choices. We introduce \emph{Target Policy Optimization} (TPO), which separates the two questions. Given scored completions, TPO constructs a target distribution $q_i \propto p_i^{\,\mathrm{old}} \exp(u_i)$ and fits the policy to it by cross-entropy. The loss gradient on sampled-completion logits is $p^θ- q$, which vanishes once the policy matches the target. On tabular bandits, transformer sequence tasks, and billion-parameter LLM RLVR, TPO matches PG, PPO, GRPO, and DG on easy tasks and substantially outperforms them under sparse reward. Code is available at https://github.com/JeanKaddour/tpo.

### 🤖 AI 总结

**一句话总结**：TPO通过先构造“目标策略分布”再用交叉熵拟合，将“该奖励哪些样本”和“参数如何更新”解耦，从而在稀疏奖励场景更稳健、效果更好。

**研究动机**：传统策略梯度/ PPO类方法把样本加权与参数步长绑定在同一次更新里，容易因学习率、clip等超参导致过冲或不足，尤其在稀疏奖励下训练不稳定、信号利用率低。作者希望把“想要的概率质量如何重分配”与“用多大步子去逼近”分开，以获得更可控的优化行为。

**核心方法**：在给定旧策略下采样并打分后，TPO先显式构造目标分布$q_i \propto p_i^{old}\exp(u_i)$（$u_i$由评分/优势等效用决定），再用交叉熵训练当前策略去匹配$q$。其在采样完成的logits上的梯度为$p^\theta-q$，当策略匹配目标分布时梯度自然归零，从而避免无谓更新并提升稳定性。

**主要结论**：在表格bandit、Transformer序列任务以及十亿参数LLM的RLVR实验中，TPO在简单任务上与PG/PPO/GRPO/DG相当，但在稀疏奖励条件下显著优于这些基线，表现出更强的鲁棒性与训练效率。

**关键词**：目标策略优化（TPO）, 强化学习（RL）, 策略梯度, 稀疏奖励, 目标分布构造, 交叉熵拟合, 采样补全评分, 上下文多臂老虎机

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06159v1) | [下载PDF](https://arxiv.org/pdf/2604.06159v1.pdf)

---

## [26. Gym-Anything: Turn any Software into an Agent Environment](https://arxiv.org/abs/2604.06126v1)

**作者**：Pranjal Aggarwal, Graham Neubig, Sean Welleck  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-07

### 📄 论文摘要

Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However, current research has largely focused on short-horizon tasks over a limited set of software with limited economic value, such as basic e-commerce and OS-configuration tasks. A key reason is that creating environments for complex software requires significant time and human effort, and therefore does not scale. To address this, we introduce Gym-Anything, a framework for converting any software into an interactive computer-use environment. We frame environment creation itself as a multi-agent task: a coding agent writes setup scripts, downloads real-world data, and configures the software, while producing evidence of correct setup. An independent audit agent then verifies evidence for the environment setup against a quality checklist. Using a taxonomy of economically valuable occupations grounded in U.S. GDP data, we apply this pipeline to 200 software applications with broad occupational coverage. The result is CUA-World, a collection of over 10K long-horizon tasks spanning domains from medical science and astronomy to engineering and enterprise systems, each configured with realistic data along with train and test splits. CUA-World also includes CUA-World-Long, a challenging long-horizon benchmark with tasks often requiring over 500 steps, far exceeding existing benchmarks. Distilling successful trajectories from the training split into a 2B vision-language model outperforms models 2$\times$ its size. We also apply the same auditing principle at test time: a separate VLM reviews completed trajectories and provides feedback on what remains, improving Gemini-3-Flash on CUA-World-Long from 11.5% to 14.0%. We release all code, infrastructure, and benchmark data to facilitate future research in realistic computer-use agents.

### 🤖 AI 总结

**一句话总结**：Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However, current research has largely focused on short-horizon tasks over a limited set of software wi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：软件环境构建框架, 自动化环境配置, 多智能体协作, 证据驱动验证, 长时序任务基准, 真实数据配置, 轨迹蒸馏, 视觉语言模型, 任务质量清单

**评分**：84

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06126v1) | [下载PDF](https://arxiv.org/pdf/2604.06126v1.pdf)

---

## [27. Learning $\mathsf{AC}^0$ Under Graphical Models](https://arxiv.org/abs/2604.06109v1)

**作者**：Gautam Chandrasekaran, Jason Gaitonde, Ankur Moitra 等 4 位作者  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-04-07

### 📄 论文摘要

In a landmark result, Linial, Mansour and Nisan (J. ACM 1993) gave a quasipolynomial-time algorithm for learning constant-depth circuits given labeled i.i.d. samples under the uniform distribution. Their work has had a deep and lasting legacy in computational learning theory, in particular introducing the $\textit{low-degree algorithm}$. However, an important critique of many results and techniques in the area is the reliance on product structure, which is unlikely to hold in realistic settings. Obtaining similar learning guarantees for more natural correlated distributions has been a longstanding challenge in the field.   In particular, we give quasipolynomial-time algorithms for learning $\mathsf{AC}^0$ substantially beyond the product setting, when the inputs come from any graphical model with polynomial growth that exhibits strong spatial mixing. The main technical challenge is in giving a workaround to Fourier analysis, which we do by showing how new sampling algorithms allow us to transfer statements about low-degree polynomial approximation under the uniform setting to graphical models. Our approach is general enough to extend to other well-studied function classes, like monotone functions and halfspaces.

### 🤖 AI 总结

**一句话总结**：提出在满足强空间混合（strong spatial mixing）且具有多项式增长的图模型分布下，以准多项式时间学习$​\mathsf{AC}^0$的算法，将经典“低阶算法”从独立同分布的均匀分布推广到相关分布。

**研究动机**：以往学习$​\mathsf{AC}^0$等函数类的关键技术高度依赖输入分布的乘积结构（独立性），但真实数据往往存在相关性；因此需要在更自然的相关分布（如图模型）下获得类似的学习保证。

**核心方法**：绕开传统傅里叶分析在相关分布下难以直接使用的问题，设计新的采样算法，将均匀分布下“可被低度多项式逼近”的性质迁移到满足强空间混合的图模型中，从而实现基于低度逼近的学习。

**主要结论**：在广泛的图模型分布族（多项式增长+强空间混合）上实现对$​\mathsf{AC}^0$的准多项式时间可学习性，并表明该框架还能推广到单调函数、半空间等其他经典函数类。

**关键词**：AC0学习, 准多项式时间算法, 图模型分布, 相关分布学习, 强空间混合, 多项式增长图, 低阶算法, 低阶多项式逼近, 采样算法, 傅里叶分析替代, 单调函数学习, 半空间学习

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06109v1) | [下载PDF](https://arxiv.org/pdf/2604.06109v1.pdf)

---

## [28. A machine learning framework for uncovering stochastic nonlinear dynamics from noisy data](https://arxiv.org/abs/2604.06081v1)

**作者**：Matteo Bosso, Giovanni Franzese, Kushal Swamy 等 6 位作者  
**分类**：cs.LG, cs.CE, math.DS  
**发布时间**：2026-04-07

### 📄 论文摘要

Modeling real-world systems requires accounting for noise - whether it arises from unpredictable fluctuations in financial markets, irregular rhythms in biological systems, or environmental variability in ecosystems. While the behavior of such systems can often be described by stochastic differential equations, a central challenge is understanding how noise influences the inference of system parameters and dynamics from data. Traditional symbolic regression methods can uncover governing equations but typically ignore uncertainty. Conversely, Gaussian processes provide principled uncertainty quantification but offer little insight into the underlying dynamics. In this work, we bridge this gap with a hybrid symbolic regression-probabilistic machine learning framework that recovers the symbolic form of the governing equations while simultaneously inferring uncertainty in the system parameters. The framework combines deep symbolic regression with Gaussian process-based maximum likelihood estimation to separately model the deterministic dynamics and the noise structure, without requiring prior assumptions about their functional forms. We verify the approach on numerical benchmarks, including harmonic, Duffing, and van der Pol oscillators, and validate it on an experimental system of coupled biological oscillators exhibiting synchronization, where the algorithm successfully identifies both the symbolic and stochastic components. The framework is data-efficient, requiring as few as 100-1000 data points, and robust to noise - demonstrating its broad potential in domains where uncertainty is intrinsic and both the structure and variability of dynamical systems must be understood.

### 🤖 AI 总结

**一句话总结**：提出一种将深度符号回归与高斯过程概率建模结合的框架，可从含噪数据中同时恢复随机非线性动力系统的方程结构与参数不确定性。

**研究动机**：真实系统数据普遍含噪，传统符号回归能找方程但缺少不确定性刻画，而高斯过程虽能量化不确定性却难提供可解释的动力学方程结构，因此需要兼顾“可解释结构发现+不确定性推断”的方法。

**核心方法**：框架用深度符号回归学习确定性动力学的符号形式，再用基于高斯过程的最大似然估计对噪声结构与系统参数不确定性进行推断，从而在不预设函数形式的情况下分离并建模确定性项与随机项。

**主要结论**：在谐振子、Duffing、van der Pol等数值基准及耦合生物振子同步实验中，该方法能同时识别符号动力学与随机成分；且在仅约100–1000个数据点下仍具数据效率与抗噪鲁棒性，适用于内在不确定性显著的领域建模。

**关键词**：随机微分方程, 符号回归, 深度符号回归, 高斯过程, 不确定性量化, 最大似然估计, 噪声结构建模, 参数推断, 数据高效学习, 同步生物振荡器

**评分**：70

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06081v1) | [下载PDF](https://arxiv.org/pdf/2604.06081v1.pdf)

---

## [29. Gated-SwinRMT: Unifying Swin Windowed Attention with Retentive Manhattan Decay via Input-Dependent Gating](https://arxiv.org/abs/2604.06014v1)

**作者**：Dipan Maity, Suman Mondal, Arindam Roy  
**分类**：cs.LG  
**发布时间**：2026-04-07

### 📄 论文摘要

We introduce Gated-SwinRMT, a family of hybrid vision transformers that combine the shifted-window attention of the Swin Transformer with the Manhattan-distance spatial decay of Retentive Networks (RMT), augmented by input-dependent gating. Self-attention is decomposed into consecutive width-wise and height-wise retention passes within each shifted window, where per-head exponential decay masks provide a two-dimensional locality prior without learned positional biases.   Two variants are proposed. \textbf{Gated-SwinRMT-SWAT} substitutes softmax with sigmoid activation, implements balanced ALiBi slopes with multiplicative post-activation spatial decay, and gates the value projection via SwiGLU; the Normalized output implicitly suppresses uninformative attention scores. \textbf{Gated-SwinRMT-Retention} retains softmax-normalized retention with an additive log-space decay bias and incorporates an explicit G1 sigmoid gate -- projected from the block input and applied after local context enhancement (LCE) but prior to the output projection~$W_O$ -- to alleviate the low-rank $W_V \!\cdot\! W_O$ bottleneck and enable input-dependent suppression of attended outputs.   We assess both variants on Mini-ImageNet ($224{\times}224$, 100 classes) and CIFAR-10 ($32{\times}32$, 10 classes) under identical training protocols, utilizing a single GPU due to resource limitations. At ${\approx}77$--$79$\,M parameters, Gated-SwinRMT-SWAT achieves $80.22\%$ and Gated-SwinRMT-Retention $78.20\%$ top-1 test accuracy on Mini-ImageNet, compared with $73.74\%$ for the RMT baseline. On CIFAR-10 -- where small feature maps cause the adaptive windowing mechanism to collapse attention to global scope -- the accuracy advantage compresses from $+6.48$\,pp to $+0.56$\,pp.

### 🤖 AI 总结

**一句话总结**：We introduce Gated-SwinRMT, a family of hybrid vision transformers that combine the shifted-window attention of the Swin Transformer with the Manhattan-distance spatial decay of Retentive Networks (RM...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Swin窗口注意力, 移位窗口, 曼哈顿距离衰减, 指数衰减掩码, 输入依赖门控, 局部上下文增强（LCE）, 低秩瓶颈（WV·WO）, Gated-SwinRMT

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2604.06014v1) | [下载PDF](https://arxiv.org/pdf/2604.06014v1.pdf)

---

## [30. Data Distribution Valuation Using Generalized Bayesian Inference](https://arxiv.org/abs/2604.05993v1)

**作者**：Cuong N. Nguyen, Cuong V. Nguyen  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-04-07

### 📄 论文摘要

We investigate the data distribution valuation problem, which aims to quantify the values of data distributions from their samples. This is a recently proposed problem that is related to but different from classical data valuation and can be applied to various applications. For this problem, we develop a novel framework called Generalized Bayes Valuation that utilizes generalized Bayesian inference with a loss constructed from transferability measures. This framework allows us to solve, in a unified way, seemingly unrelated practical problems, such as annotator evaluation and data augmentation. Using the Bayesian principles, we further improve and enhance the applicability of our framework by extending it to the continuous data stream setting. Our experiment results confirm the effectiveness and efficiency of our framework in different real-world scenarios.

### 🤖 AI 总结

**一句话总结**：提出“广义贝叶斯估值（Generalized Bayes Valuation）”框架，用广义贝叶斯推断从样本中量化数据分布的价值，并统一解决如标注者评估与数据增强等任务。

**研究动机**：传统数据估值多关注单个样本/子集，而“数据分布估值”需要评估不同数据来源/生成机制的整体贡献，且在多种实际场景中缺乏统一、可扩展的方法。

**核心方法**：构建基于可迁移性度量（transferability measures）的损失函数，并用广义贝叶斯推断将“分布价值”转化为后验式的可计算估值框架；同时扩展到连续数据流场景以支持在线/持续更新。

**主要结论**：实验表明该框架在多个真实场景中有效且高效，能够以统一方式评估数据分布价值，并在连续数据到达时保持良好适用性与可扩展性。

**关键词**：数据分布估值, 广义贝叶斯推断, 迁移性度量, 损失构造, 广义贝叶斯估值框架, 样本驱动估值, 标注者评估, 数据增强, 连续数据流, 贝叶斯更新

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.05993v1) | [下载PDF](https://arxiv.org/pdf/2604.05993v1.pdf)

---

