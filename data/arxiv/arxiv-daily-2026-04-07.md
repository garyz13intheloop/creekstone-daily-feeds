# arXiv AI 论文日报 | 2026-04-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (14 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. QED-Nano: Teaching a Tiny Model to Prove Hard Theorems](https://arxiv.org/abs/2604.04898v1)

**作者**：LM-Provers, Yuxiao Qu, Amrith Setlur 等 9 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Proprietary AI systems have recently demonstrated impressive capabilities on complex proof-based problems, with gold-level performance reported at the 2025 International Mathematical Olympiad (IMO). However, the training pipelines behind these systems remain largely undisclosed, and their reliance on large "internal" models and scaffolds makes them expensive to run, difficult to reproduce, and hard to study or improve upon. This raises a central question: can small, open models also be trained to achieve competitive reasoning performance on difficult Olympiad-level math? In this paper, we answer this question by building QED-Nano, a 4B model post-trained for Olympiad-level proofs. Our training recipe has three stages: (1) supervised fine-tuning to imbue good proof-writing styles by distilling from DeepSeek-Math-V2, (2) reinforcement learning (RL) with rubric-based rewards, and (3) expanding RL with a reasoning cache, which decomposes long proofs into iterative summarize-and-refine cycles and enables stronger test-time reasoning. QED-Nano surpasses the proof-generation performance of much larger open models, including Nomos-1 and GPT-OSS-120B, and approaches the performance of proprietary models like Gemini 3 Pro, at a fraction of the inference cost. To support further research on open mathematical reasoning, we release the full QED-Nano pipeline, including the QED-Nano and QED-Nano-SFT models, the FineProofs-SFT and FineProofs-RL datasets, and the training and evaluation code.

### 🤖 AI 总结

**一句话总结**：QED-Nano通过“SFT蒸馏+基于评分细则的RL+推理缓存”的三阶段训练，让4B小模型在奥赛级证明生成上接近顶级闭源系统并显著超过更大开源模型。

**研究动机**：现有高水平证明能力多来自闭源且依赖大模型与复杂脚手架的管线，成本高、难复现也难研究。作者希望验证小型开源模型是否也能通过可公开的训练流程获得有竞争力的奥赛级推理与证明能力。

**核心方法**：首先用DeepSeek-Math-V2蒸馏做监督微调以学习高质量证明写作风格；随后用基于rubric（评分细则）的强化学习优化证明质量；最后引入“reasoning cache”把长证明拆成迭代的总结-改写循环，增强训练与测试时的长程推理。

**主要结论**：QED-Nano在证明生成上超越Nomos-1、GPT-OSS-120B等更大开源模型，并在更低推理成本下逼近Gemini 3 Pro等闭源模型表现。作者同时开源模型、数据集与训练评测代码，为开放数学推理研究提供可复现管线。

**关键词**：奥数级证明生成, 小模型推理, 监督微调蒸馏, 基于规则的强化学习, 奖励模型评估, 推理缓存, 总结-精炼循环, 长证明分解, 后训练管线开源, 数学推理数据集, 证明写作风格学习

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04898v1) | [下载PDF](https://arxiv.org/pdf/2604.04898v1.pdf)

---

## [2. Learning, Potential, and Retention: An Approach for Evaluating Adaptive AI-Enabled Medical Devices](https://arxiv.org/abs/2604.04878v1)

**作者**：Alexis Burgon, Berkman Sahiner, Nicholas A Petrick 等 5 位作者  
**分类**：cs.AI, cs.PF  
**发布时间**：2026-04-06

### 📄 论文摘要

This work addresses challenges in evaluating adaptive artificial intelligence (AI) models for medical devices, where iterative updates to both models and evaluation datasets complicate performance assessment. We introduce a novel approach with three complementary measurements: learning (model improvement on current data), potential (dataset-driven performance shifts), and retention (knowledge preservation across modification steps), to disentangle performance changes caused by model adaptations versus dynamic environments. Case studies using simulated population shifts demonstrate the approach's utility: gradual transitions enable stable learning and retention, while rapid shifts reveal trade-offs between plasticity and stability. These measurements provide practical insights for regulatory science, enabling rigorous assessment of the safety and effectiveness of adaptive AI systems over sequential modifications.

### 🤖 AI 总结

**一句话总结**：提出“学习（learning）-潜力（potential）-保持（retention）”三指标框架，用于在模型与数据集持续变化的情况下评估自适应AI医疗器械的性能变化来源。

**研究动机**：自适应AI医疗器械会不断迭代模型与评测数据集，导致观察到的性能变化难以区分是模型变好了还是环境/数据分布变了，从而增加安全有效性评估与监管难度。

**核心方法**：提出三类互补度量：learning衡量模型在当前数据上的改进，potential刻画由数据集/人群分布变化引起的性能位移，retention评估跨多次修改后对既有知识的保留；并用模拟的人群分布漂移（渐变与突变）做案例分析以分离“模型适应”与“环境动态”的影响。

**主要结论**：在人群分布渐进变化时，模型可实现更稳定的学习与知识保持；在快速分布突变时，表现出可塑性（快速适应）与稳定性（保持旧知识）之间的权衡，该框架为序贯更新下的安全性与有效性监管评估提供了更可解释、可操作的量化依据。

**关键词**：自适应医疗器械, 自适应模型评测, 序列化模型更新, 动态评测数据集, 数据分布漂移, 人群迁移模拟, 学习度量, 潜力度量, 保留度量, 可塑性-稳定性权衡, 监管科学评估, 安全性有效性评估

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04878v1) | [下载PDF](https://arxiv.org/pdf/2604.04878v1.pdf)

---

## [3. Incompleteness of AI Safety Verification via Kolmogorov Complexity](https://arxiv.org/abs/2604.04876v1)

**作者**：Munawar Hasan  
**分类**：cs.AI  
**发布时间**：2026-04-06

### 📄 论文摘要

Ensuring that artificial intelligence (AI) systems satisfy formal safety and policy constraints is a central challenge in safety-critical domains. While limitations of verification are often attributed to combinatorial complexity and model expressiveness, we show that they arise from intrinsic information-theoretic limits. We formalize policy compliance as a verification problem over encoded system behaviors and analyze it using Kolmogorov complexity. We prove an incompleteness result: for any fixed sound computably enumerable verifier, there exists a threshold beyond which true policy-compliant instances cannot be certified once their complexity exceeds that threshold. Consequently, no finite formal verifier can certify all policy-compliant instances of arbitrarily high complexity. This reveals a fundamental limitation of AI safety verification independent of computational resources, and motivates proof-carrying approaches that provide instance-level correctness guarantees.

### 🤖 AI 总结

**一句话总结**：论文指出：基于固定形式化验证器的AI安全/政策合规验证存在信息论层面的“不完备性”，高复杂度的真实合规实例将无法被证明合规。

**研究动机**：现有观点多将验证失败归因于计算资源或模型规模带来的组合爆炸，但作者希望证明即使忽略算力限制，验证本身也存在不可克服的理论上限。

**核心方法**：将“政策合规”形式化为对编码后的系统行为进行验证的问题，并用Kolmogorov复杂度刻画实例的信息含量；在“健全且可计算枚举（c.e.）”的验证器假设下，证明存在复杂度阈值使得超过该阈值的真合规实例无法被该验证器认证。

**主要结论**：任何固定的（有限的）形式化验证器都不可能覆盖任意高复杂度的所有合规实例，这一限制独立于计算资源；因此作者提出应采用类似proof-carrying（携带证明/证据）的实例级保证思路来弥补传统验证的完备性缺陷。

**关键词**：AI安全验证, 形式化验证, 策略合规验证, 柯尔莫哥洛夫复杂度, 信息论极限, 不完备性定理, 可计算枚举验证器, 健全性, 复杂度阈值, 证明携带式验证

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04876v1) | [下载PDF](https://arxiv.org/pdf/2604.04876v1.pdf)

---

## cs.CL

## [4. Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection](https://arxiv.org/abs/2604.04932v1)

**作者**：Yang Li, Qiang Sheng, Zhengjia Wang 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-06

### 📄 论文摘要

The misuse of large language models (LLMs) requires precise detection of synthetic text. Existing works mainly follow binary or ternary classification settings, which can only distinguish pure human/LLM text or collaborative text at best. This remains insufficient for the nuanced regulation, as the LLM-polished human text and humanized LLM text often trigger different policy consequences. In this paper, we explore fine-grained LLM-generated text detection under a rigorous four-class setting. To handle such complexities, we propose RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creator and editor. Specifically, RACE utilizes Rhetorical Structure Theory to construct a logic graph for the creator's foundation while extracting Elementary Discourse Unit-level features for the editor's style. Experiments show that RACE outperforms 12 baselines in identifying fine-grained types with low false alarms, offering a policy-aligned solution for LLM regulation.

### 🤖 AI 总结

**一句话总结**：论文提出RACE方法，在“四分类”框架下同时建模文本的“创作者(creator)”与“编辑者(editor)”角色，以更细粒度地区分不同的人机协作生成形态并提升检测准确性。

**研究动机**：现有LLM文本检测多停留在二/三分类，难以区分“人写后被LLM润色”和“LLM写后被人类改写”等会引发不同监管后果的细微类型，因此需要更政策对齐的细粒度检测。

**核心方法**：RACE基于修辞结构理论(RST)为“创作者的内容逻辑/论证骨架”构建逻辑图，同时在EDU（基础话语单元）级别抽取特征以刻画“编辑者的文风与表述痕迹”，从而联合识别四类文本来源/加工方式。

**主要结论**：实验表明RACE在四分类细粒度识别上优于12个基线方法，并能在降低误报的同时更可靠地区分不同人机协作形态，为LLM生成文本的精细化监管提供了更可行的检测方案。

**关键词**：细粒度生成文本检测, 四分类设定, 人机协作文本鉴别, 创作者-编辑者建模, 修订痕迹识别, 修辞结构理论, 修辞关系图, 话语单元（EDU）特征, 篇章结构分析, 低误报检测

**评分**：79

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04932v1) | [下载PDF](https://arxiv.org/pdf/2604.04932v1.pdf)

---

## [5. Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation](https://arxiv.org/abs/2604.04894v1)

**作者**：Hengrui Gu, Xiaotian Han, Yujing Bian 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning capabilities of large language models (LLMs). However, it faces a fundamental limitation termed \textit{restricted exploration}, where the policy rapidly converges to a narrow set of solutions. While entropy regularization is a popular approach used to sustain exploration, it often proves unreliable for LLMs, suffering from high hyperparameter sensitivity and yielding only marginal performance gains. Motivated by these inefficiencies, we propose to rethink the relationship between policy entropy and exploration. By deriving a parametric formulation of group-relative advantage estimation and analyzing entropy dynamics, we conceptually decompose policy entropy into \textit{informative entropy}, which preserves diverse solution paths, and \textit{spurious entropy}, which erodes reasoning patterns. Our analysis reveals that, in contrast to blind maximization, effective exploration requires \textit{entropy refinement}-a mechanism implicitly embedded in group-relative advantage estimation that sustains informative entropy on positive rollouts while suppressing spurious entropy on negative ones. Guided by this insight, we propose \textbf{AsymGRPO}, an exploratory framework that explicitly decouples the modulation of positive and negative rollouts. This allows for independent control over the preservation of informative entropy and the suppression of spurious noise. Extensive experiments demonstrate that AsymGRPO achieves superior performance compared to strong baselines and exhibits the potential to synergize with existing entropy regularization methods.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) has significantly advanced the reasoning capabilities of large language models (LLMs). However, it faces a fundamental limitation termed \textit{r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：受限探索, 熵正则化, 策略熵, 信息熵, 虚假熵, 熵细化, 组相对优势估计, 正负轨迹解耦调制, 可验证奖励

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04894v1) | [下载PDF](https://arxiv.org/pdf/2604.04894v1.pdf)

---

## [6. Synthetic Sandbox for Training Machine Learning Engineering Agents](https://arxiv.org/abs/2604.04872v1)

**作者**：Yuhang Zhou, Lizhu Zhang, Yifan Wu 等 7 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

As large language model agents advance beyond software engineering (SWE) tasks toward machine learning engineering (MLE), verifying agent behavior becomes orders of magnitude more expensive: while SWE tasks can be verified via fast-executing unit tests, MLE verification requires running full ML pipelines -- data preprocessing, model training, and metric evaluation -- on large datasets at each rollout step, rendering trajectory-wise on-policy reinforcement learning (RL) prohibitively slow. Existing approaches retreat to supervised fine-tuning (SFT) or offline proxy rewards, sacrificing the exploration and generalization benefits of on-policy RL. We observe that sandbox data size is the primary source of this bottleneck. Based on this insight, we introduce SandMLE, a multi-agent framework that generates diverse, verifiable synthetic MLE environments from a small number of seed tasks, preserving the structural and technical complexity of real-world problems while constraining datasets to micro-scale (each task is paired with only 50-200 training samples). Through extensive experiments, we show that SandMLE reduces execution time by over 13 times, enabling large-scale, on-policy trajectory-wise RL for the first time in the MLE domain. On MLE-bench-lite, SandMLE yields significant gains over SFT baselines across Qwen3-8B, 14B, and 30B-A3B, with relative medal rate improvements ranging from 20.3% to 66.9%. Furthermore, the trained policy generalizes across unseen agentic scaffolds, achieving up to 32.4% better HumanRank score on MLE-Dojo.

### 🤖 AI 总结

**一句话总结**：SandMLE 通过从少量真实种子任务生成可验证的微型合成 MLE 沙盒，把训练/评测成本大幅降低，从而首次让 MLE 领域的大规模轨迹级在线强化学习变得可行并提升性能与泛化。

**研究动机**：MLE 任务的验证需要跑完整 ML 流水线且依赖大数据集，导致在线 RL 每步回放成本极高、训练速度不可接受，现有方法多退回到 SFT 或离线代理奖励而牺牲探索与泛化。作者观察到瓶颈主要来自沙盒数据规模，而非流程结构本身。

**核心方法**：提出 SandMLE 多智能体框架：基于少量种子任务自动生成多样、可验证的合成 MLE 环境，并将每个任务的数据集压缩到微型规模（约 50–200 条训练样本），同时保留真实问题的结构与技术复杂度。借此显著加速流水线执行，使轨迹级、on-policy RL 可以在 MLE 场景中高效运行并与不同 agent scaffolds 兼容泛化。

**主要结论**：SandMLE 将执行时间提升（加速）超过 13 倍，使 MLE 领域的在线轨迹级 RL 在工程上可规模化；在 MLE-bench-lite 上，相比 SFT 基线在多种 Qwen3 模型上获得 20.3%–66.9% 的相对 medal rate 提升。训练出的策略还能跨未见过的智能体脚手架泛化，在 MLE-Dojo 上 HumanRank 最高提升 32.4%。

**关键词**：机器学习工程代理, 合成沙盒环境, 合成任务生成, 微型数据集, 多智能体框架, 轨迹级强化学习, 可验证评测, ML流水线执行, 跨脚手架泛化

**评分**：80

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04872v1) | [下载PDF](https://arxiv.org/pdf/2604.04872v1.pdf)

---

## [7. Do No Harm: Exposing Hidden Vulnerabilities of LLMs via Persona-based Client Simulation Attack in Psychological Counseling](https://arxiv.org/abs/2604.04842v1)

**作者**：Qingyang Xu, Yaling Shen, Stephanie Fong 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-06

### 📄 论文摘要

The increasing use of large language models (LLMs) in mental healthcare raises safety concerns in high-stakes therapeutic interactions. A key challenge is distinguishing therapeutic empathy from maladaptive validation, where supportive responses may inadvertently reinforce harmful beliefs or behaviors in multi-turn conversations. This risk is largely overlooked by existing red-teaming frameworks, which focus mainly on generic harms or optimization-based attacks. To address this gap, we introduce Personality-based Client Simulation Attack (PCSA), the first red-teaming framework that simulates clients in psychological counseling through coherent, persona-driven client dialogues to expose vulnerabilities in psychological safety alignment. Experiments on seven general and mental health-specialized LLMs show that PCSA substantially outperforms four competitive baselines. Perplexity analysis and human inspection further indicate that PCSA generates more natural and realistic dialogues. Our results reveal that current LLMs remain vulnerable to domain-specific adversarial tactics, providing unauthorized medical advice, reinforcing delusions, and implicitly encouraging risky actions.

### 🤖 AI 总结

**一句话总结**：The increasing use of large language models (LLMs) in mental healthcare raises safety concerns in high-stakes therapeutic interactions. A key challenge is distinguishing therapeutic empathy from malad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：心理咨询, 心理安全对齐, 人格化客户端模拟, 红队评测框架, 多轮对话攻击, 适应性验证, 妄想强化, 未授权医疗建议, 风险行为暗示, 心理健康LLM

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04842v1) | [下载PDF](https://arxiv.org/pdf/2604.04842v1.pdf)

---

## [8. LiveFact: A Dynamic, Time-Aware Benchmark for LLM-Driven Fake News Detection](https://arxiv.org/abs/2604.04815v1)

**作者**：Cheng Xu, Changhong Jin, Yingjie Niu 等 8 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-06

### 📄 论文摘要

The rapid development of Large Language Models (LLMs) has transformed fake news detection and fact-checking tasks from simple classification to complex reasoning. However, evaluation frameworks have not kept pace. Current benchmarks are static, making them vulnerable to benchmark data contamination (BDC) and ineffective at assessing reasoning under temporal uncertainty. To address this, we introduce LiveFact a continuously updated benchmark that simulates the real-world "fog of war" in misinformation detection. LiveFact uses dynamic, temporal evidence sets to evaluate models on their ability to reason with evolving, incomplete information rather than on memorized knowledge. We propose a dual-mode evaluation: Classification Mode for final verification and Inference Mode for evidence-based reasoning, along with a component to monitor BDC explicitly. Tests with 22 LLMs show that open-source Mixture-of-Experts models, such as Qwen3-235B-A22B, now match or outperform proprietary state-of-the-art systems. More importantly, our analysis finds a significant "reasoning gap." Capable models exhibit epistemic humility by recognizing unverifiable claims in early data slices-an aspect traditional static benchmarks overlook. LiveFact sets a sustainable standard for evaluating robust, temporally aware AI verification.

### 🤖 AI 总结

**一句话总结**：LiveFact 提出一个持续更新、时间感知的动态基准，用于在“信息不完整且不断演化”的真实环境下评测 LLM 的假新闻检测与推理能力，并显式监控基准污染。

**研究动机**：现有假新闻/事实核查基准多为静态数据，既容易被训练数据污染导致虚高成绩，也无法评估模型在不同时间切片下、证据未完备时的推理与不确定性处理能力。

**核心方法**：构建持续更新的 LiveFact，提供随时间变化的证据集合以模拟“战争迷雾”，并设计双模式评测：Classification Mode 做最终真伪判定，Inference Mode 评估基于证据的推理过程，同时加入组件用于检测/监控 Benchmark Data Contamination。

**主要结论**：在 22 个 LLM 测试中，开源 MoE 模型（如 Qwen3-235B-A22B）可达到或超过部分闭源 SOTA；更关键的是发现显著“推理鸿沟”——强模型能在早期证据不足时表现出认识论谦逊、承认不可验证，这一能力是传统静态基准难以衡量的。

**关键词**：动态基准, 时间感知评测, 假新闻检测, 事实核查, 时序证据集, 时间不确定性推理, 证据驱动推理, 双模式评测, 基准数据污染监测, 认知谦逊

**评分**：80

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04815v1) | [下载PDF](https://arxiv.org/pdf/2604.04815v1.pdf)

---

## [9. SkillX: Automatically Constructing Skill Knowledge Bases for Agents](https://arxiv.org/abs/2604.04804v1)

**作者**：Chenxi Wang, Zhuoyun Yu, Xin Xie 等 11 位作者  
**分类**：cs.CL, cs.AI, cs.IR, cs.LG, cs.MA  
**发布时间**：2026-04-06

### 📄 论文摘要

Learning from experience is critical for building capable large language model (LLM) agents, yet prevailing self-evolving paradigms remain inefficient: agents learn in isolation, repeatedly rediscover similar behaviors from limited experience, resulting in redundant exploration and poor generalization. To address this problem, we propose SkillX, a fully automated framework for constructing a \textbf{plug-and-play skill knowledge base} that can be reused across agents and environments. SkillX operates through a fully automated pipeline built on three synergistic innovations: \textit{(i) Multi-Level Skills Design}, which distills raw trajectories into three-tiered hierarchy of strategic plans, functional skills, and atomic skills; \textit{(ii) Iterative Skills Refinement}, which automatically revises skills based on execution feedback to continuously improve library quality; and \textit{(iii) Exploratory Skills Expansion}, which proactively generates and validates novel skills to expand coverage beyond seed training data. Using a strong backbone agent (GLM-4.6), we automatically build a reusable skill library and evaluate its transferability on challenging long-horizon, user-interactive benchmarks, including AppWorld, BFCL-v3, and $τ^2$-Bench. Experiments show that SkillKB consistently improves task success and execution efficiency when plugged into weaker base agents, highlighting the importance of structured, hierarchical experience representations for generalizable agent learning. Our code will be publicly available soon at https://github.com/zjunlp/SkillX.

### 🤖 AI 总结

**一句话总结**：SkillX 提出一种全自动构建可复用的分层技能知识库（SkillKB）的框架，用于提升不同LLM智能体在跨环境长流程任务中的成功率与执行效率。

**研究动机**：现有自进化/自学习智能体往往各自孤立学习，反复从有限经验中“重复发现”相似行为，导致探索冗余且泛化差。为此需要一种可跨智能体、跨环境复用的结构化经验载体来降低重复试错成本。

**核心方法**：SkillX 通过自动化流水线构建技能库：将轨迹蒸馏为“战略计划-功能技能-原子技能”的三级层次表示；再基于执行反馈进行迭代技能修订以提升质量；并主动生成与验证新技能以扩展覆盖面。随后将该SkillKB以即插即用方式接入较弱基座智能体，评估其迁移效果。

**主要结论**：在 AppWorld、BFCL-v3 与 τ^2-Bench 等长时序交互基准上，SkillKB 接入后能稳定提升较弱智能体的任务成功率与执行效率，表明分层、结构化的技能表示有助于可泛化的智能体经验学习与迁移。

**关键词**：技能知识库, 可插拔技能库, 层级技能表示, 轨迹蒸馏, 策略规划, 功能技能, 原子技能, 执行反馈优化, 技能扩展生成, 长时程交互任务

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04804v1) | [下载PDF](https://arxiv.org/pdf/2604.04804v1.pdf)

---

## [10. How Far Are We? Systematic Evaluation of LLMs vs. Human Experts in Mathematical Contest in Modeling](https://arxiv.org/abs/2604.04791v1)

**作者**：Yuhang Liu, Heyan Huang, Yizhe Yang 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-06

### 📄 论文摘要

Large language models (LLMs) have achieved strong performance on reasoning benchmarks, yet their ability to solve real-world problems requiring end-to-end workflows remains unclear. Mathematical modeling competitions provide a stringent testbed for evaluating such end-to-end problem-solving capability. We propose a problem-oriented, stage-wise evaluation framework that assesses LLM performance across modeling stages using expert-verified criteria. We validate the framework's reliability by comparing automatic scores with independent human expert judgments on problems from the China Postgraduate Mathematical Contest in Modeling, demonstrating substantially stronger alignment than existing evaluation schemes. Using this framework, we reveal a comprehension-execution gap in state-of-the-art LLMs: while they perform well in early stages such as problem identification and formulation, they exhibit persistent deficiencies in execution-oriented stages including model solving, code implementation, and result analysis. These gaps persist even with increased model scale. We further trace these failures to insufficient specification, missing verification, and lack of validation, with errors propagating across stages without correction. Our findings suggest that bridging this gap requires approaches beyond model scaling, offering insights for applying LLMs to complex real-world problem solving.

### 🤖 AI 总结

**一句话总结**：论文提出一个面向数学建模竞赛的分阶段评测框架，发现当前LLM在“理解与建模”阶段表现较好，但在“求解、代码实现与结果分析”等执行阶段存在稳定且难以通过规模提升弥补的差距。

**研究动机**：现有推理基准难以衡量LLM在真实世界端到端工作流中的问题解决能力，而数学建模竞赛能系统考察从理解题意到实现与验证的完整链路。作者希望构建一个更可靠的评测体系，并量化LLM与人类专家在各建模阶段的差异与失效原因。

**核心方法**：提出“问题导向、阶段化”的评测框架，用专家验证的标准对建模流程各阶段分别打分，并用中国研究生数学建模竞赛题目进行实验。通过将自动评分与独立人类专家评审对齐来验证框架可靠性，并与现有评测方案比较一致性。

**主要结论**：最先进LLM在问题识别与公式化等早期阶段较强，但在模型求解、代码实现、结果分析/验证等执行导向阶段持续欠缺，且随模型变大仍存在“理解-执行鸿沟”。失败根因包括规格不充分、缺少校验与验证机制，错误会跨阶段传播且缺乏纠错，提示改进需要超越单纯扩展规模的方案。

**关键词**：数学建模竞赛, 端到端工作流, 阶段式评测框架, 专家验证标准, 自动评分一致性, 人类专家对比评测, 模型求解, 代码实现, 错误传播

**评分**：61

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04791v1) | [下载PDF](https://arxiv.org/pdf/2604.04791v1.pdf)

---

## cs.CV

## [11. Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)

**作者**：Hyunsoo Cha, Wonjung Woo, Byungjun Kim 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

We present Vanast, a unified framework that generates garment-transferred human animation videos directly from a single human image, garment images, and a pose guidance video. Conventional two-stage pipelines treat image-based virtual try-on and pose-driven animation as separate processes, which often results in identity drift, garment distortion, and front-back inconsistency. Our model addresses these issues by performing the entire process in a single unified step to achieve coherent synthesis. To enable this setting, we construct large-scale triplet supervision. Our data generation pipeline includes generating identity-preserving human images in alternative outfits that differ from garment catalog images, capturing full upper and lower garment triplets to overcome the single-garment-posed video pair limitation, and assembling diverse in-the-wild triplets without requiring garment catalog images. We further introduce a Dual Module architecture for video diffusion transformers to stabilize training, preserve pretrained generative quality, and improve garment accuracy, pose adherence, and identity preservation while supporting zero-shot garment interpolation. Together, these contributions allow Vanast to produce high-fidelity, identity-consistent animation across a wide range of garment types.

### 🤖 AI 总结

**一句话总结**：Vanast 将虚拟试衣与姿态驱动的人体动画统一到一步式视频生成框架中，通过合成三元组监督与双模块扩散Transformer，实现身份一致、服装准确且前后连贯的试衣动画视频。

**研究动机**：传统“两阶段”(先试衣再动画)流程把服装迁移与动作生成割裂，容易造成身份漂移、衣物扭曲与前后视角不一致；同时缺少能覆盖上下装与多来源场景的高质量监督数据来支撑端到端训练。

**核心方法**：构建大规模“人像-服装-姿态/视频”合成三元组监督：生成保持身份但换装的人像、扩展到上下装三元组、并组装无需商品图的野外三元组；在模型上提出用于视频扩散Transformer的Dual Module架构，以稳定训练、保持预训练生成能力并提升服装准确性、姿态跟随与身份保持，同时支持零样本服装插值。

**主要结论**：统一框架+三元组监督+双模块架构共同提升了生成质量，使模型能在多种服装类型下生成高保真、身份一致、动作贴合且服装前后连贯的虚拟试衣动画视频，并减少传统两阶段方法的典型失真问题。

**关键词**：虚拟试衣, 服装迁移, 姿态引导视频生成, 人体图像动画, 视频扩散模型, 合成三元组监督, 身份一致性, 前后视角一致性, 双模块架构, 零样本服装插值

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04934v1) | [下载PDF](https://arxiv.org/pdf/2604.04934v1.pdf)

---

## [12. PointTPA: Dynamic Network Parameter Adaptation for 3D Scene Understanding](https://arxiv.org/abs/2604.04933v1)

**作者**：Siyuan Liu, Chaoqun Zheng, Xin Zhou 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

Scene-level point cloud understanding remains challenging due to diverse geometries, imbalanced category distributions, and highly varied spatial layouts. Existing methods improve object-level performance but rely on static network parameters during inference, limiting their adaptability to dynamic scene data. We propose PointTPA, a Test-time Parameter Adaptation framework that generates input-aware network parameters for scene-level point clouds. PointTPA adopts a Serialization-based Neighborhood Grouping (SNG) to form locally coherent patches and a Dynamic Parameter Projector (DPP) to produce patch-wise adaptive weights, enabling the backbone to adjust its behavior according to scene-specific variations while maintaining a low parameter overhead. Integrated into the PTv3 structure, PointTPA demonstrates strong parameter efficiency by introducing two lightweight modules of less than 2% of the backbone's parameters. Despite this minimal parameter overhead, PointTPA achieves 78.4% mIoU on ScanNet validation, surpassing existing parameter-efficient fine-tuning (PEFT) methods across multiple benchmarks, highlighting the efficacy of our test-time dynamic network parameter adaptation mechanism in enhancing 3D scene understanding. The code is available at https://github.com/H-EmbodVis/PointTPA.

### 🤖 AI 总结

**一句话总结**：PointTPA通过测试时动态生成输入感知的网络参数，使3D场景点云分割在几乎不增加参数的情况下获得更高精度。

**研究动机**：场景级点云因几何形态多样、类别分布不均与空间布局变化大而难以建模，而现有方法推理时使用静态参数，难以适应不同场景的动态变化。

**核心方法**：提出测试时参数自适应框架PointTPA：用SNG（基于序列化的邻域分组）将点云划分为局部一致的patch，再用DPP（动态参数投影器）为每个patch生成自适应权重以调节骨干网络行为，并以极低开销集成到PTv3中（新增模块参数量<2%）。

**主要结论**：在仅引入极小参数开销的前提下，PointTPA在ScanNet验证集达到78.4% mIoU，优于多种参数高效微调（PEFT）方法，证明测试时动态参数适配能有效提升3D场景理解性能。

**关键词**：场景级点云, 3D语义分割, 测试时参数自适应, 动态网络参数, 参数高效微调（PEFT）, 序列化邻域分组（SNG）, 动态参数投影器（DPP）, PTv3骨干网络

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04933v1) | [下载PDF](https://arxiv.org/pdf/2604.04933v1.pdf)

---

## [13. LoMa: Local Feature Matching Revisited](https://arxiv.org/abs/2604.04931v1)

**作者**：David Nordström, Johan Edstedt, Georg Bökman 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

Local feature matching has long been a fundamental component of 3D vision systems such as Structure-from-Motion (SfM), yet progress has lagged behind the rapid advances of modern data-driven approaches. The newer approaches, such as feed-forward reconstruction models, have benefited extensively from scaling dataset sizes, whereas local feature matching models are still only trained on a few mid-sized datasets. In this paper, we revisit local feature matching from a data-driven perspective. In our approach, which we call LoMa, we combine large and diverse data mixtures, modern training recipes, scaled model capacity, and scaled compute, resulting in remarkable gains in performance. Since current standard benchmarks mainly rely on collecting sparse views from successful 3D reconstructions, the evaluation of progress in feature matching has been limited to relatively easy image pairs. To address the resulting saturation of benchmarks, we collect 1000 highly challenging image pairs from internet data into a new dataset called HardMatch. Ground truth correspondences for HardMatch are obtained via manual annotation by the authors. In our extensive benchmarking suite, we find that LoMa makes outstanding progress across the board, outperforming the state-of-the-art method ALIKED+LightGlue by +18.6 mAA on HardMatch, +29.5 mAA on WxBS, +21.4 (1m, 10$^\circ$) on InLoc, +24.2 AUC on RUBIK, and +12.4 mAA on IMC 2022. We release our code and models publicly at https://github.com/davnords/LoMa.

### 🤖 AI 总结

**一句话总结**：LoMa 通过扩大数据规模与多样性、采用现代训练配方并提升模型与计算规模，显著刷新了局部特征匹配在多个高难基准上的性能。

**研究动机**：现有局部特征匹配方法受限于训练数据规模与训练/算力配置，进步慢于数据驱动的大模型路线；同时主流评测多来自“可成功重建”的稀疏视角对，导致基准偏简单、趋于饱和。

**核心方法**：提出 LoMa：以“大而杂”的数据混合训练为核心，结合现代训练策略、扩大模型容量与训练计算，从数据驱动角度重新设计局部特征匹配训练范式；并构建更具挑战性的 HardMatch 数据集（1000 对互联网难例图像，作者人工标注真值对应）用于评测。

**主要结论**：在包含 HardMatch、WxBS、InLoc、RUBIK、IMC 2022 等的综合评测中，LoMa 全面优于现有 SOTA（如 ALIKED+LightGlue），在多个指标上取得显著提升，表明“规模化数据+训练配方+算力/容量扩展”能大幅推进局部特征匹配性能。

**关键词**：局部特征匹配, 关键点检测与描述子, 图像对应点匹配, 结构光束法平差（SfM）, 大规模数据混合训练, 模型规模扩展, 现代训练策略, 人工标注真值对应, 高难度图像对评测, 宽基线匹配（WxBS）, 跨基准性能评测

**评分**：79

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04931v1) | [下载PDF](https://arxiv.org/pdf/2604.04931v1.pdf)

---

## [14. Vero: An Open RL Recipe for General Visual Reasoning](https://arxiv.org/abs/2604.04917v1)

**作者**：Gabriel Sarch, Linrong Cai, Qunzhong Wang 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-06

### 📄 论文摘要

What does it take to build a visual reasoner that works across charts, science, spatial understanding, and open-ended tasks? The strongest vision-language models (VLMs) show such broad visual reasoning is within reach, but the recipe behind them remains unclear, locked behind proprietary reinforcement learning (RL) pipelines with non-public data. We introduce Vero, a family of fully open VLMs that matches or exceeds existing open-weight models across diverse visual reasoning tasks. We scale RL data and rewards across six broad task categories, constructing Vero-600K, a 600K-sample dataset from 59 datasets, and designing task-routed rewards that handle heterogeneous answer formats. Vero achieves state-of-the-art performance, improving over four base models by 3.7-5.5 points on average across VeroEval, our suite of 30 challenging benchmarks. Starting from Qwen3-VL-8B-Instruct, Vero outperforms Qwen3-VL-8B-Thinking on 23 of 30 benchmarks without additional proprietary thinking data. When trained from the same base model, Vero-600K exceeds existing RL datasets across task categories. Systematic ablations reveal that different task categories elicit qualitatively distinct reasoning patterns that transfer poorly in isolation, suggesting that broad data coverage is the primary driver of strong RL scaling. All data, code, and models are released.

### 🤖 AI 总结

**一句话总结**：Vero 提供一套完全开源的视觉语言模型强化学习配方，通过大规模多任务RL数据与任务路由奖励，在多类视觉推理基准上达到/超过现有开源模型表现。

**研究动机**：当前强视觉推理VLM的关键RL训练流程与数据多为闭源，导致社区难以复现与系统化扩展跨图表、科学、空间等通用视觉推理能力。作者希望用公开数据与可复用的RL方案，明确“如何做”才能稳定提升通用视觉推理。

**核心方法**：构建覆盖6大任务类别的RL训练集 Vero-600K（来自59个数据集共60万样本），并设计“任务路由奖励”（task-routed rewards）以适配异构答案格式与评测标准；在多个基座模型上进行RL训练，并用包含30个挑战基准的 VeroEval 做系统评测与消融分析。

**主要结论**：Vero 在 VeroEval 上相对四个基座模型平均提升3.7–5.5分，并在同为Qwen3-VL-8B系的对比中，无需额外专有“思考”数据即可在30项中赢下23项；消融表明单一任务类别的推理模式迁移性较差，广覆盖的任务与数据多样性是RL规模化提升通用视觉推理的主要驱动力。

**关键词**：视觉推理, 视觉语言模型（VLM）, 强化学习对齐（RLHF）, 多任务强化学习, 奖励建模, 任务路由奖励, 异构答案格式, RL 数据扩展, 数据集聚合, 视觉推理评测基准, 开放权重模型

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04917v1) | [下载PDF](https://arxiv.org/pdf/2604.04917v1.pdf)

---

## [15. SpatialEdit: Benchmarking Fine-Grained Image Spatial Editing](https://arxiv.org/abs/2604.04911v1)

**作者**：Yicheng Xiao, Wenhu Zhang, Lin Song 等 13 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

Image spatial editing performs geometry-driven transformations, allowing precise control over object layout and camera viewpoints. Current models are insufficient for fine-grained spatial manipulations, motivating a dedicated assessment suite. Our contributions are listed: (i) We introduce SpatialEdit-Bench, a complete benchmark that evaluates spatial editing by jointly measuring perceptual plausibility and geometric fidelity via viewpoint reconstruction and framing analysis. (ii) To address the data bottleneck for scalable training, we construct SpatialEdit-500k, a synthetic dataset generated with a controllable Blender pipeline that renders objects across diverse backgrounds and systematic camera trajectories, providing precise ground-truth transformations for both object- and camera-centric operations. (iii) Building on this data, we develop SpatialEdit-16B, a baseline model for fine-grained spatial editing. Our method achieves competitive performance on general editing while substantially outperforming prior methods on spatial manipulation tasks. All resources will be made public at https://github.com/EasonXiao-888/SpatialEdit.

### 🤖 AI 总结

**一句话总结**：提出用于细粒度图像空间编辑的基准SpatialEdit-Bench、合成数据集SpatialEdit-500k及基线模型SpatialEdit-16B，以更准确评测并提升几何/视角驱动的编辑能力。

**研究动机**：现有图像编辑模型在精细空间操控（物体布局、相机视角变化等）上能力不足，且缺少能同时衡量“视觉真实感+几何一致性”的专门评测体系与可规模化训练数据。

**核心方法**：构建SpatialEdit-Bench，通过视角重建与构图分析联合评估感知合理性与几何保真度；用可控Blender渲染流水线生成SpatialEdit-500k，提供物体/相机中心操作的精确真值变换，并基于该数据训练SpatialEdit-16B作为空间编辑基线模型。

**主要结论**：SpatialEdit-16B在通用编辑上具备竞争力，并在空间操控任务上显著优于既有方法；同时公开的基准与数据集为后续细粒度空间编辑的训练与评测提供了标准化支撑。

**关键词**：图像空间编辑, 几何驱动编辑, 物体布局控制, 相机视角编辑, 空间编辑基准评测, 感知真实性评估, 几何保真度评估, 视角重建, 构图分析, 合成数据集生成, 相机轨迹标注

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04911v1) | [下载PDF](https://arxiv.org/pdf/2604.04911v1.pdf)

---

## [16. ClickAIXR: On-Device Multimodal Vision-Language Interaction with Real-World Objects in Extended Reality](https://arxiv.org/abs/2604.04905v1)

**作者**：Dawar Khan, Alexandre Kouyoumdjian, Xinyu Liu 等 6 位作者  
**分类**：cs.CV, cs.GR, cs.HC  
**发布时间**：2026-04-06

### 📄 论文摘要

We present ClickAIXR, a novel on-device framework for multimodal vision-language interaction with objects in extended reality (XR). Unlike prior systems that rely on cloud-based AI (e.g., ChatGPT) or gaze-based selection (e.g., GazePointAR), ClickAIXR integrates an on-device vision-language model (VLM) with a controller-based object selection paradigm, enabling users to precisely click on real-world objects in XR. Once selected, the object image is processed locally by the VLM to answer natural language questions through both text and speech. This object-centered interaction reduces ambiguity inherent in gaze- or voice-only interfaces and improves transparency by performing all inference on-device, addressing concerns around privacy and latency. We implemented ClickAIXR in the Magic Leap SDK (C API) with ONNX-based local VLM inference. We conducted a user study comparing ClickAIXR with Gemini 2.5 Flash and ChatGPT 5, evaluating usability, trust, and user satisfaction. Results show that latency is moderate and user experience is acceptable. Our findings demonstrate the potential of click-based object selection combined with on-device AI to advance trustworthy, privacy-preserving XR interactions. The source code and supplementary materials are available at: nanovis.org/ClickAIXR.html

### 🤖 AI 总结

**一句话总结**：ClickAIXR提出一种在XR中通过“手柄点击选物+本地视觉语言模型”实现对现实物体的多模态问答交互框架，兼顾精确性、隐私与低延迟。

**研究动机**：现有XR物体交互常依赖云端大模型或凝视/语音选择，容易产生选中歧义、引入隐私风险并带来网络延迟。作者希望用更可控的点击式选择与端侧推理，提升交互透明度与可信度。

**核心方法**：在Magic Leap上实现手柄点击的真实物体选取流程，将选中物体图像输入ONNX部署的端侧VLM进行本地推理，并以文本与语音输出回答。通过用户研究对比ClickAIXR与Gemini 2.5 Flash、ChatGPT 5，从可用性、信任与满意度等维度评估体验与延迟表现。

**主要结论**：结果表明该端侧点击选物方案具有可接受的用户体验与中等延迟，并能降低凝视/语音交互的歧义。研究展示了“点击式目标锁定+端侧AI”在隐私保护与可信XR交互方面的潜力。

**关键词**：端侧视觉语言模型, XR人机交互, 多模态问答, 点击式物体选择, 控制器交互, 隐私保护推理, 低延迟推理, ClickAIXR

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04905v1) | [下载PDF](https://arxiv.org/pdf/2604.04905v1.pdf)

---

## [17. FileGram: Grounding Agent Personalization in File-System Behavioral Traces](https://arxiv.org/abs/2604.04901v1)

**作者**：Shuai Liu, Shulin Tian, Kairui Hu 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-06

### 📄 论文摘要

Coworking AI agents operating within local file systems are rapidly emerging as a paradigm in human-AI interaction; however, effective personalization remains limited by severe data constraints, as strict privacy barriers and the difficulty of jointly collecting multimodal real-world traces prevent scalable training and evaluation, and existing methods remain interaction-centric while overlooking dense behavioral traces in file-system operations; to address this gap, we propose FileGram, a comprehensive framework that grounds agent memory and personalization in file-system behavioral traces, comprising three core components: (1) FileGramEngine, a scalable persona-driven data engine that simulates realistic workflows and generates fine-grained multimodal action sequences at scale; (2) FileGramBench, a diagnostic benchmark grounded in file-system behavioral traces for evaluating memory systems on profile reconstruction, trace disentanglement, persona drift detection, and multimodal grounding; and (3) FileGramOS, a bottom-up memory architecture that builds user profiles directly from atomic actions and content deltas rather than dialogue summaries, encoding these traces into procedural, semantic, and episodic channels with query-time abstraction; extensive experiments show that FileGramBench remains challenging for state-of-the-art memory systems and that FileGramEngine and FileGramOS are effective, and by open-sourcing the framework, we hope to support future research on personalized memory-centric file-system agents.

### 🤖 AI 总结

**一句话总结**：FileGram 提出以本地文件系统的细粒度行为轨迹为基础来构建与评测可个性化的协作型 AI 代理记忆系统，从数据生成、基准评测到记忆架构给出一体化方案。

**研究动机**：文件系统场景下的个性化受隐私与真实多模态轨迹难采集的限制，导致训练与评测数据稀缺；同时现有方法偏重对话交互，忽视了文件操作中更密集、可反映偏好的行为痕迹。

**核心方法**：框架包含三部分：FileGramEngine 用“人设驱动”仿真生成大规模、细粒度多模态文件操作序列；FileGramBench 基于这些轨迹设计诊断任务（画像重建、轨迹解纠缠、人设漂移检测、多模态落地）；FileGramOS 用自底向上的记忆架构从原子动作与内容增量构建程序/语义/情景三通道记忆，并在查询时抽象汇总。

**主要结论**：实验显示 FileGramBench 对现有 SOTA 记忆系统仍具挑战性，能暴露其在画像与轨迹理解上的不足；同时 FileGramEngine 与 FileGramOS 在生成可用训练/评测数据与提升个性化记忆建模方面有效，开源有助于推动文件系统代理的记忆与个性化研究。

**关键词**：文件系统智能体, 文件系统行为轨迹, 个性化记忆, 人设驱动数据模拟, 多模态动作序列, 诊断评测基准, 轨迹解缠, 人设漂移检测, 多模态对齐, 原子动作建模, 内容增量建模

**评分**：61

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04901v1) | [下载PDF](https://arxiv.org/pdf/2604.04901v1.pdf)

---

## [18. HorizonWeaver: Generalizable Multi-Level Semantic Editing for Driving Scenes](https://arxiv.org/abs/2604.04887v1)

**作者**：Mauricio Soroco, Francesco Pittaluga, Zaid Tasneem 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

Ensuring safety in autonomous driving requires scalable generation of realistic, controllable driving scenes beyond what real-world testing provides. Yet existing instruction guided image editors, trained on object-centric or artistic data, struggle with dense, safety-critical driving layouts. We propose HorizonWeaver, which tackles three fundamental challenges in driving scene editing: (1) multi-level granularity, requiring coherent object- and scene-level edits in dense environments; (2) rich high-level semantics, preserving diverse objects while following detailed instructions; and (3) ubiquitous domain shifts, handling changes in climate, layout, and traffic across unseen environments. The core of HorizonWeaver is a set of complementary contributions across data, model, and training: (1) Data: Large-scale dataset generation, where we build a paired real/synthetic dataset from Boreas, nuScenes, and Argoverse2 to improve generalization; (2) Model: Language-Guided Masks for fine-grained editing, where semantics-enriched masks and prompts enable precise, language-guided edits; and (3) Training: Content preservation and instruction alignment, where joint losses enforce scene consistency and instruction fidelity. Together, HorizonWeaver provides a scalable framework for photorealistic, instruction-driven editing of complex driving scenes, collecting 255K images across 13 editing categories and outperforming prior methods in L1, CLIP, and DINO metrics, achieving +46.4% user preference and improving BEV segmentation IoU by +33%. Project page: https://msoroco.github.io/horizonweaver/

### 🤖 AI 总结

**一句话总结**：HorizonWeaver 提出一个可泛化的多层语义驾驶场景编辑框架，通过大规模真实/合成配对数据、语言引导掩码与联合训练损失，实现对复杂密集道路场景的可控、逼真编辑并显著提升下游感知表现。

**研究动机**：自动驾驶安全验证需要大量可控且真实的场景生成/编辑，但现有指令式图像编辑器多在物体中心或艺术数据上训练，难以处理驾驶场景的密集布局、多粒度编辑与跨域（天气/地区/交通形态）泛化问题。

**核心方法**：方法从数据、模型与训练三方面协同：构建来自 Boreas、nuScenes、Argoverse2 的真实/合成配对大规模数据集；设计“语言引导掩码”以用语义增强的mask与提示实现细粒度、指令对齐的编辑；并引入内容保持与指令对齐的联合损失以同时维持场景一致性与编辑忠实度。

**主要结论**：在 13 类编辑任务、25.5 万张图像上，HorizonWeaver 在 L1、CLIP、DINO 等指标及用户偏好上优于先前方法（用户偏好 +46.4%），同时还能将 BEV 分割 IoU 提升 +33%，显示其在逼真可控编辑与跨域泛化上的有效性。

**关键词**：自动驾驶场景编辑, 指令驱动图像编辑, 多层级语义编辑, 密集交通布局, 跨域泛化, 真实-合成配对数据集, 语言引导掩码, 语义增强分割掩码, 内容保持损失, 指令对齐训练, BEV分割评测

**评分**：84

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04887v1) | [下载PDF](https://arxiv.org/pdf/2604.04887v1.pdf)

---

## [19. DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planning and Intent-Guided Editing](https://arxiv.org/abs/2604.04875v1)

**作者**：Ke Li, Maoliang Li, Jialiang Chen 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.MM  
**发布时间**：2026-04-06

### 📄 论文摘要

Video mashup creation represents a complex video editing paradigm that recomposes existing footage to craft engaging audio-visual experiences, demanding intricate orchestration across semantic, visual, and auditory dimensions and multiple levels. However, existing automated editing frameworks often overlook the cross-level multimodal orchestration to achieve professional-grade fluidity, resulting in disjointed sequences with abrupt visual transitions and musical misalignment. To address this, we formulate video mashup creation as a Multimodal Coherency Satisfaction Problem (MMCSP) and propose the DIRECT framework. Simulating a professional production pipeline, our hierarchical multi-agent framework decomposes the challenge into three cascade levels: the Screenwriter for source-aware global structural anchoring, the Director for instantiating adaptive editing intent and guidance, and the Editor for intent-guided shot sequence editing with fine-grained optimization. We further introduce Mashup-Bench, a comprehensive benchmark with tailored metrics for visual continuity and auditory alignment. Extensive experiments demonstrate that DIRECT significantly outperforms state-of-the-art baselines in both objective metrics and human subjective evaluation. Project page and code: https://github.com/AK-DREAM/DIRECT

### 🤖 AI 总结

**一句话总结**：DIRECT 将视频混剪建模为“多模态一致性满足问题”，通过分层多智能体规划与意图引导编辑，实现更连贯的画面过渡与更对齐的音乐节奏。

**研究动机**：现有自动化视频剪辑方法往往缺乏跨层级的多模态协同（语义/视觉/听觉），导致片段拼接生硬、转场突兀以及音乐与画面不同步，难以达到专业级流畅度。

**核心方法**：提出 DIRECT 分层多智能体框架，模拟制作流程分为三层：Screenwriter 负责基于素材的全局结构锚定，Director 生成自适应剪辑意图与指导，Editor 在意图约束下进行镜头序列编辑并做细粒度优化；同时构建 Mashup-Bench 基准与针对视觉连续性、听觉对齐的评测指标。

**主要结论**：在新基准 Mashup-Bench 上，DIRECT 在客观指标与人类主观评测中均显著优于现有方法，生成的混剪在视觉连贯性与音乐对齐方面更稳定、更专业。

**关键词**：视频混剪生成, 分层多智能体规划, 意图引导剪辑, 多模态一致性约束, 语义-视觉-音频协同, 全局结构锚定, 镜头序列优化, 视觉连续性评估, 音频节奏对齐

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04875v1) | [下载PDF](https://arxiv.org/pdf/2604.04875v1.pdf)

---

## [20. The Blind Spot of Adaptation: Quantifying and Mitigating Forgetting in Fine-tuned Driving Models](https://arxiv.org/abs/2604.04857v1)

**作者**：Runhao Mao, Hanshi Wang, Yixiang Yang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

The integration of Vision-Language Models (VLMs) into autonomous driving promises to solve long-tail scenarios, but this paradigm faces the critical and unaddressed challenge of catastrophic forgetting. The very fine-tuning process used to adapt these models to driving-specific data simultaneously erodes their invaluable pre-trained world knowledge, creating a self-defeating paradox that undermines the core reason for their use. This paper provides the first systematic investigation into this phenomenon. We introduce a new large-scale dataset of 180K scenes, which enables the first-ever benchmark specifically designed to quantify catastrophic forgetting in autonomous driving. Our analysis reveals that existing methods suffer from significant knowledge degradation. To address this, we propose the Drive Expert Adapter (DEA), a novel framework that circumvents this trade-off by shifting adaptation from the weight space to the prompt space. DEA dynamically routes inference through different knowledge experts based on scene-specific cues, enhancing driving-task performance without corrupting the model's foundational parameters. Extensive experiments demonstrate that our approach not only achieves state-of-the-art results on driving tasks but also effectively mitigates catastrophic forgetting, preserving the essential generalization capabilities that make VLMs a transformative force for autonomous systems. Data and model are released at FidelityDrivingBench.

### 🤖 AI 总结

**一句话总结**：论文系统量化了自动驾驶VLM微调带来的灾难性遗忘，并提出通过“提示空间适配+专家路由”的DEA在提升驾驶任务效果的同时尽量保留预训练通用知识。

**研究动机**：将VLM用于自动驾驶能覆盖长尾场景，但常规微调会破坏其预训练世界知识，形成“适配越多、通用能力越差”的悖论。该问题此前缺乏专门基准与系统性评估，因此需要可量化遗忘的 benchmark 并寻找不损伤底座知识的适配方式。

**核心方法**：作者构建180K场景的大规模数据集与基准，用于同时评估驾驶任务表现与遗忘程度。提出Drive Expert Adapter（DEA），将适配从权重更新转到prompt/适配器层，并根据场景线索动态路由到不同“知识专家”，避免改动基础参数造成知识退化。

**主要结论**：实验显示现有方法在微调后存在显著知识降解，而DEA能在驾驶任务上达到/超过SOTA并显著缓解灾难性遗忘。结果表明通过prompt空间的专家化与动态选择，可以更好地兼顾任务适配与通用知识保留。

**关键词**：自动驾驶VLM, 灾难性遗忘, 微调退化评测, 驾驶遗忘基准, 18万场景数据集, 世界知识保留, 提示空间适配, 动态专家路由, 参数冻结适配, 长尾场景泛化

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04857v1) | [下载PDF](https://arxiv.org/pdf/2604.04857v1.pdf)

---

## [21. InfBaGel: Human-Object-Scene Interaction Generation with Dynamic Perception and Iterative Refinement](https://arxiv.org/abs/2604.04843v1)

**作者**：Yude Zou, Junji Gong, Xing Gao 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-06

### 📄 论文摘要

Human-object-scene interactions (HOSI) generation has broad applications in embodied AI, simulation, and animation. Unlike human-object interaction (HOI) and human-scene interaction (HSI), HOSI generation requires reasoning over dynamic object-scene changes, yet suffers from limited annotated data. To address these issues, we propose a coarse-to-fine instruction-conditioned interaction generation framework that is explicitly aligned with the iterative denoising process of a consistency model. In particular, we adopt a dynamic perception strategy that leverages trajectories from the preceding refinement to update scene context and condition subsequent refinement at each denoising step of consistency model, yielding consistent interactions. To further reduce physical artifacts, we introduce a bump-aware guidance that mitigates collisions and penetrations during sampling without requiring fine-grained scene geometry, enabling real-time generation. To overcome data scarcity, we design a hybrid training startegy that synthesizes pseudo-HOSI samples by injecting voxelized scene occupancy into HOI datasets and jointly trains with high-fidelity HSI data, allowing interaction learning while preserving realistic scene awareness. Extensive experiments demonstrate that our method achieves state-of-the-art performance in both HOSI and HOI generation, and strong generalization to unseen scenes. Project page: https://yudezou.github.io/InfBaGel-page/

### 🤖 AI 总结

**一句话总结**：提出InfBaGel：通过动态感知与迭代细化，在一致性模型的去噪过程中生成更一致、物理更合理的人-物-场（HOSI）交互。

**研究动机**：HOSI生成相比HOI/HSI需要考虑对象与场景的动态变化，但标注数据稀缺且容易产生碰撞/穿插等物理伪影，限制了真实可用的交互生成。

**核心方法**：构建与一致性模型迭代去噪对齐的coarse-to-fine指令条件生成框架：在每步细化中用“动态感知”基于上一轮轨迹更新场景上下文，并引入无需精细几何的“bump-aware”引导以减少碰撞与穿插；同时用混合训练策略，将HOI数据注入体素化场景占用合成伪HOSI样本，并与高保真HSI数据联合训练缓解数据不足。

**主要结论**：实验表明该方法在HOSI与HOI生成上达到SOTA，并能在未见过的场景上保持较强泛化，同时实现更少物理伪影且支持实时生成。

**关键词**：人-物-场交互生成, 一致性模型, 迭代去噪, 指令条件生成, 动态感知, 粗到细生成, 碰撞与穿透抑制, 体素占据表示, 伪HOSI数据合成, 混合训练策略, 跨场景泛化

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04843v1) | [下载PDF](https://arxiv.org/pdf/2604.04843v1.pdf)

---

## [22. Less Detail, Better Answers: Degradation-Driven Prompting for VQA](https://arxiv.org/abs/2604.04838v1)

**作者**：Haoxuan Han, Weijie Wang, Zeyu Zhang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-06

### 📄 论文摘要

Recent advancements in Vision-Language Models (VLMs) have significantly pushed the boundaries of Visual Question Answering (VQA).However,high-resolution details can sometimes become noise that leads to hallucinations or reasoning errors. In this paper,we propose Degradation-Driven Prompting (DDP), a novel framework that improves VQA performance by strategically reducing image fidelity to force models to focus on essential structural information. We evaluate DDP across two distinct tasks. Physical attributes targets images prone to human misjudgment, where DDP employs a combination of 80p downsampling, structural visual aids (white background masks and orthometric lines), and In-Context Learning (ICL) to calibrate the model's focus. Perceptual phenomena addresses various machine-susceptible visual anomalies and illusions, including Visual Anomaly (VA), Color (CI), Motion(MI),Gestalt (GI), Geometric (GSI), and Visual Illusions (VI).For this task, DDP integrates a task-classification stage with specialized tools such as blur masks and contrast enhancement alongside downsampling. Our experimental results demonstrate that less is more: by intentionally degrading visual inputs and providing targeted structural prompts, DDP enables VLMs to bypass distracting textures and achieve superior reasoning accuracy on challenging visual benchmarks.

### 🤖 AI 总结

**一句话总结**：Recent advancements in Vision-Language Models (VLMs) have significantly pushed the boundaries of Visual Question Answering (VQA).However,high-resolution details can sometimes become noise that leads t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：视觉问答, 视觉语言模型, 退化驱动提示, 图像降采样, 结构化视觉提示, 幻觉抑制, 上下文学习, 视觉错觉, 感知异常检测, 任务分类, 模糊掩码

**评分**：72

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04838v1) | [下载PDF](https://arxiv.org/pdf/2604.04838v1.pdf)

---

## [23. E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes](https://arxiv.org/abs/2604.04834v1)

**作者**：Jiajun Zhai, Hao Shi, Shangwei Guo 等 5 位作者  
**分类**：cs.CV, cs.MM, cs.RO, eess.IV  
**发布时间**：2026-04-06

### 📄 论文摘要

Robotic Vision-Language-Action (VLA) models generalize well for open-ended manipulation, but their perception is fragile under sensing-stage degradations such as extreme low light, motion blur, and black clipping. We present E-VLA, an event-augmented VLA framework that improves manipulation robustness when conventional frame-based vision becomes unreliable. Instead of reconstructing images from events, E-VLA directly leverages motion and structural cues in event streams to preserve semantic perception and perception-action consistency under adverse conditions. We build an open-source teleoperation platform with a DAVIS346 event camera and collect a real-world synchronized RGB-event-action manipulation dataset across diverse tasks and illumination settings. We also propose lightweight, pretrained-compatible event integration strategies and study event windowing and fusion for stable deployment. Experiments show that even a simple parameter-free fusion, i.e., overlaying accumulated event maps onto RGB images, could substantially improve robustness in dark and blur-heavy scenes: on Pick-Place at 20 lux, success increases from 0% (image-only) to 60% with overlay fusion and to 90% with our event adapter; under severe motion blur (1000 ms exposure), Pick-Place improves from 0% to 20-25%, and Sorting from 5% to 32.5%. Overall, E-VLA provides systematic evidence that event-driven perception can be effectively integrated into VLA models, pointing toward robust embodied intelligence beyond conventional frame-based imaging. Code and dataset will be available at https://github.com/JJayzee/E-VLA.

### 🤖 AI 总结

**一句话总结**：E-VLA通过将事件相机的运动/结构信息直接融入Vision-Language-Action模型，使机器人在极暗与严重运动模糊场景下的操作成功率显著提升。

**研究动机**：现有VLA在开放式操控上泛化强，但在低照度、运动模糊、黑场截断等传感退化下视觉语义不稳定，导致感知与动作不一致、任务成功率骤降。事件相机对亮度变化与高速运动更敏感，具备在恶劣成像条件下补足传统帧相机的潜力。

**核心方法**：提出E-VLA框架：不做事件到图像的重建，而是直接利用事件流的结构与运动线索，并设计轻量、可兼容预训练模型的事件融合策略（包括简单的事件累积图与RGB叠加的无参数融合，以及更强的event adapter），同时研究事件时间窗口与融合方式以提升部署稳定性。构建含DAVIS346的开源遥操作平台并采集同步RGB-事件-动作的真实操控数据集用于训练与评测。

**主要结论**：实验表明事件信息能系统性提升VLA在暗光与模糊下的鲁棒性：如Pick-Place在20 lux从图像单模态0%提升到叠加融合60%、event adapter 90%；在1000ms曝光的严重模糊下Pick-Place从0%到20–25%，Sorting从5%到32.5%。结果证明事件驱动感知可有效与VLA整合，为突破纯帧视觉限制的具身智能提供可行路径。

**关键词**：事件相机, 事件流融合, 视觉-语言-动作模型, 鲁棒机器人操作, 低光照感知, 运动模糊, 黑场剪切, RGB-事件-动作数据集, 遥操作采集, 事件窗口化, 事件适配器

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04834v1) | [下载PDF](https://arxiv.org/pdf/2604.04834v1.pdf)

---

## [24. Multi-Modal Sensor Fusion using Hybrid Attention for Autonomous Driving](https://arxiv.org/abs/2604.04797v1)

**作者**：Mayank Mayank, Bharanidhar Duraisamy, Florian Geiß 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Accurate 3D object detection for autonomous driving requires complementary sensors. Cameras provide dense semantics but unreliable depth, while millimeter-wave radar offers precise range and velocity measurements with sparse geometry. We propose MMF-BEV, a radar-camera BEV fusion framework that leverages deformable attention for cross-modal feature alignment on the View-of-Delft (VoD) 4D radar dataset [1]. MMF-BEV builds a BEVDepth [2] camera branch and a RadarBEVNet [3] radar branch, each enhanced with Deformable Self-Attention, and fuses them via a Deformable Cross-Attention module. We evaluate three configurations: camera-only, radar-only, and hybrid fusion. A sensor contribution analysis quantifies per-distance modality weighting, providing interpretable evidence of sensor complementarity. A two-stage training strategy - pre-training the camera branch with depth supervision, then jointly training radar and fusion modules stabilizes learning. Experiments on VoD show that MMF-BEV consistently outperforms unimodal baselines and achieves competitive results against prior fusion methods across all object classes in both the full annotated area and near-range Region of Interest.

### 🤖 AI 总结

**一句话总结**：MMF-BEV通过可变形注意力在BEV空间对齐并融合相机与4D毫米波雷达特征，在VoD数据集上实现了优于单模态的3D目标检测性能。

**研究动机**：自动驾驶3D检测需要互补传感器：相机语义密集但深度不稳，雷达测距/测速准确但几何稀疏，因此需要有效的跨模态对齐与融合来提升鲁棒性。

**核心方法**：构建相机BEVDepth分支与雷达RadarBEVNet分支，并在各自分支中加入可变形自注意力；随后用可变形交叉注意力进行跨模态特征对齐与BEV融合，并采用“两阶段训练”（相机分支先用深度监督预训练，再联合训练雷达与融合模块）稳定优化。

**主要结论**：在VoD的全标注区域与近距ROI上，融合模型一致优于相机-only与雷达-only基线并与现有融合方法具有竞争力；传感器贡献分析还显示不同距离下两种模态的权重互补，提供了可解释的融合收益证据。

**关键词**：自动驾驶, 3D目标检测, 雷达-相机融合, BEV特征融合, 可变形注意力, 跨模态对齐, 自注意力增强, 交叉注意力模块, 深度监督预训练, 传感器贡献分析, 4D毫米波雷达

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04797v1) | [下载PDF](https://arxiv.org/pdf/2604.04797v1.pdf)

---

## cs.LG

## [25. Empowering Power Outage Prediction with Spatially Aware Hybrid Graph Neural Networks and Contrastive Learning](https://arxiv.org/abs/2604.04916v1)

**作者**：Xuyang Shen, Zijie Pan, Diego Cerrai 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Extreme weather events, such as severe storms, hurricanes, snowstorms, and ice storms, which are exacerbated by climate change, frequently cause widespread power outages. These outages halt industrial operations, impact communities, damage critical infrastructure, profoundly disrupt economies, and have far-reaching effects across various sectors. To mitigate these effects, the University of Connecticut and Eversource Energy Center have developed an outage prediction modeling (OPM) system to provide pre-emptive forecasts for electric distribution networks before such weather events occur. However, existing predictive models in the system do not incorporate the spatial effect of extreme weather events. To this end, we develop Spatially Aware Hybrid Graph Neural Networks (SA-HGNN) with contrastive learning to enhance the OPM predictions for extreme weather-induced power outages. Specifically, we first encode spatial relationships of both static features (e.g., land cover, infrastructure) and event-specific dynamic features (e.g., wind speed, precipitation) via Spatially Aware Hybrid Graph Neural Networks (SA-HGNN). Next, we leverage contrastive learning to handle the imbalance problem associated with different types of extreme weather events and generate location-specific embeddings by minimizing intra-event distances between similar locations while maximizing inter-event distances across all locations. Thorough empirical studies in four utility service territories, i.e., Connecticut, Western Massachusetts, Eastern Massachusetts, and New Hampshire, demonstrate that SA-HGNN can achieve state-of-the-art performance for power outage prediction.

### 🤖 AI 总结

**一句话总结**：论文提出结合空间感知混合图神经网络与对比学习的SA-HGNN，用于在极端天气来临前更准确预测配电网停电范围与程度。

**研究动机**：现有停电预测系统未充分建模极端天气影响的空间相关性，且不同天气事件样本分布不均衡会削弱模型泛化能力。

**核心方法**：用SA-HGNN将静态特征（地表覆盖、基础设施等）与事件动态特征（风速、降水等）的空间关系编码到图表示中；再通过对比学习缓解类别不平衡，拉近同类事件中相似地点的表示、拉远跨事件表示以获得位置特定嵌入。

**主要结论**：在康涅狄格、西马、东马和新罕布什尔四个服务区域的实证结果表明，SA-HGNN在极端天气导致的停电预测任务上达到SOTA表现。

**关键词**：停电预测, 极端天气, 电力配电网络, 空间建模, 混合图神经网络, 时空特征融合, 类别不平衡处理, 位置嵌入表示, 多区域实证评测

**评分**：69

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04916v1) | [下载PDF](https://arxiv.org/pdf/2604.04916v1.pdf)

---

## [26. Data Attribution in Adaptive Learning](https://arxiv.org/abs/2604.04892v1)

**作者**：Amit Kiran Rege  
**分类**：cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Machine learning models increasingly generate their own training data -- online bandits, reinforcement learning, and post-training pipelines for language models are leading examples. In these adaptive settings, a single training observation both updates the learner and shifts the distribution of future data the learner will collect. Standard attribution methods, designed for static datasets, ignore this feedback. We formalize occurrence-level attribution for finite-horizon adaptive learning via a conditional interventional target, prove that replay-side information cannot recover it in general, and identify a structural class in which the target is identified from logged data.

### 🤖 AI 总结

**一句话总结**：Machine learning models increasingly generate their own training data -- online bandits, reinforcement learning, and post-training pipelines for language models are leading examples. In these adaptive...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：自适应学习, 数据归因, 发生级归因, 强化学习, 后训练数据生成, 条件干预目标, 有限时域, 因果识别, 日志数据, 重放信息局限

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04892v1) | [下载PDF](https://arxiv.org/pdf/2604.04892v1.pdf)

---

## [27. Optimizing LLM Prompt Engineering with DSPy Based Declarative Learning](https://arxiv.org/abs/2604.04869v1)

**作者**：Shiek Ruksana, Sailesh Kiran Kurra, Thipparthi Sanjay Baradwaj  
**分类**：cs.LG  
**发布时间**：2026-04-06

### 📄 论文摘要

Large Language Models (LLMs) have shown strong performance across a wide range of natural language processing tasks; however, their effectiveness is highly dependent on prompt design, structure, and embedded reasoning signals. Conventional prompt engineering methods largely rely on heuristic trial-and-error processes, which limits scalability, reproducibility, and generalization across tasks. DSPy, a declarative framework for optimizing text-processing pipelines, offers an alternative approach by enabling automated, modular, and learnable prompt construction for LLM-based systems.This paper presents a systematic study of DSPy-based declarative learning for prompt optimization, with emphasis on prompt synthesis, correction, calibration, and adaptive reasoning control. We introduce a unified DSPy LLM architecture that combines symbolic planning, gradient free optimization, and automated module rewriting to reduce hallucinations, improve factual grounding, and avoid unnecessary prompt complexity. Experimental evaluations conducted on reasoning tasks, retrieval-augmented generation, and multi-step chain-of-thought benchmarks demonstrate consistent gains in output reliability, efficiency, and generalization across models. The results show improvements of up to 30 to 45% in factual accuracy and a reduction of approximately 25% in hallucination rates. Finally, we outline key limitations and discuss future research directions for declarative prompt optimization frameworks.

### 🤖 AI 总结

**一句话总结**：论文系统研究用DSPy的声明式学习自动优化LLM提示词与推理控制，在多类任务上显著提升事实准确性并降低幻觉。

**研究动机**：传统提示词工程依赖人工试错，难以规模化、复现且跨任务泛化差；需要一种可模块化、可学习、可自动校准的提示优化方法来提升可靠性与效率。

**核心方法**：基于DSPy构建统一的LLM声明式架构，将符号规划、无梯度优化与自动模块重写结合，用于提示合成/纠错/校准与自适应推理控制，从而减少不必要的提示复杂度并增强事实落地。

**主要结论**：在推理任务、RAG与多步CoT基准上，该框架带来更稳定的输出与更好的泛化，事实准确率提升约30–45%，幻觉率降低约25%，但仍存在若干限制并提出未来方向。

**关键词**：声明式提示优化, 自动提示合成, 提示校正, 提示校准, 自适应推理控制, 梯度自由优化, 模块重写, 符号规划, 幻觉抑制, 事实性对齐

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04869v1) | [下载PDF](https://arxiv.org/pdf/2604.04869v1.pdf)

---

## [28. FairLogue: A Toolkit for Intersectional Fairness Analysis in Clinical Machine Learning Models](https://arxiv.org/abs/2604.04858v1)

**作者**：Nick Souligne, Vignesh Subbian  
**分类**：cs.LG, q-bio.QM  
**发布时间**：2026-04-06

### 📄 论文摘要

Objective: Algorithmic fairness is essential for equitable and trustworthy machine learning in healthcare. Most fairness tools emphasize single-axis demographic comparisons and may miss compounded disparities affecting intersectional populations. This study introduces Fairlogue, a toolkit designed to operationalize intersectional fairness assessment in observational and counterfactual contexts within clinical settings. Methods: Fairlogue is a Python-based toolkit composed of three components: 1) an observational framework extending demographic parity, equalized odds, and equal opportunity difference to intersectional populations; 2) a counterfactual framework evaluating fairness under treatment-based contexts; and 3) a generalized counterfactual framework assessing fairness under interventions on intersectional group membership. The toolkit was evaluated using electronic health record data from the All of Us Controlled Tier V8 dataset in a glaucoma surgery prediction task using logistic regression with race and gender as protected attributes. Results: Observational analysis identified substantial intersectional disparities despite moderate model performance (AUROC = 0.709; accuracy = 0.651). Intersectional evaluation revealed larger fairness gaps than single-axis analyses, including demographic parity differences of 0.20 and equalized odds true positive and false positive rate gaps of 0.33 and 0.15, respectively. Counterfactual analysis using permutation-based null distributions produced unfairness ("u-value") estimates near zero, suggesting observed disparities were consistent with chance after conditioning on covariates. Conclusion: Fairlogue provides a modular toolkit integrating observational and counterfactual methods for quantifying and evaluating intersectional bias in clinical machine learning workflows.

### 🤖 AI 总结

**一句话总结**：FairLogue 提供一个面向临床机器学习的工具包，将观察性与反事实方法结合，用于量化并检验交叉群体（如种族×性别）的公平性差异。

**研究动机**：现有公平性工具多做单一敏感属性（如仅种族或仅性别）对比，容易忽略种族与性别等多属性叠加造成的“交叉不公平”。在医疗场景中，这类隐藏差异可能影响模型的可信与公平落地。

**核心方法**：提出 Python 工具包 FairLogue：在观察性框架中将人口统计均等、均等机会、均等化优势等指标扩展到交叉群体；并提供两类反事实评估（基于治疗情境的反事实与对交叉群体成员身份干预的广义反事实）。用 All of Us EHR 数据在青光眼手术预测（逻辑回归，敏感属性为种族与性别）上进行演示与评估。

**主要结论**：观察性评估显示模型在总体性能中等（AUROC 0.709）时仍存在显著交叉公平差距，且交叉分析揭示的差距大于单轴分析（如人口统计均等差 0.20、TPR/FPR 差 0.33/0.15）。但基于置换构造零分布的反事实“u-value”接近 0，提示在控制协变量后这些差异可能与随机波动一致；总体上该工具包可模块化支持临床工作流中的交叉公平评估。

**关键词**：交叉公平性, 医疗算法公平性, 公平性评估工具包, 观察性公平性指标, 反事实公平性, 干预式反事实分析, 治疗情境公平性, 电子健康记录（EHR）, 受保护属性（种族/性别）

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04858v1) | [下载PDF](https://arxiv.org/pdf/2604.04858v1.pdf)

---

## [29. Selecting Decision-Relevant Concepts in Reinforcement Learning](https://arxiv.org/abs/2604.04808v1)

**作者**：Naveen Raman, Stephanie Milani, Fei Fang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-06

### 📄 论文摘要

Training interpretable concept-based policies requires practitioners to manually select which human-understandable concepts an agent should reason with when making sequential decisions. This selection demands domain expertise, is time-consuming and costly, scales poorly with the number of candidates, and provides no performance guarantees. To overcome this limitation, we propose the first algorithms for principled automatic concept selection in sequential decision-making. Our key insight is that concept selection can be viewed through the lens of state abstraction: intuitively, a concept is decision-relevant if removing it would cause the agent to confuse states that require different actions. As a result, agents should rely on decision-relevant concepts; states with the same concept representation should share the same optimal action, which preserves the optimal decision structure of the original state space. This perspective leads to the Decision-Relevant Selection (DRS) algorithm, which selects a subset of concepts from a candidate set, along with performance bounds relating the selected concepts to the performance of the resulting policy. Empirically, DRS automatically recovers manually curated concept sets while matching or exceeding their performance, and improves the effectiveness of test-time concept interventions across reinforcement learning benchmarks and real-world healthcare environments.

### 🤖 AI 总结

**一句话总结**：Training interpretable concept-based policies requires practitioners to manually select which human-understandable concepts an agent should reason with when making sequential decisions. This selection...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：可解释强化学习, 概念策略, 自动概念选择, 决策相关概念, 状态抽象, 序列决策, 最优动作保持, 性能界限, 测试时概念干预, 强化学习基准评测, 医疗环境强化学习

**评分**：60

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04808v1) | [下载PDF](https://arxiv.org/pdf/2604.04808v1.pdf)

---

## [30. Forgetting to Witness: Efficient Federated Unlearning and Its Visible Evaluation](https://arxiv.org/abs/2604.04800v1)

**作者**：Houzhe Wang, Xiaojie Zhu, Chi Chen  
**分类**：cs.LG, cs.CR  
**发布时间**：2026-04-06

### 📄 论文摘要

With the increasing importance of data privacy and security, federated unlearning has emerged as a novel research field dedicated to ensuring that federated learning models no longer retain or leak relevant information once specific data has been deleted. In this paper, to the best of our knowledge, we propose the first complete pipeline for federated unlearning, which includes a federated unlearning approach and an evaluation framework. Our proposed federated unlearning approach ensures high efficiency and model accuracy without the need to store historical data.It effectively leverages the knowledge distillation model alongside various optimization mechanisms. Moreover, we propose a framework named Skyeye to visualize the forgetting capacity of federated unlearning models. It utilizes the federated unlearning model as the classifier integrated into a Generative Adversarial Network (GAN). Afterward, both the classifier and discriminator guide the generator in generating samples. Throughout this process, the generator learns from the classifier's knowledge. The generator then visualizes this knowledge through sample generation. Finally, the model's forgetting capability is evaluated based on the relevance between the deleted data and the generated samples. Comprehensive experiments are conducted to illustrate the effectiveness of the proposed federated unlearning approach and the corresponding evaluation framework.

### 🤖 AI 总结

**一句话总结**：提出一个无需保存历史数据的高效联邦遗忘（Federated Unlearning）方法，并给出可视化评估框架 Skyeye 以直观衡量模型对已删除数据的“遗忘”程度。

**研究动机**：联邦学习在隐私场景下广泛应用，但当用户数据被要求删除时，现有模型可能仍保留或泄露相关信息；同时，如何在不回溯全量训练、且缺少直观评估手段的情况下验证“确实遗忘”仍是难点。

**核心方法**：作者构建完整联邦遗忘流水线：在遗忘训练侧利用知识蒸馏与多种优化机制实现高效率与精度保持、且不需要存储历史数据；在评估侧提出 Skyeye，将遗忘后的模型作为 GAN 的分类器融入生成过程，由分类器与判别器共同引导生成样本，并通过生成样本与被删除数据的相关性来可视化与量化遗忘能力。

**主要结论**：实验表明该联邦遗忘方法在效率与模型准确率方面表现良好；Skyeye 能生成反映模型知识的样本，从而使遗忘效果以“可见”的方式被评估，并能有效刻画模型对已删除数据的遗忘程度。

**关键词**：联邦遗忘, 联邦学习隐私, 高效遗忘训练, 知识蒸馏, 无历史数据存储, 遗忘能力评估, 可视化评测框架, GAN生成评估, 删除数据泄露检测, 生成样本相关性

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2604.04800v1) | [下载PDF](https://arxiv.org/pdf/2604.04800v1.pdf)

---

