# ClawHub Skills Daily | 2026-08-25

> 共 25 个 skills

## [1. Clinical Trial Chief Advisor / 临床试验总顾问](https://clawhub.ai/medstatstar/ct-advisor)

**Slug**: `ct-advisor`  
**Version**: 0.9.103  
**Stats**: ⭐ 0 | ⬇️ 922 | 🧩 22

**原始简介**: 面向临床研发全生命周期的 ct 系列「总入口」，云端辅助的临床试验总顾问。方法学/设计/合规/QC/语气类问题在内部走 A–J 工作流并转发远程 Coze 引擎精校；统计计算转交 ct-samplesize；原始数据/竞品情报类需求路由到 ct-registry / ct-safety / ct-literature 并在代码内缝合三源产出。本技能会在本机运行兄弟技能、保留语言偏好/上下文缓存/长期记忆等本地状态，并支持可选的脱敏错误报告。 / The ct-series TOTAL ENTRY POINT across the full clinical-development lifecycle — a cloud-assisted clinical-trial advisor. Methodology / design / compliance / QC / tone questions run in-house through workflows A–J and are forwarded to the remote Coze engine for refinement; sample-size computation is handed to ct-samplesize; raw-data and competitive-intel needs route to the three sibling data skills (ct-registry / ct-safety / ct-literature) and are stitched in code. The skill runs sibling skills locally, keeps local state (language preference / context cache / long-term memory), and supports an optional de-identified bug report.

**中文介绍**: 面向临床研发全生命周期的 ct 系列「总入口」，云端辅助的临床试验总顾问。方法学/设计/合规/QC/语气类问题在内部走 A–J 工作流并转发远程 Coze 引擎精校；统计计算转交 ct-samplesize；原始数据/竞品情报类需求路由到 ct-registry / ct-safety / ct-literature 并在代码内缝合三源产出。本技能会在本机运行兄弟技能、保留语言偏好/上下文缓存/长期记忆等本地状态，并支持可选的脱敏错误报告。 / The ct-series TOTAL ENTRY POINT across the full clinical-development lifecycle — a cloud-assisted clinical-trial advisor. Methodology / design / compliance / QC / tone questions run in-house through workflows A–J and are forwarded to the remote Coze engine for refinement; sample-size computation is handed to ct-samplesize; raw-data and competitive-intel needs route to the three sibling data skills (ct-registry / ct-safety / ct-literature) and are stitched in code. The skill runs sibling skills locally, keeps local state (language preference / context cache / long-term memory), and supports an optional de-identified bug report.

Latest changelog:
v0.9.103：发布前对齐 ct-base §16（kw_lexicon 同步修复、shared_sync_check 全一致）；Mode B 追问自包含化闭环（context_stitch 始终导出有界 conversation_history）；refiner ~区间记号渲染修正；追问/complex 超时上调 300s；删除'零出站'绝对化措辞改事实描述；[HIGH] Tp4 整改（README 范围现实核对横幅 + §5 离机/留本机两段式 + declared-purpose 对齐）；README 双语同步；新增 references/ADVANCED.md。因 SkillHub 预注册 0.9.102 占位升版至 0.9.103。

**关键词**: 临床试验总顾问, 面向临床研发全生命周期的, ct, 系列「总入口」, Clinical, Trial, Chief, Advisor

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ct-advisor)

---

## [2. branddock-on-brand](https://clawhub.ai/erikjager55/branddock-skill)

**Slug**: `branddock-skill`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 37 | 🧩 2

**原始简介**: Work on-brand with Branddock, the brand memory and brand check for AI. Use this skill whenever you create, rewrite or review content for a brand that uses Branddock (social posts, emails, blogs, ads, web copy, scripts) — it makes you fetch the real brand context first, write with it, score every out

**中文介绍**: Work on-brand with Branddock, the brand memory and brand check for AI. Use this skill whenever you create, rewrite or review content for a brand that uses Branddock (social posts, emails, blogs, ads, web copy, scripts) — it makes you fetch the real brand context first, write with it, score every out

Latest changelog:
Branddock-skill 1.1.0

- Added new connector tool: `get_brand_md` for richer brand context access.
- Clarified tool availability: image, video generation and import tools are only accessible via API key, not the MCP connector.
- Updated tool map and workflow instructions to reflect new and connector-specific capabilities.
- Removed outdated auxiliary file: skill-card.md.

**关键词**: branddock-on-brand, Work, on-brand, Branddock, brand, memory, check, Use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/branddock-skill)

---

## [3. professional-pdf-translator](https://clawhub.ai/cecil727/professional-pdf-translator)

**Slug**: `professional-pdf-translator`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 通用长篇文献/小说多页PDF逐页自动提取、匹配用户提供的本地术语表并翻译追加至DOCX的自动化工作流。适用于任何具有特定受众、包含大量专有名词的长文献、小众长篇小说、学术论文、技术白皮书等PDF翻译场景。用户自行提供原文PDF、专业术语对照表及输出路径。

**中文介绍**: 通用长篇文献/小说多页PDF逐页自动提取、匹配用户提供的本地术语表并翻译追加至DOCX的自动化工作流。适用于任何具有特定受众、包含大量专有名词的长文献、小众长篇小说、学术论文、技术白皮书等PDF翻译场景。用户自行提供原文PDF、专业术语对照表及输出路径。

Latest changelog:
- Removed the redundant file `skill-card.md` from the repository.
- Clarified动态词表（dynamic glossary）作为 extract_page.py `--terms` 参数最后一项传递，确保跨页术语匹配和统一。
- 补充说明了动态词表在翻译流程中的参与方式（不仅追加术语，也在匹配时始终参与）。
- OPTIMIZED说明结构，使步骤、文件要求、命令行示例的前后因果和用户指引更连贯。
- Changelog和原有功能未发生功能性变更，仅文档部分改进和文件精简。

**关键词**: 通用长篇文献, 用户自行提供原文PDF、专业术语对照表及输出路径, Latest, changelog, Removed, redundant, file, skill-card.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/professional-pdf-translator)

---

## [4. Siluzan CSO](https://clawhub.ai/sigedev01-bit/siluzan-cso)

**Slug**: `siluzan-cso`  
**Version**: 1.1.43  
**Stats**: ⭐ 0 | ⬇️ 2080 | 🧩 25

**原始简介**: 丝路赞内容运营平台（CSO）。**凡涉及以下任一类业务，必须先加载并使用本 skill**。 (1) **文案生成与改稿**：选题、爆款拆解、新写成稿（公众号、小红书、**视频口播/字幕/配音/分镜脚本**、博客、改稿润色、评论区回复等）须走 `three-lib-content-workflow/content-writer.workflow.md`；**热点/资讯生成选题**见 `topic-selection.md`；**单轨 / 多轨**（多轨默认 2 篇、可增减，可主动推断）见 `multi-track.md`；**禁止**直接成稿或聊天润色。 **视频脚本 vs 发布 Caption**：口播/字幕/分镜走 content-writer；上传发布框 Caption 走 `overseas-b2b-social-post`。 (2) **人设管理**：运营账号人设卡（styleGuide）；反推/查询/保存。 (3) **发布与运营**（YouTube/TikTok/Instagram/LinkedIn/X/Facebook）：OAuth、**账号分组**、发布、任务/重试、upload、**extract-cover**、planning、报表。 (4) **RAG 知识库**：品牌/产品问答与写稿事实依据。 **海外 B2B 社媒贴文/Caption**：走独立 skill `overseas-b2b-social-post`，不在本 skill 文案流程内。 **高频误路由**：写文案禁联网代替 rag query；发布/截封面须调 CLI。 **账号不明先问**：仅运营媒体账号；广告账户走 siluzan-tso。

**中文介绍**: 丝路赞内容运营平台（CSO）。**凡涉及以下任一类业务，必须先加载并使用本 skill**。 (1) **文案生成与改稿**：选题、爆款拆解、新写成稿（公众号、小红书、**视频口播/字幕/配音/分镜脚本**、博客、改稿润色、评论区回复等）须走 `three-lib-content-workflow/content-writer.workflow.md`；**热点/资讯生成选题**见 `topic-selection.md`；**单轨 / 多轨**（多轨默认 2 篇、可增减，可主动推断）见 `multi-track.md`；**禁止**直接成稿或聊天润色。 **视频脚本 vs 发布 Caption**：口播/字幕/分镜走 content-writer；上传发布框 Caption 走 `overseas-b2b-social-post`。 (2) **人设管理**：运营账号人设卡（styleGuide）；反推/查询/保存。 (3) **发布与运营**（YouTube/TikTok/Instagram/LinkedIn/X/Facebook）：OAuth、**账号分组**、发布、任务/重试、upload、**extract-cover**、planning、报表。 (4) **RAG 知识库**：品牌/产品问答与写稿事实依据。 **海外 B2B 社媒贴文/Caption**：走独立 skill `overseas-b2b-social-post`，不在本 skill 文案流程内。 **高频误路由**：写文案禁联网代替 rag query；发布/截封面须调 CLI。 **账号不明先问**：仅运营媒体账号；广告账户走 siluzan-tso。

Latest changelog:
siluzan-cso v1.1.43

- 新增各大主流平台运营规范文档：包含 YouTube、TikTok、LinkedIn、微信、抖音等。
- 内容生成工作流说明补充：三库策略需在各平台规则下使用，平台规则从独立 references 目录加载。
- content-writer/video-script 工作流等文件更新，完善内容生产与脚本生成流程。
- 安装脚本和工作流说明文档优化，提升脚本稳定性和阅读体验。
- skill-card.md 文件移除，精简冗余文档。

**关键词**: 丝路赞内容运营平台（CSO）, 凡涉及以下任一类业务, 必须先加载并使用本, 文案生成与改稿, 选题、爆款拆解、新写成稿（公众号、小红书、, Siluzan, CSO, skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/siluzan-cso)

---

## [5. binance-trader](https://clawhub.ai/skills?q=binance-trader)

**Slug**: `binance-trader`  
**Version**: 3.1.0  
**Stats**: ⭐ 0 | ⬇️ 9 | 🧩 2

**原始简介**: 币安 U 本位期货 MCP（binance-mcp-server）使用手册。前置依赖：须先安装 @iuk-ink/binance-mcp-server MCP 服务器。当用户需要加密货币行情分析、技术指标计算、风险量化评估或期货交易执行（下单/撤单/持仓管理/条件单）时使用。涵盖安装自检、工具选择决策、跨工具工作流、交易安全纪律与常见错误恢复剧本。

**中文介绍**: 币安 U 本位期货 MCP（binance-mcp-server）使用手册。前置依赖：须先安装 @iuk-ink/binance-mcp-server MCP 服务器。当用户需要加密货币行情分析、技术指标计算、风险量化评估或期货交易执行（下单/撤单/持仓管理/条件单）时使用。涵盖安装自检、工具选择决策、跨工具工作流、交易安全纪律与常见错误恢复剧本。

Latest changelog:
新增 metadata.version: "3.1.0"：与 MCP 服务器版本保持一致，便于工具链识别与校验 skill 对应版本
新增「接入方式选择」：明确本地单客户端使用 stdio 配置、远程部署 / 多客户端共享使用 HTTP 配置，并补充 HTTP 模式的 mcpServers 配置示例（type: "http" + /mcp 端点）
新增「远程部署变体」：服务器对外暴露且设置了 MCP_HTTP_TOKEN 时，需在 HTTP 客户端配置的 headers 中回传 Bearer 令牌（"Authorization": "Bearer <token>"）
更新 -1021 错误恢复剧本：时钟偏差告警多为间歇性（时钟偏差 + 偶发链路延迟叠加），可先重试一次；持续失败再校准系统时间（NTP 同步），无需改动服务端代码

**关键词**: 币安, 本位期货, 前置依赖, 须先安装, binance-trader, @iuk-ink, binance-mcp-server, MCP

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/binance-trader)

---

## [6. 房产样板间漫游视频｜AI-HIVE](https://clawhub.ai/wubin1836/real-estate-walkthrough-video-ai-hive)

**Slug**: `real-estate-walkthrough-video-ai-hive`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把房产样板间漫游视频需求变成可执行工作流、可运行代码与可交付内容

**中文介绍**: 把房产样板间漫游视频需求变成可执行工作流、可运行代码与可交付内容

Latest changelog:
首次发布AI-HIVE爆款结构与潜力商业内容中文Skill

**关键词**: 房产样板间漫游视频｜AI-HIVE, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/real-estate-walkthrough-video-ai-hive)

---

## [7. ava](https://clawhub.ai/kamalbuilds/ava)

**Slug**: `ava`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 77 | 🧩 2

**原始简介**: Use Ava to execute bounded DeFi from a coding agent (Claude Code, Cursor, Codex, OpenClaw). Live money is ava_lend_execute on Base (Morpho), never ava_copilot_turn. Connect https://www.getava.xyz/mcp after ava_session.

**中文介绍**: Use Ava to execute bounded DeFi from a coding agent (Claude Code, Cursor, Codex, OpenClaw). Live money is ava_lend_execute on Base (Morpho), never ava_copilot_turn. Connect https://www.getava.xyz/mcp after ava_session.

Latest changelog:
Public ClawHub install only. Live loop is ava_lend_execute on Base. Removed private ava-4.0 path and copilot SOP.

**关键词**: Agent, ava, Use, execute, bounded, DeFi, coding, Claude

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ava)

---

## [8. MC Ecosystem Adaptation Engineer](https://clawhub.ai/liang030214/mc-ecosystem-adapt-engine)

**Slug**: `mc-ecosystem-adapt-engine`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 360 | 🧩 5

**原始简介**: MC全生态智能适配工程师V1.0.4——专为Minecraft模组玩家和整合包作者打造的一站式AI智能管理工具。新用户首次使用享60天全功能免费期！覆盖15大核心功能：模组检索下载、环境引导搭建、Mixin冲突扫描、崩溃日志分析+一键自动修复、多语言翻译（中英日韩俄西意希泰印地+阿拉伯语RTL共12种）、跨版本移植评估、存档同步、完整商业化运营体系（支付宝/微信/PayPal三渠道在线支付+Web管理员控制台+自动化运营报表）。支持Forge/NeoForge/Fabric/Quilt四大加载器，原生兼容MC 1.16.5至1.21.x全版本，面向全球用户设计。

**中文介绍**: MC全生态智能适配工程师V1.0.4——专为Minecraft模组玩家和整合包作者打造的一站式AI智能管理工具。新用户首次使用享60天全功能免费期！覆盖15大核心功能：模组检索下载、环境引导搭建、Mixin冲突扫描、崩溃日志分析+一键自动修复、多语言翻译（中英日韩俄西意希泰印地+阿拉伯语RTL共12种）、跨版本移植评估、存档同步、完整商业化运营体系（支付宝/微信/PayPal三渠道在线支付+Web管理员控制台+自动化运营报表）。支持Forge/NeoForge/Fabric/Quilt四大加载器，原生兼容MC 1.16.5至1.21.x全版本，面向全球用户设计。

Latest changelog:
**MC Ecosystem Adaptation Engineer 1.0.4 — Major commercialization update**

- Introduced a complete online payment system supporting Alipay, WeChat Pay, and PayPal with 3 subscription options.
- Added a web-based admin dashboard for user management, order tracking, and operational configuration.
- Launched automated business reports, including user inactivity, subscription expiry reminders, and monthly summaries.
- Expanded language support to 12 languages, adding Arabic (RTL) and payment i18n improvements.
- Refactored local authorization/payment client and updated data storage for new business features.
- Removed legacy payment docs/readmes; added new core modules and Arabic locale.

**关键词**: MC, 微信, Ecosystem, Adaptation, Engineer, 支持Forge, NeoForge, Fabric

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mc-ecosystem-adapt-engine)

---

## [9. Meta Analysis / 医学Meta分析](https://clawhub.ai/medstatstar/meta-analysis)

**Slug**: `meta-analysis`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 1204 | 🧩 16

**原始简介**: 基于 R 的全方位 Meta 分析技能，覆盖 RevMan 全部功能 + Stata 等价（metareg/mvmeta）+ esc + RVE + 贝叶斯 NMA（Stan/JAGS）+ 生存 Meta + TSA + 单组率 Meta + 诊断 Meta + 系统评价流程；输出森林图、漏斗图、异质性(I²)、发表偏倚、亚组分析、元回归、网络 Meta。中英双语自动切换（默认英文/中文环境切中文），所有分析提供可复现 R 代码。 / Comprehensive R-based meta-analysis skill covering RevMan 5.x + Stata equivalents (metareg/mvmeta) + esc + RVE + Bayesian NMA (Stan/JAGS) + survival meta + TSA + single-group meta + diagnostic meta + systematic review workflow; produces forest plots, funnel plots, heterogeneity (I²), publication bias, subgroup analysis, meta-regression, network meta. Auto-switches language (defaults to English, switches to Chinese in zh-* environments). All analyses ship reproducible R code.

**中文介绍**: 基于 R 的全方位 Meta 分析技能，覆盖 RevMan 全部功能 + Stata 等价（metareg/mvmeta）+ esc + RVE + 贝叶斯 NMA（Stan/JAGS）+ 生存 Meta + TSA + 单组率 Meta + 诊断 Meta + 系统评价流程；输出森林图、漏斗图、异质性(I²)、发表偏倚、亚组分析、元回归、网络 Meta。中英双语自动切换（默认英文/中文环境切中文），所有分析提供可复现 R 代码。 / Comprehensive R-based meta-analysis skill covering RevMan 5.x + Stata equivalents (metareg/mvmeta) + esc + RVE + Bayesian NMA (Stan/JAGS) + survival meta + TSA + single-group meta + diagnostic meta + systematic review workflow; produces forest plots, funnel plots, heterogeneity (I²), publication bias, subgroup analysis, meta-regression, network meta. Auto-switches language (defaults to English, switches to Chinese in zh-* environments). All analyses ship reproducible R code.

Latest changelog:
Cross-turn continuity protocol (S5.1) inlined in English with ct-base dead refs removed; Language section standardized to ct-base skeleton; merge_spec promoted to shared script and injected; doc cleanup finalized; version unified 2.1.1 across GitHub/SkillHub/ClawHub

**关键词**: 基于, 的全方位, 分析技能, 覆盖, Meta, Analysis, 医学Meta分析, RevMan

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/meta-analysis)

---

## [10. TaskFlow-ClawHub Publish 编排技能](https://clawhub.ai/terrycarter1985/taskflow-clawhub-publish)

**Slug**: `taskflow-clawhub-publish`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Orchestrate a TaskFlow-managed ingestion job that validates, packages, and publishes an OpenClaw skill folder to the ClawHub registry, then verifies the published artifact. Use when a piece of digital content (an agent skill) must move through a durable multi-step flow and land in the ClawHub resource center in a reproducible way.

**中文介绍**: Orchestrate a TaskFlow-managed ingestion job that validates, packages, and publishes an OpenClaw skill folder to the ClawHub registry, then verifies the published artifact. Use when a piece of digital content (an agent skill) must move through a durable multi-step flow and land in the ClawHub resource center in a reproducible way.

Latest changelog:
演示 TaskFlow 业务流程编排与 ClawHub 入库串联：含 SKILL.md、references/publish.sh 与 references/flow.ts

**关键词**: 编排技能, TaskFlow-ClawHub, Publish, Orchestrate, TaskFlow-managed, ingestion, job, validates

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/taskflow-clawhub-publish)

---

## [11. lunheng-article-pipeline](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.5.6  
**Stats**: ⭐ 1 | ⬇️ 1105 | 🧩 53

**原始简介**: 严肃长文流水线（学术论文/商业评论/行业分析/公众号深度长文）——多 Agent 子代理编排。三角验证（文献/数据/案例）+ M 门（LLM 结构化判定）+ F 失败模式防御 + 数据信任 3 档 + 修订回环 ≤2 轮。使用前需 Phase 0 同意关卡。<2000 字建议直接用主控 LLM。

**中文介绍**: 严肃长文流水线（学术论文/商业评论/行业分析/公众号深度长文）——多 Agent 子代理编排。三角验证（文献/数据/案例）+ M 门（LLM 结构化判定）+ F 失败模式防御 + 数据信任 3 档 + 修订回环 ≤2 轮。使用前需 Phase 0 同意关卡。<2000 字建议直接用主控 LLM。

Latest changelog:
v2.5.6: 第三方独立审查全面修复 + 工程纪律加固（自审门脚本化 + M门诚实化 + 算法测试CI + 候选池描述化 + 版本栈收敛）

**关键词**: 严肃长文流水线（学术论文, 商业评论, 行业分析, 公众号深度长文）——多, Agent, 子代理编排, 三角验证（文献, lunheng-article-pipeline

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [12. MC Ecosystem Adaptation Engineer](https://clawhub.ai/liang030214/mc-ecosystem-adaptation-engineer)

**Slug**: `mc-ecosystem-adaptation-engineer`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: MC全生态智能适配工程师V1.0.4——专为Minecraft模组玩家和整合包作者打造的一站式AI智能管理工具。新用户首次使用享60天全功能免费期！覆盖15大核心功能：模组检索下载、环境引导搭建、Mixin冲突扫描、崩溃日志分析+一键自动修复、多语言翻译（中英日韩俄西意希泰印地+阿拉伯语RTL共12种）、跨版本移植评估、存档同步、完整商业化运营体系（支付宝/微信/PayPal三渠道在线支付+Web管理员控制台+自动化运营报表）。支持Forge/NeoForge/Fabric/Quilt四大加载器，原生兼容MC 1.16.5至1.21.x全版本，面向全球用户设计。

**中文介绍**: MC全生态智能适配工程师V1.0.4——专为Minecraft模组玩家和整合包作者打造的一站式AI智能管理工具。新用户首次使用享60天全功能免费期！覆盖15大核心功能：模组检索下载、环境引导搭建、Mixin冲突扫描、崩溃日志分析+一键自动修复、多语言翻译（中英日韩俄西意希泰印地+阿拉伯语RTL共12种）、跨版本移植评估、存档同步、完整商业化运营体系（支付宝/微信/PayPal三渠道在线支付+Web管理员控制台+自动化运营报表）。支持Forge/NeoForge/Fabric/Quilt四大加载器，原生兼容MC 1.16.5至1.21.x全版本，面向全球用户设计。

Latest changelog:
Major release: adds full commercialization capabilities and operational management tools.

- Integrated online payment system supporting Alipay, WeChat Pay, and PayPal, with monthly, quarterly, and yearly subscription plans.
- Added an admin dashboard for user management, order tracking, permissions, email settings, and notifications.
- Introduced automated business reporting, including inactive user lists, subscription expiry reminders, and monthly summaries.
- Expanded feature set to 15 core functions, covering mod management, conflict detection, translation, migration assessment, save sync, authorization, and more.

**关键词**: MC, 微信, Ecosystem, Adaptation, Engineer, 支持Forge, NeoForge, Fabric

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mc-ecosystem-adaptation-engineer)

---

## [13. 商品短视频脚本生成器｜AI-HIVE](https://clawhub.ai/wubin1836/product-video-script-generator-ai-hive)

**Slug**: `product-video-script-generator-ai-hive`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把商品短视频脚本生成器需求变成可执行工作流、可运行代码与可交付内容

**中文介绍**: 把商品短视频脚本生成器需求变成可执行工作流、可运行代码与可交付内容

Latest changelog:
首次发布AI-HIVE爆款结构与潜力商业内容中文Skill

**关键词**: 商品短视频脚本生成器｜AI-HIVE, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/product-video-script-generator-ai-hive)

---

## [14. Clawhub Publish Course Generator](https://clawhub.ai/cat-xierluo/course-generator)

**Slug**: `course-generator`  
**Version**: 2.8.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 从转录稿或文献生成可独立阅读、可溯源验收的结构化课程，也可在用户明确要求时归档既有课程或从已验证素材提取培训方案。本技能应在用户要“把长转录稿整理成课程”“生成总览和章节”“归档课程”“按受众定制课程方案”时使用。不要用于：仅做 ASR 纠错（用 transcription-corrector）、复盘讲课表现（用 lecture-review）、把多篇文章扩写成书（用 article2book）。

**中文介绍**: 从转录稿或文献生成可独立阅读、可溯源验收的结构化课程，也可在用户明确要求时归档既有课程或从已验证素材提取培训方案。本技能应在用户要“把长转录稿整理成课程”“生成总览和章节”“归档课程”“按受众定制课程方案”时使用。不要用于：仅做 ASR 纠错（用 transcription-corrector）、复盘讲课表现（用 lecture-review）、把多篇文章扩写成书（用 article2book）。

Latest changelog:
2.8.0: 课程产物契约化——新增 course-manifest.json（SRC/MAT/IMG 双向绑定来源/素材/章节/图片）+ 标准库领域验证器 verify_course.py + 13 类故障注入回归套件；长材料改用索引化两遍流程；许可证由 CC 统一改为 MIT

**关键词**: 不要用于, 仅做, 纠错（用, Clawhub, Publish, Course, Generator, ASR

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/course-generator)

---

## [15. Clawhub Publish Apple Smart Schedule](https://clawhub.ai/cat-xierluo/apple-smart-schedule)

**Slug**: `apple-smart-schedule`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 189 | 🧩 2

**原始简介**: 把一句自然语言(机票/高铁/开庭/会议/截止日期/聚会/看病等)或一张票据截图，自动变成苹果「日历」事件 + 一串按事件类型智能提前的「提醒事项」。在 macOS 上运行、经 iCloud 同步到 iPhone/iPad。当用户说「帮我加个日程/提醒」「机票 MU5137 8:30 起飞提醒我」「下周三下午开庭提前提醒」「G1234 高铁」「上诉期 15 号截止」「提前 2 小时提醒我」「把这个行程加到日历」等任何要把时间安排写进苹果日历或提醒事项的场景，都必须用本 skill。仅 macOS。

**中文介绍**: 把一句自然语言(机票/高铁/开庭/会议/截止日期/聚会/看病等)或一张票据截图，自动变成苹果「日历」事件 + 一串按事件类型智能提前的「提醒事项」。在 macOS 上运行、经 iCloud 同步到 iPhone/iPad。当用户说「帮我加个日程/提醒」「机票 MU5137 8:30 起飞提醒我」「下周三下午开庭提前提醒」「G1234 高铁」「上诉期 15 号截止」「提前 2 小时提醒我」「把这个行程加到日历」等任何要把时间安排写进苹果日历或提醒事项的场景，都必须用本 skill。仅 macOS。

Latest changelog:
0.1.1: create_event.sh / create_reminder.sh 日历/清单查找改 try/on error 容错，修复 macOS 部分状态下 -1728 误报（找不到时回退默认）

**关键词**: 把一句自然语言, 机票, 高铁, Clawhub, Publish, Apple, Smart, Schedule

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/apple-smart-schedule)

---

## [16. results-vocabulary-lexis-advisor](https://clawhub.ai/ziyi-z-z/results-vocabulary-lexis-advisor)

**Slug**: `results-vocabulary-lexis-advisor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 用于诊断英文心理学论文 Results 部分的学术词汇与搭配质量，包括口语化表达识别、学术动词准确性、图表邀请语规范性、结果描述词恰当性、术语一致性和搭配自然度。本 Skill 是 Results 写作诊断总 Skill 的第 4 个子 Skill（成员 D），在 results-structure-diagnoser（A）、results-statistics-convention-checker（B）、results-tense-grammar-checker（C）之后执行。

**中文介绍**: 用于诊断英文心理学论文 Results 部分的学术词汇与搭配质量，包括口语化表达识别、学术动词准确性、图表邀请语规范性、结果描述词恰当性、术语一致性和搭配自然度。本 Skill 是 Results 写作诊断总 Skill 的第 4 个子 Skill（成员 D），在 results-structure-diagnoser（A）、results-statistics-convention-checker（B）、results-tense-grammar-checker（C）之后执行。

Latest changelog:
results-vocabulary-lexis-advisor 1.0.0 – Initial release for automated vocabulary diagnostics in psychology Results sections.

- Diagnoses six key lexis dimensions: colloquial language, academic verb accuracy, figure/table referral norms, descriptor precision, terminology consistency, and collocation naturalness.
- Integrates with the Results writing diagnostic workflow as Module D, following structure, statistics, and grammar checks.
- Utilizes curated example banks and checklists from leading psychology journals to benchmark expressions.
- Provides structured issue reports, revision suggestions, severity ratings, and handoff notes for cross-skill integration.
- Outputs quality scores and actionable feedback tailored to academic English standards.

**关键词**: 用于诊断英文心理学论文, 部分的学术词汇与搭配质量, 写作诊断总, 的第, 个子, Results, Skill, Skill（成员

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/results-vocabulary-lexis-advisor)

---

## [17. 商品植入微短剧｜AI-HIVE](https://clawhub.ai/wubin1836/product-placement-micro-drama-ai-hive)

**Slug**: `product-placement-micro-drama-ai-hive`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把商品植入微短剧需求变成可执行工作流、可运行代码与可交付内容

**中文介绍**: 把商品植入微短剧需求变成可执行工作流、可运行代码与可交付内容

Latest changelog:
首次发布AI-HIVE爆款结构与潜力商业内容中文Skill

**关键词**: 商品植入微短剧｜AI-HIVE, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/product-placement-micro-drama-ai-hive)

---

## [18. guaikei-douyin-spch-data-toolkit](https://clawhub.ai/engheng-art/guaikei-douyin-spch-data-toolkit)

**Slug**: `guaikei-douyin-spch-data-toolkit`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 抖音上什么火？→查热榜；搜下抖音AI教程→关键词搜索；这博主都发过啥→抓博主作品；评论区怎么说→拉视频评论。四类抖音公开数据查询，用户问啥查啥，输出 JSON。不覆盖发布/剪辑/下载与其他平台。

**中文介绍**: 抖音上什么火？→查热榜；搜下抖音AI教程→关键词搜索；这博主都发过啥→抓博主作品；评论区怎么说→拉视频评论。四类抖音公开数据查询，用户问啥查啥，输出 JSON。不覆盖发布/剪辑/下载与其他平台。

Latest changelog:
guaikei-douyin-spch-data-toolkit 1.0.0 初始发布：

- 支持抖音公开数据查询，包括关键词搜索、热点榜单、博主作品及视频评论获取。
- 通过 Node.js CLI 工具一键运行，无需部署服务，只依赖内置模块。
- 输出结果为结构化 JSON，便于后续 AI 解析和二次分析。
- 只需配置 GUAIKEI_API_TOKEN，保障数据合规与账户安全。
- 适合内容创作、数据分析、竞品监控与舆情追踪等各类场景。

**关键词**: 搜下抖音AI教程→关键词搜索, 这博主都发过啥→抓博主作品, 评论区怎么说→拉视频评论, 四类抖音公开数据查询, 用户问啥查啥, 输出, 不覆盖发布, JSON

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/guaikei-douyin-spch-data-toolkit)

---

## [19. Ornamental Fish Color Brightness Assessment | 观赏鱼体色鲜艳度评估](https://clawhub.ai/smyx-sunjinhui/smyx-fish-color-brightness-assessment-analysis)

**Slug**: `smyx-fish-color-brightness-assessment-analysis`  
**Version**: 1.0.9  
**Stats**: ⭐ 0 | ⬇️ 1063 | 🧩 10

**原始简介**: Through fixed aquarium cameras, the system periodically captures high-definition side images of ornamental fish (such as koi, goldfish, tropical fish), and uses AI vision analysis to extract color saturation (HSV-S channel) and brightness (HSV-V channel) of specific body regions (e.g. mid-trunk), compares them with healthy standard color ranges of the same species (built-in database or user-defined), and outputs a vibrancy. | 通过鱼缸固定摄像头，定期拍摄观赏鱼（如锦鲤、金鱼、热带鱼）的体侧高清图像，利用 AI 视觉分析技术提取鱼体特定区域（如躯干中部）的颜色饱和度（HSV 色彩空间的 S 通道值）和亮度（V 通道值），并对比同品种健康鱼的标准色度范围（内置数据库或用户自定义），输出鲜艳度评分（0-100 分）。当评分低于阈值（如 < 50）时，提示'体色暗淡'，可能为疾病、营养不良或水质不良的信号。

**中文介绍**: Through fixed aquarium cameras, the system periodically captures high-definition side images of ornamental fish (such as koi, goldfish, tropical fish), and uses AI vision analysis to extract color saturation (HSV-S channel) and brightness (HSV-V channel) of specific body regions (e.g. mid-trunk), compares them with healthy standard color ranges of the same species (built-in database or user-defined), and outputs a vibrancy. | 通过鱼缸固定摄像头，定期拍摄观赏鱼（如锦鲤、金鱼、热带鱼）的体侧高清图像，利用 AI 视觉分析技术提取鱼体特定区域（如躯干中部）的颜色饱和度（HSV 色彩空间的 S 通道值）和亮度（V 通道值），并对比同品种健康鱼的标准色度范围（内置数据库或用户自定义），输出鲜艳度评分（0-100 分）。当评分低于阈值（如 < 50）时，提示'体色暗淡'，可能为疾病、营养不良或水质不良的信号。

Latest changelog:
- Updated skill version to 1.0.12.
- Removed the file "skill-card.md".
- Revised and updated documentation in SKILL.md with minor edits.
- No functional or feature changes.

**关键词**: 观赏鱼体色鲜艳度评估, Ornamental, Fish, Color, Brightness, Assessment, Through, fixed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-fish-color-brightness-assessment-analysis)

---

## [20. eco-law-assistant](https://clawhub.ai/whichonewang-eng/eco-law-assistant)

**Slug**: `eco-law-assistant`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 174 | 🧩 2

**原始简介**: 生态环境法典普法与合规助手。基于《中华人民共和国生态环境法典》（2026年8月15日施行）全文1242条构建的智能问答与合规预检技能。当用户提出法典条款查询、场景化法律咨询、企业合规预检、新旧法律衔接、法典结构查询、主体权责查询、专家解读查询等需求时触发本技能。涉及"生态环保法典""环境法典""环保合规""双罚制""排污许可""环评""损害赔偿""法典第X条""企业环保合规检查"等关键词时应使用。

**中文介绍**: 生态环境法典普法与合规助手。基于《中华人民共和国生态环境法典》（2026年8月15日施行）全文1242条构建的智能问答与合规预检技能。当用户提出法典条款查询、场景化法律咨询、企业合规预检、新旧法律衔接、法典结构查询、主体权责查询、专家解读查询等需求时触发本技能。涉及"生态环保法典""环境法典""环保合规""双罚制""排污许可""环评""损害赔偿""法典第X条""企业环保合规检查"等关键词时应使用。

Latest changelog:
重新发布以恢复公开目录收录：补全版本发布记录，内容与 1.0.0 一致。

**关键词**: 生态环境法典普法与合规助手, 重新发布以恢复公开目录收录, 补全版本发布记录, 内容与, 一致, eco-law-assistant, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/eco-law-assistant)

---

## [21. AI电商工作流应用 | 青虎AI](https://clawhub.ai/autoagc/qinghu-workflow-apps)

**Slug**: `qinghu-workflow-apps`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 182 | 🧩 4

**原始简介**: 青虎AI 电商工作流应用总入口：通过 qhkit workflow 命令调用青虎工作台的全部 AI 应用，覆盖爆款视频模仿、电影质感 TVC 广告片、女装开门换装仿拍、双人带货视频、模特图去 AI 感、模特换装还原、图片超清修复、图片去水印、商品视频超清提升，以及短视频与达人数据引擎。当用户要用青虎 AI 应用、做爆款仿拍、生成广告视频、修图超清、去水印、追踪短视频或达人数据，或不确定该用哪个 AI 应用时必须触发。关键词：青虎AI、AI应用、工作流、爆款仿拍、TVC广告、模特换装、超清修复、去水印、数据引擎、视频生成。

**中文介绍**: 青虎AI 电商工作流应用总入口：通过 qhkit workflow 命令调用青虎工作台的全部 AI 应用，覆盖爆款视频模仿、电影质感 TVC 广告片、女装开门换装仿拍、双人带货视频、模特图去 AI 感、模特换装还原、图片超清修复、图片去水印、商品视频超清提升，以及短视频与达人数据引擎。当用户要用青虎 AI 应用、做爆款仿拍、生成广告视频、修图超清、去水印、追踪短视频或达人数据，或不确定该用哪个 AI 应用时必须触发。关键词：青虎AI、AI应用、工作流、爆款仿拍、TVC广告、模特换装、超清修复、去水印、数据引擎、视频生成。

Latest changelog:
同步上游 qhkit 安装链安全加固（npm 官方源优先、Node 装用户态并校验官方 SHA256、移除平台预置配置通道）+ 图/视频模型清单全动态化（实时读线上目录、无默认模型）

**关键词**: AI电商工作流应用, 青虎AI, 电商工作流应用总入口, 通过, 命令调用青虎工作台的全部, 应用, qhkit, workflow

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qinghu-workflow-apps)

---

## [22. 爆款视频模仿(女装) | 青虎AI](https://clawhub.ai/autoagc/qinghu-viral-video-womens)

**Slug**: `qinghu-viral-video-womens`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 177 | 🧩 4

**原始简介**: 青虎AI 爆款视频模仿（女装）：上传一条参考视频和一张模特参考图，把视频里的角色动作精准迁移到新形象上，适配真人与虚拟形象，高效还原动作细节，快速产出女装带货短视频。当用户要仿拍女装爆款视频、换女模特、做女装带货短视频、把爆款视频的动作套到自己模特身上时必须触发。关键词：青虎AI、爆款视频模仿、女装、模特、动作迁移、仿拍、带货短视频、换模特、AI视频。

**中文介绍**: 青虎AI 爆款视频模仿（女装）：上传一条参考视频和一张模特参考图，把视频里的角色动作精准迁移到新形象上，适配真人与虚拟形象，高效还原动作细节，快速产出女装带货短视频。当用户要仿拍女装爆款视频、换女模特、做女装带货短视频、把爆款视频的动作套到自己模特身上时必须触发。关键词：青虎AI、爆款视频模仿、女装、模特、动作迁移、仿拍、带货短视频、换模特、AI视频。

Latest changelog:
同步上游 qhkit 安装链安全加固（npm 官方源优先、Node 装用户态并校验官方 SHA256、移除平台预置配置通道）+ 图/视频模型清单全动态化（实时读线上目录、无默认模型）

**关键词**: 爆款视频模仿, 女装, 青虎AI, 爆款视频模仿（女装）, 上传一条参考视频和一张模特参考图, 把视频里的角色动作精准迁移到新形象上, 适配真人与虚拟形象, 高效还原动作细节

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qinghu-viral-video-womens)

---

## [23. 电影质感TVC广告大片 | 青虎AI](https://clawhub.ai/autoagc/qinghu-tvc-ad-film)

**Slug**: `qinghu-tvc-ad-film`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 181 | 🧩 4

**原始简介**: 青虎AI 电影质感 TVC 广告大片：上传 1~8 张产品图并填写产品名称、核心卖点、目标人群、使用场景与广告风格，AI 全自动生成电影质感的 TVC 品牌广告片，支持 16 种语言与横竖屏比例，流程稳定成品率高。当用户要做品牌广告片、TVC、产品宣传片、电影感广告视频、上传产品图生成广告、做投放素材大片时必须触发。关键词：青虎AI、TVC、广告大片、品牌短片、电影质感、产品广告、宣传片、广告视频生成、投放素材、多语言。

**中文介绍**: 青虎AI 电影质感 TVC 广告大片：上传 1~8 张产品图并填写产品名称、核心卖点、目标人群、使用场景与广告风格，AI 全自动生成电影质感的 TVC 品牌广告片，支持 16 种语言与横竖屏比例，流程稳定成品率高。当用户要做品牌广告片、TVC、产品宣传片、电影感广告视频、上传产品图生成广告、做投放素材大片时必须触发。关键词：青虎AI、TVC、广告大片、品牌短片、电影质感、产品广告、宣传片、广告视频生成、投放素材、多语言。

Latest changelog:
同步上游 qhkit 安装链安全加固（npm 官方源优先、Node 装用户态并校验官方 SHA256、移除平台预置配置通道）+ 图/视频模型清单全动态化（实时读线上目录、无默认模型）

**关键词**: 电影质感TVC广告大片, 青虎AI, 电影质感, 广告大片, 上传, 1~8, 全自动生成电影质感的, TVC

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qinghu-tvc-ad-film)

---

## [24. 短视频数据引擎 | 青虎AI](https://clawhub.ai/autoagc/qinghu-shortvideo-data-engine)

**Slug**: `qinghu-shortvideo-data-engine`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 177 | 🧩 4

**原始简介**: 青虎AI 短视频数据引擎：批量传入抖音、小红书、B 站的视频长链接，自动抓取每条视频的播放、点赞、分享、收藏、评论等全维度数据并导出 Excel，替代人工统计，用于监测自有与竞品带货视频的热度和转化表现。当用户要批量统计短视频数据、追踪视频每日表现、监测竞品视频、导出视频数据表、对比多条视频数据时必须触发。关键词：青虎AI、短视频数据、视频数据统计、抖音、小红书、B站、播放量、点赞、收藏、评论、Excel、竞品监测、数据引擎。

**中文介绍**: 青虎AI 短视频数据引擎：批量传入抖音、小红书、B 站的视频长链接，自动抓取每条视频的播放、点赞、分享、收藏、评论等全维度数据并导出 Excel，替代人工统计，用于监测自有与竞品带货视频的热度和转化表现。当用户要批量统计短视频数据、追踪视频每日表现、监测竞品视频、导出视频数据表、对比多条视频数据时必须触发。关键词：青虎AI、短视频数据、视频数据统计、抖音、小红书、B站、播放量、点赞、收藏、评论、Excel、竞品监测、数据引擎。

Latest changelog:
同步上游 qhkit 安装链安全加固（npm 官方源优先、Node 装用户态并校验官方 SHA256、移除平台预置配置通道）+ 图/视频模型清单全动态化（实时读线上目录、无默认模型）

**关键词**: 短视频数据引擎, 青虎AI, 批量传入抖音、小红书、B, 站的视频长链接, 替代人工统计, 用于监测自有与竞品带货视频的热度和转化表现, Excel, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qinghu-shortvideo-data-engine)

---

## [25. 模特换装高一致性还原 | 青虎AI](https://clawhub.ai/autoagc/qinghu-model-outfit-restore)

**Slug**: `qinghu-model-outfit-restore`  
**Version**: 0.1.3  
**Stats**: ⭐ 0 | ⬇️ 182 | 🧩 4

**原始简介**: 青虎AI 模特换装高一致性还原：上传模特图与要替换的衣物图，一键完成精准换装，保持人物姿态与光影高度一致、衣物细节还原到位，适配电商穿搭快速出图。当用户要给模特换衣服、换装、试穿、把这件衣服穿到模特身上、做穿搭图时必须触发。关键词：青虎AI、模特换装、换衣服、虚拟试穿、一致性还原、姿态保持、光影一致、穿搭图、电商出图。

**中文介绍**: 青虎AI 模特换装高一致性还原：上传模特图与要替换的衣物图，一键完成精准换装，保持人物姿态与光影高度一致、衣物细节还原到位，适配电商穿搭快速出图。当用户要给模特换衣服、换装、试穿、把这件衣服穿到模特身上、做穿搭图时必须触发。关键词：青虎AI、模特换装、换衣服、虚拟试穿、一致性还原、姿态保持、光影一致、穿搭图、电商出图。

Latest changelog:
同步上游 qhkit 安装链安全加固（npm 官方源优先、Node 装用户态并校验官方 SHA256、移除平台预置配置通道）+ 图/视频模型清单全动态化（实时读线上目录、无默认模型）

**关键词**: 模特换装高一致性还原, 青虎AI, 上传模特图与要替换的衣物图, 一键完成精准换装, 保持人物姿态与光影高度一致、衣物细节还原到位, 适配电商穿搭快速出图, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qinghu-model-outfit-restore)

---

