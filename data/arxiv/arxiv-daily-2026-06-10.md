# arXiv AI 论文日报 | 2026-06-10

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.LG](#csLG) (15 篇)
- [cs.CV](#csCV) (8 篇)
- [cs.AI](#csAI) (2 篇)
- [cs.CL](#csCL) (5 篇)

---

## cs.AI

## [1. ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity](https://arxiv.org/abs/2606.11150v1)

**作者**：Andrew Bo Liu, Samira Nedungadi, Bryce Cai 等 6 位作者  
**分类**：cs.AI, cs.CY  
**发布时间**：2026-06-09

### 📄 论文摘要

Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilities Benchmark (ABC-Bench), a suite of tasks to measure agentic biosecurity-relevant capabilities. ABC-Bench evaluates LLM agents on both benign and dual-use biology tasks: writing code to operate liquid handling robots, designing DNA fragments for in vitro assembly, and evading DNA synthesis screening. These tasks require a combination of biology and software expertise. All tested LLM agents outperformed the median expert human baseliner on all three tasks. Agents performed highly on tasks drawing on published knowledge and well-documented protocols, and more weakly on a task requiring novel bioinformatics reasoning. In three wet-lab validation experiments, we found that OpenAI's o4-mini-high produced scripts that, when run on an OpenTrons liquid handling robot, successfully assembled DNA with expected sequences.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also per...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, ABC-Bench, Agentic, Bio-Capabilities, Benchmark, Biosecurity, Large, language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11150v1) | [下载PDF](https://arxiv.org/pdf/2606.11150v1.pdf)

---

## [2. A History-Aware Visually Grounded Critic for Computer Use Agents](https://arxiv.org/abs/2606.11078v1)

**作者**：Jaewoo Lee, Zaid Khan, Archiki Prasad 等 10 位作者  
**分类**：cs.AI, cs.CL, cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, we introduce HiViG, a History-aware Visually Grounded test-time framework, built around a multimodal critic trained on real GUI trajectories to abstract past interactions into a compact record and to evaluate actions with visual grounding. At test time, HiViG integrates the critic into the policy decision loop to provide macro-action history, which summarizes the policy's completed achievements, and visually grounded critique, which verifies raw execution coordinates against the current screenshot to intercept errors before execution. Across web, mobile, and desktop benchmarks, HiViG consistently outperforms existing scalar and verbal critics, improving average success rates over the strongest baseline by 5.8% for Qwen3-VL-32B and 9.0% for Gemini-3-Flash, and demonstrates strong cross-platform generalization. Ablations show that macro-action history mitigates short-sighted planning and visually grounded critique reduces execution errors, with both components being critical for test-time scaling in long-horizon GUI tasks.

### 🤖 AI 总结

**一句话总结**：Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User In...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, History-Aware, Visually, Grounded, Critic, Computer, Use, Various

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11078v1) | [下载PDF](https://arxiv.org/pdf/2606.11078v1.pdf)

---

## cs.CL

## [3. Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127v1)

**作者**：Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu 等 4 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded. We present a controlled study of both questions across gate configurations, recovery strategies, and generator scales, using adversarially injected corpora to provide ground-truth failure labels. We find that exact source provenance improves faithfulness gating for stronger judges, that hallucination and reward gates reject largely disjoint sample populations making both necessary, and that an adaptive recovery pipeline combining failure diagnosis with targeted regeneration achieves higher yield, recovery rate, and injection recall than naive resampling. Downstream fine-tuning quality is driven primarily by generator scale, with filtration and recovery conditions contributing meaningfully but secondarily.

### 🤖 AI 总结

**一句话总结**：Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is ground...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Provenance-Grounded, Gating, Adaptive, Recovery, Synthetic, Post-Training, Data, Curation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11127v1) | [下载PDF](https://arxiv.org/pdf/2606.11127v1.pdf)

---

## [4. PhantomBench: Benchmarking the Non-existential Threat of Language Models](https://arxiv.org/abs/2606.11105v1)

**作者**：Haeji Jung, Hila Gonen  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

Hallucinations, where language models (LMs) generate factually ungrounded responses, pose serious risks, as users tend to blindly rely on them. This is particularly concerning in high-stakes domains, where consequences of such model behavior can lead to significant harms. Despite notable progress in understanding hallucinations, it remains unclear how reliably these models can recognize the limits of their knowledge. We introduce PhantomBench, the first large-scale benchmark of its kind, comprising more than 60K non-existent terms and entities derived from real concepts across diverse domains. Using our benchmark, we evaluate a total of 21 models of various types and sizes. We show staggering hallucination rates across the board (with average rates as high as 86.7% in some cases), and note that even frontier models surprisingly fail to abstain on non-existent concepts, especially when the input presumes their existence. We then show that PhantomBench can serve as a proxy for studying model behavior on rare concepts for which models are more prone to hallucinate. We also provide a pipeline to construct PhantomBench, enabling scalable generation of non-existent concepts tailored to the specific needs of researchers and practitioners.

### 🤖 AI 总结

**一句话总结**：Hallucinations, where language models (LMs) generate factually ungrounded responses, pose serious risks, as users tend to blindly rely on them. This is particularly concerning in high-stakes domains, ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, PhantomBench, Benchmarking, Non-existential, Threat, Language, Models, Hallucinations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11105v1) | [下载PDF](https://arxiv.org/pdf/2606.11105v1.pdf)

---

## [5. VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation](https://arxiv.org/abs/2606.11079v1)

**作者**：Yunan Lu, Ryan Shea, Yusen Zhang 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-09

### 📄 论文摘要

Evaluation remains a critical bottleneck for interactive agent development. Existing evaluation methods often rely on static benchmarks, which fail to capture the dynamic, multi-step nature of agentic behavior and struggle to expose meaningful failure modes. While user-simulation-based evaluation offers a promising alternative, existing simulation frameworks suffer from two major limitations. First, they provide limited mechanisms for evaluating the quality and comprehensiveness of simulated interactions, making it difficult to assess whether a simulator sufficiently explores an agent's capabilities and failure modes. Second, most frameworks are restricted to either UI-only actions or API-only actions, limiting their ability to model the full range of realistic user behaviors. To address these limitations, we propose VISTA, a Versatile Interactive user Simulation Toolkit for Agent evaluation. Our toolkit includes a suite of six metrics for measuring the realism, capability coverage, and interaction effectiveness of simulated interactions. In addition, we develop a hybrid user simulator that integrates both UI-based interactions and API-based interactions, enabling more realistic and comprehensive evaluation across diverse interactive environments. We evaluate VISTA in e-commerce shopping and education customer service settings and demonstrate that it produces more realistic and comprehensive evaluations than existing methods.

### 🤖 AI 总结

**一句话总结**：Evaluation remains a critical bottleneck for interactive agent development. Existing evaluation methods often rely on static benchmarks, which fail to capture the dynamic, multi-step nature of agentic...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, VISTA, Versatile, Interactive, User, Simulation, Toolkit, Evaluation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11079v1) | [下载PDF](https://arxiv.org/pdf/2606.11079v1.pdf)

---

## [6. Modeling Complex Behaviors: Multi-Personality Composition and Dynamic Switching in Vision-Language Models](https://arxiv.org/abs/2606.11074v1)

**作者**：Peiqi Jia, Haonan Jia, Ziqi Miao 等 6 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

With the widespread deployment of Multimodal Large Language Models (MLLMs) in social interaction, understanding and controlling their behavior under complex personality conditions is essential. This paper introduces explicit personality conditioning and establishes a systematic evaluation framework encompassing single-personality induction, multi-personality induction, and personality switching. Experiments show that personality induction improves image captioning performance but can impair performance on tasks requiring precise reasoning, such as visual question answering (VQA). Balancing and residual effects are observed during multi-trait composition and dynamic switching, indicating that model behavior is co-modulated by both previous and current personality constraints. Existing prompt-based personality induction methods show limited transferability to multimodal settings. Our work reveals the dynamic and complex nature of personality modeling in MLLMs and underscores the need for robust, tailored methods for personality induction and evaluation. The code will be released when the paper is accepted.

### 🤖 AI 总结

**一句话总结**：With the widespread deployment of Multimodal Large Language Models (MLLMs) in social interaction, understanding and controlling their behavior under complex personality conditions is essential. This p...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Modeling, Complex, Behaviors, Multi-Personality, Composition, Dynamic, Switching, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11074v1) | [下载PDF](https://arxiv.org/pdf/2606.11074v1.pdf)

---

## [7. T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains](https://arxiv.org/abs/2606.11070v1)

**作者**：Genta Indra Winata, Amartya Chakraborty, Yuzhen Lin 等 15 位作者  
**分类**：cs.CL, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task complexity, realism, and domain diversity, and often fail to capture interactions that span multiple domains, limiting their ability to evaluate agents in realistic multi-step settings that require sustained reasoning and coordination. To address these limitations, we introduce T1-Bench, a high-fidelity, comprehensive benchmark for evaluating agentic systems in realistic customer-facing, multi-domain environments, featuring interleaved scenarios that require structured reasoning across multi-turn user-assistant interactions and substantially increasing both compositional complexity and evaluative rigor across 25 domains of varying difficulty. We evaluate T1-Bench using 12 proprietary and open-weight models, providing a reproducible and standardized framework for assessing agent behavior, tool utilization, and conversational quality in complex, multi-step environments. We further complement automatic evaluation with human judgments to strengthen the assessment of qualitative performance. Overall, T1-Bench substantially advances prior benchmarks by increasing task complexity, interaction depth, and domain coverage in simulated multi-domain environments. To facilitate future research on agentic systems, we will publicly release data and evaluation code as open source.

### 🤖 AI 总结

**一句话总结**：Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task comple...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, T1-Bench, Benchmarking, Multi-Scenario, Real-World, Domains, Recent, advances

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11070v1) | [下载PDF](https://arxiv.org/pdf/2606.11070v1.pdf)

---

## cs.CV

## [8. AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference](https://arxiv.org/abs/2606.11186v1)

**作者**：Hangfeng Liang, Yutao Hu, Yanhan Hu 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Low-light video enhancement (LLVE) remains a challenging task due to severe information degradation under low-illumination conditions. Recent multimodal approaches have significantly improved enhancement performance by incorporating auxiliary modalities, such as event streams and infrared images. However, these methods typically assume the availability of these modalities at inference, which is often not feasible in real-world scenarios. To solve this problem, in this work, we propose AMNet, a unified multimodal framework for LLVE, to support flexible modality-agnostic inference, where auxiliary modalities may be unavailable. To address the issue of modality absence, we introduce a Spatial-Spectral Dual-Gated Translator that learns the correspondence between auxiliary modalities and RGB inputs, producing implicit auxiliary representations to support the robust enhancement. Additionally, to fully facilitate the learning of cross-modal correspondence, we conduct large-scale multimodal pretraining based on the RGB-only dataset with synthetic auxiliary modalities. Extensive experiments demonstrate that AMNet could handle arbitrary inference-time modality combinations and exhibits superior performance for LLVE under modality absence conditions. Code and models are available on the project page.

### 🤖 AI 总结

**一句话总结**：Low-light video enhancement (LLVE) remains a challenging task due to severe information degradation under low-illumination conditions. Recent multimodal approaches have significantly improved enhancem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：AnyMod-LLVE, Low-Light, Video, Enhancement, Modality-Agnostic, Inference, LLVE, remains

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11186v1) | [下载PDF](https://arxiv.org/pdf/2606.11186v1.pdf)

---

## [9. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization](https://arxiv.org/abs/2606.11180v1)

**作者**：Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference. We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students. At inference, the students generate each chunk in only two denoising steps without inference-time CFG, enabling real-time lip synchronization. A lip-sync-specific teacher-trajectory analysis reveals a CFG fidelity-sync tradeoff: no-CFG predictions favor reference fidelity, whereas CFG-guided predictions favor synchronization within a mid-trajectory band. Lip Forcing translates this finding into three analysis-derived components: Sync-Window DMD, a two-step inference schedule, and a SyncNet-based reward. We validate Lip Forcing at two student scales, both distilled from the 14B teacher. The 1.3B student crosses into real-time streaming at 31 FPS, $17.6\times$ faster than its same-scale bidirectional model. The 14B student, the largest diffusion model reported for V2V lip synchronization, runs $39.8\times$ faster than its teacher at comparable reference fidelity. Time-to-first-frame is sub-millisecond at both scales, far below every diffusion baseline.

### 🤖 AI 总结

**一句话总结**：Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Lip, Forcing, Few-Step, Autoregressive, Real-time, Synchronization, Diffusion-based

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11180v1) | [下载PDF](https://arxiv.org/pdf/2606.11180v1.pdf)

---

## [10. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories](https://arxiv.org/abs/2606.11176v1)

**作者**：Kevin Qinghong Lin, Batu EI, Yuhong Shi 等 6 位作者  
**分类**：cs.CV, cs.CL, cs.CY, cs.HC  
**发布时间**：2026-06-09

### 📄 论文摘要

Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (Data2Story), a multi-agent framework that orchestrates specialized roles into a single virtual newsroom. Data2Story contributes two innovations. (i) Claims are evidence-grounded: an Inspector links every number, angle, and asset back to data, code, or an external reference. (ii) Articles are multimodally generative: rather than defaulting to plain text and static charts, Data2Story reasons about what readers will want to see, then deploys multimodal tools, such as interactive maps for geography and audio for music. We evaluate Data2Story on 18 articles, each paired with the originally published expert piece, along four axes: (a) human-agent angle coverage; (b) rubric evaluation with 53 participants across five dimensions; (c) computer-use agents as judges, a cost-saving proxy for how readers navigate interactive articles; and (d) verifiability, where a coding verifier re-executes statements against the data and checks claims against references. Data2Story produces competitive, evidence-traceable multimedia stories, with particular strength in transparency and auditability. Human articles retain an edge in editorial angle, creative design, and presentation. We position Data2Story as a collaborator for journalists, enabling more evidence-based, transparent, and verifiable reporting. Code and demos are available at https://data2story.github.io.

### 🤖 AI 总结

**一句话总结**：Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for con...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Data, Journalist, Transforming, Verifiable, Multimodal, Stories, tells

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11176v1) | [下载PDF](https://arxiv.org/pdf/2606.11176v1.pdf)

---

## [11. Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models](https://arxiv.org/abs/2606.11155v1)

**作者**：An Zhao, Shengyuan Zhang, Zhongjian Sun 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Flow Matching models have demonstrated strong performance across a wide range of generative tasks. However, their reliance on ODE-based iterative sampling incurs substantial computational overhead in inference, which limits their applicability in real-time scenes. While distillation is a promising solution, existing approaches largely borrow from diffusion-based score matching, often failing to exploit the intrinsic geometric structure of flows and suffering from training instability, high variance, and degraded generation quality. In this paper, we propose Mean Flow Distillation (MFD), a novel distillation framework tailored for flow matching models. We theoretically demonstrate that MFD acts as a temporal low-pass filter, effectively suppressing the high-frequency optimization noise inherent in variational score distillation (VSD) while ensuring global trajectory consistency. We further prove the Mean Flow Matching Theorem, establishing that matching expected average velocities is sufficient for strict distribution alignment. Empirically, on challenging tasks of high-dimensional manifolds including 4D occupancy forecasting and text-to-image generation, MFD achieves state-of-the-art performance, enabling high-fidelity single-step generation.

### 🤖 AI 总结

**一句话总结**：Flow Matching models have demonstrated strong performance across a wide range of generative tasks. However, their reliance on ODE-based iterative sampling incurs substantial computational overhead in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Mean, Flow, Distillation, Robust, Stable, Matching, Models, have

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11155v1) | [下载PDF](https://arxiv.org/pdf/2606.11155v1.pdf)

---

## [12. P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning](https://arxiv.org/abs/2606.11152v1)

**作者**：Yikang Yang, Zhanpeng Hu, Youtian Lin 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code. Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. We introduce P3D-Bench, a benchmark for parametric 3D generation. Unlike a 3D mesh, a parametric 3D program exposes explicit dimensions, construction operations and part relations, revealing whether a model recovers a design's structure, not just its appearance. Under a unified protocol, P3D-Bench covers three task families (Text-to-3D, Image-to-3D and Assembly-3D) and scores each output for executability, geometric fidelity, topology, text-grounded constraints, multiview semantic alignment and part-level structure. We evaluate frontier MLLMs and text-only LLMs on 400 text cases, 400 image cases and 203 annotated assemblies, with domain-specific models as reference points. Our extensive evaluation yields three findings. First, assemblies are the hardest setting, where models still fail to compose multiple parts into a coherent structure. Second, models can often recover the global shape and semantic identity of the target object, yet fail to reproduce the precise parametric geometry specified by the input. Third, part-level modeling remains weak on assemblies, where models recover neither the geometry of each part nor the right number of parts. These results position P3D-Bench as a benchmark for evaluating precise parametric geometry and part-level structure in parametric 3D generation.

### 🤖 AI 总结

**一句话总结**：Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world know...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, P3D-Bench, Benchmarking, MLLMs, Parametric, Generation, Structural, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11152v1) | [下载PDF](https://arxiv.org/pdf/2606.11152v1.pdf)

---

## [13. MOFA-VTON: More Fashion Possibilities with Fine-Grained Adaptations in Virtual Try-On](https://arxiv.org/abs/2606.11148v1)

**作者**：Xiaoyu Han, Chenyang Wang, Jing Wang 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Virtual try-on aims to fit an in-shop clothing image onto a specific human body. An optimal virtual try-on method should provide diverse and flexible dressing options, accurately reflecting the varied wearing styles encountered in real-life scenarios, tailored to individual preferences and fashion aspirations. However, current methods predominantly perform a direct replacement of the original clothing with the target clothing, following the same dressing pattern. This limited control over clothing adaptation may result in fixed and monotonous try-on outputs. To delve into More Fashion Possibilities with Fine-Grained Adaptations in Virtual Try-On, we propose a novel virtual try-on method, termed MOFA-VTON, which allows adjustment for clothing adaptations in try-on results through simple sketches by users. Specifically, we first design a mask construction strategy that transforms user-drawn curve sketches into a dual-region mask, replacing the traditional clothing-agnostic mask and providing fine-grained layout guidance for the subsequent generation process. Further, we propose layout adjustment blocks that utilize the cross-attention mechanism to independently learn layout correspondences for upper and lower regions of the human body, refining the spatial arrangement of the two regions. With these implementations, our method enables flexible and fine-grained adaptations of target clothing, overcoming the constraints of a fixed layout. Extensive experiments on VITON-HD and DressCode datasets demonstrate that our proposed MOFA-VTON outperforms previous state-of-the-art methods and provides more fashion possibilities for virtual try-on.

### 🤖 AI 总结

**一句话总结**：Virtual try-on aims to fit an in-shop clothing image onto a specific human body. An optimal virtual try-on method should provide diverse and flexible dressing options, accurately reflecting the varied...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：MOFA-VTON, More, Fashion, Possibilities, Fine-Grained, Adaptations, Virtual, Try-On

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11148v1) | [下载PDF](https://arxiv.org/pdf/2606.11148v1.pdf)

---

## [14. UniPET: a universal network for high-quality PET image denoising across varied dose reduction factors](https://arxiv.org/abs/2606.11131v1)

**作者**：Zhiwen Yang, Yang Zhou, Haowei Chen 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-09

### 📄 论文摘要

Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance degradation when the DRF varies beyond the assumed one in practical applications. To address the challenge posed by varied DRFs, several preliminary studies focus on the task of universal PET image denoising, aiming to train a universal model over low-dose data across DRFs. Nonetheless, these vanilla universal models often struggle with misaligned styles present in different DRF data, leading to the \textit{style elimination issue} with a significant over-smoothing effect. To deal with this issue, we innovatively introduce domain generalization to PET image denoising and propose a universal PET image denoising network (UniPET) to achieve high-quality PET image denoising across diverse DRFs. UniPET comprises two primary innovations: a style alignment network (SAN) and a region-aware learning strategy (RALS). Specifically, SAN utilizes style alignment techniques derived from domain generalization to align and recover styles across different DRFs, ensuring the model's generalizability across various DRFs while effectively preserving styles. Furthermore, to enhance style recovery, RALS distinguishes between flat and stylized regions, exclusively conducting adversarial learning on the latter, thereby more effectively guiding the model's focus towards learning stylized regions. It is demonstrated that our proposed UniPET can adaptively recover different DRF styles and achieve high-quality PET image denoising across DRFs. Comprehensive experiments show that UniPET exhibits comparable performance to individual DRF-specific models at specific DRFs and realizes state-of-the-art performance in universal PET image denoising quantitatively, perceptually, and clinically.

### 🤖 AI 总结

**一句话总结**：Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance deg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：UniPET, universal, network, high-quality, PET, image, denoising, across

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11131v1) | [下载PDF](https://arxiv.org/pdf/2606.11131v1.pdf)

---

## [15. FADA: Accessible fetal ultrasound interpretation and annotation with a selectively distilled unified vision-language model](https://arxiv.org/abs/2606.11106v1)

**作者**：Mahmood Alzubaidi, Uzair Shah, Raden Muaz 等 9 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

A global shortage of trained sonographers limits prenatal ultrasound screening in low- and middle-income countries, where over half of pregnant women receive no skilled sonography. Current deep learning approaches address detection, segmentation, or classification in isolation, each demanding a separate model and expert-specified labels at inference. We present FADA, a unified vision-language model built on Qwen3.5-VL that performs clinical interpretation, classification, detection, and segmentation through a single interpretation-first pipeline without external labels. FADA distills knowledge from four domain-specific foundation models (FetalCLIP, UltraSAM, USF-MAE, UltraFedFM) via offline pre-computed feature caching. Selective distillation, which applies feature alignment only to annotation tasks while interpretation relies on standard fine-tuning, consistently outperforms full distillation across most evaluation axes. The recommended variant, FADA-SKD, achieves 0.8820 mean Dice for segmentation, 0.7671 mAP@0.50 for detection, and 100% structured interpretation compliance. Expert sonographer validation across 237 images confirms clinically acceptable outputs in both autonomous and human-in-the-loop modes, with 73.5% of interpretations scoring perfectly under clinician guidance. The system is trainable on a single consumer GPU and deployable without cloud connectivity. We validate edge deployment by running the compressed 0.8B model on a commodity smartphone (Qualcomm Snapdragon 7 Gen 1, 12 GB RAM) using llama.cpp with GGUF quantization, completing the full 5-phase pipeline in approximately 60 seconds entirely offline. This establishes a practical pathway for integrating AI-assisted fetal assessment with portable ultrasound devices, directly addressing diagnostic access gaps in resource-constrained settings. Code, models, and data are available at https://github.com/mahmoodphd/FADA.

### 🤖 AI 总结

**一句话总结**：A global shortage of trained sonographers limits prenatal ultrasound screening in low- and middle-income countries, where over half of pregnant women receive no skilled sonography. Current deep learni...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FADA, Accessible, fetal, ultrasound, interpretation, annotation, selectively, distilled

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11106v1) | [下载PDF](https://arxiv.org/pdf/2606.11106v1.pdf)

---

## cs.LG

## [16. When to Align, When to Predict: A Phase Diagram for Multimodal Learning](https://arxiv.org/abs/2606.11190v1)

**作者**：Ilay Kamai, Hugues Van Assel, Aviv Regev 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

Cross-modal alignment (CA) and cross-modal prediction (CP) are the dominant paradigms for multimodal representation learning, yet there is no systematic understanding of when each succeeds, when each fails, and when cross-modal training helps at all -- a gap that leaves practitioners, especially in scientific domains like biomedicine or astrophysics, with heterogeneous instruments and multiple levels of organization and measurement, unable to diagnose why standard methods underperform the best single modality. We develop a unified linear framework that addresses both questions. Under a spiked signal-plus-noise model with structured cross-modal nuisance correlation, we derive separation ratios for both objectives that expose complementary failure modes: alignment whitens each modality and fails when nuisance is strongly correlated across views; prediction encodes whatever is cross-predictable through a one-sided whitening, with recovery governed by source-modality quality. The resulting phase diagram partitions multimodal problems into four regimes: Both, CA only, CP only, and Neither. We present a data-driven procedure to locate real-world datasets in this diagram using a small labeled subsample, identifying the preferred objective and prediction direction before any cross-modal training. Experiments on synthetic data, stereo-vision benchmarks, image-caption pairs, and real astrophysical data validate the predictions in the nonlinear regime, including the Neither regime where cross-modal training is actively harmful. Our framework lets practitioners diagnose their multimodal problem and choose the right objective before committing to training. Code to reproduce the results is available at https://github.com/IlayMalinyak/mm_align_vs_pred.

### 🤖 AI 总结

**一句话总结**：Cross-modal alignment (CA) and cross-modal prediction (CP) are the dominant paradigms for multimodal representation learning, yet there is no systematic understanding of when each succeeds, when each ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：When, Align, Predict, Phase, Diagram, Multimodal, Learning, Cross-modal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11190v1) | [下载PDF](https://arxiv.org/pdf/2606.11190v1.pdf)

---

## [17. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents](https://arxiv.org/abs/2606.11182v1)

**作者**：Weixian Xu, Shilong Liu, Mengdi Wang  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

### 🤖 AI 总结

**一句话总结**：In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are larg...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：EEVEE, Towards, Test-time, Prompt, Learning, Real, World, Self-Improving

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11182v1) | [下载PDF](https://arxiv.org/pdf/2606.11182v1.pdf)

---

## [18. Predicting Future Behaviors in Reasoning Models Enables Better Steering](https://arxiv.org/abs/2606.11172v1)

**作者**：Evgenii Kortukov, Piotr Komorowski, Florian Klein 等 8 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue that prior steering work implicitly relies on internal features that detect behavior in already generated text. We show that these detection features are poor predictors of future behavioral outcomes, and thus not the natural intervention target. Instead, we train activation probes to predict future behavior likelihoods from intermediate reasoning steps. These probes predict the most likely behavior with 64%-91% accuracy, revealing a separate type of internal prediction features. Building on these prediction features, we introduce a text-level steering method, Future Probe Controlled Generation. FPCG samples multiple candidate sentences and chooses the best one according to a probe predicting the future behavior likelihood. This enables steering with almost no output quality degradation. FPCG also enables steering in several evaluations where activation steering fails. These results show that distinguishing detection and prediction features enables a more nuanced approach to controlling LRM behaviors.

### 🤖 AI 总结

**一句话总结**：Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue th...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Predicting, Future, Behaviors, Reasoning, Models, Enables, Better, Steering

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11172v1) | [下载PDF](https://arxiv.org/pdf/2606.11172v1.pdf)

---

## [19. Algorithmic and Minimax Complexities in Kernel Bandits](https://arxiv.org/abs/2606.11171v1)

**作者**：Yunbei Xu  
**分类**：cs.LG, cond-mat.stat-mech, cs.IT, math.OC, math.ST  
**发布时间**：2026-06-09

### 📄 论文摘要

Gaussian-process upper confidence bound (GP-UCB) and decision-estimation-coefficient (DEC) methods may appear, at first sight, to belong to different theories. This paper places the two viewpoints in a common algorithmic-information language for frequentist RKHS bandits. GP-UCB fixes an algorithmic, rather than true, Gaussian-process prior and exploits realized-trajectory complexity together with computational tractability, whereas MAMS optimizes a robust class-wide MAIR/DEC envelope. Through the unified MAIR framework and heterogeneous positive-semidefinite algorithmic priors, we generalize both the GP-UCB analysis and the MAMS algorithm, propose a safeguarded master that combines their advantages, and provide a kernel-bandit construction showing that algorithmic complexity can be more informative than class-wide minimax or DEC certificates in overparameterized models. The resulting message is that algorithmic information and class-wide minimax coefficients answer different questions and can lead to different gaps; kernel bandits provide a clean setting in which this distinction becomes mathematically visible.

### 🤖 AI 总结

**一句话总结**：Gaussian-process upper confidence bound (GP-UCB) and decision-estimation-coefficient (DEC) methods may appear, at first sight, to belong to different theories. This paper places the two viewpoints in ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Algorithmic, Minimax, Complexities, Kernel, Bandits, Gaussian-process, upper, confidence

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11171v1) | [下载PDF](https://arxiv.org/pdf/2606.11171v1.pdf)

---

## [20. COGENT: Continuous Graph Emulators with Neural Ordinary Differential Equations for Long-Term Physical Forecasting](https://arxiv.org/abs/2606.11162v1)

**作者**：Zesheng Liu, Maryam Rahnemoonfar  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

In this work, we present COGENT, a continuous graph emulator with Neural Ordinary Differential Equations for long-term physical forecasting on irregular geospatial meshes. COGENT encodes a finite history of system states and associated forcing fields and external forcings with a graph-based history encoder, producing node-wise context vectors that capture both local spatial interactions and temporal evolution. These context vectors initialize and condition a latent Neural Ordinary Differential Equation whose dynamics are driven by interpolated future forcings and explicit relative rollout time. By modeling the forecast trajectory as a continuous latent dynamical system, COGENT can generate predictions at arbitrary future times rather than being restricted to a fixed temporal discretization. A residual decoder maps the resulting latent trajectories back to future physical states, enabling direct multi-step forecasting without repeatedly feeding predicted states back into the model. This formulation combines graph-based spatial representation, history-conditioned latent dynamics, and continuous-time rollout in a unified framework for mesh-based physical simulation emulation. In order to stabilize training with long-horizon supervision, we also propose effective rollout-horizon sampling and a progressive rollout-horizon scheduling strategy. We evaluate COGENT on transient ice-sheet simulations generated by the Ice-sheet and Sea-level System Model, demonstrating improved long-range stability over autoregressive graph baselines. These results suggest that continuous graph Neural ODEs provide a promising methodology for scalable physical forecasting on irregular geospatial meshes, particularly in applications that require stable long-horizon predictions and the ability to query system states at arbitrary times.

### 🤖 AI 总结

**一句话总结**：In this work, we present COGENT, a continuous graph emulator with Neural Ordinary Differential Equations for long-term physical forecasting on irregular geospatial meshes. COGENT encodes a finite hist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：COGENT, Continuous, Graph, Emulators, Neural, Ordinary, Differential, Equations

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11162v1) | [下载PDF](https://arxiv.org/pdf/2606.11162v1.pdf)

---

## [21. OncoTraj: a public benchmark for longitudinal resistance prediction in EGFR-mutant non-small-cell lung cancer on osimertinib](https://arxiv.org/abs/2606.11144v1)

**作者**：Abhijoy Sarkar, Aarchi Singh Thakur  
**分类**：cs.LG, q-bio.GN, q-bio.QM, stat.AP  
**发布时间**：2026-06-09

### 📄 论文摘要

Resistance to first-line osimertinib in EGFR-mutant non-small-cell lung cancer (NSCLC) is the canonical example of predictable clonal evolution under therapeutic pressure, yet no public benchmark exists for training or evaluating computational models on the corresponding longitudinal patient trajectories. We introduce OncoTraj, a public benchmark of 813 EGFR-mutant NSCLC patients receiving first-line osimertinib, harmonized from three real-world clinical-genomic sources: MSK-CHORD (672 patients), AACR Project GENIE BPC NSCLC (34 patients), and the FLAURA molecular-resistance supplement (107 patients). OncoTraj defines three locked tasks: (A) binary classification of progression by a fixed 12-month landmark, (B) regression of time-to-first-progression in days, and (C) six-class classification of the dominant resistance mechanism. We release the harmonized dataset, patient-level train/validation/test splits with an audited no-leakage guarantee, an open-source evaluation harness, and six reference baselines spanning a majority-class predictor, logistic regression, random forest, XGBoost, an LSTM, and a multi-task transformer. With v1's single-timepoint snapshot features, no task clears chance on clean within-source evaluation: the uniformity of this ceiling across every model class localizes the limit to the input modality (single-snapshot tissue NGS rather than serial ctDNA), not the algorithm. The benchmark does recover a reproducible literature-consistent association: TP53 co-mutation raises the 12-month progression rate from 29% to 59% cohort-wide. OncoTraj establishes a reproducible, leakage-audited baseline and converts the modality limit into concrete design requirements for a serial-ctDNA-enriched v2.

### 🤖 AI 总结

**一句话总结**：Resistance to first-line osimertinib in EGFR-mutant non-small-cell lung cancer (NSCLC) is the canonical example of predictable clonal evolution under therapeutic pressure, yet no public benchmark exis...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：OncoTraj, public, benchmark, longitudinal, resistance, prediction, EGFR-mutant, non-small-cell

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11144v1) | [下载PDF](https://arxiv.org/pdf/2606.11144v1.pdf)

---

## [22. First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems](https://arxiv.org/abs/2606.11138v1)

**作者**：Shreya Jha, Timo Schorlepp, Nicholas Geissler 等 5 位作者  
**分类**：cs.LG, math.NA  
**发布时间**：2026-06-09

### 📄 论文摘要

We introduce First-Order Trajectory Matching (FTM), a surrogate-modeling method that learns the first-order local transport of probability mass from trajectories of stochastic systems. By matching the symmetric first-order motion of trajectories, FTM learns the probability current velocity, whose flow preserves time marginals to match ensemble averages, while also capturing current-like trajectory quantities such as fluxes, circulations, and barrier-crossing currents. FTM learns the current velocity directly from trajectories, avoiding drift, diffusion, and score estimation. Our stability analysis separates discretization error from sampling variance and shows that the one-step simulation-free FTM loss is stable when temporal resolution and sample size are properly balanced. Across stochastic dynamical systems and PDE examples, we empirically demonstrate that FTM provides trajectory-aware ensemble predictions at low, deterministic-rollout cost.

### 🤖 AI 总结

**一句话总结**：We introduce First-Order Trajectory Matching (FTM), a surrogate-modeling method that learns the first-order local transport of probability mass from trajectories of stochastic systems. By matching the...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, First-Order, Trajectory, Matching, Fast, Ensemble, Predictions, Chaotic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11138v1) | [下载PDF](https://arxiv.org/pdf/2606.11138v1.pdf)

---

## [23. Robust Regression of General ReLUs with Queries](https://arxiv.org/abs/2606.11130v1)

**作者**：Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

We study the task of agnostically learning general (as opposed to homogeneous) ReLUs under the Gaussian distribution with respect to the squared loss. In the passive learning setting, recent work gave a computationally efficient algorithm that uses $poly(d,1/ε)$ labeled examples and outputs a hypothesis with error $O(opt)+ε$, where $opt$ is the squared loss of the best fit ReLU. Here we focus on the interactive setting, where the learner has some form of query access to the labels of unlabeled examples. Our main result is the first computationally efficient learner that uses $d polylog(1/ε)+\tilde{O}(\min\{1/p, 1/ε\})$ black-box label queries, where $p$ is the bias of the target function, and achieves error $O(opt)+ε$. We complement our algorithmic result by showing that its query complexity bound is qualitatively near-optimal, even ignoring computational constraints. Finally, we establish that query access is essentially necessary to improve on the label complexity of passive learning. Specifically, for pool-based active learning, any active learner requires $\tildeΩ(d/ε)$ labels, unless it draws a super-polynomial number of unlabeled examples.

### 🤖 AI 总结

**一句话总结**：We study the task of agnostically learning general (as opposed to homogeneous) ReLUs under the Gaussian distribution with respect to the squared loss. In the passive learning setting, recent work gave...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, We, Robust, Regression, General, ReLUs, Queries, study

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11130v1) | [下载PDF](https://arxiv.org/pdf/2606.11130v1.pdf)

---

## [24. Overcoming Rank Collapse in Feedback Alignment](https://arxiv.org/abs/2606.11123v1)

**作者**：Gauthier Boeshertz, Razvan Pascanu, Claudia Clopath  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

Backpropagation (BP) is widely viewed as biologically implausible, in part because it requires feedback weights to be the transpose of forward weights for error propagation. Interestingly, when training a network with fixed random feedback weights to circumvent this issue, learning aligns the forward weights with the feedback weights, leading the backpropagated error signal to become an approximation of the standard gradient used by BP. This process, called Feedback Alignment (FA), occurs in MLPs and very shallow CNNs but does not scale well to deeper architectures. In this work, we first investigated differences between BP and FA models, trained on CIFAR10, specifically focusing on the effective rank of the signal. We found that the FA error has a considerably lower rank and hence is constrained to a lower-dimensional subspace compared to BP, limiting exploration of the parameter space. Motivated by this observation, we evaluated two mechanisms for increasing the effective dimensionality of FA: Muon, an optimiser that orthogonalises weight updates; and hidden activity normalisation, which promotes activation orthogonality. Across larger architectures and benchmarks, we find that these methods consistently improve over FA baselines, for example, on CIFAR100 with a Resnet-18, accuracy increases by 9 percentage points. Our results identify low-dimensional gradient dynamics as a key obstacle to scaling FA and suggest that inducing higher-dimensional update geometry is a promising route toward scaling alternatives to backpropagation.

### 🤖 AI 总结

**一句话总结**：Backpropagation (BP) is widely viewed as biologically implausible, in part because it requires feedback weights to be the transpose of forward weights for error propagation. Interestingly, when traini...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BP, Overcoming, Rank, Collapse, Feedback, Alignment, Backpropagation, widely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11123v1) | [下载PDF](https://arxiv.org/pdf/2606.11123v1.pdf)

---

## [25. TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119v1)

**作者**：Heming Zou, Qi Wang, Yun Qu 等 12 位作者  
**分类**：cs.LG, cs.AI, cs.CL  
**发布时间**：2026-06-09

### 📄 论文摘要

Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources to promising prompts, yet they only leverage sample informativeness at the prompt level and neglect variation in prefix-level informativeness across turns within the same rollout. This work targets multi-turn agentic RL by modeling each ReAct-style thought-action-observation turn as a semantically distinct node, allowing budget allocation to extend from prompt roots to turn-level prefixes with further continuations, which naturally forms tree-structured rollouts. We introduce Tree Rollout Allocation for Contrastive Exploration (TRACE), a unified rollout allocation framework that enhances reward contrast within a fixed sampling budget. Technically, TRACE allocates rollout budget to both prompt roots and intermediate prefixes that are most likely to yield mixed terminal rewards. A shared generalizable predictor estimates conditional success probability at these anchors from prefix histories to guide this allocation. The resulting adaptive tree structure enriches outcome-only feedback and amplifies the policy-update signal. Empirically, TRACE achieves competitive performance and efficiency gains on typical agentic benchmarks, e.g., improving Qwen3-14B Multi-Hop QA average accuracy by 2.8 points over competitive baselines at equal sampling cost.

### 🤖 AI 总结

**一句话总结**：Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is o...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TRACE, Unified, Rollout, Budget, Allocation, Framework, Efficient, Agentic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11119v1) | [下载PDF](https://arxiv.org/pdf/2606.11119v1.pdf)

---

## [26. Data-Driven Dynamic Assortment in Online Platforms: Learning about Two Sides](https://arxiv.org/abs/2606.11118v1)

**作者**：Rahul Roy, Nur Sunar, Jayashankar M. Swaminathan  
**分类**：cs.LG, math.OC, math.PR, stat.AP, stat.ML  
**发布时间**：2026-06-09

### 📄 论文摘要

We study a dynamic assortment problem on a two-sided service platform with incomplete information and heterogeneous customers in a discrete-time setting. In each period, a customer arrives seeking service, and the platform chooses an assortment of sellers to display. The customer then proposes a transaction to at most one seller in the assortment according to a multinomial logit choice model. After a fixed number of periods, sellers review the proposals they have received and each chooses at most one customer according to another multinomial logit choice model, after which the cycle repeats. A key challenge is that the platform does not know the choice-model parameters of either customers or sellers in advance. To our knowledge, this is the first study of a dynamic assortment problem in which both sides' choice parameters are unknown. We develop a data-driven algorithm that learns these parameters while optimizing the platform's objective over time. We evaluate performance using regret, which measures revenue loss relative to a clairvoyant benchmark that knows all parameters and customer arrivals in advance. We show that the algorithm's worst-case regret grows polylogarithmically over time, and we derive a matching lower bound, establishing its rate optimality.

### 🤖 AI 总结

**一句话总结**：We study a dynamic assortment problem on a two-sided service platform with incomplete information and heterogeneous customers in a discrete-time setting. In each period, a customer arrives seeking ser...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Data-Driven, Dynamic, Assortment, Online, Platforms, Learning, about, Two

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11118v1) | [下载PDF](https://arxiv.org/pdf/2606.11118v1.pdf)

---

## [27. Limitations of Learning Tanh Neural Networks with Finite Precision](https://arxiv.org/abs/2606.11104v1)

**作者**：Philipp Grohs, Matěj Trödler  
**分类**：cs.LG, stat.ML  
**发布时间**：2026-06-09

### 📄 论文摘要

We investigate limitations of learning $\tanh$ neural networks from point evaluations under finite-precision computations and $L^p$ accuracy guarantees, building on Berner, Grohs, and Voigtländer (2023). Our approach is based on a novel construction of sharply localized bump functions via iterated $\tanh$ activations. Using this mechanism, we show that, in a finite-precision setting, no adaptive randomized algorithm based on $m$ samples can achieve a convergence rate higher than the Monte Carlo rate $O(m^{-1/p})$ in the $L^p$ norm, unless the sampling budget grows exponentially with the size of the network parameters and architecture. The results reveal fundamental limitations imposed by finite precision on the learnability of classes containing localized bump functions, extending previous results for ReLU networks to the $\tanh$ setting.

### 🤖 AI 总结

**一句话总结**：We investigate limitations of learning $\tanh$ neural networks from point evaluations under finite-precision computations and $L^p$ accuracy guarantees, building on Berner, Grohs, and Voigtländer (202...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Limitations, Learning, Tanh, Neural, Networks, Finite, Precision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11104v1) | [下载PDF](https://arxiv.org/pdf/2606.11104v1.pdf)

---

## [28. Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning](https://arxiv.org/abs/2606.11087v1)

**作者**：Zhiyuan Zhou, Andy Peng, Charles Xu 等 7 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issues with stability and affect scalability. In this paper we study the question of whether simple policy improvement schemes at test time alone, leaving stable supervised policy training intact, can be a competitive alternative which sidesteps these issues. To this end, we propose QGF (Q-Guided Flow), an RL algorithm that performs policy optimization entirely at test time. QGF works by pre-training both a reference flow policy (via a standard behavioral cloning objective) and a value function critic and, at test time, using the value gradient to guide the reference policy to generate higher-value actions without any additional policy learning. Empirically, QGF outperforms prior test-time RL methods on single-task and goal-conditioned offline RL benchmarks with high-dimensional action spaces, and is competitive with state-of-the-art training-time algorithms while being much cheaper to run. Moreover, it exhibits favorable scaling with model size by avoiding the instability of actor-critic training, offering a practical and effective alternative RL algorithm with expressive policies.

### 🤖 AI 总结

**一句话总结**：Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Test-Time, Gradient, Guidance, Flow, Policies, Reinforcement, Learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11087v1) | [下载PDF](https://arxiv.org/pdf/2606.11087v1.pdf)

---

## [29. Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081v1)

**作者**：Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-09

### 📄 论文摘要

Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links. Many practical methods reduce communication frequency but still rely on synchronous All-Reduce operations that maintain identical model states and tie progress to global collectives. This can become a bottleneck when bandwidth or worker speed is heterogeneous. We introduce GASLoC, a novel decentralized pre-training algorithm that generalizes the notion of communication acceleration to the recently popular "outer optimizer" to allow a practical gossip-based training framework that is compatible with adaptive optimizers, allows for local optimizer steps, and can utilize sparse randomized peer communication. Empirically, on a number of standard LLM training tasks, we demonstrate that GASLoC outperforms state-of-the-art decentralized algorithms in single step per communication setting for a number of topologies and, unlike existing decentralized methods in the LLM setting, it allows to obtain performance competitive with DiLoCo when utilizing multiple local steps. In the heterogeneous bandwidth setting we demonstrate the advantage of GASLoC showing that it can significantly outperform DiLoCo.

### 🤖 AI 总结

**一句话总结**：Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links. Many practical methods reduce ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Unifying, Local, Communications, Updates, Pretraining, Communication-efficient, pre-training

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11081v1) | [下载PDF](https://arxiv.org/pdf/2606.11081v1.pdf)

---

## [30. Exploring the Design Space of Reward Backpropagation for Flow Matching](https://arxiv.org/abs/2606.11075v1)

**作者**：Ruoyu Wang, Boye Niu, Xiangxin Zhou 等 6 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-09

### 📄 论文摘要

Aligning text-to-image flow matching models with human preferences via direct reward backpropagation is sample-efficient but hampered by two well-known pathologies: activations cannot be stored across the full sampling trajectory at modern model scale, and chained Jacobian products across steps inflate the reward gradient as it travels back to early indices. Connector-based methods, such as LeapAlign, address these issues by replacing the full backward trajectory with a short pinned path, highlighting a useful decoupling between sampling and optimization. However, the quality of the resulting gradient depends on how accurately this short path approximates the full rollout, especially over long intervals. We propose FlowBP, a unified surrogate-trajectory framework that treats the backward trajectory itself as the design object. FlowBP keeps a no-gradient cached rollout for sampling, then builds a lightweight backward surrogate from cached and selectively re-forwarded velocities. This view separates four choices: the reward-model input, active set, integration weights, and bridge coupling, and recovers prior direct-gradient methods as particular settings. Within this framework, we instantiate three variants: FlowBP-Sparse uses sparse Euler reconstruction, FlowBP-Bridge adds controlled bridge coupling, and FlowBP-Lagrange raises the order of leap quadrature. All three bound memory by the active-set size and limit gradient chaining to at most one Jacobian factor. Across SD3.5-M, FLUX.1-dev, and FLUX.2-Klein-base on preference, quality, and compositional metrics, the three variants improve over direct-gradient baselines on most metrics.

### 🤖 AI 总结

**一句话总结**：Aligning text-to-image flow matching models with human preferences via direct reward backpropagation is sample-efficient but hampered by two well-known pathologies: activations cannot be stored across...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Exploring, Design, Space, Reward, Backpropagation, Flow, Matching

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.11075v1) | [下载PDF](https://arxiv.org/pdf/2606.11075v1.pdf)

---

