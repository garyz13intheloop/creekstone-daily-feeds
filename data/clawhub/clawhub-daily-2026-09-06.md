# ClawHub Skills Daily | 2026-09-06

> 共 25 个 skills

## [1. Coingecko](https://clawhub.ai/bronoman/coingecko-2)

**Slug**: `coingecko-2`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Live Bitcoin & crypto price data via CoinGecko API. Fetch BTC/USD, ETH/USD, multi-asset quotes. Supports both Demo (free) and Pro API keys. No credentials in prompts—only .env isolation.

**中文介绍**: Live Bitcoin & crypto price data via CoinGecko API. Fetch BTC/USD, ETH/USD, multi-asset quotes. Supports both Demo (free) and Pro API keys. No credentials in prompts—only .env isolation.

Latest changelog:
Initial release: Live crypto price data for Hermes using CoinGecko API, with secure key handling and automatic fallback to Kraken.

- Fetch live BTC/USD, ETH/USD, and multi-asset crypto quotes
- Supports both free Demo and paid Pro CoinGecko API keys; keys secured in environment variables
- Automatic fallback to Kraken API if CoinGecko unavailable or rate-limited
- Includes scripts for price fetch, multi-asset query, and health check
- Market cap, 24h change, and volume data supported
- No API credentials appear in prompts, logs, or chat; designed for privacy and security

**关键词**: API, Coingecko, Live, Bitcoin, crypto, price, data, via

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/coingecko-2)

---

## [2. Museum Explorer](https://clawhub.ai/bonniegeng-max/museum-explorer)

**Slug**: `museum-explorer`  
**Version**: 1.6.2  
**Stats**: ⭐ 0 | ⬇️ 436 | 🧩 12

**原始简介**: 博物馆/美术馆看展全链路助手：行前生成策展卡、行中引导观展与展品讲解、行后沉淀电子手帐并产出展品打卡印章，支持同步馆方展览索引、查询近期展览、积累本地展品库。当用户提到看展、观展、策展，或想了解博物馆/美术馆正在展什么、做行前攻略、现场打卡、做手帐、集印章、约朋友分享看展时使用。信息核验标注来源与日期，禁止臆造数据。

**中文介绍**: 博物馆/美术馆看展全链路助手：行前生成策展卡、行中引导观展与展品讲解、行后沉淀电子手帐并产出展品打卡印章，支持同步馆方展览索引、查询近期展览、积累本地展品库。当用户提到看展、观展、策展，或想了解博物馆/美术馆正在展什么、做行前攻略、现场打卡、做手帐、集印章、约朋友分享看展时使用。信息核验标注来源与日期，禁止臆造数据。

Latest changelog:
扫描收尾（SDI-4+T09）：sxhm 数据溯源元数据如实化（混合源：44 临展+2 常设，按 url/status 区分）；examples 吴哥手帐副本同步 esc() 引号转义与数值钳制

**关键词**: 博物馆, 美术馆看展全链路助手, 当用户提到看展、观展、策展, 或想了解博物馆, 信息核验标注来源与日期, 禁止臆造数据, Museum, Explorer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/museum-explorer)

---

## [3. outlook-calendar](https://clawhub.ai/skills?q=outlook-calendar)

**Slug**: `outlook-calendar`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 10 | 🧩 3

**原始简介**: Read and write the signed-in user's Microsoft 365 / Outlook.com personal calendar via Microsoft Graph. Calendar-only. No mail, no files, no contacts, no directory access. Use when the user wants to list today's events, look at next week, create / update / delete a single event by id, or check token status. Trigger keywords: "outlook calendar", "ms calendar", "graph calendar", "我的 outlook 日历", "微软日历".

**中文介绍**: Read and write the signed-in user's Microsoft 365 / Outlook.com personal calendar via Microsoft Graph. Calendar-only. No mail, no files, no contacts, no directory access. Use when the user wants to list today's events, look at next week, create / update / delete a single event by id, or check token status. Trigger keywords: "outlook calendar", "ms calendar", "graph calendar", "我的 outlook 日历", "微软日历".

Latest changelog:
Security hardening per SkillSpector findings: accurate scope disclosure (family-shared 5-scope consent stated in all docs), removed OPENCLAW_CLI confirmation bypass (explicit --yes flag is the only non-interactive path), runtime validation of authority/graph_base endpoints, chmod failures now fatal, contacts read-path guidance narrowed, todo write capability documented.

**关键词**: outlook-calendar, Read, write, signed-in, user's, Microsoft, Outlook.com, personal

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/outlook-calendar)

---

## [4. outlook-todo](https://clawhub.ai/guoxh/outlook-todo)

**Slug**: `outlook-todo`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 28 | 🧩 3

**原始简介**: Read and write Microsoft To Do tasks (create, update, complete, delete) via shared Outlook Graph auth; writes require --apply plus a typed-YES prompt or an explicit --yes flag.

**中文介绍**: Read and write Microsoft To Do tasks (create, update, complete, delete) via shared Outlook Graph auth; writes require --apply plus a typed-YES prompt or an explicit --yes flag.

Latest changelog:
Security hardening per SkillSpector findings: accurate scope disclosure (family-shared 5-scope consent stated in all docs), removed OPENCLAW_CLI confirmation bypass (explicit --yes flag is the only non-interactive path), runtime validation of authority/graph_base endpoints, chmod failures now fatal, contacts read-path guidance narrowed, todo write capability documented.

**关键词**: Do, outlook-todo, Read, write, Microsoft, tasks, update, complete

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/outlook-todo)

---

## [5. outlook-contacts](https://clawhub.ai/guoxh/outlook-contacts)

**Slug**: `outlook-contacts`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 29 | 🧩 3

**原始简介**: Read and write the signed-in user's Microsoft 365 / Outlook.com personal contacts via Microsoft Graph. No mail, no files, no directory access. Use when the user wants to list/search Outlook.com contacts, find phone numbers, or look up email addresses. Trigger keywords: "outlook contacts", "ms contacts", "graph contacts", "我的联系人", "查联系人", "outlook 联系人".

**中文介绍**: Read and write the signed-in user's Microsoft 365 / Outlook.com personal contacts via Microsoft Graph. No mail, no files, no directory access. Use when the user wants to list/search Outlook.com contacts, find phone numbers, or look up email addresses. Trigger keywords: "outlook contacts", "ms contacts", "graph contacts", "我的联系人", "查联系人", "outlook 联系人".

Latest changelog:
Security hardening per SkillSpector findings: accurate scope disclosure (family-shared 5-scope consent stated in all docs), removed OPENCLAW_CLI confirmation bypass (explicit --yes flag is the only non-interactive path), runtime validation of authority/graph_base endpoints, chmod failures now fatal, contacts read-path guidance narrowed, todo write capability documented.

**关键词**: outlook-contacts, Read, write, signed-in, user's, Microsoft, Outlook.com, personal

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/outlook-contacts)

---

## [6. lunheng-article-pipeline](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.6.8  
**Stats**: ⭐ 1 | ⬇️ 1500 | 🧩 68

**原始简介**: 严肃长文流水线（学术论文/商业评论/行业分析/公众号深度长文）——多 Agent 子代理编排。三角验证（文献/数据/案例）+ M 门（LLM 结构化判定）+ F 失败模式防御 + 数据信任 3 档 + 修订回环 ≤2 轮。使用前需 Phase 0 同意关卡。<2000 字建议直接用主控 LLM。

**中文介绍**: 严肃长文流水线（学术论文/商业评论/行业分析/公众号深度长文）——多 Agent 子代理编排。三角验证（文献/数据/案例）+ M 门（LLM 结构化判定）+ F 失败模式防御 + 数据信任 3 档 + 修订回环 ≤2 轮。使用前需 Phase 0 同意关卡。<2000 字建议直接用主控 LLM。

Latest changelog:
lunheng-article-pipeline 2.6.8

- Major documentation updates: over 50 reference/agent/checklist files revised for clarity and standards.
- Expanded and clarified protocols across multiple shared and agent markdown docs.
- Updated QUICKSTART.md and core references for improved onboarding and guidance.
- No functional or interface-breaking changes to pipeline logic.  
- Improvements directly address code review and best practices adherence.

**关键词**: 严肃长文流水线（学术论文, 商业评论, 行业分析, 公众号深度长文）——多, Agent, 子代理编排, 三角验证（文献, lunheng-article-pipeline

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [7. Kaggle Openmm Md Runbook](https://clawhub.ai/orionshaowswmw/kaggle-openmm-md-runbook)

**Slug**: `kaggle-openmm-md-runbook`  
**Version**: 1.1.3  
**Stats**: ⭐ 0 | ⬇️ 78 | 🧩 7

**原始简介**: Battle-tested runbook for running long (100 ns) OpenMM molecular dynamics on Kaggle's free GPU (P100 sm_60) — covers the mandatory OpenMM 8.3.1 pin, checkpoi...

**中文介绍**: Battle-tested runbook for running long (100 ns) OpenMM molecular dynamics on Kaggle's free GPU (P100 sm_60) — covers the mandatory OpenMM 8.3.1 pin, checkpoi...

Latest changelog:
v1.1.3 — as v1.1.2 + supervisor wording hardened for review (user-started, self-stopping bounded monitor; dies with sandbox)

**关键词**: Md, ns, Kaggle, Openmm, Runbook, Battle-tested, running, long

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/kaggle-openmm-md-runbook)

---

## [8. FrameFerry](https://clawhub.ai/saju01/frameferry)

**Slug**: `frameferry`  
**Version**: 0.2.1  
**Stats**: ⭐ 1 | ⬇️ 61 | 🧩 2

**原始简介**: Archive public Instagram media through InstaCognito with bounded archive/sync runs, section-aware outcomes, durable receipts, and optional local ZIP export.

**中文介绍**: Archive public Instagram media through InstaCognito with bounded archive/sync runs, section-aware outcomes, durable receipts, and optional local ZIP export.

Latest changelog:
Fix provider pagination sentinel targeting; preserve bounded fallbacks and unknown-year provenance.

**关键词**: FrameFerry, Archive, public, Instagram, media, through, InstaCognito, bounded

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/frameferry)

---

## [9. 詹明明·今天拍什么](https://clawhub.ai/iamzifei/zmm-topic)

**Slug**: `zmm-topic`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 212 | 🧩 12

**原始简介**: 📐 詹明明·今天拍什么 ——短视频选题技能。交互式选题：供需判定 + 对标信号 + 本人真实数据佐证 + 配比检查，不一键生成选题清单。 触发方式：/zmm-topic、/拍什么、/选题、/zmm-选题、「今天拍什么」「帮我出选题」「这个题能不能做」「有个想法你帮我判断下」「这题只有一头」「这题没劲」「帮我把它讲出两头来」 Topic selection for short videos: supply-demand test, benchmark signals, real data evidence. Trigger: /zmm-topic, "what topic should I shoot", "is this topic worth making" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·今天拍什么 ——短视频选题技能。交互式选题：供需判定 + 对标信号 + 本人真实数据佐证 + 配比检查，不一键生成选题清单。 触发方式：/zmm-topic、/拍什么、/选题、/zmm-选题、「今天拍什么」「帮我出选题」「这个题能不能做」「有个想法你帮我判断下」「这题只有一头」「这题没劲」「帮我把它讲出两头来」 Topic selection for short videos: supply-demand test, benchmark signals, real data evidence. Trigger: /zmm-topic, "what topic should I shoot", "is this topic worth making" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 五处技能落后于规则的补齐（0.x.1）

**关键词**: 詹明明·今天拍什么, ——短视频选题技能, 交互式选题, 供需判定, 对标信号, 本人真实数据佐证, 配比检查, 不一键生成选题清单

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-topic)

---

## [10. workbuddy-usage-status](https://clawhub.ai/clancy-feng/workbuddy-usage-status)

**Slug**: `workbuddy-usage-status`  
**Version**: 1.3.1  
**Stats**: ⭐ 0 | ⬇️ 743 | 🧩 9

**原始简介**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信息看板时调用；不用于其他产品或系统的用量统计，也不为任意数据生成通用看板。纯本地、默认零外网依赖、可搬运；可选 --credit-xlsx 用用量导出精确覆盖 credit，或可选 --billing-token-file（用户手动导出 token，opt-in）调用官方用量 API 拉取精确 credit。 EN: Offline dashboard for WorkBuddy local usage analytics, with token as primary metric and credit as local estimate, covering thinking efficiency, model distribution & cost-performance, date-range filtering, error monitoring, usage-spike inspection. Triggers only when the user explicitly wants to view, generate, or export their own WorkBuddy local/account usage status / stats / activity dashboard; not for other products' usage analytics, nor for building generic dashboards from arbitrary data. Fully local, default zero-network; optionally --billing-token-file (user-supplied token, opt-in) calls the official usage API for precise credit, or --credit-xlsx overrides credit with precise export values.

**中文介绍**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信息看板时调用；不用于其他产品或系统的用量统计，也不为任意数据生成通用看板。纯本地、默认零外网依赖、可搬运；可选 --credit-xlsx 用用量导出精确覆盖 credit，或可选 --billing-token-file（用户手动导出 token，opt-in）调用官方用量 API 拉取精确 credit。 EN: Offline dashboard for WorkBuddy local usage analytics, with token as primary metric and credit as local estimate, covering thinking efficiency, model distribution & cost-performance, date-range filtering, error monitoring, usage-spike inspection. Triggers only when the user explicitly wants to view, generate, or export their own WorkBuddy local/account usage status / stats / activity dashboard; not for other products' usage analytics, nor for building generic dashboards from arbitrary data. Fully local, default zero-network; optionally --billing-token-file (user-supplied token, opt-in) calls the official usage API for precise credit, or --credit-xlsx overrides credit with precise export values.

Latest changelog:
v1.3.1:Bug fix and Document update

**关键词**: 离线可视化, 本机使用数据, 消耗为主指标、credit, 为本地估算, 生成本地使用信息看板, workbuddy-usage-status, WorkBuddy, token

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-usage-status)

---

## [11. 詹明明·标题与封面](https://clawhub.ai/iamzifei/zmm-title)

**Slug**: `zmm-title`  
**Version**: 0.2.7  
**Stats**: ⭐ 0 | ⬇️ 186 | 🧩 10

**原始简介**: 📐 詹明明·标题与封面 ——多平台标题与封面。按内容本身的形状选结构（12 种结构清单），过卖真 / 违禁词 / 不点名 / 黑话红线，每个标题说清用了什么结构、为什么配这条内容。**不给「通用爆款公式」——实证显示标题结构在不同账号间不通用，附脚本让你算出自己账号的规律。** 触发方式：/zmm-title、/封面、/标题、/zmm-标题、「起个标题」「抖音封面写什么」「小红书标题」「封面大字怎么写」「帮我优化这个标题」 Multi-platform titles and cover text. Picks a structure that fits the content rather than applying a "proven formula" — cross-source testing found none of 12 common title structures replicate across differently-styled accounts. Ships a script to derive your own. Trigger: /zmm-title, "give me a title", "Douyin cover text", "xiaohongshu title" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·标题与封面 ——多平台标题与封面。按内容本身的形状选结构（12 种结构清单），过卖真 / 违禁词 / 不点名 / 黑话红线，每个标题说清用了什么结构、为什么配这条内容。**不给「通用爆款公式」——实证显示标题结构在不同账号间不通用，附脚本让你算出自己账号的规律。** 触发方式：/zmm-title、/封面、/标题、/zmm-标题、「起个标题」「抖音封面写什么」「小红书标题」「封面大字怎么写」「帮我优化这个标题」 Multi-platform titles and cover text. Picks a structure that fits the content rather than applying a "proven formula" — cross-source testing found none of 12 common title structures replicate across differently-styled accounts. Ships a script to derive your own. Trigger: /zmm-title, "give me a title", "Douyin cover text", "xiaohongshu title" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 五处技能落后于规则的补齐（0.x.1）

**关键词**: 詹明明·标题与封面, ——多平台标题与封面, 按内容本身的形状选结构（12, 种结构清单）, 过卖真, 违禁词, 不点名, 黑话红线

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-title)

---

## [12. 詹明明·发布前审一遍](https://clawhub.ai/iamzifei/zmm-review)

**Slug**: `zmm-review`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 196 | 🧩 11

**原始简介**: 📐 詹明明·发布前审一遍 ——口播稿发布前审核技能。按观众的四次决定审：点不点进来 · 留不留下来 · 记不记得你 · 做不做点什么。逐句信息密度评分（60/80 分线）+ 十一问 + 红线五查（改法给稳妥版和保留力度版两版）+ 机器信号层（导流 / 广告形状 / 名单词，与内容违规分开报），默认只诊断不改。 触发方式：/zmm-review、/能不能发、/审核、/zmm-审核、「这稿子能不能发」「帮我审一下」「过一遍红线」「信息密度够不够」 Pre-publish review for talking-head scripts, organised around the viewer's four decisions: click, stay, remember, act. Per-sentence density scoring, eleven questions, red-line audit. Diagnose-only by default. Trigger: /zmm-review, "can I publish this", "review my script" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·发布前审一遍 ——口播稿发布前审核技能。按观众的四次决定审：点不点进来 · 留不留下来 · 记不记得你 · 做不做点什么。逐句信息密度评分（60/80 分线）+ 十一问 + 红线五查（改法给稳妥版和保留力度版两版）+ 机器信号层（导流 / 广告形状 / 名单词，与内容违规分开报），默认只诊断不改。 触发方式：/zmm-review、/能不能发、/审核、/zmm-审核、「这稿子能不能发」「帮我审一下」「过一遍红线」「信息密度够不够」 Pre-publish review for talking-head scripts, organised around the viewer's four decisions: click, stay, remember, act. Per-sentence density scoring, eleven questions, red-line audit. Diagnose-only by default. Trigger: /zmm-review, "can I publish this", "review my script" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 五处技能落后于规则的补齐（0.x.1）

**关键词**: 詹明明·发布前审一遍, ——口播稿发布前审核技能, 按观众的四次决定审, 点不点进来, 留不留下来, 记不记得你, 做不做点什么, 逐句信息密度评分（60

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-review)

---

## [13. 詹明明·口播稿写作](https://clawhub.ai/iamzifei/zmm-script)

**Slug**: `zmm-script`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 207 | 🧩 11

**原始简介**: 📐 詹明明·口播稿写作 ——口播稿协作写作技能（知识付费口播为主形态）。三类脚本选型 + 从内容单元装配 + 逐段共创，不一键成稿。 触发方式：/zmm-script、/写口播、/写稿、/zmm-写稿、「写个口播稿」「帮我把这个题写出来」「知识付费口播」「写条视频文案」 Collaborative koubo (talking-head) script writing: script-type selection, unit assembly, section-by-section co-writing. Trigger: /zmm-script, "write a talking-head script", "turn this topic into a video script" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·口播稿写作 ——口播稿协作写作技能（知识付费口播为主形态）。三类脚本选型 + 从内容单元装配 + 逐段共创，不一键成稿。 触发方式：/zmm-script、/写口播、/写稿、/zmm-写稿、「写个口播稿」「帮我把这个题写出来」「知识付费口播」「写条视频文案」 Collaborative koubo (talking-head) script writing: script-type selection, unit assembly, section-by-section co-writing. Trigger: /zmm-script, "write a talking-head script", "turn this topic into a video script" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 五处技能落后于规则的补齐（0.x.1）

**关键词**: 詹明明·口播稿写作, ——口播稿协作写作技能（知识付费口播为主形态）, 三类脚本选型, 从内容单元装配, 逐段共创, 不一键成稿, 触发方式, zmm-script、

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-script)

---

## [14. 詹明明·重讲一个概念](https://clawhub.ai/iamzifei/zmm-concept)

**Slug**: `zmm-concept`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 184 | 🧩 11

**原始简介**: 📐 詹明明·重讲一个概念 ——重讲一个大家都在用的概念（定价 / 选题 / 需求 / 转化 / 获客…）——拆开它，从裂缝里长出一把尺子。先锁四样再写稿，最后由本人口述定稿。 触发方式：/zmm-concept、/重讲概念、「把 XX 这个概念讲清楚」「XX 到底是什么」「为什么 XX 越 YY 越 ZZ」「掰开揉碎讲一个概念」 Re-explain a concept the audience already uses: crack it open, hand them a ruler. Lock four things before drafting; final version comes from the host's own spoken take. Trigger: /zmm-concept, "explain X properly", "why does more X lead to less Y" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·重讲一个概念 ——重讲一个大家都在用的概念（定价 / 选题 / 需求 / 转化 / 获客…）——拆开它，从裂缝里长出一把尺子。先锁四样再写稿，最后由本人口述定稿。 触发方式：/zmm-concept、/重讲概念、「把 XX 这个概念讲清楚」「XX 到底是什么」「为什么 XX 越 YY 越 ZZ」「掰开揉碎讲一个概念」 Re-explain a concept the audience already uses: crack it open, hand them a ruler. Lock four things before drafting; final version comes from the host's own spoken take. Trigger: /zmm-concept, "explain X properly", "why does more X lead to less Y" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 五处技能落后于规则的补齐（0.x.1）

**关键词**: 詹明明·重讲一个概念, ——重讲一个大家都在用的概念（定价, 选题, 需求, 转化, 获客…）——拆开它, 从裂缝里长出一把尺子, 先锁四样再写稿

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-concept)

---

## [15. Guaikei Kuaishou Public Data Fetcher](https://clawhub.ai/engheng-art/guaikei-kuaishou-public-data-fetcher)

**Slug**: `guaikei-kuaishou-public-data-fetcher`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 按关键词搜索快手视频、抓取博主公开作品和评论，返回结构化JSON，助力爆款选题、竞品监控及舆情分析。

**中文介绍**: 按关键词搜索快手视频、抓取博主公开作品和评论，返回结构化JSON，助力爆款选题、竞品监控及舆情分析。

Latest changelog:
- Initial release of guaikei-kuaishou-public-data-fetcher.
- Enables one-stop Kuaishou data collection: hot video search, creator post tracking, and comment retrieval.
- No login required; collects public data and outputs structured JSON for downstream analysis.
- Supports search by keyword, fetches creator's public posts, and extracts comments from specific videos.
- Includes robust error handling and clear input requirements.
- Requires GUAIKEI_API_TOKEN for API access.

**关键词**: 按关键词搜索快手视频、抓取博主公开作品和评论, 返回结构化JSON, 助力爆款选题、竞品监控及舆情分析, Guaikei, Kuaishou, Public, Data, Fetcher

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-kuaishou-public-data-fetcher)

---

## [16. 詹明明](https://clawhub.ai/iamzifei/zmm)

**Slug**: `zmm`  
**Version**: 0.2.8  
**Stats**: ⭐ 0 | ⬇️ 235 | 🧩 11

**原始简介**: 📐 詹明明 ——两套技能的总入口：做内容（选题/写稿/审核/复盘）+ 看生意（组合体检/营收归因/客户集中度/依赖风险/拿不准的决策）。三种模式：新手上路演示、任务前路由、任务后导航。不知道用哪个就回这里。 触发方式：/zmm、/新手上路、/zmm 教程、「做条视频」「出个口播」「今天拍什么」「内容下一步怎么走」；新手教程：/zmm 新手指南、/zmm 新手、「这个怎么用」「第一次用，带我走一遍」「不知道能干嘛」 Single entry point for both skill sets — content (topic, script, review, retro) and business (portfolio, revenue, concentration, dependency, decisions). Three modes: guided onboarding demo, pre-task routing, post-task navigation. Trigger: /zmm, "make a short video", "what should I shoot today", "how do I use this" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明 ——两套技能的总入口：做内容（选题/写稿/审核/复盘）+ 看生意（组合体检/营收归因/客户集中度/依赖风险/拿不准的决策）。三种模式：新手上路演示、任务前路由、任务后导航。不知道用哪个就回这里。 触发方式：/zmm、/新手上路、/zmm 教程、「做条视频」「出个口播」「今天拍什么」「内容下一步怎么走」；新手教程：/zmm 新手指南、/zmm 新手、「这个怎么用」「第一次用，带我走一遍」「不知道能干嘛」 Single entry point for both skill sets — content (topic, script, review, retro) and business (portfolio, revenue, concentration, dependency, decisions). Three modes: guided onboarding demo, pre-task routing, post-task navigation. Trigger: /zmm, "make a short video", "what should I shoot today", "how do I use this" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明, ——两套技能的总入口, 做内容（选题, 写稿, 审核, 复盘）+, 看生意（组合体检, 营收归因

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm)

---

## [17. Guaikei Kuaishou Rank Data Fetcher](https://clawhub.ai/engheng-art/guaikei-kuaishou-rank-data-fetcher)

**Slug**: `guaikei-kuaishou-rank-data-fetcher`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Collect and return structured public Kuaishou data by keyword search, creator posts, or video comments for trend, competitor, and sentiment analysis.

**中文介绍**: Collect and return structured public Kuaishou data by keyword search, creator posts, or video comments for trend, competitor, and sentiment analysis.

Latest changelog:
- Initial release of guaikei-kuaishou-rank-data-fetcher.
- Supports structured Kuaishou data fetching: video search by keyword, creator post tracking, and video comment capture.
- Command-line tool—no Kuaishou login required; all data is public and output as structured JSON.
- Large-scale, batch-enabled data pulls (up to 10,000 items per request).
- Input routing: keyword for video search, profile URL/user_id for creator posts, video URL for comments.
- Requires GUAIKEI_API_TOKEN for API access; detailed error handling and clear output structure provided.

**关键词**: Guaikei, Kuaishou, Rank, Data, Fetcher, Collect, return, structured

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-kuaishou-rank-data-fetcher)

---

## [18. Guaikei Kuaishou Trending Video Fetcher](https://clawhub.ai/engheng-art/guaikei-kuaishou-trending-video-fetcher)

**Slug**: `guaikei-kuaishou-trending-video-fetcher`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 按关键词搜索快手视频、抓取博主公开作品和视频评论，返回结构化JSON，支持爆款选题和竞品监控分析。

**中文介绍**: 按关键词搜索快手视频、抓取博主公开作品和视频评论，返回结构化JSON，支持爆款选题和竞品监控分析。

Latest changelog:
- Initial release of guaikei-kuaishou-trending-video-fetcher.
- Provides one-stop Kuaishou data collection: trending video search, creator post tracking, and comment fetching.
- Returns structured JSON for search, posts, and comments; no Kuaishou login required.
- Supports use cases like competitor monitoring, trending topic discovery, KOL filtering, and comment analysis.
- Requires configuration of the GUAIKEI_API_TOKEN for API access.

**关键词**: 按关键词搜索快手视频、抓取博主公开作品和视频评论, 返回结构化JSON, 支持爆款选题和竞品监控分析, Guaikei, Kuaishou, Trending, Video, Fetcher

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-kuaishou-trending-video-fetcher)

---

## [19. 詹明明·做成一个技能](https://clawhub.ai/iamzifei/zmm-skillify)

**Slug**: `zmm-skillify`  
**Version**: 0.1.5  
**Stats**: ⭐ 0 | ⬇️ 126 | 🧩 6

**原始简介**: 📐 詹明明·做成一个技能 ——把这次会话里已经跑通的做法固化成一个新技能。不是从想法造技能——是从**已经产生过正确结果的那一段过程**里提炼，所以只在事情做完之后用。 触发方式：/zmm-skillify、/固化、/做成技能、/zmm-固化、「这次的做法留下来」「把刚才那套变成技能」「下次别再重新想一遍」「这个流程以后还要用」 Turn a method that already worked in this session into a reusable skill. Extracts from a completed run, never from an idea — so it only fires after the work is done. Trigger: /zmm-skillify, "make this a skill", "save this workflow", "I don't want to re-derive this next time" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·做成一个技能 ——把这次会话里已经跑通的做法固化成一个新技能。不是从想法造技能——是从**已经产生过正确结果的那一段过程**里提炼，所以只在事情做完之后用。 触发方式：/zmm-skillify、/固化、/做成技能、/zmm-固化、「这次的做法留下来」「把刚才那套变成技能」「下次别再重新想一遍」「这个流程以后还要用」 Turn a method that already worked in this session into a reusable skill. Extracts from a completed run, never from an idea — so it only fires after the work is done. Trigger: /zmm-skillify, "make this a skill", "save this workflow", "I don't want to re-derive this next time" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·做成一个技能, ——把这次会话里已经跑通的做法固化成一个新技能, 不是从想法造技能——是从, 已经产生过正确结果的那一段过程, 里提炼, 所以只在事情做完之后用, 触发方式, zmm-skillify、

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-skillify)

---

## [20. 詹明明·我该卖什么](https://clawhub.ai/iamzifei/zmm-product)

**Slug**: `zmm-product`  
**Version**: 0.2.6  
**Stats**: ⭐ 0 | ⬇️ 189 | 🧩 9

**原始简介**: 📐 詹明明·我该卖什么 ——产品提炼技能。把碎片化的认知、经验、资源、已有产出，提炼成一个可交付、可售卖的东西。 广义产品：实物、线上产品、线下服务、课程、一套框架或理论、一个营收增长点，都算。 触发方式：/zmm-product、/提炼产品、/我该卖什么、/zmm-产品、「我有资源但不知道做什么产品」「我这个算产品吗」「怎么把我会的东西变成能卖的」「产品没特色」 Turn scattered experience, context and existing output into one deliverable worth paying for. Trigger: /zmm-product, "what should I sell", "is this actually a product", "how do I package what I know" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·我该卖什么 ——产品提炼技能。把碎片化的认知、经验、资源、已有产出，提炼成一个可交付、可售卖的东西。 广义产品：实物、线上产品、线下服务、课程、一套框架或理论、一个营收增长点，都算。 触发方式：/zmm-product、/提炼产品、/我该卖什么、/zmm-产品、「我有资源但不知道做什么产品」「我这个算产品吗」「怎么把我会的东西变成能卖的」「产品没特色」 Turn scattered experience, context and existing output into one deliverable worth paying for. Trigger: /zmm-product, "what should I sell", "is this actually a product", "how do I package what I know" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·我该卖什么, ——产品提炼技能, 把碎片化的认知、经验、资源、已有产出, 提炼成一个可交付、可售卖的东西, 广义产品, 都算, 触发方式, zmm-product、

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-product)

---

## [21. 詹明明·发布后复盘](https://clawhub.ai/iamzifei/zmm-retro)

**Slug**: `zmm-retro`  
**Version**: 0.2.7  
**Stats**: ⭐ 0 | ⬇️ 188 | 🧩 10

**原始简介**: 📐 詹明明·发布后复盘 ——短视频复盘技能。发布后把真实平台数据收回来，对照发布前的预判做归因讨论，把验证过的规律写进技能记忆——让系统学会「为什么这条火」。 触发方式：/zmm-retro、/数据出来了、/复盘、/zmm-复盘、「这条数据出来了」「为什么这条火」「为什么这条没火」「复盘一下」 Post-publish retro: collect real platform data, attribute against pre-publish predictions, write validated patterns into skill memory. Trigger: /zmm-retro, "the numbers are in", "why did this video flop/pop" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·发布后复盘 ——短视频复盘技能。发布后把真实平台数据收回来，对照发布前的预判做归因讨论，把验证过的规律写进技能记忆——让系统学会「为什么这条火」。 触发方式：/zmm-retro、/数据出来了、/复盘、/zmm-复盘、「这条数据出来了」「为什么这条火」「为什么这条没火」「复盘一下」 Post-publish retro: collect real platform data, attribute against pre-publish predictions, write validated patterns into skill memory. Trigger: /zmm-retro, "the numbers are in", "why did this video flop/pop" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·发布后复盘, ——短视频复盘技能, 发布后把真实平台数据收回来, 对照发布前的预判做归因讨论, 触发方式, 数据出来了、, 复盘、, zmm-retro、

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-retro)

---

## [22. apiguru-amazon-data](https://clawhub.ai/apiguru-app/apiguru-amazon-data)

**Slug**: `apiguru-amazon-data`  
**Version**: 1.1.11  
**Stats**: ⭐ 0 | ⬇️ 200 | 🧩 13

**原始简介**: Live Amazon marketplace data from Apiguru (a paid third-party API, 3 free calls a day) - product details, prices, reviews, keyword search, best-sellers, deals, offers and stock, seller profiles, across 20 Amazon marketplaces. Use only when the user asks for Amazon data by ASIN, Amazon URL, product, seller or keyword, or for Amazon price/stock/review monitoring. Not for other stores or general shopping advice. Never pays on its own; ask before any billable call.

**中文介绍**: Live Amazon marketplace data from Apiguru (a paid third-party API, 3 free calls a day) - product details, prices, reviews, keyword search, best-sellers, deals, offers and stock, seller profiles, across 20 Amazon marketplaces. Use only when the user asks for Amazon data by ASIN, Amazon URL, product, seller or keyword, or for Amazon price/stock/review monitoring. Not for other stores or general shopping advice. Never pays on its own; ask before any billable call.

Latest changelog:
Release 1.1.11

**关键词**: apiguru-amazon-data, Live, Amazon, marketplace, data, Apiguru, paid, third-party

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/apiguru-amazon-data)

---

## [23. 詹明明·戳不戳得中人](https://clawhub.ai/iamzifei/zmm-resonate)

**Slug**: `zmm-resonate`  
**Version**: 0.2.7  
**Stats**: ⭐ 0 | ⬇️ 190 | 🧩 10

**原始简介**: 📐 詹明明·戳不戳得中人 ——共鸣诊断技能。不从理论出发，从观众出发：这条内容让观众带走了哪一种收获（原来是这样 / 我就说吧 / 他替我说了），会不会动手（收藏 / 转发 / 评论 / 关注），每个判断都指到原文并标它是证据、推断还是待验证。模式A 诊断自己的草稿；模式B 拆一条别人的爆款反推可借的角度；模式C 判一句「我觉得不对劲」背后是一件事还是一群人的事。与 zmm-review 正交：review 防句废，resonate 防结构散。 触发方式：/zmm-resonate、/戳不戳人、/共鸣、/zmm-共鸣、「这稿有没有戳中人」「会不会没人看」「这条为什么能火」「拆一下这个爆款」「受众到底想听什么」「这事值不值得拍一条」「我总觉得哪里不对但说不上来」「这是我一个人的事还是大家的事」 Resonance diagnosis, audience-first: which takeaway the piece delivers, which action impulse it triggers, with every claim tied to a quoted line and labelled evidence / inference / to-verify. Mode A: your draft. Mode B: decode a hit. Mode C: test whether a hunch is one incident or a pattern. Trigger: /zmm-resonate, "will this resonate", "why did this blow up", "decode this viral post" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·戳不戳得中人 ——共鸣诊断技能。不从理论出发，从观众出发：这条内容让观众带走了哪一种收获（原来是这样 / 我就说吧 / 他替我说了），会不会动手（收藏 / 转发 / 评论 / 关注），每个判断都指到原文并标它是证据、推断还是待验证。模式A 诊断自己的草稿；模式B 拆一条别人的爆款反推可借的角度；模式C 判一句「我觉得不对劲」背后是一件事还是一群人的事。与 zmm-review 正交：review 防句废，resonate 防结构散。 触发方式：/zmm-resonate、/戳不戳人、/共鸣、/zmm-共鸣、「这稿有没有戳中人」「会不会没人看」「这条为什么能火」「拆一下这个爆款」「受众到底想听什么」「这事值不值得拍一条」「我总觉得哪里不对但说不上来」「这是我一个人的事还是大家的事」 Resonance diagnosis, audience-first: which takeaway the piece delivers, which action impulse it triggers, with every claim tied to a quoted line and labelled evidence / inference / to-verify. Mode A: your draft. Mode B: decode a hit. Mode C: test whether a hunch is one incident or a pattern. Trigger: /zmm-resonate, "will this resonate", "why did this blow up", "decode this viral post" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·戳不戳得中人, ——共鸣诊断技能, 不从理论出发, 从观众出发, 这条内容让观众带走了哪一种收获（原来是这样, 我就说吧, 他替我说了）, 会不会动手（收藏

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-resonate)

---

## [24. 詹明明·哪里会被划走](https://clawhub.ai/iamzifei/zmm-flow)

**Slug**: `zmm-flow`  
**Version**: 0.2.7  
**Stats**: ⭐ 0 | ⬇️ 198 | 🧩 10

**原始简介**: 📐 詹明明·哪里会被划走 ——口播稿「划走点」专项。替观众把稿子听一遍：每一拍观众手里有什么、在等什么，断在哪一拍 —— 等的没来、手里有了还在给、正在给的听不清。诊断完默认主动问是否标记式改稿。 触发方式：/zmm-flow、/会不会划走、/顺稿、/zmm-顺稿、「这稿子顺不顺」「哪里会划走」「逻辑有没有断」「读起来卡不卡」「完播会不会掉」 Drop-off check for talking-head scripts: walk the script as a listener, beat by beat — what the viewer holds, what they are waiting for, and where that chain breaks. Trigger: /zmm-flow, "does this script flow", "where will viewers drop off", "check retention risk" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·哪里会被划走 ——口播稿「划走点」专项。替观众把稿子听一遍：每一拍观众手里有什么、在等什么，断在哪一拍 —— 等的没来、手里有了还在给、正在给的听不清。诊断完默认主动问是否标记式改稿。 触发方式：/zmm-flow、/会不会划走、/顺稿、/zmm-顺稿、「这稿子顺不顺」「哪里会划走」「逻辑有没有断」「读起来卡不卡」「完播会不会掉」 Drop-off check for talking-head scripts: walk the script as a listener, beat by beat — what the viewer holds, what they are waiting for, and where that chain breaks. Trigger: /zmm-flow, "does this script flow", "where will viewers drop off", "check retention risk" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·哪里会被划走, ——口播稿「划走点」专项, 替观众把稿子听一遍, 每一拍观众手里有什么、在等什么, 断在哪一拍, ——, 等的没来、手里有了还在给、正在给的听不清, 诊断完默认主动问是否标记式改稿

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-flow)

---

## [25. 詹明明·选题先试水](https://clawhub.ai/iamzifei/zmm-mvp)

**Slug**: `zmm-mvp`  
**Version**: 0.2.5  
**Stats**: ⭐ 0 | ⬇️ 193 | 🧩 8

**原始简介**: 📐 詹明明·选题先试水 ——选题 MVP 测试技能。碎片输入（一句话想法/聊天记录/X 见闻/候选选题）→ 生成发 X 用的纯文字测试内容（篇幅不限，内容需要多长写多长，排版清晰）→ 登记测试管道 → 用真实互动数据决定该题进抖音、扩公众号还是淘汰。验证一个想法只花一条文本，不花一条真视频。 触发方式：/zmm-mvp、/发条测试、/试水、/zmm-测试、「发条推测试」「写个 X 短文」「这个想法先试试水」「值不值得拍一条」 MVP text-testing: turn a fragment into a plain-text X post (length as the idea needs, well formatted) to cheaply validate a topic before it costs a real video. Trigger: /zmm-mvp, "test this idea on X", "write a short post to validate" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

**中文介绍**: 📐 詹明明·选题先试水 ——选题 MVP 测试技能。碎片输入（一句话想法/聊天记录/X 见闻/候选选题）→ 生成发 X 用的纯文字测试内容（篇幅不限，内容需要多长写多长，排版清晰）→ 登记测试管道 → 用真实互动数据决定该题进抖音、扩公众号还是淘汰。验证一个想法只花一条文本，不花一条真视频。 触发方式：/zmm-mvp、/发条测试、/试水、/zmm-测试、「发条推测试」「写个 X 短文」「这个想法先试试水」「值不值得拍一条」 MVP text-testing: turn a fragment into a plain-text X post (length as the idea needs, well formatted) to cheaply validate a topic before it costs a real video. Trigger: /zmm-mvp, "test this idea on X", "write a short post to validate" —— 📐 詹明明 · 不给公式，给判据。每条规则都标了实测代价。

Latest changelog:
sync: 内置规则卡（280 张 / 14 技能）· 找拉力 / 一件事还是一群人 / 四次决定十一问 · 14 技能 minor 升版

**关键词**: 詹明明·选题先试水, ——选题, 测试技能, 碎片输入（一句话想法, 聊天记录, 见闻, 候选选题）→, MVP

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zmm-mvp)

---

