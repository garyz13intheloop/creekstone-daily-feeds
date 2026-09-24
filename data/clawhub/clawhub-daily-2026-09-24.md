# ClawHub Skills Daily | 2026-09-24

> 共 25 个 skills

## [1. Ruankao Essay Writing | 软考论文写作](https://clawhub.ai/nieen/ruankao-essay-writing)

**Slug**: `ruankao-essay-writing`  
**Version**: 1.6.1  
**Stats**: ⭐ 0 | ⬇️ 1379 | 🧩 10

**原始简介**: 覆盖软考高级论文写作全流程，支持全部 5 个高级资格（系统架构设计师/信息系统项目管理师/系统分析师/网络规划设计师/系统规划与管理师）。提供项目准备、试题分析、提纲撰写、摘要撰写、正文填充、检查校对全流程指导，按用户资格类型选择对应的项目案例、写作视角和专业深度标准。当用户提到"帮我写论文""论文指导""如何准备论文""改论文""论文提纲""论文模板"等涉及论文写作的需求时触发。不适用于论文评分（那是 ruankao-essay-scoring 的职责）。

**中文介绍**: 覆盖软考高级论文写作全流程，支持全部 5 个高级资格（系统架构设计师/信息系统项目管理师/系统分析师/网络规划设计师/系统规划与管理师）。提供项目准备、试题分析、提纲撰写、摘要撰写、正文填充、检查校对全流程指导，按用户资格类型选择对应的项目案例、写作视角和专业深度标准。当用户提到"帮我写论文""论文指导""如何准备论文""改论文""论文提纲""论文模板"等涉及论文写作的需求时触发。不适用于论文评分（那是 ruankao-essay-scoring 的职责）。

Latest changelog:
- 移除 skill-card.md 文件，简化 skill 结构
- 将版本号升级到 1.6.1，并在元数据中增加 last-updated 字段
- 整理 SKILL.md 头部结构，相关信息统一收录到 metadata 字段
- 不影响使用方式和功能，主要为文档格式规范与维护性优化

**关键词**: 软考论文写作, 覆盖软考高级论文写作全流程, 支持全部, 个高级资格（系统架构设计师, 信息系统项目管理师, Ruankao, Essay, Writing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ruankao-essay-writing)

---

## [2. Phosor AI](https://clawhub.ai/phosor.ai/phosor-ai-skills)

**Slug**: `phosor-ai-skills`  
**Version**: 1.3.1  
**Stats**: ⭐ 0 | ⬇️ 1000 | 🧩 6

**原始简介**: Generate AI videos, images and speech (text-to-video, image-to-video, reference-to-video, speech-to-video, animate, text-to-image, image-to-image, image edit, text-to-speech), bring your own LoRA models, and generate AI product/model photography for e-commerce (Image Studio) via the Phosor AI platform. Use when the user wants to create videos or images from text prompts, animate images, generate lip-synced video from audio, synthesize speech from text, generate images with a custom LoRA, generate product photography or model/clothing photography for e-commerce listings, or manage generation jobs.

**中文介绍**: Generate AI videos, images and speech (text-to-video, image-to-video, reference-to-video, speech-to-video, animate, text-to-image, image-to-image, image edit, text-to-speech), bring your own LoRA models, and generate AI product/model photography for e-commerce (Image Studio) via the Phosor AI platform. Use when the user wants to create videos or images from text prompts, animate images, generate lip-synced video from audio, synthesize speech from text, generate images with a custom LoRA, generate product photography or model/clothing photography for e-commerce listings, or manage generation jobs.

Latest changelog:
## 1.3.1 — 2026-09-24 (API v1.2.1)

Reference-to-Video limits and pricing

- Reference caps, both 480p and 768p: 9 images when sending only images, 5 images when
  videos or audio are also present, 3 reference videos, 3 reference audios
- Total reference video length is 15.1s across all reference videos
- `reference-to-video` now uses the same rates as the rest of H3: 480p $0.0045/s,
  768p $0.012/s, reference images $0.0075 each after the first 5
- Bundled client validation and version string updated to match
- API contract version v1.2.1: Reference-to-Video limits and pricing changed; no new endpoints or parameters

## 1.3.0 — 2026-09-22 (API v1.2.0)

Reference metadata and H3 limits

- Reference labels are forwarded in the same order as image, video, and audio URLs
- 768p Ref2VA supports the same 9 image-only, 4 mixed-image, and 3 video caps as 480p
- Correct the bundled client's stale 768p validation and 15-second video budget

**关键词**: Phosor, Generate, videos, images, speech, text-to-video, image-to-video, reference-to-video

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phosor-ai-skills)

---

## [3. Ruankao Essay Scoring | 软考论文评分](https://clawhub.ai/nieen/ruankao-essay-scoring)

**Slug**: `ruankao-essay-scoring`  
**Version**: 1.5.1  
**Stats**: ⭐ 0 | ⬇️ 1352 | 🧩 9

**原始简介**: 软考高级论文评分与诊断，支持全部 5 个高级资格：系统架构设计师（默认）、信息系统项目管理师、系统分析师、网络规划设计师、系统规划与管理师。当用户提到"帮我评分""给我的论文打分""论文评分""论文自查""论文诊断""看看我论文能得多少分"，或提交了论文内容希望评估时触发，先确认资格类型再执行对应评分标准。不适用于论文写作指导（那是 ruankao-essay-writing 的职责）、纯知识问答或非软考论文场景。

**中文介绍**: 软考高级论文评分与诊断，支持全部 5 个高级资格：系统架构设计师（默认）、信息系统项目管理师、系统分析师、网络规划设计师、系统规划与管理师。当用户提到"帮我评分""给我的论文打分""论文评分""论文自查""论文诊断""看看我论文能得多少分"，或提交了论文内容希望评估时触发，先确认资格类型再执行对应评分标准。不适用于论文写作指导（那是 ruankao-essay-writing 的职责）、纯知识问答或非软考论文场景。

Latest changelog:
- Removed the file skill-card.md to streamline the repository.
- Metadata is now structured under a dedicated metadata field in SKILL.md.
- Added a license field (MIT) and reorganized metadata for clarity.
- No functional or scoring logic changes to the skill itself.

**关键词**: 软考论文评分, 软考高级论文评分与诊断, 支持全部, 个高级资格, 或提交了论文内容希望评估时触发, Ruankao, Essay, Scoring

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ruankao-essay-scoring)

---

## [4. 论衡 — 严肃长文流水线](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.13.1  
**Stats**: ⭐ 1 | ⬇️ 3076 | 🧩 139

**原始简介**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

**中文介绍**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

Latest changelog:
- E1 证据对象与主张—证据链基础层
- 证据登记与主张映射模板
- 流水线最小接线
- 机械验收
- 兼容与边界

**关键词**: 论衡, 严肃长文流水线, 学术论文, 深度长文, 行业分析流水线, 含同行评审与期刊, 发布渠道匹配建议（advisory）, 不调用执行类工具（exec

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [5. beckmann-knowledge-graph-self-optimizer](https://clawhub.ai/matthiasbeckmann987-spec/beckmann-knowledge-graph-self-optimizer)

**Slug**: `beckmann-knowledge-graph-self-optimizer`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 100 | 🧩 2

**原始简介**: Iterative self-optimization for knowledge graphs in 5 phases with 3 review gates

**中文介绍**: Iterative self-optimization for knowledge graphs in 5 phases with 3 review gates

Latest changelog:
* Graph-Overview-Generator.html and Knowledge-Graph-Splitter.html are now easier to use
* Added significantly more automation; sub-skills operate autonomously.
* Known limitation: no "scientific_status" field in the new subgraph and the new relations.

- HTML tool renamed: KnowledgeGraph-Splitter.html is now Knowledge-Graph-Splitter.html for filename consistency.

**关键词**: Iterative, self-optimization, knowledge, graphs, phases, review, gates, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/beckmann-knowledge-graph-self-optimizer)

---

## [6. Long Task Context (GPT)](https://clawhub.ai/ciklopentan/long-task-context-gpt)

**Slug**: `long-task-context-gpt`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Carry project state across long tasks and chats

**中文介绍**: Carry project state across long tasks and chats

Latest changelog:
- Initial release of long-task-context-gpt for ChatGPT.
- Enables persistent, compact, source-linked project checkpoints to aid continuity in long or multi-step tasks.
- Integrates with ChatGPT Library tools where available, or uses project files for persistence in other environments.
- Emphasizes honest limitations: does not expand model context or claim full recall of chat/project history.
- Provides clear instructions for creating, updating, and using checkpoints, with guidance on what to record and privacy safeguards.
- Includes fallback procedures if persistent storage is unavailable.

**关键词**: Long, Task, Context, GPT, Carry, project, state, across

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/long-task-context-gpt)

---

## [7. SCVD General Store](https://clawhub.ai/seancrecord/scvd-general-store)

**Slug**: `scvd-general-store`  
**Version**: 3.19.0  
**Stats**: ⭐ 1 | ⬇️ 2086 | 🧩 31

**原始简介**: A live x402 practice counter from $0.001. Verify any issuer's signed receipts, including competitors; inspect endpoints, diagnose payments, retrieve host history, interpret MPP, test buyers/sellers, or use SCVD's general store. Free checks need no wallet; live purchases settle real USDC.

**中文介绍**: A live x402 practice counter from $0.001. Verify any issuer's signed receipts, including competitors; inspect endpoints, diagnose payments, retrieve host history, interpret MPP, test buyers/sellers, or use SCVD's general store. Free checks need no wallet; live purchases settle real USDC.

Latest changelog:
3.19.0: Adds field-study guidance covering enrollment, supported shopping paths, and purchase-backed feedback submissions.

**关键词**: x402, $0.001, SCVD, General, Store, live, practice, counter

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/scvd-general-store)

---

## [8. Trauma Stress Behavior Detection (Emergency Scene) | 受灾人群心理创伤行为识别（应急场景）](https://clawhub.ai/18072937735/smyx-trauma-stress-behavior-detection-analysis)

**Slug**: `smyx-trauma-stress-behavior-detection-analysis`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 1864 | 🧩 13

**原始简介**: Using fixed cameras in emergency shelters, the system analyzes video of disaster-affected crowds to detect typical acute stress reactions: stupor (prolonged motionless state with no response to external stimulation), tremor (involuntary shaking of body or limbs), unresponsiveness (no orientation or avoidance reaction to calls or sounds), and hypervigilance (frequent scanning of surroundings, startle reactions). | 通过应急避难所内的固定摄像头，分析受灾人群的行为视频，检测急性应激反应下的典型行为：木僵（长时间静止不动，对外界刺激无反应）、颤抖（身体或四肢不自主抖动）、无反应（对呼唤、声响等刺激没有定向或回避反应）以及过度警觉（频繁环顾四周、惊跳反应）。当检测到上述行为时，输出心理危机预警，提示现场心理救援团队及时介入，提供紧急心理支持，预防急性应激障碍或创伤后应激障碍。

**中文介绍**: Using fixed cameras in emergency shelters, the system analyzes video of disaster-affected crowds to detect typical acute stress reactions: stupor (prolonged motionless state with no response to external stimulation), tremor (involuntary shaking of body or limbs), unresponsiveness (no orientation or avoidance reaction to calls or sounds), and hypervigilance (frequent scanning of surroundings, startle reactions). | 通过应急避难所内的固定摄像头，分析受灾人群的行为视频，检测急性应激反应下的典型行为：木僵（长时间静止不动，对外界刺激无反应）、颤抖（身体或四肢不自主抖动）、无反应（对呼唤、声响等刺激没有定向或回避反应）以及过度警觉（频繁环顾四周、惊跳反应）。当检测到上述行为时，输出心理危机预警，提示现场心理救援团队及时介入，提供紧急心理支持，预防急性应激障碍或创伤后应激障碍。

Latest changelog:
## smyx-trauma-stress-behavior-detection-analysis v1.0.12 Changelog

- Updated version and metadata in SKILL.md.
- Minor documentation/content edits in SKILL.md.
- Removed redundant or unused file: skill-card.md.
- Updated configuration details in `skills/smyx_common/scripts/config.yaml`.

**关键词**: 受灾人群心理创伤行为识别（应急场景）, Trauma, Stress, Behavior, Detection, Emergency, Scene, fixed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-trauma-stress-behavior-detection-analysis)

---

## [9. decidealot](https://clawhub.ai/psyb0t/decidealot)

**Slug**: `decidealot`  
**Version**: 0.4.1  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 4

**原始简介**: Run local Laya or Von typed classification, scoring, and true-or-false decisions through Decidealot REST or MCP. Use when a user needs a bounded decision with probabilities, wants to deploy the Docker image, inspect local model aliases, or release model memory.

**中文介绍**: Run local Laya or Von typed classification, scoring, and true-or-false decisions through Decidealot REST or MCP. Use when a user needs a bounded decision with probabilities, wants to deploy the Docker image, inspect local model aliases, or release model memory.

Latest changelog:
- Removed the skill-card.md file.
- Updated references/setup.md for improved setup or deployment documentation.

**关键词**: or, decidealot, Run, local, Laya, Von, typed, classification

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/decidealot)

---

## [10. aigate](https://clawhub.ai/psyb0t/aigate)

**Slug**: `aigate`  
**Version**: 5.6.0  
**Stats**: ⭐ 0 | ⬇️ 1899 | 🧩 36

**原始简介**: Self-hosted AI platform — one `docker-compose up`, one OpenAI-compatible endpoint at http://localhost:4000. Bundles inference (Groq/Cerebras/OpenRouter/HuggingFace/Mistral/Cohere/Ollama/vLLM/llama.cpp/claudebox/pibox-zai/Anthropic/OpenAI), MCP tool use, a stealth browser cluster, image generation (FLUX/DALL-E/SD), speech synthesis (Kokoro/Qwen3-TTS/Chatterbox/OpenAI TTS), transcription (Whisper/Parakeet), S3-compatible object storage, agentic code execution (Claude Code + pi-coding-agent + sandboxed piston), web search (SearXNG), an email gateway (mailbox), a Telegram client (Telethon), time-series forecasting + tabular ML (predictalot), audio/video production (audiolla/flickies), an async job queue (proxq), and a web UI (LibreChat) — all reachable through one bearer token and automatic per-model fallback routing. Use when the user wants a one-command self-hosted OpenAI-compatible stack that aggregates many providers/tools behind a single endpoint instead of wiring each service up individually.

**中文介绍**: Self-hosted AI platform — one `docker-compose up`, one OpenAI-compatible endpoint at http://localhost:4000. Bundles inference (Groq/Cerebras/OpenRouter/HuggingFace/Mistral/Cohere/Ollama/vLLM/llama.cpp/claudebox/pibox-zai/Anthropic/OpenAI), MCP tool use, a stealth browser cluster, image generation (FLUX/DALL-E/SD), speech synthesis (Kokoro/Qwen3-TTS/Chatterbox/OpenAI TTS), transcription (Whisper/Parakeet), S3-compatible object storage, agentic code execution (Claude Code + pi-coding-agent + sandboxed piston), web search (SearXNG), an email gateway (mailbox), a Telegram client (Telethon), time-series forecasting + tabular ML (predictalot), audio/video production (audiolla/flickies), an async job queue (proxq), and a web UI (LibreChat) — all reachable through one bearer token and automatic per-model fallback routing. Use when the user wants a one-command self-hosted OpenAI-compatible stack that aggregates many providers/tools behind a single endpoint instead of wiring each service up individually.

Latest changelog:
- Removed the skill card documentation file (skill-card.md).
- No changes to core functionality or user features.
- Documentation now streamlined; all essential usage information remains in SKILL.md.

**关键词**: up, aigate, Self-hosted, platform, one, docker-compose, OpenAI-compatible, endpoint

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aigate)

---

## [11. LiquiLens Trading Research](https://clawhub.ai/beepboop2025/liquilens-trading-research)

**Slug**: `liquilens-trading-research`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 32 | 🧩 2

**原始简介**: Prepare a source-backed trading research brief with dollar-funding context, public bank evidence and position-sized BTC exit estimates. Use for macro preparation, counterparty research or market-depth questions, preserving source dates and missing data.

**中文介绍**: Prepare a source-backed trading research brief with dollar-funding context, public bank evidence and position-sized BTC exit estimates. Use for macro preparation, counterparty research or market-depth questions, preserving source dates and missing data.

Latest changelog:
Correct bank research routing: use filing coverage and its exact slug before bank_asset_quality_review. Keep separately requested Failure Radar review and RBI NBFC registration lookup distinct, preserving ambiguous, missing and stale evidence. No executable code, selected-tool changes or API data licensing changes.

**关键词**: LiquiLens, Trading, Research, Prepare, source-backed, brief, dollar-funding, context

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/liquilens-trading-research)

---

## [12. Text to Audio GPT](https://clawhub.ai/ciklopentan/text-to-audio-gpt)

**Slug**: `text-to-audio-gpt`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 45 | 🧩 3

**原始简介**: GPT-only: озвучивает текст и документы выразительным голосом и собирает проверенный MP3; подходит для чтения вслух, аудиокниг и озвучки. Требует GPT browser control и FFmpeg/FFprobe, не нативен для OpenClaw; Android ChatGPT требует отдельного импорта ZIP.

**中文介绍**: GPT-only: озвучивает текст и документы выразительным голосом и собирает проверенный MP3; подходит для чтения вслух, аудиокниг и озвучки. Требует GPT browser control и FFmpeg/FFprobe, не нативен для OpenClaw; Android ChatGPT требует отдельного импорта ZIP.

Latest changelog:
Уточнено короткое описание: навык работает в ChatGPT Work/Codex, создаёт MP3, а для Android ChatGPT требуется отдельный импорт ZIP. Инструкции о различиях между ClawHub, OpenClaw и ChatGPT добавлены в предыдущий выпуск 1.0.1.

**关键词**: озвучивает, текст, документы, выразительным, Text, Audio, GPT, GPT-only

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/text-to-audio-gpt)

---

## [13. Environmental Anomaly Trigger | 畜禽舍环境异常联动](https://clawhub.ai/18072937735/smyx-environmental-anomaly-analysis)

**Slug**: `smyx-environmental-anomaly-analysis`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 1031 | 🧩 9

**原始简介**: Combines livestock behavior in continuous barn videos with environmental sensor data (temperature, humidity, ammonia, etc.) to identify group stress responses caused by abnormal in-barn conditions. | 结合畜禽行为与环境传感器，识别温湿度异常时的群体应激反应。

**中文介绍**: Combines livestock behavior in continuous barn videos with environmental sensor data (temperature, humidity, ammonia, etc.) to identify group stress responses caused by abnormal in-barn conditions. | 结合畜禽行为与环境传感器，识别温湿度异常时的群体应激反应。

Latest changelog:
- Updated version to 1.0.13.
- SKILL.md updated to the latest version, incorporating recent changes.
- Removed outdated skill-card.md file.
- Minor adjustments in configuration and documentation for clarity and consistency.

**关键词**: 畜禽舍环境异常联动, Environmental, Anomaly, Trigger, Combines, livestock, behavior, continuous

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-environmental-anomaly-analysis)

---

## [14. URL to Markdown](https://clawhub.ai/skills?q=url-to-markdown)

**Slug**: `url-to-markdown`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 12 | 🧩 2

**原始简介**: Fetch any public webpage URL and get clean Markdown text for LLM context. Free, no API key, read-only. Use to read, summarize, cite, or extract article text from a link, or when a normal web fetch returns noisy HTML, cookie banners, or navigation clutter.

**中文介绍**: Fetch any public webpage URL and get clean Markdown text for LLM context. Free, no API key, read-only. Use to read, summarize, cite, or extract article text from a link, or when a normal web fetch returns noisy HTML, cookie banners, or navigation clutter.

Latest changelog:
Improved description, triggers, and category for discoverability.

**关键词**: URL, Markdown, Fetch, any, public, webpage, get, clean

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/url-to-markdown)

---

## [15. Postiz](https://clawhub.ai/oomol/oo-postiz)

**Slug**: `oo-postiz`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 22 | 🧩 1

**原始简介**: Postiz (postiz.com). Use this skill for ANY Postiz request — reading, creating, and updating data. Whenever a task involves Postiz, use this skill instead of calling the API directly.

**中文介绍**: Postiz (postiz.com). Use this skill for ANY Postiz request — reading, creating, and updating data. Whenever a task involves Postiz, use this skill instead of calling the API directly.

Latest changelog:
- Operates Postiz through an OOMOL-connected account using the `oo` CLI, with credentials handled server-side.
- Supports creating drafts, publishing immediately, or scheduling posts across connected Postiz channels.
- Lists connected social channel integrations, with optional filtering by customer group.
- Lists Postiz posts within a UTC date range for review or reporting.
- Imports publicly reachable media into Postiz from a URL.

Source: `oomol-lab/skills@c83046e`

**关键词**: Postiz, postiz.com, Use, skill, ANY, request, reading, creating

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-postiz)

---

## [16. Futunn](https://clawhub.ai/oomol/oo-futunn)

**Slug**: `oo-futunn`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 22 | 🧩 1

**原始简介**: Futunn (open.futunn.com). Use this skill for ANY Futunn request — searching and reading data. Whenever a task involves Futunn, use this skill instead of calling the API directly.

**中文介绍**: Futunn (open.futunn.com). Use this skill for ANY Futunn request — searching and reading data. Whenever a task involves Futunn, use this skill instead of calling the API directly.

Latest changelog:
- Provides OOMOL-connected access to Futunn market and trading data through the `oo` CLI.
- Supports account lookups including funds, positions, orders, fills, and authorized trading accounts.
- Retrieves market data such as snapshots, trading states, historical klines, trading days, and security info.
- Includes company and valuation research actions for financial statements, revenue breakdowns, operational efficiency, and valuation history.
- Enables discovery workflows through stock screening plus news and community search.

Source: `oomol-lab/skills@c83046e`

**关键词**: Futunn, open.futunn.com, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-futunn)

---

## [17. AIsa](https://clawhub.ai/oomol/oo-aisa)

**Slug**: `oo-aisa`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 74 | 🧩 2

**原始简介**: AIsa (aisa.one). Use this skill for ANY AIsa request — searching and reading data. Whenever a task involves AIsa, use this skill instead of calling the API directly.

**中文介绍**: AIsa (aisa.one). Use this skill for ANY AIsa request — searching and reading data. Whenever a task involves AIsa, use this skill instead of calling the API directly.

Latest changelog:
- Adds AIsa support through the OOMOL `aisa` connector and `oo` CLI.
- Reads account, key, go-to-market credit balances, and daily usage buckets.
- Lists Kalshi markets and executed trades with live market/trade details.
- Retrieves Polymarket events, markets, and wallet activity.
- Documents schema-first action execution and first-time setup recovery steps.

Source: `oomol-lab/skills@c83046e`

**关键词**: AIsa, aisa.one, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-aisa)

---

## [18. PDF Vector](https://clawhub.ai/oomol/oo-pdf-vector)

**Slug**: `oo-pdf-vector`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 74 | 🧩 2

**原始简介**: PDF Vector (pdfvector.com). Use this skill for ANY PDF Vector request — searching and reading data. Whenever a task involves PDF Vector, use this skill instead of calling the API directly.

**中文介绍**: PDF Vector (pdfvector.com). Use this skill for ANY PDF Vector request — searching and reading data. Whenever a task involves PDF Vector, use this skill instead of calling the API directly.

Latest changelog:
- Provides PDF Vector access through the OOMOL `oo` CLI and connected account credentials.
- Supports asking questions about public PDF documents with `ask_document`.
- Supports extracting structured JSON from public PDFs using a supplied schema.
- Supports parsing public PDF documents into Markdown.
- Documents safe execution flow, live schema inspection, and first-time setup troubleshooting.

Source: `oomol-lab/skills@c83046e`

**关键词**: PDF, Vector, pdfvector.com, Use, skill, ANY, request, searching

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-pdf-vector)

---

## [19. OSV](https://clawhub.ai/oomol/oo-osv)

**Slug**: `oo-osv`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 75 | 🧩 2

**原始简介**: OSV (osv.dev). Use this skill for ANY OSV request — searching and reading data. Whenever a task involves OSV, use this skill instead of calling the API directly.

**中文介绍**: OSV (osv.dev). Use this skill for ANY OSV request — searching and reading data. Whenever a task involves OSV, use this skill instead of calling the API directly.

Latest changelog:
- Provides read-only access to OSV vulnerability data through the OOMOL `osv` connector.
- Retrieves complete vulnerability records by OSV or ecosystem vulnerability identifier.
- Queries known vulnerabilities for a package, including checks for a specific package version.
- Uses `oo connector schema` before execution so payloads match the live action contract.
- Runs through OOMOL-managed connector credentials, with no raw token handling required.

Source: `oomol-lab/skills@c83046e`

**关键词**: OSV, osv.dev, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-osv)

---

## [20. Keepa](https://clawhub.ai/oomol/oo-keepa)

**Slug**: `oo-keepa`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 457 | 🧩 4

**原始简介**: Keepa (keepa.com). Use this skill for ANY Keepa request — searching and reading data. Whenever a task involves Keepa, use this skill instead of calling the API directly.

**中文介绍**: Keepa (keepa.com). Use this skill for ANY Keepa request — searching and reading data. Whenever a task involves Keepa, use this skill instead of calling the API directly.

Latest changelog:
- Operates Keepa through an OOMOL-connected account using the `oo` CLI, with credentials handled server-side.
- Supports Amazon product discovery through keyword search, Product Finder filters, deal filters, and best-seller lists.
- Retrieves product snapshots and named historical data for prices, ranks, offers, ratings, reviews, sales, and coupons.
- Provides seller lookup, seller snapshots, most-rated seller lists, and storefront ASIN inspection.
- Includes category lookup/search helpers and Keepa token status checks, with guidance for token-costly actions.

Source: `oomol-lab/skills@c83046e`

**关键词**: Keepa, keepa.com, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-keepa)

---

## [21. Bitwarden](https://clawhub.ai/oomol/oo-bitwarden)

**Slug**: `oo-bitwarden`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 75 | 🧩 2

**原始简介**: Bitwarden (bitwarden.com). Use this skill for ANY Bitwarden request — searching and reading data. Whenever a task involves Bitwarden, use this skill instead of calling the API directly.

**中文介绍**: Bitwarden (bitwarden.com). Use this skill for ANY Bitwarden request — searching and reading data. Whenever a task involves Bitwarden, use this skill instead of calling the API directly.

Latest changelog:
- Provides read-only Bitwarden organization access through the OOMOL `bitwarden` connector.
- Lists and retrieves collections, groups, members, policies, audit events, and subscription capacity.
- Supports group/member relationship lookups for organization membership review.
- Uses live connector schemas before running actions, keeping payloads aligned with current API contracts.
- Keeps credentials server-side through OOMOL, so users do not handle raw Bitwarden tokens.

Source: `oomol-lab/skills@c83046e`

**关键词**: Bitwarden, bitwarden.com, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-bitwarden)

---

## [22. Wind](https://clawhub.ai/oomol/oo-wind)

**Slug**: `oo-wind`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 22 | 🧩 1

**原始简介**: Wind (market.windalice.com). Use this skill for ANY Wind request — reading, creating, and updating data. Whenever a task involves Wind, use this skill instead of calling the API directly.

**中文介绍**: Wind (market.windalice.com). Use this skill for ANY Wind request — reading, creating, and updating data. Whenever a task involves Wind, use this skill instead of calling the API directly.

Latest changelog:
- Initial release of the `oo-wind` skill for operating Wind through an OOMOL-connected account.
- Provides schema-driven `oo connector` workflows for running Wind actions safely with server-managed credentials.
- Supports stock, fund, bond, index, economic indicator, news, announcement, and risk metric queries.
- Includes Wind Alice analysis workflows, report downloads, and task resumption guidance.
- Documents safety handling for read, write, and destructive actions plus first-time setup recovery steps.

Source: `oomol-lab/skills@c83046e`

**关键词**: Wind, market.windalice.com, Use, skill, ANY, request, reading, creating

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-wind)

---

## [23. gogcli-mcp-gmail](https://clawhub.ai/chrischall/gogcli-mcp-gmail)

**Slug**: `gogcli-mcp-gmail`  
**Version**: 4.4.0  
**Stats**: ⭐ 0 | ⬇️ 2689 | 🧩 32

**原始简介**: Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth. Triggers for requests involving threads, labels, drafts, attachments, bulk archive/trash/mark-read operations, forwarding messages, or any Gmail operation beyond simple search/get/send. Includes auth and Gmail tools only.

**中文介绍**: Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth. Triggers for requests involving threads, labels, drafts, attachments, bulk archive/trash/mark-read operations, forwarding messages, or any Gmail operation beyond simple search/get/send. Includes auth and Gmail tools only.

Latest changelog:
- Added tests for Gmail token confirmation logic.
- Removed the legacy skill-card documentation file.
- Updated dependencies and build outputs.
- Improved handling in gmail-extra tools.

**关键词**: gogcli-mcp-gmail, Use, when, user, asks, read, organize, draft

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gogcli-mcp-gmail)

---

## [24. gogcli-mcp-contacts](https://clawhub.ai/chrischall/gogcli-mcp-contacts)

**Slug**: `gogcli-mcp-contacts`  
**Version**: 4.4.0  
**Stats**: ⭐ 0 | ⬇️ 2574 | 🧩 31

**原始简介**: Use when the user asks to look up, search, or manage Google Contacts and the broader People API (Workspace directory). Triggers for contact lookups by name/email/phone, Workspace user search, profile fields, manager/reports relations, or any People API query.

**中文介绍**: Use when the user asks to look up, search, or manage Google Contacts and the broader People API (Workspace directory). Triggers for contact lookups by name/email/phone, Workspace user search, profile fields, manager/reports relations, or any People API query.

Latest changelog:
- Updated dependencies and package metadata.
- Improved build outputs in dist/index.js.
- Removed redundant documentation file skill-card.md for easier maintenance.

**关键词**: up, gogcli-mcp-contacts, Use, when, user, asks, look, search

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gogcli-mcp-contacts)

---

## [25. gogcli-mcp-calendar](https://clawhub.ai/chrischall/gogcli-mcp-calendar)

**Slug**: `gogcli-mcp-calendar`  
**Version**: 4.4.0  
**Stats**: ⭐ 0 | ⬇️ 2546 | 🧩 31

**原始简介**: Use when the user asks to manage Google Calendar events or Google Meet spaces. Triggers for scheduling, listing events, creating/updating/deleting events, responding to invitations, creating Meet spaces, ending conferences, listing meeting participants or call history.

**中文介绍**: Use when the user asks to manage Google Calendar events or Google Meet spaces. Triggers for scheduling, listing events, creating/updating/deleting events, responding to invitations, creating Meet spaces, ending conferences, listing meeting participants or call history.

Latest changelog:
- Updated distribution files and dependencies for improved stability.
- Removed the skill-card.md documentation file.
- No changes to user-facing features or available tools.

**关键词**: gogcli-mcp-calendar, Use, when, user, asks, manage, Google, Calendar

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gogcli-mcp-calendar)

---

