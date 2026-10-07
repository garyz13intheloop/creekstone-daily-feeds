# arXiv AI 论文日报 | 2026-10-07

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (10 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.CL](#csCL) (7 篇)
- [cs.AI](#csAI) (4 篇)

---

## cs.AI

## [1. Sherpa: Teaching LLMs to Teach Adaptively](https://arxiv.org/abs/2610.08778v1)

**作者**：Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang 等 5 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address this, we introduce Sherpa, a multi-turn reinforcement learning framework that instantiates multiple student archetypes with LLMs conditioned on distinct learning preferences and trains a teacher model to adapt its instruction by directly maximizing their learning outcomes. Teacher LLMs trained with Sherpa improve instructed students' performance across all archetypes by an average of 20.5 percentage points. Under MathTutorBench's evaluation, Sherpa raises the overall pedagogy score from 52.5% to 79.2%, indicating better teaching responses. Our human studies show that the trained teacher is preferred over the base model in 79.6% of pairwise comparisons. Together, Sherpa trains LLM teachers to adapt to diverse simulated students and become better aligned with human teachers, paving the road towards AI tutors teaching real students.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Sherpa, Teaching, Teach, Adaptively, Large, language, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08778v1) | [下载PDF](https://arxiv.org/pdf/2610.08778v1.pdf)

---

## [2. VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning](https://arxiv.org/abs/2610.08761v1)

**作者**：Zewei Zhou, Rachel Luo, Yulong Cao 等 13 位作者  
**分类**：cs.AI, cs.RO  
**发布时间**：2026-10-06

### 📄 论文摘要

Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales verification through the co-evolution of the policy, training curriculum, and judge. The Policy Improvement Loop uses a rubric judge to diagnose recurring failures, construct an adaptive curriculum, and optimize the policy. When progress plateaus and verification becomes a bottleneck, the Judge Improvement Loop selectively queries human guidance on informative failure cases and refines the judge through coactive calibration, in which humans and agents resolve disagreements and converge toward the objective rubric of physical reasoning. The revised judge then guides the next stage of data selection and policy optimization. Experiments on driving and robot navigation tasks demonstrate continuous self-improvement in both policy and judge capability across reinforcement and supervised fine-tuning. These results show how scaling verification supports continuous self-improvement as policy failure patterns evolve.

### 🤖 AI 总结

**一句话总结**：Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VeriFine, Scaling, Verification, Self-Improvement, Embodied, Reasoning, Self-improving, policies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08761v1) | [下载PDF](https://arxiv.org/pdf/2610.08761v1.pdf)

---

## [3. nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://arxiv.org/abs/2610.08699v1)

**作者**：Guangyi Liu, Yong Liu, Jiangning Zhang  
**分类**：cs.AI  
**发布时间**：2026-10-06

### 📄 论文摘要

Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.

### 🤖 AI 总结

**一句话总结**：Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Agent, nanoMuse, Open-Source, Personal, Every, Device, Own

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08699v1) | [下载PDF](https://arxiv.org/pdf/2610.08699v1.pdf)

---

## [4. ScienceClaw: Benchmarking Continual Self-Evolution of AI-for-Science Agents Across the Natural and Social Sciences](https://arxiv.org/abs/2610.08691v1)

**作者**：Mingda Zhang, Wenjin Liu, Tiesunlong Shen 等 9 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-06

### 📄 论文摘要

Large language model agents are accelerating scientific automation, yet verified executions rarely become persistent program-level improvements, and existing evaluations do not examine this process across sequential tasks in both the natural and social sciences. We formalize ScienceClaw as fixed-parameter program self-evolution that unifies task solving, scientific verification, and program updates. ScienceClaw-Eval spans 23 disciplines and measures scientific correctness, evolutionary gain, retention, cross-dataset transfer, and evolution cost through sequential streams and independent reset evaluation. Our framework repairs executable workflows through multi-turn interaction, converts re-execution-verified failure--success trajectories into linked Skill and Operator candidates, and retains an update only when source-task replay reproduces the repair and independent scientific tasks improve. Code is available at https://github.com/beita6969/ScienceClaw.

### 🤖 AI 总结

**一句话总结**：Large language model agents are accelerating scientific automation, yet verified executions rarely become persistent program-level improvements, and existing evaluations do not examine this process ac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, ScienceClaw, Benchmarking, Continual, Self-Evolution, AI-for-Science, Across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08691v1) | [下载PDF](https://arxiv.org/pdf/2610.08691v1.pdf)

---

## cs.CL

## [5. IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas](https://arxiv.org/abs/2610.08781v1)

**作者**：Ziyu Chen, Yilun Zhao, Jiashuo Sun 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-06

### 📄 论文摘要

Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-grounded ideation remains challenging, as existing approaches based on prompting or feedback lack structured supervision for how papers should be synthesized. We introduce IdeaAnchor, a paradigm for training LLMs to perform research ideation using structured specifications as privileged signals. Each IdeaAnchor instance encodes how each input paper should be synthesized into a successful idea, including their functional roles, relationships, and target synthesis criteria. We build this paradigm by mining instances from published papers, capturing how real ideas emerge from prior literature. We then train models via demonstration, self-distillation, and reinforcement learning, and further enhance generation with retrieval at inference time. Experiments show consistent improvements in ideation quality. Our analysis reveals a functional decomposition: anchor-based training strengthens creative synthesis, retrieval enhances detail elaboration, and combining both yields the best performance.

### 🤖 AI 总结

**一句话总结**：Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, IdeaAnchor, Teaching, Turn, Literature, Research, Ideas, Scientific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08781v1) | [下载PDF](https://arxiv.org/pdf/2610.08781v1.pdf)

---

## [6. AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](https://arxiv.org/abs/2610.08773v1)

**作者**：Sarim Hashmi, Mukul Ranjan, Kshitij Mishra 等 6 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a task stops teaching once the agent solves it. We introduce AdvSim2Real, which co-evolves a task curriculum, an injection adversary, and the agent inside a frozen web world model. The curriculum is rewarded for tasks the agent solves about half of the time, and the adversary only for a success flip, an injection that turns a judged success into a failure. Training in the simulator makes a 4B agent both more capable and more robust: its completion rises with and without attacks, holds against a frontier-model adversary it never trained against, and its capability gain carries over to a real browser. On 150 web tasks, AdvSim2Real raises completion under this unseen adversary by 33.6\% relative to the base agent.

### 🤖 AI 总结

**一句话总结**：Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, AdvSim2Real, Training, Web, Against, Adaptive, Prompt, Injection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08773v1) | [下载PDF](https://arxiv.org/pdf/2610.08773v1.pdf)

---

## [7. The Missing Minimal Pair: Stereotype Evaluation in LLMs](https://arxiv.org/abs/2610.08747v1)

**作者**：Nataliya Stepanova, Ivan Titov, Emily Allaway 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

A common approach to measuring bias in Large Language Models is to compare the log-likelihoods of two contrastive stereotype sentences. We argue that such single-pair comparisons are often unreliable: simply rewriting the same stereotype with an alternative attribute can yield logically inconsistent preferences. To address this, we propose a dual minimal pair setup that introduces two axes of comparison for robust stereotype evaluation. First, we present a data-augmentation framework that fills critical gaps in existing stereotype datasets by generating paraphrases and alternate attributes. We apply our framework on a set of English, Russian, Spanish and Chinese stereotypes. Second, we introduce two evaluation metrics tailored to the dual minimal pair setup. One of these metrics provides a new perspective on bias by modeling the mutual information (MI) between social groups and stereotyped attributes. This MI-based metric is better suited for aggregation and enables more robust comparisons of stereotype strength across different languages and models.   Our code is available at https://github.com/stepanat/missing-minimal-pair/.

### 🤖 AI 总结

**一句话总结**：A common approach to measuring bias in Large Language Models is to compare the log-likelihoods of two contrastive stereotype sentences. We argue that such single-pair comparisons are often unreliable:...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Missing, Minimal, Pair, Stereotype, Evaluation, common, approach

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08747v1) | [下载PDF](https://arxiv.org/pdf/2610.08747v1.pdf)

---

## [8. Holdout Best-of-N: Unbiased Evaluation and Its Cost](https://arxiv.org/abs/2610.08719v1)

**作者**：Shrey Shah, Yinheng Li  
**分类**：cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

Reusing the scores that select a Best-of-$N$ winner can overstate its expected reward. We study evaluation from a fixed matrix of $K$ independent scores per candidate for a policy that selects using $J$ fresh scores. A single estimator based only on this matrix is exactly unbiased for expected judge reward under every independent, stable collection of candidate-specific score laws if and only if $J<K$, for every pool size $M\ge N\ge2$. At $J=K-1$, the selector deepens as $K$ grows. For independent Gaussian scores with common variance and fixed $M\ge N\ge2$, the unbiased minimax risk in this regime is of order $σ^2/\sqrt K$, attained by Holdout; allowing bias improves the rate to $σ^2/K$. For two candidates, we derive the minimum-variance unbiased estimator at known variance and the sharp asymptotic unbiased minimax constant $1/(π\sqrt2)$, which Holdout attains without knowing the variance. The cyclic average over subsets and ties can be computed in $O(MK\log M)$ operations. At fixed selector depth, cyclic evaluation of bounded scores has $O(K^{-1})$ risk uniformly in pool size. The impossibility result concerns the fixed matrix: one additional fresh winner score permits unbiased evaluation of the all-$K$ policy.

### 🤖 AI 总结

**一句话总结**：Reusing the scores that select a Best-of-$N$ winner can overstate its expected reward. We study evaluation from a fixed matrix of $K$ independent scores per candidate for a policy that selects using $...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Holdout, Best-of-N, Unbiased, Evaluation, Its, Cost, Reusing, scores

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08719v1) | [下载PDF](https://arxiv.org/pdf/2610.08719v1.pdf)

---

## [9. When Forgetting is not Catastrophic: On the Mechanics of Spurious Forgetting](https://arxiv.org/abs/2610.08718v1)

**作者**：Vedant Palit, Florent Draye, Nicolas Zucchet 等 5 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Knowledge that a language model appears to forget during finetuning often remains stored and can be recovered, a phenomenon called spurious forgetting. Finetuning on new facts can even produce forgetting that undoes itself: recall of the old facts collapses, recovers as training continues on new facts alone, and only then erodes for good. We seek to understand when such forgetting is not catastrophic. A minimal associative memory reproduces these dynamics with three ingredients: keys with shared structure, concentrated new values, and normalization in the network. Finetuning moves all old representations along a common direction, hiding the old facts while preserving their relative geometry; normalization withdraws this shift once the new facts are learned, whereas fact-specific changes accumulate and cause the erosion. Moreover, subtracting the common shift eliminates the collapse in a Transformer trained on synthetic data, and removing a single direction from each weight update restores old facts in a pretrained language model. Forgetting thus combines a shared, reversible loss of access with a slow erosion of individual facts, and only the second is catastrophic. Which one dominates depends on whether the new data move old memories together or apart.

### 🤖 AI 总结

**一句话总结**：Knowledge that a language model appears to forget during finetuning often remains stored and can be recovered, a phenomenon called spurious forgetting. Finetuning on new facts can even produce forgett...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, When, Forgetting, not, Catastrophic, Mechanics, Spurious, Knowledge

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08718v1) | [下载PDF](https://arxiv.org/pdf/2610.08718v1.pdf)

---

## [10. Agreement Is Not Validity: Cross-Model LLM Consensus in Diagnosing Student Failure Modes in K-12 Math Tutoring Dialogue](https://arxiv.org/abs/2610.08703v1)

**作者**：Clayton Cohn, Joyce Fonteles, Kirk Vanacore 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

In K-12 mathematics tutoring, student-tutor dialogue provides rich evidence of learners' problem-solving processes and sources of difficulty. Learning analytics research increasingly relies on large language models (LLMs) to extract such information from dialogue for a variety of downstream tasks, including knowledge tracing, behavioral modeling, and diagnosis of student reasoning errors. However, the validity of these model-generated interpretations remains insufficiently understood. In this exploratory study, we examine the validity of LLM classifications of five student failure modes in mathematics tutoring dialogue using an operational diagnostic codebook: uncertainty, misattribution, operator selection, conceptual gap, and procedural slip. Across models, human-LLM agreement was moderate (kappa = .524-.597), while cross-model agreement was substantially higher (kappa = .755-.781; alpha = .769). These findings show that cross-model agreement can create a misleading appearance of correctness, challenging the assumption that consensus among LLMs constitutes evidence of valid learner interpretation. For learning analytics, the implication is clear: scalable labeling is useful only if the inferred constructs are valid, and model consensus cannot substitute for independent evidence of that validity.

### 🤖 AI 总结

**一句话总结**：In K-12 mathematics tutoring, student-tutor dialogue provides rich evidence of learners' problem-solving processes and sources of difficulty. Learning analytics research increasingly relies on large l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agreement, Not, Validity, Cross-Model, Consensus, Diagnosing, Student

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08703v1) | [下载PDF](https://arxiv.org/pdf/2610.08703v1.pdf)

---

## [11. Same-Number Citation Swaps: Stress-Testing Jev as a Financial Evidence Judge](https://arxiv.org/abs/2610.08675v1)

**作者**：Chuhong Xu, Bo Su, Ziyao Chen 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

Financial reports repeat values across periods, metrics and accounting lines, allowing an LLM-generated calculation to be numerically correct while citing the wrong financial role. We evaluate what probabilistic evidence verification adds beyond number matching using Jev as a source-support verifier for GPT-4.1-mini calculation traces. A signed-number-at-pointer baseline explains most recovery over exact quotation checks. To isolate the remaining role-recognition problem, we hold operands and arithmetic fixed, move citations between same-number cells, and retain controls that express equivalent facts. These contrasts reveal both wrong-role citations that pass and valid alternative citations that are withheld. Explicit column labels improve selected wrong-role decisions while also lowering support for some equivalent evidence. A constructed follow-up on 36 new source pages, labeled by a non-author reviewer, extends this evaluation and exposes the same tradeoff between detecting role errors and retaining valid citations. The contribution is a controlled evaluation that identifies what a probabilistic financial verifier distinguishes when numerical matching is held fixed. For LLM-based financial assistants, it makes numerical correctness, cited-role support and acceptance outcomes separately assessable.

### 🤖 AI 总结

**一句话总结**：Financial reports repeat values across periods, metrics and accounting lines, allowing an LLM-generated calculation to be numerically correct while citing the wrong financial role. We evaluate what pr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Same-Number, Citation, Swaps, Stress-Testing, Jev, Financial, Evidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08675v1) | [下载PDF](https://arxiv.org/pdf/2610.08675v1.pdf)

---

## cs.CV

## [12. World Models' Last Exam in Physics](https://arxiv.org/abs/2610.08791v1)

**作者**：Mingju Gao, Qingle Liu, Yuzhao Peng 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks spanning mechanics, optics, fluids, thermal and phase-change phenomena, electromagnetism, and surface tension. Each task pairs an initial image and a generation prompt with predefined physical criteria, enabling interpretable tests of observable physical relationships without requiring reference videos. Its evaluator combines task-observability screening with task-specific quantitative physical measurements. Experiments on eight video generation models across 1,280 videos reveal persistent physical inconsistencies and substantial variation across tasks, with the best model achieving an overall score of 57.76 out of 100. Evaluation on synthetic videos with known physical relationships provides evidence for the validity of the measurement module under controlled conditions. The evaluator also achieves higher agreement with human judgments than a direct vision-language model baseline in both within-task rankings and pairwise comparisons. By combining coverage across physical domains with scores grounded in measurable evidence and explicit measurement limitations, the benchmark provides an interpretable basis for diagnosing physical inconsistencies and tracking progress toward physically consistent video world models.

### 🤖 AI 总结

**一句话总结**：Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluati...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：World, Models', Last, Exam, Physics, Video, models, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08791v1) | [下载PDF](https://arxiv.org/pdf/2610.08791v1.pdf)

---

## [13. Building Rome from a Single Image](https://arxiv.org/abs/2610.08790v1)

**作者**：Jiraphon Yenphraphai, Fang Li, Tianshuo Xu 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that redesigns such an object-centric generator, e.g., Trellis 2, to work on both indoor and outdoor scenes while retaining its prior. We accomplish this by (a) partitioning the scene into adaptive chunks that scale relative to the distance to the camera; nearby chunks have a smaller size to keep the finer detail, while distant structures, e.g., buildings, are covered by large chunks; (b) making the generator capture explicit 2D-3D correspondence by lifting image features and making the model aware of the free space, observed surface, and unobserved region; (c) synthesizing around 4,000 outdoor scenes to broaden the training data, as existing scene datasets are largely indoor. Experiments on Tanks and Temples, ScanNet++, and in-the-wild images show that our method outperforms all baselines in geometric accuracy and perceptual quality across both indoor and outdoor scenes.

### 🤖 AI 总结

**一句话总结**：Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Building, Rome, Single, Image, Single-image, scene, generation, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08790v1) | [下载PDF](https://arxiv.org/pdf/2610.08790v1.pdf)

---

## [14. 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction](https://arxiv.org/abs/2610.08782v1)

**作者**：Shiqi Li, Sean Cho, Yijie Li 等 6 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-10-06

### 📄 论文摘要

Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-object states toward an interaction manifold, allowing the model to correct errors in translation, rotation, and alignment in a feed-forward manner. A key advantage of our generative formulation is that it naturally enables test-time guidance within the transport process. Rather than applying a separate post-hoc optimization after reconstruction, we directly steer the evolving generative states using physical interaction constraints and observed 2D evidence, allowing the reconstruction to be refined as part of the generative process itself. By training the generative model on diverse datasets, 4D-HOF generalizes robustly to challenging in-the-wild scenarios. Experiments on out-of-domain benchmarks show that 4D-HOF achieves state-of-the-art performance, producing more stable and accurate 4D hand-object reconstructions.

### 🤖 AI 总结

**一句话总结**：Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, 4D-HOF, Hand-Object, Flow, Matching, Feed-Forward, Interaction, Reconstruction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08782v1) | [下载PDF](https://arxiv.org/pdf/2610.08782v1.pdf)

---

## [15. ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing](https://arxiv.org/abs/2610.08779v1)

**作者**：Zhenghong Zhou, Zhe Lin, Jiebo Luo 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs in the target object's presence while preserving the surrounding action, teaching editors coordinated object behavior and source preservation. We further train a vision-language model (VLM) to predict interaction guidance from the same inputs. We introduce the ALIVE-interaction benchmark to assess interaction fidelity, source preservation, and visual coherence using a unified VLM-based protocol, and evaluate on the general video object insertion benchmark. Without VLM guidance, ALIVE improves Overall over the strongest evaluated baseline by 43.9% and 4.4% on the two benchmarks, respectively. VLM-predicted guidance further improves the ALIVE-interaction score by 0.95 points without additional user inputs.

### 🤖 AI 总结

**一句话总结**：Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ALIVE, Interaction-Aligned, Object, Insertion, First-Frame-Guided, Video, Editing, Current

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08779v1) | [下载PDF](https://arxiv.org/pdf/2610.08779v1.pdf)

---

## [16. Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap](https://arxiv.org/abs/2610.08770v1)

**作者**：Mohammed Q. Alkhatib  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Patch-based learning improves hyperspectral image (HSI) classification by exploiting local spectral-spatial information, but random train-test sampling from the same image can cause spatial patch overlap, leading to data leakage and optimistic performance estimates. This paper investigates same-class train-test spatial overlap in patch-based HSI classification using two measures: overlap percentage (OP), which quantifies the global amount of overlapped testing patch pixels, and average overlap ratio (AOR), which measures the local severity among affected testing patches. Experiments on the Pavia University dataset compare random and non-random spatial sampling using SVM, MLP, 2D-CNN, 3D-CNN, ViT, and MorpMamba. The results show that deep patch-based models achieve high accuracy under random sampling, with 3D-CNN reaching 96.17% Overall Accuracy (OA), but drop substantially under non-random spatial sampling, where 3D-CNN decreases to 55.20% and ViT and 2D-CNN drop by 40.71 and 38.81 percentage points (PP), respectively. Patch-size analysis further shows that increasing the patch size from 5x5 to 19x19 raises the random-sampling overlap percentage from 23.28% to 77.02%. These findings demonstrate that random patch-based evaluation can substantially inflate classification performance, especially for models that strongly exploit spatial context. The code associated with this paper is available at: https://github.com/mqalkhatib/Data_Leakage_in_HSI_Classification.

### 🤖 AI 总结

**一句话总结**：Patch-based learning improves hyperspectral image (HSI) classification by exploiting local spectral-spatial information, but random train-test sampling from the same image can cause spatial patch over...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data, Leakage, Patch-Based, Hyperspectral, Image, Classification, Quantifying, Impact

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08770v1) | [下载PDF](https://arxiv.org/pdf/2610.08770v1.pdf)

---

## [17. Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error](https://arxiv.org/abs/2610.08756v1)

**作者**：Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combines the information coming from all the views. Target and non-target evidence are accumulated simultaneously, weighted by the visibility of each Gaussian in each view. After that, the Gaussians are filtered with two thresholds: a main threshold $β$ selects the high-confidence seeds, and a lower one $γβ$ adds the connected components around them. For the evaluation, the labels are transferred from the Gaussians to the mesh vertices that are both visible and annotated. With this design, we can separate three sources of error: the 2D detector, the lifting and the transfer between representations. The thresholds and the transfer operator are chosen on seven Replica validation scenes, and the method is evaluated on ten held-out ScanNet++ scenes with the same values for every scene and class. The mean mIoU on the validation scenes was 0.93 with masks from the dataset annotations and 0.65 with YOLO masks, and on the ScanNet++ test scenes it was 0.80 and 0.54. Compared with thresholding the evidence per view, as a previous version of the method did, the fraction improves the test mIoU by 0.24 and makes it possible to use a single threshold for all the classes and scenes of both datasets. Finally, the error analysis shows that most of the remaining error comes from the detector.

### 🤖 AI 总结

**一句话总结**：The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confid...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Post-Training, Semantic, Lifting, Gaussian, Splatting, Separating, Detector

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08756v1) | [下载PDF](https://arxiv.org/pdf/2610.08756v1.pdf)

---

## [18. Co-Evolving Paths and Flows via Path-Flow Alignment](https://arxiv.org/abs/2610.08717v1)

**作者**：Zeyu Michael Li, William Xingxu Chen, Xiang Cheng  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

We study path-flow alignment as a unified training objective for flow matching. Instead of fixing the interpolation path and learning only the velocity field, we jointly train an endpoint-preserving path network and a flow network using the same alignment loss: the flow learns to match the path velocity, and the path learns to align its velocity to the current flow. Although every fixed learned path defines a valid flow-matching objective, the alignment loss alone is not a reliable criterion for path learning. We identify path overfitting, a failure mode in which the alignment loss decreases while sample quality worsens. We find that this failure is associated with low-entropy bottlenecks in the induced probability path, where the learned path routes samples through overly concentrated intermediate marginals. Motivated by this diagnosis, we introduce a stochastic path regularizer that hides part of the source information from the path network while preserving exact endpoints. The resulting regularization gives an explicit entropy floor for the stochastic training-path marginals and empirically suppresses the bottleneck in the learned sampler, making joint path-flow training effective. On ImageNet-256x256 with SiT backbones, our method consistently improves FID across model scales, extends to model-guidance training, and leaves the inference-time architecture and sampler unchanged. Code is available at https://github.com/lizeyu090312/traj_opt_paper

### 🤖 AI 总结

**一句话总结**：We study path-flow alignment as a unified training objective for flow matching. Instead of fixing the interpolation path and learning only the velocity field, we jointly train an endpoint-preserving p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Co-Evolving, Paths, Flows, via, Path-Flow, Alignment, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08717v1) | [下载PDF](https://arxiv.org/pdf/2610.08717v1.pdf)

---

## [19. RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins](https://arxiv.org/abs/2610.08684v1)

**作者**：Dicong Qiu, Zhiyuan Xu, Yaosheng Liu 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Modern video models can generate realistic videos from real appearance references and proxy renders that specify scene structure, viewpoint changes, and motion. Evaluating this render-to-real capability requires a real target video depicting the same scene evolution, paired with an editable, geometrically registered 3D replica. Such data has traditionally required substantial manual modeling, calibration, and animation effort. We introduce RenderBench, a benchmark of 12 reconstructed real-world scenes spanning large-scale indoor environments and egocentric viewpoints, with both static and dynamic settings. Our construction pipeline combines visual geometry, neural reconstruction, and assisted 3D authoring. Each scene is decomposed into static objects and dynamic actors, registered to the capture cameras, and accepted only after multi-view geometric and temporal validation. Each evaluation unit contains appearance reference images, a held-out real target video, an editable digital twin, a matched proxy render, and renderer-native scene annotations. We evaluate transfer models against paired real target videos, retain PAI-Bench-C-compatible structural projections, and use scene annotations to localize failures by object, visibility, articulation, and motion. The first release retains 12 of 14 registered samples (85.7%), comprising 1,496 paired real-proxy frames. All released scenes pass file-integrity and environment-edit audits, while proxy diagnostics yield a depth si-RMSE of 0.2170 and instance mIoU of 0.3673. RenderBench provides paired real observations and editable scene state for assessing both appearance fidelity and preservation of geometry and dynamics.

### 🤖 AI 总结

**一句话总结**：Modern video models can generate realistic videos from real appearance references and proxy renders that specify scene structure, viewpoint changes, and motion. Evaluating this render-to-real capabili...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RenderBench, Benchmarking, Render-to-Real, Video, Transfer, Reconstructed, Digital, Twins

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08684v1) | [下载PDF](https://arxiv.org/pdf/2610.08684v1.pdf)

---

## [20. EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding](https://arxiv.org/abs/2610.08674v1)

**作者**：Yuhao Qin, Junbo Wang, Yuke Li 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-06

### 📄 论文摘要

Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal dependencies across events. Although retrieval-augmented approaches have been introduced to provide additional context, most of them operate at the frame or snippet level, which limits their ability to model how events evolve over time and relate to each other. In this paper, we propose Event Chain Retrieval-Augmented Generation (EC-RAG), a training-free framework that organizes video content into an explicit event chain before question answering. Instead of retrieving isolated frames or text segments, EC-RAG first partitions the video into semantically coherent segments, represents each segment using multi-modal signals, and then links them into a structured chain that preserves temporal order and captures inter-event relationships. Given a query, the system identifies relevant events within this chain and gathers supporting evidence from the associated modalities. Our approach offers several practical advantages: (i) event-level abstraction that better reflects how video content is naturally structured, enabling more reliable localization compared to frame-level retrieval; (ii) structured multi-modal fusion that aggregates speech, text, and visual cues at the event level, allowing complementary information to be more effectively utilized during reasoning; and (iii) plug-and-play compatibility with existing LVLM backbones, requiring no additional training or reliance on proprietary models. Experiments on Video-MME, MLVU, and LongVideoBench show that this event-centric design consistently outperforms frame-level retrieval baselines, highlighting the importance of modeling temporal structure for long-video understanding.

### 🤖 AI 总结

**一句话总结**：Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal depend...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EC-RAG, Event, Chain, Retrieval-Augmented, Generation, Long, Video, Understanding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08674v1) | [下载PDF](https://arxiv.org/pdf/2610.08674v1.pdf)

---

## [21. PDB: Point-Based Deformation Blending for Facial Animation Retargeting](https://arxiv.org/abs/2610.08672v1)

**作者**：Sihun Cha, Hyeonseung Shin, Suah Yu 等 4 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-10-06

### 📄 论文摘要

Mesh-agnostic facial animation retargeting transfers expressions across meshes with different structures, but preserving facial motion without surface artifacts remains challenging. To address this, we present PDB, Point-Based Deformation Blending for facial animation retargeting. PDB predicts a compact set of deformed control points from a source neutral-expression pair and blending weights from the target neutral mesh. The weights are computed once per target and reused across frames, while the control points vary with each source expression. ReLU enforces non-negative weights and permits exact zeros, followed by row-wise normalization. The target mesh is reconstructed directly by multiplying the weights and control points, without a predefined cage, precomputed coordinates, a learned per-element deformation decoder, or a global reconstruction solve. Trained only with self-retargeting reconstruction supervision, PDB supports cross-identity transfer without paired cross-identity training expressions. Experiments demonstrate accurate retargeting, fast inference, and localized support in the learned weights. Joint evaluation of expression accuracy and local surface preservation shows reduced surface artifacts relative to the evaluated dense displacement method while retaining the intended motion. Perceptual evaluations further support expression fidelity and visual quality in both self- and cross-retargeting.

### 🤖 AI 总结

**一句话总结**：Mesh-agnostic facial animation retargeting transfers expressions across meshes with different structures, but preserving facial motion without surface artifacts remains challenging. To address this, w...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PDB, Point-Based, Deformation, Blending, Facial, Animation, Retargeting, Mesh-agnostic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08672v1) | [下载PDF](https://arxiv.org/pdf/2610.08672v1.pdf)

---

## cs.LG

## [22. Conformal Prediction Sets Quantify Information Gain: A Theoretical Perspective](https://arxiv.org/abs/2610.08785v1)

**作者**：Kevin Zhang, Stephen Bates  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Conformal prediction is a popular tool for uncertainty quantification that outputs prediction sets with finite-sample coverage guarantees. While prediction set size is commonly used as a heuristic measure of uncertainty, the information-theoretic basis for this interpretation remains poorly understood. In this work, we provide such a foundation using a decision-theoretic generalization of entropy tailored to set-valued prediction. In particular, we introduce a family of generalized information measures based on the size and coverage of conformal prediction sets. Notably, Shannon mutual information admits an exact integral representation in terms of these measures. We then show that, in standard classification settings, the reduction in conformal set size from additional information (i) is sandwiched between calibration-dependent members of this family and (ii) obeys a data processing inequality, both up to finite-sample calibration and model error terms. Together, our results formally relate conformal prediction to classical information-theoretic quantities and justify using set-size reduction as an information gain metric. Empirically, we validate our theory across 11 classification settings and show that set-size reduction and Shannon mutual information can rank features differently in a greedy feature selection experiment.

### 🤖 AI 总结

**一句话总结**：Conformal prediction is a popular tool for uncertainty quantification that outputs prediction sets with finite-sample coverage guarantees. While prediction set size is commonly used as a heuristic mea...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Conformal, Prediction, Sets, Quantify, Information, Gain, Theoretical, Perspective

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08785v1) | [下载PDF](https://arxiv.org/pdf/2610.08785v1.pdf)

---

## [23. Linear Bandits under Exact Sliding-Window Constraints](https://arxiv.org/abs/2610.08745v1)

**作者**：Seyed Mohammad Hadi Hosseini, Yasin Abbasi-Yadkori, Sattar Vakili  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

We study linear bandits under exact sliding-window constraints, where every consecutive block of actions must belong to a prescribed feasible set. In the offline setting, where the reward function is known, we show that convexity and cyclic-shift invariance make a stationary solution optimal when $w\mid T$ and within an additive $O(w)$ gap otherwise. In the online setting, we show that geometric structure alone is insufficient for learning, and sublinear regret can be impossible. We introduce a transition diameter $τ$ that quantifies feasible reachability and develop a rare-switching OFUL algorithm with regret $\widetilde{O}(d\sqrt{T}+τd+w)$ against the offline-optimal feasible trajectory. Finally, we remove cyclic invariance and consider general sliding-window constraints, where optimal behavior may be non-stationary. We represent recent action history as the state of a finite-memory control problem and introduce a history-state diameter $D$ that measures feasible communication between viable histories. Combining optimistic remaining-horizon planning with rare policy updates, we obtain a regret bound of $\widetilde{O}(d\sqrt{T}+dD+w)$. We evaluate our approach on real-world and synthetic benchmarks, showing that it maintains exact feasibility while achieving reward and regret comparable to baselines with substantially fewer policy updates.

### 🤖 AI 总结

**一句话总结**：We study linear bandits under exact sliding-window constraints, where every consecutive block of actions must belong to a prescribed feasible set. In the offline setting, where the reward function is ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Linear, Bandits, under, Exact, Sliding-Window, Constraints, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08745v1) | [下载PDF](https://arxiv.org/pdf/2610.08745v1.pdf)

---

## [24. Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation](https://arxiv.org/abs/2610.08743v1)

**作者**：Wenwen Si, Honghao Wei  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-10-06

### 📄 论文摘要

Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which adapts the retained action set using critic scores and an online threshold. The threshold is updated from binary feedback indicating whether the set contains an action in a proxy target. We prove a deterministic bound on the observed proxy miss rate along adaptive trajectories. To quantify the effect of pruning on reward, we derive an exact decomposition of value loss into filtering and selection losses. Under explicit proxy and critic approximation conditions, this decomposition yields a finite session reward bound that also accounts for imperfect selection and set truncation, without requiring the learning parameters to converge. Experiments on KuaiRand-Pure and MovieLens 1M compare two RLCP implementations with four RL baselines. In each of the 19 configurations, at least one RLCP variant achieves the highest catalog diversity, reaching $1.11\times$ to $5.21\times$ that of the strongest baseline, with competitive session depth and no larger retained sets.

### 🤖 AI 总结

**一句话总结**：Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Reinforcement, Learning, Conformal, Action, Sets, Application, Sequential

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08743v1) | [下载PDF](https://arxiv.org/pdf/2610.08743v1.pdf)

---

## [25. On the Computational Tractability of Robust Bandits](https://arxiv.org/abs/2610.08740v1)

**作者**：Vanessa Kosoy, Vinayak Pathak  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Learning when the environment does not belong to the learner's hypothesis class is typically handled using agnostic learning guarantees. However, for anything beyond supervised learning, agnostic guarantees are difficult to come by. Recently, imprecise bandits (Kosoy, 2025) (later renamed to robust bandits in Appel and Kosoy, 2025) were introduced as another approach to unrealizable learning in the bandits setting and a $Θ(\sqrt{T})$ regret learner was shown for a large class. However, no computational guarantees were provided. In this paper we identify a special case that admits a polynomial-time learner with $\tilde{O}(\sqrt{T})$ regret. We also show that several small generalizations of this special case are NP-hard thus indicating that the special case is at the boundary of what is tractable. It has been recently suggested (Kosoy, 2018) that computationally efficient learners for unrealizable learning problems are crucial for solving the AI alignment problem. This work is a small step in that direction.

### 🤖 AI 总结

**一句话总结**：Learning when the environment does not belong to the learner's hypothesis class is typically handled using agnostic learning guarantees. However, for anything beyond supervised learning, agnostic guar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Computational, Tractability, Robust, Bandits, Learning, when, environment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08740v1) | [下载PDF](https://arxiv.org/pdf/2610.08740v1.pdf)

---

## [26. Optimal and Efficient Online Inverse Optimization](https://arxiv.org/abs/2610.08735v1)

**作者**：Anupam Gupta, Guru Guruganesh, Honghao Lin 等 6 位作者  
**分类**：cs.LG, cs.DS  
**发布时间**：2026-10-06

### 📄 论文摘要

In online inverse linear optimization, a learner recommends an action and then observes the choice of an expert who maximizes a fixed, unknown linear objective on $\mathbb{R}^{d}$; the goal is to learn to optimize this objective without observing it. Sakaue recently obtained the optimal regret $O(\sqrt d)$ with a randomized algorithm making $(dT)^{O(d)}$ linear optimizations per round, and asked whether it can be attained in polynomial time. We answer positively: our deterministic algorithm has regret $O(\sqrt d)$ for every horizon $T$ and runs in time polynomial in $d$ and $T$. It is a variant of the variable-metric algorithms of Sakaue et al.\ and Cai et al., in which a metric update is revoked once the query point moves far enough from where the update was made.

### 🤖 AI 总结

**一句话总结**：In online inverse linear optimization, a learner recommends an action and then observes the choice of an expert who maximizes a fixed, unknown linear objective on $\mathbb{R}^{d}$; the goal is to lear...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Optimal, Efficient, Online, Inverse, Optimization, linear, learner, recommends

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08735v1) | [下载PDF](https://arxiv.org/pdf/2610.08735v1.pdf)

---

## [27. GeneICL: A Tabular Foundation Model for Bulk Transcriptomics](https://arxiv.org/abs/2610.08694v1)

**作者**：Michael Bohl, Alexander Theus, David Wissel 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Gene expression is widely measured in biomedicine, yet clinical outcome prediction remains challenging due to high dimensionality, strong feature correlations, and limited labeled data. Large self-supervised transcriptomic foundation models often fail to outperform simple supervised baselines. Tabular foundation models offer an alternative through in-context learning, but are typically pretrained on generic synthetic data rather than transcriptomic structure. We ask whether transcriptomics-aware pretraining, rather than scale, is the missing ingredient. Towards this end, we introduce GeneICL, a 4.2M-parameter tabular foundation model combining a semi-synthetic pretraining prior built from measured bulk expression profiles with a parameter-efficient recurrent architecture. We further enable right-censored survival prediction via a training-free reduction to regression using Cox partial-likelihood residuals. We evaluate GeneICL on 80 clinical outcome-prediction tasks spanning classification, regression, and survival. Tabular foundation models consistently outperform self-supervised transcriptomic models, while GeneICL achieves the best overall rank among evaluated foundation models and tuned baselines. GeneICL does so with up to 387$\times$ fewer parameters, no gradient updates at inference, and predictions within seconds on a laptop CPU.

### 🤖 AI 总结

**一句话总结**：Gene expression is widely measured in biomedicine, yet clinical outcome prediction remains challenging due to high dimensionality, strong feature correlations, and limited labeled data. Large self-sup...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：GeneICL, Tabular, Foundation, Model, Bulk, Transcriptomics, Gene, expression

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08694v1) | [下载PDF](https://arxiv.org/pdf/2610.08694v1.pdf)

---

## [28. Probabilistic Counterfactual Inference for Discrete Outcomes in Gaussian-Process Causal Models](https://arxiv.org/abs/2610.08689v1)

**作者**：Juliette Sinnott, Amir-Hossein Karimi, Mohammad Kohandel  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Counterfactual inference in Gaussian-process structural causal models (GP-SCMs) has been developed primarily for continuous endogenous variables, limiting applicability to causal graphs that contain discrete child nodes with continuous parents. We introduce a unified probabilistic framework for counterfactual inference with heterogeneous variable types by pairing GP predictors with explicit exogenous noise mechanisms. For discrete outcomes, we derive exact conditional noise-abduction procedures using a uniform threshold for binary variables, a Gumbel-max race for nominal categories, and a latent Gaussian cut-point model for ordinal ones. In each case, we propagate abducted noise through interventions while accounting for posterior uncertainty in the GP latent functions, and prove that the resulting mechanisms reproduce the fitted model's observational and interventional distributions. On synthetic SCMs with known ground-truth counterfactuals, we evaluate estimation accuracy, consistency, and robustness to coupling misspecification. A key finding is that applying a categorical coupling to ordinal data inflates counterfactual error roughly threefold even when observational fit remains comparable, and that this error does not diminish with more data. As the training set grows, the fitted structural equation converges to the truth while the counterfactual error flattens onto a floor. In the reverse direction, forcing a false order onto nominal data instead degrades the fitted equation itself. The choice of coupling must therefore be justified on structural grounds rather than read off the fit.

### 🤖 AI 总结

**一句话总结**：Counterfactual inference in Gaussian-process structural causal models (GP-SCMs) has been developed primarily for continuous endogenous variables, limiting applicability to causal graphs that contain d...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Probabilistic, Counterfactual, Inference, Discrete, Outcomes, Gaussian-Process, Causal, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08689v1) | [下载PDF](https://arxiv.org/pdf/2610.08689v1.pdf)

---

## [29. A Systematic Study of Small Language Models on Abstract Reasoning Tasks](https://arxiv.org/abs/2610.08680v1)

**作者**：Nur A Zarin Nishat, Jens Lehmann, Andrei Aioanei 等 4 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-10-06

### 📄 论文摘要

Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in small language models on the ARC-TGI benchmark, which organizes abstract grid transformations into controllable task families and supports resampling, spatial shifts, and cross-benchmark transfer. Across more than 1,000 runs, we profile decoder-only, encoder--decoder, and mixture-of-experts model families under supervised fine-tuning. We examine the efficiency and stability of skill acquisition, robustness beyond the training distribution, interactions with model family and task formulation, and layer-wise attention signatures that accompany behavioral differences. Substantial in-distribution accuracy is attainable, but acquisition is sensitive to optimization and unevenly distributed across task families. Performance deteriorates sharply outside the training distribution, including when the rule is retained but grid scale changes. Greater training-set depth and breadth yield uneven gains, while the effect of additional in-context examples depends on model family. Executable-rule induction also yields correct solutions not observed under direct grid generation. On selected tasks, attention diagnostics show distinct concentration and context-dependence profiles, but do not establish general causal mechanisms. Overall, abstract-reasoning scores are conditional on the model, adaptation regime, evaluation distribution, and response format.

### 🤖 AI 总结

**一句话总结**：Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in sma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Systematic, Study, Small, Language, Models, Reasoning, Tasks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08680v1) | [下载PDF](https://arxiv.org/pdf/2610.08680v1.pdf)

---

## [30. Variance-Optimal Off-Policy Evaluation with Conjunct Effect Modeling](https://arxiv.org/abs/2610.08677v1)

**作者**：Nicolò Felicioni, Michael Benigni, Maurizio Ferrari Dacrema 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-06

### 📄 论文摘要

Off-policy evaluation (OPE) for contextual bandit policies becomes challenging when action-level importance weighting incurs excessive variance. Doubly robust (DR) estimation remains unbiased under common support but retains these high-variance action-level weights. A prior estimator, Off-policy evaluation with Conjunct Effect Model (OffCEM), replaces them with more stable cluster-level weights, at the cost of relying on local correctness of the reward model. In this paper, we show that, under the assumptions required by DR and OffCEM, there exists an unbiased family of estimators that interpolates between OffCEM and DR. Building on this result, we propose the Variance Optimal-CEM (VOCEM) estimator, which selects the interpolation coefficient to minimize variance. We derive the population-optimal coefficient in closed form and show that the resulting estimator has variance no larger than either endpoint, OffCEM or DR. Experiments in controlled synthetic settings and on two large-action benchmarks show that VOCEM improves upon both endpoints in all 23 evaluated conditions, exhibiting greater stability and empirical robustness.

### 🤖 AI 总结

**一句话总结**：Off-policy evaluation (OPE) for contextual bandit policies becomes challenging when action-level importance weighting incurs excessive variance. Doubly robust (DR) estimation remains unbiased under co...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Variance-Optimal, Off-Policy, Evaluation, Conjunct, Effect, Modeling, OPE, contextual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.08677v1) | [下载PDF](https://arxiv.org/pdf/2610.08677v1.pdf)

---

