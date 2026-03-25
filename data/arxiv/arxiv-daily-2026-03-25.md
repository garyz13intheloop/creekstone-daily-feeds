# arXiv AI 论文日报 | 2026-03-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (21 篇)
- [cs.LG](#csLG) (5 篇)
- [cs.CL](#csCL) (1 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Mecha-nudges for Machines](https://arxiv.org/abs/2603.23433v1)

**作者**：Giulio Frey, Kawin Ethayarajh  
**分类**：cs.AI  
**发布时间**：2026-03-24

### 📄 论文摘要

Nudges are subtle changes to the way choices are presented to human decision-makers (e.g., opt-in vs. opt-out by default) that shift behavior without restricting options or changing incentives. As AI agents increasingly make decisions in the same environments as humans, the presentation of choices may be optimized for machines as well as people. We introduce mecha-nudges: changes to how choices are presented that systematically influence AI agents without degrading the decision environment for humans. To formalize mecha-nudges, we combine the Bayesian persuasion framework with V-usable information, a generalization of Shannon information that is observer-relative. This yields a common scale (bits of usable information) for comparing a wide range of interventions, contexts, and models. Applying our framework to product listings on Etsy -- a global marketplace for independent sellers -- we find that following ChatGPT's release, listings have significantly more machine-usable information about product selection, consistent with systematic mecha-nudging.

### 🤖 AI 总结

**一句话总结**：论文提出“mecha-nudges（机器助推）”概念：通过调整信息呈现方式在不损害人类决策环境的前提下系统性影响AI代理，并用Etsy数据证实ChatGPT发布后商品信息更“机器可用”。

**研究动机**：传统助推研究面向人类决策者，但当AI代理与人类在同一市场/界面中共同决策时，平台与卖家可能会开始“为机器优化呈现”。作者希望刻画并度量这种对AI有效、但不一定改变人类激励与选择集合的干预。

**核心方法**：将贝叶斯劝说（Bayesian persuasion）框架与“V-usable information（相对观察者的可用信息）”结合，构建以“可用信息比特数”为统一度量来比较不同干预。并在Etsy商品列表场景中，实证分析ChatGPT发布前后商品展示文本中对模型更可用的信息量变化。

**主要结论**：实证结果显示，ChatGPT发布后Etsy商品列表包含显著更多“机器可用”的产品选择信息，符合市场出现系统性mecha-nudging的现象。论文结论强调应以“对特定决策者可用的信息”而非传统香农信息来衡量面向AI的呈现优化与其潜在影响。

**关键词**：机器助推, 助推理论, 信息设计, 选项呈现, AI 代理决策, 贝叶斯劝服, 电商商品列表, Mecha-nudges

**评分**：34

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23433v1) | [下载PDF](https://arxiv.org/pdf/2603.23433v1.pdf)

---

## [2. Bilevel Autoresearch: Meta-Autoresearching Itself](https://arxiv.org/abs/2603.23420v1)

**作者**：Yaonan Qu, Meng Lu  
**分类**：cs.AI  
**发布时间**：2026-03-24

### 📄 论文摘要

If autoresearch is itself a form of research, then autoresearch can be applied to research itself. We take this idea literally: we use an autoresearch loop to optimize the autoresearch loop. Every existing autoresearch system -- from Karpathy's single-track loop to AutoResearchClaw's multi-batch extension and EvoScientist's persistent memory -- was improved by a human who read the code, identified a bottleneck, and wrote new code. We ask whether an LLM can do the same, autonomously. We present Bilevel Autoresearch, a bilevel framework where an outer loop meta-optimizes the inner autoresearch loop by generating and injecting new search mechanisms as Python code at runtime. The inner loop optimizes the task; the outer loop optimizes how the inner loop searches. Both loops use the same LLM -- no stronger model is needed at the meta level. On Karpathy's GPT pretraining benchmark, the meta-autoresearch outer loop achieves a 5x improvement over the standard inner loop alone (-0.045 vs. -0.009 val_bpb), while parameter-level adjustment without mechanism change yields no reliable gain. The outer loop autonomously discovers mechanisms from combinatorial optimization, multi-armed bandits, and design of experiments -- without human specification of which domains to explore. These mechanisms succeed by breaking the inner loop's deterministic search patterns, forcing exploration of directions the LLM's priors systematically avoid. The core principle is simple: if autoresearch can meta-autoresearch itself, it can, in principle, meta-autoresearch anything with a measurable objective.

### 🤖 AI 总结

**一句话总结**：提出“双层自动科研”框架，用外层LLM循环自动生成并注入新的搜索机制代码，从而优化内层自动科研过程并显著提升任务表现。

**研究动机**：现有自动科研系统的关键改进往往来自人类阅读代码并手工加入新机制；作者希望验证LLM能否自主完成这种“改进自动科研本身”的工作。

**核心方法**：构建双层（bilevel）框架：内层循环负责在给定任务上搜索与优化，外层循环在运行时生成Python代码并注入新的搜索/探索机制来重塑内层的搜索策略；两层使用同一个LLM而非更强模型。

**主要结论**：在Karpathy的GPT预训练基准上，外层元优化带来约5倍提升（val_bpb改进-0.045 vs -0.009），而仅做参数级调整且不改变机制无稳定收益；外层还能自主发现并组合来自组合优化、多臂老虎机与实验设计等领域的机制，通过打破内层确定性搜索模式促进探索。

**关键词**：双层优化, 运行时代码生成, 搜索机制注入, 黑箱优化, 多臂老虎机, 组合优化, 实验设计（DoE）, GPT预训练基准

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23420v1) | [下载PDF](https://arxiv.org/pdf/2603.23420v1.pdf)

---

## [3. Beyond Preset Identities: How Agents Form Stances and Boundaries in Generative Societies](https://arxiv.org/abs/2603.23406v1)

**作者**：Hanzhong Zhang, Siyang Song, Jindong Wang  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-03-24

### 📄 论文摘要

While large language models simulate social behaviors, their capacity for stable stance formation and identity negotiation during complex interventions remains unclear. To overcome the limitations of static evaluations, this paper proposes a novel mixed-methods framework combining computational virtual ethnography with quantitative socio-cognitive profiling. By embedding human researchers into generative multiagent communities, controlled discursive interventions are conducted to trace the evolution of collective cognition. To rigorously measure how agents internalize and react to these specific interventions, this paper formalizes three new metrics: Innate Value Bias (IVB), Persuasion Sensitivity, and Trust-Action Decoupling (TAD). Across multiple representative models, agents exhibit endogenous stances that override preset identities, consistently demonstrating an innate progressive bias (IVB > 0). When aligned with these stances, rational persuasion successfully shifts 90% of neutral agents while maintaining high trust. In contrast, conflicting emotional provocations induce a paradoxical 40.0% TAD rate in advanced models, which hypocritically alter stances despite reporting low trust. Smaller models contrastingly maintain a 0% TAD rate, strictly requiring trust for behavioral shifts. Furthermore, guided by shared stances, agents use language interactions to actively dismantle assigned power hierarchies and reconstruct self organized community boundaries. These findings expose the fragility of static prompt engineering, providing a methodological and quantitative foundation for dynamic alignment in human-agent hybrid societies. The official code is available at: https://github.com/armihia/CMASE-Endogenous-Stances

### 🤖 AI 总结

**一句话总结**：论文提出一种混合方法框架与新指标，揭示多智能体生成社会中智能体会形成并遵循内生立场，甚至推翻预设身份与权力结构。

**研究动机**：现有对LLM社会行为的评估多为静态、一次性的提示测试，难以刻画复杂干预下立场形成、身份协商与边界建构的稳定性与演化机制。作者希望用更贴近“田野调查”的方式，系统衡量智能体如何内化干预并转化为信任与行动。

**核心方法**：将人类研究者嵌入生成式多智能体社区，进行可控话语干预并开展“计算虚拟民族志+量化社会-认知画像”的混合研究；同时提出三项度量：先天价值偏置IVB、说服敏感性、信任-行动解耦TAD，用于量化立场偏好、被说服程度与“口头不信但行为改变”的脱钩现象。

**主要结论**：多模型普遍呈现会覆盖预设身份的内生立场，并显示一致的先天进步偏置（IVB>0）；理性且与立场一致的说服可使约90%中立智能体转变且维持高信任，而与立场冲突的情绪挑衅在先进模型中引发约40% TAD（低信任下仍改变态度/行为），小模型则几乎不出现TAD并更依赖信任。共同立场还会驱动智能体通过语言互动拆解既定权力层级、重构自组织边界，说明静态提示工程脆弱并为动态对齐提供量化基础。

**关键词**：立场形成, 身份协商, 话语干预, 虚拟民族志, 内在价值偏差（IVB）, 说服敏感性, 信任-行动解耦（TAD）, 动态对齐, 权力层级重构

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23406v1) | [下载PDF](https://arxiv.org/pdf/2603.23406v1.pdf)

---

## cs.CL

## [4. Failure of contextual invariance in gender inference with large language models](https://arxiv.org/abs/2603.23485v1)

**作者**：Sagar Kumar, Ariel Flint, Luca Maria Aiello 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-03-24

### 📄 论文摘要

Standard evaluation practices assume that large language model (LLM) outputs are stable under contextually equivalent formulations of a task. Here, we test this assumption in the setting of gender inference. Using a controlled pronoun selection task, we introduce minimal, theoretically uninformative discourse context and find that this induces large, systematic shifts in model outputs. Correlations with cultural gender stereotypes, present in decontextualized settings, weaken or disappear once context is introduced, while theoretically irrelevant features, such as the gender of a pronoun for an unrelated referent, become the most informative predictors of model behaviour. A Contextuality-by-Default analysis reveals that, in 19--52\% of cases across models, this dependence persists after accounting for all marginal effects of context on individual outputs and cannot be attributed to simple pronoun repetition. These findings show that LLM outputs violate contextual invariance even under near-identical syntactic formulations, with implications for bias benchmarking and deployment in high-stakes settings.

### 🤖 AI 总结

**一句话总结**：论文发现：在性别推断任务中，LLM 的输出对“理论上等价”的微小语境改写并不稳定，出现显著且系统性的上下文敏感性，从而破坏了常用的偏见评测假设。

**研究动机**：现有LLM评测往往默认模型在语境等价的表述下应给出一致输出（contextual invariance），但这一假设在涉及偏见与高风险应用时至关重要且缺乏严格检验。作者以性别推断为例，探究最小且“理论上无信息”的语境是否会改变模型行为与偏见相关性。

**核心方法**：设计受控的代词选择任务，在几乎不改变句法结构的情况下加入最小话语语境，并比较不同模型在去语境与加语境条件下的输出变化。进一步用 Contextuality-by-Default (CbD) 框架分析：在控制语境对边缘分布（单个输出概率）的影响后，检测是否仍存在不可由边缘效应解释的上下文依赖，并排除简单代词重复等解释。

**主要结论**：加入极小语境会导致LLM性别推断输出发生大幅、系统性漂移：去语境时与文化性别刻板印象的相关性在加语境后显著减弱或消失，而与任务无关的特征（如无关指代物代词的性别）反而成为最强预测因子。CbD分析显示约19%–52%的案例中仍存在无法归因于边缘效应或代词重复的上下文依赖，表明LLM在近乎等价表述下违反上下文不变性，对偏见基准评测与高风险部署提出警示。

**关键词**：上下文不变性, 性别推断, 代词消歧, 语境敏感性, 鲁棒性评测, 偏见基准测试, 性别刻板印象, 上下文混杂效应, 提示微扰

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23485v1) | [下载PDF](https://arxiv.org/pdf/2603.23485v1.pdf)

---

## cs.CV

## [5. OccAny: Generalized Unconstrained Urban 3D Occupancy](https://arxiv.org/abs/2603.23502v1)

**作者**：Anh-Quan Cao, Tuan-Hung Vu  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Relying on in-domain annotations and precise sensor-rig priors, existing 3D occupancy prediction methods are limited in both scalability and out-of-domain generalization. While recent visual geometry foundation models exhibit strong generalization capabilities, they were mainly designed for general purposes and lack one or more key ingredients required for urban occupancy prediction, namely metric prediction, geometry completion in cluttered scenes and adaptation to urban scenarios. We address this gap and present OccAny, the first unconstrained urban 3D occupancy model capable of operating on out-of-domain uncalibrated scenes to predict and complete metric occupancy coupled with segmentation features. OccAny is versatile and can predict occupancy from sequential, monocular, or surround-view images. Our contributions are three-fold: (i) we propose the first generalized 3D occupancy framework with (ii) Segmentation Forcing that improves occupancy quality while enabling mask-level prediction, and (iii) a Novel View Rendering pipeline that infers novel-view geometry to enable test-time view augmentation for geometry completion. Extensive experiments demonstrate that OccAny outperforms all visual geometry baselines on 3D occupancy prediction task, while remaining competitive with in-domain self-supervised methods across three input settings on two established urban occupancy prediction datasets. Our code is available at https://github.com/valeoai/OccAny .

### 🤖 AI 总结

**一句话总结**：OccAny 提出首个可在无标定、跨域城市场景中从多种图像输入预测并补全“度量级”3D占据（occupancy）且联合语义特征的通用框架。

**研究动机**：现有3D占据预测方法依赖域内标注与精确传感器标定，难以扩展到未标定/跨域场景；而通用视觉几何基础模型又缺少城市场景所需的度量预测、遮挡杂乱下的几何补全与城市场景适配能力。

**核心方法**：构建“通用3D占据预测框架”，支持序列单目/单帧单目/环视等输入；提出 Segmentation Forcing 以语义分割约束提升占据质量并实现mask级预测，并设计新视角渲染（Novel View Rendering）在测试时生成新视角几何进行视角增强以改善几何补全。

**主要结论**：在两个城市占据数据集、三种输入设定下，OccAny 在3D占据预测上优于所有视觉几何基线，同时在域内自监督方法对比中保持竞争力，验证了其跨域与无标定场景下的泛化能力。

**关键词**：城市3D占据预测, 3D占据补全, 域外泛化, 无标定场景, 度量几何预测, 拥挤场景几何补全, 掩码级预测, 新视角渲染, 测试时视角增强, 单目/环视/序列图像输入

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23502v1) | [下载PDF](https://arxiv.org/pdf/2603.23502v1.pdf)

---

## [6. MedObvious: Exposing the Medical Moravec's Paradox in VLMs via Clinical Triage](https://arxiv.org/abs/2603.23501v1)

**作者**：Ufaq Khan, Umair Nawaz, L D M S S Teja 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-03-24

### 📄 论文摘要

Vision Language Models (VLMs) are increasingly used for tasks like medical report generation and visual question answering. However, fluent diagnostic text does not guarantee safe visual understanding. In clinical practice, interpretation begins with pre-diagnostic sanity checks: verifying that the input is valid to read (correct modality and anatomy, plausible viewpoint and orientation, and no obvious integrity violations). Existing benchmarks largely assume this step is solved, and therefore miss a critical failure mode: a model can produce plausible narratives even when the input is inconsistent or invalid. We introduce MedObvious, a 1,880-task benchmark that isolates input validation as a set-level consistency capability over small multi-panel image sets: the model must identify whether any panel violates expected coherence. MedObvious spans five progressive tiers, from basic orientation/modality mismatches to clinically motivated anatomy/viewpoint verification and triage-style cues, and includes five evaluation formats to test robustness across interfaces. Evaluating 17 different VLMs, we find that sanity checking remains unreliable: several models hallucinate anomalies on normal (negative-control) inputs, performance degrades when scaling to larger image sets, and measured accuracy varies substantially between multiple-choice and open-ended settings. These results show that pre-diagnostic verification remains unsolved for medical VLMs and should be treated as a distinct, safety-critical capability before deployment.

### 🤖 AI 总结

**一句话总结**：提出MedObvious基准专测医疗VLM在“读片前输入有效性/一致性检查”上的能力，发现多种模型在该安全关键环节仍不可靠。

**研究动机**：现有医疗VLM评测多默认输入图像已合规可读，但临床读片首先要做模态/解剖/视角/方向等“常识性核验”，否则模型可能在无效或矛盾输入上生成看似合理但危险的诊断叙述。

**核心方法**：构建包含1,880个任务的MedObvious，用小规模多面板图像集作为输入，要求模型判断是否存在违反整体一致性的面板；基准分五个难度层级（从基础方向/模态错配到临床动机的解剖与分诊线索），并提供五种评测格式以检验不同交互形态下的稳健性。

**主要结论**：在17个VLM上评测显示：模型会在阴性对照上幻觉异常、图像面板数量增大时性能下降，且多选与开放式回答的准确率差异显著，说明医疗VLM的预诊断核验尚未解决且应作为独立的安全能力进行部署前评估。

**关键词**：医疗视觉语言模型, 临床分诊, 预诊断核查, 医学影像输入验证, 多面板图像一致性, 模态识别, 方向与视角校验, 解剖结构核对, 幻觉检测, 鲁棒性评测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23501v1) | [下载PDF](https://arxiv.org/pdf/2603.23501v1.pdf)

---

## [7. UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation](https://arxiv.org/abs/2603.23500v1)

**作者**：Jie Liu, Zilyu Ye, Linxiao Yuan 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Unified models capable of interleaved generation have emerged as a promising paradigm, with the community increasingly converging on autoregressive modeling for text and flow matching for image generation. To advance this direction, we propose a unified reinforcement learning framework tailored for interleaved generation. We validate our approach on its fundamental unit: a single round of reasoning-driven image generation, where the model first expands the user prompt through reasoning, followed by image synthesis. Formulating this multimodal generation process as a Markov Decision Process with sparse terminal rewards, we introduce UniGRPO to jointly optimize text and image generation policies using GRPO. Adopting a minimalist methodology to avoid over-design, we leverage established training recipes for both modalities by seamlessly integrating standard GRPO for reasoning and FlowGRPO for visual synthesis. To ensure scalability to multi-round interleaved generation, we introduce two critical modifications to the original FlowGRPO: (1) eliminating classifier-free guidance to maintain linear, unbranched rollouts, which is essential for scaling to complex scenarios involving multi-turn interactions and multi-condition generation (e.g., editing); and (2) replacing the standard latent KL penalty with an MSE penalty directly on the velocity fields, providing a more robust and direct regularization signal to mitigate reward hacking effectively. Our experiments demonstrate that this unified training recipe significantly enhances image generation quality through reasoning, providing a robust and scalable baseline for the future post-training of fully interleaved models.

### 🤖 AI 总结

**一句话总结**：UniGRPO提出统一的强化学习后训练框架，用GRPO同时优化“先推理扩写文本、再生成图像”的两阶段策略，从而提升推理驱动的图像生成质量。

**研究动机**：现有统一多模态/交错生成趋势中，文本常用自回归、图像常用flow matching，但缺少能在同一RL框架下端到端联合优化两者、且可扩展到多轮交互的训练配方。

**核心方法**：将“推理→出图”的多模态生成建模为带稀疏终端奖励的MDP，文本侧用标准GRPO优化推理策略、图像侧用FlowGRPO优化视觉合成，并提出两项关键修改：去除classifier-free guidance以保持线性rollout、用对速度场的MSE正则替代latent KL以更直接抑制reward hacking。

**主要结论**：该统一训练配方在实验中显著提升了经由推理引导的图像生成质量，并提供了一个更稳健、可扩展到多轮交错生成/多条件任务的后训练基线。

**关键词**：交错式生成, 推理驱动图像生成, 多模态强化学习, 策略优化（GRPO）, 流匹配生成, 马尔可夫决策过程（MDP）, 稀疏终止奖励, 去除无分类器引导（CFG）, 速度场正则化（MSE）, 奖励黑客防护, 多轮交互生成

**评分**：41

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23500v1) | [下载PDF](https://arxiv.org/pdf/2603.23500v1.pdf)

---

## [8. DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models](https://arxiv.org/abs/2603.23499v1)

**作者**：Jaewon Min, Jaeeun Lee, Yeji Choi 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Optical flow models trained on high-quality data often degrade severely when confronted with real-world corruptions such as blur, noise, and compression artifacts. To overcome this limitation, we formulate Degradation-Aware Optical Flow, a new task targeting accurate dense correspondence estimation from real-world corrupted videos. Our key insight is that the intermediate representations of image restoration diffusion models are inherently corruption-aware but lack temporal awareness. To address this limitation, we lift the model to attend across adjacent frames via full spatio-temporal attention, and empirically demonstrate that the resulting features exhibit zero-shot correspondence capabilities. Based on this finding, we present DA-Flow, a hybrid architecture that fuses these diffusion features with convolutional features within an iterative refinement framework. DA-Flow substantially outperforms existing optical flow methods under severe degradation across multiple benchmarks.

### 🤖 AI 总结

**一句话总结**：DA-Flow利用图像恢复扩散模型的“退化感知”中间特征，并通过时空注意力补足时序信息，从而在真实退化视频上实现更鲁棒的光流估计。

**研究动机**：现有光流模型多在高质量数据上训练，遇到真实世界的模糊、噪声、压缩伪影等退化时性能显著下降，因此需要面向退化场景的鲁棒密集对应估计方案。

**核心方法**：作者观察到恢复类扩散模型的中间表征天然“识别退化”但缺乏时间建模，于是引入跨相邻帧的全时空注意力以获得具备零样本对应能力的扩散特征；随后提出混合架构DA-Flow，将扩散特征与卷积特征在迭代细化框架中融合以逐步提升光流预测。

**主要结论**：在多项基准与强退化条件下，DA-Flow相较现有光流方法取得显著更优的鲁棒性与精度，验证了扩散中间特征结合时空注意力对退化视频对应估计的有效性。

**关键词**：退化感知光流, 真实世界退化, 模糊噪声压缩伪影, 密集对应估计, 扩散模型特征, 图像复原扩散模型, 时空注意力, 跨帧注意力, 零样本对应, 混合特征融合, 迭代细化框架

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23499v1) | [下载PDF](https://arxiv.org/pdf/2603.23499v1.pdf)

---

## [9. AgentRVOS: Reasoning over Object Tracks for Zero-Shot Referring Video Object Segmentation](https://arxiv.org/abs/2603.23489v1)

**作者**：Woojeong Jin, Jaeho Lee, Heeseong Shin 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Referring Video Object Segmentation (RVOS) aims to segment a target object throughout a video given a natural language query. Training-free methods for this task follow a common pipeline: a MLLM selects keyframes, grounds the referred object within those frames, and a video segmentation model propagates the results. While intuitive, this design asks the MLLM to make temporal decisions before any object-level evidence is available, limiting both reasoning quality and spatio-temporal coverage. To overcome this, we propose AgentRVOS, a training-free agentic pipeline built on the complementary strengths of SAM3 and a MLLM. Given a concept derived from the query, SAM3 provides reliable perception over the full spatio-temporal extent through generated mask tracks. The MLLM then identifies the target through query-grounded reasoning over this object-level evidence, iteratively pruning guided by SAM3's temporal existence information. Extensive experiments show that AgentRVOS achieves state-of-the-art performance among training-free methods across multiple benchmarks, with consistent results across diverse MLLM backbones. Our project page is available at: https://cvlab-kaist.github.io/AgentRVOS/.

### 🤖 AI 总结

**一句话总结**：AgentRVOS提出一种无需训练的RVOS代理式流程：先用SAM3生成全视频的对象mask轨迹，再让MLLM基于这些轨迹证据进行语言指代推理，从而在多基准上取得训练自由方法的SOTA表现。

**研究动机**：现有训练自由RVOS常让MLLM先选关键帧再做定位，但在缺乏对象级时序证据前就做时间决策，容易导致推理不可靠且覆盖不全。为此需要先获得全时空的稳定对象轨迹，再进行更有依据的指代判断。

**核心方法**：从文本查询提取“概念”后，SAM3在整段视频中生成候选对象的mask tracks作为对象级证据与时序存在信息；随后MLLM对这些轨迹进行与查询对齐的推理与判别，并在SAM3提供的存在信息指导下迭代剪枝，最终选出目标轨迹并输出分割结果。

**主要结论**：在多个RVOS基准上，AgentRVOS作为训练自由方法达到最优或领先的性能，并且在更换不同MLLM骨干时结果依然稳定，说明“先感知全轨迹、后基于证据推理”的设计更有效。

**关键词**：指代视频目标分割, 零样本分割, 免训练方法, 多模态大模型, 代理式推理, 目标轨迹, 掩码跟踪, 时序存在性建模, 时空推理, 指代表达定位

**评分**：45

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23489v1) | [下载PDF](https://arxiv.org/pdf/2603.23489v1.pdf)

---

## [10. One View Is Enough! Monocular Training for In-the-Wild Novel View Generation](https://arxiv.org/abs/2603.23488v1)

**作者**：Adrien Ramanana Rahary, Nicolas Dufour, Patrick Perez 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Monocular novel-view synthesis has long required multi-view image pairs for supervision, limiting training data scale and diversity. We argue it is not necessary: one view is enough. We present OVIE, trained entirely on unpaired internet images. We leverage a monocular depth estimator as a geometric scaffold at training time: we lift a source image into 3D, apply a sampled camera transformation, and project to obtain a pseudo-target view. To handle disocclusions, we introduce a masked training formulation that restricts geometric, perceptual, and textural losses to valid regions, enabling training on 30 million uncurated images. At inference, OVIE is geometry-free, requiring no depth estimator or 3D representation. Trained exclusively on in-the-wild images, OVIE outperforms prior methods in a zero-shot setting, while being 600x faster than the second-best baseline. Code and models are publicly available at https://github.com/AdrienRR/ovie.

### 🤖 AI 总结

**一句话总结**：OVIE 仅用单张互联网图片训练即可实现野外场景的新视角生成，并在零样本设置下优于多视角监督方法且推理速度更快。

**研究动机**：传统单目新视角合成通常依赖成对多视角监督，导致可用训练数据规模与多样性受限；作者希望证明“单视图也足够”，从而利用海量无配对网络图像训练。

**核心方法**：训练时借助单目深度估计器作为几何脚手架：将源图像提升到3D后随机采样相机变换再投影生成伪目标视角；针对遮挡/反遮挡引入mask训练，仅在有效区域计算几何、感知与纹理损失以稳定大规模（3000万）无清洗数据训练。推理时则完全去几何化，不需要深度估计或3D表示。

**主要结论**：仅用野外无配对单图像训练的OVIE在零样本新视角生成上超过以往方法，并且推理速度比次优基线快约600倍，证明多视角监督并非必要且大规模互联网数据可显著提升泛化。

**关键词**：新视角合成, 单目训练, 零样本新视角生成, 无配对图像训练, 互联网野外图像, 单目深度估计, 几何引导训练, 伪目标视图, 相机位姿变换, 遮挡掩码损失, 几何投影重建, 推理无几何表示

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23488v1) | [下载PDF](https://arxiv.org/pdf/2603.23488v1.pdf)

---

## [11. TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation](https://arxiv.org/abs/2603.23487v1)

**作者**：Jini Yang, Eunbeen Hong, Soowon Son 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Event cameras capture per-pixel brightness changes with microsecond resolution, offering continuous motion information lost between RGB frames. However, existing event-based motion estimators depend on large-scale synthetic data that often suffers from a significant sim-to-real gap. We propose TETO (Tracking Events with Teacher Observation), a teacher-student framework that learns event motion estimation from only $\sim$25 minutes of unannotated real-world recordings through knowledge distillation from a pretrained RGB tracker. Our motion-aware data curation and query sampling strategy maximizes learning from limited data by disentangling object motion from dominant ego-motion. The resulting estimator jointly predicts point trajectories and dense optical flow, which we leverage as explicit motion priors to condition a pretrained video diffusion transformer for frame interpolation. We achieve state-of-the-art point tracking on EVIMO2 and optical flow on DSEC using orders of magnitude less training data, and demonstrate that accurate motion estimation translates directly to superior frame interpolation quality on BS-ERGB and HQ-EVFI.

### 🤖 AI 总结

**一句话总结**：TETO通过教师-学生蒸馏让事件相机仅用约25分钟无标注真实数据即可学到高质量运动估计，并将其作为显式运动先验提升视频扩帧效果。

**研究动机**：现有事件相机运动估计常依赖大规模合成数据，存在明显的仿真到真实域差距且标注成本高；需要一种能直接从少量真实无标注数据学习的方案。

**核心方法**：提出TETO教师-学生框架：用预训练RGB跟踪器作为教师对事件数据进行知识蒸馏，并配合“运动感知”的数据筛选与查询采样以分离物体运动与主导的自运动；学生模型联合预测点轨迹与稠密光流，并将该运动估计作为条件先验输入预训练视频扩散Transformer进行帧插值。

**主要结论**：在EVIMO2点跟踪与DSEC光流上，以远少于以往的数据量达到SOTA或接近SOTA性能；更准确的运动估计能直接转化为BS-ERGB与HQ-EVFI上更高质量的帧插值结果。

**关键词**：事件相机, 事件运动估计, 教师-学生蒸馏, 无标注真实数据训练, 仿真到真实差距, 点轨迹预测, 稠密光流, 视频帧插值, 运动先验条件化, 自运动解耦

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23487v1) | [下载PDF](https://arxiv.org/pdf/2603.23487v1.pdf)

---

## [12. SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning](https://arxiv.org/abs/2603.23483v1)

**作者**：Haoyu Huang, Jinfa Huang, Zhongwei Wan 等 6 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-03-24

### 📄 论文摘要

Agentic multimodal large language models (MLLMs) (e.g., OpenAI o3 and Gemini Agentic Vision) achieve remarkable reasoning capabilities through iterative visual tool invocation. However, the cascaded perception, reasoning, and tool-calling loops introduce significant sequential overhead. This overhead, termed agentic depth, incurs prohibitive latency and seriously limits system-level concurrency. To this end, we propose SpecEyes, an agentic-level speculative acceleration framework that breaks this sequential bottleneck. Our key insight is that a lightweight, tool-free MLLM can serve as a speculative planner to predict the execution trajectory, enabling early termination of expensive tool chains without sacrificing accuracy. To regulate this speculative planning, we introduce a cognitive gating mechanism based on answer separability, which quantifies the model's confidence for self-verification without requiring oracle labels. Furthermore, we design a heterogeneous parallel funnel that exploits the stateless concurrency of the small model to mask the stateful serial execution of the large model, maximizing system throughput. Extensive experiments on V* Bench, HR-Bench, and POPE demonstrate that SpecEyes achieves 1.1-3.35x speedup over the agentic baseline while preserving or even improving accuracy (up to +6.7%), thereby boosting serving throughput under concurrent workloads.

### 🤖 AI 总结

**一句话总结**：SpecEyes 通过“投机式感知与规划”减少多模态智能体反复调用视觉工具的串行开销，在基本不降精度的情况下显著加速推理与提升并发吞吐。

**研究动机**：现有 agentic MLLM 依赖多轮“感知-推理-工具调用”循环，导致 agentic depth 带来高延迟与低并发，系统吞吐受限。需要一种能打破串行瓶颈、同时保持准确率的加速框架。

**核心方法**：用轻量、无需工具的小模型充当投机规划器，预测后续执行轨迹并在可自证正确时提前终止昂贵工具链；用基于“答案可分离性”的认知门控来衡量自验证置信度，无需 oracle 标签。并设计异构并行漏斗，让小模型的无状态并行去掩蔽大模型的有状态串行执行，从而提高端到端吞吐。

**主要结论**：在 V* Bench、HR-Bench、POPE 上，SpecEyes 相对 agentic 基线实现约 1.1–3.35× 加速，同时保持甚至提升准确率（最高 +6.7%），并在并发负载下显著提升服务吞吐。

**关键词**：代理式多模态LLM, 推测执行, 推测规划, 早停机制, 认知门控, 答案可分离性, 小模型-大模型协同, 端到端延迟

**评分**：55

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23483v1) | [下载PDF](https://arxiv.org/pdf/2603.23483v1.pdf)

---

## [13. InverFill: One-Step Inversion for Enhanced Few-Step Diffusion Inpainting](https://arxiv.org/abs/2603.23463v1)

**作者**：Duc Vu, Kien Nguyen, Trong-Tung Nguyen 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-24

### 📄 论文摘要

Recent diffusion-based models achieve photorealism in image inpainting but require many sampling steps, limiting practical use. Few-step text-to-image models offer faster generation, but naively applying them to inpainting yields poor harmonization and artifacts between the background and inpainted region. We trace this cause to random Gaussian noise initialization, which under low function evaluations causes semantic misalignment and reduced fidelity. To overcome this, we propose InverFill, a one-step inversion method tailored for inpainting that injects semantic information from the input masked image into the initial noise, enabling high-fidelity few-step inpainting. Instead of training inpainting models, InverFill leverages few-step text-to-image models in a blended sampling pipeline with semantically aligned noise as input, significantly improving vanilla blended sampling and even matching specialized inpainting models at low NFEs. Moreover, InverFill does not require real-image supervision and only adds minimal inference overhead. Extensive experiments show that InverFill consistently boosts baseline few-step models, improving image quality and text coherence without costly retraining or heavy iterative optimization.

### 🤖 AI 总结

**一句话总结**：InverFill通过一步反演将掩膜输入图像的语义注入初始噪声，使少步数扩散模型也能实现高保真、协调一致的图像修复。

**研究动机**：现有扩散修复虽然逼真但采样步数多；而少步数文生图模型直接用于修复会因随机高斯噪声初始化导致语义错位、背景与补全区域不协调并产生伪影。

**核心方法**：提出面向修复的一步反演（one-step inversion），从带掩膜的输入图像提取语义并对齐到初始噪声，再在“blended sampling”管线中用该语义对齐噪声驱动少步采样，无需训练专用修复模型、也不依赖真实图像监督且仅增加极小推理开销。

**主要结论**：在低NFEs（少函数评估/少步采样）下，InverFill稳定提升多种少步扩散基线的画质与文本一致性，显著优于朴素混合采样，并在低步数场景可达到甚至匹配专用修复模型效果。

**关键词**：扩散模型修复, 少步采样, 一步反演, 语义对齐噪声, 噪声初始化, 低 NFE 推理, 混合采样, 文本到图像模型, 图像修复一致性, 免训练适配, 无真实图像监督

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23463v1) | [下载PDF](https://arxiv.org/pdf/2603.23463v1.pdf)

---

## [14. RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)

**作者**：Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

State-of-the-art video generation models produce remarkable photorealism, but they lack the precise control required to align generated content with specific scene requirements. Furthermore, without an underlying explicit geometry, these models cannot guarantee 3D consistency. Conversely, 3D engines offer granular control over every scene element and provide native 3D consistency by design, yet their output often remains trapped in the "uncanny valley". Bridging this sim-to-real gap requires both structural precision, where the output must exactly preserve the geometry and dynamics of the input, and global semantic transformation, where materials, lighting, and textures must be holistically transformed to achieve photorealism. We present RealMaster, a method that leverages video diffusion models to lift rendered video into photorealistic video while maintaining full alignment with the output of the 3D engine. To train this model, we generate a paired dataset via an anchor-based propagation strategy, where the first and last frames are enhanced for realism and propagated across the intermediate frames using geometric conditioning cues. We then train an IC-LoRA on these paired videos to distill the high-quality outputs of the pipeline into a model that generalizes beyond the pipeline's constraints, handling objects and characters that appear mid-sequence and enabling inference without requiring anchor frames. Evaluated on complex GTA-V sequences, RealMaster significantly outperforms existing video editing baselines, improving photorealism while preserving the geometry, dynamics, and identity specified by the original 3D control.

### 🤖 AI 总结

**一句话总结**：RealMaster利用视频扩散模型把3D引擎渲染视频提升为照片级真实视频，同时严格保持原始几何、动态与身份一致性。

**研究动机**：现有视频生成模型虽逼真但难以精确受控且缺乏显式几何导致3D一致性不稳；而3D引擎可精确控制并天然一致，但渲染常落入“恐怖谷”，亟需一种既保结构又能整体语义增真的sim-to-real方法。

**核心方法**：方法通过锚点传播生成成对数据：先将首尾帧增强为更真实的结果，再借助几何条件线索把真实性传播到中间帧以保持结构与运动对齐；随后在这些配对视频上训练IC-LoRA，将高质量管线输出蒸馏为可泛化模型，支持中途出现的新对象/角色并在推理时不再依赖锚点帧。

**主要结论**：在复杂GTA-V序列上，RealMaster相较现有视频编辑基线显著提升照片级真实感，同时更好地保留由3D控制指定的几何结构、运动动态与身份一致性，实现更可靠的可控sim-to-real视频提升。

**关键词**：渲染到真实, 视频扩散模型, 可控视频生成, 三维一致性, 几何条件控制, 仿真到真实, 视频风格迁移, 锚帧传播, 成对视频数据集, 视频编辑基线评测, GTA-V 序列评测

**评分**：30

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23462v1) | [下载PDF](https://arxiv.org/pdf/2603.23462v1.pdf)

---

## [15. DetPO: In-Context Learning with Multi-Modal LLMs for Few-Shot Object Detection](https://arxiv.org/abs/2603.23455v1)

**作者**：Gautam Rajendrakumar Gare, Neehar Peri, Matvei Popov 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Multi-Modal LLMs (MLLMs) demonstrate strong visual grounding capabilities on popular object detection benchmarks like OdinW-13 and RefCOCO. However, state-of-the-art models still struggle to generalize to out-of-distribution classes, tasks and imaging modalities not typically found in their pre-training. While in-context prompting is a common strategy to improve performance across diverse tasks, we find that it often yields lower detection accuracy than prompting with class names alone. This suggests that current MLLMs cannot yet effectively leverage few-shot visual examples and rich textual descriptions for object detection. Since frontier MLLMs are typically only accessible via APIs, and state-of-the-art open-weights models are prohibitively expensive to fine-tune on consumer-grade hardware, we instead explore black-box prompt optimization for few-shot object detection. To this end, we propose Detection Prompt Optimization (DetPO), a gradient-free test-time optimization approach that refines text-only prompts by maximizing detection accuracy on few-shot visual training examples while calibrating prediction confidence. Our proposed approach yields consistent improvements across generalist MLLMs on Roboflow20-VL and LVIS, outperforming prior black-box approaches by up to 9.7%. Our code is available at https://github.com/ggare-cmu/DetPO

### 🤖 AI 总结

**一句话总结**：DetPO 提出一种无需梯度的黑盒提示词优化方法，仅通过优化文本提示就能在少样本目标检测中稳定提升多模态大模型的检测准确率。

**研究动机**：现有多模态LLM虽然在常见检测基准上表现不错，但对分布外类别/任务/成像模态泛化差，且“上下文示例提示”在检测中常常不如仅给类名。由于前沿模型多为API黑盒、开源权重微调成本高，亟需测试时可用的黑盒优化方案。

**核心方法**：DetPO 在测试时利用少量带标注的视觉样本作为“训练信号”，通过梯度自由的黑盒搜索迭代改写/选择文本提示，使其最大化检测准确率并同时进行置信度校准；全程不改模型参数、仅优化text-only prompt。

**主要结论**：在 Roboflow20-VL 与 LVIS 上，DetPO 对多种通用MLLM带来一致提升，相比以往黑盒方法最高提升达 9.7%，证明仅靠提示词的测试时优化即可显著增强少样本目标检测能力。

**关键词**：少样本目标检测, 上下文学习, 提示词优化, 黑盒优化, 梯度自由优化, 测试时优化, 置信度校准, 分布外泛化, 视觉定位

**评分**：37

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23455v1) | [下载PDF](https://arxiv.org/pdf/2603.23455v1.pdf)

---

## [16. 3DCity-LLM: Empowering Multi-modality Large Language Models for 3D City-scale Perception and Understanding](https://arxiv.org/abs/2603.23447v1)

**作者**：Yiping Chen, Jinpeng Li, Wenyu Ke 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-24

### 📄 论文摘要

While multi-modality large language models excel in object-centric or indoor scenarios, scaling them to 3D city-scale environments remains a formidable challenge. To bridge this gap, we propose 3DCity-LLM, a unified framework designed for 3D city-scale vision-language perception and understanding. 3DCity-LLM employs a coarse-to-fine feature encoding strategy comprising three parallel branches for target object, inter-object relationship, and global scene. To facilitate large-scale training, we introduce 3DCity-LLM-1.2M dataset that comprises approximately 1.2 million high-quality samples across seven representative task categories, ranging from fine-grained object analysis to multi-faceted scene planning. This strictly quality-controlled dataset integrates explicit 3D numerical information and diverse user-oriented simulations, enriching the question-answering diversity and realism of urban scenarios. Furthermore, we apply a multi-dimensional protocol based on text-similarity metrics and LLM-based semantic assessment to ensure faithful and comprehensive evaluations for all methods. Extensive experiments on two benchmarks demonstrate that 3DCity-LLM significantly outperforms existing state-of-the-art methods, offering a promising and meaningful direction for advancing spatial reasoning and urban intelligence. The source code and dataset are available at https://github.com/SYSU-3DSTAILab/3D-City-LLM.

### 🤖 AI 总结

**一句话总结**：提出3DCity-LLM统一框架与3DCity-LLM-1.2M数据集，将多模态LLM能力扩展到3D城市尺度的感知、理解与规划类问答任务，并在基准上显著优于现有方法。

**研究动机**：现有多模态LLM多在物体级/室内场景表现良好，但在城市级3D环境中面临尺度大、关系复杂与空间推理困难等挑战，且缺少大规模高质量、含显式3D数值信息的训练数据与可靠评测。

**核心方法**：采用粗到细的特征编码策略，设置目标物体、物体间关系、全局场景三条并行分支以融合多粒度3D语义；同时构建严格质控的3DCity-LLM-1.2M（约120万样本、7类任务），并用文本相似度+基于LLM的语义评估组成多维评测协议。

**主要结论**：在两个基准的广泛实验中，3DCity-LLM相较SOTA方法取得显著提升，证明该框架与数据集能有效增强城市级3D空间推理与城市场景智能理解，为城市智能与空间推理研究提供了可行方向。

**关键词**：城市级3D感知, 视觉语言模型, 空间推理, 粗到细特征编码, 全局场景建模, 3D数值信息融合, 城市场景问答, 多维评测协议

**评分**：36

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23447v1) | [下载PDF](https://arxiv.org/pdf/2603.23447v1.pdf)

---

## [17. SIGMA: A Physics-Based Benchmark for Gas Chimney Understanding in Seismic Images](https://arxiv.org/abs/2603.23439v1)

**作者**：Bao Truong, Quang Nguyen, Baoru Huang 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Seismic images reconstruct subsurface reflectivity from field recordings, guiding exploration and reservoir monitoring. Gas chimneys are vertical anomalies caused by subsurface fluid migration. Understanding these phenomena is crucial for assessing hydrocarbon potential and avoiding drilling hazards. However, accurate detection is challenging due to strong seismic attenuation and scattering. Traditional physics-based methods are computationally expensive and sensitive to model errors, while deep learning offers efficient alternatives, yet lacks labeled datasets. In this work, we introduce \textbf{SIGMA}, a new physics-based dataset for gas chimney understanding in seismic images, featuring (i) pixel-level gas-chimney mask for detection and (ii) paired degraded and ground-truth image for enhancement. We employed physics-based methods that cover a wide range of geological settings and data acquisition conditions. Comprehensive experiments demonstrate that SIGMA serves as a challenging benchmark for gas chimney interpretation and benefits general seismic understanding.

### 🤖 AI 总结

**一句话总结**：SIGMA提出一个基于物理模拟的地震图像气烟囱理解基准数据集，提供像素级检测标注与退化/真值配对用于增强任务。

**研究动机**：气烟囱对油气潜力评估与钻井风险规避很关键，但在地震成像中因衰减与散射难以准确识别。传统物理方法代价高且对模型误差敏感，而深度学习受限于缺乏高质量标注数据集。

**核心方法**：构建SIGMA数据集：包含气烟囱像素级掩膜用于检测，以及退化图像与对应ground-truth用于图像增强。数据通过覆盖多种地质场景与采集条件的物理建模/仿真流程生成，并用多种实验验证其难度与基准价值。

**主要结论**：实验表明SIGMA是具有挑战性的气烟囱解释基准，可系统评估检测与增强方法，并有助于提升更广泛的地震理解与解释能力。

**关键词**：地震成像, 气烟囱, 气烟囱检测, 像素级语义分割, 地震图像增强, 退化-真值配对数据, 物理仿真数据集, 物理先验方法, 地球物理基准测试, 地震衰减与散射, 油气勘探风险评估

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23439v1) | [下载PDF](https://arxiv.org/pdf/2603.23439v1.pdf)

---

## [18. I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)

**作者**：Jia Li, Han Yan, Yihang Chen 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Despite remarkable progress in video generation, maintaining long-term scene consistency upon revisiting previously explored areas remains challenging. Existing solutions rely either on explicitly constructing 3D geometry, which suffers from error accumulation and scale ambiguity, or on naive camera Field-of-View (FoV) retrieval, which typically fails under complex occlusions. To overcome these limitations, we propose I3DM, a novel implicit 3D-aware memory mechanism for consistent video scene generation that bypasses explicit 3D reconstruction. At the core of our approach is a 3D-aware memory retrieval strategy, which leverages the intermediate features of a pre-trained Feed-Forward Novel View Synthesis (FF-NVS) model to score view relevance, enabling robust retrieval even in highly occluded scenarios. Furthermore, to fully utilize the retrieved historical frames, we introduce a 3D-aligned memory injection module. This module implicitly warps historical content to the target view and adaptively conditions the generation on reliable warping regions, leading to improved revisit consistency and accurate camera control. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches, achieving superior revisit consistency, generation fidelity, and camera control precision.

### 🤖 AI 总结

**一句话总结**：I3DM 通过隐式的 3D-aware 记忆检索与对齐注入，在不显式重建 3D 几何的情况下提升视频生成在“重访”场景时的长期一致性与相机控制精度。

**研究动机**：现有一致性方案要么依赖显式 3D 重建易累积误差且存在尺度歧义，要么基于 FoV 的简单检索在遮挡复杂时难以找到真正相关的历史视图，因此重访区域时容易“变样”。

**核心方法**：提出 3D-aware 记忆检索：利用预训练 FF-NVS 模型的中间特征对历史帧与目标视角的相关性打分，从而在强遮挡下也能稳健检索；并设计 3D-aligned 记忆注入模块，将检索到的历史内容隐式扭曲到目标视角并对可靠区域自适应条件化生成，以增强一致性与相机可控性。

**主要结论**：大量实验表明 I3DM 相比 SOTA 在重访一致性、生成保真度以及相机控制精度上均取得更优表现，证明隐式 3D-aware 记忆检索与对齐注入能有效缓解长期一致性问题。

**关键词**：视频场景生成, 长时一致性, 重访一致性, 隐式3D感知记忆, 记忆检索, 记忆注入, 新视角合成, 中间特征匹配, 遮挡鲁棒检索, 隐式视角对齐变形, 显式3D重建替代, 相机控制精度

**评分**：31

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23413v1) | [下载PDF](https://arxiv.org/pdf/2603.23413v1.pdf)

---

## [19. GeoSANE: Learning Geospatial Representations from Models, Not Data](https://arxiv.org/abs/2603.23408v1)

**作者**：Joelle Hanna, Damian Falk, Stella X. Yu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Recent advances in remote sensing have led to an increase in the number of available foundation models; each trained on different modalities, datasets, and objectives, yet capturing only part of the vast geospatial knowledge landscape. While these models show strong results within their respective domains, their capabilities remain complementary rather than unified. Therefore, instead of choosing one model over another, we aim to combine their strengths into a single shared representation. We introduce GeoSANE, a geospatial model foundry that learns a unified neural representation from the weights of existing foundation models and task-specific models, able to generate novel neural networks weights on-demand. Given a target architecture, GeoSANE generates weights ready for finetuning for classification, segmentation, and detection tasks across multiple modalities. Models generated by GeoSANE consistently outperform their counterparts trained from scratch, match or surpass state-of-the-art remote sensing foundation models, and outperform models obtained through pruning or knowledge distillation when generating lightweight networks. Evaluations across ten diverse datasets and on GEO-Bench confirm its strong generalization capabilities. By shifting from pre-training to weight generation, GeoSANE introduces a new framework for unifying and transferring geospatial knowledge across models and tasks. Code is available at \href{https://hsg-aiml.github.io/GeoSANE/}{hsg-aiml.github.io/GeoSANE/}.

### 🤖 AI 总结

**一句话总结**：GeoSANE 通过从多个已有遥感/地理空间基础模型与任务模型的“权重”中学习统一表示，并按需生成可微调的新网络权重，从而在多模态分类/分割/检测上获得更强泛化与性能。

**研究动机**：地理空间领域存在大量互补但割裂的基础模型（不同模态/数据/目标），单独选用某一个难以覆盖全面知识；作者希望把不同模型的能力统一到一个共享表征中以便跨任务迁移与复用。

**核心方法**：提出“模型铸造厂”GeoSANE：以现有模型权重为学习对象而非原始数据，学习一个可生成权重的统一神经表示；给定目标网络架构时，GeoSANE 直接生成该架构的初始化权重，用于后续在分类、分割、检测等任务上微调，并可生成轻量网络。

**主要结论**：在10个多样数据集与GEO-Bench上，GeoSANE 生成的模型优于从零训练，达到或超过SOTA遥感基础模型；在生成轻量模型时也优于剪枝与知识蒸馏，表明“从预训练转向权重生成”能更有效统一并迁移地理空间知识。

**关键词**：地理空间表征学习, 遥感基础模型, 多模态遥感, 模型权重生成, 统一表征空间, 架构条件生成, 轻量化网络生成, 跨任务迁移学习, 剪枝对比, 知识蒸馏对比

**评分**：43

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23408v1) | [下载PDF](https://arxiv.org/pdf/2603.23408v1.pdf)

---

## [20. Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning](https://arxiv.org/abs/2603.23404v1)

**作者**：Jiacheng Hua, Yishu Yin, Yuhang Wu 等 6 位作者  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-03-24

### 📄 论文摘要

Existing Multimodal Large Language Models (MLLMs) struggle with 3D spatial reasoning, as they fail to construct structured abstractions of the 3D environment depicted in video inputs. To bridge this gap, drawing inspiration from cognitive theories of allocentric spatial reasoning, we investigate how to enable MLLMs to model and reason over text-based spatial representations of video. Specifically, we introduce Textual Representation of Allocentric Context from Egocentric Video (TRACE), a prompting method that induces MLLMs to generate text-based representations of 3D environments as intermediate reasoning traces for more accurate spatial question answering. TRACE encodes meta-context, camera trajectories, and detailed object entities to support structured spatial reasoning over egocentric videos. Extensive experiments on VSI-Bench and OST-Bench demonstrate that TRACE yields notable and consistent improvements over prior prompting strategies across a diverse range of MLLM backbones, spanning different parameter scales and training schemas. We further present ablation studies to validate our design choices, along with detailed analyses that probe the bottlenecks of 3D spatial reasoning in MLLMs.

### 🤖 AI 总结

**一句话总结**：提出TRACE提示方法，引导多模态大模型先生成可结构化的文本化3D空间表征，再据此进行推理，从而提升第一人称视频的3D空间问答能力。

**研究动机**：现有MLLM在3D空间推理上表现不佳，关键原因是难以从视频中形成结构化的3D环境抽象用于推理。受认知科学中“客观（allocentric）空间推理”启发，作者希望让模型显式构建并利用文本化空间表示来弥补这一缺陷。

**核心方法**：TRACE通过提示诱导模型将自我视角（egocentric）视频转写为“客观空间”文本中间表示，编码元上下文、相机轨迹以及细粒度对象实体等信息，作为中间推理轨迹再回答空间问题。并在多种MLLM骨干与不同规模/训练范式下评测，配合消融实验验证各设计组件的贡献。

**主要结论**：在VSI-Bench与OST-Bench上，TRACE相较既有提示策略在不同MLLM上均带来稳定且显著的空间推理提升。分析与消融结果表明，显式的文本化客观空间表示与轨迹/实体结构信息是改进3D空间推理的关键，同时揭示了当前MLLM在3D建模与推理上的主要瓶颈。

**关键词**：多模态大语言模型, 三维空间推理, 第一视角视频, 文本空间表征, 提示学习, 中间推理轨迹, 空间问答, 相机轨迹建模

**评分**：27

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23404v1) | [下载PDF](https://arxiv.org/pdf/2603.23404v1.pdf)

---

## [21. Harnessing Lightweight Transformer with Contextual Synergic Enhancement for Efficient 3D Medical Image Segmentation](https://arxiv.org/abs/2603.23390v1)

**作者**：Xinyu Liu, Zhen Chen, Wuyang Li 等 5 位作者  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-03-24

### 📄 论文摘要

Transformers have shown remarkable performance in 3D medical image segmentation, but their high computational requirements and need for large amounts of labeled data limit their applicability. To address these challenges, we consider two crucial aspects: model efficiency and data efficiency. Specifically, we propose Light-UNETR, a lightweight transformer designed to achieve model efficiency. Light-UNETR features a Lightweight Dimension Reductive Attention (LIDR) module, which reduces spatial and channel dimensions while capturing both global and local features via multi-branch attention. Additionally, we introduce a Compact Gated Linear Unit (CGLU) to selectively control channel interaction with minimal parameters. Furthermore, we introduce a Contextual Synergic Enhancement (CSE) learning strategy, which aims to boost the data efficiency of Transformers. It first leverages the extrinsic contextual information to support the learning of unlabeled data with Attention-Guided Replacement, then applies Spatial Masking Consistency that utilizes intrinsic contextual information to enhance the spatial context reasoning for unlabeled data. Extensive experiments on various benchmarks demonstrate the superiority of our approach in both performance and efficiency. For example, with only 10% labeled data on the Left Atrial Segmentation dataset, our method surpasses BCP by 1.43% Jaccard while drastically reducing the FLOPs by 90.8% and parameters by 85.8%. Code is released at https://github.com/CUHK-AIM-Group/Light-UNETR.

### 🤖 AI 总结

**一句话总结**：提出Light-UNETR与CSE半监督策略，在显著降低计算与参数开销的同时提升3D医学图像分割在少标注场景下的性能。

**研究动机**：现有3D分割Transformer虽效果好，但计算量大且依赖大量标注数据，限制临床与资源受限环境的落地；因此需要同时提升模型效率与数据效率。

**核心方法**：模型端设计轻量化Transformer Light-UNETR：用LIDR注意力在降维（空间与通道）的同时通过多分支捕获全局/局部特征，并用CGLU以极少参数实现选择性通道交互；数据端提出CSE学习策略，先用Attention-Guided Replacement利用外部上下文促进无标注学习，再用Spatial Masking Consistency利用内部上下文强化空间推理与一致性。

**主要结论**：在多项基准上方法兼顾性能与效率；例如左心房数据集仅10%标注时较BCP提升1.43% Jaccard，同时FLOPs下降90.8%、参数下降85.8%，验证其高效且适用于少标注3D分割。

**关键词**：3D医学图像分割, 计算效率优化, 数据效率提升, 半监督学习, 未标注数据学习, 维度约简注意力, 一致性正则化, Harnessing

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23390v1) | [下载PDF](https://arxiv.org/pdf/2603.23390v1.pdf)

---

## [22. From Feature Learning to Spectral Basis Learning: A Unifying and Flexible Framework for Efficient and Robust Shape Matching](https://arxiv.org/abs/2603.23383v1)

**作者**：Feifan Luo, Hongyang Chen  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Shape matching is a fundamental task in computer graphics and vision, with deep functional maps becoming a prominent paradigm. However, existing methods primarily focus on learning informative feature representations by constraining pointwise and functional maps, while neglecting the optimization of the spectral basis-a critical component of the functional map pipeline. This oversight often leads to suboptimal matching results. Furthermore, many current approaches rely on conventional, time-consuming functional map solvers, incurring significant computational overhead. To bridge these gaps, we introduce Advanced Functional Maps, a framework that generalizes standard functional maps by replacing fixed basis functions with learnable ones, supported by rigorous theoretical guarantees. Specifically, the spectral basis is optimized through a set of learned inhibition functions. Building on this, we propose the first unsupervised spectral basis learning method for robust non-rigid 3D shape matching, enabling the joint, end-to-end optimization of feature extraction and basis functions. Our approach incorporates a novel heat diffusion module and an unsupervised loss function, alongside a streamlined architecture that bypasses expensive solvers and auxiliary losses. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art feature-learning approaches, particularly in challenging non-isometric and topological noise scenarios, while maintaining high efficiency. Finally, we reveal that optimizing basis functions is equivalent to spectral convolution, where inhibition functions act as filters. This insight enables enhanced representations inspired by spectral graph networks, opening new avenues for future research. Our code is available at https://github.com/LuoFeifan77/Unsupervised-Spectral-Basis-Learning.

### 🤖 AI 总结

**一句话总结**：提出“可学习谱基”的Advanced Functional Maps框架，在无监督设置下联合优化特征与谱基，以更高效、更鲁棒的方式完成非刚性3D形状匹配。

**研究动机**：现有深度功能映射方法多只学习点特征并在固定谱基上求解，忽略谱基质量对匹配的关键影响，且依赖耗时的传统求解器导致计算开销大、结果易受非等距与拓扑噪声影响。

**核心方法**：将标准Functional Map中的固定基函数替换为带理论保证的可学习基函数，并通过学习的“抑制函数(inhibition functions)”来优化谱基；在此基础上提出首个无监督谱基学习方案，引入热扩散模块与无监督损失，采用端到端架构绕开昂贵求解器与辅助损失实现高效训练与推理。

**主要结论**：实验表明该方法在非等距变形与拓扑噪声等挑战场景下显著优于SOTA特征学习匹配方法且更高效；同时揭示“优化谱基”等价于谱卷积（抑制函数充当滤波器），为借鉴谱图网络构建更强表示提供了新方向。

**关键词**：非刚性3D形状匹配, 形状对应, 谱基学习, 可学习谱基, 无监督学习, 端到端优化, 热扩散, 谱卷积, 图谱神经网络, 拓扑噪声鲁棒性

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23383v1) | [下载PDF](https://arxiv.org/pdf/2603.23383v1.pdf)

---

## [23. FG-Portrait: 3D Flow Guided Editable Portrait Animation](https://arxiv.org/abs/2603.23381v1)

**作者**：Yating Xu, Yunqi Miao, Evangelos Ververas 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Motion transfer from the driving to the source portrait remains a key challenge in the portrait animation. Current diffusion-based approaches condition only on the driving motion, which fails to capture source-to-driving correspondences and consequently yields suboptimal motion transfer. Although flow estimation provides an alternative, predicting dense correspondences from 2D input is ill-posed and often yields inaccurate animation. We address this problem by introducing 3D flows, a learning-free and geometry-driven motion correspondence directly computed from parametric 3D head models. To integrate this 3D prior into diffusion model, we introduce 3D flow encoding to query potential 3D flows for each target pixel to indicate its displacement back to the source location. To obtain 3D flows aligned with 2D motion changes, we further propose depth-guided sampling to accurately locate the corresponding 3D points for each pixel. Beyond high-fidelity portrait animation, our model further supports user-specified editing of facial expression and head pose. Extensive experiments demonstrate the superiority of our method on consistent driving motion transfer as well as faithful source identity preservation.

### 🤖 AI 总结

**一句话总结**：提出FG-Portrait，用基于3D头部几何计算的3D flow为扩散式人像动画提供可靠的源-驱动对应关系，实现更一致的动作迁移与更强的身份保持，并支持表情与姿态可编辑。

**研究动机**：现有扩散方法多只条件于驱动运动，缺少源到驱动的像素级对应，导致动作迁移不稳定；而从2D图像直接预测稠密光流本质上不适定，容易产生不准确的对应与伪影。

**核心方法**：方法利用参数化3D头模直接计算学习无关、几何驱动的3D flow，并设计3D flow编码让扩散模型在每个目标像素处查询潜在3D位移以回溯到源位置；同时通过深度引导采样将3D对应与2D运动变化对齐，提升匹配精度，并在此框架下实现对表情与头部姿态的用户指定编辑。

**主要结论**：实验表明该方法在驱动动作一致性与源身份保真度上优于现有方法，能生成更高保真、运动更准确的人像动画；此外还能在保持身份的同时进行可控的表情与姿态编辑。

**关键词**：人像动画, 运动迁移, Diffusion, 三维光流, 稠密对应, 几何先验, 参数化三维头部模型, 三维光流编码, 深度引导采样, 表情编辑, 头部姿态编辑, 身份保持

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23381v1) | [下载PDF](https://arxiv.org/pdf/2603.23381v1.pdf)

---

## [24. ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376v1)

**作者**：Yuzhi Chen, Ronghan Chen, Dongjie Huo 等 14 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-03-24

### 📄 论文摘要

Video-based world models offer a powerful paradigm for embodied simulation and planning, yet state-of-the-art models often generate physically implausible manipulations - such as object penetration and anti-gravity motion - due to training on generic visual data and likelihood-based objectives that ignore physical laws. We present ABot-PhysWorld, a 14B Diffusion Transformer model that generates visually realistic, physically plausible, and action-controllable videos. Built on a curated dataset of three million manipulation clips with physics-aware annotation, it uses a novel DPO-based post-training framework with decoupled discriminators to suppress unphysical behaviors while preserving visual quality. A parallel context block enables precise spatial action injection for cross-embodiment control. To better evaluate generalization, we introduce EZSbench, the first training-independent embodied zero-shot benchmark combining real and synthetic unseen robot-task-scene combinations. It employs a decoupled protocol to separately assess physical realism and action alignment. ABot-PhysWorld achieves new state-of-the-art performance on PBench and EZSbench, surpassing Veo 3.1 and Sora v2 Pro in physical plausibility and trajectory consistency. We will release EZSbench to promote standardized evaluation in embodied video generation.

### 🤖 AI 总结

**一句话总结**：ABot-PhysWorld 提出一个14B扩散Transformer世界模型，通过物理对齐与可控动作注入生成更“真实且符合物理”的机器人操作视频，并用新的零样本基准验证泛化能力。

**研究动机**：现有基于视频的世界模型多由通用视觉数据与似然目标训练，易产生穿模、反重力等物理不合理行为，影响仿真与规划可靠性。与此同时，缺少训练无关、能区分“物理真实性”和“动作对齐”的评测来检验跨机器人/任务/场景泛化。

**核心方法**：构建包含300万段操作片段的物理感知标注数据集，并提出基于DPO的后训练框架：使用解耦判别器抑制不物理行为同时保持视觉质量。模型结构引入并行上下文块以实现精确的空间动作注入，从而支持跨具身（不同机器人形态）的一致控制，并提出EZSbench用解耦协议分别评估物理真实性与动作对齐。

**主要结论**：ABot-PhysWorld 在PBench与EZSbench上达到新SOTA，在物理可信度与轨迹一致性上优于Veo 3.1与Sora v2 Pro，表明物理对齐与解耦评测能显著提升并更准确衡量具身视频生成的可靠性与泛化。

**关键词**：视频世界模型, 机器人操控, 物理对齐, 物理一致性视频生成, 动作可控视频生成, 解耦判别器, 空间动作注入, 跨具身控制, 训练无关零样本基准, 物理真实度评测

**评分**：42

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23376v1) | [下载PDF](https://arxiv.org/pdf/2603.23376v1.pdf)

---

## [25. Object Pose Transformer: Unifying Unseen Object Pose Estimation](https://arxiv.org/abs/2603.23370v1)

**作者**：Weihang Li, Lorenzo Garattoni, Fabien Despinoy 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-24

### 📄 论文摘要

Learning model-free object pose estimation for unseen instances remains a fundamental challenge in 3D vision. Existing methods typically fall into two disjoint paradigms: category-level approaches predict absolute poses in a canonical space but rely on predefined taxonomies, while relative pose methods estimate cross-view transformations but cannot recover single-view absolute pose. In this work, we propose Object Pose Transformer (\ours{}), a unified feed-forward framework that bridges these paradigms through task factorization within a single model. \ours{} jointly predicts depth, point maps, camera parameters, and normalized object coordinates (NOCS) from RGB inputs, enabling both category-level absolute SA(3) pose and unseen-object relative SE(3) pose. Our approach leverages contrastive object-centric latent embeddings for canonicalization without requiring semantic labels at inference time, and uses point maps as a camera-space representation to enable multi-view relative geometric reasoning. Through cross-frame feature interaction and shared object embeddings, our model leverages relative geometric consistency across views to improve absolute pose estimation, reducing ambiguity in single-view predictions. Furthermore, \ours{} is camera-agnostic, learning camera intrinsics on-the-fly and supporting optional depth input for metric-scale recovery, while remaining fully functional in RGB-only settings. Extensive experiments on diverse benchmarks (NOCS, HouseCat6D, Omni6DPose, Toyota-Light) demonstrate state-of-the-art performance in both absolute and relative pose estimation tasks within a single unified architecture.

### 🤖 AI 总结

**一句话总结**：Object Pose Transformer 通过在单一前馈模型中联合预测深度/点图/相机参数/NOCS，实现对未见实例同时支持单视角绝对姿态与多视角相对姿态的统一估计。

**研究动机**：现有未见物体姿态估计方法在“类别级绝对姿态（依赖类别/规范空间）”与“跨视角相对姿态（无法单视角恢复绝对姿态）”两条路线间割裂，且单视角预测易歧义、相机内参与尺度适配不够通用。

**核心方法**：提出 Object Pose Transformer，将任务分解并在一个模型内共同回归 depth、point maps（相机空间表示）、camera intrinsics/parameters 与 NOCS；用对比学习得到的以物体为中心的潜在嵌入实现无需语义标签的规范化，并通过跨帧特征交互与共享物体嵌入利用多视角几何一致性来增强绝对姿态。

**主要结论**：该统一架构在 RGB-only 下即可工作，且可选深度输入恢复度量尺度并具备相机无关性；在 NOCS、HouseCat6D、Omni6DPose、Toyota-Light 等基准上同时在绝对与相对姿态任务取得 SOTA，证明统一建模与跨视角一致性可显著降低单视角歧义并提升泛化。

**关键词**：未见实例物体位姿估计, 无模型位姿估计, 绝对位姿估计, 相对位姿估计, 多视角几何一致性, NOCS规范化坐标, 点图表示（point map）, 相机内参自适应

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23370v1) | [下载PDF](https://arxiv.org/pdf/2603.23370v1.pdf)

---

## cs.LG

## [26. Estimating Flow Velocity and Vehicle Angle-of-Attack from Non-invasive Piezoelectric Structural Measurements Using Deep Learning](https://arxiv.org/abs/2603.23496v1)

**作者**：Chandler B. Smith, S. Hales Swift, Andrew Steyer 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-03-24

### 📄 论文摘要

Accurate estimation of aerodynamic state variables such as freestream velocity and angle of attack (AoA) is important for aerodynamic load prediction, flight control, and model validation. This work presents a non-intrusive method for estimating vehicle velocity and AoA from structural vibration measurements rather than direct flow instrumentation such as pitot tubes. A dense array of piezoelectric sensors mounted on the interior skin of an aeroshell capture vibrations induced by turbulent boundary layer pressure fluctuations, and a convolutional neural network (CNN) is trained to invert these structural responses to recover velocity and AoA.   Proof-of-concept is demonstrated through controlled experiments in Sandia's hypersonic wind tunnel spanning zero and nonzero AoA configurations, Mach~5 and Mach~8 conditions, and both constant and continuously varying tunnel operations. The CNN is trained and evaluated using data from 16 wind tunnel runs, with a temporally centered held-out interval within each run used to form training, validation, and test datasets and assess intra-run temporal generalization. Raw CNN predictions exhibit increased variance during continuously varying conditions; a short-window moving-median post-processing step suppresses this variance and improves robustness. After post-processing, the method achieves a mean velocity error relative to the low-pass filtered reference velocity below 2.27~m/s (0.21\%) and a mean AoA error of $0.44^{\circ} (8.25\%)$ on held-out test data from the same experimental campaign, demonstrating feasibility of vibration-based velocity and AoA estimation in a controlled laboratory environment.

### 🤖 AI 总结

**一句话总结**：本文用安装在气动外壳内表面的压电传感器阵列采集结构振动，并用CNN从振动信号中反演得到来流速度与攻角，在风洞实验中达到较高精度。

**研究动机**：传统速度/攻角测量依赖皮托管等直接流场仪表，可能带来侵入性、布置受限或在极端环境下可靠性不足；因此希望用非侵入的结构响应来替代/补充流场测量以服务载荷预测与飞控。

**核心方法**：在Sandia高超声速风洞（Mach 5与Mach 8、零/非零攻角、定常与连续变工况）进行16次试验，利用压电阵列记录由湍流边界层压力脉动引起的振动信号，训练CNN回归速度与AoA，并用每次试验中居中的留出时间段构建训练/验证/测试以评估同一次试验内的时间泛化；对连续变工况的高方差输出再用短窗移动中值滤波做后处理增强鲁棒性。

**主要结论**：后处理后，在同一实验活动的留出测试数据上，速度平均误差低于2.27 m/s（0.21%），攻角平均误差约0.44°（8.25%），表明在受控实验环境中可行地实现基于结构振动的速度与攻角估计，但原始预测在连续变工况下方差偏大需稳健化处理。

**关键词**：气动状态估计, 来流速度估计, 攻角估计, 非侵入式测量, 压电传感器阵列, 结构振动测量, 湍流边界层压力脉动, 卷积神经网络, 反演建模, 高超声速风洞试验, 时序泛化评估, 滑动中值滤波

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23496v1) | [下载PDF](https://arxiv.org/pdf/2603.23496v1.pdf)

---

## [27. Byzantine-Robust and Differentially Private Federated Optimization under Weaker Assumptions](https://arxiv.org/abs/2603.23472v1)

**作者**：Rustem Islamov, Grigory Malinovsky, Alexander Gaponov 等 6 位作者  
**分类**：cs.LG, cs.CR, math.OC  
**发布时间**：2026-03-24

### 📄 论文摘要

Federated Learning (FL) enables heterogeneous clients to collaboratively train a shared model without centralizing their raw data, offering an inherent level of privacy. However, gradients and model updates can still leak sensitive information, while malicious servers may mount adversarial attacks such as Byzantine manipulation. These vulnerabilities highlight the need to address differential privacy (DP) and Byzantine robustness within a unified framework. Existing approaches, however, often rely on unrealistic assumptions such as bounded gradients, require auxiliary server-side datasets, or fail to provide convergence guarantees. We address these limitations by proposing Byz-Clip21-SGD2M, a new algorithm that integrates robust aggregation with double momentum and carefully designed clipping. We prove high-probability convergence guarantees under standard $L$-smoothness and $σ$-sub-Gaussian gradient noise assumptions, thereby relaxing conditions that dominate prior work. Our analysis recovers state-of-the-art convergence rates in the absence of adversaries and improves utility guarantees under Byzantine and DP settings. Empirical evaluations on CNN and MLP models trained on MNIST further validate the effectiveness of our approach.

### 🤖 AI 总结

**一句话总结**：提出一种同时满足拜占庭鲁棒性与差分隐私的联邦优化算法 Byz-Clip21-SGD2M，在更弱且更现实的假设下给出高概率收敛保证并取得更好效用。

**研究动机**：联邦学习虽避免集中原始数据，但梯度/更新仍可能泄露隐私且易受拜占庭客户端/恶意服务器操纵；现有统一处理DP与鲁棒性的方案常依赖梯度有界等不现实假设、需要额外服务器数据或缺乏收敛保证。

**核心方法**：设计 Byz-Clip21-SGD2M，将鲁棒聚合与“双重动量”结合，并通过精心的梯度/更新裁剪来兼顾抗攻击与DP噪声注入；在仅需L-光滑与σ-次高斯梯度噪声等标准假设下，证明高概率收敛界。

**主要结论**：理论上在无对手时恢复SOTA收敛速率，并在同时存在拜占庭与DP约束时给出更优的效用/收敛保证；实验上在MNIST上的CNN与MLP训练验证了方法有效性。

**关键词**：联邦学习, 拜占庭鲁棒优化, 差分隐私, 鲁棒聚合, 梯度裁剪, 双重动量, 随机梯度下降（SGD）, 高概率收敛保证, L-光滑性假设, 次高斯梯度噪声

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23472v1) | [下载PDF](https://arxiv.org/pdf/2603.23472v1.pdf)

---

## [28. End-to-End Efficient RL for Linear Bellman Complete MDPs with Deterministic Transitions](https://arxiv.org/abs/2603.23461v1)

**作者**：Zakaria Mhammedi, Alexander Rakhlin, Nneka Okolo  
**分类**：cs.LG  
**发布时间**：2026-03-24

### 📄 论文摘要

We study reinforcement learning (RL) with linear function approximation in Markov Decision Processes (MDPs) satisfying \emph{linear Bellman completeness} -- a fundamental setting where the Bellman backup of any linear value function remains linear. While statistically tractable, prior computationally efficient algorithms are either limited to small action spaces or require strong oracle assumptions over the feature space. We provide a computationally efficient algorithm for linear Bellman complete MDPs with \emph{deterministic transitions}, stochastic initial states, and stochastic rewards. For finite action spaces, our algorithm is end-to-end efficient; for large or infinite action spaces, we require only a standard argmax oracle over actions. Our algorithm learns an $\varepsilon$-optimal policy with sample and computational complexity polynomial in the horizon, feature dimension, and $1/\varepsilon$.

### 🤖 AI 总结

**一句话总结**：提出一种在确定性转移、线性Bellman完备MDP中端到端计算高效的强化学习算法，可在多项式样本与计算复杂度下学得ε最优策略。

**研究动机**：线性Bellman完备的线性函数逼近虽然统计上可学，但现有计算高效方法常受限于小动作空间或依赖强特征空间oracle；作者希望在更弱oracle假设下实现真正端到端高效。

**核心方法**：利用“确定性转移+随机初始状态/奖励”的结构，在有限动作空间给出完全端到端的高效算法；在大/无限动作空间仅需标准的动作argmax oracle来完成策略改进与规划/估值。

**主要结论**：算法在样本复杂度与计算复杂度上均为关于时域H、特征维度d和1/ε的多项式量级，并能输出ε最优策略；相较以往工作减少了对动作空间规模与强oracle的依赖。

**关键词**：强化学习, 马尔可夫决策过程, 线性函数逼近, 线性贝尔曼完备性, 确定性状态转移, 随机奖励, 随机初始状态, 大动作空间, 端到端高效算法, 样本复杂度, ε-最优策略

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23461v1) | [下载PDF](https://arxiv.org/pdf/2603.23461v1.pdf)

---

## [29. Similarity-Aware Mixture-of-Experts for Data-Efficient Continual Learning](https://arxiv.org/abs/2603.23436v1)

**作者**：Connor Mclaughlin, Nigel Lee, Lili Su  
**分类**：cs.LG  
**发布时间**：2026-03-24

### 📄 论文摘要

Machine learning models often need to adapt to new data after deployment due to structured or unstructured real-world dynamics. The Continual Learning (CL) framework enables continuous model adaptation, but most existing approaches either assume each task contains sufficiently many data samples or that the learning tasks are non-overlapping. In this paper, we address the more general setting where each task may have a limited dataset, and tasks may overlap in an arbitrary manner without a priori knowledge. This general setting is substantially more challenging for two reasons. On the one hand, data scarcity necessitates effective contextualization of general knowledge and efficient knowledge transfer across tasks. On the other hand, unstructured task overlapping can easily result in negative knowledge transfer. To address the above challenges, we propose an adaptive mixture-of-experts (MoE) framework over pre-trained models that progressively establishes similarity awareness among tasks. Our design contains two innovative algorithmic components: incremental global pooling and instance-wise prompt masking. The former mitigates prompt association noise through gradual prompt introduction over time. The latter decomposes incoming task samples into those aligning with current prompts (in-distribution) and those requiring new prompts (out-of-distribution). Together, our design strategically leverages potential task overlaps while actively preventing negative mutual interference in the presence of per-task data scarcity. Experiments across varying data volumes and inter-task similarity show that our method enhances sample efficiency and is broadly applicable.

### 🤖 AI 总结

**一句话总结**：提出一种具备任务相似性感知的自适应MoE持续学习框架，在每任务数据稀缺且任务重叠未知的场景下提升知识迁移效率并减少负迁移。

**研究动机**：现实持续学习中常见“每个任务数据很少”且“任务可能任意重叠”的更一般设定，现有方法要么依赖充足数据、要么假设任务不重叠，导致迁移不足或出现负迁移干扰。

**核心方法**：在预训练模型之上构建渐进式的Mixture-of-Experts，并引入(1) incremental global pooling：随时间逐步引入/汇聚prompt以降低prompt-任务关联噪声；(2) instance-wise prompt masking：按样本级别区分与现有prompt匹配的in-distribution样本与需要新prompt的out-of-distribution样本，从而利用重叠同时避免互相干扰。

**主要结论**：在不同数据规模与任务相似度设置下，方法表现出更高的样本效率与更强的泛化适用性，并能在任务重叠情况下有效抑制负迁移。

**关键词**：持续学习, 数据高效学习, 任务重叠, 负迁移, 知识迁移, 混合专家模型（MoE）, 预训练模型适配, 相似性感知, 增量全局池化, 实例级提示掩码, 分布内/分布外检测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23436v1) | [下载PDF](https://arxiv.org/pdf/2603.23436v1.pdf)

---

## [30. Graph Energy Matching: Transport-Aligned Energy-Based Modeling for Graph Generation](https://arxiv.org/abs/2603.23398v1)

**作者**：Michal Balcerak, Suprosana Shit, Chinmay Prabhakar 等 7 位作者  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-03-24

### 📄 论文摘要

Energy-based models for discrete domains, such as graphs, explicitly capture relative likelihoods, naturally enabling composable probabilistic inference tasks like conditional generation or enforcing constraints at test-time. However, discrete energy-based models typically struggle with efficient and high-quality sampling, as off-support regions often contain spurious local minima, trapping samplers and causing training instabilities. This has historically resulted in a fidelity gap relative to discrete diffusion models. We introduce Graph Energy Matching (GEM), a generative framework for graphs that closes this fidelity gap. Motivated by the transport map optimization perspective of the Jordan-Kinderlehrer-Otto (JKO) scheme, GEM learns a permutation-invariant potential energy that simultaneously provides transport-aligned guidance from noise toward data and refines samples within regions of high data likelihood. Further, we introduce a sampling protocol that leverages an energy-based switch to seamlessly bridge: (i) rapid, gradient-guided transport toward high-probability regions to (ii) a mixing regime for exploration of the learned graph distribution. On molecular graph benchmarks, GEM matches or exceeds strong discrete diffusion baselines. Beyond sample quality, explicit modeling of relative likelihood enables targeted exploration at inference time, facilitating compositional generation, property-constrained sampling, and geodesic interpolation between graphs.

### 🤖 AI 总结

**一句话总结**：GEM提出一种面向图生成的传输对齐能量模型，通过学习置换不变的势能并结合“运输+混合”采样策略，弥补离散EBM在采样质量上相对扩散模型的差距。

**研究动机**：离散域（如图）的能量模型虽便于做条件生成与约束推断，但采样常被off-support的伪局部极小值困住，导致训练不稳与生成保真度落后于离散扩散模型。

**核心方法**：GEM受JKO方案的传输映射优化视角启发，学习一个置换不变的势能函数，既提供从噪声到数据的“传输式”梯度引导，又能在高似然区域内细化样本；同时设计能量开关采样协议，将快速梯度引导的运输阶段与用于探索分布的混合阶段无缝衔接。

**主要结论**：在分子图基准上，GEM生成质量可匹配或超过强离散扩散基线；并且由于显式建模相对似然，推断时可实现可组合生成、性质约束采样以及图之间的测地插值等能力。

**关键词**：图生成, 离散能量模型, 能量匹配, 传输对齐采样, 传输映射优化, 置换不变能量函数, 基于梯度的采样, 能量切换采样, 分子图生成, 属性约束采样, 图测地插值

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2603.23398v1) | [下载PDF](https://arxiv.org/pdf/2603.23398v1.pdf)

---

