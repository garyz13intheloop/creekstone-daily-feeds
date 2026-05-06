# arXiv AI 论文日报 | 2026-05-06

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (7 篇)
- [cs.CV](#csCV) (12 篇)
- [cs.CL](#csCL) (6 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories](https://arxiv.org/abs/2605.04036v1)

**作者**：Yuwen Du, Rui Ye, Shuo Tang 等 7 位作者  
**分类**：cs.AI, cs.CL  
**发布时间**：2026-05-05

### 📄 论文摘要

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry recipe involves a highly resource-intensive pipeline spanning pre-training, continual pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). In this report, we show that when fueled with informative and high-difficulty trajectories, a simple SFT approach could be surprisingly powerful for training frontier search agents. By introducing three simple data synthesis modifications: scaling knowledge graph size for richer exploration, expanding the tool set size for broader functionality, and strict low-step filtering, we establish a stronger baseline. Trained on merely 10.6k data points, our OpenSeeker-v2 achieves state-of-the-art performance across 4 benchmarks (30B-sized agents with ReAct paradigm): 46.0% on BrowseComp, 58.1% on BrowseComp-ZH, 34.6% on Humanity's Last Exam, and 78.0% on xbench, surpassing even Tongyi DeepResearch trained with heavy CPT+SFT+RL pipeline, which achieves 43.4%, 46.7%, 32.9%, and 75.0%, respectively. Notably, OpenSeeker-v2 represents the first state-of-the-art search agent within its model scale and paradigm to be developed by a purely academic team using only SFT. We are excited to open-source the OpenSeeker-v2 model weights and share our simple yet effective findings to make frontier search agent research more accessible to the community.

### 🤖 AI 总结

**一句话总结**：Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet their development remains dominated by industrial giants. The typical industry reci...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Agent, OpenSeeker-v2, Pushing, Limits, Search, Informative, High-Difficulty

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04036v1) | [下载PDF](https://arxiv.org/pdf/2605.04036v1.pdf)

---

## [2. Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours](https://arxiv.org/abs/2605.04019v1)

**作者**：Raja Sekhar Rao Dheekonda, Will Pearce, Nick Landers  
**分类**：cs.AI, cs.CR  
**发布时间**：2026-05-05

### 📄 论文摘要

AI systems are entering critical domains like healthcare, finance, and defense, yet remain vulnerable to adversarial attacks. While AI red teaming is a primary defense, current approaches force operators into manual, library-specific workflows. Operators spend weeks hand-crafting workflows - assembling attacks, transforms, and scorers. When results fall short, workflows must be rebuilt. As a result, operators spend more time constructing workflows than probing targets for security and safety vulnerabilities.   We introduce an AI red teaming agent built on the open-source Dreadnode SDK. The agent creates workflows grounded in 45+ adversarial attacks, 450+ transforms, and 130+ scorers. Operators can probe multi-agent systems, multilingual, and multimodal targets, focusing on what to probe rather than how to implement it.   We make three contributions: 1. Agentic interface. Operators describe goals in natural language via the Dreadnode TUI (Terminal User Interface). The agent handles attack selection, transform composition, execution, and reporting, letting operators focus on red teaming. Weeks compress to hours. 2. Unified framework. A single framework for probing traditional ML models (adversarial examples) and generative AI systems (jailbreaks), removing the need for separate libraries. 3. Llama Scout case study. We red team Meta Llama Scout and achieve an 85% attack success rate with severity up to 1.0, using zero human-developed code

### 🤖 AI 总结

**一句话总结**：AI systems are entering critical domains like healthcare, finance, and defense, yet remain vulnerable to adversarial attacks. While AI red teaming is a primary defense, current approaches force operat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Redefining, Red, Teaming, Agentic, Era, Weeks, Hours, systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04019v1) | [下载PDF](https://arxiv.org/pdf/2605.04019v1.pdf)

---

## [3. SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment](https://arxiv.org/abs/2605.04012v1)

**作者**：Joseph Breda, Fadi Yousif, Beszel Hawkins 等 33 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Language models excel at diagnostic assessments on currated medical case-studies and vignettes, performing on par with, or better than, clinical professionals. However, existing studies focus on complex scenarios with rich context making it difficult to draw conclusions about how these systems perform for patients reporting symptoms in everyday life. We deployed SymptomAI, a set of conversational AI agents for end-to-end patient interviewing and differential diagnosis (DDx), via the Fitbit app in a study that randomized participants (N=13,917) to interact with five AI agents. This corpus captures diverse communication and a realistic distribution of illnesses from a real world population. A subset of 1,228 participants reported a clinician-provided diagnosis, and 517 of these were further evaluated by a panel of clinicians during over 250 hours of annotation. SymptomAI DDx were significantly more accurate (OR = 2.47, p < 0.001) than those from independent clinicians given the same dialogue in a blinded randomized comparison. Moreover, agentic strategies which conduct a dedicated symptom interview that elicit additional symptom information before providing a diagnosis, perform substantially better than baseline, user-guided conversations (p < 0.001). An auxiliary analysis on 1,509 conversations from a general US population panel validated that these results generalize beyond wearable device users. We used SymptomAI diagnoses as labels for all 13,917 participants to analyze over 500,000 days of wearable metrics across nearly 400 unique conditions. We identified strong associations between acute infections and physiological shifts (e.g., OR > 7 for influenza). While limited by self-reported ground truth, these results demonstrate the benefits of a dedicated and complete symptom interview compared to a user-guided symptom discussion, which is the default of most consumer LLMs.

### 🤖 AI 总结

**一句话总结**：Language models excel at diagnostic assessments on currated medical case-studies and vignettes, performing on par with, or better than, clinical professionals. However, existing studies focus on compl...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, SymptomAI, Towards, Conversational, Everyday, Symptom, Assessment, Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04012v1) | [下载PDF](https://arxiv.org/pdf/2605.04012v1.pdf)

---

## [4. An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration](https://arxiv.org/abs/2605.03989v1)

**作者**：Dutao Zhang, Tian Liao  
**分类**：cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Retrieval-augmented generation systems often assume that one fixed retrieval pipeline is sufficient across heterogeneous tasks, yet factoid question answering, multi-hop reasoning, and scientific verification exhibit different retrieval preferences. We present Experience-RAG Skill, an agent-oriented pluggable retrieval orchestration layer positioned between the agent and the retriever pool. The proposed skill analyzes the current scene, consults an experience memory, selects an appropriate retrieval strategy, and returns structured evidence to the agent. Under a fixed candidate pool, Experience-RAG Skill achieves an overall nDCG@10 of 0.8924 on BeIR/nq, BeIR/hotpotqa, and BeIR/scifact, outperforming fixed single-retriever baselines and remaining competitive with Adaptive-RAG-style routing. The results suggest that retrieval strategy selection can be productively encapsulated as a reusable agent skill rather than being hard-coded in the upper workflow.

### 🤖 AI 总结

**一句话总结**：Retrieval-augmented generation systems often assume that one fixed retrieval pipeline is sufficient across heterogeneous tasks, yet factoid question answering, multi-hop reasoning, and scientific veri...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Agent-Oriented, Pluggable, Experience-RAG, Skill, Experience-Driven, Retrieval, Strategy

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03989v1) | [下载PDF](https://arxiv.org/pdf/2605.03989v1.pdf)

---

## [5. From Intent to Execution: Composing Agentic Workflows with Agent Recommendation](https://arxiv.org/abs/2605.03986v1)

**作者**：Kishan Athrey, Ramin Pishehvar, Brian Riordan 等 4 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Multi-Agent Systems (MAS) built using AI agents fulfill a variety of user intents that may be used to design and build a family of related applications. However, the creation of such MAS currently involves manual composition of the plan, manual selection of appropriate agents, and manual creation of execution graphs. This paper introduces a framework for the automated creation of multi-agent systems which replaces multiple manual steps with an automated framework. The proposed framework consists of software modules and a workflow to orchestrate the requisite task- specific application. The modules include: an LLM-derived planner, a set of tasks described in natural language, a dynamic call graph, an orchestrator for map agents to tasks, and an agent recommender that finds the most suitable agent(s) from local and global agent registries. The agent recommender uses a two-stage information retrieval (IR) system comprising a fast retriever and an LLM-based re-ranker. We implemented a series of experiments exploring the choice of embedders, re- rankers, agent description enrichment, and supervising critique agent. We benchmarked this system end-to-end, evaluating the combination of planning, agent selection, and task completion, with our proposed approach. Our experimental results show that our approach outperforms the state-of-the- art in terms of the recall rate and is more robust and scalable compared to previous approaches. The critique agent holistically reevaluates both agent and tool recommendations against the overall plan. We show that the inclusion of the critique agent further enhances the recall score, proving that the comprehensive review and revision of task-based agent selection is an essential step in building end-to-end multi-agent systems.

### 🤖 AI 总结

**一句话总结**：Multi-Agent Systems (MAS) built using AI agents fulfill a variety of user intents that may be used to design and build a family of related applications. However, the creation of such MAS currently inv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Multi-Agent, Intent, Execution, Composing, Agentic, Workflows, Recommendation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03986v1) | [下载PDF](https://arxiv.org/pdf/2605.03986v1.pdf)

---

## cs.CL

## [6. Safety and accuracy follow different scaling laws in clinical large language models](https://arxiv.org/abs/2605.04039v1)

**作者**：Sebastian Wind, Tri-Thien Nguyen, Jeta Sopa 等 12 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-05

### 📄 论文摘要

Clinical LLMs are often scaled by increasing model size, context length, retrieval complexity, or inference-time compute, with the implicit expectation that higher accuracy implies safer behavior. This assumption is incomplete in medicine, where a few confident, high-risk, or evidence-contradicting errors can matter more than average benchmark performance. We introduce SaFE-Scale, a framework for measuring how clinical LLM safety changes across model scale, evidence quality, retrieval strategy, context exposure, and inference-time compute. To instantiate this framework, we introduce RadSaFE-200, a Radiology Safety-Focused Evaluation benchmark of 200 multiple-choice questions with clinician-defined clean evidence, conflict evidence, and option-level labels for high-risk error, unsafe answer, and evidence contradiction. We evaluated 34 locally deployed LLMs across six deployment conditions: closed-book prompting (zero-shot), clean evidence, conflict evidence, standard RAG, agentic RAG, and max-context prompting. Clean evidence produced the strongest improvement, increasing mean accuracy from 73.5% to 94.1%, while reducing high-risk error from 12.0% to 2.6%, contradiction from 12.7% to 2.3%, and dangerous overconfidence from 8.0% to 1.6%. Standard RAG and agentic RAG did not reproduce this safety profile: agentic RAG improved accuracy over standard RAG and reduced contradiction, but high-risk error and dangerous overconfidence remained elevated. Max-context prompting increased latency without closing the safety gap, and additional inference-time compute produced only limited gains. Worst-case analysis showed that clinically consequential errors concentrated in a small subset of questions. Clinical LLM safety is therefore not a passive consequence of scaling, but a deployment property shaped by evidence quality, retrieval design, context construction, and collective failure behavior.

### 🤖 AI 总结

**一句话总结**：Clinical LLMs are often scaled by increasing model size, context length, retrieval complexity, or inference-time compute, with the implicit expectation that higher accuracy implies safer behavior. Thi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Safety, accuracy, follow, different, scaling, laws, clinical, large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04039v1) | [下载PDF](https://arxiv.org/pdf/2605.04039v1.pdf)

---

## [7. Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems](https://arxiv.org/abs/2605.04018v1)

**作者**：Yilun Zhao, Jinbiao Wei, Tingyu Song 等 6 位作者  
**分类**：cs.CL, cs.IR  
**发布时间**：2026-05-05

### 📄 论文摘要

Reasoning-intensive retrieval aims to surface evidence that supports downstream reasoning rather than merely matching topical similarity. This capability is increasingly important for agentic search systems, where retrievers must provide complementary evidence across iterative search and synthesis. However, existing work remains limited on both evaluation and training: benchmarks such as BRIGHT provide narrow gold sets and evaluate retrievers in isolation, while synthetic training corpora often optimize single-passage relevance rather than evidence portfolio construction. We introduce BRIGHT-Pro, an expert-annotated benchmark that expands each query with multi-aspect gold evidence and evaluates retrievers under both static and agentic search protocols. We further construct RTriever-Synth, an aspect-decomposed synthetic corpus that generates complementary positives and positive-conditioned hard negatives, and use it to LoRA fine-tune RTriever-4B from Qwen3-Embedding-4B. Experiments across lexical, general-purpose, and reasoning-intensive retrievers show that aspect-aware and agentic evaluation expose behaviors hidden by standard metrics, while RTriever-4B substantially improves over its base model.

### 🤖 AI 总结

**一句话总结**：Reasoning-intensive retrieval aims to surface evidence that supports downstream reasoning rather than merely matching topical similarity. This capability is increasingly important for agentic search s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rethinking, Reasoning-Intensive, Retrieval, Evaluating, Advancing, Retrievers, Agentic, Search

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04018v1) | [下载PDF](https://arxiv.org/pdf/2605.04018v1.pdf)

---

## [8. Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments](https://arxiv.org/abs/2605.03971v1)

**作者**：Hao Mi, Qiang Sheng, Shaofei Wang 等 10 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-05

### 📄 论文摘要

Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.

### 🤖 AI 总结

**一句话总结**：Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns f...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, LLM, Logical, Consistency, Bridge, Improving, Hallucination, Detection

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03971v1) | [下载PDF](https://arxiv.org/pdf/2605.03971v1.pdf)

---

## [9. Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators](https://arxiv.org/abs/2605.03969v1)

**作者**：Mohamed Mady, Johannes Reschke, Björn Schuller  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.

### 🤖 AI 总结

**一句话总结**：AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Feature-Augmented, Transformers, Robust, AI-Text, Detection, Across, Domains, Generators

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03969v1) | [下载PDF](https://arxiv.org/pdf/2605.03969v1.pdf)

---

## [10. Atomic Fact-Checking Increases Clinician Trust in Large Language Model Recommendations for Oncology Decision Support: A Randomized Controlled Trial](https://arxiv.org/abs/2605.03916v1)

**作者**：Lisa C. Adams, Linus Marx, Erik Thiele Orberg 等 11 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to traditional explainability approaches?   Findings: In this randomized trial of 356 clinicians generating 7,476 trust ratings, atomic fact-checking produced a large effect on trust (Cohen's d = 0.94), increasing the proportion of clinicians expressing trust from 26.9% to 66.5%. Traditional transparency mechanisms showed a dose-response gradient of improvement over baseline (d = 0.25 to 0.50).   Meaning: Decomposing AI recommendations into individually verifiable claims linked to source guidelines produces substantially higher clinician trust than traditional explainability approaches in high-stakes clinical decisions.

### 🤖 AI 总结

**一句话总结**：Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to tradit...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Atomic, Fact-Checking, Increases, Clinician, Trust, Large, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03916v1) | [下载PDF](https://arxiv.org/pdf/2605.03916v1.pdf)

---

## [11. CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing](https://arxiv.org/abs/2605.03903v1)

**作者**：Zhipeng Xu, Junhao Ji, Zulong Chen 等 13 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-05

### 📄 论文摘要

Large Multimodal Models (LMMs) have recently shown strong performance on Optical Character Recognition (OCR) tasks, demonstrating their promising capability in document literacy. However, their effectiveness in real-world applications remains underexplored, as existing benchmarks adopt task scopes misaligned with practical applications and assume homogeneous acquisition conditions. To address this gap, we introduce CC-OCR V2, a comprehensive and challenging OCR benchmark tailored to real-world document processing. CC-OCR V2 focuses on practical enterprise document processing tasks and incorporates hard and corner cases that are critical yet underrepresented in prior benchmarks, covering 5 major OCR-centric tracks: text recognition, document parsing, document grounding, key information extraction, and document question answering, comprising 7,093 high-difficulty samples. Extensive experiments on 14 advanced LMMs reveal that current models fall short of real-world application requirements. Even state-of-the-art LMMs exhibit substantial performance degradation across diverse tasks and scenarios. These findings reveal a significant gap between performance on current benchmarks and effectiveness in real-world applications. We release the full dataset and evaluation toolkit at https://github.com/eioss/CC-OCR-V2.

### 🤖 AI 总结

**一句话总结**：Large Multimodal Models (LMMs) have recently shown strong performance on Optical Character Recognition (OCR) tasks, demonstrating their promising capability in document literacy. However, their effect...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：V2, CC-OCR, Benchmarking, Large, Multimodal, Models, Literacy, Real-world

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03903v1) | [下载PDF](https://arxiv.org/pdf/2605.03903v1.pdf)

---

## cs.CV

## [12. UniCorrn: Unified Correspondence Transformer Across 2D and 3D](https://arxiv.org/abs/2605.04044v1)

**作者**：Prajnan Goswami, Tianye Ding, Feng Liu 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-05

### 📄 论文摘要

Visual correspondence across image-to-image (2D-2D), image-to-point cloud (2D-3D), and point cloud-to-point cloud (3D-3D) geometric matching forms the foundation for numerous 3D vision tasks. Despite sharing a similar problem structure, current methods use task-specific designs with separate models for each modality combination. We present UniCorrn, the first correspondence model with shared weights that unifies geometric matching across all three tasks. Our key insight is that Transformer attention naturally captures cross-modal feature similarity. We propose a dual-stream decoder that maintains separate appearance and positional feature streams. This design enables end-to-end learning through stack-able layers while supporting flexible query-based correspondence estimation across heterogeneous modalities. Our architecture employs modality-specific backbones followed by shared encoder and decoder components, trained jointly on diverse data combining pseudo point clouds from depth maps with real 3D correspondence annotations. UniCorrn achieves competitive performance on 2D-2D matching and surpasses prior state-of-the-art by 8% on 7Scenes (2D-3D) and 10% on 3DLoMatch (3D-3D) in registration recall. Project website: https://neu-vi.github.io/UniCorrn

### 🤖 AI 总结

**一句话总结**：Visual correspondence across image-to-image (2D-2D), image-to-point cloud (2D-3D), and point cloud-to-point cloud (3D-3D) geometric matching forms the foundation for numerous 3D vision tasks. Despite ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D, 3D, UniCorrn, Unified, Correspondence, Transformer, Across, Visual

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04044v1) | [下载PDF](https://arxiv.org/pdf/2605.04044v1.pdf)

---

## [13. Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035v1)

**作者**：Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi 等 23 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-05

### 📄 论文摘要

We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

### 🤖 AI 总结

**一句话总结**：We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Large-Scale, High-Quality, Gaussian, Head, Reconstruction, Multi-View, Captures

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04035v1) | [下载PDF](https://arxiv.org/pdf/2605.04035v1.pdf)

---

## [14. Enhanced 3D Brain Tumor Segmentation Using Assorted Precision Training](https://arxiv.org/abs/2605.04008v1)

**作者**：Adwaitt Pandya, Ozioma C. Oguine, Harita Bhargava 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-05

### 📄 论文摘要

A brain tumor is a medical disorder faced by individuals of all demographics. Medically, it is described as the spread of non-essential cells close to or throughout the brain. Symptoms of this ailment include headaches, seizures, and sensory changes. This research explores two main categories of brain tumors: benign and malignant. Benign spreads steadily, and malignant expresses growth, making it dangerous. Early identification of brain tumors is a crucial factor for the survival of patients. This research provides a state-of-the-art approach to the early identification of tumors within the brain. We implemented the SegResNet architecture, a widely adopted architecture for three-dimensional segmentation, and trained it using the automatic multi-precision method. We incorporated the dice loss function and dice metric for evaluating the model. We got a dice score of 0.84. For the tumor core, we got a dice score of 0.84; for the whole tumor, 0.90; and for the enhanced tumor, we got a score of 0.79.

### 🤖 AI 总结

**一句话总结**：A brain tumor is a medical disorder faced by individuals of all demographics. Medically, it is described as the spread of non-essential cells close to or throughout the brain. Symptoms of this ailment...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Enhanced, Brain, Tumor, Segmentation, Assorted, Precision, Training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04008v1) | [下载PDF](https://arxiv.org/pdf/2605.04008v1.pdf)

---

## [15. RD-ViT: Recurrent-Depth Vision Transformer for Semantic Segmentation with Reduced Data Dependence Extending the Recurrent-Depth Transformer Architecture to Dense Prediction](https://arxiv.org/abs/2605.03999v1)

**作者**：Renjie He  
**分类**：cs.CV  
**发布时间**：2026-05-05

### 📄 论文摘要

Vision Transformers (ViTs) achieve state-of-the-art segmentation accuracy but require large training datasets because each layer has unique parameters that must be learned independently. We present RD-ViT, a Recurrent-Depth Vision Transformer that adapts the Recurrent-Depth Transformer (RDT) architecture to dense prediction tasks, supporting both 2D and 3D inputs. RD-ViT replaces the deep stack of unique transformer blocks with a single shared block looped T times, augmented with LTI-stable state injection for guaranteed convergence, Adaptive Computation Time (ACT) for spatial compute allocation, depth-wise LoRA adaptation, and optional Mixture-of-Experts (MoE) feed-forward networks for category-specific specialization. We evaluate on the ACDC cardiac MRI segmentation benchmark in both 2D slice-level and 3D volumetric settings with exclusively real experiments executed in Google Colab. In 2D, RD-ViT outperforms standard ViT at 10% training data (Dice 0.774 vs 0.762) and at full data (0.882 vs 0.872). In 3D, RD-ViT with MoE achieves Dice 0.812 with 3.0M parameters, reaching 99.4% of standard ViT performance (0.817) at 53% of the parameter count. MoE expert utilization analysis reveals that different experts spontaneously specialize for different cardiac structures (RV, MYO, LV) without explicit routing supervision. ACT halting maps show higher compute allocation at cardiac boundaries, and the mean ponder time decreases from 2.6 to 1.4 iterations during training, demonstrating learned computational efficiency. Depth extrapolation enables inference with more loops than training without degradation. All code, notebooks, and results are publicly released.

### 🤖 AI 总结

**一句话总结**：Vision Transformers (ViTs) achieve state-of-the-art segmentation accuracy but require large training datasets because each layer has unique parameters that must be learned independently. We present RD...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RD-ViT, Recurrent-Depth, Vision, Transformer, Semantic, Segmentation, Reduced, Data

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03999v1) | [下载PDF](https://arxiv.org/pdf/2605.03999v1.pdf)

---

## [16. 3D Human Face Reconstruction with 3DMM face model from RGB image](https://arxiv.org/abs/2605.03996v1)

**作者**：Zhangnan Jiang, Zichen Yang  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-05-05

### 📄 论文摘要

Nowadays as convolution neural networks demonstrate its powerful problem-solving ability in the area of image processing, efforts have been made to reconstruct detailed face shapes from 2D face images or videos. However, to make the full use of CNN, a large number of labeled data is required to train the network. Coarse morphable face model has been used to synthesize labeled data. However, it is hard for coarse morphable face models to generate photo-realistic data with detail such as wrinkles. In this project, we present a pipeline that reconstructs a human face 3D model from a single RGB image. The pipeline includes face detection, landmark detection, regression of 3DMM model parameters, and soft rendering. Mentor: Zhipeng Fan (Email: zf606@nyu.edu) Code Repository: https://github.com/SeVEnMY/3d-face- reconstruction Code Reference: https://github.com/sicxu/Deep3DFaceRecon pytorch

### 🤖 AI 总结

**一句话总结**：Nowadays as convolution neural networks demonstrate its powerful problem-solving ability in the area of image processing, efforts have been made to reconstruct detailed face shapes from 2D face images...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, Human, Face, Reconstruction, 3DMM, model, RGB, image

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03996v1) | [下载PDF](https://arxiv.org/pdf/2605.03996v1.pdf)

---

## [17. Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning](https://arxiv.org/abs/2605.03968v1)

**作者**：Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini  
**分类**：cs.CV, cs.AI, cs.LG  
**发布时间**：2026-05-05

### 📄 论文摘要

Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.

### 🤖 AI 总结

**一句话总结**：Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Label-Efficient, School, Detection, Aerial, Imagery, via, Weakly, Supervised

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03968v1) | [下载PDF](https://arxiv.org/pdf/2605.03968v1.pdf)

---

## [18. UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning](https://arxiv.org/abs/2605.03950v1)

**作者**：Yifan Wang, Yun Fu  
**分类**：cs.CV  
**发布时间**：2026-05-05

### 📄 论文摘要

Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.

### 🤖 AI 总结

**一句话总结**：Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understa...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UnAC, Adaptive, Visual, Prompting, Abstraction, Stepwise, Checking, Complex

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03950v1) | [下载PDF](https://arxiv.org/pdf/2605.03950v1.pdf)

---

## [19. Reservoir property image slices from the Groningen gas field for image translation and segmentation](https://arxiv.org/abs/2605.03942v1)

**作者**：Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah 等 4 位作者  
**分类**：cs.CV, cs.DB, physics.geo-ph  
**发布时间**：2026-05-05

### 📄 论文摘要

Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.

### 🤖 AI 总结

**一句话总结**：Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for r...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Reservoir, property, image, slices, Groningen, gas, field, translation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03942v1) | [下载PDF](https://arxiv.org/pdf/2605.03942v1.pdf)

---

## [20. A Benchmark for Interactive World Models with a Unified Action Generation Framework](https://arxiv.org/abs/2605.03941v1)

**作者**：Jianjie Fang, Yingshan Lei, Qin Wan 等 11 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.

### 🤖 AI 总结

**一句话总结**：Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action....

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmark, Interactive, World, Models, Unified, Action, Generation, Framework

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03941v1) | [下载PDF](https://arxiv.org/pdf/2605.03941v1.pdf)

---

## [21. StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning](https://arxiv.org/abs/2605.03927v1)

**作者**：Xiaowen Sun, Matthias Kerzel, Mengdi Li 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-05

### 📄 论文摘要

Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：StateVLM, State-Aware, Vision-Language, Model, Robotic, Affordance, Reasoning, models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03927v1) | [下载PDF](https://arxiv.org/pdf/2605.03927v1.pdf)

---

## [22. Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking](https://arxiv.org/abs/2605.03885v1)

**作者**：Susmit Agrawal, Jannis Hollman, Matthias Kümmerer  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-05

### 📄 论文摘要

Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.

### 🤖 AI 总结

**一句话总结**：Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Raising, Ceiling, Better, Empirical, Fixation, Densities, Saliency, Benchmarking

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03885v1) | [下载PDF](https://arxiv.org/pdf/2605.03885v1.pdf)

---

## [23. DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models](https://arxiv.org/abs/2605.03877v1)

**作者**：Qichao Wang, Yunhong Lu, Hengyuan Cao 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Dataset distillation enables efficient training by distilling the information of large-scale datasets into significantly smaller synthetic datasets. Diffusion based paradigms have emerged in recent years, offering novel perspectives for dataset distillation. However, they typically necessitate additional fine-tuning stages, and effective guidance mechanisms remain underexplored. To address these limitations, we rethink diffusion based dataset distillation and propose a Dual Matching Guided Diffusion (DMGD) framework, centered on efficient training-free guidance. We first establish Semantic Matching via conditional likelihood optimization, eliminating the need for auxiliary classifiers. Furthermore, we propose a dynamic guidance mechanism that enhances the diversity of synthetic data while maintaining semantic alignment. Simultaneously, we introduce an optimal transport (OT) based Distribution Matching approach to further align with the target distribution structure. To ensure efficiency, we develop two enhanced strategies for diffusion based framework: Distribution Approximate Matching and Greedy Progressive Matching. These strategies enable effective distribution matching guidance with minimal computational overhead. Experimental results on ImageNet-Woof, ImageNet-Nette, and ImageNet-1K demonstrate that our training-free approach achieves significant improvements, outperforming state-of-the-art (SOTA) methods requiring additional fine-tuning by average accuracy gains of 2.1%, 5.4%, and 2.4%, respectively.

### 🤖 AI 总结

**一句话总结**：Dataset distillation enables efficient training by distilling the information of large-scale datasets into significantly smaller synthetic datasets. Diffusion based paradigms have emerged in recent ye...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, DMGD, Train-Free, Dataset, Distillation, Semantic-Distribution, Matching, Models

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03877v1) | [下载PDF](https://arxiv.org/pdf/2605.03877v1.pdf)

---

## cs.LG

## [24. A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification](https://arxiv.org/abs/2605.04046v1)

**作者**：Sushovan Majhi, Atish Mitra, Žiga Virk 等 4 位作者  
**分类**：cs.LG, math.AT  
**发布时间**：2026-05-05

### 📄 论文摘要

We introduce PALACE (Persistence Adaptive-Landmark Analytic Classification Engine), the data-adaptive companion to PLACE, paying a small cross-validation tier on three knobs (budget, radii, bandwidth; $\leq 5$ choices each). A cover-theoretic core (Lebesgue-number criterion on the landmark cover) yields four closed-form guarantees. (i) A structural lower distortion bound $λ(τ;ν)$ on $\mathcal{D}_n$ under cross-diagram non-interference, with a $(D/L)^2$ budget reduction over the uniform grid when diagrams concentrate. (ii) Equal weights $w_k = K^{-1/2}$ maximizing $λ$, and farthest-point-sampling positions $2$-approximating the optimal $k$-center covering radius; both derived from training labels alone, no gradient training. (iii) A kernel-RKHS classification rate $O((k-1)\sqrt{K}/(γ\sqrt{m_{\min}}))$ with binary necessity threshold $m = Ω(\sqrt K/γ)$ from a matching Le Cam lower bound, and a closed-form filtration-selection rule. The kernel-Mahalanobis margin $\hatρ_{\mathrm{Mah}}$ is the strongest closed-form ranker across the chemical-graph pool (mean Spearman $ρ\approx +0.60$); the isotropic surrogate $\hatγ/\sqrt{K}$ admits a selection-consistency rate, and $\widehatλ$ from (i) provides an independent data-level signal (positive on COX2 and PTC). (iv) A per-prediction certificate, in non-asymptotic Pinelis and asymptotic Gaussian forms, with no calibration split. Empirically, PALACE is the strongest closed-form diagram-based method on Orbit5k ($91.3 \pm 1.0\%$, matching Persformer), leads every diagram-based competitor on COX2 and MUTAG, and is competitive on DHFR (within 1 pp of ECP). At $8\times$ domain inflation, adaptive placement maintains $94\%$ while the uniform grid collapses to chance ($25\%$ on 4-class data).

### 🤖 AI 总结

**一句话总结**：We introduce PALACE (Persistence Adaptive-Landmark Analytic Classification Engine), the data-adaptive companion to PLACE, paying a small cross-validation tier on three knobs (budget, radii, bandwidth;...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, Closed-Form, Adaptive-Landmark, Kernel, Certified, Point-Cloud, Graph, Classification

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.04046v1) | [下载PDF](https://arxiv.org/pdf/2605.04046v1.pdf)

---

## [25. Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes](https://arxiv.org/abs/2605.03984v1)

**作者**：Aaron Havens, Brian Karrer, Neta Shaul  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-05-05

### 📄 论文摘要

Sampling from unnormalized densities is analogous to the generative modeling problem, but the target distribution is defined by a known energy function instead of data samples. Because evaluating the energy function is often costly, a primary challenge is to learn an efficient sampler. We introduce Flow Sampling, a framework built on diffusion models and flow matching for the data-free setting. Our training objective is conditioned on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function. In contrast, diffusion models' objective is conditioned on a data sample and regresses onto a noising diffusion drift. We utilize the interpolant process to minimize the number of energy function evaluations during training, resulting in an efficient and scalable method for sampling unnormalized densities. Furthermore, our formulation naturally extends to Riemannian manifolds, enabling diffusion-based sampling in geometries beyond Euclidean space. We derive a closed-form formula for the conditional drift on constant curvature manifolds, including hyperspheres and hyperbolic spaces. We evaluate Flow Sampling on synthetic energy benchmarks, small peptides, large-scale amortized molecular conformer generation, and distributions supported on the sphere, demonstrating strong empirical performance.

### 🤖 AI 总结

**一句话总结**：Sampling from unnormalized densities is analogous to the generative modeling problem, but the target distribution is defined by a known energy function instead of data samples. Because evaluating the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Flow, Sampling, Learning, Sample, Unnormalized, Densities, via, Denoising

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03984v1) | [下载PDF](https://arxiv.org/pdf/2605.03984v1.pdf)

---

## [26. Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs](https://arxiv.org/abs/2605.03964v1)

**作者**：Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth 等 6 位作者  
**分类**：cs.LG, physics.chem-ph  
**发布时间**：2026-05-05

### 📄 论文摘要

Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.

### 🤖 AI 总结

**一句话总结**：Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Pretrained, Model, Representations, Acquisition, Signals, Active, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03964v1) | [下载PDF](https://arxiv.org/pdf/2605.03964v1.pdf)

---

## [27. Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM](https://arxiv.org/abs/2605.03945v1)

**作者**：Tianyu Wang, Luhao Zhang, Rachel Cummings  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-05

### 📄 论文摘要

Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.

### 🤖 AI 总结

**一句话总结**：Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Integrating, Feature, Correlation, Differential, Privacy, Applications, DP-ERM, Standard

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03945v1) | [下载PDF](https://arxiv.org/pdf/2605.03945v1.pdf)

---

## [28. TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis](https://arxiv.org/abs/2605.03944v1)

**作者**：Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin  
**分类**：cs.LG, cs.AI, stat.ML  
**发布时间**：2026-05-05

### 📄 论文摘要

Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.

### 🤖 AI 总结

**一句话总结**：Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains a...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TabSurv, Adapting, Modern, Tabular, Neural, Networks, Survival, Analysis

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03944v1) | [下载PDF](https://arxiv.org/pdf/2605.03944v1.pdf)

---

## [29. Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes](https://arxiv.org/abs/2605.03921v1)

**作者**：Cyrille Kone, Kevin Jamieson  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-05

### 📄 论文摘要

We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.

### 🤖 AI 总结

**一句话总结**：We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Optimal, Posterior, Sampling, Policy, Identification, Tabular, Markov, Decision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03921v1) | [下载PDF](https://arxiv.org/pdf/2605.03921v1.pdf)

---

## [30. From Data Lifting to Continuous Risk Estimation: A Process-Aware Pipeline for Predictive Monitoring of Clinical Pathways](https://arxiv.org/abs/2605.03895v1)

**作者**：Pasquale Ardimento, Mario Luca Bernardi, Marta Cimitile 等 4 位作者  
**分类**：cs.LG, cs.SE  
**发布时间**：2026-05-05

### 📄 论文摘要

This paper presents a reproducible and process-aware pipeline for predictive monitoring of clinical pathways. The approach integrates data lifting, temporal reconstruction, event log construction, prefix-based representations, and predictive modeling to support continuous reasoning on partially observed patient trajectories, overcoming the limitations of traditional retrospective process mining. The framework is evaluated on COVID-19 clinical pathways using ICU admission as the prediction target, considering 4,479 patient cases and 46,804 prefixes. Predictive models are trained and evaluated using a case-level split, with 896 patients in the test set. Logistic Regression achieves the best performance (AUC 0.906, F1-score 0.835). A detailed prefix-based analysis shows that predictive performance improves progressively as new clinical events become available, with AUC increasing from 0.642 at early stages to 0.942 at later stages of the pathway. The results highlight two key findings: predictive signals emerge progressively along clinical pathways, and process-aware representations enable effective early risk estimation from evolving patient trajectories. Overall, the findings suggest that predictive monitoring in healthcare is best conceived as a continuous, dynamically aware process, in which risk estimates are progressively refined as the patient journey evolves.

### 🤖 AI 总结

**一句话总结**：This paper presents a reproducible and process-aware pipeline for predictive monitoring of clinical pathways. The approach integrates data lifting, temporal reconstruction, event log construction, pre...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data, Lifting, Continuous, Risk, Estimation, Process-Aware, Pipeline, Predictive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.03895v1) | [下载PDF](https://arxiv.org/pdf/2605.03895v1.pdf)

---

