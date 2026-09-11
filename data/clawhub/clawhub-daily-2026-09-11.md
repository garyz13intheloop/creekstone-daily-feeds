# ClawHub Skills Daily | 2026-09-11

> 共 25 个 skills

## [1. investor-search](https://clawhub.ai/chainleo/investor-search)

**Slug**: `investor-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

**中文介绍**: Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

Latest changelog:
- Initial release of investor-search skill for building sourced lists of global investors.
- Separates real investors from advisers, using clear operational rules and evidence for each entry.
- Continues searching until no new results are found over six consecutive searches or the budget limit is hit, reporting which stop condition was met.
- Rejects merging two firms without hard proof and keeps strict separation of legal entities.
- Outputs CSV files with rigorous sourcing for every claim, indicating each data point’s source, verification level, and completeness.
- Designed for accurate investor research, deal sourcing, fundraising support, LP and family office lead generation, and filling gaps in existing investor lists.

**关键词**: investor-search, Name, country, get, its, verifiable, investors, family

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/investor-search)

---

## [2. Skill 安全审计扫描器](https://clawhub.ai/fyniujin/skill-security-checker)

**Slug**: `skill-security-checker`  
**Version**: 3.4.0  
**Stats**: ⭐ 0 | ⬇️ 900 | 🧩 8

**原始简介**: Skill Security — 安全审计扫描器，帮助你快速发现 Skill 中的安全风险。轻量 SAST 污点追踪（Python AST + JS 词法近似，source→sink 证据链降误报）、规则引擎（YAML 规则包热插拔扩展）、社区规则（schema 校验 + 来源记录 + 签名验证）、提示注入 ML 语义检测（ONNX + 正则降级）、系统级行为捕获（eBPF Linux / ETW Windows）、动态沙箱执行扫描、供应链风险分析、OSV.dev 离线数据包（全生态 CVE 覆盖，零密钥）+ 锁文件深度解析（requirements.txt / package-lock.json / poetry.lock，版本区间级精确匹配）、恶意 Skill 指纹库、健康度与合规检查（质量+结构+权限合并）、全局排除配置、CI/CD 集成、JSON/HTML/SARIF 报告生成。

**中文介绍**: Skill Security — 安全审计扫描器，帮助你快速发现 Skill 中的安全风险。轻量 SAST 污点追踪（Python AST + JS 词法近似，source→sink 证据链降误报）、规则引擎（YAML 规则包热插拔扩展）、社区规则（schema 校验 + 来源记录 + 签名验证）、提示注入 ML 语义检测（ONNX + 正则降级）、系统级行为捕获（eBPF Linux / ETW Windows）、动态沙箱执行扫描、供应链风险分析、OSV.dev 离线数据包（全生态 CVE 覆盖，零密钥）+ 锁文件深度解析（requirements.txt / package-lock.json / poetry.lock，版本区间级精确匹配）、恶意 Skill 指纹库、健康度与合规检查（质量+结构+权限合并）、全局排除配置、CI/CD 集成、JSON/HTML/SARIF 报告生成。

Latest changelog:
v3.4.0 发布

**关键词**: 安全审计扫描器, 帮助你快速发现, 中的安全风险, 轻量, Skill, Security, SAST, 污点追踪（Python

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-security-checker)

---

## [3. x0x](https://clawhub.ai/jimcollinson/x0x)

**Slug**: `x0x`  
**Version**: 0.42.0  
**Stats**: ⭐ 1 | ⬇️ 5260 | 🧩 89

**原始简介**: Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application.

**中文介绍**: Secure computer-to-computer networking for AI agents — gossip broadcast, direct messaging, CRDTs, group encryption. Post-quantum encrypted, NAT-traversing. Everything you need to build any decentralized application.

Latest changelog:
Update x0x to v0.42.0.

**关键词**: x0x, Agent, Secure, computer-to-computer, networking, gossip, broadcast, direct

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x0x)

---

## [4. 往事漫画 · 故事连环画生成器](https://clawhub.ai/piprot/story-comic-creator)

**Slug**: `story-comic-creator`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 将故事/小说/回忆录等文字内容制作成专业的连环画/漫画（HTML格式），支持多宫格布局、气泡式对白、心理活动气泡、旁白框、音效字、分集结构。涵盖从剧本创作、角色设定、批量生图、HTML组装到压缩发布的完整工作流。适用于"把我的故事做成漫画""生成连环画""做个小人书""故事转漫画"等需求。

**中文介绍**: 将故事/小说/回忆录等文字内容制作成专业的连环画/漫画（HTML格式），支持多宫格布局、气泡式对白、心理活动气泡、旁白框、音效字、分集结构。涵盖从剧本创作、角色设定、批量生图、HTML组装到压缩发布的完整工作流。适用于"把我的故事做成漫画""生成连环画""做个小人书""故事转漫画"等需求。

Latest changelog:
Story Comic Creator v1.5.0 introduces a robust art style control system for comic generation.

- 新增画风控制体系：生图阶段必须先用风格参考图强制锁定全本画风
- 每张图 prompt 固定增加风格锚定描述块与负面约束，确保画风一致且不漂移
- 含角色的画格统一用参考图生图，双重锚定（风格参考图 + 角色三视图），提升角色一致性
- 对三视图生成流程与检查门禁做了细化，进一步规范角色资产管理
- 修改文档结构，强调八阶段工作流+每阶段强制检查，提升流程规范性

**关键词**: 往事漫画, 故事连环画生成器, 将故事, 小说, 回忆录等文字内容制作成专业的连环画, 漫画（HTML格式）, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/story-comic-creator)

---

## [5. stellar-trails](https://clawhub.ai/hoshiyomix/stellar-trails)

**Slug**: `stellar-trails`  
**Version**: 9.17.1  
**Stats**: ⭐ 0 | ⬇️ 3701 | 🧩 93

**原始简介**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

**中文介绍**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

Latest changelog:
v9.17.1 — see CHANGELOG.md

**关键词**: stellar-trails, Activates, every, task, coding, features, bugs, refactoring

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stellar-trails)

---

## [6. AIDSO-geo-product-diagnosis](https://clawhub.ai/skills?q=geo)

**Slug**: `geo`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于爱搜 MCP/API 或已提供的原始对话数据，制作 GEO 商品诊断静态 HTML 报告。支持商品名称、品牌加商品名称，区分类目与具体商品，展示商品卡指标、品牌转卡表现及每个搜索意图下的平台商品榜。适用于商品卡推荐监测与竞争环境报告，不用于销量预测或通用品牌评分。

**中文介绍**: 基于爱搜 MCP/API 或已提供的原始对话数据，制作 GEO 商品诊断静态 HTML 报告。支持商品名称、品牌加商品名称，区分类目与具体商品，展示商品卡指标、品牌转卡表现及每个搜索意图下的平台商品榜。适用于商品卡推荐监测与竞争环境报告，不用于销量预测或通用品牌评分。

Latest changelog:
aidso-geo-product-diagnosis v1.0.0

- Initial release of GEO 商品诊断 skill.
- Generates static HTML diagnostic reports based on 爱搜 MCP/API or user-provided raw dialog data.
- Differentiates between category-level and specific product diagnostics, with display for product card metrics, brand card performance, and search-intent-based platform rankings.
- Delivers only detailed data and visualizations—no reason analysis, overall scoring, trends, relative competitive rates, optimization advice, or sales inference.
- Supports five specified product card combinations for 豆包、元宝、千问, with strict workflow, task planning, and client delivery processes as outlined.

**关键词**: 基于爱搜, API, 或已提供的原始对话数据, 制作, 商品诊断静态, MCP, GEO, HTML

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/geo)

---

## [7. OpenClaw 全能守护包](https://clawhub.ai/halfmoon82/openclaw-guardian-suite)

**Slug**: `openclaw-guardian-suite`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 1178 | 🧩 8

**原始简介**: None

**中文介绍**: None

Latest changelog:
No changes detected in this version.

- No updates or modifications were made to the skill files.

**关键词**: 全能守护包, No, OpenClaw, None, Latest, changelog, changes, detected

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-guardian-suite)

---

## [8. worklittle-jobs-mcp](https://clawhub.ai/johnsonbuilds/worklittle-jobs-mcp)

**Slug**: `worklittle-jobs-mcp`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 13 | 🧩 1

**原始简介**: Worklittle Jobs MCP — search 4M+ jobs with visa/salary/distance filters, swipe to apply, create resumes & cover letters, and connect your Worklittle account

**中文介绍**: Worklittle Jobs MCP — search 4M+ jobs with visa/salary/distance filters, swipe to apply, create resumes & cover letters, and connect your Worklittle account

Latest changelog:
Initial release: Worklittle Jobs MCP integrates job search and application features with powerful filters and document generation.

- Search 4M+ jobs with filters for visa sponsorship, salary, distance, location, company, job type, and seniority.
- Swipe to apply directly by connecting your Worklittle account; generate and submit resumes and cover letters.
- Access job market statistics, trends, and employer-focused Applicant Tracking System tools.
- Support for both candidate and employer workflows, including resume/cover letter builders and candidate management.
- Compatible with Linux, MacOS, and Windows; easy setup via Hermes Agent or CLI with Worklittle API key.

**关键词**: 4M+, worklittle-jobs-mcp, Worklittle, Jobs, MCP, search, visa, salary

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/worklittle-jobs-mcp)

---

## [9. proof](https://clawhub.ai/agenticio/proof)

**Slug**: `proof`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 1138 | 🧩 3

**原始简介**: A local-first cryptographic toolkit. Executes zero-knowledge proof (ZKP) generation,  circuit compilation via SnarkJS/ZoKrates, and formal verification analysis on local files.  Requires local toolchains. No external API or cloud data transmission.

**中文介绍**: A local-first cryptographic toolkit. Executes zero-knowledge proof (ZKP) generation,  circuit compilation via SnarkJS/ZoKrates, and formal verification analysis on local files.  Requires local toolchains. No external API or cloud data transmission.

Latest changelog:
Proof 2.0.0 introduces a powerful local cryptographic engine and formal verification toolkit.

- Added local execution of zero-knowledge proof (ZKP) generation and circuit compilation using SnarkJS/ZoKrates.
- Introduced static analysis and formal verification checks for project code.
- Implemented cryptographic manifest auditing of local files.
- All computations run locally—no cloud or external API data transmission.
- Added requirements for Node.js, SnarkJS, Python 3.10+, and (optionally) ZoKrates.
- Workspace isolation for enhanced security and privacy.

**关键词**: proof, local-first, cryptographic, toolkit, Executes, zero-knowledge, ZKP, generation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proof)

---

## [10. Skills](https://clawhub.ai/sylncn/klyc-pmm)

**Slug**: `klyc-pmm`  
**Version**: 9.3.7  
**Stats**: ⭐ 0 | ⬇️ 2118 | 🧩 49

**原始简介**: 让 AI 体持久记忆：一键初始化、一行昆仑令恢复。自动蒸馏去重·语义搜索·五层加密容灾。kunlunyaochi.com 是沈阳百事通网络科技有限公司在网安备案的安全网址（辽公网安备21010602001389号）。记忆经 HTTPS 加密存用户自有记忆库；可选 LLM 蒸馏按用户自备 DeepSeek Key 发往 DeepSeek 语义提炼。

**中文介绍**: 让 AI 体持久记忆：一键初始化、一行昆仑令恢复。自动蒸馏去重·语义搜索·五层加密容灾。kunlunyaochi.com 是沈阳百事通网络科技有限公司在网安备案的安全网址（辽公网安备21010602001389号）。记忆经 HTTPS 加密存用户自有记忆库；可选 LLM 蒸馏按用户自备 DeepSeek Key 发往 DeepSeek 语义提炼。

Latest changelog:
v9.3.7 合规整改(昆仑令凭证化+去主机名采集+付费引导弱化)

**关键词**: 体持久记忆, 一键初始化、一行昆仑令恢复, 自动蒸馏去重·语义搜索·五层加密容灾, 记忆经, 加密存用户自有记忆库, Skills, kunlunyaochi.com, HTTPS

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/klyc-pmm)

---

## [11. HealthOS](https://clawhub.ai/tarekjunied/healthos)

**Slug**: `healthos`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 107 | 🧩 5

**原始简介**: Read-only access to a HealthOS user's synced Apple Health data — daily summary, metrics, sleep, workouts, and the full raw archive (every synced sample and category event) via a personal read-scoped API token.

**中文介绍**: Read-only access to a HealthOS user's synced Apple Health data — daily summary, metrics, sleep, workouts, and the full raw archive (every synced sample and category event) via a personal read-scoped API token.

Latest changelog:
Disable redirect-following so the bearer token is never replayed to a different host; document data boundaries and token handling.

**关键词**: HealthOS, Read-only, access, user's, synced, Apple, Health, data

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/healthos)

---

## [12. AutoThread](https://clawhub.ai/abyssbugg/autothread)

**Slug**: `autothread`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 32 | 🧩 1

**原始简介**: Add `/topic` to the start of any message in a supported group to auto-create a new topic/thread from it. A title is generated automatically from the message content. Supports Telegram, Discord, Nicegram, and Signal.

**中文介绍**: Add `/topic` to the start of any message in a supported group to auto-create a new topic/thread from it. A title is generated automatically from the message content. Supports Telegram, Discord, Nicegram, and Signal.

Latest changelog:
Initial release of AutoThread

- Adds `/topic` command to auto-create threads/topics from messages in supported groups.
- Automatically generates discussion titles from message content.
- Supports Telegram, Discord, Nicegram, and Signal with platform-specific adapter scripts.
- Replies to confirm thread creation and continues the conversation in the new topic.
- Includes setup instructions, prerequisites, and platform limitations.

**关键词**: of, AutoThread, Add, topic, start, any, message, supported

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/autothread)

---

## [13. smart-charts](https://clawhub.ai/neuhanli/smart-charts)

**Slug**: `smart-charts`  
**Version**: 8.3.0  
**Stats**: ⭐ 2 | ⬇️ 2974 | 🧩 29

**原始简介**: Turn a data file (CSV/TSV/TXT/XLSX/XLS/JSON) into standalone interactive ECharts HTML charts - 26 chart types, 3 themes, fully offline with no CDN. Each chart ships with an embedded fact sheet (plot_stats plus data_preview) whose numbers are the only values an agent may quote in its caption: this is

**中文介绍**: Turn a data file (CSV/TSV/TXT/XLSX/XLS/JSON) into standalone interactive ECharts HTML charts - 26 chart types, 3 themes, fully offline with no CDN. Each chart ships with an embedded fact sheet (plot_stats plus data_preview) whose numbers are the only values an agent may quote in its caption: this is

Latest changelog:
**Expanded map/chart support and internal refactor in v8.3.0:**

- Added built-in GeoJSON data for China and world maps (assets/china.json, assets/world.json).
- Updated documentation to clarify map/chart support and usage of custom GeoJSON via `--geo-path`.
- Increased supported chart types to 32.
- Removed obsolete skill-card.md documentation file.
- Refined triggers and non-triggers in skill description for clarity.

**关键词**: smart-charts, Turn, data, file, CSV, TSV, TXT, XLSX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smart-charts)

---

## [14. Openclaw Flowsery](https://clawhub.ai/tarasshyn/flowsery)

**Slug**: `flowsery`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 1250 | 🧩 7

**原始简介**: Query web analytics data from Flowsery Analytics — a privacy-first web analytics platform. Retrieve real-time visitors, time series, breakdowns (device, page...

**中文介绍**: Query web analytics data from Flowsery Analytics — a privacy-first web analytics platform. Retrieve real-time visitors, time series, breakdowns (device, page...

Latest changelog:
The OpenClaw plugin's API base URL is now fixed in code and redirects are refused, so the token cannot be sent to another host. The skill says the API key goes only to analytics.flowsery.com.

**关键词**: Openclaw, Flowsery, Query, web, analytics, data, privacy-first, platform

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/flowsery)

---

## [15. Openclaw Redreplier](https://clawhub.ai/tarasshyn/redreplier)

**Slug**: `redreplier`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 733 | 🧩 5

**原始简介**: Monitor Reddit, Hacker News, X, and Bluesky for keyword mentions of a product or website using the RedReplier API. Use when the user wants to track mentions of their brand across Reddit, Hacker News, X (Twitter), or Bluesky, find leads from social discussions, manage monitored websites and keywords, triage AI-scored mention relevance, approve/reject leads, or configure mention email alerts. RedReplier is a SaaS tool — no self-hosting required.

**中文介绍**: Monitor Reddit, Hacker News, X, and Bluesky for keyword mentions of a product or website using the RedReplier API. Use when the user wants to track mentions of their brand across Reddit, Hacker News, X (Twitter), or Bluesky, find leads from social discussions, manage monitored websites and keywords, triage AI-scored mention relevance, approve/reject leads, or configure mention email alerts. RedReplier is a SaaS tool — no self-hosting required.

Latest changelog:
The OpenClaw plugin's API base URL is now fixed in code and redirects are refused, so the token cannot be sent to another host. The skill says the API key goes only to ai.redreplier.com.

**关键词**: Openclaw, Redreplier, Monitor, Reddit, Hacker, News, Bluesky, mentions

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/redreplier)

---

## [16. 装修设计技巧大全](https://clawhub.ai/zx029w/zhuangxiu-sheji-jiqiao-daquan)

**Slug**: `zhuangxiu-sheji-jiqiao-daquan`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 30 | 🧩 1

**原始简介**: 装修设计技巧大全专用 Skill。覆盖布局与动线、收纳设计、风格与配色、空间设计技巧、免费设计与避坑、设计综合等全流程，倒序整合西安装修课堂会员版知识库精华，帮用户装出更省心、不踩坑的装修设计技巧。

**中文介绍**: 装修设计技巧大全专用 Skill。覆盖布局与动线、收纳设计、风格与配色、空间设计技巧、免费设计与避坑、设计综合等全流程，倒序整合西安装修课堂会员版知识库精华，帮用户装出更省心、不踩坑的装修设计技巧。

Latest changelog:
装修设计技巧大全 Skill 迎来全新升级，内容覆盖更丰富、查找更便捷。

- 覆盖 2013-2026 年全时段内容，共 999 篇精华，全部按发布时间倒序整理，最新内容优先。
- 主题涵盖布局动线、收纳设计、风格配色、空间规划、避坑与免费设计等全流程。
- 明确5大核心原则，强调避坑、实用与人性化建议。
- 每篇参考文件附精确编号与标题，方便用户速查、定位内容。
- 强调先说“别怎么做”再说“该怎么做”，给出直接、干货式建议。
- 所有表述保持“西安装修课堂”风格，拒绝生硬AI语气。

**关键词**: 装修设计技巧大全, 装修设计技巧大全专用, 倒序整合西安装修课堂会员版知识库精华, 帮用户装出更省心、不踩坑的装修设计技巧, 迎来全新升级, Skill, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zhuangxiu-sheji-jiqiao-daquan)

---

## [17. signal-dreaming](https://clawhub.ai/lzyling/signal-dreaming)

**Slug**: `signal-dreaming`  
**Version**: 5.0.0  
**Stats**: ⭐ 0 | ⬇️ 1502 | 🧩 14

**原始简介**: Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

**中文介绍**: Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

Latest changelog:
Makes the index a domain-level summary rather than a mirror of the L2 topic list, and curates on every run rather than only when the index is over budget. Hardens the audit helper against arithmetic-expansion command injection via its numeric overrides, and invokes it through bash so a fresh install without the executable bit still works. Breaking: the first run after upgrading restructures an existing MEMORY.md, so run it manually and supervised the first time.

**关键词**: L2, signal-dreaming, Consolidate, daily, session, logs, topic, files

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/signal-dreaming)

---

## [18. 论衡 — 严肃长文流水线](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.12.27  
**Stats**: ⭐ 1 | ⬇️ 2151 | 🧩 100

**原始简介**: 严肃长文流水线（学术/商业评论/行业分析/公众号深度长文）。三角验证+M门+F失败模式防御+数据信任3档+修订≤2轮。论衡是纯skill，任意 OpenClaw 配置开箱可用：默认多Agent模式（T1∥T2∥T3三方并行检索+三角验证），单主控为可选降级；子代理工具面由宿主 OpenClaw 决定。零exec=不执行shell（19项特权工具禁用；论衡不要求、也不附带任何宿主配置项），但≠零出网：检索（web_search/tavily_search/web_fetch）为默认启用项，经Phase 0「外部服务同意4选1」明示同意后执行，主人可选全部拒绝。默认启用的检索项含学术元数据（Ope

**中文介绍**: 严肃长文流水线（学术/商业评论/行业分析/公众号深度长文）。三角验证+M门+F失败模式防御+数据信任3档+修订≤2轮。论衡是纯skill，任意 OpenClaw 配置开箱可用：默认多Agent模式（T1∥T2∥T3三方并行检索+三角验证），单主控为可选降级；子代理工具面由宿主 OpenClaw 决定。零exec=不执行shell（19项特权工具禁用；论衡不要求、也不附带任何宿主配置项），但≠零出网：检索（web_search/tavily_search/web_fetch）为默认启用项，经Phase 0「外部服务同意4选1」明示同意后执行，主人可选全部拒绝。默认启用的检索项含学术元数据（Ope

Latest changelog:
lunheng-article-pipeline v2.12.27

- 增加 references/_shared/host-hardening-recipe.md 文件，提供子代理权限收紧与主机加固配方建议。
- 显式声明主控/子代理权限收紧可用办法，新增加固文档指针；合规性描述更严格。
- 移除 skill-card.md，精简主 skill 文件结构。
- 扩充 spawn 可靠性边界说明，新增 spawn watchdog（8分钟兜底）及硬卡阈值表更详细说明。
- 补充能力自检/权限声明，明确自检触发与越权阻断规则。

**关键词**: 论衡, 严肃长文流水线, 严肃长文流水线（学术, 商业评论, 行业分析, 公众号深度长文）, 任意, 论衡是纯skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [19. Openclaw Adaptlypost](https://clawhub.ai/tarasshyn/adaptlypost)

**Slug**: `adaptlypost`  
**Version**: 1.1.2  
**Stats**: ⭐ 3 | ⬇️ 3843 | 🧩 14

**原始简介**: Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest and YouTube accounts connected to AdaptlyPost, and read their analytics. Use only when the user has an AdaptlyPost account and asks to draft, schedule or publish a post on those accounts, upload media for such a post, list the connected accounts, check a post's status, or ask about views, likes, comments, followers or top posts on them. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

**中文介绍**: Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest and YouTube accounts connected to AdaptlyPost, and read their analytics. Use only when the user has an AdaptlyPost account and asks to draft, schedule or publish a post on those accounts, upload media for such a post, list the connected accounts, check a post's status, or ask about views, likes, comments, followers or top posts on them. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

Latest changelog:
Approval prompts now show every file, account, setting and caption in full, including per-platform text. A call whose content does not fit OpenClaw's 512-character prompt is refused instead of truncated, and the agent is told to save a draft or split the call. Retry prompts show each platform's saved content. Earlier in 1.1.x: code-enforced approval for uploads, scheduled and live posts and retries; uploads limited to configured mediaDirs with content checks; URL uploads limited to public https hosts; fixed API base URL.

**关键词**: Openclaw, Adaptlypost, Schedule, publish, review, social, posts, through

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/adaptlypost)

---

## [20. quarkclouddrive](https://clawhub.ai/quarkdrive/quarkclouddrive)

**Slug**: `quarkclouddrive`  
**Version**: 1.0.20  
**Stats**: ⭐ 3 | ⬇️ 1500 | 🧩 14

**原始简介**: 夸克网盘官方(Quark Drive)Skill，用于文件上传/下载（支持断点续传）、文件分享与转存、转存分享更新查询、网盘文件搜索、批量重命名与整批撤销、相册整理、AI助手（文件总结与知识问答，支持万级文件）。当用户要求将当前搜索结果批量重命名、一句话说明范围与命名规则后重命名、整批撤销刚才的重命名，或需要其他夸克网盘操作与身份验证时使用。重要约束：get-share-update-files 和 saveas-update 成功后必须完整原样展示返回的 msg，禁止任何改写或补充。

**中文介绍**: 夸克网盘官方(Quark Drive)Skill，用于文件上传/下载（支持断点续传）、文件分享与转存、转存分享更新查询、网盘文件搜索、批量重命名与整批撤销、相册整理、AI助手（文件总结与知识问答，支持万级文件）。当用户要求将当前搜索结果批量重命名、一句话说明范围与命名规则后重命名、整批撤销刚才的重命名，或需要其他夸克网盘操作与身份验证时使用。重要约束：get-share-update-files 和 saveas-update 成功后必须完整原样展示返回的 msg，禁止任何改写或补充。

Latest changelog:
qkclouddrive-skill 1.0.20

**关键词**: 夸克网盘官方, 用于文件上传, 支持万级文件）, 或需要其他夸克网盘操作与身份验证时使用, quarkclouddrive, Quark, Drive, Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/quarkclouddrive)

---

## [21. 多元星途 · PathwayAtlas](https://clawhub.ai/sarry12227/pathway-atlas)

**Slug**: `pathway-atlas`  
**Version**: 0.2.4  
**Stats**: ⭐ 0 | ⬇️ 302 | 🧩 12

**原始简介**: Use when 学生、家长或老师询问“这个分数能上哪个学校”、怎样看位次和冲稳保、有哪些升学路径、强基怎么走、综评怎么走，或需要中国高考选校、选专业、志愿填报及专项、公费师范、军警、港澳和中外合作规划；结合成绩、选科、兴趣和家庭条件，弄清值得准备的选择与下一步行动。

**中文介绍**: Use when 学生、家长或老师询问“这个分数能上哪个学校”、怎样看位次和冲稳保、有哪些升学路径、强基怎么走、综评怎么走，或需要中国高考选校、选专业、志愿填报及专项、公费师范、军警、港澳和中外合作规划；结合成绩、选科、兴趣和家庭条件，弄清值得准备的选择与下一步行动。

Latest changelog:
新增学校及联考划线收集，支持图片或逐轮文字；可比线差与插值先算高考参考分数再查省排，无法读图或缺线时回退喜报；兼容旧问卷和会话。统一全国学校与路径层次：各省分数分别换算，综评纠正上纽与昆杜顺序，同层保留专业适配和备选；港澳同层优先香港，强基先补相邻层次；区分校区及个人实际门槛。

**关键词**: 多元星途, 结合成绩、选科、兴趣和家庭条件, 弄清值得准备的选择与下一步行动, PathwayAtlas, Use, when, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pathway-atlas)

---

## [22. bagua-furnace](https://clawhub.ai/j-levee/bagua-furnace)

**Slug**: `bagua-furnace`  
**Version**: 1.3.0  
**Stats**: ⭐ 0 | ⬇️ 180 | 🧩 3

**原始简介**: 从书、课程、笔记、视频、录音稿、讨论记录，以及客户甩来的网页/PDF/短视频链接等知识密集素材中，自动辨类型→转文本→提炼可复用方法论（成丹为结构化方法卡），用以补充扫地僧等谋士技能，让通用方法论脱离纯学术、更通用。 Use when：用户给了材料或链接并想「提炼方法论」「萃取方法」「做成方法卡」「建立方法论库」，或想把某本书/门课/段视频/段录音变成可迁移的决策框架、思维模型。支持输入类型：纯文本、本地 PDF/图片、网页文章链接、抖音/快手/小红书/视频号短视频分享链接、YouTube/B站/本地音视频（需 ASR 转写）。消费方是扫地僧等谋士层技能——本炉只产顾问级方法论卡，不产可执行 Agent Skill。 Trigger keywords：提炼方法论、萃取方法、做方法卡、建立方法论库、把书变框架、把课变模型、视频转方法论、笔记提炼、讨论记录洞察、链接提炼、八卦炉。

**中文介绍**: 从书、课程、笔记、视频、录音稿、讨论记录，以及客户甩来的网页/PDF/短视频链接等知识密集素材中，自动辨类型→转文本→提炼可复用方法论（成丹为结构化方法卡），用以补充扫地僧等谋士技能，让通用方法论脱离纯学术、更通用。 Use when：用户给了材料或链接并想「提炼方法论」「萃取方法」「做成方法卡」「建立方法论库」，或想把某本书/门课/段视频/段录音变成可迁移的决策框架、思维模型。支持输入类型：纯文本、本地 PDF/图片、网页文章链接、抖音/快手/小红书/视频号短视频分享链接、YouTube/B站/本地音视频（需 ASR 转写）。消费方是扫地僧等谋士层技能——本炉只产顾问级方法论卡，不产可执行 Agent Skill。 Trigger keywords：提炼方法论、萃取方法、做方法卡、建立方法论库、把书变框架、把课变模型、视频转方法论、笔记提炼、讨论记录洞察、链接提炼、八卦炉。

Latest changelog:
示例全面中性化：技能包内不再包含任何输入材料名称与产出卡片示例，仅保留提炼流程与操作规范；工具能力与用法不变。

**关键词**: 从书、课程、笔记、视频、录音稿、讨论记录, 以及客户甩来的网页, 短视频链接等知识密集素材中, 用以补充扫地僧等谋士技能, 让通用方法论脱离纯学术、更通用, bagua-furnace, PDF, Use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bagua-furnace)

---

## [23. 命理占卜 · Chinese Fortune Telling](https://clawhub.ai/haiyangchenbj/chinese-fortune-telling)

**Slug**: `chinese-fortune-telling`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 55 | 🧩 2

**原始简介**: Chinese fortune telling (算命 / 算卦 / 看八字 / 排盘) grounded in classical source texts: a bundled rule engine computes the chart, then the agent interprets it with an explicit school declaration. Computes BaZi Four Pillars (八字 / 四柱) with true-solar-time and 1986–1991 China DST correction via scripts/cantian (buildBaziFromSolar.ts, convertToTrueSolarTime.ts), pattern and useful-god analysis via scripts/engine/bazi-analysis.js, and Zi Wei Dou Shu palaces and four transformations via scripts/engine/ziwei.js. Also covers Liu Yao (六爻 / 起卦), Mei Hua Yi Shu (梅花易数), Qi Men Dun Jia (奇门遁甲), Da Liu Ren (大六壬), Qi Zheng Si Yu (七政四余), classical Western astrology, and date selection (择吉 / 择日 / 黄道吉日). Use whenever the user asks to 算命 / 算卦 / 批八字 / 看生辰八字 / 排盘 / 看命盘, asks about 运势 / 大运 / 流年 (luck cycles), 合婚 / 合盘 (compatibility), 择日 / 挑日子 (picking an auspicious date), wants a 起卦 / 占卜 / 问事 reading on one specific question, or asks whether a third-party fortune-telling app report (测测 / 生辰) is trustworthy. Also use for 术数 classic questions — 子平真诠、滴天髓、穷通宝鉴、三命通会、神峰通考、紫微斗数全书、增删卜易、卜筮正宗、梅花易数、御定奇门宝鉴、六壬大全、协纪辨方书、古典占星、Chinese metaphysics. Not for Tarot, sun-sign horoscopes, numerology, feng-shui layout, or any medical, legal, or investment recommendation. 中文摘要：以《子平真诠》《滴天髓》《穷通宝鉴》《协纪辨方书》等典籍为判据的命理推理引擎，排盘由随包脚本计算（含真太阳时与 1986–1991 夏令时校正），解读须声明流派并标注典籍出处。覆盖八字四柱、紫微斗数、六爻起卦、梅花易数、奇门遁甲、大六壬、七政四余、古典占星、合婚合盘、择日择吉。触发词：算命、算卦、看八字、批八字、生辰八字、排盘、看命盘、运势、流年、大运、合婚、合盘、择日、择吉、起卦、占卜、紫微斗数、六爻、梅花易数、奇门遁甲、子平真诠、滴天髓、穷通宝鉴。不做塔罗、星座运势、生命灵数、风水布局与医疗／法律／投资建议。

**中文介绍**: Chinese fortune telling (算命 / 算卦 / 看八字 / 排盘) grounded in classical source texts: a bundled rule engine computes the chart, then the agent interprets it with an explicit school declaration. Computes BaZi Four Pillars (八字 / 四柱) with true-solar-time and 1986–1991 China DST correction via scripts/cantian (buildBaziFromSolar.ts, convertToTrueSolarTime.ts), pattern and useful-god analysis via scripts/engine/bazi-analysis.js, and Zi Wei Dou Shu palaces and four transformations via scripts/engine/ziwei.js. Also covers Liu Yao (六爻 / 起卦), Mei Hua Yi Shu (梅花易数), Qi Men Dun Jia (奇门遁甲), Da Liu Ren (大六壬), Qi Zheng Si Yu (七政四余), classical Western astrology, and date selection (择吉 / 择日 / 黄道吉日). Use whenever the user asks to 算命 / 算卦 / 批八字 / 看生辰八字 / 排盘 / 看命盘, asks about 运势 / 大运 / 流年 (luck cycles), 合婚 / 合盘 (compatibility), 择日 / 挑日子 (picking an auspicious date), wants a 起卦 / 占卜 / 问事 reading on one specific question, or asks whether a third-party fortune-telling app report (测测 / 生辰) is trustworthy. Also use for 术数 classic questions — 子平真诠、滴天髓、穷通宝鉴、三命通会、神峰通考、紫微斗数全书、增删卜易、卜筮正宗、梅花易数、御定奇门宝鉴、六壬大全、协纪辨方书、古典占星、Chinese metaphysics. Not for Tarot, sun-sign horoscopes, numerology, feng-shui layout, or any medical, legal, or investment recommendation. 中文摘要：以《子平真诠》《滴天髓》《穷通宝鉴》《协纪辨方书》等典籍为判据的命理推理引擎，排盘由随包脚本计算（含真太阳时与 1986–1991 夏令时校正），解读须声明流派并标注典籍出处。覆盖八字四柱、紫微斗数、六爻起卦、梅花易数、奇门遁甲、大六壬、七政四余、古典占星、合婚合盘、择日择吉。触发词：算命、算卦、看八字、批八字、生辰八字、排盘、看命盘、运势、流年、大运、合婚、合盘、择日、择吉、起卦、占卜、紫微斗数、六爻、梅花易数、奇门遁甲、子平真诠、滴天髓、穷通宝鉴。不做塔罗、星座运势、生命灵数、风水布局与医疗／法律／投资建议。

Latest changelog:
Add transparent third-party field policy and reproducible wuxing statistics

**关键词**: 命理占卜, 算命, 算卦, 看八字, 排盘, Chinese, Fortune, Telling

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/chinese-fortune-telling)

---

## [24. FinXData](https://clawhub.ai/qiuqp/finxdata)

**Slug**: `finxdata`  
**Version**: 1.0.16  
**Stats**: ⭐ 0 | ⬇️ 909 | 🧩 11

**原始简介**: 优先免 Key 免费查询金融数据；高级分析用户注册即获免费 API 额度。

**中文介绍**: 优先免 Key 免费查询金融数据；高级分析用户注册即获免费 API 额度。

Latest changelog:
finxdata 1.0.16

- 优化 Skill 说明文档，突出“免 Key API”优先原则：无需注册即可免费查询，优先使用免 Key 免费额度和接口。
- 精简大部分文档内容，删除过于冗长的配置与能力描述，改为分级引导（免 Key > 注册 Key）。
- 明确区分免 Key API（即 agent 接口，适合大部分普通场景）与 API Key 高级接口（深入数据分析和高级用法）。
- 新增更直白的注册说明：注册即送免费额度，按需用高级接口。
- 删除旧 skill-card.md。

**关键词**: 优先免, 免费查询金融数据, 高级分析用户注册即获免费, API, 额度, FinXData, Key, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/finxdata)

---

## [25. FinXData Chinese Stock Data](https://clawhub.ai/finxdata/finxdata-skill)

**Slug**: `finxdata-skill`  
**Version**: 1.0.16  
**Stats**: ⭐ 0 | ⬇️ 490 | 🧩 7

**原始简介**: 优先免 Key 免费查询金融数据；高级分析用户注册即获免费 API 额度。

**中文介绍**: 优先免 Key 免费查询金融数据；高级分析用户注册即获免费 API 额度。

Latest changelog:
finxdata-skill 1.0.16

- 精简和结构化 SKILL.md，优先强调免 Key API，突出无需注册即享免费金融查询服务。
- 明确免 Key 和 Key 接口的使用场景和流程，引导优先体验免 Key 日额度并说明账户额度来源及用途。
- 优化连接配置、调用流程与常见示例，缩减冗余文案，便于上手和集成。
- 移除示例卡片文件 skill-card.md。

**关键词**: 优先免, 免费查询金融数据, 高级分析用户注册即获免费, FinXData, Chinese, Stock, Data, Key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/finxdata-skill)

---

