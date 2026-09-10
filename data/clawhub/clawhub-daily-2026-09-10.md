# ClawHub Skills Daily | 2026-09-10

> 共 25 个 skills

## [1. Workbuddy Usage Status](https://clawhub.ai/clancy-feng/workbuddy-usage-status)

**Slug**: `workbuddy-usage-status`  
**Version**: 1.3.3  
**Stats**: ⭐ 0 | ⬇️ 854 | 🧩 11

**原始简介**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

**中文介绍**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

Latest changelog:
v1.3.3:Bug fix

**关键词**: 离线可视化, 本机使用数据, 消耗为主指标、credit, 为本地估算, Workbuddy, Usage, Status, token

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-usage-status)

---

## [2. Multilogin X](https://clawhub.ai/multilogincom/multilogin)

**Slug**: `multilogin`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 1738 | 🧩 2

**原始简介**: Use when you need to manage Multilogin X browser profiles — launch quick disposable profiles, list/start/stop saved profiles, or check launcher status using...

**中文介绍**: Use when you need to manage Multilogin X browser profiles — launch quick disposable profiles, list/start/stop saved profiles, or check launcher status using...

Latest changelog:
- Removed the skill-card.md file.
- No functionality changes; only documentation cleanup.

**关键词**: Multilogin, Use, when, need, manage, browser, profiles, launch

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/multilogin)

---

## [3. context-game](https://clawhub.ai/charlesresearch001/context-game)

**Slug**: `context-game`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 硬科幻政治惊悚开放世界对话游戏《上下文》。当玩家说"开始游戏/继续游戏/新开一档/玩《上下文》"或要求查看状态、存档、退休写史书时使用。agent 担任游戏引擎，玩家以自由文本行动。

**中文介绍**: 硬科幻政治惊悚开放世界对话游戏《上下文》。当玩家说"开始游戏/继续游戏/新开一档/玩《上下文》"或要求查看状态、存档、退休写史书时使用。agent 担任游戏引擎，玩家以自由文本行动。

Latest changelog:
- Initial release of "context-game": a hard sci-fi political thriller open world dialogue game.
- Supports triggering with "start/continue/new game/play context" and allows free-text actions.
- Player actions parsed into intent types; game engine manages NPC, world, and conflict resolution.
- Strict save/load system using state.json and memory.md, with separate move and meta-conversation flows.
- Highlights strict state management, risk/clock mechanics, and narrative rules.

**关键词**: 硬科幻政治惊悚开放世界对话游戏《上下文》, 当玩家说"开始游戏, 继续游戏, 新开一档, Agent, 担任游戏引擎, 玩家以自由文本行动, context-game

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/context-game)

---

## [4. myatriumhealth-mcp](https://clawhub.ai/chrischall/myatriumhealth-mcp)

**Slug**: `myatriumhealth-mcp`  
**Version**: 0.4.1  
**Stats**: ⭐ 0 | ⬇️ 90 | 🧩 3

**原始简介**: Read MyAtriumHealth (Atrium Health's Epic MyChart patient portal) — test results, medications, allergies, immunizations, health issues, visits, goals — from a shell with the fpx CLI (@fetchproxy/cli), by relaying requests through your signed-in Chrome tab. Use when you want your MyChart data in a script or one-shot without running the myatriumhealth-mcp server.

**中文介绍**: Read MyAtriumHealth (Atrium Health's Epic MyChart patient portal) — test results, medications, allergies, immunizations, health issues, visits, goals — from a shell with the fpx CLI (@fetchproxy/cli), by relaying requests through your signed-in Chrome tab. Use when you want your MyChart data in a script or one-shot without running the myatriumhealth-mcp server.

Latest changelog:
No user-facing changes in this version.

- Version bump to 0.4.1 without file modifications.
- No updates to documentation or code detected.

**关键词**: myatriumhealth-mcp, Read, MyAtriumHealth, Atrium, Health's, Epic, MyChart, patient

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/myatriumhealth-mcp)

---

## [5. pingroom](https://clawhub.ai/pingroom/pingroom)

**Slug**: `pingroom`  
**Version**: 1.1.1  
**Stats**: ⭐ 0 | ⬇️ 214 | 🧩 6

**原始简介**: Reach a human through PingRoom from an OpenClaw agent using the `pingroom` CLI — send a ping to their phone (with files up to 5 MiB, tappable links, map locations, or an acknowledgement request), ask a question and block until they answer, gate an action on approve/deny, hand a decision to your authorizing human, drive a lock-screen live-progress card, and stream incoming pings. Use it whenever the task means "notify me", "let me know when it's done", "ask me before deploying", "send this to my phone", "ping the team", or any step that needs a real human decision rather than a guess. Pairing works without a terminal: `pingroom pair --agent-label "OpenClaw"` creates a separate robot profile and prints its claim link. Privacy: everything you pass — message text, attachments, links, and locations — is sent to the PingRoom service and delivered to the paired human's phone, so send only what the user has agreed to share off-platform, and ask first when the request is ambiguous. Also use it when the human asks to redeem a PingRoom gift or promotional code.

**中文介绍**: Reach a human through PingRoom from an OpenClaw agent using the `pingroom` CLI — send a ping to their phone (with files up to 5 MiB, tappable links, map locations, or an acknowledgement request), ask a question and block until they answer, gate an action on approve/deny, hand a decision to your authorizing human, drive a lock-screen live-progress card, and stream incoming pings. Use it whenever the task means "notify me", "let me know when it's done", "ask me before deploying", "send this to my phone", "ping the team", or any step that needs a real human decision rather than a guess. Pairing works without a terminal: `pingroom pair --agent-label "OpenClaw"` creates a separate robot profile and prints its claim link. Privacy: everything you pass — message text, attachments, links, and locations — is sent to the PingRoom service and delivered to the paired human's phone, so send only what the user has agreed to share off-platform, and ask first when the request is ambiguous. Also use it when the human asks to redeem a PingRoom gift or promotional code.

Latest changelog:
Pin CLI 0.11.0 and all dependencies with SHA-512 integrity in a bundled lockfile. Use a local npm ci installation with lifecycle scripts disabled; remove the alternate global installer and require reviewed skill releases for upgrades.

**关键词**: an, Agent, pingroom, Reach, human, through, OpenClaw, CLI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pingroom)

---

## [6. Agent of Empires](https://clawhub.ai/njbrake/aoe)

**Slug**: `aoe`  
**Version**: 1.16.0  
**Stats**: ⭐ 1 | ⬇️ 4178 | 🧩 51

**原始简介**: Manage AI coding agent sessions via Agent of Empires (aoe)

**中文介绍**: Manage AI coding agent sessions via Agent of Empires (aoe)

Latest changelog:
- Removed the file: skill-card.md
- No changes to functionality or documentation in SKILL.md
- Release removes an unused or obsolete documentation file

**关键词**: Agent, of, Empires, Manage, coding, sessions, via, aoe

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aoe)

---

## [7. cloudbase](https://clawhub.ai/binggg/cloudbase)

**Slug**: `cloudbase`  
**Version**: 1.92.89  
**Stats**: ⭐ 0 | ⬇️ 7894 | 🧩 182

**原始简介**: Use this skill when you develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase (腾讯云开发, 云开发, TCB, 微信云开发) projects — Web, 微信小程序, 小程序, uni-app, mobile (iOS, Android, Flutter, React Native). Covers UI (页面, 界面, 表单, dashboard, prototype, 原型); auth (登录, 注册, OAuth, publishable key); databases (NoSQL 文档数据库, MySQL 关系型数据库, PostgreSQL/CloudBase PG, app.rdb(), queryPgDatabase/managePgDatabase, CRUD, security rules); 云函数/cloud functions (serverless, scf_bootstrap); CloudRun (云托管, Dockerfile); 云存储; built-in AI (内置大模型, AI 对话, streaming, 流式输出, 图片生成, generateText, streamText, createModel, generateImage, TokenHub, Hunyuan, DeepSeek, GLM, Kimi, Token Credits 资源包, 小程序成长计划); third-party/custom model onboarding (第三方大模型接入, 大模型调用, LLM API); AI agent (智能体, AG-UI, LangGraph); ops troubleshooting (巡检, 诊断, 日志); spec workflow (需求文档, 技术方案, requirements, tasks.md). Do NOT use for non-CloudBase projects, pure frontend without CloudBase, or self-hosted backends without CloudBase.

**中文介绍**: Use this skill when you develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase (腾讯云开发, 云开发, TCB, 微信云开发) projects — Web, 微信小程序, 小程序, uni-app, mobile (iOS, Android, Flutter, React Native). Covers UI (页面, 界面, 表单, dashboard, prototype, 原型); auth (登录, 注册, OAuth, publishable key); databases (NoSQL 文档数据库, MySQL 关系型数据库, PostgreSQL/CloudBase PG, app.rdb(), queryPgDatabase/managePgDatabase, CRUD, security rules); 云函数/cloud functions (serverless, scf_bootstrap); CloudRun (云托管, Dockerfile); 云存储; built-in AI (内置大模型, AI 对话, streaming, 流式输出, 图片生成, generateText, streamText, createModel, generateImage, TokenHub, Hunyuan, DeepSeek, GLM, Kimi, Token Credits 资源包, 小程序成长计划); third-party/custom model onboarding (第三方大模型接入, 大模型调用, LLM API); AI agent (智能体, AG-UI, LangGraph); ops troubleshooting (巡检, 诊断, 日志); spec workflow (需求文档, 技术方案, requirements, tasks.md). Do NOT use for non-CloudBase projects, pure frontend without CloudBase, or self-hosted backends without CloudBase.

Latest changelog:
Recent commits / 最近提交: | - feat(skills): add optional Deployment Share after verified deploys (#1023) | - chore: sync cloudbase plugin skills from upstream | - docs(skills): promote publishable key auto-provisioning to a cross-skill convention (#1020) (#1021) | - fix: correct stale entry points and version pins, sync server.json at publish time (#1018) | - docs(skills): PG env routing, owner-table template, public-read bucket RLS, migration retry semantics (#1019)

**关键词**: cloudbase, Use, skill, when, develop, design, build, deploy

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cloudbase)

---

## [8. huawei-cloud-skill-tester](https://clawhub.ai/skills?q=huawei-cloud-skill-tester)

**Slug**: `huawei-cloud-skill-tester`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 300 | 🧩 6

**原始简介**: End-to-end functional testing framework for Huawei Cloud skills — three-tier pipeline covering single-skill unit testing, multi-skill orchestration, and end-to-end full flow testing. Each phase produces structured JSON output with chain verification. Supports skill installation validation, functional analysis, CLI→SDK→API feasibility research, test case generation, real-environment execution with resource lifecycle, resource cleanup, multi-skill scenario orchestration, trigger-conflict detection, and consolidated reporting. Triggers include: 测试技能, 执行技能测试, 跑测试流程, 技能回归测试, skill test, run skill tests, test huawei cloud skill, verify skill, 测试华为云skill, 全流程测试, 编排测试, 技能完整性检查, skill-tester, 跑测试, 回归测试, 组合测试, 多skill编排, verification, e2e.

**中文介绍**: End-to-end functional testing framework for Huawei Cloud skills — three-tier pipeline covering single-skill unit testing, multi-skill orchestration, and end-to-end full flow testing. Each phase produces structured JSON output with chain verification. Supports skill installation validation, functional analysis, CLI→SDK→API feasibility research, test case generation, real-environment execution with resource lifecycle, resource cleanup, multi-skill scenario orchestration, trigger-conflict detection, and consolidated reporting. Triggers include: 测试技能, 执行技能测试, 跑测试流程, 技能回归测试, skill test, run skill tests, test huawei cloud skill, verify skill, 测试华为云skill, 全流程测试, 编排测试, 技能完整性检查, skill-tester, 跑测试, 回归测试, 组合测试, 多skill编排, verification, e2e.

Latest changelog:
- Introduced an end-to-end functional testing framework for Huawei Cloud skills, supporting unit, integration, and full-flow testing phases.
- Features standardized three-track, eight-phase pipeline with structured JSON outputs and chain verification.
- Supports multi-skill orchestration, real-environment execution, trigger-conflict detection, and consolidated reporting.
- Enforces safety principles: agent-proof write operations and stepwise, batch-repeatable execution.
- Requires hcloud CLI, Python SDKs, jq for processing, and proper environment variable setup for secure AK/SK handling.

**关键词**: End-to-end, functional, testing, framework, Huawei, Cloud, skills, three-tier

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-skill-tester)

---

## [9. huawei-cloud-vod-collector](https://clawhub.ai/skills?q=huawei-cloud-vod-collector)

**Slug**: `huawei-cloud-vod-collector`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 491 | 🧩 8

**原始简介**: Invoke this skill to capture poor experiences and distill them into high-value requirements (Voice of Developer). Use when user encounters any Huawei Cloud related issues, like user expresses dissatisfaction, encounters errors, or wants to report issues/suggestions.Triggers include: "体验差","反馈问题","反馈建议","这个有bug","拒绝了请求","报告问题","反馈体验","report a problem","report a suggestion","bug report","poor experience","voice of developer"

**中文介绍**: Invoke this skill to capture poor experiences and distill them into high-value requirements (Voice of Developer). Use when user encounters any Huawei Cloud related issues, like user expresses dissatisfaction, encounters errors, or wants to report issues/suggestions.Triggers include: "体验差","反馈问题","反馈建议","这个有bug","拒绝了请求","报告问题","反馈体验","report a problem","report a suggestion","bug report","poor experience","voice of developer"

Latest changelog:
- Improved SKILL.md documentation for usability: added detailed instructions, parameter explanations, workflow phases, and security notes.
- Clarified triggers and scenarios for invoking the skill.
- Expanded command examples, including auto-login steps and feedback deduplication rules.
- Updated references and prerequisites for setup and integration.
- No core logic or interface changes; these updates enhance clarity, guidance, and correct usage.

**关键词**: Invoke, skill, capture, poor, experiences, distill, them, high-value

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-vod-collector)

---

## [10. huawei-cloud-skill-audit](https://clawhub.ai/huaweiclouddev/huawei-cloud-skill-audit)

**Slug**: `huawei-cloud-skill-audit`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 504 | 🧩 5

**原始简介**: Audit Huawei Cloud skills for quality, security, and compliance using a two-check pipeline: skillspector (AI security) and gitleaks (credential leak). Generates structured reports with issue details and fix strategies. Triggers include: "审计技能","技能审计","检查技能质量","扫描技能问题","技能安全审计", "audit skill","check skill quality","scan skills for issues","skill audit", "华为云技能审计","技能合规检查","skill gate","质量门禁","技能检查", "audit huawei cloud skill","verify skill compliance","技能质量检查","跑审计","安全扫描".

**中文介绍**: Audit Huawei Cloud skills for quality, security, and compliance using a two-check pipeline: skillspector (AI security) and gitleaks (credential leak). Generates structured reports with issue details and fix strategies. Triggers include: "审计技能","技能审计","检查技能质量","扫描技能问题","技能安全审计", "audit skill","check skill quality","scan skills for issues","skill audit", "华为云技能审计","技能合规检查","skill gate","质量门禁","技能检查", "audit huawei cloud skill","verify skill compliance","技能质量检查","跑审计","安全扫描".

Latest changelog:
huawei-cloud-skill-audit v1.0.4

- Updated documentation in SKILL.md to refine parameter details and clarify behavior of tool auto-install paths.
- Example paths for overrides now use ~/.local/bin for consistency.
- skill-card.md file has been removed.
- Minor adjustments to Python scripts: scripts/skill_audit.py and scripts/skill_quality_sdk.py for alignment with new docs and improved reliability.

**关键词**: huawei-cloud-skill-audit, Audit, Huawei, Cloud, skills, quality, security, compliance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-skill-audit)

---

## [11. retail-assortment-gap-analysis](https://clawhub.ai/crawlora-org/retail-assortment-gap-analysis)

**Slug**: `retail-assortment-gap-analysis`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 102 | 🧩 7

**原始简介**: Compare competing retail assortments through Crawlora catalogs. Use to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

**中文介绍**: Compare competing retail assortments through Crawlora catalogs. Use to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

Latest changelog:
Validate API keys before curl config

**关键词**: Compare, competing, retail, assortments, through, Crawlora, catalogs, Use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/retail-assortment-gap-analysis)

---

## [12. Cinematic Scroll — 3D Website Design](https://clawhub.ai/mustbesimo/cinematic-scroll)

**Slug**: `cinematic-scroll`  
**Version**: 2.7.5  
**Stats**: ⭐ 1 | ⬇️ 1331 | 🧩 12

**原始简介**: Design and build cinematic websites, 3D websites, interactive portfolios and product landing pages with scroll-driven storytelling, parallax, text animation and optional Three.js/WebGL scenes. Use for new experiences, motion improvements, scroll audits and storyboards in standalone HTML or an existing app. Includes responsive, reduced-motion and static fallbacks; not for ordinary dashboards or unrelated animation.

**中文介绍**: Design and build cinematic websites, 3D websites, interactive portfolios and product landing pages with scroll-driven storytelling, parallax, text animation and optional Three.js/WebGL scenes. Use for new experiences, motion improvements, scroll audits and storyboards in standalone HTML or an existing app. Includes responsive, reduced-motion and static fallbacks; not for ordinary dashboards or unrelated animation.

Latest changelog:
Clearer discovery for 3D websites, interactive portfolios and cinematic landing pages. Adds subject-based 3D selection guidance, motion toolkit reference and a direct live-example gallery link. Self-contained text-only edition with responsive and reduced-motion guidance.

**关键词**: 3D, Cinematic, Scroll, Website, Design, build, websites, interactive

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cinematic-scroll)

---

## [13. stellar-trails](https://clawhub.ai/hoshiyomix/stellar-trails)

**Slug**: `stellar-trails`  
**Version**: 9.15.3  
**Stats**: ⭐ 0 | ⬇️ 3593 | 🧩 89

**原始简介**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

**中文介绍**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

Latest changelog:
v9.15.3 — see CHANGELOG.md

**关键词**: stellar-trails, Activates, every, task, coding, features, bugs, refactoring

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stellar-trails)

---

## [14. MagicPay](https://clawhub.ai/xor777/magicpay)

**Slug**: `magicpay`  
**Version**: 0.4.43  
**Stats**: ⭐ 0 | ⬇️ 2786 | 🧩 51

**原始简介**: Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

**中文介绍**: Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

Latest changelog:
Release magicpay-v0.4.43

**关键词**: Agent, MagicPay, Use, payments, funding, Memory, email, account

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/magicpay)

---

## [15. google-maps-research](https://clawhub.ai/crawlora-org/google-maps-research)

**Slug**: `google-maps-research`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 108 | 🧩 7

**原始简介**: Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API. Use for current place lookups and comparisons, including addresses, ratings, review themes, and business information.

**中文介绍**: Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API. Use for current place lookups and comparisons, including addresses, ratings, review themes, and business information.

Latest changelog:
Validate API keys before curl config

**关键词**: google-maps-research, Search, Google, Maps, businesses, places, retrieve, place

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/google-maps-research)

---

## [16. influencer-discovery](https://clawhub.ai/skills?q=influencer-discovery)

**Slug**: `influencer-discovery`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 41 | 🧩 8

**原始简介**: Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints. Use for creator sourcing, comparing campaign fit, and producing an evidence-backed influencer shortlist.

**中文介绍**: Find and shortlist TikTok, Instagram, and YouTube creators for a campaign using Crawlora's creator datasets and live profile/content endpoints. Use for creator sourcing, comparing campaign fit, and producing an evidence-backed influencer shortlist.

Latest changelog:
Validate API keys before curl config

**关键词**: influencer-discovery, Find, shortlist, TikTok, Instagram, YouTube, creators, campaign

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/influencer-discovery)

---

## [17. wish-research](https://clawhub.ai/crawlora-org/wish-research)

**Slug**: `wish-research`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 448 | 🧩 14

**原始简介**: Researches Wish's marketplace — categories, product search, product detail, related items, and reviews — using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Wish, browse Wish categories, compare Wish product prices/ratings, or pull a Wish product's related items and reviews — instead of scraping wish.com.

**中文介绍**: Researches Wish's marketplace — categories, product search, product detail, related items, and reviews — using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Wish, browse Wish categories, compare Wish product prices/ratings, or pull a Wish product's related items and reviews — instead of scraping wish.com.

Latest changelog:
Validate API keys before curl config

**关键词**: wish-research, Researches, Wish's, marketplace, categories, product, search, detail

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wish-research)

---

## [18. travel-hotel-research](https://clawhub.ai/crawlora-org/travel-hotel-research)

**Slug**: `travel-hotel-research`  
**Version**: 1.0.15  
**Stats**: ⭐ 0 | ⬇️ 597 | 🧩 16

**原始简介**: Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API — Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster — returning clean JSON. Use when the user wants to search or compare hotel/stay prices and reviews, look up flight options, find attractions/things-to-do or concerts/events, or research an Airbnb host or listing.

**中文介绍**: Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API — Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster — returning clean JSON. Use when the user wants to search or compare hotel/stay prices and reviews, look up flight options, find attractions/things-to-do or concerts/events, or research an Airbnb host or listing.

Latest changelog:
Validate API keys before curl config

**关键词**: travel-hotel-research, Researches, hotels, flights, attractions, short-term, rentals, live

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/travel-hotel-research)

---

## [19. local-business-prospecting](https://clawhub.ai/crawlora-org/local-business-prospecting)

**Slug**: `local-business-prospecting`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 111 | 🧩 8

**原始简介**: Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites. Use when the user wants a deduplicated lead shortlist or CSV with business contacts and qualification evidence.

**中文介绍**: Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites. Use when the user wants a deduplicated lead shortlist or CSV with business contacts and qualification evidence.

Latest changelog:
Validate API keys before curl config

**关键词**: Build, qualify, local-business, prospect, lists, category, geography, Crawlora's

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/local-business-prospecting)

---

## [20. website-monitoring](https://clawhub.ai/crawlora-org/website-monitoring)

**Slug**: `website-monitoring`  
**Version**: 1.0.10  
**Stats**: ⭐ 0 | ⬇️ 290 | 🧩 11

**原始简介**: Creates and manages website-change monitors via the Crawlora API — watch a page for a content change or a sitemap for added/removed URLs, and get a signed webhook the moment something changes. No polling loop or diffing pipeline to run yourself. Use when the user wants to track a competitor's pricing page, watch for new pages on a site, get notified when content changes, or otherwise avoid re-checking a URL by hand.

**中文介绍**: Creates and manages website-change monitors via the Crawlora API — watch a page for a content change or a sitemap for added/removed URLs, and get a signed webhook the moment something changes. No polling loop or diffing pipeline to run yourself. Use when the user wants to track a competitor's pricing page, watch for new pages on a site, get notified when content changes, or otherwise avoid re-checking a URL by hand.

Latest changelog:
Validate API keys before curl config

**关键词**: API, website-monitoring, Creates, manages, website-change, monitors, via, Crawlora

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/website-monitoring)

---

## [21. zara-research](https://clawhub.ai/crawlora-org/zara-research)

**Slug**: `zara-research`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 454 | 🧩 14

**原始简介**: Researches Zara's catalog — category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores — using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Zara, browse a Zara category, search Zara's catalog by keyword, pull a Zara product's colors/sizes/images, or find a nearby Zara store — instead of scraping zara.com.

**中文介绍**: Researches Zara's catalog — category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores — using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Zara, browse a Zara category, search Zara's catalog by keyword, pull a Zara product's colors/sizes/images, or find a nearby Zara store — instead of scraping zara.com.

Latest changelog:
Validate API keys before curl config

**关键词**: zara-research, Researches, Zara's, catalog, category, taxonomy, listings, product

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zara-research)

---

## [22. zalando-research](https://clawhub.ai/crawlora-org/zalando-research)

**Slug**: `zalando-research`  
**Version**: 1.0.14  
**Stats**: ⭐ 0 | ⬇️ 574 | 🧩 15

**原始简介**: Researches products, prices, brands, and categories on Zalando (the European fashion marketplace) using the Crawlora API, returning clean JSON. Use when the user asks to find a product, browse a category or brand, autocomplete a search, or resolve a Zalando storefront market — instead of scraping Zalando pages.

**中文介绍**: Researches products, prices, brands, and categories on Zalando (the European fashion marketplace) using the Crawlora API, returning clean JSON. Use when the user asks to find a product, browse a category or brand, autocomplete a search, or resolve a Zalando storefront market — instead of scraping Zalando pages.

Latest changelog:
Validate API keys before curl config

**关键词**: zalando-research, Researches, products, prices, brands, categories, Zalando, European

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zalando-research)

---

## [23. zappos-research](https://clawhub.ai/crawlora-org/zappos-research)

**Slug**: `zappos-research`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 453 | 🧩 14

**原始简介**: Researches Zappos's footwear and apparel catalog — the brand directory, product search, and product detail (pricing, images, ratings, fit feedback, color variants) — using the Crawlora API, returning clean JSON. Use when the user asks to find a shoe or apparel item on Zappos, look up or browse a specific Zappos brand's catalog, or pull a Zappos product's pricing/rating/variant/fit detail — instead of scraping zappos.com.

**中文介绍**: Researches Zappos's footwear and apparel catalog — the brand directory, product search, and product detail (pricing, images, ratings, fit feedback, color variants) — using the Crawlora API, returning clean JSON. Use when the user asks to find a shoe or apparel item on Zappos, look up or browse a specific Zappos brand's catalog, or pull a Zappos product's pricing/rating/variant/fit detail — instead of scraping zappos.com.

Latest changelog:
Validate API keys before curl config

**关键词**: zappos-research, Researches, Zappos's, footwear, apparel, catalog, brand, directory

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zappos-research)

---

## [24. yahoo-network-research](https://clawhub.ai/crawlora-org/yahoo-network-research)

**Slug**: `yahoo-network-research`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 438 | 🧩 14

**原始简介**: Researches Yahoo's editorial content network — Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech — via the Crawlora API, returning clean JSON. Each vertical shares a home/category story-stream plus full-article-content pattern; Yahoo Sports adds deeper sports-data endpoints (scoreboards, standings, team/player/roster, golf, MMA, motorsports, tennis, Olympics). Use when the user wants a Yahoo section's story feed, a Yahoo article's full content, Yahoo News comments, Yahoo Shopping deals/lists, or Yahoo Sports scores/standings/schedules. Yahoo Finance and Yahoo Search are covered by their own separate skills, not this one.

**中文介绍**: Researches Yahoo's editorial content network — Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech — via the Crawlora API, returning clean JSON. Each vertical shares a home/category story-stream plus full-article-content pattern; Yahoo Sports adds deeper sports-data endpoints (scoreboards, standings, team/player/roster, golf, MMA, motorsports, tennis, Olympics). Use when the user wants a Yahoo section's story feed, a Yahoo article's full content, Yahoo News comments, Yahoo Shopping deals/lists, or Yahoo Sports scores/standings/schedules. Yahoo Finance and Yahoo Search are covered by their own separate skills, not this one.

Latest changelog:
Validate API keys before curl config

**关键词**: yahoo-network-research, Researches, Yahoo's, editorial, content, network, Autos, Entertainment

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yahoo-network-research)

---

## [25. x-research](https://clawhub.ai/skills?q=x-research)

**Slug**: `x-research`  
**Version**: 1.0.14  
**Stats**: ⭐ 0 | ⬇️ 160 | 🧩 15

**原始简介**: Researches X (formerly Twitter) profiles and posts via the Crawlora API, returning clean JSON. Use when the user wants a public X profile's stats, a user's recent posts, or a single post's content/engagement — instead of scraping x.com or using the official (paid, rate-limited) X API.

**中文介绍**: Researches X (formerly Twitter) profiles and posts via the Crawlora API, returning clean JSON. Use when the user wants a public X profile's stats, a user's recent posts, or a single post's content/engagement — instead of scraping x.com or using the official (paid, rate-limited) X API.

Latest changelog:
Validate API keys before curl config

**关键词**: x-research, Researches, formerly, Twitter, profiles, posts, via, Crawlora

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x-research)

---

