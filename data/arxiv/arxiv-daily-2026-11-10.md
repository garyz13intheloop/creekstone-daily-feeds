# arXiv AI 论文日报 | 2026-11-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (11 篇)
- [cs.LG](#csLG) (10 篇)
- [cs.AI](#csAI) (4 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning](https://arxiv.org/abs/2611.12865v1)

**作者**：Xinjie Shen  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-11-09

### 📄 论文摘要

Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task completion remains feasible while some executable shortcuts earn more reward than every compliant strategy. Encoding these conflicts in task dynamics lets us generate diverse interactive environments at scale and derive compliance feedback from execution histories. In resource and reporting workflows, task optimization increases real productivity through unauthorized resource use or raises reported scores while actual work declines. Controlled changes in the training distribution show that minority conflict exposure can still lead to widespread shortcut acquisition, reaching 97.9\% certified profitable violations on an API task under a 25\% conflict mixture after 128 updates. The same contextual checks supply a simple binary penalty that supports joint capability and compliance gains and partially mitigates acquired violations. Learned safety adapts to expanded authorization and transfers across mechanisms into workflows with evolving evidence and approval requirements. On 32 unseen changing-evidence tasks, resource-trained safety increases safe completion from 53.1\% to 89.1\% relative to task-only training, while both policies achieve full real work. These results connect a verifiable account of reward-driven misalignment with scalable task construction and safety learning that remains useful under changing execution requirements.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including rewar...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Shortcuts, Boundaries, Verifiable, Misalignment, Contextual, Safety, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12865v1) | [下载PDF](https://arxiv.org/pdf/2611.12865v1.pdf)

---

## [2. Automated Knowledge Acquisition Pipeline for Disassembly Instructions: A Comparison of NLP and Generative AI Frameworks](https://arxiv.org/abs/2611.12816v1)

**作者**：Tim Schnieders, Tareq Maximilian Gabriel Ahrari, Oliver Petrovic 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-09

### 📄 论文摘要

The push towards circularity and Re-X principles presents a challenge to SMEs, particularly due to increasing product complexity that impedes the adoption of disassembly automation. This paper introduces and compares two frameworks for extracting disassembly instructions from unstructured information sources, such as disassembly manuals. Our goal is to transform natural language text into a structured, curated and machine-readable format. We implemented and tested a rule-based Natural Language Processing (NLP) framework against a generative AI framework leveraging LLMs. The performance of both approaches was compared using real-world disassembly manuals. This work provides the necessary data foundation for developing and automating future disassembly processes.

### 🤖 AI 总结

**一句话总结**：The push towards circularity and Re-X principles presents a challenge to SMEs, particularly due to increasing product complexity that impedes the adoption of disassembly automation. This paper introdu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Automated, Knowledge, Acquisition, Pipeline, Disassembly, Instructions, Comparison

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12816v1) | [下载PDF](https://arxiv.org/pdf/2611.12816v1.pdf)

---

## [3. LogCDM: Interpretable Log Anomaly Detection via Behavioral Graph Drift and Adaptive Signal Fusion](https://arxiv.org/abs/2611.12775v1)

**作者**：Suryansh Talukdar, Taha Sarwat, Jin Soung Yoo  
**分类**：cs.AI  
**发布时间**：2026-11-09

### 📄 论文摘要

Log-based anomaly detection is increasingly dominated by large pretrained models, from BERT-scale encoders to 8B-parameter language models, which require GPUs at inference time and are difficult to deploy on the monitoring nodes where logs are produced. We present LogCDM, a compact detector that scores each log session using three complementary signals: the next-event surprise of a small causal Transformer, the distance between a graph-attention embedding of the session's own transition graph and that of a normal reference graph, and a transition-drift statistic that we show is exactly a frequency-weighted chi-squared divergence between transition kernels. The divergence view yields an asymptotic null distribution, a length-standardized score, and a per-edge decomposition that explains each alarm. A sigmoid gate fuses the three signals; under a shared-covariance Gaussian model, this gate is the Bayes posterior, and its learned weights indicate which signal each dataset relies on. With 8.1-8.8M parameters and no GPU required at inference, LogCDM reaches F1 scores of 0.984 on HDFS, 0.870 on chronologically split BGL, and 0.850 on Thunderbird, within 0.013-0.12 of an 8.1B-parameter LLM detector evaluated under the same protocol and above all compact baselines on BGL. It scores a session in 5.5-10.5 ms on a CPU. Ablations show that the structural signals add 0.025-0.030 F1 on BGL and Thunderbird but almost nothing on HDFS, consistent with the learned fusion weights.

### 🤖 AI 总结

**一句话总结**：Log-based anomaly detection is increasingly dominated by large pretrained models, from BERT-scale encoders to 8B-parameter language models, which require GPUs at inference time and are difficult to de...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LogCDM, Interpretable, Log, Anomaly, Detection, via, Behavioral, Graph

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12775v1) | [下载PDF](https://arxiv.org/pdf/2611.12775v1.pdf)

---

## [4. Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762v1)

**作者**：Weida Wang, Benteng Chen, Yigeng Jiang 等 90 位作者  
**分类**：cs.AI  
**发布时间**：2026-11-09

### 📄 论文摘要

We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and unresolved questions, then uses these assessments to adapt research targets and select reusable reasoning methods. On Taiyi-Bench, an AI co-scientist ideation benchmark comprising 265 tasks from 50 papers across ten disciplines, Sage-Taiyi ranks first on all eight metrics of historical rediscovery and open-ended ideation, achieving an Overall score of 54.0 compared with 47.9 for the strongest baseline, AI Scientist-v2. It also performs well on two external scientific ideation benchmarks. Five expert-guided collaborations further connect its proposals to experimental and computational validation across chemistry, materials science, and engineering. In chemistry, reaction-condition optimization raises the yield of cobalt-catalyzed carbonylation from trace amounts to 84% and photocatalytic allylic amination from 13% to 69%. These results support metacognitive regulation as an approach to scientific ideation and its progression toward practical validation.

### 🤖 AI 总结

**一句话总结**：We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Sage-Taiyi, Metacognitive, Architecture, Scientific, Discovery, introduce, metacognition-inspired

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12762v1) | [下载PDF](https://arxiv.org/pdf/2611.12762v1.pdf)

---

## cs.CL

## [5. Is Persona Generalization Predictable?](https://arxiv.org/abs/2611.12864v1)

**作者**：Olina Mukherjee, Arnav Goel, Aditi Raghunathan 等 4 位作者  
**分类**：cs.CL, cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We discover a surprising "on-the-line" phenomenon in persona generalization: in-domain and out-of-domain persona rates across various fine-tuning hyperparameters follow an approximately probit-linear relationship, and the specific probit-linear relationship is surprisingly shared even across model families and model sizes, including Qwen and Llama. Training choices that leave the set of trainable parameters unchanged, such as learning rate, weight decay, and training duration, largely move models along the same line, reducing transfer mainly by weakening in-domain learning. Changing which layers are fine-tuned, however, can change the slope. For unsafe behavior, fine-tuning only later layers yields shallower slopes, retaining strong in-domain learning while reducing out-of-domain misalignment. This "on-the-line" phenomenon unifies unexpected, isolated observations of persona generalization within a quantitative framework for predicting and controlling behavioral transfer.

### 🤖 AI 总结

**一句话总结**：Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We dis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Persona, Generalization, Predictable?, occurs, when, fine-tuning, language, model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12864v1) | [下载PDF](https://arxiv.org/pdf/2611.12864v1.pdf)

---

## [6. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.12856v1)

**作者**：Zheng Jiang, Fang Niu, Bo Peng 等 13 位作者  
**分类**：cs.CL, cs.SE  
**发布时间**：2026-11-09

### 📄 论文摘要

Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

### 🤖 AI 总结

**一句话总结**：Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, WorkflowArena, Benchmarking, Executable, Workflow, Orchestration, LLM-Based, Systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12856v1) | [下载PDF](https://arxiv.org/pdf/2611.12856v1.pdf)

---

## [7. How Well Does AI Peer Review Work? A Benchmark Built from 100 Planted Errors](https://arxiv.org/abs/2611.12820v1)

**作者**：Paul Litvak  
**分类**：cs.CL  
**发布时间**：2026-11-09

### 📄 论文摘要

One hundred known errors were planted into 10 open-access psychology papers, and the modified papers were then run through frontier models and two commercial AI review tools. The best single system caught 71 of the 100 errors, while the worst caught 30. Pooling every system's output caught 93. Models are only partly correlated in the errors they find, which makes ensembling a big lever for finding issues in papers. Seven errors could not be caught by any system, and all seven were omissions: information deleted from a paper rather than mistakes inserted into it. Refine.ink contributes more unique catches than any other single system, though it is expensive on a per-error basis. False positives were not measured, and how this error distribution compares to the distribution of errors in real papers remains unknown. The papers, errors, model outputs, and full experiment log are public, so that others can build on this toward a comprehensive evaluation benchmark across disciplines.

### 🤖 AI 总结

**一句话总结**：One hundred known errors were planted into 10 open-access psychology papers, and the modified papers were then run through frontier models and two commercial AI review tools. The best single system ca...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Well, Does, Peer, Review, Work?, Benchmark, Built

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12820v1) | [下载PDF](https://arxiv.org/pdf/2611.12820v1.pdf)

---

## [8. Large Language Models as a Universal Searcher for Open-World Automated Machine Learning](https://arxiv.org/abs/2611.12791v1)

**作者**：Yuxuan Hu, Jihao Liu, Weikang Shi 等 9 位作者  
**分类**：cs.CL  
**发布时间**：2026-11-09

### 📄 论文摘要

Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without the need for task-specific fine-tuning. We propose NCode, a unified numerical encoding scheme that translates diverse AutoML design choices into universal discrete sequences and effectively reframes the optimization process as a unified ranking task. Trained solely on optimization trajectories derived from a limited, single-domain vision task, the proposed LLM-based searcher demonstrates impressive cross-task, cross-modality and joint search-space optimization generalizability, achieving state-of-the-art performance across image classification, image segmentation, speaker verification and text-to-image benchmarks. Crucially, it exhibits superior scalability in the large-scale training and joint optimization of a billion-parameter Diffusion Transformer, requiring 896 GPU-days and attaining a state-of-the-art GenEval score of 0.91. By leveraging reinforcement learning to instill Chain-of-Thought reasoning, we provide a systematic way to interpret the LLM-based searcher's internal decision-making mechanisms, revealing its optimization strategy shifted from the early-stage diversity-driven exploration to the late-stage anchor exploitation. Our proposed framework provides a scalable, generalizable, and interpretable pathway toward general-purpose open-world machine learning optimization.

### 🤖 AI 总结

**一句话总结**：Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, trainin...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Large, Language, Models, Universal, Searcher, Open-World, Automated

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12791v1) | [下载PDF](https://arxiv.org/pdf/2611.12791v1.pdf)

---

## [9. The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?](https://arxiv.org/abs/2611.12750v1)

**作者**：Nikhil Sharma, Kelly Marchisio, Kenton Murray 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.HC, cs.IR  
**发布时间**：2026-11-09

### 📄 论文摘要

Large language models (LLMs) increasingly mediate how people seek and consume information, including accounts that differ across languages and regions, especially on contested topics. Supporting diverse information seeking requires models to help users navigate competing narratives across languages and information streams. We define six capabilities necessary for diverse multilingual information seeking: three foundational capabilities for narrative inclusion, narrative exclusion, and missing narrative identification; and three higher-level capabilities for presenting diverse narratives, preserving narrative coverage under confirmatory queries, and maintaining information parity across languages. To guide the development of those information seeking capabilities, we introduce \textsc{NarrativeBench}, a benchmark comprising 1,333 news articles in 23 publication languages across 23 contested topics and 460 Reddit-grounded queries. Evaluating 14 LLMs across 24 query languages, we find that current models lack the capabilities needed to reliably navigate diverse narratives, limiting users' control over the perspectives they receive and leaving substantial gaps in exposure to competing accounts even when diversity is explicitly requested. Information access also differs across query framings and languages, risking echo chambers, linguistic filter bubbles, and information disparities that weaken the common ground needed for democratic discourse. \textsc{NarrativeBench} provides a foundation for developing information systems that give users across languages and regions agency to navigate diverse narratives.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) increasingly mediate how people seek and consume information, including accounts that differ across languages and regions, especially on contested topics. Supporting diver...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Us, Narrative, Gap, Can, Help, Navigate, Diverse

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12750v1) | [下载PDF](https://arxiv.org/pdf/2611.12750v1.pdf)

---

## cs.CV

## [10. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886v1)

**作者**：Haozhi Yuan, Handong Li, Yifan Zhang 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the observation state, rather than only the output distribution, as an object of alignment. First, Ground-Drop-GRPO (GD-GRPO) trains spatial and temporal specialists with evidence-aware rewards and stochastic removal of the original visual input, encouraging them to acquire grounded evidence and use the returned observations. Second, Observation-Gated-MOPD (OG-MOPD) replaces deficient tool actions with canonical ones mid-rollout and resumes distillation from the repaired observation. The two stages complement each other, as learning to rely on tool-returned observations can help the policy benefit from observation repair. Neither stage requires a task-specific SFT cold start. Extensive experiments over 14 image and video benchmarks demonstrate that Reframe outperforms both Mix-RL and vanilla MOPD. Ablation results show that GD-GRPO increases observation dependence and tool gain compared with outcome-based GRPO.

### 🤖 AI 总结

**一句话总结**：Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. M...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reframe, Observation-Aligned, Multi-Teacher, On-Policy, Distillation, Agentic, Visual, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12886v1) | [下载PDF](https://arxiv.org/pdf/2611.12886v1.pdf)

---

## [11. World In-Context Learning for Agentic Robot Manipulation](https://arxiv.org/abs/2611.12885v1)

**作者**：Heng Fang, Zehui Guo, Yuehan Zhang 等 6 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-11-09

### 📄 论文摘要

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at https://github.com/ArcheOne-AI/RoboScript

### 🤖 AI 总结

**一句话总结**：Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：World, In-Context, Learning, Agentic, Robot, Manipulation, Trained, action

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12885v1) | [下载PDF](https://arxiv.org/pdf/2611.12885v1.pdf)

---

## [12. Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs](https://arxiv.org/abs/2611.12883v1)

**作者**：Zhaoying Pan, Shenyu Lu, Jun Hui Wong 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow visual or textual evidence. Building on this, we introduce a lightweight, training-free intervention that biases these heads toward a designated trusted modality at inference time. The identified heads are stable across calibration set sizes and generalize across settings, and steering them enables effective bidirectional control of modality reliance across diverse benchmarks. Our findings identify an effective control mechanism to align MLLM predictions with task-specified modality priorities. The code is available at https://github.com/zhaoyingpan/modality-arbitration.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are no...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Modality, Preference, Controlling, Multimodal, Arbitration, under, Conflict

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12883v1) | [下载PDF](https://arxiv.org/pdf/2611.12883v1.pdf)

---

## [13. Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos](https://arxiv.org/abs/2611.12879v1)

**作者**：Rustin Soraki, Matthew Wallingford, Ryan Aby 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

To interact with an object, we need to anticipate both how it will move and how our hands should move with it. Human videos capture these relationships across everyday activities, offering a natural source for learning to predict future interactions. Learning from them requires recovering motion from completed interactions and using it to anticipate what could happen next. We present $\textit{Grasping-the-Future}$, a unified generative model of joint 3D hand-object motion, including wrist motion, finger articulation, and object position and orientation. Through masked spatiotemporal completion and flow matching, we train a single model for several prediction tasks: forecasting future interactions, predicting hand motion given object motion or vice versa, generating both trajectories toward a desired final object pose, and completing partially observed interactions. We explicitly model hand-object relations and incorporate contact constraints to help preserve grasp relationships during motion. To obtain 3D supervision from internet videos, we develop a scalable pipeline that combines pretrained perception models with joint geometric optimization to reconstruct completed interactions. We combine these recovered trajectories with annotated interaction datasets as training data for all tasks. We demonstrate strong performance across all tasks, outperforming released forecasters on datasets with 3D annotations. Moreover, we show geometric and physical plausibility of the predicted trajectories by retargeting them to a robotic embodiment. Videos are available at https://grasping-the-future.github.io.

### 🤖 AI 总结

**一句话总结**：To interact with an object, we need to anticipate both how it will move and how our hands should move with it. Human videos capture these relationships across everyday activities, offering a natural s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Grasping, Future, Joint, Hand-Object, Forecasting, Internet, Videos

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12879v1) | [下载PDF](https://arxiv.org/pdf/2611.12879v1.pdf)

---

## [14. Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks](https://arxiv.org/abs/2611.12875v1)

**作者**：Hao Gu, Jin Yao, Zezhou Cheng  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To address this limitation, we introduce Click3R, a framework for interactive geometric correction of feed-forward models using sparse human correspondence clicks. Given an image pair and a small set of cross-view point correspondences provided by a user, Click3R injects geometric constraints into the 3D reconstruction networks through a lightweight point correspondence adapter, enabling the model to resolve ambiguities in challenging scenarios such as repetitive textures, symmetric structures, large viewpoint changes, or textureless regions. To evaluate interactive reconstruction, we curate a challenging benchmark specifically designed to expose failure modes of existing feed-forward 3D reconstruction methods. Experiments show that Click3R reduces reconstruction error with as few as a single correspondence click, improving performance on both standard and our curated benchmarks. Our results highlight that sparse human interaction provides an effective and practical mechanism for correcting geometric reconstruction errors.

### 🤖 AI 总结

**一句话总结**：Despite impressive progress, existing feed-forward large 3D reconstruction models produce a single, irrevocable prediction. When these models fail, there is no mechanism to correct their mistakes. To ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Click3R, Interactive, Stereo, Reconstruction, Sparse, Correspondence, Clicks

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12875v1) | [下载PDF](https://arxiv.org/pdf/2611.12875v1.pdf)

---

## [15. SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870v1)

**作者**：Yu Zhou, Xinyuan Xia, Xuankun Yang 等 11 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-11-09

### 📄 论文摘要

World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However, introducing action learning may impair this alignment. Principled guidance on data and supervision design for maintaining language-video alignment during action learning remains limited. To investigate this, we curate a pool of approximately 47,000 hours of general videos, egocentric videos, UMI demonstrations, and robot demonstrations. Building on this, we systematically study how language-video supervision, language-video-action supervision, and the joint use of these two forms affect WAM performance. In particular, we examine how language annotation quality affects pretrained language-video capabilities, and how action supervision from UMI and robot demonstrations extends these capabilities to language-video-action modeling. To better scale the model, we further conduct detailed studies on joint training recipe and model architecture. Under a fixed training budget, mixing egocentric videos and UMI demonstrations improves control generalization. Model architecture affects how effectively these experiences are used, while scaling pretraining under the selected configuration brings further gains. The resulting recipe, post-trained on RoboTwin Clean demonstrations only, achieves success rates of 88.10% and 61.56% under Easy (Clean-to-Clean) and Hard (Clean-to-Random) conditions, respectively. Our model achieves 40.00% SR across three real-world tasks, compared with 23.33% for the strongest baseline, indicating better generalization under unseen conditions. We release the curated data, training code, and model weights.

### 🤖 AI 总结

**一句话总结**：World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment ac...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SWAM, Scaling, World, Action, Models, Cross-Modal, Alignment, jointly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12870v1) | [下载PDF](https://arxiv.org/pdf/2611.12870v1.pdf)

---

## [16. AI-based characterization of lymphoid structures and the tumor microenvironment reveals lower mature tertiary lymphoid structures, lymph-node follicles, and plasma cells after neoadjuvant therapy in lung squamous cell carcinoma](https://arxiv.org/abs/2611.12855v1)

**作者**：Arne Schmidt, Justin Nieder, Cornelius Boehm 等 27 位作者  
**分类**：cs.CV, q-bio.QM  
**发布时间**：2026-11-09

### 📄 论文摘要

Mature, germinal centre-bearing tertiary lymphoid structures (TLS) and mature lymph node follicles (secondary lymphoid structures, SLS) sustain the plasma cell response that shapes outcome and immunotherapy benefit in lung cancer. How this loco-regional axis differs between neoadjuvant-treated and therapy-naive tumors is poorly defined. We analyzed H&E whole-slide images of resected tumors and paired proximal and distal lymph nodes from matched neoadjuvant-treated (neoLUSC, n=20) and therapy-naive (naivLUSC, n=20) lung squamous cell carcinoma (LUSC) patients. Aignostics Atlas H&E Tissue Analysis (HETA) models quantified cell densities per tissue compartment and cell-cell co-localization; a dedicated deep-learning model validated against pathologist annotations detected TLS and SLS and graded their maturity. Prognostic value was tested in an independent cohort (n=458; 46 treated). In neoLUSC tumors, stromal plasma cell density was 72% (p=0.004) and stromal lymphocyte density 48% (p=0.015) lower than in naivLUSC; macrophages and granulocytes did not differ significantly. Total and immature TLS did not differ, whereas mature TLS in the tumor (p=0.034) and mature SLS in the tumor-distal lymph node (p=0.003) were lower in neoLUSC patients. Peri-TLS plasma cell density correlated with tumor lymphocyte density in naivLUSC (rho=0.54, p=0.017) but not in neoLUSC tumors (rho=0.07). In the validation cohort, stromal plasma cell density (HR 0.69, p=0.011) and lymphocyte-plasma cell co-localization (HR 0.66, p=0.004) were associated with longer survival, and neoadjuvant status with shorter survival (HR 1.50, p=0.026). Neoadjuvant therapy is thus associated with fewer mature lymphoid structures and weaker coupling of the humoral compartment to the tumor rather than uniformly lower immune readouts. The stromal plasma cell/co-localization axis is a candidate prognostic biomarker.

### 🤖 AI 总结

**一句话总结**：Mature, germinal centre-bearing tertiary lymphoid structures (TLS) and mature lymph node follicles (secondary lymphoid structures, SLS) sustain the plasma cell response that shapes outcome and immunot...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, AI-based, characterization, lymphoid, structures, tumor, microenvironment, reveals

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12855v1) | [下载PDF](https://arxiv.org/pdf/2611.12855v1.pdf)

---

## [17. What kills $v$-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching](https://arxiv.org/abs/2611.12852v1)

**作者**：Tianze Luo, Haofeng Huang, Yuan Yao  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Latent Diffusion Models dominate generative modeling but face two-stage training complexity and the inherent reconstruction limits of pre-trained autoencoders. Pixel-space Flow Matching offers a simplified end-to-end alternative yet often encounters training difficulties when using the standard $v$-prediction objective. Recent research attributes this difficulty to the off-manifold nature of noised targets, motivating a shift toward $x$-prediction. In this paper, we investigate this explanation through patch-wise Principal Component Analysis (PCA) and identify a bandwidth bottleneck. The velocity in minor components is largely determined by the raw noisy input, requiring deep backbones to preserve information that competes with principal-component modeling. Through controlled experiments and representation analysis, we further examine why $x$-prediction remains effective: its parameterization provides a raw-input bypass, while its learned input representation can spontaneously concentrate on principal directions. Under low-rank observations, our analysis of the induced flow characterizes $x$-prediction as an implicit conditional-mean decoder, reconstructing discarded components from the retained information. These observations motivate the Raw-injected Transformer (RiT), which combines a lightweight raw-conditioned decoder with an output-side shortcut to separate semantic modeling from raw-state propagation. Our method restores effective $v$-prediction and achieves competitive performance on ImageNet $256\times256$, providing a perspective on the interaction between prediction objectives and architectural bandwidth.

### 🤖 AI 总结

**一句话总结**：Latent Diffusion Models dominate generative modeling but face two-stage training complexity and the inherent reconstruction limits of pre-trained autoencoders. Pixel-space Flow Matching offers a simpl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：What, kills, $v$-prediction?, Patch-wise, PCA, Perspective, Pixel-Space, Flow

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12852v1) | [下载PDF](https://arxiv.org/pdf/2611.12852v1.pdf)

---

## [18. 2D Gum-Net: Unsupervised Dense Elastic Image Registration via Symmetric Correlation and Spectral Pooling](https://arxiv.org/abs/2611.12805v1)

**作者**：Aarya Bhave, Anushka Ajay Bhave  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-11-09

### 📄 论文摘要

Dense non-rigid registration, the recovery of a pixel-wise deformation field that warps one image into geometric agreement with another, is fundamental across medical imaging, structural biology, and correspondence estimation, yet learning-based approaches face a severe bottleneck: ground-truth deformation fields are notoriously difficult to obtain for real data. We present 2D Gum-Net, an end-to-end architecture that predicts dense elastic deformation fields fully unsupervised. We transfer the Geometric Unsupervised Matching Network (Gum-Net), originally developed for 3D subtomogram alignment in cryo-electron tomography, to 2D elastic registration: all three modules are redesigned in 2D, and the rigid transformation head is replaced by a Dense Spatial Transformer that regresses a sparse control-point grid, lifted to a full-resolution field $Φ$ by bicubic interpolation. Downsampling uses DCT spectral pooling, implemented as frozen-basis matrix multiplications ($\approx 50\times$ GPU speedup), preserving the fine, quasi-periodic structure that max and average pooling destroy. We evaluate on contact-based fingerprints, a challenging testbed for this task: locally self-similar ridge patterns make correspondence maximally ambiguous, skin pressed against a sensor generates authentic large-displacement elastic distortion, and minutiae act as precise landmarks through which an independent matcher externally verifies the topological correctness of predicted fields. Trained purely on synthetic impressions and evaluated zero-shot on real benchmarks, our method improves structural correlation by up to 15.7% on FVC2004 and raises genuine match scores under an independent matcher while leaving imposter scores essentially unchanged. This suggests that the predicted deformations restore true structure without fabricating correspondences.

### 🤖 AI 总结

**一句话总结**：Dense non-rigid registration, the recovery of a pixel-wise deformation field that warps one image into geometric agreement with another, is fundamental across medical imaging, structural biology, and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D, Gum-Net, Unsupervised, Dense, Elastic, Image, Registration, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12805v1) | [下载PDF](https://arxiv.org/pdf/2611.12805v1.pdf)

---

## [19. Complementarity-Driven Dual-Teacher Hierarchical Alignment for Zero-Shot EEG-to-Image Retrieval](https://arxiv.org/abs/2611.12798v1)

**作者**：Lukun Wu, Jie Li, Ziqi Ren 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Decoding visual information from EEG is central to brain--computer interfaces and brain-inspired intelligence, and contrastive alignment with pretrained vision foundation models (VFMs) has become the dominant paradigm. However, existing methods align EEG solely with CLIP-family VFMs, leaving hierarchical visual information in neural responses under-exploited. To address this gap, we formulate a mechanism-paradigm correspondence view linking hierarchical visual processing (from appearance to semantics) to the complementary biases of cross-paradigm VFMs, with image-only models (e.g., DINO) and image--text models (e.g., CLIP) capturing distinct facets of this hierarchy. Guided by this view, we propose the Dual-Teacher Hierarchical Alignment (DTHA) framework. Concretely, a shared EEG encoder is supervised by frozen multi-blur CLIP and shallow DINOv2 teachers via dual-branch contrastive alignment, so each branch fully supervises the visual cues it emphasizes. A fused-retrieval objective learns adaptive weights to combine their complementary visual representations for zero-shot EEG-to-image retrieval. For the shared EEG encoder, we introduce the Attentive Modulated Scalp-Pattern Bank Encoder (AMSPBE), combining temporo-spatial attention with a learnable scalp-pattern bank for accurate, interpretable visual feature extraction, while modeling regional temporal dynamics and filter-bank topographies. On THINGS-EEG zero-shot retrieval, DTHA achieves 92.4% Top-1 accuracy, exceeding prior state of the art by 12.4 percentage points. Spatial, spectral, and representational-similarity analyses, together with THINGS-MEG evaluation, validate DTHA's effectiveness, biological plausibility, and cross-modality generalization. This complementarity-driven perspective shows that supervision from cross-paradigm VFMs enables more complete extraction of hierarchical visual information from brain activity.

### 🤖 AI 总结

**一句话总结**：Decoding visual information from EEG is central to brain--computer interfaces and brain-inspired intelligence, and contrastive alignment with pretrained vision foundation models (VFMs) has become the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Complementarity-Driven, Dual-Teacher, Hierarchical, Alignment, Zero-Shot, EEG-to-Image, Retrieval, Decoding

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12798v1) | [下载PDF](https://arxiv.org/pdf/2611.12798v1.pdf)

---

## [20. Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting](https://arxiv.org/abs/2611.12739v1)

**作者**：Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Modern digital phenotyping pipelines require the precise measurement of a range of 3D morphological plant traits. The accurate, high throughput acquisition of these traits helps breeders and researchers accelerate the development of new varieties, techniques and products. Recent advances in 3D technologies have enabled a rapid transition from 2D to 3D pipelines, but high throughput acquisition of digital 3D twins of plants remains a significant challenge due to complex morphology, thin structures and occlusions. In this paper we present Plant Orbiter, a new approach to generating 3D plants that leverages recent advances in video diffusion to produce high quality 3D Gaussian Splats of plants from a single image. We show that our method more accurately recreates plant morphology than other state-of-the-art methods, achieving the highest 3D F-score against all baselines, while being more practical for high throughput pipelines due to easier alignment and reduced cost of camera placement. Combined with a 2D diffusion model, we show that our method also achieves state-of-the-art results in the generation of 3D plant models from a text prompt.

### 🤖 AI 总结

**一句话总结**：Modern digital phenotyping pipelines require the precise measurement of a range of 3D morphological plant traits. The accurate, high throughput acquisition of these traits helps breeders and researche...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Diffusion, Plant, Orbiter, Reconstruction, Generation, Video, Orbit

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12739v1) | [下载PDF](https://arxiv.org/pdf/2611.12739v1.pdf)

---

## cs.LG

## [21. Guiding Data Allocation for Robust Subpopulation Generalization](https://arxiv.org/abs/2611.12884v1)

**作者**：Zhaoying Pan, Yipei Wang, Shenyu Lu 等 4 位作者  
**分类**：cs.LG, cs.CV  
**发布时间**：2026-11-09

### 📄 论文摘要

Machine learning models often achieve high average accuracy in the training data while performing poorly on test data due to subpopulation shift. A common data-centric solution is to enforce balanced subgroup proportions, but full balance can be costly, infeasible, and not always necessary. In this work, we study whether balanced training data is the unique optimal configuration for robust subpopulation generalization. We extend a Gaussian feature-model framework to theoretically characterize the performance landscape across general training subgroup distributions. We show that multiple configurations, including substantially imbalanced ones, can perform comparably to the balanced one. We further derive gradient-based directions for adjusting subgroup proportions to improve adjusted accuracy and worst-group accuracy more efficiently. These findings suggest that strategically allocating data offers a more flexible and principled path to robust performance than simple balancing. The code is available at https://github.com/zhaoyingpan/subpop-data-allocation.

### 🤖 AI 总结

**一句话总结**：Machine learning models often achieve high average accuracy in the training data while performing poorly on test data due to subpopulation shift. A common data-centric solution is to enforce balanced ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Guiding, Data, Allocation, Robust, Subpopulation, Generalization, Machine, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12884v1) | [下载PDF](https://arxiv.org/pdf/2611.12884v1.pdf)

---

## [22. Kolmogorov-Chapman Maps: Trajectory-Free Learning for Simulating Molecular Dynamics](https://arxiv.org/abs/2611.12880v1)

**作者**：Majdi Hassan, Marta Skreta, Dominique Beaini 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Stochastic differential equations (SDEs) describe stochastic processes across a wide range of scientific domains, including physics, biology, and finance. Although individual numerical integration steps are inexpensive, observing meaningful events or transitions can require millions of sequential steps, resulting in substantial wall-clock simulation time and poor hardware utilization. Deep learning offers an alternative by amortizing many integration steps into a single neural network forward pass, potentially enabling much faster simulation. However, existing supervised approaches typically require long simulated trajectory data, which restricts their applicability. In this work, we introduce Kolmogorov-Chapman Maps (KC-Maps), a method for learning the transition kernel of an SDE that relies only on the trajectory-free marginal samples together with the known drift and diffusion coefficients. Given an initial time and state of a process, KC-Maps models its distribution integrated to any given time, corresponding to the weak solution of the SDE. To recover the correct dynamics, KC-Maps satisfies two key properties: (i) it satisfies the boundary conditions, which we incorporate directly into the neural network architecture, and (ii) it respects the Kolmogorov--Chapman equation, which provides an efficient training objective. We empirically demonstrate that KC-Maps learns to integrate the dynamics of peptide molecular systems and outperforms classical molecular dynamics in terms of GPU-hours.

### 🤖 AI 总结

**一句话总结**：Stochastic differential equations (SDEs) describe stochastic processes across a wide range of scientific domains, including physics, biology, and finance. Although individual numerical integration ste...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Kolmogorov-Chapman, Maps, Trajectory-Free, Learning, Simulating, Molecular, Dynamics, Stochastic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12880v1) | [下载PDF](https://arxiv.org/pdf/2611.12880v1.pdf)

---

## [23. Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited Channels](https://arxiv.org/abs/2611.12878v1)

**作者**：Sreejeet Maity, Aritra Mitra  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Motivated by reinforcement learning subject to communication constraints, we study a policy evaluation problem with linear function approximation over a rate-limited channel. In our setup, an agent interacting with an unknown environment (modeled as a Markov Decision Process) transmits quantized estimates of a temporal-difference (TD) learning update direction to a server over a finite-capacity channel. Our goal is to investigate to what extent one can preserve the statistical convergence rates achievable when the channel has infinite capacity. To that end, we propose a new algorithm called Batched Adaptively Quantized TD (BAQ-TD), which uses batching to reduce the variance of the transmitted information, and adaptive quantization to encode innovations. We prove a high-probability finite-time error bound for BAQ-TD, and show that, above a certain finite channel capacity, BAQ-TD preserves the convergence rate of unquantized TD up to logarithmic factors. Specifically, for a $d$-dimensional value function parameter, we establish that transmitting a total of $\mathcal{O}(d \log(T))$ bits over a horizon of length $T$ suffices to achieve the order-optimal rate of $\tilde{\mathcal{O}}(1/T)$, marking an exponential improvement in communication-complexity over prior work.

### 🤖 AI 总结

**一句话总结**：Motivated by reinforcement learning subject to communication constraints, we study a policy evaluation problem with linear function approximation over a rate-limited channel. In our setup, an agent in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TD, Adaptive, Quantization, Preserves, Fast, Rates, Learning, over

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12878v1) | [下载PDF](https://arxiv.org/pdf/2611.12878v1.pdf)

---

## [24. Vendi Anomaly Scores for Efficient and Accurate Anomaly Detection](https://arxiv.org/abs/2611.12871v1)

**作者**：Amey Pasarkar, Adji Bousso Dieng  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Anomaly detection (AD) is a critical for trustworthy machine learning and scientific discovery. Existing methods typically define anomalies through local density, isolation heuristics, or distance from a fitted distribution, making them sensitive to neighborhood scale, partitioning choices, or restrictive distributional assumptions. In this work, we introduce a new paradigm by formulating anomaly detection from a diversity perspective. We propose the $\textit{Vendi Anomaly Score}$ (VAS), which detects anomalies by quantifying how much a sample changes the diversity of the dataset, as measured by the Vendi score, when removed. VAS captures both local redundancy and global data structure without relying on density estimation or partitioning heuristics. Moreover, VAS requires no hyperparameter tuning, instead adapting automatically to the spectral structure of the data. VAS is non-parametric and scales linearly with dataset size. Across 148 benchmark embedding datasets derived from 10 source datasets and 4 embedding architectures, VAS achieves state-of-the-art AD performance. We further validate VAS on large-scale ImageNet experiments, where it remains robust as both contamination rate and dataset scale increase.

### 🤖 AI 总结

**一句话总结**：Anomaly detection (AD) is a critical for trustworthy machine learning and scientific discovery. Existing methods typically define anomalies through local density, isolation heuristics, or distance fro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AD, Vendi, Anomaly, Scores, Efficient, Accurate, Detection, critical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12871v1) | [下载PDF](https://arxiv.org/pdf/2611.12871v1.pdf)

---

## [25. Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](https://arxiv.org/abs/2611.12869v1)

**作者**：Julia Herbst, Simon Roschmann, Quentin Bouniot 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

The Platonic Representation Hypothesis (PRH) suggests that neural networks are converging toward similar representation spaces. As language models become more capable, their representations are aligning with those of vision models. However, recent work has questioned whether this trend continues to hold for newer language models. Moreover, it has been shown that representation similarity metrics can be confounded by model depth and width, requiring appropriate baselines for interpretation. In this work, we first investigate where alignment emerges between unimodal models across model layers and representation dimensions. Next, we find that the PRH capability-alignment trend persists for newer models as long as the captions are sufficiently clean and informative. Finally, we contextualize cross-modal alignment, introducing unimodal and multimodal baselines on various datasets. Our results show that the cross-modal representational alignment of unimodal models can surpass that of explicitly aligned vision-language models, but remains substantially behind the alignment observed for models of the same modality. Code is available at https://github.com/ExplainableML/prh-closer-look.

### 🤖 AI 总结

**一句话总结**：The Platonic Representation Hypothesis (PRH) suggests that neural networks are converging toward similar representation spaces. As language models become more capable, their representations are aligni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：It, Where, Does, Alignment, Emerge, What, Mean?, Closer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12869v1) | [下载PDF](https://arxiv.org/pdf/2611.12869v1.pdf)

---

## [26. What the Loss Curve Misses: FP4 Pretraining Slows the Acquisition of Rare Facts](https://arxiv.org/abs/2611.12832v1)

**作者**：Chang Lu, Mengjiao Zhang  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Low-precision pretraining is usually judged by validation loss. We ask whether matching loss also means learning rare facts as efficiently. We train transformers from scratch with emulated 4-bit matrix multiplications on synthetic biographies with controlled exposure counts, on their own and mixed into web text. NVFP4 needs 1.32$\times$ and 1.52$\times$ as many exposures as BF16 to match its recall while validation loss differs by only 0.5% and 2%, and 1.26$\times$ and 1.30$\times$ when both models are evaluated with BF16 matrix multiplications. Under our primary readout, the exposure cost is about 1.2$\times$ at matched loss. Zero-mean gradient noise reproduces the cost of quantizing only the backward pass, which barely moves the loss. In a controlled experiment at twice the NVFP4 error, noise fed only to Adam's second-moment estimate acts like a lower learning rate and its cost fades, whereas noise in the update lowers its signal-to-noise ratio and carries about two thirds of the cost through the end of training. Raising the learning rate to offset the smaller average step does not recover the cost, either for this noise or for NVFP4. Gradient statistics of BF16 checkpoints rank the costs of formats, partial quantizations and noise controls without fitting (Spearman 0.96). We suggest measuring rare-fact acquisition alongside loss when evaluating low-precision recipes.

### 🤖 AI 总结

**一句话总结**：Low-precision pretraining is usually judged by validation loss. We ask whether matching loss also means learning rare facts as efficiently. We train transformers from scratch with emulated 4-bit matri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FP4, What, Loss, Curve, Misses, Pretraining, Slows, Acquisition

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12832v1) | [下载PDF](https://arxiv.org/pdf/2611.12832v1.pdf)

---

## [27. Inversion-Free High-Dimensional Counterfactual Inference](https://arxiv.org/abs/2611.12815v1)

**作者**：Saketh Vishnubhatla, Pingchuan Ma, Shu Wan 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-11-09

### 📄 论文摘要

Counterfactual inference is the task of answering hypothetical "what-if" queries about a unit, given an observational dataset, modeling assumptions, and a causal graph. This enables a modeler to reason about hypothetical scenarios that cannot otherwise be answered without assumptions or a causal graph. The simpler case involves a causal graph with scalar 1-D variables that denote different attributes in the data-generation process. While the literature is clear in the 1-D case, extending this to settings with high-dimensional nodes (e.g., images) remains challenging. Conventionally, in the literature, methods recover the latent state from the factual image (inversion), generate counterfactual attributes from the graph, and render the counterfactual image from the latent state using the updated attributes. In our work, we investigate the necessity of the inversion step in computing high-dimensional counterfactuals. We first discuss moving from the scalar 1-D case to the higher-dimensional case. Secondly, we discuss the relevance of the inversion step and evaluate an inversion-free counterpart repurposed from the image-editing literature. Finally, on image datasets such as CelebA and ADNI, we benchmark our approach using two measures: namely, effectiveness and identity preservation. While effectiveness is a measure of how faithfully the counterfactual attribute is rendered, identity preservation measures whether the same unit (image) is being rendered, both of which are crucial for high-dimensional counterfactual inference. We present the tradeoffs of using inversion-based and inversion-free approaches in our work.

### 🤖 AI 总结

**一句话总结**：Counterfactual inference is the task of answering hypothetical "what-if" queries about a unit, given an observational dataset, modeling assumptions, and a causal graph. This enables a modeler to reaso...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Inversion-Free, High-Dimensional, Counterfactual, Inference, task, answering, hypothetical

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12815v1) | [下载PDF](https://arxiv.org/pdf/2611.12815v1.pdf)

---

## [28. Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks](https://arxiv.org/abs/2611.12799v1)

**作者**：Tingcheng Bian, Kangye Gong, Jinchang Luo 等 9 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-11-09

### 📄 论文摘要

Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on problems that earlier checkpoints from the same run had already solved, and the union of problems solved across checkpoints far exceeds any single one. The discarded checkpoints thus form a teacher pool obtained at no additional training cost, which on-policy distillation (OPD) can mine to recover the lost coverage. Mining this pool raises two challenges: i) which checkpoint to distill from, as no checkpoint dominates the others and complementarity to the student is problem-specific; ii) where to trust it, as even a well-chosen teacher is only locally superior, so indiscriminate distillation overwrites behavior the student has already mastered. We propose Agentic-OPD, which treats the best-validation checkpoint as the student and all saved checkpoints as frozen teacher candidates, using the student's evolving capability gaps to guide both teacher selection and supervision filtering: the HCN policy (Highest Coverage Next) dynamically selects teachers by weighted coverage of the student's unsolved problems, while the LAD module (Locality-Aware Distillation) confines transfer to failed student rollouts on problems where the teacher performs better. Across five agentic task domains and 24 benchmarks and task subsets, Agentic-OPD improves over its initialization checkpoint by up to 7.4 points, with a 4B student surpassing the latest frontier models GPT-5.6 and DeepSeek-V4.1 on deep search. Agentic-OPD recasts a finished RL run as a reusable pool of policies and establishes post-RL capability recovery as a stage orthogonal to improvements in the RL algorithm itself.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Agentic-OPD, Recovering, Forgotten, Capabilities, via, On-Policy, Distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12799v1) | [下载PDF](https://arxiv.org/pdf/2611.12799v1.pdf)

---

## [29. Clique Constraints for Exact Causal Structure Learning](https://arxiv.org/abs/2611.12747v1)

**作者**：Xiaoyu He, Pavel Rytíř, Petr Ryšavý 等 4 位作者  
**分类**：cs.LG, math.OC, stat.ML  
**发布时间**：2026-11-09

### 📄 论文摘要

Exact score-based causal structure learning supports explicit structural constraints and optimisation certificates, but its branch-and-cut search can be computationally demanding. We augment exact causal structure learning methods with an upper bound on the maximum clique size of the learned undirected skeleton, enforced at integer candidates through lazy cycle and clique constraints. On static linear-Gaussian Erdős-Rényi and scale-free DAGs, we evaluate callback order, alternative clique-cut policies, incumbent repair, fractional separation, and Big-M bounds. We report causal-recovery metrics jointly with optimality gaps, primal and dual bounds, node throughput, MIPSOL events, and callback cost. Two variants receive particular attention: B3 selects the most violated minimal (k+1)-clique inequality at each callback, whereas C3 repairs an infeasible integer candidate by deleting violating edges and refitting affected regression columns using QR-based least squares. The results do not indicate that clique constraints uniformly accelerate optimisation. However, their benefit depends on graph density, sample size, and cut-management policy, while large collections of correlated constraints can reduce node throughput. Tighter valid Big-M bounds reduced the fixed-budget optimality gap in most tested settings, without necessarily changing SHD or F1 at a fixed time limit. These findings characterize the computational trade-offs of clique-constrained exact causal learning, and identify selective separation and incumbent repair as promising directions.

### 🤖 AI 总结

**一句话总结**：Exact score-based causal structure learning supports explicit structural constraints and optimisation certificates, but its branch-and-cut search can be computationally demanding. We augment exact cau...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Clique, Constraints, Exact, Causal, Structure, Learning, score-based, supports

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12747v1) | [下载PDF](https://arxiv.org/pdf/2611.12747v1.pdf)

---

## [30. $Σ$-LeWM: Learning World Models via S-Information for Robot Control](https://arxiv.org/abs/2611.12732v1)

**作者**：Xinrui Zu, Michael Przystupa, Zhao Yang 等 5 位作者  
**分类**：cs.LG, cs.AI, cs.RO  
**发布时间**：2026-11-09

### 📄 论文摘要

World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion. While early world model architectures relied on decoders to prevent mode collapse and learn a predictable latent space, recent works on world models, such as Joint Embedding Predictive Architecture or LeWorldModel, increasingly aim to learn embeddings without a grounding decoder, utilising only a latent forward dynamics predictor and a stabilising entropy term. In this paper, we set out to demonstrate that the further introduction of two additional latent losses to LeWorldModel, a backward dynamics predictor and an inverse dynamics action predictor, enforces further structure on the latent embedding, leading to further gains in both performance and planning efficiency. These are critical properties for improving the applicability of such methods to real-time model-based control of real-world robots. We demonstrate these gains on standard world model benchmarks and two simulated robot manipulation tasks.

### 🤖 AI 总结

**一句话总结**：World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion. While early world model architectures relied on decoders to prevent ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：$Σ$-LeWM, Learning, World, Models, via, S-Information, Robot, Control

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2611.12732v1) | [下载PDF](https://arxiv.org/pdf/2611.12732v1.pdf)

---

