# arXiv AI 论文日报 | 2026-09-02

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.CL](#csCL) (9 篇)
- [cs.LG](#csLG) (6 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers](https://arxiv.org/abs/2609.01567v1)

**作者**：Matteo Merler, Giovanni Bonetta, Davide Zago 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-09-01

### 📄 论文摘要

Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertain, executes the suggested action during training, and distills guidance into a lightweight Reinforcement Learning (RL) policy. Because VLM advice is not always reliable, SAGE can weight teacher-action distillation using environment-derived advantages rather than treating all suggestions as equally useful. Across sparse-reward visual reasoning and navigation tasks, SAGE learns policies that act without VLM guidance at evaluation time and improves over unguided RL in several environments, including settings where the learned policy exceeds its VLM teacher. The results show that selective guidance is most beneficial when the VLM can help the agent discover high-reward trajectories, and less useful when unguided exploration already succeeds or teacher actions do not lead to informative experience. SAGE also reduces VLM usage by prompting the teacher only on a fraction of training steps and requiring no VLM calls at deployment. Overall, our results suggest that VLMs don't need to be used as fixed policies to be useful; they can instead act as temporary, imperfect sources of guidance whose value is tested and internalized through interaction.

### 🤖 AI 总结

**一句话总结**：Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve fr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Selective, Guidance, via, Entropy, Learning, Autonomous, Policies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01567v1) | [下载PDF](https://arxiv.org/pdf/2609.01567v1.pdf)

---

## [2. Can LLMs Discover Scientific Laws in Real and Parallel Worlds?](https://arxiv.org/abs/2609.01552v1)

**作者**：Yiming Huang, Ziche Liu, Zhuohang Wu 等 14 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-01

### 📄 论文摘要

Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constraints. As LLM capabilities advance and their role in AI for Science expands, it remains an open problem whether they can genuinely discover scientific laws and how this ability should be evaluated. Existing evaluations, however, often either simplify discovery through synthetic settings or reuse published targets that may already be familiar to LLMs. We therefore introduce SCILAWS-BENCH, a benchmark for scientific law discovery built from published research and real scientific data. It comprises 118 problems drawn from 381 scientific papers, covering 291 candidate laws and roughly 8M real data points across six scientific disciplines. Each problem is instantiated in two complementary settings: (1) SCILAWS-REAL asks models to propose laws from fixed real observations and evaluates held-out predictive fit and scientific validity derived from the source literature, and (2) SCILAWS-PARALLEL asks models to actively query residual-calibrated worlds and recover synthesized hidden laws derived from published forms. This two-setting task design preserves each problem's scientific context while separately evaluating fixed-record law discovery and active recovery of a newly synthesized hidden law. We find that predictive fit can diverge from scientific validity, memorization shapes whether models reproduce or move beyond published formulas, and our best-of-N study reveals a selection bottleneck. Our work provides a paper-grounded benchmark and new empirical perspectives for evaluating AI for scientific discovery. Project page: https://yiyihum.github.io/SciLaws-Bench

### 🤖 AI 总结

**一句话总结**：Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Can, Discover, Scientific, Laws, Real, Parallel, Worlds?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01552v1) | [下载PDF](https://arxiv.org/pdf/2609.01552v1.pdf)

---

## [3. EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](https://arxiv.org/abs/2609.01526v1)

**作者**：Qing Zhao, Haowei Li, Weijian Deng 等 5 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Scientific agents must learn not only how to reason, but also what to believe. However, existing LLM agents typically express scientific hypotheses in free-form text, leaving their beliefs implicit and difficult to test or revise. We introduce EvoSCM, which equips scientific agents with explicit structural causal models that evolve as new experimental evidence is collected. EvoSCM maintains a population of competing SCM hypotheses, each encoding a candidate causal explanation of the environment, and evolves them through a closed discovery loop. In each round, the agent abduces latent mechanisms from accumulated evidence, designs discriminative interventions, and commits to falsifiable predictions that it tests through experimentation. Discrepancies between prediction and observation are inductively distilled into correction rules that revise the causal structures and mechanisms of each hypothesis, and the agent then deductively validates the revised population against accumulated evidence and structural consistency to guide the next round. We evaluate EvoSCM on DiscoverPhysics, a benchmark requiring agents to uncover the hidden dynamics of noncanonical physical worlds through experimentation. EvoSCM consistently improves scientific discovery over baselines, yielding more accurate explanations and predictions while making more effective use of experimental interactions.

### 🤖 AI 总结

**一句话总结**：Scientific agents must learn not only how to reason, but also what to believe. However, existing LLM agents typically express scientific hypotheses in free-form text, leaving their beliefs implicit an...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EvoSCM, Scientific, Belief, Revision, Through, Causal, Model, Evolution

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01526v1) | [下载PDF](https://arxiv.org/pdf/2609.01526v1.pdf)

---

## [4. When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation](https://arxiv.org/abs/2609.01519v1)

**作者**：Peiying Zhu, Sidi Chang  
**分类**：cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instantiating the behavior named in the claim. We audit this risk in a multi-turn buyer--seller testbed for configurable hotel transactions. An initial implementation reported welfare gains from two marketplace guardrails of +87.4, +35.0, and +28.8 across a Qwen2.5 1.5B--14B ladder. It also gave guarded and unguarded agents different offer schemas and choice procedures. Holding the schema and buyer chooser fixed changes the paired contrasts to +7.2, -13.9, and +23.8. The four largest 14B single-generation effects averaged +229; after three generations per profile-condition, they averaged +37.6 (95% bootstrap interval [-34.2, 109.3]), while generation residuals account for 49.9% of variation in this post-hoc probe. A seller-incentive check is non-monotone: increasing profit pressure produces less profit than the default seller prompt. Scripted positive controls show why this matters. A profit-maximizing seller already attains first-best welfare, so guardrails mostly redistribute and reduce welfare; they create welfare only when the seller is explicitly programmed to force inefficient bundles. We contribute a construct-validity contract separating incentive validity, protocol isolation, stochastic stability, and welfare accounting, and returning INVALID or INCONCLUSIVE before substantive policy claims. In our case, the original estimate is INVALID under protocol isolation, while the controlled study remains INCONCLUSIVE under incentive validity and stochastic stability. The case does not show that guardrails are ineffective; it shows their apparent value is unidentified until the simulated agents and protocol pass these checks.

### 🤖 AI 总结

**一句话总结**：Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instant...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, When, Guardrails, Look, Effective, Construct, Validity, Failures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01519v1) | [下载PDF](https://arxiv.org/pdf/2609.01519v1.pdf)

---

## cs.CL

## [5. The Rise of Verbal Reinforcement Learning](https://arxiv.org/abs/2609.01597v1)

**作者**：Kshitij Tayal, Arun Sharma, Genta Indra Winata 等 5 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{Language as Grounding Signal}, where language defines the task itself by specifying goals, states, and reward structures; (2) \textbf{Language as Deliberative Feedback}, where natural language guides reasoning at test time without the need to update model parameters; (3) \textbf{Language as Learning Signal}, where language-based feedback shapes model parameters through training. Within each pillar, we synthesize representative work, distinguish key subcategories of approaches, and outline the distinct role language plays in shaping agent behavior. Together, this taxonomy shows how verbal reinforcement is reshaping agent development, while also defining the challenges and opportunities for building more capable and aligned agents.

### 🤖 AI 总结

**一句话总结**：Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and moder...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Rise, Verbal, Reinforcement, Learning, Natural, language, emerging

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01597v1) | [下载PDF](https://arxiv.org/pdf/2609.01597v1.pdf)

---

## [6. StudentSim: Training LLM-based Student Simulators](https://arxiv.org/abs/2609.01591v1)

**作者**：Ke Yang, Chenglong Wang, Michel Galley 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or corrections, while LLM role-play follows guidance fluently but does not reliably match the competence of the student being imitated. We present StudentSim, a training framework that turns sparse per-student data into individualized simulators through pooled training followed by per-student specialization. The resulting simulators both mirror a student's own responses and update them under tutor guidance. We also introduce StudentSimEval, a standardized protocol covering 60 students across chess, second-language English writing, and mathematics, using public learner datasets with de-identified records shared for research. StudentSimEval measures behavioral fidelity (F), or how well a simulator matches a student's responses, and guidance responsiveness (R), or how readily it updates under tutor guidance, with all methods fit and evaluated on the same records. Across all three domains, StudentSim outperforms GPT-5.4 on both metrics. In chess, StudentSim reaches F=0.51 and R=0.91, compared with 0.23 and 0.72 for GPT-5.4 and 0.45 and 0.27 for Maia2. As a proof of concept, using StudentSim as a reward model for tutor reinforcement learning produces a chess tutor that expert humans rate as more accurate, better-guided, and more personalized than a no-RL baseline and a tutor trained against a GPT-5.4 simulator reward. Code is available at https://github.com/microsoft/StudentSim.

### 🤖 AI 总结

**一句话总结**：AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to coll...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StudentSim, Training, LLM-based, Student, Simulators, tutors, most, useful

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01591v1) | [下载PDF](https://arxiv.org/pdf/2609.01591v1.pdf)

---

## [7. Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics](https://arxiv.org/abs/2609.01575v1)

**作者**：Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents curated by a Difficulty-Aware pipeline for layout diversity, fact-extractability, and cross-model consistency. Fitting on a single H100 and serving heterogeneous workflows via prompting, the model leads all deployable (non-reasoning) baselines up to an order of magnitude larger. A quality-adjusted cost analysis, with confirmation and correction costs calibrated from production telemetry, shows it reduces expected costs by over 80% against the human baseline and by more than 50% against the best competing open-source model, while larger baselines remain economically unviable.

### 🤖 AI 总结

**一句话总结**：Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude ext...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Closing, Cost-Quality, Gap, Document, VLMs, Difficulty-Aware, Data, Curation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01575v1) | [下载PDF](https://arxiv.org/pdf/2609.01575v1.pdf)

---

## [8. Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs](https://arxiv.org/abs/2609.01573v1)

**作者**：Jingtan Wang, Arun Verma, Xiaoqiang Lin 等 7 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-01

### 📄 论文摘要

How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad trends (e.g., SFT dominates in low-data regimes), lacks a principled allocation framework, and does not examine whether the optimal ratio transfers across model sizes. We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal region, the set of allocations within a specified tolerance of peak performance. Empirically, this region is wide even for small tolerances (2-10%), widens with model scale, and transfers reliably from small proxy models to large target models. This yields a practical strategy: small proxy-model experiments suffice to identify a transferable near-optimal region, eliminating the need for exhaustive large-scale search. Our results hold consistently across tasks, model families, and both preference-based off-policy and reward-supervision on-policy RL methods. We further analyze how the asymmetry in annotation costs between SFT and RL data shifts the near-optimal region.

### 🤖 AI 总结

**一句话总结**：How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad tr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Scaling, Near-Optimal, SFT-RL, Annotation, Budget, Allocation, Small, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01573v1) | [下载PDF](https://arxiv.org/pdf/2609.01573v1.pdf)

---

## [9. From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix](https://arxiv.org/abs/2609.01572v1)

**作者**：Olga Tsymboi, Dmitrii Stoianov, Ramil Latypov 等 14 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU pool. We consolidate traffic from over 200 internal applications onto a single model by closing quality gaps identified through production error analysis along three axes: instruction following, function-calling, and internal task distribution. Quality is tracked by offline benchmarks stratified to production traffic and scored by deterministic verifiers or calibrated LLM judges. Rather than optimising all objectives jointly, which introduces cross-domain reward interference, we train a separate GRPO expert per axis and merge them via two-stage SLERP. Each expert's reward exposes a distinct failure mode, namely semantic collapse, over-calling, and verbosity hacking, each requiring a domain-specific fix. In non-reasoning mode the recipe surpasses a ${\sim}7\times$ larger by total parameters baseline on the in-house Arena with 69.6 to 65.8, instruction following with 0.85 to 0.83, and function-calling with 0.79 to 0.77, while lifting general dialogue benchmarks. The model absorbs 50% of platform traffic, 116M requests per month, at a fraction of the serving cost.

### 🤖 AI 总结

**一句话总结**：Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Production, Traffic, Post-Training, Building, Self-Hosted, Covers, Corporate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01572v1) | [下载PDF](https://arxiv.org/pdf/2609.01572v1.pdf)

---

## [10. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification](https://arxiv.org/abs/2609.01564v1)

**作者**：Manish Gupta, Chaitanya Giri, Jayasimha Talur  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the model lacks the signal to choose correctly between them. We propose a framework that (1) identifies which label pairs the model struggles to distinguish, (2) expands the candidate set to include confusable labels, and (3) generates targeted rules to differentiate between similar candidates. The framework requires no fine-tuning, and the generated rules transfer to smaller, cheaper models. On three benchmarks (WOS, Flipkart, LEDGAR), our approach improves Macro F1 by up to 10.0pp over retrieval baselines, with smaller models (2B--20B) gaining up to 11.5pp via cross-model transfer.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Confusion, Clarity, Confusion-Aware, Retrieval, Knowledge, Injection, Text, Classification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01564v1) | [下载PDF](https://arxiv.org/pdf/2609.01564v1.pdf)

---

## [11. A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains](https://arxiv.org/abs/2609.01563v1)

**作者**：Ema Salkić, Alexander Fichtl, Philipp Ulrich 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linking each item to its category, sources, and related events, then merges duplicates and ranks them with a three-layer mechanism combining an algorithmic formula, an LLM relevance adjustment, and expert validation. Applied to five companies across the value chain, the pipeline produces 76,207 scored items, of which an independent check finds 92.6% valid. The automated rankings match expert judgment at an average Spearman correlation of 0.55 for risks and 0.72 for opportunities, and the resulting matrices identify trade restrictions as the dominant cross-company risk.

### 🤖 AI 总结

**一句话总结**：Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：systematic, Approach, constructing, Chance-and-Risk, Matrix, Semiconductor, Supply, Chains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01563v1) | [下载PDF](https://arxiv.org/pdf/2609.01563v1.pdf)

---

## [12. SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue](https://arxiv.org/abs/2609.01548v1)

**作者**：Stephanie Fong, Yiwen Jiang, Zimu Wang 等 15 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks remain scarce. Existing general-domain evaluations typically rely on static prompts and fixed-format tasks, overlooking conversational contexts and audience effects in everyday communication. To address these gaps, we introduce SDARE-Bench, the first scenario-based benchmark evaluating both stigma detection and open-ended response generation in LLMs, comprising 1,138 dyadic queries and 1,388 group dialogue. Empirical results across 8 LLMs consistently demonstrate poor identification of stigma components, especially in group dialogues. In open-ended response generation, stigma expression was substantially higher in group settings than in dyadic, with weaker resistance to stigma and more unrealistic advice. Responses were evaluated using a classifier trained on 1,392 human annotated responses. In constructed group pressure settings, stigma expression rates further increased to a striking average of 97.5%. Our findings identify stigma response as a recurring LLM safety vulnerability, especially in socially complex conversational contexts.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks rema...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SDARE-Bench, Evaluating, Large, Language, Models, Conversational, Stigma, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01548v1) | [下载PDF](https://arxiv.org/pdf/2609.01548v1.pdf)

---

## [13. GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](https://arxiv.org/abs/2609.01491v1)

**作者**：Elias Stengel-Eskin, Newton Sander, Carlos Bonetti 等 7 位作者  
**分类**：cs.CL, cs.AI, cs.MA  
**发布时间**：2026-09-01

### 📄 论文摘要

The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We find that language evolution does occur between LLM agents, that the resulting languages are compositional and morphologically productive, and that they deviate from the LLMs' English prior in ways that render them incomprehensible to humans. Moreover, we identify several qualities essential to this evolution: pressure towards efficiency; the strength of the models backing the agents; and access to a "postmortem" stage in which agents can agree on linguistic conventions. Importantly, we observe that different conditions govern the transmission of language to new agents. Specifically, we find that agents learn new languages from usage alone, take an active role in this learning, and that while stronger models are required for novel language emergence, weaker models can learn an existing language once it has emerged. Taken together, our results indicate that current LLMs have the potential for cumulative cultural evolution -- previously attested only in humans -- with mixed populations of agents developing capacities that go beyond their lowest common denominator.

### 🤖 AI 总结

**一句话总结**：The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, LLM, GlossoGen, Emergent, Language, Complex, Interactions, growing

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01491v1) | [下载PDF](https://arxiv.org/pdf/2609.01491v1.pdf)

---

## cs.CV

## [14. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System](https://arxiv.org/abs/2609.01607v1)

**作者**：Penghao Wu, Haiwen Diao, Weichen Fan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal to the other: generation enriches the visual features learned for understanding, while understanding strengthens vision--language alignment for generation. However, when both objectives are forced through the same computation path, one tends to dominate. A task-decoupled architecture that specializes conflicting visual computation while preserving semantic interaction avoids this asymmetric degradation. At the task level, through three case studies, we find positive bidirectional transfer when understanding and generation tasks rely on shared knowledge. At the system level, we show that an end-to-end UMM outperforms a matched planner--executor pipeline on complex tasks that explicitly require both image understanding and generation. Together, these results show that the value of UMMs extends beyond a unified interface: appropriate specialization, shared task knowledge, and end-to-end optimization can turn coexistence into synergy.

### 🤖 AI 总结

**一句话总结**：While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may rei...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Uncovering, Understanding-Generation, Synergy, Native, Unified, Multimodal, Models, Representation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01607v1) | [下载PDF](https://arxiv.org/pdf/2609.01607v1.pdf)

---

## [15. UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture](https://arxiv.org/abs/2609.01598v1)

**作者**：Asees Kaur, Suzanne S. Sindi, Erica M. Rutter  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep learning approaches such as U-Net achieve strong general-purpose segmentation performance but often produce fragmented or discontinuous predictions in fine vascular regions, since they do not explicitly enforce structural connectivity. Region growing algorithms preserve spatial context and topological continuity, but are highly sensitive to seed point initialization and can be computationally expensive. We propose UI-VISA (U-Net Initialized Vascular Image Segmentation Architecture), a hybrid pipeline that combines the complementary strengths of both approaches. UI-VISA uses U-Net's foreground predictions as informed seed points for a CNN-guided region growing algorithm, which then iteratively refines the segmentation by enforcing local connectivity and recovering fine vessel details that U-Net alone tends to miss or over-predict. We evaluate UI-VISA against standalone U-Net and a prior region-growing-based method (VISA) using 5-fold cross-validation on 26 DSA images. UI-VISA achieves the highest mean Dice and clDice scores across folds, and a paired Wilcoxon signed-rank test shows the improvement in clDice is statistically significant ($p=0.023$), consistent with the method's design goal of preserving vascular connectivity, while the improvement in Dice does not reach significance ($p=0.104$).

### 🤖 AI 总结

**一句话总结**：Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep lear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UI-VISA, U-Net, Initialized, Vascular, Image, Segmentation, Architecture, Accurate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01598v1) | [下载PDF](https://arxiv.org/pdf/2609.01598v1.pdf)

---

## [16. A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios](https://arxiv.org/abs/2609.01584v1)

**作者**：Sergio M. Silva, Otavio T. Remer, Gabriel E. Lima 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. However, models trained under controlled conditions often degrade in real surveillance scenarios due to changes in viewpoint, occlusion, illumination, and sensor characteristics. This paper introduces Unconstrained Vehicle Identification Benchmark (UVIB), a benchmark for evaluating three operational vehicle-analysis tasks: front/rear orientation, occlusion-related suitability for Vehicle Make and Model Recognition (VMMR), and color clarity. The benchmark contains 84,835 vehicle images from seven public Brazilian datasets, grouped into surveillance and general acquisition domains, with unified binary annotations that were not jointly available in the original sources. Four representative architectures, EfficientNetV2-S, ResNet-50, ViT/B-16, and YOLO11s-cls, are evaluated under mixed-domain, cross-domain, and cross-dataset protocols. The results show that domain shift has a stronger impact than architecture choice, with substantial degradation in cross-domain settings, especially for VMMR suitability and color clarity. While orientation generalizes more reliably, VMMR suitability remains affected by class imbalance and ambiguous occlusions, and color clarity is highly sensitive to illumination and sensor modality. These findings highlight the need for benchmarks and evaluation protocols that explicitly measure operational robustness beyond standard in-domain accuracy. The proposed benchmark is publicly available at https://github.com/UFPR-IPASP-PR/uvib-vehicle-attributes/.

### 🤖 AI 总结

**一句话总结**：Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. Howev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmark, Vehicle, Attribute, Classification, Cross-Domain, Surveillance, Scenarios, analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01584v1) | [下载PDF](https://arxiv.org/pdf/2609.01584v1.pdf)

---

## [17. SpatialGuard: Harness-Guided Verifiable Spatial Reasoning for Text-to-Image Generation](https://arxiv.org/abs/2609.01582v1)

**作者**：Ziyun Qian, Zizhi Chen, Yizhou Liu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned methods improve controllability, but often lack an optimizable and verifiable spatial intermediary before visual sampling. As a result, object relations, occlusion, visibility, and camera constraints can decay during multi-round generation. This paper presents SpatialGuard, a structured layout-guided framework for complex 3D spatial text-to-image generation. SpatialGuard parses prompts into image synthesis-oriented 3D layouts through a Spatial Layout Architect, realizes them as visual conditions and candidate images through a Visual Realizer, and uses a Visual Alignment Critic to validate consistency among prompt, layout, and image. To keep constraints stable across iterations, SpatialGuard introduces a Layout Harness that organizes rule constraints, tool invocation, shared knowledge, and feedback loops around the editable layout state. This design turns complex spatial generation from implicit prompt following into a verifiable process of planning, realization, validation, and repair. Comprehensive experiments show that SpatialGuard achieves state-of-the-art performance in complex 3D spatial layout generation and improves spatial faithfulness over existing text-to-image and layout control baselines.

### 🤖 AI 总结

**一句话总结**：Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned method...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpatialGuard, Harness-Guided, Verifiable, Spatial, Reasoning, Text-to-Image, Generation, Complex

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01582v1) | [下载PDF](https://arxiv.org/pdf/2609.01582v1.pdf)

---

## [18. BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net](https://arxiv.org/abs/2609.01554v1)

**作者**：Marven Sherif, Amgad Elmasry, Youssef Ghazal 等 4 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, PET, and a sparse scribble map for each of foreground and background. The network is initialised from the autoPET-III winning weights and extended from two to four input channels, with the two scribble channels zero-initialised so that the pretrained representation is preserved exactly at initialisation. Every model is fine-tuned per fold from the corresponding autoPET-III fold checkpoint, so that no validation case is seen during pretraining. PET intensities are normalised against a per-scan aorta blood-pool reference derived from a CT segmentation, which removes tracer- and centre-specific scaling without requiring lesion labels. At inference the five fold models are ensembled by averaging their softmax outputs per sliding-window patch, before Gaussian-weighted stitching. On the challenge's five-fold split, with each fold evaluated on its own validation cases, mean Dice is 0.554 and mean lesion-level F1 is 0.528 without scribbles, rising to 0.751 and 0.733 after five correction rounds. About 85% of that gain follows the first scribble, and the spread between fold models narrows five-fold over the same rounds, so interaction largely compensates for how well or badly a given model segments unaided.

### 🤖 AI 总结

**一句话总结**：Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V cha...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BS, CT, Take, Hint, Interactive, Multitracer, PET, Lesion

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01554v1) | [下载PDF](https://arxiv.org/pdf/2609.01554v1.pdf)

---

## [19. What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models](https://arxiv.org/abs/2609.01551v1)

**作者**：Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive physics, and (iii) anomaly detection. Both models encode camera motion, with best results ($>90$ ROC AUC) emerging at 60-70% of network depth, and achieve moderate anomaly detection performance ($>60$ ROC AUC), but remain near chance on intuitive-physics tasks, suggesting a limited encoding of deeper physical reasoning. Beyond classification, we find that temporal features from individual videos form smooth low-dimensional trajectories in representation space, suggesting that camera motion is not only linearly decodable but also geometrically organized. Based on these results, we apply geometry-aware spline-based steering in the model's latent representations to interpolate camera motion, yielding steered videos with smoother trajectories and more coherent temporal progression than linear interpolation.

### 🤖 AI 总结

**一句话总结**：Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, Where, How, Probing, Spatiotemporal, Representations, Video, Foundation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01551v1) | [下载PDF](https://arxiv.org/pdf/2609.01551v1.pdf)

---

## [20. Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison](https://arxiv.org/abs/2609.01530v1)

**作者**：Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko's frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.

### 🤖 AI 总结

**一句话总结**：Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Revisiting, Cross-View, Completion, Self-Supervised, Pre-Training, via, Reconstruction, Error

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01530v1) | [下载PDF](https://arxiv.org/pdf/2609.01530v1.pdf)

---

## [21. DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2609.01516v1)

**作者**：Qian Wang, Yu Wang, Weiqi Li 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered novel views. Recent efforts attempt to utilize powerful diffusion priors, yet they typically process rendered and reference views concatenated along an additional dimension in a single network. These methods overlook an inherent nature that different views should maintain appearance similarity but differ in structure due to view shifts, leading to blur caused by conflicts between the two properties. In this paper, we propose DualDiff, a novel pipeline that leverages dual diffusion priors with a Structure-Appearance Attention (SAA) module to introduce reference guidance for refining low-quality novel views rendered from flawed 3D representations. Specifically, we retain one diffusion branch to focus on extracting structural information from the low-quality novel views, while introducing another branch to ensure appearance consistency with reference views. Furthermore, we present a 3D reconstruction framework named DualDiff3D, which integrates a reliability-enhanced Render-Refine-Optimize (RRO) loop to progressively and robustly incorporate the refined novel views, yielding more accurate 3DGS. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods even in the inference-only setting, with further performance gains achievable through training. Our code and pre-trained weights are available at https://github.com/Akaneqwq/DualDiff3D.

### 🤖 AI 总结

**一句话总结**：While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, 3D, DualDiff3D, Dual, Structure-Appearance, Priors, Reliability-Enhanced, Gaussian

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01516v1) | [下载PDF](https://arxiv.org/pdf/2609.01516v1.pdf)

---

## [22. TempCloze: Can Video-LLMs Identify the Missing Middle?](https://arxiv.org/abs/2609.01515v1)

**作者**：Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu 等 7 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly long-take and egocentric videos. We construct same-source distractors along three dimensions: Semantic asks what event should happen, Alignment probes when it should occur, and Progression tests how it should unfold, while shared scenes and objects reduce appearance cues. Our evaluation of 10 proprietary and 21 open-source Video-LLMs reveals Alignment as the primary bottleneck: models often recognize plausible semantic content and local event progression but struggle with temporal alignment. We further conduct error pattern and behavioral sensitivity analyses on TempCloze-Mixed and TempCloze-Hard with four representative models to examine where errors arise and how candidate order, context direction, visible span, frame density, and test-time scaling influence model choices.

### 🤖 AI 总结

**一句话总结**：Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcut...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TempCloze, Can, Video-LLMs, Identify, Missing, Middle?, Temporal, reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01515v1) | [下载PDF](https://arxiv.org/pdf/2609.01515v1.pdf)

---

## [23. Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation](https://arxiv.org/abs/2609.01511v1)

**作者**：Lucas Cunha, Lucas Sotomaior, Lucas Gasperin 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across spatial, spectral, and hybrid input representations. The results show that clean-set performance is not a reliable indicator of robustness under compression, resizing, and blurring. Xception with RGB obtains the best clean performance, reaching 0.884 mean ROC-AUC, but degrades substantially on the harder partition. In contrast, frozen DINOv3 achieves the strongest degraded-set result, with 0.726 mean ROC-AUC, while training only a linear classification head. The representation analysis indicates that Fourier-domain cues are most useful when combined with RGB information, whereas purely spectral inputs consistently underperform spatial representations. Qualitative attribution maps further suggest that convolutional detectors focus on localized artifacts, while DINOv3 relies on broader facial structure. These findings reinforce the need for degraded evaluation protocols and highlight self-supervised visual representations as a promising direction for robust face forgery detection. Our source code is publicly available at https://github.com/lucasdocunha/FaceForgery-Benchmark/.

### 🤖 AI 总结

**一句话总结**：Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmarking, Spatial, Spectral, Self-Supervised, Cues, Face, Forgery, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01511v1) | [下载PDF](https://arxiv.org/pdf/2609.01511v1.pdf)

---

## [24. CameraEditor: Camera-Controlled Image Editing via Video-Prior Sequential Modeling](https://arxiv.org/abs/2609.01479v1)

**作者**：Xin Shen, Chengyou Jia, Keshuo Xing 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-01

### 📄 论文摘要

Beyond semantic content, camera parameters play a pivotal role in dictating the geometric perspective and appearance of any given image. While recent image editing models excel at semantic and stylistic manipulation, they struggle with explicit camera parameter control. When handling large perspective shifts, instruction-driven models face a dilemma: they either suffer from structural tearing or generate conservative outputs that ignore geometric instructions. To address this, we introduce CameraEditor, a framework that reformulates camera-controlled editing from a spatial problem into a temporal sequence prediction task. By leveraging the temporal coherence of video diffusion models, our approach integrates an explicit geometric perception module with a dynamic reference routing mechanism. This allows us to construct geometrically rigorous visual reference pairs via dynamic panorama cropping, overcoming the ambiguity of text-based instructions. Furthermore, CameraEditor strategically inserts intermediate transition frames to decompose large perspective shifts, providing a robust temporal buffer that preserves content identity and spatial coherence. We construct a training dataset of 5,760 instances. As an independent contribution, we introduce CamEditor-Bench, a model-agnostic evaluation suite of 462 test cases. Extensive experiments demonstrate that CameraEditor achieves state-of-the-art camera control precision and source identity preservation, outperforming existing methods.

### 🤖 AI 总结

**一句话总结**：Beyond semantic content, camera parameters play a pivotal role in dictating the geometric perspective and appearance of any given image. While recent image editing models excel at semantic and stylist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CameraEditor, Camera-Controlled, Image, Editing, via, Video-Prior, Sequential, Modeling

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01479v1) | [下载PDF](https://arxiv.org/pdf/2609.01479v1.pdf)

---

## cs.LG

## [25. The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally](https://arxiv.org/abs/2609.01587v1)

**作者**：Jundong Hu, Shekar Ramachandran  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-09-01

### 📄 论文摘要

Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) across 9 open-weight models in 4 architecture families, we test 3 intuitive hypotheses: that quantization damage lives in task circuits, where the model computes, or in weight statistics. None of them predicts which layers benefit from restored precision. Recovery is instead diffuse: for 8 of 9 models, recovering 75% of the gap takes roughly half the layers; the lone exception, Qwen3-8B, is sharply concentrated. At a matched precision budget, spending it globally on finer quantization granularity beats locally repairing the most recoverable layers for all 8 group-128-compatible models (all but OpenLLaMA, whose width rules out group-128), by 21-52 points, including the concentrated Qwen3-8B. We report 2 secondary findings: the residual is budget-limited (8-bit is near-lossless in our evaluation across RTN, GPTQ, and AWQ), and the location of peak recovery correlates with architecture within a family, though not across families. Within this budget setting, global granularity is a better default than selectively protecting critical layers. More broadly, cheap signals that correlate with quantization damage do not necessarily identify where restoring precision improves accuracy; this must be tested with causal intervention.

### 🤖 AI 总结

**一句话总结**：Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization da...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Structure, Quantization, Damage, Why, Next, Bit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01587v1) | [下载PDF](https://arxiv.org/pdf/2609.01587v1.pdf)

---

## [26. Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks](https://arxiv.org/abs/2609.01558v1)

**作者**：Jing Xiao, Xinhai Chen, Qinglin Wang 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-01

### 📄 论文摘要

Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constructed by gradient surgery, $u_t$ the optimizer proposal, and $\mathcal{C}_t$ the conflict-free cone induced by the loss-specific gradients. We show that modern optimizers can transform $a_t$ through mechanisms such as historical state, adaptive scaling, preconditioning, or decoupled weight decay, so $a_t \in \mathcal{C}_t$ does not generally imply $u_t \in \mathcal{C}_t$. We refer to this optimizer-induced discrepancy in conflict-freeness between $a_t$ and $u_t$ as Gradient-Update Mismatch (GUM). Accordingly, we propose Gradient-Update Alignment (GUA), which projects $u_t$ onto $\mathcal{C}_t$ to obtain the aligned update $p_t$ and applies $p_t$ to the parameters. When the optimizer maintains internal state, GUA further adjusts this state toward targets reconstructed from the applied update. We conduct extensive experiments and find that GUM is widespread across momentum, adaptive, and curvature-based optimizers, with conflict rates reaching up to 86.3%. Across all PINN settings, GUA achieves conflict-free applied updates and consistently improves various gradient surgery methods, reducing the relative $L_2$ error by up to 98.2% in individual settings. Data and code are available at https://github.com/JingXiao10/GUA.

### 🤖 AI 总结

**一句话总结**：Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery met...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Gradient-Update, Mismatch, Rethinking, Conflict-Free, Training, Physics-Informed, Neural

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01558v1) | [下载PDF](https://arxiv.org/pdf/2609.01558v1.pdf)

---

## [27. A Mathematical Theory of Reusable Neural Bases for Network Compression](https://arxiv.org/abs/2609.01550v1)

**作者**：Binshuai Wang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

As large AI models become increasingly prevalent across a wide range of applications, memory cost has become a critical bottleneck in both training and inference. To mitigate this issue, we introduce the Linear Reusable Neural Bases Architecture (LRNBA), a novel framework aimed at improving parameter efficiency and reducing memory cost. Inspired by recurrent neural network (RNN) designs, the core idea of our approach is to represent each network block as a linear combination of a shared set of neural bases, thereby enjoying highly network compression rate while maintaining stable training. The proposed architecture allows for the construction of significantly wider and deeper networks under the same parameter budget. Extensive experiments demonstrate that our model achieves comparable or even faster convergence and lower loss than classical architectures, while maintaining stable training dynamics.

### 🤖 AI 总结

**一句话总结**：As large AI models become increasingly prevalent across a wide range of applications, memory cost has become a critical bottleneck in both training and inference. To mitigate this issue, we introduce ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Mathematical, Theory, Reusable, Neural, Bases, Network, Compression

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01550v1) | [下载PDF](https://arxiv.org/pdf/2609.01550v1.pdf)

---

## [28. Quantum Sparse Autoencoders for Q-Matrix Estimation in Cognitive Diagnosis](https://arxiv.org/abs/2609.01537v1)

**作者**：Arif Hassan Zidan, Yi Pan, Bowen Guo 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-01

### 📄 论文摘要

Q-matrices play a central role in cognitive diagnosis within educational data mining (EDM), specifying which latent skills each assessment item requires. Data-driven Q-matrix estimation remains challenging when assessments involve many correlated skills and when real response patterns depart from idealized generative assumptions. We introduce a novel quantum sparse autoencoder (QSAE) for Q-matrix estimation, which, to the best of our knowledge, is the first application of quantum machine learning (QML) to cognitive diagnosis. Overall, the QSAE embeds each student's binary response vector into a quantum circuit using an encoder, compresses it into a sparse latent representation, and maps that representation to the Q-matrix. We benchmark the QSAE against a classical autoencoder (CAE) across 60 simulated datasets and 9 real-world assessment datasets. The results reveal complementary strengths. Although the CAE partially achieves higher average accuracy under several simulation conditions, the QSAE is substantially more stable across replications, exhibiting lower variance in 49 of the 60 conditions. Moreover, on real assessment data, the QSAE outperforms the CAE on 6 of the 9 datasets. These findings suggest that the principal advancement of QML in this setting is not universal accuracy improvement, but enhanced robustness and capability to explore latent-structure complexity in real datasets.

### 🤖 AI 总结

**一句话总结**：Q-matrices play a central role in cognitive diagnosis within educational data mining (EDM), specifying which latent skills each assessment item requires. Data-driven Q-matrix estimation remains challe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Quantum, Sparse, Autoencoders, Q-Matrix, Estimation, Cognitive, Diagnosis, Q-matrices

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01537v1) | [下载PDF](https://arxiv.org/pdf/2609.01537v1.pdf)

---

## [29. Optimizing Byzantine Node Placement in Decentralized Federated Learning](https://arxiv.org/abs/2609.01495v1)

**作者**：Edoardo Gabrielli, Gabriele Tolomei  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-09-01

### 📄 论文摘要

Security evaluations of decentralized federated learning (DFL) typically focus on how Byzantine participants behave, while largely overlooking which participants are compromised. Yet, because aggregation is distributed over a communication graph, the placement of Byzantine nodes determines how malicious influence propagates through the network. We therefore treat Byzantine placement as an explicit adversarial decision and formulate the attacker's objective as selecting, under a fixed compromise budget, the set of participants that maximizes its finite-time impact on honest nodes. To approximate this objective without executing the learning process for every candidate placement, we introduce Byzantine Placement Influence (BPI), a set-level measure derived from the actual gossip dynamics that quantifies the cumulative exposure of honest nodes to Byzantine sources over the training horizon. Unlike placement criteria based on node centrality heuristics, BPI directly accounts for weighted multi-hop propagation and interactions among compromised nodes. We develop efficient algorithms for optimizing BPI and evaluate them across six heterogeneous graph families, untargeted model poisoning, and backdoor attacks. BPI-guided placements consistently identify highly damaging configurations across different network structures and remain effective when the linear gossip assumption is relaxed through Byzantine-robust aggregation. Our results show that Byzantine placement is a critical but under-modeled dimension of DFL threat models and robustness evaluations.

### 🤖 AI 总结

**一句话总结**：Security evaluations of decentralized federated learning (DFL) typically focus on how Byzantine participants behave, while largely overlooking which participants are compromised. Yet, because aggregat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Optimizing, Byzantine, Node, Placement, Decentralized, Federated, Learning, Security

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01495v1) | [下载PDF](https://arxiv.org/pdf/2609.01495v1.pdf)

---

## [30. Rethinking Learnability in Offline Data-driven Optimization](https://arxiv.org/abs/2609.01493v1)

**作者**：Chao Qian, Chen-Guang Wang, Rong-Xi Tan 等 4 位作者  
**分类**：cs.LG, cs.AI, cs.NE  
**发布时间**：2026-09-01

### 📄 论文摘要

Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization improves the efficiency of BBO algorithms by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires no additional online evaluations. Many offline optimization methods have been proposed, but a fundamental question remains unanswered: what learnability is sufficient for offline optimization? Prior theoretical studies show that Probably Approximately Correct (PAC) learnability is insufficient, as the optimal region may remain poorly learned even when most regions are well learned. In this paper, we propose algorithm-dependent learnability, which requires accuracy only on the optimizer's trajectory. We prove that its value-query form is sufficient for representative discrete settings, including greedy and local search for submodular maximization, while its first-order analogue is sufficient for projected gradient descent on convex minimization. Motivated by this notion, we formalize a trajectory-learning framework comprising trajectory construction, trajectory modeling, and candidate generation, and analyze existing trajectory-based methods under it. We further propose Uncertainty-aware Gradient-guided Trajectory Learning (UGTL), which constructs locally coherent improvement trajectories reflecting plausible search paths, models them with conditional diffusion, and selects a diverse candidate set. On five Design-Bench tasks, UGTL achieves the best aggregate mean rank, $3.1/25$, among 25 methods. Controlled trajectory analyses and cross-architecture replacements confirm that our trajectory construction plays a significant role in the improvement.

### 🤖 AI 总结

**一句话总结**：Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rethinking, Learnability, Offline, Data-driven, Optimization, Black-Box, BBO, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.01493v1) | [下载PDF](https://arxiv.org/pdf/2609.01493v1.pdf)

---

