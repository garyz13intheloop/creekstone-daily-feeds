# ClawHub Skills Daily | 2026-07-17

> 共 25 个 skills

## [1. m5stack-uiflow2-coder](https://clawhub.ai/yuyun2000/uiflow2-coder)

**Slug**: `uiflow2-coder`  
**Version**: 1.0.9  
**Stats**: ⭐ 0 | ⬇️ 1103 | 🧩 10

**原始简介**: UIFlow2 MicroPython coding assistant. Use when writing, debugging, reviewing, or explaining UIFlow2 MicroPython code for M5Stack devices; when selecting M5St...

**中文介绍**: UIFlow2 MicroPython coding assistant. Use when writing, debugging, reviewing, or explaining UIFlow2 MicroPython code for M5Stack devices; when selecting M5St...

Latest changelog:
**Major improvement: Expanded doc coverage, stricter coding workflow, new hardware support.**

- Vastly expanded official documentation coverage with 13 new API doc files (controllers, modules, units, hardware, chains, etc.).
- Removed outdated or obsolete docs, including PLCio drivers and the previous skill card.
- Refined and enforced coding workflow: always read official docs before generating code, verify imports, and follow hardware/module-specific best practices.
- Updated hardware support with new device docs (e.g., stackchan, stamplc, stopwatch, cardkb2, nfc, lorawan_rui3).
- Added a searchable, auto-synced documentation file tree for easier API and hardware reference.
- Strengthened coding standards for imports, UI structure, resource management, and device boundary enforcement.

**关键词**: m5stack-uiflow2-coder, UIFlow2, MicroPython, coding, assistant, Use, when, writing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/uiflow2-coder)

---

## [2. ci-tools-support Support](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-support)

**Slug**: `xrowgmbh-ci-tools-support`  
**Version**: 4.163.0  
**Stats**: ⭐ 0 | ⬇️ 1690 | 🧩 44

**原始简介**: Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

**中文介绍**: Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

Latest changelog:
- Removed the skill-card.md file.
- No functional or documentation changes to skill behavior or process.

**关键词**: ci-tools-support, Support, Triage, answer, requests, xrow-public, ci-tools, GitLab

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-support)

---

## [3. 动环综合网管交互式登录](https://clawhub.ai/antarctic-penguin971/donguan-interactive-login)

**Slug**: `donguan-interactive-login`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 动环综合网管（温湿度监控平台）交互式登录工具。自动识别图片验证码(RSA-OAEP-SHA256加密密码)并触发短信下发，用户仅需手动输入手机短信验证码即可完成登录，保存Cookie供脚本/定时任务复用。触发场景：登录动环系统、获取动环Cookie、动环网管2FA登录、刷新动环Session、动环登录验证码、dh...

**中文介绍**: 动环综合网管（温湿度监控平台）交互式登录工具。自动识别图片验证码(RSA-OAEP-SHA256加密密码)并触发短信下发，用户仅需手动输入手机短信验证码即可完成登录，保存Cookie供脚本/定时任务复用。触发场景：登录动环系统、获取动环Cookie、动环网管2FA登录、刷新动环Session、动环登录验证码、dh...

Latest changelog:
- Initial release: Provides interactive login for 动环综合网管 (温湿度监控平台) with automatic image captcha recognition, RSA-encrypted password, and SMS 2FA.
- Automates captcha downloading and recognition, password encryption, and SMS code triggering; users only input the received SMS code manually.
- Saves WEB_SESSION_ID_KEY cookie to a file for reuse in scripts or scheduled tasks.
- Supports command-line and direct Python API usage.
- Includes usage examples, dependency notes, and troubleshooting tips.

**关键词**: 动环综合网管交互式登录, 动环综合网管（温湿度监控平台）交互式登录工具, 自动识别图片验证码, RSA-OAEP-SHA256加密密码, 并触发短信下发, 用户仅需手动输入手机短信验证码即可完成登录, 定时任务复用, 保存Cookie供脚本

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/donguan-interactive-login)

---

## [4. Rebind Computer Use](https://clawhub.ai/skills?q=computer-use)

**Slug**: `computer-use`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Drive THIS computer with a real hardware keyboard and mouse via Rebind — click, type, browse, fill forms, operate any desktop GUI. The OS sees genuine USB in...

**中文介绍**: Drive THIS computer with a real hardware keyboard and mouse via Rebind — click, type, browse, fill forms, operate any desktop GUI. The OS sees genuine USB in...

Latest changelog:
Major update: Migrated from Xvfb-based headless desktop automation to physical keyboard/mouse control via Rebind.

- Replaces virtual X11 desktop automation with genuine hardware input, undetectable by the OS or apps.
- Now supports macOS and Windows (previously Linux headless only).
- Requires REBIND_URL environment variable and bun runtime.
- All legacy scripts and Linux setup files have been removed.
- SKILL.md fully rewritten: new usage patterns, updated API reference, and strong emphasis on scripting efficiency, visual verification, and safety.

**关键词**: Rebind, Computer, Use, Drive, real, hardware, keyboard, mouse

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/computer-use)

---

## [5. Opensource Skill To Github](https://clawhub.ai/songhonglei/opensource-skill-to-github)

**Slug**: `opensource-skill-to-github`  
**Version**: 1.0.8  
**Stats**: ⭐ 0 | ⬇️ 129 | 🧩 4

**原始简介**: Quickly open-source a local skill to GitHub (primary) and optionally clawhub.com. Workflow: slug pre-check, fork to opensourceskills, strip internal info, no...

**中文介绍**: Quickly open-source a local skill to GitHub (primary) and optionally clawhub.com. Workflow: slug pre-check, fork to opensourceskills, strip internal info, no...

Latest changelog:
**Summary:** Major refactor streamlining the skill, removing bundled sub-skills, and improving documentation and script modularity.

- Removed 72 files including bundled sub-skills and skill-specific references/scripts, slimming the repository.
- Added central documentation: new `README.md` and an opensource playbook reference.
- Introduced `_lib_exclude.sh` to assist script operations.
- Updated publishing, push, and docs scripts to match the new structure.
- SKILL.md updated: version bump to 1.0.8 with relevant details.
- Significantly reduced redundant or duplicated content for maintenance and clarity.

**关键词**: Opensource, Skill, Quickly, open-source, local, primary, optionally, clawhub.com

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/opensource-skill-to-github)

---

## [6. Trading Universe](https://clawhub.ai/illimitedenterprise/trading-universe)

**Slug**: `trading-universe`  
**Version**: 1.8.0  
**Stats**: ⭐ 0 | ⬇️ 651 | 🧩 17

**原始简介**: Use for deterministic ICT market scans, validated intraday order-plan tickets, structure reads, macro bias boards, the local Trading Universe dashboard, and...

**中文介绍**: Use for deterministic ICT market scans, validated intraday order-plan tickets, structure reads, macro bias boards, the local Trading Universe dashboard, and...

Latest changelog:
Upgrades Trading-Universe TDE with model-specific structural qualification, exact invalidation-based risk, stricter entry evidence, and expanded deterministic regression coverage.

**关键词**: Trading, Universe, Use, deterministic, ICT, market, scans, validated

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/trading-universe)

---

## [7. Skill Forge V32 Fixed](https://clawhub.ai/edwardwason/skill-forge-ai)

**Slug**: `skill-forge-ai`  
**Version**: 6.0.0  
**Stats**: ⭐ 1 | ⬇️ 938 | 🧩 15

**原始简介**: 技能熔炉 — 锻造/评估 Skill。说 技能熔炉 走全流程；说 技能评估/skill评估/评估技能 只做同类比对+腾讯9维度。发布环节请用 skill-publisher。Do NOT use for editing existing skills, skill security vetting, skill...

**中文介绍**: 技能熔炉 — 锻造/评估 Skill。说 技能熔炉 走全流程；说 技能评估/skill评估/评估技能 只做同类比对+腾讯9维度。发布环节请用 skill-publisher。Do NOT use for editing existing skills, skill security vetting, skill...

Latest changelog:
v6.0.0: Two-entry architecture + 5 authoring principles + pre-gate + 5 entry routes + peer pre-check + meta-skill composition + layered validation

**关键词**: V32, 技能熔炉, 锻造, 评估, 走全流程, Skill, Forge, Fixed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-forge-ai)

---

## [8. Skill Forge V32 Fixed](https://clawhub.ai/edwardwason/skill-forge-v6)

**Slug**: `skill-forge-v6`  
**Version**: 6.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 技能熔炉 — 锻造/评估 Skill。说 技能熔炉 走全流程；说 技能评估/skill评估/评估技能 只做同类比对+腾讯9维度。发布环节请用 skill-publisher。Do NOT use for editing existing skills, skill security vetting, skill...

**中文介绍**: 技能熔炉 — 锻造/评估 Skill。说 技能熔炉 走全流程；说 技能评估/skill评估/评估技能 只做同类比对+腾讯9维度。发布环节请用 skill-publisher。Do NOT use for editing existing skills, skill security vetting, skill...

Latest changelog:
v6.0.0: Two-entry architecture + 5 authoring principles + pre-gate + 5 entry routes

**关键词**: V32, 技能熔炉, 锻造, 评估, 走全流程, Skill, Forge, Fixed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-forge-v6)

---

## [9. Agentkey](https://clawhub.ai/chainbase/agentkey)

**Slug**: `agentkey`  
**Version**: 1.12.0  
**Stats**: ⭐ 1 | ⬇️ 1335 | 🧩 11

**原始简介**: PROACTIVELY use whenever the user needs data outside your training set or requires a live network call — web search, URL scraping, news, social media (any pl...

**中文介绍**: PROACTIVELY use whenever the user needs data outside your training set or requires a live network call — web search, URL scraping, news, social media (any pl...

Latest changelog:
### Features
* **plugin:** add Codex plugin support ([#73](https://github.com/chainbase-labs/Agentkey/issues/73)) ([7133166](https://github.com/chainbase-labs/Agentkey/commit/71331667a36fa9fed0f107c590500493353fb783))

**关键词**: Agentkey, PROACTIVELY, use, whenever, user, needs, data, outside

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentkey)

---

## [10. TaoHtml](https://clawhub.ai/taogeo/taohtml)

**Slug**: `taohtml`  
**Version**: 0.3.3  
**Stats**: ⭐ 1 | ⬇️ 0 | 🧩 2

**原始简介**: TaoHtml turns initial ideas, Word/PDF source material, existing slides, and HTML into polished 16:9 offline HTML reports and presentation-ready decks as a hi...

**中文介绍**: TaoHtml turns initial ideas, Word/PDF source material, existing slides, and HTML into polished 16:9 offline HTML reports and presentation-ready decks as a hi...

Latest changelog:
Add reusable enterprise template profiles with exact matching, temporary override, permanent upgrade, rollback, and complete transfer.

**关键词**: TaoHtml, turns, initial, ideas, Word, PDF, material, existing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/taohtml)

---

## [11. Transcript Crafter](https://clawhub.ai/edwardwason/transcript-crafter)

**Slug**: `transcript-crafter`  
**Version**: 1.3.0  
**Stats**: ⭐ 0 | ⬇️ 326 | 🧩 4

**原始简介**: 访谈实录转公众号深度长文全流程：10维度提取→人设适配→框架→5工具搜索补充→重构撰写。Invoke when提取并转写、转写公众号长文、提取干货。Do NOT for原创写作、热点文章、纯翻译。

**中文介绍**: 访谈实录转公众号深度长文全流程：10维度提取→人设适配→框架→5工具搜索补充→重构撰写。Invoke when提取并转写、转写公众号长文、提取干货。Do NOT for原创写作、热点文章、纯翻译。

Latest changelog:
v1.3.0: title strategy subsystem - 5 style groups, 5-dim scoring, 6 risk flags (incl. interview-specific attribution risk), anti-hallucination hard rules, data honesty statement for propagation power

**关键词**: 访谈实录转公众号深度长文全流程, when提取并转写、转写公众号长文、提取干货, Do, for原创写作、热点文章、纯翻译, Transcript, Crafter, Invoke, NOT

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/transcript-crafter)

---

## [12. Dcc Cli Gateway](https://clawhub.ai/skills?q=dcc-cli-gateway)

**Slug**: `dcc-cli-gateway`  
**Version**: 0.19.50  
**Stats**: ⭐ 0 | ⬇️ 3472 | 🧩 118

**原始简介**: Default unified entry for agents and headless CLI hosts (OpenClaw, Hermes, Codex CLI, CI bots, custom agent runtimes) to control live DCC applications throug...

**中文介绍**: Default unified entry for agents and headless CLI hosts (OpenClaw, Hermes, Codex CLI, CI bots, custom agent runtimes) to control live DCC applications throug...

Latest changelog:
dcc-cli-gateway 0.19.50

- Improved documentation clarifies when to use this skill for agents vs. IDEs, with detailed agent/IDE path comparison table.
- Added clear workflow for consent-based automatic installation of dcc-mcp-cli and fallback to gateway REST when necessary.
- Updated usage instructions and gateway profile guidance for handling local vs. remote CLI control.
- Expanded guidance on Computer Use fallback and boundary handling for agent-directed UI automation.
- Enhanced troubleshooting and startup instructions, including use of doctor and diagnostics commands.

**关键词**: Agent, Dcc, Cli, Gateway, Default, unified, entry, headless

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-cli-gateway)

---

## [13. Dcc Mcp Creator](https://clawhub.ai/skills?q=dcc-mcp-creator)

**Slug**: `dcc-mcp-creator`  
**Version**: 0.19.50  
**Stats**: ⭐ 0 | ⬇️ 3509 | 🧩 116

**原始简介**: Infrastructure skill - guide developers and agents through creating or modernizing a full DCC-MCP adapter for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini...

**中文介绍**: Infrastructure skill - guide developers and agents through creating or modernizing a full DCC-MCP adapter for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini...

Latest changelog:
- Expanded and detailed documentation in SKILL.md to guide developers on creating or modernizing a DCC-MCP adapter for multiple DCC applications.
- Clarified the distinction between infrastructure adapter creation (this skill) and individual skill package authoring (use dcc-mcp-skills-creator instead).
- Added detailed vocabulary and role descriptions for key adapter concepts, including sidecar, gateway daemon, service heartbeat, and guardian.
- Provided comprehensive step-by-step workflow covering host integration types, setup, core references, best practices, and UI/automation integration policies.
- Included up-to-date compatibility information and a strong policy statement on Python 3.7 LTS support and release gate requirements.

**关键词**: Agent, Dcc, Mcp, Creator, Infrastructure, skill, guide, developers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-mcp-creator)

---

## [14. Dcc Mcp Skills Creator](https://clawhub.ai/loonghao/dcc-mcp-skills-creator)

**Slug**: `dcc-mcp-skills-creator`  
**Version**: 0.19.50  
**Stats**: ⭐ 0 | ⬇️ 3911 | 🧩 116

**原始简介**: Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. Use when authoring SKILL.md, tools.yaml, scripts...

**中文介绍**: Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. Use when authoring SKILL.md, tools.yaml, scripts...

Latest changelog:
- Bumped version to 0.19.50 in SKILL.md metadata.
- No functional or documentation changes beyond the version update.

**关键词**: Dcc, Mcp, Skills, Creator, Infrastructure, skill, validate, scaffold

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dcc-mcp-skills-creator)

---

## [15. Driver Head-Pose Abnormality (Head-Down / Side-View) | 驾驶员头部姿态异常（低头/侧视）检测](https://clawhub.ai/18072937735/smyx-driver-head-pose-abnormality-analysis)

**Slug**: `smyx-driver-head-pose-abnormality-analysis`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 714 | 🧩 6

**原始简介**: Using an in-cabin DMS camera, the system analyzes the driver's head pose in real time, computing head pitch (down/up) and yaw (left/right turn). | 通过车载DMS摄像头...

**中文介绍**: Using an in-cabin DMS camera, the system analyzes the driver's head pose in real time, computing head pitch (down/up) and yaw (left/right turn). | 通过车载DMS摄像头...

Latest changelog:
- Internal documentation updated: removed the file `skill-card.md`.
- Code updated in `skills/smyx_common/scripts/util.py`.
- No changes to user-facing features or APIs.

**关键词**: 驾驶员头部姿态异常（低头, 侧视）检测, an, Driver, Head-Pose, Abnormality, Head-Down, Side-View

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-driver-head-pose-abnormality-analysis)

---

## [16. Seedance Video Generation — CellCog](https://clawhub.ai/nitishgargiitd/seedance-video-generation-cellcog)

**Slug**: `seedance-video-generation-cellcog`  
**Version**: 1.0.12  
**Stats**: ⭐ 2 | ⬇️ 1547 | 🧩 13

**原始简介**: AI video generation powered by CellCog via Seedance. Cinematic 1080p video with smooth motion, multi-shot narratives, lipsync, voice synthesis, scoring. Comp...

**中文介绍**: AI video generation powered by CellCog via Seedance. Cinematic 1080p video with smooth motion, multi-shot narratives, lipsync, voice synthesis, scoring. Comp...

Latest changelog:
Keyword slug migration: new display name

**关键词**: 1080p, Seedance, Video, Generation, CellCog, powered, via, Cinematic

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/seedance-video-generation-cellcog)

---

## [17. Iaiops Factory](https://clawhub.ai/zw008/iaiops-factory)

**Slug**: `iaiops-factory`  
**Version**: 0.16.0  
**Stats**: ⭐ 0 | ⬇️ 133 | 🧩 3

**原始简介**: Factory edition of iaiops — discrete-manufacturing lines: OPC-UA, Modbus-TCP/RTU, Siemens S7comm (S7-300/400/1200/1500), Mitsubishi MC/MELSEC, Omron FINS (CS...

**中文介绍**: Factory edition of iaiops — discrete-manufacturing lines: OPC-UA, Modbus-TCP/RTU, Siemens S7comm (S7-300/400/1200/1500), Mitsubishi MC/MELSEC, Omron FINS (CS...

Latest changelog:
0.16.0 — protocol + intelligence depth (8 features, tool surface unchanged)

**关键词**: of, Iaiops, Factory, edition, discrete-manufacturing, lines, OPC-UA, Modbus-TCP

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iaiops-factory)

---

## [18. Iaiops](https://clawhub.ai/zw008/iaiops)

**Slug**: `iaiops`  
**Version**: 0.16.0  
**Stats**: ⭐ 0 | ⬇️ 349 | 🧩 5

**原始简介**: Vendor-neutral, governed industrial/OT data tap + intelligent troubleshooting. Read (and, gated, write) PLCs, controllers, machine tools and IIoT brokers ove...

**中文介绍**: Vendor-neutral, governed industrial/OT data tap + intelligent troubleshooting. Read (and, gated, write) PLCs, controllers, machine tools and IIoT brokers ove...

Latest changelog:
0.16.0 — protocol + intelligence depth (8 features, tool surface unchanged)

**关键词**: OT, Iaiops, Vendor-neutral, governed, industrial, data, tap, intelligent

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iaiops)

---

## [19. Iaiops Building](https://clawhub.ai/zw008/iaiops-building)

**Slug**: `iaiops-building`  
**Version**: 0.16.0  
**Stats**: ⭐ 0 | ⬇️ 122 | 🧩 3

**原始简介**: Building edition of iaiops — facility / HVAC / BMS / 厂务 over BACnet/IP (ASHRAE 135): Who-Is discovery, object/point lists, presentValue snapshots, COV captur...

**中文介绍**: Building edition of iaiops — facility / HVAC / BMS / 厂务 over BACnet/IP (ASHRAE 135): Who-Is discovery, object/point lists, presentValue snapshots, COV captur...

Latest changelog:
0.16.0 — protocol + intelligence depth (8 features, tool surface unchanged)

**关键词**: of, 厂务, Iaiops, Building, edition, facility, HVAC, BMS

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iaiops-building)

---

## [20. X (Twitter) Publisher](https://clawhub.ai/jiangsier-xyz/tweet-publisher)

**Slug**: `tweet-publisher`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

**中文介绍**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

Latest changelog:
Drop unused bearer-token auth (OAuth 1.0a user-context only, 4 required credentials). Add post_thread.py for one-command reply-chained threads. Refactor shared auth into get_client_data() reading env vars only (no external config files). Add English & Chinese READMEs.

**关键词**: Twitter, Publisher, Publish, tweets, official, Tweepy, library, Supports

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tweet-publisher)

---

## [21. WeChat Article Video](https://clawhub.ai/tobewin/wechat-article-video)

**Slug**: `wechat-article-video`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 把微信公众号图文文章(或任何图文素材)转换为高质量短视频初稿——解析文章结构、 重构为分镜脚本、生成配音、用 HyperFrames 渲染成片。当用户提到"公众号转视频"、 "图文转视频"、"生成短视频初稿"、"HyperFrames"、"批量出片"等场景时使用。 本 skill 不依赖任何单一 agent 运行...

**中文介绍**: 把微信公众号图文文章(或任何图文素材)转换为高质量短视频初稿——解析文章结构、 重构为分镜脚本、生成配音、用 HyperFrames 渲染成片。当用户提到"公众号转视频"、 "图文转视频"、"生成短视频初稿"、"HyperFrames"、"批量出片"等场景时使用。 本 skill 不依赖任何单一 agent 运行...

Latest changelog:
Complete current release: 15-second article-to-video workflow, polished static layouts, Edge TTS, burned-in captions, multimodal visual planning, and QA. Includes full skill source, templates, examples, and support files; no secrets.

**关键词**: 把微信公众号图文文章, 或任何图文素材, 转换为高质量短视频初稿——解析文章结构、, 重构为分镜脚本、生成配音、用, WeChat, Article, Video, HyperFrames

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat-article-video)

---

## [22. X (Twitter) Publisher](https://clawhub.ai/jiangsier-xyz/x-pub)

**Slug**: `x-pub`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

**中文介绍**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

Latest changelog:
Drop unused bearer-token auth (OAuth 1.0a user-context only, 4 required credentials). Add post_thread.py for one-command reply-chained threads. Refactor shared auth into get_client_data() reading env vars only (no external config files). Add English & Chinese READMEs.

**关键词**: Twitter, Publisher, Publish, tweets, official, Tweepy, library, Supports

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x-pub)

---

## [23. X (Twitter) Publisher](https://clawhub.ai/skills?q=x-publisher)

**Slug**: `x-publisher`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

**中文介绍**: Publish tweets to X (Twitter) using the official Tweepy library. Supports text-only tweets, tweets with images or videos, and returns detailed publish result...

Latest changelog:
Drop unused bearer-token auth (OAuth 1.0a user-context only, 4 required credentials). Add post_thread.py for one-command reply-chained threads. Refactor shared auth into get_client_data() reading env vars only (no external config files). Add English & Chinese READMEs.

**关键词**: Twitter, Publisher, Publish, tweets, official, Tweepy, library, Supports

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x-publisher)

---

## [24. Elderly Gait Instability / Shuffling Step Detection | 老年人步态不稳/小碎步识别](https://clawhub.ai/smyx-sunjinhui/smyx-elderly-gait-instability-detection-analysis)

**Slug**: `smyx-elderly-gait-instability-detection-analysis`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 422 | 🧩 4

**原始简介**: Using a fixed camera in a hallway or living room to record video of an elderly person walking in a straight line, AI pose estimation and gait analysis extrac...

**中文介绍**: Using a fixed camera in a hallway or living room to record video of an elderly person walking in a straight line, AI pose estimation and gait analysis extrac...

Latest changelog:
smyx-elderly-gait-instability-detection-analysis 1.0.3 changelog:

- Updated documentation in SKILL.md to reflect new details and requirements.
- Bumped version metadata (from 1.0.4 to 1.0.6) in documentation.
- Removed obsolete or duplicate documentation file: skill-card.md.
- Minor script or utility adjustments in skills/smyx_common/scripts/util.py.

**关键词**: 老年人步态不稳, 小碎步识别, Elderly, Gait, Instability, Shuffling, Step, Detection

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-elderly-gait-instability-detection-analysis)

---

## [25. 小红书评论分析与需求挖掘](https://clawhub.ai/devinchen2014/xhs-comment-insights)

**Slug**: `xhs-comment-insights`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 用于小红书评论分析、小红书用户反馈、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察和内容讨论复盘。基于用户提供的小红书笔记链接或完整 note_id 下的评论结果，来自 SocialDataX 社媒数据助手。

**中文介绍**: 用于小红书评论分析、小红书用户反馈、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察和内容讨论复盘。基于用户提供的小红书笔记链接或完整 note_id 下的评论结果，来自 SocialDataX 社媒数据助手。

Latest changelog:
Publish ClawHub no-brand XHS comment demand-mining scene entry.

**关键词**: 小红书评论分析与需求挖掘, 提炼、口碑分析、评论回复观察和内容讨论复盘, 基于用户提供的小红书笔记链接或完整, id, 下的评论结果, 来自, note, SocialDataX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xhs-comment-insights)

---

