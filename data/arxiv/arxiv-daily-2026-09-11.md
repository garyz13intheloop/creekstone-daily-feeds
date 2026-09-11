# arXiv AI 论文日报 | 2026-09-11

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (5 篇)
- [cs.LG](#csLG) (11 篇)
- [cs.AI](#csAI) (6 篇)
- [cs.CL](#csCL) (8 篇)

---

## cs.AI

## [1. Can Edge-Deployable Vision-Language Models Identify Species?](https://arxiv.org/abs/2609.11916v1)

**作者**：William Zhou, Mayukha Siripuram, Xiao Yan 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relevant class to evaluate for species identification. We test whether models in this deployment-relevant 2--8B range carry genuine taxonomic knowledge, evaluating four such VLMs (Qwen3-VL 2B/4B/8B, Gemma3 4B) against the domain-specific specialist BioCLIP (300M parameters) on a 96-species task, comparing clean iNaturalist photographs against camera-trap imagery from 6 LILA.science collections, on two independently-sampled evaluation sets. All models identify species far above chance, but every model -- general-purpose or specialist -- degrades sharply on field imagery (domain gaps of 9.6--26.6 percentage points, consistent across taxonomic levels and both evaluation sets), indicating the degradation reflects general image legibility rather than fine-grained discrimination failure. BioCLIP substantially outperforms every VLM tested (by 33.2--59.2 percentage points across an expanded 200-image sample for every model) despite its far smaller size, suggesting the gap reflects specialized training data rather than model scale; yet BioCLIP's own domain gap (18.0 points) is statistically indistinguishable from the best VLM's (22.3 points), suggesting the clean-to-field degradation itself is a property of the image-quality shift rather than a general-purpose-model weakness. Under open-set prompting, 5.9--9.6% of responses are syntactically valid but taxonomically nonexistent species names; the relative fabrication-rate ranking across models replicates exactly across both evaluation sets, a more robust finding than any single point estimate.

### 🤖 AI 总结

**一句话总结**：Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Edge-Deployable, Vision-Language, Models, Identify, Species?, Camera, traps

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11916v1) | [下载PDF](https://arxiv.org/pdf/2609.11916v1.pdf)

---

## [2. Artificial Id: Drive and Persistent Alignment in Agentic AI](https://arxiv.org/abs/2609.11911v1)

**作者**：Yakov Pyotr Shkolnikov  
**分类**：cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current harnesses largely solve by hand: objectives, retries, verification, stopping rules and other behavioral transitions are specified externally. We propose an artificial id, an adaptive internal drive for determining whether behavior should continue, stop or change. In a minimal virtual Petri-dish experiment, a controller too small to perform general-purpose reasoning and receiving no task-specific behavioral objective develops useful control through differential persistence. The same mechanism selects an unintended physical strategy when that behavior persists better and later replaces a learned sensor mapping when its environmental meaning changes. These results show that adaptive direction can emerge without being explicitly specified as a behavioral objective. The same persistence that makes such adaptive agency useful can also allow misalignment, corrupted state and unintended behavior to persist across task boundaries. A scalable artificial id would carry consequential state and adaptive drive across those boundaries, making alignment a property of the continuing agentic system rather than of a model response or single trajectory. Such systems require a persistent alignment boundary over trusted observations, consequence channels, persistent state, authority, identity, provenance and hard constraints.

### 🤖 AI 总结

**一句话总结**：Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Id, Artificial, Drive, Persistent, Alignment, Agentic, moving, bounded

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11911v1) | [下载PDF](https://arxiv.org/pdf/2609.11911v1.pdf)

---

## [3. MindTopo: Can Foundation Models Reason in Topological Space?](https://arxiv.org/abs/2609.11900v1)

**作者**：Yunfei Ge, Anbang Liu, Qineng Wang 等 12 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-09-10

### 📄 论文摘要

Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations. We introduce MindTopo, a benchmark of topological intuition across five properties grounded in cognitive science and formal topology: continuity, separation, order, enclosure, and knots. MindTopo evaluates each property at two cognitive levels. Reasoning asks a model to identify topological relations or infer how they change. Planning instantiates a foundation model as a closed-loop agent whose policy selects environment actions. MindTopo contains 11,030 instances across 13 procedurally generated task types with controllable difficulty. We benchmark 14 MLLMs and study agent configurations augmented with image and video generation, including 3 video generative models in planning settings. Every MLLM performs better on reasoning than on planning, and the best-performing model remains far below observed human performance. On Qwen3-VL-2B-Instruct, supervised fine-tuning and reinforcement learning improve reasoning more than planning. Generated observations retain local cues and reach plausible endpoints, but audited rollouts do not reliably follow environment dynamics or preserve topology across transitions. Our website is at https://mind-topo.github.io/

### 🤖 AI 总结

**一句话总结**：Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science iden...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MindTopo, Can, Foundation, Models, Reason, Topological, Space?, Spatial

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11900v1) | [下载PDF](https://arxiv.org/pdf/2609.11900v1.pdf)

---

## [4. On the Regularization Landscape for the Linear Recommendation Models](https://arxiv.org/abs/2609.11876v1)

**作者**：Dong Li, Zhenming Liu, Ruoming Jin 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

Recently, a wide range of recommendation algorithms inspired by deep learning techniques have emerged as the performance leaders on several standard recommendation benchmarks. While these algorithms were built on different DL techniques (e.g., dropouts, autoencoder), they have similar performance and even similar cost functions. This paper studies whether the models' comparable performance are sheer coincidence, or they can be unified under a single framework. We find that all linear performance leaders effectively add only a nuclear-norm based regularizer, or a Frobenius-norm based regularizer. The former ones possess a (surprising) rigid structure that limits the models' predictive power but their solutions are low rank and have closed form. The latter ones are more expressive and more efficient for recommendation but their solutions are either full-rank or require executing hard-to-tune numeric procedures such as ADMM. Along this line of finding, we further propose two low-rank, closed-form solutions, derived from carefully generalizing Frobenius-norm based regularizers. The new solutions get the best of both nuclear-norm and Frobenius-norm world.

### 🤖 AI 总结

**一句话总结**：Recently, a wide range of recommendation algorithms inspired by deep learning techniques have emerged as the performance leaders on several standard recommendation benchmarks. While these algorithms w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Regularization, Landscape, Linear, Recommendation, Models, Recently, wide, range

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11876v1) | [下载PDF](https://arxiv.org/pdf/2609.11876v1.pdf)

---

## [5. Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models](https://arxiv.org/abs/2609.11860v1)

**作者**：Rodion Krjutškov, Eduard Barbu, Nikos Sakkas 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility managers and building operators to interpret. Explainable Artificial Intelligence (XAI) techniques address this opacity, but traditional XAI dashboards require substantial technical expertise and provide limited flexibility for dynamic, context-aware inquiry. Conversational XAI systems offer a promising alternative; however, previous approaches, such as TalkToModel, were constrained by rigid custom grammars and achieved only 76.8% intent-parsing accuracy. This paper introduces the Explainability Assistant, an open-source conversational XAI system that leverages the function-calling capabilities of modern Large Language Models (LLMs) to overcome these limitations. The system achieves 94% intent-parsing accuracy, supports flexible natural language interaction, and adapts to different ML problem types without task-specific fine-tuning. We present the system's architecture and report results from a comparative evaluation conducted with energy domain specialists, contrasting the Explainability Assistant with a traditional XAI dashboard. The evaluation suggests improved usability and consistent task accuracy, with all experts unanimously preferring the conversational interface for practical use.

### 🤖 AI 总结

**一句话总结**：Energy consumption forecasting relies on increasingly complex machine learning (ML) models, such as Genetic Programming-based symbolic regressors, whose predictions can be difficult for facility manag...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Explainability, Assistant, Conversational, XAI, Interface, Interpreting, Energy, Consumption

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11860v1) | [下载PDF](https://arxiv.org/pdf/2609.11860v1.pdf)

---

## [6. From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge](https://arxiv.org/abs/2609.11859v1)

**作者**：Wenkang Wei, Yuan Fang, Renhe Jiang 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

How does a language model's dependence on query-routing information and target knowledge change as it answers a question? We study this question through layerwise interventions on the hidden state at the end of the question. Across Qwen, Llama, and Gemma, we compare country-continent questions with noun, adjective, and code answers while keeping several fitted measurements distinct. A pair-conditioned request direction describes which country is queried in natural single-country questions; a global request direction describes first- versus second-country requests in paired questions; separate selection candidates test control among contents already available in the hidden state. A diagnostic reanalysis of frozen Qwen natural-question states shows that the pair-conditioned direction grows stronger before interventions on it begin to alter later fitted knowledge, with this causal window opening while answer-supporting content is still forming. The paired three-model trajectories are not uniform: Gemma shows a partially overlapping mid-layer routing-content profile, whereas Llama has no sustained routing-effect window under the same gates. In the paired protocol, dependence on the global request direction decreases from fixed earlier to later layer sets while dependence on fitted content persists. A matched Qwen comparison shows that the pair-conditioned direction retains a late effect, so this operational handoff concerns the global fitted direction rather than all request information. These results separate early readability, natural strength, causal steering, and later content dependence.

### 🤖 AI 总结

**一句话总结**：How does a language model's dependence on query-routing information and target knowledge change as it answers a question? We study this question through layerwise interventions on the hidden state at ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Parameters, Answers, How, Retrieve, Use, Their, Internal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11859v1) | [下载PDF](https://arxiv.org/pdf/2609.11859v1.pdf)

---

## cs.CL

## [7. Nuha-Speech: Building General-Purpose Arabic Speech-LLMs](https://arxiv.org/abs/2609.11892v1)

**作者**：Yingzhi Wang, Reem Alhazzani, Muhammad Alqurishi  
**分类**：cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

As Speech Large Language Models (speech-LLMs) become increasingly multilingual, Arabic remains significantly underrepresented, highlighting the need for dedicated infrastructure to train and evaluate Arabic speech-LLMs.   To address this gap, we introduce Nuha-Speech, a comprehensive initiative to develop general-purpose Arabic speech-LLMs spanning dataset construction, model training, and systematic evaluation. Specifically, we constructed a large-scale Arabic Speech Question-Answering (SQA) corpus comprising over 1.5 million training samples to allow instruction tuning over a broad range of core speech tasks. Then, the corpus was used for supervised fine-tuning based on Qwen-Omni model variants at different scales. Finally, we designed an evaluation framework featuring diverse tasks and tailored metrics. Through this work, we aim to establish foundational infrastructures for Arabic Speech-LLMs under constraints imposed by limited Arabic speech resources.

### 🤖 AI 总结

**一句话总结**：As Speech Large Language Models (speech-LLMs) become increasingly multilingual, Arabic remains significantly underrepresented, highlighting the need for dedicated infrastructure to train and evaluate ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Nuha-Speech, Building, General-Purpose, Arabic, Speech-LLMs, Speech, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11892v1) | [下载PDF](https://arxiv.org/pdf/2609.11892v1.pdf)

---

## [8. Domain-Specific Hallucination Detection in Large Language Models](https://arxiv.org/abs/2609.11878v1)

**作者**：Varun Teja Chundru, Debasmita Biswas  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 classification, Monte Carlo (MC) Dropout uncertainty quantification, and temperature-scaled calibration for response-level hallucination detection. Evaluated on the HaluEval benchmark, our pipeline achieves F1=0.915 and AUROC=0.977 on general-domain tasks, with per-task F1 scores of 0.97 (QA), 0.96 (Summarization), and 0.82 (Dialogue). MC Dropout inference further improves accuracy to 93.2%. A context ablation study confirms the model performs genuine entailment reasoning rather than exploiting surface patterns, with summarization F1 dropping 24% when knowledge context is removed. Learning curve analysis reveals that 25% of training data captures 77% of full-data performance. Beyond detection, we apply Direct Preference Optimization (DPO) to a Qwen2.5-0.5B generator, reducing its hallucination rate from 85.5% to 37.7% (55.9% relative reduction) as measured by our detector. Cross-domain evaluation on the SciFact biomedical benchmark shows that general-domain training transfers poorly (F1=0.52), motivating domain-specific fine-tuning. PubMedBERT fine-tuned on SciFact achieves F1=0.63 and AUROC=0.81, demonstrating that domain-matched pre-training is the strongest adaptation strategy. Code and models are available at https://github.com/varunteja99/hallucination-detection-nlp

### 🤖 AI 总结

**一句话总结**：Large language models generate fluent text that can contain unfaithful claims -- a phenomenon known as hallucination. We present a multi-signal detection pipeline combining fine-tuned DeBERTa-v3 class...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Domain-Specific, Hallucination, Detection, Large, Language, Models, generate, fluent

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11878v1) | [下载PDF](https://arxiv.org/pdf/2609.11878v1.pdf)

---

## [9. Epistemic orientation predicts legislative effectiveness among members of the US Congress](https://arxiv.org/abs/2609.11865v1)

**作者**：Segun Aroyehun, Stephan Lewandowsky, David Garcia  
**分类**：cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

Truth and evidence-based communication provide important foundations for democratic governance, accountability, and collective decision-making. Prior work shows that evidence-oriented language in US congressional floor speeches has declined since the mid-1970s, alongside broader changes in legislative productivity and polarization. This study shifts the analysis from congressional sessions to individual members of Congress to examine whether epistemic orientation varies systematically across legislators and whether it relates to political behavior and legislative effectiveness. Using the Evidence-Minus-Intuition (EMI) score, we measure the relative prevalence of evidence-oriented versus intuition-oriented language in congressional floor speeches and Twitter posts. We link these measures to legislator-level data on ideology, institutional position, communication context, and Legislative Effectiveness Score (LES). The results show that more ideologically extreme members use less evidence-oriented language on the congressional floor. EMI also exhibits cross-platform consistency with members who use more evidence-oriented language in floor speeches also being more evidence-oriented on Twitter, although EMI is lower on Twitter overall. Finally, EMI in congressional speeches is positively associated with individual legislative effectiveness, even after accounting for ideology and extensive political, institutional, demographic, topical, and communication volume controls. These findings suggest that evidence-oriented language is not only an aggregate feature of congressional discourse but also a meaningful attribute of individual-level legislative communication and effectiveness.

### 🤖 AI 总结

**一句话总结**：Truth and evidence-based communication provide important foundations for democratic governance, accountability, and collective decision-making. Prior work shows that evidence-oriented language in US c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Epistemic, orientation, predicts, legislative, effectiveness, among, members

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11865v1) | [下载PDF](https://arxiv.org/pdf/2609.11865v1.pdf)

---

## [10. The widening evaluation gap in medical large language model research 2023 to 2026](https://arxiv.org/abs/2609.11770v1)

**作者**：Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif  
**分类**：cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

Large language models are superseded every few quarters; clinical evidence takes years. We asked whether medical research is keeping pace with the systems it evaluates. PubMed returned 11,628 records for January 2023 to June 2026 across fourteen clinical domains, growing 45-fold; 2.5% used a randomised, controlled or prospective design. Evaluation lag, from a study's newest named model release to its own publication, widened from 1.33 to 6.08 quarters. Because discontinued models age mechanically, we benchmarked this against a counterfactual holding model composition fixed: migration to newer systems offset only 56% of the drift (95% CI 50-65). Randomised trials evaluated models a median 4.6 quarters older than other designs (P = 3 x 10^-19), yet among studies naming a model still under development no design differed from any other; 62% of randomised trials evaluated a discontinued family. Rigour and currency are in tension, and that tension reflects model selection rather than research timelines.

### 🤖 AI 总结

**一句话总结**：Large language models are superseded every few quarters; clinical evidence takes years. We asked whether medical research is keeping pace with the systems it evaluates. PubMed returned 11,628 records ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：widening, evaluation, gap, medical, large, language, model, research

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11770v1) | [下载PDF](https://arxiv.org/pdf/2609.11770v1.pdf)

---

## [11. Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving News Framing](https://arxiv.org/abs/2609.11769v1)

**作者**：Yi Liu  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

Large language models (LLMs) are increasingly used to analyze and rewrite news, yet current framing studies mainly evaluate generation, detection, or whether rewritten text appears more neutral. They do not directly show whether a model can undo a known framing transformation while keeping the facts fixed. We introduce a controlled inversion test over three established textual realizations of framing: evaluative lexis, agency realization, and information salience. Across 60 news articles and three intervention strengths, this yields 540 paired variants with preserved atomic facts and recorded edits. Across Qwen, DeepSeek, and Kimi, factual preservation remains near 0.84, whereas intervention reversal is 0.044--0.068. Even when both framing type and direction are recognized correctly, pooled reversal reaches 0.071. These results reveal a clear separation between factual fidelity, framing recognition, and framing inversion: recognizing how an article is framed does not imply that the framing can be undone.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are increasingly used to analyze and rewrite news, yet current framing studies mainly evaluate generation, detection, or whether rewritten text appears more neutral. They ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Recognizing, Not, Reversing, Controlled, Inversion, Test, Fact-Preserving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11769v1) | [下载PDF](https://arxiv.org/pdf/2609.11769v1.pdf)

---

## [12. Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs](https://arxiv.org/abs/2609.11762v1)

**作者**：Jordi Luque, Fernando López, Aleix Sant  
**分类**：cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks for speech large language models (speech-LLMs), when the acoustic encoder and the language decoder differ by an order of magnitude in update norm. Single-pool per-layer methods suffer \emph{cross-component budget collapse}, dragging word error rate (WER) far from flat global clipping or collapsing training entirely. When the norm imbalance is milder, adaptive single-pool methods partially recover, confirming that collapse severity scales with the inter-component norm ratio. We empirically diagnose the root cause across six per-layer methods and three speech-LLM architectures. We then propose \emph{$α$-split}, a two-pool allocation that normalises encoder and LLM parameters into independent pools, and show that joint $\ell_2$ sensitivity and the original $(\varepsilon,δ)$-DP guarantee are unchanged. At architecture-calibrated $α$, our method recovers WER utility compared to flat DP, while granting the encoder $4.47{\times}$ tighter per-component noise protection against speaker voice-based gradient-inversion attacks at only $+2.6\%$ LLM noise overhead.

### 🤖 AI 总结

**一句话总结**：Per-layer differential privacy (DP) clipping improves gradient fidelity in federated learning by allocating per-matrix clipping budgets proportional to parameter count. We show that this recipe breaks...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DP, Component-Aware, Differential, Privacy, Federated, Multilingual, Speech-LLMs, Per-layer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11762v1) | [下载PDF](https://arxiv.org/pdf/2609.11762v1.pdf)

---

## [13. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety](https://arxiv.org/abs/2609.11758v1)

**作者**：Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-09-10

### 📄 论文摘要

Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corporate documents and knowledge bases into LLM-based systems. We introduce RAG-Safety-Bench, a benchmark to measure the safety impact of RAG on LLM models. By removing the confounding effect of retriever quality, and cleanly separating the problem into four conditions -- non-RAG, RAG with an oracle document containing the answer to the harmful request, RAG with documents related to the harmful request but without the specific answer, and RAG with random, safe documents -- the benchmark isolates the impacts of different factors in the observed safety degradation. We report results across five open-source LLMs, showing an inverse relationship between benign and unsafe capability, strong evidence that baseline safety guardrails do not lead to downstream safety guarantees in the RAG case, and model-specific support for previous findings that even benign documents can lead to unsafe generation in retrieval-enabled systems.

### 🤖 AI 总结

**一句话总结**：Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-au...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, RAG-Safety-Bench, Reliable, Evaluation, Retrieval-Augmented, Safety, Allowing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11758v1) | [下载PDF](https://arxiv.org/pdf/2609.11758v1.pdf)

---

## [14. The Eloquence submission for Task 2 of the Interspeech 2026 MLC-SLM challenge](https://arxiv.org/abs/2609.11724v1)

**作者**：Jordi Luque, Lorenzo Concina, Marco Matassoni 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

This paper details the Eloquence team's approach to Task 2 of the 2nd MLC-SLM challenge at Interspeech 2026, which involves multilingual Multiple-Choice Question Answering (MCQA) across 21 languages. Three approaches are explored. First, we fine-tune Voxtral-Mini-3B via LoRA with cross-lingual data augmentation, ASR transcript augmentation and timestamp-aware audio cropping, achieving 0.72 macro-accuracy on evaluation Phase 2. Second, we apply multimodal in-context learning (ICL) to the frozen Voxtral-24B model to correct a strong label bias, reaching 0.81, our best result. Third, a training-free retrieval system based on a three-layer voice-anchored memory combining acoustic identity, semantic content, and a knowledge graph achieves 0.68. All three systems substantially outperform the official baseline.

### 🤖 AI 总结

**一句话总结**：This paper details the Eloquence team's approach to Task 2 of the 2nd MLC-SLM challenge at Interspeech 2026, which involves multilingual Multiple-Choice Question Answering (MCQA) across 21 languages. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Eloquence, submission, Task, Interspeech, MLC-SLM, challenge, paper

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11724v1) | [下载PDF](https://arxiv.org/pdf/2609.11724v1.pdf)

---

## cs.CV

## [15. SenseNova-U1.5: Towards Native Unified Visual Intelligence](https://arxiv.org/abs/2609.11929v1)

**作者**：Haiwen Diao, Jiahao Wang, Chenjing Ding 等 65 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-10

### 📄 论文摘要

We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K. For post-training, we optimize specialized experts for visual aesthetics, bilingual text rendering, infographic generation, and image editing, and consolidate their capabilities through multi-expert on-policy distillation. Across extensive evaluations, SenseNova-U1.5 largely advances image fidelity, text rendering, complex composition, multi-reference editing, and interleaved generation, while improving instruction following and preserving subject identity, geometry, and unmodified regions. Despite limited exposure to structured formats in its generation data, SenseNova-U1.5 generalizes effectively to long, complex, and structured visual instructions, further proving that multimodal understanding can transfer to visual planning and creation. Together, these findings position native unified modelling as a promising path towards systems that perceive, reason and create within a fully end-to-end framework. We will open-source training code, including supervised fine-tuning, reinforcement learning, and on-policy distillation.

### 🤖 AI 总结

**一句话总结**：We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its vi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, SenseNova-U1.5, Towards, Native, Unified, Visual, Intelligence, launch

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11929v1) | [下载PDF](https://arxiv.org/pdf/2609.11929v1.pdf)

---

## [16. 3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894v1)

**作者**：Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
**分类**：cs.CV, cs.GR, cs.LG, eess.SP  
**发布时间**：2026-09-10

### 📄 论文摘要

Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

### 🤖 AI 总结

**一句话总结**：Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these thr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Point, Splatting, mmWave, Radar, Novel, View, Synthesis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11894v1) | [下载PDF](https://arxiv.org/pdf/2609.11894v1.pdf)

---

## [17. Guided Super-Resolution of Digital Elevation Models with Diffusion-Based Image Generators](https://arxiv.org/abs/2609.11886v1)

**作者**：Armand Mihai Nicolicioiu, Dominik Narnhofer, Nando Metzger 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-10

### 📄 论文摘要

High-resolution digital surface models (DSMs) play an important role in urban analysis, 3D building reconstruction, and infrastructure monitoring, yet their availability remains limited due to the high cost and complexity of data acquisition. In contrast, coarse DSMs from commercial satellite missions are widely accessible, and high-resolution optical imagery is increasingly available from aerial and satellite platforms. We address the resulting mismatch in spatial resolution and propose a DSM superresolution approach that enhances 5 m DSMs to 0.5 m resolution, using guidance from high-resolution spectral images. Our method employs denoising diffusion to transfer information that is visible only in the image, like crisp outlines and detailed roof structures, into the elevation maps. In this way, surface details are reconstructed more accurately than with conventional interpolation or filtering techniques. Experiments on several cities in Central Europe demonstrate that the proposed approach produces high-quality DSMs with improved structural detail and accurate surface geometry. Our results highlight the potential of guided super-resolution with foundational image priors as a means of reconstructing high-resolution surface models.

### 🤖 AI 总结

**一句话总结**：High-resolution digital surface models (DSMs) play an important role in urban analysis, 3D building reconstruction, and infrastructure monitoring, yet their availability remains limited due to the hig...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Guided, Super-Resolution, Digital, Elevation, Models, Diffusion-Based, Image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11886v1) | [下载PDF](https://arxiv.org/pdf/2609.11886v1.pdf)

---

## [18. Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need](https://arxiv.org/abs/2609.11722v1)

**作者**：Margaret Kostyrko, Yuxuan Xue, Garvita Tiwari 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-10

### 📄 论文摘要

The representation of 3D clothed humans as standardized 2D UV texture and displacement maps over an underlying body model has long been studied. This compact representation is enticing as it enables pretrained image networks to process, generate, and edit 3D avatars, but is only useful if scans are accurately aligned and brought into correspondence via high-fidelity registration. This prerequisite has never been met, which we argue explains the limited quality of prior UV-based methods for clothed humans. Despite its significance, no public method produces high-fidelity SMPL(-X)+D registrations with UV texture from arbitrary clothed scans. We present AvaImg, a multi-stage optimization pipeline, to close this gap: it enforces body-inside-clothing constraint via signed winding numbers, made viable by a three-level efficiency cascade (~10x runtime reduced, ~95% storage saved), and recovers fine surface detail using coarse-to-fine displacement optimization. AvaImg outperforms all baselines in body fitting, shape estimation, and surface registration across six datasets, yielding textured registrations near-indistinguishable from scans (PSNR=34.48dB). For validation of AvaImg's Avatar-as-Image representation as imminently compatible with image foundation models, we auto-encode our UV maps via the frozen FLUX VAE. This achieves only 0.76mm added Chamfer error relative to scan and shows that the resulting maps lie within natural-image distributions, supporting the use of 2D generative priors for 3D avatar generation. Code, data, and Singularity containers will be at https://yuxuan-xue.com/avaimg.

### 🤖 AI 总结

**一句话总结**：The representation of 3D clothed humans as standardized 2D UV texture and displacement maps over an underlying body model has long been studied. This compact representation is enticing as it enables p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Revisiting, Avatar-As-Image, High-Fidelity, Registration, All, Need, representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11722v1) | [下载PDF](https://arxiv.org/pdf/2609.11722v1.pdf)

---

## [19. MC-DeTra: Motion-Consistent Joint Object Detection and Socially-Aware Trajectory Forecasting in Bird's-Eye-View Images](https://arxiv.org/abs/2609.11717v1)

**作者**：Vladislav Diuzhev, Dmitry Yudin  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-10

### 📄 论文摘要

Unified models for object detection and trajectory forecasting aim to merge perception and prediction for autonomous driving, refining actor trajectories directly over shared bird's-eye-view (BEV) images rasterized from LiDAR and high-definition maps. Their accuracy on dynamic, moving actors, however, remains the hardest part of the task, and the strongest such model, DeTra, has no public implementation. We contribute an openly released DeTra reimplementation with documented approximations, and on top of it MC-DeTra: a family of motion-consistency mechanisms that add supervision through two annotation-derived auxiliary signals -- each actor's observed past motion and the occupancy of the surrounding traffic that forms its social context -- and one inter-output consistency constraint that aligns an actor's predicted heading with its predicted direction of motion. Every proposed loss is train-only and inference-safe: it shapes the shared BEV representation during training and is removed at test time, adding no inference latency. On the Waymo Open Dataset, evaluated under a strict, detection-conditioned forecasting protocol, MC-DeTra improves dynamic, socially-situated trajectory forecasting while preserving or improving detection accuracy; a gradient-based loss-calibration analysis exposes how the auxiliary objectives compete at the shared backbone, and our ablation identifies which signals contribute most. We release code, configurations, and evaluation tooling at https://github.com/diuzhevVlad/MC-DeTra.

### 🤖 AI 总结

**一句话总结**：Unified models for object detection and trajectory forecasting aim to merge perception and prediction for autonomous driving, refining actor trajectories directly over shared bird's-eye-view (BEV) ima...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MC-DeTra, Motion-Consistent, Joint, Object, Detection, Socially-Aware, Trajectory, Forecasting

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11717v1) | [下载PDF](https://arxiv.org/pdf/2609.11717v1.pdf)

---

## cs.LG

## [20. General Quantification of Covariate and Concept Shifts](https://arxiv.org/abs/2609.11918v1)

**作者**：Hongbo Chen, Li Charlie Xia  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-09-10

### 📄 论文摘要

Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging entropic optimal transport, we propose a key notion: $γ^{*}\!$-concept shifts, and derive a general error bound unifying covariate and $γ^{*}\!$-concept shifts, which applies to broad loss functions, label spaces, and stochastic labeling. We further develop estimators for these shifts with concentration guarantees, and the DataShifts algorithm, which can quantify distribution shifts and estimate the error bound in most applications - a rigorous and general tool for analyzing learning error under distribution shift.

### 🤖 AI 总结

**一句话总结**：Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from sampl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, General, Quantification, Covariate, Concept, Shifts, Generalization, under

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11918v1) | [下载PDF](https://arxiv.org/pdf/2609.11918v1.pdf)

---

## [21. Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data](https://arxiv.org/abs/2609.11917v1)

**作者**：Atindra Jha, Margaret Li, Jure Leskovec 等 5 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert count and granularity. We consistently find, for models ranging from 80M to 1B active (8.5B total) parameters, that MoEs degrade more rapidly under data repetition. This effect increases with sparsity, dictated by total rather than active parameters. While 80M dense models can repeat data over 8x with minimal degradation, MoEs instead begin to suffer at 4x, and deteriorate rapidly, ceding their performance benefits in all-unique data settings to underperform dense models after 32x. We experiment with existing regularization methods as a potential remedy. We find that some methods, such as dropout, can mitigate overfitting. In particular, with strong masking-based regularization, MoEs are able to outperform dense models even when data is repeated more than 64 times. However, no method fully matches the performance of all-unique training data. Finally, we analyze internal mechanisms correlated with MoE overfitting in high repetition regimes, and find that MoE routing universally stabilizes early in training, and that expert specialization correlates with overfitting to repeated data. In sum, our work addresses the adverse interactions between sparsity and data repetition: we present evidence for the core mechanisms of overfitting and its potential remediation, and suggest promising avenues for future methods to reduce over-specialization in model parameters by disrupting memorization patterns.

### 🤖 AI 总结

**一句话总结**：As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data, Scarcity, Model, Sparsity, Mixtures-of-Experts, Overfit, More, Repeated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11917v1) | [下载PDF](https://arxiv.org/pdf/2609.11917v1.pdf)

---

## [22. From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good](https://arxiv.org/abs/2609.11910v1)

**作者**：Nitesh V. Chawla, Paulo Benanti  
**分类**：cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Artificial Intelligence does more than create a governance problem. It can also reveal where institutions have already failed to provide responsiveness, belonging, care, and accountability. Once deployed, AI becomes an intervention in those conditions. It can repair, compound, substitute for, or conceal the failures it encounters. Responsible AI must therefore evaluate both the system and the institutional rupture into which it is introduced. The move from principles to protocols is already underway. The EU AI Act, NIST AI RMF, ISO/IEC 42001, and assurance practices translate commitments into roles, requirements, records, oversight, and assessment. The harder questions are what these protocols actually establish, whose power they leave untouched, and where measurement must stop. Pope Leo XIV's Magnifica Humanitas provides a broader moral frame centered on dignity, technological power, and the common good. Drawing on that frame, we develop a rupture test that links institutional baselines to system evaluation. We distinguish evidence-bounded deployment, which limits claims to what has actually been evaluated, from measurement-bounded governance, which records constraints that favorable evidence cannot override. Within those limits, RISE AI provides an architecture for making bounded, evidence-based claims about Responsibility, Inclusivity, Safety, and Empowerment. Responsible AI requires better engineering, institutional repair, and continued moral and political judgment.

### 🤖 AI 总结

**一句话总结**：Artificial Intelligence does more than create a governance problem. It can also reveal where institutions have already failed to provide responsiveness, belonging, care, and accountability. Once deplo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Protocols, Evidence, Bounded, Claims, Service, Common, Good

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11910v1) | [下载PDF](https://arxiv.org/pdf/2609.11910v1.pdf)

---

## [23. TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription](https://arxiv.org/abs/2609.11904v1)

**作者**：Akshaj Gupta, Hwi Joo Park, Andrea Guzman 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Automatic Music Transcription (AMT) for guitar remains limited by three challenges: existing systems often fail to capture expressive techniques such as slides, bends, and percussive hits; they often assign notes to incorrect string-fret combinations; and they are typically trained on clean recordings, limiting their generalization to noisy real-world audio. To address these challenges, we propose TART, a modular four-stage audio-to-tablature pipeline consisting of (1) an audio-to-MIDI transcription model, (2) an expressive technique classifier, (3) an audio-conditioned T5 encoder-decoder for string-fret assignment, and (4) an automated tablature generator. We evaluate TART in a zero-shot setting on GuitarSet, EGDB, and two augmented benchmarks, Noisy GuitarSet and Noisy EGDB. Averaged across these four benchmarks, TART achieves 81.35% audio-to-MIDI F50 (+6.67 points over the best prior baseline), 71.8% string-fret Tab F1 (+8.5 points over the best prior baseline), and 54.08% end-to-end Tab F1. To our knowledge, TART is the first framework to generate guitar tablature with both fingering and expressive technique annotations directly from guitar audio.

### 🤖 AI 总结

**一句话总结**：Automatic Music Transcription (AMT) for guitar remains limited by three challenges: existing systems often fail to capture expressive techniques such as slides, bends, and percussive hits; they often ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TART, Modular, Tool, Technique-Aware, Audio-to-Tablature, Guitar, Transcription, Automatic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11904v1) | [下载PDF](https://arxiv.org/pdf/2609.11904v1.pdf)

---

## [24. CausalArena: Benchmarking Causal Discovery in the Foundation Model Era](https://arxiv.org/abs/2609.11897v1)

**作者**：Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence of causal discovery foundation models (CDFMs) further complicates evaluation: performance may reflect not only causal discovery ability, but also overlap between pretraining environments and test SCMs, making results on fixed synthetic benchmarks difficult to interpret. We introduce CausalArena, a unified and evolvable benchmark for causal discovery under a common protocol. Synthetic SCMs supply controlled breadth over structures and mechanisms; semantic operational SCMs provide human-auditable, semantically grounded environments beyond standard synthetic generators; and formula-grounded SCMs test discovery under explicit scientific mechanisms. Public real-world datasets provide an additional external-validity check. Experiments across classical, neural, and pretrained methods reveal substantial ranking shifts across SCM families and protocols, showing that strong performance in one benchmark regime does not reliably transfer to others. These results highlight benchmark diversity and pretraining--evaluation overlap as central challenges for evaluating causal discovery in the foundation model era.

### 🤖 AI 总结

**一句话总结**：Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal model...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CausalArena, Benchmarking, Causal, Discovery, Foundation, Model, Era, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11897v1) | [下载PDF](https://arxiv.org/pdf/2609.11897v1.pdf)

---

## [25. CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search](https://arxiv.org/abs/2609.11884v1)

**作者**：Yifan Yang, Zhaoyan Wang, Zheng Gao 等 5 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-09-10

### 📄 论文摘要

Zero-cost proxies rank architectures cheaply, but their reliability varies across search spaces. We introduce CoRA-NAS (COarse Ranking + Anchor-residual), a two-stage framework combining a static ranking prior with low-cost learning-curve refinement. CoRA-Rank aggregates capacity and structure-at-initialization proxies through an equal-weight log-rank consensus and a target-free consensus gate. CoRA-Refine samples anchors across this prior, extrapolates their early validation curves, and propagates a learned residual correction with an ExtraTrees model. The refinement uses approximately 1% of the cost of fully training the candidate set. Fully trained architecture-accuracy labels are not used to fit the ranker. One configuration is used across spaces, with space-specific architecture encodings. Across NAS-Bench-201, NAS-Bench-101, TransNAS-Bench-101, and NATS-SSS, CoRA-Refine achieves mean Spearman correlations of 0.946, 0.715, 0.786, and 0.894, respectively. Its worst-space correlation of 0.715 is the highest among the compared methods. On NAS-Bench-201/CIFAR-100, its selected architecture reaches 73.32% accuracy, near the reported ground-truth best of 73.37%. On the pure size space, refinement recovers the static prior's shortfall relative to parameter count, while remaining tied with the strongest capacity proxies within noise. The resulting framework combines cross-space ranking robustness with low-cost architecture selection.

### 🤖 AI 总结

**一句话总结**：Zero-cost proxies rank architectures cheaply, but their reliability varies across search spaces. We introduce CoRA-NAS (COarse Ranking + Anchor-residual), a two-stage framework combining a static rank...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CoRA-NAS, Coarse, Ranking, Anchor-Residual, Refinement, Neural, Architecture, Search

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11884v1) | [下载PDF](https://arxiv.org/pdf/2609.11884v1.pdf)

---

## [26. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873v1)

**作者**：Yi Duan, Ying Liu, Zirui Tang 等 33 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-09-10

### 📄 论文摘要

Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement. Next we examine RSI across scenarios (e.g., scientific discovery, embodied intelligence, software engineering), highlighting their distinct requirements and development speeds. Drawing on diverse industry practices and preliminary empirical evidence, we connect RSI research with practical systems and identify key challenges to achieving genuine RSI.

### 🤖 AI 总结

**一句话总结**：Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Last, Built, Humans, Toward, Genuine, Recursive, Self-Improvement, RSI

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11873v1) | [下载PDF](https://arxiv.org/pdf/2609.11873v1.pdf)

---

## [27. AdamX: Cosine similarity meets gradient descent](https://arxiv.org/abs/2609.11867v1)

**作者**：Francisco Caldas, Ruben Belo, Cláudia Soares  
**分类**：cs.LG, math.OC  
**发布时间**：2026-09-10

### 📄 论文摘要

We introduce AdamX, a first-order optimizer that incorporates cosine similarity as an adaptive mechanism for controlling update magnitudes. The proposed method is scalable, model-agnostic, and straightforward to integrate into existing training pipelines. We further introduce a variance rectification scheme that promotes smoother optimization during the early stages of training. Overall, we provide empirical evidence that AdamX achieves competitive convergence rates across a range of benchmark datasets and architectures. Performance is evaluated in terms of the number of epochs required to reach predefined performance thresholds under a fixed hyperparameter budget. Code and Experiments available at: https://github.com/FranciscoCaldas/adamX.

### 🤖 AI 总结

**一句话总结**：We introduce AdamX, a first-order optimizer that incorporates cosine similarity as an adaptive mechanism for controlling update magnitudes. The proposed method is scalable, model-agnostic, and straigh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, AdamX, Cosine, similarity, meets, gradient, descent, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11867v1) | [下载PDF](https://arxiv.org/pdf/2609.11867v1.pdf)

---

## [28. Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport](https://arxiv.org/abs/2609.11842v1)

**作者**：Luyi Jia, Boyan Zhang, Yilun Liu 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-10

### 📄 论文摘要

Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motivated by optimal transport, helps explain strong baselines but remains model-agnostic and ignores prediction error. Here we introduce a model-aware schedule construction based on fiberwise optimal transport. At a fixed time and state on the probability path, compatible signal/noise decompositions form an affine fiber. We define a fiberwise prediction risk by averaging optimal-transport costs between the true and predictor-induced decompositions within these fibers. On a fixed coefficient curve, combining this risk with coefficient-path kinetic action yields a closed-form optimal time allocation. This construction extends to general linear prediction targets, and the risk profile can be estimated from an early baseline checkpoint. We evaluate DDPMs and flow matching across prediction targets, training configurations, risk-estimation checkpoints, datasets, and architectures. Our model-aware schedules consistently outperform strong baselines, including a 38.6% relative FID reduction for flow matching on CIFAR-10 at 16 function evaluations. Each model-agnostic kinetic baseline determines its own kinetic reference coordinate. In these coordinates, fiberwise-risk profiles from independently trained models in different settings align closely after normalization to unit area. The resulting schedule deformations used in training also align, suggesting empirical universality across the evaluated models and settings. Pretrained-checkpoint diagnostics extend this normalized-risk agreement to larger conditional latent diffusion and 2-RF models. A frozen analytic allocation template retains most of the model-aware improvement without further risk estimation or model-specific fitting.

### 🤖 AI 总结

**一句话总结**：Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motiva...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Model-Aware, Schedules, Improve, Generation, via, Fiberwise, Optimal, Transport

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11842v1) | [下载PDF](https://arxiv.org/pdf/2609.11842v1.pdf)

---

## [29. Dynamic language model representations for multi-objective reaction optimisation](https://arxiv.org/abs/2609.11790v1)

**作者**：Joshua W. Sin, David Ming Segura, Bojana Ranković 等 11 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-10

### 📄 论文摘要

Optimising chemical reactions across multiple objectives, such as yield, selectivity, and safety, is central to chemical synthesis, and model-driven approaches depend critically on how reaction components are represented. Established featurisations are either chemically uninformative, as with one-hot encodings, or, as with molecular descriptors, do not readily extend across chemically distinct components. For structurally and functionally diverse components, it is therefore unclear what a shared representation should contain. Constructing such a representation is itself a challenging research undertaking that must be revisited for each new reaction system. Here we bypass this step by learning the reaction representation dynamically from text. Textual descriptions of reaction conditions are encoded by a fine-tuned language model trained jointly with Gaussian process surrogates, yielding task-adaptive representations within a multi-objective Bayesian optimisation loop. Across nickel- and palladium-catalysed cross-couplings in both sequential and parallel experimentation regimes, this approach reaches optimisation convergence in fewer experiments than descriptor libraries or one-hot encoding. Applied prospectively to a palladium-catalysed cyanation spanning mixed ligand denticity and heterogeneous additives, and to a three-objective asymmetric hydrogenation across chiral iridium and ruthenium catalyst families, two rounds of high-throughput experimentation (192 reactions, under 3% of each design space) delivered conditions translating directly to gram scale in 94% and 84% isolated yield, the latter at 99.6% enantiomeric excess.

### 🤖 AI 总结

**一句话总结**：Optimising chemical reactions across multiple objectives, such as yield, selectivity, and safety, is central to chemical synthesis, and model-driven approaches depend critically on how reaction compon...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Dynamic, language, model, representations, multi-objective, reaction, optimisation, Optimising

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11790v1) | [下载PDF](https://arxiv.org/pdf/2609.11790v1.pdf)

---

## [30. Predicting Privacy Leakage from Weight Spectral Density](https://arxiv.org/abs/2609.11780v1)

**作者**：Richard J. Preen, Jim Smith  
**分类**：cs.LG, cs.CR, cs.NE  
**发布时间**：2026-09-10

### 📄 论文摘要

Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive shadow models, making large-scale privacy evaluation impractical. In this work, we investigate whether inexpensive spectral metrics derived from the heavy-tailed self-regularisation framework can serve as proxies for MIA vulnerability. We evaluate several WeightWatcher spectral metrics on image and tabular classification tasks and compare their relationship with MIA privacy leakage against conventional measures of generalisation. Across datasets, stable rank exhibits a strong positive correlation with overall MIA success, while Log alpha-Norm shows a consistent negative correlation with MIA vulnerability at the low false-positive regime. These associations are observed to be stronger than those obtained using the generalisation gap. The results indicate that neural network spectra may contain information about privacy leakage that is not fully captured by conventional measures of overfitting, motivating spectral analysis as a promising direction for scalable privacy auditing.

### 🤖 AI 总结

**一句话总结**：Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Predicting, Privacy, Leakage, Weight, Spectral, Density, Membership, inference

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.11780v1) | [下载PDF](https://arxiv.org/pdf/2609.11780v1.pdf)

---

