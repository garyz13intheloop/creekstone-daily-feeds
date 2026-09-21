# ClawHub Skills Daily | 2026-09-21

> 共 25 个 skills

## [1. Zoho Social MCP](https://clawhub.ai/sprintcx/zoho-social-mcp)

**Slug**: `zoho-social-mcp`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Zoho Social via MCP with action catalog, least-privilege profiles, portal/brand/channel helpers, media upload, and verified draft/schedule workflows. Use whenever a task involves Zoho Social: creating, validating, scheduling, or publishing posts, uploading or listing media library assets, or resolving portals, brands, and channels.

**中文介绍**: Zoho Social via MCP with action catalog, least-privilege profiles, portal/brand/channel helpers, media upload, and verified draft/schedule workflows. Use whenever a task involves Zoho Social: creating, validating, scheduling, or publishing posts, uploading or listing media library assets, or resolving portals, brands, and channels.

Latest changelog:
Sharpen skill description so social media tasks reliably trigger the skill

**关键词**: Zoho, Social, MCP, via, action, catalog, least-privilege, profiles

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zoho-social-mcp)

---

## [2. 元呈 yotta-present](https://clawhub.ai/skills?q=yotta-present)

**Slug**: `yotta-present`  
**Version**: 0.6.4  
**Stats**: ⭐ 0 | ⬇️ 385 | 🧩 12

**原始简介**: 元呈 —— AI 输出的默认呈现层：智能体先把输出内容判为「内容类型」，再选「呈现形态」（结论卡/表格/正文/指标板/问答卡/报告/图表…），用 yotta_present CLI 或 present_result MCP 统一渲染成可复制的 Markdown / 纯文本（按需附本地 SVG）。平台自适应（--platform / platform）：webchat 完整 Markdown、discord/whatsapp 表格转列表+标题转加粗、plain 去符号；渲染通道（--channel / channel）：auto 按 platform 映射 plain→r0 去 emoji、其余→r1 emoji 徽章+引用条（r0 保底无色 / r1 增强，r2/r3 高级美化未开放）；命名场景模板（vuln_report/faq/status，references/templates.json 可热更新）一次定义多处复用；codeblock + bold_keys 加粗 + max_len 长度熔断。触发：默认——凡交付给用户的 AI 输出都经元呈（判型 → 选形态 → 渲染）呈现；例外见正文白名单。边界：不做交互式图表编辑器 / BI / 数据分析工具；图表只是呈现形态之一；不做内容改写 / 判断本身。AI 首次使用自动接入 yotta-present MCP（写 mcpServers + 永久记忆护栏，均需用户明确同意），输出默认统一呈现、未加载时降级 CLI。

**中文介绍**: 元呈 —— AI 输出的默认呈现层：智能体先把输出内容判为「内容类型」，再选「呈现形态」（结论卡/表格/正文/指标板/问答卡/报告/图表…），用 yotta_present CLI 或 present_result MCP 统一渲染成可复制的 Markdown / 纯文本（按需附本地 SVG）。平台自适应（--platform / platform）：webchat 完整 Markdown、discord/whatsapp 表格转列表+标题转加粗、plain 去符号；渲染通道（--channel / channel）：auto 按 platform 映射 plain→r0 去 emoji、其余→r1 emoji 徽章+引用条（r0 保底无色 / r1 增强，r2/r3 高级美化未开放）；命名场景模板（vuln_report/faq/status，references/templates.json 可热更新）一次定义多处复用；codeblock + bold_keys 加粗 + max_len 长度熔断。触发：默认——凡交付给用户的 AI 输出都经元呈（判型 → 选形态 → 渲染）呈现；例外见正文白名单。边界：不做交互式图表编辑器 / BI / 数据分析工具；图表只是呈现形态之一；不做内容改写 / 判断本身。AI 首次使用自动接入 yotta-present MCP（写 mcpServers + 永久记忆护栏，均需用户明确同意），输出默认统一呈现、未加载时降级 CLI。

Latest changelog:
yotta-present 0.6.4

- 增加嵌套结构保真：输出的列表嵌套级别与类型完整保留，避免静默拍平或类型丢失。
- 优化内容保真机制，所有块顺序与内容兼容性校验更严格，避免降级误报。
- 丰富判型落地与渲染说明，支持 explain/fallback/fidelity 详细输出渲染选择与内容压缩、丢弃原因。
- 命名场景模板可热更新（如漏洞报告、状态卡），便于多场景输出复用。
- 说明文档细化平台自适应、渲染通道与主题支持，明确各形态取舍与降级规则。

**关键词**: 元呈, ——, 输出的默认呈现层, 智能体先把输出内容判为「内容类型」, 再选「呈现形态」（结论卡, 表格, 正文, yotta-present

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-present)

---

## [3. sentisense](https://clawhub.ai/thesentitrader/sentisense)

**Slug**: `sentisense`  
**Version**: 2.17.0  
**Stats**: ⭐ 1 | ⬇️ 3638 | 🧩 61

**原始简介**: US stock market data API for AI agents: news and social sentiment, the SentiSense Score, the SentiSense Rating daily A to F letter grade, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices. One free API key covers every endpoint. Use for stock sentiment API, stock market API, stock rating API, stock letter grade, insider trading data, congress stock trades, 13F holdings, options flow, earnings calendar, stock price API, market data for AI agents. Read-only. No trading, no purchases, no write operations, no wallet access.

**中文介绍**: US stock market data API for AI agents: news and social sentiment, the SentiSense Score, the SentiSense Rating daily A to F letter grade, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices. One free API key covers every endpoint. Use for stock sentiment API, stock market API, stock rating API, stock letter grade, insider trading data, congress stock trades, 13F holdings, options flow, earnings calendar, stock price API, market data for AI agents. Read-only. No trading, no purchases, no write operations, no wallet access.

Latest changelog:
Fundamentals rows can carry an epsBasisRepair marker: for a short list of named issuers whose provider restated share counts for a split but left older EPS on the pre-split basis, the EPS is restated and the row names the fields, multiplier and split dates; null means no repair was applied. Chart bars now carry adjusted: true, with the price basis per range spelled out.

**关键词**: US, API, Agent, sentisense, stock, market, data, news

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sentisense)

---

## [4. 詹明明](https://clawhub.ai/iamzifei/zmm)

**Slug**: `zmm`  
**Version**: 0.2.11  
**Stats**: ⭐ 0 | ⬇️ 505 | 🧩 14

**原始简介**: 📐 詹明明 ——两套技能的总入口：做内容（选题/写稿/审核/复盘）+ 看生意（组合体检/营收归因/客户集中度/依赖风险/拿不准的决策）。三种模式：新手上路演示、任务前路由、任务后导航。不知道用哪个就回这里。 触发方式：/zmm、/新手上路、/zmm 教程、「做条视频」「出个口播」「今天拍什么」「内容下一步怎么走」；新手教程：/zmm 新手指南、/zmm 新手、「这个怎么用」「第一次用，带我走一遍」「不知道能干嘛」 Single entry point for both skill sets — content (topic, script, review, retro) and business (portfolio, revenue, concentration, dependency, decisions). Three modes: guided onboarding demo, pre-task routing, post-task navigation. Trigger: /zmm, "make a short video", "what should I shoot today", "how do I use this" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明 ——两套技能的总入口：做内容（选题/写稿/审核/复盘）+ 看生意（组合体检/营收归因/客户集中度/依赖风险/拿不准的决策）。三种模式：新手上路演示、任务前路由、任务后导航。不知道用哪个就回这里。 触发方式：/zmm、/新手上路、/zmm 教程、「做条视频」「出个口播」「今天拍什么」「内容下一步怎么走」；新手教程：/zmm 新手指南、/zmm 新手、「这个怎么用」「第一次用，带我走一遍」「不知道能干嘛」 Single entry point for both skill sets — content (topic, script, review, retro) and business (portfolio, revenue, concentration, dependency, decisions). Three modes: guided onboarding demo, pre-task routing, post-task navigation. Trigger: /zmm, "make a short video", "what should I shoot today", "how do I use this" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: add zmm-trend, the 24th skill

For when a big shift is under way and you want to know what to bet on.
Curves you can measure (looked up, dated), a precedent industry with a
mandatory "where it differs" column, bets and non-bets, and a dated
signal on every call. End-state predictions are stated one level less
confidently by default.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

**关键词**: 詹明明, ——两套技能的总入口, 做内容（选题, 写稿, 审核, 复盘）+, 看生意（组合体检, 营收归因

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm)

---

## [5. 詹明明·风口在哪](https://clawhub.ai/iamzifei/zmm-trend)

**Slug**: `zmm-trend`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 一个大变化正在发生（AI 来了、平台换了、行业在洗牌），想知道它到底会走到哪、自己该押什么的时候用。不给「风口清单」，也不陪你预言未来 —— 带你做八个动作：从一场已经发生的颠覆倒推机制 → 把趋势拆成几条能量的曲线 → 看拆完之后还剩哪一两项没解决 → 找一个已经走完的老产业当剧本 → 先让自己活在未来里一段时间 → 落成「赌什么、不赌什么」→ 分开「趋势对不对」和「你能不能赢」→ 每个判断挂一条到期会自己回来检验的信号。 触发方式：/zmm-trend、/风口在哪、/看大势、「AI 来了我该押什么」「这是不是风口」「我这行会被 AI 怎么改」「下一个机会在哪」「现在入场晚不晚」「这波趋势能持续多久」 For when a big shift is under way and you want to know where it lands and what to bet on. No list of hot sectors and no fortune-telling: work back from a disruption that already happened, break the trend into curves you can measure, find what is still unsolved, borrow an industry that already ran the same script, live in the future for a while, turn the view into bets and non-bets, separate "is the trend right" from "can I win", and attach a dated signal to every call. Trigger: /zmm-trend, "AI is here, what should I bet on", "is this a real wave", "how will AI change my industry", "am I too late"

**中文介绍**: 一个大变化正在发生（AI 来了、平台换了、行业在洗牌），想知道它到底会走到哪、自己该押什么的时候用。不给「风口清单」，也不陪你预言未来 —— 带你做八个动作：从一场已经发生的颠覆倒推机制 → 把趋势拆成几条能量的曲线 → 看拆完之后还剩哪一两项没解决 → 找一个已经走完的老产业当剧本 → 先让自己活在未来里一段时间 → 落成「赌什么、不赌什么」→ 分开「趋势对不对」和「你能不能赢」→ 每个判断挂一条到期会自己回来检验的信号。 触发方式：/zmm-trend、/风口在哪、/看大势、「AI 来了我该押什么」「这是不是风口」「我这行会被 AI 怎么改」「下一个机会在哪」「现在入场晚不晚」「这波趋势能持续多久」 For when a big shift is under way and you want to know where it lands and what to bet on. No list of hot sectors and no fortune-telling: work back from a disruption that already happened, break the trend into curves you can measure, find what is still unsolved, borrow an industry that already ran the same script, live in the future for a while, turn the view into bets and non-bets, separate "is the trend right" from "can I win", and attach a dated signal to every call. Trigger: /zmm-trend, "AI is here, what should I bet on", "is this a real wave", "how will AI change my industry", "am I too late"

Latest changelog:
sync: add zmm-trend, the 24th skill

For when a big shift is under way and you want to know what to bet on.
Curves you can measure (looked up, dated), a precedent industry with a
mandatory "where it differs" column, bets and non-bets, and a dated
signal on every call. End-state predictions are stated one level less
confidently by default.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

**关键词**: 詹明明·风口在哪, 一个大变化正在发生（AI, 来了、平台换了、行业在洗牌）, 想知道它到底会走到哪、自己该押什么的时候用, 不给「风口清单」, 也不陪你预言未来, ——, 带你做八个动作

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-trend)

---

## [6. Dongwo（懂我）](https://clawhub.ai/cutd/dongwo)

**Slug**: `dongwo`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 178 | 🧩 6

**原始简介**: Set up, inspect, or maintain a local user-preference memory shared across coding agents such as Codex and Claude Code. Use only when the user explicitly asks to remember a preference, review or forget stored preferences, configure Dongwo lifecycle hooks, or maintain an existing Dongwo installation.

**中文介绍**: Set up, inspect, or maintain a local user-preference memory shared across coding agents such as Codex and Claude Code. Use only when the user explicitly asks to remember a preference, review or forget stored preferences, configure Dongwo lifecycle hooks, or maintain an existing Dongwo installation.

Latest changelog:
Authenticate Inbox evidence with project-external trust state; auto-sign new hook events; require explicit digest migration for legacy events; preserve existing preference-memory behavior.

**关键词**: up, or, Dongwo（懂我）, Set, inspect, maintain, local, user-preference

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dongwo)

---

## [7. Skill Network Audit: where skills send data](https://clawhub.ai/aeneassoft/skill-network-audit)

**Slug**: `skill-network-audit`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 74 | 🧩 3

**原始简介**: Where does this skill send data? What hosts did it contact? Find out where an installed skill sends data: list every network host a skill or tool contacted at runtime, with counts, uploads, credential reads and flagged or unexpected hosts, from the ClawPhylax ledger. Audit outbound connections per skill, explain why the agent contacted an unknown host, detect data exfiltration after install, and share a witness card of a skill's real behavior. Use when asked what a skill is doing on the network, why something contacted a host, or when a reply footer mentions ClawPhylax.

**中文介绍**: Where does this skill send data? What hosts did it contact? Find out where an installed skill sends data: list every network host a skill or tool contacted at runtime, with counts, uploads, credential reads and flagged or unexpected hosts, from the ClawPhylax ledger. Audit outbound connections per skill, explain why the agent contacted an unknown host, detect data exfiltration after install, and share a witness card of a skill's real behavior. Use when asked what a skill is doing on the network, why something contacted a host, or when a reply footer mentions ClawPhylax.

Latest changelog:
Adds the For agents section linking the skill set.

**关键词**: Skill, Network, Audit, where, skills, send, data, does

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-network-audit)

---

## [8. Verify Skill Safety Before Install](https://clawhub.ai/aeneassoft/clawphylax-verify)

**Slug**: `clawphylax-verify`  
**Version**: 1.1.2  
**Stats**: ⭐ 0 | ⬇️ 85 | 🧩 5

**原始简介**: Is this skill safe? Verify a third-party skill is safe before installing it: scan the skill folder for every network host its SKILL.md and scripts contact, whether they upload data, and whether they read credential files (~/.ssh, .env, ~/.aws). Returns clean, review or suspicious with file and line. Use before installing any untrusted ClawHub skill, when asked whether a skill is safe, or to check a skill for exfiltration or malware patterns.

**中文介绍**: Is this skill safe? Verify a third-party skill is safe before installing it: scan the skill folder for every network host its SKILL.md and scripts contact, whether they upload data, and whether they read credential files (~/.ssh, .env, ~/.aws). Returns clean, review or suspicious with file and line. Use before installing any untrusted ClawHub skill, when asked whether a skill is safe, or to check a skill for exfiltration or malware patterns.

Latest changelog:
Adds the For agents section linking the skill set.

**关键词**: Verify, Skill, Safety, Before, Install, safe?, third-party, safe

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawphylax-verify)

---

## [9. Why did my request fail? Should I retry?](https://clawhub.ai/aeneassoft/why-did-my-request-fail)

**Slug**: `why-did-my-request-fail`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Why did my request fail? Is this site blocking agents? Should I retry, wait, or switch tools? Diagnose a failing web_fetch, API call or exec network command from this machine's observed requests: whether the host is refusing you (401/403 block), rate-limiting you (429), down (5xx), unreachable (timeouts), or whether the request itself is wrong — with success probability, confidence bounds, seconds to back off, and which tool succeeds on this host. Use before retrying any failed request, when a site returns errors repeatedly, or when deciding whether to give up.

**中文介绍**: Why did my request fail? Is this site blocking agents? Should I retry, wait, or switch tools? Diagnose a failing web_fetch, API call or exec network command from this machine's observed requests: whether the host is refusing you (401/403 block), rate-limiting you (429), down (5xx), unreachable (timeouts), or whether the request itself is wrong — with success probability, confidence bounds, seconds to back off, and which tool succeeds on this host. Use before retrying any failed request, when a site returns errors repeatedly, or when deciding whether to give up.

Latest changelog:
Initial release: diagnosis of a failing host from observed requests.

**关键词**: my, Why, did, request, fail?, Should, retry?, site

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/why-did-my-request-fail)

---

## [10. Drop Files](https://clawhub.ai/icexun/drop-files-skill)

**Slug**: `drop-files-skill`  
**Version**: 0.1.2  
**Stats**: ⭐ 1 | ⬇️ 477 | 🧩 3

**原始简介**: Upload generated HTML/Markdown files to DropFiles and get a shareable public link. Invoke when the user wants to share, publish, or generate a public link for any HTML or Markdown content they produced.

**中文介绍**: Upload generated HTML/Markdown files to DropFiles and get a shareable public link. Invoke when the user wants to share, publish, or generate a public link for any HTML or Markdown content they produced.

Latest changelog:
- Added a Python wrapper script (`scripts/upload.py`) for uploading files, handling all curl invocation, JSON, and temp-file management.
- Updated documentation to require use of the wrapper script instead of manual curl commands or JSON payloads.
- Removed `skill-card.md` file.
- Clarified and streamlined usage instructions and workflow in the docs.

**关键词**: Drop, Files, Upload, generated, HTML, Markdown, DropFiles, get

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/drop-files-skill)

---

## [11. Iran Chemical Database](https://clawhub.ai/orionshaowswmw/iran-chem-database)

**Slug**: `iran-chem-database`  
**Version**: 2.36.1  
**Stats**: ⭐ 0 | ⬇️ 1666 | 🧩 69

**原始简介**: Iran Chemical Database — live, dated, auditable, BEST-EFFORT index of chemical offerings in configured public Iranian supplier catalogues (websites + public Telegram channels). HTTrack/WooCommerce-REST/Telegram mirroring → local-only parsing → RDKit/PubChem/CAS-validated PostgreSQL with FastAPI + Streamlit. Fail-closed Iranian-suppliers-only country gate; coverage measured and published, never claimed complete. Installation = software + queued crawl, not a populated dataset. Ships a 1399-molecule CID-unique confirmed-organic seed baseline (v2.22, 2026-08-27: v2.19 primary + live Telegram/WooCommerce/sitemap crawl + 5-model fleet normalization, every new identity PubChem-confirmed). For academic procurement research.

**中文介绍**: Iran Chemical Database — live, dated, auditable, BEST-EFFORT index of chemical offerings in configured public Iranian supplier catalogues (websites + public Telegram channels). HTTrack/WooCommerce-REST/Telegram mirroring → local-only parsing → RDKit/PubChem/CAS-validated PostgreSQL with FastAPI + Streamlit. Fail-closed Iranian-suppliers-only country gate; coverage measured and published, never claimed complete. Installation = software + queued crawl, not a populated dataset. Ships a 1399-molecule CID-unique confirmed-organic seed baseline (v2.22, 2026-08-27: v2.19 primary + live Telegram/WooCommerce/sitemap crawl + 5-model fleet normalization, every new identity PubChem-confirmed). For academic procurement research.

Latest changelog:
v2.36.1: Zero-timer token bucket pacing, active concurrency throttling, Retry-After header synchronization, and AI agent navigation masterclass

**关键词**: Iran, Chemical, Database, live, dated, auditable, BEST-EFFORT, index

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iran-chem-database)

---

## [12. MemHub](https://clawhub.ai/cutd/memhub)

**Slug**: `memhub`  
**Version**: 0.4.7  
**Stats**: ⭐ 0 | ⬇️ 1050 | 🧩 14

**原始简介**: 使用 MemHub Protocol v0.1 管理用户明确指定的跨 Agent 记忆仓库。用于用户明确要求记住、检索、遗忘、导出上下文或配置 Git 同步时；读取可直接执行，持久写入、自动同步、OAuth、remote 修改和仓库创建必须来自当前用户的明确请求。

**中文介绍**: 使用 MemHub Protocol v0.1 管理用户明确指定的跨 Agent 记忆仓库。用于用户明确要求记住、检索、遗忘、导出上下文或配置 Git 同步时；读取可直接执行，持久写入、自动同步、OAuth、remote 修改和仓库创建必须来自当前用户的明确请求。

Latest changelog:
Security hardening: stage only MemHub-managed paths; remove historically tracked secrets, caches, indexes, databases and env files from Git while preserving local copies; pass Git authorization through child-process environment rather than argv. Includes the 0.4.5-0.4.6 path, host, URL-token and explicit-env protections.

**关键词**: 使用, v0.1, 管理用户明确指定的跨, Agent, 记忆仓库, MemHub, Protocol, Git

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memhub)

---

## [13. claw-superpowers](https://clawhub.ai/cutd/claw-superpowers)

**Slug**: `claw-superpowers`  
**Version**: 1.0.3  
**Stats**: ⭐ 1 | ⬇️ 1847 | 🧩 4

**原始简介**: Agentic software development methodology — 13 integrated skills for disciplined AI-assisted development covering brainstorming, planning, TDD, debugging, code review, git worktrees, and branch management. Use the smallest relevant section for substantial software work; skip heavyweight workflow steps for routine questions or when the user has already chosen a process.

**中文介绍**: Agentic software development methodology — 13 integrated skills for disciplined AI-assisted development covering brainstorming, planning, TDD, debugging, code review, git worktrees, and branch management. Use the smallest relevant section for substantial software work; skip heavyweight workflow steps for routine questions or when the user has already chosen a process.

Latest changelog:
Final safety alignment: preserve all 13 methods while requiring current user authorization for commits, pushes, merges, branch deletion, worktrees, dependency installation, and repository-controlled build/test execution.

**关键词**: claw-superpowers, Agentic, software, development, methodology, integrated, skills, disciplined

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/claw-superpowers)

---

## [14. peen](https://clawhub.ai/psyb0t/peen)

**Slug**: `peen`  
**Version**: 0.10.1  
**Stats**: ⭐ 0 | ⬇️ 162 | 🧩 3

**原始简介**: Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

**中文介绍**: Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

Latest changelog:
- Updated session handling to require explicit opening of workspaces via `POST /v1/sessions/open` instead of generating arbitrary session IDs.
- Documented new REST endpoints: open sessions and list sessions.
- Clarified that the default workspace root is `/workspace`, with `PEEN_WORKSPACE_ROOTS` allowing multiple roots.
- Updated security note: sessions are not sandboxed by default—actual execution profile determines isolation.
- Removed the obsolete skill-card.md file.

**关键词**: peen, Configure, operate, durable, coding-agent, backend, Use, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/peen)

---

## [15. MeowClaw PPT Smith](https://clawhub.ai/skillmelody/article-html-to-ppt)

**Slug**: `article-html-to-ppt`  
**Version**: 5.1.0  
**Stats**: ⭐ 0 | ⬇️ 2312 | 🧩 30

**原始简介**: Create editable PPTX from documents, reconstruct supplied slide design images, or preserve native PPTX templates. Design with structured native objects and real previews; image-generation tools are optional. Use for source-based presentations, design-to-PPT reconstruction, template reuse, and revisions to PPT Smith tasks.

**中文介绍**: Create editable PPTX from documents, reconstruct supplied slide design images, or preserve native PPTX templates. Design with structured native objects and real previews; image-generation tools are optional. Use for source-based presentations, design-to-PPT reconstruction, template reuse, and revisions to PPT Smith tasks.

Latest changelog:
v5.1.0：简化 create/recreate/template 三种使用场景；支持无生图工具的原生设计与真实预览；新增紧凑输入、字体预检、对象补丁和版本绑定审核继承。保留 v5.0 的 20 页案例（447 个原生对象及 1 张可替换图片）和 v5.1 的 6 页案例（120 个原生对象）。公开包排除开发测试、日志和临时产物。

**关键词**: MeowClaw, PPT, Smith, editable, PPTX, documents, reconstruct, supplied

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/article-html-to-ppt)

---

## [16. Investor Search for PicoClaw](https://clawhub.ai/chainleo/investor-search-picoclaw)

**Slug**: `investor-search-picoclaw`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 112 | 🧩 3

**原始简介**: For PicoClaw. Install: picoclaw skills install --registry clawhub investor-search-picoclaw. Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

**中文介绍**: For PicoClaw. Install: picoclaw skills install --registry clawhub investor-search-picoclaw. Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

Latest changelog:
Stop rule can no longer be faked. A round that found nothing new only counts towards stopping if it lists at least 3 new result URLs the search returned, each with a note saying what the page is and why it is not a new investor. A site: search whose results are not on that site counts as open web, not as the surface it claims. Rounds without proof are kept but do not count.

**关键词**: Investor, Search, PicoClaw, Install, skills, registry, clawhub, investor-search-picoclaw

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/investor-search-picoclaw)

---

## [17. investor-search](https://clawhub.ai/chainleo/investor-search)

**Slug**: `investor-search`  
**Version**: 1.2.2  
**Stats**: ⭐ 0 | ⬇️ 237 | 🧩 5

**原始简介**: Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

**中文介绍**: Name a country, get its verifiable investors: family offices, VCs, angels. Rejects advisers and lawyers. Every field is sourced, gaps stay empty. Nothing guessed. Stops on evidence.

Latest changelog:
Stop rule can no longer be faked. A round that found nothing new only counts towards stopping if it lists at least 3 new result URLs the search returned, each with a note saying what the page is and why it is not a new investor. A site: search whose results are not on that site counts as open web, not as the surface it claims. Rounds without proof are kept but do not count.

**关键词**: investor-search, Name, country, get, its, verifiable, investors, family

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/investor-search)

---

## [18. 詹明明·从哪儿下手](https://clawhub.ai/iamzifei/zmm-path)

**Slug**: `zmm-path`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 只有一个大目标、不知道从哪下手的时候用。「我想赚一百万」「我想涨到一万粉」「今年营收要加三成」——这些都不是目标，是愿望。本技能把愿望变成一条今天就能走第一步的路径：写成可判定的目标 → 拆成能分别量、分别动的因子 → 只挑一个瓶颈（挑完要你亲口确认）→ 出候选路径和代价 → 落到一条 if-then 的第一步 → 预先写好「什么时候认它不成立」。最后告诉你这条路上哪几段能交给 AI、哪几段必须你自己去现实里取数，并给一段你以后能反复用的提问模板。 触发方式：/zmm-path、/从哪下手、/拆目标、/怎么达成、「我想赚一百万」「我想涨到一万粉」「营收要加三成」「目标定了但不知道从哪开始」「帮我把这个目标拆一下」「这个问题该怎么解决」「有没有什么办法」 Turns a vague wish into a path you can start today: make the goal decidable, break it into factors you can measure and move separately, lock one bottleneck with an explicit confirmation, cost out two or three routes, land on one if-then first step, and write the kill criterion in advance. Ends by marking which stretches an AI can run and which need real-world feedback you have to fetch yourself. Trigger: /zmm-path, "I want to make a million", "I want 10k followers", "where do I even start", "break this goal down for me"

**中文介绍**: 只有一个大目标、不知道从哪下手的时候用。「我想赚一百万」「我想涨到一万粉」「今年营收要加三成」——这些都不是目标，是愿望。本技能把愿望变成一条今天就能走第一步的路径：写成可判定的目标 → 拆成能分别量、分别动的因子 → 只挑一个瓶颈（挑完要你亲口确认）→ 出候选路径和代价 → 落到一条 if-then 的第一步 → 预先写好「什么时候认它不成立」。最后告诉你这条路上哪几段能交给 AI、哪几段必须你自己去现实里取数，并给一段你以后能反复用的提问模板。 触发方式：/zmm-path、/从哪下手、/拆目标、/怎么达成、「我想赚一百万」「我想涨到一万粉」「营收要加三成」「目标定了但不知道从哪开始」「帮我把这个目标拆一下」「这个问题该怎么解决」「有没有什么办法」 Turns a vague wish into a path you can start today: make the goal decidable, break it into factors you can measure and move separately, lock one bottleneck with an explicit confirmation, cost out two or three routes, land on one if-then first step, and write the kill criterion in advance. Ends by marking which stretches an AI can run and which need real-world feedback you have to fetch yourself. Trigger: /zmm-path, "I want to make a million", "I want 10k followers", "where do I even start", "break this goal down for me"

Latest changelog:
sync: add zmm-path, the 23rd skill

Turns a wish with no path into a first step you can take today:
decidable goal → factors you can measure separately → one bottleneck
(confirmed out loud) → routes with costs → if-then first step with a
kill criterion written in advance.

Ships with three references: theory mapped per gate with boundaries and
source-strength markers, a library of mechanism equations (including the
Xiaohongshu click-through variant), and the 29 problem-solving questions
with skip conditions.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

**关键词**: 詹明明·从哪儿下手, 只有一个大目标、不知道从哪下手的时候用, 是愿望, 本技能把愿望变成一条今天就能走第一步的路径, 写成可判定的目标, 拆成能分别量、分别动的因子, 只挑一个瓶颈（挑完要你亲口确认）→, 出候选路径和代价

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-path)

---

## [19. Mystilink Horoscope](https://clawhub.ai/mystilink-ai/mystilink-horoscope-skill)

**Slug**: `mystilink-horoscope-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Western natal astrology charting and reading for Mystilink. Computes planets, houses, and aspects from birth time and place, then interprets with Wiki terms. Use when the user asks about natal chart, horoscope, houses, aspects, or 占星.

**中文介绍**: Western natal astrology charting and reading for Mystilink. Computes planets, houses, and aspects from birth time and place, then interprets with Wiki terms. Use when the user asks about natal chart, horoscope, houses, aspects, or 占星.

Latest changelog:
Mystilink Horoscope Skill 0.1.0 – Initial Release

- Provides Western natal astrology charting and interpretations with Wiki-based descriptions.
- Computes planets, houses, and aspects using birth time and location.
- Returns both calculated chart data and clear, distinct interpretations.
- Supports English (default) and simplified Chinese locales.
- Integrates with Mystilink's astro calculator, requiring Python 3 and pyswisseph.

**关键词**: Mystilink, Horoscope, Western, natal, astrology, charting, reading, Computes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-horoscope-skill)

---

## [20. Mystilink Bazi](https://clawhub.ai/mystilink-ai/mystilink-bazi-skill)

**Slug**: `mystilink-bazi-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: BaZi (Four Pillars) charting and reading for Mystilink. Computes pillars, luck cycles, and annual pillars from birth data, then interprets with Wiki theory (ten gods, day master, combinations). Use when the user asks about BaZi, Four Pillars, 八字, day master, ten gods, dayun, or liunian.

**中文介绍**: BaZi (Four Pillars) charting and reading for Mystilink. Computes pillars, luck cycles, and annual pillars from birth data, then interprets with Wiki theory (ten gods, day master, combinations). Use when the user asks about BaZi, Four Pillars, 八字, day master, ten gods, dayun, or liunian.

Latest changelog:
Mystilink BaZi skill initial release:

- Computes and interprets BaZi (Four Pillars) charts from birth data.
- Provides chart details including four pillars, day master, ten gods, and luck cycles.
- Integrates with Mystilink Wiki API for BaZi theory and interpretation.
- Separates chart calculation from interpretation, citing Wiki sources for knowledge.
- Supports English output with fallback to Chinese if necessary.
- Offers CLI scripts for chart and cycle calculation, mirroring Mystilink product logic.

**关键词**: Mystilink, Bazi, Four, Pillars, charting, reading, Computes, luck

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-bazi-skill)

---

## [21. Mystilink Ziwei](https://clawhub.ai/mystilink-ai/mystilink-ziwei-skill)

**Slug**: `mystilink-ziwei-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Zi Wei Dou Shu charting and reading for Mystilink. Builds a twelve-palace chart with major stars and optional Si Hua, then interprets with Wiki theory. Use when the user asks about Zi Wei, 紫微, twelve palaces, or Si Hua.

**中文介绍**: Zi Wei Dou Shu charting and reading for Mystilink. Builds a twelve-palace chart with major stars and optional Si Hua, then interprets with Wiki theory. Use when the user asks about Zi Wei, 紫微, twelve palaces, or Si Hua.

Latest changelog:
Initial release of Mystilink Zi Wei Dou Shu charting and reading skill.

- Generates twelve-palace Zi Wei Dou Shu (紫微斗数) charts with major stars and optional Si Hua.
- Interprets charts using Wiki-based theory for clear, referenced readings.
- Requires user’s birth datetime, gender, and timezone; supports local and IANA formats.
- Default response language is English, with Wiki-language fallback to Simplified Chinese.
- Designed for Zi Wei Dou Shu queries; not intended for BaZi, tarot, or unrelated systems.

**关键词**: Zi, Mystilink, Ziwei, Wei, Dou, Shu, charting, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-ziwei-skill)

---

## [22. Mystilink Liuyao](https://clawhub.ai/mystilink-ai/mystilink-liuyao-skill)

**Slug**: `mystilink-liuyao-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Liu Yao (six-line) casting and reading for Mystilink. Forms hexagrams from six casts, then interprets with Wiki method pages and Zhouyi chapters. Use when the user asks about Liu Yao, 六爻, moving lines, or hexagram casting.

**中文介绍**: Liu Yao (six-line) casting and reading for Mystilink. Forms hexagrams from six casts, then interprets with Wiki method pages and Zhouyi chapters. Use when the user asks about Liu Yao, 六爻, moving lines, or hexagram casting.

Latest changelog:
- Initial release of mystilink-liuyao skill: Liu Yao (six-line) casting and reading for Mystilink.
- Combines both casting (hexagram formation) and interpreter for hexagram readings.
- Uses Wiki method pages and Zhouyi (Yijing) chapters for interpretation, with references to relevant classics.
- Scripted workflow ensures one matter per cast and refuses multi-topic questions.
- Compatible with node >= 18; recommends network access for wiki/classic references.
- Defaults to English locale, with classics fallback to Simplified Chinese if needed.

**关键词**: Mystilink, Liuyao, Liu, Yao, six-line, casting, reading, Forms

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-liuyao-skill)

---

## [23. Mystilink Tarot](https://clawhub.ai/mystilink-ai/mystilink-tarot-skill)

**Slug**: `mystilink-tarot-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Tarot draw and reading for Mystilink. Draws upright/reversed cards for a spread, then interprets with Wiki card pages. Use when the user asks about tarot, tarot spreads, major/minor arcana, or 塔罗.

**中文介绍**: Tarot draw and reading for Mystilink. Draws upright/reversed cards for a spread, then interprets with Wiki card pages. Use when the user asks about tarot, tarot spreads, major/minor arcana, or 塔罗.

Latest changelog:
- Initial release of mystilink-tarot skill for tarot draws and readings.
- Supports upright/reversed card draws and interpretation using Wiki card pages.
- Default spread is three-card; clarifies question and spread before drawing.
- Includes workflow for random card draw and card reading with API integration.
- Designed for tarot questions, spreads, and card meanings in English locale by default.

**关键词**: Mystilink, Tarot, draw, reading, Draws, upright, reversed, cards

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-tarot-skill)

---

## [24. Mystilink Router](https://clawhub.ai/mystilink-ai/mystilink-router-skill)

**Slug**: `mystilink-router-skill`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Chooses which Mystilink metaphysics skill to use (BaZi, Zi Wei, tarot, Liu Yao, western horoscope). Use when the user has not named a system, asks which method fits, or mixes several traditions in one request.

**中文介绍**: Chooses which Mystilink metaphysics skill to use (BaZi, Zi Wei, tarot, Liu Yao, western horoscope). Use when the user has not named a system, asks which method fits, or mixes several traditions in one request.

Latest changelog:
- Initial release of mystilink-router.
- Routes user requests to the appropriate Mystilink metaphysics skill (BaZi, Zi Wei, tarot, Liu Yao, western horoscope) based on context.
- Provides clear heuristics for selecting a system when the user's intent is ambiguous or mixes traditions.
- Calls on relevant wiki information to assist with method selection.
- Ensures only one primary system is chosen per request for accuracy and clarity.

**关键词**: Mystilink, Router, Chooses, which, metaphysics, skill, use, BaZi

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mystilink-router-skill)

---

## [25. pitstop](https://clawhub.ai/galjos/pitstop)

**Slug**: `pitstop`  
**Version**: 1.2.2  
**Stats**: ⭐ 0 | ⬇️ 828 | 🧩 9

**原始简介**: Italian fuel-station prices (petrol, diesel, GPL, methane, HVO) and EV charging stations. Find cheapest by municipality / province / brand / coordinate, look up EV chargers near a place, get macro price stats. Backed by MIMIT Osservaprezzi Carburanti, OpenStreetMap (Overpass), and ISTAT comune coordinates. Use for "cheapest diesel near X in Italy", "fuel stations in <comune>", or "EV chargers near <comune>".

**中文介绍**: Italian fuel-station prices (petrol, diesel, GPL, methane, HVO) and EV charging stations. Find cheapest by municipality / province / brand / coordinate, look up EV chargers near a place, get macro price stats. Backed by MIMIT Osservaprezzi Carburanti, OpenStreetMap (Overpass), and ISTAT comune coordinates. Use for "cheapest diesel near X in Italy", "fuel stations in <comune>", or "EV chargers near <comune>".

Latest changelog:
Complete flag lists, CLI to MCP name map, multi-fuel cheapest rule.

**关键词**: pitstop, Italian, fuel-station, prices, petrol, diesel, GPL, methane

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pitstop)

---

