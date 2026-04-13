# arXiv AI 论文日报 | 2026-04-13

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (9 篇)
- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (11 篇)
- [cs.AI](#csAI) (3 篇)

---

## cs.AI

## [1. Process Reward Agents for Steering Knowledge-Intensive Reasoning](https://arxiv.org/abs/2604.09482v1)

**作者**：Jiwoong Sohn, Tomasz Sternal, Kenneth Styppa 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Reasoning in knowledge-intensive domains remains challenging as intermediate steps are often not locally verifiable: unlike math or code, evaluating step correctness may require synthesizing clues across large external knowledge sources. As a result, subtle errors can propagate through reasoning traces, potentially never to be detected. Prior work has proposed process reward models (PRMs), including retrieval-augmented variants, but these methods operate post hoc, scoring completed trajectories, which prevents their integration into dynamic inference procedures. Here, we introduce Process Reward Agents (PRA), a test-time method for providing domain-grounded, online, step-wise rewards to a frozen policy. In contrast to prior retrieval-augmented PRMs, PRA enables search-based decoding to rank and prune candidate trajectories at every generation step. Experiments on multiple medical reasoning benchmarks demonstrate that PRA consistently outperforms strong baselines, achieving 80.8% accuracy on MedQA with Qwen3-4B, a new state of the art at the 4B scale. Importantly, PRA generalizes to unseen frozen policy models ranging from 0.5B to 8B parameters, improving their accuracy by up to 25.7% without any policy model updates. More broadly, PRA suggests a paradigm in which frozen reasoners are decoupled from domain-specific reward modules, allowing the deployment of new backbones in complex domains without retraining.

### 🤖 AI 总结

**一句话总结**：Reasoning in knowledge-intensive domains remains challenging as intermediate steps are often not locally verifiable: unlike math or code, evaluating step correctness may require synthesizing clues acr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Process, Reward, Steering, Knowledge-Intensive, Reasoning, domains, remains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09482v1) | [下载PDF](https://arxiv.org/pdf/2604.09482v1.pdf)

---

## [2. E3-TIR: Enhanced Experience Exploitation for Tool-Integrated Reasoning](https://arxiv.org/abs/2604.09455v1)

**作者**：Weiyang Guo, Zesheng Shi, Liye Zhao 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

While Large Language Models (LLMs) have demonstrated significant potential in Tool-Integrated Reasoning (TIR), existing training paradigms face significant limitations: Zero-RL suffers from inefficient exploration and mode degradation due to a lack of prior guidance, while SFT-then-RL is limited by high data costs and capability plateaus caused by low-entropy collapse. To address these challenges, we propose E3-TIR (Enhanced Experience Exploitation), a warm-up paradigm for the early stages of agent training. Specifically, we formulate training as the dynamic integration of three experience types: Expert Prefixes, Expert Guided, and Self-Exploration. By executing diverse branching exploration around expert "anchors" and employing a mix policy optimization mechanism, we effectively mitigate distribution shifts and resolve optimization conflicts arising from shared prefixes. Our method dynamically adapts the model's knowledge boundaries, effectively balancing exploration diversity with training efficiency.Experimental results demonstrate that E3-TIR achieves a 6 performance improvement over traditional paradigms on tool-use tasks, while requiring less than 10 of the synthetic data. Furthermore, in terms of ROI, a comprehensive metric integrating performance, data cost, and training efficiency we achieve a 1.46x gain compared to baselines. Code is available at https://github.com/yuki-younai/E3-TIR.

### 🤖 AI 总结

**一句话总结**：While Large Language Models (LLMs) have demonstrated significant potential in Tool-Integrated Reasoning (TIR), existing training paradigms face significant limitations: Zero-RL suffers from inefficien...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：E3-TIR, Enhanced, Experience, Exploitation, Tool-Integrated, Reasoning, While, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09455v1) | [下载PDF](https://arxiv.org/pdf/2604.09455v1.pdf)

---

## [3. Do We Really Need to Approach the Entire Pareto Front in Many-Objective Bayesian Optimisation?](https://arxiv.org/abs/2604.09417v1)

**作者**：Chao Jiang, Jingyu Huang, Miqing Li  
**分类**：cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Many-objective optimisation, a subset of multi-objective optimisation, involves optimisation problems with more than three objectives. As the number of objectives increases, the number of solutions needed to adequately represent the entire Pareto front typically grows substantially. This makes it challenging, if not infeasible, to design a search algorithm capable of effectively exploring the entire Pareto front. This difficulty is particularly acute in the Bayesian optimisation paradigm, where sample efficiency is critical and only a limited number of solutions (often a few hundred) are evaluated. Moreover, after the optimisation process, the decision-maker eventually selects just one solution for deployment, regardless of how many high-quality, diverse solutions are available. In light of this, we argue an idea that under a very limited evaluation budget, it may be more useful to focus on finding a single solution of the highest possible quality for the decision-maker, rather than aiming to approximate the entire Pareto front as existing many-/multi-objective Bayesian optimisation methods typically do. Bearing this idea in mind, this paper proposes a \underline{s}ingle \underline{p}oint-based \underline{m}ulti-\underline{o}bjective search framework (SPMO) that aims to improve the quality of solutions along a direction that leads to a good tradeoff between objectives. Within SPMO, we present a simple acquisition function, called expected single-point improvement (ESPI), working under both noiseless and noisy scenarios. We show that ESPI can be optimised effectively with gradient-based methods via the sample average approximation (SAA) approach and theoretically prove its convergence guarantees under the SAA. We also empirically demonstrate that the proposed SPMO is computationally tractable and outperforms state-of-the-arts on a wide range of benchmark and real-world problems.

### 🤖 AI 总结

**一句话总结**：Many-objective optimisation, a subset of multi-objective optimisation, involves optimisation problems with more than three objectives. As the number of objectives increases, the number of solutions ne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, We, Really, Need, Approach, Entire, Pareto, Front

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09417v1) | [下载PDF](https://arxiv.org/pdf/2604.09417v1.pdf)

---

## cs.CL

## [4. Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism](https://arxiv.org/abs/2604.09544v1)

**作者**：Hadas Orgad, Boyi Wei, Kaden Zheng 等 7 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Large language models (LLMs) undergo alignment training to avoid harmful behaviors, yet the resulting safeguards remain brittle: jailbreaks routinely bypass them, and fine-tuning on narrow domains can induce ``emergent misalignment'' that generalizes broadly. Whether this brittleness reflects a fundamental lack of coherent internal organization for harmfulness remains unclear. Here we use targeted weight pruning as a causal intervention to probe the internal organization of harmfulness in LLMs. We find that harmful content generation depends on a compact set of weights that are general across harm types and distinct from benign capabilities. Aligned models exhibit a greater compression of harm generation weights than unaligned counterparts, indicating that alignment reshapes harmful representations internally--despite the brittleness of safety guardrails at the surface level. This compression explains emergent misalignment: if weights of harmful capabilities are compressed, fine-tuning that engages these weights in one domain can trigger broad misalignment. Consistent with this, pruning harm generation weights in a narrow domain substantially reduces emergent misalignment. Notably, LLMs harmful generation capability is dissociated from how they recognize and explain such content. Together, these results reveal a coherent internal structure for harmfulness in LLMs that may serve as a foundation for more principled approaches to safety.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) undergo alignment training to avoid harmful behaviors, yet the resulting safeguards remain brittle: jailbreaks routinely bypass them, and fine-tuning on narrow domains can...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Large, Language, Models, Generate, Harmful, Content, Distinct, Unified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09544v1) | [下载PDF](https://arxiv.org/pdf/2604.09544v1.pdf)

---

## [5. Case-Grounded Evidence Verification: A Framework for Constructing Evidence-Sensitive Supervision](https://arxiv.org/abs/2604.09537v1)

**作者**：Soroosh Tayebi Arasteh, Mehdi Joodaki, Mahshad Lotfinia 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.IR, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Evidence-grounded reasoning requires more than attaching retrieved text to a prediction: a model should make decisions that depend on whether the provided evidence supports the target claim. In practice, this often fails because supervision is weak, evidence is only loosely tied to the claim, and evaluation does not test evidence dependence directly. We introduce case-grounded evidence verification, a general framework in which a model receives a local case context, external evidence, and a structured claim, and must decide whether the evidence supports the claim for that case. Our key contribution is a supervision construction procedure that generates explicit support examples together with semantically controlled non-support examples, including counterfactual wrong-state and topic-related negatives, without manual evidence annotation. We instantiate the framework in radiology and train a standard verifier on the resulting support task. The learned verifier substantially outperforms both case-only and evidence-only baselines, remains strong under correct evidence, and collapses when evidence is removed or swapped, indicating genuine evidence dependence. This behavior transfers across unseen evidence articles and an external case distribution, though performance degrades under evidence-source shift and remains sensitive to backbone choice. Overall, the results suggest that a major bottleneck in evidence grounding is not only model capacity, but the lack of supervision that encodes the causal role of evidence.

### 🤖 AI 总结

**一句话总结**：Evidence-grounded reasoning requires more than attaching retrieved text to a prediction: a model should make decisions that depend on whether the provided evidence supports the target claim. In practi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Case-Grounded, Evidence, Verification, Framework, Constructing, Evidence-Sensitive, Supervision, Evidence-grounded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09537v1) | [下载PDF](https://arxiv.org/pdf/2604.09537v1.pdf)

---

## [6. Many Ways to Be Fake: Benchmarking Fake News Detection Under Strategy-Driven AI Generation](https://arxiv.org/abs/2604.09514v1)

**作者**：Xinyu Wang, Sai Koneru, Wenbo Zhang 等 6 位作者  
**分类**：cs.CL, cs.HC  
**发布时间**：2026-04-10

### 📄 论文摘要

Recent advances in large language models (LLMs) have enabled the large-scale generation of highly fluent and deceptive news-like content. While prior work has often treated fake news detection as a binary classification problem, modern fake news increasingly arises through human-AI collaboration, where strategic inaccuracies are embedded within otherwise accurate and credible narratives. These mixed-truth cases represent a realistic and consequential threat, yet they remain underrepresented in existing benchmarks. To address this gap, we introduce MANYFAKE, a synthetic benchmark containing 6,798 fake news articles generated through multiple strategy-driven prompting pipelines that capture many ways fake news can be constructed and refined. Using this benchmark, we evaluate a range of state-of-the-art fake news detectors. Our results show that even advanced reasoning-enabled models approach saturation on fully fabricated stories, but remain brittle when falsehoods are subtle, optimized, and interwoven with accurate information.

### 🤖 AI 总结

**一句话总结**：Recent advances in large language models (LLMs) have enabled the large-scale generation of highly fluent and deceptive news-like content. While prior work has often treated fake news detection as a bi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Many, Ways, Fake, Benchmarking, News, Detection, Under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09514v1) | [下载PDF](https://arxiv.org/pdf/2604.09514v1.pdf)

---

## [7. You Can't Fight in Here! This is BBS!](https://arxiv.org/abs/2604.09501v1)

**作者**：Richard Futrell, Kyle Mahowald  
**分类**：cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

Norm, the formal theoretical linguist, and Claudette, the computational language scientist, have a lovely time discussing whether modern language models can inform important questions in the language sciences. Just as they are about to part ways until they meet again, 25 of their closest friends show up -- from linguistics, neuroscience, cognitive science, psychology, philosophy, and computer science. We use this discussion to highlight what we see as some common underlying issues: the String Statistics Strawman (the mistaken idea that LMs can't be linguistically competent or interesting because they, like their Markov model predecessors, are statistical models that learn from strings) and the As Good As it Gets Assumption (the idea that LM research as it stands in 2026 is the limit of what it can tell us about linguistics). We clarify the role of LM-based work for scientific insights into human language and advocate for a more expansive research program for the language sciences in the AI age, one that takes on the commentators' concerns in order to produce a better and more robust science of both human language and of LMs.

### 🤖 AI 总结

**一句话总结**：Norm, the formal theoretical linguist, and Claudette, the computational language scientist, have a lovely time discussing whether modern language models can inform important questions in the language ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can't, Fight, Here!, BBS!, Norm, formal, theoretical, linguist

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09501v1) | [下载PDF](https://arxiv.org/pdf/2604.09501v1.pdf)

---

## [8. BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation](https://arxiv.org/abs/2604.09497v1)

**作者**：Hippolyte Gisserot-Boukhlef, Nicolas Boizard, Emmanuel Malherbe 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Accurate evaluation is central to the large language model (LLM) ecosystem, guiding model selection and downstream adoption across diverse use cases. In practice, however, evaluating generative outputs typically relies on rigid lexical methods to extract and assess answers, which can conflate a model's true problem-solving ability with its compliance with predefined formatting guidelines. While recent LLM-as-a-Judge approaches mitigate this issue by assessing semantic correctness rather than strict structural conformity, they also introduce substantial computational overhead, making evaluation costly. In this work, we first systematically investigate the limitations of lexical evaluation through a large-scale empirical study spanning 36 models and 15 downstream tasks, demonstrating that such methods correlate poorly with human judgments. To address this limitation, we introduce BERT-as-a-Judge, an encoder-driven approach for assessing answer correctness in reference-based generative settings, robust to variations in output phrasing, and requiring only lightweight training on synthetically annotated question-candidate-reference triplets. We show that it consistently outperforms the lexical baseline while matching the performance of much larger LLM judges, providing a compelling tradeoff between the two and enabling reliable, scalable evaluation. Finally, through extensive experimentation, we provide detailed insights into BERT-as-a-Judge's performance to offer practical guidance for practitioners, and release all project artifacts to foster downstream adoption.

### 🤖 AI 总结

**一句话总结**：Accurate evaluation is central to the large language model (LLM) ecosystem, guiding model selection and downstream adoption across diverse use cases. In practice, however, evaluating generative output...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, BERT-as-a-Judge, Robust, Alternative, Lexical, Methods, Efficient, Reference-Based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09497v1) | [下载PDF](https://arxiv.org/pdf/2604.09497v1.pdf)

---

## [9. Agentic Jackal: Live Execution and Semantic Value Grounding for Text-to-JQL](https://arxiv.org/abs/2604.09470v1)

**作者**：Vishnu Murali, Anmol Gulati, Elias Lumer 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

Translating natural language into Jira Query Language (JQL) requires resolving ambiguous field references, instance-specific categorical values, and complex Boolean predicates. Single-pass LLMs cannot discover which categorical values (e.g., component names or fix versions) actually exist in a given Jira instance, nor can they verify generated queries against a live data source, limiting accuracy on paraphrased or ambiguous requests. No open, execution-based benchmark exists for mapping natural language to JQL. We introduce Jackal, the first large-scale, execution-based text-to-JQL benchmark comprising 100,000 validated NL-JQL pairs on a live Jira instance with over 200,000 issues. To establish baselines on Jackal, we propose Agentic Jackal, a tool-augmented agent that equips LLMs with live query execution via the Jira MCP server and JiraAnchor, a semantic retrieval tool that resolves natural-language mentions of categorical values through embedding-based similarity search. Among 9 frontier LLMs evaluated, single-pass models average only 43.4% execution accuracy on short natural-language queries, highlighting that text-to-JQL remains an open challenge. The agentic approach improves 7 of 9 models, with a 9.0% relative gain on the most linguistically challenging variant; in a controlled ablation isolating JiraAnchor, categorical-value accuracy rises from 48.7% to 71.7%, with component-field accuracy jumping from 16.9% to 66.2%. Our analysis identifies inherent semantic ambiguities, such as issue-type disambiguation and text-field selection, as the dominant failure modes rather than value-resolution errors, pointing to concrete directions for future work. We publicly release the benchmark, all agent transcripts, and evaluation code to support reproducibility.

### 🤖 AI 总结

**一句话总结**：Translating natural language into Jira Query Language (JQL) requires resolving ambiguous field references, instance-specific categorical values, and complex Boolean predicates. Single-pass LLMs cannot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, Jackal, Live, Execution, Semantic, Value, Grounding, Text-to-JQL

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09470v1) | [下载PDF](https://arxiv.org/pdf/2604.09470v1.pdf)

---

## [10. Across the Levels of Analysis: Explaining Predictive Processing in Humans Requires More Than Machine-Estimated Probabilities](https://arxiv.org/abs/2604.09466v1)

**作者**：Sathvik Nair, Colin Phillips  
**分类**：cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

Under the lens of Marr's levels of analysis, we critique and extend two claims about language models (LMs) and language processing: first, that predicting upcoming linguistic information based on context is central to language processing, and second, that many advances in psycholinguistics would be impossible without large language models (LLMs). We further outline future directions that combine the strengths of LLMs with psycholinguistic models.

### 🤖 AI 总结

**一句话总结**：Under the lens of Marr's levels of analysis, we critique and extend two claims about language models (LMs) and language processing: first, that predicting upcoming linguistic information based on cont...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Across, Levels, Analysis, Explaining, Predictive, Processing, Humans

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09466v1) | [下载PDF](https://arxiv.org/pdf/2604.09466v1.pdf)

---

## [11. Many-Tier Instruction Hierarchy in LLM Agents](https://arxiv.org/abs/2604.09443v1)

**作者**：Jingyu Zhang, Tianjian Li, William Jurayj 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Large language model agents receive instructions from many sources-system messages, user prompts, tool outputs, and more-each carrying different levels of trust and authority. When these instructions conflict, models must reliably follow the highest-privilege instruction to remain safe and effective. The dominant paradigm, instruction hierarchy (IH), assumes a fixed, small set of privilege levels (typically fewer than five) defined by rigid role labels (e.g., system > user). This is inadequate for real-world agentic settings, where conflicts can arise across far more sources and contexts. In this work, we propose Many-Tier Instruction Hierarchy (ManyIH), a paradigm for resolving instruction conflicts among instructions with arbitrarily many privilege levels. We introduce ManyIH-Bench, the first benchmark for ManyIH. ManyIH-Bench requires models to navigate up to 12 levels of conflicting instructions with varying privileges, comprising 853 agentic tasks (427 coding and 426 instruction-following). ManyIH-Bench composes constraints developed by LLMs and verified by humans to create realistic and difficult test cases spanning 46 real-world agents. Our experiments show that even the current frontier models perform poorly (~40% accuracy) when instruction conflict scales. This work underscores the urgent need for methods that explicitly target fine-grained, scalable instruction conflict resolution in agentic settings.

### 🤖 AI 总结

**一句话总结**：Large language model agents receive instructions from many sources-system messages, user prompts, tool outputs, and more-each carrying different levels of trust and authority. When these instructions ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Many-Tier, Instruction, Hierarchy, Large, language, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09443v1) | [下载PDF](https://arxiv.org/pdf/2604.09443v1.pdf)

---

## [12. Automated Instruction Revision (AIR): A Structured Comparison of Task Adaptation Strategies for LLM](https://arxiv.org/abs/2604.09418v1)

**作者**：Solomiia Bilyk, Volodymyr Getmanskyi, Taras Firman  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

This paper studies Automated Instruction Revision (AIR), a rule-induction-based method for adapting large language models (LLMs) to downstream tasks using limited task-specific examples. We position AIR within the broader landscape of adaptation strategies, including prompt optimization, retrieval-based methods, and fine-tuning. We then compare these approaches across a diverse benchmark suite designed to stress different task requirements, such as knowledge injection, structured extraction, label remapping, and logical reasoning. The paper argues that adaptation performance is strongly task-dependent: no single method dominates across all settings. Across five benchmarks, AIR was strongest or near-best on label-remapping classification, while KNN retrieval performed best on closed-book QA, and fine-tuning dominated structured extraction and event-order reasoning. AIR is most promising when task behavior can be captured by compact, interpretable instruction rules, while retrieval and fine-tuning remain stronger in tasks dominated by source-specific knowledge or dataset-specific annotation regularities.

### 🤖 AI 总结

**一句话总结**：This paper studies Automated Instruction Revision (AIR), a rule-induction-based method for adapting large language models (LLMs) to downstream tasks using limited task-specific examples. We position A...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：自动化指令修订 AIR, 指令规则归纳, LLM 任务适配, 少样本迁移, 提示优化, KNN 检索增强, 模型微调, 标签重映射分类, 结构化信息抽取, 闭卷问答, 事件顺序推理, 适配策略对比评测

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09418v1) | [下载PDF](https://arxiv.org/pdf/2604.09418v1.pdf)

---

## cs.CV

## [13. EgoTL: Egocentric Think-Aloud Chains for Long-Horizon Tasks](https://arxiv.org/abs/2604.09535v1)

**作者**：Lulin Liu, Dayou Li, Yiqing Liang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Large foundation models have made significant advances in embodied intelligence, enabling synthesis and reasoning over egocentric input for household tasks. However, VLM-based auto-labeling is often noisy because the primary data sources lack accurate human action labels, chain-of-thought (CoT), and spatial annotations; these errors are amplified during long-horizon spatial instruction following. These issues stem from insufficient coverage of minute-long, daily household planning tasks and from inaccurate spatial grounding. As a result, VLM reasoning chains and world-model synthesis can hallucinate objects, skip steps, or fail to respect real-world physical attributes. To address these gaps, we introduce EgoTL. EgoTL builds a think-aloud capture pipeline for egocentric data. It uses a say-before-act protocol to record step-by-step goals and spoken reasoning with word-level timestamps, then calibrates physical properties with metric-scale spatial estimators, a memory-bank walkthrough for scene context, and clip-level tags for navigation instructions and detailed manipulation actions. With EgoTL, we are able to benchmark VLMs and World Models on six task dimensions from three layers and long-horizon generation over minute-long sequences across over 100 daily household tasks. We find that foundation models still fall short as egocentric assistants or open-world simulators. Finally, we finetune foundation models with human CoT aligned with metric labels on the training split of EgoTL, which improves long-horizon planning and reasoning, step-wise reasoning, instruction following, and spatial grounding.

### 🤖 AI 总结

**一句话总结**：Large foundation models have made significant advances in embodied intelligence, enabling synthesis and reasoning over egocentric input for household tasks. However, VLM-based auto-labeling is often n...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EgoTL, Egocentric, Think-Aloud, Chains, Long-Horizon, Tasks, Large, foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09535v1) | [下载PDF](https://arxiv.org/pdf/2604.09535v1.pdf)

---

## [14. VisionFoundry: Teaching VLMs Visual Perception with Synthetic Images](https://arxiv.org/abs/2604.09531v1)

**作者**：Guanyu Zhou, Yida Yin, Wenhao Chai 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.CL  
**发布时间**：2026-04-10

### 📄 论文摘要

Vision-language models (VLMs) still struggle with visual perception tasks such as spatial understanding and viewpoint recognition. One plausible contributing factor is that natural image datasets provide limited supervision for low-level visual skills. This motivates a practical question: can targeted synthetic supervision, generated from only a task keyword such as Depth Order, address these weaknesses? To investigate this question, we introduce VisionFoundry, a task-aware synthetic data generation pipeline that takes only the task name as input and uses large language models (LLMs) to generate questions, answers, and text-to-image (T2I) prompts, then synthesizes images with T2I models and verifies consistency with a proprietary VLM, requiring no reference images or human annotation. Using VisionFoundry, we construct VisionFoundry-10K, a synthetic visual question answering (VQA) dataset containing 10k image-question-answer triples spanning 10 tasks. Models trained on VisionFoundry-10K achieve substantial improvements on visual perception benchmarks: +7% on MMVP and +10% on CV-Bench-3D, while preserving broader capabilities and showing favorable scaling behavior as data size increases. Our results suggest that limited task-targeted supervision is an important contributor to this bottleneck and that synthetic supervision is a promising path toward more systematic training for VLMs.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) still struggle with visual perception tasks such as spatial understanding and viewpoint recognition. One plausible contributing factor is that natural image datasets prov...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VisionFoundry, Teaching, VLMs, Visual, Perception, Synthetic, Images, Vision-language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09531v1) | [下载PDF](https://arxiv.org/pdf/2604.09531v1.pdf)

---

## [15. Envisioning the Future, One Step at a Time](https://arxiv.org/abs/2604.09527v1)

**作者**：Stefan Andreas Baumann, Jannik Wiese, Tommaso Martorella 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Accurately anticipating how complex, diverse scenes will evolve requires models that represent uncertainty, simulate along extended interaction chains, and efficiently explore many plausible futures. Yet most existing approaches rely on dense video or latent-space prediction, expending substantial capacity on dense appearance rather than on the underlying sparse trajectories of points in the scene. This makes large-scale exploration of future hypotheses costly and limits performance when long-horizon, multi-modal motion is essential. We address this by formulating the prediction of open-set future scene dynamics as step-wise inference over sparse point trajectories. Our autoregressive diffusion model advances these trajectories through short, locally predictable transitions, explicitly modeling the growth of uncertainty over time. This dynamics-centric representation enables fast rollout of thousands of diverse futures from a single image, optionally guided by initial constraints on motion, while maintaining physical plausibility and long-range coherence. We further introduce OWM, a benchmark for open-set motion prediction based on diverse in-the-wild videos, to evaluate accuracy and variability of predicted trajectory distributions under real-world uncertainty. Our method matches or surpasses dense simulators in predictive accuracy while achieving orders-of-magnitude higher sampling speed, making open-set future prediction both scalable and practical. Project page: http://compvis.github.io/myriad.

### 🤖 AI 总结

**一句话总结**：Accurately anticipating how complex, diverse scenes will evolve requires models that represent uncertainty, simulate along extended interaction chains, and efficiently explore many plausible futures. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Envisioning, Future, One, Step, Time, Accurately, anticipating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09527v1) | [下载PDF](https://arxiv.org/pdf/2604.09527v1.pdf)

---

## [16. RIRF: Reasoning Image Restoration Framework](https://arxiv.org/abs/2604.09511v1)

**作者**：Wending Yan, Rongkai Zhang, Kaihua Tang 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Universal image restoration (UIR) aims to recover clean images from diverse and unknown degradations using a unified model. Existing UIR methods primarily focus on pixel reconstruction and often lack explicit diagnostic reasoning over degradation composition, severity, and scene semantics prior to restoration. We propose Reason and Restore (R\&R), a novel framework that integrates structured Chain-of-Thought (CoT) reasoning into the image restoration pipeline. R\&R introduces an explicit reasoner, implemented by fine-tuning Qwen3-VL, to diagnose degradation types, quantify degradation severity, infer key degradation-related factors, and describe relevant scene and object semantics. The resulting structured reasoning provides interpretable and fine-grained diagnostic priors for the restorer. To further improve restoration quality, the quantified degradation severity produced by the reasoner is leveraged as reinforcement learning (RL) signals to guide and strengthen the restorer. Unlike existing multimodal LLM-based agentic systems that decouple reasoning from low-level vision tasks, R\&R tightly couples semantic diagnostic reasoning with pixel-level restoration in a unified framework. Extensive experiments across diverse UIR benchmarks demonstrate that R\&R achieves state-of-the-art performance while offering unique interpretability into the restoration process.

### 🤖 AI 总结

**一句话总结**：Universal image restoration (UIR) aims to recover clean images from diverse and unknown degradations using a unified model. Existing UIR methods primarily focus on pixel reconstruction and often lack ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RIRF, Reasoning, Image, Restoration, Framework, Universal, UIR, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09511v1) | [下载PDF](https://arxiv.org/pdf/2604.09511v1.pdf)

---

## [17. Incremental Semantics-Aided Meshing from LiDAR-Inertial Odometry and RGB Direct Label Transfer](https://arxiv.org/abs/2604.09478v1)

**作者**：Muhammad Affan, Ville Lehtola, George Vosselman  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-04-10

### 📄 论文摘要

Geometric high-fidelity mesh reconstruction from LiDAR-inertial scans remains challenging in large, complex indoor environments -- such as cultural buildings -- where point cloud sparsity, geometric drift, and fixed fusion parameters produce holes, over-smoothing, and spurious surfaces at structural boundaries. We propose a modular, incremental RGB+LiDAR pipeline that generates incremental semantics-aided high-quality meshes from indoor scans through scan frame-based direct label transfer. A vision foundation model labels each incoming RGB frame; labels are incrementally projected and fused onto a LiDAR-inertial odometry map; and an incremental semantics-aware Truncated Signed Distance Function (TSDF) fusion step produces the final mesh via marching cubes. This frame-level fusion strategy preserves the geometric fidelity of LiDAR while leveraging rich visual semantics to resolve geometric ambiguities at reconstruction boundaries caused by LiDAR point-cloud sparsity and geometric drift. We demonstrate that semantic guidance improves geometric reconstruction quality; quantitative evaluation is therefore performed using geometric metrics on the Oxford Spires dataset, while results from the NTU VIRAL dataset are analyzed qualitatively. The proposed method outperforms state-of-the-art geometric baselines ImMesh and Voxblox, demonstrating the benefit of semantics-aided fusion for geometric mesh quality. The resulting semantically labelled meshes are of value when reconstructing Universal Scene Description (USD) assets, offering a path from indoor LiDAR scanning to XR and digital modeling.

### 🤖 AI 总结

**一句话总结**：Geometric high-fidelity mesh reconstruction from LiDAR-inertial scans remains challenging in large, complex indoor environments -- such as cultural buildings -- where point cloud sparsity, geometric d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Incremental, Semantics-Aided, Meshing, LiDAR-Inertial, Odometry, RGB, Direct, Label

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09478v1) | [下载PDF](https://arxiv.org/pdf/2604.09478v1.pdf)

---

## [18. Realizing Immersive Volumetric Video: A Multimodal Framework for 6-DoF VR Engagement](https://arxiv.org/abs/2604.09473v1)

**作者**：Zhengxian Yang, Shengqi Wang, Shi Pan 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Fully immersive experiences that tightly integrate 6-DoF visual and auditory interaction are essential for virtual and augmented reality. While such experiences can be achieved through computer-generated content, constructing them directly from real-world captured videos remains largely unexplored. We introduce Immersive Volumetric Videos, a new volumetric media format designed to provide large 6-DoF interaction spaces, audiovisual feedback, and high-resolution, high-frame-rate dynamic content. To support IVV construction, we present ImViD, a multi-view, multi-modal dataset built upon a space-oriented capture philosophy. Our custom capture rig enables synchronized multi-view video-audio acquisition during motion, facilitating efficient capture of complex indoor and outdoor scenes with rich foreground--background interactions and challenging dynamics. The dataset provides 5K-resolution videos at 60 FPS with durations of 1-5 minutes, offering richer spatial, temporal, and multimodal coverage than existing benchmarks. Leveraging this dataset, we develop a dynamic light field reconstruction framework built upon a Gaussian-based spatio-temporal representation, incorporating flow-guided sparse initialization, joint camera temporal calibration, and multi-term spatio-temporal supervision for robust and accurate modeling of complex motion. We further propose, to our knowledge, the first method for sound field reconstruction from such multi-view audiovisual data. Together, these components form a unified pipeline for immersive volumetric video production. Extensive benchmarks and immersive VR experiments demonstrate that our pipeline generates high-quality, temporally stable audiovisual volumetric content with large 6-DoF interaction spaces. This work provides both a foundational definition and a practical construction methodology for immersive volumetric videos.

### 🤖 AI 总结

**一句话总结**：Fully immersive experiences that tightly integrate 6-DoF visual and auditory interaction are essential for virtual and augmented reality. While such experiences can be achieved through computer-genera...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VR, Realizing, Immersive, Volumetric, Video, Multimodal, Framework, 6-DoF

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09473v1) | [下载PDF](https://arxiv.org/pdf/2604.09473v1.pdf)

---

## [19. AsymLoc: Towards Asymmetric Feature Matching for Efficient Visual Localization](https://arxiv.org/abs/2604.09445v1)

**作者**：Mohammad Omama, Gabriele Berton, Eric Foxlin 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Precise and real-time visual localization is critical for applications like AR/VR and robotics, especially on resource-constrained edge devices such as smart glasses, where battery life and heat dissipation can be a primary concerns. While many efficient models exist, further reducing compute without sacrificing accuracy is essential for practical deployment. To address this, we propose asymmetric visual localization: a large Teacher model processes pre-mapped database images offline, while a lightweight Student model processes the query image online. This creates a challenge in matching features from two different models without resorting to heavy, learned matchers.   We introduce AsymLoc, a novel distillation framework that aligns a Student to its Teacher through a combination of a geometry-driven matching objective and a joint detector-descriptor distillation objective, enabling fast, parameter-less nearest-neighbor matching. Extensive experiments on HPatches, ScanNet, IMC2022, and Aachen show that AsymLoc achieves up to 95% of the teacher's localization accuracy using an order of magnitude smaller models, significantly outperforming existing baselines and establishing a new state-of-the-art efficiency-accuracy trade-off.

### 🤖 AI 总结

**一句话总结**：Precise and real-time visual localization is critical for applications like AR/VR and robotics, especially on resource-constrained edge devices such as smart glasses, where battery life and heat dissi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AsymLoc, Towards, Asymmetric, Feature, Matching, Efficient, Visual, Localization

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09445v1) | [下载PDF](https://arxiv.org/pdf/2604.09445v1.pdf)

---

## [20. SCoRe: Clean Image Generation from Diffusion Models Trained on Noisy Images](https://arxiv.org/abs/2604.09436v1)

**作者**：Yuta Matsuzaki, Seiichi Uchida, Shumpei Takezaki  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Diffusion models trained on noisy datasets often reproduce high-frequency training artifacts, significantly degrading generation quality. To address this, we propose SCoRe (Spectral Cutoff Regeneration), a training-free, generation-time spectral regeneration method for clean image generation from diffusion models trained on noisy images. Leveraging the spectral bias of diffusion models, which infer high-frequency details from low-frequency cues, SCoRe suppresses corrupted high-frequency components of a generated image via a frequency cutoff and regenerates them via SDEdit. Crucially, we derive a theoretical mapping between the cutoff frequency and the SDEdit initialization timestep based on Radially Averaged Power Spectral Density (RAPSD), which prevents excessive noise injection during regeneration. Experiments on synthetic (CIFAR-10) and real-world (SIDD) noisy datasets demonstrate that SCoRe substantially outperforms post-processing and noise-robust baselines, restoring samples closer to clean image distributions without any retraining or fine-tuning.

### 🤖 AI 总结

**一句话总结**：Diffusion models trained on noisy datasets often reproduce high-frequency training artifacts, significantly degrading generation quality. To address this, we propose SCoRe (Spectral Cutoff Regeneratio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SCoRe, Clean, Image, Generation, Models, Trained, Noisy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09436v1) | [下载PDF](https://arxiv.org/pdf/2604.09436v1.pdf)

---

## [21. Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v1)

**作者**：Wonbong Jang, Shikun Liu, Soubhik Sanyal 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Recovering camera parameters from images and rendering scenes from novel viewpoints have long been treated as separate tasks in computer vision and graphics. This separation breaks down when image coverage is sparse or poses are ambiguous, since each task needs what the other produces. We propose Rays as Pixels, a Video Diffusion Model (VDM) that learns a joint distribution over videos and camera trajectories. We represent each camera as dense ray pixels (raxels) and denoise them jointly with video frames through Decoupled Self-Cross Attention mechanism. A single trained model handles three tasks: predicting camera trajectories from video, jointly generating video and camera trajectory from input images, and generating video from input images along a target camera trajectory. Because the model can both predict trajectories from a video and generate views conditioned on its own predictions, we evaluate it through a closed-loop self-consistency test, demonstrating that its forward and inverse predictions agree. Notably, trajectory prediction requires far fewer denoising steps than video generation, even a few denoising steps suffice for self-consistency. We report results on pose estimation and camera-controlled video generation.

### 🤖 AI 总结

**一句话总结**：Recovering camera parameters from images and rendering scenes from novel viewpoints have long been treated as separate tasks in computer vision and graphics. This separation breaks down when image cov...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, of, Rays, Pixels, Learning, Joint, Distribution, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09429v1) | [下载PDF](https://arxiv.org/pdf/2604.09429v1.pdf)

---

## [22. PhysInOne: Visual Physics Learning and Reasoning in One Suite](https://arxiv.org/abs/2604.09415v1)

**作者**：Siyuan Zhou, Hejun Wang, Hu Cheng 等 39 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.RO  
**发布时间**：2026-04-10

### 📄 论文摘要

We present PhysInOne, a large-scale synthetic dataset addressing the critical scarcity of physically-grounded training data for AI systems. Unlike existing datasets limited to merely hundreds or thousands of examples, PhysInOne provides 2 million videos across 153,810 dynamic 3D scenes, covering 71 basic physical phenomena in mechanics, optics, fluid dynamics, and magnetism. Distinct from previous works, our scenes feature multiobject interactions against complex backgrounds, with comprehensive ground-truth annotations including 3D geometry, semantics, dynamic motion, physical properties, and text descriptions. We demonstrate PhysInOne's efficacy across four emerging applications: physics-aware video generation, long-/short-term future frame prediction, physical property estimation, and motion transfer. Experiments show that fine-tuning foundation models on PhysInOne significantly enhances physical plausibility, while also exposing critical gaps in modeling complex physical dynamics and estimating intrinsic properties. As the largest dataset of its kind, orders of magnitude beyond prior works, PhysInOne establishes a new benchmark for advancing physics-grounded world models in generation, simulation, and embodied AI.

### 🤖 AI 总结

**一句话总结**：We present PhysInOne, a large-scale synthetic dataset addressing the critical scarcity of physically-grounded training data for AI systems. Unlike existing datasets limited to merely hundreds or thous...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PhysInOne, Visual, Physics, Learning, Reasoning, One, Suite

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09415v1) | [下载PDF](https://arxiv.org/pdf/2604.09415v1.pdf)

---

## [23. SynFlow: Scaling Up LiDAR Scene Flow Estimation with Synthetic Data](https://arxiv.org/abs/2604.09411v1)

**作者**：Qingwen Zhang, Xiaomeng Zhu, Chenhan Jiang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-04-10

### 📄 论文摘要

Reliable 3D dynamic perception requires models that can anticipate motion beyond predefined categories, yet progress is hindered by the scarcity of dense, high-quality motion annotations. While self-supervision on unlabeled real data offers a path forward, empirical evidence suggests that scaling unlabeled data fails to close the performance gap due to noisy proxy signals. In this paper, we propose a shift in paradigm: learning robust real-world motion priors entirely from scalable simulation. We introduce SynFlow, a data generation pipeline that generates large-scale synthetic dataset specifically designed for LiDAR scene flow. Unlike prior works that prioritize sensor-specific realism, SynFlow employs a motion-oriented strategy to synthesize diverse kinematic patterns across 4,000 sequences ($\sim$940k frames), termed SynFlow-4k. This represents a 34x scale-up in annotated volume over existing real-world benchmarks. Our experiments demonstrate that SynFlow-4k provides a highly domain-invariant motion prior. In a zero-shot regime, models trained exclusively on our synthetic data generalize across multiple real-world benchmarks, rivaling in-domain supervised baselines on nuScenes and outperforming state-of-the-art methods on TruckScenes by 31.8%. Furthermore, SynFlow-4k serves as a label-efficient foundation: fine-tuning with only 5% of real-world labels surpasses models trained from scratch on the full available budget. We open-source the pipeline and dataset to facilitate research in generalizable 3D motion estimation. More detail can be found at https://kin-zhang.github.io/SynFlow.

### 🤖 AI 总结

**一句话总结**：Reliable 3D dynamic perception requires models that can anticipate motion beyond predefined categories, yet progress is hindered by the scarcity of dense, high-quality motion annotations. While self-s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Up, SynFlow, Scaling, LiDAR, Scene, Flow, Estimation, Synthetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09411v1) | [下载PDF](https://arxiv.org/pdf/2604.09411v1.pdf)

---

## cs.LG

## [24. ANTIC: Adaptive Neural Temporal In-situ Compressor](https://arxiv.org/abs/2604.09543v1)

**作者**：Sandeep S. Cranganore, Andrei Bodnar, Gianluca Galleti 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

The persistent storage requirements for high-resolution, spatiotemporally evolving fields governed by large-scale and high-dimensional partial differential equations (PDEs) have reached the petabyte-to-exabyte scale. Transient simulations modeling Navier-Stokes equations, magnetohydrodynamics, plasma physics, or binary black hole mergers generate data volumes that are prohibitive for modern high-performance computing (HPC) infrastructures. To address this bottleneck, we introduce ANTIC (Adaptive Neural Temporal in situ Compressor), an end-to-end in situ compression pipeline. ANTIC consists of an adaptive temporal selector tailored to high-dimensional physics that identifies and filters informative snapshots at simulation time, combined with a spatial neural compression module based on continual fine-tuning that learns residual updates between adjacent snapshots using neural fields. By operating in a single streaming pass, ANTIC enables a combined compression of temporal and spatial components and effectively alleviates the need for explicit on-disk storage of entire time-evolved trajectories. Experimental results demonstrate how storage reductions of several orders of magnitude relate to physics accuracy.

### 🤖 AI 总结

**一句话总结**：The persistent storage requirements for high-resolution, spatiotemporally evolving fields governed by large-scale and high-dimensional partial differential equations (PDEs) have reached the petabyte-t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ANTIC, Adaptive, Neural, Temporal, In-situ, Compressor, persistent, storage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09543v1) | [下载PDF](https://arxiv.org/pdf/2604.09543v1.pdf)

---

## [25. Toward World Models for Epidemiology](https://arxiv.org/abs/2604.09519v1)

**作者**：Zeeshan Memon, Yiqi Su, Christo Kurisummoottil Thomas 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

World models have emerged as a unifying paradigm for learning latent dynamics, simulating counterfactual futures, and supporting planning under uncertainty. In this paper, we argue that computational epidemiology is a natural and underdeveloped setting for world models. This is because epidemic decision-making requires reasoning about latent disease burden, imperfect and policy-dependent surveillance signals, and intervention effects are mediated by adaptive human behavior. We introduce a conceptual framework for epidemiological world models, formulating epidemics as controlled, partially observed dynamical systems in which (i) the true epidemic state is latent, (ii) observations are noisy and endogenous to policy, and (iii) interventions act as sequential actions whose effects propagate through behavioral and social feedback. We present three case studies that illustrate why explicit world modeling is necessary for policy-relevant reasoning: strategic misreporting in behavioral surveillance, systematic delays in time-lagged signals such as hospitalizations and deaths, and counterfactual intervention analysis where identical histories diverge under alternative action sequences.

### 🤖 AI 总结

**一句话总结**：World models have emerged as a unifying paradigm for learning latent dynamics, simulating counterfactual futures, and supporting planning under uncertainty. In this paper, we argue that computational ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Toward, World, Models, Epidemiology, have, emerged, unifying

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09519v1) | [下载PDF](https://arxiv.org/pdf/2604.09519v1.pdf)

---

## [26. Integrated electro-optic attention nonlinearities for transformers](https://arxiv.org/abs/2604.09512v1)

**作者**：Luis Mickeler, Kai Lion, Alfonso Nardi 等 8 位作者  
**分类**：cs.LG, physics.optics  
**发布时间**：2026-04-10

### 📄 论文摘要

Transformers have emerged as the dominant neural-network architecture, achieving state-of-the-art performance in language processing and computer vision. At the core of these models lies the attention mechanism, which requires a nonlinear, non-negative mapping using the Softmax function. However, although Softmax operations account for less than 1% of the total operation count, they can disproportionately bottleneck overall inference latency. Here, we use thin-film lithium niobate (TFLN) Mach-Zehnder modulators (MZMs) as analog nonlinear computational elements to drastically reduce the latency of nonlinear computations. We implement electro-optic alternatives to digital Softmax and Sigmoid, and evaluate their performance in Vision Transformers and Large Language Models. Our system maintains highly competitive accuracy, even under aggressive 4-bit input-output quantization of the analog units. We further characterize system noise at encoding speeds up to 10 GBaud and assess model robustness under various noise conditions. Our findings suggest that TFLN modulators can serve as nonlinear function units within hybrid co-packaged hardware, enabling high-speed and energy-efficient nonlinear computation.

### 🤖 AI 总结

**一句话总结**：Transformers have emerged as the dominant neural-network architecture, achieving state-of-the-art performance in language processing and computer vision. At the core of these models lies the attention...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Integrated, electro-optic, attention, nonlinearities, transformers, have, emerged

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09512v1) | [下载PDF](https://arxiv.org/pdf/2604.09512v1.pdf)

---

## [27. SafeAdapt: Provably Safe Policy Updates in Deep Reinforcement Learning](https://arxiv.org/abs/2604.09452v1)

**作者**：Maksim Anisimov, Francesco Belardinelli, Matthew Wicker  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-04-10

### 📄 论文摘要

Safety guarantees are a prerequisite to the deployment of reinforcement learning (RL) agents in safety-critical tasks. Often, deployment environments exhibit non-stationary dynamics or are subject to changing performance goals, requiring updates to the learned policy. This leads to a fundamental challenge: how to update an RL policy while preserving its safety properties on previously encountered tasks? The majority of current approaches either do not provide formal guarantees or verify policy safety only a posteriori. We propose a novel a priori approach to safe policy updates in continual RL by introducing the Rashomon set: a region in policy parameter space certified to meet safety constraints within the demonstration data distribution. We then show that one can provide formal, provable guarantees for arbitrary RL algorithms used to update a policy by projecting their updates onto the Rashomon set. Empirically, we validate this approach across grid-world navigation environments (Frozen Lake and Poisoned Apple) where we guarantee an a priori provably deterministic safety on the source task during downstream adaptation. In contrast, we observe that regularisation-based baselines experience catastrophic forgetting of safety constraints while our approach enables strong adaptation with provable guarantees that safety is preserved.

### 🤖 AI 总结

**一句话总结**：Safety guarantees are a prerequisite to the deployment of reinforcement learning (RL) agents in safety-critical tasks. Often, deployment environments exhibit non-stationary dynamics or are subject to ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SafeAdapt, Provably, Safe, Policy, Updates, Deep, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09452v1) | [下载PDF](https://arxiv.org/pdf/2604.09452v1.pdf)

---

## [28. AdaCubic: An Adaptive Cubic Regularization Optimizer for Deep Learning](https://arxiv.org/abs/2604.09437v1)

**作者**：Ioannis Tsingalis, Constantine Kotropoulos, Corentin Briat  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

A novel regularization technique, AdaCubic, is proposed that adapts the weight of the cubic term. The heart of AdaCubic is an auxiliary optimization problem with cubic constraints that dynamically adjusts the weight of the cubic term in Newton's cubic regularized method. We use Hutchinson's method to approximate the Hessian matrix, thereby reducing computational cost. We demonstrate that AdaCubic inherits the cubically regularized Newton method's local convergence guarantees. Our experiments in Computer Vision, Natural Language Processing, and Signal Processing tasks demonstrate that AdaCubic outperforms or competes with several widely used optimizers. Unlike other adaptive algorithms that require hyperparameter fine-tuning, AdaCubic is evaluated with a fixed set of hyperparameters, rendering it a highly attractive optimizer in settings where fine-tuning is infeasible. This makes AdaCubic an attractive option for researchers and practitioners alike. To our knowledge, AdaCubic is the first optimizer to leverage cubic regularization in scalable deep learning applications.

### 🤖 AI 总结

**一句话总结**：A novel regularization technique, AdaCubic, is proposed that adapts the weight of the cubic term. The heart of AdaCubic is an auxiliary optimization problem with cubic constraints that dynamically adj...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, AdaCubic, Adaptive, Cubic, Regularization, Optimizer, Deep, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09437v1) | [下载PDF](https://arxiv.org/pdf/2604.09437v1.pdf)

---

## [29. Offline Local Search for Online Stochastic Bandits](https://arxiv.org/abs/2604.09423v1)

**作者**：Gerdus Benadè, Rathish Das, Thomas Lavastida  
**分类**：cs.LG  
**发布时间**：2026-04-10

### 📄 论文摘要

Combinatorial multi-armed bandits provide a fundamental online decision-making environment where a decision-maker interacts with an environment across $T$ time steps, each time selecting an action and learning the cost of that action. The goal is to minimize regret, defined as the loss compared to the optimal fixed action in hindsight under full-information. There has been substantial interest in leveraging what is known about offline algorithm design in this online setting. Offline greedy and linear optimization algorithms (both exact and approximate) have been shown to provide useful guarantees when deployed online. We investigate local search methods, a broad class of algorithms used widely in both theory and practice, which have thus far been under-explored in this context. We focus on problems where offline local search terminates in an approximately optimal solution and give a generic method for converting such an offline algorithm into an online stochastic combinatorial bandit algorithm with $O(\log^3 T)$ (approximate) regret. In contrast, existing offline-to-online frameworks yield regret (and approximate regret) which depend sub-linearly, but polynomially on $T$. We demonstrate the flexibility of our framework by applying it to three online stochastic combinatorial optimization problems: scheduling to minimize total completion time, finding a minimum cost base of a matroid and uncertain clustering.

### 🤖 AI 总结

**一句话总结**：Combinatorial multi-armed bandits provide a fundamental online decision-making environment where a decision-maker interacts with an environment across $T$ time steps, each time selecting an action and...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Offline, Local, Search, Online, Stochastic, Bandits, Combinatorial, multi-armed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09423v1) | [下载PDF](https://arxiv.org/pdf/2604.09423v1.pdf)

---

## [30. NOMAD: Generating Embeddings for Massive Distributed Graphs](https://arxiv.org/abs/2604.09419v1)

**作者**：Aishwarya Sarkar, Sayan Ghosh, Nathan R. Tallent 等 4 位作者  
**分类**：cs.LG, cs.DC  
**发布时间**：2026-04-10

### 📄 论文摘要

Successful machine learning on graphs or networks requires embeddings that not only represent nodes and edges as low-dimensional vectors but also preserve the graph structure. Established methods for generating embeddings require flexible exploration of the entire graph through repeated use of random walks that capture graph structure with samples of nodes and edges. These methods create scalability challenges for massive graphs with millions-to-billions of edges because single-node solutions have inadequate memory and processing capabilities.   We present NOMAD, a distributed-memory graph embedding framework using the Message Passing Interface (MPI) for distributed graphs. NOMAD implements proximity-based models proposed in the widely popular LINE (Large-scale Information Network Embedding) algorithm. We propose several practical trade-offs to improve the scalability and communication overheads confronted by irregular and distributed graph embedding methods, catering to massive-scale graphs arising in web and science domains. NOMAD demonstrates median speedups of 10/100x on CPU-based NERSC Perlmutter cluster relative to the popular reference implementations of multi-threaded LINE and node2vec, 35-76x over distributed PBG, and competitive embedding quality relative to LINE, node2vec, and GraphVite, while yielding 12-370x end-to-end speedups on real-world graphs.

### 🤖 AI 总结

**一句话总结**：Successful machine learning on graphs or networks requires embeddings that not only represent nodes and edges as low-dimensional vectors but also preserve the graph structure. Established methods for ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：NOMAD, Generating, Embeddings, Massive, Distributed, Graphs, Successful, machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2604.09419v1) | [下载PDF](https://arxiv.org/pdf/2604.09419v1.pdf)

---

