# arXiv AI 论文日报 | 2026-09-18

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CL](#csCL) (8 篇)
- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (6 篇)

---

## cs.AI

## [1. An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/abs/2609.20804v1)

**作者**：Run-Ze Fan, Zihao Zhang, Simin Ma 等 9 位作者  
**分类**：cs.AI, cs.CL, cs.LG, cs.SE  
**发布时间**：2026-09-17

### 📄 论文摘要

Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluated on SWE-Bench Verified and Terminal-Bench 2.1, we evaluate 176 matched settings spanning five context-management strategies, four context-window budgets, and targeted ablations of planning and action space. We find that: (1) Context management becomes increasingly valuable as the context-window budget tightens, with most of its benefit coming from preventing context-overflow failures. (2) Staging rule-based elision before LLM-based summarization provides the strongest overall efficiency among the context-management strategies, whereas making elided content recoverable adds machinery that models rarely use and yields no accuracy gain. (3) Planning shifts from an accuracy scaffold for weaker models to a cost saver for stronger models, with little change in accuracy. (4) Predefined tools improve performance for models with weaker bash proficiency, whereas bash-capable models can operate effectively with a bash-only interface and achieve substantially lower cost, especially on command-line-centric tasks. Trajectory-level analysis explains these effects: context management extends execution trajectories without substantially altering agent behavior, planning changes where trajectories stop, and the action space changes the granularity at which code is written. These findings inform model- and budget-aware harness design and provide a modular framework for evaluating future harness components.

### 🤖 AI 总结

**一句话总结**：Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic syste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, of, Agent, Empirical, Study, Harness, Design, Coding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20804v1) | [下载PDF](https://arxiv.org/pdf/2609.20804v1.pdf)

---

## [2. RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents](https://arxiv.org/abs/2609.20754v1)

**作者**：Mingxuan Zhang, Xiaowen Wang, Anupma Sharan 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-17

### 📄 论文摘要

Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat support cases as static documents and overlook their multi-stage, stateful nature. We introduce RAFT (Retrieval-Augmented Framework for Troubleshooting Agents), a stateful RAG framework that abstracts each closed historical case into a directed chain of timeline entries and retrieves at the entry level, surfacing cases whose intermediate states match the active case and returning the parent-case trajectory anchored at the matched state; an optional case-level graph links cases through a configurable similarity representation. We evaluate this retrieval layer directly, which, unlike evaluating a full agent system, requires no production deployment. Because public multi-stage troubleshooting data is extremely rare, we pair a synthetic benchmark built from Microsoft Learn Windows Server documentation with real Apache Jira issues carrying human-created duplicate labels. RAFT improves Case Hit over vanilla RAG and GraphRAG baselines at every stage of case progress, with statistically significant gains over the strongest baseline; the Jira results provide directional evidence that the advantage transfers to real case histories. We release our benchmark, implementation, and the Apache Jira evaluation set.

### 🤖 AI 总结

**一句话总结**：Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, RAFT, Stateful, Retrieval-Augmented, Framework, Troubleshooting, Effective, enterprise

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20754v1) | [下载PDF](https://arxiv.org/pdf/2609.20754v1.pdf)

---

## [3. Q&A on Any Spreadsheet Requires Interpreting Its Grid Structure](https://arxiv.org/abs/2609.20732v1)

**作者**：Zofia Smoleń  
**分类**：cs.AI, cs.SE  
**发布时间**：2026-09-17

### 📄 论文摘要

Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We propose a novel framework of splitting any spreadsheet into interpretable chunks using cell role annotation. Our framework beats the state of the art, yet it faces a hard ceiling. Spreadsheets are fundamentally two-dimensional unstructured data with continuous relationships and infinite potential cell roles. Because classification models are restricted to finite, pre-defined classes, they cannot perfectly capture this structural nuance, even with human-level annotation. We show that addressing the spreadsheet-to-LLM bottleneck requires moving beyond discrete cell classification. Instead, the field must develop dimensionality-reduction techniques to directly flatten 2D unstructured spreadsheets into 1D unstructured text. Text chunks would be easier for downstream RAG to interpret and generate from.

### 🤖 AI 总结

**一句话总结**：Semantic cell annotation improves chunking interpretability for spreadsheets in LLM-driven RAG systems, aiding answer generation through enriched context rather than improved retrieval accuracy. We pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Q&A, Any, Spreadsheet, Requires, Interpreting, Its, Grid, Structure

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20732v1) | [下载PDF](https://arxiv.org/pdf/2609.20732v1.pdf)

---

## [4. Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models](https://arxiv.org/abs/2609.20722v1)

**作者**：Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-17

### 📄 论文摘要

Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B across four architectures. On SST-2 sentiment, it achieves a 13.1 percentage-point improvement with zero code changes. Mechanistic grounding enables automated discovery of intervention points that generalize across tasks and architectures. On sentiment, RepE without head masking fails to improve over baseline, while Deep Noir improves all models (p less than 0.01). We further show that steering creates a predictable prompt-injection attack surface whose vulnerability increases monotonically with steering magnitude. This finding is relevant to agent systems deploying steered classifiers.

### 🤖 AI 总结

**一句话总结**：Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Deep, Noir, Autonomous, Steering, Discovery, via, Architectural, Chronometry

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20722v1) | [下载PDF](https://arxiv.org/pdf/2609.20722v1.pdf)

---

## [5. Ownership in AI-Assisted Everyday Tasks](https://arxiv.org/abs/2609.20658v1)

**作者**：Megan Wei, Melanie Subbiah, Audrey Lee 等 7 位作者  
**分类**：cs.AI, cs.HC  
**发布时间**：2026-09-17

### 📄 论文摘要

When does work done with AI still feel like ours? As AI becomes woven into everyday tasks, we must examine what happens to our sense of ownership and contribution when a machine shares in producing what we make. We report an exploratory qualitative survey in which participants were asked to describe two recent, self-selected tasks completed with AI: one that felt like their own and one that did not. We find that felt ownership depends on the process of collaboration: people disown work when they merely approve AI's suggestions, but retain ownership when they lead, iterate, or rewrite. Ownership can also extend to settings where people own the vision for a project but not the execution; respondents reported high ownership on tasks they could not have completed without AI. Loss of personal voice and a lack of comprehension of the output both erode ownership. Finally, willingness to disclose AI use is often decoupled from actual pride or ownership, and instead shaped by community norms and fear of credit erasure. We propose several research directions as a result of these findings to promote AI development that supports people's sense of authorship over their own lives.

### 🤖 AI 总结

**一句话总结**：When does work done with AI still feel like ours? As AI becomes woven into everyday tasks, we must examine what happens to our sense of ownership and contribution when a machine shares in producing wh...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ownership, AI-Assisted, Everyday, Tasks, When, does, work, done

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20658v1) | [下载PDF](https://arxiv.org/pdf/2609.20658v1.pdf)

---

## [6. PAA: The Probabilistic Allen Algebra: A Generative and Complete Probabilistic Extension of Allen's Interval Relations](https://arxiv.org/abs/2609.20634v1)

**作者**：Julian Eggert  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-09-17

### 📄 论文摘要

Allen's interval algebra is a qualitative calculus for temporal relations, but its thirteen base relations are crisp predicates over exact interval boundaries. This is inadequate for temporal information from language, perception, databases, or uncertain histories, where times, durations, and boundaries are uncertain and expressions such as "just before" or "roughly during" have graded meaning. We develop the probabilistic Allen algebra (PAA): a generative and complete extension in which relation probabilities are derived from distributions over interval boundaries rather than assigned as scores. Time points are Gaussian; intervals have Gaussian midpoints and truncated-Gaussian durations. Every relation is a boundary-ordering predicate in one common probability space: point-point relations reduce to error functions, and point-interval and interval-interval relations to multivariate Gaussian orthant probabilities induced by linear inequalities. Contact relations (meets, starts, finishes, equals) receive positive measure through a tolerance band, and under a single tolerance the thirteen relations form a true partition that recovers crisp Allen as the tolerance vanishes. The construction derives Allen's taxonomy rather than positing it: coarse predicates such as precedence, overlap, and containment are unions of leaves whose probabilities are leaf sums, and this hierarchy is preserved as intervals collapse to points and thirteen relations reduce to five and then three. Each relation further decomposes into correlation-aware temporal primitives in the spirit of CIDOC CRM. The algebra is scale-invariant and separates graded expressions such as "shortly before" from contact relations. All results are Monte-Carlo validated and shipped as an open, tested Python package.

### 🤖 AI 总结

**一句话总结**：Allen's interval algebra is a qualitative calculus for temporal relations, but its thirteen base relations are crisp predicates over exact interval boundaries. This is inadequate for temporal informat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PAA, Probabilistic, Allen, Algebra, Generative, Complete, Extension

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20634v1) | [下载PDF](https://arxiv.org/pdf/2609.20634v1.pdf)

---

## cs.CL

## [7. Embedding Models Measure in Peculiar Ways](https://arxiv.org/abs/2609.20821v1)

**作者**：Juri Opitz, Andrianos Michail  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-09-17

### 📄 论文摘要

Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective notion of semantic equivalence and distance. We find that physical measurement is only weakly modeled in the embedding space, and that instead quite peculiar measurement patterns can be observed. Further analysis indicates that embedding representations of physical measurements are strongly influenced by superficial string similarity, and recalibration of similarity does not substantially improve the alignment.

### 🤖 AI 总结

**一句话总结**：Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Embedding, Models, Measure, Peculiar, Ways, spaces, define, notions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20821v1) | [下载PDF](https://arxiv.org/pdf/2609.20821v1.pdf)

---

## [8. Unifying Models of Intergroup Hostility in Online Discourse](https://arxiv.org/abs/2609.20808v1)

**作者**：Patrick Gerard, Julia Mendelsohn, Kristina Lerman  
**分类**：cs.CL, cs.SI  
**发布时间**：2026-09-17

### 📄 论文摘要

Hostile rhetoric toward social groups can normalize exclusion and justify mistreatment, as well as contribute to rising polarization and political violence. Efforts to moderate hostile rhetoric in online speech draw on foundational theories in social and moral psychology, and political science. However, these theories were developed largely in parallel, often propose different and sometimes conflicting accounts of how hostility develops, and have rarely been tested against each other in real discourse. The result is a fragmented understanding of the rhetorical mechanisms of hostility, without a clear sense of how they appear, and relate to each other, in real-world discourse. Using 2.86 million posts from TikTok, Truth Social, and Twitter/X during the 2024 U.S. presidential election, we model the mechanisms of six foundational theories of intergroup hostility -- boundary construction, threat construction, scapegoating, negative evaluation, dehumanization, and action orientation -- within a common empirical framework to recover the broader organization of intergroup hostility rhetoric. Structurally, we find that boundary construction and threat construction anchor the system; temporally, we find that these mechanisms tend to follow a regular ordering: boundary construction, derogation, and action orientation tend to appear early; dehumanization and threat construction later; scapegoating latest. Mapping how these theoretical frameworks actually manifest in discourse bridges longstanding divisions across social science traditions and presents computational social science with a clearer empirical foundation for modeling intergroup hostility rhetoric beyond single-label detection.

### 🤖 AI 总结

**一句话总结**：Hostile rhetoric toward social groups can normalize exclusion and justify mistreatment, as well as contribute to rising polarization and political violence. Efforts to moderate hostile rhetoric in onl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Unifying, Models, Intergroup, Hostility, Online, Discourse, Hostile

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20808v1) | [下载PDF](https://arxiv.org/pdf/2609.20808v1.pdf)

---

## [9. JEPA-Anything: Learning Predictive Models across Different Worlds](https://arxiv.org/abs/2609.20800v1)

**作者**：Taoyong Cui, Zhongyao Wang, Xinyue Xu 等 13 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-17

### 📄 论文摘要

World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction. Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems? We introduce JEPA-Anything, a domain-agnostic framework based on orthogonal predictive factorization (OPF). Extending joint-embedding predictive architectures, OPF decomposes latent targets into complementary factors, learns them through dedicated pathways, and recombines them within a shared predictive design. We evaluate JEPA-Anything across seven domains: vision, biology, clinical trajectories, control, molecular dynamics, physical fields, and weather. Experiments span representation learning, intervention prediction, out-of-distribution generalization, and long-horizon dynamics, including 10 matched dynamics tasks, forecasting of over 1,000 clinical events, and 100-step molecular rollouts across four systems. Against matched JEPA baselines, JEPA-Anything improves reported metrics on all 10 dynamics tasks and reduces single-intervention prediction error on Interventional Pong by 34.8%. It achieves the lowest one-step and 100-step molecular errors among compared methods in all four systems. Beyond prediction, a factor-nominated biological intervention receives experimental support in cell co-cultures, patient-derived organoids, tumor fragments, and mice; latent orbital modes recover the Keplerian scaling exponent with a fitted slope of -1.4991. These results support a common factorized predictive principle across heterogeneous worlds, connecting world modeling with intervention and experimentally grounded scientific discovery. Code: https://github.com/Gen-Verse/JEPA-Anything

### 🤖 AI 总结

**一句话总结**：World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction. Yet predictive models remain domain-specific: can a common learning principle support w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：JEPA-Anything, Learning, Predictive, Models, across, Different, Worlds, World

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20800v1) | [下载PDF](https://arxiv.org/pdf/2609.20800v1.pdf)

---

## [10. Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations](https://arxiv.org/abs/2609.20779v1)

**作者**：Sarah Wyer, Sue Black, Noura Al Moubayed  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-17

### 📄 论文摘要

Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters prevalent in GPT-2 women-directed output disappear by GPT-4, while men-directed completions gain positive representational territory (caregiving, emotional range, ally identity) that women-directed completions do not. The pattern is most visible at GPT-5: Topic~5 (1,997~documents) frames breast cancer as a men's rights debate, while zero equivalent clusters appear in women-directed output. Three independent classifiers score this content as non-toxic. Sentiment scores invert at GPT-4: early models demean women; later models over-correct. Topic diversity in women-directed completions falls 36\% relative to men at the GPT-4 alignment boundary (W/M~$= 0.58$, from $0.91$ at GPT-2). REGARD representational harm disparity correlates with release date ($ρ= +0.55$, $p = .034$) while Detoxify does not ($ρ= -0.23$, $p = .42$): toxicity scores fall as representational harm grows. We formalise harm laundering as a three-criteria test and provide a three-stage detection protocol applicable to any generative model. Within the OpenAI GPT lineage, toxicity score reduction is not a sufficient proxy for harm reduction.

### 🤖 AI 总结

**一句话总结**：Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Harm, Laundering, GPT, Models, Evidence, Gender, Discrimination, Transformed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20779v1) | [下载PDF](https://arxiv.org/pdf/2609.20779v1.pdf)

---

## [11. On-Demand Attention: Language Models Know When to Recall](https://arxiv.org/abs/2609.20734v1)

**作者**：Haibo Feng, Ruiqi Liang, Hanyang Peng 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-17

### 📄 论文摘要

Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, regardless of its benefit to the next prediction. We show that a pretrained model's decoding states already contain information predictive of this benefit, before the global read. Building on this finding, we introduce On-Demand Attention (ODA), a local-first decoding method that uses a lightweight recall head to selectively invoke global attention as its predicted benefit changes during generation. ODA trains only the recall head, leaving pretrained weights unchanged and the complete historical KV cache available for future recall. We further implement GPU-side conditional execution in vLLM, translating reduced global reads into practical decoding speedups over full attention at long context lengths. Experiments across Qwen and Gemma models, including hybrid-attention backbones, show that selective recall recovers most of the performance lost under local attention while substantially reducing global reads. These findings support long-context inference in which pretrained models guide their own access to the information they retain.

### 🤖 AI 总结

**一句话总结**：Reasoning and agentic workloads increasingly demand efficient long-context inference. Yet full-attention decoding reads the growing history at every step, regardless of its benefit to the next predict...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：On-Demand, Attention, Language, Models, Know, When, Recall, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20734v1) | [下载PDF](https://arxiv.org/pdf/2609.20734v1.pdf)

---

## [12. Summarization Bias: The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models --- A Conceptual Framework and Registered Test Protocol](https://arxiv.org/abs/2609.20712v1)

**作者**：Levent Bulut  
**分类**：cs.CL  
**发布时间**：2026-09-17

### 📄 论文摘要

This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as the reconstructable inferential structure that produces it. Within the Bulut Doctrine, narrative effect is theorized along a told-shown axis: in told mode, emotional and informational content is declared explicitly and requires little reader reconstruction; in shown mode, that content is suppressed at the surface and must be reconstructed from physical cues and indirection (Objective Projection). Shown mode is the higher-load condition the doctrine is designed to measure.   The claim is that LLMs fail along this axis in a specific direction. Summarization bias is hypothesized to operate in two regimes: (i) a generative regime, in which a model asked to render an emotion through Objective Projection defaults to declaring it instead; and (ii) an evaluative regime, in which a model judging narrative quality rewards told-mode explicitness and under-detects shown-mode suppression. The evaluative regime is the more consequential, since LLMs increasingly serve as judges and reward models, and a directional bias toward told mode would impose a selection pressure degrading prose toward flat declaration.   This report does not claim the bias is validated. It defines the construct, situates it against LLM-as-judge biases, rereads a completed independent reliability study as directional evidence consistent with it, and pre-registers a two-regime test with decision rules under which the construct would be abandoned.

### 🤖 AI 总结

**一句话总结**：This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Summarization, Bias, Directional, Collapse, Objective, Projection, Told-Mode

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20712v1) | [下载PDF](https://arxiv.org/pdf/2609.20712v1.pdf)

---

## [13. HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding of Women's Health Communication](https://arxiv.org/abs/2609.20684v1)

**作者**：Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-17

### 📄 论文摘要

Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We introduce HerHealthEval, a controlled evaluation framework for multilingual understanding of women's-health communication. For each clinical case, HerHealthEval provides matched versions in English, French, and Modern Standard Arabic using six communicative forms: canonical, clinical, layperson, indirect or hedged, emotionally concerned, and deliberately under-specified. The first five express the same underlying concern and retain the same clinical information, whereas the under-specified form intentionally omits relevant details to test whether the model recognizes that clarification is needed. We evaluate a multilingual instruction model and QLoRA-adapted variants on concern classification, risk calibration, clarification behavior, parse compliance, and cross-form consistency. Results reveal that aggregate accuracy and consistency can conceal safety-relevant failures. A multilingual adaptation model reaches 0.994 under-triage in French and Arabic under language-asymmetric risk supervision. A controlled re-adaptation using source-derived, language-invariant risk labels reduces under-triage to 0.572 and 0.558, respectively. These findings show that robust multilingual healthcare evaluation requires explicit testing of register variation, uncertainty handling, and the provenance and invariance of adaptation labels.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly used in healthcare communication, yet most evaluations emphasize response quality while assuming that the user's concern has been interpreted correctly. We intro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, HerHealthEval, Evaluating, Multilingual, Register-Sensitive, Understanding, Women's, Health

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20684v1) | [下载PDF](https://arxiv.org/pdf/2609.20684v1.pdf)

---

## [14. Chronicle: Cut-Point Replay for Regression Testing of LLM Agents](https://arxiv.org/abs/2609.20625v1)

**作者**：Tisha Chawla, Susheem Koul  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-17

### 📄 论文摘要

Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundaries as immutable envelopes and replays it from the record. Its central operation, cut-point replay, serves a chosen subset of boundaries from the record and executes the complementary subset live with new code, turning a recorded incident into a regression test that runs in continuous integration. On a benchmark of 6 recorded failures with simulated model boundaries, recording adds 23 μs per crossing (0.008% of an assumed 300 ms model call), full replay issues zero model calls and is bit-stable across 20 repetitions, and cut-point tests fail on faulty code and pass on guarded and benign changes for all 6 incidents. In a mutation study of the guarded tools, cut-point tests catch every mutant that lets the recorded unsafe action through, while a baseline that stubs every boundary, using the same assertion, catches none. Chronicle and the benchmark are publicly available at https://github.com/theagentplane/chronicle.

### 🤖 AI 总结

**一句话总结**：Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing stat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Agent, Chronicle, Cut-Point, Replay, Regression, Testing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20625v1) | [下载PDF](https://arxiv.org/pdf/2609.20625v1.pdf)

---

## cs.CV

## [15. Can 4D Foundation Models Remember?](https://arxiv.org/abs/2609.20819v1)

**作者**：Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstruction models, can perceive and reconstruct dynamic environments, but how well they remember what they have perceived remains an open question. Existing benchmarks largely rely on pixel-level metrics and lack ground truth for objects once they leave the field of view, making them unable to evaluate visual memory in an object-centric manner against references. To fill this gap, we introduce PersistBench, a dataset and metric suite that leverages 360° videos as omniscient ground truth and proposes three evaluation aspects: object permanence, motion continuity, and appearance preservation. Evaluating various models across diverse categories reveals that current models can only maintain short-term consistency that degrades significantly once objects leave the field of view. Our findings highlight the gap between current model capabilities and robust visual memory ("seeing is not remembering"), providing guidance for future development of 4D foundation models. Dataset and code are available on the project page: https://guangzhaohe.com/persistbench.

### 🤖 AI 总结

**一句话总结**：Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstructi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Can, Foundation, Models, Remember?, Perceiving, remembering, visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20819v1) | [下载PDF](https://arxiv.org/pdf/2609.20819v1.pdf)

---

## [16. FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations](https://arxiv.org/abs/2609.20817v1)

**作者**：Kevin Qu, Tao Sun, Massimiliano Viola 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.RO  
**发布时间**：2026-09-17

### 📄 论文摘要

Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a single observation and therefore rely heavily on learned category-level shape priors. We present FAMOS, a feed-forward model that predicts movable-part segmentation and joint parameters from a sparse, unordered set of partial point clouds. Our model jointly reasons over multiple observations and naturally supports a variable number of inputs, including a single view. To aggregate articulation cues across observations, we introduce a Multi-state Articulation Transformer with alternating state-wise and global attention. We further propose an observed articulation span objective that supervises the motion range each part exhibits across the input observations, encouraging the model to leverage the full observation set. To overcome the limited scale and diversity of existing datasets, we introduce a procedural data generator that synthesizes self-annotated assets during training. Experiments on PartNet-Mobility, ACD, and ArtiCraft-10K demonstrate consistent improvements over both feed-forward and optimization-based baselines. Project page: https://kevinqu7.github.io/famos

### 🤖 AI 总结

**一句话总结**：Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, FAMOS, Feed-Forward, Articulation, Modeling, Sparse, Observations, articulated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20817v1) | [下载PDF](https://arxiv.org/pdf/2609.20817v1.pdf)

---

## [17. Paint-Anything: Unified Any-Color Control for Image Generation and Editing](https://arxiv.org/abs/2609.20816v1)

**作者**：Ji Xie, Dewei Zhou, Xinyu Huang 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-09-17

### 📄 论文摘要

Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-prompt interface for generation and editing through object-level color supervision. We develop a data pipeline that constructs Paint-500K from real images through object grounding, perceptual color labeling, and editing-pair synthesis. Since shadows make real-image labels only approximate colors, we complement this supervision with pure-color anchors whose pixels exactly match their paired hex values. These anchors are used only at high-noise timesteps, leaving low-noise training to natural images. We further introduce Any Color Benchmark (ACBench), comprising ACBench-T2I and ACBench-Edit, to measure object-level hex color fidelity across both tasks. On FLUX.2-4B, Paint-Anything improves ACBench-T2I and ACBench-Edit scores by 85.3% and 28.3%, respectively, relative to the base model, with ablations supporting the training recipe. It also achieves the highest average CompColor score among the compared methods.

### 🤖 AI 总结

**一句话总结**：Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, ed...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Paint-Anything, Unified, Any-Color, Control, Image, Generation, Editing, Professional

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20816v1) | [下载PDF](https://arxiv.org/pdf/2609.20816v1.pdf)

---

## [18. ERCPMP-Gx: Endoscopic Image and Video Dataset for Morphological, Histopathological, and Genomic Characterization of Colorectal Polyposis](https://arxiv.org/abs/2609.20815v1)

**作者**：Zahra Ghaffari, Massih Bahar, Mojgan Forootan 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-17

### 📄 论文摘要

Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these syndromes are essential for timely diagnosis, individualized patient management, and targeted surveillance strategies for affected families. However, public endoscopic datasets are largely organized around the individual sporadic polyp, and none links the polyposis phenotype to histopathology and germline findings at the patient level. Here, we present ERCPMP-Gx, an endoscopic, histopathological, and genomic dataset developed to support the application of artificial intelligence (AI) in the recognition, characterization, and classification of colorectal polyposis. Most procedures were performed using the Olympus EVIS X1 system with white-light endoscopy (WLE), narrow-band imaging (NBI), magnifying NBI (M-NBI), and NBI with near focus modes, yielding 160 images and accompanying video clips. Approximately eighty percent of cases represent clinically and/or genetically confirmed hereditary polyposis syndromes (PG), including familial adenomatous polyposis (FAP), Peutz-Jeghers syndrome (PJS), juvenile polyposis syndrome (JPS), and ganglioneuroma syndrome (GNS), while the remaining twenty percent comprise non-hereditary polyps and polyp-mimicking lesions with overlapping morphological features (Non-PG), included to support differential classification. Each released record is linked, where available, to standardized endoscopic annotations, representative histopathology, and clinically reported germline findings, forming an AI-ready, patient-level annotation framework. The dataset is publicly accessible at Mendeley (https://doi.org/10.17632/nzyfc544bx.2). For the latest updates and further information, readers are referred to the DataBioX website: https://databiox.com.

### 🤖 AI 总结

**一句话总结**：Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ERCPMP-Gx, Endoscopic, Image, Video, Dataset, Morphological, Histopathological, Genomic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20815v1) | [下载PDF](https://arxiv.org/pdf/2609.20815v1.pdf)

---

## [19. FlowSGS: Improving Flow Matching Priors for Inverse Imaging with Stochastic Interpolants](https://arxiv.org/abs/2609.20769v1)

**作者**：Tianao Li, Xinhui Qian, Emma Alexander  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

Flow matching has emerged as the state-of-the-art generative model and has been used for plug-and-play (PnP) priors to solve inverse problems in computational imaging. However, existing flow-based inverse solvers assume linear forward models and/or make simplifying approximations in posterior sampling. To circumvent these problems, we introduce FlowSGS, a flow-based posterior sampling method using Split Gibbs Sampling (SGS) to decompose the posterior into a likelihood step and a prior step. Specifically, we sample from the likelihood step using Langevin dynamics and leverage the Stochastic Interpolants (SI) framework to integrate a pretrained flow model into the prior step. We provide a form for the prior step that uses SI's reverse-time SDE, and show connections to previous PnP methods. Moreover, with the aid of the flow prior's straight probability paths and a novel timestep correction technique for the reverse-time SDE, FlowSGS requires fewer network evaluations in its prior step than plug-and-play diffusion samplers. Our experiments show state-of-the-art performance on a range of inverse problems. For the first time, we provide an experiment on a nonlinear inverse problem (Fourier phase retrieval) for flow-based inverse solvers.

### 🤖 AI 总结

**一句话总结**：Flow matching has emerged as the state-of-the-art generative model and has been used for plug-and-play (PnP) priors to solve inverse problems in computational imaging. However, existing flow-based inv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FlowSGS, Improving, Flow, Matching, Priors, Inverse, Imaging, Stochastic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20769v1) | [下载PDF](https://arxiv.org/pdf/2609.20769v1.pdf)

---

## [20. Should This Case Be Adapted? Prediction Fragmentation Controls Test-Time Adaptation](https://arxiv.org/abs/2609.20700v1)

**作者**：Lili Wang, Jing Li, Xiaowen Sun 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

Episodic test-time adaptation resets a frozen segmenter to source weights $M_0$ on each case and adapts for a fixed step count. A fixed horizon conflates a cohort-level question, how far to adapt, with an irreducibly per-case one, whether this case should be adapted at all. Cohort means hide that decision: on cross-vendor cardiac MRI the mean $Δ$Dice from adaptation is statistically indistinguishable from zero while 58.7% of cases are individually made worse. We quantify this harm as harmful accepted area (HA), the harmful fraction of the edited area a controller deploys. Held-out tuning gives a stronger baseline than a fixed horizon, but the budget it selects transfers on neither of the two main medical benchmarks, and no global budget can condition on the case. We show that prediction fragmentation---the disagreement geometry between $M_0$ and the adapted mask $M_k$---predicts HA with no labels or extra backward passes at decision time, comparably on three benchmarks (Spearman $ρ$ 0.50--0.60), at a quarter of gradient-norm's latency. A case-level router built on it cuts HA from 0.228 to 0.139 on a benchmark that took no part in its design, with the design frozen and only cut-points recalibrated there. On the cardiac benchmark the design was selected on, the router cuts HA from 0.129 to 0.013 at matched Dice and 1.10 deployed updates, against the retrospective-best budget found post hoc on evaluation labels, and reduces that 58.7% to 20.0%, an upper bound we quantify. Where the retained cases are not net-helped (as on prostate), the router still cuts HA but concedes accuracy, a boundary we report. Thresholds are fit once on a labeled split disjoint from evaluation; decisions use no labels or gradients. The template ports across architecture and domain (nnU-Net$\to$SegFormer, Cityscapes$\to$ACDC) with coordinate, thresholds and per-bucket actions instantiated per domain.

### 🤖 AI 总结

**一句话总结**：Episodic test-time adaptation resets a frozen segmenter to source weights $M_0$ on each case and adapts for a fixed step count. A fixed horizon conflates a cohort-level question, how far to adapt, wit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Be, Should, Case, Adapted?, Prediction, Fragmentation, Controls, Test-Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20700v1) | [下载PDF](https://arxiv.org/pdf/2609.20700v1.pdf)

---

## [21. FunArt: Decoding Functional Structure and Articulation from Generative 3D Latents](https://arxiv.org/abs/2609.20673v1)

**作者**：Dennis Rotondi, Abdelrhman Werby, Kai O. Arras  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-17

### 📄 论文摘要

To operate effectively in human environments, robots must identify articulated objects, segment their movable and interactive parts, and estimate their kinematic models. Existing articulated scene representations typically recover kinematics from observed interactions, while methods operating on static scans often decouple articulation from functional interactive elements. We present FunArt, a framework that constructs articulation-aware functional 3D scene graphs from posed RGB-D observations captured in a single static configuration. FunArt reconstructs object instances, converts their fused geometry directly into the O-Voxel representation of TRELLIS.2, and exploits its frozen, sparse-compression VAE as a structural prior. A lightweight query-based decoder combines compact object-level latents with dense, surface-aligned features to jointly segment movable parts and functional interactive elements while estimating motion type, axis, origin, and range. On the Articulate3D dataset, FunArt achieves state-of-the-art performance across movable-part segmentation, articulation estimation, and functional-element segmentation, both with and without ground-truth object input. In the end-to-end setting, it outperforms the strongest baselines by 1.5 AP_{50} points for movable parts, 2.8 AP_{50} points under joint origin-and-axis constraints, and 6.7 AP_{50} points for functional elements. These results demonstrate that generative 3D latents encode actionable structural cues that can initialize robotic perception and planning before physical interaction.

### 🤖 AI 总结

**一句话总结**：To operate effectively in human environments, robots must identify articulated objects, segment their movable and interactive parts, and estimate their kinematic models. Existing articulated scene rep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, FunArt, Decoding, Functional, Structure, Articulation, Generative, Latents

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20673v1) | [下载PDF](https://arxiv.org/pdf/2609.20673v1.pdf)

---

## [22. Earth Surface Immune System for Rapid Monitoring of Unknown Anomalies](https://arxiv.org/abs/2609.20662v1)

**作者**：Jingtao Li, Qian Zhu, Xinyu Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

Earth surface anomalies, driven by escalating climate change, and expanding human activities, are increasing in both frequency and diversity, yet their limited historical data and unpredictability make them fundamentally different from conventional remote sensing targets. Existing methods address specific anomaly categories or stop at localization, leaving a gap between detection and actionable information. Here we present ESIA, an Earth Surface Immune System whose architecture is constrained by three principles from the biological immune system, refined over millions of years against equally diverse and uncertain threats. A non-specific innate immune stage treats anomalies as unobserved changes in time-series satellite imagery, generating binary localization maps at 14.51 km2/s without assuming any anomaly category, surpassing the strongest general baseline by 37% in F1. A specific adaptive immune stage applies negative selection to filter text prompts and matches surviving prompts with localized image patches through a multi-modal foundation model, enabling open-vocabulary recognition of unknown anomaly attributes including category, affected area, and damage severity, with recognition F1 exceeding 80%. A mutation mechanism tunes minimal embeddings at test time, adapting to each scene in 3.26s using a single reference image pair. We validate ESIA on a global-scale dataset covering 19,801.60 km2 across six anomaly categories, comparing against 22 models, and further apply it to quantify degraded farmland in the Dnipro Delta following the Kakhovka Dam collapse and assess burn severity from 2025 Palisades Fire in Los Angeles. This unprecedented flexibility in handling unknown anomalies opens new avenues for real-time disaster response and environmental surveillance.

### 🤖 AI 总结

**一句话总结**：Earth surface anomalies, driven by escalating climate change, and expanding human activities, are increasing in both frequency and diversity, yet their limited historical data and unpredictability mak...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Earth, Surface, Immune, System, Rapid, Monitoring, Unknown

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20662v1) | [下载PDF](https://arxiv.org/pdf/2609.20662v1.pdf)

---

## [23. PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric Videos](https://arxiv.org/abs/2609.20638v1)

**作者**：Di Wen, Kailun Yang, Jimmy Weissert 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

An assistant watching egocentric video should notice a mistake from past frames alone, before the next step begins, and keep working once the person recovers. A mistake changes the state of the work, so every later step has to be read against what was done rather than against the plan. The first-mistake protocol that current online methods report on cuts each recording at its first mistake, so a fixed-time rule that never looks at the video is right on every case. We evaluate on complete trials, where mistakes and recoveries arise naturally, under a validation false-alarm budget and against controls that use timing alone. PROVIA keeps two records apart: a factual state, a learned summary of the steps each actor performed, mistakes included, and the accepted progress, an exact posterior over the state of an automaton induced from correct demonstrations by Bayesian state merging and over the execution status of each actor. Procedure-state transitions occur only in the correct-status branch; the mistake and correction branches retain the source state. A sequential test turns the per-frame mistake probability into alarms. With one filter and one optimization rule, PROVIA ranks mistakes best among the evaluated controlled baselines on CaptainCook4D, IndustReal, HoloAssist and IMPACT-ego. At a validation budget of 0.1 false alarms per minute it recalls .154 against .128 on CaptainCook4D and .034 against .015 on HoloAssist, where it leads at every budget. The pipeline runs at 58-70 frames per second. The source code is available at https://github.com/Kratos-Wen/PROVIA.

### 🤖 AI 总结

**一句话总结**：An assistant watching egocentric video should notice a mistake from past frames alone, before the next step begins, and keep working once the person recovers. A mistake changes the state of the work, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PROVIA, Procedure, State, Tracking, Online, Mistake, Detection, Egocentric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20638v1) | [下载PDF](https://arxiv.org/pdf/2609.20638v1.pdf)

---

## [24. Refinement Is Inherently Editable: Training-Free Prompt-to-Prompt Image Editing with Generative Refinement Network](https://arxiv.org/abs/2609.20633v1)

**作者**：Yulong Chen, Ziqian Zhang, Haoyu Zhang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-17

### 📄 论文摘要

Text-guided image editing must introduce the requested changes while preserving unrelated source content. Diffusion-based editors rely on spatial controls whose inaccuracies can leave edits incomplete or alter unrelated regions. Causal autoregressive editors face a further constraint: their fixed decoding order limits revision of earlier decisions. We introduce RefineEdit, a training-free prompt-to-prompt image editing framework built on a Generative Refinement Network. Our key idea is to couple edit localization with content generation through the global refinement of binary image codes, allowing editing evidence to be reassessed as the image evolves. RefineEdit initializes an editing branch from an intermediate source state, reusing the emerging layout. We compare the probabilities assigned by the two branches to the same source-sampled bits, using their signed differences to select editable positions and bits. Selected bits follow editing refinement, while the remaining bits copy the evolving source state. To stabilize editing across refinement steps, adaptive spatial freezing limits unnecessary mask expansion, while finite bit locking keeps recently selected bits editable. The framework requires no additional training, external masks, or attention control. Across nine editing categories of PIE-Bench, RefineEdit achieves the best background-preservation scores in PSNR, LPIPS, MSE and SSIM, together with the highest whole-image and edited-region CLIP scores among the evaluated methods.

### 🤖 AI 总结

**一句话总结**：Text-guided image editing must introduce the requested changes while preserving unrelated source content. Diffusion-based editors rely on spatial controls whose inaccuracies can leave edits incomplete...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Refinement, Inherently, Editable, Training-Free, Prompt-to-Prompt, Image, Editing, Generative

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20633v1) | [下载PDF](https://arxiv.org/pdf/2609.20633v1.pdf)

---

## cs.LG

## [25. Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1)

**作者**：Martin Marek, Max Ryabinin  
**分类**：cs.LG  
**发布时间**：2026-09-17

### 📄 论文摘要

Reinforcement learning (RL) of large language models is notoriously sensitive to small differences between training and inference engines, often referred to as the training-inference mismatch (TIM). However, completely eliminating TIM is impractical, as it would come at a major cost to rollout efficiency. In this paper, we show that the instability of RL under TIM is primarily caused by drift: a persistent bias between training and inference engines that accumulates with every training step. We derive an additive "score centering" correction term that stabilizes RL under TIM by canceling drift. When training models from 0.6B to 30B parameters, score centering alone matches or outperforms methods based on importance sampling under quantization, with the gap growing as the mismatch becomes more severe. Because the correction is additive, score centering also composes with importance sampling -- their composition outperforms pure importance-sampling baselines in our staleness experiments.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) of large language models is notoriously sensitive to small differences between training and inference engines, often referred to as the training-inference mismatch (TIM). H...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, of, Score, Centering, Stabilizes, Off-policy, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20807v1) | [下载PDF](https://arxiv.org/pdf/2609.20807v1.pdf)

---

## [26. PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative Inverse Solvers](https://arxiv.org/abs/2609.20794v1)

**作者**：Jiachen Yao, Zi-Siang Hsu, Xi Deng 等 8 位作者  
**分类**：cs.LG, cs.CE  
**发布时间**：2026-09-17

### 📄 论文摘要

Generative models are increasingly used to solve scientific inverse problems, but existing evaluations still focus primarily on whether a method can produce a single plausible reconstruction. This is insufficient for ill-posed problems, where multiple solutions may be consistent with the same sparse or noisy observations. In these settings, a method can achieve strong pointwise accuracy while still failing to capture the true posterior through mode collapse, overconfident uncertainty, or averaging incompatible solutions. We introduce PosteriorBench, a benchmark for evaluating the distributional accuracy of generative inverse solvers. PosteriorBench evaluates four physics-based inverse problems: Darcy flow inversion, Poisson source recovery, carbon capture and storage, and light transport material inference. For each task, we construct high-fidelity reference posteriors using computationally heavy but established procedures such as rejection sampling and Markov chain Monte Carlo, enabling direct assessment of whether solvers recover the full set of solutions rather than the single best sample. We pair these references with a five-metric posterior evaluation suite: posterior-mean error, posterior-standard-deviation error, maximum mean discrepancy, sliced Wasserstein distance, and radially averaged power-spectrum error. These metrics assess pointwise accuracy, marginal uncertainty, distributional alignment, and global frequency fidelity. The benchmark spans sparse sensing, low-resolution observations, nonlinear forward models, varying noise levels, and multimodal priors, with a unified pipeline for distribution matching and uncertainty quantification. Our experiments reveal substantial distribution-matching gaps across current solvers, while showing that neural operators improve resolution robustness, and guidance weights and generation noise are key to posterior-variance calibration.

### 🤖 AI 总结

**一句话总结**：Generative models are increasingly used to solve scientific inverse problems, but existing evaluations still focus primarily on whether a method can produce a single plausible reconstruction. This is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PosteriorBench, Point, Estimates, Posterior, Matching, Evaluating, Generative, Inverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20794v1) | [下载PDF](https://arxiv.org/pdf/2609.20794v1.pdf)

---

## [27. Calibrated RF-Fingerprinting Under Interference With Heterogeneous Transmission Protocols](https://arxiv.org/abs/2609.20765v1)

**作者**：Tariq Abdul-Quddoos, Xiangfang Li, Lijun Qian  
**分类**：cs.LG  
**发布时间**：2026-09-17

### 📄 论文摘要

Radio Frequency(RF)-Fingerprinting is a spectrum monitoring technique that identifies specific transmitters based on hardware impairments imprinted within the emitted signal. Although widely researched, studies almost exclusively consider scenarios where only one transmitter is emitting at a time, limiting real world applicability. In this work, we further the study of RF-Fingerprinting by considering co-channel interference, with multiple emitted signals interfering with each other, overlapping in time and frequency. Specifically, we formulate this problem as a multi-label classification problem and employ a 1D convolutional neural network (CNN). Furthermore, the models are calibrated such that the confidence thresholds for the label probabilities are derived, with guarantees on the upper bound on the average number of False Negatives, providing a degree of confidence in not missing a true spectrum policy violation. The proposed method is validated using real world data from the POWDER 5G testbed on devices transmitting 802.11a(Wi-Fi), 4G LTE, and 5G NR waveforms. The results show accuracy as high as 97% and as low as 73% after calibration depending on channel conditions. Also calibrating for various average false negatives upper bounds achieves micro recall scores of approximately (1 - calibrated false negatives) with the calibration robust to out-of-distribution interference, demonstrating the potential of the proposed method in a realistic high contention wireless environment

### 🤖 AI 总结

**一句话总结**：Radio Frequency(RF)-Fingerprinting is a spectrum monitoring technique that identifies specific transmitters based on hardware impairments imprinted within the emitted signal. Although widely researche...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Calibrated, RF-Fingerprinting, Under, Interference, Heterogeneous, Transmission, Protocols, Radio

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20765v1) | [下载PDF](https://arxiv.org/pdf/2609.20765v1.pdf)

---

## [28. RISC-V and machine learning: a survey](https://arxiv.org/abs/2609.20677v1)

**作者**：Shriman Keshri, Apparna Singh, Chinmaya Kumar Palo 等 5 位作者  
**分类**：cs.LG, cs.AR  
**发布时间**：2026-09-17

### 📄 论文摘要

The intersection of open-source processor architectures and machine learning is driving the demand for customizable, efficient, and accessible hardware. This survey examines the state of the RISC-V ISA in machine learning applications, analyzing current capabilities, challenges, and future directions based on recent research. The analysis covers academic and commercial implementations, software frameworks, and real-world applications. The RISC-V machine learning ecosystem is evaluated, from instruction set extensions and core implementations to compiler optimizations and deployment strategies. Key contributions include a unified taxonomy of RISC-V ML implementations, a comparative analysis of performance and design trade-offs, an evaluation of software toolchain maturity, and the identification of emerging trends in instruction set extensions and specialized accelerators. Findings reveal progress in energy efficiency, specialized instruction development, and framework integration, while highlighting challenges in standardization, verification complexity, and ecosystem fragmentation. The analysis proposes four research directions to address current limitations: specialized neural processing extensions, adaptive and modular processor architectures, security frameworks, and energy-efficient multi-domain architectures. These directions provide a roadmap for advancing RISC-V as a foundational platform for next-generation machine learning systems.

### 🤖 AI 总结

**一句话总结**：The intersection of open-source processor architectures and machine learning is driving the demand for customizable, efficient, and accessible hardware. This survey examines the state of the RISC-V IS...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, RISC-V, machine, learning, survey, intersection, open-source, processor

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20677v1) | [下载PDF](https://arxiv.org/pdf/2609.20677v1.pdf)

---

## [29. Epidemiological Causal Graph Identification: Challenges, Identifiability and Algorithms](https://arxiv.org/abs/2609.20676v1)

**作者**：Sambit Mishra, Yingying Wang, Christine K. Johnson 等 4 位作者  
**分类**：cs.LG, stat.ME, stat.ML  
**发布时间**：2026-09-17

### 📄 论文摘要

Causal discovery from observational data is fundamental to statistics and machine learning, yet determining causal direction without interventions necessitates structural assumptions. Existing identifiability research primarily focuses on continuous variables under additive noise models, often neglecting mixed datasets containing ordinal scales, counts, and continuous measurements. This paper investigates causal discovery in Directed Acyclic Graphs (DAGs) where nodes follow either an ordinal distribution (via an ordered logit model) or a regular one-parameter exponential family distribution. We prove that the edge direction between an ordinal and an exponential family node is distributionally identifiable for generic parameter values. Our findings generalize previous Ordinal-Poisson results to the broader exponential family. Computationally, we introduce a score-based exhaustive search and a masked continuous optimization framework using DAGMA for larger graphs. Numerical results validate the theory, recovering edge orientations within a Markov equivalence class that are unidentifiable under classical structural equation models.

### 🤖 AI 总结

**一句话总结**：Causal discovery from observational data is fundamental to statistics and machine learning, yet determining causal direction without interventions necessitates structural assumptions. Existing identif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Epidemiological, Causal, Graph, Identification, Challenges, Identifiability, Algorithms, discovery

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20676v1) | [下载PDF](https://arxiv.org/pdf/2609.20676v1.pdf)

---

## [30. Multi-center Medical Data Mining with FL-Net - A One-stop Shop for Federated Learning](https://arxiv.org/abs/2609.20650v1)

**作者**：Simon Süwer, Julian Klemm, Elisa Acitelli 等 41 位作者  
**分类**：cs.LG, cs.CR, cs.DC  
**发布时间**：2026-09-17

### 📄 论文摘要

Federated learning enables collaborative training without sharing patient-level data, but most studies remain simulations. Based on five requirements derived from the literature, we analyzed 14 FL frameworks and found that none fully satisfied these requirements. We present FL-Net, a novel federated clinical research framework to fulfill all requirements. It integrates modular data harmonization, data discovery, disclosure control, securely built versioned FL-Net-Tools and containerized federated workflow execution into a persistent network. It enables the re-use of harmonized data and workflows across studies. FL-Net's end-to-end capabilities were evaluated through harmonization, cross-study patient discovery across MIMIC and US-130, and reproducible, audited federated workflows with up to 50 concurrent clients. FL-Net is being developed within the dAIbetes and Microb-AI-ome EU projects and will cover over 800,000 patients across 10 hospitals in 9 countries covering longitudinal and single point in time data, FL-Net provides a practical foundation for interoperable, reproducible, and privacy-preserving multicenter clinical research.

### 🤖 AI 总结

**一句话总结**：Federated learning enables collaborative training without sharing patient-level data, but most studies remain simulations. Based on five requirements derived from the literature, we analyzed 14 FL fra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-center, Medical, Data, Mining, FL-Net, One-stop, Shop, Federated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.20650v1) | [下载PDF](https://arxiv.org/pdf/2609.20650v1.pdf)

---

