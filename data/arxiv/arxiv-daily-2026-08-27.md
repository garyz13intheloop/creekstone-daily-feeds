# arXiv AI 论文日报 | 2026-08-27

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings](https://arxiv.org/abs/2608.26088v1)

**作者**：Evelyn Ma, Rama Kumar Pasumarthi, Kishwar Shafin 等 28 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predictive planetary models remains bottlenecked by a fragmented data ecosystem, requiring manual data retrieval, multimodal data curation and fusion along with iterative model selection. We present the Planetary Prediction Engine (PPE), an autonomous AI system that executes this end-to-end workflow directly from natural-language queries. PPE synthesizes multimodal datasets on the fly, retrieving spatiotemporally relevant covariates across open-web and Earth observation platforms (Data Commons, Google Earth Engine) and fusing them with geospatial foundation model embeddings (PDFM, AlphaEarth). Simultaneously, it searches over task-tailored model architecture families with automated overfitting guards. Across diverse tasks, geographies, and scientific domains, PPE consistently outperforms state-of-the-art or manually tuned expert baselines. For US spatial regression, PPE improves mean $R^2$ across 21 CDC health indicators (76.8% vs. 60.0%), FEMA national risk indices (64.9% vs. 60.0%), and the Social Vulnerability Index (66.2% vs. 58.6%). For spatial downscaling in data-scarce settings, PPE integrates localized proxies to double baseline accuracy in Nigerian food security indicators ($R^2$ of 66.1% vs. 31.5%). For epidemiological nowcasting of the 2026 DRC Bundibugyo Ebola outbreak, PPE achieves a Recall@10 of 83.3% (identifying 15 of 18 newly invaded health zones across five weekly forecasts), a +10.3 percentage-point improvement over the public state-of-the-art modeling (~73%). By combining autonomous multimodal planetary data discovery with targeted model optimization, PPE lowers the technical barrier to planetary-scale analytics, enabling rapid, customized, expert-level deployment.

### 🤖 AI 总结

**一句话总结**：Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predicti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Planetary, Prediction, Engine, Autonomous, Geospatial, via, Intelligent, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26088v1) | [下载PDF](https://arxiv.org/pdf/2608.26088v1.pdf)

---

## [2. SwarmWorld: Stigmergic technological evolution in societies of language-model agents](https://arxiv.org/abs/2608.26081v1)

**作者**：Subhadeep Pal, Fiona Y. Wang, Markus J. Buehler  
**分类**：cs.AI, cond-mat.mtrl-sci, cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new substrate for this process, yet most multi-agent systems rely on direct conversation, predefined roles, or centralized workflows. It remains unclear whether decentralized agents can build functional technologies and outperform independent search. Here, initially homogeneous LLM agents in SwarmWorld self-organize without assigned roles or recipes into evolving technological societies. Agents explore a spatial environment, process resources, test materials, construct persistent artifacts, and write executable controllers evaluated by a deterministic simulator under unseen disturbances after the agents are removed. SwarmWorld splits cognition from consequence: agents propose architectures and controllers within fixed action and material schemas, while the simulated world determines function. Shared societies develop broader, more resilient technological portfolios than a strong best-of-N isolated-search baseline, although isolated search remains competitive for the strongest artifact. Agents differentiate into exploration, construction, maintenance, and coordination behaviors, transitioning as the world matures. Technologies accumulate through collaborative construction, executable inheritance, and persistent agent-artifact networks, with most reuse beginning through physical observation rather than communication. Explicit cultural mechanisms amplify collaboration and organization, but functional benefits depend on outcome and timescale. Physical stigmergy alone supports capable societies, while interaction drives persistent technological ecologies rather than universally superior individual inventions.

### 🤖 AI 总结

**一句话总结**：Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new su...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, SwarmWorld, Stigmergic, technological, evolution, societies, language-model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26081v1) | [下载PDF](https://arxiv.org/pdf/2608.26081v1.pdf)

---

## [3. Trace Integrity for LLM Data Agents: A Vision for Auditable Structured Reasoning in Real-World Systems](https://arxiv.org/abs/2608.26036v1)

**作者**：Srimonti Dutta, Akshata Kishore Moharir  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Answer accuracy is an insufficient reliability signal for LLM data agents. In structured-data tasks, a benchmark-correct answer can be produced by an invalid trace. This paper introduces Trace Integrity, a deployment reliability criterion for evaluating whether the computation recorded behind an answer is explicit, executable, schema-valid, operator-faithful, replayable, answer-consistent, and auditable. We identify the Structure Gap as the deployment failure mode that makes Trace Integrity necessary: natural-language reasoning and free-form rationales do not reliably specify the operator-level programs required by real-world systems. We operationalize Trace Integrity with execution contracts, structured artifacts that bind user intent to schema elements, operator plans, assumptions, executable queries, verification status, and final-answer linkage. We also introduce CAIT (Correct Answer / Invalid Trace) Rate, which measures how often answer-only evaluation counts computationally unsupported outputs as successes. In an empirical demonstration on BIRD Mini-Dev, Direct SQL, Operation Summary + SQL, and Contract-First SQL achieve answer accuracies of 20%, 22%, and 24%, while their Trace Integrity Pass Rates are 39%, 43%, and 40% and their CAIT Rates remain high at 55%, 59.1%, and 45.8%, showing that answer accuracy, trace validity, and silent-failure risk are distinct evaluation signals. Real-world LLM data agents should, therefore, be evaluated not only by whether their outputs match a reference answer, but by whether those outputs are backed by auditable computation.

### 🤖 AI 总结

**一句话总结**：Answer accuracy is an insufficient reliability signal for LLM data agents. In structured-data tasks, a benchmark-correct answer can be produced by an invalid trace. This paper introduces Trace Integri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Trace, Integrity, Data, Vision, Auditable, Structured

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26036v1) | [下载PDF](https://arxiv.org/pdf/2608.26036v1.pdf)

---

## [4. Imitation Learning for Connection-Tableau Construction](https://arxiv.org/abs/2608.26009v1)

**作者**：Fredrik Rømming, Mantas Bakšys, Martin S. Fixman 等 4 位作者  
**分类**：cs.AI, cs.LG, cs.LO  
**发布时间**：2026-08-26

### 📄 论文摘要

An automated theorem prover builds a proof step by step, choosing at each point what to add and what to remove. We cast this construction as a policy acting in a transition system induced by a formal calculus, which fixes which steps are sound: for clausal connection tableaux, leanCoP-style search and plCoP/rlCoP-style planning then become stateful policies over one interface, and policy-learning methods apply directly. We equip such policies with a graph neural network that scores proof edits from structure that transfers across problems, train it by imitation learning from found proofs, and measure how performance holds as we remove search scaffolding, from full symbolic backtracking to a policy the network drives alone. Within a fixed step budget on M2k, MPTP2078-bushy, and TPTP v9.2.1, learned policies solve up to 46% more problems than leanCoP, and reach proofs in an order of magnitude fewer steps.

### 🤖 AI 总结

**一句话总结**：An automated theorem prover builds a proof step by step, choosing at each point what to add and what to remove. We cast this construction as a policy acting in a transition system induced by a formal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Imitation, Learning, Connection-Tableau, Construction, automated, theorem, prover

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26009v1) | [下载PDF](https://arxiv.org/pdf/2608.26009v1.pdf)

---

## [5. AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://arxiv.org/abs/2608.26004v1)

**作者**：Sheng Liang, Yongyue Zhang, Nathanael Brian 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but this degrades task accuracy. Speculative decoding (SD) accelerates generation losslessly, yet it assumes the drafter and verifier share an identical context, preventing SD from resolving the accuracy-overhead trade-off. We propose AsymSpec, an asymmetric speculative decoding framework that breaks this symmetry: a lightweight drafter reads the full input while the large verifier operates on the compressed view. The drafter steers the verifier via a contrastive $δ$-fusion of logits, modulated by a divergence-aware acceptance gate that preserves verification stability and high draft acceptance rates. Evaluated across four agentic capabilities and two end-to-end agent benchmarks, AsymSpec reaches $\approx 90\%$ of full-context accuracy on average, delivering $1.3$--$1.7\times$ throughput speedups at $0.2$--$0.3\times$ the compute cost on isolated text capabilities. These results show that asymmetric context access yields substantial gains precisely when compression discards critical reasoning signals.

### 🤖 AI 总结

**一句话总结**：Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, AsymSpec, Context-Asymmetric, Speculative, Decoding, Agentic, pipelines, face

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26004v1) | [下载PDF](https://arxiv.org/pdf/2608.26004v1.pdf)

---

## [6. ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs](https://arxiv.org/abs/2608.25992v1)

**作者**：Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang  
**分类**：cs.AI, cs.MA  
**发布时间**：2026-08-26

### 📄 论文摘要

Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operating costs due to repeated LLM invocations and long-horizon context accumulation. Existing cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows, in which the right LLM at each step depends on evolving task progress, remaining task difficulty, and cost-efficiency requirements. We present ProgRouter, an online progress-guided routing framework that adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets. ProgRouter introduces a multi-view task progress scorer that combines coarse workflow outcome regimes with fine-grained signals on subtask completion, progress trends, and workflow state quality. Then, a dual-path task progress predictor and an adaptive meta-gating mechanism estimate the progress gain for each candidate routed LLM. ProgRouter makes online step-wise routing decisions that balance progress gain, task time budgets, and long-term operating cost efficiency. Experiments on HumanEval Plus, MBPP, MATH-500, and ASQA, spanning agentic code generation, mathematical reasoning, and retrieval-augmented long-form question answering, demonstrate that ProgRouter reduces the operating cost relative to key baselines while maintaining strong task-solving performance.

### 🤖 AI 总结

**一句话总结**：Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, LLM, ProgRouter, Online, Progress-Guided, Orchestration, Workflows, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25992v1) | [下载PDF](https://arxiv.org/pdf/2608.25992v1.pdf)

---

## [7. Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs](https://arxiv.org/abs/2608.25986v1)

**作者**：Zongyu Wu, Yilong Wang, Xiaochen Wang 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-26

### 📄 论文摘要

Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages structured knowledge to provide (M)LLMs with high-quality external information. Building on these works, recent studies have explored multimodal knowledge graphs (MMKGs) as knowledge bases for GraphRAG. This enables Graph RAG to integrate knowledge across multiple modalities, thereby further enhancing its performance. However, existing MMKG-based RAG methods generally follow a common pipeline in which different modalities are largely processed independently before being fusion. As a result, textual context is only used to a limited extent during visual information extraction and subsequent multimodal knowledge fusion. This brings a semantic gap between images and text which limits the multimodal GraphRAG performance. To address this issue, we propose a novel framework for constructing a Context-Enhanced MMKG (CEMMKG) to better support multimodal GraphRAG. The proposed CEMMKG enriches each image with complementary textual context at both local and global scopes. Local context goes beyond the surrounding text by incorporating sentences that are semantically related to the image, while global context provides a summary of the entire passage. We further introduce a multi-granularity design for the local context, allowing it to capture semantically relevant information at different levels of detail. Extensive experiments on the selected vision-centric dataset validate that CEMMKG is effective in leveraging contextual information to improve MMKG-based RAG performance. Moreover, its effectiveness across different MMKG-based RAG methods demonstrates its broad applicability.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-b...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RAG, Multi-Granularity, Context-Enhanced, over, Multimodal, Knowledge, Graphs, Retrieval-augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25986v1) | [下载PDF](https://arxiv.org/pdf/2608.25986v1.pdf)

---

## [8. SciMIF: Understanding Multimodal Instruction Following in Scientific Domains](https://arxiv.org/abs/2608.25973v1)

**作者**：Ye Shen, Yuting Zheng, Dun Pei 等 7 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Understanding instruction-following capabilities in scientific domains is essential for effectively leveraging Multimodal Large Language Models (MLLMs) to advance the development of scientific fields. In this work, we introduce SciMIF, a novel benchmark designed to evaluate the capability of MLLMs in following complex scientific instructions. Specifically, based on an extensive analysis of 22 distinct tasks across 5 representative scientific disciplines, we propose a comprehensive taxonomy comprising 10 constraint groups that captures both general functional requirements and discipline-specific characteristics. Guided by this taxonomy, we develop a high-fidelity instruction injection pipeline to systematically augment existing scientific datasets. We conduct comprehensive experiments on multiple state-of-the-art closed-source and open-source MLLMs. Our findings reveal significant performance disparities across different scientific disciplines, with chemistry posing greater challenges for current MLLMs. Furthermore, we observe that increasing the model scale does not yield corresponding improvements in constraint adherence, and current models still struggle severely with fine-grained constraints and instructions requiring the deep application of disciplinary knowledge. SciMIF fills the current void in evaluating multimodal instruction adherence within scientific domains, laying a crucial foundation for future enhancements of MLLMs in rigorous scientific applications. Data and code will be released at https://github.com/shenye7436/SciMIF .

### 🤖 AI 总结

**一句话总结**：Understanding instruction-following capabilities in scientific domains is essential for effectively leveraging Multimodal Large Language Models (MLLMs) to advance the development of scientific fields....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SciMIF, Understanding, Multimodal, Instruction, Following, Scientific, Domains, instruction-following

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25973v1) | [下载PDF](https://arxiv.org/pdf/2608.25973v1.pdf)

---

## cs.CL

## [9. Fine-Tuning Whisper for Automatic Speech Recognition in Baniwa: A Preliminary Study](https://arxiv.org/abs/2608.26060v1)

**作者**：Leonardo Duart, Tiago Fonseca, Thiago Chacón  
**分类**：cs.CL, stat.ML  
**发布时间**：2026-08-26

### 📄 论文摘要

Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated on high-resource languages, while indigenous languages continue to suffer from a lack of speech resources and language technologies. This work presents a preliminary study on the adaptation of Whisper for Automatic Speech Recognition in Baniwa, an indigenous Arawakan language spoken in Brazil, Colombia, and Venezuela. The experiments were conducted using a corpus of 1,373 manually transcribed recordings obtained from a linguistic documentation project. The corpus contains approximately 0.54 hours of speech and consists primarily of isolated words and short elicited utterances. The Whisper Small model was fine-tuned using supervised learning and evaluated using Word Error Rate (WER) and Character Error Rate (CER). The best model achieved a WER of 37.5% and a CER of 7.45%, demonstrating that multilingual foundation models can be successfully adapted to extremely low-resource indigenous languages. The results establish an initial baseline for Baniwa Automatic Speech Recognition and provide a foundation for future research involving larger datasets, language-specific adaptation strategies, and post-processing techniques.

### 🤖 AI 总结

**一句话总结**：Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Fine-Tuning, Whisper, Automatic, Speech, Recognition, Baniwa, Preliminary, Study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26060v1) | [下载PDF](https://arxiv.org/pdf/2608.26060v1.pdf)

---

## [10. VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013v1)

**作者**：Min Zeng, Guanxin Tan, Libin Cen 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging. Existing synthesis pipelines typically follow a one-pass generate-and-filter paradigm, discarding feedback from failed samples, verifier outcomes, and target-model errors. We present VISA (Visual Instruction Synthesis Agent), an agentic framework that reformulates multimodal instruction synthesis as a self-evolving loop. At each round, VISA analyzes an image to filter incompatible constraints and discover new verifiable ones, samples diversity- and difficulty-aware constraint sets from persistent memory, generates candidate instructions, and verifies the resulting samples with executable tools and structured large language model judges. Failed samples trigger diagnostic-guided recovery, while accepted samples are probed against the target model to estimate difficulty. The resulting verifier signals and target-model failure profiles are written back to memory, allowing subsequent rounds to adaptively expand the constraint space, reduce template repetition, and focus on unresolved model weaknesses. The same verifier contracts further provide reward signals for reinforcement learning without a separately trained reward model. Experiments on MM-IFEval show that VISA consistently improves multimodal instruction following over strong baselines, while preserving general multimodal capability across seven public benchmarks.

### 🤖 AI 总结

**一句话总结**：Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging. Existing synthesis pipelines typically follow a one-pass generate-and-filter parad...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VISA, Agentic, Self-Evolving, Data, Synthesis, Multimodal, Instruction, Following

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26013v1) | [下载PDF](https://arxiv.org/pdf/2608.26013v1.pdf)

---

## [11. Distinct dynamics of conceptual and referential disruptions in human reading and large language model processing](https://arxiv.org/abs/2608.25999v1)

**作者**：Rui He, Nihal Altay, Wolfram Hinzen  
**分类**：cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Linguistic meaning is grounded in conceptual content, from which reference to particular entities emerges as words enter discourse. To examine the processing dynamics associated with these two dimensions of meaning, we selectively disrupted conceptual or referential information in short narratives and traced the resulting effects in human self-paced reading and in the predictive and representational processing of large language models. In human reading, conceptual disruptions produced a strong but localized processing cost, emerging immediately after the distorted word, reaching an early maximum, and then declining rapidly. Referential disruptions produced weaker effects, which decreased more gradually across subsequent words, and were more strongly modulated by sentence boundaries. In the language model, both disruptions emerged immediately at the manipulated word. Contextual model surprisal showed a pattern closely paralleling human reading: conceptual disruption produced a larger, more locally concentrated effect that decayed rapidly, whereas referential disruption produced a smaller and more gradual downstream effect. Output-layer representations showed a different pattern: referential disruption produced a larger initial displacement, while both distortions were subsequently characterized by power-law decay. Together, these results provide convergent evidence for distinguishable processing dynamics of two types of meaning: conceptual information imposes a more locally concentrated integration cost, whereas referential information engages a more distributed process of maintaining discourse-level identity.

### 🤖 AI 总结

**一句话总结**：Linguistic meaning is grounded in conceptual content, from which reference to particular entities emerges as words enter discourse. To examine the processing dynamics associated with these two dimensi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Distinct, dynamics, conceptual, referential, disruptions, human, reading

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25999v1) | [下载PDF](https://arxiv.org/pdf/2608.25999v1.pdf)

---

## [12. When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs](https://arxiv.org/abs/2608.25977v1)

**作者**：Yao Fu, Lijia Huang, Xiaomin Li 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-26

### 📄 论文摘要

Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a common framework for assessing LLMs' personality, existing studies focus primarily on full-precision models and evaluate only final outputs. They overlook the widespread deployment of quantized LLMs requiring low memory footprints, whose personality traits remain underexplored. In this work, we present a systematic MBTI analysis of open-source LLMs across multiple precisions, including mainstream 4-bit methods (GPTQ, AWQ) and extreme 2-bit settings (AQLM variants). Beyond output-level evaluation, we examine how personality emerges across layers through option-level entropy and confidence-gap dynamics, and introduce Uncertainty-Amplified Layer Decoding (UALD) to study decoding-induced personality drift at inference time. Our results reveal a key insight: LLMs' personality is not a static property, but an emergent, layer-dependent decision process sensitive to quantization, prompting, and decoding. Specifically, we find that (1) ENFJ remains dominant across model families and precisions; (2) 4-bit quantization largely preserves coarse personality structure, while 2-bit quantization disrupts fine-grained prompt consistency and cross-precision agreement; (3) personality decisions emerges in upper layers, following substantial ambiguity in early layers; and (4) inference decoding can shift personality, while personality-aligned conditioning improves robustness. These findings provide a new perspective on the behavioral reliability of quantized LLMs and highlight the importance of considering internal dynamics and inference strategies in personality-sensitive chatbot applications.

### 🤖 AI 总结

**一句话总结**：Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, When, Personality, Meets, Quantization, Layer-wise, MBTI, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25977v1) | [下载PDF](https://arxiv.org/pdf/2608.25977v1.pdf)

---

## [13. Lost but not erased: Finding traces of a forgotten language in neural speech models](https://arxiv.org/abs/2608.25976v1)

**作者**：Peter Plantinga, Charlotte Moore, Peter W. Donhauser 等 5 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

International adoptees retain phonological traces of a birth language they can no longer speak or comprehend, a persistence typically attributed to a biologically-timed critical period. We asked whether it could instead reflect the ordinary dynamics of learning, using automatic speech recognition models that simulate the international adoptee experience without maturational confounds. Models were trained on one language and then abruptly switched to a second. We found that traces of the first language persisted throughout second-language training, but mainly in the lowest, pre-phonemic layers. These traces were functional, as models with early exposure re-learned their lost first language 14% faster than naive models; this advantage held even against models adopted early from a related language and disappeared when the earliest layers were substituted from a non-adopted model. We argue that these critical-period effects reflect entrenchment of foundational representations rather than a maturational loss of plasticity, and that experience plays a central role in critical periods in language acquisition.

### 🤖 AI 总结

**一句话总结**：International adoptees retain phonological traces of a birth language they can no longer speak or comprehend, a persistence typically attributed to a biologically-timed critical period. We asked wheth...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Lost, but, not, erased, Finding, traces, forgotten

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25976v1) | [下载PDF](https://arxiv.org/pdf/2608.25976v1.pdf)

---

## cs.CV

## [14. VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105v1)

**作者**：Junxiang Xu, Ruisi Wang, Fanyi Pu 等 52 位作者  
**分类**：cs.CV, cs.AI, cs.LG, cs.MM, cs.RO  
**发布时间**：2026-08-26

### 📄 论文摘要

Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language. Yet progress remains bottlenecked by the lack of scalable training tasks, reliable feedback, and controlled comparisons across generative substrates. In this work, we introduce VBVR-Pro, a closed-loop testbed that makes native visual reasoning through generation trainable, verifiable, optimizable, and experimentally controllable. 1) Task scaling. VBVR-Pro turns visual reasoning into a controlled task space of 300 procedurally generated tasks. Models trained on VBVR-Pro show strong transfer beyond the proposed suite across seven external visual reasoning benchmarks such as RISE-Video, MME-CoF-Pro, and BabyVision. 2) Verifiable rewards. VBVR-Pro provides verifiable reward scorers for task-grounded evaluation. Through a systematic study of leading MLLMs as judges, we identify recurring failure modes of the prevalent VLM-as-a-judge paradigm. In contrast, the proposed scorers are grounded in deterministic, task-specific rules, achieve fine-grained alignment with human judgments. Importantly, they serve as reliable reward signals for large-scale multi-task reinforcement learning and demonstrate stronger post-RL performance across visual reasoning tasks. 3) Mechanism study. VBVR-Pro enables controlled modality studies across more than 30 image, video, and interleaved generators. Our analysis shows that video generation remains strongest for tasks requiring persistent spatiotemporal state tracking, while interleaved generation provides a compute-efficient alternative. Critically, ablations and probing suggest the presence of vision-native trajectories that are crucial to visual reasoning. We release all data, models, scorers, and code.

### 🤖 AI 总结

**一句话总结**：Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VBVR-Pro, Scalable, Verifiable, Suite, Native, Visual, Reasoning, treats

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26105v1) | [下载PDF](https://arxiv.org/pdf/2608.26105v1.pdf)

---

## [15. RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101v1)

**作者**：Bojia Zi, Xiaoyan Yang, Yu Zhou 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

Recent advances in video editing have been largely driven by large-scale instruction-based datasets. However, existing datasets still suffer from two critical limitations. First, target videos are commonly produced by automatic editing models, which may introduce visible artifacts and unreliable supervision signals. Second, most public datasets rely primarily on textual instructions, while lacking visual references that are crucial for precise, identity-preserving, and controllable editing. To address these limitations, we introduce RefVideo-6M, a large-scale reference-guided editing dataset containing 5 million video editing samples and 1 million image editing samples. To ensure reliable supervision, our dataset uses a construction pipeline that treats artifact-free real videos as editing targets and generates quality-filtered input conditions with multiple editing experts. In addition, it provides approximately 6 million visual references, covering diverse reference types and editing scenarios, thereby enabling models to learn fine-grained visual correspondence beyond text-only instructions. Based on RefVideo-6M, we further train a reference-guided video editing model, Ref-MoT, to evaluate the effectiveness and scalability of the proposed dataset. Extensive experiments demonstrate that RefVideo-6M provides substantially more reliable supervision than existing datasets and enables the training of powerful editing models with improved visual quality, controllability, and reference consistency. The open-source dataset is available at https://huggingface.co/datasets/RefVideo6M/RefVideo6M.

### 🤖 AI 总结

**一句话总结**：Recent advances in video editing have been largely driven by large-scale instruction-based datasets. However, existing datasets still suffer from two critical limitations. First, target videos are com...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RefVideo-6M, Reliable, Reference-Based, Dataset, Instructional, Video, Editing, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26101v1) | [下载PDF](https://arxiv.org/pdf/2608.26101v1.pdf)

---

## [16. MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching](https://arxiv.org/abs/2608.26094v1)

**作者**：Hao Yin, Paritosh Parmar, Lijun Gu 等 9 位作者  
**分类**：cs.CV, cs.AI, cs.ET, cs.HC, cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Existing action quality assessment (AQA) datasets and methods rely primarily on visual inputs such as RGB and pose, overlooking physiological dynamics such as muscle mechanics and often modeling actions as monolithic patterns. These limitations hinder fine-grained, biomechanically grounded feedback. We introduce MyoMechanix, a multimodal ecosystem for weight-loaded actions that aligns motion with muscle activity. Expert-annotated, it contains 7,500+ samples of 20 actions from 38 subjects, with synchronized multiview RGB video, 3D pose, sEMG, and additional physiological signals, forming the largest multimodal AQA benchmark to date. We further construct the Fitness Knowledge Graph (FKG), which organizes expert annotations into structured relationships among actions, phases, key steps, errors, and corrective feedback, enabling compositional scoring and interpretable assessment. Building on these representations, we develop CUBIST (Compositional Ontological Reasoning Engine), which performs decomposition-analysis-recomposition for fine-grained error attribution and feedback generation. We also establish MyoMechanix-AQA, MyoMechanix-VideoQA, and a novel MyoMechanix-Video2EMG task. Experiments show that multimodal sensing and structured representations improve performance, interpretability, and error attribution, with CUBIST achieving state-of-the-art results; VideoQA enhances language-grounded action understanding; and Video2EMG suggests video-based alternatives to costly EMG sensing. MyoMechanix advances skilled activity understanding toward biomechanically grounded, multimodal, and compositional reasoning for Physical AI applications in fitness, rehabilitation, healthcare, and machine learning. Project page: https://haoyin116.github.io/MyoMechanix/

### 🤖 AI 总结

**一句话总结**：Existing action quality assessment (AQA) datasets and methods rely primarily on visual inputs such as RGB and pose, overlooking physiological dynamics such as muscle mechanics and often modeling actio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MyoMechanix, Biomechanically-Grounded, Compositional, Skilled, Activity, Understanding, Coaching, Existing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26094v1) | [下载PDF](https://arxiv.org/pdf/2608.26094v1.pdf)

---

## [17. StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.26067v1)

**作者**：Zhe Liu, Jinghua Hou, Yuxiang Lu 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored temporal modeling. It treats each (visual observation, language instruction) pair as an atomic temporal unit: bidirectional attention within each pair enables cross-modal fusion, while causal attention across pairs preserves autoregressive streaming inference. This ensures the language instruction serves as a persistent semantic anchor throughout task execution. To bridge the gap between synchronous training and asynchronous real-robot deployment, we introduce a andom-interval streaming training strategy: a proper inter-frame interval (e.g., every 3 frames) enables faster and smoother action execution. Beyond this, randomizing the interval further improves robustness to frame-timing perturbations, supporting asynchronous deployment in practice. Furthermore, by leveraging the length extrapolation capability of the LLM backbone, StreamPI seamlessly inherits pretrained single-frame weights and supports flexible single-frame and multi-frame inference. Experiments on real-robot tasks spanning memory-dependent and precise perception scenarios, as well as the simulation benchmark LIBERO, demonstrate that StreamPI outperforms pi0.5 across diverse tasks.

### 🤖 AI 总结

**一句话总结**：Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StreamPI, Streaming, Multimodal, Temporal, Modeling, Vision-Language-Action, Models, VLA

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26067v1) | [下载PDF](https://arxiv.org/pdf/2608.26067v1.pdf)

---

## [18. UltraPIPS: Improving model perception in B-mode ultrasound with foundation models](https://arxiv.org/abs/2608.26033v1)

**作者**：Tal Grutman, Tali Ilovitsh  
**分类**：cs.CV, eess.IV  
**发布时间**：2026-08-26

### 📄 论文摘要

In medical imaging, it is common to use learned perceptual image patch similarity (LPIPS) to compare images semantically in feature space. Although backbones pretrained on natural images are widely used for LPIPS computation, B-mode ultrasound images possess distinct speckle patterns and acoustic-specific image statistics that are fundamentally different from natural images and even from other images in radiology. Consequently, we propose that domain-specific models are needed to measure perceptual similarity in ultrasound data, a finding which is not necessarily the case for other imaging modalities. We compare LPIPS metrics across downstream tasks like classification, segmentation and reconstruction using natural image, medical generalist and ultrasound backbone models and show that selection of LPIPS backbone is a non-trivial design choice. In particular, the ultrasound backbone models were more correlated with downstream performance of supervised models than classical and natural image models, and optimization of the LPIPS loss with an ultrasound backbone achieved a strong balance between reconstruction quality and realism. Our code is available at https://github.com/talg2324/UltraPIPS and introduces the UltraPIPS library, a set of LPIPS metrics based on the open-source foundation models analyzed in this paper.

### 🤖 AI 总结

**一句话总结**：In medical imaging, it is common to use learned perceptual image patch similarity (LPIPS) to compare images semantically in feature space. Although backbones pretrained on natural images are widely us...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UltraPIPS, Improving, model, perception, B-mode, ultrasound, foundation, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26033v1) | [下载PDF](https://arxiv.org/pdf/2608.26033v1.pdf)

---

## [19. Uncertainty-Guided Latent Diffusion Models for Faithful Super Resolution](https://arxiv.org/abs/2608.25998v1)

**作者**：Ren Wang, Yung-Yu Chuang  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

The perception-distortion trade-off poses a fundamental challenge in single-image super-resolution (SR). Although diffusion-based SR methods excel at generating perceptually realistic images, achieving high fidelity remains a key limitation. Recent advances in diffusion-based SR have shown promise in improving fidelity, but these methods often compromise perceptual quality due to their high reliance on a high-fidelity image. To address this, we introduce UGDiff, a novel diffusion guidance paradigm designed to further improve the perception-distortion balance. In particular, we first estimate the reconstruction uncertainty of the latent features corresponding to a high-fidelity image. This uncertainty is then used to guide the diffusion process to selectively restore high-frequency details in high-uncertainty regions, while preserving fidelity elsewhere. Furthermore, our guidance method adaptively identifies the high-uncertainty regions by considering not only the estimated uncertainty but also the posterior variance of the diffusion sampler at each timestep. This relaxes the reliance on the high-fidelity image in the later stages of sampling, thereby achieving a better perception-distortion balance. Extensive experimental results demonstrate that our method performs favorably against state-of-the-art diffusion-based SR methods.

### 🤖 AI 总结

**一句话总结**：The perception-distortion trade-off poses a fundamental challenge in single-image super-resolution (SR). Although diffusion-based SR methods excel at generating perceptually realistic images, achievin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Uncertainty-Guided, Latent, Models, Faithful, Super, Resolution, perception-distortion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25998v1) | [下载PDF](https://arxiv.org/pdf/2608.25998v1.pdf)

---

## [20. FRAME: separating sampling variation from representational cause in medical imaging fairness](https://arxiv.org/abs/2608.25981v1)

**作者**：Mahshad Lotfinia, Daniel Truhn, Andreas Maier 等 4 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Subgroup performance differences are the standard evidence for fairness bias in medical imaging, and the usual response removes the demographic information that a model encodes. Here we introduce Fair-model Reference And Mechanism Evaluation (FRAME), a two-step framework for auditing such a claim. The first step derives a fair-model reference, the distribution of the difference under exact fairness at the observed subgroup sizes. In the second step, we test the remainder with two operators in representation space. One operator cannot change a within-group ranking by construction. Across 702,206 images and 36 encoders, the reference accounts for a median 41% of the reported race difference and 22% of the age difference. Injecting demographic decodability leaves the remainder unchanged, while entangling the group with the disease direction raises the race difference from 0.077 to 0.118. No intervention we tested changes the remainder more than a change of random seed does. Those interventions reduce a difference at the operating point and leave the within-group ranking difference at a median of 0.000. Applied to 89 differences in 9 published studies across 6 medical imaging modalities, the reference accounts for a median 25% of a rate difference and 70% of a difference in the area under the receiver operating characteristic curve. Image-text pretraining instead raises worst-group performance by about 0.05. Applying FRAME before choosing an intervention could distinguish differences that need a mechanistic explanation from differences compatible with sampling variation at the current cohort sizes.

### 🤖 AI 总结

**一句话总结**：Subgroup performance differences are the standard evidence for fairness bias in medical imaging, and the usual response removes the demographic information that a model encodes. Here we introduce Fair...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FRAME, separating, sampling, variation, representational, cause, medical, imaging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25981v1) | [下载PDF](https://arxiv.org/pdf/2608.25981v1.pdf)

---

## [21. PANDA - Prototype-Anchored Alignment for Partially Unpaired Multimodal Learning, with Applications to Alzheimers MRI and TCGA Pathology](https://arxiv.org/abs/2608.25970v1)

**作者**：Sheethal Bhat, Mahfuzur Rahman Chowdhury, Paula Andrea Perez-Toro 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-26

### 📄 论文摘要

Multimodal medical prediction often faces incomplete pairing: auxiliary modalities with complementary signal are available for only a subset of subjects (or none) and cannot be assumed at deployment. We introduce PANDA (Prototype Anchored Data Alignment), a two-stage framework that transfers auxiliary information to a primary-modality model without auxiliary inputs at inference. Stage 1 learns a shared embedding from the paired subset and estimates class prototypes from auxiliary modalities; Stage 2 trains the primary encoder on all subjects using cross-entropy plus alignment to the frozen prototypes. Because supervision is defined at the class-prototype level, PANDA accommodates arbitrary pairing rates, including zero subject overlap. We evaluate PANDA on two applications. On a 1,021-subject multi-scanner ADNI cohort, we perform AD/CN classification with three auxiliary modalities at distinct pairing rates: tabular scores (44.8%), FDG-PET (18.7%), and external handwriting kinematics (0% overlap). Relative to the same-backbone MRI-only baseline, PANDA attains AUC 0.868 +-0.020 (+7.9pp) and reduces 1.5T CN false positives by 24.3pp; on a fully trainable Conv5-FC3 backbone it reaches AUC 0.893 (best overall). A pairing-rate ablation shows that the joint anchor remains within seed noise from 75% to 5% pairing. On TCGA-Lung survival prediction from whole-slide images with RNA-seq as auxiliary data, PANDA improves over WSI-only on 2-year OS (AUC +3.5pp) and Cox PH (C-index +9.0pts) and outperforms full-fusion training, which underperforms WSI-only, while requiring no RNA at inference; wide confidence intervals on this smaller cohort keep the gains below conventional significance. Overall, PANDA provides a deployment-oriented mechanism for leveraging incomplete auxiliary modalities to improve primary-modality prediction.

### 🤖 AI 总结

**一句话总结**：Multimodal medical prediction often faces incomplete pairing: auxiliary modalities with complementary signal are available for only a subset of subjects (or none) and cannot be assumed at deployment. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PANDA, Prototype-Anchored, Alignment, Partially, Unpaired, Multimodal, Learning, Applications

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25970v1) | [下载PDF](https://arxiv.org/pdf/2608.25970v1.pdf)

---

## [22. Less Contouring, More Accuracy: Lesion-Guided ROI Deep Learning for Ovarian Ultrasound Classification](https://arxiv.org/abs/2608.25965v1)

**作者**：Mehran Ahmad, Ali Abbasian Ardakani, Afshin Mohammadi 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

Ovarian lesion classification using transvaginal ultrasound remains challenging due to overlapping imaging characteristics and the dependence on expert interpretation. This study investigates whether lesion-guided region-of-interest (ROI) deep learning can achieve competitive diagnostic performance while reducing the annotation burden associated with pixel-level lesion segmentation. Two publicly available ovarian ultrasound datasets were evaluated: the Multi-Modality Ovarian Tumor Ultrasound (MMOTU) dataset for eight-class classification and the Ovarian Ultrasound Dataset (OUD) for binary classification. Four strategies were compared under a unified framework: global image-based deep learning, lesion-guided ROI-based deep learning, lesion contour-based deep learning, and contour-based radiomics with machine learning classifiers. Four deep learning architectures, MaxViT-Tiny, Swin Transformer, EfficientNet-B7, and ResNet18, were evaluated. Radiomics models were developed using support vector machine, k-nearest neighbors, and artificial neural network classifiers, with ANOVA-based feature selection applied for the lower-sample OUD dataset. The lesion-guided ROI strategy achieved the strongest overall performance, with MaxViT-Tiny obtaining 93.10% accuracy and an AUC of 0.99 on MMOTU and 97.56% accuracy and an AUC of 0.99 on OUD. The contour-based approach achieved comparable accuracy but required substantially higher annotation effort. These findings demonstrate that lesion-guided ROI deep learning provides an effective balance between diagnostic performance and annotation efficiency, offering a practical approach for scalable AI-assisted ovarian ultrasound analysis

### 🤖 AI 总结

**一句话总结**：Ovarian lesion classification using transvaginal ultrasound remains challenging due to overlapping imaging characteristics and the dependence on expert interpretation. This study investigates whether ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Less, Contouring, More, Accuracy, Lesion-Guided, Deep, Learning, Ovarian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25965v1) | [下载PDF](https://arxiv.org/pdf/2608.25965v1.pdf)

---

## [23. 4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956v1)

**作者**：Yueen Ma, Zenglin Xu, Irwin King  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeatedly process redundant background content. Although point clouds can represent the world in 3D space, they can be difficult to align and accumulate across viewpoints. In this paper, we leverage an explicit 4D Gaussian Splatting (4DGS) representation that separately models dynamic objects and the static background of a scene. For dynamic objects, we use a policy model to predict future actor actions and a world model to predict transformations of their observed Gaussian splats. The static background need not be regenerated for future states, as much of it has already been observed in past frames. This forms an object-centric world action model, which we name 4DGS-WAM. It lifts 2D observations into a persistent 4D representation so that previously observed static content can be reused during future prediction. Future-state extrapolation can then focus on modeling the evolution of dynamic objects. Experiments on KITTI-MOT evaluate short-horizon prediction and past reconstruction.

### 🤖 AI 总结

**一句话总结**：Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, 4DGS-WAM, Bridging, Past, Future, Object-Centric, World, Action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25956v1) | [下载PDF](https://arxiv.org/pdf/2608.25956v1.pdf)

---

## [24. Auditable CT Phenotyping Through Report-derived Radiological Observations](https://arxiv.org/abs/2608.25948v1)

**作者**：Riga Wu, Walter Witschey, Yicheng Li 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-26

### 📄 论文摘要

Medical image foundation models can predict clinical phenotypes from computed tomography (CT), but strong performance leaves open whether they read disease-specific findings or shortcuts that correlate with the diagnosis. We tested this in 221 electronic-health-record (EHR) phenotypes using Auditable CT phenotyping (ACT), built on report-derived radiological observations. We trained ACT on 38,317 patients, mined 376,194 observations and evaluated it in 25,183 held-out patients. ACT exceeded five vision-language baselines on zero-shot annotation, and CT-CLIP across 221 phenotypes from unseen CT pulmonary angiography, both under zero-shot scoring (0.651 versus 0.572) and under linear probing (0.709 versus 0.662). Reading each probe exposes what accuracy conceals: only 97 observations occupy the 221 rank-1 positions, and one phrase describing aortic and coronary calcification ranks first for 20 phenotypes, including osteoporosis, urinary tract infection and major depressive disorder. Restricting the bank to clinician-specified evidence redirects those probes onto phenotype-related observations in 86 phenotypes at no accuracy cost (0.751 versus 0.741). Accurate CT-based EHR phenotyping can therefore rest on observations that are not valid evidence for the coded phenotype and that ACT can identify and intervene on.

### 🤖 AI 总结

**一句话总结**：Medical image foundation models can predict clinical phenotypes from computed tomography (CT), but strong performance leaves open whether they read disease-specific findings or shortcuts that correlat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CT, Auditable, Phenotyping, Through, Report-derived, Radiological, Observations, Medical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25948v1) | [下载PDF](https://arxiv.org/pdf/2608.25948v1.pdf)

---

## cs.LG

## [25. Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role](https://arxiv.org/abs/2608.26093v1)

**作者**：Ahmad Khan, Akram Bin Sediq, Sara Azadegi Naeini 等 4 位作者  
**分类**：cs.LG, cs.IT, eess.SY  
**发布时间**：2026-08-26

### 📄 论文摘要

Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that this design layer can be surrendered to an autonomous agent in its entirety. We adopt the autoresearch protocol, in which an AI coding agent edits a training script, runs a fixed-budget experiment, and retains or discards the change according to a single immutable metric. We grant the agent authority over the architecture family, the input representation, the output parameterization, the loss function and the task-sampling law, and set it a target chosen for its difficulty: sum-least-percentile-rate power control across a multicell network. The formulation targets cell-edge throughput and is non-convex, non-smooth and strongly NP-hard away from its max-min vertex. Safeguards render the results trustworthy: a hash-pinned evaluator, an enforced inference contract and a pre-registered falsifier per experiment. In eighty-one unattended experiments over twenty-six hours, the agent reached $99.5\%$ of a converged minorization-maximization reference in one fixed-cost inference pass, at roughly $600\times$ lower inference cost, closing $94\%$ of the gap from its first working architecture, with one parameter set serving every network size and percentile target. It recovered provable structure rather than tuned constants: the output parameterization it discovered reproduces the exact max-min-optimal allocation at the minimum percentile, for every value of the trained weights.

### 🤖 AI 总结

**一句话总结**：Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agentic, Autoresearch, Cell-Edge, Power, Control, Radically, Redefining, Researcher's

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26093v1) | [下载PDF](https://arxiv.org/pdf/2608.26093v1.pdf)

---

## [26. TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086v1)

**作者**：Jiarui Yan, Weiwei Sun, Sijie Li 等 5 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-26

### 📄 论文摘要

Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over hours of feedback, and on most competitions still finishes below strong human competitors. Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. We introduce TraceML, which pairs human and agent work on the same competitions under one version-level schema: 4,465 human Kaggle trajectories across 134 competitions, seven of which are also worked by two agent scaffolds, giving 430 paired human and 207 agent trajectories. Every code version carries its score, its timestamp, and labels for the action taken, its intent, the edit size, and the score effect. Read this way, the gap becomes concrete. Experts alternate data work, validation, model changes, and ensembling, and return to approaches they had set aside. Each agent scaffold instead collapses into a narrow loop: Codex spends its steps re-weighting ensembles and tuning submissions, MLEvolve mutates its model in place, and neither pivots at the human rate nor reopens abandoned work. A short planning prompt distilled from human practice moves the behaviors it names toward the human profile and lifts scores, but the effort profile stays agent-shaped: instruction closes only the part of the gap that reduces to instructions. We release the corpus, the schema, the labelers, and the extraction pipeline at https://huggingface.co/datasets/jerryyan/TraceML.

### 🤖 AI 总结

**一句话总结**：Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, TraceML, Empirical, Analysis, Human-Agent, Planning, Machine

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26086v1) | [下载PDF](https://arxiv.org/pdf/2608.26086v1.pdf)

---

## [27. ICON Decomposition: Multivariate Concept-Level Explanations of Deep Representations for Model Auditing](https://arxiv.org/abs/2608.26083v1)

**作者**：Roshan Prakash Rane, Marco Simnacher, Manuel Pfeuffer 等 10 位作者  
**分类**：cs.LG, cs.AI, cs.CV, stat.ML  
**发布时间**：2026-08-26

### 📄 论文摘要

Deep neural networks often exploit spurious associations in their training data, a failure known as shortcut learning. Concept-based explainability methods screen for shortcuts by testing whether concepts such as a patient's sex or scanner settings can be decoded from a network layer. Because each concept is evaluated in isolation, these methods can mistake correlations between concepts as evidence that the model uses them. We introduce ICON decomposition, which instead quantifies how much of a layer's variance each concept explains after accounting for all other concepts and the outcome. On synthetic data with known ground truth, ICON recovers concept importance more accurately than seven alternative baseline methods. On skin-lesion and brain-imaging models, it isolates the concepts on which a model genuinely relies, quantifies the representation unexplained by any of the supplied concepts, and yields sparse explanations that we validate by retraining and out-of-distribution testing.

### 🤖 AI 总结

**一句话总结**：Deep neural networks often exploit spurious associations in their training data, a failure known as shortcut learning. Concept-based explainability methods screen for shortcuts by testing whether conc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, ICON, Decomposition, Multivariate, Concept-Level, Explanations, Deep, Representations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26083v1) | [下载PDF](https://arxiv.org/pdf/2608.26083v1.pdf)

---

## [28. Group-Shared Low-Rank Approximation for Mobile-Efficient Pointwise Convolutions in Large-Kernel CNNs](https://arxiv.org/abs/2608.26069v1)

**作者**：Hao Luo, Yiting Yang, Wenyi Zhao 等 13 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes storage-efficient edge deployment. While existing efficient architectures adopt parameter-efficient depthwise separable convolution backbones that leverage techniques like low-rank approximation and weight sharing to compress depthwise convolutions, we identify a critical oversight: pointwise convolutions dominate parameter volume (>87% in models like RepLKNet-31B) and constitute the primary deployment bottleneck on resource-constrained edge devices. This results in prohibitive storage costs and severe memory-loading constraints on resource-limited devices (e.g., smartphones with 4-12 GB Random Access Memory (RAM)). To overcome this, we propose Channel Group-Shared (CGS) low-rank approximation, a novel Singular Value Decomposition (SVD)-based parameter-sharing strategy. CGS constructs a structured low-rank paradigm isomorphic to SVD decomposition, comprising shared (high-parameter-cost) down/up-projection matrices across channel groups within a layer and channel-group-specific (low-parameter-cost) scalable diagonal matrices. This group-sharing design achieves significant parameter reduction. Extensive experiments demonstrate that large-kernel CNNs (RepLKNet, ConvNeXt, SLaK) enhanced with CGS strike an empirically favorable balance between competitive performance and substantially reduced storage costs. Crucially, by alleviating storage constraints, reducing memory bandwidth pressure during loading, and minimizing model loading latency, CGS enables the feasible deployment of pre-trained large-kernel CNN models on edge devices, thereby bridging the gap between high-performance vision models and practical edge deployment.

### 🤖 AI 总结

**一句话总结**：Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes st...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Group-Shared, Low-Rank, Approximation, Mobile-Efficient, Pointwise, Convolutions, Large-Kernel, CNNs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26069v1) | [下载PDF](https://arxiv.org/pdf/2608.26069v1.pdf)

---

## [29. DualOPSD: Adaptive Privileged Teachers for On-Policy Self-Distillation](https://arxiv.org/abs/2608.26019v1)

**作者**：Yutong Chen, Guangfu Guo, Zhichao Xu 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-08-26

### 📄 论文摘要

On-policy self-distillation (OPSD) uses a privileged copy of the student model to provide dense supervision without an external teacher. OPSD keeps this privileged teacher fixed, even though the student distribution and output style change during training. We propose DualOPSD, an asymmetric alternating framework that adapts both policies. The student first learns from the privileged teacher. The teacher then moves toward the updated student distribution on the same student trajectory. This update makes later supervision responsive to the learner and does not require another rollout. On Qwen3-8B in non-thinking mode, DualOPSD improves avg@12 over OPSD by 23.61, 13.89, and 10.00 points on AIME 2024, AIME 2025, and HMMT 2025. Results at 1.7B and 4B show that the accuracy gain depends on model scale. Across all three scales, DualOPSD reduces truncation. The 4B diagnostic also shows lower KL in both directions between the teacher and student.

### 🤖 AI 总结

**一句话总结**：On-policy self-distillation (OPSD) uses a privileged copy of the student model to provide dense supervision without an external teacher. OPSD keeps this privileged teacher fixed, even though the stude...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DualOPSD, Adaptive, Privileged, Teachers, On-Policy, Self-Distillation, OPSD, uses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.26019v1) | [下载PDF](https://arxiv.org/pdf/2608.26019v1.pdf)

---

## [30. When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness in LLMs](https://arxiv.org/abs/2608.25941v1)

**作者**：Suchit Gupte, Xueru Zhang, Mohammad Mahdi Khalili  
**分类**：cs.LG  
**发布时间**：2026-08-26

### 📄 论文摘要

Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood. We present a systematic study of how pruning affects SAE behavior and theoretically show that, for a fixed SAE, its impact is governed by perturbation energy, a covariance-weighted norm. This perspective exposes a key limitation of magnitude pruning: by ignoring activation geometry, it distorts the learned representation space and degrades SAE functionality. Activation-aware methods such as Wanda and SparseGPT, in contrast, implicitly control perturbation energy and are therefore substantially more robust at preserving SAE behavior. We further reveal a consistent structural vulnerability across all pruning methods: middle layers are significantly more sensitive to pruning than early or late layers. Guided by this insight, we propose a layer-wise sparsity allocation strategy, achieving lower perplexity under the same average pruning sparsity. Experiments across four model architectures validate our theoretical findings. Code is publicly available at https://github.com/osu-srml/sae-robustness-under-pruning/tree/main.

### 🤖 AI 总结

**一句话总结**：Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Pruning, Meets, Interpretability, Preserving, Sparse, Autoencoder, Robustness

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.25941v1) | [下载PDF](https://arxiv.org/pdf/2608.25941v1.pdf)

---

