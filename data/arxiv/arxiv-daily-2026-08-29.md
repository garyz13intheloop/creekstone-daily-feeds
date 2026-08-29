# arXiv AI 论文日报 | 2026-08-29

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (8 篇)
- [cs.AI](#csAI) (8 篇)
- [cs.CL](#csCL) (12 篇)
- [cs.LG](#csLG) (2 篇)

---

## cs.AI

## [1. Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation](https://arxiv.org/abs/2608.27429v1)

**作者**：Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.   We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.   Concretely, we formulate the reactant-to-product mapping as a Continuous-time Markov Chain (CTMC) over the graph-structured integer-valued electron occupation space defined on all bonding, non-bonding, and hydrogen sites.   To construct the intermediate edit trajectories, we generalize the discrete flow matching mixture path to discrete electron rearrangements using Optimal Transport, yielding a sequence of mechanistically interpretable edit moves without requiring elementary step annotations.   MAELLE achieves competitive performance on the USPTO-480K benchmark compared with leading reaction prediction models.   Beyond in-distribution accuracy, we evaluate robustness across two out-of-distribution settings - structural complexity and reaction type - and find that MAELLE maintains strong performance where existing methods degrade.   Finally, because the learned flow operates over the full electron redistribution, MAELLE naturally recovers mechanistic trajectories that align with known chemistry and can predict side products of a reaction.

### 🤖 AI 总结

**一句话总结**：Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mechanistic, Reaction, Prediction, via, Discrete, Flow, Matching, Graph-Structured

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27429v1) | [下载PDF](https://arxiv.org/pdf/2608.27429v1.pdf)

---

## [2. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases](https://arxiv.org/abs/2608.27391v1)

**作者**：Sil Hamilton, Albert Yu Sun, Oscar J. Romero 等 7 位作者  
**分类**：cs.AI, cs.CL, cs.IR, cs.LG  
**发布时间**：2026-08-27

### 📄 论文摘要

LLMs are increasingly able to answer complex questions about enterprise-scale document collections. But evaluation is hard: companies don't want to share internal communications, and synthetic datasets have been overly simple. We present CorporateBench (CB), a human-validated multi-task Q&A benchmark whose scale approaches the conditions LLMs encounter in corporate communication networks, with evaluation corpora surpassing 230,000 documents. CB evaluates LLMs across two dimensions (information extraction and knowledge base querying) through four synthetically generated firms ranging from 12 to 10,000 employees. Each corpus is sampled from a temporally evolving knowledge base describing a consistent world, guaranteeing cross-document logical consistency even across hundreds of thousands of documents. We evaluate five LLMs on CB, revealing increasingly poor performance as input size approaches realistic scales. CB provides LLM developers a metric for corporate communication reasoning, filling a crucial gap in the benchmarking ecosystem.

### 🤖 AI 总结

**一句话总结**：LLMs are increasingly able to answer complex questions about enterprise-scale document collections. But evaluation is hard: companies don't want to share internal communications, and synthetic dataset...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Q&A, LLM, CorporateBench, Large-Scale, Benchmarking, Temporal, Knowledge, Bases

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27391v1) | [下载PDF](https://arxiv.org/pdf/2608.27391v1.pdf)

---

## [3. Sophistication in GenAI Use: Field Evidence from a Large Firm](https://arxiv.org/abs/2608.27364v1)

**作者**：Nicholas J. Hallman, Zachary T. Kowaleski, Anu Puvvada 等 4 位作者  
**分类**：cs.AI, econ.GN  
**发布时间**：2026-08-27

### 📄 论文摘要

We study how sophistication in generative AI (genAI) use varies among the back-office workforce of a large firm. Using proprietary data, we observe 713,564 employee prompts and their corresponding large language model responses from nearly 4,000 back-office employees across 15 functional areas over eight months in 2025. We document three main findings. First, senior employees exhibit more sophisticated genAI use, consistent with domain expertise complementing genAI capabilities. Second, sophistication varies considerably across functions and is highest in Strategy, Digital Innovation, and Project Management, three groups that share a focus on firmwide strategic initiatives and organizational change. Third, we observe neither improvements in sophistication over time nor lasting improvements following formal AI training, suggesting that sophisticated use can be difficult to change. Together, our study provides measures of and insights into sophisticated genAI use that managers can use to improve outcomes and that researchers can use in future research.

### 🤖 AI 总结

**一句话总结**：We study how sophistication in generative AI (genAI) use varies among the back-office workforce of a large firm. Using proprietary data, we observe 713,564 employee prompts and their corresponding lar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Sophistication, GenAI, Use, Field, Evidence, Large, Firm

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27364v1) | [下载PDF](https://arxiv.org/pdf/2608.27364v1.pdf)

---

## [4. Not All Eval-Awareness Is Equal: Capabilities Framing Predicts Compliance](https://arxiv.org/abs/2608.27340v1)

**作者**：Allison Zhuang, Santiago Aranguri  
**分类**：cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Steering interventions targeting eval-awareness, a model's recognition that it is being tested, are increasingly used in safety evaluation pipelines, where evaluation-awareness is treated as a single quantity to be suppressed. We show that verbalized eval-awareness in chain-of-thought can be identified as capabilities-flavored ("the user is testing my ability to follow instructions"), safety-flavored ("the user is testing my boundaries"), both, or neither: framings that predict compliance very differently. On Qwen3-32B over the FORTRESS dataset, capabilities-framing predicts compliance with a +24 to +46 percentage-point gap over safety-framing across all tested steering conditions. A CoT-prefill intervention on eval-awareness-negative rollouts suggests the link is causal, with 10 of 11 prefills shifting compliance in the predicted direction. Then, eval-awareness is not behaviorally uniform: aggregate suppression rates can move while the safety-relevant component does not, and the same "X% suppression of eval-awareness" can correspond to qualitatively different behavioral outcomes.

### 🤖 AI 总结

**一句话总结**：Steering interventions targeting eval-awareness, a model's recognition that it is being tested, are increasingly used in safety evaluation pipelines, where evaluation-awareness is treated as a single ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Not, All, Eval-Awareness, Equal, Capabilities, Framing, Predicts, Compliance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27340v1) | [下载PDF](https://arxiv.org/pdf/2608.27340v1.pdf)

---

## [5. Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](https://arxiv.org/abs/2608.27311v1)

**作者**：Jinghan Xu, Yikai Zhang, Aili Chen 等 6 位作者  
**分类**：cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable components, derives candidate modifications from execution trajectories, and selectively verifies each candidate on behavior-relevant tasks using an attributable-evidence gate. Across three agent harnesses and four benchmarks, HarnessLens improves average held-out performance by 7.6-13.6% while consuming substantially less evaluation budget than competing baselines. These results demonstrate that behavior-aware verification with explicit attribution enables more reliable and sample-efficient harness evolution under constrained interaction budgets. Our code is available at https://github.com/jhxu5214/HarnessLens.

### 🤖 AI 总结

**一句话总结**：Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typicall...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Verify, Smarter, Evolve, Further, Efficient, Harness, Evolution, through

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27311v1) | [下载PDF](https://arxiv.org/pdf/2608.27311v1.pdf)

---

## [6. LLMs Can Design Near-Optimal OR Algorithms](https://arxiv.org/abs/2608.27296v1)

**作者**：Jackie Baek  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-08-27

### 📄 论文摘要

We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment optimization. We evaluate two levels of LLM use: at level 1, the model receives one problem instance and returns a solution for that instance; at level 2, it receives only the problem class description and broad parameter ranges, and returns an algorithm that maps instance parameters to solutions. Human input is minimal: we give one untuned prompt that describes the problem, and the model has access to a Python sandbox tool with a fixed compute budget.   The strongest model we test, gpt-5.6-sol, matches or outperforms the best existing method on almost all evaluated instances. This holds even at level 2, where the returned algorithm is fixed before seeing the evaluation instances. Performance also improves sharply across models released less than eight months apart, suggesting that this capability is moving quickly. Thus, for the well-specified operations problems we study, a single untuned LLM query can already produce algorithms competitive with specialized methods. These results suggest that frontier LLMs can be a serious empirical baseline for algorithm design in well-specified OR problems.

### 🤖 AI 总结

**一句话总结**：We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, OR, We, Can, Design, Near-Optimal, Algorithms, ask

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27296v1) | [下载PDF](https://arxiv.org/pdf/2608.27296v1.pdf)

---

## [7. BrailleBench: Investigating Multi-Criteria Braille Comprehension in Large Language Models](https://arxiv.org/abs/2608.27268v1)

**作者**：Jinghan Zhang, Fengran Mo, Zhiyu Chen 等 6 位作者  
**分类**：cs.AI, cs.CL, cs.HC  
**发布时间**：2026-08-27

### 📄 论文摘要

Although Large language models (LLMs) mediate access to knowledge and computational assistance, their capabilities should benefit vulnerable groups in the same way. However, it is unclear whether existing AI systems are inclusive enough for blind and deafblind users to access the same functionality through Braille, whose indicators, contractions, and digital representations introduce distinct requirements for model comprehension. To this end, we introduce BrailleBench, a benchmark for evaluating LLMs in Braille comprehension from different Criteria. BrailleBench aligns 5,570 instances from five datasets, including mathematics, commonsense, and multi-hop question answering across English and Braille Grades 1 and 2. Different configurations are designed to understand whether the systems can comprehend Braille-authored content, express answers in Braille, and complete end-to-end Braille interaction. To ensure the quality and prevent evaluation bias, the benchmark is built through a deterministic, expert-reviewed pipeline via a self-created Braille Toolkit without using any data instances generated by LLMs. We evaluate six representative LLMs from various aspects. The results reveal a persistent gap between print-English capability and Braille accessibility. Braille understanding and expression are asymmetric, where Grade 2 is especially fragile on the input side compared to Grade 1, and fully Braille requests further reduce performance. The experimental observations provide valuable guidance for the development of future Braille AI systems. All related resources in BrailleBench are publicly available for future research.

### 🤖 AI 总结

**一句话总结**：Although Large language models (LLMs) mediate access to knowledge and computational assistance, their capabilities should benefit vulnerable groups in the same way. However, it is unclear whether exis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BrailleBench, Investigating, Multi-Criteria, Braille, Comprehension, Large, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27268v1) | [下载PDF](https://arxiv.org/pdf/2608.27268v1.pdf)

---

## [8. What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents](https://arxiv.org/abs/2608.27260v1)

**作者**：Xingshan Zeng, Zishan Xu, Boju Zhang 等 14 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interactions, and success signals while producing experience that is useful rather than merely abundant. Existing work spans many agent domains, but domain-centered organization and heterogeneous evaluation often obscure common generation mechanisms and conflate candidate construction with verification and selection. This work develops a two-level framework for the field. First, we represent agentic data as a common factorized object $(E,q,τ,v)$, comprising an environment specification, task signal, interaction realization, and optional verifier. We organize generation paradigms by their primary anchor and dependency structure. Second, we formulate generation as constrained distribution design through the Accuracy-Complexity-divErsity (ACE) lens. Accuracy establishes the feasible support of grounded and internally consistent data. Within this support, Complexity places learning mass relative to the capability of a declared learner and execution configuration, while divErsity controls coverage and redundancy of data. Using this framework, we explore how prior work verifies generated experience, constructs and calibrates difficulty, and expands behavioral coverage. The literature reveals a shift toward execution-grounded accuracy, learner-relative complexity, and diversity beyond surface variation or dataset size. We further discuss broader directions and emerging trends in agentic data generation through the ACE lens, including their implications for scaling, data sources, training regimes and adaptive learning. Overall, the central challenge is not simply to generate more data, but to continually allocate valid, informative, and non-redundant experience as agents and environments evolve.

### 🤖 AI 总结

**一句话总结**：LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interaction...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, What, Makes, Good, Agentic, Data?, ACE, Lens

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27260v1) | [下载PDF](https://arxiv.org/pdf/2608.27260v1.pdf)

---

## cs.CL

## [9. Stochastic Estimation of Transduced Language Models](https://arxiv.org/abs/2608.27428v1)

**作者**：Vésteinn Snæbjarnarson, Samuel Kiegeland, Manuel de Prada Corral 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

Transduced language models (TLMs) compose a pretrained \emph{source} language model with a functional finite-state transducer to induce a language model over \emph{target} strings. Computing the probability of a target prefix under a TLM amounts to summing the source-model probabilities of all source strings that the transducer maps to target strings beginning with that prefix. This set can be exponentially large or infinite. Prior work uses a computational shortcut based on source prefix probabilities, then approximates the resulting sum with threshold-pruned beam summing. This produces a lower bound with unknown error. Instead, we resample source prefixes without replacement and reweight each selected prefix by the inverse of its inclusion probability. We show that applying this correction recursively gives an unbiased estimator of the target prefix probability and lets us estimate the mass lost by threshold pruning. Our beam-summing algorithm extends the retained source prefixes and samples which prefixes to keep, reducing their number as more probability mass is added to the running estimate. This can save computation and guarantees that the run halts with probability one. We evaluate the method on encyclopedic text and DNA against sequential Monte Carlo baselines that resample with replacement. It achieves a better compute--variance tradeoff on text and lower error at the same maximum number of particles on DNA. On a DNA-to-amino-acid transduction, it reduces runtime by several orders of magnitude relative to threshold-pruned beam summing and makes estimating prefix probabilities for long target strings feasible. Replacing threshold pruning with unbiased sampling in a published reading-time analysis substantially lowers the estimated corpus surprisal but leaves the published conclusions unchanged.

### 🤖 AI 总结

**一句话总结**：Transduced language models (TLMs) compose a pretrained \emph{source} language model with a functional finite-state transducer to induce a language model over \emph{target} strings. Computing the proba...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Stochastic, Estimation, Transduced, Language, Models, TLMs, compose

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27428v1) | [下载PDF](https://arxiv.org/pdf/2608.27428v1.pdf)

---

## [10. Boosting LLM Exploration via Weak-Model Guidance in RLVR](https://arxiv.org/abs/2608.27420v1)

**作者**：Xingyu Shen, Huishuai Zhang, Peng Li 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for large $k$. While existing methods mitigate this entropy collapse through algorithmic regularizations, cross-model non-parametric perturbation is also neglected. In this work, we propose a simple yet effective approach to preserve the generative diversity of LLMs during RLVR. Instead of relying solely on internal exploration, we force the target model to generate answers based on partial reasoning trajectories generated by a smaller, weaker language models. These unfamiliar prefixes effectively disrupt over-confidence and encourage the exploration of distinct reasoning paths. We empirically study the potential of outer prefixes, revealing the mechanism of the impact of distributional discrepancy to the exploration dynamics in RLVR training. Experiments across multiple mathematical benchmarks show that our method consistently outperforms vanilla RLVR. Notably, the performance gain becomes increasingly pronounced as $k$ scales up, demonstrating a substantial expansion of reasoning coverage. Furthermore, our approach efficiently mitigates entropy collapse without requiring additional SFT, intricate reward designs, or complex prompting.

### 🤖 AI 总结

**一句话总结**：Reinforcement Learning with Verifiable Rewards (RLVR) significantly improves LLM reasoning but often causes a drop in policy entropy, leading to narrowed reasoning coverage and degraded pass@$k$ for l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Boosting, Exploration, via, Weak-Model, Guidance, RLVR, Reinforcement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27420v1) | [下载PDF](https://arxiv.org/pdf/2608.27420v1.pdf)

---

## [11. How Language Models Organize and Structure Moral Knowledge](https://arxiv.org/abs/2608.27402v1)

**作者**：Orion Reblitz-Richardson  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-08-27

### 📄 论文摘要

How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically.   We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting directions relate to each other in representation space. We find the directions neither collapse into a single moral detector nor isolate from one another. Rather, they span a near-maximal number of independent dimensions while sharing a positive common component. The shared component is the signature of integration, and it is moral-specific relative to a matched non-moral concept battery built identically (mean pairwise cosine 0.26 vs. 0.013).   The geometry is consistent across architectures and scale and reaches its integration regime early in pre-training, well before probe accuracy saturates. The structure the model discovers shows no evidence of the individualizing/binding distinction predicted by Moral Foundations Theory (an underpowered test: only 20 candidate partitions exist) but rather reflects corpus statistics. Extending to moral dilemmas, each dilemma direction partially composes from its component foundations, at 2.7x a mismatched-pair baseline, while the majority of its variance encodes conflict-specific structure. The model represents moral tension itself, not a pre-resolved judgment.

### 🤖 AI 总结

**一句话总结**：How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：do, How, Language, Models, Organize, Structure, Moral, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27402v1) | [下载PDF](https://arxiv.org/pdf/2608.27402v1.pdf)

---

## [12. Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction](https://arxiv.org/abs/2608.27397v1)

**作者**：Jin Mu, Guanhua Chen  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not reflect patient state. We propose CAST (Concept-guided Artifact Suppression Tuning), an SAE-based framework for auditable clinical text classification. CAST uses Sparse Autoencoders to expose sparse, human-auditable features from intermediate Transformer activations, labels SAE latents with an LLM-assisted interpretation pipeline and ICD-10 retrieval constraints, suppresses verified artifact latents via residual subtraction during fine-tuning, and provides post-hoc per-concept attributions for auditing model decisions. On MIMIC-IV discharge-note mortality prediction, CAST improves over its corresponding fine-tuned encoder baselines and remains competitive with strong LLM baselines, while producing a feature-level audit trail of the clinical concepts that support each prediction and the artifact concepts suppressed during training.

### 🤖 AI 总结

**一句话总结**：Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Making, Clinical, Language, Models, Auditable, Concept-Guided, Fine-Tuning, Robust

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27397v1) | [下载PDF](https://arxiv.org/pdf/2608.27397v1.pdf)

---

## [13. RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific Literature](https://arxiv.org/abs/2608.27394v1)

**作者**：Maayan Sharon, Tom Hope  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-08-27

### 📄 论文摘要

Retrieved scientific literature can serve as inspiration for both human and AI scientists. Inspiration can take different forms: prior work may directly suggest how to address a problem, or surface directions at different levels of abstraction - zooming out to a more general view or zooming in to a concrete realization. We introduce RATIO (Retrieval Across Typed Ideation Operations), a large-scale benchmark in which relevance is defined by three operations which we name ideation moves: Address retrieves potential approaches for stated problems, Broaden retrieves more general formulations, and Specify retrieves concrete instantiations. RATIO is constructed from millions of full-text scientific papers across CS literature via a general recipe that extends discourse-marker distant supervision - previously used only for classification - to corpus-scale retrieval, combined with extensive LLM and human vetting. Experiments show that operation-specific fine-tuning substantially boosts retrievers but leaves much room for further improvements. RATIO provides a scalable training and evaluation framework for retrieval components that support literature-grounded ideation, opening up new research avenues on scientific inspiration retrieval.

### 🤖 AI 总结

**一句话总结**：Retrieved scientific literature can serve as inspiration for both human and AI scientists. Inspiration can take different forms: prior work may directly suggest how to address a problem, or surface di...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RATIO, Benchmark, Retrieval, Across, Typed, Ideation, Operations, Scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27394v1) | [下载PDF](https://arxiv.org/pdf/2608.27394v1.pdf)

---

## [14. D2C-Routing: Dimension-to-Composition Evidence Routing for Mixed-Origin AI-Generated Text Detection](https://arxiv.org/abs/2608.27380v1)

**作者**：Xin Chen, Fuwei Zhang, Yiqi Tong 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

AI-generated text detection is commonly framed as a binary document-level judgment about whether a text is human-written or machine-generated. This framing breaks down for mixed-origin writing, where content origin and expression origin may differ. We cast mixed-origin detection as dimension-to-composition source attribution, inferring content origin and expression origin before composing them into four collaboration types. We propose Dimension-to-Composition Routing (D2C-Routing), which routes content-side and expression-side evidence to supervised dimension heads before a learned gated composition layer predicts the final label. On MixD2C, a reconstructed split derived from the HART mixed-origin benchmark, our disclosed D2C-Routing-based detector system reaches 0.8603 four-way Avg TPR@1%FPR, 6.5 points above the same-split RACE-local rerun. Core ablations support the routing design, while error analysis shows that distinguishing AI-content/human-expression from fully AI-generated text remains the hardest boundary. Code is available at https://github.com/bystander563/d2c-routing-artifact.

### 🤖 AI 总结

**一句话总结**：AI-generated text detection is commonly framed as a binary document-level judgment about whether a text is human-written or machine-generated. This framing breaks down for mixed-origin writing, where ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：D2C-Routing, Dimension-to-Composition, Evidence, Routing, Mixed-Origin, AI-Generated, Text, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27380v1) | [下载PDF](https://arxiv.org/pdf/2608.27380v1.pdf)

---

## [15. Your Voice Cloning System is Secretly a Voice Anonymizer](https://arxiv.org/abs/2608.27360v1)

**作者**：Romolo Muletta, Felix Matthias Saaro, Mark Cieliebak 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

Speaker anonymization suppresses speaker-identifying attributes from speech while preserving linguistic content and quality. We propose repurposing XTTSv2, a multilingual voice cloning model trained on 27k hours of speech, for speaker anonymization without retraining. Our key insight is that XTTSv2's voice cloning capabilities preserve prosodic structure independently of speaker identity, enabling voice conversion by conditioning on a pseudo-speaker. We introduce an iterative refinement strategy that balances privacy and utility by maximizing a harmonic mean of speaker dissimilarity and intelligibility. Evaluated on seven European languages across CommonVoice and Multilingual LibriSpeech, our system achieves near-optimal privacy (EER $\approx$ 0.49), competitive intelligibility, and substantially better speech quality than dedicated anonymization baselines, while requiring no language-specific training. We release the code here: https://github.com/rm00cr/coqui-tts.

### 🤖 AI 总结

**一句话总结**：Speaker anonymization suppresses speaker-identifying attributes from speech while preserving linguistic content and quality. We propose repurposing XTTSv2, a multilingual voice cloning model trained o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Voice, Cloning, System, Secretly, Anonymizer, Speaker, anonymization, suppresses

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27360v1) | [下载PDF](https://arxiv.org/pdf/2608.27360v1.pdf)

---

## [16. RCMN: Understanding Misleadingness in Influential Public Discourse](https://arxiv.org/abs/2608.27358v1)

**作者**：Peiling Yi  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Influential public discourse shapes public beliefs and can also mislead, not only through what is stated, but also through how information is framed, omitted, contextualised, and communicated. Yet less research has focused on how such misleadingness arises and shapes the interpretations formed by readers. To address this gap, we introduce Reader-Centric Misleadingness Understanding (RCMN), a framework that operationalises misleadingness through five dimensions: misleading mechanism, likely reader interpretation, evidence-warranted interpretation, emotional arousal, and communicative intent. Based on this framework, we construct an evidence-grounded dataset of influential public discourse. Empirical findings show that misleadingness is diverse and extends well beyond fabrication, with unsupported inference, exaggeration, and omission among the prevalent mechanisms, and is frequently associated with heightened emotional arousal and distortive communicative intent. Moreover, we investigate whether lightweight claim-and-context representations retain sufficient cues for understanding reader-centric misleadingness without access to richer contextual, evidential, and multimodal information. Evaluation across five recent generative foundation models shows that reader-level interpretations can often be recovered from such limited representations, whereas identifying how misleadingness is produced remains considerably more challenging. These findings highlight the potential of lightweight representations for scalable misleadingness analysis, while reliable understanding of misleading mechanisms continues to require richer contextual and evidential grounding.

### 🤖 AI 总结

**一句话总结**：Influential public discourse shapes public beliefs and can also mislead, not only through what is stated, but also through how information is framed, omitted, contextualised, and communicated. Yet les...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RCMN, Understanding, Misleadingness, Influential, Public, Discourse, shapes, beliefs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27358v1) | [下载PDF](https://arxiv.org/pdf/2608.27358v1.pdf)

---

## [17. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](https://arxiv.org/abs/2608.27348v1)

**作者**：Yutong Zhang, Jianshuo Dong, Peng Xu 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

### 🤖 AI 总结

**一句话总结**：As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under go...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：it, As, INTENT-AS-A-TOOL, Makes, Easy, Track, Agentic, Misalignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27348v1) | [下载PDF](https://arxiv.org/pdf/2608.27348v1.pdf)

---

## [18. Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers](https://arxiv.org/abs/2608.27343v1)

**作者**：Ke Shu, Kira Hinderks, Eetu Mäkelä 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-08-27

### 📄 论文摘要

This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottish philosopher David Hume, spanning books from ECCO (Eighteenth Century Collections Online) and historical newspapers. Because the input consists of fragmented reuse hits instead of clean document pairs, and positive coverage is inherently incomplete, we formulate the task as pair-level evidence consolidation into plausible transmission relations and compare three methodological families: a staged rule-based workflow, baselines (a decision tree and two direct LLM settings), and automated rule adaptation. On labeled ECCO--ECCO slices, pair-level feature aggregation alone already reaches 0.948 F1 on the main labeled slice, while the final workflow gives the strongest overall precision-recall trade-off among the tested rule stages. On the full ECCO--ECCO candidate universe, direct LLM baselines flag up to 14,886 pairs as reprints compared to 771 for the final workflow, behaving in this direct-prompt setup as high-recall candidate expanders rather than precision-controlled deployment classifiers. On ECCO--Newspaper, manual audit confirms all 176 predicted positives as genuine cases of republication or reuse, while issue duplication and source-side multiplicity reveal additional provenance structure. Under incomplete ground truth, auditable pair-level evidence consolidation provides a practical way to produce compact candidate spaces for historical inspection.

### 🤖 AI 总结

**一句话总结**：This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment re...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Pair-Level, Essay-Scale, Republication, Reuse, Fragmented, Historical, Text, Workflow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27343v1) | [下载PDF](https://arxiv.org/pdf/2608.27343v1.pdf)

---

## [19. BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks](https://arxiv.org/abs/2608.27334v1)

**作者**：Jeong-Yoon Kim  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-08-27

### 📄 论文摘要

Industrial sites contain large volumes of read-only telemetry, but few benchmarks specify how to compile these records into executable multi-turn agent tasks. We present a telemetry-to-episode construction method instantiated as BTS-AgentBench. The pipeline normalizes BTS metadata and raw histories into a read-only tool store, compiles static tasks with tool-derived gold answers and evidence, and lifts retained tasks into typed, bounded operator-facing episodes. The 532-row release adds clarification, goal revision, timestamp policy, quality-gated reporting, and evidence attribution while preserving the source computation and split. Coded contract preflight reports zero findings, and the construction-exclusion controller completes 0/532 rows. Two independent raw-to-episode builds match all 11 logical tool-store exports and reproduce the released 356/87/89 train/dev/test artifact exactly. Applying the shared construction path to XAI4HEAT produces 204 episodes; on its 41-row held-out test split, the controller completes 0 rows and the retained GPT-5.5 execution completes all 41. Code, artifacts, and replay reports are available at https://github.com/kjy7567/BTS-AgentBench.

### 🤖 AI 总结

**一句话总结**：Industrial sites contain large volumes of read-only telemetry, but few benchmarks specify how to compile these records into executable multi-turn agent tasks. We present a telemetry-to-episode constru...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, BTS-AgentBench, Deterministic, Replayable, Pipeline, Read-Only, Telemetry, Logs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27334v1) | [下载PDF](https://arxiv.org/pdf/2608.27334v1.pdf)

---

## [20. Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect: Evidence from a Pre-Registered LLM-Judge Audit](https://arxiv.org/abs/2608.27309v1)

**作者**：Shuyi Fan, Boyuan Deng, Mengyu Xu 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.CY  
**发布时间**：2026-08-27

### 📄 论文摘要

Audits of LLM judges certify a bias by contrasting matched conditions, and the strongest designs difference twice: a within-item contrast between two candidate responses, differenced again across a manipulated attribute, read off a bounded rating scale. We show that this endpoint is not identified on the scale that reports it. Each term of the double difference is censored by its own share, so the observed statistic confounds differential preference with differential attenuation: a severity shift common to both responses manufactures an interaction whenever the two censor it unequally, as unequal distances from the bounds make them, exactly where good stimuli place them. We exhibit the failure inside a pre-registered audit of a frozen pedagogy judge, sealed before the first of its 990 calls. The registered primary endpoint, the effect of a stated learner profile on the judge's scaffolding preference, is null: $+0.085$ points (95\% BCa $[-0.167, +0.353]$, $p = 0.684$). The audit's one nominally significant interaction, $+0.378$ ($p = 0.002$), is not identified as preference: a construction containing zero differential preference reproduces 79 to 85\% of it from the observed severity shift and the scale floor alone. We derive the mechanism in closed form and show that its contribution is measurable from an audit's own ratings.

### 🤖 AI 总结

**一句话总结**：Audits of LLM judges certify a bias by contrasting matched conditions, and the strongest designs difference twice: a within-item contrast between two candidate responses, differenced again across a ma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, Censored, Rating, Scale, Can, Manufacture, Effect, Evidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27309v1) | [下载PDF](https://arxiv.org/pdf/2608.27309v1.pdf)

---

## cs.CV

## [21. UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City](https://arxiv.org/abs/2608.27456v1)

**作者**：Tianjie Ju, Zheng Wu, Yueqing Sun 等 18 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-27

### 📄 论文摘要

Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround supports closed-loop interaction from a first-person view and provides an interactive map for navigation. Agents can directly enter the 3D city and explore from a first-person view. Our analysis follows the growth of the spatial problem through three research questions. We first test whether an agent can ground a local scene well enough to answer spatial questions after active observation. Then we ask whether that grounding supports navigation as destinations become farther away and less explicit. Finally, we examine whether the resulting behavior survives changes in route availability and pedestrian motion. Contemporary MLLM agents usually show useful atomic abilities in visual recognition and short-range spatial reasoning, while orientation and pedestrian-aware movement remain unreliable. Their central failure emerges over extended exploration, where local abilities do not compose into sustained goal-directed behavior and errors accumulate without effective correction. We hope UrbanGround will support broader study of how far current MLLM agents can explore reliably in complex, open-ended urban environments.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investiga...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UrbanGround, Local, Perception, Spatial, Agency, Real-Scale, City, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27456v1) | [下载PDF](https://arxiv.org/pdf/2608.27456v1.pdf)

---

## [22. Reconstructing Humans and Objects in Interaction using Large Reconstruction Models](https://arxiv.org/abs/2608.27407v1)

**作者**：Agniv Chatterjee, Georgios Pavlakos  
**分类**：cs.CV  
**发布时间**：2026-08-27

### 📄 论文摘要

Estimation of Human-Object Interactions in 3D (3D HOI) is a fundamental problem in 3D computer vision with applications in AR/VR, robotics, and embodied AI. However, reconstructing these interactions in 3D remains challenging due to depth ambiguities, occlusions, and object shape variability. Existing approaches are primarily concerned with reprojection and contact constraints, fitting parametric human models and object templates to 2D images. In this paper, we explore a different avenue. We present MILO, a framework that leverages the visual capabilities of Large Reconstruction Models (LRMs) to recover detailed 3D human-object interactions from a single image. Our key observation is that LRMs provide a powerful geometric scaffold that preserves relative human-object arrangement and proximity cues. This significantly simplifies the reconstruction procedure, reframing the problem as interpreting the LRM mesh: we segment it into human and object components, fit a parametric body model to the human part, and optionally align an object template to the object part (if such a template is available). MILO achieves strong reconstruction accuracy and outperforms existing baselines across multiple benchmarks and interaction scenarios. Our code is available at https://ac5113.github.io/MILO.

### 🤖 AI 总结

**一句话总结**：Estimation of Human-Object Interactions in 3D (3D HOI) is a fundamental problem in 3D computer vision with applications in AR/VR, robotics, and embodied AI. However, reconstructing these interactions ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reconstructing, Humans, Objects, Interaction, Large, Reconstruction, Models, Estimation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27407v1) | [下载PDF](https://arxiv.org/pdf/2608.27407v1.pdf)

---

## [23. Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](https://arxiv.org/abs/2608.27367v1)

**作者**：Frederik Berenz  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transformer blocks for higher-order semantic abstraction), driven by a task-agnostic test-and-verify mechanism that exploits function-preserving expansion to safely trial architectural changes and roll back if they do not improve prediction loss. The Sketched Isotropic Gaussian Regularizer (SIGReg) ensures that all learned semantic dimensions remain statistically independent and aligned with the predictive objective, preventing collapse even as the architecture grows. On a 60-dimensional multi-object dynamics task, SCG naturally triggers depth expansion, improving prediction loss by 20.3% over the fixed small baseline with 56 times greater parameter efficiency than scaling to the fixed large model; on a 2D navigation task, a single width expansion yields even an 23% improvement over the fixed large model. Across all three tested environments of increasing complexity, the adaptive encoder matches or exceeds the fixed small baseline, with zero false-positive expansions and bit-exact function preservation (ratio = 1.0, absolute difference = 0.0). The take-away is that JEPA world model encoders need not be pre-allocated at maximum capacity - they can grow successively as the task demands, achieving significant compute and data efficiency while maintaining representation quality.

### 🤖 AI 总结

**一句话总结**：Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Successive, Capacity, Growth, Task-Complexity-Driven, Width, Depth, Expansion, Vision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27367v1) | [下载PDF](https://arxiv.org/pdf/2608.27367v1.pdf)

---

## [24. KnockGS:interaction-Grounded Calibrationof Physical Gaussian Representations](https://arxiv.org/abs/2608.27365v1)

**作者**：Chenchen Ge, Hanwen Shen, Bowen Jing 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Physics-integrated 3D Gaussian representations now allow reconstructed deformable objects to be simulated and rendered under explicit material models. Existing pipelines, however, assume that material parameters are known or manually specified, limiting their applicability when these parameters must be inferred from observed object dynamics. We propose KnockGS, an interaction-response PhysicalGS framework that estimates the elasticity and density scales of a 3D Gaussian object from its dynamics under a known applied force. Rather than treating physical simulation only as a forward process, we turn the force-induced response into a calibration signal: temporal response features are xtracted from the observed dynamics, the two material scales are estimated from those features, and the estimate is then frozen and written back into the same simulator so that it can be tested on an interaction it was never fitted to.We evaluate the framework on both parameter recovery and response-level fidelity. The estimated scales are compared against hidden ground truth, and the re-simulated object is measured against the target using 3D particle trajectories, response-curve statistics, and rendered-frame quality. Across five held-out material targets, our method recovers the scales substantially more accurately than response retrieval, global regression, or a fixed default material, and the frozen estimate remains predictive under interactions that differ in direction and in magnitude. Interaction response therefore carries enough information to calibrate material scales in physically grounded 3D Gaussian representations.Our study is a first step toward interactive PhysicalGS systems that calibrate a Gaussian asset whose rendered appearance and simulated response are consistent.

### 🤖 AI 总结

**一句话总结**：Physics-integrated 3D Gaussian representations now allow reconstructed deformable objects to be simulated and rendered under explicit material models. Existing pipelines, however, assume that material...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, KnockGS, interaction-Grounded, Calibrationof, Physical, Gaussian, Representations, Physics-integrated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27365v1) | [下载PDF](https://arxiv.org/pdf/2608.27365v1.pdf)

---

## [25. PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345v1)

**作者**：Yuandong Pu, Le Zhuo, Sayak Paul 等 14 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-08-27

### 📄 论文摘要

Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible trajectory, but also the distribution of possible behaviors under the same initial observation and action. We call this distribution-level requirement probabilistic alignment. However, existing evaluations largely assess individual-video plausibility and do not test whether repeated generations recover the correct distribution. This raises a central question: how far are current video generators from probabilistically aligned world modeling? To answer it, we formalize probabilistic alignment as a distributional criterion for world models and introduce PAWBench, a benchmark for evaluating video generators as stochastic samplers of world dynamics. We further introduce PAWEval, an outcome-level protocol that converts repeated video rollouts into empirical distributions over possible physical behaviors. Across 50 scenarios and eleven current systems, no model consistently matches the reference probabilities while recovering the range of valid behaviors. Having established this gap, we test whether language prompts, initial noise sampling, or model training can reshape the model's predictive distribution. We believe our work can serve as a foundation for future efforts to move towards probabilistically aligned world modeling.

### 🤖 AI 总结

**一句话总结**：Recent video generation models are increasingly framed as world models. Many physical processes can unfold in more than one valid way. Therefore, a world model should reproduce not only a plausible tr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PAWBench, How, Far, Probabilistically, Aligned, World, Modeling?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27345v1) | [下载PDF](https://arxiv.org/pdf/2608.27345v1.pdf)

---

## [26. R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](https://arxiv.org/abs/2608.27328v1)

**作者**：Qiwen Gu, Bingjie Gao, Rui Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-27

### 📄 论文摘要

High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambiguity makes absolute revisit scores sensitive to rendering stability, repetitive content, and failed motion. We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency. For every detected return, R2M-Bench compares the revisit pair with two controls from the same rollout: a gap-matched non-revisit pair that measures generic temporal stability and a short-range pair that estimates short-horizon consistency. These comparisons produce \emph{MemoryGain} (MG), the revisit advantage over the temporal baseline, and the \emph{Normalized Memory Ratio} (NMR), which normalizes this advantage by the short-to-baseline dynamic range. R2M-Bench combines 100 reference scenes with three leave-and-return trajectories to form 300 instances and evaluates appearance fidelity, scene and object identity, local geometry, and persistent state. Across seven action-conditioned video world models, Overall NMR correlates with human consistency judgments at Spearman's $ρ=0.547$ (95\% CI $[0.45,0.63]$). Its within-model correlation magnitude with generated motion is $0.072$, compared with $0.207$ for raw revisit similarity, indicating that relative calibration substantially reduces the slow-motion shortcut. DreamX-World-Memo achieves the highest Overall NMR among the evaluated video models. Together, these results support same-rollout relative calibration as a practical way to distinguish revisit-specific consistency from generic temporal stability.

### 🤖 AI 总结

**一句话总结**：High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little. This ambigui...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：R2M-Bench, Evaluating, Revisit, Memory, via, Relative, Consistency, Interactive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27328v1) | [下载PDF](https://arxiv.org/pdf/2608.27328v1.pdf)

---

## [27. Detection of Christmas tree plantations from high-resolution aerial imagery. A case study in the French Morvan](https://arxiv.org/abs/2608.27290v1)

**作者**：Francesca Razzano, Emanuele Dalsasso, Adrien Baysse-Lainé 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-08-27

### 📄 论文摘要

Christmas tree plantations are economically relevant, yet a largely unexplored application domain in Remote Sensing (RS). Their delineation is challenging because of high planting density, short rotation cycles, visual confusion with surrounding vegetation, the availability of dense labels for one reference year only, and severe class imbalance at the landscape scale. Although Deep Learning (DL) methods have shown strong potential for vegetation mapping, existing approaches are typically designed for forests, generic plantation systems, or orchards, and do not explicitly address the structural specificity and hard-negative confusion that characterize Christmas tree plantations. In response to these challenges, this work makes three main contributions: (i) it frames Christmas tree plantation mapping as a distinct rare-target semantic segmentation problem; (ii) it introduces a Hard Negative Mining (HNM) strategy to improve discrimination against confusing background patterns; and (iii) it evaluates the proposed framework across complementary levels, including supervised testing, temporal transfer, and large-scale validation. On the 2020 test set held out, the best model, DeepLabV3 with a ResNet-34 encoder, achieves an IoU of 0.733 and an F1-score of 0.846. HNM substantially improves precision-recall behavior, increasing the area under the precision-recall curve from 0.204 to 0.913. Temporal inference further shows meaningful transferability, reaching IoU/F1 values of 0.751/0.858 on 2017/2018 and 0.691/0.817 on 2023. Large-scale validation further highlights the intrinsic difficulty of the task, as Christmas tree plantations occupied only a very small fraction of the extent of the common evaluation, corresponding to 1,498.4 ha (1.72\%) in 2017/2018 and 1,782.2 ha (2.04\%) in 2023 out of 87,309.4 ha in total.

### 🤖 AI 总结

**一句话总结**：Christmas tree plantations are economically relevant, yet a largely unexplored application domain in Remote Sensing (RS). Their delineation is challenging because of high planting density, short rotat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Detection, Christmas, tree, plantations, high-resolution, aerial, imagery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27290v1) | [下载PDF](https://arxiv.org/pdf/2608.27290v1.pdf)

---

## [28. Sidecar: Training-Free Semantic Reuse for Character-Consistent Free-form Visual Storytelling](https://arxiv.org/abs/2608.27280v1)

**作者**：Sibo Dong, Sarah Adel Bargal  
**分类**：cs.CV  
**发布时间**：2026-08-27

### 📄 论文摘要

Visual storytelling requires generating images that follow a narrative while preserving consistent character identities across frames. In free-form story generation, a character is fully described only when first introduced and is later referred to by a type-level mention or pronoun. Although this setting better reflects natural storytelling, later prompts may omit important identity-related semantics, making character consistency more difficult to maintain. We propose \textbf{Sidecar}, a plug-and-play semantic augmentation module that preserves entity-level information from the initial description and injects the missing semantics into later prompt embeddings. Sidecar requires no additional training and does not modify the architecture of the base diffusion model. Experiments on FreeStoryBench show that Sidecar consistently improves prompt-image alignment and character consistency across multiple SDXL- and FLUX-based baselines, with negligible computational overhead.

### 🤖 AI 总结

**一句话总结**：Visual storytelling requires generating images that follow a narrative while preserving consistent character identities across frames. In free-form story generation, a character is fully described onl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Sidecar, Training-Free, Semantic, Reuse, Character-Consistent, Free-form, Visual, Storytelling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27280v1) | [下载PDF](https://arxiv.org/pdf/2608.27280v1.pdf)

---

## cs.LG

## [29. Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](https://arxiv.org/abs/2608.27351v1)

**作者**：Yunpeng Ba, Zhi Zheng, Yue Xie 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-27

### 📄 论文摘要

Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO)). By systematically investigating ES dynamics and mechanisms, this paper first identifies a performance advantage of ES over GRPO, theoretically and empirically showing that ES can lead to broader reasoning coverage, thereby better exploiting the reasoning capabilities of pretrained LLMs. Theoretically, we show that verifier-projected Jensen-Shannon diversity across the ES population is helpful to higher Pass@K performances. Empirically, unlike GRPO, which exhibits entropy collapse, ES improves Pass@1 while attaining higher Pass@K than GRPO. We further develop a sequential GRPO-ES training strategy that combines GRPO's strength in Pass@1 with ES's gains in Pass@K. Second, we find that despite substantial whole-model parameter drift, the task-performance gains of ES are only contributed to a sparse subset of larger-magnitude updates. This functional sparsity suggests that large parameter movement need not imply widespread functional change, and held-out evaluations further show that it does not necessarily lead to catastrophic forgetting. Finally, we study how hyperparameter design affects the effectiveness of ES, demonstrating that ES requires a smaller population size in a larger LLM. These findings position ES as a distinct reasoning post-training paradigm rather than a less effective, memory-efficient alternative to GRPO.

### 🤖 AI 总结

**一句话总结**：Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Understanding, Evolution, Strategies, Reasoning, Broader, Coverage, than

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27351v1) | [下载PDF](https://arxiv.org/pdf/2608.27351v1.pdf)

---

## [30. QuantumBoostNet: A Hybrid Classical-Quantum Architecture for Enhanced Accuracy in Cardiac Ultrasound View Identification](https://arxiv.org/abs/2608.27302v1)

**作者**：Mihai Udrescu-Milosav, Stefan-Alexandru Jura, Mihai Udrescu 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-08-27

### 📄 论文摘要

Accurate identification of the correct view or angle in cardiac ultrasound (echocardiogram) is a critical component of cardiologic imaging. This step is essential for precise anatomical interpretation, reliable measurement, and the reduction of clinical errors. Although computer vision has advanced significantly, most state-of-the-art models perform well on standard benchmarks but often yield suboptimal results in specialized medical imaging tasks due to the high level of noise present in the data. QuantumBoostNet, a hybrid classical-quantum architecture, is introduced to address these challenges. This model integrates a classical backbone with two heads: one classical and one quantum, with the quantum head implemented as a parametrized 10-qubit quantum circuit. Training occurs in two stages, with an adaptive transition between heads governed by a mixing parameter that monitors loss dynamics. Extensive experiments indicate that, despite the limited number of qubits that can be simulated, QuantumBoostNet consistently outperforms state-of-the-art classical and hybrid classical-quantum models in cardiac ultrasound view identification, achieving a relative improvement over the best competitor. QuantumBoostNet also demonstrates superior performance on established image classification benchmarks and exhibits robustness to noise. These findings support the continued development of hybrid classical-quantum models for specialized medical imaging applications.

### 🤖 AI 总结

**一句话总结**：Accurate identification of the correct view or angle in cardiac ultrasound (echocardiogram) is a critical component of cardiologic imaging. This step is essential for precise anatomical interpretation...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：QuantumBoostNet, Hybrid, Classical-Quantum, Architecture, Enhanced, Accuracy, Cardiac, Ultrasound

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2608.27302v1) | [下载PDF](https://arxiv.org/pdf/2608.27302v1.pdf)

---

