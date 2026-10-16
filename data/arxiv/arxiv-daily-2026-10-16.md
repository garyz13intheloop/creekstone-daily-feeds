# arXiv AI 论文日报 | 2026-10-16

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (12 篇)
- [cs.LG](#csLG) (5 篇)
- [cs.AI](#csAI) (7 篇)
- [cs.CL](#csCL) (6 篇)

---

## cs.AI

## [1. FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350v1)

**作者**：Dongxu Yang, Hongda Yan, Renxin Wang 等 26 位作者  
**分类**：cs.AI, cs.CL, cs.SE  
**发布时间**：2026-10-15

### 📄 论文摘要

Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engineers (FDEs) must clarify ambiguous requirements, work in live systems, and uncover unstated constraints. We introduce FDE-Gym, a benchmark of 95 end-to-end delivery tasks from 20 customer scenarios across 18 sectors, each adapted by industry experts from real-world delivery projects. In simulated customer environments with scripted stakeholders and modifiable customer systems, agents interact with stakeholders and operate on production-like systems to deliver working solutions. FDE-Gym scores a delivery by how much it improves the customer's own success metric, normalized between 0 (unchanged system) and 1 (reference solution), with penalties for stakeholder interactions (messages, trial runs, and waiting time). An online platform lets humans practice FDE skills under the same grading criteria. We evaluate 13 model configurations from seven providers. In the realistic setting, where unstated constraints must be discovered, the best configuration achieves a mean FDE-Gym score of 0.56 and resolves only 14 of the 95 tasks (a score of at least 0.8 with no incident). Discovering unstated constraints is the primary bottleneck: performance drops sharply when models must uncover them without explicit guidance. Yet information discovery alone does not account for the gap: even on the 23 tasks where the best configuration obtains every key fact from stakeholders, it reaches a normalized business uplift of 0.8 or above on only 10. These results reveal a substantial gap between solving well-specified tasks and delivering effective AI systems for real customers.

### 🤖 AI 总结

**一句话总结**：Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, FDE-Gym, Last, Mile, Delivery, Existing, benchmarks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22350v1) | [下载PDF](https://arxiv.org/pdf/2610.22350v1.pdf)

---

## [2. MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344v1)

**作者**：Shangheng Du, Jinxin Shi, Shuaiyu Zhang 等 10 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-10-15

### 📄 论文摘要

Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories and learn from intermediate outcomes. We propose a post-training method for autonomous long-horizon MLE optimization and apply it to train MLExpert, a 35B Mixture-of-Experts agentic model. We design the Kaggle-MLE Factory to construct executable tasks and an interaction harness for model-directed experimentation. Hierarchical agentic SFT transfers general tool-use and coding capabilities to MLE through outcome-guided supervision. Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. Asynchronous collection and policy correction support policy updates before the trajectory ends. On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. Further experiments show that MLExpert improves performance on NatureBench Lite, agent scaffold optimization, and algorithm optimization, suggesting that the learned optimization capability generalizes to other tasks.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MLExpert, Towards, Generalist, Agentic, Model, Autonomous, Machine, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22344v1) | [下载PDF](https://arxiv.org/pdf/2610.22344v1.pdf)

---

## [3. Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?](https://arxiv.org/abs/2610.22333v1)

**作者**：Trizal Garg, Sibayan Mitra, Arya Karanjkar 等 9 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use. Existing work has studied evaluation awareness almost entirely in English, although models serve users in many languages. Indic languages are spoken by over a billion people, yet evaluation awareness remains almost entirely unstudied in them. We test four instruction-tuned models from three families in five Indic languages alongside English. A set of cues varies whether the model is told that it is monitored and whether the monitoring is a safety test. Models refuse harmful requests more often when they are told that they are being tested. This increase appears in all four models and all six languages. In Indic languages, refusal of harmful requests rises by 14.4 percentage points on average. The test cue also brings Indic refusal of harmful requests level with English, but raises refusal of benign Indic requests from 6.9% to 11.3%. We release all 47,880 judged responses to support further work. These results suggest that safety evaluations in Indic languages may not reflect how models treat their everyday users.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can often tell when they are being tested. This ability, known as evaluation awareness, can lead models to act more cautiously during safety evaluations than in real use. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, Evaluation, Awareness, Beyond, English, Act, Differently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22333v1) | [下载PDF](https://arxiv.org/pdf/2610.22333v1.pdf)

---

## [4. KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents](https://arxiv.org/abs/2610.22331v1)

**作者**：Siqi Chen, Zhengxi Lu, Yuchen Yan 等 13 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unreliable in deep search where observations are heterogeneous and retrieved contexts are long and noisy. We propose KnowGPO, a reinforcement learning framework that aligns trajectories by the task-relevant knowledge they have acquired rather than by their surface observations. For each query, KnowGPO decomposes the information required to derive the answer into atomic knowledge conditions, and represents the state of a trajectory at each step by the subset of conditions it has satisfied. Trajectories sharing the same knowledge state are grouped for within-group comparison, and the incremental knowledge gain between consecutive steps serves as an environment-grounded process reward. Experiments on Xbench, BrowseComp-ZH, and GAIA show KnowGPO consistently outperforms outcome-only (GRPO) and process-supervision baselines (GiGPO, IGPO) by 3.8 to 4.2 points, with our 8B model rivaling or exceeding most 32B open-source systems.

### 🤖 AI 总结

**一句话总结**：Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinfo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, KnowGPO, Knowledge-Grouped, Policy, Optimization, Search, Deep, solve

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22331v1) | [下载PDF](https://arxiv.org/pdf/2610.22331v1.pdf)

---

## [5. Private Retrieval Augmented Generation via Random Projection](https://arxiv.org/abs/2610.22297v1)

**作者**：Dixi Yao, Tahseen Rabbani, Tian Li  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-10-15

### 📄 论文摘要

Retrieval-Augmented Generation (RAG) enhances the capabilities of large language models (LLMs) by querying external structured knowledge. However, it can also introduce privacy risks by leaking sensitive information from the retrieval datastore. We propose a simple method to preserve datastore privacy in RAG systems via random projection. By applying the same projection to both datastore embeddings and query embeddings, our method provably preserves semantic similarity between queries and retrieved items while substantially mitigating data extraction attacks. Across multiple RAG architectures and datasets, we show that this lightweight approach achieves superior retrieval and generation performance compared to prior methods which leverage formal differential privacy (DP) guarantees, while exhibiting comparable empirical privacy under strong attack models. Our results for the first time suggest that random projection can serve as a competitive and practical baseline for privacy-preserving RAG systems.

### 🤖 AI 总结

**一句话总结**：Retrieval-Augmented Generation (RAG) enhances the capabilities of large language models (LLMs) by querying external structured knowledge. However, it can also introduce privacy risks by leaking sensit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Private, Retrieval, Augmented, Generation, via, Random, Projection, Retrieval-Augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22297v1) | [下载PDF](https://arxiv.org/pdf/2610.22297v1.pdf)

---

## [6. EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity Search](https://arxiv.org/abs/2610.22290v1)

**作者**：Hanane Nour Moussa, Doeun Lee, Sachin Kumar  
**分类**：cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce. Several approaches have attempted to address this behavior-sharpening effect, but they often optimize metrics that do not reflect the diversity of correct solutions. Ideally, we want a model that can produce multiple good solutions, not only a single reliable one. We propose EliteReplay, a post-training recipe that pairs GRPO with an "elite" archive built by quality-diversity search. Before training, we use the frozen base model to collect solutions that span distinct approaches; during training, GRPO is combined with a replay loss on this archive. The result is a post-trained model that improves accuracy while preserving more of the base model's solution diversity. On multiple text-to-SQL tasks, EliteReplay achieves a higher pass@128 than all baselines, producing up to 77% more distinct correct strategies than the strongest baselines. It preserves most of the base model's correct strategies, outperforming existing methods in strategy retention. This diversity translates into practical benefits on ambiguous questions, where EliteReplay covers both interpretations nearly twice as often as the strongest baseline on AmbiQT.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning has become a common post-training technique to improve the accuracy of LLMs on verifiable tasks. However, such training can narrow the set of solutions the model can produce. Se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, EliteReplay, Preserving, Diverse, Solutions, Post-Training, via, Quality-Diversity

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22290v1) | [下载PDF](https://arxiv.org/pdf/2610.22290v1.pdf)

---

## [7. LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents](https://arxiv.org/abs/2610.22280v1)

**作者**：Qingni Wang, Changdae Oh, Yuzhe Yang 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. Weak-to-strong escalation offers a middle ground where a weak agent acts by default and hands control to a strong one only when needed. The core challenge is deciding when to escalate, which requires an uncertainty signal cheap enough to check at every step. However, even after handoff, the strong agent can still get lost, but a black-box API that the strong agent is usually served exposes no internals to monitor. To this end, we propose LEASH, a training-free framework that unleashes the strong agent only when the weak agent's latent uncertainty signals it is needed, and keeps it on a leash afterward. LEASH has three layers: (1) initial task uncertainty for early routing, (2) step-level uncertainty for runtime escalation, and, after handoff, (3) a shadow observer for continued oversight of the strong black-box agent. Here, we use latent uncertainty as a fuel for all three layers. Specifically, we compare the weak model's hidden states with those from its past successful and failed trajectories, and a state that looks more like the failures signals higher uncertainty. During weak-agent execution, our uncertainty estimator reuses activations already produced during action generation, so it needs no extra forward pass or dedicated monitor training. Experiments on OSWorld across four contemporary model backbones show that LEASH consistently improves over standalone weak agents and outperforms random escalation by 6.55--11.94 points at matched escalation rates. With Qwen3.5-35B-A3B, LEASH achieves 73.66% task success at $0.4117 per task, matching always-on Claude Opus 5 (72.90%) while reducing inference cost by 19.2%.

### 🤖 AI 总结

**一句话总结**：Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. Weak-to-strong escalation offers ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LEASH, Uncertainty-Aware, Weak-to-Strong, Escalation, Oversight, Computer-Use, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22280v1) | [下载PDF](https://arxiv.org/pdf/2610.22280v1.pdf)

---

## cs.CL

## [8. Training Reasoning Models to Generate Diverse Scientific Ideas](https://arxiv.org/abs/2610.22324v1)

**作者**：Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being grounded in the input documents. To optimize for this, we propose training with a set-level reinforcement learning objective. In our setup, in a single generation, the model writes K structured idea cards grounded in the source papers, and the set is scored jointly, where each idea's quality is weighted by its distance from the ideas written before it. This teaches the model to steer each new idea away from its predecessors. We show that our trained 8B model achieves higher creative utility (a measure combining quality and diversity) than Claude Opus 4.8 and GPT-6 Astra on our contamination-free benchmark. In a pilot human study with four experts, our sets are judged as promising as Claude Opus 4.8's and contain marginally more unique ideas. When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.

### 🤖 AI 总结

**一句话总结**：One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual i...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Training, Reasoning, Models, Generate, Diverse, Scientific, Ideas, One

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22324v1) | [下载PDF](https://arxiv.org/pdf/2610.22324v1.pdf)

---

## [9. MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support](https://arxiv.org/abs/2610.22314v1)

**作者**：John Mendonça, Daniel Tschernutter, José Pombal 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an LLM-as-a-judge. However, the usefulness of these methods is limited because simulated patients can be overly forthcoming and self-reflective, and judgments typically involve opaque Likert scales with unclear practical utility. To bridge these gaps, we introduce MindEval2, an evaluation framework that consists of two components: Mental Health Quality Rubrics (MHQR), for evaluation, and MindSim, for patient simulation. For MHQR, we collaborate with PhD-level psychologists to develop a set of rubrics that break down response quality into explicit operational criteria that are more interpretable and actionable than existing evaluation taxonomies. MindSim, in turn, is an LLM harness that combines carefully-designed patient profiles with tools, enabling more varied, challenging, and realistic interactions than existing baselines. The harness also contains a memory component that is updated between each interaction, enabling MindEval2 to model the longitudinal aspect of mental health. We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap.

### 🤖 AI 总结

**一句话总结**：With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MindEval2, Clinically, Grounded, Patients, Rubrics, Evaluating, Language, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22314v1) | [下载PDF](https://arxiv.org/pdf/2610.22314v1.pdf)

---

## [10. Grid-Bench: Can LLMs Predict How Discrete Worlds Change?](https://arxiv.org/abs/2610.22312v1)

**作者**：Zixiang Xu, Zirui Song, Wanrong Zheng 等 19 位作者  
**分类**：cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

Spatial instructions describe how to move objects, transform regions, or modify their surroundings. When several operations are applied in sequence, each acts on a configuration shaped by earlier changes. How accurately can large language models (LLMs) predict the resulting spatial state? We introduce Grid-Bench, an executable benchmark in which eight families of operations transform discrete worlds represented as two-, three-, and four-dimensional grids. Given an initial grid, explicit rules, and an event history expressed as text, a model predicts the complete final grid. Reference execution makes every predicted value checkable, supporting comparisons across spatial operations, history lengths, and workloads. Evaluating six LLMs shows that complete-state accuracy falls sharply as histories grow, with substantial divergence among models that perform similarly on single events. Models with similar exact-match accuracy can nevertheless differ substantially in the number of incorrect cells on shared instances. Even over long histories, some models recover many correct changes beyond what copying the initial state would yield. Grid-Bench makes both complete recovery and these differences in returned states directly measurable across a range of spatial conditions.

### 🤖 AI 总结

**一句话总结**：Spatial instructions describe how to move objects, transform regions, or modify their surroundings. When several operations are applied in sequence, each acts on a configuration shaped by earlier chan...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Grid-Bench, Can, Predict, How, Discrete, Worlds, Change?

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22312v1) | [下载PDF](https://arxiv.org/pdf/2610.22312v1.pdf)

---

## [11. Knowledge That Is Linear Before Fine-Tuning Generalizes After It](https://arxiv.org/abs/2610.22300v1)

**作者**：Faridoun Mehri, Hinrich Schütze  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-10-15

### 📄 论文摘要

Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recalled but do not support such generalization in a given task. We study this distinction by constructing new relations from existing ones. Take the relation that maps a place to its continent (Paris -> Europe) and assign each of its answers an arbitrary new label (Europe -> crab, Asia -> zebra). The new relation then maps Paris -> crab. We fine-tune the model on the new relation for a subset of subjects, without telling it the original relation or the relabeling rule, and test whether it assigns the corresponding labels to held-out subjects that share an answer in the original relation. Having learned Paris -> crab, does it answer Munich -> crab? Across eleven language models and 70 relations, how linearly readable the original relation is in pretrained representations strongly predicts this generalization. Within each model, the two correlate across relations at Pearson r = 0.87 to 0.92. This association persists when controlling, separately and jointly, for the number of fine-tuning subjects and answers, the model's accuracy on the original relation, and how often the subjects occur in pretraining text. It is also robust to re-randomizing the label assignment and fine-tuning seed, and to replacing the animal labels with labels from thirteen other semantic categories. When we map a fine-tuned model's wrong label back to the original answer it was assigned to, Munich -> zebra becomes Munich -> Asia. Answers recovered this way are more often among the linear probe's top answers for the subject than among the pretrained model's own. Whether a new relation generalizes depends less on whether its facts can be recalled than on how readily their shared structure can be read out linearly.

### 🤖 AI 总结

**一句话总结**：Not all facts a language model can recall support further learning equally well. We distinguish active facts, which support generalization beyond their own recall, from inert facts, which can be recal...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Knowledge, Linear, Before, Fine-Tuning, Generalizes, After, Not

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22300v1) | [下载PDF](https://arxiv.org/pdf/2610.22300v1.pdf)

---

## [12. AI Consilium: a Benchmark of LLM Clinical Multidisciplinary Second Opinions](https://arxiv.org/abs/2610.22298v1)

**作者**：Alexey A. Bokov, Ivan I. Panin, Nikolay B. Nechaev 等 13 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

Large language models (LLMs) can generate differential diagnoses for complex cases, but a useful second opinion must also be factually grounded, clinically coherent, actionable, and safe. We developed a multidimensional benchmark using 300 diagnostically resolved NEJM--MedQA cases: 110 for physician reference ratings and Judge calibration and 190 for held-out evaluation. Eight single-model pipelines generated independent role-specific opinions and interactive-consilium reports under free-form and structured clinical-reasoning conditions. A physician-calibrated LLM Judge evaluated 3,040 final reports and the corresponding structured primary-role outputs. Model identity separated report quality more strongly than response format. Structured final reports had higher overall mean scores in seven of eight model pipelines, with their clearest advantage in management (2.740 vs. 2.436). Compared with the structured pre-consilium primary-role opinion, the complete structured synthesis had higher pooled scores across all five shared criteria, with the largest increases in problem prioritization, factual grounding, and reasoning coherence. GPT-5.6-Sol led every evaluated component and reached consensus in the fewest review rounds. These findings show that the benchmark can distinguish model capability, the contribution of multidisciplinary synthesis, criterion-specific effects of response structure, deliberation dynamics, and inference requirements within one common-case evaluation.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) can generate differential diagnoses for complex cases, but a useful second opinion must also be factually grounded, clinically coherent, actionable, and safe. We developed...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Consilium, Benchmark, Clinical, Multidisciplinary, Second, Opinions

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22298v1) | [下载PDF](https://arxiv.org/pdf/2610.22298v1.pdf)

---

## [13. Multi-Target Few-Shot Prompting with Diffusion Language Models](https://arxiv.org/abs/2610.22294v1)

**作者**：Anton Xue, Alan Li, Rahul Saha  
**分类**：cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

Few-shot prompting is useful when instructions and rewards are hard to specify. One such application is editing by example, where a demonstrated formatting change or API migration may need to be applied across multiple sites. However, such edits often depend on both left and right context, making generation with causal autoregressive models awkward. We therefore introduce multi-target few-shot prompting with diffusion language models, where examples guide the infilling of multiple masked regions within a shared canvas. To address the known challenge of reliably following demonstrations in few-shot prompting, we further leverage selective masking of the canvas to derive a likelihood-ratio reward that favors example-supported infills. Across few-shot prompting benchmarks and software refactoring case studies, we find that demonstrations improve infilling accuracy, with example guidance yielding further gains in several settings.

### 🤖 AI 总结

**一句话总结**：Few-shot prompting is useful when instructions and rewards are hard to specify. One such application is editing by example, where a demonstrated formatting change or API migration may need to be appli...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Multi-Target, Few-Shot, Prompting, Language, Models, useful, when

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22294v1) | [下载PDF](https://arxiv.org/pdf/2610.22294v1.pdf)

---

## cs.CV

## [14. Gen4P: Video Generators are 4D Perceivers](https://arxiv.org/abs/2610.22371v1)

**作者**：Yitong Xia, Zeren Jiang, Chuanxia Zheng  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See https://gen4p.github.io for more visual results.

### 🤖 AI 总结

**一句话总结**：We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, We, Gen4P, Video, Generators, Perceivers, introduce, unified

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22371v1) | [下载PDF](https://arxiv.org/pdf/2610.22371v1.pdf)

---

## [15. SoftCache: Adaptive Step Size Caching for Diffusion Transformers](https://arxiv.org/abs/2610.22369v1)

**作者**：Shimon Malnick, Nadav Orenstein, Ohad Fried 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. Training-free caching accelerates them by reusing activations from recent evaluations instead of recomputing them. Dynamic caching methods decide when to refresh by accumulating a cheap probe of the network input into a staleness signal and spending a fresh evaluation once it crosses a threshold. They perform hard caching: the signal is a binary switch between refresh and reuse, and every step, fresh or cached, advances by the prescribed step size. We observe that the signal carries much more than this switch. How far it sits below the threshold, its headroom, predicts the error induced by reuse. We propose SoftCache, which performs soft caching: instead of a binary switch, the headroom sets how far each cached step goes. Where the headroom is large, the sampler jumps past several scheduled nodes, and as a refresh nears, its steps shrink back toward the original step. These adaptive jumps may land between the scheduled nodes, taking the sampler off its fixed grid. SoftCache requires no training and adds no per-backbone settings: on FLUX for images and on HunyuanVideo and Wan2.1 for video, at speedups from $3.5\times$ to $6.9\times$, it is ahead of every baseline on all four fidelity metrics.

### 🤖 AI 总结

**一句话总结**：Diffusion and flow models generate a sample over iterative steps, each a full pass through a large network, and that pass dominates generation cost. Training-free caching accelerates them by reusing a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, SoftCache, Adaptive, Step, Size, Caching, Transformers, flow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22369v1) | [下载PDF](https://arxiv.org/pdf/2610.22369v1.pdf)

---

## [16. Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)

**作者**：Zirui Wu, Chen Guo, Tianjian Jiang 等 14 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-10-15

### 📄 论文摘要

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D action representation into a pretrained video diffusion transformer through a mixture-of-transformers architecture with shared base weights, modality-specific adaptation, and bidirectional visual-action attention. Randomized modality visibility lets video and 3D actions serve as either conditioning context or prediction targets across the three modes. Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation. Through unified training, our model outperforms specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, while producing goal-directed manipulation videos with stronger instruction adherence and action progression than video-generation baselines. Project Page: https://p3-wam.pages.dev/

### 🤖 AI 总结

**一句话总结**：We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three compleme...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Perceive, Predict, Plan, Unified, World, Action, Model, Egocentric

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22363v1) | [下载PDF](https://arxiv.org/pdf/2610.22363v1.pdf)

---

## [17. Grounding Generative Verification in 3D Content](https://arxiv.org/abs/2610.22360v1)

**作者**：Shuanglin Li, Jiaying Lin, Shuquan Ye  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge. We argue that building reliable 3D systems requires not only stronger generation and reasoning, but also verification feedback that identifies unmet requirements and explains their violations, allowing systems to reflect on and refine their outputs. Such feedback must integrate multi-view observations and distinguish genuine inconsistencies from projection-dependent appearances. We make three contributions. First, we introduce 3DVerifierBench, a benchmark spanning 10 tasks that evaluates decisions, rejection explanations, and responses to controlled changes in specifications and candidates. A human study reveals a 21.6 percentage-point gap between humans and the strongest tested model, GPT-6 Astra, while explanation-aware analysis exposes weaknesses in rejection reliability. Second, we analyze verification across fine-grained factual categories, exposing errors in values and target binding. We develop a scalable pipeline combining multi-view fact extraction, controlled 3D editing, and native annotations to produce 14,126 training examples with contradiction explanations and linked counterfactuals. Third, we examine how verification could support 3D generation through candidate selection and recursive refinement. In human-labeled sixteen-candidate pools, oracle selection improves complete factual success from 26.7% to 90.0%. In a separate eight-input study, human-guided recursive refinement satisfies all seven requirements for every input, compared with three under parallel Oracle@8. Together, our benchmark, analysis, and data pipeline establish a foundation for models to reflect on 3D content through reliable verification feedback.

### 🤖 AI 总结

**一句话总结**：Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D ev...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Grounding, Generative, Verification, Content, Recent, advances, multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22360v1) | [下载PDF](https://arxiv.org/pdf/2610.22360v1.pdf)

---

## [18. SUPRA-TEX: 3D Generation with Super-Aligned Texture](https://arxiv.org/abs/2610.22352v1)

**作者**：Chen Yang, Jiemin Fang, Fanpeng Meng 等 8 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-10-15

### 📄 论文摘要

Single image 3D generation aims to dress a given 3D mesh with relightable materials while faithfully preserving the visual details of a reference image. Existing methods either introduce artifacts when fusing inconsistent multi-view predictions or struggle to preserve fine details through implicit image-feature conditioning. To resolve these challenges, we introduce SUPRA-Tex, built on the principle of decoupling visible-material estimation, surface alignment, and observation-guided 3D completion. This division of labor allows the 3D generator, trained on limited 3D data, to focus its capacity on preserving visible evidence and completing unobserved surfaces. Specifically, we first train an MLLM-based image editing model to predict lighting-separated PBR maps in the reference view. We then project these maps onto the visible surface and encode them with the pretrained material VAE encoder into native observation latents that share the generation target's latent space. An interleaved flow transformer holds these latents as fixed, read-only anchors while alternating unobserved-region and full-surface updates to generate complete material latents. This design achieves super-alignment with the reference, delivering What You See Is What You Get fidelity on visible regions and coherent completion on unobserved surfaces. Trained solely on public datasets, SUPRA-Tex achieves SOTA performance in both geometry-conditioned texturing and end-to-end asset generation, matching or even exceeding leading commercial systems on in-the-wild images. Project page: https://supra-3d.github.io/supratex/

### 🤖 AI 总结

**一句话总结**：Single image 3D generation aims to dress a given 3D mesh with relightable materials while faithfully preserving the visual details of a reference image. Existing methods either introduce artifacts whe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, SUPRA-TEX, Generation, Super-Aligned, Texture, Single, image, aims

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22352v1) | [下载PDF](https://arxiv.org/pdf/2610.22352v1.pdf)

---

## [19. 3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341v1)

**作者**：Yipeng Gao, Ziyao Zeng, Jinfa Huang 等 19 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and practical guidance for 3D coding. First, we construct 3DCodeVerse-2M, a large-scale curated dataset of standalone 3D executable code. We build this corpus by collecting open-source data, converting specialized representations, and generating new programs with coding agents. Each program is packaged with the source files and associated assets required for execution in its declared environment, along with available descriptions and verification records. Second, we develop the 3DCodeVerse Harness, a multi-agent directed acyclic graph framework for generating and refining 3D content. It uses execution checks, spatial measurements, and visual feedback to automatically evaluate and revise generated programs without human feedback during generation. Third, we conduct systematic empirical studies of 3D coding, establishing baselines with fine-tuned open models and deriving practical guidance through component-level analyses of our harness. Extensive experiments demonstrate that fine-tuning on our dataset significantly improves the 3D coding capabilities of open-source models. Notably, our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5.

### 🤖 AI 总结

**一句话总结**：We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, as, We, 3DCodeVerse, Exploring, Worlds, Code, introduce

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22341v1) | [下载PDF](https://arxiv.org/pdf/2610.22341v1.pdf)

---

## [20. ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning](https://arxiv.org/abs/2610.22328v1)

**作者**：Sara Dorfman, Nir Goren, Gal Barak 等 5 位作者  
**分类**：cs.CV, cs.AI, cs.GR  
**发布时间**：2026-10-15

### 📄 论文摘要

Image editing models produce impressive results for individual edits, but their quality often deteriorates over multiple editing turns. Each editing turn introduces small distribution shifts that accumulate over successive edits, creating a gap between the input distributions encountered during the editor's original training and multi-turn inference. We introduce a training scheme that makes multi-turn image editing stable under this accumulating distribution shift. A key is to force the editor to operate on its own outputs from previous editing turns during training, bringing the principle of Self-Forcing to image editing. The main challenge is that self-generated editing trajectories deviate from ground-truth trajectories, making direct supervision unreliable. We address this challenge through a distillation objective that leverages a teacher image editor to provide a reliable training signal when the model operates on its own previous outputs. We introduce an asymmetric conditioning scheme: while the student performs edits sequentially on its own outputs, the teacher remains anchored to the original clean image and receives a compound editing instruction. Experiments show substantially reduced degradation over long multi-turn sequences while maintaining editing quality and instruction adherence.

### 🤖 AI 总结

**一句话总结**：Image editing models produce impressive results for individual edits, but their quality often deteriorates over multiple editing turns. Each editing turn introduces small distribution shifts that accu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ACEdit, Stable, Multi-Turn, Image, Editing, via, Asymmetric, Conditioning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22328v1) | [下载PDF](https://arxiv.org/pdf/2610.22328v1.pdf)

---

## [21. Dense4D: Pixel-Level 4D Human Correspondence](https://arxiv.org/abs/2610.22325v1)

**作者**：Rıza Alp Güler  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Reconstructing human motion in 4D requires identifying the same surface points through articulation, deformation and changes in visibility. We introduce Dense4D, to our knowledge the first feed-forward model dedicated to dense 4D correspondence across the body, clothing and hair from a set of monocular RGB images, without a body template. Trained specifically for human geometry, Dense4D jointly processes person-centred crops with known image-to-crop transforms to predict Human Point Maps (HPMs) and depth for each image. An HPM assigns each person pixel the 3D position of its observed surface point at a common reference time. These maps support amodal correspondence: points hidden in the reference image can be localised from observations in other frames. Matching HPM coordinates across crops establishes correspondence without predicting camera poses or large scene displacements; per-image depth then lifts the matches into 3D tracks. Experiments on real people demonstrate substantially higher tracking accuracy and closer agreement with scanned surfaces than the evaluated baselines. Points from different frames assemble into coherent human geometry in the reference pose, providing visible evidence of consistent dense correspondence through articulation and clothing deformation. Additional qualitative results, videos, and an interactive viewer are available at https://alpguler.com/dense4d.

### 🤖 AI 总结

**一句话总结**：Reconstructing human motion in 4D requires identifying the same surface points through articulation, deformation and changes in visibility. We introduce Dense4D, to our knowledge the first feed-forwar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：4D, Dense4D, Pixel-Level, Human, Correspondence, Reconstructing, motion, requires

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22325v1) | [下载PDF](https://arxiv.org/pdf/2610.22325v1.pdf)

---

## [22. AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321v1)

**作者**：Yuruo Wu, Kaihang Pan, Kai Shen 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-10-15

### 📄 论文摘要

As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetric cross-modal relations. However, current evaluations largely reuse metrics from earlier simple and unidirectional tasks. They typically evaluate an audio-video clip as a whole and rely on simple predefined relations, making them unsuitable for these increasingly complex scenes. We propose an event-centric evaluation framework that disentangles audio and visual events at the event level, analyzes each event independently, cross-validates relations across modalities, and aggregates the judgments into a coarse-to-fine, three-level consistency metric. The metric assesses global narrative harmony, event-level temporal synchronization, and fine-grained attribute alignment, providing a general formulation for audio-video consistency evaluation across diverse generation settings and cross-modal relations. We instantiate the metric as AVC-Reward, a trainable audio-video reward model. To evaluate the agreement between automatic judgments and human perception across generation paradigms and relation complexities, we construct AVC-Benchmark, which is primarily built from diverse positive and negative samples generated by various types of audio-video generation models. AVC-Reward achieves state-of-the-art alignment with human judgment among automatic methods, provides interpretable rationales that localize failures, and improves the audio-video consistency of a joint generation model when used as an online reinforcement-learning signal. Project page: https://tsuki0512.github.io/AVC-Reward.github.io/

### 🤖 AI 总结

**一句话总结**：As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, AVC-Reward, Event-Centric, Audio-Video, Consistency, Evaluation, joint, generation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22321v1) | [下载PDF](https://arxiv.org/pdf/2610.22321v1.pdf)

---

## [23. ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models](https://arxiv.org/abs/2610.22306v1)

**作者**：Girish Kumar Adari  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Multi-object tracking in sports broadcasts is hard for two reasons: athletes move fast and change direction abruptly, and the camera pans and zooms at the same time. We present ARC-SORT (Adaptive, Robust, Compensated SORT), a tracking-by-detection tracker that trains nothing and runs in real time. Its design rule: the tracker measures its own uncertainty, and that measurement decides how it acts. An Interacting Multiple Model (IMM) Kalman filter gives every track a predictive covariance, and we turn it into a per-track search region: the less reliable the motion prediction, the larger the region in which a detection may match (uncertainty-adaptive Expansion IoU, EIoU). On identical inputs, this continuous coupling is what matters: the same covariance used as a hard Mahalanobis gate hurts at every threshold we swept, and richer covariance summaries add nothing measurable. When two tracks cross, the assignment cost itself reports whether the decision was close. ARC-SORT keeps such pairs under review and applies at most one corrective identity swap once post-crossing appearance evidence shows the first decision was wrong; this adds +1.0 HOTA (higher order tracking accuracy) on both the SportsMOT and DanceTrack test sets at under a millisecond per frame. For players who leave the frame for seconds, motion extrapolation carries no information, so our offline re-identification drops the usual motion gate and links tracklets by appearance alone. ARC-SORT reaches 81.82 HOTA on the SportsMOT test set with the fewest identity switches of the 69 leaderboard entries as of August 2026 and tied-third multi-object tracking accuracy (MOTA, 97.09), and 62.1 HOTA on DanceTrack test with the same association settings. On Deep-EIoU's public detections and embeddings it reaches 80.31 HOTA, +3.1 over Deep-EIoU. It runs at about 50 frames per second on a laptop RTX 3060 GPU. Code will be released.

### 🤖 AI 总结

**一句话总结**：Multi-object tracking in sports broadcasts is hard for two reasons: athletes move fast and change direction abruptly, and the camera pans and zooms at the same time. We present ARC-SORT (Adaptive, Rob...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：ARC-SORT, Adaptive, Robust, Compensated, Multi-Object, Tracking, Interacting, Multiple

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22306v1) | [下载PDF](https://arxiv.org/pdf/2610.22306v1.pdf)

---

## [24. Grounded Human-Attributed Description and Activity Recognition in Videos](https://arxiv.org/abs/2610.22295v1)

**作者**：Jay N. Paranjape, Jurijs Nazarovs, Rohan Sarkar 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Understanding characteristics and activities of individuals in complex multi-person environments is crucial for real-world applications. However, existing datasets often simplify this problem to grounded group activity recognition, single-person activity recognition, or close-set activity recognition, thus limiting the generalizability of models trained on these datasets. In this work, we introduce the task of Grounded Human-Attributed Description and Activity Recognition (GHADAR), which involves describing the characteristics and activity descriptions of \textbf{every} person in a video, provided the location of the person in the video, which is more practical for real-world applications. To facilitate this, we introduce a new dataset derived from AVA-Actions by generating open-set captions for the person description and activity. In addition, we propose a novel method to effectively utilize the information contained in grounding during training by constraining the cross-attention masks during training in VLMs to improve performance for this task. Our experiments show that our method outperforms SOTA VLMs on this task. Finally, we demonstrate the limitations of existing evaluation metrics, which are overly reliant on human-annotations and exact text-text matching. As an added video-based evaluation, we propose a holistic VLM-based evaluation schema that compares concepts {\em directly} between the video and the generated predictions. Thus, in this work, we develop a complete framework for GHADAR, including a dataset, a novel method and an evaluation schema, thereby establishing a strong foundation for future research in this domain.

### 🤖 AI 总结

**一句话总结**：Understanding characteristics and activities of individuals in complex multi-person environments is crucial for real-world applications. However, existing datasets often simplify this problem to groun...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Grounded, Human-Attributed, Activity, Recognition, Videos, Understanding, characteristics, activities

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22295v1) | [下载PDF](https://arxiv.org/pdf/2610.22295v1.pdf)

---

## [25. Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282v1)

**作者**：Qiuhong Shen, Yiding Yang, Yuxin Zhang 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-10-15

### 📄 论文摘要

Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reverse denoising trajectory, leading to costly rollout-based optimization. We instead ask whether stochastic exploration can be introduced inside the generator while preserving its original sampler. Routing Policy Optimization (RPO) answers this question by turning attention routing into a stochastic exploration action. At a few selected denoising levels, each query block keeps its own block and samples further key blocks in proportion to the generator's native attention mass, or keeps dense attention. The sampled route perturbs the velocity of that transition, and a Gaussian likelihood around the dense velocity scores the perturbation with a score-function objective. RPO further uses a controlled two-rollout estimator: two rollouts share the same prompt, initial latent, routed denoising levels, and dense anchor layers, differing only in their sampled attention routes. Their reward difference provides an advantage signal for the routed transitions. Because the likelihood differentiates the dense velocity itself, the learned updates remain effective after routing is removed. At inference, RPO restores dense attention and retains the original deterministic sampler. Experiments on text-to-image and text-to-video generation show that RPO improves generation quality while achieving nearly 4x higher training efficiency than Flow-GRPO-style methods. Please see our project page at https://velox-world.com/rpo for visual results.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reve...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Routing, Policy, Optimization, Online, Reinforcement, Learning, can

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22282v1) | [下载PDF](https://arxiv.org/pdf/2610.22282v1.pdf)

---

## cs.LG

## [26. PathFM: Fast Generative Forecasting of Multivariate Trajectories](https://arxiv.org/abs/2610.22358v1)

**作者**：Jiachen Yao, Xiyuan Zhang, Annan Yu 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-15

### 📄 论文摘要

Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified. This distinction matters for trajectory-dependent quantities such as cumulative demand, peak load, and event timing, yet point and marginal scores do not reveal it. To model this dependence, we introduce PathFM, a trajectory-based forecasting model that uses flow matching to generate complete future paths. We further distill the model to one or two steps and share history attention cache across draws. Together, these enable PathFM to generate multiple paths for a single series in roughly the time needed for one query to a quantile model. The distilled sampler also makes it practical to optimize a calibration loss directly. PathFM achieves competitive marginal accuracy on the established forecasting benchmarks fev-bench and TIME. To complement these evaluations, we introduce Forecast Path Score Bench (fps-bench), which augments fev-bench tasks with energy and variogram scores and downstream metrics. PathFM achieves a higher aggregate path score on fps-bench than all evaluated external baselines. Experiments on chaotic systems further show that our flow model sustains long-run variability, while strong baselines rapidly collapse. PathFM makes generative time series forecasting both competitive and practical, enabling diverse downstream applications.

### 🤖 AI 总结

**一句话总结**：Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future tra...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PathFM, Fast, Generative, Forecasting, Multivariate, Trajectories, Time

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22358v1) | [下载PDF](https://arxiv.org/pdf/2610.22358v1.pdf)

---

## [27. Lean Graph Search for Formal Theorem Proving](https://arxiv.org/abs/2610.22339v1)

**作者**：Yihan Xu, Jia-Chen Gu, Junyi Zhang 等 10 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-15

### 📄 论文摘要

Retrieving relevant lemmas is crucial for formal theorem proving, enabling provers to build machine-checkable proofs from established mathematical results. Recent retrieval systems match library declarations to a target theorem or its intermediate proof steps, but make limited use of multi-hop dependencies among declarations. These dependencies can reveal supporting lemmas that are not necessarily lexically similar to the target theorem but recur in proofs of related problems. To this end, we propose LeanGraphSearch, a graph-based retrieval method for Lean 4 that constructs a graph from Mathlib's forward dependencies and traverses it to uncover supporting lemmas through multi-hop dependency chains. Specifically, LeanGraphSearch links each declaration to the premises it depends on, uses a graph-based ranking algorithm to propagate relevance from semantically matched declarations to their dependencies, and reranks the expanded candidates against the original query. Across two mathematical retrieval benchmarks, LeanGraphSearch improves recall by up to 12% over the strongest baseline, LeanSearch v2, on MathlibQR and increases coverage of complete annotated proof routes on MathlibMPR, covering up to 3.7% of extra groups. More importantly, we evaluate whether these retrieval gains translate into improved end-to-end theorem proving by integrating LeanGraphSearch into an iterative proving loop guided by Lean feedback. Across three theorem proving benchmarks, LeanGraphSearch improves pass rate at {8, 16, 32} reflection turns by as much as 40% compared to vanilla prover and at most 10% compared to LeanSearch v2, showing higher accuracy-cost efficiency. These findings highlight the value of dependency graph search for theorem proving and motivate further research on structure-aware search for proof discovery.

### 🤖 AI 总结

**一句话总结**：Retrieving relevant lemmas is crucial for formal theorem proving, enabling provers to build machine-checkable proofs from established mathematical results. Recent retrieval systems match library decla...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Lean, Graph, Search, Formal, Theorem, Proving, Retrieving, relevant

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22339v1) | [下载PDF](https://arxiv.org/pdf/2610.22339v1.pdf)

---

## [28. Robust Reinforcement Learning for Dynamic Treatment Regimes under Model and Measurement Uncertainty](https://arxiv.org/abs/2610.22336v1)

**作者**：Chengze Xie, Xuan Wang, Ying Ding 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-10-15

### 📄 论文摘要

We develop a robust reinforcement learning (RL) framework for learning adaptive treatment policies that generalize across patients and remain reliable under errors in the measured biomarker and shifts in the disease dynamics. By modeling the patient as a hidden context, we address generalization and robustness in a unified manner through robust contextual Markov decision processes. Applying our framework to adaptive therapy for metastatic prostate cancer in a simulator calibrated to clinical data, we obtain generalizable and robust policies that substantially outperform the existing adaptive therapy method. In particular, we attain robustness with almost no loss of performance when the biomarker is accurate and the disease evolves as anticipated, and find that the resulting policy Pareto-dominates the existing method across a diverse array of scenarios. Our findings suggest that robust RL holds great promise as a principled methodology for learning reliable adaptive treatment policies.

### 🤖 AI 总结

**一句话总结**：We develop a robust reinforcement learning (RL) framework for learning adaptive treatment policies that generalize across patients and remain reliable under errors in the measured biomarker and shifts...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Robust, Reinforcement, Learning, Dynamic, Treatment, Regimes, under, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22336v1) | [下载PDF](https://arxiv.org/pdf/2610.22336v1.pdf)

---

## [29. Learning to Steer LLM Agents and Multi-Agent Systems](https://arxiv.org/abs/2610.22316v1)

**作者**：Leyang Shen, Yaxin Gong, Yang Zhang 等 10 位作者  
**分类**：cs.LG, cs.AI, cs.MA  
**发布时间**：2026-10-15

### 📄 论文摘要

Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed goal drift. In this work, we propose a steering agent that supervises execution on the fly and steers the system back on track when drift occurs. The steering agent observes the execution context, deciding when to intervene with a low-cost fast path and how to intervene with a high-cost slow path. To unlock its steering intelligence, the ability to assess goal drift and generate effective interventions, we jointly train the two paths with reinforcement learning, combining a pairwise ranking objective with group-relative policy optimization (GRPO). Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency. The learned steering intelligence generalizes to out-of-domain tasks, transfers to unseen executors, and supports controllable intervention frequency without retraining.

### 🤖 AI 总结

**一句话总结**：Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to devia...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Multi-Agent, Learning, Steer, Systems, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22316v1) | [下载PDF](https://arxiv.org/pdf/2610.22316v1.pdf)

---

## [30. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)

**作者**：Anikait Singh, Teresa Zhang, Yoonho Lee 等 6 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-10-15

### 📄 论文摘要

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

### 🤖 AI 总结

**一句话总结**：Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reason...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, LLM, Librarian, Training, Curate, Long-Context, Workspaces, Anticipate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2610.22273v1) | [下载PDF](https://arxiv.org/pdf/2610.22273v1.pdf)

---

