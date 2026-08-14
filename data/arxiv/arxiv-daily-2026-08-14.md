# arXiv AI 论文日报 | 2026-08-14

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.CL](#csCL) (4 篇)

---

## cs.AI

## [1. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](https://arxiv.org/abs/2608.13558v1)

**作者**：Bobo Li, Hao Fei, Tianjie Ju 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-13

### 📄 论文摘要

Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

### 🤖 AI 总结

**一句话总结**：Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workf...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, OmniScientist, Omni-Modal, Omni-Discipline, Scientist, Recent, advances, foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13558v1) | [下载PDF](https://arxiv.org/pdf/2608.13558v1.pdf)

---

## [2. QuoteBench: How Matched Scores Can Hide Command-Path Failures](https://arxiv.org/abs/2608.13547v1)

**作者**：Shangao Li, Yao Zhang, Volker Tresp 等 4 位作者  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-08-13

### 📄 论文摘要

LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation. QuoteBench measures this boundary with exact final-state validation on 56 one-shot tasks from 14 incident-derived families, crossing the generation contract with the execution transport around one deliberately unescaped added parser. Escaping at the interpolation point reproduces each replayed reply's raw-path outcome, so any recovery under a disclosed boundary must come from the model changing its generation. Across eight same-window configurations, replaying the same reply through the added parser lowers success by 55.4 to 73.2 percentage points; disclosure recovers 30.4 to 60.7 points for six configurations, and zero or slightly negative for the other two. Raw generation is nearly saturated at the frontier; boundary adaptation is what still separates models. GPT-5.6-sol's matched gap of -3.6 points hides -64.3 points of damage and +60.7 points of compensation. The deployment configuration reorders models: one reversal among 26 comparable pairs is unambiguous and four more sit on single-task margins. Evaluations of command-issuing agents should report the model configuration, generation contract, execution path, operating point, and final-state validator rather than treat a matched score as an intrinsic model property.

### 🤖 AI 总结

**一句话总结**：LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QuoteBench, How, Matched, Scores, Can, Hide, Command-Path, Failures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13547v1) | [下载PDF](https://arxiv.org/pdf/2608.13547v1.pdf)

---

## [3. MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](https://arxiv.org/abs/2608.13476v1)

**作者**：Saisha Shetty, Satvik Tripathi, Austin Lin 等 9 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-13

### 📄 论文摘要

We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. The framework supports both API-based and local CPU-compatible deployments and is entirely configurable via YAML, without code modifications. MARC is designed to be model-agnostic, interpretable, and accessible to clinical domain experts without programming expertise. The full framework is available at https://github.com/Penn-RAIL/MARC-v1.

### 🤖 AI 总结

**一句话总结**：We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coor...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：v1, An, Multi-Agent, MARC, Open-Source, Framework, Clinical, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13476v1) | [下载PDF](https://arxiv.org/pdf/2608.13476v1.pdf)

---

## [4. A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](https://arxiv.org/abs/2608.13456v1)

**作者**：Avinash Kori, Fabrizio Russo  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entity interactions, and entity-to-environment interactions that determine and explain the dynamics of a system. We provide a formal definition of Causal WMs (CWMs) grounded in the tasks they are intended to support, connecting world modelling with existing work in causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making. Finally, we relate CWMs to the literature on identifiability, clarifying when the components of a WM can be recovered from data and up to which equivalence. With this, we ground WMs in representations and structures that support causal reasoning and informed decision-making.

### 🤖 AI 总结

**一句话总结**：World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unifying, Perspective, Causal, World, Models, Observations, Representations, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13456v1) | [下载PDF](https://arxiv.org/pdf/2608.13456v1.pdf)

---

## cs.CL

## [5. SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization](https://arxiv.org/abs/2608.13538v1)

**作者**：Weihan Meng, Hongzhu Guo, Yi Jing 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-13

### 📄 论文摘要

Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downstream layers to generate natural-language explanations of the injected features. Once trained, the resulting verbalizer explains SAE features directly from decoder directions, addressing both limitations. Our experiments show that the learned verbalization capability generalizes to unseen features, transfers across separately trained SAE dictionaries, and, with a lightweight adapter, extends to SAE features from different LLMs. Intervention experiments show that injecting multiple directions yields an explanation combining their meanings, while reversing individual directions produces corresponding meaning shifts.

### 🤖 AI 总结

**一句话总结**：Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SAEVerbalizer, Generating, Explanations, Sparse, Autoencoder, Features, via, Representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13538v1) | [下载PDF](https://arxiv.org/pdf/2608.13538v1.pdf)

---

## [6. DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data](https://arxiv.org/abs/2608.13517v1)

**作者**：Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-13

### 📄 论文摘要

Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir v1 outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish. The model is available on the Hugging Face Hub: https://huggingface.co/danish-foundation-models/DFM-Mimir

### 🤖 AI 总结

**一句话总结**：Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：v1, An, DFM, Mimir, Open, HRM, Delivering, Frontier

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13517v1) | [下载PDF](https://arxiv.org/pdf/2608.13517v1.pdf)

---

## [7. Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining](https://arxiv.org/abs/2608.13515v1)

**作者**：Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-13

### 📄 论文摘要

Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence by how much its gradient update reduces the squared distance to the final parameters of a given pretraining run, and estimate this quantity from intermediate checkpoints without retraining. Applying the method to 18 configurations from the Pythia and PolyPythia suites, we find systematic temporal changes in influential data. Early in training, literature-related data are more strongly aligned with the trajectory toward the final parameters, whereas STEM data become more strongly aligned in later stages. This qualitative crossover is broadly consistent across model configurations. Our results provide a tractable trajectory-level view of how influential data change throughout pretraining, complementing influence analyses defined with respect to specific downstream tasks or validation sets.

### 🤖 AI 总结

**一句话总结**：Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capab...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Measuring, Task-Agnostic, Training, Data, Influence, Across, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13515v1) | [下载PDF](https://arxiv.org/pdf/2608.13515v1.pdf)

---

## [8. Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity](https://arxiv.org/abs/2608.13484v1)

**作者**：Dananjay Srinivas, Saksham Khatwani, Maria Pacheco  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-13

### 📄 论文摘要

When asked about entities outside their knowledge boundary, LLMs routinely fabricate plausible-sounding details rather than backing off to safer, more general claims. We frame this failure through a Gricean lens: a cooperative speaker who is uncertain about a referent retreats up the specificity hierarchy, trading informativeness for truthfulness. We ask whether LLMs have the ingredients to perform this retreat. Using a T-REx-based benchmark that varies entity familiarity and referent specificity, we probe models to answer two questions: (i) do their activations encode whether a referent falls inside the knowledge boundary, and (ii) do they anticipate the specificity of the referent they are about to generate? We find that the answer to both is yes, but the two signals are not reconciled in generation. Models overwhelmingly prefer specific referents even when the entity is unknown to them, and do so even when offered correct generic alternatives. The substrate for a Gricean retreat is present, but the policy that would act on it is not. We position our findings as a first step toward Gricean alignment, training or steering objectives that couple knowledge-boundary awareness to referent-specificity during generation.

### 🤖 AI 总结

**一句话总结**：When asked about entities outside their knowledge boundary, LLMs routinely fabricate plausible-sounding details rather than backing off to safer, more general claims. We frame this failure through a G...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Toward, Gricean, Retreat, Probing, Knowledge, Boundaries, Referent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13484v1) | [下载PDF](https://arxiv.org/pdf/2608.13484v1.pdf)

---

## cs.CV

## [9. AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560v1)

**作者**：Yaxin Luo, Haobin Jiang, Jialv Zou 等 14 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-08-13

### 📄 论文摘要

Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design priors, where a meta-harness optimizer guides a code agent to recursively improve harness based on rollout feedback. To instantiate and evaluate this framework, we focus on the academic paper-to-poster generation task and introduce PosterBench, comprising a 100-paper Main Track spanning five disciplines and PosterBench-mini, a shared 10-paper subset for controlled evaluation. On the PosterBench Main Track, AutoDesign achieves the highest score of 78.32, surpassing the closed-source commercial system Claude Design by 7.45 points. Across seven controlled code-agent-model configurations, integrating the learned DesignHarness consistently improves performance, increasing the average PosterBench Score from 54.99 to 67.39 (+12.4%). In a fully autonomous long-horizon loop, it executes 253 tool calls and 11 editing turns within 40 minutes for under $3, reaching average conference-poster quality in human evaluation. A system-blind human study further demonstrates that AutoDesign achieves the highest human preference among evaluated systems.

### 🤖 AI 总结

**一句话总结**：Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal har...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AutoDesign, Meta-Harness, Optimization, Long-Horizon, Agentic, Design, Transforming, multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13560v1) | [下载PDF](https://arxiv.org/pdf/2608.13560v1.pdf)

---

## [10. PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552v1)

**作者**：Kaixin Ding, Xi Chen, Minghong Cai 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or walk into the water and inspect whether realistic water ripples are generated. The action sequence required to achieve the same objective may vary substantially between models, making fixed action-conditioned evaluation unsuitable for cross-model comparison. To address this, we employ multi-modal Agent Players to interact with world models toward specified long-horizon objectives. Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective. To evaluate performance thoroughly, we assess models along four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution. In addition, we incorporate basic ability metrics for video quality and controllability. Experiments across nine state-of-the-art world models reveal that current models remain unreliable on long-horizon interactive objectives, particularly in maintaining spatial consistency and persistent state evolution. Code and data are available at https://github.com/kxding/PlayWorld.

### 🤖 AI 总结

**一句话总结**：Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long seque...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, PlayWorld, Benchmarking, World, Models, Players, over, Long-Horizon

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13552v1) | [下载PDF](https://arxiv.org/pdf/2608.13552v1.pdf)

---

## [11. Alaya-EVOKE: From Linear-Scaling Supervision to Endless World](https://arxiv.org/abs/2608.13546v1)

**作者**：Yuanyang Yin, Gongxuan Wang, Yifan Zhan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state and redesigning the teacher for long-horizon interactive generation. Scene geometry is maintained in an external, camera-indexed world state bank, from which only view-relevant information is retrieved, keeping the denoiser context bounded as the session grows. Rather than treating the teacher as a fixed generator, we design it for long-horizon supervision: its sparse attention combines chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state, yielding linear growth in memory and compute while enabling supervision over long horizons. Such supervision exposes content drift that stays locally plausible within short windows, while per-chunk conditioning enables prompt changes and event control throughout the sequence. A 30-second distribution-matching objective, applied under self-forced rollouts, transfers both capabilities to a three-step student that uses no classifier-free guidance, improving resistance to long-term drift while preserving responsive conditioning. With bounded context and recurrent external memory, Evoke supports open-ended, continuously evolving generation; on a single H200 at $384\times 640$, each $1.5\,\mathrm{s}$ chunk is generated in $2.11\,\mathrm{s}$. As a three-step world model, Evoke achieves state-of-the-art performance on WBench while remaining competitive on VBench-Long and VBench-2.0.

### 🤖 AI 总结

**一句话总结**：Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Alaya-EVOKE, Linear-Scaling, Supervision, Endless, World, Interactive, models, must

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13546v1) | [下载PDF](https://arxiv.org/pdf/2608.13546v1.pdf)

---

## [12. TabSOM: A tabular-to-image encoding method based on self-organizing maps](https://arxiv.org/abs/2608.13513v1)

**作者**：David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara 等 6 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SNE, UMAP, PCA). However, they encode only the marginal value of each feature and discard information about feature relationships. We propose TabSOM, a tabular-to-image encoding built on the Self-Organizing Map (SOM), which provides: (i) a spatial layout in which every input feature occupies a fixed canvas position derived from its component plane via collision-free Hungarian assignment; and (ii) a graph that captures pairwise feature relationships derived from the SOM component planes. The resulting image stacks two multi-scale node channels: one encodes feature values at fixed scales, while the other encodes pairwise feature interactions as spatial connections between related features. Two SOM-derived interpretability approaches are introduced: a prototype-inspired partial dependence plot and a class--separation importance score. Benchmarked against twelve existing tabular-to-image methods across public binary-classification datasets, TabSOM ranks first or second on every dataset and achieves the lowest variance of any method evaluated. Interpretability obtained with TabSOM was validated against Random Forest, XGBoost, and SHAP, the class-separation score shows reasonable agreement with established baselines on the top-ranked features while capturing complementary structural information from input data. These results demonstrate that TabSOM provides an effective and interpretable approach for applying deep learning architectures to tabular data, bridging the performance--interpretability gap in this domain.

### 🤖 AI 总结

**一句话总结**：Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image rep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TabSOM, tabular-to-image, encoding, method, self-organizing, maps, methods, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13513v1) | [下载PDF](https://arxiv.org/pdf/2608.13513v1.pdf)

---

## [13. GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502v1)

**作者**：Yanming Yang, Chenxi Song, Ping Wang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations and camera poses. In this work, we propose a novel framework that reconstructs high-quality 3D scenes from a single SCI measurement by leveraging 3D Gaussian Splatting (3DGS) and the powerful priors of large-scale vision foundation models (VFMs). Our primary reconstruction combines measurement-derived 3D VFM initialization with SCI-aware Gaussian optimization. After coarse-stage convergence, an auxiliary 2D VFM provides pseudo-view supervision at synthesized viewpoints for local appearance refinement. To further address the instability caused by ambiguous SCI supervision during 3DGS optimization, we introduce Opacity-Guided Splitting and Growth Regulation (OSGR), an SCI-specific densification strategy that augments split candidates using local opacity statistics, discourages loss-compensating opacity inflation through mean-opacity regulation, and bounds representation growth with explicit candidate-ratio and Gaussian-count constraints. Extensive experiments across multiple benchmarks demonstrate that our method achieves the strongest overall performance, combining leading reconstruction quality and robustness to viewpoint variation with competitive computational efficiency.

### 🤖 AI 总结

**一句话总结**：Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing tempora...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GS$^, $CI, Robust, Gaussian, Splatting, Snapshot, Compressive, Imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13502v1) | [下载PDF](https://arxiv.org/pdf/2608.13502v1.pdf)

---

## [14. TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](https://arxiv.org/abs/2608.13495v1)

**作者**：Yi-Chung Chen, Philip Jacobson, Tom Lampo 等 9 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on shortcuts from static scene context and struggle to distinguish motion-centric events, such as turning left versus right or accelerating versus decelerating. In this work, we study how to adapt a general-purpose multimodal embedding model to driving-video retrieval. We first fine-tune Qwen3-VL-Embedding on paired clips and reasoning traces from nuReasoning using an InfoNCE objective. While this stage substantially improves overall retrieval, caption supervision alone remains insufficient for fine-grained motion understanding. We therefore introduce TraVEL (Trajectory-Guided Video Embedding Learning), a motion-aware fine-tuning framework that uses ego-trajectory similarity as a reward within Group Relative Policy Optimization. Trajectories serve only as privileged training supervision; retrieval still operates on single-vector video embeddings without ego poses, expert rules, or auxiliary perception outputs. We further construct a driving-video retrieval benchmark from nuReasoning. Experiments show that TraVEL improves motion-centric retrieval across model scales: relative to SFT, it raises longitudinal and lateral mAP by 9.8 and 4.7 points at 2B, with corresponding gains of 7.2 and 1.5 points at 8B. TraVEL thus combines physically grounded supervision with efficient embedding-based search.

### 🤖 AI 总结

**一句话总结**：Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TraVEL, Trajectory-Guided, Video, Embedding, Learning, Driving-Video, Retrieval, Efficiently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13495v1) | [下载PDF](https://arxiv.org/pdf/2608.13495v1.pdf)

---

## [15. DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489v1)

**作者**：DreamX Team, Rui Chen, Xiangxiang Chu 等 10 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-08-13

### 📄 论文摘要

We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.

### 🤖 AI 总结

**一句话总结**：We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, DreamX-Phi, Action-Conditioned, Video, World, Model, Robotic, Manipulation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13489v1) | [下载PDF](https://arxiv.org/pdf/2608.13489v1.pdf)

---

## [16. MapRoute++: Surrogate-Guided Semantic Routing for Visual Concept Unlearning](https://arxiv.org/abs/2608.13478v1)

**作者**：Ashok Urlana, L. D. M. S. Sai Teja, Vivek Hruday Kavuri 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

We present our submission to Task 3 of the Gen$μ$ 2.0 Challenge on visual concept unlearning. Building on MapRoute, we introduce task-specific training objectives, richer concept representations, and semantic routing for concept-specific mapper selection. Our approach improves robust concept removal while preserving unrelated and semantically adjacent concepts. On the official benchmark, evaluated using the Erasing-Retention-Robustness (ERR) metric on Stable Diffusion v1.4, our method outperforms the state-of-the-art baseline by 12.1\% on average across the five concept categories, achieving substantial gains.

### 🤖 AI 总结

**一句话总结**：We present our submission to Task 3 of the Gen$μ$ 2.0 Challenge on visual concept unlearning. Building on MapRoute, we introduce task-specific training objectives, richer concept representations, and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, MapRoute++, Surrogate-Guided, Semantic, Routing, Visual, Concept, Unlearning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13478v1) | [下载PDF](https://arxiv.org/pdf/2608.13478v1.pdf)

---

## [17. MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](https://arxiv.org/abs/2608.13463v1)

**作者**：Daniel Perkins, John Squires, Janou Milligan 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learners (SSL), and vision-language models (VLMs), each trained on a unified label space constructed from multiple image datasets with differing distributions and characteristics. Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains. Crucially, we show that ARMDIL effectively navigates these trade-offs, performing competitively with specialized training-based routers. Furthermore, it drastically improves adaptability by allowing new information to be integrated via simple prompt modifications, while enhancing interpretability through natural language reasoning traces. These advances in cross-dataset image classification pave the way for more reliable general-purpose vision systems such as AI assistants and autonomous robots.

### 🤖 AI 总结

**一句话总结**：Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MLLM-Routed, Heterogeneous, Ensembles, Robust, Cross-Dataset, Image, Classification, Modern

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13463v1) | [下载PDF](https://arxiv.org/pdf/2608.13463v1.pdf)

---

## [18. SNM-VFI: Symmetric Nonlinear Motion-Guided Generative Video Frame Interpolation](https://arxiv.org/abs/2608.13460v1)

**作者**：Jisoo Jeong, Hong Cai, Jamie Menjay Lin 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

We propose Symmetric Nonlinear Motion-guided Generative Video Frame Interpolation (SNM-VFI), a training-free framework for motion-controllable generative video frame interpolation with pre-trained optical flow and video diffusion models. Unlike conventional diffusion-based VFI methods that synthesize intermediate frames from random noise, SNM-VFI guides the generative process with correspondence-aware frames produced by a symmetric nonlinear motion model. Specifically, we first utilize a pre-trained optical flow model to construct multi-frame nonlinear flow-based intermediate frames and confidence maps. These flow-guided frames are then encoded as latent priors to initialize and iteratively guide a pre-trained Video Diffusion model, enabling the diffusion model to preserve dense motion correspondence while improving perceptual realism. To further enhance output quality, we employ confidence maps to fuse structurally reliable flow-based predictions with diffusion-generated details in uncertain regions such as occlusions and object boundaries. Extensive evaluations on challenging benchmarks, including DAVIS, Sintel, and KITTI, demonstrate that SNM-VFI achieves strong perceptual quality, competitive reconstruction accuracy, and robust temporal coherence across diverse motion scenarios.

### 🤖 AI 总结

**一句话总结**：We propose Symmetric Nonlinear Motion-guided Generative Video Frame Interpolation (SNM-VFI), a training-free framework for motion-controllable generative video frame interpolation with pre-trained opt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SNM-VFI, Symmetric, Nonlinear, Motion-Guided, Generative, Video, Frame, Interpolation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13460v1) | [下载PDF](https://arxiv.org/pdf/2608.13460v1.pdf)

---

## [19. Fine-Grained Action Recognition with Cross-Attentive Latent Sparse Experts](https://arxiv.org/abs/2608.13458v1)

**作者**：Imtiaz Ul Hassan, Tasweer Ahmad, Nik Bessis 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Fine-grained human action recognition (FHAR) must distinguish visually similar actions that differ mainly in body configuration, timing, or local appearance. RGB representations retain visual context but often suppress joint-level geometry, whereas skeleton representations encode kinematics but discard dense spatial detail. We introduce FineX, which factorizes fine-grained cues into RGB appearance, pose heatmap geometry, and skeletal-graph topology. Pairwise cross-attention enables symmetric, stream-preserving information exchange, followed by a streamwise latent sparse Mixture-of-Experts that routes each representation to a content-dependent subset of shared experts, regularized by a load-balancing objective. FineX achieves state-of-the-art results on Gym99, Gym288, and Diving48. On the long-tailed Gym288, it raises mean class accuracy from 68.6% to 76.2% (+7.6 points) without textual supervision or large-scale vision-language pre-training, demonstrating the benefit of structured visual-pose-graph fusion and conditional expert refinement for FHAR.

### 🤖 AI 总结

**一句话总结**：Fine-grained human action recognition (FHAR) must distinguish visually similar actions that differ mainly in body configuration, timing, or local appearance. RGB representations retain visual context ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fine-Grained, Action, Recognition, Cross-Attentive, Latent, Sparse, Experts, human

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13458v1) | [下载PDF](https://arxiv.org/pdf/2608.13458v1.pdf)

---

## [20. UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](https://arxiv.org/abs/2608.13453v1)

**作者**：Yukun Dai, Mingzhe Dai, Tianshi Wang 等 6 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-13

### 📄 论文摘要

Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $π_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.

### 🤖 AI 总结

**一句话总结**：Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their dir...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniTexture, Cross-Task, Universal, Adversarial, Textures, Vision-Language-Action, Models, VLA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13453v1) | [下载PDF](https://arxiv.org/pdf/2608.13453v1.pdf)

---

## cs.LG

## [21. Defensive Boosting for Online Probabilistic Forecasting](https://arxiv.org/abs/2608.13554v1)

**作者**：Georgy Noarov, Aaron Roth  
**分类**：cs.LG, cs.CC, cs.DS, stat.ML  
**发布时间**：2026-08-13

### 📄 论文摘要

We study online probabilistic forecasting of binary outcomes chosen by an adaptive adversary. Given an online learning algorithm for a weak hypothesis class $H$, we would like to efficiently obtain two incomparable guarantees that existing online boosting techniques provide separately. Online gradient boosting competes in Brier score with the best predictor induced by the span of $H$ on every sequence, but promises nothing when the span does not contain an accurate predictor. Online weak-to-strong boosting drives classification error to zero under a weak-learning condition, but promises little when that condition fails.   We give a simple defensive forecasting algorithm, the Defensive Booster, that obtains both guarantees. On every adaptive sequence, its Brier score is competitive with the best prediction induced by the span of $H$ at the same rate as online gradient boosting; simultaneously, whenever the realized transcript satisfies the smooth weak-learning condition, its Brier score and randomized classification error satisfy the same rate guarantee as online classification boosting. This is achieved by operationalizing the "dual view" of boosting: When the algorithm's randomized classification error is persistently high, its mistake weights form a smooth reweighting on which every weak hypothesis has low edge, yielding an ex-post hard-core certificate that the weak-learning condition fails. We also develop a strongly adaptive variant, which satisfies both guarantees on every time interval. The Defensive Booster is very efficient: it accesses just one weak-class learner, whereas the prior online boosting methods we compare against maintain large weak-learner ensembles. Experiments on synthetic and real data streams demonstrate its strong predictive performance (sometimes substantially improving over all prior baselines) coupled with orders-of-magnitude faster runtime.

### 🤖 AI 总结

**一句话总结**：We study online probabilistic forecasting of binary outcomes chosen by an adaptive adversary. Given an online learning algorithm for a weak hypothesis class $H$, we would like to efficiently obtain tw...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, of, Defensive, Boosting, Online, Probabilistic, Forecasting, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13554v1) | [下载PDF](https://arxiv.org/pdf/2608.13554v1.pdf)

---

## [22. Exponential Convex Calibration Dimension for the Multi-Label Jaccard Measure](https://arxiv.org/abs/2608.13549v1)

**作者**：Mingyuan Zhang  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-08-13

### 📄 论文摘要

The per-instance Jaccard score, or intersection over union (IoU), is standard in multi-label classification and binary segmentation. With $s$ labels, its loss matrix has $2^s$ outcomes and reports. Under the convention $\mathrm{Jac}(\varnothing,\varnothing)=1$, we prove that the Jaccard score, shifted-loss, and ordinary loss matrices are nonsingular and that the loss columns have affine dimension $2^s-1$. The proof combines a finite MinHash Gram representation with Boolean Möbius inversion. For exact calibration, we prove $2^{s-1} \leq \mathrm{CCdim}(L^{\mathrm{Jac}}) \leq 2^s-1$. The lower bound uses a factorially weighted distribution with $2^{s-1}+1$ supported outcomes and Bayes-optimal reports. Consequently, every exactly calibrated convex surrogate requires exponentially many prediction coordinates. We also give two polynomial-dimensional approximation guarantees with explicit regret transfers. A new $F_1$-to-Jaccard transfer turns an existing $(s^2+1)$-dimensional $F_1$ surrogate into a polynomial-time rule with asymptotic Jaccard regret at most $3-2\sqrt{2}$. For any $α>0$ and $0<ρ<1$, a MinHash square-loss surrogate attains Jaccard-regret floor $α$ uniformly over arbitrary conditional label distributions. With probability at least $1-ρ$, the direct construction has dimension $O((s^2+s\log(1/ρ))/α^2)$, while a signed variant has dimension $O((s+\log(1/ρ))/α^2)$. Thus zero-regret calibration requires exponential dimension, whereas every fixed additive regret tolerance admits polynomial prediction dimension.

### 🤖 AI 总结

**一句话总结**：The per-instance Jaccard score, or intersection over union (IoU), is standard in multi-label classification and binary segmentation. With $s$ labels, its loss matrix has $2^s$ outcomes and reports. Un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Exponential, Convex, Calibration, Dimension, Multi-Label, Jaccard, Measure, per-instance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13549v1) | [下载PDF](https://arxiv.org/pdf/2608.13549v1.pdf)

---

## [23. The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity](https://arxiv.org/abs/2608.13520v1)

**作者**：Martin J. Wainwright  
**分类**：cs.LG, cs.AI, cs.IT, math.ST, stat.ML  
**发布时间**：2026-08-13

### 📄 论文摘要

We study masking diffusion for discrete sampling and introduce a path-resolved measure of data geometry called the \emph{unmasking growth complexity} ({\textsf{UGC}\xspace}). Its local increments directly control Kullback--Leibler (KL) discretization error, yielding a unified analysis of Bernoulli-subset and fixed-cardinality unmasking schemes. In log-reveal-odds coordinates, this structure yields optimized single-block and multi-block schedules, and quantifies the gains from adapting computational effort to data geometry. Crucially, we show how {\textsf{UGC}\xspace} increments can be estimated from samples via KL increments along coupled reveal trajectories. This leads to \emph{certified-optimal} samplers that achieve a prescribed KL error with high probability and iteration complexity within a constant factor of the corresponding oracle procedure. Collapsing the \ugc path yields the aggregate {\textsf{UGC}\xspace} mass, which connects to classical multivariate dependence measures and complexity measures from previous analyses of discrete diffusion. In the fine-partition limit, the squared integral of the square-root {\textsf{UGC}\xspace} density determines the sharp leading-order optimal Euler discretization error. Examples exhibit substantial dimension-dependent gains over coarse schedules, including $\widetildeΩ(\sqrt{d})$ improvements achievable with a constant number of adaptively placed blocks.

### 🤖 AI 总结

**一句话总结**：We study masking diffusion for discrete sampling and introduce a path-resolved measure of data geometry called the \emph{unmasking growth complexity} ({\textsf{UGC}\xspace}). Its local increments dire...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Diffusion, data, geometry, masking, Certified-optimal, schedules, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13520v1) | [下载PDF](https://arxiv.org/pdf/2608.13520v1.pdf)

---

## [24. Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology](https://arxiv.org/abs/2608.13518v1)

**作者**：Yunsung Chung, Yingshuo Liu, Abboud F. Hassan 等 7 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregular trajectory: clinical observations, medication changes, repeat interventions, and physiological measurements are recorded asynchronously and can change risk assessment over time. We propose an intervention-aware clinical world model that represents each patient with a structured latent state and evolves it through time-ordered post-intervention events. The model first encodes baseline imaging into a 3D spatial latent state. It then updates this state using procedural context, static covariates, elapsed time, and peri-event physiological embeddings. Follow-up imaging provides training-only supervision through a latent forecasting objective. We apply the framework to atrial fibrillation ablation. During the 90-day recovery window, irregular post-procedure records provide clinically meaningful evidence for long-term recurrence risk. In repeated internal cross-validation on DECAAF-II, our model achieves AUROC 0.756 and AUPRC 0.777 for recurrence prediction. It also achieves a scar-extent MAE of 2.971 percentage points without requiring follow-up MRI intensities at inference. The learned state supports recurrence-risk queries at different horizons and retrospective input editing of blanking-period records.

### 🤖 AI 总结

**一句话总结**：Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregula...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Intervention-Aware, Clinical, World, Model, Post-Op, Outcome, Forecasting, Cardiology

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13518v1) | [下载PDF](https://arxiv.org/pdf/2608.13518v1.pdf)

---

## [25. Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505v1)

**作者**：Lei Bai, Jiaqi Cao, Chiyu Chen 等 125 位作者  
**分类**：cs.LG, cs.CL, cs.CV  
**发布时间**：2026-08-13

### 📄 论文摘要

Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific documents, interleaved image-text data, and diverse scientific corpora. Starting from the pretrained checkpoint, we apply a unified post-training pipeline consisting of supervised fine-tuning, scalable multi-task reinforcement learning (RL), black- and white-box agentic RL, and on-policy distillation. This pipeline is supported by practical techniques that improve rollout and training stability and efficiency, including partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly for agentic tasks. At the architecture level, Intern-S2-Preview-397B extends time series modelling from efficient long-sequence understanding to numerical forecasting, while Memory Decoder is studied as a separate memory-augmented path for rapid scientific specialization without modifying the frozen 397B backbone. Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show that Intern-S2-Preview-397B achieves competitive or leading results in multiple settings. The time series modules improve scientific signal understanding and forecasting on SciTS, while the separate Intern-MemDec-4B extension improves the Biology-Instructions average score from 56.92 to 60.32 without modifying the frozen 397B backbone.

### 🤖 AI 总结

**一句话总结**：Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Intern-S2-Preview, Scientific, Agentic, Foundation, Model, discovery, increasingly, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13505v1) | [下载PDF](https://arxiv.org/pdf/2608.13505v1.pdf)

---

## [26. Sparse Orthogonal Regression Technique: A Spectral Framework for Equation Discovery, Approximation, and Integration](https://arxiv.org/abs/2608.13504v1)

**作者**：Sabin Roman, Ljupco Todorovski, Saso Dzeroski  
**分类**：cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

We develop the Sparse Orthogonal Regression Technique (SORT), a sparse spectral framework for learning orthonormal-basis expansions from noisy and irregularly sampled data. SORT estimates expansion coefficients directly from observations using L1-regularized regression, avoiding explicit quadrature or analytic inner-product evaluation. The central application is data-driven discovery of ordinary differential equations: vector fields are represented in chosen orthogonal bases and learned as sparse coefficient expansions. This provides a complementary route to symbolic regression, grammar-based discovery, and SINDy-style sparse identification by first recovering a compact spectral representation, which can later guide searches for simpler analytic forms. Across the dynamical-system experiments, SORT matches or improves upon library-based sparse-regression baselines when the basis is well adapted to the problem, and shows more stable degradation under sparse sampling, noisy derivative estimates, and representation mismatch. Specific examples illustrate why this representation is useful: if a finite library misses the problem-specific nonlinearity, the resulting model can fail. SORT is not immune to mismatch, but it shifts the problem away from brittle selection among generic terms to basis design adapted to the problem domain. The experiments also show that dominant low-order coefficients persist as model order increases, supporting order-consistent model growth. Beyond equation discovery, the same learned expansion supports nonlinear approximation and estimation of complex, high-dimensional integrals by coefficient readout. Overall, SORT provides a reusable intermediate representation for system identification, approximation, and integration, while making basis design an explicit part of the scientific modeling problem.

### 🤖 AI 总结

**一句话总结**：We develop the Sparse Orthogonal Regression Technique (SORT), a sparse spectral framework for learning orthonormal-basis expansions from noisy and irregularly sampled data. SORT estimates expansion co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sparse, Orthogonal, Regression, Technique, Spectral, Framework, Equation, Discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13504v1) | [下载PDF](https://arxiv.org/pdf/2608.13504v1.pdf)

---

## [27. Active-Trace Complexity Bounds for Moreau--Yosida Unadjusted Langevin Sampling](https://arxiv.org/abs/2608.13467v1)

**作者**：Yuchen Xin, Zhihua Zhang  
**分类**：cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

We study the Moreau--Yosida unadjusted Langevin algorithm (MYULA) for the nonsmooth composite target \[ π(dx)\propto \exp\{-f(x)-g(x)\}\,dx, \qquad x\in\mathbb R^d, \] where \(f\) is \(m\)-strongly convex with \(L_f\)-Lipschitz gradient and \(g\) is convex and \(G\)-Lipschitz. Let \(g_λ\) be the Moreau envelope of \(g\), \(π_λ\) the corresponding smoothed target, and \(a_λ=\operatorname{tr}H_λ\), where \(H_λ\) is the a.e./weak Hessian of \(g_λ\). We show that the leading MYULA discretization error is controlled by the reference active trace \(B_{\mathrm{ref}}\), the average of \(a_λ\) along the heat substep of one MYULA update started from \(π_λ\), rather than by the global curvature bound \(d/λ\). If \(M_λ\) is an a.e. upper bound for \(a_λ\), then, up to logarithmic factors, \[ N \lesssim \frac{1}{m} \left[ L_f + \frac{ τ_f+G^2+B_{\mathrm{ref}} }{ \varepsilon_{\mathrm{alg}}^2 } + \frac{M_λ}{\varepsilon_{\mathrm{alg}}} \right], \qquad τ_f:= \sup_x\operatorname{tr}\nabla^2 f(x), \] iterations suffice to ensure \(\sqrt m\,W_2(μ_N,π_λ)\leq\varepsilon_{\mathrm{alg}}\), where \(μ_N\) is the law of the \(N\)-th iterate and \(W_2\) is the quadratic Wasserstein distance. We also prove the Moreau-bias bound \[ \sqrt m\,W_2(π_λ,π) \leq \frac{G^2λ}{4}. \] Thus, choosing \(λ\asymp\varepsilon/G^2\) gives an end-to-end guarantee for \(π\). The universal estimate \(B_{\mathrm{ref}}\leq d/λ\) yields \(\widetilde O(\varepsilon^{-3})\) accuracy dependence. For the structured piecewise-linear, lasso-type, group, and total-variation penalties considered here, curvature--tube estimates make \(B_{\mathrm{ref}}\) independent of \(λ\), yielding \(\widetilde O(\varepsilon^{-2})\) for the same classical MYULA kernel.

### 🤖 AI 总结

**一句话总结**：We study the Moreau--Yosida unadjusted Langevin algorithm (MYULA) for the nonsmooth composite target \[ π(dx)\propto \exp\{-f(x)-g(x)\}\,dx, \qquad x\in\mathbb R^d, \] where \(f\) is \(m\)-strongly co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Active-Trace, Complexity, Bounds, Moreau--Yosida, Unadjusted, Langevin, Sampling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13467v1) | [下载PDF](https://arxiv.org/pdf/2608.13467v1.pdf)

---

## [28. Concept Drift Detection and Adaptive Retraining of Malware Classification Models](https://arxiv.org/abs/2608.13465v1)

**作者**：Christofer Washington Berruz Chungata, Martin Jurecek, Katerina Potika 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.CR  
**发布时间**：2026-08-13

### 📄 论文摘要

Concept drift refers to changes over time in the statistical properties of data, as compared to the data that was used to train a learning model. Machine learning models for malware detection or classification are particularly susceptible to performance degradation caused by concept drift, as attackers constantly modify existing malware. In this chapter, we analyze two machine learning-based approaches to automated concept drift detection-a novel approach based on One-Class Support Vector Machines (OCSVM) and a previously-studied technique based on Minibatch K-Means (MK-Means). For comparison we also consider Maximum Mean Discrepancy (MMD), a statistical technique for detecting changes in multidimensional data. We conduct an extensive series of experiments comparing the effectiveness of four learning models, namely, Multilayer Perceptron, Random Forest, Support Vector Machines, and eXtreme Gradient Boosting. For each of these models, we consider three distinct scenarios: A static scenario where no model retraining occurs, a periodic scenario where models are constantly retrained irrespective of concept drift, and a drift-aware scenario where models are only retrained when concept drift is detected. Under the drift-aware scenario, we analyze the tradeoff between accuracy and training efficiency using Pareto Front analysis. We find that all three concept drift detection techniques achieve classification accuracy comparable to periodic retraining, while offering substantially greater efficiency in terms of the number of models that must be retrained. In addition, drift-aware retraining based on our OCSVM technique generally outperforms the MK-Means and MMD approaches. Overall, these results provide strong evidence that we can accurately detect concept drift in malware classification models.

### 🤖 AI 总结

**一句话总结**：Concept drift refers to changes over time in the statistical properties of data, as compared to the data that was used to train a learning model. Machine learning models for malware detection or class...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Concept, Drift, Detection, Adaptive, Retraining, Malware, Classification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13465v1) | [下载PDF](https://arxiv.org/pdf/2608.13465v1.pdf)

---

## [29. Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization](https://arxiv.org/abs/2608.13461v1)

**作者**：Jiayi Dan, Bo Li, Lu Deng 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

Post-click conversion rate (CVR) is a key metric in various scenarios including e-commerce and advertising, reflecting the efficiency and user experience in the second stage of the conversion process. Estimating the causal effect on CVR is therefore of great practical importance. However, directly applying existing causal inference methods to clicked samples introduces sample selection bias and increased variance due to the exclusion of non-click data. Recent studies on CVR prediction introduce "ideal loss", which optimizes model parameters using an unbiased estimate of the loss over the full sample. Nevertheless, there is no guarantee that unbiasedness of the loss implies unbiasedness of the final estimator.   We revisit this challenge from the perspective of semiparametric theory. Specifically, we develop a new doubly robust causal effect estimator for chain-structured outcomes such as CVR, and derive its theoretical properties in detail. It achieves a faster convergence rate compared to nuisance parameters estimation and is therefore more robust when using flexible nonparametric estimators, including neural networks. Based on these theoretical findings, we further design a framework based on targeted regularization to improve numerical stability and practical applicability.   Extensive experiments on synthetic and real-world data demonstrate the effectiveness and robustness of our method. In addition, we find that naively combining loss debiasing with standard causal estimators underperforms our method, highlighting the necessity of developing the new estimator tailored to this CVR-style objective with solid theoretical guarantees.

### 🤖 AI 总结

**一句话总结**：Post-click conversion rate (CVR) is a key metric in various scenarios including e-commerce and advertising, reflecting the efficiency and user experience in the second stage of the conversion process....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Doubly, Robust, Estimation, Causal, Effect, CVR, Targeted

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13461v1) | [下载PDF](https://arxiv.org/pdf/2608.13461v1.pdf)

---

## [30. Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](https://arxiv.org/abs/2608.13457v1)

**作者**：Van Khoa Nguyen, Alexandros Kalousis  
**分类**：cs.LG  
**发布时间**：2026-08-13

### 📄 论文摘要

Generating crystals has recently attracted significant interest due to their broad applications in materials science. However, existing generative models struggle to produce complete crystallographic specifications, limiting their ability to capture global symmetry and structural dependencies. In particular, current state-of-the-art approaches generate crystals only up to site symmetries and rely on sampling space groups from empirical distributions during generation. Inspired by \emph{spontaneous symmetry breaking} in physics, where crystals break symmetries under external conditions, we propose a novel diffusion-based framework that generates full structure specifications by reversing from the lowest-symmetry priors. Our method leverages a Markovian jump-diffusion process to model these symmetry-breaking dynamics, enabling it to traverse different space groups in a physically motivated manner. Our model, dubbed \emph{Symmetry-breaking Crystal Diffusion} (SbCD), introduces a principled approach to explicitly incorporate inter-space-group transitions into the generative process. In de novo generation experiments on MP20 and MPTS-52, SbCD outperforms its symmetry-preserving counterpart by a substantial margin, offering a promising perspective for generative modeling of crystalline materials.

### 🤖 AI 总结

**一句话总结**：Generating crystals has recently attracted significant interest due to their broad applications in materials science. However, existing generative models struggle to produce complete crystallographic ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：De, Symmetry-Breaking, Novo, Crystal, Generation, via, Markovian, Jump

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.13457v1) | [下载PDF](https://arxiv.org/pdf/2608.13457v1.pdf)

---

