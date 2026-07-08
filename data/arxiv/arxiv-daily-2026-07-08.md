# arXiv AI 论文日报 | 2026-07-08

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.LG](#csLG) (3 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (7 篇)

---

## cs.AI

## [1. Rethinking Indic AI from a Lens of Cultural Heritage Preservation](https://arxiv.org/abs/2607.06544v1)

**作者**：Aparna Madva, Sharath Srivatsa, Srinath Srinivasa 等 4 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-07-07

### 📄 论文摘要

As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this civilization. AI is seen as a ''double-edged sword'' where on the one hand, it can enable access and inclusion for a large population, on the other, it can homogenize worldviews and exclude underrepresented languages and worldviews. In this paper, we try to characterize this problem by addressing the extensive characteristic nature of Indian linguistics and the way they closely connect to cultural practices and worldview. We then perform a longitudinal survey of how Natural Language Processing (NLP) techniques have evolved in this space, tracing the historical development of Indic NLP, covering key milestones, methodological shifts, and resource creation efforts. In addition, the paper also examines the structural and sociolinguistic characteristics of Indian languages, such as rich morphology, complex scripts and grammar rules, diglossia, and large dialectal variation, and explains how these create unique challenges for building AI foundation models. We then discuss the growing role of Indic foundation models and analyze how these models address these long-standing resource and representation gaps. Finally, we propose a research direction called 'Culture Sensing', which re-imagines AI based on hermeneutic reasoning. Culture Sensing aims to address open problems such as ensuring equitable performance across low-resource languages and producing outputs that are culturally meaningful. By bringing together past work, current techniques, and emerging trends, this paper outlines research directions that can guide the next phase of Indic NLP and contribute to the development of more robust and inclusive Indic foundation models.

### 🤖 AI 总结

**一句话总结**：As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, As, Rethinking, Indic, Lens, Cultural, Heritage, Preservation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06544v1) | [下载PDF](https://arxiv.org/pdf/2607.06544v1.pdf)

---

## [2. The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology](https://arxiv.org/abs/2607.06531v1)

**作者**：Ghassen Marrakchi, Basarab Matei  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-07-07

### 📄 论文摘要

- Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. To address this inflexibility, we propose the Large Cancer Assistant (LCA), a model-agnostic, post-hoc orchestration framework designed for scalable clinical decision support. - Methods: The LCA is mathematically formalized as a 7-tuple architecture grounded in the principle of Algorithmic Impermeability, ensuring the orchestration logic remains strictly independent of underlying black-box AI models. We introduce the Entry Theory, leveraging Geometric Deep Learning (GDL) to standardize multimodal patient data along distinct structural and medical axes. The system dynamically orchestrates data via a Cancer Switching Module and intentionally isolates the core AI execution from volatile hospital IT infrastructures by outputting a Standardized Intermediate Payload (SIP). - Results: A Proof of Concept (PoC) validated the orchestration logic across four technical scenarios. The framework executed a nominal flow with negligible orchestration overhead. It empirically demonstrated algorithmic impermeability by maintaining an invariant routing projection during AI model swaps, and it validated strict failure-safety by achieving a 100\% recall rate in generating targeted Supplementary Data Requests (SDR) under injected data anomalies. Multi-protocol execution capability was also successfully verified. - Conclusion: By structurally decoupling multimodal ingestion from feature inference, the LCA provides a highly adaptable and modular orchestration foundation. The SIP establishes a clear architectural boundary, natively setting the stage for downstream Electronic Medical Record (EMR) interoperability as an independent future paradigm.

### 🤖 AI 总结

**一句话总结**：- Objective: Multimodal deep learning models in oncology are currently limited by monolithic designs that rigidly couple data ingestion, clinical routing, and artificial intelligence (AI) inference. T...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Large, Cancer, Assistant, LCA, Model-Agnostic, Orchestration, Framework, Scalable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06531v1) | [下载PDF](https://arxiv.org/pdf/2607.06531v1.pdf)

---

## [3. Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment](https://arxiv.org/abs/2607.06522v1)

**作者**：Han-Jun Ko, Jr-Jen Chen, Haobo Yuan 等 7 位作者  
**分类**：cs.AI, cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-thought (CoT) reasoning that contradicts physical reality, and misalignment between the model's reasoning and actions. We present VAORA (Visual Action Outcome Reasoning Alignment), a novel reward design that directly addresses both issues. VAORA introduces two complementary rewards: Visual Alignment Reward, which anchors VLM reasoning to the visual context independent of the agent action itself, and Visual-Action Alignment Reward, which grounds reasoning in the visual outcome induced by the model's action. Together, these rewards suppress hallucinated CoT and reduce the gap between reasoning and behavior. To improve training stability, we further employ smooth, dense rewards by estimating success probabilities using a pre-trained in-domain expert agent. Experiments on PHYRE and Virtual Tool support our performances across novel-task and unseen-environment settings, confirming that grounded and generalizable physical intelligence can be induced through VAORA.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-tho...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bridging, Physical, Reasoning, Task, Generalization, via, Visual, Action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06522v1) | [下载PDF](https://arxiv.org/pdf/2607.06522v1.pdf)

---

## [4. RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models](https://arxiv.org/abs/2607.06504v1)

**作者**：Qian Sun, Yong-Ming Tian, Jia-Wei Huang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Recent years have witnessed the emergence of multivariate modeling using time series foundation models (TSFMs), which achieve advanced zero-shot generalization. Modern multivariate TSFMs are predominantly pretrained on multivariate synthetic data, which is easier to scale but may fail to capture the complex temporal dynamics and cross-variable relationships present in real-world time series. This raises a key question: Whether and to what extent the leading TSFMs trained with the real-world corpus perform better than those trained with synthetic data? To answer this, we establish the RMISC corpus, a considerably large-scale, high-quality, openly accessible, real-world, and multivariate time series archive that contains around 200 datasets and 142 billion time points across diverse domains. Furthermore, we pretrain four advanced TSFMs on univariate, synthetic multivariate, and real-world multivariate data and evaluate their zero-shot generalization capabilities on standard in-distribution and out-of-distribution benchmarks. Experimental results show that incorporating real-world multivariate data predominantly improves the generalization performance for both univariate and multivariate TSFMs. These results provide a deeper understanding of how real-world multivariate data contributes to the development of stronger TSFMs.

### 🤖 AI 总结

**一句话总结**：Recent years have witnessed the emergence of multivariate modeling using time series foundation models (TSFMs), which achieve advanced zero-shot generalization. Modern multivariate TSFMs are predomina...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RMISC, Large-scale, Real-world, Multivariate, Corpus, Time, Series, Foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06504v1) | [下载PDF](https://arxiv.org/pdf/2607.06504v1.pdf)

---

## [5. Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade](https://arxiv.org/abs/2607.06503v1)

**作者**：Kai Ruan, Zihe Huang, Ziqi Zhou 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Large language model (LLM) agents solving multi-step tasks frequently commit to trajectories that are doomed to fail, yet continue to consume substantial inference compute before the failure becomes observable. We show that failure is predictable early from the agent's internal representations: lightweight per-round probes on hidden activations anticipate eventual episode failure as early as the first interaction round, where scorers reading only the agent's observable behavior are barely better than chance. We turn this signal into a practical abort cascade: one distribution-free calibrated gate per round, with per-round recall budgets jointly searched so that eventually-successful episodes survive all gates at a user-specified global rate; this episode-level guarantee is the one that matters in deployment, since false-abort risk accumulates across gates. Across two agent models on TextCraft, the cascade meets every recall target from 90% to 97% and, at the 90% target, saves 47.1% +/- 10.3% (Qwen-2.5-7B) and 37.2% +/- 8.8% (Llama-3.2-3B) of inference compute, 1.6--1.7x the best single-gate policy. An otherwise-identical cascade reading only behavior saves roughly half as much, and adding behavioral features to the probe yields no further gain: the hidden states capture what behavior reveals. Finally, we characterize the sample complexity of certifying high recall targets, telling practitioners which recall promises their data can, and provably cannot, back. The code will be released soon.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM) agents solving multi-step tasks frequently commit to trajectories that are doomed to fail, yet continue to consume substantial inference compute before the failure becomes o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Agent, Doomed, Start, Early, Abort, Episodes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06503v1) | [下载PDF](https://arxiv.org/pdf/2607.06503v1.pdf)

---

## [6. Multi-Agent Deep Reinforcement Learning for Multi Objective Battery Management in Dairy Farms](https://arxiv.org/abs/2607.06489v1)

**作者**：Marcos Eduardo Cruz Victorio, Karl Mason  
**分类**：cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

The dairy industry in Ireland has a large potential for the integration of renewable energy and the reduction of carbon emissions. However, researchers of distributed generation control are mainly focused on residential and commercial applications. To contribute to the effective integration of renewable energy in the dairy sector, this paper presents a multi-objective optimisation control system based on differential evolution and multi agent Deep Reinforcement Learning. The proposed control is organised in two layers: the upper layer uses dynamic pricing, and the lower layer is based on multi-agent reinforcement learning for battery management. This paper also simulates the electrical response of the proposed control system in a rural distribution circuit. The simulation results show that the proposed control framework can improve profits from energy arbitrage up to 18% compared to using Rule-based models, increase the use of distributed generation without significantly increasing cost, and comply with the Irish grid code in terms of voltage variation.

### 🤖 AI 总结

**一句话总结**：The dairy industry in Ireland has a large potential for the integration of renewable energy and the reduction of carbon emissions. However, researchers of distributed generation control are mainly foc...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Deep, Reinforcement, Learning, Multi, Objective, Battery, Management

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06489v1) | [下载PDF](https://arxiv.org/pdf/2607.06489v1.pdf)

---

## [7. A Physics-Informed Neural Network Framework for Elastodynamic Wave Propagation in Bimaterial Systems](https://arxiv.org/abs/2607.06479v1)

**作者**：Sonal Ankush Chibire, Jenn-Terng Gau, Bo Zhang  
**分类**：cs.AI, math-ph  
**发布时间**：2026-07-07

### 📄 论文摘要

Physics-informed neural networks (PINNs) provide a promising framework for solving partial differential equations while embedding the underlying physical laws directly into the learning process. This study presents a PINN-based framework for modeling transient elastodynamic wave propagation in bimaterial systems governed by the axisymmetric equations of linear elasticity. A steel-aluminum specimen representative of a Split Hopkinson Pressure Bar configuration is considered, and the governing elastodynamic equations, together with the corresponding initial, boundary, and interface conditions, are incorporated directly into the network through a physics-informed loss function. High-fidelity finite-element simulations performed using ANSYS Workbench Explicit Dynamics are used for validation and as supplementary data constraints during training. The proposed framework accurately predicts wave transmission and reflection across the bimaterial interface and reproduces axial and radial displacement histories, face-averaged responses, and the dominant stress and strain evolution with close agreement to the finite-element solutions. The trained network further demonstrates the ability to predict wave responses at previously unseen time instants and for modified material properties without requiring additional finite-element simulations, providing a continuous surrogate model for elastodynamic analysis. Mesh-sensitivity studies confirm numerical robustness, while additional material combinations demonstrate the generality of the proposed methodology. The results show that integrating physics-informed neural networks with explicit finite-element analysis provides an accurate and computationally efficient framework for elastodynamic wave propagation in heterogeneous solids, offering an effective surrogate modeling approach for high-rate solid mechanics and impact engineering applications.

### 🤖 AI 总结

**一句话总结**：Physics-informed neural networks (PINNs) provide a promising framework for solving partial differential equations while embedding the underlying physical laws directly into the learning process. This ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Physics-Informed, Neural, Network, Framework, Elastodynamic, Wave, Propagation, Bimaterial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06479v1) | [下载PDF](https://arxiv.org/pdf/2607.06479v1.pdf)

---

## [8. Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](https://arxiv.org/abs/2607.06447v1)

**作者**：Jihao Liu, Guoxiong Gao, Zeming Sun 等 11 位作者  
**分类**：cs.AI, cs.CL, cs.MA  
**发布时间**：2026-07-07

### 📄 论文摘要

Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrating such agents effectively remains challenging, due to the difficulty of coordinating parallel proof search while keeping intermediate claims organized and reliable. In this paper, we propose Danus, an orchestration system for research-level mathematical reasoning centered on a shared fact graph as a global memory-management mechanism. Danus consists of a main agent that performs planning and coordination, multiple worker agents that carry out proof search in parallel, and a stateless verifier that checks proposed mathematical claims before they are admitted into the fact graph. Each verified fact is stored together with its proof and logical dependencies, allowing the system to build long arguments incrementally while keeping the shared proof state organized. The main agent periodically summarizes the evolving proof state, redirects workers across promising directions, and supports interaction with human mathematicians through progress reports. We evaluate Danus through six research-level case studies in algebraic geometry, singularity theory, and combinatorics, illustrating how the fact-graph memory mechanism enables Danus to construct long, detailed mathematical proofs. Our results suggest that fact-graph-based orchestration provides an effective route toward scaling mathematical reasoning agents for long-horizon research problems. Danus is open source at https://github.com/frenzymath/Danus.

### 🤖 AI 总结

**一句话总结**：Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Danus, Orchestrating, Mathematical, Reasoning, Fact-Graph, Memory, Recent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06447v1) | [下载PDF](https://arxiv.org/pdf/2607.06447v1.pdf)

---

## cs.CL

## [9. On the feasibility of dependency parsing of non-human sequences without a gold standard. Is evaluation possible in other species?](https://arxiv.org/abs/2607.06542v1)

**作者**：Ramon Ferrer-i-Cancho, Catherine Hobaiter, Thore Bergman 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-07-07

### 📄 论文摘要

Dependency parsing consists of finding a tree representation for a sequence. Unsupervised dependency parsing aims to develop parsing methods without a gold standard during model training. In human languages, an unsupervised parser can be evaluated because some gold standard is usually available or can be created. For other species, a gold standard is unknown. Thus one may conclude that it is impossible to determine the accuracy of an unsupervised parser and, consequently, dependency parsing is unfeasible in other species. However, here we apply recent advances in network science to demonstrate that the proportion of correct edges retrieved by a parser must be high for the sequences of vocalizations or gestures that non-human primates produce due to the fast decay of the sequence length distribution. In contrast, human language sequences lack that property. Therefore, evaluation without a gold standard is feasible in non-human primates but a hard problem in humans.

### 🤖 AI 总结

**一句话总结**：Dependency parsing consists of finding a tree representation for a sequence. Unsupervised dependency parsing aims to develop parsing methods without a gold standard during model training. In human lan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, feasibility, dependency, parsing, non-human, sequences, without, gold

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06542v1) | [下载PDF](https://arxiv.org/pdf/2607.06542v1.pdf)

---

## [10. Life Style Levels: Neighborhood Delineation using Geospatial Data](https://arxiv.org/abs/2607.06529v1)

**作者**：Srivatsa Kulkarni, Debarag Banerjee  
**分类**：cs.CL  
**发布时间**：2026-07-07

### 📄 论文摘要

Fine-scale socioeconomic information is often unavailable across rapidly ur-banizing regions of the developing world, like India, limiting the ability to delineate intra-urban variations in affluence and deprivation. This study pro-poses a scalable, grid-based urban delineation framework using building morphology derived from open-source satellite imagery. Urban areas across 59 Indian cities and towns are partitioned into high-resolution spatial grids and characterized using interpretable morphological indicators, which are combined into a transparent, rule-based scoring framework to delineate areas with contrasting levels of urban affluence. The resulting classifications are validated through ground-level Google Street View observations, revealing a sharp contrast between the grid classes which are consistent with the ex-pected effects of the lifestyle affluence indicators. We further investigate density-based clustering of building footprints in Mumbai to identify dense urban settlements, demonstrating that the resulting clusters exhibit substan-tial spatial overlap with known informal settlements across the city. Finally, we conduct an exploratory analysis mapping consumer loan delinquency across the derived affluence classes. By relying entirely on publicly available geospatial data, the proposed framework provides a scalable, interpretable, and cost-effective approach for granular urban affluence mapping across In-dian cities.

### 🤖 AI 总结

**一句话总结**：Fine-scale socioeconomic information is often unavailable across rapidly ur-banizing regions of the developing world, like India, limiting the ability to delineate intra-urban variations in affluence ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Life, Style, Levels, Neighborhood, Delineation, Geospatial, Data, Fine-scale

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06529v1) | [下载PDF](https://arxiv.org/pdf/2607.06529v1.pdf)

---

## [11. RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](https://arxiv.org/abs/2607.06527v1)

**作者**：Sambaran Bandyopadhyay, Ananth Muppidi  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Multi-hop Question Answering over Knowledge Graphs faces a critical challenge: traditional retrieve-then-read pipelines break differentiability, preventing the retriever from learning to bridge the semantic gap where intermediate nodes lack lexical overlap with the query. To address this, we propose RSF-GLLM, a framework decoupling differentiable graph reasoning from answer generation. Our Recurrent Soft-Flow (RSF) module employs a GRU-guided query updater to propagate continuous relevance scores, utilizing a dynamic gating mechanism to traverse semantically dissimilar bridge nodes via structural cues. We introduce flow sparsity regularization to theoretically guarantee convergence from soft probabilities to discrete reasoning paths. These paths are extracted and textualized to fine-tune a Large Language Model (LLM), ensuring generation is grounded in factual topology. Experiments on WebQSP and CWQ demonstrate that RSF-GLLM achieves competitive performance with superior inference efficiency compared to LLM based computationally expensive approaches.

### 🤖 AI 总结

**一句话总结**：Multi-hop Question Answering over Knowledge Graphs faces a critical challenge: traditional retrieve-then-read pipelines break differentiability, preventing the retriever from learning to bridge the se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QA, RSF-GLLM, Bridging, Semantic, Gap, Multi-Hop, Knowledge, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06527v1) | [下载PDF](https://arxiv.org/pdf/2607.06527v1.pdf)

---

## [12. DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2607.06507v1)

**作者**：Yaqi Wu, Xiaolei Guo, Chenyu Zhou 等 10 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-07-07

### 📄 论文摘要

Multi-hop retrieval-augmented generation (RAG) acquires evidence sequentially, with each new document potentially revealing missing facts, bridge entities, query defects, or sufficient support for answering. Existing methods provide useful operations such as iterative retrieval, query reformulation, evidence critique, and sufficiency judging, but typically organize them within method-specific pipelines or predefined control topologies. This leaves underexplored how to learn a shared state-conditioned policy that chooses among currently valid evidence operations. We introduce DynaKRAG, which formulates multi-hop evidence acquisition as state-conditioned control over atomic evidence operations. At each step, a validity layer constructs the executable action set, and a learned controller selects the next operation. The resulting transition updates the evidence state and may enable new operations at subsequent steps. With Qwen2.5-7B-Instruct, DynaKRAG achieves F1 scores of 0.5998 on HotpotQA, 0.5340 on 2Wiki, and 0.3061 on MuSiQue, outperforming the strongest controlled baseline on all three benchmarks. Replacing the learned controller with a uniform-valid policy reduces F1 by 3.96--5.78 points, while removing sufficiency feedback hurts all three datasets. Controlled retrieval-cap experiments further show that additional retrieval is not uniformly beneficial. Together, these results demonstrate the benefit of coordinating retrieval, diagnosis, and gap-directed acquisition under an evolving evidence state.

### 🤖 AI 总结

**一句话总结**：Multi-hop retrieval-augmented generation (RAG) acquires evidence sequentially, with each new document potentially revealing missing facts, bridge entities, query defects, or sufficient support for ans...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DynaKRAG, Unified, Framework, Learnable, Evidence, Control, Multi-Hop, Retrieval-Augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06507v1) | [下载PDF](https://arxiv.org/pdf/2607.06507v1.pdf)

---

## [13. Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine](https://arxiv.org/abs/2607.06495v1)

**作者**：Juan S. Santillana  
**分类**：cs.CL, cs.AI, cs.LG, stat.AP  
**发布时间**：2026-07-07

### 📄 论文摘要

Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time. We present Pitwall, a production system that generates natural-language Formula 1 strategy briefings in English, Spanish, and Portuguese, treating faithfulness as an architectural property rather than an aspiration: every published sentence is decomposed into typed factual claims (positions, gaps, tyres, pace, overtakes, race control) and each claim is verified against the probabilistic race state that prompted it. The same verifier gates the fine-tuning data: of 3,045 model-written targets, only the 81.9% whose every claim is state-supported are retained, the rest falling back to a provably faithful template, so the generator never sees an ungrounded target. Verification is meaningful because of the grounding substrate: a vectorized Monte Carlo engine (N=2,000 per-lap race continuations) calibrated on 126 races (2018-2024) and validated on fully held-out 2025-2026 seasons (winner-in-top-3 90.3% over 155 backtests; held-out Brier 0.0745). A recurring finding spans both halves of the system: virtues trade off and must be gated separately. In simulation, calibration-optimal is not decision-optimal; in generation, fine-tuning on richer targets buys vividness that collapses into hallucination when the grounding state is sparse -- a failure a four-base replication traces to base-model instruction adherence, not scale, and that sparse-context auditing removes from the production model. End-to-end operation -- live timing to verified trilingual briefings -- was confirmed at two consecutive live Grands Prix (Austria and Britain, 2026); at Silverstone a timestamped probability trace, committed to disk before the outcome was known, locked onto the eventual winner ten laps before the flag.

### 🤖 AI 总结

**一句话总结**：Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pitwall, Faithful, Natural-Language, Race-Strategy, Briefings, Calibrated, Real-Time, Monte

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06495v1) | [下载PDF](https://arxiv.org/pdf/2607.06495v1.pdf)

---

## [14. Data Analysis in the Wild: Benchmarking Large Language Models Against Real-World Data Complexities](https://arxiv.org/abs/2607.06482v1)

**作者**：So Hasegawa, Shailaja Keyur Sampat, Lei Liu 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Current benchmarks for evaluating Large Language Models (LLMs) in data analysis often fail to reflect real-world settings. They typically focus on fact retrieval from small tables and overlook the challenges of large multi-tabular datasets, external knowledge integration, and exploratory insight discovery. We introduce DataGovBench, a benchmark derived from governmental open data designed to evaluate LLMs in practical scenarios. The benchmark includes two tasks: Table QA that requires solving complex decomposable questions and producing textual answers or visualizations, and Table Insight that evaluates the ability of models to generate expert-level findings through exploratory data analysis. Comprehensive experiments with state-of-the-art LLMs, both with and without agentic frameworks, reveal significant performance gaps across both tasks. These results suggest that current LLM-based systems remain far from satisfying the demands of real-world data analytics. DataGovBench provides a challenging benchmark for advancing research on LLMs capable of both answering analytical queries and discovering insights from data. Code and sample data are available at https://github.com/SoHasegawa/datagovbench.

### 🤖 AI 总结

**一句话总结**：Current benchmarks for evaluating Large Language Models (LLMs) in data analysis often fail to reflect real-world settings. They typically focus on fact retrieval from small tables and overlook the cha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data, Analysis, Wild, Benchmarking, Large, Language, Models, Against

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06482v1) | [下载PDF](https://arxiv.org/pdf/2607.06482v1.pdf)

---

## [15. From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b](https://arxiv.org/abs/2607.06452v1)

**作者**：Taeyun Roh, Eunha Lee, Wonjune Jang 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures for yes/no, factoid, and list questions according to their distinct reasoning and evaluation requirements. For yes/no questions, snippet shuffling and self-reflection are used to reduce sensitivity to evidence ordering and improve decision stability. For factoid questions, full-snippet input is combined with chain-of-thought-based in-context learning to support accurate biomedical entity identification. For list questions, a multi-agent architecture is employed, in which evidence extraction, candidate generation, answer verification, and final aggregation are handled collaboratively. Preliminary experiments on BioASQ 13b were used to identify effective inference strategies for each question type, and the resulting framework was subsequently evaluated in the official BioASQ 14b Task B challenge. In the official evaluation, our framework showed competitive performance across multiple batches and achieved first place in the factoid subtask of Batch 4. These results demonstrate the effectiveness of combining question-type-specific inference, ensemble prediction, and agent-based verification for reliable biomedical question answering.

### 🤖 AI 总结

**一句话总结**：Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LLM, 14b, Voting, Collaboration, Answer-Type-Aware, Pipelines, BioASQ

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06452v1) | [下载PDF](https://arxiv.org/pdf/2607.06452v1.pdf)

---

## cs.CV

## [16. Vision as Unified Multimodal Generation](https://arxiv.org/abs/2607.06560v1)

**作者**：Xiaoyang Han, Jianhua Li, Kewang Deng 等 17 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

We formulate computer vision as unified multimodal generation, where heterogeneous visual tasks are expressed in the native text and image generation spaces of a unified multimodal model, without task-specific architectures. Under this formulation, SenseNova-Vision uses natural-language instructions and optional visual prompts to specify tasks, target regions or views, and decoding conventions, and generates responses as text for symbolic outputs, images for dense spatial predictions, or mixed text-and-image outputs for compositional tasks. To support large-scale training, we convert diverse computer vision annotations into instruction-response examples compatible with these generation spaces, resulting in the SenseNova-Vision Corpus, a computer-vision instruction-response corpus spanning text, image, and mixed targets. Starting from an off-the-shelf pretrained unified multimodal model, SenseNova-Vision is trained primarily on this corpus, with auxiliary multimodal data used as a capability-preserving mixture, and requires no task-specific prediction heads or architectural modifications. The resulting model covers a broad range of vision tasks, including detection, OCR, keypoint estimation, segmentation, depth estimation, surface normal prediction, point maps, and camera pose estimation, while supporting language-defined variants that combine category, color, region, and other visual cues. Experiments show that a single unified model can match leading task-specialized systems across structured visual understanding, dense geometric prediction, segmentation, and multi-view visual geometry. These results suggest unified multimodal generation as a scalable route for integrating computer vision capabilities into general-purpose foundation models. The model and corpus are publicly available.

### 🤖 AI 总结

**一句话总结**：We formulate computer vision as unified multimodal generation, where heterogeneous visual tasks are expressed in the native text and image generation spaces of a unified multimodal model, without task...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, We, Vision, Unified, Multimodal, Generation, formulate, computer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06560v1) | [下载PDF](https://arxiv.org/pdf/2607.06560v1.pdf)

---

## [17. ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555v1)

**作者**：Ruihang Zhang, Felix Taubner, Pooja Ravi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Tracking the six-degree-of-freedom (6-DoF) pose of objects and surfaces from monocular video is a long-standing problem in computer vision. To tackle this problem, existing methods require inputs beyond the video itself-such as 3D models, depth maps, object masks, or task-specific learned features-and they struggle with textureless, transparent, reflective, or deformable surfaces. Here, we introduce ProxyPose, which recasts 6-DoF pose tracking as video-to-video translation. Given only a video and a single marked pixel in the first frame, a fine-tuned video diffusion model translates the input into a proxy video-a synthetic video depicting a colored polyhedron undergoing the same local rigid-body motion as the surface region at the marked pixel. Because the proxy's geometry and appearance are known by construction, recovering its full 6-DoF trajectory reduces to classical pose estimation with off-the-shelf solvers. This formulation leverages large-scale video pre-training to absorb the hardest aspects of pose tracking-handling challenging materials, occlusions, and deformations-into the translation step, while operating at the pixel level with no assumptions about object identity, boundaries, or global rigidity. ProxyPose achieves state-of-the-art 6-DoF pose tracking accuracy without the additional inputs required by competing methods and after fine-tuning the video model only on synthetic data. We further demonstrate that ProxyPose extends to face tracking, camera pose estimation, and challenging in-the-wild scenes that are beyond the reach of existing approaches. Project page: https://ruihangzhang97.github.io/proxypose/.

### 🤖 AI 总结

**一句话总结**：Tracking the six-degree-of-freedom (6-DoF) pose of objects and surfaces from monocular video is a long-standing problem in computer vision. To tackle this problem, existing methods require inputs beyo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ProxyPose, 6-DoF, Pose, Tracking, via, Video-to-Video, Translation, six-degree-of-freedom

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06555v1) | [下载PDF](https://arxiv.org/pdf/2607.06555v1.pdf)

---

## [18. MonoIR-RS: Infrared Remote Sensing Vision-Language Learning with CLIP and VLM Adaptation](https://arxiv.org/abs/2607.06552v1)

**作者**：Jiaju Han, Ma Yaqi, Yahui Chai 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Infrared remote-sensing imagery captures intensity structure, object-background contrast, and illumination-invariant cues often invisible in RGB imagery. Yet, most remote-sensing vision-language resources and models focus on visible-band semantics, leaving infrared vision-language understanding underexplored. We introduce MonoIR-RS, a large-scale infrared remote-sensing vision-language dataset and benchmark that couples IR-aware data construction with CLIP-style contrastive adaptation and VLM instruction tuning. Built from the same source pool and split as FusionRS, MonoIR-RS retains the infrared image as the model-facing modality, yielding 600,000 synthesized infrared images and 59,032 retained IR-aware caption records. The model experiments use this retained language-supervision subset, whose captions rewrite supervision around grayscale structure and infrared-style contrast instead of RGB appearance. We show that the synthesized infrared imagery is markedly closer to real thermal imagery than a grayscale conversion on the AVIID benchmark. We fine-tune five CLIP backbones and six VLM backbones, and calibrate them against zero-shot behavior: IR-aware adaptation lifts CLIP mean recall by up to 12.8 points and drives VLM captioning IR-cue coverage to 100% while reducing residual RGB-color leakage to near zero. By isolating the infrared modality from RGB-IR dual-modal learning, MonoIR-RS offers a controlled, reproducible testbed for aligning infrared remote-sensing evidence with language.

### 🤖 AI 总结

**一句话总结**：Infrared remote-sensing imagery captures intensity structure, object-background contrast, and illumination-invariant cues often invisible in RGB imagery. Yet, most remote-sensing vision-language resou...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MonoIR-RS, Infrared, Remote, Sensing, Vision-Language, Learning, CLIP, VLM

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06552v1) | [下载PDF](https://arxiv.org/pdf/2607.06552v1.pdf)

---

## [19. Unsupervised Domain Adaptation for Calcification Classification in Mammography Across Multi-Site Datasets](https://arxiv.org/abs/2607.06549v1)

**作者**：Xuan Liu, Derek L. Nguyen, Emily C. Barre 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Deep learning-based computer-aided diagnosis (CAD) systems have shown strong performance in breast cancer diagnosis, particularly for classification tasks in mammography. However, domain shifts across multi-site datasets remain a challenge, especially when models are applied to unseen domains. In this work, we proposed a calcification classification framework to improve malignant versus benign breast disease classification across multi-site mammography datasets. The framework consisted of two components: (1) an unsupervised domain adaptation module based on style transfer models (AdaIN and CycleGAN) to generate vendor-specific and technique-specific training samples without additional annotations, and (2) a supervised classification module using Swin Transformer V2 as the backbone. We evaluated the proposed method on three datasets: cross-validation on OPTIMAM (National Health Service, United Kingdom; n=2994), followed by external validation on EMBED (Emory University; n=125), and Duke Calcification Dataset v1 (n=788). These datasets cover multiple vendors and include both full-field digital mammography and synthetic 2D images derived from digital breast tomosynthesis. The proposed framework improved cross-site performance for both EMBED (AUC 0.68 to 0.72) and the Duke Calcification Dataset (AUC 0.68 to 0.73). These findings indicate that domain adaptation can reduce domain shifts and improve the generalization for calcification classification across multi-site datasets.

### 🤖 AI 总结

**一句话总结**：Deep learning-based computer-aided diagnosis (CAD) systems have shown strong performance in breast cancer diagnosis, particularly for classification tasks in mammography. However, domain shifts across...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Unsupervised, Domain, Adaptation, Calcification, Classification, Mammography, Across, Multi-Site

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06549v1) | [下载PDF](https://arxiv.org/pdf/2607.06549v1.pdf)

---

## [20. Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516v1)

**作者**：Songbur Wong, Xiaosong Jia, Junqi You 等 15 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Evaluating end-to-end autonomous driving (E2E-AD) remains challenging, as existing driving simulation methods often trade off closed-loop interactivity (e.g., CARLA) and real-world visual fidelity (e.g., nuScenes). We present \textbf{\emph{Point as Skeleton}}, a generative sensor simulation framework for state-updated autoregressive driving video generation, in which an autoregressive generator synthesizes visual observations from step-wise updated ego states, actor states, scene maps, and point-cloud skeleton conditions. To support closed-loop rollout, we introduce Reset-and-Roll, which adapts rolling diffusion inference to simulation by preventing future-conditioned latent states from being committed across simulation steps. To stabilize error accumulation during step-wise autoregressive rollout, we introduce point-cloud skeletons that decouple foreground and background assets and project them into camera-view painted-point and template-depth conditions, providing appearance and geometric cues. We further implement a nuPlan-based renderer-level closed-loop generative interface for evaluating generation under ego deviations from the original log. Experiments on nuScenes and nuPlan show that \textit{Point as Skeleton} improves autoregressive generation quality during closed-loop rollout, demonstrating its potential for visually faithful closed-loop driving simulation. The code is available at https://github.com/krauwu/point-as-skeleton.

### 🤖 AI 总结

**一句话总结**：Evaluating end-to-end autonomous driving (E2E-AD) remains challenging, as existing driving simulation methods often trade off closed-loop interactivity (e.g., CARLA) and real-world visual fidelity (e....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Point, Skeleton, Accumulated, Cloud, Enhanced, Autoregressive, Generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06516v1) | [下载PDF](https://arxiv.org/pdf/2607.06516v1.pdf)

---

## [21. AirflowAttack: Thermal-Airflow Adversarial Perturbations against Infrared Remote-Sensing Vision-Language Models](https://arxiv.org/abs/2607.06485v1)

**作者**：Cong Su, Jiaju Han, Xuemeng Sun 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Vision-language models (VLMs) are increasingly deployed on infrared (IR) remote sensing imagery in security-critical settings, yet their adversarial robustness remains unexamined. We present AirflowAttack, to our knowledge the first adversarial attack for IR remote-sensing VLMs and the first to weaponize thermal-airflow turbulence as the perturbation prior. A lightweight generator synthesizes a single input-agnostic perturbation regularized toward physically plausible airflow patterns. Optimized on one surrogate CLIP model, it attains a mean zero-shot scene-classification attack success rate (ASR, the fraction of samples whose top-1 class changes) of 48.5% across five diverse CLIP backbones, far exceeding four IR-specific physical baselines (27.7--37.0%). Applied to six state-of-the-art VLMs, it cuts scene-classification accuracy by up to 38.2% relative, yet paradoxically makes some models more confident in their IR analysis, confabulating the perturbation as genuine thermal evidence such as temperature gradients and convection. Ablations show the airflow prior raises physical plausibility at no measurable cost to attack success. Together with a benchmark spanning eleven models and four tasks, these findings expose critical vulnerabilities in the rapidly expanding IR VLM ecosystem.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) are increasingly deployed on infrared (IR) remote sensing imagery in security-critical settings, yet their adversarial robustness remains unexamined. We present AirflowAt...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AirflowAttack, Thermal-Airflow, Adversarial, Perturbations, against, Infrared, Remote-Sensing, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06485v1) | [下载PDF](https://arxiv.org/pdf/2607.06485v1.pdf)

---

## [22. Mitigating Domain Shift in Conditioned Floor Plan Generation: Synthetic Pre-training for Data-Efficient Adaptation](https://arxiv.org/abs/2607.06483v1)

**作者**：Matthieu Ospici, Arnaud Gueze, Luc Bourrat 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Robustness to domain shift is a key requirement for floor plan generative models to be applicable beyond the single dataset they were trained on, as floor plans vary widely across regions due to distinct architectural cultures, spatial constraints, and construction practices, while acquiring new annotated datasets remains costly and domain-specific. Yet, no prior work has studied this robustness in the context of conditioned floor plan generation. In this paper, we evaluate state-of-the-art models from two fundamentally different generative paradigms across three public datasets (RPLAN, MagicPlan and Swiss Dwellings) and show that they are highly sensitive to domain shift, with up to an order of magnitude performance degradation when transferred across domains. To mitigate this with minimal target-domain supervision, we introduce a procedural method to generate a large-scale synthetic training dataset that enforces strict physical constraints (non-overlapping rooms, valid door placement, graph consistency) while intentionally sacrificing architectural realism through highly irregular spatial arrangements and aggressive geometric perturbation of room shapes. We show that pre-training on this synthetic data considerably improves zero-shot cross-domain performance, outperforming in-domain training on MagicPlan. Furthermore, it provides a highly effective initialization for fine-tuning, accelerating target domain adaptation and outperforming real-world initialization baselines by up to 40% in a low-data regime.

### 🤖 AI 总结

**一句话总结**：Robustness to domain shift is a key requirement for floor plan generative models to be applicable beyond the single dataset they were trained on, as floor plans vary widely across regions due to disti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mitigating, Domain, Shift, Conditioned, Floor, Plan, Generation, Synthetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06483v1) | [下载PDF](https://arxiv.org/pdf/2607.06483v1.pdf)

---

## [23. A VLM-Enhanced Framework for Comprehensive Traffic Sign Condition Assessment Integrating Daytime Visual Performance and Nighttime Retroreflectivity Evaluation](https://arxiv.org/abs/2607.06478v1)

**作者**：Linlin Zhang, Neema Jakisa Owor, Xiang Yu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Traffic signs are crucial components of road safety, serving as visual tools under all lighting conditions. The Manual on Uniform Traffic Control Devices (MUTCD) specifies daytime visual factors such as legibility and color contrast, and nighttime retroreflectivity requirements. Traditional assessment methods rely on manual inspections, which the Federal Highway Administration (FHWA) notes are subjective, labor-intensive and pose safety concerns, while retroreflectometers are expensive and unaffordable for smaller agencies. Most existing studies focus on either daytime factors or nighttime retroreflectivity but rarely integrate both aspects comprehensively. This study develops a novel framework that systematically evaluates traffic signs through integrated daytime-nighttime assessment. The methodology employs three fine-tuned Vision Language Models (VLMs) for daytime visual performance assessment across four key factors: legibility, color, surface and shape integrity, and surrounding environment conditions. VLM predictions are converted to numerical scores through sentiment analysis and Contrastive Language-Image Pre-Training (CLIP) scoring, while nighttime performance is assessed using LiDAR-derived retroreflectivity following established calibration procedures. The framework integrates these components into a comprehensive Sign Condition Index (SCI) for maintenance guidance. Evaluation results demonstrated that LLaVA and Qwen outperformed InternVL, achieving bidirectional cosine similarity scores of 0.67-0.76 across all factors. Among 462 validated traffic signs, 68 were flagged by the proposed framework as requiring immediate replacement due to inadequate retroreflectivity performance. This research provides a cost-effective alternative to traditional manual inspections for comprehensive traffic sign condition assessment.

### 🤖 AI 总结

**一句话总结**：Traffic signs are crucial components of road safety, serving as visual tools under all lighting conditions. The Manual on Uniform Traffic Control Devices (MUTCD) specifies daytime visual factors such ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VLM-Enhanced, Framework, Comprehensive, Traffic, Sign, Condition, Assessment, Integrating

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06478v1) | [下载PDF](https://arxiv.org/pdf/2607.06478v1.pdf)

---

## [24. EgoPolice: A Benchmark for Egocentric Video Understanding in High-Stakes Police Body-Worn Camera Footage](https://arxiv.org/abs/2607.06468v1)

**作者**：Max Gonzalez Saez-Diez, Jihoon Chung, Adam D. Wolsky 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

We introduce EgoPolice, a carefully curated dataset of real, egocentric police-civilian interactions, sourced from publicly available body-worn camera videos. We select police-civilian action labels that are critical for police behavioral research and annotate them at a second-by-second granularity. The videos feature rapid and irregular camera motion, dense human interactions, and rare high-stakes events, making the dataset a challenging benchmark for motion-robust and context-aware egocentric perception. We provide two different tasks, classification and multiple-choice question-answering, and benchmark both open-source and closed-source models. We find that even the best video models like Gemini 2.5 Pro still struggle to accurately predict high-risk actions such as "Weapon Out". Beyond serving as a benchmark, EgoPolice provides a foundation for developing models capable of identifying events of interest in large-scale body-worn camera video repositories, enabling more efficient downstream human review.

### 🤖 AI 总结

**一句话总结**：We introduce EgoPolice, a carefully curated dataset of real, egocentric police-civilian interactions, sourced from publicly available body-worn camera videos. We select police-civilian action labels t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EgoPolice, Benchmark, Egocentric, Video, Understanding, High-Stakes, Police, Body-Worn

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06468v1) | [下载PDF](https://arxiv.org/pdf/2607.06468v1.pdf)

---

## [25. Verification of Dynamic Holographic Behavior in Identity Documents](https://arxiv.org/abs/2607.06466v1)

**作者**：Glen Pouliquen, Joseph Chazalon, Guillaume Chiron 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

This paper addresses the remote verification of the authenticity of Optically Variable Devices (commonly known as holograms) on identity documents. Typically placed over the cardholder's photo, these devices provide strong and easily verifiable security for human inspection but pose challenges for automated verification. Existing approaches easily cover static frauds (e.g. paper photocopy) and can be evaluated for such, but their capacity to detect real, dynamic fraud cases (e.g. handcrafted hologram) has not been evaluated to date because of the lack of public datasets. Furthermore, they are usually trained to detect known attack types, and few of them can generalize to new, unseen attacks. This work features three contributions to address these limitations: 1) a new public dataset, MIDV-DynAttack, which extends the existing MIDV-Holo dataset with realistic, static and dynamic attacks against identity document specimens, tripling the number of attack samples compared to the original dataset, 2) a novel verification method which can assess the authenticity of a specific hologram thanks to the analysis of its dynamic behavior and appearance, can be trained without dynamic attack samples, and exhibits new state-of-the-art performance, 3) a benchmark of existing approaches which follows a clear evaluation protocol and emphasizes the inability of other approaches to deal with dynamic attacks, as well as new challenging attacks to deal with. Code and dataset are publicly available at https://github.com/EPITAResearchLab/pouliquen.25.icdar.

### 🤖 AI 总结

**一句话总结**：This paper addresses the remote verification of the authenticity of Optically Variable Devices (commonly known as holograms) on identity documents. Typically placed over the cardholder's photo, these ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Verification, Dynamic, Holographic, Behavior, Identity, Documents, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06466v1) | [下载PDF](https://arxiv.org/pdf/2607.06466v1.pdf)

---

## [26. Andha-Dhun: A First Look at Audio Descriptions in Hindi](https://arxiv.org/abs/2607.06457v1)

**作者**：Ritabrata Chakraborty, Divy Kala, Nisheeth Bhooshan Gupta 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-07-07

### 📄 论文摘要

Audio Descriptions (ADs) narrate visual content for Blind and Low Vision (BLV) audiences during gaps in audiovisual media. There is growing momentum around ADs in movies and TV shows, and with mandates from India's Central Board of Film Certification (CBFC), there is a need to expand ADs beyond English. Yet, there is no work that generates ADs for any Indian language. To address this gap, we present the first systematic study of ADs in Hindi, contributing to aspects such as data, generation, and evaluation. We introduce Andha-Dhun, the first dataset of human-authored Hindi ADs collected from 8 full-length movies. We explore two approaches for generating ADs in Hindi: (i) directly from English dense video descriptions, and (ii) translating English ADs into Hindi. We evaluate these approaches using perplexity and LLM-as-a-judge metrics to assess fluency and quality respectively. We also analyze movies that have both English and Hindi human-authored ADs and find that naive translation introduces artifacts and narrows diversity compared to original Hindi ADs. Direct machine translation fails to adapt cultural references, while human-translated ADs do better but still fall short. Our findings emphasize that the purpose of Hindi ADs is accessibility for Indian BLV audiences, and that this requires adapting content for the audience more than strict fidelity to the source.

### 🤖 AI 总结

**一句话总结**：Audio Descriptions (ADs) narrate visual content for Blind and Low Vision (BLV) audiences during gaps in audiovisual media. There is growing momentum around ADs in movies and TV shows, and with mandate...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：at, Andha-Dhun, First, Look, Audio, Descriptions, Hindi, ADs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06457v1) | [下载PDF](https://arxiv.org/pdf/2607.06457v1.pdf)

---

## [27. Analysis-by-Proxy: Localization Signals in VLMs Operating as Condition Encoders](https://arxiv.org/abs/2607.06445v1)

**作者**：Yoav Baron, Sara Dorfman, Roni Paiss 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Vision-Language Models (VLMs) are increasingly utilized as the conditioning backbone for diffusion-based image editing due to their remarkable multimodal reasoning capabilities. While standalone VLMs demonstrate strong localization capabilities, editing pipelines frequently struggle to maintain this accuracy, particularly in complex, multi-entity scenes. In this work, we investigate this performance gap, hypothesizing that it stems from treating the VLM as a condition encoder. In this role, the model is restricted to a single forward pass, preventing the autoregressive generation process for which it was optimized, thereby failing to fully expose its capabilities. To investigate whether this spatial understanding persists when the VLM is used as a condition encoder, we introduce Analysis-by-Proxy. In this framework, we train a lightweight, interpretable proxy model on the VLM's intermediate representations using an auxiliary localization task. By analyzing the VLM through this proxy, we uncover the specific VLM representations that encode localization information. Our findings expose a fundamental mismatch between how spatial knowledge is represented within a VLM condition encoder and how it is extracted by current editing pipelines. We reveal that under single-pass constraints, the localization signal does not reliably propagate to the predefined layer configurations commonly used for conditioning. Instead, this crucial signal remains hidden within intermediate representations, at locations that vary depending on the input prompt. Using our introduced Analysis-by-Proxy framework, we reveal the fundamental failures of existing condition extraction strategies in editing pipelines, opening the door to more principled design of conditioning architectures.

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) are increasingly utilized as the conditioning backbone for diffusion-based image editing due to their remarkable multimodal reasoning capabilities. While standalone VLMs ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Analysis-by-Proxy, Localization, Signals, VLMs, Operating, Condition, Encoders

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06445v1) | [下载PDF](https://arxiv.org/pdf/2607.06445v1.pdf)

---

## cs.LG

## [28. Graph Convolutional Attention: A Spectral Perspective on Graph Denoising and Diffusion](https://arxiv.org/abs/2607.06546v1)

**作者**：Shervin Khalafi, Igor Krawczuk, Sergio Rozada 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-07-07

### 📄 论文摘要

Denoising graphs is a fundamental problem in graph learning and the core operation of graph diffusion models. Attention-based architectures like graph transformers have recently shown promise in denoising graphs. However, our principled understanding of attention-based graph denoising remains limited, making it unclear whether standard attention is the right mechanism for this task. Here we show that, under a denoising objective, linear attention is suboptimal and can only learn an average spectral denoising filter over the training distribution. This creates a fundamental limitation as graphs often vary spectrally across the distribution. To overcome this limitation, we introduce Spectral Attention, which directly utilizes the input graph spectrum and provably outperforms linear attention by a margin governed by the spectral diversity of the distribution. We then derive Graph Convolutional Attention (GCA), a practical and permutation-equivariant realization of this idea that implements spectral denoising through graph-filtered queries and keys. For stochastic block models, GCA provably matches the idealized Spectral Attention mechanism. We further show that the softmax operation, that follows the attention, provides additional denoising by approximately projecting noisy eigenvectors onto the clean eigenspace. Empirically, replacing linear attention with GCA consistently improves graph denoising and diffusion on synthetic and real datasets, with gains strongly correlated with spectral diversity. In DiGress, GCA matches standard graph-transformer performance without computing expensive structural features, and when combined with the recently proposed PEARL positional encodings, avoids explicit eigendecomposition computations resulting in faster inference without degrading quality. The code can be found here: github.com/shervinkhalafi/graph_conv_att

### 🤖 AI 总结

**一句话总结**：Denoising graphs is a fundamental problem in graph learning and the core operation of graph diffusion models. Attention-based architectures like graph transformers have recently shown promise in denoi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Graph, Convolutional, Attention, Spectral, Perspective, Denoising, graphs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06546v1) | [下载PDF](https://arxiv.org/pdf/2607.06546v1.pdf)

---

## [29. GraphBU: MILP Instance Generation with Graph-Native Block Units](https://arxiv.org/abs/2607.06532v1)

**作者**：Xiaolei Guo, Chenyu Zhou, Jianghao Lin 等 4 位作者  
**分类**：cs.LG, math.OC  
**发布时间**：2026-07-07

### 📄 论文摘要

Mixed-integer linear programming (MILP) instances used for solver development are hard to obtain when models come from private or application-specific pipelines. A generator must keep the structure that solvers and learned policies rely on. Existing general generators usually choose their generation unit from a formulation template, summary statistics, local graph edits, or blocks found after recombination. These units do not explicitly record how a local part of the MILP is coupled to the rest of the instance. We propose GraphBU, a graph-native generator whose basic unit is a local subproblem plus its interface. The method promotes coupling nodes into master constraints or boundary variables and uses the resulting block units for compatibility-checked replacement. The analysis focuses on the properties needed by this construction: promotion separates interfaces, replacement can preserve feasibility under an interface-slack condition, and the graph construction is invariant to row-column permutations. On MILP instances generation, this unit keeps graph statistics close to the source family, preserves feasibility on most datasets, and improves downstream Predict-and-Search training. Genrated by GraphBU, The average graph-statistical similarity was approximately 0.934, the average feasibility was approximately 96.7%, and the average increase in the main index of downstream PS was approximately 8.0%.

### 🤖 AI 总结

**一句话总结**：Mixed-integer linear programming (MILP) instances used for solver development are hard to obtain when models come from private or application-specific pipelines. A generator must keep the structure th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GraphBU, MILP, Instance, Generation, Graph-Native, Block, Units, Mixed-integer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06532v1) | [下载PDF](https://arxiv.org/pdf/2607.06532v1.pdf)

---

## [30. EntroPath: Maximum Entropy Path Ensemble Embedding for Manifold Learning](https://arxiv.org/abs/2607.06497v1)

**作者**：Przemysław Rola  
**分类**：cs.LG, q-bio.QM, stat.ML  
**发布时间**：2026-07-07

### 📄 论文摘要

We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally normalised random walks or on shortest-path distances. The former can concentrate diffusion in densely sampled regions, while the latter are sensitive to spurious shortcut edges in the graph. EntroPath instead builds its dissimilarities from the maximum entropy random walk (MERW), which aggregates the full ensemble of k-step paths between points rather than relying on any single trajectory. We show that the resulting free-energy dissimilarity converges to squared geodesic distance in the short-time limit, via Varadhan's heat-kernel formula. The diffusion depth k interpolates smoothly between local neighbourhood structure and global manifold geometry, and the symmetrised kernel admits an exact Gram factorisation connecting EntroPath to kernel methods. We further provide scalable extensions via landmark projection and diffusion-potential pseudotime. Across synthetic manifolds and single-cell benchmarks, EntroPath consistently matches or outperforms diffusion- and shortest-path-based methods, while remaining competitive with neighbourhood-preserving embeddings (UMAP, t-SNE) on local-structure metrics. Its gains are most pronounced on manifolds with non-uniform sampling density and well-separated branching trajectories, where path-ensemble diffusion more faithfully preserves the underlying geodesic geometry.

### 🤖 AI 总结

**一句话总结**：We introduce EntroPath, a manifold learning method that recovers geodesic geometry from data graphs through ensembles of diffusion paths. Many existing graph-based embeddings rely either on locally no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EntroPath, Maximum, Entropy, Path, Ensemble, Embedding, Manifold, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2607.06497v1) | [下载PDF](https://arxiv.org/pdf/2607.06497v1.pdf)

---

