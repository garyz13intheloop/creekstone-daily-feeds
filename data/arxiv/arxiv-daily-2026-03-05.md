# arXiv AI 论文日报 | 2026-03-05

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. A Dual-Helix Governance Approach Towards Reliable Agentic AI for WebGIS Development](https://arxiv.org/abs/2603.04390v1)

**作者**：Boyuan, Guan, Wencong Cui 等 4 位作者  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-03-04

### 📄 论文摘要

WebGIS development requires rigor, yet agentic AI frequently fails due to five large language model (LLM) limitations: context constraints, cross-session forgetting, stochasticity, instruction failure, and adaptation rigidity. We propose a dual-helix governance framework reframing these challenges as structural governance problems that model capacity alone cannot resolve. We implement the framework as a 3-track architecture (Knowledge, Behavior, Skills) that uses a knowledge graph substrate to stabilize execution by externalizing domain facts and enforcing executable protocols, complemented by a self-learning cycle for autonomous knowledge growth. Applying this to the FutureShorelines WebGIS tool, a governed agent refactored a 2,265-line monolithic codebase into modular ES6 components. Results demonstrated a 51\% reduction in cyclomatic complexity and a 7-point increase in maintainability index. A comparative experiment against a zero-shot LLM confirms that externalized governance, not just model capability, drives operational reliability in geospatial engineering. This approach is implemented in the open-source AgentLoom governance toolkit.

### 🤖 AI 总结

**一句话总结**：提出“双螺旋治理”框架，用知识/行为/技能三轨与知识图谱外置治理来提升Agentic AI在WebGIS开发中的可靠性，并在真实项目中显著提升代码可维护性。

**研究动机**：WebGIS工程要求高确定性与可追溯性，但LLM/Agent常受上下文限制、跨会话遗忘、随机性、指令失效与适应僵化影响而不稳定；作者认为这些是“治理结构问题”，仅靠更强模型难以根治。

**核心方法**：设计双螺旋治理框架并落地为三轨架构（Knowledge/Behavior/Skills），以知识图谱作为底座外置领域事实与可执行协议来约束执行，同时引入自学习循环实现自治知识增长与迭代。

**主要结论**：在FutureShorelines WebGIS工具中，受治理的智能体将2265行单体代码重构为模块化ES6组件，使圈复杂度下降51%、可维护性指数提升7点；对比零样本LLM实验表明可靠性主要来自外置治理而非单纯模型能力提升，且已在开源AgentLoom工具包中实现。

**关键词**：智能体治理框架, 双螺旋治理, 可靠性工程, 知识图谱, 外部化知识, 可执行协议, 自学习循环, 代码重构, 可维护性评估

**评分**：48

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04390v1) | [下载PDF](https://arxiv.org/pdf/2603.04390v1.pdf)

---

## [2. $τ$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge](https://arxiv.org/abs/2603.04370v1)

**作者**：Quan Shi, Alexandra Zytek, Pedram Razavi 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.IR  
**发布时间**：2026-03-04

### 📄 论文摘要

Conversational agents are increasingly deployed in knowledge-intensive settings, where correct behavior depends on retrieving and applying domain-specific knowledge from large, proprietary, and unstructured corpora during live interactions with users. Yet most existing benchmarks evaluate retrieval or tool use independently of each other, creating a gap in realistic, fully agentic evaluation over unstructured data in long-horizon interactions. We introduce $τ$-Knowledge, an extension of $τ$-Bench for evaluating agents in environments where success depends on coordinating external, natural-language knowledge with tool outputs to produce verifiable, policy-compliant state changes. Our new domain, $τ$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates. Across embedding-based retrieval and terminal-based search, even frontier models with high reasoning budgets achieve only $\sim$25.5% pass^1, with reliability degrading sharply over repeated trials. Agents struggle to retrieve the correct documents from densely interlinked knowledge bases and to reason accurately over complex internal policies. Overall, $τ$-Knowledge provides a realistic testbed for developing agents that integrate unstructured knowledge in human-facing deployments.

### 🤖 AI 总结

**一句话总结**：提出τ-Knowledge基准，用于评估对话式智能体在长流程交互中结合非结构化知识与工具操作的真实能力，结果显示前沿模型通过率仅约25.5%。

**研究动机**：现有基准往往将检索与工具使用分开评测，难以反映智能体在真实部署中需从大型私有非结构化语料检索并遵循内部政策完成可验证操作的整体能力。

**核心方法**：在τ-Bench上扩展出τ-Knowledge，并构建τ-Banking环境：智能体需在约700份互相关联的知识文档中检索信息（嵌入检索或终端搜索），结合工具输出来执行符合政策的账户状态变更并可被验证。

**主要结论**：即使高推理预算的前沿模型整体通过率仍低（~25.5%），且多次重复试验可靠性显著下降；主要瓶颈在于密集互链知识库中的正确文档检索与对复杂内部政策的准确推理，表明该基准能有效暴露真实部署中的关键难点。

**关键词**：非结构化知识检索, 知识密集对话, 长程交互, 检索增强生成（RAG）, 多文档推理, 策略合规执行, 可验证状态变更, 金融客服流程, 智能体可靠性评测

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04370v1) | [下载PDF](https://arxiv.org/pdf/2603.04370v1.pdf)

---

## cs.CL

## [3. AgentIR: Reasoning-Aware Retrival for Deep Research Agents](https://arxiv.org/abs/2603.04384v1)

**作者**：Zijian Chen, Xueguang Ma, Shengyao Zhuang 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-04

### 📄 论文摘要

Deep Research agents are rapidly emerging as primary consumers of modern retrieval systems. Unlike human users who issue and refine queries without documenting their intermediate thought processes, Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore. To exploit this overlooked signal, we introduce: (1) Reasoning-Aware Retrieval, a retrieval paradigm that jointly embeds the agent's reasoning trace alongside its query; and (2) DR-Synth, a data synthesis method that generates Deep Research retriever training data from standard QA datasets. We demonstrate that both components are independently effective, and their combination yields a trained embedding model, AgentIR-4B, with substantial gains. On the challenging BrowseComp-Plus benchmark, AgentIR-4B achieves 68\% accuracy with the open-weight agent Tongyi-DeepResearch, compared to 50\% with conventional embedding models twice its size, and 37\% with BM25. Code and data are available at: https://texttron.github.io/AgentIR/.

### 🤖 AI 总结

**一句话总结**：AgentIR提出将研究型智能体的“推理轨迹+查询”联合编码用于检索，并配套合成训练数据方法，显著提升深度研究场景的检索效果。

**研究动机**：深度研究智能体在每次检索前会生成显式自然语言推理，包含丰富意图与上下文，但现有检索器通常只看最终查询而忽略这部分信息，导致检索不匹配。

**核心方法**：提出Reasoning-Aware Retrieval：将智能体推理trace与query一起嵌入并用于相似度检索；提出DR-Synth：从标准QA数据合成适用于深度研究检索训练的数据，进而训练得到AgentIR-4B嵌入模型。

**主要结论**：两项组件各自都能带来提升，组合后效果最佳；在BrowseComp-Plus上，AgentIR-4B配合Tongyi-DeepResearch达到68%准确率，显著优于更大常规模型（50%）和BM25（37%）。

**关键词**：深度研究智能体, 推理感知检索, 推理轨迹建模, 查询-推理联合嵌入, 稠密检索, 文本嵌入模型, 检索器训练数据合成, QA数据集迁移, BM25基线

**评分**：50

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04384v1) | [下载PDF](https://arxiv.org/pdf/2603.04384v1.pdf)

---

## [4. AILS-NTUA at SemEval-2026 Task 12: Graph-Based Retrieval and Reflective Prompting for Abductive Event Reasoning](https://arxiv.org/abs/2603.04319v1)

**作者**：Nikolas Karafyllis, Maria Lymperaiou, Giorgos Filandrianos 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-04

### 📄 论文摘要

We present a winning three-stage system for SemEval 2026 Task~12: Abductive Event Reasoning that combines graph-based retrieval, LLM-driven abductive reasoning with prompt design optimized through reflective prompt evolution, and post-hoc consistency enforcement; our system ranks first on the evaluation-phase leaderboard with an accuracy score of 0.95. Cross-model error analysis across 14 models (7~families) reveals three shared inductive biases: causal chain incompleteness, proximate cause preference, and salience bias, whose cross-family convergence (51\% cause-count reduction) indicates systematic rather than model-specific failure modes in multi-label causal reasoning.

### 🤖 AI 总结

**一句话总结**：提出一个三阶段系统，将图检索增强、反思式提示优化的LLM溯因推理与一致性后处理结合，在SemEval-2026任务12中以0.95准确率夺冠，并归纳出多模型共有的系统性错误偏置。

**研究动机**：溯因事件推理需要在多标签因果候选中补全隐含因果链，现有模型易受信息缺失与显著性干扰而产生稳定错误。作者旨在通过检索与提示工程提升因果证据覆盖，并系统分析不同模型家族的共同失败模式。

**核心方法**：三阶段流程：①基于图结构的检索为事件提供相关因果证据/候选；②使用LLM进行溯因推理，并通过“反思式提示演化”迭代优化提示以提升推理质量；③对输出进行事后一致性约束/校正，减少自相矛盾与不完整因果链。

**主要结论**：系统在评测榜上排名第一（Accuracy=0.95），验证了图检索+反思式提示+一致性约束对多标签因果推理的有效性。跨14个模型的误差分析发现三类共享归纳偏置（因果链不完整、偏好近因、显著性偏置），且跨家族收敛表明这是系统性而非单一模型问题。

**关键词**：溯因事件推理, 多标签因果推理, 图检索, 检索增强推理, 提示词优化, 反思式提示演化, 一致性约束, 跨模型误差分析, 归纳偏置, 因果链不完整, 显著性偏置, 近因偏好

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04319v1) | [下载PDF](https://arxiv.org/pdf/2603.04319v1.pdf)

---

## [5. World Properties without World Models: Recovering Spatial and Temporal Structure from Co-occurrence Statistics in Static Word Embeddings](https://arxiv.org/abs/2603.04317v1)

**作者**：Elan Barenholtz  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Recent work interprets the linear recoverability of geographic and temporal variables from large language model (LLM) hidden states as evidence for world-like internal representations. We test a simpler possibility: that much of the relevant structure is already latent in text itself. Applying the same class of ridge regression probes to static co-occurrence-based embeddings (GloVe and Word2Vec), we find substantial recoverable geographic signal and weaker but reliable temporal signal, with held-out R^2 values of 0.71-0.87 for city coordinates and 0.48-0.52 for historical birth years. Semantic-neighbor analyses and targeted subspace ablations show that these signals depend strongly on interpretable lexical gradients, especially country names and climate-related vocabulary. These findings suggest that ordinary word co-occurrence preserves richer spatial, temporal, and environmental structure than is often assumed, revealing a remarkable and underappreciated capacity of simple static embeddings to preserve world-shaped structure from text alone. Linear probe recoverability alone therefore does not establish a representational move beyond text.

### 🤖 AI 总结

**一句话总结**：论文表明：仅凭静态词向量（GloVe/Word2Vec）的共现统计，就能线性恢复出相当强的地理信息与一定的时间信息，因此“可线性探测”并不足以证明模型学到了超越文本的世界模型。

**研究动机**：以往研究将LLM隐状态中可线性读出的地理/时间变量视为“内部世界表征”的证据；作者质疑这些结构是否其实已潜藏在文本共现规律里。

**核心方法**：对GloVe和Word2Vec应用与LLM研究相同的岭回归线性探针，预测城市经纬度与历史人物出生年份，并用语义邻居分析与定向子空间消融定位信号来源（如国家名、气候相关词汇）。

**主要结论**：静态共现词向量可高精度恢复城市坐标（R^2≈0.71–0.87），并稳定但较弱地恢复时间信息（R^2≈0.48–0.52）；这些信号主要依赖可解释的词汇梯度，说明文本共现本身已编码丰富的“世界形”结构，线性可恢复性不能单独证明存在世界模型。

**关键词**：静态词向量, 共现统计, 线性探测, 岭回归探针, 地理坐标回归, 时间信号预测, 语义邻居分析, 子空间消融, 词汇梯度可解释性, 世界模型证据检验

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04317v1) | [下载PDF](https://arxiv.org/pdf/2603.04317v1.pdf)

---

## [6. $V_1$: Unifying Generation and Self-Verification for Parallel Reasoners](https://arxiv.org/abs/2603.04304v1)

**作者**：Harman Singh, Xiuyu Li, Kusha Sareen 等 17 位作者  
**分类**：cs.CL  
**发布时间**：2026-03-04

### 📄 论文摘要

Test-time scaling for complex reasoning tasks shows that leveraging inference-time compute, by methods such as independently sampling and aggregating multiple solutions, results in significantly better task outcomes. However, a critical bottleneck is verification: sampling is only effective if correct solutions can be reliably identified among candidates. While existing approaches typically evaluate candidates independently via scalar scoring, we demonstrate that models are substantially stronger at pairwise self-verification. Leveraging this insight, we introduce $V_1$, a framework that unifies generation and verification through efficient pairwise ranking. $V_1$ comprises two components: $V_1$-Infer, an uncertainty-guided algorithm using a tournament-based ranking that dynamically allocates self-verification compute to candidate pairs whose relative correctness is most uncertain; and $V_1$-PairRL, an RL framework that jointly trains a single model as both generator and pairwise self-verifier, ensuring the verifier adapts to the generator's evolving distribution. On code generation (LiveCodeBench, CodeContests, SWE-Bench) and math reasoning (AIME, HMMT) benchmarks, $V_1$-Infer improves Pass@1 by up to $10%$ over pointwise verification and outperforms recent test-time scaling methods while being significantly more efficient. Furthermore, $V_1$-PairRL achieves $7$--$9%$ test-time scaling gains over standard RL and pointwise joint training, and improves base Pass@1 by up to 8.7% over standard RL in a code-generation setting.

### 🤖 AI 总结

**一句话总结**：V1通过将候选解的生成与“成对自验证”统一起来，用更高效的成对排序替代点式打分，从而在推理/代码任务的test-time scaling中显著提升准确率与效率。

**研究动机**：多采样聚合能提升复杂推理表现，但瓶颈在于如何可靠地从候选中识别正确解；作者发现模型做“成对比较谁更可能正确”比对单个候选做标量评分更强。

**核心方法**：提出V1框架：V1-Infer用不确定性引导的锦标赛式成对排名，把验证算力动态分配给最“难分胜负”的候选对；V1-PairRL用强化学习把同一个模型同时训练为生成器与成对验证器，使验证器随生成分布共同演化并保持匹配。

**主要结论**：在代码（LiveCodeBench/CodeContests/SWE-Bench）与数学（AIME/HMMT）基准上，V1-Infer相对点式验证可将Pass@1最高提升约10%且更高效，并优于近期test-time scaling方法；V1-PairRL相对标准RL与点式联合训练带来约7–9%的test-time scaling增益，并在代码场景中将基础Pass@1最高再提高8.7%。

**关键词**：测试时扩展, 推理时计算分配, 候选采样聚合, 自验证, 成对验证, 成对排序, 不确定性引导, 锦标赛排序, 生成-验证联合训练, 强化学习（RL）, 代码生成评测, 数学推理评测

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04304v1) | [下载PDF](https://arxiv.org/pdf/2603.04304v1.pdf)

---

## cs.CV

## [7. SimpliHuMoN: Simplifying Human Motion Prediction](https://arxiv.org/abs/2603.04399v1)

**作者**：Aadya Agrawal, Alexander Schwing  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Human motion prediction combines the tasks of trajectory forecasting and human pose prediction. For each of the two tasks, specialized models have been developed. Combining these models for holistic human motion prediction is non-trivial, and recent methods have struggled to compete on established benchmarks for individual tasks. To address this, we propose a simple yet effective transformer-based model for human motion prediction. The model employs a stack of self-attention modules to effectively capture both spatial dependencies within a pose and temporal relationships across a motion sequence. This simple, streamlined, end-to-end model is sufficiently versatile to handle pose-only, trajectory-only, and combined prediction tasks without task-specific modifications. We demonstrate that this approach achieves state-of-the-art results across all tasks through extensive experiments on a wide range of benchmark datasets, including Human3.6M, AMASS, ETH-UCY, and 3DPW.

### 🤖 AI 总结

**一句话总结**：提出一个简洁的Transformer端到端模型SimpliHuMoN，用统一架构同时做好人体姿态、轨迹及其联合的人体运动预测，并在多数据集上达到SOTA。

**研究动机**：现有方法往往分别为轨迹预测和姿态预测设计专门模型，二者融合成完整人体运动预测较复杂，且联合模型在各自经典基准上常难以与单任务模型竞争。

**核心方法**：使用堆叠的自注意力模块同时建模姿态内部的空间依赖与序列跨时间的动态关系，以同一套网络在不做任务特定改动的情况下支持pose-only、trajectory-only和combined预测。

**主要结论**：在Human3.6M、AMASS、ETH-UCY、3DPW等多种基准上通过大量实验验证，该简化的Transformer方案在三类任务上均取得最先进性能，显示统一端到端建模的有效性与泛化性。

**关键词**：人体运动预测, 轨迹预测, 人体姿态预测, 自注意力, 时空建模, 端到端学习, 多任务统一模型, 姿态序列建模

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04399v1) | [下载PDF](https://arxiv.org/pdf/2603.04399v1.pdf)

---

## [8. ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training](https://arxiv.org/abs/2603.04385v1)

**作者**：Haian Jin, Rundi Wu, Tianyuan Zhang 等 7 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Feed-forward transformer models have driven rapid progress in 3D vision, but state-of-the-art methods such as VGGT and $π^3$ have a computational cost that scales quadratically with the number of input images, making them inefficient when applied to large image collections. Sequential-reconstruction approaches reduce this cost but sacrifice reconstruction quality. We introduce ZipMap, a stateful feed-forward model that achieves linear-time, bidirectional 3D reconstruction while matching or surpassing the accuracy of quadratic-time methods. ZipMap employs test-time training layers to zip an entire image collection into a compact hidden scene state in a single forward pass, enabling reconstruction of over 700 frames in under 10 seconds on a single H100 GPU, more than $20\times$ faster than state-of-the-art methods such as VGGT. Moreover, we demonstrate the benefits of having a stateful representation in real-time scene-state querying and its extension to sequential streaming reconstruction.

### 🤖 AI 总结

**一句话总结**：ZipMap 提出一种具备“场景状态”的前馈式3D重建模型，通过线性时间处理大规模图像集合，在速度大幅提升的同时达到或超过二次复杂度方法的精度。

**研究动机**：现有基于Transformer的SOTA 3D重建（如VGGT、π^3）计算量随输入图像数呈二次增长，难以扩展到大规模序列；而顺序式重建虽更快但常损失质量。

**核心方法**：ZipMap 采用“stateful”架构与测试时训练（test-time training）层，在单次前向中将整段图像集合压缩为紧凑的隐藏场景状态，并支持双向（bidirectional）重建与实时状态查询；同时可扩展到流式/在线的顺序重建设置。

**主要结论**：在保证或超越精度的前提下，ZipMap 将计算复杂度降为线性，并展示了显著的推理加速（如单张H100上700+帧<10秒、相对VGGT快20倍以上）；此外，显式场景状态还能支持实时查询并利于流式重建应用。

**关键词**：三维重建, 状态表示, 线性时间推理, 双向重建, 测试时训练（TTT）, 隐藏场景状态, 大规模图像集合重建, 实时场景状态查询, 流式重建, 序列式重建

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04385v1) | [下载PDF](https://arxiv.org/pdf/2603.04385v1.pdf)

---

## [9. TaxonRL: Reinforcement Learning with Intermediate Rewards for Interpretable Fine-Grained Visual Reasoning](https://arxiv.org/abs/2603.04380v1)

**作者**：Maximilian von Klinski, Maximilian Schall  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-03-04

### 📄 论文摘要

Traditional vision-language models struggle with contrastive fine-grained taxonomic reasoning, particularly when distinguishing between visually similar species within the same genus or family. We introduce TaxonRL, a reinforcement learning approach using Group Relative Policy Optimization with intermediate rewards that decomposes the reasoning process into hierarchical taxonomic predictions. Our method incentivizes models to explicitly reason about species-level, genus-level, and family-level features before making final classifications. This structured approach is designed not only to boost accuracy but also to yield a transparent, verifiable decision-making process. On the challenging Birds-to-Words dataset, TaxonRL achieves 91.7\% average accuracy, exceeding human performance (77.3\%) while generating interpretable reasoning traces. We demonstrate strong cross-domain generalization, showing substantial gains in primate and marine species verification. Our results establish that enforcing structured, hierarchical reasoning provides a powerful and transferable framework for fine-grained visual discrimination.

### 🤖 AI 总结

**一句话总结**：TaxonRL 通过带中间奖励的强化学习强制模型按“科-属-种”层级推理，从而在细粒度物种辨别上同时提升准确率与可解释性。

**研究动机**：传统视觉-语言模型在同属/同科的高相似物种对比辨别上容易混淆，且决策过程缺乏可验证的推理痕迹。作者希望用结构化的分类学层级推理来提升细粒度识别鲁棒性与透明度。

**核心方法**：提出 TaxonRL：采用 Group Relative Policy Optimization 的强化学习框架，引入中间奖励，将最终预测分解为依次做出科、属、种的层级预测并对每步显式特征依据进行激励。该训练机制促使模型生成可追踪的分层推理链，同时优化最终分类表现。

**主要结论**：在 Birds-to-Words 数据集上达到 91.7% 平均准确率，超过人类 77.3%，并能输出可解释的推理轨迹。方法还在灵长类与海洋物种验证任务上表现出良好的跨领域泛化，说明层级化约束推理具有可迁移性。

**关键词**：细粒度视觉识别, 视觉语言模型, 分类学推理, 层级分类预测, 中间奖励, 强化学习微调, 组相对策略优化（GRPO）, 可解释推理轨迹, 物种验证, 跨域泛化

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04380v1) | [下载PDF](https://arxiv.org/pdf/2603.04380v1.pdf)

---

## [10. Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)

**作者**：Shenghai Yuan, Yuanyang Yin, Zongjian Li 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

We introduce Helios, the first 14B video generation model that runs at 19.5 FPS on a single NVIDIA H100 GPU and supports minute-scale generation while matching the quality of a strong baseline. We make breakthroughs along three key dimensions: (1) robustness to long-video drifting without commonly used anti-drifting heuristics such as self-forcing, error-banks, or keyframe sampling; (2) real-time generation without standard acceleration techniques such as KV-cache, sparse/linear attention, or quantization; and (3) training without parallelism or sharding frameworks, enabling image-diffusion-scale batch sizes while fitting up to four 14B models within 80 GB of GPU memory. Specifically, Helios is a 14B autoregressive diffusion model with a unified input representation that natively supports T2V, I2V, and V2V tasks. To mitigate drifting in long-video generation, we characterize typical failure modes and propose simple yet effective training strategies that explicitly simulate drifting during training, while eliminating repetitive motion at its source. For efficiency, we heavily compress the historical and noisy context and reduce the number of sampling steps, yielding computational costs comparable to -- or lower than -- those of 1.3B video generative models. Moreover, we introduce infrastructure-level optimizations that accelerate both inference and training while reducing memory consumption. Extensive experiments demonstrate that Helios consistently outperforms prior methods on both short- and long-video generation. We plan to release the code, base model, and distilled model to support further development by the community.

### 🤖 AI 总结

**一句话总结**：Helios 是一个14B自回归扩散视频生成模型，可在单张H100上以19.5FPS实时生成分钟级长视频，并在质量上对标强基线且显著提升长视频稳定性。

**研究动机**：现有长视频生成常出现漂移与重复动作，且依赖自强制/误差库/关键帧等启发式补丁；同时大模型实时推理与训练往往依赖KV-cache、稀疏注意力、量化或复杂并行框架，成本高、落地难。

**核心方法**：提出统一输入表示以原生支持T2V/I2V/V2V，并通过“在训练中显式模拟漂移”的策略来提升长视频鲁棒性、从源头抑制重复运动；在效率上对历史与噪声上下文做强压缩并减少采样步数，同时配合基础设施级推理/训练优化，在不使用常见加速与分布式框架的前提下实现高吞吐与低显存。

**主要结论**：实验表明 Helios 在短视频与长视频生成上均优于以往方法，并在单卡上实现接近实时的分钟级生成；其训练与部署无需复杂并行/加速技巧且显存占用更友好，作者计划开源代码与模型以促进社区发展。

**关键词**：长视频生成, 实时视频生成, 自回归扩散模型, 分钟级视频生成, 视频漂移鲁棒性, 漂移模拟训练, 重复运动抑制, 上下文压缩, 采样步数减少, 统一输入表示, 单卡推理（H100）

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04379v1) | [下载PDF](https://arxiv.org/pdf/2603.04379v1.pdf)

---

## [11. FocusGraph: Graph-Structured Frame Selection for Embodied Long Video Question Answering](https://arxiv.org/abs/2603.04349v1)

**作者**：Tatiana Zemskova, Solomon Andryushenko, Ilya Obrubov 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

The ability to understand long videos is vital for embodied intelligent agents, because their effectiveness depends on how well they can accumulate, organize, and leverage long-horizon perceptual memories. Recently, multimodal LLMs have been gaining popularity for solving the long video understanding task due to their general ability to understand natural language and to leverage world knowledge. However, as the number of frames provided to an MLLM increases, the quality of its responses tends to degrade, and inference time grows. Therefore, when using MLLMs for long video understanding, a crucial step is selecting key frames from the video to answer user queries.   In this work, we develop FocusGraph, a framework for keyframe selection for question answering over long egocentric videos. It leverages a lightweight trainable Scene-Caption LLM Selector that selects query-relevant clips based on their graph-based captions, and a training-free method for selecting keyframes from these clips. Unlike existing methods, the proposed Scene-Caption LLM Selector does not rely on the original sequence of low-resolution frames; instead, it operates on a compact textual representation of the scene. We then design a training-free Patch-wise Sparse-Flow Retention (PSFR) method to select keyframes from the resulting sequence of clips, which are fed into an MLLM to produce the final answer. Together, these components enable FocusGraph to achieve state-of-the-art results on challenging egocentric long-video question answering benchmarks, including FindingDory and HourVideo, while significantly reducing inference time relative to baseline approaches.

### 🤖 AI 总结

**一句话总结**：FocusGraph 通过“文本图结构场景描述→LLM选相关片段→无训练选关键帧”的流程，高效从长第一视角视频中挑选少量关键帧交给多模态大模型回答问题，并在精度与速度上优于基线。

**研究动机**：长视频直接喂给多模态LLM会导致回答质量下降且推理耗时显著增加，因此需要一种能针对问题快速筛出最相关片段/关键帧的选择机制。

**核心方法**：提出轻量可训练的 Scene-Caption LLM Selector：基于视频片段的图结构caption（紧凑文本表示）而非低分辨率帧序列，检索/选择与查询相关的clips；再用无需训练的 PSFR（Patch-wise Sparse-Flow Retention）从选中clips中挑关键帧，最终将关键帧输入MLLM生成答案。

**主要结论**：在 FindingDory 与 HourVideo 等长时程第一视角视频问答基准上达到SOTA，同时相较常见基线显著降低推理时间，证明“文本化场景图选择+无训练关键帧筛选”能兼顾效率与效果。

**关键词**：长视频问答, 具身智能体, 关键帧选择, 查询相关片段检索, 图结构场景描述, 场景字幕生成, 稀疏光流保留, 无训练关键帧抽取, 推理加速

**评分**：39

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04349v1) | [下载PDF](https://arxiv.org/pdf/2603.04349v1.pdf)

---

## [12. Underrepresented in Foundation Model Pretraining Data? A One-Shot Probe](https://arxiv.org/abs/2603.04346v1)

**作者**：Chris Vorster, Mayug Maniparambil, Noel E. O'Connor 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

Large-scale Vision-Language Foundation Models (VLFMs), such as CLIP, now underpin a wide range of computer vision research and applications. VLFMs are often adapted to various domain-specific tasks. However, VLFM performance on novel, specialised, or underrepresented domains remains inconsistent. Evaluating VLFMs typically requires labelled test sets, which are often unavailable for niche domains of interest, particularly those from the Global South. We address this gap by proposing a highly data-efficient method to predict a VLFM's zero-shot accuracy on a target domain using only a single labelled image per class. Our approach uses a Large Language Model to generate plausible counterfactual descriptions of a given image. By measuring the VLFM's ability to distinguish the correct description from these hard negatives, we engineer features that capture the VLFM's discriminative power in its shared embedding space. A linear regressor trained on these similarity scores estimates the VLFM's zero-shot test accuracy across various visual domains with a Pearson-r correlation of 0.96. We demonstrate our method's performance across five diverse datasets, including standard benchmark datasets and underrepresented datasets from Africa. Our work provides a low-cost, reliable tool for probing VLFMs, enabling researchers and practitioners to make informed decisions about data annotation efforts before committing significant resources. The model training code, generated captions and counterfactuals are released here: https://github.com/chris-vorster/PreLabellingProbe.

### 🤖 AI 总结

**一句话总结**：提出一种“一类一张标注图”的探针方法，用LLM生成反事实描述并用相似度特征回归预测VLFM在目标域的零样本准确率。

**研究动机**：许多小众/欠代表领域（尤其全球南方）缺少标注测试集，导致难以评估CLIP等视觉-语言基础模型在目标域的可靠性与是否值得投入标注成本。

**核心方法**：对每类仅给定1张标注图，先用LLM为该图生成多个“看似合理但错误”的反事实描述作为硬负例；再计算VLFM对真描述与负描述的相似度差异等特征，并训练线性回归器由这些特征预测该模型在该域的零样本测试准确率。

**主要结论**：该方法在五个不同数据集上能高相关地估计VLFM零样本准确率（Pearson r≈0.96），且对包含非洲等欠代表数据集同样有效，为低成本预评估与标注决策提供了实用工具。

**关键词**：视觉-语言基础模型, 零样本准确率预测, 单样本探测, LLM生成反事实描述, 困难负样本, 相似度特征工程, 共享嵌入空间判别性, 线性回归评估器, 领域泛化评测, 低标注成本评测, 弱势代表域数据集

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04346v1) | [下载PDF](https://arxiv.org/pdf/2603.04346v1.pdf)

---

## [13. Enhancing Authorship Attribution with Synthetic Paintings](https://arxiv.org/abs/2603.04343v1)

**作者**：Clarissa Loures, Caio Hosken, Luan Oliveira 等 5 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Attributing authorship to paintings is a historically complex task, and one of its main challenges is the limited availability of real artworks for training computational models. This study investigates whether synthetic images, generated through DreamBooth fine-tuning of Stable Diffusion, can improve the performance of classification models in this context. We propose a hybrid approach that combines real and synthetic data to enhance model accuracy and generalization across similar artistic styles. Experimental results show that adding synthetic images leads to higher ROC-AUC and accuracy compared to using only real paintings. By integrating generative and discriminative methods, this work contributes to the development of computer vision techniques for artwork authentication in data-scarce scenarios.

### 🤖 AI 总结

**一句话总结**：通过将DreamBooth微调的Stable Diffusion生成的合成画作与真实画作混合训练，可提升绘画作者归属（authorship attribution）分类模型的准确性与泛化能力。

**研究动机**：绘画作者鉴定长期困难且真实作品数据稀缺，导致模型训练受限、易过拟合并难以适应相近画风的区分需求。

**核心方法**：使用DreamBooth对Stable Diffusion进行艺术家风格微调以生成合成画作，并提出真实+合成数据的混合训练方案来训练判别式分类模型；通过对比仅用真实数据与混合数据的实验评估（如ROC-AUC与Accuracy）。

**主要结论**：引入合成画作能在ROC-AUC和准确率上优于仅用真实画作训练，说明生成式数据增强可在数据匮乏场景下有效提高艺术品作者归属模型的性能与泛化。

**关键词**：绘画作者归属, 艺术品鉴定, 数据稀缺学习, 合成数据增强, Diffusion, 生成-判别联合, 图像分类, 风格泛化, 真实性验证

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04343v1) | [下载PDF](https://arxiv.org/pdf/2603.04343v1.pdf)

---

## [14. Hold-One-Shot-Out (HOSO) for Validation-Free Few-Shot CLIP Adapters](https://arxiv.org/abs/2603.04341v1)

**作者**：Chris Vorster, Mayug Maniparambil, Noel E. O'Connor 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

In many CLIP adaptation methods, a blending ratio hyperparameter controls the trade-off between general pretrained CLIP knowledge and the limited, dataset-specific supervision from the few-shot cases. Most few-shot CLIP adaptation techniques report results by ablation of the blending ratio on the test set or require additional validation sets to select the blending ratio per dataset, and thus are not strictly few-shot. We present a simple, validation-free method for learning the blending ratio in CLIP adaptation. Hold-One-Shot-Out (HOSO) presents a novel approach for CLIP-Adapter-style methods to compete in the newly established validation-free setting. CLIP-Adapter with HOSO (HOSO-Adapter) learns the blending ratio using a one-shot, hold-out set, while the adapter trains on the remaining few-shot support examples. Under the validation-free few-shot protocol, HOSO-Adapter outperforms the CLIP-Adapter baseline by more than 4 percentage points on average across 11 standard few-shot datasets. Interestingly, in the 8- and 16-shot settings, HOSO-Adapter outperforms CLIP-Adapter even with the optimal blending ratio selected on the test set. Ablation studies validate the use of a one-shot hold-out mechanism, decoupled training, and improvements over the naively learnt blending ratio baseline. Code is released here: https://github.com/chris-vorster/HOSO-Adapter

### 🤖 AI 总结

**一句话总结**：提出HOSO：用“留出1个样本”的方式在无需验证集/测试集调参的前提下自动学习CLIP适配中的混合比例，使CLIP-Adapter在严格few-shot设定下显著更强。

**研究动机**：现有few-shot CLIP适配方法通常依赖在测试集上做混合比例消融或额外验证集选超参，破坏了“严格few-shot/无验证”设定；需要一种不引入额外数据即可确定混合比例的方案。

**核心方法**：HOSO将每类few-shot支持集中的1个样本作为hold-out，用其来学习（或选择）预训练CLIP与适配器输出的混合比例，同时适配器仅用剩余样本训练，并采用解耦训练等设计以避免朴素学习比例的不稳定/偏置。

**主要结论**：在11个标准few-shot数据集的无验证协议下，HOSO-Adapter平均比CLIP-Adapter提升4+个百分点；在8/16-shot时甚至超过“在测试集上选到最优混合比例”的CLIP-Adapter，消融验证了one-shot hold-out与解耦训练的有效性。

**关键词**：少样本学习, 免验证集协议, 超参数选择, 混合比例, 一张样本留出, 参数高效微调, 解耦训练, 少样本图像分类, 评测基准

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04341v1) | [下载PDF](https://arxiv.org/pdf/2603.04341v1.pdf)

---

## [15. Balancing Fidelity, Utility, and Privacy in Synthetic Cardiac MRI Generation: A Comparative Study](https://arxiv.org/abs/2603.04340v1)

**作者**：Madhura Edirisooriya, Dasuni Kawya, Ishan Kumarasinghe 等 8 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Deep learning in cardiac MRI (CMR) is fundamentally constrained by both data scarcity and privacy regulations. This study systematically benchmarks three generative architectures: Denoising Diffusion Probabilistic Models (DDPM), Latent Diffusion Models (LDM), and Flow Matching (FM) for synthetic CMR generation. Utilizing a two-stage pipeline where anatomical masks condition image synthesis, we evaluate generated data across three critical axes: fidelity, utility, and privacy. Our results show that diffusion-based models, particularly DDPM, provide the most effective balance between downstream segmentation utility, image fidelity, and privacy preservation under limited-data conditions, while FM demonstrates promising privacy characteristics with slightly lower task-level performance. These findings quantify the trade-offs between cross-domain generalization and patient confidentiality, establishing a framework for safe and effective synthetic data augmentation in medical imaging.

### 🤖 AI 总结

**一句话总结**：论文系统对比DDPM、LDM与Flow Matching在合成心脏MRI上的表现，发现DDPM在图像逼真度、下游分割效用与隐私保护之间取得最佳综合平衡。

**研究动机**：心脏MRI深度学习受限于数据稀缺与隐私法规，亟需可安全使用的合成数据来扩充训练集，同时避免患者信息泄露。

**核心方法**：采用“两阶段”流程：先生成/获取解剖学分割掩膜，再以掩膜为条件进行图像合成；并对DDPM、LDM、FM三类生成架构在保真度、效用（分割任务表现）与隐私三轴上做系统基准评测。

**主要结论**：扩散模型整体更优，其中DDPM在小数据场景下兼顾分割性能、视觉保真度与隐私表现最佳；FM在隐私特性上更有潜力但任务层面性能略逊，论文量化了跨域泛化与患者保密之间的权衡并给出评估框架。

**关键词**：合成医学影像, 隐私保护合成数据, Diffusion, 潜变量扩散模型, 流匹配, 掩膜条件生成, 两阶段生成管线, 数据增广

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04340v1) | [下载PDF](https://arxiv.org/pdf/2603.04340v1.pdf)

---

## [16. ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)

**作者**：Zihao Huang, Tianqi Liu, Zhaoxi Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

Synthesizing physically plausible articulated human-object interactions (HOI) without 3D/4D supervision remains a fundamental challenge. While recent zero-shot approaches leverage video diffusion models to synthesize human-object interactions, they are largely confined to rigid-object manipulation and lack explicit 4D geometric reasoning. To bridge this gap, we formulate articulated HOI synthesis as a 4D reconstruction problem from monocular video priors: given only a video generated by a diffusion model, we reconstruct a full 4D articulated scene without any 3D supervision. This reconstruction-based approach treats the generated 2D video as supervision for an inverse rendering problem, recovering geometrically consistent and physically plausible 4D scenes that naturally respect contact, articulation, and temporal coherence. We introduce ArtHOI, the first zero-shot framework for articulated human-object interaction synthesis via 4D reconstruction from video priors. Our key designs are: 1) Flow-based part segmentation: leveraging optical flow as a geometric cue to disentangle dynamic from static regions in monocular video; 2) Decoupled reconstruction pipeline: joint optimization of human motion and object articulation is unstable under monocular ambiguity, so we first recover object articulation, then synthesize human motion conditioned on the reconstructed object states. ArtHOI bridges video-based generation and geometry-aware reconstruction, producing interactions that are both semantically aligned and physically grounded. Across diverse articulated scenes (e.g., opening fridges, cabinets, microwaves), ArtHOI significantly outperforms prior methods in contact accuracy, penetration reduction, and articulation fidelity, extending zero-shot interaction synthesis beyond rigid manipulation through reconstruction-informed synthesis.

### 🤖 AI 总结

**一句话总结**：ArtHOI通过把扩散模型生成的单目视频当作先验监督，反向重建出几何一致的4D人-可动物体场景，从而零样本合成更真实的关节式HOI。

**研究动机**：现有零样本人-物交互生成多依赖视频扩散模型，但通常只适用于刚体物体且缺少显式4D几何推理，导致接触不准、穿插和时序不稳定。

**核心方法**：将HOI合成表述为“从视频先验做4D重建”的逆渲染优化：用光流做部件分割以区分动态/静态区域，并采用解耦流程先重建物体关节运动，再在重建的物体状态条件下合成人体运动以缓解单目歧义与联合优化不稳定。

**主要结论**：在开冰箱/柜门/微波炉等多类可动物体场景中，ArtHOI相比先前方法显著提升接触准确性、减少穿插并提高关节运动保真度，实现从视频生成到几何驱动的更物理可信交互合成。

**关键词**：关节人-物交互合成, 零样本生成, 4D重建, 单目视频先验, 视频扩散模型, 逆向渲染优化, 光流分割, 物体关节运动恢复, 人体运动合成, 接触一致性, 穿透抑制, 时序一致性

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04338v1) | [下载PDF](https://arxiv.org/pdf/2603.04338v1.pdf)

---

## [17. Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection](https://arxiv.org/abs/2603.04337v1)

**作者**：Dacheng Qi, Chenyu Wang, Jingwei Xu 等 9 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-03-04

### 📄 论文摘要

Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error.

### 🤖 AI 总结

**一句话总结**：Pointer-CAD 将B-Rep几何信息与命令序列统一到“指针式”生成框架中，使LLM能在生成过程中显式选择边/面等实体，从而更可靠地生成与编辑复杂CAD模型。

**研究动机**：纯命令序列表示难以表达对几何实体（边/面）的选择，导致倒角/圆角等复杂编辑操作受限；同时对连续变量的离散化会引入量化误差并造成拓扑错误。

**核心方法**：将CAD生成分步进行，每步在文本描述与已生成B-Rep的条件下生成下一条指令；当操作需要选择几何实体时，模型预测“Pointer”在候选边/面集合中选择最一致的目标，并配套构建约57.5万模型的数据集与自动标注生成专家级自然语言描述用于训练。

**主要结论**：实验表明该指针选择机制显著提升复杂几何结构的可生成性与可编辑性，并将分割/实体选择相关错误降到极低水平，相比以往命令序列方法明显减少由量化误差带来的拓扑不准确。

**关键词**：LLM条件生成, 指针式命令序列, 几何实体选择, 边-面指针选择, 序列化建模, 倒角-圆角编辑, 量化误差, 拓扑错误, CAD数据标注流水线, 大规模CAD数据集

**评分**：47

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04337v1) | [下载PDF](https://arxiv.org/pdf/2603.04337v1.pdf)

---

## [18. Scalable Evaluation of the Realism of Synthetic Environmental Augmentations in Images](https://arxiv.org/abs/2603.04325v1)

**作者**：Damian J. Ruck, Paul Vautravers, Oliver Chalkley 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Evaluation of AI systems often requires synthetic test cases, particularly for rare or safety-critical conditions that are difficult to observe in operational data. Generative AI offers a promising approach for producing such data through controllable image editing, but its usefulness depends on whether the resulting images are sufficiently realistic to support meaningful evaluation.   We present a scalable framework for assessing the realism of synthetic image-editing methods and apply it to the task of adding environmental conditions-fog, rain, snow, and nighttime-to car-mounted camera images. Using 40 clear-day images, we compare rule-based augmentation libraries with generative AI image-editing models. Realism is evaluated using two complementary automated metrics: a vision-language model (VLM) jury for perceptual realism assessment, and embedding-based distributional analysis to measure similarity to genuine adverse-condition imagery.   Generative AI methods substantially outperform rule-based approaches, with the best generative method achieving approximately 3.6 times the acceptance rate of the best rule-based method. Performance varies across conditions: fog proves easiest to simulate, while nighttime transformations remain challenging. Notably, the VLM jury assigns imperfect acceptance even to real adverse-condition imagery, establishing practical ceilings against which synthetic methods can be judged. By this standard, leading generative methods match or exceed real-image performance for most conditions.   These results suggest that modern generative image-editing models can enable scalable generation of realistic adverse-condition imagery for evaluation pipelines. Our framework therefore provides a practical approach for scalable realism evaluation, though validation against human studies remains an important direction for future work.

### 🤖 AI 总结

**一句话总结**：提出一套可扩展的自动化评测框架，用于衡量合成环境增强（雾/雨/雪/夜晚）图像的真实感，并发现生成式图像编辑显著优于规则库增强。

**研究动机**：AI系统评估常需覆盖罕见或安全关键场景，但真实数据难获取；因此需要验证生成式编辑产生的合成恶劣天气图像是否足够真实以支撑可靠评测。

**核心方法**：在40张晴天车载相机图像上，对比规则增强库与生成式图像编辑模型；用两类自动指标评估真实感：VLM“评审团”做感知逼真度判定，以及基于嵌入的分布相似性分析来衡量与真实恶劣天气图像的接近程度。

**主要结论**：生成式方法在各条件下整体显著领先（最佳方法接受率约为最佳规则法的3.6倍），雾最易模拟、夜晚最难；且VLM对真实恶劣天气图像也并非全通过，形成“实用上限”，在该基准下领先生成方法多数条件可达到或超过真实图像表现，但仍需人类研究进一步验证。

**关键词**：合成数据评测, 图像编辑增强, 环境条件模拟, 恶劣天气图像, 自动驾驶感知, 真实感评估, 视觉语言模型评审, 嵌入分布对齐, 规则增强方法, 生成式图像编辑模型

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04325v1) | [下载PDF](https://arxiv.org/pdf/2603.04325v1.pdf)

---

## [19. SPRINT: Semi-supervised Prototypical Representation for Few-Shot Class-Incremental Tabular Learning](https://arxiv.org/abs/2603.04321v1)

**作者**：Umid Suleymanov, Murat Kantarcioglu, Kevin S Chan 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Real-world systems must continuously adapt to novel concepts from limited data without forgetting previously acquired knowledge. While Few-Shot Class-Incremental Learning (FSCIL) is established in computer vision, its application to tabular domains remains largely unexplored. Unlike images, tabular streams (e.g., logs, sensors) offer abundant unlabeled data, a scarcity of expert annotations and negligible storage costs, features ignored by existing vision-based methods that rely on restrictive buffers. We introduce SPRINT, the first FSCIL framework tailored for tabular distributions. SPRINT introduces a mixed episodic training strategy that leverages confidence-based pseudo-labeling to enrich novel class representations and exploits low storage costs to retain base class history. Extensive evaluation across six diverse benchmarks spanning cybersecurity, healthcare, and ecological domains, demonstrates SPRINT's cross-domain robustness. It achieves a state-of-the-art average accuracy of 77.37% (5-shot), outperforming the strongest incremental baseline by 4.45%.

### 🤖 AI 总结

**一句话总结**：SPRINT 提出面向表格数据的少样本类增量学习框架，通过半监督伪标注与低成本存储的历史回放，实现新类快速适应且尽量不遗忘旧类。

**研究动机**：现有 FSCIL 方法主要针对视觉任务，忽略了表格流数据“未标注数据丰富、标注稀缺、存储成本低”的现实特性，导致在表格领域难以有效利用数据并缓解遗忘。

**核心方法**：SPRINT 采用混合式 episodic 训练：对新类使用基于置信度的伪标签将大量未标注样本纳入训练以增强原型表示；同时利用表格数据存储便宜的优势保留基类历史数据用于回放，稳定旧类性能。

**主要结论**：在网络安全、医疗与生态等 6 个表格基准上，SPRINT 展现跨领域鲁棒性，5-shot 平均准确率达 77.37%，较最强增量基线提升 4.45%，达到 SOTA。

**关键词**：少样本类增量学习（FSCIL）, 表格数据学习, 半监督学习, 置信度伪标签, 原型表示学习, 持续学习, 灾难性遗忘, 混合式情景训练, 基类历史回放, 表格数据流, 跨领域基准评测

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04321v1) | [下载PDF](https://arxiv.org/pdf/2603.04321v1.pdf)

---

## [20. MOO: A Multi-view Oriented Observations Dataset for Viewpoint Analysis in Cattle Re-Identification](https://arxiv.org/abs/2603.04314v1)

**作者**：William Grolleau, Achraf Chaouch, Astrid Sabourin 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Animal re-identification (ReID) faces critical challenges due to viewpoint variations, particularly in Aerial-Ground (AG-ReID) settings where models must match individuals across drastic elevation changes. However, existing datasets lack the precise angular annotations required to systematically analyze these geometric variations. To address this, we introduce the Multi-view Oriented Observation (MOO) dataset, a large-scale synthetic AG-ReID dataset of $1,000$ cattle individuals captured from $128$ uniformly sampled viewpoints ($128,000$ annotated images). Using this controlled dataset, we quantify the influence of elevation and identify a critical elevation threshold, above which models generalize significantly better to unseen views. Finally, we validate the transferability to real-world applications in both zero-shot and supervised settings, demonstrating performance gains across four real-world cattle datasets and confirming that synthetic geometric priors effectively bridge the domain gap. Collectively, this dataset and analysis lay the foundation for future model development in cross-view animal ReID. MOO is publicly available at https://github.com/TurtleSmoke/MOO.

### 🤖 AI 总结

**一句话总结**：提出并开源MOO合成数据集（1000头牛、128个均匀视角、12.8万张带角度标注图），用于系统研究跨视角（尤其空-地）牛只ReID中的视角/仰角变化，并验证其对真实数据的迁移增益。

**研究动机**：空-地ReID受视角与高度变化影响显著，但现有动物ReID数据集缺少精确的视角/角度标注，难以定量分析几何变化对模型泛化的影响。

**核心方法**：构建可控的大规模合成AG-ReID数据集MOO，对每个个体从128个均匀采样视点渲染并提供精确角度注释；基于该数据集分析仰角对性能的影响并寻找关键阈值，同时在四个真实牛只数据集上进行零样本与有监督迁移评估。

**主要结论**：仰角存在“关键阈值”，超过该高度后模型对未见视角的泛化显著更好；合成数据中学习到的几何先验可有效缓解域差异，在真实数据的零样本与监督设置中均带来性能提升。

**关键词**：动物重识别(ReID, 跨视角匹配, 空地重识别(AG-ReID, 视角变化鲁棒性, 精确角度标注, 多视角合成数据集, 仿真到真实迁移(Sim2Real, 几何先验, 海拔角阈值分析, 零样本迁移(Zero-shot, 监督迁移学习

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04314v1) | [下载PDF](https://arxiv.org/pdf/2603.04314v1.pdf)

---

## [21. Dual Diffusion Models for Multi-modal Guided 3D Avatar Generation](https://arxiv.org/abs/2603.04307v1)

**作者**：Hong Li, Yutang Feng, Minqi Meng 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-04

### 📄 论文摘要

Generating high-fidelity 3D avatars from text or image prompts is highly sought after in virtual reality and human-computer interaction. However, existing text-driven methods often rely on iterative Score Distillation Sampling (SDS) or CLIP optimization, which struggle with fine-grained semantic control and suffer from excessively slow inference. Meanwhile, image-driven approaches are severely bottlenecked by the scarcity and high acquisition cost of high-quality 3D facial scans, limiting model generalization. To address these challenges, we first construct a novel, large-scale dataset comprising over 100,000 pairs across four modalities: fine-grained textual descriptions, in-the-wild face images, high-quality light-normalized texture UV maps, and 3D geometric shapes. Leveraging this comprehensive dataset, we propose PromptAvatar, a framework featuring dual diffusion models. Specifically, it integrates a Texture Diffusion Model (TDM) that supports flexible multi-condition guidance from text and/or image prompts, alongside a Geometry Diffusion Model (GDM) guided by text prompts. By learning the direct mapping from multi-modal prompts to 3D representations, PromptAvatar eliminates the need for time-consuming iterative optimization, successfully generating high-fidelity, shading-free 3D avatars in under 10 seconds. Extensive quantitative and qualitative experiments demonstrate that our method significantly outperforms existing state-of-the-art approaches in generation quality, fine-grained detail alignment, and computational efficiency.

### 🤖 AI 总结

**一句话总结**：提出PromptAvatar：基于双扩散模型从文本和/或图像提示直接生成高保真、无阴影的3D头像，推理无需迭代优化且可在10秒内完成。

**研究动机**：现有文本驱动3D头像多依赖SDS/CLIP迭代优化，语义细粒度控制不足且推理极慢；图像驱动方法又受高质量3D人脸扫描数据稀缺与成本高限制，泛化能力受阻。

**核心方法**：构建包含10万+四模态配对数据（细粒度文本、野外人脸图、光照归一化UV纹理、3D几何）的新数据集；训练双扩散模型：TDM在纹理空间支持文本/图像多条件引导生成UV纹理，GDM由文本引导生成几何形状，实现从多模态提示到3D表示的直接映射。

**主要结论**：在不进行耗时迭代优化的情况下，方法能快速生成细节对齐且质量更高的3D头像；实验表明其在生成质量、细粒度语义一致性与计算效率上显著优于现有SOTA。

**关键词**：多模态引导, 3D头像生成, 文本到3D, 图像到3D, Diffusion, 双扩散模型, 纹理扩散模型, 几何扩散模型, UV纹理贴图, 3D人脸几何, 快速推理

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04307v1) | [下载PDF](https://arxiv.org/pdf/2603.04307v1.pdf)

---

## cs.LG

## [22. Accurate and Efficient Hybrid-Ensemble Atmospheric Data Assimilation in Latent Space with Uncertainty Quantification](https://arxiv.org/abs/2603.04395v1)

**作者**：Hang Fan, Juan Nathaniel, Yi Xiao 等 8 位作者  
**分类**：cs.LG, physics.ao-ph  
**发布时间**：2026-03-04

### 📄 论文摘要

Data assimilation (DA) combines model forecasts and observations to estimate the optimal state of the atmosphere with its uncertainty, providing initial conditions for weather prediction and reanalyses for climate research. Yet, existing traditional and machine-learning DA methods struggle to achieve accuracy, efficiency and uncertainty quantification simultaneously. Here, we propose HLOBA (Hybrid-Ensemble Latent Observation-Background Assimilation), a three-dimensional hybrid-ensemble DA method that operates in an atmospheric latent space learned via an autoencoder (AE). HLOBA maps both model forecasts and observations into a shared latent space via the AE encoder and an end-to-end Observation-to-Latent-space mapping network (O2Lnet), respectively, and fuses them through a Bayesian update with weights inferred from time-lagged ensemble forecasts. Both idealized and real-observation experiments demonstrate that HLOBA matches dynamically constrained four-dimensional DA methods in both analysis and forecast skill, while achieving end-to-end inference-level efficiency and theoretical flexibility applies to any forecasting model. Moreover, by exploiting the error decorrelation property of latent variables, HLOBA enables element-wise uncertainty estimates for its latent analysis and propagates them to model space via the decoder. Idealized experiments show that this uncertainty highlights large-error regions and captures their seasonal variability.

### 🤖 AI 总结

**一句话总结**：提出HLOBA：在自编码器学习的气象潜空间中进行三维混合集合数据同化，实现接近4D同化的精度与更高效率，并提供可传播到物理空间的不确定性估计。

**研究动机**：传统与机器学习同化方法往往难以同时兼顾精度、计算效率和不确定性量化；需要一种可端到端快速推理、且能与任意预报模型兼容的同化框架。

**核心方法**：用AE将模式背景场编码到共享潜空间，并用O2Lnet将观测直接映射到潜空间；在潜空间通过基于时间滞后集合预报推断的权重做贝叶斯更新融合背景与观测，并利用潜变量误差去相关性进行逐元素不确定性估计，再经解码器回传到模式空间。

**主要结论**：理想化与真实观测实验表明，HLOBA在分析与预报技巧上可匹配动力约束的四维同化方法，同时具备推理级效率与对任意预报模型的灵活性；其不确定性估计能定位大误差区域并刻画季节性变化。

**关键词**：大气数据同化, 混合集合同化, 潜空间同化, 自编码器, 观测算子学习, 贝叶斯更新, 不确定性量化, 逐元素不确定性估计, 时间滞后集合预报, 误差去相关, 天气预报初始化, 气候再分析

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04395v1) | [下载PDF](https://arxiv.org/pdf/2603.04395v1.pdf)

---

## [23. Robustness of Agentic AI Systems via Adversarially-Aligned Jacobian Regularization](https://arxiv.org/abs/2603.04378v1)

**作者**：Furkan Mumcu, Yasin Yilmaz  
**分类**：cs.LG, cs.AI, cs.CR, cs.MA  
**发布时间**：2026-03-04

### 📄 论文摘要

As Large Language Models (LLMs) transition into autonomous multi-agent ecosystems, robust minimax training becomes essential yet remains prone to instability when highly non-linear policies induce extreme local curvature in the inner maximization. Standard remedies that enforce global Jacobian bounds are overly conservative, suppressing sensitivity in all directions and inducing a large Price of Robustness. We introduce Adversarially-Aligned Jacobian Regularization (AAJR), a trajectory-aligned approach that controls sensitivity strictly along adversarial ascent directions. We prove that AAJR yields a strictly larger admissible policy class than global constraints under mild conditions, implying a weakly smaller approximation gap and reduced nominal performance degradation. Furthermore, we derive step-size conditions under which AAJR controls effective smoothness along optimization trajectories and ensures inner-loop stability. These results provide a structural theory for agentic robustness that decouples minimax stability from global expressivity restrictions.

### 🤖 AI 总结

**一句话总结**：提出AAJR：只在对抗上升方向约束雅可比敏感度，从而提升多智能体/代理式LLM系统的鲁棒最小最大训练稳定性，并降低鲁棒性带来的性能代价。

**研究动机**：在代理式AI的最小最大鲁棒训练中，策略高度非线性会导致内层最大化的局部曲率极端、训练不稳定；而全局雅可比上界约束过于保守，会在所有方向压制敏感度并显著损害名义性能。

**核心方法**：AAJR通过“轨迹对齐”的正则化，仅沿对抗优化（内层上升）方向控制雅可比/敏感度，而不是对所有方向施加全局界；并给出理论证明其相较全局约束具有更大的可行策略类，以及推导保证内层稳定的步长条件来控制轨迹上的有效平滑性。

**主要结论**：在温和条件下，AAJR的可容纳策略集合严格大于全局雅可比约束，意味着更小的近似差距与更低的鲁棒性性能损失；同时其步长条件可确保内循环对抗优化的稳定性，从结构上实现“稳定性”与“表达能力”的解耦。

**关键词**：多智能体 LLM 系统, 鲁棒最小最大训练, 雅可比正则化, 轨迹对齐正则化, 内循环稳定性, 步长条件, 局部曲率控制, 有效光滑性

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04378v1) | [下载PDF](https://arxiv.org/pdf/2603.04378v1.pdf)

---

## [24. Robust Unscented Kalman Filtering via Recurrent Meta-Adaptation of Sigma-Point Weights](https://arxiv.org/abs/2603.04360v1)

**作者**：Kenan Majewski, Michał Modzelewski, Marcin Żugaj 等 4 位作者  
**分类**：cs.LG, eess.SP  
**发布时间**：2026-03-04

### 📄 论文摘要

The Unscented Kalman Filter (UKF) is a ubiquitous tool for nonlinear state estimation; however, its performance is limited by the static parameterization of the Unscented Transform (UT). Conventional weighting schemes, governed by fixed scaling parameters, assume implicit Gaussianity and fail to adapt to time-varying dynamics or heavy-tailed measurement noise. This work introduces the Meta-Adaptive UKF (MA-UKF), a framework that reformulates sigma-point weight synthesis as a hyperparameter optimization problem addressed via memory-augmented meta-learning. Unlike standard adaptive filters that rely on instantaneous heuristic corrections, our approach employs a Recurrent Context Encoder to compress the history of measurement innovations into a compact latent embedding. This embedding informs a policy network that dynamically synthesizes the mean and covariance weights of the sigma points at each time step, effectively governing the filter's trust in the prediction versus the measurement. By optimizing the system end-to-end through the filter's recursive logic, the MA-UKF learns to maximize tracking accuracy while maintaining estimation consistency. Numerical benchmarks on maneuvering targets demonstrate that the MA-UKF significantly outperforms standard baselines, exhibiting superior robustness to non-Gaussian glint noise and effective generalization to out-of-distribution (OOD) dynamic regimes unseen during training.

### 🤖 AI 总结

**一句话总结**：提出MA-UKF，通过循环元学习根据历史创新自适应生成UKF的sigma点权重，从而在非高斯噪声与OOD动态下更稳健地提升跟踪精度与一致性。

**研究动机**：传统UKF的Unscented Transform权重由固定超参数决定，隐含高斯假设且无法随时间变化的动力学与重尾测量噪声自适应，导致性能与鲁棒性受限。

**核心方法**：将sigma点均值/协方差权重合成视为超参数优化问题：用循环上下文编码器压缩历史测量创新为潜变量，再由策略网络在每个时刻动态输出权重，并通过滤波递推的端到端训练优化跟踪误差与估计一致性。

**主要结论**：在机动目标基准上，MA-UKF相较标准基线显著更准确且更鲁棒，尤其在非高斯glint重尾噪声下表现更好，并能泛化到训练未见的OOD动态场景。

**关键词**：无迹卡尔曼滤波（UKF）, 无迹变换（UT）, sigma点权重自适应, 元学习自适应滤波, 记忆增强元学习, 循环上下文编码器, 超参数优化, 非线性状态估计, 重尾测量噪声, 非高斯glint噪声, 机动目标跟踪

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04360v1) | [下载PDF](https://arxiv.org/pdf/2603.04360v1.pdf)

---

## [25. Dissecting Quantization Error: A Concentration-Alignment Perspective](https://arxiv.org/abs/2603.04359v1)

**作者**：Marco Federici, Boris van Breugel, Paul Whatmough 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Quantization can drastically increase the efficiency of large language and vision models, but typically incurs an accuracy drop. Recently, function-preserving transforms (e.g. rotations, Hadamard transform, channel-wise scaling) have been successfully applied to reduce post-training quantization error, yet a principled explanation remains elusive. We analyze linear-layer quantization via the signal-to-quantization-noise ratio (SQNR), showing that for uniform integer quantization at a fixed bit width, SQNR decomposes into (i) the concentration of weights and activations (capturing spread and outliers), and (ii) the alignment of their dominant variation directions. This reveals an actionable insight: beyond concentration - the focus of most prior transforms (e.g. rotations or Hadamard) - improving alignment between weight and activation can further reduce quantization error. Motivated by this, we introduce block Concentration-Alignment Transforms (CAT), a lightweight linear transformation that uses a covariance estimate from a small calibration set to jointly improve concentration and alignment, approximately maximizing SQNR. Experiments across several LLMs show that CAT consistently matches or outperforms prior transform-based quantization methods at 4-bit precision, confirming the insights gained in our framework.

### 🤖 AI 总结

**一句话总结**：论文提出用“集中度-对齐度”分解来解释量化误差，并据此设计CAT变换在4-bit后训练量化中稳定提升LLM精度。

**研究动机**：现有函数保持变换（旋转、Hadamard、缩放等）能缓解PTQ精度损失，但缺少统一的原理解释，且多数只关注权重/激活的“分布集中度”而忽略二者的“方向对齐”。

**核心方法**：作者用SQNR分析线性层均匀整数定点量化，将SQNR分解为(1)权重与激活的集中度（离群与尺度扩散）和(2)主导变化方向的对齐度；据此提出块状CAT变换，利用小规模校准集估计协方差来联合改善集中度与对齐度，从而近似最大化SQNR并降低量化噪声。

**主要结论**：除提升集中度外，改善权重-激活的对齐也能显著降低量化误差；CAT在多种LLM的4-bit量化实验中持续达到或超过已有基于变换的量化方法，验证了该理论框架的有效性。

**关键词**：后训练量化, 低比特量化（4-bit）, 线性层量化, 量化误差分析, 信号量化噪声比（SQNR）, 权重-激活浓度, 权重-激活对齐, 函数保持变换, 协方差校准, 块状浓度-对齐变换（CAT）, 变换式量化方法

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04359v1) | [下载PDF](https://arxiv.org/pdf/2603.04359v1.pdf)

---

## [26. Efficient Refusal Ablation in LLM through Optimal Transport](https://arxiv.org/abs/2603.04355v1)

**作者**：Geraldin Nanfack, Eugene Belilovsky, Elvis Dohmatob  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Safety-aligned language models refuse harmful requests through learned refusal behaviors encoded in their internal representations. Recent activation-based jailbreaking methods circumvent these safety mechanisms by applying orthogonal projections to remove refusal directions, but these approaches treat refusal as a one-dimensional phenomenon and ignore the rich distributional structure of model activations. We introduce a principled framework based on optimal transport theory that transforms the entire distribution of harmful activations to match harmless ones. By combining PCA with closed-form Gaussian optimal transport, we achieve efficient computation in high-dimensional representation spaces while preserving essential geometric structure. Across six models (Llama-2, Llama-3.1, Qwen-2.5; 7B-32B parameters), our method achieves up to 11% higher attack success rates than state-of-the-art baselines while maintaining comparable perplexity, demonstrating superior preservation of model capabilities. Critically, we discover that layer-selective intervention (applying optimal transport to 1-2 carefully chosen layers at approximately 40-60% network depth) substantially outperforms full-network interventions, revealing that refusal mechanisms may be localized rather than distributed. Our analysis provides new insights into the geometric structure of safety representations and suggests that current alignment methods may be vulnerable to distributional attacks beyond simple direction removal.

### 🤖 AI 总结

**一句话总结**：提出一种基于最优传输的“拒答消融”框架，将有害请求触发的激活分布整体变换为无害分布，从而更有效绕过安全拒答且较好保持模型能力。

**研究动机**：现有基于投影移除“拒答方向”的越狱方法将拒答简化为一维信号，忽视激活的分布结构，导致攻击效果与能力保持存在局限。作者希望用更原则性的分布匹配来刻画并消融拒答行为。

**核心方法**：在表示空间中对“有害/无害”激活做PCA降维后，利用闭式高斯最优传输（OT）学习一个分布级线性变换，将有害激活分布对齐到无害分布，并在推理时对选定层的激活进行干预。进一步探索层选择策略，发现仅对网络深度约40–60%处的1–2层做OT干预最有效。

**主要结论**：在Llama-2/Llama-3.1/Qwen-2.5等6个7B–32B模型上，该方法较SOTA基线最高提升约11%攻击成功率，同时困惑度相近，表明能力保留更好。结果还显示拒答机制可能更“局部化”在特定层，且对齐系统可能易受分布级攻击而不仅是方向移除。

**关键词**：拒绝行为消融, 激活投影越狱, 最优传输, 高斯最优传输, 分布匹配, 表示空间几何, 层选择性干预, 安全对齐机制, 攻击成功率评测, 困惑度保持

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04355v1) | [下载PDF](https://arxiv.org/pdf/2603.04355v1.pdf)

---

## [27. Out-of-distribution transfer of PDE foundation models to material dynamics under extreme loading](https://arxiv.org/abs/2603.04354v1)

**作者**：Mahindra Rautela, Alexander Most, Siddharth Mansingh 等 12 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-04

### 📄 论文摘要

Most PDE foundation models are pretrained and fine-tuned on fluid-centric benchmarks. Their utility under extreme-loading material dynamics remains unclear. We benchmark out-of-distribution transfer on two discontinuity-dominated regimes in which shocks, evolving interfaces, and fracture produce highly non-smooth fields: shock-driven multi-material interface dynamics (perturbed layered interface or PLI) and dynamic fracture/failure evolution (FRAC). We formulate the downstream task as terminal-state prediction, i.e., learning a long-horizon map that predicts the final state directly from the first snapshot without intermediate supervision. Using a unified training and evaluation protocol, we evaluate two open-source pretrained PDE foundation models, POSEIDON and MORPH, and compare fine-tuning from pretrained weights against training from scratch across training-set sizes to quantify sample efficiency under distribution shift.

### 🤖 AI 总结

**一句话总结**：论文评估两种开源PDE基础模型在极端载荷材料动力学（含激波、界面与断裂等强不连续场）上的分布外迁移能力，并量化预训练微调相对从零训练的样本效率收益。

**研究动机**：现有PDE基础模型多在流体基准上预训练/微调，其在极端载荷下的材料动力学（高非光滑、含冲击与断裂）任务上是否仍可用、是否具备样本效率优势尚不明确。

**核心方法**：构建两类不连续主导的下游基准：激波驱动多材料界面动力学（PLI）与动态断裂/失效演化（FRAC），并将任务统一为“终态预测”（仅用首帧直接预测最终状态、无中间监督）。在统一训练评测协议下，对POSEIDON与MORPH进行分布外迁移实验，对比预训练权重微调与从头训练，并在不同训练集规模下评估样本效率。

**主要结论**：在PLI与FRAC两种强分布偏移场景中，预训练PDE基础模型的迁移表现与样本效率可通过系统基准被定量刻画；论文给出了POSEIDON/MORPH在终态长时程预测下的分布外泛化对比，并揭示微调与从零训练在不同数据量下的性能差异。

**关键词**：PDE基础模型, 分布外迁移, 极端载荷材料动力学, 冲击波动力学, 多材料界面演化, 动态断裂与失效, 间断主导场, 终端状态预测, 长时域预测, 微调对比从头训练, 样本效率, 分布偏移评测

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04354v1) | [下载PDF](https://arxiv.org/pdf/2603.04354v1.pdf)

---

## [28. What Does Flow Matching Bring To TD Learning?](https://arxiv.org/abs/2603.04333v1)

**作者**：Bhavya Agrawalla, Michal Nauman, Aviral Kumar  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Recent work shows that flow matching can be effective for scalar Q-value function estimation in reinforcement learning (RL), but it remains unclear why or how this approach differs from standard critics. Contrary to conventional belief, we show that their success is not explained by distributional RL, as explicitly modeling return distributions can reduce performance. Instead, we argue that the use of integration for reading out values and dense velocity supervision at each step of this integration process for training improves TD learning via two mechanisms. First, it enables robust value prediction through \emph{test-time recovery}, whereby iterative computation through integration dampens errors in early value estimates as more integration steps are performed. This recovery mechanism is absent in monolithic critics. Second, supervising the velocity field at multiple interpolant values induces more \emph{plastic} feature learning within the network, allowing critics to represent non-stationary TD targets without discarding previously learned features or overfitting to individual TD targets encountered during training. We formalize these effects and validate them empirically, showing that flow-matching critics substantially outperform monolithic critics (2$\times$ in final performance and around 5$\times$ in sample efficiency) in settings where loss of plasticity poses a challenge e.g., in high-UTD online RL problems, while remaining stable during learning.

### 🤖 AI 总结

**一句话总结**：论文解释了流匹配（Flow Matching）critic 之所以优于传统TD critic，并非因为分布式RL，而是因为“积分读出+多步速度监督”带来的测试时误差恢复与更强的特征可塑性。

**研究动机**：尽管流匹配已被发现能有效估计标量Q值，但其优越性来源不清，且常被误认为是分布式RL的收益。作者希望澄清其与标准critic的关键差异，并解释在高UTD等易失去可塑性的场景下为何更强。

**核心方法**：将Q值通过沿插值变量的积分过程读出，并在积分的每一步对速度场进行密集监督，而非一次性“单体”输出Q值。作者形式化分析两机制：测试时通过多步积分迭代抑制早期误差（test-time recovery），以及多插值点监督促使网络学习更可迁移/不易遗忘的特征以适应非平稳TD目标。

**主要结论**：实证表明显式建模回报分布不但不能解释提升，甚至可能降性能；真正增益来自积分推断的误差恢复与多步监督带来的可塑性提升。流匹配critic在高UTD在线RL等场景中相较单体critic取得约2×最终性能和约5×样本效率提升，并保持训练稳定。

**关键词**：流匹配, 时序差分学习, Q 值估计, 积分读出, 速度场监督, 密集监督, 测试时恢复, 特征可塑性, 非平稳 TD 目标, 高 UTD 在线强化学习, 样本效率

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04333v1) | [下载PDF](https://arxiv.org/pdf/2603.04333v1.pdf)

---

## [29. PTOPOFL: Privacy-Preserving Personalised Federated Learning via Persistent Homology](https://arxiv.org/abs/2603.04323v1)

**作者**：Kelly L Vomo-Donfack, Adryel Hoszu, Grégory Ginot 等 4 位作者  
**分类**：cs.LG, cs.CR, cs.DC, math.AT, stat.ML  
**发布时间**：2026-03-04

### 📄 论文摘要

Federated learning (FL) faces two structural tensions: gradient sharing enables data-reconstruction attacks, while non-IID client distributions degrade aggregation quality. We introduce PTOPOFL, a framework that addresses both challenges simultaneously by replacing gradient communication with topological descriptors derived from persistent homology (PH). Clients transmit only 48-dimensional PH feature vectors-compact shape summaries whose many-to-one structure makes inversion provably ill-posed-rather than model gradients. The server performs topology-guided personalised aggregation: clients are clustered by Wasserstein similarity between their PH diagrams, intra-cluster models are topology-weighted,and clusters are blended with a global consensus. We prove an information-contraction theorem showing that PH descriptors leak strictly less mutual information per sample than gradients under strongly convex loss functions, and we establish linear convergence of the Wasserstein-weighted aggregation scheme with an error floor strictly smaller than FedAvg. Evaluated against FedAvg, FedProx, SCAFFOLD, and pFedMe on a non-IID healthcare scenario (8 hospitals, 2 adversarial) and a pathological benchmark (10 clients), PTOPOFL achieves AUC 0.841 and 0.910 respectively-the highest in both settings-while reducing reconstruction risk by a factor of 4.5 relative to gradient sharing. Code is publicly available at https://github.com/MorillaLab/TopoFederatedL and data at https://doi.org/10.5281/zenodo.18827595.

### 🤖 AI 总结

**一句话总结**：PTOPOFL用持久同调的拓扑特征向量替代梯度通信，在提升联邦学习个性化聚合效果的同时显著降低数据重建泄露风险。

**研究动机**：联邦学习中共享梯度容易遭受数据重建攻击，而客户端非IID分布又会使全局聚合（如FedAvg）性能下降、个性化不足；需要一种兼顾隐私与非IID鲁棒性的通信与聚合机制。

**核心方法**：客户端不上传梯度/参数，而是从本地训练过程（或模型/表示）提取48维持久同调（PH）拓扑描述符；服务器用PH图的Wasserstein相似度对客户端聚类，并在簇内进行拓扑加权聚合、再与全局共识融合实现个性化；理论上给出PH信息收缩（互信息泄露更小）与Wasserstein加权聚合的线性收敛及更低误差下界。

**主要结论**：在医疗非IID与病态非IID基准上，PTOPOFL相对FedAvg/FedProx/SCAFFOLD/pFedMe取得最高AUC（0.841、0.910），并将相对梯度共享的重建风险降低约4.5倍，表明拓扑特征通信可同时改善隐私与个性化性能。

**关键词**：隐私保护联邦学习, 个性化联邦学习, 梯度反演攻击, 持久同调（PH）, 拓扑特征向量, 客户端聚类, 拓扑加权聚合, 互信息泄露, 线性收敛性分析

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04323v1) | [下载PDF](https://arxiv.org/pdf/2603.04323v1.pdf)

---

## [30. Activation Outliers in Transformer Quantization: Reproduction, Statistical Analysis, and Deployment Tradeoffs](https://arxiv.org/abs/2603.04308v1)

**作者**：Pranav Kumar Kaliaperumal  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-04

### 📄 论文摘要

Post-training quantization (PTQ) of transformers is known to suffer from severe accuracy degradation due to structured activation outliers, as originally analyzed by Bondarenko et al. (EMNLP 2021) in work associated with Qualcomm AI Research. This paper provides a reproducible empirical reproduction and systems-level extension of that phenomenon in BERT-base fine-tuned on QNLI. When global W8A8 quantization is applied, validation accuracy drops sharply from 89.66% (FP32) to 54.33%, a decrease of 35.33 points. Statistical analysis of FP32 activations shows strongly heavy-tailed behavior that intensifies with model depth: kurtosis reaches 271 in the final layers and approximately 55% of activation energy is concentrated in the top 1% of channels. We evaluate several mitigation strategies. Mixed precision PTQ restores accuracy close to the FP32 baseline (89.42%). Per-embedding-group (PEG) quantization shows strong sensitivity to grouping structure, improving accuracy from 66.12% with three groups to 86.18% with four groups. In contrast, percentile-based calibration, even at thresholds between 99.0 and 99.99, fails to recover accuracy (about 50.54%), indicating that large activation channels encode structured signal rather than rare noise. Deployment profiling on an RTX 3050 GPU shows minimal differences in latency and memory usage across methods (median latency about 58-59 ms; VRAM usage about 484-486 MB), highlighting the importance of hardware-aware evaluation. Overall, the results show that PTQ failure in transformers is primarily driven by structured channel dominance amplified through residual connections. Effective mitigation therefore requires channel-aware precision allocation rather than scalar clipping alone.

### 🤖 AI 总结

**一句话总结**：论文复现并扩展了Transformer在PTQ下因结构化激活离群导致W8A8精度崩溃的问题，并表明通道感知的混合精度/分组量化可有效恢复准确率而单纯剪裁无效。

**研究动机**：已有研究指出Transformer的激活离群会让PTQ显著掉点，但缺少可复现实证与系统部署层面的权衡分析；本文旨在复现现象、量化其统计特征并评估可行缓解策略与部署代价。

**核心方法**：在BERT-base(QNLI)上对比FP32与全局W8A8 PTQ的精度变化，并对各层FP32激活做重尾统计分析（峰度、能量集中度）；进一步评测混合精度、按embedding组(PEG)量化、百分位校准剪裁等策略，并在RTX 3050上做延迟/显存profiling。

**主要结论**：PTQ失败主要由残差连接放大的“通道主导型”结构化激活离群驱动：全局W8A8使精度从89.66%跌至54.33%，而混合精度可回到89.42%，PEG效果依赖分组结构；百分位剪裁在99.0–99.99阈值下仍难恢复（~50%），且不同方法在该GPU上的延迟/显存差异很小，强调硬件感知评估与通道级精度分配的重要性。

**关键词**：激活异常值, 结构化通道主导, 重尾分布激活, W8A8 量化, 混合精度量化, PEG 分组量化, 百分位校准, 残差连接放大效应, 硬件感知评测, 部署性能剖析

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2603.04308v1) | [下载PDF](https://arxiv.org/pdf/2603.04308v1.pdf)

---

