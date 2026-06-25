# arXiv AI 论文日报 | 2026-06-25

> 共 30 篇论文，由AI自动总结

## 📑 目录

- [cs.CV](#csCV) (9 篇)
- [cs.CL](#csCL) (8 篇)
- [cs.LG](#csLG) (8 篇)
- [cs.AI](#csAI) (5 篇)

---

## cs.AI

## [1. The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1)

**作者**：Seth Dobrin, Łukasz Chmiel  
**分类**：cs.AI, cs.CR, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems.   We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment.   We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.

### 🤖 AI 总结

**一句话总结**：AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prom...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Agent, Unfireable, Safety, Kernel, Execution-Time, Alignment, Other, Escapable

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26057v1) | [下载PDF](https://arxiv.org/pdf/2606.26057v1.pdf)

---

## [2. Autodata: An agentic data scientist to create high quality synthetic data](https://arxiv.org/abs/2606.25996v1)

**作者**：Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu 等 15 位作者  
**分类**：cs.AI, cs.CL, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data. We show how to train (meta-optimize) such a data scientist agent, so that it learns to create even stronger data. We describe the overall formulation, and a specific practical implementation, Agentic Self-Instruct. We conduct experiments on computer science research tasks, legal reasoning tasks and reasoning with mathematical objects, where we obtain improved results compared to classical synthetic dataset creation methods. Further, meta-optimizing the data scientist agent itself delivers an even larger performance uplift. Agentic data creation provides a way to convert increased inference compute into higher quality model training. Overall, we believe this direction has the potential to change the way we build AI data.

### 🤖 AI 总结

**一句话总结**：We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data. We show how to train (meta-optimize) such a data scientist...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Autodata, agentic, data, scientist, high, quality, synthetic

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25996v1) | [下载PDF](https://arxiv.org/pdf/2606.25996v1.pdf)

---

## [3. InvestPhilBench: A Multi-Layer Dynamic Benchmark for Evaluating Large Language Model Procedural Reasoning in Expert Investment Philosophy](https://arxiv.org/abs/2606.25984v1)

**作者**：Mingguang Chen, Bo Qu  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Large language models are increasingly deployed as investment research assistants, yet no benchmark tests whether they can accurately reconstruct and apply the specific procedural decision frameworks of expert investors. We introduce InvestPhilBench, a multi-layer dynamic benchmark spanning eight cognitive tiers, from principle identification (L1) to novel framework extrapolation (L8). The v0.6 release comprises 118 primary-source-verified investment principle cards, 25 decision framework cards with explicit topology metadata, and 243 QA questions (197 dev / 46 held-out test). For reproducible scoring at scale we introduce the Benchmark Automated Scoring Pipeline (BASP) -- five algorithmic metrics (OGRS, KCCS, SAP@k, IVP, CKCA) -- the Failure Mode Detection Protocol (FMDP) with computable rules for six failure modes, and Gate Reconstruction Accuracy (GRA), a per-gate metric for questions with gold reasoning programs. In this release, InvestPhilBench is primarily a benchmark-and-methodology contribution. A four-model sanity wave on the 188-question development split shows a sharp provider-tier split (BASP 0.906 vs. 0.438); these mixed-judge numbers are confounded upper bounds. The central finding: the BASP composite saturates at the frontier (Claude L4 = 0.932) while GRA still exposes a procedural deficit (frontier L4 GRA approx. 0.77, L7 GRA 0.57-0.62) -- composite scoring rewards fluent prose and hides the procedural gap. v0.6 implements a unified judge and true model-in-the-loop retrieval/oracle conditions; the de-confounded multi-model leaderboard and full three-condition run are v1.0 deliverables. On a 100-item expert-annotated gold set the automated BASP composite tracks the human reference at Pearson r = 0.72 (MAE = 0.10), with attribution (SAP@3) the weakest sub-metric and the failure-mode detector running sensitive-but-over-flagging.

### 🤖 AI 总结

**一句话总结**：Large language models are increasingly deployed as investment research assistants, yet no benchmark tests whether they can accurately reconstruct and apply the specific procedural decision frameworks ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：InvestPhilBench, Multi-Layer, Dynamic, Benchmark, Evaluating, Large, Language, Model

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25984v1) | [下载PDF](https://arxiv.org/pdf/2606.25984v1.pdf)

---

## [4. WinDOM: Self-Family Distillation for Small-Model GUI Grounding](https://arxiv.org/abs/2606.25964v1)

**作者**：Chengheng Li-Chen, Zhiqian Zhou, Hao Chen 等 4 位作者  
**分类**：cs.AI, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to obtain bounding-box training data without expensive human annotation, and how to combine supervised fine-tuning with reinforcement learning. We address both, with the explicit goal of pushing small-model performance rather than scaling up. WinDOM is a $54{,}425$-record grounding corpus harvested by driving an open-source Windows 11 web reimplementation under headless Playwright, with bounding boxes read directly off the DOM and no OCR or human annotation. Self-Family Distillation (SFD) is a single rejection-sampling cold-start parameterised only by the teacher choice: either an EMA of the student (no external model) or a frozen larger same-family teacher. We then treat the saturation depth of the SFD cold-start as an explicit GRPO hyperparameter. On a Qwen3.5-2B student, the under-saturated cold-start is a better GRPO initialiser than the converged one: SFD-4B with Early-init RL gains $+5.4$ OOD-mean ($+3.5$ ScreenSpot-Pro, $+7.0$ OSWorld-G, $+5.8$ ScreenSpot-V2) over the base. The same-size EMA mode lands within roughly one OOD-mean point of the cross-size $4$B variant ($65.2$ vs $66.3$) without an external teacher.

### 🤖 AI 总结

**一句话总结**：Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to obtain bound...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：WinDOM, Self-Family, Distillation, Small-Model, GUI, Grounding, Small, sim$2B

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25964v1) | [下载PDF](https://arxiv.org/pdf/2606.25964v1.pdf)

---

## [5. Agentic System as Compressor: Quantifying System Intelligence in Bits](https://arxiv.org/abs/2606.25960v1)

**作者**：Zihan Qin, Hongrui Zhang  
**分类**：cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

Large language models are turning from isolated predictors into agentic systems: they call tools, retrieve evidence, obey environment constraints, use verifiers, and complete tasks through search and multi-turn interaction. We adopts an analytical viewpoint based on "compression is intelligence": under a fixed task distribution, interface, and compute budget, a stronger agentic system lets a target object be reconstructed with fewer bits. We operationalize the measure with arithmetic coding, seed coding, and a fallback, and evaluate it in five settings: reversed text, chess moves, protein sequences, retrieval-augmented question answering, and semantic story compression; in all of them agentic components reduce codelength. These small, controlled experiments cover component types typical of real agentic systems, show that codelength can analyze how components, observers, and budgets change residual uncertainty, and offer guidance for evaluating real agent systems.

### 🤖 AI 总结

**一句话总结**：Large language models are turning from isolated predictors into agentic systems: they call tools, retrieve evidence, obey environment constraints, use verifiers, and complete tasks through search and ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, Agentic, System, Compressor, Quantifying, Intelligence, Bits, Large

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25960v1) | [下载PDF](https://arxiv.org/pdf/2606.25960v1.pdf)

---

## cs.CL

## [6. Real-Time Voice AI Hears but Does Not Listen](https://arxiv.org/abs/2606.26083v1)

**作者**：Martijn Bartelds, Federico Bianchi, James Zou  
**分类**：cs.CL, eess.AS  
**发布时间**：2026-06-24

### 📄 论文摘要

Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.

### 🤖 AI 总结

**一句话总结**：Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Real-Time, Voice, Hears, but, Does, Not, Listen, Speech

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26083v1) | [下载PDF](https://arxiv.org/pdf/2606.26083v1.pdf)

---

## [7. Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models](https://arxiv.org/abs/2606.26079v1)

**作者**：Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli  
**分类**：cs.CL, cs.CV, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.

### 🤖 AI 总结

**一句话总结**：Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability proper...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Same, Evidence, Different, Answer, Auditing, Order, Sensitivity, Multimodal

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26079v1) | [下载PDF](https://arxiv.org/pdf/2606.26079v1.pdf)

---

## [8. When Certainty Is an Artifact: Keyword Lexicon Blindness and the (Mis)Measurement of Rhetorical Stance](https://arxiv.org/abs/2606.26062v1)

**作者**：Bo Chen  
**分类**：cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

Can a statistically significant, large-effect-size finding in computational social science be entirely an artifact of the measurement instrument? We present a case where the answer appears to be yes. Analyzing 85 interviews across four public intellectuals (2016--2026), we find a robust negative-affect/emphatic-certainty lexical co-occurrence pattern under keyword-based scoring ($r = 0.72$--$0.93$, $p < 0.01$ for all four speakers). Replacing keyword counting with LLM-based zero-shot semantic classification on the complete diarized corpus (32,625 sentences) dramatically reduces this correlation: Dalio's $r = 0.851$ drops to $r = 0.206$, with two speakers showing negative $r(\text{neg}, \text{emphatic})$ and one showing null. In contrast, the LLM reveals a strong negative-hedging coupling across speakers -- Rogoff's $r(\text{neg}, \text{hedged}) = 0.875$ ($p = 0.001$) and Zeihan's $r(\text{neg}, \text{hedged}) = 0.722$ ($p = 0.008$) -- consistent with the conventional expectation that pessimistic discourse attracts hedging, not certainty. Sentence-level error analysis traces this discrepancy to three structural failure modes in keyword lexicons -- syntactic blindness, polysemy blindness, and categorical absence -- illustrated through cases where keyword counting inverts semantic meaning (e.g., ''never absolutely totally confident'' scored as high-certainty). We argue that keyword lexicons measure a universal lexical co-occurrence tendency -- negative discourse naturally attracts emphatic vocabulary -- that is orthogonal to, and can systematically invert, rhetorical stance. Treating keyword counts as measurements of epistemic certainty is a category error: a finding that appears to be about a speaker's psychology may be entirely about the counting of words.

### 🤖 AI 总结

**一句话总结**：Can a statistically significant, large-effect-size finding in computational social science be entirely an artifact of the measurement instrument? We present a case where the answer appears to be yes. ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：an, When, Certainty, Artifact, Lexicon, Blindness, Mis, Measurement

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26062v1) | [下载PDF](https://arxiv.org/pdf/2606.26062v1.pdf)

---

## [9. AI translation of literary texts is "fine", but readers still prefer human translations](https://arxiv.org/abs/2606.26040v1)

**作者**：Yves Ferstler, Adam Podoxin, Ty Brassington 等 6 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.

### 🤖 AI 总结

**一句话总结**：AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, translation, literary, texts, "fine", but, readers, still

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26040v1) | [下载PDF](https://arxiv.org/pdf/2606.26040v1.pdf)

---

## [10. Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning](https://arxiv.org/abs/2606.26036v1)

**作者**：Poojitha Thota, Shirin Nilizadeh  
**分类**：cs.CL, cs.CR  
**发布时间**：2026-06-24

### 📄 论文摘要

Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.

### 🤖 AI 总结

**一句话总结**：Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disprop...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Detect, Unlearn, Restore, Defending, Text, Summarization, Models, Against

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26036v1) | [下载PDF](https://arxiv.org/pdf/2606.26036v1.pdf)

---

## [11. The Tatoxa System for Text Detoxification in Low-Resource Languages: The Case of Tatar](https://arxiv.org/abs/2606.26015v1)

**作者**：Ilseyar Alimova, Bogdan Monogov, Artyom Mazur 等 8 位作者  
**分类**：cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource languages such as Tatar have received little research attention. In this paper we present Tatoxa, a novel state-of-the-art system for text detoxification in the Tatar language. Comparative experiments show that the proposed approach outperforms existing open source and proprietary commercial LLMs on key quality metrics. We also introduce a new dataset for text detoxification in Tatar, designed for fine tuning and evaluation in low resource settings. Finally, cross lingual transfer experiments indicate that transfer from other languages, including the culturally close Russian, performs significantly worse than training on native Tatar data even when a large Russian corpus is available.

### 🤖 AI 总结

**一句话总结**：Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource langu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Tatoxa, System, Text, Detoxification, Low-Resource, Languages, Case

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26015v1) | [下载PDF](https://arxiv.org/pdf/2606.26015v1.pdf)

---

## [12. Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect](https://arxiv.org/abs/2606.26003v1)

**作者**：Dihia Lanasri, Fairouz Taki, Asma Kemmoum  
**分类**：cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.

### 🤖 AI 总结

**一句话总结**：Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This l...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：An, Dziri, Voicebot, End-to-End, Low-Resource, Speech-to-Speech, Conversational, System

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26003v1) | [下载PDF](https://arxiv.org/pdf/2606.26003v1.pdf)

---

## [13. SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models](https://arxiv.org/abs/2606.25990v1)

**作者**：Liang-Yuan Wu, Zih-Ching Chen, Tongshuang Wu 等 5 位作者  
**分类**：cs.CL, cs.AI, cs.SD  
**发布时间**：2026-06-24

### 📄 论文摘要

As multimodal conversational systems increasingly engage in spoken interaction, their ability to navigate paralinguistic social cues has become a critical bottleneck for natural human-AI communication. However, existing evaluations of machine emotional intelligence assess reasoning exclusively through isolated text or passive acoustic perception, overlooking the complex cross-modal reasoning required for active, multi-turn dialogue. We introduce \textsc{SpeechEQ}, a comprehensive framework designed to evaluate the sociolinguistic reasoning of Speech-Language Models (SLMs). The framework includes a validated dataset of 2,265 dialogues across 15 Emotional Quotient (EQ) subscales grounded in EQ-i 2.0 theory, along with a multi-turn evaluation protocol measured by our proposed Spoken EQ (SEQ) score inspired by human EQ assessments. Experiments show limitations in how both existing Speech Emotion Recognition and end-to-end Speech-Language Models understand and apply paralinguistic cues through speech. While end-to-end architectures outperform cascaded systems, \textsc{SpeechEQ} reveals that current multimodal models remain bottlenecked by a text-reliant ``modality shortcut,'' an alignment-induced ``safety trap,'' and ``contextual amnesia,'' highlighting the barriers to truly emotionally aware AI. Our benchmark can be accessed at https://huggingface.co/datasets/SpeechEQ/SpeechEQ and demo page at https://binomial14.github.io/speecheq-demo/

### 🤖 AI 总结

**一句话总结**：As multimodal conversational systems increasingly engage in spoken interaction, their ability to navigate paralinguistic social cues has become a critical bottleneck for natural human-AI communication...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：SpeechEQ, Benchmarking, Emotional, Intelligence, Quotient, Socially, Aware, Voice

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25990v1) | [下载PDF](https://arxiv.org/pdf/2606.25990v1.pdf)

---

## cs.CV

## [14. TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)

**作者**：Hao Sun, Hao Yan, Mengting Chen 等 10 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-24

### 📄 论文摘要

While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.

### 🤖 AI 总结

**一句话总结**：While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive depe...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TryOnCrafter, Unleashing, Camera, Trajectories, Realistic, Video, Virtual, Try-on

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26092v1) | [下载PDF](https://arxiv.org/pdf/2606.26092v1.pdf)

---

## [15. MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation](https://arxiv.org/abs/2606.26087v1)

**作者**：JoungBin Lee, Jaewoo Jung, Jongmin Lee 等 11 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-24

### 📄 论文摘要

Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.

### 🤖 AI 总结

**一句话总结**：Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：as, 4D, MVTrack4Gen, Multi-View, Point, Tracking, Geometric, Supervision

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26087v1) | [下载PDF](https://arxiv.org/pdf/2606.26087v1.pdf)

---

## [16. A cross-process welding penetration status prediction algorithm based on unsupervised domain adaptation in laser and TIG welding](https://arxiv.org/abs/2606.26078v1)

**作者**：Sen Li, Haichao Cui, Chendong Shao 等 5 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models between welding processes with distinct physical mechanisms:for instance, from arc-dominated tungsten inert gas (TIG) welding to keyhole-based laser welding. To overcome this limitation, we propose an unsupervised domain adaptation (UDA) framework integrated with a gradual source domain expansion (GSDE) strategy. Evaluated on dedicated TIG and laser welding datasets, our approach achieves high accuracy in both same-process and cross-process transfer tasks. Specifically, it attains average accuracies of 90.65% on TIGFH and 90.72% on LSPS in same-process settings, surpassing a supervised baseline by 35.83% and 38.87%, respectively. More notably, in cross-process scenarios, it reaches 80.48% for TIG to Laser and 81.13% for Laser to TIG, improving upon the baseline by 43.39% and 43.40%. UMAP visualizations verify that the model learns domain-invariant features while maintaining discriminative class boundaries. This method considerably lowers the relabeling cost for new welding processes and enhances the versatility of intelligent monitoring across different welding systems.

### 🤖 AI 总结

**一句话总结**：Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models betw...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：cross-process, welding, penetration, status, prediction, algorithm, unsupervised, domain

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26078v1) | [下载PDF](https://arxiv.org/pdf/2606.26078v1.pdf)

---

## [17. A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks](https://arxiv.org/abs/2606.26059v1)

**作者**：Sen Li, Xiaoying Liu, Xiaojian Xu 等 8 位作者  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.

### 🤖 AI 总结

**一句话总结**：The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is t...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：welding, penetration, prediction, model, laser, process, self-supervised, learning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26059v1) | [下载PDF](https://arxiv.org/pdf/2606.26059v1.pdf)

---

## [18. How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations](https://arxiv.org/abs/2606.26041v1)

**作者**：Yuxing Cheng, Yuan Wu, Yi Chang  
**分类**：cs.CV, cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and select 5 representative types at 3 severity levels each based on their impact and cross-model discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR), Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18 models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts and tables are substantially more fragile than document-like inputs under perturbation.

### 🤖 AI 总结

**一句话总结**：Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation rem...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, How, Robust, OCR-Reasoning?, Evaluating, OCR-Reasoning, Robustness, Vision-Language

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26041v1) | [下载PDF](https://arxiv.org/pdf/2606.26041v1.pdf)

---

## [19. TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs](https://arxiv.org/abs/2606.26029v1)

**作者**：Yu-Yang Chen, Lan-Zhe Guo  
**分类**：cs.CV, cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly understood. We introduce TriViewBench, a controlled three-view visual reasoning benchmark constructed from synthetic 3D scenes with explicitly parameterized object count and occlusion. The benchmark contains 1,923 scenes and over 14K Question-Answer (QA) pairs organized into four complexity levels and three reasoning categories: Local Decision, Object Counting, and Global Recovery. We evaluate 18 open- and closed-source MLLMs under a unified prompting protocol. All 18 models exhibit an identical capability hierarchy without exception (Local Decision > Object Counting > Global Recovery), and performance degrades monotonically with complexity: Local Decision tasks decline modestly (12.11% relative drop), while Object Counting degrades substantially (59.14%) and Global Recovery collapses severely (80.02%). Error analysis on Object Counting reveals two mechanistically independent failure modes: single-view tasks are dominated by undercounting due to occlusion blindness, whereas the multi-view task reverses to overcounting due to cross-view identity confusion. Chain-of-Thought (CoT) prompting yields near-zero overall benefit ($Δ= -0.16\%$) and its effect on Global Recovery is strongly capability-gated, suggesting that the bottleneck lies in cross-view spatial representation rather than reasoning strategy. These findings reveal fundamental scalability limitations in current MLLMs and position TriViewBench as a controlled diagnostic framework for analyzing structural reasoning failures.

### 🤖 AI 总结

**一句话总结**：Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly un...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：TriViewBench, Controlled, Complexity, Scaling, Multi-View, Structural, Reasoning, MLLMs

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26029v1) | [下载PDF](https://arxiv.org/pdf/2606.26029v1.pdf)

---

## [20. From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)

**作者**：Long Cao, Zhongquan Wang, Jie Li 等 7 位作者  
**分类**：cs.CV, cs.GR  
**发布时间**：2026-06-24

### 📄 论文摘要

Image priors can synthesize target conditions for 3D Gaussian street scenes, but independently edited views do not define a coherent 3D target. Direct fitting can propagate view-specific noise, while existing pipelines do not jointly handle imperfect sparse anchors and standard-rasterizer deployment. To address this gap, teacher-relative appearance residual distillation is introduced for appearance baking. A structured space for frequency decomposition, confidence estimation, and primitive-level lifting is formed by residuals between teacher anchors and original renders. The direct optimization signal is supplied by renderer-space matching, while primitive assignment is regularized by support-aware Gaussian-space aggregation. Supported detail is admitted and unsupported noise is suppressed through confidence-gated coarse-to-fine optimization, after which all residuals are baked into fixed-geometry spherical-harmonic coefficients. The teacher and auxiliary training modules are discarded at inference. Evaluation across Waymo street assets, Tanks and Temples scenes, and multiple target conditions shows a favorable overall balance of target alignment, content preservation, artifact suppression, and cross-view consistency over editing-based baselines. Ablations confirm the effectiveness of the main components. Code will be released at https://github.com/Cagares/Baking-for-3D-Gaussian.

### 🤖 AI 总结

**一句话总结**：Image priors can synthesize target conditions for 3D Gaussian street scenes, but independently edited views do not define a coherent 3D target. Direct fitting can propagate view-specific noise, while ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：2D, 3D, Sparse, Imperfect, Anchors, Consistent, Gaussian, Street

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26007v1) | [下载PDF](https://arxiv.org/pdf/2606.26007v1.pdf)

---

## [21. Taxonomy-aware deep learning for hierarchical marine species classification in underwater imagery](https://arxiv.org/abs/2606.25989v1)

**作者**：Dan Zimmerman, Dimitris A. Pados, George Sklivanitis  
**分类**：cs.CV, cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Automated classification of marine species from underwater imagery is essential for scalable ocean biodiversity monitoring and conservation policy. Existing approaches struggle with severe domain shift across collection platforms, fine-grained visual similarity between closely related species, and uneven annotation granularity, where many specimens can only be identified to genus or a coarser taxonomic rank. We present a taxonomy-aware deep learning framework that aligns both the training loss and the inference rule with the hierarchical structure of biological classification, combining a taxonomy-weighted loss, minimum-risk Bayesian inference, multi-scale feature encoding, and independent per-rank classification heads. Evaluated on the FathomNet 2025 dataset1 (79 marine classes across seven taxonomic ranks), the system achieves a mean taxonomic distance of 1.581, within 3% of the 1st-place solution (1.535), with the largest gains from metric-aligned inference and simple, decoupled components that generalize better than learned dependencies under distribution shift.

### 🤖 AI 总结

**一句话总结**：Automated classification of marine species from underwater imagery is essential for scalable ocean biodiversity monitoring and conservation policy. Existing approaches struggle with severe domain shif...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Taxonomy-aware, deep, learning, hierarchical, marine, species, classification, underwater

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25989v1) | [下载PDF](https://arxiv.org/pdf/2606.25989v1.pdf)

---

## [22. A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention](https://arxiv.org/abs/2606.25962v1)

**作者**：Hoju Shin, Jiah Kim, Seung-Wook Kim 等 4 位作者  
**分类**：cs.CV  
**发布时间**：2026-06-24

### 📄 论文摘要

Modern stereo-capable smartphones enable immersive XR content capture. However, hardware heterogeneity across camera modules often causes severe asymmetric blur artifacts. Existing methods and benchmarks largely assume homogeneous stereo setups and therefore do not explicitly address such asymmetric degradation. To bridge this gap, we present a dedicated framework for heterogeneous stereo deblurring. First, we introduce the heterogeneous stereo deblurring (HSD) dataset, constructed from real smartphone stereo captures via multi-frame integration. Second, we propose physically- and epipolar-constrained cross attention (PECA), a lightweight module that restricts cross-view matching to an epipolar search window bounded by a optics-derived disparity upper bound. By enforcing physically valid disparity constraints, PECA enables efficient and reliable cross-view feature fusion. Moreover, our confidence-weighted attention with residual fusion emphasizes cross-guided deblurring when correspondences are reliable, while naturally falling back to self-deblurring in occluded or unreliable regions. PECA is architecture-agnostic and consistently improves CNN-, Transformer-, and NAFNet-based baselines. Extensive experiments on HSD show that PECA-enhanced models achieve improved restoration performance with favorable efficiency.

### 🤖 AI 总结

**一句话总结**：Modern stereo-capable smartphones enable immersive XR content capture. However, hardware heterogeneity across camera modules often causes severe asymmetric blur artifacts. Existing methods and benchma...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Benchmark, Heterogeneous, Stereo, Deblurring, Physically, Epipolar-constrained, Cross, Attention

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25962v1) | [下载PDF](https://arxiv.org/pdf/2606.25962v1.pdf)

---

## cs.LG

## [23. Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents](https://arxiv.org/abs/2606.26080v1)

**作者**：Changdae Oh, Wendi Li, Seongheon Park 等 6 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.

### 🤖 AI 总结

**一句话总结**：Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and s...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：LLM, Agent, Neglected, Free, Lunch, Post-training, Progress, Advantage

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26080v1) | [下载PDF](https://arxiv.org/pdf/2606.26080v1.pdf)

---

## [24. Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071v1)

**作者**：Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan 等 4 位作者  
**分类**：cs.LG, cs.AI  
**发布时间**：2026-06-24

### 📄 论文摘要

A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.

### 🤖 AI 总结

**一句话总结**：A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a c...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Model, Forensics, Investigating, Whether, Concerning, Behavior, Reflects, Misalignment

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26071v1) | [下载PDF](https://arxiv.org/pdf/2606.26071v1.pdf)

---

## [25. Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining](https://arxiv.org/abs/2606.26050v1)

**作者**：Juliana Li, Diya Sreedhar  
**分类**：cs.LG, cond-mat.dis-nn, cs.AI, cs.CL  
**发布时间**：2026-06-24

### 📄 论文摘要

Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to held-out probes (0.94 by step 925). By step 3,500 the same model scores near zero on the same probes, although the rule's evidence is still in the training data. We call this within-run reversal natural ungrokking: the corpus decides, with no trace in the loss curve, which learned rules a model keeps.   Which rules survive is predictable from one corpus statistic: how often the training stream shows the rule winning. Across un-intervened runs (two corpora, three budgets, three seeds), support frequency decides a rule's fate; the data-to-parameter ratio only modulates how deeply a doomed rule falls. The same emerge-then-collapse dynamics appear in public Pythia checkpoints, collapse depth ordered by model scale as predicted. The forgetting is a displacement: a competing surface pattern out-competes the rule, and the log-probability margin between them crosses zero within 100 training steps of the behavioral collapse.   Control over this fate is asymmetric: the same edit that destroys a rule on demand cannot restore it. Flipping support to counter-evidence in place kills the rule with monotone dose-response in two unrelated rules; but injecting support back, even to 450 times the level that naturally sustains it, buys no recovery. Every confirmatory threshold and prediction was pre-registered before the data it governed was read.

### 🤖 AI 总结

**一句话总结**：Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to h...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Natural, Ungrokking, Asymmetric, Control, Which, Rules, Survive

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26050v1) | [下载PDF](https://arxiv.org/pdf/2606.26050v1.pdf)

---

## [26. Is Variational Monte Carlo Robust? Sharp Moment Thresholds and Heavy-tailed Stochastic Optimization](https://arxiv.org/abs/2606.26009v1)

**作者**：Philipp Grohs, Davide Nobile  
**分类**：cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Variational Monte Carlo (VMC) is a central algorithm in electronic structure theory and has gained renewed importance through modern neural-network ansätze such as FermiNet. At its core, VMC seeks ground states by minimizing the Rayleigh quotient by stochastic optimization. In this work, we show that the resulting stochastic optimization problem is intrinsically governed by the nodal geometry of the underlying wave function. More precisely, we establish that properties of the nodal set determine the integrability of the local energy and gradient estimators that drive VMC. For broad and practically relevant ansatz classes, including Slater-Jastrow wave functions with variable-exponent Slater-type orbitals, we prove that these estimators are generically heavy-tailed and fail to admit higher moments. At the same time, for general analytic ansätze, we prove weak moment bounds for the relevant estimators and identify precise low-moment regimes, showing how generic and degenerate nodal structures lead to different integrability thresholds. Building on this analysis, we introduce a new robust variant of VMC $\unicode{x2013}$ coined PS-Clip-VMC $\unicode{x2013}$ which is based on clipping both the local energy and the gradient random variable. We prove that PS-Clip-VMC converges both in expectation and with high probability in the weak moment regime of VMC. Preliminary experiments for training FermiNet on Atoms with up to 18 electrons suggest that PS-Clip-VMC is significantly more robust than standard methods.

### 🤖 AI 总结

**一句话总结**：Variational Monte Carlo (VMC) is a central algorithm in electronic structure theory and has gained renewed importance through modern neural-network ansätze such as FermiNet. At its core, VMC seeks gro...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Variational, Monte, Carlo, Robust?, Sharp, Moment, Thresholds, Heavy-tailed

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26009v1) | [下载PDF](https://arxiv.org/pdf/2606.26009v1.pdf)

---

## [27. Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization](https://arxiv.org/abs/2606.26002v1)

**作者**：Kamar Hibatallah Baghdadi, Kawther Guoual Belhamidi, Sara Belhadj 等 5 位作者  
**分类**：cs.LG, cs.AI, math.OC  
**发布时间**：2026-06-24

### 📄 论文摘要

We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression search across two levels of abstraction: low-level agents (LLAs) operate independently per block, selecting per-kernel configurations over a multi-discrete action space spanning bitwidth, pruning keep-ratio, quantization type, and granularity, while high-level agents (HLAs) coordinate global budget allocation via ensemble voting guided by Fisher Information-based sensitivity estimates. To mitigate the computational cost of policy evaluation, an iterative active learning loop interleaves surrogate-guided RL optimization with post-compression fine-tuning, using a lightweight MLP surrogate to amortize expensive evaluations and a logit-MSE proxy during cold-start. The surrogate is used for reward shaping rather than as a replacement for final post-compression evaluation. The controller is architecture-agnostic by design, with a modular layer abstraction decoupling the RL environment from the underlying network topology. Experiments across Vision Transformer and CNN benchmarks demonstrate effective parameter-storage compression ratios of 5.99 - 6.72$\times$ with a 3.83 % gain in one setting and 0.55 - 5.62 % accuracy drops elsewhere, supporting hierarchical policy decomposition and sensitivity-aware guidance as practical design choices for joint neural network compression.

### 🤖 AI 总结

**一句话总结**：We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression se...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Hierarchical, Reinforcement, Learning, Neural, Network, Compression, HiReLC, Pruning

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.26002v1) | [下载PDF](https://arxiv.org/pdf/2606.26002v1.pdf)

---

## [28. The Inference-Compute Frontier and a Latency-Efficient Architecture for Limit Order Book Prediction](https://arxiv.org/abs/2606.25986v1)

**作者**：C. Evans Hedges  
**分类**：cs.LG, q-fin.ST, q-fin.TR  
**发布时间**：2026-06-24

### 📄 论文摘要

We study whether a scaling-law-style inference-compute frontier appears in limit order book prediction. Using FI-2010 and a suite of models ranging from small decision trees to neural LOB architectures, we find that the realized empirical frontier of predictive loss versus structural forward work is well summarized by a power law. In particular, with MLPLOB held out as an architecture family, a power-law fit to the low- and mid-compute non-MLPLOB frontier extrapolates across multiple orders of magnitude and attains $R^2=0.941$ on the excluded high-compute MLPLOB target frontier.   A similar exercise in latency space gives substantially weaker results, showing that latency is not merely noisy compute. We use this gap to motivate FastBiNLOB, a dense axis-separable LOB mixer built from hardware-friendly temporal and feature mixing operations. In a five-seed experiment, FastBiNLOB exceeds the published $y_{10}$ and $y_{100}$ macro-F1 targets at notably lower latency than existing published SOTA architectures.

### 🤖 AI 总结

**一句话总结**：We study whether a scaling-law-style inference-compute frontier appears in limit order book prediction. Using FI-2010 and a suite of models ranging from small decision trees to neural LOB architecture...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：Inference-Compute, Frontier, Latency-Efficient, Architecture, Limit, Order, Book, Prediction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25986v1) | [下载PDF](https://arxiv.org/pdf/2606.25986v1.pdf)

---

## [29. Tensorion: A Tensor-Aware Generalization of the Muon Optimizer](https://arxiv.org/abs/2606.25975v1)

**作者**：Vladimir Bogachev, Vladimir Aletov, Alexander Molozhavenko 等 5 位作者  
**分类**：cs.LG, cs.CV, math.NA  
**发布时间**：2026-06-24

### 📄 论文摘要

Common first-order optimizers, such as Adam, implicitly treat each parameter block as an unstructured vector, which disregards the multilinear weight structure present in many modern machine learning models. Recent work has shown that exploiting matrix structure can improve optimization dynamics. A notable example is Muon, which performs steepest descent under the spectral norm constraint. We take the next step and introduce Tensorion, a tensor-aware optimizer that extends Muon's constrained optimization perspective from matrices to higher-order tensors. Tensorion is built around a linear minimization oracle (LMO) over a tensor norm ball. The norm is carefully chosen to balance two objectives: tightly bounding the tensor spectral norm, while still keeping the LMO tractable. This LMO becomes computable because it reduces to operations on adaptively selected unfolding matrices. Notably, when restricted to order-2 tensors (i.e., matrices), Tensorion recovers Muon exactly. Experiments on tensor-based computer vision problems suggest that Tensorion can offer improved convergence behavior and more stable gradient updates compared with Adam-based and existing tensor-aware baselines in the evaluated settings.

### 🤖 AI 总结

**一句话总结**：Common first-order optimizers, such as Adam, implicitly treat each parameter block as an unstructured vector, which disregards the multilinear weight structure present in many modern machine learning ...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Tensorion, Tensor-Aware, Generalization, Muon, Optimizer, Common, first-order

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25975v1) | [下载PDF](https://arxiv.org/pdf/2606.25975v1.pdf)

---

## [30. Improving Neural Network Training by Decoupling the Magnitude and Direction of Weight Vectors](https://arxiv.org/abs/2606.25971v1)

**作者**：Alexander Hägele, Alejandro Hernández-Cano, Atli Kosson 等 4 位作者  
**分类**：cs.LG  
**发布时间**：2026-06-24

### 📄 论文摘要

Modern neural network training relies on optimizers such as Adam and Muon which act on each weight matrix as a single object. Yet every weight matrix carries two distinct quantities -- a \emph{magnitude} and a \emph{direction} -- and all optimizers stepping in the matrix as a whole couple their dynamics: the directional change from an update depends on the current magnitude, while the magnitude drifts as a byproduct of learning the direction, so neither is governed directly by the learning rate. Typical training therefore leans on surrounding recipes such as weight decay and warmup to keep learning stable at scale, though these regulate the coupling only indirectly; other recent methods instead constrain the weight to a fixed-norm sphere, but add no learnable magnitude, leaving scale control to normalization layers alone. We propose \emph{Magnitude--Direction (MD) Decoupling}, an optimizer modification that factorizes each weight into a fixed-norm direction on a hypersphere and learnable per-row and per-column magnitude gains, updated at separate learning rates, all while the model still sees a single fused weight tensor. The method is agnostic to the base optimizer and removes the need for weight decay and warmup. Across both Adam and Muon, MD Decoupling improves on well-tuned baselines, transfers the optimal LR across model width without retuning, and continues to help at scale on large Mixture-of-Experts (MoE) models. Treating magnitude and direction as separately controlled quantities thus yields more predictable training dynamics and a simple, broadly applicable improvement to modern optimizers.

### 🤖 AI 总结

**一句话总结**：Modern neural network training relies on optimizers such as Adam and Muon which act on each weight matrix as a single object. Yet every weight matrix carries two distinct quantities -- a \emph{magnitu...

**研究动机**：自动分析失败，请查看原文

**核心方法**：自动分析失败，请查看原文

**主要结论**：自动分析失败，请查看原文

**关键词**：of, Improving, Neural, Network, Training, Decoupling, Magnitude, Direction

**评分**：0

**论文链接**：[查看原文](https://arxiv.org/abs/2606.25971v1) | [下载PDF](https://arxiv.org/pdf/2606.25971v1.pdf)

---

