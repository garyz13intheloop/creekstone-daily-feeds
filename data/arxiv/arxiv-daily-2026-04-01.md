# arXiv AI 论文日报 | 2026-04-01

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (15 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. Extending MONA in Camera Dropbox: Reproduction, Learned Approval, and Design Implications for Reward-Hacking Mitigation](https://arxiv.org/abs/2603.29993v1)

**作者**：Nathan Heath  
**分类**：cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

Myopic Optimization with Non-myopic Approval (MONA) mitigates multi-step reward hacking by restricting the agent's planning horizon while supplying far-sighted approval as a training signal~\cite{farquhar2025mona}. The original paper identifies a critical open question: how the method of constructing approval -- particularly the degree to which approval depends on achieved outcomes -- affects whether MONA's safety guarantees hold. We present a reproduction-first extension of the public MONA Camera Dropbox environment that (i)~repackages the released codebase as a standard Python project with scripted PPO training, (ii)~confirms the published contrast between ordinary RL (91.5\% reward-hacking rate) and oracle MONA (0.0\% hacking rate) using the released reference arrays, and (iii)~introduces a modular learned-approval suite spanning oracle, noisy, misspecified, learned, and calibrated approval mechanisms. In reduced-budget pilot sweeps across approval methods, horizons, dataset sizes, and calibration strategies, the best calibrated learned-overseer run achieves zero observed reward hacking but substantially lower intended-behavior rates than oracle MONA (11.9\% vs.\ 99.9\%), consistent with under-optimization rather than re-emergent hacking. These results operationalize the MONA paper's approval-spectrum conjecture as a runnable experimental object and suggest that the central engineering challenge shifts from proving MONA's concept to building learned approval models that preserve sufficient foresight without reopening reward-hacking channels. Code, configurations, and reproduction commands are publicly available. https://github.com/codernate92/mona-camera-dropbox-repro

### 🤖 AI 总结

**一句话总结**：Myopic Optimization with Non-myopic Approval (MONA) mitigates multi-step reward hacking by restricting the agent's planning horizon while supplying far-sighted approval as a training signal~\cite{farq...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：奖励劫持缓解, 短视优化, 非短视认可, 学习型认可模型, 认可校准, 规划视野限制, 监督信号设计, 安全保证分析

**评分**：67

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29993v1) | [下载PDF](https://arxiv.org/pdf/2603.29993v1.pdf)

---

## [2. Structured Intent as a Protocol-Like Communication Layer: Cross-Model Robustness, Framework Comparison, and the Weak-Model Compensation Effect](https://arxiv.org/abs/2603.29953v1)

**作者**：Peng Gang  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-03-31

### 📄 论文摘要

How reliably can structured intent representations preserve user goals across different AI models, languages, and prompting frameworks? Prior work showed that PPS (Prompt Protocol Specification), a 5W3H-based structured intent framework, improves goal alignment in Chinese and generalizes to English and Japanese. This paper extends that line of inquiry in three directions: cross-model robustness across Claude, GPT-4o, and Gemini 2.5 Pro; controlled comparison with CO-STAR and RISEN; and a user study (N=50) of AI-assisted intent expansion in ecologically valid settings. Across 3,240 model outputs (3 languages x 6 conditions x 3 models x 3 domains x 20 tasks), evaluated by an independent judge (DeepSeek-V3), we find that structured prompting substantially reduces cross-language score variance relative to unstructured baselines. The strongest structured conditions reduce cross-language sigma from 0.470 to about 0.020. We also observe a weak-model compensation pattern: the lowest-baseline model (Gemini) shows a much larger D-A gain (+1.006) than the strongest model (Claude, +0.217). Under the current evaluation resolution, 5W3H, CO-STAR, and RISEN achieve similarly high goal-alignment scores, suggesting that dimensional decomposition itself is an important active ingredient. In the user study, AI-expanded 5W3H prompts reduce interaction rounds by 60 percent and increase user satisfaction from 3.16 to 4.04. These findings support the practical value of structured intent representation as a robust, protocol-like communication layer for human-AI interaction.

### 🤖 AI 总结

**一句话总结**：结构化意图框架（如5W3H/PPS）能作为“协议层”显著提升跨模型、跨语言的目标对齐稳定性，并在较弱模型上带来更大的补偿性收益。

**研究动机**：不同大模型、不同语言与不同提示框架下，用户目标往往在传递中发生漂移；作者希望验证结构化意图表示是否能更可靠地保真用户意图并减少跨条件波动。

**核心方法**：在三种语言、三种模型（Claude/GPT-4o/Gemini 2.5 Pro）、多领域多任务上，对比无结构提示与多种结构化框架（5W3H/PPS、CO-STAR、RISEN）并由独立评审模型打分；同时开展N=50用户研究评估AI辅助意图扩写的交互效率与满意度。

**主要结论**：结构化提示显著降低跨语言表现方差（最强条件将sigma从0.470降至约0.020），且出现“弱模型补偿效应”（Gemini增益远高于Claude）；在当前评估分辨率下5W3H/CO-STAR/RISEN得分相近，暗示“维度分解”是关键机制，用户研究中还表现为交互轮次减少约60%并提升满意度（3.16→4.04）。

**关键词**：结构化意图表示, 协议式提示, 5W3H, 目标对齐评测, 跨语言鲁棒性, 跨模型泛化, 提示框架对比, 维度分解, 弱模型补偿效应, 意图扩展

**评分**：69

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29953v1) | [下载PDF](https://arxiv.org/pdf/2603.29953v1.pdf)

---

## [3. Physiological and Semantic Patterns in Medical Teams Using an Intelligent Tutoring System](https://arxiv.org/abs/2603.29950v1)

**作者**：Xiaoshan Huang, Conrad Borchers, Jiayi Zhang 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-03-31

### 📄 论文摘要

Effective collaboration requires teams to manage complex cognitive and emotional states through Socially Shared Regulation of Learning (SSRL). Physiological synchrony (i.e., longitudinal alignment in physiological signals) can indicate these states, but is hard to interpret on its own. We investigate the physiological and conversational dynamics of four medical dyads diagnosing a virtual patient case using an intelligent tutoring system. Semantic shifts in dialogue were correlated with transient physiological synchrony peaks. We also coded utterance segments for SSRL and derived cosine similarity using sentence embeddings. The results showed that activating prior knowledge featured significantly lower semantic similarity than simpler task execution. High physiological synchrony was associated with lower semantic similarity, suggesting that such moments involve exploratory and varied language use. Qualitative analysis triangulated these synchrony peaks as ``pivotal moments'': successful teams synchronized during shared discovery, while unsuccessful teams peaked during shared uncertainty. This research advances human-centered AI by demonstrating how biological signals can be fused with dialogues to understand critical moments in problem solving.

### 🤖 AI 总结

**一句话总结**：研究发现医学生二人组在智能辅导系统中诊断虚拟病例时，对话语义的“转折/变化”常与短暂的生理同步峰值同时出现，这些峰值对应团队问题求解的关键时刻（成功的共同发现或失败的共同不确定）。

**研究动机**：团队协作中的SSRL涉及复杂的认知与情绪调节，而仅靠生理同步信号虽能反映共同状态却难以解释其具体含义；因此需要将生理信号与对话语义结合来识别协作中的关键瞬间并提升可解释性。

**核心方法**：对4组医疗二人团队在智能辅导系统中完成虚拟病人诊断任务进行多模态分析：计算生理同步（随时间的对齐程度）并检测同步峰值，同时对对话进行SSRL编码并用句向量嵌入计算语义余弦相似度，最后将语义变化与同步峰值进行相关与质性三角验证。

**主要结论**：结果显示“激活先验知识”的语义相似度显著低于“简单任务执行”，且高生理同步往往伴随更低的语义相似度，表明同步高点可能发生在探索性、语言多样性更强的互动中；质性分析进一步指出这些同步峰值是“关键时刻”，成功团队在共同发现时同步，失败团队在共同困惑/不确定时同步。

**关键词**：生理同步, 智能辅导系统, 虚拟病人诊断, 医学双人团队协作, 句子嵌入, 余弦相似度, 关键时刻识别, 多模态信号融合

**评分**：56

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29950v1) | [下载PDF](https://arxiv.org/pdf/2603.29950v1.pdf)

---

## [4. ScoringBench: A Benchmark for Evaluating Tabular Foundation Models with Proper Scoring Rules](https://arxiv.org/abs/2603.29928v1)

**作者**：Jonas Landsgesell, Pascal Knoll  
**分类**：cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

Tabular foundation models such as TabPFN and TabICL already produce full predictive distributions yet prevailing regression benchmarks evaluate them almost exclusively via point estimate metrics RMSE R2 These aggregate measures often obscure model performance in the tails of the distribution a critical deficit for high stakes decision making in domains like finance and clinical research where asymmetric risk profiles are the norm We introduce ScoringBench an open benchmark that computes a comprehensive suite of proper scoring rules like CRPS CRLS Interval Score Energy Score weighted CRPS and Brier Score alongside standard point metrics providing a richer picture of probabilistic forecast quality We evaluate realTabPFNv2.5 fine tuned with different scoring rule objectives and TabICL relative to untuned realTabPFNv2.5 across a suite of regression benchmarks Our results confirm that model rankings depend on the chosen scoring rule and that no single pretraining objective is universally optimal This demonstrates that for applications sensitive to extreme events the choice of evaluation metric is as much a domain specific requirement as the data itself ScoringBench is available at https://github.com/jonaslandsgesell/ScoringBench A live preview of the current leaderboard is available at https://scoringbench.bolt.host The leaderboard is maintained via git pull requests to ensure transparency traceability agility and reproducibility

### 🤖 AI 总结

**一句话总结**：ScoringBench 提出一个面向表格基础模型回归任务的概率预测评测基准，用多种“适当评分规则”替代只看点估计指标，从而更真实地比较模型在分布尾部等高风险区域的表现。

**研究动机**：现有回归基准多用 RMSE/R2 等点指标，容易掩盖预测分布尾部的好坏，而金融、临床等场景往往对极端事件与风险不对称更敏感。表格基础模型（如 TabPFN、TabICL）本就输出完整预测分布，因此需要更匹配的概率预测评价体系。

**核心方法**：构建 ScoringBench 基准，除常规点指标外系统计算 CRPS、CRLS、Interval Score、Energy Score、加权 CRPS、Brier Score 等一套 proper scoring rules，并提供开源代码与可追溯的 leaderboard 流程。用该基准对 realTabPFNv2.5（不同评分规则目标微调）与 TabICL 等模型在多套回归基准上进行对比评测。

**主要结论**：实验显示模型排名会随所选评分规则而变化，说明仅用单一指标可能得出误导性结论；同时不存在对所有任务都最优的统一预训练/微调目标。对关注极端风险的应用而言，评价指标的选择与数据本身一样是强领域相关的关键决策。

**关键词**：表格基础模型, 概率回归评测, 预测分布, 适当评分规则, 区间评分, 能量评分, 尾部风险评估, 基准测试排行榜

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29928v1) | [下载PDF](https://arxiv.org/pdf/2603.29928v1.pdf)

---

## cs.CL

## [5. ContextClaim: A Context-Driven Paradigm for Verifiable Claim Detection](https://arxiv.org/abs/2603.30025v1)

**作者**：Yufeng Li, Rrubaa Panchendrarajan, Arkaitz Zubiaga  
**分类**：cs.CL  
**发布时间**：2026-03-31

### 📄 论文摘要

Verifiable claim detection asks whether a claim expresses a factual statement that can, in principle, be assessed against external evidence. As an early filtering stage in automated fact-checking, it plays an important role in reducing the burden on downstream verification components. However, existing approaches to claim detection, whether based on check-worthiness or verifiability, rely solely on the claim text itself. This is a notable limitation for verifiable claim detection in particular, where determining whether a claim is checkable may benefit from knowing what entities and events it refers to and whether relevant information exists to support verification. Inspired by the established role of evidence retrieval in later-stage claim verification, we propose Context-Driven Claim Detection (ContextClaim), a paradigm that advances retrieval to the detection stage. ContextClaim extracts entity mentions from the input claim, retrieves relevant information from Wikipedia as a structured knowledge source, and employs large language models to produce concise contextual summaries for downstream classification. We evaluate ContextClaim on two datasets covering different topics and text genres, the CheckThat! 2022 COVID-19 Twitter dataset and the PoliClaim political debate dataset, across encoder-only and decoder-only models under fine-tuning, zero-shot, and few-shot settings. Results show that context augmentation can improve verifiable claim detection, although its effectiveness varies across domains, model architectures, and learning settings. Through component analysis, human evaluation, and error analysis, we further examine when and why the retrieved context contributes to more reliable verifiability judgments.

### 🤖 AI 总结

**一句话总结**：ContextClaim 将“检索与上下文生成”前移到可核查性声明检测阶段，通过引入外部知识上下文来提升判断一段文本是否可被事实核查的准确性。

**研究动机**：现有可核查性/值得核查检测多仅依赖声明文本本身，但“是否可核查”往往取决于声明涉及的实体/事件及外部是否存在可用证据，因此需要在检测阶段就引入证据线索。

**核心方法**：先从输入声明中抽取实体提及，再从 Wikipedia 检索相关信息作为结构化知识来源，并用大语言模型生成精炼上下文摘要，最后在微调/零样本/小样本设置下用编码器或解码器模型进行可核查性分类。

**主要结论**：在 CheckThat! 2022 COVID-19 Twitter 与 PoliClaim 两个数据集上，上下文增强总体可提升可核查性声明检测表现，但收益受领域、模型架构与学习设置影响；进一步分析与人工评估揭示了检索到的上下文在何种情形下能更可靠地改善判断。

**关键词**：可验证声明检测, 事实核查过滤, 上下文增强, 证据检索前置, 实体提取, 维基百科检索, 上下文摘要生成, LLM, 零样本学习, 少样本学习, 跨域评测

**评分**：71

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30025v1) | [下载PDF](https://arxiv.org/pdf/2603.30025v1.pdf)

---

## [6. Enhancing Structural Mapping with LLM-derived Abstractions for Analogical Reasoning in Narratives](https://arxiv.org/abs/2603.29997v1)

**作者**：Mohammadhossein Khojasteh, Yifan Jiang, Stefano De Giorgis 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

Analogical reasoning is a key driver of human generalization in problem-solving and argumentation. Yet, analogies between narrative structures remain challenging for machines. Cognitive engines for structural mapping are not directly applicable, as they assume pre-extracted entities, whereas LLMs' performance is sensitive to prompt format and the degree of surface similarity between narratives. This gap motivates a key question: What is the impact of enhancing structural mapping with LLM-derived abstractions on their analogical reasoning ability in narratives? To that end, we propose a modular framework named YARN (Yielding Abstractions for Reasoning in Narratives), which uses LLMs to decompose narratives into units, abstract these units, and then passes them to a mapping component that aligns elements across stories to perform analogical reasoning. We define and operationalize four levels of abstraction that capture both the general meaning of units and their roles in the story, grounded in prior work on framing. Our experiments reveal that abstractions consistently improve model performance, resulting in competitive or better performance than end-to-end LLM baselines. Closer error analysis reveals the remaining challenges in abstraction at the right level, in incorporating implicit causality, and an emerging categorization of analogical patterns in narratives. YARN enables systematic variation of experimental settings to analyze component contributions, and to support future work, we make the code for YARN openly available.

### 🤖 AI 总结

**一句话总结**：提出YARN框架，用LLM先将叙事分解并抽象成不同层级的结构表示，再进行结构映射对齐，从而提升叙事类类比推理表现。

**研究动机**：传统结构映射方法往往假设实体与关系已被预先抽取，难直接用于原始叙事文本；而端到端LLM类比推理对提示格式和表层相似度敏感，导致跨故事结构类比不稳定。

**核心方法**：YARN采用模块化流程：用LLM将故事分解为叙事单元并生成抽象表示（定义并实现四种抽象层级，兼顾单元语义与叙事角色，借鉴framing理论），再将这些抽象输入映射组件，对齐两则故事元素以完成类比推理。

**主要结论**：实验表明，引入LLM生成的抽象能稳定提升结构映射/类比推理性能，达到或超过端到端LLM基线；误差分析显示挑战主要在于选取合适抽象粒度、建模隐含因果关系，以及叙事类比模式的系统化归类。

**关键词**：类比推理, 叙事结构类比, 结构映射, 叙事单元分解, 多层次抽象, 角色与框架语义, 跨故事对齐, 模块化推理框架, 隐式因果建模

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29997v1) | [下载PDF](https://arxiv.org/pdf/2603.29997v1.pdf)

---

## [7. Rewrite the News: Tracing Editorial Reuse Across News Agencies](https://arxiv.org/abs/2603.29937v1)

**作者**：Soveatin Kuntur, Nina Smirnova, Anna Wroblewska 等 5 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-03-31

### 📄 论文摘要

This paper investigates sentence-level text reuse in multilingual journalism, analyzing where reused content occurs within articles. We present a weakly supervised method for detecting sentence-level cross-lingual reuse without requiring full translations, designed to support automated pre-selection to reduce information overload for journalists (Holyst et al., 2024). The study compares English-language articles from the Slovenian Press Agency (STA) with reports from 15 foreign agencies (FA) in seven languages, using publication timestamps to retain the earliest likely foreign source for each reused sentence. We analyze 1,037 STA and 237,551 FA articles from two time windows (October 7-November 2, 2023; February 1-28, 2025) and identify 1,087 aligned sentence pairs after filtering to the earliest sources. Reuse occurs in 52% of STA articles and 1.6% of FA articles and is predominantly non-literal, involving paraphrase and compositional reuse from multiple sources. Reused content tends to appear in the middle and end of English articles, while leads are more often original, indicating that simple lexical matching overlooks substantial editorial reuse. Compared with prior work focused on monolingual overlap, we (i) detect reuse across languages without requiring full translation, (ii) use publication timing to identify likely sources, and (iii) analyze where reused material is situated within articles. Dataset and code: https://github.com/kunturs/lrec2026-rewrite-news.

### 🤖 AI 总结

**一句话总结**：论文提出一种弱监督的跨语言句子级复用检测方法，并发现新闻机构间大量复用以释义/组合改写为主且多出现在文章中后段而非导语。

**研究动机**：跨语言新闻编辑中存在大量隐性的句子复用，但传统依赖字面匹配或完整翻译的做法难以覆盖改写与信息重组，且会给记者带来信息过载。作者希望在不做全文翻译的前提下，自动预筛出可能复用的内容以辅助溯源与编辑分析。

**核心方法**：将STA英文稿与15家外媒（7种语言）报道进行弱监督句子对齐，检测跨语言复用且不要求完整翻译；再结合发布时间戳，为每个复用句保留最早出现的外媒作为“可能来源”，并统计复用句在文章位置分布。

**主要结论**：在两段时间窗中，复用出现在52%的STA文章中但仅占外媒文章的1.6%，且以非字面复用（释义、从多源组合）为主；复用内容更常位于英文文章的中段与结尾，导语更偏原创，说明仅靠词汇重合会显著低估编辑复用。

**关键词**：句子级对齐, 弱监督方法, 多语新闻写作, 时间戳溯源, 新闻机构来源识别, 文章结构位置分析, Rewrite, News

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29937v1) | [下载PDF](https://arxiv.org/pdf/2603.29937v1.pdf)

---

## cs.CV

## [8. OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation](https://arxiv.org/abs/2603.30045v1)

**作者**：Yuheng Liu, Xin Lin, Xinke Li 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Modeling scenes using video generation models has garnered growing research interest in recent years. However, most existing approaches rely on perspective video models that synthesize only limited observations of a scene, leading to issues of completeness and global consistency. We propose OmniRoam, a controllable panoramic video generation framework that exploits the rich per-frame scene coverage and inherent long-term spatial and temporal consistency of panoramic representation, enabling long-horizon scene wandering. Our framework begins with a preview stage, where a trajectory-controlled video generation model creates a quick overview of the scene from a given input image or video. Then, in the refine stage, this video is temporally extended and spatially upsampled to produce long-range, high-resolution videos, thus enabling high-fidelity world wandering. To train our model, we introduce two panoramic video datasets that incorporate both synthetic and real-world captured videos. Experiments show that our framework consistently outperforms state-of-the-art methods in terms of visual quality, controllability, and long-term scene consistency, both qualitatively and quantitatively. We further showcase several extensions of this framework, including real-time video generation and 3D reconstruction. Code is available at https://github.com/yuhengliu02/OmniRoam.

### 🤖 AI 总结

**一句话总结**：OmniRoam 提出一种可控的全景长视频生成框架，利用全景表示的全局覆盖与时空一致性，实现从单张图像/短视频出发的长时程“世界漫游”生成。

**研究动机**：现有多以透视视角视频模型为主，只能看到场景的局部观察，容易导致场景不完整、长期生成时的全局一致性差。全景视频天然覆盖更广且更利于保持空间与时间一致性，因此适合支撑长视野、长时程的场景探索与漫游。

**核心方法**：框架分两阶段：先在 preview 阶段用“轨迹可控”的生成模型快速合成场景概览；再在 refine 阶段对视频进行时间延展与空间超分辨率上采样，产出长距离高分辨率全景视频。训练上引入两个包含合成与真实采集的全景视频数据集，以提升可控性与长期一致性。

**主要结论**：实验表明 OmniRoam 在画质、可控性与长程场景一致性方面稳定优于现有方法，并展示了实时生成与 3D 重建等扩展能力，说明全景表示能有效支撑高保真长时程世界漫游生成。

**关键词**：全景视频生成, 长时域视频生成, 场景漫游, 轨迹可控生成, 全局一致性, 时空一致性, 两阶段生成, 时序扩展, 空间超分辨率, 全景视频数据集, 三维重建

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30045v1) | [下载PDF](https://arxiv.org/pdf/2603.30045v1.pdf)

---

## [9. Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)

**作者**：Kaleb Newman, Tyler Zhu, Olga Russakovsky  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Video diffusion models exhibit emergent reasoning capabilities like solving mazes and puzzles, yet little is understood about how they reason during generation. We take a first step towards understanding this and study the internal planning dynamics of video models using 2D maze solving as a controlled testbed. Our investigations reveal two findings. Our first finding is early plan commitment: video diffusion models commit to a high-level motion plan within the first few denoising steps, after which further denoising alters visual details but not the underlying trajectory. Our second finding is that path length, not obstacle density, is the dominant predictor of maze difficulty, with a sharp failure threshold at 12 steps. This means video models can only reason over long mazes by chaining together multiple sequential generations. To demonstrate the practical benefits of our findings, we introduce Chaining with Early Planning, or ChEaP, which only spends compute on seeds with promising early plans and chains them together to tackle complex mazes. This improves accuracy from 7% to 67% on long-horizon mazes and by 2.5x overall on hard tasks in Frozen Lake and VR-Bench across Wan2.2-14B and HunyuanVideo-1.5. Our analysis reveals that current video models possess deeper reasoning capabilities than previously recognized, which can be elicited more reliably with better inference-time scaling.

### 🤖 AI 总结

**一句话总结**：论文发现视频扩散模型在生成早期就会“承诺”一条高层运动路径规划，并可通过利用这一早期规划信号（ChEaP）显著提升长时程迷宫求解成功率。

**研究动机**：尽管视频扩散模型展现出解迷宫等“涌现推理”能力，但其在生成过程中的内部规划何时形成、如何影响成败仍不清楚；作者用2D迷宫作为可控环境来刻画这种推理动态。

**核心方法**：在2D迷宫基准上分析不同去噪步的轨迹变化，检验是否存在早期路径规划锁定，并系统比较影响难度的因素（路径长度 vs 障碍密度）；据此提出ChEaP：只对早期计划看起来有希望的随机种子继续投入计算，并将多段短规划的连续生成进行链式拼接以解决长迷宫。

**主要结论**：视频扩散模型通常在最初少数去噪步就确定高层运动计划，后续去噪主要细化视觉细节而不改变轨迹；迷宫难度主要由路径长度决定且在约12步出现明显失败阈值，利用早期规划筛选与链式生成可将长时程任务准确率从7%提升到67%，并在多个基准与模型上带来约2.5倍提升。

**关键词**：视频扩散模型, 迷宫求解, 早期计划承诺, 去噪步规划, 运动轨迹规划, 路径长度阈值, 长时序推理, 串联生成, 早期规划筛选, 推理时计算扩展

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30043v1) | [下载PDF](https://arxiv.org/pdf/2603.30043v1.pdf)

---

## [10. Benchmarking PhD-Level Coding in 3D Geometric Computer Vision](https://arxiv.org/abs/2603.30038v1)

**作者**：Wenyi Li, Renkai Luo, Yue Yu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

AI-assisted coding has rapidly reshaped software practice and research workflows, yet today's models still struggle to produce correct code for complex 3D geometric vision. If models could reliably write such code, the research of our community would change substantially. To measure progress toward that goal, we introduce GeoCodeBench, a PhD-level benchmark that evaluates coding for 3D vision. Each problem is a fill-in-the-function implementation task curated from representative papers at recent venues: we first let a tool propose candidate functions from official repositories, then perform careful human screening to select core 3D geometric components. For every target, we generate diverse, edge-case unit tests, enabling fully automatic, reproducible scoring. We evaluate eight representative open- and closed-source models to reflect the current ecosystem. The best model, GPT-5, attains only 36.6% pass rate, revealing a large gap between current capabilities and dependable 3D scientific coding. GeoCodeBench organizes tasks into a two-level hierarchy: General 3D capability (geometric transformations and mechanics/optics formulation) and Research capability (novel algorithm implementation and geometric logic routing). Scores are positively correlated across these axes, but research-oriented tasks are markedly harder. Context ablations further show that "more paper text" is not always better: cutting off at the Method section statistically outperforms full-paper inputs, highlighting unresolved challenges in long-context scientific comprehension. Together, these findings position GeoCodeBench as a rigorous testbed for advancing from generic coding to trustworthy 3D geometric vision coding.

### 🤖 AI 总结

**一句话总结**：论文提出并发布GeoCodeBench，用自动化单元测试评测大模型在3D几何计算机视觉“科研级”代码实现上的真实能力，结果显示当前最强模型通过率也仅36.6%。

**研究动机**：尽管AI辅助编程普及，但模型在复杂且高精度要求的3D几何视觉代码上仍常出错，缺少能客观衡量“是否能写对科研代码”的基准来追踪进展与差距。

**核心方法**：从近期代表性论文的官方代码库中由工具提名候选函数，再经人工筛选确定核心3D几何组件，形成“填空式函数实现”任务，并为每题构造覆盖边界条件的多样化单元测试以支持全自动、可复现评分；同时按“通用3D能力/研究能力”两级层次组织任务，并对8个开闭源模型及不同论文上下文截断策略进行对比评测。

**主要结论**：现有模型在3D几何视觉科研编码上与“可靠可用”仍有显著差距（最佳仅36.6%通过率），且研究型任务明显更难但与通用能力得分正相关；此外长上下文并不总是提升效果，截断到Method部分反而统计显著优于全文输入，暴露了长上下文科学理解的未解问题。

**关键词**：3D几何视觉编码, 代码生成基准, 函数补全任务, 单元测试生成, 自动化可复现评分, 几何变换, 新算法实现, 长上下文消融

**评分**：81

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30038v1) | [下载PDF](https://arxiv.org/pdf/2603.30038v1.pdf)

---

## [11. Conditional Polarization Guidance for Camouflaged Object Detection](https://arxiv.org/abs/2603.30008v1)

**作者**：QIfan Zhang, Hao Wang, Xiangrong Qin 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Camouflaged object detection (COD) aims to identify targets that are highly blended with their backgrounds. Recent works have shown that the optical characteristics of polarization cues play a significant role in improving camouflaged object detection. However, most existing polarization-based approaches depend on complex visual encoders and fusion mechanisms, leading to increased model complexity and computational overhead, while failing to fully explore how polarization can explicitly guide hierarchical RGB representation learning. To address these limitations, we propose CPGNet, an asymmetric RGB-polarization framework that introduces a conditional polarization guidance mechanism to explicitly regulate RGB feature learning for camouflaged object detection. Specifically, we design a lightweight polarization interaction module that jointly models these complementary cues and generates reliable polarization guidance in a unified manner. Unlike conventional feature fusion strategies, the proposed conditional guidance mechanism dynamically modulates RGB features using polarization priors, enabling the network to focus on subtle discrepancies between camouflaged objects and their backgrounds. Furthermore, we introduce a polarization edge-guided frequency refinement strategy that enhances high-frequency components under polarization constraints, effectively breaking camouflage patterns. Finally, we develop an iterative feedback decoder to perform coarse-to-fine feature calibration and progressively refine camouflage prediction. Extensive experiments on polarization datasets across multiple tasks, along with evaluations on non-polarization datasets, demonstrate that CPGNet consistently outperforms state-of-the-art methods.

### 🤖 AI 总结

**一句话总结**：提出CPGNet，通过条件极化引导机制显式调控RGB分层特征学习，以更有效地检测与背景高度融合的伪装目标。

**研究动机**：现有基于极化线索的COD方法往往依赖复杂编码器与融合结构，带来较高计算开销与模型复杂度。与此同时，它们未充分挖掘“极化信息如何作为先验显式指导RGB特征学习”，从而限制了对细微差异的捕获能力。

**核心方法**：构建非对称RGB-极化框架CPGNet：用轻量极化交互模块联合建模互补线索并生成可靠的极化指导，再以条件引导方式动态调制RGB特征而非简单融合。结合极化边缘引导的频域细化增强高频细节以破除伪装纹理，并通过迭代反馈解码器进行由粗到细的特征校准与预测逐步精炼。

**主要结论**：在多种极化数据集任务以及非极化数据集评测中，CPGNet均持续优于现有SOTA方法，说明条件极化指导与频域/迭代精炼策略能有效提升伪装目标与背景的可分性并改善检测性能。

**关键词**：伪装目标检测, 偏振线索, 条件偏振引导, RGB-偏振框架, 特征动态调制, 偏振交互模块, 边缘引导频域细化, 高频增强, 迭代反馈解码器, 粗到细预测细化, 层次RGB表征学习

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30008v1) | [下载PDF](https://arxiv.org/pdf/2603.30008v1.pdf)

---

## [12. SurgNavAR: An Augmented Reality Surgical Navigation Framework for Optical See-Through Head Mounted Displays](https://arxiv.org/abs/2603.29990v1)

**作者**：Abdullah Thabit, Mohamed Benmahdjoub, Rafiuddin Jinabade 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Augmented reality (AR) devices with head mounted displays (HMDs) facilitate the direct superimposition of 3D preoperative imaging data onto the patient during surgery. To use an HMD-AR device as a stand-alone surgical navigation system, the device should be able to locate the patient and surgical instruments, align preoperative imaging data with the patient, and visualize navigation data in real time during surgery. Whereas some of the technologies required for this are known, integration in such devices is cumbersome and requires specific knowledge and expertise, hampering scientific progress in this field. This work therefore aims to present and evaluate an integrated HMD-based AR surgical navigation framework that is adaptable to diverse surgical applications. The framework tracks 2D patterns as reference markers attached to the patient and surgical instruments. It allows for the calibration of surgical tools using pivot and reference-based calibration techniques. It enables image-to-patient registration using point-based matching and manual positioning. The integrated functionalities of the framework are evaluated on two HMD devices, the HoloLens 2 and Magic Leap 2, with two surgical use cases being evaluated in a phantom setup: AR-guided needle insertion and rib fracture localization. The framework was able to achieve a mean tooltip calibration accuracy of 1 mm, a registration accuracy of 3 mm, and a targeting accuracy below 5 mm on the two surgical use cases. The framework presents an easy-to-use configurable tool for HMD-based AR surgical navigation, which can be extended and adapted to many surgical applications. The framework is publicly available at https://github.com/abdullahthabit/SurgNavAR.

### 🤖 AI 总结

**一句话总结**：提出并评估了一个面向光学透视式头显（HoloLens 2、Magic Leap 2）的增强现实手术导航框架SurgNavAR，可实现患者/器械跟踪、配准与实时导航显示，并在仿体实验中达到毫米级精度。

**研究动机**：现有HMD-AR手术导航所需的跟踪、工具标定、影像-患者配准与可视化等技术虽已存在，但在头显设备上集成复杂、门槛高，阻碍了研究与应用扩展。

**核心方法**：框架采用2D图案标记（marker）对患者与手术器械进行跟踪，提供枢轴（pivot）与基于参考的器械标定，并支持点匹配与手动定位的影像到患者配准；在两类用例（AR引导穿刺、肋骨骨折定位）的仿体环境中于两款头显上进行端到端评测。

**主要结论**：SurgNavAR在实验中实现平均1 mm的器械尖端标定精度、约3 mm的配准精度和低于5 mm的目标定位误差，证明其可作为易用、可配置且可扩展的HMD独立AR手术导航方案，并已开源以便进一步适配多种手术场景。

**关键词**：增强现实手术导航, 光学透视式头显, 2D标记追踪, 术中器械追踪, 工具尖端标定, 枢轴标定, 参考标定, 图像-患者配准, 点配准, 实时导航可视化, AR引导穿刺, 肋骨骨折定位

**评分**：74

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29990v1) | [下载PDF](https://arxiv.org/pdf/2603.29990v1.pdf)

---

## [13. Trimodal Deep Learning for Glioma Survival Prediction: A Feasibility Study Integrating Histopathology, Gene Expression, and MRI](https://arxiv.org/abs/2603.29968v1)

**作者**：Iain Swift, JingHua Ye  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

Multimodal deep learning has improved prognostic accuracy for brain tumours by integrating histopathology and genomic data, yet the contribution of volumetric MRI within unified survival frameworks remains unexplored. This pilot study extends a bimodal framework by incorporating Fluid Attenuated Inversion Recovery (FLAIR) MRI from BraTS2021 as a third modality. Using the TCGA-GBMLGG cohort (664 patients), we evaluate three unimodal models, nine bimodal configurations, and three trimodal configurations across early, late, and joint fusion strategies. In this small cohort setting, trimodal early fusion achieves an exploratory Composite Score (CS = 0.854), with a controlled $Δ$CS of +0.011 over the bimodal baseline on identical patients, though this difference is not statistically significant (p = 0.250, permutation test). MRI achieves reasonable unimodal discrimination (CS = 0.755) but does not substantially improve bimodal pairs, while providing measurable uplift in the three-way combination. All MRI containing experiments are constrained to 19 test patients, yielding wide bootstrap confidence intervals (e.g. [0.400,1.000]) that preclude definitive conclusions. These findings provide preliminary evidence that a third imaging modality may add prognostic value even with limited sample sizes, and that additional modalities require sufficient multimodal context to contribute effectively.

### 🤖 AI 总结

**一句话总结**：该研究探索将病理切片、基因表达与FLAIR MRI三模态深度学习联合用于胶质瘤生存预测，三模态早期融合在小样本下取得略高于双模态的综合表现但统计上不显著。

**研究动机**：现有多模态预后模型多聚焦病理与基因组信息，MRI体积影像在统一生存预测框架中的增益尚不清楚；作者希望验证加入FLAIR MRI作为第三模态是否能提升预后预测能力。

**核心方法**：基于TCGA-GBMLGG队列构建单模态、双模态与三模态模型，并比较早期/晚期/联合等多种融合策略；MRI来自BraTS2021的FLAIR子集，使用Composite Score评估并通过置换检验与bootstrap置信区间评估差异与不确定性。

**主要结论**：三模态早期融合获得探索性最佳CS=0.854，相比相同患者的双模态基线提升ΔCS=+0.011但不显著(p=0.250)；MRI单模态区分度尚可(CS=0.755)，对双模态组合提升有限，但在三模态组合中有可测增益，不过受限于仅19名测试患者导致置信区间很宽，结论需更大样本验证。

**关键词**：胶质瘤生存预测, 多模态深度学习, 三模态融合, 早期融合, 晚期融合, 联合融合, 组织病理图像, 基因表达, 生存分析

**评分**：61

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29968v1) | [下载PDF](https://arxiv.org/pdf/2603.29968v1.pdf)

---

## [14. Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight](https://arxiv.org/abs/2603.29967v1)

**作者**：Badhan Mazumder, Sir-Lord Wiafe, Aline Kotoski 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Understanding how brain structure and function interact is key to explaining intelligence yet modeling them jointly is challenging as the structural and functional connectome capture complementary aspects of organization. We introduced Multi-scale Adaptive Graph Network (MAGNet), a Transformer-style graph neural network framework that adaptively learns structure-function interactions. MAGNet leverages source-based morphometry from structural MRI to extract inter-regional morphological features and fuses them with functional network connectivity from resting-state fMRI. A hybrid graph integrates direct and indirect pathways, while local-global attention refines connectivity importance and a joint loss simultaneously enforces cross-modal coherence and optimizes the prediction objective end-to-end. On the ABCD dataset, MAGNet outperformed relevant baselines, demonstrating effective multimodal integration for advancing our understanding of cognitive function.

### 🤖 AI 总结

**一句话总结**：Understanding how brain structure and function interact is key to explaining intelligence yet modeling them jointly is challenging as the structural and functional connectome capture complementary asp...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：结构-功能耦合, 脑连接组, 多模态脑影像融合, 结构MRI形态特征, 静息态fMRI功能连接, 图注意力网络, 多尺度自适应图, 局部-全局注意力, 混合图建模, 跨模态一致性损失, 认知能力预测

**评分**：58

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29967v1) | [下载PDF](https://arxiv.org/pdf/2603.29967v1.pdf)

---

## [15. Scaling Video Pretraining for Surgical Foundation Models](https://arxiv.org/abs/2603.29966v1)

**作者**：Sicheng Lu, Zikai Xiao, Jianhui Wei 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Surgical video understanding is essential for computer-assisted interventions, yet existing surgical foundation models remain constrained by limited data scale, procedural diversity, and inconsistent evaluation, often lacking a reproducible training pipeline. We propose SurgRec, a scalable and reproducible pretraining recipe for surgical video understanding, instantiated with two variants: SurgRec-MAE and SurgRec-JEPA. We curate a large multi-source corpus of 10,535 videos and 214.5M frames spanning endoscopy, laparoscopy, cataract, and robotic surgery. Building on this corpus, we develop a unified pretraining pipeline with balanced sampling and standardize a reproducible benchmark across 16 downstream datasets and four clinical domains with consistent data splits. Across extensive comparisons against SSL baselines and vision-language models, SurgRec consistently achieves superior performance across downstream datasets. In contrast, VLMs prove unreliable for fine-grained temporal recognition, exhibiting both performance gaps and sensitivity to prompt phrasing. Our work provides a reproducible, scalable foundation for the community to build more general surgical video models. All code, models, and data will be publicly released.

### 🤖 AI 总结

**一句话总结**：提出SurgRec可扩展且可复现的手术视频自监督预训练方案，并在多临床域下游任务上系统性优于现有SSL与部分视觉语言模型。

**研究动机**：现有手术领域基础模型受限于数据规模与手术流程多样性不足、评测不一致且训练流程难复现，导致泛化能力与可比较性较弱。作者希望建立可规模化的数据与统一基准，推动更通用的手术视频理解模型。

**核心方法**：构建覆盖内镜/腹腔镜/白内障/机器人手术的多源大规模语料（10,535段视频、2.145亿帧），并设计统一预训练流水线（含平衡采样）与可复现的下游评测基准（16个数据集、统一划分）。在该配方下实例化两种预训练变体SurgRec-MAE与SurgRec-JEPA，并与SSL基线及VLM进行对比。

**主要结论**：SurgRec在16个下游数据集与四个临床域上整体表现更优且更稳定；相较之下，VLM在细粒度时序识别上不可靠，存在性能差距且对提示词措辞敏感。工作同时提供标准化、可复现的训练与评测框架，并承诺公开代码、模型与数据以促进社区研究。

**关键词**：视频基础模型, 自监督预训练, 掩码自编码器, 多源手术视频语料, 平衡采样, 可复现训练管线, 下游基准评测, 时序动作识别, 视觉语言模型对比

**评分**：69

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29966v1) | [下载PDF](https://arxiv.org/pdf/2603.29966v1.pdf)

---

## [16. NeuroBRIDGE: Behavior-Conditioned Koopman Dynamics with Riemannian Alignment for Early Substance Use Initiation Prediction from Longitudinal Functional Connectome](https://arxiv.org/abs/2603.29960v1)

**作者**：Badhan Mazumder, Sir-Lord Wiafe, Vince D. Calhoun 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Early identification of adolescents at risk for substance use initiation (SUI) is vital yet difficult, as most predictors treat connectivity as static or cross-sectional and miss how brain networks change over time and with behavior. We proposed NeuroBRIDGE (Behavior conditioned RIemannian Koopman Dynamics on lonGitudinal connEctomes), a novel graph neural network-based framework that aligns longitudinal functional connectome in a Riemannian tangent space and couples dual-time attention with behavioral-conditioned Koopman dynamics to capture temporal change. Evaluated on ABCD, NeuroBRIDGE improved future SUI prediction over relevant baselines while offering interpretable insights into neural pathways, refining our understanding of neurodevelopmental risk and informing targeted prevention.

### 🤖 AI 总结

**一句话总结**：NeuroBRIDGE 通过在黎曼切空间对齐纵向功能连接组并引入行为条件的 Koopman 动力学建模，提升了对青少年未来物质使用启动（SUI）的早期预测能力并提供可解释的神经通路线索。

**研究动机**：现有 SUI 风险预测多将脑连接视为静态或仅用横断面数据，难以捕捉随发育与行为变化的网络动态，从而限制了早期识别与干预的准确性与可解释性。

**核心方法**：提出基于图神经网络的 NeuroBRIDGE：先将纵向功能连接组映射到黎曼流形的切空间进行对齐，再结合“双时间尺度注意力”与“行为条件的 Koopman 动力学”来刻画跨时间的可线性化潜在演化并用于预测。

**主要结论**：在 ABCD 数据集上，NeuroBRIDGE 相比相关基线取得更好的未来 SUI 预测表现，同时能揭示与风险相关的关键脑网络/通路变化，为理解神经发育风险机制与制定靶向预防提供支持。

**关键词**：青少年风险预测, 纵向功能连接组, 脑网络时序建模, 图神经网络, 黎曼切空间对齐, 行为条件建模, 双时间注意力, 可解释神经通路

**评分**：76

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29960v1) | [下载PDF](https://arxiv.org/pdf/2603.29960v1.pdf)

---

## [17. Detecting Unknown Objects via Energy-based Separation for Open World Object Detection](https://arxiv.org/abs/2603.29954v1)

**作者**：Jun-Woo Heo, Keonhee Park, Gyeong-Moon Park  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

In this work, we tackle the problem of Open World Object Detection (OWOD). This challenging scenario requires the detector to incrementally learn to classify known objects without forgetting while identifying unknown objects without supervision. Previous OWOD methods have enhanced the unknown discovery process and employed memory replay to mitigate catastrophic forgetting. However, since existing methods heavily rely on the detector's known class predictions for detecting unknown objects, they struggle to effectively learn and recognize unknown object representations. Moreover, while memory replay mitigates forgetting of old classes, it often sacrifices the knowledge of newly learned classes. To resolve these limitations, we propose DEUS (Detecting Unknowns via energy-based Separation), a novel framework that addresses the challenges of Open World Object Detection. DEUS consists of Equiangular Tight Frame (ETF)-Subspace Unknown Separation (EUS) and an Energy-based Known Distinction (EKD) loss. EUS leverages ETF-based geometric properties to create orthogonal subspaces, enabling cleaner separation between known and unknown object representations. Unlike prior energy-based approaches that consider only the known space, EUS utilizes energies from both spaces to better capture distinct patterns of unknown objects. Furthermore, EKD loss enforces the separation between previous and current classifiers, thus minimizing knowledge interference between previous and newly learned classes during memory replay. We thoroughly validate DEUS on OWOD benchmarks, demonstrating outstanding performance improvements in unknown detection while maintaining competitive known class performance.

### 🤖 AI 总结

**一句话总结**：提出DEUS框架，通过能量分离与子空间正交化提升开放世界目标检测中“未知目标”发现能力，并兼顾增量学习的已知类性能。

**研究动机**：现有OWOD方法过度依赖已知类预测来推断未知，导致未知表征学习不足；同时记忆回放虽缓解旧类遗忘，却容易干扰新学类知识、牺牲新类性能。

**核心方法**：DEUS包含两部分：EUS利用等角紧框架(ETF)构造正交子空间，并同时利用已知/未知空间的能量来更干净地区分未知表征；EKD损失约束历史与当前分类器分离，降低回放训练中旧类与新类的知识互相干扰。

**主要结论**：在OWOD基准上，DEUS显著提升未知目标检测效果，同时保持与现有方法具有竞争力的已知类检测/分类表现，并更好地平衡旧类记忆与新类学习。

**关键词**：开放世界目标检测, 未知目标检测, 增量学习, 灾难性遗忘, 记忆回放, 能量模型, 能量分离, ETF 子空间, 子空间分离, 分类器去干扰, 能量损失

**评分**：64

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29954v1) | [下载PDF](https://arxiv.org/pdf/2603.29954v1.pdf)

---

## [18. EC-Bench: Enumeration and Counting Benchmark for Ultra-Long Videos](https://arxiv.org/abs/2603.29943v1)

**作者**：Fumihiko Tsuchiya, Taiki Miyanishi, Mahiro Ukai 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Counting in long videos remains a fundamental yet underexplored challenge in computer vision. Real-world recordings often span tens of minutes or longer and contain sparse, diverse events, making long-range temporal reasoning particularly difficult. However, most existing video counting benchmarks focus on short clips and evaluate only the final numerical answer, providing little insight into what should be counted or whether models consistently identify relevant instances across time. We introduce EC-Bench, a benchmark that jointly evaluates enumeration, counting, and temporal evidence grounding in long-form videos. EC-Bench contains 152 videos longer than 30 minutes and 1,699 queries paired with explicit evidence spans. Across 22 multimodal large language models (MLLMs), the best model achieves only 29.98% accuracy on Enumeration and 23.74% on Counting, while human performance reaches 78.57% and 82.97%, respectively. Our analysis reveals strong relationships between enumeration accuracy, temporal grounding, and counting performance. These results highlight fundamental limitations of current MLLMs and establish EC-Bench as a challenging benchmark for long-form quantitative video reasoning.

### 🤖 AI 总结

**一句话总结**：EC-Bench 提出一个针对30分钟以上超长视频的“枚举-计数-证据定位”综合基准，揭示当前多模态大模型在长程定量推理上与人类存在显著差距。

**研究动机**：现有视频计数数据集多为短片段且只评估最终数字，无法诊断模型是否在长视频中持续、准确地识别并对齐应被计数的事件实例。真实世界长视频事件稀疏且多样，迫切需要能评估长程时序推理与可解释证据的基准。

**核心方法**：构建 EC-Bench：包含152个≥30分钟视频与1,699个查询，并为每个查询标注明确的时间证据片段，联合评测枚举（列出实例）、计数（给出数量）与时间证据落地（grounding）。在22个MLLM上进行系统评测，并分析枚举准确率、证据定位质量与计数表现之间的关系。

**主要结论**：最优模型在枚举与计数上仅达29.98%与23.74%，显著低于人类的78.57%与82.97%，表明现有MLLM在超长视频的稳定实例识别与长程推理上存在根本局限。实验还发现枚举准确、时间证据对齐与计数性能强相关，说明提升可验证的时序定位与实例一致性是改进长视频计数的关键。

**关键词**：超长视频, 视频计数, 事件枚举, 时间证据定位, 长程时序推理, 视频问答, 多模态大模型, 计数基准测试, 稀疏事件检测

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29943v1) | [下载PDF](https://arxiv.org/pdf/2603.29943v1.pdf)

---

## [19. Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance](https://arxiv.org/abs/2603.29941v1)

**作者**：Vanessa Emanuela Guarino, Claudia Winklmayr, Jannik Franzen 等 10 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-03-31

### 📄 论文摘要

Uncertainty Quantification (UQ) is crucial for ensuring the reliability of automated image segmentations in safety-critical domains like biomedical image analysis or autonomous driving. In segmentation, UQ generates pixel-wise uncertainty scores that must be aggregated into image-level scores for downstream tasks like Out-of-Distribution (OoD) or failure detection. Despite routine use of aggregation strategies, their properties and impact on downstream task performance have not yet been comprehensively studied. Global Average is the default choice, yet it does not account for spatial and structural features of segmentation uncertainty. Alternatives like patch-, class- and threshold-based strategies exist, but lack systematic comparison, leading to inconsistent reporting and unclear best practices. We address this gap by (1) formally analyzing properties, limitations, and pitfalls of common strategies; (2) proposing novel strategies that incorporate spatial uncertainty structure and (3) benchmarking their performance on OoD and failure detection across ten datasets that vary in image geometry and structure. We find that aggregators leveraging spatial structure yield stronger performance in both downstream tasks studied. However, the performance of individual aggregators depends heavily on dataset characteristics, so we (4) propose a meta-aggregator that integrates multiple aggregators and performs robustly across datasets.

### 🤖 AI 总结

**一句话总结**：Uncertainty Quantification (UQ) is crucial for ensuring the reliability of automated image segmentations in safety-critical domains like biomedical image analysis or autonomous driving. In segmentatio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：分割不确定性, 不确定性量化, 像素级不确定性, 图像级聚合, 空间感知聚合, 结构化不确定性, 分布外检测, 失败检测, 不确定性聚合策略, 元聚合器, 跨数据集基准评测

**评分**：65

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29941v1) | [下载PDF](https://arxiv.org/pdf/2603.29941v1.pdf)

---

## [20. Gloria: Consistent Character Video Generation via Content Anchors](https://arxiv.org/abs/2603.29931v1)

**作者**：Yuhang Yang, Fan Zhang, Huaijin Pi 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Digital characters are central to modern media, yet generating character videos with long-duration, consistent multi-view appearance and expressive identity remains challenging. Existing approaches either provide insufficient context to preserve identity or leverage non-character-centric information as the memory, leading to suboptimal consistency. Recognizing that character video generation inherently resembles an outside-looking-in scenario. In this work, we propose representing the character visual attributes through a compact set of anchor frames. This design provides stable references for consistency, while reference-based video generation inherently faces challenges of copy-pasting and multi-reference conflicts. To address these, we introduce two mechanisms: Superset Content Anchoring, providing intra- and extra-training clip cues to prevent duplication, and RoPE as Weak Condition, encoding positional offsets to distinguish multiple anchors. Furthermore, we construct a scalable pipeline to extract these anchors from massive videos. Experiments show our method generates high-quality character videos exceeding 10 minutes, and achieves expressive identity and appearance consistency across views, surpassing existing methods.

### 🤖 AI 总结

**一句话总结**：提出以少量“内容锚帧”（anchor frames）作为角色外观记忆的参考式视频生成框架，实现超长时长（10分钟以上）且多视角一致的角色视频生成。

**研究动机**：现有角色视频生成方法要么上下文不足导致身份/外观漂移，要么依赖非角色中心的信息作为记忆而一致性不佳，尤其在长视频和多视角下更明显。参考图/帧条件生成还常出现“复制粘贴”伪影与多参考冲突，限制了稳定可控的角色表现。

**核心方法**：将角色视觉属性压缩为一组锚帧作为稳定参照，并提出Superset Content Anchoring（引入片内与片外的训练线索以抑制重复拷贝、增强一致性）与“RoPE as Weak Condition”（用相对位置编码区分多个锚帧、缓解多参考冲突）。同时构建可扩展的自动化管线，从海量视频中提取并整理这些锚帧以支持大规模训练/推理。

**主要结论**：实验表明该方法可生成高质量、时长超过10分钟的角色视频，并在多视角与表情/动作变化下保持更强的身份与外观一致性，整体效果优于现有方法。

**关键词**：角色视频生成, 长时序一致性, 多视角外观一致性, 身份保持, 参考驱动生成, 锚点帧, 内容锚定, 位置偏移编码, 大规模锚点提取管线

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29931v1) | [下载PDF](https://arxiv.org/pdf/2603.29931v1.pdf)

---

## [21. End-to-End Image Compression with Segmentation Guided Dual Coding for Wind Turbines](https://arxiv.org/abs/2603.29927v1)

**作者**：Raül Pérez-Gonzalo, Andreas Espersen, Søren Forchhammer 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-03-31

### 📄 论文摘要

Transferring large volumes of high-resolution images during wind turbine inspections introduces a bottleneck in assessing and detecting severe defects. Efficient coding must preserve high fidelity in blade regions while aggressively compressing the background. In this work, we propose an end-to-end deep learning framework that jointly performs segmentation and dual-mode (lossy and lossless) compression. The segmentation module accurately identifies the blade region, after which our region-of-interest (ROI) compressor encodes it at superior quality compared to the rest of the image. Unlike conventional ROI schemes that merely allocate more bits to salient areas, our framework integrates: (i) a robust segmentation network (BU-Netv2+P) with a CRF-regularized loss for precise blade localization, (ii) a hyperprior-based autoencoder optimized for lossy compression, and (iii) an extended bits-back coder with hierarchical models for fully lossless blade reconstruction. Furthermore, our ROI framework removes the sequential dependency in bits-back coding by reusing background-coded bits, enabling parallelized and efficient dual-mode compression. To the best of our knowledge, this is the first fully integrated learning-based ROI codec combining segmentation, lossy, and lossless compression, ensuring that subsequent defect detection is not compromised. Experiments on a large-scale wind turbine dataset demonstrate superior compression performance and efficiency, offering a practical solution for automated inspections.

### 🤖 AI 总结

**一句话总结**：提出一种端到端的分割引导双编码框架，对风机叶片区域进行高保真（可无损）压缩、对背景进行更强有损压缩，以在降低传输成本的同时不影响缺陷检测。

**研究动机**：风机巡检会产生大量高分辨率图像，传输与存储成为瓶颈；同时缺陷主要出现在叶片区域，要求该区域尽可能高保真而背景可更激进压缩。

**核心方法**：先用带CRF正则损失的分割网络（BU-Netv2+P）精确定位叶片ROI，再对背景采用超先验（hyperprior）自编码器进行有损压缩、对叶片采用扩展bits-back与分层模型实现可并行的无损重建，并通过复用背景编码比特消除bits-back的顺序依赖以提升效率。

**主要结论**：在大规模风机数据集上，该集成式ROI编解码器在压缩率与效率上优于对比方法，并能保证叶片区域的高保真（甚至无损）重建，从而更适用于后续自动缺陷检测与巡检流程。

**关键词**：风机叶片巡检, ROI 图像压缩, 端到端压缩, 分割引导编码, 双模式编码, 有损压缩, 无损压缩, 超先验自编码器, 层次概率模型, CRF 正则化损失

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29927v1) | [下载PDF](https://arxiv.org/pdf/2603.29927v1.pdf)

---

## [22. Abstraction in Style](https://arxiv.org/abs/2603.29924v1)

**作者**：Min Lu, Yuanfeng He, Anthony Chen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-03-31

### 📄 论文摘要

Artistic styles often embed abstraction beyond surface appearance, involving deliberate reinterpretation of structure rather than mere changes in texture or color. Conventional style transfer methods typically preserve the input geometry and therefore struggle to capture this deeper abstraction behavior, especially for illustrative and nonphotorealistic styles. In this work, we introduce Abstraction in Style (AiS), a generative framework that separates structural abstraction from visual stylization. Given a target image and a small set of style exemplars, AiS first derives an intermediate abstraction proxy that reinterprets the target's structure in accordance with the abstraction logic exhibited by the style. The proxy captures semantic structure while relaxing geometric fidelity, enabling subsequent stylization to operate on an abstracted representation rather than the original image. In a second stage, the abstraction proxy is rendered to produce the final stylized output, preserving visual coherence with the reference style. Both stages are implemented using a shared image space analogy, enabling transformations to be learned from visual exemplars without explicit geometric supervision. By decoupling abstraction from appearance and treating abstraction as an explicit, transferable process, AiS supports a wider range of stylistic transformations, improves controllability, and enables more expressive stylization.

### 🤖 AI 总结

**一句话总结**：AiS 将“结构抽象”与“外观风格化”解耦，先抽象再渲染，从而更好地迁移具有结构重解释特征的艺术风格。

**研究动机**：传统风格迁移多保持输入几何结构，仅改变纹理/颜色，难以复现插画与非写实风格中更深层的“结构性抽象”规律。为捕捉这种抽象逻辑，需要一种能在结构层面重解释内容、而非只做表面外观替换的方法。

**核心方法**：AiS 分两阶段：先根据少量风格示例为目标图像生成“抽象代理”（abstraction proxy），在保留语义结构的同时放松几何精确性；再将该代理渲染为最终风格化结果以匹配参考风格的视觉一致性。两阶段通过共享的“图像空间类比”机制从视觉示例中学习变换，无需显式几何监督，并将抽象作为可迁移的独立过程来建模与控制。

**主要结论**：通过显式分离并迁移结构抽象，AiS 能覆盖更广的风格变换类型，尤其对插画/非写实风格更有效。该解耦设计提升了可控性与表达力，使风格化不再局限于保持原始几何的外观替换。

**关键词**：结构抽象, 风格迁移, 非真实感渲染, 插画风格, 两阶段生成框架, 抽象代理, 视觉风格化, 示例驱动学习, 图像空间类比, 几何保真放松, 可控风格化

**评分**：66

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29924v1) | [下载PDF](https://arxiv.org/pdf/2603.29924v1.pdf)

---

## cs.LG

## [23. Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?](https://arxiv.org/abs/2603.30036v1)

**作者**：Max Kaufmann, David Lindner, Roland S. Zimmermann 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

Chain-of-Thought (CoT) monitoring, in which automated systems monitor the CoT of an LLM, is a promising approach for effectively overseeing AI systems. However, the extent to which a model's CoT helps us oversee the model - the monitorability of the CoT - can be affected by training, for instance by the model learning to hide important features of its reasoning. We propose and empirically validate a conceptual framework for predicting when and why this occurs. We model LLM post-training as an RL environment where the reward decomposes into two terms: one term depending on final outputs and another term depending on the CoT. Our framework allows us to classify these two terms as "aligned", "orthogonal", or "in-conflict" before training. We predict that training with in-conflict terms will reduce monitorability, orthogonal terms will not affect it, and aligned terms will improve it. To validate our framework, we use it to classify a set of RL environments, train LLMs within those environments, and evaluate how training affects CoT monitorability. We find that (1) training with "in-conflict" reward terms reduces CoT monitorability and (2) optimizing in-conflict reward terms is difficult.

### 🤖 AI 总结

**一句话总结**：论文提出一个“奖励项对齐/正交/冲突”的框架来预测在何种训练条件下优化Chain-of-Thought（CoT）是安全的，并实验证明“冲突”会降低CoT可监控性。

**研究动机**：CoT监控被视为监督LLM的重要手段，但训练过程中模型可能学会在CoT中隐藏关键信息，从而削弱可监控性；因此需要在训练前判断哪些优化会损害或提升CoT的可监督性。

**核心方法**：将LLM后训练建模为RL环境，把总奖励分解为“依赖最终输出”的奖励项与“依赖CoT”的奖励项，并在训练前将两者关系分类为对齐（aligned）/正交（orthogonal）/冲突（in-conflict）；随后在多种可分类的RL环境中训练LLM并评估CoT monitorability的变化以验证预测。

**主要结论**：实证结果显示：当奖励项彼此“冲突”时，优化会显著降低CoT可监控性，同时这类冲突奖励项本身也更难被有效优化；与框架预测一致，冲突是导致CoT监控失效的重要风险因素。

**关键词**：思维链监控, 可监控性, 后训练强化学习, 奖励分解, 输出奖励, 思维链奖励, 奖励对齐, 正交奖励, 冲突奖励, 推理隐藏

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30036v1) | [下载PDF](https://arxiv.org/pdf/2603.30036v1.pdf)

---

## [24. Reward-Based Online LLM Routing via NeuralUCB](https://arxiv.org/abs/2603.30035v1)

**作者**：Ming-Hua Tsai, Phat Tran  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-03-31

### 📄 论文摘要

This study investigates the use of NeuralUCB for cost-aware large language model (LLM) routing. Existing routing approaches can be broadly grouped into supervised routing methods and partial-feedback methods, each with different tradeoffs in efficiency and adaptivity. We implement a NeuralUCB-based routing policy and evaluate it on RouterBench under a simulated online setting. Experimental results show that the proposed method consistently outperforms random and min-cost baselines in utility reward. Compared with the max-quality reference, our method achieves substantially lower inference cost while maintaining competitive reward. These findings suggest that NeuralUCB is a promising approach for cost-aware LLM routing, while also highlighting remaining challenges in action discrimination and exploration.

### 🤖 AI 总结

**一句话总结**：本文将NeuralUCB用于在线、成本感知的LLM路由，在保持较高效用奖励的同时显著降低推理成本。

**研究动机**：现有LLM路由方法要么依赖监督信号、适应性不足，要么在部分反馈设置下探索效率有限；因此需要一种能在在线交互中兼顾成本与收益的自适应策略。

**核心方法**：将LLM选择建模为上下文多臂老虎机问题，采用NeuralUCB作为路由策略，在RouterBench的模拟在线环境中基于不完全反馈进行探索-利用，并以效用奖励与推理成本为优化目标进行评估。

**主要结论**：NeuralUCB路由在效用奖励上稳定优于随机与最低成本基线，并相比“最高质量”参考显著降低成本且保持有竞争力的奖励，但在动作区分与探索策略上仍存在挑战。

**关键词**：成本感知推理, 上下文多臂老虎机, 部分反馈, 奖励驱动优化, 推理成本-质量权衡, 动作区分, Reward-Based, Online

**评分**：73

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30035v1) | [下载PDF](https://arxiv.org/pdf/2603.30035v1.pdf)

---

## [25. Tucker Attention: A generalization of approximate attention mechanisms](https://arxiv.org/abs/2603.30033v1)

**作者**：Timon Klein, Jonas Kusch, Sebastian Sager 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-03-31

### 📄 论文摘要

The pursuit of reducing the memory footprint of the self-attention mechanism in multi-headed self attention (MHA) spawned a rich portfolio of methods, e.g., group-query attention (GQA) and multi-head latent attention (MLA). The methods leverage specialized low-rank factorizations across embedding dimensions or attention heads. From the point of view of classical low-rank approximation, these methods are unconventional and raise questions of which objects they really approximate and how to interpret the low-rank behavior of the resulting representations. To answer these questions, this work proposes a generalized view on the weight objects in the self-attention layer and a factorization strategy, which allows us to construct a parameter efficient scheme, called Tucker Attention. Tucker Attention requires an order of magnitude fewer parameters for comparable validation metrics, compared to GQA and MLA, as evaluated in LLM and ViT test cases. Additionally, Tucker Attention~encompasses GQA, MLA, MHA as special cases and is fully compatible with flash-attention and rotary position embeddings (RoPE). This generalization strategy yields insights of the actual ranks achieved by MHA, GQA, and MLA, and further enables simplifications for MLA.

### 🤖 AI 总结

**一句话总结**：提出“Tucker Attention”这一统一的低秩分解视角与实现方案，在保持效果接近的同时显著减少自注意力层参数量，并将MHA/GQA/MLA纳入同一框架。

**研究动机**：现有GQA、MLA等近似注意力方法虽能降内存/参数，但其低秩近似对象与“到底在近似什么”缺乏清晰的经典低秩解释，难以比较与理解其表示的秩行为。

**核心方法**：重新定义自注意力层中权重对象的广义视图，并用Tucker分解构造参数高效的Tucker Attention；该方案可退化为MHA、GQA、MLA的特例，并兼容flash-attention与RoPE，同时给出对实际有效秩的分析与对MLA的进一步简化。

**主要结论**：在LLM与ViT实验中，Tucker Attention在相近验证指标下较GQA/MLA实现数量级更少的参数；统一框架还揭示了MHA/GQA/MLA实际达到的秩特性，并据此提出对MLA的简化改进。

**关键词**：近似注意力机制, 自注意力内存优化, 多头注意力（MHA）, 低秩张量分解（Tucker）, 参数高效注意力, 秩分析, 旋转位置编码（RoPE）, LLM 与 ViT 评测

**评分**：82

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30033v1) | [下载PDF](https://arxiv.org/pdf/2603.30033v1.pdf)

---

## [26. Tracking Equivalent Mechanistic Interpretations Across Neural Networks](https://arxiv.org/abs/2603.30002v1)

**作者**：Alan Sun, Mariya Toneva  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-03-31

### 📄 论文摘要

Mechanistic interpretability (MI) is an emerging framework for interpreting neural networks. Given a task and model, MI aims to discover a succinct algorithmic process, an interpretation, that explains the model's decision process on that task. However, MI is difficult to scale and generalize. This stems in part from two key challenges: there is no precise notion of a valid interpretation; and, generating interpretations is often an ad hoc process. In this paper, we address these challenges by defining and studying the problem of interpretive equivalence: determining whether two different models share a common interpretation, without requiring an explicit description of what that interpretation is. At the core of our approach, we propose and formalize the principle that two interpretations of a model are equivalent if all of their possible implementations are also equivalent. We develop an algorithm to estimate interpretive equivalence and case study its use on Transformer-based models. To analyze our algorithm, we introduce necessary and sufficient conditions for interpretive equivalence based on models' representation similarity. We provide guarantees that simultaneously relate a model's algorithmic interpretations, circuits, and representations. Our framework lays a foundation for the development of more rigorous evaluation methods of MI and automated, generalizable interpretation discovery methods.

### 🤖 AI 总结

**一句话总结**：提出“解释等价性”框架，用于在不显式给出解释内容的情况下判断两个神经网络是否共享同一机制性解释，并给出可估计算法与理论条件。

**研究动机**：机制可解释性（MI）难以规模化与泛化，部分原因是“什么算有效解释”缺乏精确定义且解释生成过程往往较为临时和经验化。作者希望通过可验证的“等价性”概念来更严格地评估与迁移解释。

**核心方法**：形式化定义解释等价性原则：若两种解释的所有可能实现也彼此等价，则这两种解释等价；据此提出估计解释等价性的算法并在Transformer模型上做案例研究。为分析算法，作者基于表示相似性给出解释等价的充要条件，并建立解释（算法层面）、电路（circuit层面）与表示（representation层面）之间的联系与保证。

**主要结论**：作者给出了可操作的解释等价性估计方法，并提供理论保证将模型的算法性解释、电路结构与表示相似性统一起来，从而为更严格的MI评估与更自动化、可泛化的解释发现奠定基础。

**关键词**：机制可解释性, 解释等价性, 等价性估计算法, 表示相似性, 算法解释, 神经网络电路, 实现等价性, 可解释性评测框架

**评分**：68

**论文链接**：[查看原文](https://arxiv.org/abs/2603.30002v1) | [下载PDF](https://arxiv.org/pdf/2603.30002v1.pdf)

---

## [27. Aligning Validation with Deployment: Target-Weighted Cross-Validation for Spatial Prediction](https://arxiv.org/abs/2603.29981v1)

**作者**：Alexander Brenning, Thomas Suesse  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-03-31

### 📄 论文摘要

Cross-validation (CV) is commonly used to estimate predictive risk when independent test data are unavailable. Its validity depends on the assumption that validation tasks are sampled from the same distribution as prediction tasks encountered during deployment. In spatial prediction and other settings with structured data, this assumption is frequently violated, leading to biased estimates of deployment risk. We propose Target-Weighted CV (TWCV), an estimator of deployment risk that accounts for discrepancies between validation and deployment task distributions, thus accounting for (1) covariate shift and (2) task-difficulty shift. We characterize prediction tasks by descriptors such as covariates and spatial configuration. TWCV assigns weights to validation losses such that the weighted empirical distribution of validation tasks matches the corresponding distribution over a target domain. The weights are obtained via calibration weighting, yielding an importance-weighted estimator that targets deployment risk. Since TWCV requires adequate coverage of the deployment distribution's support, we combine it with spatially buffered resampling that diversifies the task difficulty distribution. In a simulation study, conventional as well as spatial estimators exhibit substantial bias depending on sampling, whereas buffered TWCV remains approximately unbiased across scenarios. A case study in environmental pollution mapping further confirms that discrepancies between validation and deployment task distributions can affect performance assessment, and that buffered TWCV better reflects the prediction task over the target domain. These results establish task distribution mismatch as a primary source of CV bias in spatial prediction and show that calibration weighting combined with a suitable validation task generator provides a viable approach to estimating predictive risk under dataset shift.

### 🤖 AI 总结

**一句话总结**：提出目标加权交叉验证（TWCV），通过对验证损失加权使验证任务分布对齐部署任务分布，从而更无偏地估计空间预测的部署风险。

**研究动机**：传统CV默认验证任务与部署预测任务同分布，但在空间数据中常因协变量漂移与任务难度分布变化而被破坏，导致对实际部署风险的系统性偏差。

**核心方法**：将“预测任务”用协变量与空间配置等描述符表征，并用校准加权（calibration weighting）学习权重，使加权后的验证任务经验分布匹配目标域任务分布，以得到面向部署风险的重要性加权估计；同时结合空间缓冲重采样以增加对目标域支持集与任务难度的覆盖，缓解权重估计所需覆盖不足问题。

**主要结论**：仿真显示常规CV及一些空间CV在不同采样条件下偏差显著，而“缓冲TWCV”在多场景下近似无偏；污染制图案例也表明验证/部署任务分布不匹配会扭曲性能评估，缓冲TWCV更能反映目标域部署表现。

**关键词**：空间预测, 部署风险估计, 交叉验证偏差, 任务分布失配, 目标加权交叉验证（TWCV）, 协变量漂移, 任务难度漂移, 校准加权, 重要性加权, 空间缓冲重采样, 空间交叉验证, 环境污染制图

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29981v1) | [下载PDF](https://arxiv.org/pdf/2603.29981v1.pdf)

---

## [28. Quantifying Cross-Modal Interactions in Multimodal Glioma Survival Prediction via InterSHAP: Evidence for Additive Signal Integration](https://arxiv.org/abs/2603.29977v1)

**作者**：Iain Swift, JingHua Ye, Ruairi O'Reilly  
**分类**：cs.LG, cs.AI, q-bio.QM  
**发布时间**：2026-03-31

### 📄 论文摘要

Multimodal deep learning for cancer prognosis is commonly assumed to benefit from synergistic cross-modal interactions, yet this assumption has not been directly tested in survival prediction settings. This work adapts InterSHAP, a Shapley interaction index-based metric, from classification to Cox proportional hazards models and applies it to quantify cross-modal interactions in glioma survival prediction. Using TCGA-GBM and TCGA-LGG data (n=575), we evaluate four fusion architectures combining whole-slide image (WSI) and RNA-seq features. Our central finding is an inverse relationship between predictive performance and measured interaction: architectures achieving superior discrimination (C-index 0.64$\to$0.82) exhibit equivalent or lower cross-modal interaction (4.8\%$\to$3.0\%). Variance decomposition reveals stable additive contributions across all architectures (WSI${\approx}$40\%, RNA${\approx}$55\%, Interaction${\approx}$4\%), indicating that performance gains arise from complementary signal aggregation rather than learned synergy. These findings provide a practical model auditing tool for comparing fusion strategies, reframe the role of architectural complexity in multimodal fusion, and have implications for privacy-preserving federated deployment.

### 🤖 AI 总结

**一句话总结**：作者将InterSHAP从分类扩展到Cox生存模型，发现多模态胶质瘤生存预测中更高性能并不对应更强跨模态交互，主要收益来自加性互补信息整合。

**研究动机**：多模态深度学习常被认为依赖“跨模态协同/交互”带来性能提升，但在生存预测任务中这一假设缺乏直接可量化的检验与审计工具。

**核心方法**：将基于Shapley交互指数的InterSHAP适配到Cox比例风险模型，并在TCGA-GBM/LGG（n=575）上比较4种WSI+RNA-seq融合架构，量化跨模态交互占比并做方差分解评估各模态与交互对预测的贡献。

**主要结论**：性能更好的融合架构（C-index 0.64→0.82）反而表现出相当或更低的跨模态交互（4.8%→3.0%），且贡献分解稳定显示WSI≈40%、RNA≈55%、交互≈4%，表明提升主要来自加性信号聚合而非学到的协同交互。

**关键词**：多模态生存预测, 胶质瘤预后, 跨模态交互, Cox比例风险模型, 多模态特征融合, 全切片图像（WSI）, 方差分解, 加性信号整合, 模型审计

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29977v1) | [下载PDF](https://arxiv.org/pdf/2603.29977v1.pdf)

---

## [29. Meteorology-Driven GPT4AP: A Multi-Task Forecasting LLM for Atmospheric Air Pollution in Data-Scarce Settings](https://arxiv.org/abs/2603.29974v1)

**作者**：Prasanjit Dey, Soumyabrata Dev, Bianca Schoen-Phelan  
**分类**：cs.LG  
**发布时间**：2026-03-31

### 📄 论文摘要

Accurate forecasting of air pollution is important for environmental monitoring and policy support, yet data-driven models often suffer from limited generalization in regions with sparse observations. This paper presents Meteorology-Driven GPT for Air Pollution (GPT4AP), a parameter-efficient multi-task forecasting framework based on a pre-trained GPT-2 backbone and Gaussian rank-stabilized low-rank adaptation (rsLoRA). The model freezes the self-attention and feed-forward layers and adapts lightweight positional and output modules, substantially reducing the number of trainable parameters. GPT4AP is evaluated on six real-world air quality monitoring datasets under few-shot, zero-shot, and long-term forecasting settings. In the few-shot regime using 10% of the training data, GPT4AP achieves an average MSE/MAE of 0.686/0.442, outperforming DLinear (0.728/0.530) and ETSformer (0.734/0.505). In zero-shot cross-station transfer, the proposed model attains an average MSE/MAE of 0.529/0.403, demonstrating improved generalization compared with existing baselines. In long-term forecasting with full training data, GPT4AP remains competitive, achieving an average MAE of 0.429, while specialized time-series models show slightly lower errors. These results indicate that GPT4AP provides a data-efficient forecasting approach that performs robustly under limited supervision and domain shift, while maintaining competitive accuracy in data-rich settings.

### 🤖 AI 总结

**一句话总结**：GPT4AP通过在GPT-2上进行参数高效适配，实现了在观测稀缺与跨站点迁移场景下的多任务空气污染预测，并在少样本/零样本设置中显著优于多种基线。

**研究动机**：空气污染预测对环境治理很关键，但许多数据驱动模型在监测稀疏地区容易过拟合、泛化差，且跨站点迁移与长期预测困难。作者希望用预训练语言模型的迁移能力，在少标注与域偏移下仍保持稳定预测性能。

**核心方法**：提出Meteorology-Driven GPT4AP：以预训练GPT-2为骨干，冻结自注意力与前馈层，仅对轻量的位置与输出模块进行适配，并引入Gaussian rank-stabilized LoRA（rsLoRA）做低秩参数高效微调。框架支持多任务预测，并在少样本、零样本跨站点与长期预测三类设置下评测。

**主要结论**：在仅用10%训练数据的少样本条件下，GPT4AP平均MSE/MAE为0.686/0.442，优于DLinear与ETSformer；在零样本跨站点迁移中平均MSE/MAE达0.529/0.403，显示更强泛化。全量数据的长期预测中其MAE约0.429，虽略逊于部分专用时序模型但仍具竞争力，证明其在数据稀缺与域迁移场景下更稳健、数据效率更高。

**关键词**：空气污染预测, 气象驱动建模, 多任务时间序列预测, 数据稀缺场景, 少样本学习, 零样本迁移, 跨站点泛化, 参数高效微调, 低秩适配, GPT-2骨干网络, 长期预测

**评分**：78

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29974v1) | [下载PDF](https://arxiv.org/pdf/2603.29974v1.pdf)

---

## [30. Real-Time Explanations for Tabular Foundation Models](https://arxiv.org/abs/2603.29946v1)

**作者**：Luan Borges Teodoro Reis Sena, Francisco Galuppo Azevedo  
**分类**：cs.LG  
**发布时间**：2026-03-31

### 📄 论文摘要

Interpretability is central for scientific machine learning, as understanding \emph{why} models make predictions enables hypothesis generation and validation. While tabular foundation models show strong performance, existing explanation methods like SHAP are computationally expensive, limiting interactive exploration. We introduce ShapPFN, a foundation model that integrates Shapley value regression directly into its architecture, producing both predictions and explanations in a single forward pass. On standard benchmarks, ShapPFN achieves competitive performance while producing high-fidelity explanations ($R^2$=0.96, cosine=0.99) over 1000\times faster than KernelSHAP (0.06s vs 610s). Our code is available at https://github.com/kunumi/ShapPFN

### 🤖 AI 总结

**一句话总结**：ShapPFN 将 Shapley 值回归直接集成到表格基础模型中，实现一次前向传播同时输出预测与高保真解释，并将解释生成速度提升到比 KernelSHAP 快 1000× 以上。

**研究动机**：表格基础模型虽性能强，但常用解释方法（如 SHAP）计算代价高，难以支持交互式、实时的科学探索与假设验证。

**核心方法**：提出 ShapPFN：在模型架构中内置 Shapley value regression，使模型在推理时无需额外采样/拟合即可同步产出预测结果与特征归因解释。

**主要结论**：在标准基准上，ShapPFN 预测性能具竞争力，同时解释质量很高（R^2=0.96、cosine=0.99），且解释生成时间从 610s 降至 0.06s，实现实时可解释性。

**关键词**：表格基础模型, 实时可解释性, 单次前向解释, 高保真特征归因, 交互式模型探索, 科学机器学习解释, 基准评测, Real-Time

**评分**：81

**论文链接**：[查看原文](https://arxiv.org/abs/2603.29946v1) | [下载PDF](https://arxiv.org/pdf/2603.29946v1.pdf)

---

