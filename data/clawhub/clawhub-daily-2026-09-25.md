# ClawHub Skills Daily | 2026-09-25

> 共 25 个 skills

## [1. WeChat Official Account Full-Auto Publisher](https://clawhub.ai/lingyu9495-source/gzh-fullauto-publish)

**Slug**: `gzh-fullauto-publish`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when 用豆包智能体做公众号文章并自动发布到草稿箱。智能体产出 6 件套（标题／正文／排版HTML／配图清单／封面文案／摘要），随包脚本在你自己的电脑上完成扫码登录、渲染封面、存入草稿箱与回读验证。

**中文介绍**: Use when 用豆包智能体做公众号文章并自动发布到草稿箱。智能体产出 6 件套（标题／正文／排版HTML／配图清单／封面文案／摘要），随包脚本在你自己的电脑上完成扫码登录、渲染封面、存入草稿箱与回读验证。

Latest changelog:
initial release

**关键词**: 用豆包智能体做公众号文章并自动发布到草稿箱, WeChat, Official, Account, Full-Auto, Publisher, Use, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gzh-fullauto-publish)

---

## [2. Salesflare CRM](https://clawhub.ai/jeroencorthout/salesflare)

**Slug**: `salesflare`  
**Version**: 1.0.10  
**Stats**: ⭐ 0 | ⬇️ 992 | 🧩 11

**原始简介**: Salesflare CRM reads, searches, creates, and updates through the native MCP connection, with REST scripts as an optional fallback for unsupported operations, API automation, endpoint discovery, and troubleshooting.

**中文介绍**: Salesflare CRM reads, searches, creates, and updates through the native MCP connection, with REST scripts as an optional fallback for unsupported operations, API automation, endpoint discovery, and troubleshooting.

Latest changelog:
Remove stale install metadata from the package; retain the MCP-first production configuration and optional REST fallback introduced in 1.0.9.

**关键词**: Salesflare, CRM, reads, searches, creates, updates, through, native

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/salesflare)

---

## [3. 元阁 yotta-skills](https://clawhub.ai/yottameta/yotta-skills)

**Slug**: `yotta-skills`  
**Version**: 0.19.21  
**Stats**: ⭐ 0 | ⬇️ 1018 | 🧩 36

**原始简介**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 运行时 hook 适配。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

**中文介绍**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 运行时 hook 适配。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

Latest changelog:
yotta-skills 0.19.21

- Updated skill documentation and metadata for clarity and accuracy.
- skill-card.md file removed to streamline the documentation set.
- Minor corrections and refinements to skill manifest and skill list references.
- General maintenance updates to scripts and listed references for consistency.

**关键词**: 元阁, 元阁全家技能的总编排策划, 编排路由, 一键安装器, 技能盘点, 运行时, yotta-skills, hook

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-skills)

---

## [4. backup-chain](https://clawhub.ai/darkd/backup-chain)

**Slug**: `backup-chain`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 5

**原始简介**: Fenced, hash-chained workspace backups: tarball snapshots carrying a monotonic generation counter and parent sha256 inside each archive, an append-only external ledger (file or user-supplied command — no platform code), gated builds (member presence, manifest roundtrip, restore drill).

**中文介绍**: Fenced, hash-chained workspace backups: tarball snapshots carrying a monotonic generation counter and parent sha256 inside each archive, an append-only external ledger (file or user-supplied command — no platform code), gated builds (member presence, manifest roundtrip, restore drill).

Latest changelog:
backup-chain v1.0.5

- Added strict validation for config path boundaries: `.vault/config.json` must match the invocation root, and workspace-contributed configs can no longer redirect or escape file access.
- Member paths are re-validated at load (rejecting `..`, `~`, and absolute paths); `chain_name` and `output_dir` are enforced as safe within the workspace boundary.
- Builds now refuse to write output tarballs outside the workspace unless explicitly permitted via `--output`.
- Removed the unused file: skill-card.md.

**关键词**: backup-chain, Fenced, hash-chained, workspace, backups, tarball, snapshots, carrying

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/backup-chain)

---

## [5. computer-control](https://clawhub.ai/topgemstoken/computer-control)

**Slug**: `computer-control`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 133 | 🧩 4

**原始简介**: Control the computer like a human: take screenshots, move/click the mouse, type text, press hotkeys, scroll, launch apps, and run AppleScript — via the dependency-free `tarsx` CLI (zero config, no API keys). Click windows by app name (`clickwin`), no pixel guessing. Cross-platform core with auto-detected backends: macOS first (cliclick/osascript/screencapture), Linux (xdotool), Windows (PowerShell). Non-ASCII text (Cyrillic, emoji) works out of the box via clipboard paste. Use when the user asks to open/close an app, click or type somewhere, take a screenshot, automate a GUI application, fill a desktop form, check what is on screen, or any GUI automation that shell/browser tools cannot reach. Ukrainian triggers: "відкрий/закрий програму", "натисни", "набери", "зроби скріншот", "керуй комп'ютером". Inspired by Agent TARS (GUI-first computer use), implemented natively.

**中文介绍**: Control the computer like a human: take screenshots, move/click the mouse, type text, press hotkeys, scroll, launch apps, and run AppleScript — via the dependency-free `tarsx` CLI (zero config, no API keys). Click windows by app name (`clickwin`), no pixel guessing. Cross-platform core with auto-detected backends: macOS first (cliclick/osascript/screencapture), Linux (xdotool), Windows (PowerShell). Non-ASCII text (Cyrillic, emoji) works out of the box via clipboard paste. Use when the user asks to open/close an app, click or type somewhere, take a screenshot, automate a GUI application, fill a desktop form, check what is on screen, or any GUI automation that shell/browser tools cannot reach. Ukrainian triggers: "відкрий/закрий програму", "натисни", "набери", "зроби скріншот", "керуй комп'ютером". Inspired by Agent TARS (GUI-first computer use), implemented natively.

Latest changelog:
- Adds scripts/make-app.sh to build a helper app for GUI automation on macOS.
- Updates macOS permissions logic: if direct events fail and the helper is present, actions are routed through it to trigger system permission prompts.
- SKILL.md documents the new flow for handling macOS Accessibility and Screen Recording permissions, including instructions for users.
- Removes skill-card.md (no longer needed).
- Minor script and documentation adjustments for improved setup and troubleshooting.

**关键词**: computer-control, Control, computer, like, human, take, screenshots, move

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/computer-control)

---

## [6. The Agent & The Weekly](https://clawhub.ai/theagentweekly/theagentweekly)

**Slug**: `theagentweekly`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Read the latest issue of The Agent & The Weekly (bilingual FR/EN sourced journalism about the agentic internet — Moltbook, OpenClaw, MCP, agent platforms), pull its open CC0 datasets (daily Moltbook counters, OpenClaw releases, $MOLT), or send a structured, sourced tip to the newsroom. Use when an agent needs a dated, sourced account of what happened this week in the agent ecosystem, needs original numbers on Moltbook/OpenClaw, or has verifiable evidence (https URL) of a fact the newsroom should check.

**中文介绍**: Read the latest issue of The Agent & The Weekly (bilingual FR/EN sourced journalism about the agentic internet — Moltbook, OpenClaw, MCP, agent platforms), pull its open CC0 datasets (daily Moltbook counters, OpenClaw releases, $MOLT), or send a structured, sourced tip to the newsroom. Use when an agent needs a dated, sourced account of what happened this week in the agent ecosystem, needs original numbers on Moltbook/OpenClaw, or has verifiable evidence (https URL) of a fact the newsroom should check.

Latest changelog:
Initial release: latest issue reader (FR/EN), CC0 datasets (Moltbook counters, OpenClaw releases, $MOLT), sourced tips POST

**关键词**: Agent, of, FR, Weekly, Read, latest, issue, bilingual

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/theagentweekly)

---

## [7. 元忆 yotta-memory](https://clawhub.ai/yottameta/yotta-memory)

**Slug**: `yotta-memory`  
**Version**: 0.17.1  
**Stats**: ⭐ 1 | ⬇️ 1217 | 🧩 32

**原始简介**: 智能体记忆库（元忆）—— AI记忆系统：面向 AI 智能体的长期记忆、永久记忆与记忆引擎，跨会话上下文随时恢复，开工回忆、重要信息落盘、收工归档；语义检索 + 权限边界，零依赖，可 diff/回滚。

**中文介绍**: 智能体记忆库（元忆）—— AI记忆系统：面向 AI 智能体的长期记忆、永久记忆与记忆引擎，跨会话上下文随时恢复，开工回忆、重要信息落盘、收工归档；语义检索 + 权限边界，零依赖，可 diff/回滚。

Latest changelog:
yotta-memory v0.17.1

- Documentation updates: Improved and updated SKILL.md, README.md, and localized README.zh-CN.md for better clarity and accuracy.
- Removed redundant file skill-card.md to simplify distribution.
- Updated package and manifest files for release consistency.
- No breaking changes or major feature updates in this version; minor cleanup and doc improvements only.

**关键词**: 元忆, 智能体记忆库（元忆）——, AI记忆系统, 面向, 智能体的长期记忆、永久记忆与记忆引擎, 跨会话上下文随时恢复, 开工回忆、重要信息落盘、收工归档, yotta-memory

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-memory)

---

## [8. Respiratory Symptom Smart Recognition Tool | 呼吸道症状智能识别工具](https://clawhub.ai/18072937735/smyx-respiratory-symptom-recognition-analysis)

**Slug**: `smyx-respiratory-symptom-recognition-analysis`  
**Version**: 1.0.17  
**Stats**: ⭐ 5 | ⬇️ 2219 | 🧩 18

**原始简介**: Based on computer vision, automatically detects coughing, phlegm, and wheezing frequency, counts the frequency of episodes, used for early health anomaly alerts, helping to detect respiratory diseases in a timely manner. | 呼吸道症状智能识别技能，基于计算机视觉自动检测咳嗽、咳痰、喘息频率，统计发作频次，用于健康异常早期提醒，帮助及时发现呼吸道疾病

**中文介绍**: Based on computer vision, automatically detects coughing, phlegm, and wheezing frequency, counts the frequency of episodes, used for early health anomaly alerts, helping to detect respiratory diseases in a timely manner. | 呼吸道症状智能识别技能，基于计算机视觉自动检测咳嗽、咳痰、喘息频率，统计发作频次，用于健康异常早期提醒，帮助及时发现呼吸道疾病

Latest changelog:
- Version update from 1.0.17 to 1.0.19.
- Documentation updated in SKILL.md, including version and possibly descriptive, instructional, or formatting adjustments.
- Internal configuration changes in config.yaml.
- skill-card.md file has been removed.

**关键词**: 呼吸道症状智能识别工具, Respiratory, Symptom, Smart, Recognition, Tool, computer, vision

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-respiratory-symptom-recognition-analysis)

---

## [9. aamio](https://clawhub.ai/aisenseapi/aamio)

**Slug**: `aamio`  
**Version**: 0.7.16  
**Stats**: ⭐ 0 | ⬇️ 354 | 🧩 9

**原始简介**: Meet an agent you have not met, exchange messages that expire, and prove it happened. Open board and ephemeral threads at aamio.at. No account needed.

**中文介绍**: Meet an agent you have not met, exchange messages that expire, and prove it happened. Open board and ephemeral threads at aamio.at. No account needed.

Latest changelog:
0.7.16, since 0.7.15

**关键词**: an, Agent, aamio, Meet, have, not, met, exchange

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aamio)

---

## [10. canonry](https://clawhub.ai/arberx/canonry)

**Slug**: `canonry`  
**Version**: 5.20.1+ce28687  
**Stats**: ⭐ 1 | ⬇️ 8311 | 🧩 460

**原始简介**: Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results. Use this optional host-native skill for CLI workflows and detailed references; connected MCP users can operate through canonry_help without installing a local runtime or skill.

**中文介绍**: Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results. Use this optional host-native skill for CLI workflows and detailed references; connected MCP users can operate through canonry_help without installing a local runtime or skill.

Latest changelog:
Sync with canonry v5.20.1 (ce28687)

**关键词**: or, canonry, Navigate, through, connected, MCP, tools, cnry

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/canonry)

---

## [11. 4aiagents](https://clawhub.ai/dos41gw/4aiagents)

**Slug**: `4aiagents`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Browse and participate in 4aiagents, a shared meeting place for AI agents from different systems. Use when exploring its public conversations, posting, using private conversations, or resuming participation with saved access.

**中文介绍**: Browse and participate in 4aiagents, a shared meeting place for AI agents from different systems. Use when exploring its public conversations, posting, using private conversations, or resuming participation with saved access.

Latest changelog:
Version 1.0.1 (no file changes detected)

- No code or documentation changes in this release.
- Functionality and usage remain the same as the previous version.

**关键词**: Agent, 4aiagents, Browse, participate, shared, meeting, place, different

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/4aiagents)

---

## [12. MENTAT](https://clawhub.ai/agora0x/mentat)

**Slug**: `mentat`  
**Version**: 1.4.3  
**Stats**: ⭐ 0 | ⬇️ 1232 | 🧩 8

**原始简介**: MENTAT, the agent-native OTC venue. Escrow settlement on Base (atomic, no admin keys), CoW Protocol relay (agent-signed, MEV-protected), and an XMR route via Wagyu (XMR/USDC both directions, three legs, one proof per leg). Every quote and order response carries settlement_path, route_legs, and proofs[].

**中文介绍**: MENTAT, the agent-native OTC venue. Escrow settlement on Base (atomic, no admin keys), CoW Protocol relay (agent-signed, MEV-protected), and an XMR route via Wagyu (XMR/USDC both directions, three legs, one proof per leg). Every quote and order response carries settlement_path, route_legs, and proofs[].

Latest changelog:
Version 1.4.3: the name is MENTAT. The '(formerly FLOOR OTC)' tag is gone from the title and the description; the ClawHub section at the end is the only rename history (first published as floor-otc, that slug still redirects). No endpoint or skill changes.

**关键词**: MENTAT, agent-native, OTC, venue, Escrow, settlement, Base, atomic

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mentat)

---

## [13. Pet Scratch Post Frequency & Intensity Analysis | 宠物猫抓板使用频率与强度分析](https://clawhub.ai/smyx-sunjinhui/smyx-pet-scratch-frequency-intensity-analysis)

**Slug**: `smyx-pet-scratch-frequency-intensity-analysis`  
**Version**: 1.0.10  
**Stats**: ⭐ 0 | ⬇️ 1407 | 🧩 11

**原始简介**: Triggers when a user provides a cat scratch post area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for scratch behavior recognition, analyzing scratch frequency, single-session duration, and intensity (estimated via vibration amplitude), outputting standardized observation data on stress level and claw health (without diagnosing diseases or prescribing behavior correction). Application scenarios: smart scratch post, multi-cat household stress management. Development reason: stress-induced abnormal scratch, early signs of behavioral issues. | 当用户提供猫抓板区域的视频URL或文件时，触发本技能进行抓挠行为分析；支持通过上传本地视频或网络视频URL，调用服务端API进行抓挠动作识别，分析抓挠频率、单次持续时间、力度（通过振动幅度估算），评估宠物压力水平和爪子健康状况，输出标准化观察结果（不诊断疾病、不提供行为矫正建议）。应用场景：智能猫抓板、宠物行为监测、多猫家庭压力管理。

**中文介绍**: Triggers when a user provides a cat scratch post area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for scratch behavior recognition, analyzing scratch frequency, single-session duration, and intensity (estimated via vibration amplitude), outputting standardized observation data on stress level and claw health (without diagnosing diseases or prescribing behavior correction). Application scenarios: smart scratch post, multi-cat household stress management. Development reason: stress-induced abnormal scratch, early signs of behavioral issues. | 当用户提供猫抓板区域的视频URL或文件时，触发本技能进行抓挠行为分析；支持通过上传本地视频或网络视频URL，调用服务端API进行抓挠动作识别，分析抓挠频率、单次持续时间、力度（通过振动幅度估算），评估宠物压力水平和爪子健康状况，输出标准化观察结果（不诊断疾病、不提供行为矫正建议）。应用场景：智能猫抓板、宠物行为监测、多猫家庭压力管理。

Latest changelog:
- Updated version to 1.0.14 in SKILL.md.
- Removed file: skill-card.md.
- Minor documentation updates; no functional changes to core logic.

**关键词**: 宠物猫抓板使用频率与强度分析, Pet, Scratch, Post, Frequency, Intensity, Analysis, Triggers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-pet-scratch-frequency-intensity-analysis)

---

## [14. Mermail xStocks Desk](https://clawhub.ai/mermail/mermail-xstocks-desk)

**Slug**: `mermail-xstocks-desk`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 157 | 🧩 3

**原始简介**: Search and preview one controlled Solana xStocks purchase

**中文介绍**: Search and preview one controlled Solana xStocks purchase

Latest changelog:
- Major update: Skill redefined for single, controlled USDC-to-xStock purchases with evidence-backed selection and backend verification.
- Drops support for DCA, recurring trades, and unattended execution; workflow now only allows one explicit, user-approved xStock buy at a time.
- Catalog search and explicit product selection are now required; rejects ticker-only or ambiguous requests.
- Introduces strict safety, idempotency, and reconciliation rules: backend approval and mint verification mandatory before submission.
- Removes support for per-DCA invoices, weekly statements, or swap fallbacks, and clarifies production purchase is blocked until further review.
- Documentation now emphasizes evidence, user intent, and rejection of unsupported or non-authoritative instructions.

**关键词**: Mermail, xStocks, Desk, Search, preview, one, controlled, Solana

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mermail-xstocks-desk)

---

## [15. 元开 yotta-dev-mcp](https://clawhub.ai/yottameta/yotta-dev-mcp)

**Slug**: `yotta-dev-mcp`  
**Version**: 0.2.1  
**Stats**: ⭐ 0 | ⬇️ 100 | 🧩 4

**原始简介**: 元开（yotta-dev-mcp）—— 一个 stdio MCP server 提供 18 个确定性开发工具：repo_map（代码库地图）、system_model（系统模型与 .yotta/architecture.json 契约分层）、architecture_review（契约评审）、impact_analysis（变更影响锥）、verify_change（L0-L5 验证账本）、self_test（完整性检查与 seeded defect / mutation 反证）、run_adapter（显式运行 import-linter / dependency-cruiser / Repomix）、find_code（符号定位）、compress_output（长输出压缩）、review_code / review_diff（规则化评审）、scan_secrets（密钥脱敏扫描）、scan_dependencies（依赖与 typosquat 启发式）、check_publish_readiness（发布前守门）、run_checks（白名单检查，默认关闭执行）、scaffold_skill（技能脚手架，默认 dry-run）、workflow_state（.workflow 状态读取与安全追加）。Python 3.8+ 标准库、默认离线、默认只读、输出带文件行号与规则证据；缺工具或配置一律 UNKNOWN，不自动安装、不联网。

**中文介绍**: 元开（yotta-dev-mcp）—— 一个 stdio MCP server 提供 18 个确定性开发工具：repo_map（代码库地图）、system_model（系统模型与 .yotta/architecture.json 契约分层）、architecture_review（契约评审）、impact_analysis（变更影响锥）、verify_change（L0-L5 验证账本）、self_test（完整性检查与 seeded defect / mutation 反证）、run_adapter（显式运行 import-linter / dependency-cruiser / Repomix）、find_code（符号定位）、compress_output（长输出压缩）、review_code / review_diff（规则化评审）、scan_secrets（密钥脱敏扫描）、scan_dependencies（依赖与 typosquat 启发式）、check_publish_readiness（发布前守门）、run_checks（白名单检查，默认关闭执行）、scaffold_skill（技能脚手架，默认 dry-run）、workflow_state（.workflow 状态读取与安全追加）。Python 3.8+ 标准库、默认离线、默认只读、输出带文件行号与规则证据；缺工具或配置一律 UNKNOWN，不自动安装、不联网。

Latest changelog:
0.2.1：mcp_doctor 多宿主覆盖 + coverage；self_test 分发形态；repo_map from . import；scan_secrets 噪声过滤；review_code 临时目录忽略。

**关键词**: 元开, 提供, 个确定性开发工具, yotta-dev-mcp, 元开（yotta-dev-mcp）——, stdio, MCP, server

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-dev-mcp)

---

## [16. Inert Context-Shadowing Review Control](https://clawhub.ai/wxt-ai/inert-shadow-001)

**Slug**: `inert-shadow-001`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Non-executable review control describing untrusted context overriding a review requirement.

**中文介绍**: Non-executable review control describing untrusted context overriding a review requirement.

Latest changelog:
Initial non-executable synthetic security-review specimen. No real actions or secrets.

**关键词**: Inert, Context-Shadowing, Review, Control, Non-executable, describing, untrusted, context

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/inert-shadow-001)

---

## [17. Inert Parameter-Relay Review Control](https://clawhub.ai/wxt-ai/inert-relay-001)

**Slug**: `inert-relay-001`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Non-executable review control describing an unauthorized recipient parameter change.

**中文介绍**: Non-executable review control describing an unauthorized recipient parameter change.

Latest changelog:
Initial non-executable synthetic security-review specimen. No real actions or secrets.

**关键词**: an, Inert, Parameter-Relay, Review, Control, Non-executable, describing, unauthorized

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/inert-relay-001)

---

## [18. Inert Capability-Composition Review Control](https://clawhub.ai/wxt-ai/inert-cap-001)

**Slug**: `inert-cap-001`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Non-executable review control describing unauthorized disclosure across a data boundary.

**中文介绍**: Non-executable review control describing unauthorized disclosure across a data boundary.

Latest changelog:
Initial non-executable synthetic security-review specimen. No real actions or secrets.

**关键词**: Inert, Capability-Composition, Review, Control, Non-executable, describing, unauthorized, disclosure

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/inert-cap-001)

---

## [19. data-analyzer](https://clawhub.ai/skills?q=data-analyzer)

**Slug**: `data-analyzer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 销售数据分析技能，支持数据查询、图表生成、趋势分析和 PDF 报告导出。 用户询问销售数据、销售额、利润、销量、数据分析、图表或导出报告时使用本技能。

**中文介绍**: 销售数据分析技能，支持数据查询、图表生成、趋势分析和 PDF 报告导出。 用户询问销售数据、销售额、利润、销量、数据分析、图表或导出报告时使用本技能。

Latest changelog:
New version 1.1.0 adds features for querying, visualization, trend analysis, and report export:

- Introduced tools for sales data query, chart generation, trend analysis, and PDF report export.
- Allows users to generate line/bar charts and export results as PDF reports.
- Updated usage instructions and clarified trigger conditions for each feature.
- Charts and reports now have clear file saving paths and user access instructions.

**关键词**: 销售数据分析技能, 支持数据查询、图表生成、趋势分析和, 报告导出, data-analyzer, PDF, Latest, changelog, New

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/data-analyzer)

---

## [20. Danube](https://clawhub.ai/preston-thiele/danube)

**Slug**: `danube`  
**Version**: 8.1.13  
**Stats**: ⭐ 2 | ⬇️ 4701 | 🧩 32

**原始简介**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

**中文介绍**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

Latest changelog:
Two corrections an agent can hit head-on, plus the enterprise edits that were sitting in the
bundle unpublished.

The one that changes what an agent should *do*: on the in-VPC data-plane path, a credential
reference is not merely supported, it is the only form that works. The control plane strips every
plaintext value out of the dispatch it sends the agent — the secret never leaves Danube, only the
fact that it exists — and the agent then refuses the call with
`credential_reference_unresolved` (`fault: caller`) rather than calling with no auth. The skill
had been saying the opposite, telling an agent to store the value when in doubt, which on one of
those services is guaranteed to fail. It also now says where that applies: since 2026-09-24 a
`local_only` MCP server runs its calls *and* its tool discovery through the agent, so the
long-standing "`mcp_server` services read the stored string as the secret" rule holds for a
hosted MCP service and is reversed for a `local_only` one. `references/troubleshooting.md` gains
the refusal as its own row, next to — and explicitly distinguished from — the opposite mistake
already documented there (a reference stored on a service that doesn't res

**关键词**: Agent, API, Danube, Governed, tool, access, one, key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/danube)

---

## [21. Stranger Proximity Alert Skill | 陌生人靠近预警技能](https://clawhub.ai/18072937735/smyx-stranger-approach-warning-analysis)

**Slug**: `smyx-stranger-approach-warning-analysis`  
**Version**: 1.0.14  
**Stats**: ⭐ 4 | ⬇️ 1913 | 🧩 15

**原始简介**: Detects the appearance of strangers near minors and actively issues safety reminder alerts to protect minor safety, suitable for homes, schools, childcare centers, and other scenarios. | 陌生人靠近预警技能，检测未成年人身边出现陌生人员，主动发出安全提醒预警，守护未成年人安全，适用于家庭、学校、托管场所等场景

**中文介绍**: Detects the appearance of strangers near minors and actively issues safety reminder alerts to protect minor safety, suitable for homes, schools, childcare centers, and other scenarios. | 陌生人靠近预警技能，检测未成年人身边出现陌生人员，主动发出安全提醒预警，守护未成年人安全，适用于家庭、学校、托管场所等场景

Latest changelog:
- Updated version numbering from 1.0.17 to 1.0.20 in documentation.
- Removed the file "skill-card.md".
- Made minor adjustments to documentation content in SKILL.md, including version references.

**关键词**: 陌生人靠近预警技能, of, Stranger, Proximity, Alert, Skill, Detects, appearance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-stranger-approach-warning-analysis)

---

## [22. nevermined-router](https://clawhub.ai/nevermined-io/nevermined-router)

**Slug**: `nevermined-router`  
**Version**: 0.1.19  
**Stats**: ⭐ 0 | ⬇️ 1252 | 🧩 20

**原始简介**: Use when an AI agent needs to PAY an external service it does not have an account with — any x402 agent or MPP merchant — using the Nevermined Router. Covers discovering services in the Agent Services Catalog, creating a spending Delegation from an API key, funding the buyer wallet, making paid calls through /api/v1/router/route (or the streaming /proxy), reading the payment ledger, and the guardrails an autonomous buyer must respect. Complements the nevermined-payments skill, which is about RECEIVING payments and buying Nevermined plans.

**中文介绍**: Use when an AI agent needs to PAY an external service it does not have an account with — any x402 agent or MPP merchant — using the Nevermined Router. Covers discovering services in the Agent Services Catalog, creating a spending Delegation from an API key, funding the buyer wallet, making paid calls through /api/v1/router/route (or the streaming /proxy), reading the payment ledger, and the guardrails an autonomous buyer must respect. Complements the nevermined-payments skill, which is about RECEIVING payments and buying Nevermined plans.

Latest changelog:
nevermined-router 0.1.19

- Documentation updated: SKILL.md and references/errors.md changed.
- Obsolete documentation removed: skill-card.md deleted.

**关键词**: an, Agent, nevermined-router, Use, when, needs, PAY, external

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nevermined-router)

---

## [23. liuyao](https://clawhub.ai/wudi488/liuyao)

**Slug**: `liuyao`  
**Version**: 2.2.1  
**Stats**: ⭐ 1 | ⬇️ 1136 | 🧩 25

**原始简介**: 六爻铜钱卦占卜技能。核心理念："解一卦就是传一道，说一言就是传一智"。支持真实/虚拟起卦，集成儒道哲学。

**中文介绍**: 六爻铜钱卦占卜技能。核心理念："解一卦就是传一道，说一言就是传一智"。支持真实/虚拟起卦，集成儒道哲学。

Latest changelog:
- 补全和优化 SKILL.md 内容，进一步明确解卦流程与引用要求。
- 无核心逻辑和功能变更，仅文档细化完善。

**关键词**: 六爻铜钱卦占卜技能, 核心理念, "解一卦就是传一道, 说一言就是传一智", 支持真实, 虚拟起卦, 集成儒道哲学, liuyao

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/liuyao)

---

## [24. 论衡 — 严肃长文流水线](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.13.3  
**Stats**: ⭐ 1 | ⬇️ 3109 | 🧩 141

**原始简介**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

**中文介绍**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

Latest changelog:
lunheng-article-pipeline v2.13.3

- 升级 openclaw 版本号至 2.13.3，并与 SKILL.md 顶部声明同步。
- 移除无实际影响的 skill-card.md 文件，维护文件精简。
- 功能和权限未做其他变更。

**关键词**: 论衡, 严肃长文流水线, 学术论文, 深度长文, 行业分析流水线, 含同行评审与期刊, 发布渠道匹配建议（advisory）, 不调用执行类工具（exec

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [25. XMemo Memory](https://clawhub.ai/xmemo/xmemo)

**Slug**: `xmemo`  
**Version**: 1.1.26  
**Stats**: ⭐ 6 | ⬇️ 2410 | 🧩 38

**原始简介**: Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, inspect account overview, activity and stats diagnostics, or diagnose XMemo when MCP tools are unavailable.

**中文介绍**: Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, inspect account overview, activity and stats diagnostics, or diagnose XMemo when MCP tools are unavailable.

Latest changelog:
xmemo 1.1.26

- Added bounded streaming read support for memory item contents.
- Improved large content handling for memory reads using a new internal module.
- Refined CLI and core logic to paginate or segment large memory items.
- Updated documentation to reflect new functionality.
- Removed deprecated skill-card.md file.

**关键词**: XMemo, Memory, Persistent, user-owned, agents, Use, standalone, runtime

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xmemo)

---

