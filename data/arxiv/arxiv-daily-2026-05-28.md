# arXiv AI 论文日报 | 2026-05-28

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (6 篇)
- [cs.CL](#csCL) (11 篇)
- [cs.CV](#csCV) (6 篇)
- [cs.AI](#csAI) (7 篇)

---

## cs.AI

## [1. Calibrating Conservatism for Scalable Oversight](https://arxiv.org/abs/2605.28807v1)

**作者**：William Overman, Mohsen Bayati  
**分类**：cs.AI  
**发布时间**：2026-05-27

### 📄 论文摘要

Agentic AI systems capable of autonomous planning and extended environmental interaction pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed their own capabilities? Existing approaches to scalable oversight rely on complex assumptions, remain largely heuristic, or lack practical methods for sequential settings with statistical guarantees. We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline. Inspired by Attainable Utility Preservation, CCO enables collective conservatism: actions face a penalty proportional to overseer concern, so high-utility actions are still selected when overseers find them unobjectionable and overridden only when concern accumulates. CCO calibrates this conservatism online using Conformal Decision Theory, ensuring that undesirable outcomes remain below a user-specified target threshold with finite-time bounds and no distributional assumptions. On a modified version of SWE-bench, weaker overseers successfully constrain an adversarially misaligned stronger agent; on MACHIAVELLI, CCO substantially reduces ethical violations while preserving reward. In both settings, empirical violation rates closely match the specified targets, as predicted by the theory.

### 🤖 AI 总结

**一句话总结**：Agentic AI systems capable of autonomous planning and extended environmental interaction pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Calibrating, Conservatism, Scalable, Oversight, Agentic, systems, capable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28807v1) | [下载PDF](https://arxiv.org/pdf/2605.28807v1.pdf)

---

## [2. CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models](https://arxiv.org/abs/2605.28792v1)

**作者**：Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago 等 6 位作者  
**分类**：cs.AI, cs.HC, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity. EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing deep learning methods due to two major factors: (1) existing EEG models are predominantly built upon the attention mechanism, incurring quadratic scaling as the sequence length increases, and (2) raw EEG signals must be processed in a sliding-window fashion due to fixed-length input requirements, preventing global understanding of the entire signal. To this extent, we propose CaMBRAIN - the first Causal, Mamba-based state space model (SSM) capable of real-time inference of EEG signals, arguing that bidirectional approaches are needlessly expensive given the causal, unidirectional nature of EEG. However, training such a model is non-trivial, as crucial EEG events can be extremely brief - within fractions of a second - yet separated by long intervals spanning minutes. Current EEG methods use self-supervised objectives that optimize for signal reconstruction, but these are not well suited for streaming SSMs; they fail to explicitly train the hidden state to retain the salient long-range context needed for streaming inference. We therefore introduce a multi-stage self-supervised training pipeline specifically tailored to encourage long-range memory retention and strong performance on EEG signals, while preserving the linear-time complexity of state space models. CaMBRAIN achieves state-of-the-art (SOTA) results across 3 different EEG datasets with >10x higher throughput than existing models, enabling the first model capable of long-range, continuous inference of variable-length EEG signals.

### 🤖 AI 总结

**一句话总结**：Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity. EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CaMBRAIN, Real-time, Continuous, EEG, Inference, Causal, State, Space

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28792v1) | [下载PDF](https://arxiv.org/pdf/2605.28792v1.pdf)

---

## [3. Utility-Aware Multimodal Contrastive Learning for Product Image Generation](https://arxiv.org/abs/2605.28733v1)

**作者**：Xiaohang Feng, Yiling Xie  
**分类**：cs.AI  
**发布时间**：2026-05-27

### 📄 论文摘要

Product images strongly influence consumer decision-making in online marketplaces. Empowered by multimodal contrastive learning, generative AI can output images that closely align with text prompts. Yet existing generative AI models do not directly optimize marketplace performance. This is a critical gap, since semantic alignment alone does not guarantee that an image will sell. To address this limitation, we propose a \textit{utility-aware multimodal contrastive learning} framework that incorporates consumer demand into a novel Utility-Aware InfoNCE loss. Optimizing this utility-aware objective guides generation toward images that are both semantically coherent and demand-enhancing. This effect arises directly from a shift in the learned image-text representation space toward demand-driven visual cues, which we also validate through the theoretical bound of the proposed objective. In downstream applications on Amazon and Airbnb, product images generated and edited by our method outperform state-of-the-art models in increasing demand and preserving fidelity, while maintaining text-image consistency. Notably, our utility-aware framework preserves inverse U-shaped demand patterns for attributes such as aesthetics and uniqueness, improving demand-based performance while preserving fidelity and semantic consistency. Human-subject experiments further validate its commercial effectiveness. As generative AI technology continues to evolve, our utility-aware component can be flexibly embedded into emerging generative models to improve direct commercial use.

### 🤖 AI 总结

**一句话总结**：Product images strongly influence consumer decision-making in online marketplaces. Empowered by multimodal contrastive learning, generative AI can output images that closely align with text prompts. Y...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Utility-Aware, Multimodal, Contrastive, Learning, Product, Image, Generation, images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28733v1) | [下载PDF](https://arxiv.org/pdf/2605.28733v1.pdf)

---

## [4. AlphaTransit: Learning to Design City-scale Transit Routes](https://arxiv.org/abs/2605.28730v1)

**作者**：Bibek Poudel, Sai Swaminathan, Weizi Li  
**分类**：cs.AI  
**发布时间**：2026-05-27

### 📄 论文摘要

Designing a transit network requires many sequential route extension decisions, but their quality is often visible only after the full network is assembled. This delayed-feedback challenge lies at the heart of the Transit Route Network Design Problem (TRNDP), where route interactions can be deceptive: an extension that appears useful locally can create transfer bottlenecks, produce redundant overlap, or reduce overall throughput. To guide route construction under delayed simulator feedback, we introduce AlphaTransit, a search-based planning framework for cityscale bus network design. AlphaTransit couples Monte Carlo Tree Search (MCTS) with a neural policy-value network: the policy proposes route extensions, the value estimates downstream design quality, and search uses these predictions to refine each decision. This provides decision-time lookahead during route construction without running simulator rollouts inside the search tree. We evaluate AlphaTransit on a new Bloomington TRNDP benchmark with realistic road topology and censusderived demand, under mixed and full transit demand settings. In the Bloomington network, AlphaTransit attains the highest service rate in both demand settings, reaching 54.6% and 82.1%, respectively. Relative to reinforcement learning without search, these correspond to 9.9% and 11.4% service rate gains; relative to MCTS without learned guidance, they correspond to 2.5% and 11.2% gains. These results suggest that coupling learned guidance with MCTS is more effective than using either approach alone for transit network design. Our code and data are publicly available in https://github.com/poudel-bibek/AlphaTransit.

### 🤖 AI 总结

**一句话总结**：Designing a transit network requires many sequential route extension decisions, but their quality is often visible only after the full network is assembled. This delayed-feedback challenge lies at the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AlphaTransit, Learning, Design, City-scale, Transit, Routes, Designing, network

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28730v1) | [下载PDF](https://arxiv.org/pdf/2605.28730v1.pdf)

---

## [5. Multi-Adapter Representation Interventions via Energy Calibration](https://arxiv.org/abs/2605.28722v1)

**作者**：Manjiang Yu, Hongji Li, Junwei Chen 等 7 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-27

### 📄 论文摘要

Representation intervention has emerged as a promising paradigm for aligning large language models toward desired behaviors without modifying model weights. Existing methods typically apply a fixed intervention uniformly across all inputs. However, we find that the appropriate intervention direction and strength vary substantially across samples, and such indiscriminate intervention leads to degradation of general capabilities on benign inputs. To address these challenges, we propose Multi-Adapter Representation Interventions via Energy Calibration (MARI). Specifically, we introduce a competitive multi-adapter mechanism in which specialized experts capture non-linear correction patterns and adaptively determine the appropriate intervention direction and strength for different samples. Furthermore, we design an energy-based gating module that leverages internal propagation dynamics to distinguish inputs that are applicable for intervention. Extensive experiments across diverse model families and parameter scales demonstrate that MARI achieves state-of-the-art alignment performance. Our method significantly improves performance on TruthfulQA, BBQ, and safety benchmarks, while maintaining and even improving general capabilities on tasks such as MMLU and ARC. Our code is available at https://github.com/V1centNevwake/MARI.

### 🤖 AI 总结

**一句话总结**：Representation intervention has emerged as a promising paradigm for aligning large language models toward desired behaviors without modifying model weights. Existing methods typically apply a fixed in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Adapter, Representation, Interventions, via, Energy, Calibration, intervention, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28722v1) | [下载PDF](https://arxiv.org/pdf/2605.28722v1.pdf)

---

## [6. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?](https://arxiv.org/abs/2605.28721v1)

**作者**：HuiMing Fan, Xiao Wang, Zheng Chu 等 8 位作者  
**分类**：cs.AI  
**发布时间**：2026-05-27

### 📄 论文摘要

Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledge Dependence (IKD): even with tool access, agents often rely on intrinsic knowledge -- information encoded in the model before retrieval -- rather than on external evidence. Agents answer up to 44.5% of BrowseComp questions without tools, generate more than half of their search queries from internally produced hypotheses rather than retrieved leads, and perform worse than closed-book baselines when answer-supporting evidence is removed. These results suggest that static search benchmarks can reward memory-backed verification rather than evidence-driven discovery, conflating what agents already know with what they can find. We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage. It contains 335 human-authored questions whose answers depend on facts published within the 90 days preceding benchmark construction, drawn from six updated sources and filtered to exclude globally salient events. On LiveBrowseComp, all evaluated agents fall below 2% closed-book accuracy, search-augmented scores drop by 25-40 points relative to BrowseComp, and prior model rankings no longer reliably predict performance. LiveBrowseComp is available at https://huggingface.co/datasets/Forival/LiveBrowseComp.

### 🤖 AI 总结

**一句话总结**：Are LLM-based search agents genuinely searching, or using the web to verify what they already know? We study this question on BrowseComp with three diagnostics. Our analysis reveals Intrinsic Knowledg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, or, LiveBrowseComp, Search, Searching, Just, Verifying, What

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28721v1) | [下载PDF](https://arxiv.org/pdf/2605.28721v1.pdf)

---

## [7. OpenURMA: A Clean-Room Open Implementation of the Unified Bus Protocol](https://arxiv.org/abs/2605.28717v1)

**作者**：Bojie Li  
**分类**：cs.AI, cs.AR, cs.NI  
**发布时间**：2026-05-27

### 📄 论文摘要

Modern datacenter RDMA is bottlenecked at the network interface, not the wire. A NIC running RoCE or InfiniBand holds per-connection state for every (application, remote-endpoint) pair - hundreds of megabytes at 1024-application fanout - and pays a four-traversal PCIe round trip on a 64-byte operation, inflating latency an order of magnitude beyond the wire. Both follow from the Queue Pair over PCIe abstraction RDMA inherits from InfiniBand.   Huawei's Unified Bus (UB), a public 2025 specification, changes the abstraction: it decouples per-application endpoint state from per-host transport state so connection context grows additively, exposes ordering as opt-in, and reaches remote memory through native CPU load/store to an on-chip-bus controller. UB ships in Huawei's closed Ascend 950 silicon.   OpenURMA is the first clean-room open implementation of UB's transport and transaction layers, realised at three tiers - synthesisable RTL on Alveo U50, a cycle-level two-node SystemC simulator, and a gem5 full-system scaffold - each with a matched OpenRoCE (RoCEv2 RC) baseline. The contribution is the implementation, harness, and controlled comparison closed silicon does not admit. On the canonical 64-byte remote fetch - LOAD on UB-spec Sec.8.3, READ on RoCEv2 RC - UB's load/store path delivers ~500 ns end-to-end, 4.37x below the matched baseline (2186 ns), sustains 2.80x higher throughput, and fits in ~14% of a U50's LUTs.

### 🤖 AI 总结

**一句话总结**：Modern datacenter RDMA is bottlenecked at the network interface, not the wire. A NIC running RoCE or InfiniBand holds per-connection state for every (application, remote-endpoint) pair - hundreds of m...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, OpenURMA, Clean-Room, Open, Implementation, Unified, Bus, Protocol

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28717v1) | [下载PDF](https://arxiv.org/pdf/2605.28717v1.pdf)

---

## cs.CL

## [8. VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading](https://arxiv.org/abs/2605.28818v1)

**作者**：Jinzhou Wu, Zhengwu Ma, Jixing Li 等 5 位作者  
**分类**：cs.CL, q-bio.NC  
**发布时间**：2026-05-27

### 📄 论文摘要

Large language models (LLMs) have become increasingly useful computational models of human language processing, but it remains unclear whether vision-language learning makes text representations more human-like during natural reading. Here, we address this question by comparing tightly matched LLM and vision-language model (VLM) pairs under a strictly text-only setting, allowing us to isolate the effect of multimodal training history from online visual input or cross-modal fusion. We evaluate model alignment with a human natural-reading dataset that includes whole-cortex fMRI responses and synchronized eye-tracking saccades. Our findings demonstrate that multimodal pretraining may not confer a uniform, global advantage in human alignment during natural reading, indicating that language-internal representations remain the key factor for modeling human text processing. However, the VLM advantage could emerge more selectively when sentences contain stronger visual semantic content, with converging evidence from both fMRI and eye-movement alignments. Together, our findings provide a controlled in silico framework for testing how visual learning history shapes model-human alignment of language processing, suggesting that multimodal pretraining contributes selectively rather than globally to human-like language representations during natural reading.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) have become increasingly useful computational models of human language processing, but it remains unclear whether vision-language learning makes text representations more ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VLMs, May, Not, Globally, Enhance, Human, Alignment, over

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28818v1) | [下载PDF](https://arxiv.org/pdf/2605.28818v1.pdf)

---

## [9. Self-Improving Language Models with Bidirectional Evolutionary Search](https://arxiv.org/abs/2605.28814v1)

**作者**：Guowei Xu, Zhenting Qi, Huangyuan Su 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Search has been proposed as an effective method for self-improving language models and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as best-of-N sampling and tree search face two fundamental limitations: they are guided by sparse verification signals, and they construct candidates primarily through autoregressive expansion, restricting exploration to regions with substantial model probability mass. To address these, we propose Bidirectional Evolutionary Search (BES), a search framework that couples forward candidate evolution with backward goal decomposition. In the forward search, BES augments standard expansion with evolution operators that recombine partial trajectories to generate candidates that are difficult to obtain from a single model rollout. In the backward search, BES recursively decomposes the original task into checkable subgoals, producing dense intermediate feedback that guides forward search. We provide theoretical motivation showing that candidates generated by expansion-only search are confined to a narrow entropy shell while evolutionary operators can escape it, and that backward search can exponentially reduce the number of required samples to find a correct answer. Experiments show that on challenging post-training tasks where mainstream post-training algorithms fail to improve, BES enables consistent gains, and on three open problem solving benchmarks at inference time, BES outperforms existing open-source frameworks in both average and best-case performance. Code and trained models are available at https://github.com/Embodied-Minds-Lab/BES.

### 🤖 AI 总结

**一句话总结**：Search has been proposed as an effective method for self-improving language models and agentic systems, both for post-training sample generation and for inference. However, widely used methods such as...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Self-Improving, Language, Models, Bidirectional, Evolutionary, Search, has, been

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28814v1) | [下载PDF](https://arxiv.org/pdf/2605.28814v1.pdf)

---

## [10. OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration](https://arxiv.org/abs/2605.28805v1)

**作者**：Xinchen Zhang, Bowei Liu, Jiale Liu 等 10 位作者  
**分类**：cs.CL, cs.AI, cs.CV, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding boxes) outperform textual explanations as meta-verification rationales, enabling efficient rule-based reinforcement learning rewards while avoiding reliance on model-based rewards from auxiliary judge models. Second, decoupling reinforcement learning objectives for binary judgment and meta-verification substantially outperforms joint reward optimization, due to intrinsic differences in output structure and learning dynamics. Based on these insights, we train OmniVerifier-M1, a generalist visual verifier leveraging symbolic meta-verification and decoupled reinforcement learning. OmniVerifier-M1 provides robust verification and fine-grained error localization, and further enables M1-TTS, a verifier-driven agentic generation system achieving dynamic region-level self-correction. This approach paves the way for more reliable, interpretable, and fine-grained multimodal verification, supporting safer and more controllable foundation model deployment.

### 🤖 AI 总结

**一句话总结**：Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OmniVerifier-M1, Multimodal, Meta-Verifier, Explicit, Structured, Recalibration, Visual, outcomes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28805v1) | [下载PDF](https://arxiv.org/pdf/2605.28805v1.pdf)

---

## [11. Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization](https://arxiv.org/abs/2605.28802v1)

**作者**：Beiduo Chen, Pingjun Hong, Ziyun Zhang 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Free-text explanations extend human label variation (HLV) beyond label disagreement by revealing the reasoning and preferences behind annotators' decisions. We study whether large language models (LLMs) can learn and reproduce such annotator-specific label-explanation behavior. Using two sentence-pair tasks with four annotators each -- natural language inference and paraphrase judgment -- we first analyze whether annotators exhibit stable individual patterns. We find that such patterns are weak at the single-annotation level due to strong input-content effects, but become detectable after input-content reduction and annotator-level aggregation. We then compare prompting and supervised fine-tuning (SFT) baselines and propose cross-annotator preference optimization (CAPO), which contrasts a target annotator's response with other valid but less target-specific annotations for the same input. Experiments show that prompting is limited and unstable, SFT better captures annotator-specific behavior, and CAPO further improves aggregation-aware imitation and judge-based attribution while preserving target-specific reasoning patterns under human validation. Overall, our results show that HLV can be learned as annotator-specific label-explanation behavior, suggesting a path toward scalable explanation-based annotation grounded in annotator histories rather than labels alone.

### 🤖 AI 总结

**一句话总结**：Free-text explanations extend human label variation (HLV) beyond label disagreement by revealing the reasoning and preferences behind annotators' decisions. We study whether large language models (LLM...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Human, Label, Variation, Stable, Signal, Learning, Annotator-Specific

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28802v1) | [下载PDF](https://arxiv.org/pdf/2605.28802v1.pdf)

---

## [12. Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay](https://arxiv.org/abs/2605.28782v1)

**作者**：Mariah Al Giptiah Binte Yusoff, Jakin Tan, Bocheng Chen 等 5 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Discourse particles, such as \textit{well} and \textit{kind of}, are crucial components that enable LLMs to ``speak'' more like humans. They are used to convey emotions, intentions, and interpersonal meanings. However, existing studies have not yet built a comprehensive understanding of LLMs' capabilities in handling discourse particles. Moreover, the limited number of studies focuses primarily on high-resource languages such as English, with little attention paid to Southeast Asian languages. In this paper, we (1) propose \textsc{MalayPrag}, a benchmark designed to systematically evaluate and analyze LLMs' capabilities in handling discourse particles in colloquial Malay; and (2) introduce five attributes that provide a linguistically grounded, unified framework for interpreting the pragmatic functions of discourse particles. Applying these two contributions, we prompt ten off-the-shelf LLMs to perform three prediction tasks. The experimental results reveal substantial challenges for current LLMs in accurately connecting discourse particles with their pragmatic functions in Malay. The provision of the five attributes designed in this study is found to significantly improve these connections, highlighting the need for structured scaffolding for models' pragmatic competence.

### 🤖 AI 总结

**一句话总结**：Discourse particles, such as \textit{well} and \textit{kind of}, are crucial components that enable LLMs to ``speak'' more like humans. They are used to convey emotions, intentions, and interpersonal ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Can, Large, Language, Models, Handle, Discourse, Particles?, Case

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28782v1) | [下载PDF](https://arxiv.org/pdf/2605.28782v1.pdf)

---

## [13. The Abstraction Gap in Vision-Language Causal Reasoning](https://arxiv.org/abs/2605.28779v1)

**作者**：Chinh Hoang, Mohammad Rashedul Hasan  
**分类**：cs.CL, cs.CV  
**发布时间**：2026-05-27

### 📄 论文摘要

Vision-language models (VLMs) generate fluent causal explanations, but current evaluations cannot distinguish linguistic plausibility from faithful causal reasoning. We introduce a dual-probe methodology that isolates these properties. The Text-Only Probe measures linguistic quality. The Chain-Text Probe requires models to first generate explicit causal chains. The Abstraction Gap (AG) metric quantifies the normalized performance difference. Evaluating eight VLMs on CAGE (Causal Abstraction Gap Evaluation), a benchmark of 49,500 questions across 5,500 images spanning Pearl's causal hierarchy, we find seven models exhibit AG exceeding 0.50 with text scores of 6--8 but chain scores below 2.5. Fine-tuning on 45,000 chain-annotated examples fails to close the gap. However, one model achieves near-zero AG. The capability exists within current VLM architectures and depends on pretraining and architectural choices. CAGE provides a diagnostic tool for assessing faithful causal reasoning in VLMs.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) generate fluent causal explanations, but current evaluations cannot distinguish linguistic plausibility from faithful causal reasoning. We introduce a dual-probe methodol...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Abstraction, Gap, Vision-Language, Causal, Reasoning, models, VLMs, generate

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28779v1) | [下载PDF](https://arxiv.org/pdf/2605.28779v1.pdf)

---

## [14. Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?](https://arxiv.org/abs/2605.28778v1)

**作者**：Gabrielle Kaili-May Liu, Arman Cohan  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

LLMs' linguistically expressed confidence should faithfully reflect their intrinsic uncertainty. While recent work shows LLMs struggle to use epistemic markers (e.g., "it is likely...") in a human-aligned fashion, it remains unclear whether models can apply their own linguistic confidence framework to associate markers with specific confidence levels in a stable and generalizable way, and how contextual features impact this ability. We conduct the first systematic study of this question, formalizing _marker internal confidence_ (MIC) as the estimated intrinsic confidence a model associates with a specific epistemic marker in a given task domain. We present 7 metrics to evaluate the stability of MICs within and across distributions. Applying our analysis framework to diverse models and tasks, we find that LLMs remain faithfully miscalibrated even under model-centric interpretation of marker meanings, struggling to differentiate markers by internal confidence across distributions despite preserving a somewhat consistent ranking order across tasks. This supplies critical, complementary evidence to existing work toward a holistic understanding of faithful calibration in LLMs, emphasizing the need for more aligned and stable marker use to improve trustworthiness and reliability.

### 🤖 AI 总结

**一句话总结**：LLMs' linguistically expressed confidence should faithfully reflect their intrinsic uncertainty. While recent work shows LLMs struggle to use epistemic markers (e.g., "it is likely...") in a human-ali...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Can, Use, Linguistic, Uncertainty, Markers, Reliably, Reflect

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28778v1) | [下载PDF](https://arxiv.org/pdf/2605.28778v1.pdf)

---

## [15. Agent Explorative Policy Optimization for Multimodal Agentic Reasoning](https://arxiv.org/abs/2605.28774v1)

**作者**：Minki Kang, Shizhe Diao, Ryo Hachiuma 等 7 位作者  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Vision-language models with extended reasoning succeed on complex problems, but many real-world problems require external tools that internal reasoning alone often cannot resolve. Agentic reasoning therefore interleaves two behaviors with a structural asymmetry: thinking (the self-contained default) and tool use (a high-variance auxiliary acting). We refer to this asymmetry as the Thinking-Acting Gap. Under standard RL recipes like GRPO, the gap manifests as two diagnostic symptoms during training: tool use is attempted on only ~30% of rollouts, and when attempted, the tool-using rollouts within a group are all-wrong on ~40% of questions, suppressing the learning signal at the tool calls that needed it. We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection. Across nine multimodal benchmarks and three scales of Qwen3-VL-Thinking, SFT+AXPO outperforms SFT+GRPO at average (+1.8pp Pass@1 and +1.8pp Pass@4 at 8B on average) and 8B with SFT+AXPO surpasses the 32B Base on Pass@4 with 4 times fewer parameters.

### 🤖 AI 总结

**一句话总结**：Vision-language models with extended reasoning succeed on complex problems, but many real-world problems require external tools that internal reasoning alone often cannot resolve. Agentic reasoning th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Explorative, Policy, Optimization, Multimodal, Agentic, Reasoning, Vision-language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28774v1) | [下载PDF](https://arxiv.org/pdf/2605.28774v1.pdf)

---

## [16. Rethinking Memory as Continuously Evolving Connectivity](https://arxiv.org/abs/2605.28773v1)

**作者**：Jizhan Fang, Buqiang Xu, Zhixian Wang 等 15 位作者  
**分类**：cs.CL, cs.AI, cs.LG, cs.MA, cs.MM  
**发布时间**：2026-05-27

### 📄 论文摘要

Existing memory-augmented LLM agents often treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agentic environments where feedback, task variation, and heterogeneous signals continuously reshape what should be remembered and how it should be connected. To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through three stages: initial connection formation, feedback-driven refinement, and long-term consolidation. During execution, FluxMem repairs missing links, prunes interference, aligns abstraction granularity, and distills recurrent successful trajectories into reusable procedural circuits, guided by one metric for memory generalizability and evolutionary maturity. Across three fundamentally distinct benchmarks including LoCoMo, Mind2Web, and GAIA, FluxMem achieves consistent state-of-the-art performance, demonstrating strong adaptation and generalization in complex agentic environments. The code will be open-sourced in https://github.com/zjunlp/LightMem.

### 🤖 AI 总结

**一句话总结**：Existing memory-augmented LLM agents often treat memory as a static repository with pre-defined representations and fixed retrieval pipelines, which is brittle in dynamic agentic environments where fe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Rethinking, Memory, Continuously, Evolving, Connectivity, Existing, memory-augmented

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28773v1) | [下载PDF](https://arxiv.org/pdf/2605.28773v1.pdf)

---

## [17. Stance Detection in Prediction Markets: Addressing Imbalanced Trader Commentary via Counterfactual Augmentation and Market Context](https://arxiv.org/abs/2605.28745v1)

**作者**：Thomas Mbrice  
**分类**：cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Prediction markets such as Polymarket aggregate crowd beliefs into real-time probability estimates, and the comments traders post beneath each market contain rich directional stance signals that prices alone cannot capture. This work introduces the first stance detection study applied to prediction market commentary, a domain characterized by extreme brevity, trader- specific vernacular, and severe class imbalance (only 8.7% of comments oppose the market outcome). RoBERTa-base is fine-tuned across a 4 x 3 ablation: four input configurations ({2- class, 3-class} x {with/without market context}) and three augmentation conditions (baseline, 50% synthetic, 100% synthetic). Synthetic minority-class samples are generated via LLM-driven Pro -> Anti counterfactual flips using the Anthropic API. Results show that (1) market context is the single most impactful factor, raising 3-class Anti recall from 0.10 to 0.45; (2) counterfactual augmentation is conditionally effective, improving Anti F1 in weak configurations (0.10 -> 0.24) while degrading strong ones (2-class-ctx macro F1: 0.68 -> 0.50 at full dose); and (3) 50% augmentation is the optimal dose, with 100% consistently hurting performance. Attention-based interpretability analysis provides mechanistic support for all three findings.

### 🤖 AI 总结

**一句话总结**：Prediction markets such as Polymarket aggregate crowd beliefs into real-time probability estimates, and the comments traders post beneath each market contain rich directional stance signals that price...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stance, Detection, Prediction, Markets, Addressing, Imbalanced, Trader, Commentary

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28745v1) | [下载PDF](https://arxiv.org/pdf/2605.28745v1.pdf)

---

## [18. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems](https://arxiv.org/abs/2605.28732v1)

**作者**：Xinle Deng, Ruobin Zhong, Hujin Peng 等 18 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is crucial to understand how information is synthesized, propagated, or corrupted over time. In this work, we study the new problem of error tracing and attribution in LLM memory systems. We propose a novel framework that transforms memory pipelines into executable memory evolution graphs, enabling fine-grained tracing of operational information flow. We then construct MemTraceBench, a benchmark collected from representative memory systems such as Long-Context, RAG, Mem0, and EverMemOS, to systematically study memory failure modes. We further introduce an automatic attribution method that iteratively traces operation subgraphs to pinpoint the root cause of any failed case. Our analysis reveals that memory failures are systematic, stemming from operation-level issues like information loss and retrieval misalignment. Crucially, we leverage these fine-grained attribution signals to guide downstream prompt optimization, establishing a closed-loop system that automatically corrects faults and boosts end-task performance by up to 7.62%. Code will be released at https://github.com/zjunlp/MemTrace.

### 🤖 AI 总结

**一句话总结**：Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is cr...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MemTrace, Tracing, Attributing, Errors, Large, Language, Model, Memory

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28732v1) | [下载PDF](https://arxiv.org/pdf/2605.28732v1.pdf)

---

## cs.CV

## [19. HarmoVid: Relightful Video Portrait Harmonization](https://arxiv.org/abs/2605.28811v1)

**作者**：Jun Myeong Choi, Jae Shin Yoon, Luchao Qi 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-05-27

### 📄 论文摘要

We present a method for harmonizing the lighting of a foreground video to match a target background scene, adjusting shadows, color tone, and illumination intensity (relightful harmonization). Unlike images, acquiring labeled data for videos, where identical motions are recorded under different lighting conditions, is practically infeasible and non-scalable. While one way to create such paired data is to apply existing image-based harmonization models frame by frame to a video, the resulting outputs often suffer from significant temporal jitters. We overcome this problem by introducing a novel lighting deflickering model that can stabilize the global and local lighting flickering artifacts. Our video diffusion model learns from these upgraded deflickered data with a volume of real and synthetic videos to generate high-quality video harmonization results. We further propose an asymmetric alpha mask conditioning technique to learn the clean boundaries from real videos. Experiments demonstrate that our model achieves strong temporal coherence, naturalness, cleaner boundaries, and physically meaningful lighting behavior, while maintaining strong relighting expressiveness compared to prior image-based and video-based harmonization methods.

### 🤖 AI 总结

**一句话总结**：We present a method for harmonizing the lighting of a foreground video to match a target background scene, adjusting shadows, color tone, and illumination intensity (relightful harmonization). Unlike ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, HarmoVid, Relightful, Video, Portrait, Harmonization, present, method

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28811v1) | [下载PDF](https://arxiv.org/pdf/2605.28811v1.pdf)

---

## [20. AREA: Attribute Extraction and Aggregation for CLIP-Based Class-Incremental Learning](https://arxiv.org/abs/2605.28809v1)

**作者**：Zhen-Hao Xie, Yu-Cheng Shi, Da-Wei Zhou  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Class-Incremental Learning (CIL) is important in building real-world learning systems. In CLIP-based CIL, the model performs classification by comparing similarity between visual and textual embeddings obtained from template prompts, e.g., ``a photo of a [CLASS]''. This seemingly monolithic matching process can be decomposed into two conceptually distinct stages: attribute extraction and attribute aggregation. For example, a model may recognize cat using attributes such as fur texture and whiskers. When learning a new class like car, the model must extract additional attributes like wheels and adjust how they are aggregated in the shared representation space. However, since only data from the current task is available, incremental updates can bias both attribute extraction and aggregation toward new classes, leading to catastrophic forgetting. Therefore, we propose AREA for attribute extraction and aggregation in CLIP-based CIL. To stabilize extraction, we anchor class-level visual and textual attributes on the hyperspherical embedding space via principal geodesic analysis. To stabilize aggregation, we learn lightweight task-specific experts with scoring and residual refinement, regularized by a variational information bottleneck objective. During inference, we perform routing over task attribute manifolds via optimal transport for more concise prediction. Experiments show that AREA consistently outperforms SOTA methods. Code is available at https://github.com/LAMDA-CL/ICML2026-AREA.

### 🤖 AI 总结

**一句话总结**：Class-Incremental Learning (CIL) is important in building real-world learning systems. In CLIP-based CIL, the model performs classification by comparing similarity between visual and textual embedding...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AREA, Attribute, Extraction, Aggregation, CLIP-Based, Class-Incremental, Learning, CIL

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28809v1) | [下载PDF](https://arxiv.org/pdf/2605.28809v1.pdf)

---

## [21. Personal Visual Memory from Explicit and Implicit Evidence](https://arxiv.org/abs/2605.28806v1)

**作者**：Viet Nguyen, Thao Nguyen, Vishal M. Patel 等 4 位作者  
**分类**：cs.CV, cs.CL, cs.IR  
**发布时间**：2026-05-27

### 📄 论文摘要

Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information needed for later questions is typically recoverable from text alone, and most memory systems reduce image turns to generic captions. Yet images often carry personal information that text rarely states -- both explicit evidence, such as recurring user-associated entities, and implicit evidence, such as latent user facts inferred from visual or multimodal cues. We introduce a benchmark for personal visual memory that targets both forms of evidence, and propose VisualMem, a hybrid visual--text architecture that augments a text-memory backend with a structured personal visual memory module. Rather than collapsing images into captions, VisualMem uses conversational context to resolve identity, ownership, and durable user facts. Experiments show that VisualMem substantially outperforms prior memory systems on our benchmark while remaining competitive on standard text-memory benchmarks, indicating that personal visual memory is a distinct and important component of long-term memory for personalized AI agents.

### 🤖 AI 总结

**一句话总结**：Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information nee...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Personal, Visual, Memory, Explicit, Implicit, Evidence, Long-term, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28806v1) | [下载PDF](https://arxiv.org/pdf/2605.28806v1.pdf)

---

## [22. Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling](https://arxiv.org/abs/2605.28803v1)

**作者**：Xinyu Wang, Mingze Li, Sicheng Lyu 等 9 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We challenge this assumption with Omega-QVLA, the first training-free post-training quantization framework that compresses both the language backbone and the entire diffusion action head of a VLA model to a uniform W4A4 precision, eliminating the need for mixed-precision allocation. Omega-QVLA combines a composite SVD-Hadamard rotation that equalizes per-channel weight energy while diffusing residual activation outliers with per-step DiT activation scaling quantization that absorbs dynamic-range drift across denoising steps. On LIBERO, Omega-QVLA compresses Pi 0.5 and GR00T N1.5 to W4A4 with 98.0% and 87.8% task success rates, matching or exceeding their FP16 references of 97.1% and 87.0%, while reducing the static memory footprint by 71.3%. Real-world manipulation experiments further confirm smooth, accurate manipulation where prior methods fail. Code is available at https://github.com/UCMP13753/Omega-QVLA.

### 🤖 AI 总结

**一句话总结**：Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deploym...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Ω-QVLA, Robust, Quantization, Vision-Language-Action, Models, via, Composite, Rotation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28803v1) | [下载PDF](https://arxiv.org/pdf/2605.28803v1.pdf)

---

## [23. Bias Leaves a Gradient Trail: Label-Free Bias Identification via Gradient Probes on Concept Decompositions](https://arxiv.org/abs/2605.28780v1)

**作者**：Thomas Vitry, Kieran Edgeworth, Stefan Wermter 等 4 位作者  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Vision classifiers can exploit spurious correlations, achieving high in-distribution accuracy yet failing under distribution shift. Existing approaches to bias mitigation and analysis often depend on curated datasets, spurious-attribute or group labels, or retraining, which may be infeasible once a model is deployed or the relevant bias is unknown. We present a bias-label-free, post-hoc method for identifying spurious concepts in frozen vision models, relying only on standard class labels from a held-out audit dataset. For each target class, we collect patches from inputs predicted as that class and apply non-negative matrix factorization to intermediate activations to obtain a bank of interpretable concept vectors. Candidate concepts are then ranked with a bias estimator derived from their interaction with backpropagated gradients on misclassified examples: bias concepts tend to get activated when correcting false negatives and suppressed when correcting false positives. On Colored MNIST and Waterbirds the method recovers concepts aligned with the known spurious cue, and on CelebA it surfaces decision-relevant directions that only partially coincide with the annotated gender attribute; suppressing the top-ranked concepts at inference time improves worst-group accuracy by up to 17.9 percentage points on Waterbirds and 10.4 on CelebA without any retraining or parameter updates. Our method identifies decision-relevant spurious directions that need not coincide with annotated ones, providing both an interpretable auditing tool and an actionable debiasing handle for frozen vision models. Code is available at https://github.com/vitryt/label-free-bias-identification.

### 🤖 AI 总结

**一句话总结**：Vision classifiers can exploit spurious correlations, achieving high in-distribution accuracy yet failing under distribution shift. Existing approaches to bias mitigation and analysis often depend on ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Bias, Leaves, Gradient, Trail, Label-Free, Identification, via, Probes

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28780v1) | [下载PDF](https://arxiv.org/pdf/2605.28780v1.pdf)

---

## [24. SeeGroup: Multi-Layer Depth Estimation of Transparent Surfaces via Self-Determined Grouping](https://arxiv.org/abs/2605.28735v1)

**作者**：Hongyu Wen, Jia Deng  
**分类**：cs.CV  
**发布时间**：2026-05-27

### 📄 论文摘要

Transparent objects are common in daily life, and it is important to understand their multilayer depth, including the transparent surface and the objects behind it. Existing methods for multilayer depth typically extend single-layer prediction. They define layers by the front-to-back ordering of 3D points and predict the layers sequentially. However, as layered geometry can admit multiple valid groupings of 3D points into layers, a predefined grouping strategy is inherently restrictive. In this work, we propose SeeGroup, a multi-layer depth estimation method that avoids imposing a predefined grouping and allows the model itself to adaptively assign surfaces to depth maps. We formulate per-pixel multi-layer depth as a point process, treating depth layers as unordered events along each camera ray. This induces a permutation-invariant likelihood over the observed depth layers, yielding a loss that naturally supports arbitrary layer groupings. Experiments demonstrate that our method significantly advances the state of the art of multi-layer depth estimation, improving quadruplet relative depth accuracy on LayeredDepth benchmark from 61.34% to 70.09%. Code is available at https://github.com/princeton-vl/SeeGroup.

### 🤖 AI 总结

**一句话总结**：Transparent objects are common in daily life, and it is important to understand their multilayer depth, including the transparent surface and the objects behind it. Existing methods for multilayer dep...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, SeeGroup, Multi-Layer, Depth, Estimation, Transparent, Surfaces, via

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28735v1) | [下载PDF](https://arxiv.org/pdf/2605.28735v1.pdf)

---

## cs.LG

## [25. PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective](https://arxiv.org/abs/2605.28819v1)

**作者**：Yangyi Huang, Ruotian Peng, Zeju Qiu 等 7 位作者  
**分类**：cs.LG, cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Parameter-efficient finetuning (PEFT) has become the standard approach for adapting large language models, yet evaluations largely emphasize downstream accuracy while overlooking the retention of pretrained capabilities. We argue that PEFT should be assessed through the stability-plasticity dilemma: the trade-off between target-task adaptation and resistance to forgetting. We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention. Across methods, we find distinct stability-plasticity profiles; under comparable parameter budgets, orthogonal finetuning achieves the most favorable Pareto frontier. To explain these differences, we analyze PEFT updates from two geometric perspectives. In weight space, spectral analysis reveals how parameterizations interact with the pretrained singular-value structure. In activation space, retention metrics show whether finetuning preserves or distorts general-capability representations, with forgetting linked to non-isometric representation distortion. Finally, an analysis shows that final SFT checkpoints often overshoot a better target-retention operating point. Inspired by this, we present case studies of a post-hoc improvement with path-wise rewinding.

### 🤖 AI 总结

**一句话总结**：Parameter-efficient finetuning (PEFT) has become the standard approach for adapting large language models, yet evaluations largely emphasize downstream accuracy while overlooking the retention of pret...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：PEFT-Arena, Understanding, Parameter-Efficient, Finetuning, Stability-Plasticity, Perspective, PEFT, has

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28819v1) | [下载PDF](https://arxiv.org/pdf/2605.28819v1.pdf)

---

## [26. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents](https://arxiv.org/abs/2605.28775v1)

**作者**：Suji Kim, Kangsan Kim, Sung Ju Hwang  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical specialization targets, but they remain substantially weaker and exhibit uneven domain-specific failures. A straightforward remedy is to synthesize large-scale training data for the target domain, yet we find that this naive approach yields only marginal improvements. Building on this observation, we introduce LearnWeak, an annotation-free specialization framework for small computer-use agents that uses a stronger reference agent to identify the student's weaknesses in the target domain, synthesize targeted tasks, and construct supervision automatically. LearnWeak further introduces an error-aware specialization objective that disentangles planning and execution errors, enabling more behaviorally precise updates than broad uniform supervision. On OSWorld, LearnWeak achieves average gains of 11.6 and 11.1 percentage points over EvoCUA-8B and OpenCUA-7B, respectively, across eight domains. We also validate that our student-aware dataset generation and training approaches outperform existing autonomous trajectory generation and training baselines. Our work highlights the importance of student awareness in both data synthesis and agent training, pointing toward a more principled and efficient path for specializing small computer-use agents in diverse domains.

### 🤖 AI 总结

**一句话总结**：Computer-use agents (CUAs) have recently made substantial progress, but deploying a separate large expert for each software domain remains expensive. Small open computer-use agents are more practical ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Learn, Weaknesses, Automated, Domain, Specialization, Small, Computer-Use

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28775v1) | [下载PDF](https://arxiv.org/pdf/2605.28775v1.pdf)

---

## [27. Principled Algorithms for Optimizing Generalized Metrics in Multi-Label Learning](https://arxiv.org/abs/2605.28767v1)

**作者**：Mehryar Mohri, Yutao Zhong  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-05-27

### 📄 论文摘要

Many real-world classification tasks require predicting multiple labels per instance, necessitating the optimization of complex evaluation metrics such as the $F$-measure and Jaccard index. While the Empirical Utility Maximization (EUM) framework is natural for these population-level metrics, existing theoretical results are largely limited to asymptotic Bayes-consistency. In this paper, we develop principled learning algorithms for optimizing a broad class of generalized metrics within the EUM framework, grounded in the stronger notion of $H$-consistency. Our key contribution is the design of novel surrogate loss functions for multi-label learning that admit provable $H$-consistency bounds, enabling optimization with non-asymptotic guarantees tailored to the hypothesis class and finite samples. Crucially, we prove these combinatorially formulated surrogates decompose exactly, operating in strictly $O(l)$ time without approximations. Building on this foundation, we introduce MMO (Multi-Label Metric Optimization), a new family of algorithms for optimizing generalized linear-fractional metrics. We validate our approach through extensive experiments, demonstrating robust scalability and superior performance over state-of-the-art continuous baselines on large-scale datasets (MS-COCO, Reuters-21578) in high-sparsity, deep learning regimes. Our results offer both theoretical rigor and practical effectiveness for general multi-label metric optimization.

### 🤖 AI 总结

**一句话总结**：Many real-world classification tasks require predicting multiple labels per instance, necessitating the optimization of complex evaluation metrics such as the $F$-measure and Jaccard index. While the ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Principled, Algorithms, Optimizing, Generalized, Metrics, Multi-Label, Learning, Many

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28767v1) | [下载PDF](https://arxiv.org/pdf/2605.28767v1.pdf)

---

## [28. LLM Zeroth-Order Fine-Tuning is an Inference Workload](https://arxiv.org/abs/2605.28760v1)

**作者**：Zelin Li, Caiwen Ding  
**分类**：cs.LG  
**发布时间**：2026-05-27

### 📄 论文摘要

Zeroth-order (ZO) fine-tuning is attractive for large language models because it replaces backpropagation with forward objective evaluations. Existing implementations nevertheless execute ZO algorithms inside conventional training loops, even though their dominant work is repeated scoring under nearby parameter states. This creates a workload-runtime mismatch: the algorithm asks for structured inference-style scoring, while the system exposes a sequence of fragmented training-loop steps. We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime. On OPT-13B SST-2, the resulting vLLM execution path completes the 20k-step LoZO run in 0.51 estimated training hours versus 4.15 hours for the official LoZO baseline under the matched LoRA-only setting, an 8.13x speedup, while reaching 0.922 final evaluation accuracy and 0.931 final full-validation accuracy. In core-step scaling experiments across OPT-1.3B to OPT-13B, the same runtime reorganization gives 2.34x--7.72x speedups. A MeZO-style high-rank factorized experiment shows that the same runtime paradigm can track a MeZO-like loss trajectory while running up to 2.55x faster. More broadly, representing ZO updates as dynamic adapter states suggests a practical path toward inference-time training, where lightweight adaptation can be scheduled as an inference-like workload rather than as a separate training job.

### 🤖 AI 总结

**一句话总结**：Zeroth-order (ZO) fine-tuning is attractive for large language models because it replaces backpropagation with forward objective evaluations. Existing implementations nevertheless execute ZO algorithm...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, an, ZO, Zeroth-Order, Fine-Tuning, Inference, Workload, attractive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28760v1) | [下载PDF](https://arxiv.org/pdf/2605.28760v1.pdf)

---

## [29. Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL](https://arxiv.org/abs/2605.28751v1)

**作者**：Kunhao Zheng, Pierre Chambon, Juliette Decugis 等 7 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-05-27

### 📄 论文摘要

Linear interpolation between fine-tuned checkpoints has been shown to trace the Pareto front between competing objectives, but whether extrapolative weight averaging can extend such frontiers to new checkpoints useful at inference time, without additional RL training, remains unclear. We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency. Starting from a shared initialization, we train checkpoints under nested unit-test coverage: low-coverage rewards require passing smaller-input tests, while high-coverage rewards require passing progressively larger tests up to the full suite. This sweep reveals the emergence of a correctness-efficiency frontier: on hard problems, higher-coverage reward reduces optimization failures but increases correctness failures, leaving solve rate nearly unchanged. Interpolation between low- and high-coverage checkpoints recovers this frontier, while extrapolation extends it beyond the trained endpoints. Both the frontier and its extrapolative continuation appear across three inference settings, pure reasoning, tool use, and agentic coding, and across two model scales, 32B and 7B. At the problem level, moving along the frontier changes which problems are solved, making extrapolated checkpoints complementary policies in inference-time scaling. Ensembles with extrapolative weight averaging broaden coverage and improve pass@250 on LCB/hard by 3.3% over the best single checkpoint at matched sample budget. These results show that nested unit-test coverage in code RL induces a frontier that extrapolative weight averaging can navigate, extend, and exploit.

### 🤖 AI 总结

**一句话总结**：Linear interpolation between fine-tuned checkpoints has been shown to trace the Pareto front between competing objectives, but whether extrapolative weight averaging can extend such frontiers to new c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：RL, Extrapolative, Weight, Averaging, Reveals, Correctness-Efficiency, Frontiers, Code

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28751v1) | [下载PDF](https://arxiv.org/pdf/2605.28751v1.pdf)

---

## [30. BIRDNet: Mining and Encoding Boolean Implication Knowledge Graphs as Interpretable Deep Neural Networks](https://arxiv.org/abs/2605.28739v1)

**作者**：Tirtharaj Dash  
**分类**：cs.LG, cs.AI, cs.NE, q-bio.QM  
**发布时间**：2026-05-27

### 📄 论文摘要

Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exception binomial test. The mined implications form a typed directed graph, equivalent to a propositional rule base of 2-literal clauses. We encode this graph as the connectivity of a layered neural network, called BIRDNet, in which each hidden unit corresponds to one mined rule and binds only to its two features. We show two consequences of this design: First, the architecture is sparse by construction: at most $2/d$ of the weights in each BIR layer are active, where $d$ is the input dimension. Second, the model is interpretable: every trained unit keeps a stable symbolic identity, so rules can be read off the network without surrogate models. Unlike most neurosymbolic models, BIRDNet does not consume an external rule base; its structural prior is mined from the data. We evaluate BIRDNet on six transcriptomic and proteomic benchmarks. Our results show that BIRDNet stays within 0.02 AUROC of the strongest dense baseline, at a small accuracy cost, while using up to $96\times$ fewer active parameters than an architecture-matched dense MLP. First-layer rules recover known biological signatures across multiple cancer subtypes and tissue types, including canonical amplicons, lineage-defining co-expression modules, and immune-infiltration markers. Data and code are available at: https://github.com/MAHI-Group/BIRDNet.

### 🤖 AI 总结

**一句话总结**：Tabular data in knowledge-rich domains often carries a latent prior in the form of Boolean implication relationships (BIRs) between pairs of features. We mine such relationships with a sparse-exceptio...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, BIRDNet, Mining, Encoding, Boolean, Implication, Knowledge, Graphs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2605.28739v1) | [下载PDF](https://arxiv.org/pdf/2605.28739v1.pdf)

---

