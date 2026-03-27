# arXiv AI 论文日报 | 2026-03-27

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.AI](#csAI) (5 篇)
- [cs.CL](#csCL) (4 篇)
- [cs.LG](#csLG) (6 篇)

---

## cs.AI

## [1. Training the Knowledge Base through Evidence Distillation and Write-Back Enrichment](https://arxiv.org/abs/2603.25737v1)

**作者**：Yuxing Lu, Xukai Zhao, Wei Wu 等 4 位作者  
**分类**：cs.AI, cs.CL, cs.IR  
**发布时间**：2026-03-26

### 📄 论文摘要

The knowledge base in a retrieval-augmented generation (RAG) system is typically assembled once and never revised, even though the facts a query requires are often fragmented across documents and buried in irrelevant content. We argue that the knowledge base should be treated as a trainable component and propose WriteBack-RAG, a framework that uses labeled examples to identify where retrieval succeeds, isolate the relevant documents, and distill them into compact knowledge units that are indexed alongside the original corpus. Because the method modifies only the corpus, it can be applied once as an offline preprocessing step and combined with any RAG pipeline. Across four RAG methods, six benchmarks, and two LLM backbones, WriteBack-RAG improves every evaluated setting, with gains averaging +2.14%. Cross-method transfer experiments further show that the distilled knowledge benefits RAG pipelines other than the one used to produce it, confirming that the improvement resides in the corpus itself.

### 🤖 AI 总结

**一句话总结**：WriteBack-RAG将知识库视为可训练组件，通过证据蒸馏与写回增强离线改造语料，从而在多种RAG管线与基座模型上稳定提升效果。

**研究动机**：传统RAG的知识库通常一次性构建后不再更新，但真实查询所需事实往往分散在多文档且夹杂噪声，导致检索命中却难以有效利用。作者认为应利用标注数据识别“检索何时成功”，并把分散证据压缩成更易检索与消费的知识单元。

**核心方法**：WriteBack-RAG用带标签样例评估检索表现，定位并筛出真正相关的证据文档片段，然后将其蒸馏成紧凑的“知识单元”写回到语料库，并与原始语料一起建立索引。由于只修改语料而不改动模型/管线，它可作为一次性离线预处理，并可与任意RAG方法组合使用。

**主要结论**：在四种RAG方法、六个基准和两种LLM骨干上均带来一致提升，平均增益约+2.14%。跨方法迁移表明蒸馏写回的收益主要来自语料本身的增强，可普惠不同RAG管线。

**关键词**：检索增强生成（RAG）, 可训练知识库, 证据蒸馏, 写回式知识增强, 语料库增广, 离线预处理, 监督式检索优化, 知识单元抽取, 索引扩展, 跨方法迁移, 检索鲁棒性

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25737v1) | [下载PDF](https://arxiv.org/pdf/2603.25737v1.pdf)

---

## [2. Back to Basics: Revisiting ASR in the Age of Voice Agents](https://arxiv.org/abs/2603.25727v1)

**作者**：Geeyang Tay, Wentao Ma, Jaewon Lee 等 11 位作者  
**分类**：cs.AI, cs.MM  
**发布时间**：2026-03-26

### 📄 论文摘要

Automatic speech recognition (ASR) systems have achieved near-human accuracy on curated benchmarks, yet still fail in real-world voice agents under conditions that current evaluations do not systematically cover. Without diagnostic tools that isolate specific failure factors, practitioners cannot anticipate which conditions, in which languages, will cause what degree of degradation. We introduce WildASR, a multilingual (four-language) diagnostic benchmark sourced entirely from real human speech that factorizes ASR robustness along three axes: environmental degradation, demographic shift, and linguistic diversity. Evaluating seven widely used ASR systems, we find severe and uneven performance degradation, and model robustness does not transfer across languages or conditions. Critically, models often hallucinate plausible but unspoken content under partial or degraded inputs, creating concrete safety risks for downstream agent behavior. Our results demonstrate that targeted, factor-isolated evaluation is essential for understanding and improving ASR reliability in production systems. Besides the benchmark itself, we also present three analytical tools that practitioners can use to guide deployment decisions.

### 🤖 AI 总结

**一句话总结**：论文提出并发布WildASR这一来自真实人类语音的多语种诊断基准，用于系统化分解ASR在真实语音代理场景中的鲁棒性问题，并揭示多种ASR在不同条件下会出现严重退化与“幻听式”错误。

**研究动机**：现有ASR在标准化榜单上接近人类，但在真实语音代理中遇到噪声、口音/人群差异、语言多样性等因素时仍频繁失败，且缺少能隔离具体失效因素的诊断评测工具来指导部署与风险预估。

**核心方法**：构建WildASR：覆盖四种语言、全部源自真实语音的数据集，并沿三条轴（环境退化、人口统计/说话人群体偏移、语言多样性）进行因子化设计；在此基准上评测7个常用ASR系统，并提供3个分析工具辅助定位退化来源与部署决策。

**主要结论**：多数ASR在真实条件下表现出现严重且不均衡的下降，且鲁棒性难以在不同语言与条件间迁移；在输入不完整或退化时模型还会生成看似合理但未被说出的内容，带来下游语音代理的明确安全风险，因而需要因子隔离的针对性评测与诊断来提升生产可靠性。

**关键词**：自动语音识别, 语音助手, 鲁棒性评测, 诊断基准, 多语言评测, 真实语音数据, 环境退化, 人口统计偏移, 语言多样性, 语音安全风险, 跨语言泛化

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25727v1) | [下载PDF](https://arxiv.org/pdf/2603.25727v1.pdf)

---

## [3. R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning](https://arxiv.org/abs/2603.25720v1)

**作者**：Zirui Zhang, Haoyu Dong, Kexin Pei 等 4 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Robust perception and reasoning require consistency across sensory modalities. Yet current multimodal models often violate this principle, yielding contradictory predictions for visual and textual representations of the same concept. Rather than masking these failures with standard voting mechanisms, which can amplify systematic biases, we show that cross-modal inconsistency provides a rich and natural signal for learning. We introduce RC2, a reinforcement learning framework that resolves internal conflicts by enforcing cross-modal cycle consistency. By requiring a model to perform backward inference, switch modalities, and reliably reconstruct the answer through forward inference, we obtain a dense, label-free reward. This cyclic constraint encourages the model to align its internal representations autonomously. Optimizing for this structure mitigates modality-specific errors and improves reasoning accuracy by up to 7.6 points. Our results suggest that advanced reasoning emerges not only from scaling data, but also from enforcing a structurally consistent understanding of the world.

### 🤖 AI 总结

**一句话总结**：R-C2通过强化学习施加跨模态“循环一致性”约束，把视觉-文本预测不一致转化为无标注奖励信号，从而提升多模态推理准确性。

**研究动机**：现有多模态模型对同一概念的视觉与文本表征常给出相互矛盾的预测，传统投票/集成往往只是掩盖问题并可能放大系统性偏差。作者认为这种跨模态不一致本身是可用于学习的自然监督信号。

**核心方法**：提出RC2强化学习框架：让模型先进行反向推断、切换模态，再通过前向推断重构答案，以“能否在跨模态循环中自洽重建”构造密集、无需标签的奖励。通过优化该循环一致性约束，模型可在训练中自动对齐跨模态内部表征并减少模态特有错误。

**主要结论**：施加跨模态循环一致性可显著缓解视觉/文本通道的冲突并提升推理性能，最高带来约7.6个点的准确率增益。结果表明，推理能力不仅依赖数据规模，也可通过结构性一致性约束来涌现和增强。

**关键词**：多模态推理, 跨模态一致性, 循环一致性, 强化学习, 无标签奖励, 稠密奖励信号, 反向推理, 模态切换, 表示对齐, 偏差放大抑制, 模态特定错误缓解

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25720v1) | [下载PDF](https://arxiv.org/pdf/2603.25720v1.pdf)

---

## [4. Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?](https://arxiv.org/abs/2603.25719v1)

**作者**：Abhishek Bhandwaldar, Mihir Choudhury, Ruchir Puri 等 4 位作者  
**分类**：cs.AI, cs.AR, cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

We present an empirical study of how far general-purpose coding agents -- without hardware-specific training -- can optimize hardware designs from high-level algorithmic specifications. We introduce an agent factory, a two-stage pipeline that constructs and coordinates multiple autonomous optimization agents.   In Stage~1, the pipeline decomposes a design into sub-kernels, independently optimizes each using pragma and code-level transformations, and formulates an Integer Linear Program (ILP) to assemble globally promising configurations under an area constraint. In Stage~2, it launches $N$ expert agents over the top ILP solutions, each exploring cross-function optimizations such as pragma recombination, loop fusion, and memory restructuring that are not captured by sub-kernel decomposition.   We evaluate the approach on 12 kernels from HLS-Eval and Rodinia-HLS using Claude Code (Opus~4.5/4.6) with AMD Vitis HLS. Scaling from 1 to 10 agents yields a mean $8.27\times$ speedup over baseline, with larger gains on harder benchmarks: streamcluster exceeds $20\times$ and kmeans reaches approximately $10\times$. Across benchmarks, agents consistently rediscover known hardware optimization patterns without domain-specific training, and the best designs often do not originate from top-ranked ILP candidates, indicating that global optimization exposes improvements missed by sub-kernel search. These results establish agent scaling as a practical and effective axis for HLS optimization.

### 🤖 AI 总结

**一句话总结**：提出“Agent Factory”两阶段多智能体流水线，用通用编程代理在HLS中自动探索pragma/代码变换与跨函数优化，在多基准上实现显著加速。

**研究动机**：现有HLS优化高度依赖硬件专家经验与手工迭代，且单一代理或局部搜索容易陷入次优；作者希望验证“无硬件专训的通用编码代理”在硬件优化上能走多远，并评估多智能体扩展是否带来稳定收益。

**核心方法**：两阶段：阶段1将设计分解为子kernel，各自做pragma与代码级变换并用ILP在面积约束下组合出全局候选；阶段2对ILP前若干解启动N个“专家代理”进行跨函数/全局优化（如pragma重组、循环融合、内存结构重整），以弥补分解搜索的盲区。

**主要结论**：在12个HLS基准（Vitis HLS + Claude Code）上，代理从1扩展到10个带来平均8.27×加速，困难任务收益更大（streamcluster >20×、kmeans≈10×）；代理无需领域训练也能复现经典硬件优化模式，且最佳设计常不来自ILP最高排名，说明全局多智能体搜索能发现分解与ILP阶段遗漏的改进。

**关键词**：高层次综合（HLS）优化, 代码智能体（Agent）, 多智能体协同优化, 两阶段优化流水线, 子内核分解, 跨函数优化, 编译指令（pragma）优化, 整数线性规划（ILP）, 循环融合, 存储结构重构, 面积约束优化

**评分**：53

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25719v1) | [下载PDF](https://arxiv.org/pdf/2603.25719v1.pdf)

---

## [5. Is Mathematical Problem-Solving Expertise in Large Language Models Associated with Assessment Performance?](https://arxiv.org/abs/2603.25633v1)

**作者**：Liang Zhang, Yu Fu, Xinyi Jin  
**分类**：cs.AI  
**发布时间**：2026-03-26

### 📄 论文摘要

Large Language Models (LLMs) are increasingly used in math education not only as problem solvers but also as assessors of learners' reasoning. However, it remains unclear whether stronger math problem-solving ability is associated with stronger step-level assessment performance. This study examines that relationship using the GSM8K and MATH subsets of PROCESSBENCH, a human-annotated benchmark for identifying the earliest erroneous step in mathematical reasoning. We evaluate two LLM-based math tutor agent settings, instantiated with GPT-4 and GPT-5, in two independent tasks on the same math problems: solving the original problem and assessing a benchmark-provided solution by predicting the earliest erroneous step. Results show a consistent within-model pattern: assessment accuracy is substantially higher on math problem items the same model solved correctly than on items it solved incorrectly, with statistically significant associations across both models and datasets. At the same time, assessment remains more difficult than direct problem solving, especially on error-present solutions. These findings suggest that math problem-solving expertise supports stronger assessment performance, but reliable step-level diagnosis also requires additional capabilities such as step tracking, monitoring, and precise error localization. The results have implications for the design and evaluation of AI-supported Adaptive Instructional Systems (AISs) for formative assessment in math education.

### 🤖 AI 总结

**一句话总结**：研究发现：LLM在数学题上解题越正确，其对同题解答过程“最早错误步”的诊断评估也越准确，但评估整体仍比直接解题更难。

**研究动机**：LLM正被用于数学教育中的形成性评价与推理诊断，但尚不清楚模型的解题能力是否与逐步评估（定位最早错误步骤）能力相关。

**核心方法**：在PROCESSBENCH的GSM8K与MATH子集上，用GPT-4与GPT-5构建两种数学辅导代理设置，对同一批题分别执行两项独立任务：解原题与评估给定解答（预测最早错误步），并统计解题正确性与评估准确率的关联及显著性。

**主要结论**：两种模型与两个数据集上均呈现一致的“模型内”关联：模型解对的题，其评估准确率显著高于模型解错的题，且统计显著；同时逐步错误定位（尤其面对包含错误的解答）比直接解题更困难，提示可靠诊断还需额外能力如步骤跟踪、监控与精确定位。

**关键词**：数学推理评测, 步骤级诊断, 最早错误步骤定位, 过程式解题评测, 形成性评价, 自适应教学系统, 数学解题能力, 评估-解题关联性, 错误定位, 推理步骤跟踪

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25633v1) | [下载PDF](https://arxiv.org/pdf/2603.25633v1.pdf)

---

## cs.CL

## [6. Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723v1)

**作者**：Linyue Pan, Lexiao Zou, Shuo Guo 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-26

### 📄 论文摘要

Agent performance increasingly depends on \emph{harness engineering}, yet harness design is usually buried in controller code and runtime-specific conventions, making it hard to transfer, compare, and study as a scientific object. We ask whether the high-level control logic of an agent harness can instead be externalized as a portable executable artifact. We introduce \textbf{Natural-Language Agent Harnesses} (NLAHs), which express harness behavior in editable natural language, and \textbf{Intelligent Harness Runtime} (IHR), a shared runtime that executes these harnesses through explicit contracts, durable artifacts, and lightweight adapters. Across coding and computer-use benchmarks, we conduct controlled evaluations of operational viability, module ablation, and code-to-text harness migration.

### 🤖 AI 总结

**一句话总结**：提出“自然语言代理执行框架”(NLAH)与统一运行时(IHR)，把原本写在控制器代码里的Agent harness逻辑外置为可移植、可编辑、可执行的自然语言工件，并在多类基准上验证其可行性与收益。

**研究动机**：现有Agent性能越来越依赖harness工程，但其设计细节常被埋在特定运行时/控制器代码与隐式约定中，导致难以复用迁移、难以公平比较、也难以作为可研究的“科学对象”被系统分析。

**核心方法**：用NLAH以自然语言显式描述harness的高层控制逻辑（如步骤编排、工具调用规则、错误处理与状态约束），并用IHR通过“明确契约 + 持久化工件 + 轻量适配器”来执行这些文本化harness；同时进行受控实验，包括运行可行性评估、模块消融以及从代码harness到文本harness的迁移对比。

**主要结论**：在编程与计算机使用等基准上，文本化harness在共享运行时下能够稳定执行并达到可用性能，且关键运行时组件对效果有可量化贡献；同时代码到自然语言harness的迁移可行，提升了可移植性与可比较性，使harness设计更易迭代与研究。

**关键词**：Agent 控制逻辑外置, 可移植可执行工件, 共享运行时, 运行时契约, 耐久化工件, 轻量适配器, 代码到文本迁移, 模块消融评测

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25723v1) | [下载PDF](https://arxiv.org/pdf/2603.25723v1.pdf)

---

## [7. Measuring What Matters -- or What's Convenient?: Robustness of LLM-Based Scoring Systems to Construct-Irrelevant Factors](https://arxiv.org/abs/2603.25674v1)

**作者**：Cole Walsh, Rodica Ivan  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-03-26

### 📄 论文摘要

Automated systems have been widely adopted across the educational testing industry for open-response assessment and essay scoring. These systems commonly achieve performance levels comparable to or superior than trained human raters, but have frequently been demonstrated to be vulnerable to the influence of construct-irrelevant factors (i.e., features of responses that are unrelated to the construct assessed) and adversarial conditions. Given the rising usage of large language models in automated scoring systems, there is a renewed focus on ``hallucinations'' and the robustness of these LLM-based automated scoring approaches to construct-irrelevant factors. This study investigates the effects of construct-irrelevant factors on a dual-architecture LLM-based scoring system designed to score short essay-like open-response items in a situational judgment test. It was found that the scoring system was generally robust to padding responses with meaningless text, spelling errors, and writing sophistication. Duplicating large passages of text resulted in lower scores predicted by the system, on average, contradicting results from previous studies of non-LLM-based scoring systems, while off-topic responses were heavily penalized by the scoring system. These results provide encouraging support for the robustness of future LLM-based scoring systems when designed with construct relevance in mind.

### 🤖 AI 总结

**一句话总结**：论文评估一套用于情境判断测验短作文评分的双架构LLM评分系统，发现其对多种“构念无关因素”总体较鲁棒，且能强烈惩罚跑题作答。

**研究动机**：自动作文评分虽已广泛应用，但常受拼写、灌水、文风等与能力无关因素及对抗输入影响；随着LLM进入评分系统，需要重新检验其在“幻觉/噪声”条件下的稳健性与公平性。

**核心方法**：作者以一套双架构的LLM自动评分系统为对象，在情境判断测验的短开放作答上系统施加构念无关扰动（无意义填充、拼写错误、写作复杂度、重复粘贴大段文本、跑题内容等），比较模型预测分数的变化以衡量鲁棒性。

**主要结论**：系统对无意义填充、拼写错误与写作复杂度变化整体不敏感；大段重复文本反而平均降低得分（与以往非LLM评分研究相反），而跑题作答会被显著降分，表明在强调构念相关性设计下LLM评分系统具备较好的稳健性。

**关键词**：LLM自动评分, 教育测评, 开放式作答评分, 鲁棒性评测, 构念无关因素, 离题检测, 文本填充攻击, 文本重复检测, 情境判断测验, 双架构模型

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25674v1) | [下载PDF](https://arxiv.org/pdf/2603.25674v1.pdf)

---

## [8. Beyond Via: Analysis and Estimation of the Impact of Large Language Models in Academic Papers](https://arxiv.org/abs/2603.25638v1)

**作者**：Mingmeng Geng, Yuhang Dong, Thierry Poibeau  
**分类**：cs.CL, cs.AI, cs.CY, cs.DL, cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

Through an analysis of arXiv papers, we report several shifts in word usage that are likely driven by large language models (LLMs) but have not previously received sufficient attention, such as the increased frequency of "beyond" and "via" in titles and the decreased frequency of "the" and "of" in abstracts. Due to the similarities among different LLMs, experiments show that current classifiers struggle to accurately determine which specific model generated a given text in multi-class classification tasks. Meanwhile, variations across LLMs also result in evolving patterns of word usage in academic papers. By adopting a direct and highly interpretable linear approach and accounting for differences between models and prompts, we quantitatively assess these effects and show that real-world LLM usage is heterogeneous and dynamic.

### 🤖 AI 总结

**一句话总结**：论文通过对arXiv论文文本的统计分析，量化了LLM使用对学术写作词汇模式（尤其标题与摘要用词）的影响，并指出这种影响随模型/提示而动态变化且难以精确溯源到具体模型。

**研究动机**：尽管LLM已广泛用于学术写作，但其带来的细粒度语言漂移（例如特定词在标题/摘要中的系统性增减）与真实使用的异质性缺乏可解释、可量化的分析。

**核心方法**：基于arXiv语料，统计对比标题与摘要的词频变化，并在控制不同模型与提示差异的前提下，采用直接且可解释的线性估计方法来量化LLM对用词分布的影响；同时评估多分类场景下“判别由哪个LLM生成”的分类器能力。

**主要结论**：观测到多种可能由LLM驱动的写作风格变化（如标题中“beyond”“via”增多、摘要中“the”“of”减少），且由于不同LLM文本相似，现有分类器难以在多分类中可靠识别具体来源模型；但模型间仍存在差异，使得学术文本的LLM影响呈现异质且随时间演化的动态模式。

**关键词**：学术写作风格变化, LLM 影响评估, 词频漂移, 风格计量分析, LLM 文本检测, 模型归因, 多分类识别, 可解释线性模型, 提示词差异

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25638v1) | [下载PDF](https://arxiv.org/pdf/2603.25638v1.pdf)

---

## [9. PICon: A Multi-Turn Interrogation Framework for Evaluating Persona Agent Consistency](https://arxiv.org/abs/2603.25620v1)

**作者**：Minseo Kim, Sujeong Im, Junseong Choi 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-26

### 📄 论文摘要

Large language model (LLM)-based persona agents are rapidly being adopted as scalable proxies for human participants across diverse domains. Yet there is no systematic method for verifying whether a persona agent's responses remain free of contradictions and factual inaccuracies throughout an interaction. A principle from interrogation methodology offers a lens: no matter how elaborate a fabricated identity, systematic interrogation will expose its contradictions. We apply this principle to propose PICon, an evaluation framework that probes persona agents through logically chained multi-turn questioning. PICon evaluates consistency along three core dimensions: internal consistency (freedom from self-contradiction), external consistency (alignment with real-world facts), and retest consistency (stability under repetition). Evaluating seven groups of persona agents alongside 63 real human participants, we find that even systems previously reported as highly consistent fail to meet the human baseline across all three dimensions, revealing contradictions and evasive responses under chained questioning. This work provides both a conceptual foundation and a practical methodology for evaluating persona agents before trusting them as substitutes for human participants. We provide the source code and an interactive demo at: https://kaist-edlab.github.io/picon/

### 🤖 AI 总结

**一句话总结**：PICon通过“逻辑链式”的多轮追问来系统检测LLM人格代理在对话中的一致性，并发现其在自洽、事实对齐与重复稳定性上仍显著落后于人类。

**研究动机**：LLM人格代理正被用作人类参与者的可扩展替代，但缺乏一种系统方法验证其在长程交互中是否会自相矛盾、偏离事实或在重复提问时不稳定。作者借鉴审讯学观点：再精心的虚构身份也会在持续追问下暴露矛盾，从而提出对应评测需求。

**核心方法**：提出PICon评测框架，用多轮、逻辑依赖的链式问题对人格代理进行“追问式”探测，并从内部一致性（不自相矛盾）、外部一致性（符合现实事实）和复测一致性（重复提问稳定）三维度量化评估。实验对比7组人格代理与63名真实人类参与者，观察矛盾、事实错误与回避性回答等现象。

**主要结论**：即便先前被报告为“高一致性”的系统，在PICon的链式追问下仍无法达到人类基线，三类一致性指标均暴露出矛盾与规避行为。PICon为在将人格代理作为人类替代之前提供了更可靠的概念框架与可操作的评测方法（并开源代码与Demo）。

**关键词**：人格代理, 一致性评测, 多轮审问, 链式提问, 自相矛盾检测, 事实一致性, 复测一致性, 回避回答检测, 人类基线对比, LLM 评测框架

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25620v1) | [下载PDF](https://arxiv.org/pdf/2603.25620v1.pdf)

---

## cs.CV

## [10. ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)

**作者**：Yawen Luo, Xiaoyu Shi, Junhao Zhuang 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Multi-shot video generation is crucial for long narrative storytelling, yet current bidirectional architectures suffer from limited interactivity and high latency. We propose ShotStream, a novel causal multi-shot architecture that enables interactive storytelling and efficient on-the-fly frame generation. By reformulating the task as next-shot generation conditioned on historical context, ShotStream allows users to dynamically instruct ongoing narratives via streaming prompts. We achieve this by first fine-tuning a text-to-video model into a bidirectional next-shot generator, which is then distilled into a causal student via Distribution Matching Distillation. To overcome the challenges of inter-shot consistency and error accumulation inherent in autoregressive generation, we introduce two key innovations. First, a dual-cache memory mechanism preserves visual coherence: a global context cache retains conditional frames for inter-shot consistency, while a local context cache holds generated frames within the current shot for intra-shot consistency. And a RoPE discontinuity indicator is employed to explicitly distinguish the two caches to eliminate ambiguity. Second, to mitigate error accumulation, we propose a two-stage distillation strategy. This begins with intra-shot self-forcing conditioned on ground-truth historical shots and progressively extends to inter-shot self-forcing using self-generated histories, effectively bridging the train-test gap. Extensive experiments demonstrate that ShotStream generates coherent multi-shot videos with sub-second latency, achieving 16 FPS on a single GPU. It matches or exceeds the quality of slower bidirectional models, paving the way for real-time interactive storytelling. Training and inference code, as well as the models, are available on our

### 🤖 AI 总结

**一句话总结**：ShotStream 提出一种因果式流式多镜头视频生成框架，可在用户持续交互指令下以低延迟生成连贯的长叙事视频。

**研究动机**：现有多镜头视频生成多依赖双向架构，难以在生成过程中实时插入新指令且推理延迟高；同时自回归式多镜头生成容易出现跨镜头不一致与误差累积。

**核心方法**：将任务改写为“基于历史上下文的下一镜头生成”，先把文本到视频模型微调成双向下一镜头生成器，再用分布匹配蒸馏得到因果学生模型以支持流式生成；通过全局/局部双缓存记忆与 RoPE 不连续指示区分跨镜头与镜头内上下文以保持一致性，并用两阶段蒸馏（先用真值历史做镜头内 self-forcing，再逐步过渡到用自生成历史做镜头间 self-forcing）缓解误差累积与训练-测试分布差异。

**主要结论**：实验表明 ShotStream 在单 GPU 上可实现亚秒级延迟与约 16 FPS 的生成速度，同时在多镜头连贯性与总体质量上达到或超过更慢的双向模型，为实时交互式叙事视频生成提供了可行方案。

**关键词**：多镜头视频生成, 交互式叙事, 流式提示, 因果生成架构, 下一镜头生成, 文本到视频, 分布匹配蒸馏, 双向生成器, 双缓存记忆机制, RoPE不连续指示, 两阶段自驱动蒸馏

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25746v1) | [下载PDF](https://arxiv.org/pdf/2603.25746v1.pdf)

---

## [11. MuRF: Unlocking the Multi-Scale Potential of Vision Foundation Models](https://arxiv.org/abs/2603.25744v1)

**作者**：Bocheng Zou, Mu Cai, Mark Stanley 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Vision Foundation Models (VFMs) have become the cornerstone of modern computer vision, offering robust representations across a wide array of tasks. While recent advances allow these models to handle varying input sizes during training, inference typically remains restricted to a single, fixed scale. This prevalent single-scale paradigm overlooks a fundamental property of visual perception: varying resolutions offer complementary inductive biases, where low-resolution views excel at global semantic recognition and high-resolution views are essential for fine-grained refinement. In this work, we propose Multi-Resolution Fusion (MuRF), a simple yet universally effective strategy to harness this synergy at inference time. Instead of relying on a single view, MuRF constructs a unified representation by processing an image at multiple resolutions through a frozen VFM and fusing the resulting features. The universality of MuRF is its most compelling attribute. It is not tied to a specific architecture, serving instead as a fundamental, training-free enhancement to visual representation. We empirically validate this by applying MuRF to a broad spectrum of critical computer vision tasks across multiple distinct VFM families - primarily DINOv2, but also demonstrating successful generalization to contrastive models like SigLIP2.

### 🤖 AI 总结

**一句话总结**：MuRF 在推理阶段将同一图像的多分辨率特征通过冻结的视觉基础模型提取并融合，作为一种无需训练的通用增强策略提升多类视觉任务表现。

**研究动机**：现有 VFM 虽可在训练时适配不同输入尺寸，但推理常固定单一尺度，忽略低分辨率利于全局语义、高分辨率利于细节判别的互补归纳偏置。

**核心方法**：对输入图像构造多个分辨率视图，分别送入冻结的 VFM（如 DINOv2、SigLIP2）提取特征，并将多尺度特征进行融合得到统一表示，用于下游任务推理；整个过程训练无关、架构无关。

**主要结论**：实验证明 MuRF 可在多种关键视觉任务与多种 VFM 家族上稳定带来收益，显示多尺度推理融合是一种简单、通用且有效的表示增强手段。

**关键词**：多分辨率融合, 多尺度推理, 视觉基础模型, 特征融合, 冻结骨干网络, 免训练增强, 视觉表征学习, 分辨率归纳偏置, 细粒度识别, 全局语义识别

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25744v1) | [下载PDF](https://arxiv.org/pdf/2603.25744v1.pdf)

---

## [12. Vega: Learning to Drive with Natural Language Instructions](https://arxiv.org/abs/2603.25741v1)

**作者**：Sicheng Zuo, Yuxuan Li, Wenzhao Zheng 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-03-26

### 📄 论文摘要

Vision-language-action models have reshaped autonomous driving to incorporate languages into the decision-making process. However, most existing pipelines only utilize the language modality for scene descriptions or reasoning and lack the flexibility to follow diverse user instructions for personalized driving. To address this, we first construct a large-scale driving dataset (InstructScene) containing around 100,000 scenes annotated with diverse driving instructions with the corresponding trajectories. We then propose a unified Vision-Language-World-Action model, Vega, for instruction-based generation and planning. We employ the autoregressive paradigm to process visual inputs (vision) and language instructions (language) and the diffusion paradigm to generate future predictions (world modeling) and trajectories (action). We perform joint attention to enable interactions between the modalities and use individual projection layers for different modalities for more capabilities. Extensive experiments demonstrate that our method not only achieves superior planning performance but also exhibits strong instruction-following abilities, paving the way for more intelligent and personalized driving systems.

### 🤖 AI 总结

**一句话总结**：Vega 通过构建大规模指令驾驶数据集并设计统一的视觉-语言-世界-动作模型，实现可按自然语言指令进行预测与规划的个性化自动驾驶。

**研究动机**：现有视觉-语言-动作驾驶方法多将语言用于描述/推理，难以灵活执行多样化用户驾驶指令，限制了个性化与可控性。为此需要同时具备高质量指令-轨迹监督与能融合多模态进行规划的统一模型。

**核心方法**：作者构建 InstructScene 数据集（约10万场景），为每个场景提供多样驾驶指令及对应轨迹。提出 Vega：用自回归范式编码视觉与语言，并用扩散范式生成未来世界预测与轨迹（动作），通过联合注意力实现多模态交互，并为不同模态设置独立投影层提升表达能力。

**主要结论**：实验表明 Vega 在规划性能上优于基线，同时具备更强的指令跟随能力，证明了“大规模指令数据+统一多模态生成规划框架”可有效推动更智能、个性化的自动驾驶系统。

**关键词**：自动驾驶规划, 自然语言指令驾驶, 指令跟随, 视觉-语言-动作模型, 世界模型, 扩散轨迹生成, 自回归建模, 多模态联合注意力, 驾驶指令数据集, 轨迹预测

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25741v1) | [下载PDF](https://arxiv.org/pdf/2603.25741v1.pdf)

---

## [13. PSDesigner: Automated Graphic Design with a Human-Like Creative Workflow](https://arxiv.org/abs/2603.25738v1)

**作者**：Xincheng Shuai, Song Tang, Yutong Huang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Graphic design is a creative and innovative process that plays a crucial role in applications such as e-commerce and advertising. However, developing an automated design system that can faithfully translate user intentions into editable design files remains an open challenge. Although recent studies have leveraged powerful text-to-image models and MLLMs to assist graphic design, they typically simplify professional workflows, resulting in limited flexibility and intuitiveness. To address these limitations, we propose PSDesigner, an automated graphic design system that emulates the creative workflow of human designers. Building upon multiple specialized components, PSDesigner collects theme-related assets based on user instructions, and autonomously infers and executes tool calls to manipulate design files, such as integrating new assets or refining inferior elements. To endow the system with strong tool-use capabilities, we construct a design dataset, CreativePSD, which contains a large amount of high-quality PSD design files annotated with operation traces across a wide range of design scenarios and artistic styles, enabling models to learn expert design procedures. Extensive experiments demonstrate that PSDesigner outperforms existing methods across diverse graphic design tasks, empowering non-specialists to conveniently create production-quality designs.

### 🤖 AI 总结

**一句话总结**：PSDesigner 通过模拟人类设计师的创作流程与工具调用，实现从用户意图到可编辑PSD文件的自动化高质量平面设计生成。

**研究动机**：现有基于文生图与MLLM的设计辅助方法往往简化专业工作流，难以将用户意图可靠地转化为可编辑、可迭代的设计文件，导致灵活性与直觉性不足。

**核心方法**：提出由多个专用组件组成的PSDesigner：先按主题指令自动收集相关素材，再自主推理并执行工具调用来操作PSD（如插入新元素、调整布局与精修低质元素）。为强化工具使用能力，构建CreativePSD数据集，包含高质量PSD及跨场景/风格的操作轨迹标注，用于学习专家级设计步骤。

**主要结论**：实验表明PSDesigner在多种平面设计任务上优于现有方法，能让非专业用户更便捷地产出接近生产级质量、且可编辑的设计成果。

**关键词**：自动化平面设计, 可编辑设计文件, PSD 文件编辑, 创意工作流建模, 多模态大语言模型, 文生图模型, 设计资产检索, 操作轨迹学习, 电商广告设计

**评分**：52

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25738v1) | [下载PDF](https://arxiv.org/pdf/2603.25738v1.pdf)

---

## [14. MegaFlow: Zero-Shot Large Displacement Optical Flow](https://arxiv.org/abs/2603.25739v1)

**作者**：Dingxi Zhang, Fangjinhua Wang, Marc Pollefeys 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Accurate estimation of large displacement optical flow remains a critical challenge. Existing methods typically rely on iterative local search or/and domain-specific fine-tuning, which severely limits their performance in large displacement and zero-shot generalization scenarios. To overcome this, we introduce MegaFlow, a simple yet powerful model for zero-shot large displacement optical flow. Rather than relying on highly complex, task-specific architectural designs, MegaFlow adapts powerful pre-trained vision priors to produce temporally consistent motion fields. In particular, we formulate flow estimation as a global matching problem by leveraging pre-trained global Vision Transformer features, which naturally capture large displacements. This is followed by a few lightweight iterative refinements to further improve the sub-pixel accuracy. Extensive experiments demonstrate that MegaFlow achieves state-of-the-art zero-shot performance across multiple optical flow benchmarks. Moreover, our model also delivers highly competitive zero-shot performance on long-range point tracking benchmarks, demonstrating its robust transferability and suggesting a unified paradigm for generalizable motion estimation. Our project page is at: https://kristen-z.github.io/projects/megaflow.

### 🤖 AI 总结

**一句话总结**：MegaFlow利用预训练ViT的全局特征做全局匹配并辅以轻量迭代细化，实现无需微调的零样本大位移光流估计并取得SOTA表现。

**研究动机**：现有大位移光流方法常依赖迭代局部搜索和/或特定领域微调，导致在超大位移与零样本泛化场景下性能受限。作者希望用更通用的视觉先验，在不依赖复杂任务特化设计的前提下提升大位移与跨数据集泛化能力。

**核心方法**：将光流估计建模为全局匹配问题，利用预训练的全局Vision Transformer特征天然覆盖大位移对应关系；随后通过少量轻量级迭代refinement提升亚像素精度并增强时间一致的运动场输出。

**主要结论**：实验表明MegaFlow在多个光流基准上取得零样本SOTA，并在长程点跟踪任务上也表现强劲，显示出良好的可迁移性与潜在的统一泛化运动估计范式。

**关键词**：大位移光流估计, 零样本光流, 光流全局匹配, 预训练视觉先验, 时序一致性, 迭代细化, 亚像素精度, 长程点跟踪, 跨数据集泛化, 运动估计统一范式

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25739v1) | [下载PDF](https://arxiv.org/pdf/2603.25739v1.pdf)

---

## [15. Unleashing Guidance Without Classifiers for Human-Object Interaction Animation](https://arxiv.org/abs/2603.25734v1)

**作者**：Ziyin Wang, Sirui Xu, Chuan Guo 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Generating realistic human-object interaction (HOI) animations remains challenging because it requires jointly modeling dynamic human actions and diverse object geometries. Prior diffusion-based approaches often rely on hand-crafted contact priors or human-imposed kinematic constraints to improve contact quality. We propose LIGHT, a data-driven alternative in which guidance emerges from the denoising pace itself, reducing dependence on manually designed priors. Building on diffusion forcing, we factor the representation into modality-specific components and assign individualized noise levels with asynchronous denoising schedules. In this paradigm, cleaner components guide noisier ones through cross-attention, yielding guidance without auxiliary classifiers. We find that this data-driven guidance is inherently contact-aware, and can be enhanced when training is augmented with a broad spectrum of synthetic object geometries, encouraging invariance of contact semantics to geometric diversity. Extensive experiments show that pace-induced guidance more effectively mirrors the benefits of contact priors than conventional classifier-free guidance, while achieving higher contact fidelity, more realistic HOI generation, and stronger generalization to unseen objects and tasks.

### 🤖 AI 总结

**一句话总结**：提出LIGHT：通过“异步去噪节奏”让更干净的模态在扩散过程中引导更嘈杂的模态，实现无需分类器/手工接触先验的高保真HOI动画生成。

**研究动机**：现有HOI扩散生成往往依赖手工接触先验或运动学约束来保证接触质量，设计成本高且泛化到新物体/新任务时不稳；作者希望用纯数据驱动的方式自动学出“接触感知”的引导机制。

**核心方法**：基于diffusion forcing将表示分解为模态特定组件（如人体动作/物体几何等），为不同组件分配不同噪声强度并采用异步去噪日程；在去噪过程中，较“干净”的组件通过cross-attention引导较“噪”的组件，从而形成无分类器的内生guidance；训练时加入大量合成几何多样的物体以增强接触语义对几何变化的不变性。

**主要结论**：节奏诱导的guidance天然具备接触感知能力，效果比传统classifier-free guidance更接近甚至优于手工接触先验的收益；实验显示其接触保真度与HOI真实感更高，并在未见物体与任务上具有更强泛化。

**关键词**：人-物交互动画生成, 扩散模型生成, 无分类器引导, 节奏诱导引导, 异步去噪调度, 模态分解表示, 噪声级别分配, 交叉注意力引导, 接触感知建模, 合成物体几何增强, 未见物体泛化

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25734v1) | [下载PDF](https://arxiv.org/pdf/2603.25734v1.pdf)

---

## [16. BizGenEval: A Systematic Benchmark for Commercial Visual Content Generation](https://arxiv.org/abs/2603.25732v1)

**作者**：Yan Li, Zezi Zeng, Ziwei Zhou 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Recent advances in image generation models have expanded their applications beyond aesthetic imagery toward practical visual content creation. However, existing benchmarks mainly focus on natural image synthesis and fail to systematically evaluate models under the structured and multi-constraint requirements of real-world commercial design tasks. In this work, we introduce BizGenEval, a systematic benchmark for commercial visual content generation. The benchmark spans five representative document types: slides, charts, webpages, posters, and scientific figures, and evaluates four key capability dimensions: text rendering, layout control, attribute binding, and knowledge-based reasoning, forming 20 diverse evaluation tasks. BizGenEval contains 400 carefully curated prompts and 8000 human-verified checklist questions to rigorously assess whether generated images satisfy complex visual and semantic constraints. We conduct large-scale benchmarking on 26 popular image generation systems, including state-of-the-art commercial APIs and leading open-source models. The results reveal substantial capability gaps between current generative models and the requirements of professional visual content creation. We hope BizGenEval serves as a standardized benchmark for real-world commercial visual content generation.

### 🤖 AI 总结

**一句话总结**：BizGenEval 提出一个面向商业视觉内容生成的系统化基准，用于评测图像生成模型在多约束设计任务中的真实能力差距。

**研究动机**：现有图像生成评测多聚焦自然图像与美学效果，难以覆盖商业设计中对文本、版式、属性绑定与知识推理等结构化约束的要求，因此需要更贴近实际工作流的统一基准。

**核心方法**：构建覆盖幻灯片、图表、网页、海报、科研图五类文档的基准，从文本渲染、布局控制、属性绑定、知识推理四个维度形成20项任务；提供400条精心策划的提示词与8000条人工核验清单问题，并对26个主流商用API与开源模型进行大规模对比评测。

**主要结论**：评测显示当前主流生成模型在满足商业设计的复杂视觉与语义约束方面仍存在显著能力缺口，距离专业级视觉内容创作需求有较大差距；BizGenEval可作为标准化评测工具推动该方向改进。

**关键词**：商业视觉内容生成, 图像生成评测基准, 结构化设计约束, 多约束提示评测, 文本渲染, 版式控制, 属性绑定, 知识推理, 文档类图像生成, 人工核验清单评测

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25732v1) | [下载PDF](https://arxiv.org/pdf/2603.25732v1.pdf)

---

## [17. PixelSmile: Toward Fine-Grained Facial Expression Editing](https://arxiv.org/abs/2603.25728v1)

**作者**：Jiabin Hua, Hengyuan Xu, Aojie Li 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-26

### 📄 论文摘要

Fine-grained facial expression editing has long been limited by intrinsic semantic overlap. To address this, we construct the Flex Facial Expression (FFE) dataset with continuous affective annotations and establish FFE-Bench to evaluate structural confusion, editing accuracy, linear controllability, and the trade-off between expression editing and identity preservation. We propose PixelSmile, a diffusion framework that disentangles expression semantics via fully symmetric joint training. PixelSmile combines intensity supervision with contrastive learning to produce stronger and more distinguishable expressions, achieving precise and stable linear expression control through textual latent interpolation. Extensive experiments demonstrate that PixelSmile achieves superior disentanglement and robust identity preservation, confirming its effectiveness for continuous, controllable, and fine-grained expression editing, while naturally supporting smooth expression blending.

### 🤖 AI 总结

**一句话总结**：PixelSmile 通过对扩散模型进行对称联合训练并结合强度监督与对比学习，实现了可线性控制、细粒度且兼顾身份保持的连续表情编辑。

**研究动机**：现有细粒度表情编辑受限于表情语义天然重叠，导致结构混淆、编辑不准或难以连续可控。为此作者构建带连续情感标注的FFE数据集与FFE-Bench，以系统评估编辑准确性、可控性与身份保持的权衡。

**核心方法**：提出PixelSmile扩散框架，通过“完全对称”的联合训练来解耦表情语义，并引入表情强度监督与对比学习以增强不同表情之间的可分性与强表达性。编辑时利用文本潜空间插值实现稳定的线性强度控制，并天然支持平滑的表情混合。

**主要结论**：在FFE-Bench等实验中，PixelSmile在表情解耦、编辑精度与线性可控性上优于对比方法，同时保持更鲁棒的身份一致性。结果表明其适用于连续、可控、细粒度的表情编辑，并能实现平滑过渡与混合。

**关键词**：面部表情编辑, 细粒度编辑, Diffusion, 表情语义解耦, 连续情感标注, 表情编辑基准, 身份保持, 线性可控性, 文本潜空间插值, 强度监督, 表情混合

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25728v1) | [下载PDF](https://arxiv.org/pdf/2603.25728v1.pdf)

---

## [18. AnyHand: A Large-Scale Synthetic Dataset for RGB(-D) Hand Pose Estimation](https://arxiv.org/abs/2603.25726v1)

**作者**：Chen Si, Yulin Liu, Bo Ai 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

We present AnyHand, a large-scale synthetic dataset designed to advance the state of the art in 3D hand pose estimation from both RGB-only and RGB-D inputs. While recent works with foundation approaches have shown that an increase in the quantity and diversity of training data can markedly improve performance and robustness in hand pose estimation, existing real-world-collected datasets on this task are limited in coverage, and prior synthetic datasets rarely provide occlusions, arm details, and aligned depth together at scale. To address this bottleneck, our AnyHand contains 2.5M single-hand and 4.1M hand-object interaction RGB-D images, with rich geometric annotations. In the RGB-only setting, we show that extending the original training sets of existing baselines with AnyHand yields significant gains on multiple benchmarks (FreiHAND and HO-3D), even when keeping the architecture and training scheme fixed. More impressively, the model trained with AnyHand shows stronger generalization to the out-of-domain HO-Cap dataset, without any fine-tuning. We also contribute a lightweight depth fusion module that can be easily integrated into existing RGB-based models. Trained with AnyHand, the resulting RGB-D model achieves superior performance on the HO-3D benchmark, showing the benefits of depth integration and the effectiveness of our synthetic data.

### 🤖 AI 总结

**一句话总结**：提出大规模合成数据集AnyHand（含RGB与对齐RGB-D）以提升3D手部姿态估计在RGB与RGB-D场景下的性能与泛化。

**研究动机**：真实采集的手部姿态数据集覆盖不足，现有合成数据集也很少在大规模下同时提供遮挡、手臂细节与对齐深度，限制了模型在复杂场景（尤其手-物交互）中的鲁棒性与泛化。

**核心方法**：构建AnyHand：包含250万单手与410万手-物交互的RGB-D图像，并提供丰富几何标注；同时提出可轻量集成到RGB模型中的深度融合模块，用于将深度信息有效注入现有网络。

**主要结论**：在不改变基线架构与训练策略的情况下，用AnyHand扩充训练可显著提升FreiHAND与HO-3D等基准表现，并在HO-Cap等域外数据上无需微调仍具更强泛化；结合深度融合模块的RGB-D模型在HO-3D上进一步取得更优结果，验证了合成对齐深度与数据规模多样性的价值。

**关键词**：3D手部姿态估计, RGB-D手部姿态估计, 合成数据集, 手-物交互, 几何标注, 遮挡建模, 深度对齐, 深度融合模块, 域外泛化, HO-3D基准

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25726v1) | [下载PDF](https://arxiv.org/pdf/2603.25726v1.pdf)

---

## [19. No Hard Negatives Required: Concept Centric Learning Leads to Compositionality without Degrading Zero-shot Capabilities of Contrastive Models](https://arxiv.org/abs/2603.25722v1)

**作者**：Hai X. Pham, David T. Hoffmann, Ricardo Guerrero 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

Contrastive vision-language (V&L) models remain a popular choice for various applications. However, several limitations have emerged, most notably the limited ability of V&L models to learn compositional representations. Prior methods often addressed this limitation by generating custom training data to obtain hard negative samples. Hard negatives have been shown to improve performance on compositionality tasks, but are often specific to a single benchmark, do not generalize, and can cause substantial degradation of basic V&L capabilities such as zero-shot or retrieval performance, rendering them impractical. In this work we follow a different approach. We identify two root causes that limit compositionality performance of V&Ls: 1) Long training captions do not require a compositional representation; and 2) The final global pooling in the text and image encoders lead to a complete loss of the necessary information to learn binding in the first place. As a remedy, we propose two simple solutions: 1) We obtain short concept centric caption parts using standard NLP software and align those with the image; and 2) We introduce a parameter-free cross-modal attention-pooling to obtain concept centric visual embeddings from the image encoder. With these two changes and simple auxiliary contrastive losses, we obtain SOTA performance on standard compositionality benchmarks, while maintaining or improving strong zero-shot and retrieval capabilities. This is achieved without increasing inference cost. We release the code for this work at https://github.com/SamsungLabs/concept_centric_clip.

### 🤖 AI 总结

**一句话总结**：提出一种无需硬负样本的“概念中心”对比学习训练策略，在不牺牲（甚至提升）零样本与检索能力的前提下显著增强视觉-语言模型的组合性表示。

**研究动机**：以硬负样本提升组合性的方法通常依赖特定数据构造、难以泛化，并会明显损害CLIP类模型的零样本/检索等基础能力；作者认为组合性不足的根因来自训练文本过长与全局池化导致绑定信息丢失。

**核心方法**：将长caption用标准NLP工具切分为更短的“概念片段”并与图像对齐训练，同时在视觉侧引入无参数的跨模态注意力池化生成概念中心的视觉嵌入；配合简单的辅助对比损失以强化概念级对齐与绑定学习。

**主要结论**：在标准组合性评测上取得SOTA，同时保持或提升零样本分类与图文检索表现；且不增加推理成本，证明通过概念中心表征与更合适的池化可替代硬负样本带来的收益。

**关键词**：视觉-语言对比学习, 组合性表征, 概念中心学习, 无硬负样本训练, 短概念字幕切分, 跨模态注意力池化, 概念中心视觉嵌入, 全局池化信息丢失, 绑定学习, 零样本能力保持, 图文检索性能

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25722v1) | [下载PDF](https://arxiv.org/pdf/2603.25722v1.pdf)

---

## [20. TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)

**作者**：Quynh Phung, Long Mai, Cusuh Ham 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

We study object motion path editing in videos, where the goal is to alter a target object's trajectory while preserving the original scene content. Unlike prior video editing methods that primarily manipulate appearance or rely on point-track-based trajectory control, which is often challenging for users to provide during inference, especially in videos with camera motion, we offer a practical, easy-to-use approach to controllable object-centric motion editing. We present Trace, a framework that enables users to design the desired trajectory in a single anchor frame and then synthesizes a temporally consistent edited video. Our approach addresses this task with a two-stage pipeline: a cross-view motion transformation module that maps first-frame path design to frame-aligned box trajectories under camera motion, and a motion-conditioned video re-synthesis module that follows these trajectories to regenerate the object while preserving the remaining content of the input video. Experiments on diverse real-world videos show that our method produces more coherent, realistic, and controllable motion edits than recent image-to-video and video-to-video methods.

### 🤖 AI 总结

**一句话总结**：TRACE 允许用户在视频第一帧上画出目标物体的期望运动路径，并在存在相机运动的情况下生成时序一致、场景保持的运动编辑视频。

**研究动机**：现有视频编辑多偏向外观操控或依赖点轨迹（point tracks）作为运动控制信号，推理时对用户输入要求高且在相机运动场景下更难用。作者希望提供一种更直观的“在单帧设计轨迹即可”的对象级运动编辑方式，同时尽量保留原视频其他内容不变。

**核心方法**：两阶段流程：首先用跨视角运动变换模块将第一帧的路径设计映射为考虑相机运动的逐帧对齐盒轨迹（box trajectories）；随后用运动条件的视频再合成模块沿这些轨迹重生成目标物体，并保持背景与非目标区域的时空一致性。

**主要结论**：在多样真实视频实验中，TRACE 相比近期 image-to-video 与 video-to-video 方法能产生更连贯、更真实且更可控的对象运动编辑结果，尤其在包含相机运动时表现更稳定。

**关键词**：视频目标运动编辑, 轨迹引导视频编辑, 首帧轨迹设计, 相机运动补偿, 跨视角运动变换, 边界框轨迹, 时序一致性, 运动条件视频生成, 视频重合成, 视频到视频编辑

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25707v1) | [下载PDF](https://arxiv.org/pdf/2603.25707v1.pdf)

---

## [21. Wan-Weaver: Interleaved Multi-modal Generation via Decoupled Training](https://arxiv.org/abs/2603.25706v1)

**作者**：Jinbo Xing, Zeyinzi Jiang, Yuxiang Tuo 等 18 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Recent unified models have made unprecedented progress in both understanding and generation. However, while most of them accept multi-modal inputs, they typically produce only single-modality outputs. This challenge of producing interleaved content is mainly due to training data scarcity and the difficulty of modeling long-range cross-modal context. To address this issue, we decompose interleaved generation into textual planning and visual consistency modeling, and introduce a framework consisting of a planner and a visualizer. The planner produces dense textual descriptions for visual content, while the visualizer synthesizes images accordingly. Under this guidance, we construct large-scale textual-proxy interleaved data (where visual content is represented in text) to train the planner, and curate reference-guided image data to train the visualizer. These designs give rise to Wan-Weaver, which exhibits emergent interleaved generation ability with long-range textual coherence and visual consistency. Meanwhile, the integration of diverse understanding and generation data into planner training enables Wan-Weaver to achieve robust task reasoning and generation proficiency. To assess the model's capability in interleaved generation, we further construct a benchmark that spans a wide range of use cases across multiple dimensions. Extensive experiments demonstrate that, even without access to any real interleaved data, Wan-Weaver achieves superior performance over existing methods.

### 🤖 AI 总结

**一句话总结**：Wan-Weaver 通过“文本规划 + 图像一致性建模”的解耦训练，在无需真实图文交错数据的情况下实现了长程连贯且视觉一致的多模态交错生成。

**研究动机**：现有统一多模态模型多能接收多模态输入，但通常只能输出单一模态；交错输出受限于真实交错训练数据稀缺与长距离跨模态上下文难以建模。

**核心方法**：将交错生成分解为两部分：Planner 负责生成对视觉内容的密集文本规划（用文本代理视觉内容）并用大规模“文本代理交错数据”训练；Visualizer 在参考引导的图像数据上训练以根据规划合成图像并保持视觉一致性。

**主要结论**：实验与新构建的交错生成基准表明：即便不使用真实交错数据，Wan-Weaver 仍在交错生成质量（文本连贯与视觉一致）上优于现有方法，并因融合多类理解/生成数据而具备更强的推理与生成鲁棒性。

**关键词**：多模态交错生成, 解耦训练, 文本规划, 视觉一致性建模, 规划器-可视化器架构, 文本代理数据, 参考引导图像生成, 长程跨模态上下文, 交错生成基准评测, 统一多模态模型

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25706v1) | [下载PDF](https://arxiv.org/pdf/2603.25706v1.pdf)

---

## [22. LEMMA: Laplacian pyramids for Efficient Marine SeMAntic Segmentation](https://arxiv.org/abs/2603.25689v1)

**作者**：Ishaan Gakhar, Laven Srivastava, Sankarshanaa Sagaram 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-26

### 📄 论文摘要

Semantic segmentation in marine environments is crucial for the autonomous navigation of unmanned surface vessels (USVs) and coastal Earth Observation events such as oil spills. However, existing methods, often relying on deep CNNs and transformer-based architectures, face challenges in deployment due to their high computational costs and resource-intensive nature. These limitations hinder the practicality of real-time, low-cost applications in real-world marine settings.   To address this, we propose LEMMA, a lightweight semantic segmentation model designed specifically for accurate remote sensing segmentation under resource constraints. The proposed architecture leverages Laplacian Pyramids to enhance edge recognition, a critical component for effective feature extraction in complex marine environments for disaster response, environmental surveillance, and coastal monitoring. By integrating edge information early in the feature extraction process, LEMMA eliminates the need for computationally expensive feature map computations in deeper network layers, drastically reducing model size, complexity and inference time. LEMMA demonstrates state-of-the-art performance across datasets captured from diverse platforms while reducing trainable parameters and computational requirements by up to 71x, GFLOPs by up to 88.5\%, and inference time by up to 84.65\%, as compared to existing models. Experimental results highlight its effectiveness and real-world applicability, including 93.42\% IoU on the Oil Spill dataset and 98.97\% mIoU on Mastr1325.

### 🤖 AI 总结

**一句话总结**：LEMMA 通过在轻量级语义分割网络中引入拉普拉斯金字塔进行早期边缘增强，在海洋遥感场景下实现了高精度且显著降算力的实时分割。

**研究动机**：海洋环境语义分割对无人船自主航行与溢油等海岸监测至关重要，但现有深层CNN/Transformer模型计算与资源开销大，难以在低成本、实时的实际部署条件下使用。

**核心方法**：提出轻量模型 LEMMA，利用拉普拉斯金字塔提取并强化边缘信息，并将其在特征提取早期融合，从而减少对深层昂贵特征图计算的依赖，降低参数量、复杂度与推理时间。

**主要结论**：LEMMA 在多平台数据集上达到SOTA或接近SOTA效果，同时相较现有模型最多实现参数/计算量降低约71倍、GFLOPs降低88.5%、推理时间降低84.65%，并在 Oil Spill 数据集获得93.42% IoU、在 Mastr1325 获得98.97% mIoU，体现出较强的工程可用性。

**关键词**：海洋语义分割, 轻量化分割模型, 遥感图像分割, 拉普拉斯金字塔, 边缘感知特征, 资源受限部署, 实时推理, 低算力计算机视觉, 无人水面艇导航, 溢油检测, 海岸监测, 参数效率优化

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25689v1) | [下载PDF](https://arxiv.org/pdf/2603.25689v1.pdf)

---

## [23. Just Zoom In: Cross-View Geo-Localization via Autoregressive Zooming](https://arxiv.org/abs/2603.25686v1)

**作者**：Yunus Talha Erzurumlu, Jiyong Kwag, Alper Yilmaz  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-26

### 📄 论文摘要

Cross-view geo-localization (CVGL) estimates a camera's location by matching a street-view image to geo-referenced overhead imagery, enabling GPS-denied localization and navigation. Existing methods almost universally formulate CVGL as an image-retrieval problem in a contrastively trained embedding space. This ties performance to large batches and hard negative mining, and it ignores both the geometric structure of maps and the coverage mismatch between street-view and overhead imagery. In particular, salient landmarks visible from the street view can fall outside a fixed satellite crop, making retrieval targets ambiguous and limiting explicit spatial inference over the map. We propose Just Zoom In, an alternative formulation that performs CVGL via autoregressive zooming over a city-scale overhead map. Starting from a coarse satellite view, the model takes a short sequence of zoom-in decisions to select a terminal satellite cell at a target resolution, without contrastive losses or hard negative mining. We further introduce a realistic benchmark with crowd-sourced street views and high-resolution satellite imagery that reflects real capture conditions. On this benchmark, Just Zoom In achieves state-of-the-art performance, improving Recall@1 within 50 m by 5.5% and Recall@1 within 100 m by 9.6% over the strongest contrastive-retrieval baseline. These results demonstrate the effectiveness of sequential coarse-to-fine spatial reasoning for cross-view geo-localization.

### 🤖 AI 总结

**一句话总结**：提出“Just Zoom In”用自回归的逐步放大决策在城市级卫星地图上进行粗到细定位，避免对比学习检索范式并取得更高召回率。

**研究动机**：传统CVGL几乎都做成对比学习的图像检索，依赖大batch与难负样本且忽略地图几何结构；同时固定大小卫星裁剪会与街景可见地标产生覆盖不匹配，导致目标歧义与难以显式空间推理。

**核心方法**：将定位改写为在整幅城市级开销地图上的“序列决策”问题：从粗分辨率开始，模型自回归地做若干次zoom-in选择，逐级缩小到最终目标分辨率的卫星网格单元；训练不需要对比损失或hard negative mining，并引入更贴近真实采集条件的街景+高分卫星新基准。

**主要结论**：在新基准上方法达到SOTA，相比最强对比检索基线Recall@1提升（50m内+5.5%、100m内+9.6%），表明顺序式的粗到细空间推理能更有效解决跨视角地理定位中的覆盖不匹配与歧义问题。

**关键词**：跨视角地理定位, 街景-卫星图匹配, GPS拒止定位, 自回归缩放, 序列决策, 粗到细空间推理, 城市尺度地图检索, 卫星图分层网格, 无硬负样本挖掘, 真实街景-高分卫星基准

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25686v1) | [下载PDF](https://arxiv.org/pdf/2603.25686v1.pdf)

---

## [24. LanteRn: Latent Visual Structured Reasoning](https://arxiv.org/abs/2603.25629v1)

**作者**：André G. Viveiros, Nuno Gonçalves, Matthias Lindemann 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

While language reasoning models excel in many tasks, visual reasoning remains challenging for current large multimodal models (LMMs). As a result, most LMMs default to verbalizing perceptual content into text, a strong limitation for tasks requiring fine-grained spatial and visual understanding. While recent approaches take steps toward thinking with images by invoking tools or generating intermediate images, they either rely on external modules, or incur unnecessary computation by reasoning directly in pixel space. In this paper, we introduce LanteRn, a framework that enables LMMs to interleave language with compact latent visual representations, allowing visual reasoning to occur directly in latent space. LanteRn augments a vision-language transformer with the ability to generate and attend to continuous visual thought embeddings during inference. We train the model in two stages: supervised fine-tuning to ground visual features in latent states, followed by reinforcement learning to align latent reasoning with task-level utility. We evaluate LanteRn on three perception-centric benchmarks (VisCoT, V*, and Blink), observing consistent improvements in visual grounding and fine-grained reasoning. These results suggest that internal latent representations provide a promising direction for more efficient multimodal reasoning.

### 🤖 AI 总结

**一句话总结**：LanteRn 让大模型在推理时将语言与紧凑的“视觉潜变量思维”交错使用，从而在潜空间中进行更高效、更细粒度的视觉结构化推理。

**研究动机**：现有多模态模型常把视觉内容先“翻译”成文本来推理，导致空间与细节理解受限；而直接在像素空间推理或依赖外部工具又带来额外计算与模块复杂度。

**核心方法**：在视觉-语言Transformer中引入可生成、可被注意力读取的连续视觉思维嵌入（latent visual thought embeddings），使模型能在推理过程中直接操作潜表示而非像素。训练采用两阶段：先用监督微调将视觉特征扎根到潜状态，再用强化学习将潜空间推理与任务效用对齐。

**主要结论**：在VisCoT、V*与Blink三类感知导向基准上，LanteRn 在视觉对齐与细粒度推理上取得稳定提升，表明“内部潜表示推理”是更高效多模态推理的有前景方向。

**关键词**：多模态大模型, 视觉推理, 潜在空间推理, 潜在视觉表征, 连续视觉思维嵌入, 视觉特征对齐, 监督微调, 强化学习对齐, 视觉定位

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25629v1) | [下载PDF](https://arxiv.org/pdf/2603.25629v1.pdf)

---

## cs.LG

## [25. Neural Network Conversion of Machine Learning Pipelines](https://arxiv.org/abs/2603.25699v1)

**作者**：Man-Ling Sung, Jan Silovsky, Man-Hung Siu 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-26

### 📄 论文摘要

Transfer learning and knowledge distillation has recently gained a lot of attention in the deep learning community. One transfer approach, the student-teacher learning, has been shown to successfully create ``small'' student neural networks that mimic the performance of a much bigger and more complex ``teacher'' networks. In this paper, we investigate an extension to this approach and transfer from a non-neural-based machine learning pipeline as teacher to a neural network (NN) student, which would allow for joint optimization of the various pipeline components and a single unified inference engine for multiple ML tasks. In particular, we explore replacing the random forest classifier by transfer learning to a student NN. We experimented with various NN topologies on 100 OpenML tasks in which random forest has been one of the best solutions. Our results show that for the majority of the tasks, the student NN can indeed mimic the teacher if one can select the right NN hyper-parameters. We also investigated the use of random forest for selecting the right NN hyper-parameters.

### 🤖 AI 总结

**一句话总结**：论文提出将传统机器学习流水线（以随机森林为代表）作为“教师”，通过蒸馏/迁移学习训练神经网络“学生”以在多数任务上复现其性能。

**研究动机**：非神经网络的ML流水线通常由多个组件组成、难以端到端联合优化且推理引擎分散；若能转为单一神经网络，可实现统一推理与联合优化并可能降低部署复杂度。

**核心方法**：以随机森林分类器为教师模型，在100个OpenML任务上训练不同拓扑与超参数的学生神经网络去拟合教师输出/行为，并探索用随机森林来帮助选择合适的神经网络超参数。

**主要结论**：在多数OpenML任务上，只要超参数选得合适，学生神经网络能够较好地模仿随机森林教师的效果；同时随机森林可用于指导或筛选有效的神经网络超参数配置。

**关键词**：知识蒸馏, 学生-教师学习, 模型压缩, 机器学习流水线转换, 非神经模型迁移, 随机森林蒸馏, 表格分类, 神经网络拓扑搜索, 超参数选择

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25699v1) | [下载PDF](https://arxiv.org/pdf/2603.25699v1.pdf)

---

## [26. A Unified Memory Perspective for Probabilistic Trustworthy AI](https://arxiv.org/abs/2603.25692v1)

**作者**：Xueji Zhao, Likai Pei, Jianbo Liu 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.AR, cs.ET  
**发布时间**：2026-03-26

### 📄 论文摘要

Trustworthy artificial intelligence increasingly relies on probabilistic computation to achieve robustness, interpretability, security and privacy. In practical systems, such workloads interleave deterministic data access with repeated stochastic sampling across models, data paths and system functions, shifting performance bottlenecks from arithmetic units to memory systems that must deliver both data and randomness. Here we present a unified data-access perspective in which deterministic access is treated as a limiting case of stochastic sampling, enabling both modes to be analyzed within a common framework. This view reveals that increasing stochastic demand reduces effective data-access efficiency and can drive systems into entropy-limited operation. Based on this insight, we define memory-level evaluation criteria, including unified operation, distribution programmability, efficiency, robustness to hardware non-idealities and parallel compatibility. Using these criteria, we analyze limitations of conventional architectures and examine emerging probabilistic compute-in-memory approaches that integrate sampling with memory access, outlining pathways toward scalable hardware for trustworthy AI.

### 🤖 AI 总结

**一句话总结**：论文提出把确定性内存访问视为随机采样的极限情形，用统一框架分析“数据+随机性”的内存瓶颈，并给出评估指标与概率型存内计算的硬件路径。

**研究动机**：可信AI越来越依赖概率计算（采样）以获得鲁棒性/可解释性/安全与隐私，但实际系统中确定性访存与反复随机采样交织，使性能瓶颈从算力转向必须同时提供数据与熵源的内存系统。

**核心方法**：作者提出统一的数据访问视角：将确定性访问纳入随机采样框架，从而量化随机需求如何降低有效访存效率并可能进入“熵受限”工作区；据此定义内存级评估准则（统一操作、分布可编程性、效率、对非理想的鲁棒性、并行兼容性），并对传统架构与新兴概率存内计算进行对比分析。

**主要结论**：随着随机采样强度提升，系统有效数据访问效率下降并可能受限于可用熵/随机性供给；传统架构在上述准则下存在结构性限制，而将采样与访存融合的概率Compute-in-Memory有望成为可扩展可信AI硬件的重要方向。

**关键词**：可信AI, 概率计算, 随机采样, 统一数据访问框架, 内存瓶颈, 熵受限运行, 内存级评测指标, 分布可编程性, 概率存内计算, 随机性供给, 硬件非理想鲁棒性

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25692v1) | [下载PDF](https://arxiv.org/pdf/2603.25692v1.pdf)

---

## [27. On Neural Scaling Laws for Weather Emulation through Continual Training](https://arxiv.org/abs/2603.25687v1)

**作者**：Shashank Subramanian, Alexander Kiefer, Arnur Nigmetov 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

Neural scaling laws, which in some domains can predict the performance of large neural networks as a function of model, data, and compute scale, are the cornerstone of building foundation models in Natural Language Processing and Computer Vision. We study neural scaling in Scientific Machine Learning, focusing on models for weather forecasting. To analyze scaling behavior in as simple a setting as possible, we adopt a minimal, scalable, general-purpose Swin Transformer architecture, and we use continual training with constant learning rates and periodic cooldowns as an efficient training strategy. We show that models trained in this minimalist way follow predictable scaling trends and even outperform standard cosine learning rate schedules. Cooldown phases can be re-purposed to improve downstream performance, e.g., enabling accurate multi-step rollouts over longer forecast horizons as well as sharper predictions through spectral loss adjustments. We also systematically explore a wide range of model and dataset sizes under various compute budgets to construct IsoFLOP curves, and we identify compute-optimal training regimes. Extrapolating these trends to larger scales highlights potential performance limits, demonstrating that neural scaling can serve as an important diagnostic for efficient resource allocation. We open-source our code for reproducibility.

### 🤖 AI 总结

**一句话总结**：本文在天气预报模拟任务中验证了神经网络缩放律：用极简Swin Transformer配合持续训练与冷却策略，可获得可预测的性能随规模提升趋势并实现更高效的算力分配。

**研究动机**：NLP/CV中的缩放律已指导大模型构建，但在科学机器学习（尤其天气预报）中仍缺乏系统刻画；作者希望用尽量简单的设置理解“模型/数据/算力”扩展对性能的影响并寻找算力最优训练方案。

**核心方法**：采用可扩展的通用Swin Transformer作为最小化基线，并使用恒定学习率的持续训练（periodic cooldown冷却阶段）替代常见cosine调度；在多种模型与数据规模、不同算力预算下构建IsoFLOP曲线，分析缩放趋势并外推更大规模的性能上限，同时在冷却阶段加入多步rollout与频谱损失调整以提升下游表现。

**主要结论**：在该极简训练范式下，天气模拟模型呈现稳定可预测的缩放规律，且持续训练+冷却可优于标准cosine学习率；IsoFLOP分析给出了算力最优的训练配比与可预期的性能上限，冷却阶段还能显著改善长时域多步预测与预测清晰度。

**关键词**：神经缩放律, 天气预报模型, 科学机器学习, 持续训练, 恒定学习率, 冷却阶段, 计算最优训练, 多步滚动预测, 频谱损失

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25687v1) | [下载PDF](https://arxiv.org/pdf/2603.25687v1.pdf)

---

## [28. Longitudinal Digital Phenotyping for Early Cognitive-Motor Screening](https://arxiv.org/abs/2603.25673v1)

**作者**：Diego Jimenez-Oviedo, Ruben Vera-Rodriguez, Ruben Tolosana 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-26

### 📄 论文摘要

Early detection of atypical cognitive-motor development is critical for timely intervention, yet traditional assessments rely heavily on subjective, static evaluations. The integration of digital devices offers an opportunity for continuous, objective monitoring through digital biomarkers. In this work, we propose an AI-driven longitudinal framework to model developmental trajectories in children aged 18 months to 8 years. Using a dataset of tablet-based interactions collected over multiple academic years, we analyzed six cognitive-motor tasks (e.g., fine motor control, reaction time). We applied dimensionality reduction (t-SNE) and unsupervised clustering (K-Means++) to identify distinct developmental phenotypes and tracked individual transitions between these profiles over time. Our analysis reveals three distinct profiles: low, medium, and high performance. Crucially, longitudinal tracking highlights a high stability in the low-performance cluster (>90% retention in early years), suggesting that early deficits tend to persist without intervention. Conversely, higher-performance clusters show greater variability, potentially reflecting engagement factors. This study validates the use of unsupervised learning on touchscreen data to uncover heterogeneous developmental paths. The identified profiles serve as scalable, data-driven proxies for cognitive growth, offering a foundation for early screening tools and personalized pediatric interventions.

### 🤖 AI 总结

**一句话总结**：提出一个基于儿童平板触控交互数据的纵向无监督学习框架，识别并追踪不同认知-运动发育表型，用于早期筛查。

**研究动机**：传统儿童发育评估往往主观且静态，难以持续捕捉早期异常轨迹；数字设备可提供连续、客观的数字生物标志物以支持早期干预。

**核心方法**：收集18个月至8岁儿童跨学年的平板交互数据，围绕6类认知-运动任务提取表现指标；用t-SNE降维可视化、K-Means++聚类得到发育表型，并在个体层面纵向追踪其在不同表型间的转移与稳定性。

**主要结论**：发现低/中/高三类表现表型，其中低表现簇在早期具有>90%的高留存率，提示早期缺陷若无干预可能持续；高表现簇更易波动，可能与参与度等因素相关，验证触屏数据+无监督学习可作为可扩展的早筛与个性化干预基础。

**关键词**：数字表型, 纵向监测, 认知-运动发育筛查, 发育轨迹建模, 触屏交互数据, 数字生物标志物, 无监督聚类, 发育表型, 个体转移跟踪

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25673v1) | [下载PDF](https://arxiv.org/pdf/2603.25673v1.pdf)

---

## [29. Uncertainty-Guided Label Rebalancing for CPS Safety Monitoring](https://arxiv.org/abs/2603.25670v1)

**作者**：John Ayotunde, Qinghua Xu, Guancheng Wang 等 4 位作者  
**分类**：cs.LG, cs.SE  
**发布时间**：2026-03-26

### 📄 论文摘要

Safety monitoring is essential for Cyber-Physical Systems (CPSs). However, unsafe events are rare in real-world CPS operations, creating an extreme class imbalance that degrades safety predictors. Standard rebalancing techniques perform poorly on time-series CPS telemetry, either generating unrealistic synthetic samples or overfitting on the minority class. Meanwhile, behavioral uncertainty in CPS operations, defined as the degree of doubt or uncertainty in CPS decisions , is often correlated with safety outcomes but unexplored in safety monitoring. To that end, we propose U-Balance, a supervised approach that leverages behavioral uncertainty to rebalance imbalanced datasets prior to training a safety predictor. U-Balance first trains a GatedMLP-based uncertainty predictor that summarizes each telemetry window into distributional kinematic features and outputs an uncertainty score. It then applies an uncertainty-guided label rebalancing (uLNR) mechanism that probabilistically relabels \textit{safe}-labeled windows with unusually high uncertainty as \textit{unsafe}, thereby enriching the minority class with informative boundary samples without synthesizing new data. Finally, a safety predictor is trained on the rebalanced dataset for safety monitoring. We evaluate U-Balance on a large-scale UAV benchmark with a 46:1 safe-to-unsafe ratio. Results confirm a moderate but significant correlation between behavioral uncertainty and safety. We then identify uLNR as the most effective strategy to exploit uncertainty information, compared to direct early and late fusion. U-Balance achieves a 0.806 F1 score, outperforming the strongest baseline by 14.3 percentage points, while maintaining competitive inference efficiency. Ablation studies confirm that both the GatedMLP-based uncertainty predictor and the uLNR mechanism contribute significantly to U-Balance's effectiveness.

### 🤖 AI 总结

**一句话总结**：提出U-Balance：利用CPS运行中的行为不确定性对严重类别不平衡数据进行“概率重标注”，从而显著提升安全事件预测的F1表现。

**研究动机**：真实CPS中不安全事件极少导致极端类不平衡，传统过采样/合成方法在时序遥测上易生成不真实样本或对少数类过拟合；同时行为不确定性与安全结果相关但在安全监测中尚未被系统利用。

**核心方法**：先训练基于GatedMLP的不确定性预测器，将遥测窗口提炼为分布式运动学特征并输出不确定性分数；再用不确定性引导的标签再平衡（uLNR）对“高不确定但标为安全”的窗口按概率重标为“不安全”，在不生成新数据的情况下补充边界样本，最后在重平衡数据上训练安全预测器。

**主要结论**：在46:1的UAV基准上，行为不确定性与安全性存在中等但显著相关；uLNR比早/晚融合更有效，U-Balance取得0.806 F1，较最强基线提升14.3个百分点且推理效率具竞争力，消融验证不确定性预测器与uLNR均有关键贡献。

**关键词**：信息物理系统安全监控, 类别不平衡学习, 时序遥测数据, 不确定性估计, 行为不确定性, 不确定性引导重采样, 概率重标记, 边界样本挖掘, 运动学分布特征, 无人机安全基准

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25670v1) | [下载PDF](https://arxiv.org/pdf/2603.25670v1.pdf)

---

## [30. Anchored-Branched Steady-state WInd Flow Transformer (AB-SWIFT): a metamodel for 3D atmospheric flow in urban environments](https://arxiv.org/abs/2603.25635v1)

**作者**：Armand de Villeroché, Rem-Sophia Mouradi, Vincent Le Guen 等 8 位作者  
**分类**：cs.LG, physics.ao-ph  
**发布时间**：2026-03-26

### 📄 论文摘要

Air flow modeling at a local scale is essential for applications such as pollutant dispersion modeling or wind farm modeling. To circumvent costly Computational Fluid Dynamics (CFD) computations, deep learning surrogate models have recently emerged as promising alternatives. However, in the context of urban air flow, deep learning models struggle to adapt to the high variations of the urban geometry and to large mesh sizes. To tackle these challenges, we introduce Anchored Branched Steady-state WInd Flow Transformer (AB-SWIFT), a transformer-based model with an internal branched structure uniquely designed for atmospheric flow modeling. We train our model on a specially designed database of atmospheric simulations around randomised urban geometries and with a mixture of unstable, neutral, and stable atmospheric stratifications. Our model reaches the best accuracy on all predicted fields compared to state-of-the-art transformers and graph-based models. Our code and data is available at https://github.com/cerea-daml/abswift.

### 🤖 AI 总结

**一句话总结**：AB-SWIFT 提出一种带“锚定-分支”内部结构的Transformer代理模型，在复杂城市几何与大网格条件下高精度预测3D城市大气稳态流场。

**研究动机**：城市局地风场对污染扩散等应用关键，但CFD代价高；现有深度学习代理在城市几何变化大、网格规模大时泛化与扩展性不足。

**核心方法**：构建包含随机化城市几何、并混合不稳定/中性/稳定分层的大气流动仿真数据库进行训练；提出Transformer架构AB-SWIFT，通过内部分支结构专门适配大气流场多变量预测并提升对复杂几何的适应性。

**主要结论**：在所有预测物理场指标上，AB-SWIFT 相比SOTA Transformer与图模型取得最佳精度，证明其适用于城市环境3D大气流的高效代理建模，并开源代码与数据以支持复现与扩展。

**关键词**：城市大气流场建模, 三维风场预测, 深度学习代理模型, CFD替代建模, 分支结构网络, 大规模网格泛化, 随机城市几何数据集, 大气稳定度分层, 污染物扩散模拟, 风电场风资源建模

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.25635v1) | [下载PDF](https://arxiv.org/pdf/2603.25635v1.pdf)

---

