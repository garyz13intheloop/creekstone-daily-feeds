# arXiv AI 论文日报 | 2026-03-01

> 共 15 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (5 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (1 篇)
- [cs.LG](#csLG) (7 篇)

---

## cs.AI

## [1. DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science](https://arxiv.org/abs/2602.24288v1)

**作者**：Fan Shu, Yite Wang, Ruofan Wu 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-02-27

### 📄 论文摘要

The fast-growing demands in using Large Language Models (LLMs) to tackle complex multi-step data science tasks create an emergent need for accurate benchmarking. There are two major gaps in existing benchmarks: (i) the lack of standardized, process-aware evaluation that captures instruction adherence and process fidelity, and (ii) the scarcity of accurately labeled training data. To bridge these gaps, we introduce DARE-bench, a benchmark designed for machine learning modeling and data science instruction following. Unlike many existing benchmarks that rely on human- or model-based judges, all tasks in DARE-bench have verifiable ground truth, ensuring objective and reproducible evaluation. To cover a broad range of tasks and support agentic tools, DARE-bench consists of 6,300 Kaggle-derived tasks and provides both large-scale training data and evaluation sets. Extensive evaluations show that even highly capable models such as gpt-o4-mini struggle to achieve good performance, especially in machine learning modeling tasks. Using DARE-bench training tasks for fine-tuning can substantially improve model performance. For example, supervised fine-tuning boosts Qwen3-32B's accuracy by 1.83x and reinforcement learning boosts Qwen3-4B's accuracy by more than 8x. These significant improvements verify the importance of DARE-bench both as an accurate evaluation benchmark and critical training data.

### 🤖 AI 总结

**一句话总结**：DARE-bench 提供一个具备可验证真值的大规模数据科学/建模指令遵循基准与训练集，用于客观评测并提升LLM在多步数据科学任务中的过程与指令保真度。

**研究动机**：现有基准难以标准化评估LLM在数据科学多步骤任务中的“过程正确性与指令遵循”，且缺少高质量、可规模化的标注训练数据。

**核心方法**：构建由 6,300 个 Kaggle 衍生任务组成的 DARE-bench，所有任务都有可核验的 ground truth，从而避免主观的人类/模型裁判并支持可复现实验；同时提供训练集与评测集以覆盖建模与数据科学指令跟随场景。

**主要结论**：实验显示即便是强模型也在建模类任务上表现吃力；用 DARE-bench 进行微调能显著提升准确率（如 SFT 使 Qwen3-32B 提升 1.83x，RL 使 Qwen3-4B 提升 8x+），证明其既是有效评测基准也是关键训练数据来源。

**关键词**：数据科学基准, 指令遵循, 过程一致性, 过程感知评测, 可验证真值, 可复现评估, 多步任务, 模型微调数据, 监督微调, 强化学习微调

**评分**：40

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24288v1) | [下载PDF](https://arxiv.org/pdf/2602.24288v1.pdf)

---

## [2. A Minimal Agent for Automated Theorem Proving](https://arxiv.org/abs/2602.24273v1)

**作者**：Borja Requena Pozo, Austin Letson, Krystian Nowakowski 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-02-27

### 📄 论文摘要

We propose a minimal agentic baseline that enables systematic comparison across different AI-based theorem prover architectures. This design implements the core features shared among state-of-the-art systems: iterative proof refinement, library search and context management. We evaluate our baseline using qualitatively different benchmarks and compare various popular models and design choices, and demonstrate competitive performance compared to state-of-the-art approaches, while using a significantly simpler architecture. Our results demonstrate consistent advantages of an iterative approach over multiple single-shot generations, especially in terms of sample efficiency and cost effectiveness. The implementation is released open-source as a candidate reference for future research and as an accessible prover for the community.

### 🤖 AI 总结

**一句话总结**：提出一个用于自动定理证明的“最小化智能体”基线，用更简单的架构实现与SOTA相近的效果，并证明迭代式证明生成更高效。

**研究动机**：现有AI定理证明系统架构复杂且各自定制，难以在同一标准下公平比较不同模型与设计选择。作者希望给出一个覆盖主流系统共同关键能力的简洁参考实现，便于系统化评测与复现。

**核心方法**：设计最小智能体基线，包含迭代式证明精炼、库检索与上下文管理等核心组件，并在多种性质不同的基准上对比多种流行模型与设计选项。通过实验比较迭代式流程与多次single-shot生成在样本效率与成本上的差异，并开源实现。

**主要结论**：该最小化架构在多类基准上表现具有竞争力，接近或对标部分SOTA方法，同时显著简化系统复杂度。实验显示迭代式证明策略相较多次单次生成更具一致优势，尤其在样本效率与成本效益方面。

**关键词**：自动定理证明, 智能体基线, 最小化架构, 迭代式证明精炼, 证明搜索, 定理库检索, 上下文管理, 单次生成对比, 基准评测, 样本效率

**评分**：51

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24273v1) | [下载PDF](https://arxiv.org/pdf/2602.24273v1.pdf)

---

## cs.CL

## [3. Do LLMs Benefit From Their Own Words?](https://arxiv.org/abs/2602.24287v1)

**作者**：Jenny Y. Huang, Leshem Choshen, Ramon Astudillo 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-02-27

### 📄 论文摘要

Multi-turn interactions with large language models typically retain the assistant's own past responses in the conversation history. In this work, we revisit this design choice by asking whether large language models benefit from conditioning on their own prior responses. Using in-the-wild, multi-turn conversations, we compare standard (full-context) prompting with a user-turn-only prompting approach that omits all previous assistant responses, across three open reasoning models and one state-of-the-art model. To our surprise, we find that removing prior assistant responses does not affect response quality on a large fraction of turns. Omitting assistant-side history can reduce cumulative context lengths by up to 10x. To explain this result, we find that multi-turn conversations consist of a substantial proportion (36.4%) of self-contained prompts, and that many follow-up prompts provide sufficient instruction to be answered using only the current user turn and prior user turns. When analyzing cases where user-turn-only prompting substantially outperforms full context, we identify instances of context pollution, in which models over-condition on their previous responses, introducing errors, hallucinations, or stylistic artifacts that propagate across turns. Motivated by these findings, we design a context-filtering approach that selectively omits assistant-side context. Our findings suggest that selectively omitting assistant history can improve response quality while reducing memory consumption.

### 🤖 AI 总结

**一句话总结**：LLM在多轮对话中往往不需要依赖自己之前的回复；选择性移除助手历史既能显著压缩上下文长度，又可能提升回答质量。

**研究动机**：多轮对话通常保留助手先前输出，但这会带来上下文膨胀与成本上升；作者质疑“保留助手历史”是否真的有助于后续质量。

**核心方法**：在真实多轮对话数据上，对比“全上下文提示”与“仅保留用户轮次（删除所有历史助手回复）”在多个推理模型/先进模型上的表现，并分析自包含提示比例与“上下文污染”案例；进一步提出选择性过滤助手侧上下文的策略。

**主要结论**：大量轮次中删除助手历史对质量几乎无影响，且可将累计上下文长度最多降低约10倍；当出现显著差异时，常见原因是模型过度依赖自身旧输出导致错误/幻觉/风格伪影传播，选择性省略助手历史可同时降内存并改善质量。

**关键词**：多轮对话, 助手历史省略, 上下文过滤, 上下文污染, 过度条件化, 幻觉传播, 上下文长度压缩, 提示自包含性, 响应质量评测, 推理模型对比

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24287v1) | [下载PDF](https://arxiv.org/pdf/2602.24287v1.pdf)

---

## cs.CV

## [4. UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images](https://arxiv.org/abs/2602.24290v1)

**作者**：Junhwa Hur, Charles Herrmann, Songyou Peng 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-27

### 📄 论文摘要

Dense 4D reconstruction from unposed images remains a critical challenge, with current methods relying on slow test-time optimization or fragmented, task-specific feedforward models. We introduce UFO-4D, a unified feedforward framework to reconstruct a dense, explicit 4D representation from just a pair of unposed images. UFO-4D directly estimates dynamic 3D Gaussian Splats, enabling the joint and consistent estimation of 3D geometry, 3D motion, and camera pose in a feedforward manner. Our core insight is that differentiably rendering multiple signals from a single Dynamic 3D Gaussian representation offers major training advantages. This approach enables a self-supervised image synthesis loss while tightly coupling appearance, depth, and motion. Since all modalities share the same geometric primitives, supervising one inherently regularizes and improves the others. This synergy overcomes data scarcity, allowing UFO-4D to outperform prior work by up to 3 times in joint geometry, motion, and camera pose estimation. Our representation also enables high-fidelity 4D interpolation across novel views and time. Please visit our project page for visual results: https://ufo-4d.github.io/

### 🤖 AI 总结

**一句话总结**：UFO-4D提出一个统一的前馈框架，仅用两张无位姿图像即可联合重建显式稠密4D表示（几何+运动+相机位姿），并实现高质量跨视角与时间的插值渲染。

**研究动机**：现有从无位姿图像进行稠密4D重建的方法往往依赖耗时的测试时优化，或将几何/运动/位姿拆分为彼此割裂的前馈模型，导致效率低、泛化与一致性差。

**核心方法**：方法直接前馈预测动态3D Gaussian Splats，并通过对同一动态高斯表示可微渲染多种信号（外观/深度/运动等）来训练；利用自监督图像合成损失把多模态紧耦合，使共享几何基元带来互相正则与增益，从而同时估计3D几何、3D运动和相机位姿。

**主要结论**：多信号可微渲染与共享表示的协同监督缓解了数据稀缺并显著提升联合估计性能，报告称在几何/运动/位姿上相对先前方法最高可达3倍提升，同时支持高保真新视角与时间维度的4D插值。

**关键词**：稠密4D重建, 无姿态图像, 前馈重建, 动态3D高斯溅射, 显式4D表示, 可微渲染, 自监督图像合成, 相机位姿估计, 三维运动估计, 多模态联合学习, 新视角时间插值

**评分**：29

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24290v1) | [下载PDF](https://arxiv.org/pdf/2602.24290v1.pdf)

---

## [5. Mode Seeking meets Mean Seeking for Fast Long Video Generation](https://arxiv.org/abs/2602.24289v1)

**作者**：Shengqu Cai, Weili Nie, Chao Liu 等 11 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-27

### 📄 论文摘要

Scaling video generation from seconds to minutes faces a critical bottleneck: while short-video data is abundant and high-fidelity, coherent long-form data is scarce and limited to narrow domains. To address this, we propose a training paradigm where Mode Seeking meets Mean Seeking, decoupling local fidelity from long-term coherence based on a unified representation via a Decoupled Diffusion Transformer. Our approach utilizes a global Flow Matching head trained via supervised learning on long videos to capture narrative structure, while simultaneously employing a local Distribution Matching head that aligns sliding windows to a frozen short-video teacher via a mode-seeking reverse-KL divergence. This strategy enables the synthesis of minute-scale videos that learns long-range coherence and motions from limited long videos via supervised flow matching, while inheriting local realism by aligning every sliding-window segment of the student to a frozen short-video teacher, resulting in a few-step fast long video generator. Evaluations show that our method effectively closes the fidelity-horizon gap by jointly improving local sharpness, motion and long-range consistency. Project website: https://primecai.github.io/mmm/.

### 🤖 AI 总结

**一句话总结**：提出一种“全局叙事一致性 + 局部画质/运动逼真度”解耦的训练范式，在少量长视频数据下实现分钟级、少步数的高质量长视频生成。

**研究动机**：长视频生成受限于高质量长视频数据稀缺且领域窄，而短视频数据丰富但难以提供长程一致性；需要同时弥补“局部保真”与“长程连贯”之间的鸿沟。

**核心方法**：使用统一的Decoupled Diffusion Transformer并分两头训练：全局Flow Matching头在少量长视频上做监督学习以建模叙事/长程结构；局部Distribution Matching头将滑窗片段用反向KL（mode-seeking）对齐到冻结的短视频教师，从而继承局部清晰度与运动细节并支持few-step生成。

**主要结论**：该方法在评测中同时提升局部清晰度、运动质量与长程一致性，有效缩小“保真度-时长”差距，并能在有限长视频监督下生成分钟级连贯视频。

**关键词**：长视频生成, 分钟级视频生成, 长程时序一致性, 叙事结构建模, 解耦表示学习, 反向KL散度, 教师-学生蒸馏, 滑动窗口训练, 少步采样推理

**评分**：26

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24289v1) | [下载PDF](https://arxiv.org/pdf/2602.24289v1.pdf)

---

## [6. Hierarchical Action Learning for Weakly-Supervised Action Segmentation](https://arxiv.org/abs/2602.24275v1)

**作者**：Junxian Huang, Ruichu Cai, Hao Zhu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-27

### 📄 论文摘要

Humans perceive actions through key transitions that structure actions across multiple abstraction levels, whereas machines, relying on visual features, tend to over-segment. This highlights the difficulty of enabling hierarchical reasoning in video understanding. Interestingly, we observe that lower-level visual and high-level action latent variables evolve at different rates, with low-level visual variables changing rapidly, while high-level action variables evolve more slowly, making them easier to identify. Building on this insight, we propose the Hierarchical Action Learning (\textbf{HAL}) model for weakly-supervised action segmentation. Our approach introduces a hierarchical causal data generation process, where high-level latent action governs the dynamics of low-level visual features. To model these varying timescales effectively, we introduce deterministic processes to align these latent variables over time. The \textbf{HAL} model employs a hierarchical pyramid transformer to capture both visual features and latent variables, and a sparse transition constraint is applied to enforce the slower dynamics of high-level action variables. This mechanism enhances the identification of these latent variables over time. Under mild assumptions, we prove that these latent action variables are strictly identifiable. Experimental results on several benchmarks show that the \textbf{HAL} model significantly outperforms existing methods for weakly-supervised action segmentation, confirming its practical effectiveness in real-world applications.

### 🤖 AI 总结

**一句话总结**：提出HAL层级动作学习模型，通过建模“高层动作变量慢变、低层视觉特征快变”的层级因果过程，在弱监督动作分割上显著优于现有方法。

**研究动机**：人类通过关键转折以多层抽象理解动作，但现有方法多依赖局部视觉特征而易过分割；作者观察到高层动作潜变量变化更慢、更易识别，值得显式建模以提升弱监督分割。

**核心方法**：构建层级因果生成过程：高层潜在动作变量支配低层视觉动态，并用确定性时间对齐机制处理不同时尺度；采用层级金字塔Transformer同时表示视觉与潜变量，并施加稀疏转移约束以强制高层动作的慢变与少切换，从而增强潜变量识别并给出可辨识性证明。

**主要结论**：在温和假设下证明高层潜在动作变量严格可辨识，且在多个基准上的实验结果显示HAL在弱监督动作分割任务中显著超过现有方法，验证了其实用性。

**关键词**：弱监督动作分割, 层级动作学习, 层级因果生成模型, 多尺度时序建模, 潜变量建模, 时间尺度分离, 确定性对齐, 稀疏转移约束, 潜变量可辨识性

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24275v1) | [下载PDF](https://arxiv.org/pdf/2602.24275v1.pdf)

---

## [7. Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models](https://arxiv.org/abs/2602.24264v1)

**作者**：Arnas Uselis, Andrea Dittadi, Seong Joon Oh  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-02-27

### 📄 论文摘要

Compositional generalization, the ability to recognize familiar parts in novel contexts, is a defining property of intelligent systems. Although modern models are trained on massive datasets, they still cover only a tiny fraction of the combinatorial space of possible inputs, raising the question of what structure representations must have to support generalization to unseen combinations. We formalize three desiderata for compositional generalization under standard training (divisibility, transferability, stability) and show they impose necessary geometric constraints: representations must decompose linearly into per-concept components, and these components must be orthogonal across concepts. This provides theoretical grounding for the Linear Representation Hypothesis: the linear structure widely observed in neural representations is a necessary consequence of compositional generalization. We further derive dimension bounds linking the number of composable concepts to the embedding geometry. Empirically, we evaluate these predictions across modern vision models (CLIP, SigLIP, DINO) and find that representations exhibit partial linear factorization with low-rank, near-orthogonal per-concept factors, and that the degree of this structure correlates with compositional generalization on unseen combinations. As models continue to scale, these conditions predict the representational geometry they may converge to. Code is available at https://github.com/oshapio/necessary-compositionality.

### 🤖 AI 总结

**一句话总结**：论文证明要在视觉嵌入模型中实现组合泛化，表征必须可线性分解为按概念的成分且不同概念成分近似正交，并在CLIP/SigLIP/DINO中得到部分验证。

**研究动机**：现实输入的组合空间远大于训练数据覆盖范围，模型要识别“熟悉部件在新组合中出现”需要理解表征应具备的必要结构与几何约束。

**核心方法**：提出组合泛化在标准训练下的三个性质要求（可分性、可迁移性、稳定性），从理论上推导其对嵌入几何的必要条件（线性分解与概念间正交）及维度下界，并在多种现代视觉模型上测量概念因子的低秩与近正交性并关联到未见组合泛化表现。

**主要结论**：组合泛化在理论上强制嵌入呈现“线性因子化+概念正交”的几何结构，并给出可组合概念数与维度的约束；实证结果显示现有模型仅部分满足（低秩、近正交），且满足程度与未见组合的泛化能力正相关。

**关键词**：组合泛化, 视觉嵌入模型, 表示几何约束, 线性分解表示, 正交表示, 概念因子分解, 低秩因子, 线性表示假设, 维度下界, 未见组合泛化评测, 概念可组合性

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24264v1) | [下载PDF](https://arxiv.org/pdf/2602.24264v1.pdf)

---

## [8. Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution](https://arxiv.org/abs/2602.24240v1)

**作者**：Chengyan Deng, Zhangquan Chen, Li Yu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-02-27

### 📄 论文摘要

Diffusion-based Real-World Image Super-Resolution (Real-ISR) achieves impressive perceptual quality but suffers from high computational costs due to iterative sampling. While recent distillation approaches leveraging large-scale Text-to-Image (T2I) priors have enabled one-step generation, they are typically hindered by prohibitive parameter counts and the inherent capability bounds imposed by teacher models. As a lightweight alternative, Consistency Models offer efficient inference but struggle with two critical limitations: the accumulation of consistency drift inherent to transitive training, and a phenomenon we term "Geometric Decoupling" - where the generative trajectory achieves pixel-wise alignment yet fails to preserve structural coherence. To address these challenges, we propose GTASR (Geometric Trajectory Alignment Super-Resolution), a simple yet effective consistency training paradigm for Real-ISR. Specifically, we introduce a Trajectory Alignment (TA) strategy to rectify the tangent vector field via full-path projection, and a Dual-Reference Structural Rectification (DRSR) mechanism to enforce strict structural constraints. Extensive experiments verify that GTASR delivers superior performance over representative baselines while maintaining minimal latency. The code and model will be released at https://github.com/Blazedengcy/GTASR.

### 🤖 AI 总结

**一句话总结**：GTASR通过联合几何与轨迹一致性学习，实现真实场景超分辨率的一步生成，在保持极低推理延迟的同时提升结构与感知质量。

**研究动机**：扩散式Real-ISR虽然效果好但采样迭代导致计算开销高；现有一步蒸馏依赖大模型先验且参数庞大，而一致性模型又易出现训练传递导致的漂移与“几何解耦”（像素对齐但结构失真）。

**核心方法**：提出GTASR一致性训练范式：用Trajectory Alignment（TA）通过全路径投影校正切向量场以抑制一致性漂移；再用Dual-Reference Structural Rectification（DRSR）引入双参考结构约束，强制生成轨迹保持结构一致性。

**主要结论**：大量实验表明GTASR在代表性基线之上取得更优的真实图像超分表现，并维持一步推理带来的最小延迟与较轻量的模型开销。

**关键词**：真实图像超分辨率, Diffusion, 一步采样, 一致性模型, 蒸馏学习, 文本到图像先验, 轨迹对齐, 全路径投影, 切向量场校正, 结构一致性约束, 几何解耦, 低延迟推理

**评分**：35

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24240v1) | [下载PDF](https://arxiv.org/pdf/2602.24240v1.pdf)

---

## cs.LG

## [9. CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation](https://arxiv.org/abs/2602.24286v1)

**作者**：Weinan Dai, Hanlin Wu, Qiying Yu 等 16 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-27

### 📄 论文摘要

GPU kernel optimization is fundamental to modern deep learning but remains a highly specialized task requiring deep hardware expertise. Despite strong performance in general programming, large language models (LLMs) remain uncompetitive with compiler-based systems such as torch.compile for CUDA kernel generation. Existing CUDA code generation approaches either rely on training-free refinement or fine-tune models within fixed multi-turn execution-feedback loops, but both paradigms fail to fundamentally improve the model's intrinsic CUDA optimization ability, resulting in limited performance gains. We present CUDA Agent, a large-scale agentic reinforcement learning system that develops CUDA kernel expertise through three components: a scalable data synthesis pipeline, a skill-augmented CUDA development environment with automated verification and profiling to provide reliable reward signals, and reinforcement learning algorithmic techniques enabling stable training. CUDA Agent achieves state-of-the-art results on KernelBench, delivering 100\%, 100\%, and 92\% faster rate over torch.compile on KernelBench Level-1, Level-2, and Level-3 splits, outperforming the strongest proprietary models such as Claude Opus 4.5 and Gemini 3 Pro by about 40\% on the hardest Level-3 setting.

### 🤖 AI 总结

**一句话总结**：CUDA Agent 通过大规模“代理式”强化学习与可验证/可剖析的开发环境训练，使LLM具备更强的CUDA内核优化能力，并在KernelBench上显著超越torch.compile与多款强力闭源模型。

**研究动机**：CUDA内核优化对深度学习性能至关重要但高度依赖硬件专家经验，而现有LLM生成CUDA内核相比编译器系统（如torch.compile）性能落后。现有训练-free迭代或固定多轮反馈微调难以提升模型“内生”的CUDA优化能力，收益有限。

**核心方法**：提出CUDA Agent系统：用可扩展的数据合成管线生成训练任务，在带技能增强的CUDA开发环境中进行自动验证与性能profiling以提供可靠奖励信号，并配合稳定的强化学习算法技术进行大规模训练。通过“生成-运行-验证/测量-奖励-更新”的闭环，使模型学习高性能CUDA优化策略。

**主要结论**：CUDA Agent在KernelBench Level-1/2/3上相对torch.compile分别实现约100%/100%/92%的更高“更快率”，并在最难的Level-3上比Claude Opus 4.5、Gemini 3 Pro等强闭源模型快约40%，达到新的SOTA。结果表明，代理式RL+可靠奖励信号能实质提升LLM的CUDA内核优化能力，而非仅依赖外部迭代修补。

**关键词**：CUDA 内核生成, GPU 内核优化, 代码生成模型训练, 可扩展数据合成, 执行反馈奖励, 自动化验证, 技能增强开发环境, CUDA

**评分**：63

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24286v1) | [下载PDF](https://arxiv.org/pdf/2602.24286v1.pdf)

---

## [10. Memory Caching: RNNs with Growing Memory](https://arxiv.org/abs/2602.24281v1)

**作者**：Ali Behrouz, Zeman Li, Yuan Deng 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-27

### 📄 论文摘要

Transformers have been established as the de-facto backbones for most recent advances in sequence modeling, mainly due to their growing memory capacity that scales with the context length. While plausible for retrieval tasks, it causes quadratic complexity and so has motivated recent studies to explore viable subquadratic recurrent alternatives. Despite showing promising preliminary results in diverse domains, such recurrent architectures underperform Transformers in recall-intensive tasks, often attributed to their fixed-size memory. In this paper, we introduce Memory Caching (MC), a simple yet effective technique that enhances recurrent models by caching checkpoints of their memory states (a.k.a. hidden states). Memory Caching allows the effective memory capacity of RNNs to grow with sequence length, offering a flexible trade-off that interpolates between the fixed memory (i.e., $O(L)$ complexity) of RNNs and the growing memory (i.e., $O(L^2)$ complexity) of Transformers. We propose four variants of MC, including gated aggregation and sparse selective mechanisms, and discuss their implications on both linear and deep memory modules. Our experimental results on language modeling, and long-context understanding tasks show that MC enhances the performance of recurrent models, supporting its effectiveness. The results of in-context recall tasks indicate that while Transformers achieve the best accuracy, our MC variants show competitive performance, close the gap with Transformers, and performs better than state-of-the-art recurrent models.

### 🤖 AI 总结

**一句话总结**：提出Memory Caching（MC）通过缓存RNN的历史隐藏状态让“有效记忆容量”随序列长度增长，从而在性能上缩小与Transformer在长上下文/召回任务的差距。

**研究动机**：现有RNN类长序列模型常因固定大小记忆而在召回密集任务落后于Transformer；但Transformer的随上下文增长记忆带来二次复杂度，促使探索兼具更强记忆与更低复杂度的替代方案。

**核心方法**：MC在RNN运行过程中缓存若干“记忆检查点”（隐藏状态），并在后续通过门控聚合或稀疏选择等机制从缓存中读取/融合信息，使计算复杂度在传统RNN的O(L)与Transformer的O(L^2)之间可调。

**主要结论**：在语言建模与长上下文理解实验中，MC显著增强了循环模型表现；在in-context召回任务上虽仍不及Transformer最优，但多种MC变体能获得接近的准确率，并优于当前SOTA循环架构。

**关键词**：记忆缓存, 隐藏状态缓存, 增长式记忆, 长上下文建模, 次二次复杂度, 召回密集任务, 上下文内召回, 门控聚合, 稀疏选择机制, 语言模型评测

**评分**：25

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24281v1) | [下载PDF](https://arxiv.org/pdf/2602.24281v1.pdf)

---

## [11. Who Guards the Guardians? The Challenges of Evaluating Identifiability of Learned Representations](https://arxiv.org/abs/2602.24278v1)

**作者**：Shruti Joshi, Théo Saulus, Wieland Brendel 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-27

### 📄 论文摘要

Identifiability in representation learning is commonly evaluated using standard metrics (e.g., MCC, DCI, R^2) on synthetic benchmarks with known ground-truth factors. These metrics are assumed to reflect recovery up to the equivalence class guaranteed by identifiability theory. We show that this assumption holds only under specific structural conditions: each metric implicitly encodes assumptions about both the data-generating process (DGP) and the encoder. When these assumptions are violated, metrics become misspecified and can produce systematic false positives and false negatives. Such failures occur both within classical identifiability regimes and in post-hoc settings where identifiability is most needed. We introduce a taxonomy separating DGP assumptions from encoder geometry, use it to characterise the validity domains of existing metrics, and release an evaluation suite for reproducible stress testing and comparison.

### 🤖 AI 总结

**一句话总结**：论文探讨了表示学习中可识别性的评估挑战，指出标准指标在假设条件被违反时可能产生误导性结果。

**研究动机**：研究表明，当前用于评估可识别性的标准指标在特定结构条件下才有效，而在假设被违反时可能导致错误的评估结果。

**核心方法**：提出了一种分类法，将数据生成过程假设与编码器几何特性分开，从而表征现有指标的有效性范围，并发布了一个评估套件用于可重复的压力测试和比较。

**主要结论**：通过分析指标的有效性和假设，本文提出了一个新的框架，以改善对学习表示的可识别性评估，强调了标准评估方法的局限性。

**关键词**：表征学习可辨识性, 解耦表征评测, 可辨识性理论, 合成基准, 真值因子, 评测指标失配, 数据生成过程假设, 编码器几何, 系统性假阳性, 系统性假阴性, 评测套件, 压力测试评测

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24278v1) | [下载PDF](https://arxiv.org/pdf/2602.24278v1.pdf)

---

## [12. Efficient Discovery of Approximate Causal Abstractions via Neural Mechanism Sparsification](https://arxiv.org/abs/2602.24266v1)

**作者**：Amir Asiaee  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-02-27

### 📄 论文摘要

Neural networks are hypothesized to implement interpretable causal mechanisms, yet verifying this requires finding a causal abstraction -- a simpler, high-level Structural Causal Model (SCM) faithful to the network under interventions. Discovering such abstractions is hard: it typically demands brute-force interchange interventions or retraining. We reframe the problem by viewing structured pruning as a search over approximate abstractions. Treating a trained network as a deterministic SCM, we derive an Interventional Risk objective whose second-order expansion yields closed-form criteria for replacing units with constants or folding them into neighbors. Under uniform curvature, our score reduces to activation variance, recovering variance-based pruning as a special case while clarifying when it fails. The resulting procedure efficiently extracts sparse, intervention-faithful abstractions from pretrained networks, which we validate via interchange interventions.

### 🤖 AI 总结

**一句话总结**：将结构化剪枝视为对神经网络“因果抽象”的高效搜索，通过可闭式计算的干预风险评分提取稀疏且在干预下近似保真的高层机制。

**研究动机**：验证神经网络是否实现可解释的因果机制需要找到在干预下与网络一致的高层SCM，但现有方法往往依赖昂贵的互换干预枚举或反复重训练，成本过高。

**核心方法**：把已训练网络视为确定性SCM，提出Interventional Risk目标并做二阶展开，得到替换神经元为常数或将其折叠进相邻单元的闭式评分；在“曲率均匀”假设下该评分退化为激活方差，从而统一并解释方差剪枝的适用与失效条件。

**主要结论**：该方法能从预训练网络中高效抽取稀疏机制作为近似因果抽象，并通过互换干预实验验证其对干预行为的（近似）保真性，同时澄清了仅用方差剪枝何时可靠、何时会失败。

**关键词**：因果抽象, 结构因果模型（SCM）, 干预一致性, 互换干预, 结构化剪枝, 机制稀疏化, 神经机制可解释性, 干预风险目标, 二阶近似, 激活方差剪枝, 预训练网络压缩

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24266v1) | [下载PDF](https://arxiv.org/pdf/2602.24266v1.pdf)

---

## [13. Coverage-Aware Web Crawling for Domain-Specific Supplier Discovery via a Web--Knowledge--Web Pipeline](https://arxiv.org/abs/2602.24262v1)

**作者**：Yijiashun Qi, Yijiazhen Qi, Tanmay Wagh  
**分类**：cs.LG  
**发布时间**：2026-02-27

### 📄 论文摘要

Identifying the full landscape of small and medium-sized enterprises (SMEs) in specialized industry sectors is critical for supply-chain resilience, yet existing business databases suffer from substantial coverage gaps -- particularly for sub-tier suppliers and firms in emerging niche markets. We propose a \textbf{Web--Knowledge--Web (W$\to$K$\to$W)} pipeline that iteratively (1)~crawls domain-specific web sources to discover candidate supplier entities, (2)~extracts and consolidates structured knowledge into a heterogeneous knowledge graph, and (3)~uses the knowledge graph's topology and coverage signals to guide subsequent crawling toward under-represented regions of the supplier space. To quantify discovery completeness, we introduce a \textbf{coverage estimation framework} inspired by ecological species-richness estimators (Chao1, ACE) adapted for web-entity populations. Experiments on the semiconductor equipment manufacturing sector (NAICS 333242) demonstrate that the W$\to$K$\to$W pipeline achieves the highest precision (0.138) and F1 (0.118) among all methods using the same 213-page crawl budget, building a knowledge graph of 765 entities and 586 relations while reaching peak recall by iteration~3 with only 112 pages.

### 🤖 AI 总结

**一句话总结**：提出一个“Web→Knowledge→Web”迭代管线，用知识图谱的覆盖信号反向指导爬虫，在固定爬取预算下更完整、精准地发现细分领域中小供应商。

**研究动机**：现有商业数据库对专精行业的中小企业（尤其是次级供应商与新兴利基市场）覆盖不足，影响供应链韧性评估与供应商全景识别。需要一种能量化“发现是否接近完整”并主动补齐缺口的自动化发现方法。

**核心方法**：构建W→K→W闭环：先爬取领域网页发现候选企业，再抽取/融合为异构知识图谱，随后利用图谱拓扑与覆盖信号引导下一轮爬取朝向欠覆盖区域。并提出借鉴生态“物种丰富度”估计（Chao1、ACE）的覆盖估计框架，用于估算供应商总体规模与发现完整度。

**主要结论**：在半导体设备制造（NAICS 333242）实验中，该方法在相同213页预算下取得最高precision=0.138与F1=0.118，构建765实体、586关系的知识图谱；且在第3轮迭代、仅112页时即达到峰值召回，显示覆盖感知引导能更高效补齐长尾供应商。

**关键词**：领域网页爬虫, 中小企业识别, 供应链韧性, Web-知识-Web 管道, 知识图谱构建, 异构知识图谱, 知识图谱引导爬取, 覆盖率估计

**评分**：44

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24262v1) | [下载PDF](https://arxiv.org/pdf/2602.24262v1.pdf)

---

## [14. Histopathology Image Normalization via Latent Manifold Compaction](https://arxiv.org/abs/2602.24251v1)

**作者**：Xiaolong Zhang, Jianwei Zhang, Selim Sevim 等 6 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-02-27

### 📄 论文摘要

Batch effects arising from technical variations in histopathology staining protocols, scanners, and acquisition pipelines pose a persistent challenge for computational pathology, hindering cross-batch generalization and limiting reliable deployment of models across clinical sites. In this work, we introduce Latent Manifold Compaction (LMC), an unsupervised representation learning framework that performs image harmonization by learning batch-invariant embeddings from a single source dataset through explicit compaction of stain-induced latent manifolds. This allows LMC to generalize to target domain data unseen during training. Evaluated on three challenging public and in-house benchmarks, LMC substantially reduces batch-induced separations across multiple datasets and consistently outperforms state-of-the-art normalization methods in downstream cross-batch classification and detection tasks, enabling superior generalization.

### 🤖 AI 总结

**一句话总结**：提出一种无监督的潜在流形压缩（LMC）方法，通过学习批次不变的表示实现病理图像染色归一化，并提升跨批次/跨机构泛化。

**研究动机**：病理图像因染色流程、扫描仪与采集管线差异产生显著批次效应，导致模型跨批次性能下降、部署不可靠。现有归一化方法往往难以在未见过的目标域上稳定泛化。

**核心方法**：LMC在单一源数据上进行无监督表示学习，显式“压缩”由染色差异诱导的潜在空间流形分离，从而得到对批次/染色变化不敏感的嵌入并用于图像协调。该机制使其无需目标域参与训练也能迁移到未见目标域数据。

**主要结论**：在多个公开与自建基准上，LMC显著降低不同批次在特征空间的分离度，并在跨批次分类与检测等下游任务中持续优于现有SOTA归一化方法，带来更强的跨域泛化能力。

**关键词**：计算病理, 组织病理图像归一化, 染色归一化, 批次效应, 图像域适配, 域泛化, 无监督表征学习, 批次不变嵌入, 潜在流形压缩（LMC）, 跨批次分类检测

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24251v1) | [下载PDF](https://arxiv.org/pdf/2602.24251v1.pdf)

---

## [15. Chunk-wise Attention Transducers for Fast and Accurate Streaming Speech-to-Text](https://arxiv.org/abs/2602.24245v1)

**作者**：Hainan Xu, Vladimir Bataev, Travis M. Bartley 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-02-27

### 📄 论文摘要

We propose Chunk-wise Attention Transducer (CHAT), a novel extension to RNN-T models that processes audio in fixed-size chunks while employing cross-attention within each chunk. This hybrid approach maintains RNN-T's streaming capability while introducing controlled flexibility for local alignment modeling. CHAT significantly reduces the temporal dimension that RNN-T must handle, yielding substantial efficiency improvements: up to 46.2% reduction in peak training memory, up to 1.36X faster training, and up to 1.69X faster inference. Alongside these efficiency gains, CHAT achieves consistent accuracy improvements over RNN-T across multiple languages and tasks -- up to 6.3% relative WER reduction for speech recognition and up to 18.0% BLEU improvement for speech translation. The method proves particularly effective for speech translation, where RNN-T's strict monotonic alignment hurts performance. Our results demonstrate that the CHAT model offers a practical solution for deploying more capable streaming speech models without sacrificing real-time constraints.

### 🤖 AI 总结

**一句话总结**：CHAT在RNN-T的流式框架中引入按固定chunk处理与chunk内交叉注意力，在保持实时性的同时显著提升训练/推理效率并提高多语种识别与翻译精度。

**研究动机**：传统RNN-T严格单调对齐与长时间步建模带来效率开销，并在语音翻译等需要更灵活局部对齐的任务上限制性能；需要一种不牺牲流式约束却能增强对齐建模的方案。

**核心方法**：将输入音频切分为固定大小chunk，模型以chunk为单位推进以减少时间维度；在每个chunk内使用cross-attention增强局部对齐与上下文建模，同时整体仍沿用RNN-T式的流式解码机制。

**主要结论**：CHAT在多语言/多任务上相较RNN-T获得稳定精度提升（最高相对WER降6.3%、BLEU升18.0%），并带来明显效率收益（峰值训练显存降至46.2%、训练最高1.36×、推理最高1.69×加速），尤其改善语音翻译场景。

**关键词**：流式语音识别, 流式语音翻译, 注意力转导器, 分块注意力, 跨注意力, 局部对齐建模, 单调对齐约束, 低延迟推理, 训练内存优化

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2602.24245v1) | [下载PDF](https://arxiv.org/pdf/2602.24245v1.pdf)

---

