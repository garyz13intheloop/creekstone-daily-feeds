# arXiv AI 论文日报 | 2026-09-30

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (13 篇)
- [cs.CL](#csCL) (3 篇)
- [cs.LG](#csLG) (9 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning](https://arxiv.org/abs/2609.38147v1)

**作者**：Paras Dahal, Anton Bakhtin, Taco Cohen 等 12 位作者  
**分类**：cs.AI  
**发布时间**：2026-09-29

### 📄 论文摘要

As agents take on longer and more complex problems, controlling the execution becomes a task in its own right. Each step in the run brings new control choices, like which partial work to build on, whether to start fresh, or when to stop. We introduce agentic meta-reasoning, an inference-time harness that makes these choices an explicit and structured reasoning process. Workers carry out the task-level computation, while a controller consolidates what the run has established, explores next options, assesses what each option is worth under the remaining budget, and dispatches the chosen work with context drawn from persistent memory. Between decisions the controller carries only a compact account of the run rather than replaying its full history. Our baselines span production coding agents and research harnesses, together with a Direct Control Agent using the same workers and compute budget allowance. On ProgramBench, which tests long-horizon agentic capability through program reconstruction, meta-reasoning achieves 71.5% with GPT-5.5 against 58.0% for Codex; with Opus 4.8 it achieves 67.2% against 65.5% for Claude Code. On the other benchmarks, spanning abstract reasoning, multi-domain long-horizon reasoning, and proof generation, it gains between 3.6 and 4.2 points over direct control, averaged across three frontier models. It keeps improving over the tested budget ranges where direct control plateaus, though its overhead can hurt at small budgets. Artifact-graph analysis reveals more reuse of earlier work, higher coverage of correct solutions in most settings, and nonuniform gains in final selection. These results indicate that spending computation on structured control becomes more important as agents scale to longer runs.

### 🤖 AI 总结

**一句话总结**：As agents take on longer and more complex problems, controlling the execution becomes a task in its own right. Each step in the run brings new control choices, like which partial work to build on, whe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：As, Thinking, Before, Scaling, Agentic, Inference, Through, Meta-Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38147v1) | [下载PDF](https://arxiv.org/pdf/2609.38147v1.pdf)

---

## [2. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI](https://arxiv.org/abs/2609.38143v1)

**作者**：Cheng Qian, Kunlun Zhu, Beibin Li 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the frozen skill bank to construct harnesses for unseen tasks. Across Harness-Bench and NewtonBench, full-bank meta-skills improve macro-average performance by 8.95 percentage points over no-skill construction, and 12.02 points over direct delivery of the same bank to the Target. These results highlight the value of translating experience into executable support. Gains when the same model serves both roles further suggest a path to system level self-improvement through learning to build better environments.

### 🤖 AI 总结

**一句话总结**：Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Learning, Meta-Skills, Harness, Design, Test-Time, AI4AI, performance

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38143v1) | [下载PDF](https://arxiv.org/pdf/2609.38143v1.pdf)

---

## [3. AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation](https://arxiv.org/abs/2609.38142v1)

**作者**：Rishabh Agrawal, Hejie Cui, Shasha Li 等 5 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice less strongly than those of other corrections. Keeping them less often than the rest improves the model's eventual performance compared to learning from every correction. Motivated by this, our method, Advisor Self-Distillation (AdviSD), pairs outcome-based reinforcement learning with self-distillation from a feedback-conditioned copy of the advisor selectively. Reflection proposes corrections, and the advisor scores the same recorded executor response with and without its issued advice, using the magnitude of the difference to select decisions for supervision. This approach does not require executor likelihoods or additional executor rollouts. Experiments with Qwen3-8B advisors for Gemini and Claude show that AdviSD outperforms advisor-GRPO by 4.2-6.4 percentage points on BFCL-v3 and by 3.9-5.1 score points on EnvScaler. The trained advisors generalize to out-of-domain tasks and transfer across different executor versions and model families. AdviSD also beats matched-count random selection, supporting the value of its selection rule.

### 🤖 AI 总结

**一句话总结**：A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, AdviSD, Learning, Advise, Frontier, via, Targeted, Multi-Turn

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38142v1) | [下载PDF](https://arxiv.org/pdf/2609.38142v1.pdf)

---

## [4. Stochastic World Models for Verifying Vision-Based Neural Feedback Systems](https://arxiv.org/abs/2609.38120v1)

**作者**：I. Samuel Akinwande, Mykel J. Kochenderfer, Clark Barrett  
**分类**：cs.AI, eess.SY  
**发布时间**：2026-09-29

### 📄 论文摘要

Verifying a vision-based neural feedback system requires a model of the observations its controller acts upon. Such a model must capture the variation the sensor produces, while remaining tractable for closed-loop analysis. Generative adversarial networks (GANs) have served as perception surrogates, but they are large, reproduce complex scenes poorly, and are hard to verify. We explore stochastic world models as a richer class of perception surrogates. We train a world model with physically grounded latents, built from operations that standard verifiers bound. It reproduces held-out frames more faithfully than GAN surrogates with up to 130 times as many parameters. To verify these surrogates, we develop a procedure that combines falsification, adaptive refinement, symbolic, and backward analyses. On an emergency braking benchmark with a GAN surrogate, our procedure resolves the entire state space, 38% of which the state-of-the-art verifier left unresolved. On the RGB version of the benchmark, where no verification results have previously been reported, our procedure resolves over 80% of the state space with a world model surrogate.

### 🤖 AI 总结

**一句话总结**：Verifying a vision-based neural feedback system requires a model of the observations its controller acts upon. Such a model must capture the variation the sensor produces, while remaining tractable fo...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Stochastic, World, Models, Verifying, Vision-Based, Neural, Feedback, Systems

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38120v1) | [下载PDF](https://arxiv.org/pdf/2609.38120v1.pdf)

---

## [5. Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution](https://arxiv.org/abs/2609.38108v1)

**作者**：Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera 等 5 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: selecting an appropriate plan for the task and executing it faithfully. Existing planner--executor systems can fail at either stage, while final task success alone cannot distinguish selection from execution failures. We therefore study the Plan Declaration--Execution Gap and introduce Planning-as-Routing, where an LLM declares one of four planning modes: Predefined, Sequential, Hierarchical, or Search, and a deterministic router dispatches the task to the corresponding pattern-specific executor. Across four benchmarks and three LLMs, we find three consistent patterns. First, generic Plan+ReAct often fails to preserve declared planning structure, especially for longer plans: across three benchmarks, only (22)--(45%) of trajectories preserve it, whereas pattern-specific executors enforce the intended structure. Second, planning-mode effectiveness varies across environments and models: Search performs best on ALFWorld, Hierarchical on SWE-bench, and the strongest pattern can vary across models within the same benchmark. Third, the largest gains come from execution: pattern-specific executors improve task success from (0.48) to (0.92) on ALFWorld and from (0.36) to (0.44) on SWE-bench Verified over Plan+ReAct. Current LLMs, however, do not reliably select the strongest mode for each task, although few-shot examples improve selection in some benchmark--model combinations. Overall, reliable agent planning requires both effective mode selection and faithful execution: routing substantially closes the execution gap, while task-specific mode selection remains open.

### 🤖 AI 总结

**一句话总结**：Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Do, LLM, Agent, Execute, Plans, They, Declare?, Planning-Mode

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38108v1) | [下载PDF](https://arxiv.org/pdf/2609.38108v1.pdf)

---

## cs.CL

## [6. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](https://arxiv.org/abs/2609.38169v1)

**作者**：Bingchen Yao, Haobo Xu, Haokun Lin 等 9 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding steps; spatially, errors in different key rows affect model outputs differently, while state magnitudes vary substantially along both rows and columns. Motivated by these observations, we propose STEPQuant, a spatial-temporal post-training quantization framework for Delta-rule recurrent states. STEPQuant allocates precision according to error magnitude and memory lifetime, and jointly fits key-row and value-column scales based on state distributions and key-row impact on output error. Experiments on Qwen3.8-27B and Kimi-Linear-48B-A3B-Instruct across both long- and short-generation benchmarks show that STEPQuant closely matches FP32-state accuracy under a nominal 6-bit budget and outperforms uniform INT8 in its 4-bit configuration. Integrated into SGLang with optimized GPU kernels, 6-bit STEPQuant achieves over 5x recurrent-state compression and reduces total serving memory by up to 68.7%. Our code is available at https://github.com/Dreamer-Toby/STEPQuant.

### 🤖 AI 总结

**一句话总结**：Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recur...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：STEPQuant, When, Where, Errors, Matter, Delta-Rule, Recurrent, State

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38169v1) | [下载PDF](https://arxiv.org/pdf/2609.38169v1.pdf)

---

## [7. LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning](https://arxiv.org/abs/2609.38137v1)

**作者**：Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen 等 4 位作者  
**分类**：cs.CL  
**发布时间**：2026-09-29

### 📄 论文摘要

Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic matching, together with strategic and adaptive reasoning over global and local context. Much of the context is semantically relevant but only a small subset is useful at each step, creating both a challenging search problem and different accuracy--cost tradeoffs across processing strategies. For example, one task requires identifying every person satisfying several conditions using evidence scattered across documents; strategically checking the most selective condition first can narrow the search before verifying the remaining conditions. We evaluate multiple families of frontier language models with four state-of-the-art harnesses. Our benchmarks remain challenging even for strong model--harness combinations: the best reaches 68\% macro-average accuracy across four evaluation suites. More importantly, we find that the same underlying model can exhibit markedly different efficiency under different harnesses. Our results establish efficiency as an important axis for long-context evaluation and provide a testbed for developing harnesses that process context strategically rather than exhaustively.

### 🤖 AI 总结

**一句话总结**：Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harne...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LongHarness, Bench, Stress-Testing, Language, Model, Harnesses, Long-Context, Reasoning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38137v1) | [下载PDF](https://arxiv.org/pdf/2609.38137v1.pdf)

---

## [8. How Local Mixing Encodes Relative Position in Global NoPE Attention](https://arxiv.org/abs/2609.38109v1)

**作者**：Cutter Dawes, Nick Alonso, Tom Figliolia 等 4 位作者  
**分类**：cs.CL, cs.AI, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in global attention layers has recently been shown to be successful at scale. How and why this approach works is not well-understood. In this paper, we develop an explanation of how hybrid models of this sort can implicitly encode position at global NoPE layers. Supported by both theoretical and empirical evidence, our central argument is that SWA and gated linear attention induce a recency bias in the residual stream that propagates to, and is selected by, the global attention logits. Moreover, in contrast to the implicit position encodings found in models with only global NoPE attention, in which positional information arises solely from the causal mask, the recency bias in hybrid models can be maintained across long sequences. In addition to deepening our understanding of how hybrid models encode position, these findings may provide insights for how to encode position in a way that can extrapolate to longer sequence lengths indefinitely.

### 🤖 AI 总结

**一句话总结**：The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：How, Local, Mixing, Encodes, Relative, Position, Global, NoPE

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38109v1) | [下载PDF](https://arxiv.org/pdf/2609.38109v1.pdf)

---

## cs.CV

## [9. Adversarial Training for Pixel Diffusion](https://arxiv.org/abs/2609.38170v1)

**作者**：Xin Lin, Zhifei Zhang, Yuqian Zhou 等 7 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Pixel diffusion models generate RGB images directly, avoiding the bottleneck of an autoencoder, yet their outputs still systematically underrepresent fine-scale natural-image statistics. We show that adversarial learning provides an effective post-training correction for this deficiency. Starting from a pretrained model, we retain its original diffusion or flow-matching objective and add an adversarial loss to the predicted output at non-high-noise timesteps, leaving the model architecture and sampling procedure unchanged. To our knowledge, this is the first systematic study of adversarial post-training for pixel diffusion. Across two pixel backbones, the method jointly improves distribution fidelity, coverage, prompt alignment, and perceptual quality. We further investigate why it works. Frequency-band and power-law analyses show that the original models systematically underproduce natural-image high-frequency content, while adversarial post-training restores this missing spectral power. In contrast, perceptual loss also increases high-frequency content but sacrifices distribution fidelity and prompt alignment. Nearest-neighbor, recall, and matched no-GAN SFT controls further rule out memorization, mode dropping, and additional optimization as simple explanations. Finally, we examine the boundary of this effect. Under the tested latent diffusion configurations, the same procedure does not produce comparable joint gains and adds almost no decoded high-frequency power. These results identify direct output access to the image statistics being corrected as a key factor governing when adversarial post-training succeeds.

### 🤖 AI 总结

**一句话总结**：Pixel diffusion models generate RGB images directly, avoiding the bottleneck of an autoencoder, yet their outputs still systematically underrepresent fine-scale natural-image statistics. We show that ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Adversarial, Training, Pixel, models, generate, RGB, images

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38170v1) | [下载PDF](https://arxiv.org/pdf/2609.38170v1.pdf)

---

## [10. Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163v1)

**作者**：Haoyi Jiang, Liu Liu, Xinjiang Wang 等 15 位作者  
**分类**：cs.CV, cs.RO  
**发布时间**：2026-09-29

### 📄 论文摘要

World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction. We study the design of this space through controlled comparisons, finding that neither reconstruction fidelity nor pre-trained perceptual features alone ensure effective policy learning. These findings motivate ReWAM, a representation-centric world-action model built on pre-trained DINO features. Feature Calibration and a Temporal Representation Bottleneck organize these features into compact world states suited to dynamics modeling. Action-Grounded Representation Shaping routes only action-loss gradients to the bottleneck, thereby letting the policy shape what the representation encodes while the world model learns how it evolves. Without generative video pre-training, ReWAM achieves 93.6% success on RoboTwin 2.0. On RoboDojo, it achieves an average score of 12.29 and a success rate of 8.28% using approximately 600 hours of embodied pre-training data.

### 🤖 AI 总结

**一句话总结**：World-action models jointly learn robot policies and predict future observations, making the representation space an interface between control and prediction. We study the design of this space through...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Rethinking, Representations, World-Action, Modeling, models, jointly, learn, robot

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38163v1) | [下载PDF](https://arxiv.org/pdf/2609.38163v1.pdf)

---

## [11. DMA$^2$: Pixel-space Distribution Matching with Adversarial and Anchor Losses](https://arxiv.org/abs/2609.38156v1)

**作者**：Xin Lin, Zhifei Zhang, Yuqian Zhou 等 9 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Distribution matching distillation (DMD) provides a general framework for few-step diffusion generation, but its modern text-to-image instantiations have been developed primarily around latent diffusion. It therefore overlooks key properties and design opportunities of native RGB. We revisit two DMD interfaces for pixel-space teachers. On the teacher-matching side, diagnostics show low-noise RGB matching is dominated by a local-texture cue, motivating a fixed high-noise matching band. On the real-data side, native clean-RGB outputs allow guidance from an external visual representation without traversing a decoder or sharing the heavy fake-score critic. DINO-Adv removes this critic from the adversarial gradient path and supplies local parametric patch guidance. For distribution-level guidance, we introduce AF-Loss, a parameter-free auxiliary semantic distribution-field objective designed for text-to-image DMD. It operates on detached rolling real and generated supports in the shared DINOv2 space while preserving prompt-conditioned teacher supervision. AF-Loss adds no learnable parameters or inference-time computation. Together these designs form DMA$^2$. Across DPG-Bench, GenEval, VQAScore, and COCO30K, the four-step DMA$^2$ student performs better than the 25-step teacher and evaluated few-step distillers.

### 🤖 AI 总结

**一句话总结**：Distribution matching distillation (DMD) provides a general framework for few-step diffusion generation, but its modern text-to-image instantiations have been developed primarily around latent diffusi...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：DMA$^2$, Pixel-space, Distribution, Matching, Adversarial, Anchor, Losses, distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38156v1) | [下载PDF](https://arxiv.org/pdf/2609.38156v1.pdf)

---

## [12. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies](https://arxiv.org/abs/2609.38155v1)

**作者**：Hui Ren, Lei Fan, Henry Pao 等 8 位作者  
**分类**：cs.CV, cs.AI, cs.CL, cs.IR, cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity unresolved: different objects may share a description, while observations of the same object remain disconnected across events. Retrieving relevant events therefore does not necessarily recover the "biography" of the particular entity a question concerns. To address this, we introduce Grounded Entity Biographies (GEB), a long-video memory framework that groups visually grounded observations of the same physical instance across clips into retrievable biographies while preserving the context of each moment. During question answering, the biography is retrieved alongside episodic evidence, allowing the model to follow an entity through events using identity links established during memory construction. Evaluations across four benchmarks, including day-long and week-long recordings, demonstrate improvements over prior memory frameworks in both multiple-choice and open-ended question answering. On EgoLifeQA, GEB achieves 72.0% accuracy, 4.4 percentage points above the best published result. Ablations show that grounded identity association and biography reading both contribute to the gains, which additional descriptions alone do not fully recover.

### 🤖 AI 总结

**一句话总结**：Answering questions about long videos often requires connecting events involving the same objects across hours or days. Chronological descriptions and text-derived entities can leave physical identity...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Beyond, Timeline, Augmenting, Long-Video, Memory, Grounded, Entity, Biographies

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38155v1) | [下载PDF](https://arxiv.org/pdf/2609.38155v1.pdf)

---

## [13. LongLive-Plug: Once-for-All Distillation for Video Generation](https://arxiv.org/abs/2609.38154v1)

**作者**：Shuai Yang, Luozhou Wang, Wei Huang 等 12 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or to improve long-video generation. This stage is typically repeated for every specialized model. We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs on a base model for training-free, plug-and-play deployment to compatible downstream models. These capabilities include single-pass classifier-free guidance, few-step sampling, and long-context error correction for autoregressive generation. The adapters remain reusable even when downstream models add conditioning branches, expand output channels. Despite training at a fixed guidance scale, our dedicated CFG LoRA provides text guidance control through its inference weight. Combining it with a few-step LoRA simultaneously preserves few-step generation and CFG controllability on downstream tasks. We verify training-free deployment on 54 downstream models across three backbone families and eight task categories, including world modeling, robotics, editing, and multimodal generation. The approach may support additional compatible models. Each capability can thus be distilled once per backbone family and reused without per-target retraining.

### 🤖 AI 总结

**一句话总结**：Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, LongLive-Plug, Once-for-All, Distillation, Video, Generation, models, increasingly

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38154v1) | [下载PDF](https://arxiv.org/pdf/2609.38154v1.pdf)

---

## [14. PowerSim: Differentiable Physics Simulation and Rendering with Power Diagrams](https://arxiv.org/abs/2609.38153v1)

**作者**：Trong-Tung Nguyen, Anand Bhattad  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

We introduce PowerSim, a method to bring physically grounded, differentiable dynamics to PowerFoam's power diagram based 3D representation. PowerSim directly couples a pre-trained PowerFoam scene to the Material Point Method (MPM) by exploiting a natural alignment between the two: the geometric and appearance properties of each primitive correspond closely to the quantities MPM already tracks as an object deforms. Consequently, simulated motion can drive the scene's geometry and appearance directly, without an auxiliary representation in between. Built on this framework, we enable a range of applications on real and synthetic scenes: (1) simulating a static scene under user interaction, (2) recovering spatially varying material fields, (3) compositing primitives from independently captured scenes into a single simulation-ready scene and (4) ray-tracing reflections that update consistently as the object deforms. Our results suggest that PowerSim excels over previous frameworks for physically grounded dynamics, while unlocking unique advantages-such as secondary ray lighting effects on dynamic scenes. Results are best viewed on our project website: https://power-sim.github.io/.

### 🤖 AI 总结

**一句话总结**：We introduce PowerSim, a method to bring physically grounded, differentiable dynamics to PowerFoam's power diagram based 3D representation. PowerSim directly couples a pre-trained PowerFoam scene to t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：We, PowerSim, Differentiable, Physics, Simulation, Rendering, Power, Diagrams

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38153v1) | [下载PDF](https://arxiv.org/pdf/2609.38153v1.pdf)

---

## [15. FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)

**作者**：Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

We introduce FracGen, a fracture-aware video generation model that produces plausible, controllable fracture dynamics from a single image of an intact object, conditioned on physics signals. To train FracGen, we build FracSim, a fracture-aware simulation framework that augments material point method (MPM) simulation with a continuum damage model, producing paired fracture videos and dense, pixel-aligned physical fields at no additional cost beyond standard rendering. FracGen leverages these maps in two ways: it is trained to jointly predict them alongside RGB video, encouraging the model to capture physical state rather than surface appearance; and it is supervised with physics-informed losses that encourage consistency among the predicted maps. As a result, FracGen captures distinct material-specific fracture behavior without expensive test-time simulation or per-scene tuning, while offering fine-grained control over where an object tears, how fast the crack propagates, and how much deformation precedes failure. We further introduce a benchmark for evaluating the physical plausibility of generated fracture video, and show through extensive experiments that FracGen outperforms existing video generation baselines in both physical and visual fidelity. Results are best viewed in our project website: https://fracgen.github.io/.

### 🤖 AI 总结

**一句话总结**：We introduce FracGen, a fracture-aware video generation model that produces plausible, controllable fracture dynamics from a single image of an intact object, conditioned on physics signals. To train ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：FracGen, Learning, How, Objects, Stretch, Tear, Physics-Informed, Video

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38152v1) | [下载PDF](https://arxiv.org/pdf/2609.38152v1.pdf)

---

## [16. CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer](https://arxiv.org/abs/2609.38136v1)

**作者**：Teng Zhou, Yunhao Chen  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference appear in the generated output. Although prior data-driven and training-free methods can reduce leakage, they often face a leakage-degradation dilemma: stronger content suppression may weaken style fidelity, while richer style preservation may reintroduce unwanted reference content. We identify this dilemma across the full style-transfer pipeline, including feature separation, feature-space grounding, and diffusion generation. To address these issues, we propose CLeaR, a training-free framework for content-leakage-resistant style transfer. CLeaR first uses Orthogonal Subspace Projection to define content-reduced style targets in each vision foundation model (VFM) feature space. It then performs Ensemble Inversion, which optimizes a shared pixel-space style anchor satisfying style constraints across multiple VFMs. Finally, Energy-Guided Calibration maintains style alignment during diffusion sampling by steering the denoising trajectory toward the ensemble-defined style manifold. We further provide a theoretical analysis showing that the style-anchor estimation error decreases with the number of VFMs. Experiments on StyleBench demonstrate that CLeaR improves style alignment, reduces content leakage, and achieves better LLM-as-Judge evaluation compared with existing methods. The code is available at \href{https://github.com/0606zt/CLeaR}{https://github.com/0606zt/CLeaR}.

### 🤖 AI 总结

**一句话总结**：Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference ap...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：CLeaR, Unified, Framework, Resolving, Leakage-Degradation, Dilemma, Style, Transfer

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38136v1) | [下载PDF](https://arxiv.org/pdf/2609.38136v1.pdf)

---

## [17. HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)

**作者**：Lei Ke, Jiahao Pan, Zeyue Tian 等 16 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time. Yet prevailing interactive world models remain strictly silent, focusing exclusively on visual rendering and control while overlooking the acoustic dimension. We present HelixWorld, a real-time interactive audio-visual world model where visual scenes and camera-grounded spatial stereo sound co-evolve natively under user interaction. We curate a high-fidelity spatial audio-visual dataset with true stereo acoustics and metric camera poses, upon which we pre-train a bidirectional teacher conditioned on 6-DoF camera trajectories and user actions. To enable low-latency causal interaction, we distill the teacher into a few-step streaming student via an online trajectory distillation loss, sustaining drift-free joint audio-visual rollouts at 24 FPS on a single GPU. Furthermore, we formalize spatial-acoustic consistency and introduce HelixBench to evaluate whether synthesized sound fields faithfully track dynamic viewpoint motion. Extensive experiments demonstrate that HelixWorld matches state-of-the-art silent world models in visual fidelity and responsiveness, while significantly surpassing existing baselines in camera-aligned spatial-acoustic immersion.

### 🤖 AI 总结

**一句话总结**：World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time. Yet prevailing interactive world models remain strictly silent, focusing exclusively on v...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：HelixWorld, Real-time, Interactive, Audio-Visual, World, Model, simulation, inherently

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38123v1) | [下载PDF](https://arxiv.org/pdf/2609.38123v1.pdf)

---

## [18. VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents](https://arxiv.org/abs/2609.38119v1)

**作者**：Jinfa Huang, Jianming Xu, Jingyang Lin 等 5 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Long-form video understanding requires multimodal agents to iteratively gather evidence over many reasoning steps. However, most existing agentic methods suffer from semantic thrashing: as append-only working memory grows, attention to key evidence collapses, and the agent loses access to what it has already found. First, we provide a structural argument showing that append-only memory can incorporate newly observed target evidence, but cannot remove accumulated noise or prevent ordered context growth without a rewrite operator. Second, motivated by this analysis, we propose VideoLoop, a multimodal agent with two coupled loops. The outer loop reasons over the video and the inner loop, after each step, retrieves artifacts from an unbounded filesystem of past observations and intermediate analysis, and rewrites a bounded working memory. Extensive experiments demonstrate the effectiveness of VideoLoop, which improves four popular LVLM backbones in a plug-and-play manner, with an average gain of 4.2% points over baseline on VideoMME (long). Further analysis of working memory suggests that VideoLoop mitigates semantic thrashing: on the hardest quarter of VideoMME (long) questions, a blind judge that reads only the agent's context answers 81.1% correctly, versus 60.9% for the append-only agent. With Gemini 3.1 Pro, VideoLoop reaches 88.3% on VideoMME (long), 88.8% on VideoMMMU, and 80.9% on LongVideoBench (long).

### 🤖 AI 总结

**一句话总结**：Long-form video understanding requires multimodal agents to iteratively gather evidence over many reasoning steps. However, most existing agentic methods suffer from semantic thrashing: as append-only...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VideoLoop, Looped, Working, Memory, Against, Semantic, Thrashing, Long-Form

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38119v1) | [下载PDF](https://arxiv.org/pdf/2609.38119v1.pdf)

---

## [19. GA-EIRFS: A Geometry-Augmented Repeat-Factor Sampling Method for Long-Tailed LiDAR 3D Object Detection](https://arxiv.org/abs/2609.38116v1)

**作者**：Taufiq Ahmed, Constantino Álvarez Casado, Daniel Herrera Castro 等 6 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Long-tailed 3D object detection is treated as a class-frequency problem, but LiDAR supervision quality depends on object observability: similar frequencies can hide different geometric evidence. We introduce Geometry-Augmented Exponentially Weighted Instance-Aware Repeat Factor Sampling (GA-EIRFS), a detector-agnostic method that modulates a frequency-based repeat factor with a fixed geometry score combining point count, surface-normal entropy, and surface coverage. GA-EIRFS changes only frame-sampling probabilities, leaving the detector and inference unchanged. On nuScenes it improves mean average precision (mAP) and the nuScenes detection score (NDS) in four converged experiments with CenterPoint and PointPillars over two seeds; for CenterPoint at seed 666, mAP rises from 0.552 to 0.563 and bicycle AP from 0.306 to 0.359. Per-class gains correlate with the class sampling-weight increase (Spearman rho=0.70, p=0.025) but not with geometry score alone (rho=0.32, p=0.37), so geometry amplifies frequency-driven need. KITTI results vary across seeds, most for the rarest class. Code: https://github.com/Multimodal-Sensing-Lab/GA-EIRFS.

### 🤖 AI 总结

**一句话总结**：Long-tailed 3D object detection is treated as a class-frequency problem, but LiDAR supervision quality depends on object observability: similar frequencies can hide different geometric evidence. We in...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：3D, GA-EIRFS, Geometry-Augmented, Repeat-Factor, Sampling, Method, Long-Tailed, LiDAR

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38116v1) | [下载PDF](https://arxiv.org/pdf/2609.38116v1.pdf)

---

## [20. Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History](https://arxiv.org/abs/2609.38114v1)

**作者**：Weiqiang Wang, Zhuokun Chen, Yusheng Dai 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Autoregressive video diffusion enables interactive streaming generation, but suffers from error accumulation over long rollouts. Self-rollout training reduces exposure bias, yet finite rollouts leave long-range drift unresolved. We observe that the noise level of the history key-value (K/V) representations trades visual quality against motion, and that restoring gradients through the history aligns causal training far more closely with bidirectional training. Motivated by these observations, we introduce Self-Aligned Forcing (SAF), a training scheme that aligns the history of each block with the noise level of the block being denoised. Specifically, the history is the K/V produced by preceding blocks at the same denoising stage, so all blocks at a stage can be denoised in a single forward pass under a causal mask. This keeps the noisy history differentiable, allowing future losses to optimize how it is encoded. SAF therefore avoids a separate no-gradient rollout and per-block timestep-zero recaching, training up to 1.8x faster than prior methods with lower memory. At inference, SAF achieves the highest single-GPU throughput among existing methods and keeps one history bank per stage for a multi-GPU pipeline, reaching 49.1 FPS on 4 GPUs. Experiments show superior long-horizon generation with a better balance between visual quality and motion. Project page: https://anonymous.4open.science/w/self-aligned-forcing/.

### 🤖 AI 总结

**一句话总结**：Autoregressive video diffusion enables interactive streaming generation, but suffers from error accumulation over long rollouts. Self-rollout training reduces exposure bias, yet finite rollouts leave ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Diffusion, Self-Aligned, Forcing, Streaming, Video, Differentiable, Noisy, History

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38114v1) | [下载PDF](https://arxiv.org/pdf/2609.38114v1.pdf)

---

## [21. VISTA: Internalizing Collective Visual Experience via On-Policy Distillation for Active Multimodal Agents](https://arxiv.org/abs/2609.38086v1)

**作者**：Zheng Jiang, Houde Qian, Yiming Chen 等 8 位作者  
**分类**：cs.CV  
**发布时间**：2026-09-29

### 📄 论文摘要

Active multimodal agents use visual tools to acquire task-relevant evidence while reasoning. Although reinforcement learning samples multiple interaction trajectories per input, outcome-based objectives primarily use the group to estimate scalar advantages, leaving complementary visual discoveries underused. We introduce VISTA, which internalizes collective visual experience through on-policy distillation by turning observations from same-input rollouts into shared supervision. Collective visual experience distillation (CVED) organizes these observations with their interaction context and aligns them with individual decisions, while heterogeneity-aware policy improvement (HAPI) reinforces successful trajectories and provides experience-guided distillation for unsuccessful attempts. An experience-conditioned teacher evaluates the student's sampled response prefixes, allowing discoveries from one trajectory to guide learning in another without replacing the student's original history or generating new target trajectories. The trained agent retains its visual tools and acts using its own interaction history. VISTA achieves the strongest average performance among the evaluated active multimodal agents of comparable size and consistently outperforms same-backbone training baselines across fine-grained perception and general reasoning tasks, demonstrating the value of collective experience for active multimodal learning.

### 🤖 AI 总结

**一句话总结**：Active multimodal agents use visual tools to acquire task-relevant evidence while reasoning. Although reinforcement learning samples multiple interaction trajectories per input, outcome-based objectiv...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：VISTA, Internalizing, Collective, Visual, Experience, via, On-Policy, Distillation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38086v1) | [下载PDF](https://arxiv.org/pdf/2609.38086v1.pdf)

---

## cs.LG

## [22. A Spectral Theory of Distortion in LLM Graph Reconstruction: Sharp Bounds and Empirical Characterization](https://arxiv.org/abs/2609.38161v1)

**作者**：Jianru Shen  
**分类**：cs.LG, cs.DM  
**发布时间**：2026-09-29

### 📄 论文摘要

Evaluations of graph reconstruction by language models typically report a single aggregate distance between the original and the reconstructed graph. We prove that for the Wasserstein distance between Laplacian spectra such a summary is bracketed by two edge counts, the net change in edge number from below and the symmetric difference from above, each scaled by $2/n$ where $n$ is the number of vertices. The bracket is sharp: its two ends coincide exactly when the reconstruction only adds edges or only deletes them, and on that class the distance is a rescaled edge count that says nothing about which edges changed. When the ends differ, the residual between the distance and the lower end is positive only if the reconstruction both invented and lost edges, which turns it into a certificate of mixed editing computable from the reported summaries alone. We characterize these regimes in 135 reconstructions produced by three open-weight models over 45 synthetic graphs. Seventy-seven outputs are one-sided and 29 mixed outputs have $X > 0$, including cases where edge count is exactly preserved while nineteen edges were simultaneously invented and lost. The three models differ in editing policy, ranging from copying the input to attempting completion at the cost of large hallucination volume, a distinction that aggregate distortion does not reveal.

### 🤖 AI 总结

**一句话总结**：Evaluations of graph reconstruction by language models typically report a single aggregate distance between the original and the reconstructed graph. We prove that for the Wasserstein distance between...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, LLM, Spectral, Theory, Distortion, Graph, Reconstruction, Sharp

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38161v1) | [下载PDF](https://arxiv.org/pdf/2609.38161v1.pdf)

---

## [23. Multi-Agent Flow Matching with Decoupled Generative Guidance](https://arxiv.org/abs/2609.38133v1)

**作者**：Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti  
**分类**：cs.LG, cs.MA, cs.RO, math.OC  
**发布时间**：2026-09-29

### 📄 论文摘要

Generative modeling is widely used for producing diverse objects from complex, multimodal distributions. However, its expressivity does not, in general, come with formal guarantees that the generated objects satisfy hard constraints or requirements. In multi-agent generation, this problem becomes more challenging because a hard requirement can depend on multiple agents, while each agent may need to determine its own guidance input without relying on the simultaneously computed guidance inputs of other agents. To this end, we introduce DeGG-Flow, a general framework for multi-agent flow matching with decoupled generative guidance. By representing the generative process as a control-affine dynamical system, we develop guidance conditions for two classes of coupled requirements: shared requirements whose satisfaction depends on multiple agents together, and private requirements associated with each individual agent dependent on its neighbors. For both classes, we establish feasibility conditions and finite-horizon convergence guarantees. We further derive a Wasserstein bound that characterizes the distributional deviation induced by the guidance. We demonstrate DeGG-Flow on multi-robot collaboration for crossing a spatial gap by reconfiguring the environment, and on multi-object scene generation with affordance requirements. Across both applications, DeGG-Flow directly generates objects that satisfy all corresponding hard requirements, including at team sizes unseen during training.

### 🤖 AI 总结

**一句话总结**：Generative modeling is widely used for producing diverse objects from complex, multimodal distributions. However, its expressivity does not, in general, come with formal guarantees that the generated ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Multi-Agent, Flow, Matching, Decoupled, Generative, Guidance, modeling, widely

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38133v1) | [下载PDF](https://arxiv.org/pdf/2609.38133v1.pdf)

---

## [24. Achieving an $O(1/N)$ Optimality Gap in Average-Reward Weakly-Coupled MDPs](https://arxiv.org/abs/2609.38132v1)

**作者**：Yige Hong, Xiangcheng Zhang, Qiaomin Xie 等 5 位作者  
**分类**：cs.LG, math.OC, math.PR  
**发布时间**：2026-09-29

### 📄 论文摘要

We study average-reward weakly-coupled Markov decision processes (WCMDPs), where a WCMDP consists of $N$ smaller MDPs, called arms, that share multiple per-step budget constraints. We consider the setting where the arms have identical model parameters, multiple actions, and state- and action-dependent costs. For restless bandits (RBs), a well-studied special case of WCMDPs, prior work has developed policies that achieve an $O(1/\sqrt{N})$ optimality gap under general conditions, and has further identified conditions under which policies can achieve a better-than-$1/\sqrt{N}$ optimality gap. However, for general WCMDPs, no prior result achieves an optimality gap better than $1/\sqrt{N}$. In this paper, we identify conditions analogous to those for RBs under which a better-than-$1/\sqrt{N}$ optimality gap is achievable, and design a policy that attains an $O(1/N)$ optimality gap. Notably, unlike prior approaches based on generalizing priority orderings, our policy is not priority-based but rather is designed to induce locally linear mean-field dynamics.

### 🤖 AI 总结

**一句话总结**：We study average-reward weakly-coupled Markov decision processes (WCMDPs), where a WCMDP consists of $N$ smaller MDPs, called arms, that share multiple per-step budget constraints. We consider the set...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, $O, Achieving, Optimality, Gap, Average-Reward, Weakly-Coupled, MDPs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38132v1) | [下载PDF](https://arxiv.org/pdf/2609.38132v1.pdf)

---

## [25. WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms](https://arxiv.org/abs/2609.38121v1)

**作者**：Jiale Chen, Vage Egiazarian, Eldar Kurtić 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

KV cache memory and bandwidth costs grow with context length and batch size, which limits efficient long-context inference. To address this bottleneck, we introduce WUSH-KV for low-bit KV-cache quantization. It adapts WUSH, which constructs a data-aware transform from the second-order statistics of both factors in a matrix product to reduce quantization error. WUSH-KV uses calibration data to construct separate key and value transforms, with the value transform folded into the model weights and the key transform applied after RoPE. The transforms can be paired with clipped quantizers. For one such quantizer, QuEST INT, we show that, under mild assumptions, the WUSH transform is near-optimal. With this quantizer, WUSH-KV reduces layerwise reconstruction error and achieves the lowest end-to-end perplexity among other tested transforms. For end-to-end evaluation, we integrate WUSH-KV into SGLang using OSCAR-style percentile-clipped affine quantization. At 2-bit, WUSH-KV performs comparably to or outperforms the OSCAR transform across all evaluated models and downstream tasks.

### 🤖 AI 总结

**一句话总结**：KV cache memory and bandwidth costs grow with context length and batch size, which limits efficient long-context inference. To address this bottleneck, we introduce WUSH-KV for low-bit KV-cache quanti...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：KV, WUSH-KV, Cache, Quantization, Data-Adaptive, Transforms, memory, bandwidth

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38121v1) | [下载PDF](https://arxiv.org/pdf/2609.38121v1.pdf)

---

## [26. Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling](https://arxiv.org/abs/2609.38104v1)

**作者**：Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan 等 7 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified under the base model without parameter updates or external rewards, avoiding the costly optimization and jagged generalization of RL. However, this approach faces a fundamental exploration--exploitation trade-off, as % strong sharpening restricts exploration, trapping samplers in plausible but incorrect reasoning trajectories, whereas weak sharpening leaves the answer distribution diffuse. To resolve this trade-off, we introduce \textbf{Parallel Power Tempering (PPT)}, instantiating power-sharpened LLM sampling via parallel tempering. Running multiple \emph{interacting} replicas in parallel at different sharpening levels allows lower-power replicas to explore diverse reasoning trajectories and higher-power chains to further exploit higher-likelihood responses favored by the sharpened target. Specifically, we tailor \method{} to inference-time sampling by mitigating a truncation bias, identified in prior power samplers, and investigate effective swap strategies under finite memory and compute budgets. Extensive experimentation shows that \method{} substantially improves single-chain power-sharpened sampling and outperforms RL-post-trained models, producing higher-quality reasoning traces and even achieving performance comparable to frontier models.

### 🤖 AI 总结

**一句话总结**：Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Explore, Broadly, Reason, Sharply, Push, Small, Models, toward

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38104v1) | [下载PDF](https://arxiv.org/pdf/2609.38104v1.pdf)

---

## [27. Tail-Influence Sampling for CVaR Policy Evaluation](https://arxiv.org/abs/2609.38096v1)

**作者**：Pauline Bourigault, Xiaotong Ji, Matthieu Zimmer 等 5 位作者  
**分类**：cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Policies with similar mean returns can differ sharply in rare failures, yet estimating lower-tail conditional value-at-risk (CVaR) accurately can require many costly rollouts. When different conditional components of a stochastic workflow can be queried separately, we ask how to allocate a fixed evaluation budget to estimate a fixed policy's CVaR most accurately. We derive a tail influence for each queryable conditional law that aggregates how its uncertainty affects CVaR across every Bellman reuse. Its variance yields the fixed-design efficiency bound and the oracle Neyman allocation. Tail-Influence Sampling (TIS) estimates these influence scales from a pilot model and reallocates fresh queries toward kernels that matter most for the tail; a visitation-anchored variant protects against pilot underallocation. Under fixed dimension and a positive quantile margin, TIS attains oracle asymptotic variance and first-order MSE including pilot cost, while the anchored variant is within a factor two of the oracle. We also characterize an exact-grid regime in which tail- and mean-optimal allocations coincide. On CliffWalking, TIS reduces MSE by 41% versus learned occupancy and 76% versus complete rollouts at the same charged transition budget. In frozen language-model review workflows, anchored TIS beats an equally regularized mean-influence blend in 23 of 24 MMLU-Pro settings and reaches 2.4-3.4$\times$ lower MSE than rollouts on six-call FinQA reviews.

### 🤖 AI 总结

**一句话总结**：Policies with similar mean returns can differ sharply in rare failures, yet estimating lower-tail conditional value-at-risk (CVaR) accurately can require many costly rollouts. When different condition...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Tail-Influence, Sampling, CVaR, Policy, Evaluation, Policies, similar, mean

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38096v1) | [下载PDF](https://arxiv.org/pdf/2609.38096v1.pdf)

---

## [28. Probe-Space Preconditioning for Fast and Stable Zero-Order Training](https://arxiv.org/abs/2609.38095v1)

**作者**：Francois Chaubard, Mykel J. Kochenderfer, Chris Ré  
**分类**：cs.LG  
**发布时间**：2026-09-29

### 📄 论文摘要

Backpropagation (BP) dominates deep learning but imposes a massive memory tax. For example, training OPT-30B with Adam requires $\approx$ 600GB of GPU memory (assuming batch size 8 and sequence length 2048). Alternatively, zero-order optimization (ZOO) trains in inference-mode (requiring only $\approx$ 60GB for the same model): no stored activations, no gradients, and no optimizer states. However, ZOO convergence has lagged behind BP. In this work, we evaluate two methods to close this gap. First, we show that reallocating training compute budget from many steps to large effective batch sizes with many perturbations (or probes) but fewer steps, allows 1SPSA (Spall, 1992) to outperform zero order methods like MeZO (Malladi et al., 2023) with less training compute. Next, we introduce 1.5-SPSA, adding a single "clean" forward-pass per step to 1SPSA to calculate a cheap diagonal preconditioner in probe-space, which improves convergence rate and convergence by down-weighting high curvature directions. Benchmarking on 6 post-training datasets on both Qwen3 and OPT model families, we show that 1.5-SPSA achieves State-of-the-Art results over previous ZOO solvers with much less optimization steps. For example, we train OPT-13B (for direct comparison to MeZO) and find 1.5-SPSA achieves +3.1% accuracy on SST-2 over both MeZO and BP in only 70 steps vs. MeZO's 100,000 steps. Finally, we combine an 8-bit-packing random generator, triton fused unpack/apply kernels, and distributed parallelism to achieve fast and stable training of models as large as OPT-30B in-place on commodity GPUs (e.g. A100).

### 🤖 AI 总结

**一句话总结**：Backpropagation (BP) dominates deep learning but imposes a massive memory tax. For example, training OPT-30B with Adam requires $\approx$ 600GB of GPU memory (assuming batch size 8 and sequence length...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：BP, Probe-Space, Preconditioning, Fast, Stable, Zero-Order, Training, Backpropagation

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38095v1) | [下载PDF](https://arxiv.org/pdf/2609.38095v1.pdf)

---

## [29. Dimensionally consistent surrogate modelling through dimensional analysis and harmonic expansions](https://arxiv.org/abs/2609.38094v1)

**作者**：Ernest Tarrus, Hector Gisbert  
**分类**：cs.LG, hep-ph  
**发布时间**：2026-09-29

### 📄 论文摘要

Dimensional homogeneity is a fundamental constraint on physically meaningful models, requiring invariance under changes of units. We present a data-driven method for constructing surrogate models that satisfy this constraint at the level of the hypothesis class. Starting from a dimension matrix of measured variables, the method derives Buckingham $Π$-groups, constructs admissible dimensional prefactors, and approximates the remaining dimensionless dependence using truncated harmonic expansions on normalized invariant domains. Once the prefactor and dictionary are fixed, the coefficients are obtained from a regularized linear regression problem. We test the approach on the simple pendulum, Planck's black-body law, the double-pendulum Lyapunov field, and an experimental COBE/FIRAS black-body spectrum dataset. The results show that dimensional constraints improve conditioning, robustness to noise, and sample efficiency relative to unconstrained baselines, while the choice of dictionary becomes important in non-periodic or multi-invariant settings. The learned expressions are explicit and inexpensive to evaluate, which makes them useful as surrogate models for structured physical problems.

### 🤖 AI 总结

**一句话总结**：Dimensional homogeneity is a fundamental constraint on physically meaningful models, requiring invariance under changes of units. We present a data-driven method for constructing surrogate models that...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Dimensionally, consistent, surrogate, modelling, through, dimensional, analysis, harmonic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38094v1) | [下载PDF](https://arxiv.org/pdf/2609.38094v1.pdf)

---

## [30. Traversing the solution space of neural networks with Hessian Null Space Continuation](https://arxiv.org/abs/2609.38081v1)

**作者**：Ann Huang, Mitchell Ostrow, Zhouyang Lu 等 6 位作者  
**分类**：cs.LG, q-bio.NC, stat.ML  
**发布时间**：2026-09-29

### 📄 论文摘要

On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. However, it is unclear how these solutions are related in weight space. We unify these subfields and show for the first time that many different internal mechanisms exist within a local mode-connected region in weight space. To do so, we introduce Hessian Null Space Continuation (HNC), a scalable method that uses local curvature to traverse regions of weight space that preserve network function, and can be steered toward solutions with specified properties. In RNNs trained on a memory task, HNC reaches drastically different representations and dynamics with maintained behavior. In ImageNet-trained Vision Transformers, HNC finds representations that differ more from the original network than any independently trained model with a different architecture or objective. In reinforcement-learning agents, HNC uncovers a distinct navigation strategy at comparable return and exposes reward hacking in an AI Safety Gridworld. Finally, HNC measures the local geometry of the solution set, showing how model size and task complexity shape its dimension and functional sensitivity. Our results show that a surprisingly large amount of representational diversity exists near a single trained solution, unseen by standard gradient-based optimization. HNC identifies and quantifies this diversity, opening new possibilities for mechanistic understanding of solution spaces and for model merging, editing, and fine-tuning.

### 🤖 AI 总结

**一句话总结**：On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolat...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Traversing, solution, space, neural, networks, Hessian, Null

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2609.38081v1) | [下载PDF](https://arxiv.org/pdf/2609.38081v1.pdf)

---

