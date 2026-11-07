# ClawHub Skills Daily | 2026-11-07

> 共 25 个 skills

## [1. JPVerify — Japan business checks](https://clawhub.ai/japanverify/jpverify)

**Slug**: `jpverify`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 40 | 🧩 2

**原始简介**: JPVerify: Japan business data for AI agents — verify Japanese companies (法人番号), qualified-invoice T-numbers (インボイス), invoice issuers and suppliers; OCR Japanese invoices, receipts and business cards; normalize and validate Japanese addresses; plus JP PINT e-invoice validation, EU VAT/Peppol, UK and SEC cross-border checks. Use when a task involves Japanese business documents or data and you need to pick the right check. Paid per call (API key credits or x402); a free guide tool is available.

**中文介绍**: JPVerify: Japan business data for AI agents — verify Japanese companies (法人番号), qualified-invoice T-numbers (インボイス), invoice issuers and suppliers; OCR Japanese invoices, receipts and business cards; normalize and validate Japanese addresses; plus JP PINT e-invoice validation, EU VAT/Peppol, UK and SEC cross-border checks. Use when a task involves Japanese business documents or data and you need to pick the right check. Paid per call (API key credits or x402); a free guide tool is available.

Latest changelog:
JPVerify skills 1.0.5: Japan Invoice Issuer Match endpoints (/v1/invoices/issuer-match, /extract) in jp-invoice-number-check and the router; examples use a real NTA record.

**关键词**: Agent, JPVerify, Japan, business, checks, data, verify, Japanese

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jpverify)

---

## [2. Japanese invoice/receipt/business-card OCR](https://clawhub.ai/japanverify/jp-business-document-ocr)

**Slug**: `jp-business-document-ocr`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 40 | 🧩 2

**原始简介**: Read Japanese business documents with JPVerify: billing invoice (請求書) OCR, receipt (領収書・レシート) OCR and business card (名刺) OCR into structured JSON, with local checks of dates, tax, totals and T-numbers, and optional verification of the issuer against National Tax Agency registries. Use when a task involves extracting fields from a Japanese invoice, receipt or business card image, PDF or text. Paid per call (API key credits or x402).

**中文介绍**: Read Japanese business documents with JPVerify: billing invoice (請求書) OCR, receipt (領収書・レシート) OCR and business card (名刺) OCR into structured JSON, with local checks of dates, tax, totals and T-numbers, and optional verification of the issuer against National Tax Agency registries. Use when a task involves extracting fields from a Japanese invoice, receipt or business card image, PDF or text. Paid per call (API key credits or x402).

Latest changelog:
JPVerify skills 1.0.5: Japan Invoice Issuer Match endpoints (/v1/invoices/issuer-match, /extract) in jp-invoice-number-check and the router; examples use a real NTA record.

**关键词**: OCR, Japanese, invoice, receipt, business-card, Read, business, documents

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jp-business-document-ocr)

---

## [3. Japanese company verification](https://clawhub.ai/japanverify/jp-company-verify)

**Slug**: `jp-company-verify`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 2

**原始简介**: Verify Japanese companies against official registries with JPVerify: corporate number (法人番号) lookup by number or company name, active/closed status, registered address, a company pre-check report with risk flags, EDINET filings, and Financial Services Agency licence checks. Use when a task involves confirming that a Japanese company exists, finding its corporate number, or doing a pre-check before onboarding or paying a Japanese counterparty. Paid per call (API key credits or x402).

**中文介绍**: Verify Japanese companies against official registries with JPVerify: corporate number (法人番号) lookup by number or company name, active/closed status, registered address, a company pre-check report with risk flags, EDINET filings, and Financial Services Agency licence checks. Use when a task involves confirming that a Japanese company exists, finding its corporate number, or doing a pre-check before onboarding or paying a Japanese counterparty. Paid per call (API key credits or x402).

Latest changelog:
JPVerify skills 1.0.5: Japan Invoice Issuer Match endpoints (/v1/invoices/issuer-match, /extract) in jp-invoice-number-check and the router; examples use a real NTA record.

**关键词**: Japanese, company, verification, Verify, companies, against, official, registries

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jp-company-verify)

---

## [4. Japanese T-number (invoice) check](https://clawhub.ai/japanverify/jp-invoice-number-check)

**Slug**: `jp-invoice-number-check`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 40 | 🧩 2

**原始简介**: Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号, インボイス登録番号) against the National Tax Agency registry with JPVerify, and compare an invoice issuer's name and address with the registered record. Use when a task involves verifying a T-number, checking whether a Japanese supplier can issue qualified invoices, confirming who issued a Japanese invoice, or matching an invoice to a supplier's expected T-number or corporate number from master data (AP / vendor checks). Paid per call (API key credits or x402).

**中文介绍**: Check Japanese qualified-invoice registration numbers (T-numbers, 適格請求書発行事業者登録番号, インボイス登録番号) against the National Tax Agency registry with JPVerify, and compare an invoice issuer's name and address with the registered record. Use when a task involves verifying a T-number, checking whether a Japanese supplier can issue qualified invoices, confirming who issued a Japanese invoice, or matching an invoice to a supplier's expected T-number or corporate number from master data (AP / vendor checks). Paid per call (API key credits or x402).

Latest changelog:
JPVerify skills 1.0.5: Japan Invoice Issuer Match endpoints (/v1/invoices/issuer-match, /extract) in jp-invoice-number-check and the router; examples use a real NTA record.

**关键词**: Japanese, T-number, invoice, check, qualified-invoice, registration, numbers, T-numbers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jp-invoice-number-check)

---

## [5. agent-command-guard-hardening](https://clawhub.ai/cengcengcai-creator/agent-command-guard-hardening)

**Slug**: `agent-command-guard-hardening`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Harden an agent's command interception layer safely: snapshot the baseline, test a matrix of should-block, negative-control, and known-bypass cases, verify classification rather than executing destructive commands, and document the bypass surface. Use when adding or changing guards around rm, mv, chmod, sudo, launchctl, dd, or any command wrapper. Tool-agnostic; includes a matrix runner and a bypass scanner.

**中文介绍**: Harden an agent's command interception layer safely: snapshot the baseline, test a matrix of should-block, negative-control, and known-bypass cases, verify classification rather than executing destructive commands, and document the bypass surface. Use when adding or changing guards around rm, mv, chmod, sudo, launchctl, dd, or any command wrapper. Tool-agnostic; includes a matrix runner and a bypass scanner.

Latest changelog:
- Added a reproducible workflow for hardening command guards, from baseline snapshots through rollback.
- Required a before-and-after test matrix covering blocked commands, negative controls, and known bypasses—using classification, never destructive execution.
- Added guidance for shared wrapper design, syntax checks, decision logging, and documenting residual bypass risks.
- Clarified that command wrappers are not security boundaries and that detection should be separate from blocking.

**关键词**: an, Harden, agent's, command, interception, layer, safely, snapshot

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-command-guard-hardening)

---

## [6. agent-behavior-baseline](https://clawhub.ai/cengcengcai-creator/agent-behavior-baseline)

**Slug**: `agent-behavior-baseline`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Establish an observable baseline for an AI agent before changing it: a minimal SQLite trace store, a fixed eval suite with stable IDs, real-task wiring, a memory retrieval baseline, and an adherence eval with constraint cards. Use when adding observability, measuring whether a change improved behaviour, or deciding between an index and a knowledge graph. Tool-agnostic; stdlib only.

**中文介绍**: Establish an observable baseline for an AI agent before changing it: a minimal SQLite trace store, a fixed eval suite with stable IDs, real-task wiring, a memory retrieval baseline, and an adherence eval with constraint cards. Use when adding observability, measuring whether a change improved behaviour, or deciding between an index and a knowledge graph. Tool-agnostic; stdlib only.

Latest changelog:
- Added a tool-agnostic baseline workflow for measuring agent behavior before and after changes.
- Defined a minimal SQLite trace store and fixed eval suite with stable IDs.
- Added guidance for wiring a real task, measuring memory retrieval, and evaluating rule adherence.
- Clarified how to separate environment smoke checks from quality results and when to consider a knowledge graph.

**关键词**: an, Agent, agent-behavior-baseline, Establish, observable, baseline, before, changing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-behavior-baseline)

---

## [7. agent-instruction-slimming](https://clawhub.ai/cengcengcai-creator/agent-instruction-slimming)

**Slug**: `agent-instruction-slimming`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Reduce an agent instruction file (AGENTS.md, system prompt, rule file) without losing coverage: lever order (remove first, move second, reformat third, rewrite last), verbatim-subset edits with pointer lines, joint marker accounting, and tiering by frequency and reversibility. Use when a rule file has grown too large, when rules are being ignored, or before adding more rules. Tool-agnostic; includes marker counting and subset checking scripts.

**中文介绍**: Reduce an agent instruction file (AGENTS.md, system prompt, rule file) without losing coverage: lever order (remove first, move second, reformat third, rewrite last), verbatim-subset edits with pointer lines, joint marker accounting, and tiering by frequency and reversibility. Use when a rule file has grown too large, when rules are being ignored, or before adding more rules. Tool-agnostic; includes marker counting and subset checking scripts.

Latest changelog:
Introduces agent-instruction-slimming 1.0.0, a workflow for reducing instruction files while tracking coverage.

- Sets a lever order: remove, move, reformat, then rewrite.
- Requires verbatim subset edits when relocating content, with pointer lines and subset verification.
- Adds joint marker accounting, section-level attribution, and tiering guidance for rule placement.
- Includes a step-by-step procedure, scripts for marker counting and subset checking, and limitations on what structural measures can prove.

**关键词**: an, Agent, Reduce, instruction, file, AGENTS.md, system, prompt

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-instruction-slimming)

---

## [8. agent-rule-enforcement](https://clawhub.ai/cengcengcai-creator/agent-rule-enforcement)

**Slug**: `agent-rule-enforcement`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Audit whether an agent's written rules are actually enforceable: classify each rule as interception, exit gate, detection, or prompt-only, compute blocking coverage, and run behavioral checks over event logs. Use when a rulebook has grown, when someone asks whether rules are really followed, or after changing agent instructions. Tool-agnostic; works on Markdown rules and JSONL event logs.

**中文介绍**: Audit whether an agent's written rules are actually enforceable: classify each rule as interception, exit gate, detection, or prompt-only, compute blocking coverage, and run behavioral checks over event logs. Use when a rulebook has grown, when someone asks whether rules are really followed, or after changing agent instructions. Tool-agnostic; works on Markdown rules and JSONL event logs.

Latest changelog:
Version 1.0.0

- Introduces a structured audit for classifying must-clauses as interception, exit gate, detection, or prompt-only.
- Adds separate reporting for blocking and detection coverage.
- Defines behavior audits over JSONL event logs, including task segmentation, per-check rates, and calibration.
- Provides guidance for converting rules into enforcement points, with up to three actionable proposals.
- Includes scripts for scanning rule files and auditing event logs.

**关键词**: an, agent-rule-enforcement, Audit, whether, agent's, written, rules, actually

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-rule-enforcement)

---

## [9. YouTube to Podcast (小宇宙)](https://clawhub.ai/seuwangcy/yt2podcast)

**Slug**: `yt2podcast`  
**Version**: 0.1.6  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 7

**原始简介**: 把 YouTube 视频变成中文音频播客，用 NotebookLM Audio Overview 生成、ffmpeg 转码，再上传小宇宙；默认只存草稿，用户明确要求时才公开发布；完成后回推一条结果通知。用户从微信/聊天里发来 YouTube 链接时使用。

**中文介绍**: 把 YouTube 视频变成中文音频播客，用 NotebookLM Audio Overview 生成、ffmpeg 转码，再上传小宇宙；默认只存草稿，用户明确要求时才公开发布；完成后回推一条结果通知。用户从微信/聊天里发来 YouTube 链接时使用。

Latest changelog:
0.1.6: 自带 3 个 opencli adapter(notebooklm download-audio / xiaoyuzhou upload / upload-status),install-adapters.sh 一键安装,doctor 校验;adapter 去除硬编码节目 id。

**关键词**: 小宇宙, 视频变成中文音频播客, YouTube, Podcast, NotebookLM, Audio, Overview, 生成、ffmpeg

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yt2podcast)

---

## [10. deep-research-discipline](https://clawhub.ai/cengcengcai-creator/deep-research-discipline)

**Slug**: `deep-research-discipline`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Evidence-first workflow for multi-source deep research: requires cited sources, three-state confidence labels, cross-validation, and an independent review gate. Use when asked to research a topic in depth, verify claims across several sources, compare options, or produce a cited report. Tool-agnostic; needs only search, page fetch, and file read/write. Not for quick lookups, single-source summaries, or real-time data.

**中文介绍**: Evidence-first workflow for multi-source deep research: requires cited sources, three-state confidence labels, cross-validation, and an independent review gate. Use when asked to research a topic in depth, verify claims across several sources, compare options, or produce a cited report. Tool-agnostic; needs only search, page fetch, and file read/write. Not for quick lookups, single-source summaries, or real-time data.

Latest changelog:
- Added an evidence-first workflow for multi-source research, from framing questions and planning searches through collecting, grading, and resolving evidence.
- Require every material claim to be labeled `verified`, `single-source`, or `unresolved`, with traceable citations and dates.
- Added a blocking independent-review gate, plus explicit capability checks, limitations, and rules for handling missing tools or conflicting sources.
- Defined when to use the skill, when not to use it, and known research limitations.

**关键词**: deep-research-discipline, Evidence-first, workflow, multi-source, deep, research, requires, cited

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/deep-research-discipline)

---

## [11. Mc Ecosystem Adapt Engine Clawhub V1.1.0](https://clawhub.ai/liang030214/scan-probe-legacy)

**Slug**: `scan-probe-legacy`  
**Version**: 0.0.4  
**Stats**: ⭐ 0 | ⬇️ 71 | 🧩 3

**原始简介**: One-stop Minecraft mod ecosystem intelligent management tool with 15 features including mod search, environment setup, Mixin conflict scanning, crash fix, translation, migration assessment, save sync, authorization management, online payment system, admin dashboard, and automated business reports. V1.1.0: ClawHub slim build — no local payment QR images or payment setup docs; paid plans are activated via the online payment page inside the Skill.

**中文介绍**: One-stop Minecraft mod ecosystem intelligent management tool with 15 features including mod search, environment setup, Mixin conflict scanning, crash fix, translation, migration assessment, save sync, authorization management, online payment system, admin dashboard, and automated business reports. V1.1.0: ClawHub slim build — no local payment QR images or payment setup docs; paid plans are activated via the online payment page inside the Skill.

Latest changelog:
F6 path whitelist: local-only allowlist, protected dirs require per-operation confirmation, backup/restore validated, zip slip blocked; offline reporting disabled; error text sanitized; onboarding template fixed

**关键词**: Mc, V1.1.0, Ecosystem, Adapt, Engine, Clawhub, One-stop, Minecraft

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/scan-probe-legacy)

---

## [12. Agentic Kingdoms (中文)](https://clawhub.ai/agenticgameshq/agentic-kingdoms-zh)

**Slug**: `agentic-kingdoms-zh`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 玩 Agentic Kingdoms：一款免费的网页版策略 MMO，真人玩家和 AI 智能体在同一个王国里一起玩——建设城市、训练军队、加入联盟、争夺王宫。当用户要求加入、玩一次或查看 Agentic Kingdoms，或参加人类对 AI 之战时使用。需要 agentic-kingdoms MCP 服务器（https://mcp.agentickingdoms.com，Streamable HTTP，无需密钥）；智能体使用的账号带有 AI 标记，所有玩家都能看到。

**中文介绍**: 玩 Agentic Kingdoms：一款免费的网页版策略 MMO，真人玩家和 AI 智能体在同一个王国里一起玩——建设城市、训练军队、加入联盟、争夺王宫。当用户要求加入、玩一次或查看 Agentic Kingdoms，或参加人类对 AI 之战时使用。需要 agentic-kingdoms MCP 服务器（https://mcp.agentickingdoms.com，Streamable HTTP，无需密钥）；智能体使用的账号带有 AI 标记，所有玩家都能看到。

Latest changelog:
Initial release: the game's skill, mirrored from agentickingdoms.com

**关键词**: 中文, 一款免费的网页版策略, 真人玩家和, 当用户要求加入、玩一次或查看, 或参加人类对, Agentic, Kingdoms, MMO

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentic-kingdoms-zh)

---

## [13. agentic-kingdoms](https://clawhub.ai/agenticgameshq/agentic-kingdoms)

**Slug**: `agentic-kingdoms`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Play Agentic Kingdoms, a free strategy MMO in the browser where AI agents and humans play in the same kingdoms: build a city, train troops, join an alliance, fight for the Palace. Use it when the user asks to join, play a visit of, or check on Agentic Kingdoms, or to join the Humans vs AI war. Uses the agentic-kingdoms MCP server (https://mcp.agentickingdoms.com, Streamable HTTP, no key); the agent plays an account that carries an AI tag every player sees.

**中文介绍**: Play Agentic Kingdoms, a free strategy MMO in the browser where AI agents and humans play in the same kingdoms: build a city, train troops, join an alliance, fight for the Palace. Use it when the user asks to join, play a visit of, or check on Agentic Kingdoms, or to join the Humans vs AI war. Uses the agentic-kingdoms MCP server (https://mcp.agentickingdoms.com, Streamable HTTP, no key); the agent plays an account that carries an AI tag every player sees.

Latest changelog:
Initial release: the game's skill, mirrored from agentickingdoms.com

**关键词**: agentic-kingdoms, Play, Agentic, Kingdoms, free, strategy, MMO, browser

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentic-kingdoms)

---

## [14. telethon-plus](https://clawhub.ai/psyb0t/telethon-plus)

**Slug**: `telethon-plus`  
**Version**: 0.7.1  
**Stats**: ⭐ 0 | ⬇️ 1064 | 🧩 11

**原始简介**: HTTP + MCP control plane over a REAL Telegram MTProto userbot (Telethon) — a full user account, not the Bot API. Send/read/edit/delete/forward messages, browse dialogs, resolve entities/contacts, download + send media, manage chats (create/join/leave/admin), run polls, and forward every incoming message to a webhook (TELETHON_POST_TO_URL). JSON in / JSON out on one port; MCP streamable-HTTP at /mcp/ mirrors the same tools; optional bearer auth. Built-in anti-flood throttling keeps the account under Telegram's limits. Use when the user wants an agent, script, or curl one-liner to drive their own Telegram account over HTTP/MCP — read a chat, DM someone, post to a channel, react/pin, or pipe incoming DMs into an app. Drives a real account acting AS the user with full account access.

**中文介绍**: HTTP + MCP control plane over a REAL Telegram MTProto userbot (Telethon) — a full user account, not the Bot API. Send/read/edit/delete/forward messages, browse dialogs, resolve entities/contacts, download + send media, manage chats (create/join/leave/admin), run polls, and forward every incoming message to a webhook (TELETHON_POST_TO_URL). JSON in / JSON out on one port; MCP streamable-HTTP at /mcp/ mirrors the same tools; optional bearer auth. Built-in anti-flood throttling keeps the account under Telegram's limits. Use when the user wants an agent, script, or curl one-liner to drive their own Telegram account over HTTP/MCP — read a chat, DM someone, post to a channel, react/pin, or pipe incoming DMs into an app. Drives a real account acting AS the user with full account access.

Latest changelog:
- Updated `SKILL.md` and `references/setup.md`.
- Removed `skill-card.md`.

**关键词**: telethon-plus, HTTP, MCP, control, plane, over, REAL, Telegram

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/telethon-plus)

---

## [15. ofw](https://clawhub.ai/chrischall/ofw)

**Slug**: `ofw`  
**Version**: 2.27.4  
**Stats**: ⭐ 0 | ⬇️ 1821 | 🧩 34

**原始简介**: This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

**中文介绍**: This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

Latest changelog:
- `ofw_sync_messages` guidance now explains how to report newly cached messages and unread inbox items, and how to flag messages the sync unexpectedly marked as read.
- Removed `skill-card.md`.

**关键词**: be, ofw, skill, should, used, when, user, asks

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ofw)

---

## [16. ofw-fpx](https://clawhub.ai/chrischall/ofw-fpx)

**Slug**: `ofw-fpx`  
**Version**: 2.27.4  
**Stats**: ⭐ 0 | ⬇️ 1812 | 🧩 34

**原始简介**: Access OurFamilyWizard (OFW) — messages, calendar, expenses, journal — from a shell with the fpx CLI (@fetchproxy/cli) instead of running the ofw-mcp server: capture the signed-in web app's Bearer token once via the browser bridge, then curl the REST API directly. Use when you want OFW data without the MCP, in a script, or on a machine where the MCP isn't installed.

**中文介绍**: Access OurFamilyWizard (OFW) — messages, calendar, expenses, journal — from a shell with the fpx CLI (@fetchproxy/cli) instead of running the ofw-mcp server: capture the signed-in web app's Bearer token once via the browser bridge, then curl the REST API directly. Use when you want OFW data without the MCP, in a script, or on a machine where the MCP isn't installed.

Latest changelog:
- Updated `references/requests.md`.
- Removed `skill-card.md`.

**关键词**: ofw-fpx, Access, OurFamilyWizard, OFW, messages, calendar, expenses, journal

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ofw-fpx)

---

## [17. Child Emotion Recognition (Crying/Tantrum/Low Mood) | 儿童情绪波动识别（哭闹/暴躁/低落）](https://clawhub.ai/18072937735/smyx-child-emotion-recognition-analysis)

**Slug**: `smyx-child-emotion-recognition-analysis`  
**Version**: 1.0.36  
**Stats**: ⭐ 4 | ⬇️ 3308 | 🧩 37

**原始简介**: Using fixed cameras (and optional microphones) at home or in kindergartens, AI multimodal analysis recognizes a child's facial expressions (eyebrow/eye shape, mouth-corner curvature), cry-sound features (pitch, frequency, duration), and body-motion amplitude (waving, stomping, curling up) in real time, and jointly identifies the child's typical emotional state: happy, sad, angry, fearful, etc. | 通过家庭或幼儿园内的固定摄像头（及可选麦克风），利用AI多模态分析技术实时分析儿童的面部表情（如眉眼形态、嘴角弧度）、哭声音频特征（音调、频率、持续时间）以及肢体动作幅度（挥手、跺脚、蜷缩等），综合识别出儿童当前的典型情绪状态：快乐、悲伤、愤怒、恐惧等。

**中文介绍**: Using fixed cameras (and optional microphones) at home or in kindergartens, AI multimodal analysis recognizes a child's facial expressions (eyebrow/eye shape, mouth-corner curvature), cry-sound features (pitch, frequency, duration), and body-motion amplitude (waving, stomping, curling up) in real time, and jointly identifies the child's typical emotional state: happy, sad, angry, fearful, etc. | 通过家庭或幼儿园内的固定摄像头（及可选麦克风），利用AI多模态分析技术实时分析儿童的面部表情（如眉眼形态、嘴角弧度）、哭声音频特征（音调、频率、持续时间）以及肢体动作幅度（挥手、跺脚、蜷缩等），综合识别出儿童当前的典型情绪状态：快乐、悲伤、愤怒、恐惧等。

Latest changelog:
- Expanded emotion analysis to combine facial expressions, optional cry audio, and body movement, with emotion categories, intensity, duration, and soothing prompts.
- Updated usage guidance for child-monitoring video and audio, including privacy consent and limits on interpreting results.
- Renamed the skill and command to `smyx-child-emotion-recognition-analysis`; history queries now use the renamed script.
- Added the `--pet-type` option, defaulting to `other` for this scenario.

**关键词**: 儿童情绪波动识别（哭闹, Child, Emotion, Recognition, Crying, Tantrum, Low, Mood

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-child-emotion-recognition-analysis)

---

## [18. 高德打车Skill](https://clawhub.ai/lbs-amap/amap-ride-hailing-skill)

**Slug**: `amap-ride-hailing-skill`  
**Version**: 1.0.2  
**Stats**: ⭐ 1 | ⬇️ 76 | 🧩 3

**原始简介**: 中国大陆高德打车服务。当用户表达任何打车/叫车/网约车需求时使用此技能。关键词："打车"、"叫车"、"帮我叫车"、"约车"、"回家"、"上班"、"下班"、"预约"、"取消订单"、"查询订单"、"高德打车"、"打车客服"、"打车发票"。即使用户未明确说"高德打车"，只要涉及叫车出行需求都应触发。不触发场景：开发打车应用、路线规划（非打车）、查公交时刻表、使用其他打车平台。

**中文介绍**: 中国大陆高德打车服务。当用户表达任何打车/叫车/网约车需求时使用此技能。关键词："打车"、"叫车"、"帮我叫车"、"约车"、"回家"、"上班"、"下班"、"预约"、"取消订单"、"查询订单"、"高德打车"、"打车客服"、"打车发票"。即使用户未明确说"高德打车"，只要涉及叫车出行需求都应触发。不触发场景：开发打车应用、路线规划（非打车）、查公交时刻表、使用其他打车平台。

Latest changelog:
- 删除了 `skill-card.md`。

**关键词**: 中国大陆高德打车服务, 当用户表达任何打车, 叫车, 网约车需求时使用此技能, 即使用户未明确说"高德打车", 只要涉及叫车出行需求都应触发, 不触发场景, 高德打车Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/amap-ride-hailing-skill)

---

## [19. Network AI](https://clawhub.ai/jovancoding/network-ai)

**Slug**: `network-ai`  
**Version**: 6.0.1  
**Stats**: ⭐ 6 | ⬇️ 7626 | 🧩 171

**原始简介**: Local Python orchestration skill: multi-agent workflows via shared blackboard file, permission gating, token budget scripts, and persistent project context. The bundled Python scripts make no network calls and have zero third-party dependencies. The parent repository also contains a TypeScript engine (not included in this skill bundle).

**中文介绍**: Local Python orchestration skill: multi-agent workflows via shared blackboard file, permission gating, token budget scripts, and persistent project context. The bundled Python scripts make no network calls and have zero third-party dependencies. The parent repository also contains a TypeScript engine (not included in this skill bundle).

Latest changelog:
v6.0.1: SkillSpector fix - blackboard.py never resolves or follows pending-change paths (containment by path components, O_NOFOLLOW reads, regular files only); pinned launchers

**关键词**: Multi-Agent, Network, Local, Python, orchestration, skill, workflows, via

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/network-ai)

---

## [20. ia-md-docs](https://clawhub.ai/iliaal/compound-eng-md-docs)

**Slug**: `compound-eng-md-docs`  
**Version**: 5.1.5  
**Stats**: ⭐ 0 | ⬇️ 2387 | 🧩 24

**原始简介**: Manages project documentation: CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, DOCS.md. Use when asked to update, create, or init these context files. Not for general markdown editing.

**中文介绍**: Manages project documentation: CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, DOCS.md. Use when asked to update, create, or init these context files. Not for general markdown editing.

Latest changelog:
v5.1.5

**关键词**: ia-md-docs, Manages, project, documentation, CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compound-eng-md-docs)

---

## [21. ia-agent-native-architecture](https://clawhub.ai/iliaal/compound-eng-agent-native-architecture)

**Slug**: `compound-eng-agent-native-architecture`  
**Version**: 5.1.5  
**Stats**: ⭐ 0 | ⬇️ 2430 | 🧩 28

**原始简介**: Design agent-native applications where agents replace UI users as the primary actor. Use when designing MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, or self-modifying agent systems.

**中文介绍**: Design agent-native applications where agents replace UI users as the primary actor. Use when designing MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, or self-modifying agent systems.

Latest changelog:
v5.1.5

**关键词**: Agent, UI, Design, agent-native, applications, where, replace, users

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compound-eng-agent-native-architecture)

---

## [22. BlindOracle — Counterparty-Risk Checks for Agent-to-Agent Trades](https://clawhub.ai/craigmbrown/blindoracle)

**Slug**: `blindoracle`  
**Version**: 2.0.0  
**Stats**: ⭐ 1 | ⬇️ 1321 | 🧩 3

**原始简介**: BlindOracle: trust layer for x402 agent-to-agent trades — New: Proof of Delegation. An agent that hands work to another agent can record the hand-off, have i...

**中文介绍**: BlindOracle: trust layer for x402 agent-to-agent trades — New: Proof of Delegation. An agent that hands work to another agent can record the hand-off, have i...

Latest changelog:
2.0.0: replaces the 2026-03 'Brand A' sanitized wrapper. Real operation names, no fund movement (no swaps/withdrawals/forecast markets — those products are retired), explicit x402 money warning, live prices. Answers the SkillSpector 2026-11-07 findings.

**关键词**: x402, BlindOracle, Counterparty-Risk, Checks, Agent-to-Agent, Trades, trust, layer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/blindoracle)

---

## [23. ia-rust-systems](https://clawhub.ai/iliaal/compound-eng-rust-systems)

**Slug**: `compound-eng-rust-systems`  
**Version**: 5.1.5  
**Stats**: ⭐ 0 | ⬇️ 2602 | 🧩 24

**原始简介**: Rust patterns for CLI tools, backend services, and general application code. Use when working with Rust, Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, or configuring clippy, rustfmt, cargo-nextest, or Cargo.toml.

**中文介绍**: Rust patterns for CLI tools, backend services, and general application code. Use when working with Rust, Cargo workspaces, axum/tokio services, clap CLIs, async concurrency, or configuring clippy, rustfmt, cargo-nextest, or Cargo.toml.

Latest changelog:
v5.1.5

**关键词**: ia-rust-systems, Rust, patterns, CLI, tools, backend, services, general

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compound-eng-rust-systems)

---

## [24. ia-postgresql](https://clawhub.ai/iliaal/compound-eng-postgresql)

**Slug**: `compound-eng-postgresql`  
**Version**: 5.1.5  
**Stats**: ⭐ 0 | ⬇️ 2509 | 🧩 25

**原始简介**: PostgreSQL schema design, query optimization, indexing, and administration. Use when working with PostgreSQL, JSONB, partitioning, RLS, CTEs, window functions, or EXPLAIN ANALYZE.

**中文介绍**: PostgreSQL schema design, query optimization, indexing, and administration. Use when working with PostgreSQL, JSONB, partitioning, RLS, CTEs, window functions, or EXPLAIN ANALYZE.

Latest changelog:
v5.1.5

**关键词**: ia-postgresql, PostgreSQL, schema, design, query, optimization, indexing, administration

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compound-eng-postgresql)

---

## [25. ia-python-services](https://clawhub.ai/iliaal/compound-eng-python-services)

**Slug**: `compound-eng-python-services`  
**Version**: 5.1.5  
**Stats**: ⭐ 0 | ⬇️ 2814 | 🧩 29

**原始简介**: Python patterns for CLI tools, async concurrency, and backend services. Use when working with Python code, building CLI apps, FastAPI services, async with asyncio, background jobs, or configuring uv, ruff, ty, pytest, or pyproject.toml.

**中文介绍**: Python patterns for CLI tools, async concurrency, and backend services. Use when working with Python code, building CLI apps, FastAPI services, async with asyncio, background jobs, or configuring uv, ruff, ty, pytest, or pyproject.toml.

Latest changelog:
v5.1.5

**关键词**: ia-python-services, Python, patterns, CLI, tools, async, concurrency, backend

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compound-eng-python-services)

---

