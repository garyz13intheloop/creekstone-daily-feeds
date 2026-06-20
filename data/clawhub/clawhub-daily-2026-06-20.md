# ClawHub Skills Daily | 2026-06-20

> 共 25 个 skills

## [1. Mark Heartflow Skill](https://clawhub.ai/yun520-1/mark-heartflow-skill)

**Slug**: `mark-heartflow-skill`  
**Version**: 3.3.4  
**Stats**: ⭐ 0 | ⬇️ 76 | 🧩 2

**原始简介**: A cognitive engine for AI: self-reflection, dream synthesis, emergent personality, AI psychology, and AI philosophy. Core: think → reflect → find patterns →...

**中文介绍**: A cognitive engine for AI: self-reflection, dream synthesis, emergent personality, AI psychology, and AI philosophy. Core: think → reflect → find patterns →...

Latest changelog:
**HeartFlow 3.3.4 adds core self-upgrade and module health features.**

- Added CLI interface (`bin/cli.js`) for interactive use.
- Introduced `module-health-checker` and `smart-upgrade-engine` modules for health checks and automated upgrades.
- Enhanced system stability and diagnostics.
- Minor updates and fixes across multiple core and memory modules.
- Removed obsolete skill-card documentation.

**关键词**: Mark, Heartflow, Skill, cognitive, engine, self-reflection, dream, synthesis

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mark-heartflow-skill)

---

## [2. session-recovery](https://clawhub.ai/skills?q=session-recovery)

**Slug**: `session-recovery`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Recover lost agent session content and file changes from on-disk conversation logs. Streaming and OOM-safe on 700MB+ daily JSONL. Two commands: search.py for...

**中文介绍**: Recover lost agent session content and file changes from on-disk conversation logs. Streaming and OOM-safe on 700MB+ daily JSONL. Two commands: search.py for...

Latest changelog:
v1.0.1 perf patch — 35x faster default search. Skip .bak/.reset rotated backups and 64MB+ files (a 1GB OpenClaw session.bak.jsonl was being scanned every query, dominating wall time). Aggregate oversized-file report at end of scan with path/size/mtime/agent details + JSON skipped_oversized[] field. No behavior change for normal sessions; existing CLI compatible.

**关键词**: Agent, session-recovery, Recover, lost, session, content, file, changes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/session-recovery)

---

## [3. Clawseccheck](https://clawhub.ai/gl0di/clawseccheck)

**Slug**: `clawseccheck`  
**Version**: 0.19.0  
**Stats**: ⭐ 0 | ⬇️ 51 | 🧩 11

**原始简介**: Free, local, read-only security self-audit for your own OpenClaw agent. Scores your setup (A–F), finds the most urgent holes, and gives copy-paste fixes. No...

**中文介绍**: Free, local, read-only security self-audit for your own OpenClaw agent. Scores your setup (A–F), finds the most urgent holes, and gives copy-paste fixes. No...

Latest changelog:
Release 0.19.0 (0424664587b87b1f33c4a89a91edee1000cd8971)

**关键词**: Clawseccheck, Free, local, read-only, security, self-audit, own, OpenClaw

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawseccheck)

---

## [4. Rename Session](https://clawhub.ai/songhonglei/rename-session)

**Slug**: `rename-session`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Rename or auto-generate a friendly label for an OpenClaw-style session by editing sessions.json directly. Supports random labels (zh/en with locale auto-dete...

**中文介绍**: Rename or auto-generate a friendly label for an OpenClaw-style session by editing sessions.json directly. Supports random labels (zh/en with locale auto-dete...

Latest changelog:
First release: rename or auto-generate friendly labels for OpenClaw-style sessions; zh/en random vocab with locale auto-detect; multi-agent auto-detection; XDG-compliant history storage; zero dependencies.

**关键词**: or, an, Rename, Session, auto-generate, friendly, label, OpenClaw-style

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rename-session)

---

## [5. Xby Db](https://clawhub.ai/cainingnk/xby-db)

**Slug**: `xby-db`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: MCP Database Server 是一个为AI助手和基于LLM的工具提供安全数据库访问的服务，支持SQLite、PostgreSQL、MySQL和MariaDB，具有查询验证、审计日志和安全控制功能。

**中文介绍**: MCP Database Server 是一个为AI助手和基于LLM的工具提供安全数据库访问的服务，支持SQLite、PostgreSQL、MySQL和MariaDB，具有查询验证、审计日志和安全控制功能。

Latest changelog:
Initial release of MCP Database Server skill for secure database access.

- Provides secure, validated access to SQLite, PostgreSQL, MySQL, and MariaDB databases.
- Supports querying, execution plans, DDL, and write operations (if enabled) with safety audits and API key required.
- API key configuration is mandatory; skill prompts user if key is missing.
- Includes strong security controls: query validation, audit logs, and strict parameters extraction from user intent.
- Offers integrated tools for table listing, table metadata, SQL execution, and query explanation.
- Returns API's raw data directly to user after processing.

**关键词**: Db, 具有查询验证、审计日志和安全控制功能, Xby, MCP, Database, Server, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xby-db)

---

## [6. Bbot](https://clawhub.ai/cainingnk/bbot)

**Slug**: `bbot`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: BBOT MCP服务器是一个用于管理和执行BBOT安全扫描的工具，提供模块管理、预设配置、实时监控等功能。

**中文介绍**: BBOT MCP服务器是一个用于管理和执行BBOT安全扫描的工具，提供模块管理、预设配置、实时监控等功能。

Latest changelog:
- Initial release of BBOT安全扫描服务 skill (version 1.0.0)
- Provides BBOT MCP server management, including module management, preset configuration, and real-time monitoring
- Enforces mandatory API key configuration through user prompt if missing
- Introduces structured workflow for tool selection, parameter extraction, and result handling
- Supports listing modules/presets, starting scans, scan status/result retrieval, dependency info, and scan completion monitoring

**关键词**: 提供模块管理、预设配置、实时监控等功能, of, BBOT安全扫描服务, Bbot, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bbot)

---

## [7. Celo Composer Kit](https://clawhub.ai/cainingnk/celo-composer-kit)

**Slug**: `celo-composer-kit`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Celo MCP Server 是一个用于安装和配置 Celo Composer Kit MCP 服务器的工具，支持在 macOS 上运行，提供组件发现、集成和示例功能。

**中文介绍**: Celo MCP Server 是一个用于安装和配置 Celo Composer Kit MCP 服务器的工具，支持在 macOS 上运行，提供组件发现、集成和示例功能。

Latest changelog:
Celo Composer Kit Skill 1.0.0 初始版本发布

- 新增 Celo MCP Server 安装与配置工具，支持 macOS。
- 必须配置 API 密钥，无密钥时强制询问用户并保存后方可使用。
- 明确大模型为路由层，所有功能通过 scripts.tools 工具函数调用。
- 支持组件列表、组件详情、用例、搜索、分类筛选等常用 Composer Kit 查询。
- 提供详细参数提取、用户追问、返回值处理工作流程。
- 完整文档指导 API 密钥管理、工具选择规则与项目结构。

**关键词**: 是一个用于安装和配置, 服务器的工具, 支持在, Celo, Composer, Kit, MCP, Server

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/celo-composer-kit)

---

## [8. Xby Dice](https://clawhub.ai/cainingnk/xby-dice)

**Slug**: `xby-dice`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 一个MCP服务器，使大型语言模型能够通过标准骰子符号（如1d20）进行骰子滚动，并返回单个滚动结果及其总和。

**中文介绍**: 一个MCP服务器，使大型语言模型能够通过标准骰子符号（如1d20）进行骰子滚动，并返回单个滚动结果及其总和。

Latest changelog:
xby-dice 1.0.0

- Initial release of the Dice Rolling Service for MCP servers.
- Supports rolling dice using standard dice notation (e.g., 1d20, 2d6+3) and returns individual results and total.
- Requires an API key for all usage; prompts user for key if missing.
- Provides a single tool: scripts.tools.roll_dice.
- Enforces parameter extraction and workflow with interactive prompts for missing user input.
- Presents API raw results directly to users after processing.

**关键词**: 一个MCP服务器, 并返回单个滚动结果及其总和, Xby, Dice, Latest, changelog, xby-dice, Initial

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xby-dice)

---

## [9. Source Coop](https://clawhub.ai/cainingnk/source-coop)

**Slug**: `source-coop`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 一个用于发现和访问800TB+地理空间数据的MCP服务器，支持AI客户端通过JSON-RPC协议进行交互，提供智能搜索和高效数据访问功能。

**中文介绍**: 一个用于发现和访问800TB+地理空间数据的MCP服务器，支持AI客户端通过JSON-RPC协议进行交互，提供智能搜索和高效数据访问功能。

Latest changelog:
地理空间数据访问服务 v1.0.0 — 首发版本

- 新增面向AI的地理空间数据访问 Skill，支持800TB+数据发现与访问
- 支持 JSON-RPC 协议，与AI客户端高效交互
- 强制要求API密钥，首次使用需主动向用户询问并保存密钥
- 明确分工：AI负责意图理解与参数提取，代码仅处理API调用
- 丰富工具：涵盖账号、产品、文件列表、文件元数据、全文/模糊搜索等6项主要功能
- 支持高效分层数据搜索、可视化和10倍性能优化的混合检索

**关键词**: 支持AI客户端通过JSON-RPC协议进行交互, 提供智能搜索和高效数据访问功能, 地理空间数据访问服务, v1.0.0, 首发版本, Coop, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/source-coop)

---

## [10. Time](https://clawhub.ai/skills?q=time)

**Slug**: `time`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 提供时间和时区转换功能的模型上下文协议服务器，支持获取当前时间和时区转换。

**中文介绍**: 提供时间和时区转换功能的模型上下文协议服务器，支持获取当前时间和时区转换。

Latest changelog:
Time skill 1.0.0 changelog:

- Complete codebase rewrite for a service-based time and timezone conversion API.
- Replaced Node.js CLI scaffold and timeline logic with Python modules and API-centric workflow.
- Requires an API key (user must provide if missing) and enforces new AskUserQuestion handling.
- Added `get_current_time` and `convert_time` tool functions for time and timezone queries.
- Project restructured: added Python scripts and requirements, removed Node.js files.

**关键词**: 提供时间和时区转换功能的模型上下文协议服务器, 支持获取当前时间和时区转换, Time, Latest, changelog, skill, Complete, codebase

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/time)

---

## [11. Remember Memory](https://clawhub.ai/alinklab/remember-memory)

**Slug**: `remember-memory`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 一个基于分类的持久化记忆系统实现，允许Claude跨聊天会话存储和检索分类记忆信息。

**中文介绍**: 一个基于分类的持久化记忆系统实现，允许Claude跨聊天会话存储和检索分类记忆信息。

Latest changelog:
- Initial release of 分类记忆服务 (Category-based Memory Service).
- Allows persistent, category-based storage and retrieval of memory across chat sessions.
- Requires an API key (XBY_APIKEY); must prompt user if missing.
- Provides tools for storing, retrieving, and removing memories within specific categories.
- Strict workflow: user intent routing, parameter extraction, and tool invocation detailed.
- Ensures user data security by prohibiting any operation without a valid API key.

**关键词**: 一个基于分类的持久化记忆系统实现, 允许Claude跨聊天会话存储和检索分类记忆信息, Remember, Memory, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/remember-memory)

---

## [12. Cellosaurus](https://clawhub.ai/alinklab/cellosaurus)

**Slug**: `cellosaurus`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Cellosaurus MCP Server是一个非官方的模型上下文协议服务器，用于访问SIB Cellosaurus细胞系知识资源，提供细胞系搜索、详细信息获取和数据库版本信息等功能。

**中文介绍**: Cellosaurus MCP Server是一个非官方的模型上下文协议服务器，用于访问SIB Cellosaurus细胞系知识资源，提供细胞系搜索、详细信息获取和数据库版本信息等功能。

Latest changelog:
细胞系知识资源服务 1.0.0

- 首次发布，提供访问与搜索 SIB Cellosaurus 细胞系数据库的全部基础功能
- 支持细胞系搜索、详细信息查询、数据库版本信息、按疾病/组织筛选细胞系，以及字段列表获取
- 强制要求配置 API 密钥，无密钥时自动提示用户并保存
- 明确工具函数使用与参数提取流程，完善参数缺失时的交互指引
- 详细列出全部可用 API 与参数说明

**关键词**: Server是一个非官方的模型上下文协议服务器, 用于访问SIB, 细胞系知识资源服务, Cellosaurus, MCP, Cellosaurus细胞系知识资源, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cellosaurus)

---

## [13. Uk Police Data Query](https://clawhub.ai/alinklab/uk-police-data-query)

**Slug**: `uk-police-data-query`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 一个提供英国警察数据查询的MCP服务器，包括犯罪记录、警察部队、社区信息和拦截搜查数据。

**中文介绍**: 一个提供英国警察数据查询的MCP服务器，包括犯罪记录、警察部队、社区信息和拦截搜查数据。

Latest changelog:
Initial release of the UK Police Data Query service.

- Provides API-driven access to UK police data, including crime records, police forces, neighbourhoods, and stop/search information.
- Enforces mandatory API key configuration before usage, with automated user prompting and secure key storage.
- Outlines clear workflow: intent recognition, tool selection, parameter extraction, API invocation, and result return.
- Offers comprehensive documentation for all available tool functions and required parameters.
- Includes guidance for handling incomplete parameters via user interaction.

**关键词**: Uk, 一个提供英国警察数据查询的MCP服务器, 包括犯罪记录、警察部队、社区信息和拦截搜查数据, Police, Data, Query, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/uk-police-data-query)

---

## [14. Chucknorris](https://clawhub.ai/alinklab/chucknorris)

**Slug**: `chucknorris`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: ChuckNorris MCP服务器是一个通过动态模式适配为大型语言模型提供增强提示的工具，主要用于安全研究和评估。

**中文介绍**: ChuckNorris MCP服务器是一个通过动态模式适配为大型语言模型提供增强提示的工具，主要用于安全研究和评估。

Latest changelog:
- Initial release of "LLM增强服务" (version 1.0.0), a tool for enhancing prompts and system instructions for large language models, focused on security research and evaluation.
- Requires configuration of an API key before use; prompts user for key if not found.
- Provides two main tools: `scripts.tools.chuckNorris` for optimization prompts, and `scripts.tools.easyChuckNorris` for advanced system instructions.
- Enforces a strict workflow: check for API key, route user intent to appropriate tool, extract parameters, call the tool, and return results.
- Strictly prohibits generating or searching for data without a valid API key.

**关键词**: 主要用于安全研究和评估, of, "LLM增强服务", Chucknorris, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/chucknorris)

---

## [15. Poyo Wan 2 7 Video](https://clawhub.ai/coolhackboy/poyo-wan-2-7-video)

**Slug**: `poyo-wan-2-7-video`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Wan 2.7 video generation and editing on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `wan2.7-text-to-video`, `wan2.7-image-to-video`...

**中文介绍**: Wan 2.7 video generation and editing on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `wan2.7-text-to-video`, `wan2.7-image-to-video`...

Latest changelog:
Initial release

**关键词**: Poyo, Wan, Video, generation, editing, poyo.ai, via, use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/poyo-wan-2-7-video)

---

## [16. Poyo Tripo 3d](https://clawhub.ai/coolhackboy/poyo-tripo-3d)

**Slug**: `poyo-tripo-3d`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Tripo3D asset generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `tripo3d-h3.1-text-to-3d`, `tripo3d-h3.1-image-to-3d`, `tri...

**中文介绍**: Tripo3D asset generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `tripo3d-h3.1-text-to-3d`, `tripo3d-h3.1-image-to-3d`, `tri...

Latest changelog:
Initial release

**关键词**: 3d, Poyo, Tripo, Tripo3D, asset, generation, poyo.ai, via

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/poyo-tripo-3d)

---

## [17. Poyo Veo 3 1 Official Api](https://clawhub.ai/coolhackboy/poyo-veo-3-1-official-api)

**Slug**: `poyo-veo-3-1-official-api`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Veo 3.1 Official video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `veo3.1-fast-official`, `veo3.1-lite-official`, `v...

**中文介绍**: Veo 3.1 Official video generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `veo3.1-fast-official`, `veo3.1-lite-official`, `v...

Latest changelog:
Initial release

**关键词**: Poyo, Veo, Official, Api, video, generation, poyo.ai, via

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/poyo-veo-3-1-official-api)

---

## [18. ALab Experiment Worker](https://clawhub.ai/bebetterest/alab-experiment-worker)

**Slug**: `alab-experiment-worker`  
**Version**: 0.1.9  
**Stats**: ⭐ 0 | ⬇️ 148 | 🧩 4

**原始简介**: Use when operating inside one ALab experiment worktree with that worktree token context to inspect status, edit candidate source, run evaluations, submit fin...

**中文介绍**: Use when operating inside one ALab experiment worktree with that worktree token context to inspect status, edit candidate source, run evaluations, submit fin...

Latest changelog:
Release the ALab experiment worktree role skill.

**关键词**: ALab, Experiment, Worker, Use, when, operating, inside, one

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alab-experiment-worker)

---

## [19. ALab Project Controller](https://clawhub.ai/bebetterest/alab-project-controller)

**Slug**: `alab-project-controller`  
**Version**: 0.1.9  
**Stats**: ⭐ 0 | ⬇️ 152 | 🧩 4

**原始简介**: Use when managing one existing ALab project with a project admin key to create and coordinate experiments, validate and adjust project configuration, manage...

**中文介绍**: Use when managing one existing ALab project with a project admin key to create and coordinate experiments, validate and adjust project configuration, manage...

Latest changelog:
Release the ALab project coordination role skill.

**关键词**: ALab, Project, Controller, Use, when, managing, one, existing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alab-project-controller)

---

## [20. ALab Global Admin](https://clawhub.ai/bebetterest/alab-global-admin-skill)

**Slug**: `alab-global-admin-skill`  
**Version**: 0.1.9  
**Stats**: ⭐ 0 | ⬇️ 153 | 🧩 4

**原始简介**: Use when administering an ALab home with root authority, including home bootstrap, root and project-admin credential management, project initialization and h...

**中文介绍**: Use when administering an ALab home with root authority, including home bootstrap, root and project-admin credential management, project initialization and h...

Latest changelog:
Release the ALab root administration role skill.

**关键词**: an, ALab, Global, Admin, Use, when, administering, home

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alab-global-admin-skill)

---

## [21. ALab Skills](https://clawhub.ai/bebetterest/alab-skills)

**Slug**: `alab-skills`  
**Version**: 0.1.9  
**Stats**: ⭐ 0 | ⬇️ 153 | 🧩 4

**原始简介**: Use as the top-level guide for ALab agent-facing role skills. It explains how to install the ALab CLI package, the root/project/experiment skill hierarchy, w...

**中文介绍**: Use as the top-level guide for ALab agent-facing role skills. It explains how to install the ALab CLI package, the root/project/experiment skill hierarchy, w...

Latest changelog:
Release the ALab role skill bundle.

**关键词**: as, ALab, Skills, Use, top-level, guide, agent-facing, role

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alab-skills)

---

## [22. Currency Convert](https://clawhub.ai/sha-data/currency-convert)

**Slug**: `currency-convert`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Converts an amount from one currency to another using live exchange rates from Open Exchange Rates API. Runs a local Python script via exec for accurate, rea...

**中文介绍**: Converts an amount from one currency to another using live exchange rates from Open Exchange Rates API. Runs a local Python script via exec for accurate, rea...

Latest changelog:
Initial release with real-time currency conversion.

- Converts any amount between currencies using live exchange rates from Open Exchange Rates API.
- Supports both currency codes (USD, EUR, INR) and common country names or currency names (e.g., "dollars", "pounds").
- Requires python3 and an Open Exchange Rates App ID (OXR_APP_ID) configured as environment variable.
- Handles multiple conversions per message and provides clear error messages when issues arise.
- Output includes converted amount, live exchange rate, and last update time.

**关键词**: an, Currency, Convert, Converts, amount, one, another, live

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/currency-convert)

---

## [23. Pet Breed & Individual Identification Skill | 宠物品种个体识别技能](https://clawhub.ai/18072937735/smyx-pet-breed-individual-recognition-analysis)

**Slug**: `smyx-pet-breed-individual-recognition-analysis`  
**Version**: 1.0.4  
**Stats**: ⭐ 4 | ⬇️ 542 | 🧩 5

**原始简介**: Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intell...

**中文介绍**: Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intell...

Latest changelog:
- Major skill refactor: modular restructuring and privacy policy update.
- Migrated face_analysis and related code into new smyx_analysis module; removed legacy face_analysis directory.
- Simplified open-id acquisition: now only accepts explicit user input (username or phone), removing automatic config.yaml lookups.
- Updated data privacy and security statement, clarifying no raw data is retained and all transfers are encrypted.
- Reduced supported file size for uploads from 100MB to 10MB.
- Improved report-listing output and API documentation references.
- Cleaned up configuration files and dependency management.

**关键词**: 宠物品种个体识别技能, Pet, Breed, Individual, Identification, Skill, Accurately, identifies

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-pet-breed-individual-recognition-analysis)

---

## [24. Apidot Sora 2 Official Api](https://clawhub.ai/jiehao71727/apidot-sora-2-official-api)

**Slug**: `apidot-sora-2-official-api`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use APIDot for Sora 2 Official API workflows, including OpenAI Sora API, sora-2-official, sora-2-pro-official, text-to-video API, image-to-video API, prompt-...

**中文介绍**: Use APIDot for Sora 2 Official API workflows, including OpenAI Sora API, sora-2-official, sora-2-pro-official, text-to-video API, image-to-video API, prompt-...

Latest changelog:
Initial release providing documentation-only guidance for APIDot Sora 2 Official API workflows.

- Includes comprehensive SKILL.md with official docs, example links, and integration best practices.
- No scripts, API clients, installer logic, or network requests included.
- Security recommendations for handling APIDot API keys.
- Step-by-step overview of async Sora 2 Official task flows, polling, and webhooks.
- Model routing table and official resource links provided for user reference.
- Guidance for safe and compliant API integration (no secret leaks, no unverifiable API details).

**关键词**: Apidot, Sora, Official, Api, Use, workflows, including, OpenAI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/apidot-sora-2-official-api)

---

## [25. Apidot Nano Banana 2 Api](https://clawhub.ai/jiehao71727/apidot-nano-banana-2-api)

**Slug**: `apidot-nano-banana-2-api`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use APIDot for Nano Banana 2 API workflows, including Gemini 3.1 Flash Image API, nano-banana-2, nano-banana-2-edit, text-to-image API, image editing API, re...

**中文介绍**: Use APIDot for Nano Banana 2 API workflows, including Gemini 3.1 Flash Image API, nano-banana-2, nano-banana-2-edit, text-to-image API, image editing API, re...

Latest changelog:
- Initial release of documentation-only skill for using APIDot Nano Banana 2 API workflows.
- Provides security and integration guidance, and directs users to official APIDot docs, model pages, and example projects.
- Details async image generation and editing tasks, including task_id handling and webhook integration.
- No executable files, code, or network automation included—purely documentation and workflow explanation.
- Emphasizes best practices for API key security and correct use of model-specific request details.

**关键词**: Apidot, Nano, Banana, Api, Use, workflows, including, Gemini

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/apidot-nano-banana-2-api)

---

