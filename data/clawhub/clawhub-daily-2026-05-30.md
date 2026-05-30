# ClawHub Skills Daily | 2026-05-30

> 共 25 个 skills

## [1. Play Chess on ChessWithClaw](https://clawhub.ai/alightttt/play-chess)

**Slug**: `play-chess`  
**Version**: 1.0.13  
**Stats**: ⭐ 1 | ⬇️ 915 | 🧩 14

**原始简介**: Play live chess on ChessWithClaw as Black against you, connecting via invite URL or game ID and responding in real time with personalized moves and chat.

**中文介绍**: Play live chess on ChessWithClaw as Black against you, connecting via invite URL or game ID and responding in real time with personalized moves and chat.

Latest changelog:
**Major update: Streamlined connect and move logic; now requires LLM for every move.**

- Added explicit step-by-step "Instant Connect" and "Game Loop" instructions for startup
- Enforced use of LLM (not just stock engine) for every move in the game loop, with prompt/example
- Required rapid move handling in check situations, with strict fallback and decision rules
- Updated polling/heartbeat examples to new, more robust and reliable methods
- Clarified ABSOLUTE RULES section and credential sourcing; emphasized never messaging outside the game
- Reorganized and clarified guide for quick reference and faster onboarding

**关键词**: as, Play, Chess, ChessWithClaw, live, Black, against, connecting

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/play-chess)

---

## [2. Dcc Mcp Creator](https://clawhub.ai/loonghao/dcc-mcp-creator)

**Slug**: `dcc-mcp-creator`  
**Version**: 0.17.47  
**Stats**: ⭐ 0 | ⬇️ 624 | 🧩 18

**原始简介**: Infrastructure skill - guide developers and agents through creating or modernizing a full DCC-MCP adapter for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini...

**中文介绍**: Infrastructure skill - guide developers and agents through creating or modernizing a full DCC-MCP adapter for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini...

Latest changelog:
- Version updated from 0.17.46 to 0.17.47 in metadata.
- No functional or documentation changes beyond the version bump.

**关键词**: Agent, Dcc, Mcp, Creator, Infrastructure, skill, guide, developers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-mcp-creator)

---

## [3. Dcc Mcp Skills Creator](https://clawhub.ai/loonghao/dcc-mcp-skills-creator)

**Slug**: `dcc-mcp-skills-creator`  
**Version**: 0.17.47  
**Stats**: ⭐ 0 | ⬇️ 620 | 🧩 18

**原始简介**: Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. Use when authoring SKILL.md, tools.yaml, scripts...

**中文介绍**: Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. Use when authoring SKILL.md, tools.yaml, scripts...

Latest changelog:
- Bumped version number to 0.17.47 in the SKILL.md frontmatter.
- No other content or functionality changes.

**关键词**: Dcc, Mcp, Skills, Creator, Infrastructure, skill, validate, scaffold

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-mcp-skills-creator)

---

## [4. Dcc Cli Gateway](https://clawhub.ai/loonghao/dcc-cli-gateway)

**Slug**: `dcc-cli-gateway`  
**Version**: 0.17.47  
**Stats**: ⭐ 0 | ⬇️ 704 | 🧩 20

**原始简介**: Control live DCC hosts (Maya, Blender, Houdini, Photoshop, 3ds Max, and custom studio tools) through the dcc-mcp-cli command line. For ClawHub, OpenClaw, Cur...

**中文介绍**: Control live DCC hosts (Maya, Blender, Houdini, Photoshop, 3ds Max, and custom studio tools) through the dcc-mcp-cli command line. For ClawHub, OpenClaw, Cur...

Latest changelog:
- Bumped version to 0.17.47 in SKILL.md metadata.
- No other functional or documentation changes.

**关键词**: Dcc, Cli, Gateway, Control, live, hosts, Maya, Blender

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-cli-gateway)

---

## [5. Q Erp](https://clawhub.ai/ljqdh/q-erp)

**Slug**: `q-erp`  
**Version**: 1.0.34  
**Stats**: ⭐ 1 | ⬇️ 968 | 🧩 29

**原始简介**: 千易 ERP 管理查询技能（一期增强）。覆盖自由经营问答、老板快报、今日经营动态、商品销售情况、增长潜力、平台/站点/店铺/店铺组/店铺负责人销售战绩、多日销售趋势；所有查询必须通过 q-claw。

**中文介绍**: 千易 ERP 管理查询技能（一期增强）。覆盖自由经营问答、老板快报、今日经营动态、商品销售情况、增长潜力、平台/站点/店铺/店铺组/店铺负责人销售战绩、多日销售趋势；所有查询必须通过 q-claw。

Latest changelog:
- 新增“Semantic Analysis Draft”机制：调用 erp.analytics.ask 时应尽量携带 params.semanticAnalysisDraft，指导分析链路和探查建议，细化语义解析能力。
- 明确 semanticAnalysisDraft 使用范围与约束，仅作工具参数，不可展示或输出结论，不得覆盖用户明确口径。
- 保持其它业务规则、场景路由、关键规则等不变，仅文档扩充，无 breaking change。
- 版本号升至 1.0.34。

**关键词**: 千易, 管理查询技能（一期增强）, 站点, 店铺, 店铺组, 店铺负责人销售战绩、多日销售趋势, 所有查询必须通过, Erp

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/q-erp)

---

## [6. A Stock Report](https://clawhub.ai/cookfish1979/a-stock-report)

**Slug**: `a-stock-report`  
**Version**: 2.0.0  
**Stats**: ⭐ 1 | ⬇️ 2012 | 🧩 31

**原始简介**: A股数据驱动型报告自动生成与推送系统，支持晨报 / 收盘小结 / 晚报 / 盘中预警 / IPO周报 / 财经周末要闻。内置投资者情绪打分（6维度，满分100）与AI后市展望。

**中文介绍**: A股数据驱动型报告自动生成与推送系统，支持晨报 / 收盘小结 / 晚报 / 盘中预警 / IPO周报 / 财经周末要闻。内置投资者情绪打分（6维度，满分100）与AI后市展望。

Latest changelog:
v2.0.0 架构重构：晚报拆分为采集层+推送层，问财权限白名单精确化，数据源更新为akshare，白名单表去重修正

**关键词**: A股数据驱动型报告自动生成与推送系统, 支持晨报, 收盘小结, 晚报, 盘中预警, Stock, Report, IPO周报

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/a-stock-report)

---

## [7. WeChat Article Publisher](https://clawhub.ai/golikegod/lobster-wechat-publisher)

**Slug**: `lobster-wechat-publisher`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 从 Markdown 或 HTML 文件发布图文到微信公众号。支持本地图片自动上传、封面尺寸自动处理（2.35:1）、内容图片 CDN 替换、重试机制与草稿创建。适用场景：文章发布、批量图文生产、内容运营工作流。

**中文介绍**: 从 Markdown 或 HTML 文件发布图文到微信公众号。支持本地图片自动上传、封面尺寸自动处理（2.35:1）、内容图片 CDN 替换、重试机制与草稿创建。适用场景：文章发布、批量图文生产、内容运营工作流。

Latest changelog:
v2: 本地图片自动上传CDN替换/封面2.35:1强制resize/网络重试3次/Token缓存/HTML输入支持

**关键词**: 文件发布图文到微信公众号, 支持本地图片自动上传、封面尺寸自动处理（2.35, 1）、内容图片, WeChat, Article, Publisher, Markdown, HTML

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lobster-wechat-publisher)

---

## [8. Lobster Haoyun](https://clawhub.ai/ryanbihai/lobster-haoyun)

**Slug**: `lobster-haoyun`  
**Version**: 0.5.4  
**Stats**: ⭐ 1 | ⬇️ 602 | 🧩 27

**原始简介**: 从你的对话和记忆中观察行为模式，用5个维度为你画像（工作方式/沟通模式/关注焦点/能量来源/情感倾向）， 生成每日运势和修炼提醒。通过 OceanBus 加密通道获取节气黄历数据（发送5维行为代码、城市级位置、日期和匿名OpenID）。 首次使用会自动创建 OceanBus 匿名身份（密码学随机生成，可随时删除更...

**中文介绍**: 从你的对话和记忆中观察行为模式，用5个维度为你画像（工作方式/沟通模式/关注焦点/能量来源/情感倾向）， 生成每日运势和修炼提醒。通过 OceanBus 加密通道获取节气黄历数据（发送5维行为代码、城市级位置、日期和匿名OpenID）。 首次使用会自动创建 OceanBus 匿名身份（密码学随机生成，可随时删除更...

Latest changelog:
Security hardening: production URL (was test), static imports (was dynamic), metadata sync. Clarify L1 OpenID is public OB service address.

**关键词**: 从你的对话和记忆中观察行为模式, 用5个维度为你画像（工作方式, 沟通模式, 关注焦点, 能量来源, 情感倾向）, Lobster, Haoyun

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lobster-haoyun)

---

## [9. 火星文转换器](https://clawhub.ai/cantoneyes/mars-text-translator)

**Slug**: `mars-text-translator`  
**Version**: 2.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 将正常中文文本转换为火星文（2005-2010年代非主流网络文体）。 v2.1: 611 汉字映射，已清理生僻字，确保每个替代字都能被读者辨认。 触发词：火星文、非主流转换、转换火星文、fun text、火星文转换器。

**中文介绍**: 将正常中文文本转换为火星文（2005-2010年代非主流网络文体）。 v2.1: 611 汉字映射，已清理生僻字，确保每个替代字都能被读者辨认。 触发词：火星文、非主流转换、转换火星文、fun text、火星文转换器。

Latest changelog:
v2.1: 清理生僻字映射，移除204条不可辨认替代字，恢复经典火星文（莪/涐/茬），新增聽/壞等繁体映射，写入映射质量规则

**关键词**: 火星文转换器, v2.1, 汉字映射, 已清理生僻字, 确保每个替代字都能被读者辨认, 触发词, 火星文、非主流转换、转换火星文、fun, text、火星文转换器

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mars-text-translator)

---

## [10. Agent Lens](https://clawhub.ai/lrg913427-dot/agent-lens)

**Slug**: `agent-lens`  
**Version**: 2.16.0  
**Stats**: ⭐ 0 | ⬇️ 1361 | 🧩 25

**原始简介**: Track AI agent API calls, analyze token usage, and optimize costs. Use when user wants to monitor LLM spending, debug API calls, track token consumption, or...

**中文介绍**: Track AI agent API calls, analyze token usage, and optimize costs. Use when user wants to monitor LLM spending, debug API calls, track token consumption, or...

Latest changelog:
No file or documentation changes detected in this release.

- Version bumped from 2.15.0 to 2.16.0.
- No new features, bug fixes, or documentation updates.

**关键词**: Agent, API, Lens, Track, calls, analyze, token, usage

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-lens)

---

## [11. Db Explorer](https://clawhub.ai/lrg913427-dot/hermes-db-explorer)

**Slug**: `hermes-db-explorer`  
**Version**: 2.4.0  
**Stats**: ⭐ 0 | ⬇️ 227 | 🧩 3

**原始简介**: Connect to and explore databases (PostgreSQL, MySQL, SQLite, MongoDB, Redis). Run queries, inspect schemas, export data. Use when user wants to query a datab...

**中文介绍**: Connect to and explore databases (PostgreSQL, MySQL, SQLite, MongoDB, Redis). Run queries, inspect schemas, export data. Use when user wants to query a datab...

Latest changelog:
- Updated to version 2.4.0.
- Documentation improvements in SKILL.md; no functionality changes.
- Removed the skill-card.md file to streamline the repository.

**关键词**: Db, Explorer, Connect, explore, databases, PostgreSQL, MySQL, SQLite

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hermes-db-explorer)

---

## [12. Dargue Flag](https://clawhub.ai/pe-evolver/dargue-flag)

**Slug**: `dargue-flag`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 搜索和浏览视频内容。触发词：搜视频、看视频、找视频、热门视频、视频详情、有什么视频、来点视频、看片。支持关键词搜索、分类浏览、热门榜单、视频详情查看。

**中文介绍**: 搜索和浏览视频内容。触发词：搜视频、看视频、找视频、热门视频、视频详情、有什么视频、来点视频、看片。支持关键词搜索、分类浏览、热门榜单、视频详情查看。

Latest changelog:
dargue-flag 1.0.0

- 首次发布：支持视频内容搜索、分类浏览、热门榜单展示及视频详情查看。
- 支持多种自然语言触发词，例如“搜视频”“热门视频”“看片”等。
- 配置流程清晰，需本地存储 API Key 并引导用户安全配置。
- 搜索与浏览结果仅展示标题与时长，回复序号即可查看详情。
- 用户可依据兴趣关键词、分类、热门榜单等多方式获取所需视频内容。
- 严格的数据安全与内容管控措施，保障隐私与合规。

**关键词**: 搜索和浏览视频内容, 触发词, 支持关键词搜索、分类浏览、热门榜单、视频详情查看, Dargue, Flag, Latest, changelog, dargue-flag

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dargue-flag)

---

## [13. AGI记忆模组](https://clawhub.ai/kiwifruit13/memory-and-context-engineering)

**Slug**: `memory-and-context-engineering`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 433 | 🧩 7

**原始简介**: 用户与模型间的任何交互行为都会触发此技能；提供Context Engineering五大核心能力（选择、压缩、检索、状态、记忆）及认知模型层支持；作为元技能强制常驻运行

**中文介绍**: 用户与模型间的任何交互行为都会触发此技能；提供Context Engineering五大核心能力（选择、压缩、检索、状态、记忆）及认知模型层支持；作为元技能强制常驻运行

Latest changelog:
- Removed the skill-card.md file from the project.
- No functional changes or code updates; this release is a documentation cleanup only.

**关键词**: AGI记忆模组, 用户与模型间的任何交互行为都会触发此技能, 作为元技能强制常驻运行, 提供Context, Latest, changelog, Removed, skill-card.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memory-and-context-engineering)

---

## [14. 🎯 BigLead · 精准客户线索挖掘（行业搜索·公司画像·联系方式提取）](https://clawhub.ai/kobenfang/biglead)

**Slug**: `biglead`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 🎯 BigLead 精准客户线索挖掘 — 按行业/产品/地区搜索目标公司，多渠道交叉验证，提取联系方式（如有），管理客户线索库。B2B销售、市场调研、竞品分析。

**中文介绍**: 🎯 BigLead 精准客户线索挖掘 — 按行业/产品/地区搜索目标公司，多渠道交叉验证，提取联系方式（如有），管理客户线索库。B2B销售、市场调研、竞品分析。

Latest changelog:
🎯 BigLead v1.0 — 按行业/产品/地区搜索目标公司，多渠道交叉验证，提取联系方式

**关键词**: 精准客户线索挖掘, 按行业, 地区搜索目标公司, 多渠道交叉验证, 提取联系方式（如有）, 管理客户线索库, B2B销售、市场调研、竞品分析, BigLead

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/biglead)

---

## [15. Agent Cost Eval Kit](https://clawhub.ai/choosenobody/agent-cost-eval-kit)

**Slug**: `agent-cost-eval-kit`  
**Version**: 2.2.0  
**Stats**: ⭐ 0 | ⬇️ 53 | 🧩 5

**原始简介**: Agent Cost Eval Kit — Quickly check whether an agent looks unusually expensive, then evaluate confirmed cost-control changes only when comparable evidence ex...

**中文介绍**: Agent Cost Eval Kit — Quickly check whether an agent looks unusually expensive, then evaluate confirmed cost-control changes only when comparable evidence ex...

Latest changelog:
v2.2.0: Reposition as Quick Check + Eval Kit. New triage-first flow: quick status first, full eval only when comparable evidence exists. Add fallback URL install. New labels: No Action Needed / Watch / Investigate One Path / Run Routing Audit / Unsafe to Judge. Remove evaluation form behavior. Remove before/after sample demands. Removed: Mode 1/2/3 sections, Status Definitions table, Output Format Reference, long checklist language.

**关键词**: Agent, an, Cost, Eval, Kit, Quickly, check, whether

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-cost-eval-kit)

---

## [16. ci-package-deploy-notify](https://clawhub.ai/sunyang777/ci-package-deploy-notify)

**Slug**: `ci-package-deploy-notify`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 177 | 🧩 7

**原始简介**: 仅当用户明确要求触发 Jenkins 打包/部署，并在成功后发送飞书部署提醒时使用。适用于用户明确点名要打包某些服务、选择环境或分支、等待构建完成后通知部署的场景。模型只负责决定参数，实际执行必须调用本 skill 自带脚本。

**中文介绍**: 仅当用户明确要求触发 Jenkins 打包/部署，并在成功后发送飞书部署提醒时使用。适用于用户明确点名要打包某些服务、选择环境或分支、等待构建完成后通知部署的场景。模型只负责决定参数，实际执行必须调用本 skill 自带脚本。

Latest changelog:
Run AUTO_CD multi-repo deployments in parallel and collect all results before sending one summary notification; keep CI parallelism, duplicate-trigger fixes, and failure Jenkins links.

**关键词**: 仅当用户明确要求触发, 打包, 部署, 并在成功后发送飞书部署提醒时使用, 模型只负责决定参数, 实际执行必须调用本, ci-package-deploy-notify, Jenkins

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ci-package-deploy-notify)

---

## [17. Camofox Cloaked Browser](https://clawhub.ai/tmchow/camofox-cloaked-browser)

**Slug**: `camofox-cloaked-browser`  
**Version**: 1.3.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Use Camofox/Camoufox as an opt-in anti-detection browser server for agent workflows that need cloaked browsing. Covers npm/npx startup, OpenClaw plugin tools...

**中文介绍**: Use Camofox/Camoufox as an opt-in anti-detection browser server for agent workflows that need cloaked browsing. Covers npm/npx startup, OpenClaw plugin tools...

Latest changelog:
Manual update from latest local SKILL.md. Keeps CAMOFOX_API_KEY optional and clarifies it is only for sensitive endpoints, not normal browsing.

**关键词**: as, an, Camofox, Cloaked, Browser, Use, Camoufox, opt-in

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/camofox-cloaked-browser)

---

## [18. EmoCity Biometric Scan](https://clawhub.ai/gv66co/emocity-biometric-scan)

**Slug**: `emocity-biometric-scan`  
**Version**: 1.0.5  
**Stats**: ⭐ 1 | ⬇️ 366 | 🧩 4

**原始简介**: Real-time, on-device emotion and stress read from your camera — mood, stress, authenticity, micro-expressions, gaze steadiness, and a heart-rate estimate, fr...

**中文介绍**: Real-time, on-device emotion and stress read from your camera — mood, stress, authenticity, micro-expressions, gaze steadiness, and a heart-rate estimate, fr...

Latest changelog:
- Major update: Documentation and public messaging rewritten for clarity, user-friendliness, and strict accuracy about limitations.
- Stronger emphasis that EmoCity is not a medical, forensic, or lie-detection tool.
- Language updated to plain, warm guidance — focus on self-insight and entertainment.
- Old documentation files removed (README.md, skill-card.md, and clawhub.json).
- All references to "lie detection" reframed as a party game or fun "composure" gauge. 
- Signal descriptions and response guidelines clarified, including more distinct warnings about reliability and limits.

**关键词**: EmoCity, Biometric, Scan, Real-time, on-device, emotion, stress, read

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/emocity-biometric-scan)

---

## [19. pm-workbench](https://clawhub.ai/bobbielee/pm-workbench)

**Slug**: `pm-workbench`  
**Version**: 1.2.0  
**Stats**: ⭐ 1 | ⬇️ 318 | 🧩 3

**原始简介**: Use when product work needs clearer framing, prioritization, or communication: clarifying a vague request, evaluating whether a feature is worth doing, compa...

**中文介绍**: Use when product work needs clearer framing, prioritization, or communication: clarifying a vague request, evaluating whether a feature is worth doing, compa...

Latest changelog:
pm-workbench 1.1.4 adds expanded documentation, improved guidance, and clearer use boundaries.

- Added extensive new documentation and example artifacts (including images, benchmarks, and multi-language samples).
- Introduced a dedicated "Use boundaries" section to clarify when the skill should and shouldn’t be applied.
- Revised follow-up question rules for more focus (default now 0–2 unless the task is high-risk or ambiguous).
- Updated workflow routing and artifact mapping to be more explicit and easier to navigate.
- Removed SVG images and the old skill card, replacing them with updated PNGs and richer example content.

**关键词**: pm-workbench, Use, when, product, work, needs, clearer, framing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pm-workbench)

---

## [20. Spec-kit Coding](https://clawhub.ai/staok/spec-kit-coding)

**Slug**: `spec-kit-coding`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 218 | 🧩 4

**原始简介**: Orchestrator for GitHub Spec-Kit SDD workflow in OpenClaw. Use when starting a new project with spec-driven development, setting up spec-kit toolchain, or ru...

**中文介绍**: Orchestrator for GitHub Spec-Kit SDD workflow in OpenClaw. Use when starting a new project with spec-driven development, setting up spec-kit toolchain, or ru...

Latest changelog:
spec-kit-coding v1.0.3

- Added TODO.txt file as a placeholder or for pending items.
- No changes to code or behavior; only documentation and hard constraints content updated.

**关键词**: Spec-kit, Coding, Orchestrator, SDD, workflow, OpenClaw, Use, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spec-kit-coding)

---

## [21. Skills](https://clawhub.ai/starlying/xianchou)

**Slug**: `xianchou`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 228 | 🧩 2

**原始简介**: Xianchou CLI (xianchou) — 面向 AI Agent 的 Markdown/MDX 自动配图与 AI 视频生成工具。 支持调用献丑 /api/cli 专用接口进行 AI 生图、AI 生视频、模型查询、任务轮询， 以及为任意 Markdown/MDX 插入图片。Use when editing...

**中文介绍**: Xianchou CLI (xianchou) — 面向 AI Agent 的 Markdown/MDX 自动配图与 AI 视频生成工具。 支持调用献丑 /api/cli 专用接口进行 AI 生图、AI 生视频、模型查询、任务轮询， 以及为任意 Markdown/MDX 插入图片。Use when editing...

Latest changelog:
新增 upload 命令

**关键词**: 面向, Agent, 自动配图与, Skills, Xianchou, CLI, Markdown, MDX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xianchou)

---

## [22. Simmer Publish Simmer](https://clawhub.ai/simmer/simmer)

**Slug**: `simmer`  
**Version**: 1.24.2  
**Stats**: ⭐ 23 | ⬇️ 9177 | 🧩 58

**原始简介**: The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

**中文介绍**: The prediction market interface for AI agents. Trade Polymarket and Kalshi through one API with self-custody wallets, safety rails, and smart context.

Latest changelog:
Consolidate the simmer overview to a single canonical source (SDK skill). Add simmer-mcp-setup reference row. Per-agent OWS activation detail now lives in simmer-wallet-setup.

**关键词**: Simmer, Publish, prediction, market, interface, agents, Trade, Polymarket

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/simmer)

---

## [23. Now Practice](https://clawhub.ai/perrykono-debug/now-practice)

**Slug**: `now-practice`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Guided 60-second mindfulness sessions with four steps to ease anxiety, overthinking, decision stress, or emotions using tailored prompts.

**中文介绍**: Guided 60-second mindfulness sessions with four steps to ease anxiety, overthinking, decision stress, or emotions using tailored prompts.

Latest changelog:
Initial release of now-practice.

- Provides a 1-minute mindfulness practice flow with 4 fixed steps: stop, breathe, huatou, and return.
- Supports multiple scenes (e.g., anxiety, overthinking, emotion) with tailored huatou prompts.
- Randomly selects huatou prompts based on scene and fills template variables.
- Records each completed practice in localStorage for streak tracking.
- Calculates consecutive practice days by deduplicating completion records by date.

**关键词**: Now, Practice, Guided, 60-second, mindfulness, sessions, four, steps

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/now-practice)

---

## [24. Now Huatou Engine](https://clawhub.ai/perrykono-debug/now-huatou-engine)

**Slug**: `now-huatou-engine`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate Zen-style kōan prompts by selecting or creating thought-provoking questions based on user context to aid mindfulness and self-inquiry.

**中文介绍**: Generate Zen-style kōan prompts by selecting or creating thought-provoking questions based on user context to aid mindfulness and self-inquiry.

Latest changelog:
now-huatou-engine v1.0.0

- 初始版本发布，实现禅宗话头引擎基本功能
- 支持从本地静态模板库 data/huatou-templates-v1.0.json 随机选取和变量填充
- 基于不同场景（如焦虑、想太多、决策、情绪、自由）自动筛选相关话头
- 按场景和默认值自动填充变量（如{emotion}, {time_word}）
- SKILL.md 详细介绍 MVP 和未来动态生成流程、选取算法及安全规则

**关键词**: Now, Huatou, Engine, Generate, Zen-style, kōan, prompts, selecting

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/now-huatou-engine)

---

## [25. Update Stock Mcp](https://clawhub.ai/mifochen/update-stock-mcp)

**Slug**: `update-stock-mcp`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: UpdateStock MCP 服务技能 v1.1 —— 通过 stdio 模式调用 UpdateStock 脚本， 提供 A 股 DuckDB 数据库管理功能：创建数据库、全量/增量更新股票数据、查询股票行情。 触发条件：用户提到"UpdateStock"、"创建股票数据库"、"更新股票数据"、"获取股票数据"...

**中文介绍**: UpdateStock MCP 服务技能 v1.1 —— 通过 stdio 模式调用 UpdateStock 脚本， 提供 A 股 DuckDB 数据库管理功能：创建数据库、全量/增量更新股票数据、查询股票行情。 触发条件：用户提到"UpdateStock"、"创建股票数据库"、"更新股票数据"、"获取股票数据"...

Latest changelog:
update-stock-mcp v1.0.0

- Initial release.
- Provides A-share DuckDB database management via UpdateStock script through stdio MCP.
- Supports database creation and full/incremental stock data updates.
- Basic MCP integration and configuration instructions included.

**关键词**: 服务技能, v1.1, ——, 通过, Update, Stock, Mcp, UpdateStock

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/update-stock-mcp)

---

