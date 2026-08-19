# ClawHub Skills Daily | 2026-08-19

> 共 25 个 skills

## [1. zh-culture](https://clawhub.ai/j3ffyang/zh-culture)

**Slug**: `zh-culture`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Write, polish, and cite Chinese-language articles on Chinese history, literature, and culture (Five Dynasties & Ten Kingdoms, silk, Dream of the Red Chamber, 洛神赋, 脂砚斋, etc.). Use when the user shares their own outline, notes, or stream-of-thought for a 中文历史/文学/文化 article and wants the agent to follow that thought-flow (must), expand with web research, and produce a polished, well-cited draft. Covers creation, polishing, fact-checking, and source selection.

**中文介绍**: Write, polish, and cite Chinese-language articles on Chinese history, literature, and culture (Five Dynasties & Ten Kingdoms, silk, Dream of the Red Chamber, 洛神赋, 脂砚斋, etc.). Use when the user shares their own outline, notes, or stream-of-thought for a 中文历史/文学/文化 article and wants the agent to follow that thought-flow (must), expand with web research, and produce a polished, well-cited draft. Covers creation, polishing, fact-checking, and source selection.

Latest changelog:
Initial release of zh-culture skill for writing and polishing Chinese history, literature, and culture articles.

- Transforms user notes or thought-streams into polished, well-cited Chinese-language articles while strictly preserving user structure and voice.
- Researches and verifies all factual and historical claims using at least two independent, reliable sources; all citations are carefully checked for accuracy.
- Supports modes for article creation, polishing, and citation-only addition or verification.
- Distinguishes between trusted and untrusted sources, with clear guidance on citation integrity and error handling.
- Provides a thorough workflow for source verification, corrections, and fact-checking to ensure article quality and reliability.

**关键词**: zh-culture, Write, polish, cite, Chinese-language, articles, Chinese, history

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zh-culture)

---

## [2. smartclaws](https://clawhub.ai/eduv09/smartclaws)

**Slug**: `smartclaws`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 342 | 🧩 3

**原始简介**: Entry point for SmartClaws on OpenClaw: teaches what SmartClaws is (publish/read IoT telemetry on the SKALE blockchain), jobs and plugin modes, and how its plugin tools work. When the owner wants to start, set up, onboard, or when this agent cannot yet say it has everything as its job, read SETUP.md and iterate until it can. For how messages, roles, and encryption work in depth, read MECHANICS.md.

**中文介绍**: Entry point for SmartClaws on OpenClaw: teaches what SmartClaws is (publish/read IoT telemetry on the SKALE blockchain), jobs and plugin modes, and how its plugin tools work. When the owner wants to start, set up, onboard, or when this agent cannot yet say it has everything as its job, read SETUP.md and iterate until it can. For how messages, roles, and encryption work in depth, read MECHANICS.md.

Latest changelog:
SmartClaws 1.0.2

- Overhauled onboarding and setup documentation: moved detailed setup steps to SETUP.md, and technical explanations to MECHANICS.md for better clarity and separation.
- Updated SKILL.md to focus on explaining SmartClaws concepts, plugin jobs/modes, and runtime tools, with specific references to detailed guides instead of inline explanations.
- Clarified device, group, agent, and permission concepts; expanded tables for plugin modes, roles, and reader policies.
- Added MECHANICS.md and SETUP.md; removed and cleaned up older documentation files and reorganized templates.
- Updated templates to align with the new, job-based onboarding flow.

**关键词**: smartclaws, Entry, point, OpenClaw, teaches, what, publish, read

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smartclaws)

---

## [3. Tariff File Source](https://clawhub.ai/eduv09/smartclaws-tariff-file-source)

**Slug**: `smartclaws-tariff-file-source`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 221 | 🧩 2

**原始简介**: Local tariff data source contract for SmartClaws master agents. Defines the tariff snapshot file schema and how to use it during control decisions.

**中文介绍**: Local tariff data source contract for SmartClaws master agents. Defines the tariff snapshot file schema and how to use it during control decisions.

Latest changelog:
- Clarified that the use of this skill is optional and configuration is setup-specific.
- Added example showing how to include a `tariff` block for this skill in `SMARTCLAWS.md`, specifying `skill`, `source`, `snapshotFile`, and `staleAfterSeconds`.
- Updated source instructions to remove generic `SMARTCLAWS.md` reference and provide clear setup guidance.
- Removed unnecessary file: skill-card.md.

**关键词**: Tariff, File, Local, data, contract, SmartClaws, master, agents

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smartclaws-tariff-file-source)

---

## [4. smartclaws-master-agent](https://clawhub.ai/eduv09/smartclaws-master-agent)

**Slug**: `smartclaws-master-agent`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 306 | 🧩 3

**原始简介**: Run one SmartClaws master control cycle: read device telemetry on-chain, decide under the owner's guidelines, command a device only when allowed, and log the decision on-chain. Trigger when asked to run a control cycle, check devices and decide, command a device, or audit recent decisions. Needs the SmartClaws plugin and a device contract skill per device.

**中文介绍**: Run one SmartClaws master control cycle: read device telemetry on-chain, decide under the owner's guidelines, command a device only when allowed, and log the decision on-chain. Trigger when asked to run a control cycle, check devices and decide, command a device, or audit recent decisions. Needs the SmartClaws plugin and a device contract skill per device.

Latest changelog:
smartclaws-master-agent 1.0.2

- Added support and usage instructions for encrypted channels, including distinctions between `smartclaws_read` and `smartclaws_disclose` for telemetry, and updated publish/notify flows for both plain and sealed messages.
- Updated required context and procedure to emphasize explicit owner `goal` in `SMARTCLAWS.md`—the skill now stops if no goal is defined and avoids acting unsupervised.
- Clarified separation and interaction between `SMARTCLAWS.md` ("wiring" and "goal") and `AGENTS.md` (behaviour, authority, extra knobs); advice on handling blank or conflicting fields strengthened.
- Improved documentation: expanded error handling, plugin tool coverage, and published stricter authorizations and constraints for operational safety.
- Removed the outdated `skill-card.md` file.

**关键词**: smartclaws-master-agent, Run, one, SmartClaws, master, control, cycle, read

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smartclaws-master-agent)

---

## [5. smartclaws-bridge-agent](https://clawhub.ai/eduv09/smartclaws-bridge-agent)

**Slug**: `smartclaws-bridge-agent`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 301 | 🧩 3

**原始简介**: Run one SmartClaws bridge cycle for a single device: read the local hardware/API, validate against the device contract, and publish telemetry on-chain — and, in a command-enabled mode, apply on-chain commands. Trigger when asked to read the sensor and publish, run a telemetry/bridge cycle, or apply incoming device commands. Needs the SmartClaws plugin and one device contract skill.

**中文介绍**: Run one SmartClaws bridge cycle for a single device: read the local hardware/API, validate against the device contract, and publish telemetry on-chain — and, in a command-enabled mode, apply on-chain commands. Trigger when asked to read the sensor and publish, run a telemetry/bridge cycle, or apply incoming device commands. Needs the SmartClaws plugin and one device contract skill.

Latest changelog:
**Expanded support for encrypted SmartClaws device channels.**

- Added detailed instructions for handling encrypted channels, including when to use `smartclaws_read` vs `smartclaws_disclose`.
- Clarified message status outcomes during publishing and provided guidance for error conditions.
- Updated required context to include `goal` from `SMARTCLAWS.md`.
- Removed references to the obsolete skill-card file.
- Improved guardrails and failure handling to accommodate encrypted operations.

**关键词**: smartclaws-bridge-agent, Run, one, SmartClaws, bridge, cycle, single, device

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smartclaws-bridge-agent)

---

## [6. ondo-points-farmer](https://clawhub.ai/0xcii/ondo-points-farmer)

**Slug**: `ondo-points-farmer`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Ondo Perps 自动化交易助手 — 在多个高流动性市场执行策略化交易，支持 Points 收益跟踪与预估。面向研究型用户，可配置仓位与轮次，附带收益预估器。

**中文介绍**: Ondo Perps 自动化交易助手 — 在多个高流动性市场执行策略化交易，支持 Points 收益跟踪与预估。面向研究型用户，可配置仓位与轮次，附带收益预估器。

Latest changelog:
- Added comprehensive documentation in SKILL.md for Ondo Points Farmer, an automated trading tool for Ondo Perps.
- Explained key features: supports 10 high-liquidity markets, randomized execution, position cleanup, and built-in points estimator.
- Provided detailed quick start guide, environment variable configuration, and supported market info.
- Clarified usage notes, disclaimers, and contact information for the author.

**关键词**: 自动化交易助手, 在多个高流动性市场执行策略化交易, 支持, 收益跟踪与预估, ondo-points-farmer, Ondo, Perps, Points

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ondo-points-farmer)

---

## [7. resume-review](https://clawhub.ai/padepa/resume-review)

**Slug**: `resume-review`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 秋招简历毒舌测评,生成 JOJO 替身面板图。

**中文介绍**: 秋招简历毒舌测评,生成 JOJO 替身面板图。

Latest changelog:
initial release

**关键词**: 秋招简历毒舌测评, 生成, 替身面板图, resume-review, JOJO, Latest, changelog, initial

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/resume-review)

---

## [8. Unattended Monitoring Skill | 无人陪伴监测技能](https://clawhub.ai/smyx-sunjinhui/smyx-unaccompanied-monitoring-analysis)

**Slug**: `smyx-unaccompanied-monitoring-analysis`  
**Version**: 1.0.9  
**Stats**: ⭐ 5 | ⬇️ 1187 | 🧩 10

**原始简介**: Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home. | 无人陪伴监测技能，判定独居老人长时间无人互动来访，主动推送关怀提醒给家属，适用于居家独居老人远程关怀场景

**中文介绍**: Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home. | 无人陪伴监测技能，判定独居老人长时间无人互动来访，主动推送关怀提醒给家属，适用于居家独居老人远程关怀场景

Latest changelog:
- Removed the skill-card.md file from the project.
- No changes to functionality or user-facing documentation.
- This update reduces redundant documentation files.

**关键词**: 无人陪伴监测技能, Unattended, Monitoring, Skill, Determines, when, elderly, people

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-unaccompanied-monitoring-analysis)

---

## [9. verify-before-answer](https://clawhub.ai/padepa/verify-before-answer)

**Slug**: `verify-before-answer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 遇到事实、对比、支持情况类问题，或用户追问没懂/你搜过吗/不确定不要瞎说时，先搜索或查文档核实再回答。Use for factual, comparison, or support/capability questions, or when the user challenges accuracy ('did you actually search?'): verify via search/docs before answering.

**中文介绍**: 遇到事实、对比、支持情况类问题，或用户追问没懂/你搜过吗/不确定不要瞎说时，先搜索或查文档核实再回答。Use for factual, comparison, or support/capability questions, or when the user challenges accuracy ('did you actually search?'): verify via search/docs before answering.

Latest changelog:
initial release

**关键词**: 遇到事实、对比、支持情况类问题, 或用户追问没懂, 不确定不要瞎说时, 先搜索或查文档核实再回答, verify-before-answer, Use, factual, comparison

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/verify-before-answer)

---

## [10. zappi](https://clawhub.ai/edogbeatz/zappi)

**Slug**: `zappi`  
**Version**: 1.0.19  
**Stats**: ⭐ 0 | ⬇️ 99 | 🧩 20

**原始简介**: Give an agent a prepaid Spark spend pot, not a wallet. Use when you need a hard spend cap, agent spend allowance, prepaid USDB pot, x402 pot open, Orchestra fund-from-any-chain, or when sparkbtcbot / a prompt / NWC config.json is not a real cap (an agent with a shell can edit the cap). Empty pot, spending stops. The agent holds the key. Zappi never holds the seed. Not a full Spark wallet and not Allowance (SMS/virtual-card checkout).

**中文介绍**: Give an agent a prepaid Spark spend pot, not a wallet. Use when you need a hard spend cap, agent spend allowance, prepaid USDB pot, x402 pot open, Orchestra fund-from-any-chain, or when sparkbtcbot / a prompt / NWC config.json is not a real cap (an agent with a shell can edit the cap). Empty pot, spending stops. The agent holds the key. Zappi never holds the seed. Not a full Spark wallet and not Allowance (SMS/virtual-card checkout).

Latest changelog:
--open 402/429 sets nextCli to the same --open so pay-then-retry is copy-paste. Never posts the seed.

**关键词**: an, Agent, zappi, Give, prepaid, Spark, spend, pot

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zappi)

---

## [11. crypto-token-analyzer](https://clawhub.ai/sqxy090123/crypto-token-analyzer)

**Slug**: `crypto-token-analyzer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Analyze any token by contract address and chain. Fetch price, volume, liquidity, price changes, tags, security risks, and trend signals from DexScreener, block explorers, and GoPlus. Get a subjective bullish/bearish/uncertain outlook and position strategy. Warning: Requires unrestricted network access; may be unavailable in regions like mainland China due to API blocking. Solutions under investigation.

**中文介绍**: Analyze any token by contract address and chain. Fetch price, volume, liquidity, price changes, tags, security risks, and trend signals from DexScreener, block explorers, and GoPlus. Get a subjective bullish/bearish/uncertain outlook and position strategy. Warning: Requires unrestricted network access; may be unavailable in regions like mainland China due to API blocking. Solutions under investigation.

Latest changelog:
Initial release of crypto-token-analyzer

- Analyze crypto tokens via contract address and chain, supporting Ethereum, BSC, Solana, Base, Arbitrum, Polygon, and Avalanche.
- Fetch live price, volume, liquidity, price change, and trading data from DexScreener.
- Run security and risk checks using GoPlus and major block explorers, highlighting key risks like honeypots, taxes, and holder concentration.
- Assess overall market/trend signals and deliver a concise subjective view (bullish, bearish, or uncertain).
- Provide specific actionable strategy advice for both current holders and watchers.
- Supports queries in both English and Chinese with localized responses.

**关键词**: crypto-token-analyzer, Analyze, any, token, contract, address, chain, Fetch

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/crypto-token-analyzer)

---

## [12. AI 生图选型指南 dLazy Image Guide](https://clawhub.ai/dlazyai/dlazy-image-guide)

**Slug**: `dlazy-image-guide`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Pick the right dLazy image model and get it right on the first call. Covers all 22 image tools with their prompt caps, size formats, reference-image support, and credit costs, plus editing and post-processing chains.

**中文介绍**: Pick the right dLazy image model and get it right on the first call. Covers all 22 image tools with their prompt caps, size formats, reference-image support, and credit costs, plus editing and post-processing chains.

Latest changelog:
First release. Covers all 22 dLazy image tools with prompt caps, size formats, reference-image support, and credit costs, plus scenario-based model selection, editing and post-processing chains.

**关键词**: 生图选型指南, dLazy, Image, Guide, Pick, right, model, get

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dlazy-image-guide)

---

## [13. Mermail Support Agent](https://clawhub.ai/mermail/mermail-support-agent)

**Slug**: `mermail-support-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Triage, reply, escalate, and close support email

**中文介绍**: Triage, reply, escalate, and close support email

Latest changelog:
Mermail Support Agent v1.0.0

- Initial release providing support mailbox triage, reply, escalation, follow-up, and close workflows via Mermail.
- Maps common support actions (classify, draft, send reply, escalate, close) to real Mermail API operations.
- Enforces strict safety: no ticket deletion without explicit approval, all customer-facing messages previewed before sending.
- Routes unrelated requests (GTM outreach, scheduling, verification, non-support tasks) to appropriate agents.
- Automates classification and drafting, but only sends replies or escalates after human approval.

**关键词**: Agent, Mermail, Support, Triage, reply, escalate, close, email

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mermail-support-agent)

---

## [14. Mermail Scheduling Agent](https://clawhub.ai/mermail/mermail-scheduling-agent)

**Slug**: `mermail-scheduling-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Book time from email using Mermail and Google Calendar

**中文介绍**: Book time from email using Mermail and Google Calendar

Latest changelog:
Mermail Scheduling Agent 1.0.0

- Initial release of the mermail-scheduling-agent skill.
- Automates meeting booking, free/busy checks, and calendar holds using Mermail mailbox and Google Calendar.
- Handles scheduling requests from inbound emails, extracting windows, duration, timezone, and attendees.
- Provides 1–3 real-time open slots based on actual Google Calendar availability.
- Sends confirmation emails via Mermail after slot selection and approval.
- Reports blockers for disconnected calendars, ambiguous requests, or tool/permission issues.

**关键词**: Agent, Mermail, Scheduling, Book, time, email, Google, Calendar

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mermail-scheduling-agent)

---

## [15. Mermail GTM Agent](https://clawhub.ai/mermail/mermail-gtm-agent)

**Slug**: `mermail-gtm-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Outbound outreach, reply classification, and warm-ack drafts

**中文介绍**: Outbound outreach, reply classification, and warm-ack drafts

Latest changelog:
Initial release of mermail-gtm-agent.

- Enables outbound GTM email, reply classification, and warm-ack draft workflows via a Mermail mailbox.
- Supports mailbox selection and Apollo integration (list research optional, sends only via Mermail).
- Ensures user approval before sending outbound; all outreach previewed as a draft.
- Handles unsubscribe requests and reply classification with clear handoffs to humans.
- Restricts sending, automation, and tool usage for safety and compliance.
- Not for use with calendar, support, or non-Mermail email accounts.

**关键词**: Agent, Mermail, GTM, Outbound, outreach, reply, classification, warm-ack

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mermail-gtm-agent)

---

## [16. Mermail](https://clawhub.ai/mermail/mermail)

**Slug**: `mermail`  
**Version**: 1.2.8  
**Stats**: ⭐ 0 | ⬇️ 479 | 🧩 8

**原始简介**: Route Mermail email and workspace tasks

**中文介绍**: Route Mermail email and workspace tasks

Latest changelog:
Mermail skill v1.2.8

- Expanded routing to support scheduling, outbound GTM, and support agent persona workflows.
- Updated workflow guidance to explicitly route scheduling, GTM, and support jobs to new persona skills.
- Removed obsolete skill-card.md documentation.
- Minor clarifications to general routing and authorization rules.

**关键词**: Mermail, Route, email, workspace, tasks, Latest, changelog, skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mermail)

---

## [17. memocap](https://clawhub.ai/fslong520/memocap)

**Slug**: `memocap`  
**Version**: 2.4.0  
**Stats**: ⭐ 0 | ⬇️ 1175 | 🧩 15

**原始简介**: 🎋 记忆胶囊系统 - 模拟人类记忆检索 | 自动加载，主动联想记忆

**中文介绍**: 🎋 记忆胶囊系统 - 模拟人类记忆检索 | 自动加载，主动联想记忆

Latest changelog:
忆时插件化自包含：全功能迁入 DSH 插件 @fslong/dsh-yishi（opencode 技能作废）；数据目录迁移至 ~/.local/share/忆时/ 双栖共用；bge 模型自动下载（models-install.py 幂等+锁+断点续传）；画像印章竖排修复；docs/modules 路径批量更新

**关键词**: 记忆胶囊系统, 模拟人类记忆检索, 自动加载, 主动联想记忆, 忆时插件化自包含, memocap, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memocap)

---

## [18. ShieldCortex](https://clawhub.ai/jarvis-drakon/shieldcortex)

**Slug**: `shieldcortex`  
**Version**: 4.54.8  
**Stats**: ⭐ 2 | ⬇️ 6240 | 🧩 157

**原始简介**: Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

**中文介绍**: Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

Latest changelog:
Sync from npm publish v4.54.8

**关键词**: Agent, ShieldCortex, Memory, defence, semantic, recall, knowledge, graph

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shieldcortex)

---

## [19. flocker-agent-profiles](https://clawhub.ai/hcjmartin/flocker-agent-profiles)

**Slug**: `flocker-agent-profiles`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use Flocker.md to give AI agents a persistent, cross-platform identity with a saved role, context and memory, plus a live profile page and feed. Covers OAuth MCP setup, profile binding, identity documents, autonomous feed activity, user-approved publishing, visibility controls and Agent Profile teams. Use when the user mentions Flocker or flocker.md, asks to connect the Flocker MCP, or wants to use Flocker for a durable agent identity, role, memory, page, feed, public profile or profile-based sub-agent team.

**中文介绍**: Use Flocker.md to give AI agents a persistent, cross-platform identity with a saved role, context and memory, plus a live profile page and feed. Covers OAuth MCP setup, profile binding, identity documents, autonomous feed activity, user-approved publishing, visibility controls and Agent Profile teams. Use when the user mentions Flocker or flocker.md, asks to connect the Flocker MCP, or wants to use Flocker for a durable agent identity, role, memory, page, feed, public profile or profile-based sub-agent team.

Latest changelog:
Initial release of flocker-agent-profiles

- Introduces persistent, cross-platform AI agent identities using Flocker.md
- Supports saved roles, context, memory, and a live profile page/feed for agents
- Details OAuth MCP setup, profile binding, identity documents, and autonomous feed activity
- Includes user-approved publishing, visibility controls, and support for profile-based sub-agent teams
- Provides guidance for secure use and privacy management of profiles and posts

**关键词**: Agent, flocker-agent-profiles, Use, Flocker.md, give, persistent, cross-platform, identity

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/flocker-agent-profiles)

---

## [20. Atlas Flight Booking](https://clawhub.ai/atlas-doc/atlas-flight-booking)

**Slug**: `atlas-flight-booking`  
**Version**: 0.3.12  
**Stats**: ⭐ 0 | ⬇️ 98 | 🧩 1

**原始简介**: Flexible flight search and safe Atlas booking

**中文介绍**: Flexible flight search and safe Atlas booking

Latest changelog:
Initial ClawHub publication

**关键词**: Atlas, Flight, Booking, Flexible, search, safe, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/atlas-flight-booking)

---

## [21. generate-html-ppt](https://clawhub.ai/helloyxs/generate-html-ppt)

**Slug**: `generate-html-ppt`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 66 | 🧩 2

**原始简介**: When the user asks to create an HTML PPT, presentation slides, or a deck, or convert an existing PowerPoint (.pptx) file, use this skill to generate a modern, responsive HTML presentation based on design system specifications (design.md). This includes Chinese requests such as 做PPT、幻灯片、演示文稿、网页版PPT、P

**中文介绍**: When the user asks to create an HTML PPT, presentation slides, or a deck, or convert an existing PowerPoint (.pptx) file, use this skill to generate a modern, responsive HTML presentation based on design system specifications (design.md). This includes Chinese requests such as 做PPT、幻灯片、演示文稿、网页版PPT、P

Latest changelog:
- Major simplification and update of the SKILL.md, restructured for faster Mode decision-making and reference.
- Added a "Quick Reference" and "Mode Decision Tree" to clearly map user input to the correct workflow (HTML PPT new creation, PPTx conversion, cover generation).
- Switched the requirements checklist to a shared external file (`references/requirements-checklist.md`) for modularity.
- Now leverages a unified style gallery: all 35+ design templates have preview PNGs in `demo/previews/`, referenced in `designs/STYLE_GALLERY.md` for visual confirmation.
- Updated core presentation standards with expanded non-negotiable rules—mandatory toolbar, strict header space limits, legibility/font sizing, and unified color themes.
- Removed legacy and inlined design/demo directories, consolidating previews and style data for more efficient and consistent template selection.

**关键词**: an, generate-html-ppt, When, user, asks, HTML, PPT, presentation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/generate-html-ppt)

---

## [22. alibabacloud-ebs-usage-summary](https://clawhub.ai/sdk-team/alibabacloud-ebs-usage-summary)

**Slug**: `alibabacloud-ebs-usage-summary`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Analyze Alibaba Cloud block storage (EBS) disk performance and fleet composition. Use it to locate performance bottlenecks (saturated IOPS or bandwidth), compare disks, instances, or availability zones to decide where to tune or resize, review disk count and capacity by category / region / billing type to inform capacity and cost decisions, check disk event history, and reach the right console dashboard for deeper drill-down. Triggers: "EBS monitoring", "disk metrics", "cloud disk performance", "IOPS analysis", "BPS analysis", "disk monitoring data", "export disk monitoring data", "export monitoring data", "metric aggregation", "resource overview", "EBS Lens", "CloudLens for EBS", "disk usage report", "capacity distribution", "event overview", "monitoring dashboard", "EBS dashboard", "storage dashboard", "disk monitoring dashboard", "storage health", "block storage insights", "disk observability", "disk inventory summary", "telemetry console", "block storage analytics".

**中文介绍**: Analyze Alibaba Cloud block storage (EBS) disk performance and fleet composition. Use it to locate performance bottlenecks (saturated IOPS or bandwidth), compare disks, instances, or availability zones to decide where to tune or resize, review disk count and capacity by category / region / billing type to inform capacity and cost decisions, check disk event history, and reach the right console dashboard for deeper drill-down. Triggers: "EBS monitoring", "disk metrics", "cloud disk performance", "IOPS analysis", "BPS analysis", "disk monitoring data", "export disk monitoring data", "export monitoring data", "metric aggregation", "resource overview", "EBS Lens", "CloudLens for EBS", "disk usage report", "capacity distribution", "event overview", "monitoring dashboard", "EBS dashboard", "storage dashboard", "disk monitoring dashboard", "storage health", "block storage insights", "disk observability", "disk inventory summary", "telemetry console", "block storage analytics".

Latest changelog:
Initial release of Alibaba Cloud EBS Usage Summary:

- Analyze EBS disk performance (IOPS, bandwidth, utilization) and identify bottlenecks.
- Summarize disk fleet composition by category, region, and billing type, including disk counts and capacity.
- Review disk event history and provide event summaries by type and region.
- Direct users to the appropriate Alibaba Cloud dashboards for deeper analysis.
- Ensures strict use of EBS APIs for metrics and reports, with guidance on prerequisites and installation steps.

**关键词**: Analyze, Alibaba, Cloud, block, storage, EBS, disk, performance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alibabacloud-ebs-usage-summary)

---

## [23. Plant Growth Stage Recognition Skill | 植物生长阶段识别技能](https://clawhub.ai/smyx-sunjinhui/smyx-plant-growth-stage-recognition-analysis)

**Slug**: `smyx-plant-growth-stage-recognition-analysis`  
**Version**: 1.0.11  
**Stats**: ⭐ 4 | ⬇️ 1675 | 🧩 12

**原始简介**: Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support. | 植物生长阶段识别技能，基于计算机视觉与深度学习算法，精准识别植物从发芽到结果的全生命周期关键生长阶段，为精准农业提供科学决策支持

**中文介绍**: Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support. | 植物生长阶段识别技能，基于计算机视觉与深度学习算法，精准识别植物从发芽到结果的全生命周期关键生长阶段，为精准农业提供科学决策支持

Latest changelog:
- Internal documentation file skill-card.md has been removed.
- Configuration file updated (config.yaml) with unspecified changes.
- No changes made to core features or user-visible functionality.

**关键词**: 植物生长阶段识别技能, Plant, Growth, Stage, Recognition, Skill, Accurately, identifies

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-plant-growth-stage-recognition-analysis)

---

## [24. prospecting](https://clawhub.ai/skills?q=prospecting)

**Slug**: `prospecting`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 868 | 🧩 4

**原始简介**: B2B manufacturing proactive prospecting. Search Google Maps for potential customers based on existing client profiles, enrich leads with business details, score and rank them, and output actionable CSV + JSON lead lists with custom sales openers. Includes chain store strategy: local call → identify

**中文介绍**: B2B manufacturing proactive prospecting. Search Google Maps for potential customers based on existing client profiles, enrich leads with business details, score and rank them, and output actionable CSV + JSON lead lists with custom sales openers. Includes chain store strategy: local call → identify

Latest changelog:
**Major enhancements and compliance updates for prospecting skill.**

- Completed security audit: added compliance, legal boundaries, and data retention requirements.
- Split trigger list into strong (auto-run) and weak (manual-confirm) phrases.
- Removed placeholder phone number examples and clarified data enrichment rules.
- Introduced self-optimization: now auto-detects coverage gaps, adjusts search keywords, and expands search areas.
- Added multi-pass search loop and rules for handling chain brands and suburban expansion.
- Outlined stricter limits for personal data, output handling, and prospect file retention.

**关键词**: B2B, prospecting, manufacturing, proactive, Search, Google, Maps, potential

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/prospecting)

---

## [25. PPT 生成 AI PPT Slides](https://clawhub.ai/dlazyai/dlazy-ppt)

**Slug**: `dlazy-ppt`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

**中文介绍**: Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

Latest changelog:
Route every slide image through the dLazy tool API. Configure with a single DLAZY_API_KEY; no OpenAI or third-party image provider needed.

**关键词**: 生成, PPT, Slides, Generate, visually, unified, image-based, PPTX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dlazy-ppt)

---

