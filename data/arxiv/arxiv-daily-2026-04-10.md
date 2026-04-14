# arXiv AI 论文日报 | 2026-04-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (4 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.AI](#csAI) (6 篇)

---

## cs.AI

## [1. New Hybrid Fine-Tuning Paradigm for LLMs: Algorithm Design and Convergence Analysis Framework](https://arxiv.org/abs/2604.09940v1)

**作者**：Shaocong Ma, Peiran Yu, Heng Huang  
**分类**：cs.AI, cs.LG, math.OC  
**发布时间**：2026-04-10

### 📄 论文摘要

Fine-tuning Large Language Models (LLMs) typically involves either full fine-tuning, which updates all model parameters, or Parameter-Efficient Fine-Tuning (PEFT), which adjusts a small subset of parameters. However, both approaches have inherent limitations: full fine-tuning is computationally expensive, while PEFT often struggles to learn new knowledge and exhibits suboptimal performance. To overcome these issues, we propose a novel hybrid fine-tuning approach that jointly updates both LLMs and PEFT modules using a combination of zeroth-order and first-order optimization methods. To analyze our new algorithm, we develop a theoretical framework centered on the concept of hybrid smoothness condition, which accounts for the heterogeneous nature of the optimization landscape in joint LLM and PEFT training. We derive a rigorous convergence analysis for the convergence of reshuffling-type SGD algorithm under multiple learning rates and demonstrate its effectiveness through extensive empirical studies across various downstream tasks and model architectures. On the practical side, our results demonstrate consistent performance improvement, making the approach a viable solution for large-scale language model fine-tuning.

### 🤖 AI 总结

**一句话总结**：本文提出了一种结合零阶和一阶优化方法的混合微调新范式，用于联合更新LLMs和PEFT模块，并提供了基于混合平滑条件的严格收敛性理论分析。

**研究动机**：全量微调计算开销大，而参数高效微调(PEFT)方法在学习新知识和性能表现上存在不足，两种现有方法都难以满足大规模语言模型高效微调的需求。

**核心方法**：提出混合微调框架，使用重排型SGD算法联合优化LLMs和PEFT模块；引入混合平滑条件来刻画联合训练的异质优化景观，并在此基础上推导出多学习率下的收敛性理论保证。

**主要结论**：实验表明该方法在多种下游任务和模型架构上实现了一致的性能提升，验证了混合优化策略的有效性，为大规模语言模型微调提供了计算效率与性能兼顾的可行方案。

**关键词**：混合微调, 零阶优化, 一阶优化, 混合平滑条件, 收敛性分析, 多学习率, 联合优化, New

**评分**：8

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09940v1) | [下载PDF](https://arxiv.org/pdf/2604.09940v1.pdf)

---

## [2. HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks](https://arxiv.org/abs/2604.09937v1)

**作者**：Suhana Bedi, Ryan Welch, Ethan Steinberg 等 15 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Healthcare administration accounts for over $1 trillion in annual spending, making it a promising target for LLM-based computer-use agents (CUAs). While clinical applications of LLMs have received significant attention, no benchmark exists for evaluating CUAs on end-to-end administrative workflows. To address this gap, we introduce HealthAdminBench, a benchmark comprising four realistic GUI environments: an EHR, two payer portals, and a fax system, and 135 expert-defined tasks spanning three administrative task types: Prior Authorization, Appeals and Denials Management, and Durable Medical Equipment (DME) Order Processing. Each task is decomposed into fine-grained, verifiable subtasks, yielding 1,698 evaluation points. We evaluate seven agent configurations under multiple prompting and observation settings and find that, despite strong subtask performance, end-to-end reliability remains low: the best-performing agent (Claude Opus 4.6 CUA) achieves only 36.3 percent task success, while GPT-5.4 CUA attains the highest subtask success rate (82.8 percent). These results reveal a substantial gap between current agent capabilities and the demands of real-world administrative workflows. HealthAdminBench provides a rigorous foundation for evaluating progress toward safe and reliable automation of healthcare administrative workflows.

### 🤖 AI 总结

**一句话总结**：HealthAdminBench是一个评估LLM计算机代理在医疗行政管理任务上的基准，发现当前最佳代理仅达到36.3%的端到端任务成功率，表明现有代理能力与实际医疗行政工作流程需求之间存在显著差距。

**研究动机**：医疗行政每年支出超过1万亿美元，是LLM代理自动化的一个有前景的目标，但目前缺乏专门评估代理端到端行政工作流程能力的基准。

**核心方法**：该基准包含4个真实GUI环境（电子健康记录系统、两个付款方门户、传真系统），涵盖135个专家定义的任务，分为3种行政任务类型，产生1,698个可验证评估点，对7种代理配置进行评估。

**主要结论**：尽管子任务表现强劲，但端到端可靠性仍然较低：表现最佳的Claude Opus 4.6 CUA仅实现36.3%的任务成功，而GPT-5.4 CUA达到最高子任务成功率82.8%，揭示了当前代理能力与真实医疗行政需求之间的巨大差距。

**关键词**：LLM, Agent, HealthAdminBench, Evaluating, Computer-Use, Healthcare, Administration, Tasks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09937v1) | [下载PDF](https://arxiv.org/pdf/2604.09937v1.pdf)

---

## [3. GLEaN: A Text-to-image Bias Detection Approach for Public Comprehension](https://arxiv.org/abs/2604.09923v1)

**作者**：Bochu Ding, Brinnae Bent, Augustus Wendell  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Text-to-image (T2I) models, and their encoded biases, increasingly shape the visual media the public encounters. While researchers have produced a rich body of work on bias measurement, auditing, and mitigation in T2I systems, those methods largely target technical stakeholders, leaving a gap in public legibility. We introduce GLEaN (Generative Likeness Evaluation at N-Scale), a portrait-based explainability pipeline designed to make T2I model biases visually understandable to a broad audience. GLEaN comprises three stages: automated large-scale image generation from identity prompts, facial landmark-based filtering and spatial alignment, and median-pixel composition that distills a model's central tendency into a single representative portrait. The resulting composites require no statistical background to interpret; a viewer can see, at a glance, who a model 'imagines' when prompted with 'a doctor' versus a 'felon.' We demonstrate GLEaN on Stable Diffusion XL across 40 social and occupational identity prompts, producing composites that reproduce documented biases and surface new associations between skin tone and predicted emotion. We find in a between-subjects user study (N = 291) that GLEaN portraits communicate biases as effectively as conventional data tables, but require significantly less viewing time. Because the method relies solely on generated outputs, it can also be replicated on any black-box and closed-weight systems without access to model internals. GLEaN offers a scalable, model-agnostic approach to bias explainability, purpose-built for public comprehension, and is publicly available at https://github.com/cultureiolab/GLEaN.

### 🤖 AI 总结

**一句话总结**：GLEaN是一个基于肖像的T2I模型偏见可视化解释管道，通过大规模图像生成和median-pixel组合，将模型偏见以直观肖像形式呈现给普通公众。

**研究动机**：现有T2I模型偏见研究主要面向技术研究人员，普通公众难以理解，导致公众对AI生成内容的偏见缺乏认知。

**核心方法**：GLEaN包含三阶段：1)大规模自动化图像生成，2)面部地标过滤与空间对齐，3)median-pixel合成生成代表性肖像，用户研究(N=291)验证其有效性。

**主要结论**：GLEaN肖像与数据表格在传达偏见方面效果相当，但观看时间显著减少；该方法可应用于任意黑盒或闭源模型，提供可扩展的偏见解释方案。

**关键词**：可解释性, GLEaN, Text-to-image, Bias, Detection, Approach, Public, Comprehension

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09923v1) | [下载PDF](https://arxiv.org/pdf/2604.09923v1.pdf)

---

## [4. In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach](https://arxiv.org/abs/2604.09889v1)

**作者**：Pallock Halder, Satyajit Mojumder  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

AI agents are being increasingly deployed across a wide range of real-world applications. In this paper, we propose an agentic AI framework for in-situ process monitoring for defect detection in wire-arc additive manufacturing (WAAM). The autonomous agent leverages a WAAM process monitoring dataset and a trained classification tool to build AI agents and uses a large language model (LLM) for in-situ process monitoring decision-making for defect detection. A processing agent is developed based on welder process signals, such as current and voltage, and a monitoring agent is developed based on acoustic data collected during the process. Both agents are tasked with identifying porosity defects from processing and monitoring signals, respectively. Ground truth X-ray computed tomography (XCT) data are used to develop classification tools for both the processing and monitoring agents. Furthermore, a multi-agent framework is demonstrated in which the processing and monitoring agents are orchestrated together for parallel decision-making on the given task of defect classification. Evaluation metrics are proposed to determine the efficacy of both individual agents, the combined single-agent, and the coordinated multi-agent system. The multi-agent configuration outperforms all individual-agent counterparts, achieving a decision accuracy of 91.6% and an F1 score of 0.821 on decided runs, across 15 independent runs, and a reasoning quality score of 3.74 out of 5. These in-situ process monitoring agents hold significant potential for autonomous real-time process monitoring and control toward building qualified parts for WAAM and other additive manufacturing processes.

### 🤖 AI 总结

**一句话总结**：AI agents are being increasingly deployed across a wide range of real-world applications. In this paper, we propose an agentic AI framework for in-situ process monitoring for defect detection in wire-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, In-situ, process, monitoring, defect, detection, wire-arc, additive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09889v1) | [下载PDF](https://arxiv.org/pdf/2604.09889v1.pdf)

---

## [5. What do your logits know? (The answer may surprise you!)](https://arxiv.org/abs/2604.09885v1)

**作者**：Masha Fedzechkina, Eleonora Gualdoni, Rita Ramos 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Recent work has shown that probing model internals can reveal a wealth of information not apparent from the model generations. This poses the risk of unintentional or malicious information leakage, where model users are able to learn information that the model owner assumed was inaccessible. Using vision-language models as a testbed, we present the first systematic comparison of information retained at different "representational levels'' as it is compressed from the rich information encoded in the residual stream through two natural bottlenecks: low-dimensional projections of the residual stream obtained using tuned lens, and the final top-k logits most likely to impact model's answer. We show that even easily accessible bottlenecks defined by the model's top logit values can leak task-irrelevant information present in an image-based query, in some cases revealing as much information as direct projections of the full residual stream.

### 🤖 AI 总结

**一句话总结**：研究表明视觉-语言模型的简单top-k logits瓶颈就能泄露图像查询中的任务无关信息，泄露量甚至接近完整的残差流投影。

**研究动机**：探针研究已证明模型内部表示蕴含丰富信息，但这些信息对模型所有者和用户存在不对称性，可能导致意外或恶意的信息泄露风险。

**核心方法**：以视觉-语言模型为测试平台，系统比较残差流经两个自然瓶颈（tuned lens低维投影和top-k logits）后保留的信息量差异。

**主要结论**：即使是最易访问的top logit瓶颈也能泄露图像中的任务无关信息，在某些情况下泄露程度接近直接投影完整残差流的结果，揭示了严重的安全和隐私隐患。

**关键词**：信息泄露, 模型探查, 表示层级, 视觉-语言模型, 残差流投影, 模型内省, 瓶颈压缩, What

**评分**：12

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09885v1) | [下载PDF](https://arxiv.org/pdf/2604.09885v1.pdf)

---

## [6. MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/abs/2604.09852v1)

**作者**：Vasilis Kontonis, Yuchen Zeng, Shivam Garg 等 10 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Reasoning models think in long, unstructured streams with no mechanism for compressing or organizing their own intermediate state. We introduce MEMENTO: a method that teaches models to segment reasoning into blocks, compress each block into a memento, i.e., a dense state summary, and reason forward by attending only to mementos, reducing context, KV cache, and compute. To train MEMENTO models, we release OpenMementos, a public dataset of 228K reasoning traces derived from OpenThoughts-v3, segmented and annotated with intermediate summaries. We show that a two-stage SFT recipe on OpenMementos is effective across different model families (Qwen3, Phi-4, Olmo 3) and scales (8B--32B parameters). Trained models maintain strong accuracy on math, science, and coding benchmarks while achieving ${\sim}2.5\times$ peak KV cache reduction. We extend vLLM to support our inference method, achieving ${\sim}1.75\times$ throughput improvement while also enabling us to perform RL and further improve accuracy. Finally, we identify a dual information stream: information from each reasoning block is carried both by the memento text and by the corresponding KV states, which retain implicit information from the original block. Removing this channel drops accuracy by 15\,pp on AIME24.

### 🤖 AI 总结

**一句话总结**：MEMENTO通过教LLM将推理过程分块并压缩为记忆摘要，实现约2.5倍KV缓存压缩和1.75倍吞吐量提升，同时保持精度。

**研究动机**：现有推理模型在长链推理时使用无结构的长上下文流，缺乏压缩和组织中间状态的机制，导致KV缓存和计算资源浪费。

**核心方法**：发布OpenMementos数据集（228K推理轨迹），采用两阶段SFT训练让模型学会分块和摘要生成，并扩展vLLM支持基于memento的推理和RL微调。

**主要结论**：MEMENTO在不同模型家族（Qwen3/Phi-4/Olmo3）和规模（8B-32B）上均有效，在数学、科学、编程基准上保持精度的同时实现显著资源压缩，并揭示了memento文本与KV状态的双重信息流机制。

**关键词**：推理分割, 状态摘要, KV缓存压缩, RL微调, 推理效率, 上下文压缩, MEMENTO, Teaching

**评分**：24

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09852v1) | [下载PDF](https://arxiv.org/pdf/2604.09852v1.pdf)

---

## cs.CL

## [7. Human vs. Machine Deception: Distinguishing AI-Generated and Human-Written Fake News Using Ensemble Learning](https://arxiv.org/abs/2604.09960v1)

**作者**：Samuel Jaeger, Calvin Ibeneye, Aya Vera-Jimenez 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

The rapid adoption of large language models has introduced a new class of AI-generated fake news that coexists with traditional human-written misinformation, raising important questions about how these two forms of deceptive content differ and how reliably they can be distinguished. This study examines linguistic, structural, and emotional differences between human-written and AI-generated fake news and evaluates machine learning and ensemble-based methods for distinguishing these content types. A document-level feature representation is constructed using sentence structure, lexical diversity, punctuation patterns, readability indices, and emotion-based features capturing affective dimensions such as fear, anger, joy, sadness, trust, and anticipation. Multiple classification models, including logistic regression, random forest, support vector machines, extreme gradient boosting, and a neural network, are applied alongside an ensemble framework that aggregates predictions across models. Model performance is assessed using accuracy and area under the receiver operating characteristic curve. The results show strong and consistent classification performance, with readability-based features emerging as the most informative predictors and AI-generated text exhibiting more uniform stylistic patterns. Ensemble learning provides modest but consistent improvements over individual models. These findings indicate that stylistic and structural properties of text provide a robust basis for distinguishing AI-generated misinformation from human-written fake news.

### 🤖 AI 总结

**一句话总结**：The rapid adoption of large language models has introduced a new class of AI-generated fake news that coexists with traditional human-written misinformation, raising important questions about how thes...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AI生成内容检测, 假新闻识别, 集成学习, 文体特征, 情感分析, 可读性指标, 文本分类, 内容欺骗, 模型可解释性

**评分**：38

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09960v1) | [下载PDF](https://arxiv.org/pdf/2604.09960v1.pdf)

---

## [8. Should We be Pedantic About Reasoning Errors in Machine Translation?](https://arxiv.org/abs/2604.09890v1)

**作者**：Calvin Bao, Marine Carpuat  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Across multiple language pairings (English $\to$ \{Spanish, French, German, Mandarin, Japanese, Urdu, Cantonese\}), we find reasoning errors in translation. To quantify how often these reasoning errors occur, we leverage an automated annotation protocol for reasoning evaluation wherein the goal is to detect if a reasoning step is any of three error categories: (1) source sentence-misaligned, (2) model hypothesis-misaligned, or (3) reasoning trace-misaligned. We probe the reasoning model with perturbed traces correcting for these identified reasoning errors using an array of weak-to-strong interventions: hedging, removal, re-reasoning after removal, hindsight, and oracle interventions. Experimenting with interventions on the reasoning traces suggests that small corrections to the reasoning have little impact on translation quality, but stronger interventions yield the highest resolution rates, despite translation quality gains being mixed. We find ultimately that reasoning errors in MT can be identified with high precision in Urdu but lower precision in Spanish, but that removing these reasoning errors does not resolve the initial errors significantly, suggesting limited reasoning faithfulness for machine translation.

### 🤖 AI 总结

**一句话总结**：机器翻译中存在推理错误，但修正这些推理错误对翻译质量的提升效果有限，表明机器翻译模型的推理忠实度较低。

**研究动机**：机器翻译模型可能产生推理错误，但目前尚不清楚这些推理错误对翻译质量的实际影响程度，以及修正推理错误是否能有效改善翻译结果。

**核心方法**：设计自动化标注协议检测三类推理错误（源句对齐、模型假设对齐、推理轨迹对齐错误），在7种语言对中进行实验，采用弱到强干预策略（对冲、移除、重推理、后见之明、神谕干预）来测试修正推理错误的效果。

**主要结论**：推理错误可在多种语言对中被高精度识别，但修正这些推理错误并不能显著改善翻译质量，说明机器翻译中的推理忠实度有限，翻译质量提升不能简单依赖推理修正。

**关键词**：机器翻译, 推理错误, 推理评估, 多语言翻译, 干预措施, 翻译质量, 推理忠实度, 错误分类, 自动标注, 推理追踪

**评分**：6

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09890v1) | [下载PDF](https://arxiv.org/pdf/2604.09890v1.pdf)

---

## [9. Simulating Organized Group Behavior: New Framework, Benchmark, and Analysis](https://arxiv.org/abs/2604.09874v1)

**作者**：Xinkai Zou, Yiming Huang, Zhuohang Wu 等 8 位作者  
**分类**：cs.CL, cs.SI  
**发布时间**：2026-04-10

### 📄 论文摘要

Simulating how organized groups (e.g., corporations) make decisions (e.g., responding to a competitor's move) is essential for understanding real-world dynamics and could benefit relevant applications (e.g., market prediction). In this paper, we formalize this problem as a concrete research platform for group behavior understanding, providing: (1) a task definition with benchmark and evaluation criteria, (2) a structured analytical framework with a corresponding algorithm, and (3) detailed temporal and cross-group analysis. Specifically, we propose Organized Group Behavior Simulation, a task that models organized groups as collective entities from a practical perspective: given a group facing a particular situation (e.g., AI Boom), predict the decision it would take. To support this task, we present GROVE (GRoup Organizational BehaVior Evaluation), a benchmark covering 44 entities with 8,052 real-world context-decision pairs collected from Wikipedia and TechCrunch across 9 domains, with an end-to-end evaluation protocol assessing consistency, initiative, scope, magnitude, and horizon. Beyond straightforward prompting pipelines, we propose a structured analytical framework that converts collective decision-making events into an interpretable, adaptive, and traceable behavioral model, achieving stronger performance than summarization- and retrieval-based baselines. It further introduces an adapter mechanism for time-aware evolution and group-aware transfer, and traceable evidence nodes grounding each decision rule in originating historical events. Our analysis reveals temporal behavioral drift within individual groups, which the time-aware adapter effectively captures for stronger prediction, and structured cross-group similarity that enables knowledge transfer for data-scarce organizations.

### 🤖 AI 总结

**一句话总结**：本文提出有组织团体行为模拟(OGBS)任务和GROVE基准，用于建模和预测组织的集体决策，包含时间感知适配器和跨组知识迁移机制，在8,052个真实世界案例上验证了方法的有效性。

**研究动机**：理解有组织团体（如公司）如何应对竞争对手行动等情境做出决策，对市场预测等应用至关重要，但此前缺乏系统性的研究平台和评估标准。

**核心方法**：提出GROVE基准（44个实体、8,052个上下文-决策对）以及结构化分析框架，通过时间感知适配器捕捉组内行为漂移，利用跨组相似性实现知识迁移，并采用可追溯的证据节点支撑决策规则。

**主要结论**：实验表明该框架优于摘要和检索基线方法，时间感知适配器能有效捕捉个体组织的行为演变，跨组知识迁移对数据稀缺的组织特别有价值。

**关键词**：组织行为模拟, 集体决策, 行为建模, 时间感知适配, 跨群体分析, 知识迁移, 评估协议, 实体行为预测, 决策追溯

**评分**：33

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09874v1) | [下载PDF](https://arxiv.org/pdf/2604.09874v1.pdf)

---

## [10. Spoiler Alert: Narrative Forecasting as a Metric for Tension in LLM Storytelling](https://arxiv.org/abs/2604.09854v1)

**作者**：Peiqi Sui, Yutong Zhu, Tianyi Cheng 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

LLMs have so far failed both to generate consistently compelling stories and to recognize this failure--on the leading creative-writing benchmark (EQ-Bench), LLM judges rank zero-shot AI stories above New Yorker short stories, a gold standard for literary fiction. We argue that existing rubrics overlook a key dimension of compelling human stories: narrative tension. We introduce the 100-Endings metric, which walks through a story sentence by sentence: at each position, a model predicts how the story will end 100 times given only the text so far, and we measure tension as how often predictions fail to match the ground truth. Beyond the mismatch rate, the sentence-level curve yields complementary statistics, such as inflection rate, a geometric measure of how frequently the curve reverses direction, tracking twists and revelations. Unlike rubric-based judges, 100-Endings correctly ranks New Yorker stories far above LLM outputs. Grounded in narratological principles, we design a story-generation pipeline using structural constraints, including analysis of story templates, idea formulation, and narrative scaffolding. Our pipeline significantly increases narrative tension as measured by the 100-Endings metric, while maintaining performance on the EQ-Bench leaderboard.

### 🤖 AI 总结

**一句话总结**：论文提出100-Endings指标，通过让LLM预测100种可能结局的不匹配率来衡量叙事张力，并设计了基于叙事学原理的故事生成pipeline。

**研究动机**：现有LLM故事生成和评估存在缺陷——LLM评判竟将AI故事排在《纽约客》文学短篇之上，原因是现有评估标准忽视了叙事张力的核心维度。

**核心方法**：100-Endings指标逐句遍历故事，让模型仅基于已有文本预测100种可能结局，通过计算预测与真实结局的不匹配率量化张力，并引入inflection rate追踪情节转折；同时设计含故事模板分析、创意构思和叙事脚手架的生成pipeline。

**主要结论**：100-Endings正确地将《纽约客》故事排在LLM输出之上，证明其能有效捕捉叙事张力；该pipeline显著提升了生成故事的叙事张力，同时保持了EQ-Bench基准的性能。

**关键词**：叙事张力, 故事生成, 创意写作, 拐点率, 故事预测, 叙事脚手架, 文学基准, Spoiler

**评分**：17

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09854v1) | [下载PDF](https://arxiv.org/pdf/2604.09854v1.pdf)

---

## cs.CV

## [11. Cross-Cultural Value Awareness in Large Vision-Language Models](https://arxiv.org/abs/2604.09945v1)

**作者**：Phillip Howard, Xin Su, Kathleen C. Fraser  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

The rapid adoption of large vision-language models (LVLMs) in recent years has been accompanied by growing fairness concerns due to their propensity to reinforce harmful societal stereotypes. While significant attention has been paid to such fairness concerns in the context of social biases, relatively little prior work has examined the presence of stereotypes in LVLMs related to cultural contexts such as religion, nationality, and socioeconomic status. In this work, we aim to narrow this gap by investigating how cultural contexts depicted in images influence the judgments LVLMs make about a person's moral, ethical, and political values. We conduct a multi-dimensional analysis of such value judgments in five popular LVLMs using counterfactual image sets, which depict the same person across different cultural contexts. Our evaluation framework diagnoses LVLM awareness of cultural value differences through the use of Moral Foundations Theory, lexical analyses, and the sensitivity of generated values to depicted cultural contexts.

### 🤖 AI 总结

**一句话总结**：该论文通过反事实图像集评估大型视觉语言模型如何根据图像中的文化背景做出道德、伦理和政治价值判断，揭示了模型对文化差异的敏感性。

**研究动机**：大型视觉语言模型在快速普及中可能强化有害社会刻板印象，现有研究多关注社会偏见，对宗教、国籍、社会经济地位等文化相关刻板印象关注不足。

**核心方法**：使用描绘同一人物在不同文化背景下的反事实图像集，对五个主流LVLMs进行多维度分析，结合道德基础理论、词汇分析和价值敏感性测试来诊断模型的文化价值观意识。

**主要结论**：研究发现图像中呈现的文化背景确实会影响LVLMs产生的价值判断，揭示了模型对文化情境的敏感性和文化刻板印象的潜在影响。

**关键词**：大型视觉语言模型, 文化偏见, 跨文化分析, 道德基础理论, 反事实图像, 价值判断, 刻板印象, 词法分析, 敏感性分析

**评分**：23

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09945v1) | [下载PDF](https://arxiv.org/pdf/2604.09945v1.pdf)

---

## [12. I Walk the Line: Examining the Role of Gestalt Continuity in Object Binding for Vision Transformers](https://arxiv.org/abs/2604.09942v1)

**作者**：Alexa R. Tartaglini, Michael A. Lepori  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Object binding is a foundational process in visual cognition, during which low-level perceptual features are joined into object representations. Binding has been considered a fundamental challenge for neural networks, and a major milestone on the way to artificial models with flexible visual intelligence. Recently, several investigations have demonstrated evidence that binding mechanisms emerge in pretrained vision models, enabling them to associate portions of an image that contain an object. The question remains: how are these models binding objects together? In this work, we investigate whether vision models rely on the principle of Gestalt continuity to perform object binding, over and above other principles like similarity and proximity. Using synthetic datasets, we demonstrate that binding probes are sensitive to continuity across a wide range of pretrained vision transformers. Next, we uncover particular attention heads that track continuity, and show that these heads generalize across datasets. Finally, we ablate these attention heads, and show that they often contribute to producing representations that encode object binding.

### 🤖 AI 总结

**一句话总结**：本文揭示了预训练视觉Transformer模型中的注意力头能够追踪Gestalt连续性原则，并利用该机制实现物体绑定。

**研究动机**：物体绑定是视觉认知的基础过程，之前研究证明预训练视觉模型具备绑定能力，但其背后的机制尚不清楚，需要探究模型是否遵循Gestalt连续性原则而非相似性或接近性原则进行绑定。

**核心方法**：使用合成数据集测试连续性敏感性，识别并 ablation 追踪连续性的特定注意力头，验证这些注意力头对物体绑定表示的贡献。

**主要结论**：研究发现在多种预训练视觉Transformer中都存在对连续性敏感的绑定探测机制，特定的注意力头能够追踪连续性且具有跨数据集泛化能力， ablation 实验证明这些头对物体绑定表示的产生有实质贡献。

**关键词**：物体绑定, 注意力头, 合成数据集, 视觉认知, 表征学习, 消融实验, 连续性追踪, 神经网络建模

**评分**：3

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09942v1) | [下载PDF](https://arxiv.org/pdf/2604.09942v1.pdf)

---

## [13. BLPR: Robust License Plate Recognition under Viewpoint and Illumination Variations via Confidence-Driven VLM Fallback](https://arxiv.org/abs/2604.09927v1)

**作者**：Guillermo Auza Banegas, Diego Calvimontes Vera, Sergio Castro Sandoval 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Robust license plate recognition in unconstrained environments remains a significant challenge, particularly in underrepresented regions with limited data availability and unique visual characteristics, such as Bolivia. Recognition accuracy in real-world conditions is often degraded by factors such as illumination changes and viewpoint distortion. To address these challenges, we introduce BLPR, a novel deep learning-based License Plate Detection and Recognition (LPDR) framework specifically designed for Bolivian license plates. The proposed system follows a two-stage pipeline where a YOLO-based detector is pretrained on synthetic data generated in Blender to simulate extreme perspectives and lighting conditions, and subsequently fine-tuned on street-level data collected in La Paz, Bolivia. Detected plates are geometrically rectified and passed to a character recognition model. To improve robustness under ambiguous scenarios, a lightweight vision-language model (Gemma3 4B) is selectively triggered as a confidence-based fallback mechanism. The proposed framework further leverages synthetic-to-real domain adaptation to improve robustness under diverse real-world conditions. We also introduce the first publicly available Bolivian LPDR dataset, enabling evaluation under diverse viewpoint and illumination conditions. The system achieves a character-level recognition accuracy of 89.6% on real-world data, demonstrating its effectiveness for deployment in challenging urban environments. Our project is publicly available at https://github.com/EdwinTSalcedo/BLPR.

### 🤖 AI 总结

**一句话总结**：BLPR是一个针对玻利维亚车牌的双阶段深度学习检测识别框架，通过YOLO检测器结合合成数据预训练和真实数据微调，并引入VLM置信度回退机制实现了复杂环境下的鲁棒车牌识别。

**研究动机**：在光照变化和视角失真等非约束条件下，车牌识别准确率显著下降，且玻利维亚等数据稀缺地区缺乏针对性的研究和数据集。

**核心方法**：系统采用YOLO检测器在Blender生成的合成极端视角光照数据上预训练，再基于拉巴斯街景数据微调，检测到的车牌经几何校正后由字符识别模型处理，当识别置信度不足时触发Gemma3 4B视觉语言模型作为回退机制。

**主要结论**：BLPR在真实世界数据上达到89.6%的字符级识别准确率，同时发布了首个公开的玻利维亚车牌数据集，验证了合成数据预训练与VLM回退策略相结合的有效性。

**关键词**：车牌识别, 视觉语言模型, 合成数据, 域适应, 几何校正, 玻利维亚车牌, 光照变化, 视角失真, 字符识别

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09927v1) | [下载PDF](https://arxiv.org/pdf/2604.09927v1.pdf)

---

## [14. Does Your VFM Speak Plant? The Botanical Grammar of Vision Foundation Models for Object Detection](https://arxiv.org/abs/2604.09920v1)

**作者**：Lars Lundqvist, Earl Ranario, Hamid Kamangir 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Vision foundation models (VFMs) offer the promise of zero-shot object detection without task-specific training data, yet their performance in complex agricultural scenes remains highly sensitive to text prompt construction. We present a systematic prompt optimization framework evaluating four open-vocabulary detectors -- YOLO World, SAM3, Grounding DINO, and OWLv2 -- for cowpea flower and pod detection across synthetic and real field imagery. We decompose prompts into eight axes and conduct one-factor-at-a-time analysis followed by combinatorial optimization, revealing that models respond divergently to prompt structure: conditions that optimize one architecture can collapse another. Applying model-specific combinatorial prompts yields substantial gains over a naive species-name baseline, including +0.357 mAP@0.5 for YOLO World and +0.362 mAP@0.5 for OWLv2 on synthetic cowpea flower data. To evaluate cross-task generalization, we use an LLM to translate the discovered axis structure to a morphologically distinct target -- cowpea pods -- and compare against prompting using the discovered optimal structures from synthetic flower data. Crucially, prompt structures optimized exclusively on synthetic data transfer effectively to real-world fields: synthetic-pipeline prompts match or exceed those discovered on labeled real data for the majority of model-object combinations (flower: 0.374 vs. 0.353 for YOLO World; pod: 0.429 vs. 0.371 for SAM3). Our findings demonstrate that prompt engineering can substantially close the gap between zero-shot VFMs and supervised detectors without requiring manual annotation, and that optimal prompts are model-specific, non-obvious, and transferable across domains.

### 🤖 AI 总结

**一句话总结**：本文通过系统性的提示优化框架，使视觉基础模型在零样本农业场景检测中显著提升性能，发现最优提示具有模型特异性且能从合成数据有效迁移到真实场景。

**研究动机**：视觉基础模型虽承诺零样本目标检测无需任务特定训练数据，但在复杂农业场景中的表现对文本提示的构造高度敏感，缺乏系统性的提示优化指导。

**核心方法**：作者将提示分解为八个维度，对比评估了YOLO World、SAM3、Grounding DINO和OWLv2四种开放词汇检测器，通过单因素分析和组合优化揭示了不同模型对提示结构的差异化响应，并利用大语言模型将发现的轴结构迁移到形态不同的目标进行跨任务泛化评估。

**主要结论**：模型特定的组合提示可带来显著性能提升（如YOLO World和OWLv2在合成豆荚花数据上分别提升+0.357和+0.362 mAP@0.5），且仅基于合成数据优化的提示结构能有效迁移到真实田间场景，无需人工标注即可大幅缩小零样本模型与监督检测器之间的差距。

**关键词**：视觉基础模型, 零样本目标检测, 提示优化框架, 开放词汇检测, 农业场景感知, 植物表型分析, 模型特定提示, 合成数据迁移, 跨域泛化能力, 组合优化

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09920v1) | [下载PDF](https://arxiv.org/pdf/2604.09920v1.pdf)

---

## [15. From UAV Imagery to Agronomic Reasoning: A Multimodal LLM Benchmark for Plant Phenotyping](https://arxiv.org/abs/2604.09907v1)

**作者**：Yu Wu, Guangzeng Han, Ibra Niang Niang 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

To improve crop genetics, high-throughput, effective and comprehensive phenotyping is a critical prerequisite. While such tasks were traditionally performed manually, recent advances in multimodal foundation models, especially in vision-language models (VLMs), have enabled more automated and robust phenotypic analysis. However, plant science remains a particularly challenging domain for foundation models because it requires domain-specific knowledge, fine-grained visual interpretation, and complex biological and agronomic reasoning. To address this gap, we develop PlantXpert, an evidence-grounded multimodal reasoning benchmark for soybean and cotton phenotyping. Our benchmark provides a structured and reproducible framework for agronomic adaptation of VLMs, and enables controlled comparison between base models and their domain-adapted counterparts. We constructed a dataset comprising 385 digital images and more than 3,000 benchmark samples spanning key plant science domains including disease, pest control, weed management, and yield. The benchmark can assess diverse capabilities including visual expertise, quantitative reasoning, and multi-step agronomic reasoning. A total of 11 state-of-the-art VLMs were evaluated. The results indicate that task-specific fine-tuning leads to substantial improvement in accuracy, with models such as Qwen3-VL-4B and Qwen3-VL-30B achieving up to 78%. At the same time, gains from model scaling diminish beyond a certain capacity, generalization across soybean and cotton remains uneven, and quantitative as well as biologically grounded reasoning continue to pose substantial challenges. These findings suggest that PlantXpert can serve as a foundation for assessing evidence-grounded agronomic reasoning and for advancing multimodal model development in plant science.

### 🤖 AI 总结

**一句话总结**：PlantXpert是一个用于大豆和棉花表型分析的多模态推理基准测试，通过385张图像和3000+样本评估11个VLM，表明任务微调可提升性能至78%，但模型扩展收益递减、跨作物泛化和定量推理仍具挑战。

**研究动机**：高通量作物表型分析对育种至关重要，但现有方法缺乏标准化评估框架；植物科学需要领域知识、细粒度视觉解释和复杂生物推理，对通用视觉语言模型构成特殊挑战。

**核心方法**：构建PlantXpert基准测试，包含385张UAV图像和3000+样本，涵盖疾病、害虫、杂草和产量等领域，评估11个SOTA VLM的视觉专业知识、定量推理和多步农艺推理能力，并对比基础模型与领域适配模型。

**主要结论**：任务特定微调可显著提升准确率至78%，但模型扩展收益递减；跨作物泛化不均衡，定量和生物学推理仍是主要挑战，表明PlantXpert可作为评估多模态模型农艺推理能力的基础框架。

**关键词**：植物表型分析, 农业推理, 无人机遥感, 领域适应, 大豆棉花, 定量推理, 视觉语言模型, 模型微调

**评分**：19

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09907v1) | [下载PDF](https://arxiv.org/pdf/2604.09907v1.pdf)

---

## [16. PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09903v1)

**作者**：Anh Thuan Tran, Jana Kosecka  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

3D Gaussian Splatting (3DGS) has recently unlocked real-time, high-fidelity novel view synthesis by representing scenes using explicit 3D primitives. However, traditional methods often require millions of Gaussians to capture complex scenes, leading to significant memory and storage demands. Recent approaches have addressed this issue through pruning and per-scene fine-tuning of Gaussian parameters, thereby reducing the model size while maintaining visual quality. These strategies typically rely on 2D images to compute important scores followed by scene-specific optimization. In this work, we introduce PointSplat, 3D geometry-driven prune-and-refine framework that bridges previously disjoint directions of gaussian pruning and transformer refinement. Our method includes two key components: (1) an efficient geometry-driven strategy that ranks Gaussians based solely on their 3D attributes, removing reliance on 2D images during pruning stage, and (2) a dual-branch encoder that separates, re-weights geometric and appearance to avoid feature imbalance. Extensive experiments on ScanNet++ and Replica across varying sparsity levels demonstrate that PointSplat consistently achieves competitive rendering quality and superior efficiency without additional per-scene optimization.

### 🤖 AI 总结

**一句话总结**：PointSplat提出一种3D几何驱动的剪枝与Transformer精化框架，通过仅基于3D属性排名高斯和双分支编码器设计，在大幅压缩模型的同时保持渲染质量。

**研究动机**：传统3DGS需要数百万高斯来表示复杂场景，导致高内存和存储消耗；现有剪枝方法依赖2D图像评分且需要逐场景微调，效率较低。

**核心方法**：该框架包含两个核心组件：(1) 3D几何驱动的剪枝策略，仅根据高斯的3D属性（如位置、尺度、协方差）进行重要性排名，摆脱对2D图像的依赖；(2) 双分支编码器将几何特征和外观特征分离并重新加权，避免特征不平衡问题。

**主要结论**：在ScanNet++和Replica数据集上的广泛实验表明，PointSplat在不同稀疏度水平下均能达到竞争力的渲染质量和优越的效率，且无需额外的逐场景优化。

**关键词**：3D高斯溅射, 几何驱动剪枝, 双分支编码器, 新视角合成, 神经渲染, 场景稀疏化, 实时渲染, 点云渲染

**评分**：28

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09903v1) | [下载PDF](https://arxiv.org/pdf/2604.09903v1.pdf)

---

## [17. Not Your Stereo-Typical Estimator: Combining Vision and Language for Volume Perception](https://arxiv.org/abs/2604.09886v1)

**作者**：Gautham Vinod, Bruce Coburn, Siddeshwar Raghavan 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM, eess.IV  
**发布时间**：2026-04-10

### 📄 论文摘要

Accurate volume estimation of objects from visual data is a long-standing challenge in computer vision with significant applications in robotics, logistics, and smart health. Existing methods often rely on complex 3D reconstruction pipelines or struggle with the ambiguity inherent in single-view images. To address these limitations, we introduce a new method that fuses implicit 3D cues from stereo vision with explicit prior knowledge from natural language text. Our approach extracts deep features from a stereo image pair and a descriptive text prompt that contains the object's class and an approximate volume, then integrates them using a simple yet effective projection layer into a unified, multi-modal representation for regression. We conduct extensive experiments on public datasets demonstrating that our text-guided approach significantly outperforms vision-only baselines. Our findings show that leveraging even simple textual priors can effectively guide the volume estimation task, paving the way for more context-aware visual measurement systems. Code: https://gitlab.com/viper-purdue/stereo-typical-estimator.

### 🤖 AI 总结

**一句话总结**：本文提出一种融合立体视觉和自然语言文本的多模态体积估计方法，通过联合学习视觉深度特征和文本先验知识来提高单视角图像中物体体积预测的准确性。

**研究动机**：现有体积估计方法依赖复杂3D重建流程或难以处理单视角图像的固有歧义性，需要探索更灵活且鲁棒的解决方案。

**核心方法**：该方法从立体图像对提取深度视觉特征，同时从包含物体类别和近似体积的文本提示中提取语义先验，通过投影层将两种模态融合为统一表示进行体积回归。

**主要结论**：大量实验表明，文本引导的方法显著优于纯视觉基线，证明即使是简单的文本先验也能有效指导体积估计任务，为构建更具备上下文感知能力的视觉测量系统提供了新思路。

**关键词**：体积估计, 立体视觉, 多模态学习, 文本先验, 深度特征, 投影层, 3D重建, 机器人, 视觉测量, 上下文感知

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09886v1) | [下载PDF](https://arxiv.org/pdf/2604.09886v1.pdf)

---

## [18. Topo-ADV: Generating Topology-Driven Imperceptible Adversarial Point Clouds](https://arxiv.org/abs/2604.09879v1)

**作者**：Gayathry Chandramana Krishnan Nampoothiry, Raghuram Venkatapuram, Anirban Ghosh 等 4 位作者  
**分类**：cs.CV, cs.CG  
**发布时间**：2026-04-10

### 📄 论文摘要

Deep neural networks for 3D point cloud understanding have achieved remarkable success in object classification and recognition, yet recent work shows that these models remain highly vulnerable to adversarial perturbations. Existing 3D attacks predominantly manipulate geometric properties such as point locations, curvature, or surface structure, implicitly assuming that preserving global shape fidelity preserves semantic content. In this work, we challenge this assumption and introduce the first topology-driven adversarial attack for point cloud deep learning. Our key insight is that the homological structure of a 3D object constitutes a previously unexplored vulnerability surface. We propose Topo-ADV, an end-to-end differentiable framework that incorporates persistent homology as an explicit optimization objective, enabling gradient-based manipulation of topological features during adversarial example generation. By embedding persistence diagrams through differentiable topological representations, our method jointly optimizes (i) a topology divergence loss that alters persistence, (ii) a misclassification objective, and (iii) geometric imperceptibility constraints that preserve visual plausibility. Experiments demonstrate that subtle topology-driven perturbations consistently achieve up to 100% attack success rates on benchmark datasets such as ModelNet40, ShapeNet Part, and ScanObjectNN using PointNet and DGCNN classifiers, while remaining geometrically indistinguishable from the original point clouds, beating state-of-the-art methods on various perceptibility metrics.

### 🤖 AI 总结

**一句话总结**：本文提出Topo-ADV，首个利用拓扑结构（持续同调）生成3D点云对抗样本的攻击方法，在保持视觉不可察觉的同时实现接近100%的攻击成功率。

**研究动机**：现有3D对抗攻击主要关注几何属性（位置、曲率等），假设保持全局形状保真度即保留语义内容，但作者认为3D对象的同调结构是一个未被探索的攻击面，可作为新的漏洞利用途径。

**核心方法**：Topo-ADV将持续同调嵌入可微分框架，通过联合优化三个目标：拓扑散度损失（改变持续图）、误分类损失和几何不可察觉约束，实现端到端的拓扑特征梯度操纵。

**主要结论**：在ModelNet40、ShapeNet Part和ScanObjectNN数据集上，Topo-ADV对PointNet和DGCNN分类器达到100%攻击成功率，同时在多个感知性指标上优于现有方法，证明了拓扑扰动是3D深度学习模型的有效攻击向量。

**关键词**：持久同调, 拓扑驱动, 3D深度学习, 可微分框架, 拓扑发散损失, 几何不可感知性, 同调结构, 点云分类

**评分**：32

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09879v1) | [下载PDF](https://arxiv.org/pdf/2604.09879v1.pdf)

---

## [19. DINO_4D: Semantic-Aware 4D Reconstruction](https://arxiv.org/abs/2604.09877v1)

**作者**：Yiru Yang, Zhuojie Wu, Quentin Marguet 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-04-10

### 📄 论文摘要

In the intersection of computer vision and robotic perception, 4D reconstruction of dynamic scenes serve as the critical bridge connecting low-level geometric sensing with high-level semantic understanding. We present DINO\_4D, introducing frozen DINOv3 features as structural priors, injecting semantic awareness into the reconstruction process to effectively suppress semantic drift during dynamic tracking. Experiments on the Point Odyssey and TUM-Dynamics benchmarks demonstrate that our method maintains the linear time complexity $O(T)$ of its predecessors while significantly improving Tracking Accuracy (APD) and Reconstruction Completeness. DINO\_4D establishes a new paradigm for constructing 4D World Models that possess both geometric precision and semantic understanding.

### 🤖 AI 总结

**一句话总结**：DINO_4D通过引入冻结的DINOv3特征作为语义结构先验，实现了同时具备几何精度和语义理解的4D动态场景重建。

**研究动机**：当前4D重建方法缺乏语义感知能力，导致动态跟踪过程中出现语义漂移问题，需要在几何重建基础上注入语义理解能力。

**核心方法**：使用预训练冻结的DINOv3特征作为结构先验，在4D重建过程中注入语义感知，有效抑制语义漂移，保持O(T)线性时间复杂度。

**主要结论**：在Point Odyssey和TUM-Dynamics基准上，DINO_4D显著提升了跟踪精度(APD)和重建完整性，为构建兼具几何精度和语义理解的4D世界模型提供了新范式。

**关键词**：4D重建, 动态场景, 语义感知, 结构先验, 语义漂移, 动态跟踪, 几何精度, 世界模型, 机器人感知

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09877v1) | [下载PDF](https://arxiv.org/pdf/2604.09877v1.pdf)

---

## [20. PAS: Estimating the target accuracy before domain adaptation](https://arxiv.org/abs/2604.09863v1)

**作者**：Raphaella Diniz, Jackson de Faria, Martin Ester  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

The goal of domain adaptation is to make predictions for unlabeled samples from a target domain with the help of labeled samples from a different but related source domain. The performance of domain adaptation methods is highly influenced by the choice of source domain and pre-trained feature extractor. However, the selection of source data and pre-trained model is not trivial due to the absence of a labeled validation set for the target domain and the large number of available pre-trained models. In this work, we propose PAS, a novel score designed to estimate the transferability of a source domain set and a pre-trained feature extractor to a target classification task before actually performing domain adaptation. PAS leverages the generalization power of pre-trained models and assesses source-target compatibility based on the pre-trained feature embeddings. We integrate PAS into a framework that indicates the most relevant pre-trained model and source domain among multiple candidates, thus improving target accuracy while reducing the computational overhead. Extensive experiments on image classification benchmarks demonstrate that PAS correlates strongly with actual target accuracy and consistently guides the selection of the best-performing pre-trained model and source domain for adaptation.

### 🤖 AI 总结

**一句话总结**：提出PAS评分方法，无需真实标签即可在域适应前预估源域和预训练模型对目标任务的迁移效果，从而优化选择。

**研究动机**：域适应方法的表现高度依赖源域和预训练特征提取器的选择，但目标域缺少标注数据，且候选模型数量庞大，导致选择困难。

**核心方法**：PAS利用预训练模型的泛化能力，基于特征嵌入评估源域与目标域的兼容性，集成到框架中自动推荐最优预训练模型和源域组合。

**主要结论**：图像分类基准实验表明PAS与实际目标准确率强相关，能持续指导选择表现最佳的预训练模型和源域适配方案。

**关键词**：PAS, Estimating, target, accuracy, before, domain, adaptation, goal

**评分**：14

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09863v1) | [下载PDF](https://arxiv.org/pdf/2604.09863v1.pdf)

---

## [21. Do vision models perceive illusory motion in static images like humans?](https://arxiv.org/abs/2604.09853v1)

**作者**：Isabella Elaine Rosario, Fan L. Cheng, Zitang Sun 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Understanding human motion processing is essential for building reliable, human-centered computer vision systems. Although deep neural networks (DNNs) achieve strong performance in optical flow estimation, they remain less robust than humans and rely on fundamentally different computational strategies. Visual motion illusions provide a powerful probe into these mechanisms, revealing how human and machine vision align or diverge. While recent DNN-based motion models can reproduce dynamic illusions such as reverse-phi, it remains unclear whether they can perceive illusory motion in static images, exemplified by the Rotating Snakes illusion. We evaluate several representative optical flow models on Rotating Snakes and show that most fail to generate flow fields consistent with human perception. Under simulated conditions mimicking saccadic eye movements, only the human-inspired Dual-Channel model exhibits the expected rotational motion, with the closest correspondence emerging during the saccade simulation. Ablation analyses further reveal that both luminance-based and higher-order color--feature--based motion signals contribute to this behavior and that a recurrent attention mechanism is critical for integrating local cues. Our results highlight a substantial gap between current optical-flow models and human visual motion processing, and offer insights for developing future motion-estimation systems with improved correspondence to human perception and human-centric AI.

### 🤖 AI 总结

**一句话总结**：论文评估了主流光流模型在静态图像中感知旋转蛇错觉的能力，发现仅有受人类启发的双通道模型能在模拟扫视运动时产生与人类一致的旋转运动感知。

**研究动机**：理解人类运动感知机制对构建可靠、以人为中心的计算机视觉系统至关重要，当前深度神经网络虽在光流估计上表现优异，但采用与人类根本不同的计算策略且鲁棒性不足。

**核心方法**：研究者在旋转蛇错觉上测试多类光流模型，通过模拟扫视眼动条件评估感知效果，并进行消融实验分析亮度信号、高阶颜色特征信号及递归注意力机制的贡献。

**主要结论**：大多数现有光流模型无法产生与人类感知一致的运动场，仅双通道模型在扫视模拟中展现预期的旋转运动，揭示了当前模型与人类视觉运动处理之间存在显著差距，为开发更符合人类感知的运动估计系统提供方向。

**关键词**：光流估计, 视觉运动错觉, 旋转蛇错觉, 扫视眼动模拟, 双通道模型, 递归注意力机制, 人类视觉感知对齐, 运动特征信号, 人类中心AI, 光学流模型评测

**评分**：22

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09853v1) | [下载PDF](https://arxiv.org/pdf/2604.09853v1.pdf)

---

## cs.LG

## [22. SLM Finetuning for Natural Language to Domain Specific Code Generation in Production](https://arxiv.org/abs/2604.09952v1)

**作者**：Renjini R. Nair, Damian K. Kowalczyk, Marco Gaudesi 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Many applications today use large language models for code generation; however, production systems have strict latency requirements that can be difficult to meet with large models. Small language models with a few billion parameters are resource efficient but may suffer from limited reasoning, hallucinations, or poor retention of longer context. Fine tuning improves task specific accuracy by embedding domain knowledge directly into model weights, reducing reliance on runtime context. We previously implemented a baseline natural language to code generation approach using a retrieval augmented generation pipeline that dynamically selected few shot examples to embed domain specific language context for a large language model. In this study, we evaluate small language models for generating domain specific language from natural language by fine tuning variants of Mistral and other models on a dataset of natural language code pairs. Our results show that the fine-tuned models achieve improved performance and latency on test datasets compared to larger models. We also demonstrate that the trained model can be further fine-tuned for customer specific scenarios without degrading general performance, helping resolve production issues. Load testing followed by production deployment confirmed optimal performance in terms of latency and quality. These findings demonstrate that task specific fine tuning with small language models provides an efficient, faster, and cost-effective alternative to large language models for domain specific language generation.

### 🤖 AI 总结

**一句话总结**：通过在自然语言到代码配对数据集上微调小型语言模型（如Mistral变体），实现了比大型模型更优的性能和延迟，用于生产环境中的领域特定代码生成。

**研究动机**：生产系统对延迟有严格要求，大型语言模型难以满足，而小型语言模型虽然资源高效，但存在推理能力有限、幻觉和上下文保留不足等问题。

**核心方法**：对Mistral等小型语言模型进行任务特定微调，在自然语言代码对数据集上训练，并将其与基于检索增强生成（RAG）的大型模型基线进行对比评估。

**主要结论**：微调后的小型语言模型在测试数据集上实现了性能和延迟的改进，可进一步针对客户特定场景进行微调而不影响通用性能，证明了任务特定微调是领域特定代码生成的高效、快速且经济的方法。

**关键词**：SLM, Finetuning, Natural, Language, Domain, Specific, Code, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09952v1) | [下载PDF](https://arxiv.org/pdf/2604.09952v1.pdf)

---

## [23. Vestibular reservoir computing](https://arxiv.org/abs/2604.09943v1)

**作者**：Smita Deb, Shirin Panahi, Mulugeta Haile 等 4 位作者  
**分类**：cs.LG, nlin.CD, physics.data-an  
**发布时间**：2026-04-10

### 📄 论文摘要

Reservoir computing (RC) is a computational framework known for its training efficiency, making it ideal for physical hardware implementations. However, realizing the complex interconnectivity of traditional reservoirs in physical systems remains a significant challenge. This paper proposes a physical RC scheme inspired by the biological vestibular system. To overcome hardware complexity, we introduce a designed uncoupled topology and demonstrate that it achieves performance comparable to fully coupled networks. We theoretically analyze the difference between these topologies by deriving a memory capacity formula for linear reservoirs, identifying specific conditions where both configurations yield equivalent memory. These analytical results are demonstrated to approximately hold for nonlinear reservoir systems. Furthermore, we systematically examine the impact of reservoir size on predictive statistics and memory capacity. Our findings suggest that uncoupled reservoir architectures offer a mathematically sound and practically feasible pathway for efficient physical reservoir computing.

### 🤖 AI 总结

**一句话总结**：提出一种受生物前庭系统启发的物理储备池计算方案，使用解耦拓扑结构降低硬件复杂度，同时保持与全耦合网络相当的性能。

**研究动机**：传统储备池计算虽训练效率高，但在物理硬件实现中面临复杂互连的挑战，需要寻找更易实现的架构方案。

**核心方法**：设计一种解耦拓扑结构替代传统的全耦合网络，通过理论分析推导出线性储备池的记忆容量公式，确定两种拓扑等效的具体条件，并在非线性系统中验证。

**主要结论**：解耦储备池架构在数学上严格等价于全耦合网络，且在大规模系统中可达到相近性能，为高效物理储备池计算提供了可行路径。

**关键词**：储备池计算, 物理储备池计算, 前庭系统, 非耦合拓扑, 记忆容量, 网络拓扑, 硬件复杂度, 训练效率, 非线性储备池, 预测统计

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09943v1) | [下载PDF](https://arxiv.org/pdf/2604.09943v1.pdf)

---

## [24. A Hybrid Intelligent Framework for Uncertainty-Aware Condition Monitoring of Industrial Systems](https://arxiv.org/abs/2604.09932v1)

**作者**：Maryam Ahang, Todd Charter, Masoud Jalayer 等 4 位作者  
**分类**：cs.LG, cs.AI, eess.SP  
**发布时间**：2026-04-10

### 📄 论文摘要

Hybrid approaches that combine data-driven learning with physics-based insight have shown promise for improving the reliability of industrial condition monitoring. This work develops a hybrid condition monitoring framework that integrates primary sensor measurements, lagged temporal features, and physics-informed residuals derived from nominal surrogate models. Two hybrid integration strategies are examined. The first is a feature-level fusion approach that augments the input space with residual and temporal information. The second is a model-level ensemble approach in which machine learning classifiers trained on different feature types are combined at the decision level. Both hybrid approaches of the condition monitoring framework are evaluated on a continuous stirred-tank reactor (CSTR) benchmark using several machine learning models and ensemble configurations. Both feature-level and model-level hybridization improve diagnostic accuracy relative to single-source baselines, with the best model-level ensemble achieving a 2.9\% improvement over the best baseline ensemble. To assess predictive reliability, conformal prediction is applied to quantify coverage, prediction-set size, and abstention behavior. The results show that hybrid integration enhances uncertainty management, producing smaller and well-calibrated prediction sets at matched coverage levels. These findings demonstrate that lightweight physics-informed residuals, temporal augmentation, and ensemble learning can be combined effectively to improve both accuracy and decision reliability in nonlinear industrial systems.

### 🤖 AI 总结

**一句话总结**：提出一种结合物理模型残差和时序特征与机器学习的混合工业系统状态监测框架，通过特征级融合和模型级集成两种策略提升诊断准确性和不确定性量化能力。

**研究动机**：单一数据驱动或物理模型方法在复杂工业系统监测中存在局限性，需要融合领域知识与数据驱动学习的优势以提高监测可靠性和可解释性。

**核心方法**：开发特征级融合（将残差和时序特征与主传感器数据结合）和模型级集成（不同特征类型训练分类器后在决策层组合）两种混合策略，并应用保形预测进行不确定性量化评估。

**主要结论**：在CSTR基准上的实验表明，两种混合方法均优于单一来源基线，最佳模型级集成获得2.9%的准确率提升，且混合集成产生更小且校准良好的预测集，有效增强不确定性和可靠性管理。

**关键词**：状态监测, 不确定性量化, 混合学习, 物理信息模型, 特征融合, 模型集成, 共形预测, 工业系统, 故障诊断, 残差分析

**评分**：18

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09932v1) | [下载PDF](https://arxiv.org/pdf/2604.09932v1.pdf)

---

## [25. K-STEMIT: Knowledge-Informed Spatio-Temporal Efficient Multi-Branch Graph Neural Network for Subsurface Stratigraphy Thickness Estimation from Radar Data](https://arxiv.org/abs/2604.09922v1)

**作者**：Zesheng Liu, Maryam Rahnemoonfar  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Subsurface stratigraphy contains important spatio-temporal information about accumulation, deformation, and layer formation in polar ice sheets. In particular, variations in internal ice layer thickness provide valuable constraints for snow mass balance estimation and projections of ice sheet change. Although radar sensors can capture these layered structures as depth-resolved radargrams, convolutional neural networks applied directly to radar images are often sensitive to speckle noise and acquisition artifacts. In addition, purely data-driven methods may underuse physical knowledge, leading to unrealistic thickness estimates under spatial or temporal extrapolation. To address these challenges, we develop K-STEMIT, a novel knowledge-informed, efficient, multi-branch spatio-temporal graph neural network that combines a geometric framework for spatial learning with temporal convolution to capture temporal dynamics, and incorporates physical data synchronized from the Model Atmospheric Regional physical weather model. An adaptive feature fusion strategy is employed to dynamically combine features learned from different branches. Extensive experiments have been conducted to compare K-STEMIT against current state-of-the-art methods in both knowledge-informed and non-knowledge-informed settings, as well as other existing methods. Results show that K-STEMIT consistently achieves the highest accuracy while maintaining near-optimal efficiency. Most notably, incorporating adaptive feature fusion and physical priors reduces the root mean-squared error by 21.01% with negligible additional cost compared to its conventional multi-branch variants. Additionally, our proposed K-STEMIT achieves consistently lower per-year relative MAE, enabling reliable, continuous spatiotemporal assessment of snow accumulation variability across large spatial regions.

### 🤖 AI 总结

**一句话总结**：K-STEMIT是一种融合物理先验知识的多分支时空图神经网络，能够从雷达数据中高精度、高效率地估计极地冰盖地下地层厚度。

**研究动机**：现有雷达图像处理方法对噪声敏感，纯数据驱动方法缺乏物理约束导致外推时估计不现实，而冰层厚度变化对雪量平衡和冰盖变化预测具有重要科学价值。

**核心方法**：K-STEMIT结合几何框架进行空间学习、时间卷积捕捉动态变化，并融入大气区域物理天气预报模型的同步数据，采用自适应特征融合策略动态整合多分支特征。

**主要结论**：K-STEMIT在知识驱动和非知识驱动设置下均达到最高精度，RMSE降低21.01%且计算成本可忽略，并可实现大空间区域雪积累变异性的可靠连续时空评估。

**关键词**：K-STEMIT, Knowledge-Informed, Spatio-Temporal, Efficient, Multi-Branch, Graph, Neural, Network

**评分**：21

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09922v1) | [下载PDF](https://arxiv.org/pdf/2604.09922v1.pdf)

---

## [26. Regularized Entropy Information Adaptation with Temporal-Awareness Networks for Simultaneous Speech Translation](https://arxiv.org/abs/2604.09916v1)

**作者**：Joseph Liu, Nameer Hirschkind, Xiao Yu 等 4 位作者  
**分类**：cs.LG, eess.AS  
**发布时间**：2026-04-10

### 📄 论文摘要

Simultaneous Speech Translation (SimulST) requires balancing high translation quality with low latency. Recent work introduced REINA, a method that trains a Read/Write policy based on estimating the information gain of reading more audio. However, we find that information-based policies often lack temporal context, leading the policy to bias itself toward reading most of the audio before starting to write. We improve REINA using two distinct strategies: a supervised alignment network (REINA-SAN) and a timestep-augmented network (REINA-TAN). Our results demonstrate that while both methods significantly outperform the baseline and resolve stability issues, REINA-TAN provides a slightly superior Pareto frontier for streaming efficiency, whereas REINA-SAN offers more robustness against 'read loops'. Applied to Whisper, both methods improve the pareto frontier of streaming efficiency as measured by Normalized Streaming Efficiency (NoSE) scores up to 7.1% over existing competitive baselines.

### 🤖 AI 总结

**一句话总结**：本文提出REINA-SAN和REINA-TAN两种时间感知网络改进方法，解决同时语音翻译中信息增益策略缺乏时间上下文的问题，在Whisper模型上实现NoSE分数最高7.1%的提升。

**研究动机**：现有基于信息增益的REINA方法在同时语音翻译中存在时间上下文缺失问题，导致策略偏向于在写入前读取大部分音频，产生'读取循环'和稳定性问题。

**核心方法**：提出两种改进策略：REINA-SAN通过监督对齐网络增强时间感知能力，REINA-TAN通过时间步增强网络改善流媒体效率；两种方法均在保持翻译质量的同时优化延迟-质量权衡。

**主要结论**：实验表明REINA-TAN在流媒体效率Pareto前沿上略优，REINA-SAN对读取循环更具鲁棒性；应用于Whisper后，NoSE分数相比现有基线提升达7.1%。

**关键词**：同时语音翻译, 读写策略, 信息增益, 时间感知网络, 流式效率, 帕累托前沿, 监督对齐网络, 低延迟, 流式翻译

**评分**：13

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09916v1) | [下载PDF](https://arxiv.org/pdf/2604.09916v1.pdf)

---

## [27. Last-Iterate Convergence of Randomized Kaczmarz and SGD with Greedy Step Size](https://arxiv.org/abs/2604.09909v1)

**作者**：Michał Dereziński, Xiaoyu Dong  
**分类**：cs.LG, math.NA, math.OC, stat.ML  
**发布时间**：2026-04-10

### 📄 论文摘要

We study last-iterate convergence of SGD with greedy step size over smooth quadratics in the interpolation regime, a setting which captures the classical Randomized Kaczmarz algorithm as well as other popular iterative linear system solvers. For these methods, we show that the $t$-th iterate attains an $O(1/t^{3/4})$ convergence rate, addressing a question posed by Attia, Schliserman, Sherman, and Koren, who gave an $O(1/t^{1/2})$ guarantee for this setting. In the proof, we introduce the family of stochastic contraction processes, whose behavior can be described by the evolution of a certain deterministic eigenvalue equation, which we analyze via a careful discrete-to-continuous reduction.

### 🤖 AI 总结

**一句话总结**：本文证明了带贪婪步长的随机梯度下降(SGD)和随机Kaczmarz算法在平滑二次函数插值设定下达成了 O(1/t^{3/4}) 的最后迭代收敛率，相比之前的 O(1/t^{1/2}) 有显著提升。

**研究动机**：现有文献对于这类方法的最后迭代收敛率仅达到 O(1/t^{1/2})，Attia等人提出了能否改进这一结果的问题，本文旨在解决这一理论差距。

**核心方法**：通过引入随机收缩过程族来描述算法行为，利用确定性特征值方程刻画其演化，并采用精细的离散到连续降维技术进行分析。

**主要结论**：成功证明 t 步迭代可达 O(1/t^{3/4}) 收敛率，完成了 Attia 等人提出的开放问题，揭示了贪婪步长选择策略在提升收敛速率方面的理论优势。

**关键词**：随机梯度下降, 贪婪步长策略, 末次迭代收敛, 插值机制, 平滑二次优化, 迭代线性系统求解, 收敛率分析, 随机收缩过程, 离散连续约化

**评分**：15

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09909v1) | [下载PDF](https://arxiv.org/pdf/2604.09909v1.pdf)

---

## [28. SemEnrich: Self-Supervised Semantic Enrichment of Radiology Reports for Vision-Language Learning](https://arxiv.org/abs/2604.09887v1)

**作者**：Halil Ibrahim Gulluk, Olivier Gevaert  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Medical vision-language datasets are often limited in size and biased toward negative findings, as clinicians report abnormalities mostly but might omit some positive/neutral findings because they might be considered as irrelevant to the patient's condition. We propose a self-supervised data enrichment method that leverages semantic clustering of report sentences. Then we enrich the findings in the medical reports in the training set by adding positive/neutral observations from different clusters in a self-supervised manner. Our approach yields consistent gains in supervised fine-tuning (5.63%, 3.04%, 7.40%, 5.30%, 7.47% average gains on COMET score, Bert score, Sentence Bleu, CheXbert-F1 and RadGraph-F1 scores respectively). Ablation studies confirm that improvements stem from semantic clustering rather than random augmentation. Furthermore, we introduce a way to incorporate semantic cluster information into the reward design for GRPO training, which leads to further performance gains (2.78%, 3.14%, 12.80% average gains on COMET score, Bert score and Sentence Bleu scores respectively). We share our code at https://anonymous.4open.science/r/SemEnrich-75CF

### 🤖 AI 总结

**一句话总结**：SemEnrich是一种自监督语义增强方法，通过对放射学报告句子进行语义聚类，将不同聚类中的正向/中性观察添加到训练数据中，从而提升医学视觉语言模型的性能。

**研究动机**：医学视觉语言数据集规模有限且存在负向偏置，因为临床医生通常报告异常发现而遗漏正向或中性观察，导致模型训练数据不均衡。

**核心方法**：该方法首先对报告句子进行语义聚类，然后以自监督方式从不同聚类中提取正向/中性观察来丰富训练数据；此外还将语义聚类信息融入GRPO训练的奖励设计中。

**主要结论**：在监督微调中取得5.63%至7.47%的平均提升（AUC分数），消融实验验证了语义聚类的有效性；结合GRPO训练后进一步获得2.78%至12.80%的性能增益。

**关键词**：语义聚类, 医学报告丰富化, 自监督数据增强, 放射学报告, 视觉-语言学习, 监督微调, 奖励设计, SemEnrich

**评分**：20

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09887v1) | [下载PDF](https://arxiv.org/pdf/2604.09887v1.pdf)

---

## [29. Efficient Personalization of Generative User Interfaces](https://arxiv.org/abs/2604.09876v1)

**作者**：Yi-Hao Peng, Samarth Das, Jeffrey P. Bigham 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.CV, cs.HC  
**发布时间**：2026-04-10

### 📄 论文摘要

Generative user interfaces (UIs) create new opportunities to adapt interfaces to individual users on demand, but personalization remains difficult because desirable UI properties are subjective, hard to articulate, and costly to infer from sparse feedback. We study this problem through a new dataset in which 20 trained designers each provide pairwise judgments over the same 600 generated UIs, enabling direct analysis of preference divergence. We find substantial disagreement across designers (average kappa = 0.25), and written rationales reveal that even when designers appeal to similar concepts such as hierarchy or cleanliness, designers differ in how they define, prioritize, and apply those concepts. Motivated by these findings, we develop a sample-efficient personalization method that represents a new user in terms of prior designers rather than a fixed rubric of design concepts. In a technical evaluation, our preference model outperforms both a pretrained UI evaluator and a larger multimodal model, and scales better with additional feedback. When used to personalize generation, it also produces interfaces preferred by 12 new designers over baseline approaches, including direct user prompting. Our findings suggest that lightweight preference elicitation can serve as a practical foundation for personalized generative UI systems.

### 🤖 AI 总结

**一句话总结**：提出一种基于设计师偏好而非固定设计规则的生成式UI高效个性化方法。

**研究动机**：生成式UI个性化面临挑战，因为用户偏好具有主观性、难以明确表达，且从稀疏反馈中推断成本高昂。

**核心方法**：通过收集20位设计师对600个生成UI的成对偏好判断构建数据集，训练偏好模型将新用户表示为先前设计师的组合，实现样本高效的用户适应。

**主要结论**：该方法在偏好预测和UI生成质量上均优于预训练评估器和更大规模多模态模型，证明轻量级偏好获取可作为个性化生成式UI系统的实用基础。

**关键词**：生成式UI, 个性化, 偏好建模, 成对判断, 设计评估, 多模态模型, 界面生成, 概念对齐, 样本效率

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09876v1) | [下载PDF](https://arxiv.org/pdf/2604.09876v1.pdf)

---

## [30. Relational Preference Encoding in Looped Transformer Internal States](https://arxiv.org/abs/2604.09870v1)

**作者**：Jan Kirin  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

We investigate how looped transformers encode human preference in their internal iteration states. Using Ouro-2.6B-Thinking, a 2.6B-parameter looped transformer with iterative refinement, we extract hidden states from each loop iteration and train lightweight evaluator heads (~5M parameters) to predict human preference on the Anthropic HH-RLHF dataset. Our pairwise evaluator achieves 95.2% test accuracy on 8,552 unseen examples, surpassing a full-batch L-BFGS probe (84.5%) while the base model remains completely frozen.   Our central finding is that loop states encode preference predominantly relationally: a linear probe on pairwise differences achieves 84.5%, the best nonlinear independent evaluator reaches only 65% test accuracy, and linear independent classification scores 21.75%, below chance and with inverted polarity. Interpreted precisely, the evaluator functions as a model-internal consistency probe, measuring how stably Ouro's own learned value system organizes its representations rather than how well it predicts noisy human annotations.   We also document a systematic architecture search that established a genuine 70% ceiling for independent scoring, and show how the 50% argument-swap protocol required to prevent degenerate pairwise solutions deflated pairwise training metrics by about 31 points at peak, creating the false appearance that pairwise and pointwise evaluators shared the same ceiling.   Finally, we show that a cosine learning-rate dead zone at epoch 2 accidentally acted as early stopping, preserving the generalization peak before overfitting degraded test accuracy from 95.2% to 62.4% by epoch 5. Cross-epoch flip-test analysis shows that antisymmetry correlation remains stable while strict sign-flip rate mainly tracks scorer bias. We propose the flip test as a mandatory diagnostic for pairwise preference evaluators.

### 🤖 AI 总结

**一句话总结**：循环Transformer（Ouro-2.6B-Thinking）的内部状态通过关系式编码偏好信息，成对差异探测准确率达84.5%，完整成对评估器达95.2%，远超独立评分70%的上限。

**研究动机**：理解循环Transformer如何在其迭代状态中组织和编码人类偏好，对于改进RLHF和奖励模型设计具有重要意义。

**核心方法**：从Ouro模型的每个循环迭代中提取隐藏状态，训练轻量级评估头（约5M参数）预测人类偏好，并在Anthropic HH-RLHF数据集上评估，同时探索架构搜索确立独立评分上限。

**主要结论**：循环状态偏好编码以关系式为主，成对差异探测远超独立评分，且余弦学习率死区意外起到早停作用保留了泛化峰值；论文提出flip test作为成对偏好评估器的强制诊断工具。

**关键词**：迭代细化, 线性探针, 关系编码, 偏好预测, 轻量级评估器, 成对评估, 内部状态, 一致性探测

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09870v1) | [下载PDF](https://arxiv.org/pdf/2604.09870v1.pdf)

---

