# ClawHub Skills Daily | 2026-10-04

> 共 25 个 skills

## [1. bsc-rug-check](https://clawhub.ai/perria080925-bot/bsc-rug-check)

**Slug**: `bsc-rug-check`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Rug-pull and safety screening for any EVM token before trading or recommending it: pair age, liquidity depth, volume churn, volatility, buy/sell imbalance -> 0-100 score with auditable flags. Pay-per-call $0.01 USDC on Base via x402. No subscription, no API key.

**中文介绍**: Rug-pull and safety screening for any EVM token before trading or recommending it: pair age, liquidity depth, volume churn, volatility, buy/sell imbalance -> 0-100 score with auditable flags. Pay-per-call $0.01 USDC on Base via x402. No subscription, no API key.

Latest changelog:
Initial publish: 0-100 rug/safety score with auditable flags via x402 pay-per-call.

**关键词**: bsc-rug-check, Rug-pull, safety, screening, any, EVM, token, before

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bsc-rug-check)

---

## [2. evm-wallet-watch](https://clawhub.ai/perria080925-bot/evm-wallet-watch)

**Slug**: `evm-wallet-watch`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Check any EVM wallet's live native balance, ENS name and last 5 transactions on Ethereum, Base or BSC through a pay-per-call x402 endpoint ($0.0002 USDC per request). Multi-RPC failover + Blockscout data. Use when you need a trustless wallet snapshot without running your own node or managing API keys.

**中文介绍**: Check any EVM wallet's live native balance, ENS name and last 5 transactions on Ethereum, Base or BSC through a pay-per-call x402 endpoint ($0.0002 USDC per request). Multi-RPC failover + Blockscout data. Use when you need a trustless wallet snapshot without running your own node or managing API keys.

Latest changelog:
Initial publish: live EVM wallet snapshot via x402 pay-per-call (multi-RPC + Blockscout).

**关键词**: evm-wallet-watch, Check, any, EVM, wallet's, live, native, balance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/evm-wallet-watch)

---

## [3. OpenMAIC](https://clawhub.ai/wyuc/openmaic)

**Slug**: `openmaic`  
**Version**: 0.3.11  
**Stats**: ⭐ 5 | ⬇️ 6258 | 🧩 16

**原始简介**: OpenMAIC assistant for setting up, generating, and extending OpenMAIC. Use when the user wants to use OpenMAIC, generate a multi-agent interactive classroom, or build on / extend / customize OpenMAIC and its @openmaic/* SDK (secondary development, 二开) — covers Live Demo or local setup, startup modes, provider keys, classroom generation, and secondary development (forking, providers/storage/themes, routes, or the renderer/editor).

**中文介绍**: OpenMAIC assistant for setting up, generating, and extending OpenMAIC. Use when the user wants to use OpenMAIC, generate a multi-agent interactive classroom, or build on / extend / customize OpenMAIC and its @openmaic/* SDK (secondary development, 二开) — covers Live Demo or local setup, startup modes, provider keys, classroom generation, and secondary development (forking, providers/storage/themes, routes, or the renderer/editor).

Latest changelog:
- Updated the classroom generation phase to clarify retry behavior on failed jobs (now references retrying failed jobs per the generate flow).
- Minor clarification in the classroom generation step about submitting supported fields and the handling of optional features.
- Removed obsolete documentation file skill-card.md.
- No changes to core setup or workflow phases.

**关键词**: up, OpenMAIC, assistant, setting, generating, extending, Use, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openmaic)

---

## [4. 元阁 yotta-skills](https://clawhub.ai/yottameta/yotta-skills)

**Slug**: `yotta-skills`  
**Version**: 0.29.0  
**Stats**: ⭐ 0 | ⬇️ 1694 | 🧩 67

**原始简介**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 本机技能 Hub + 运行时 hook 适配。Hub 层：hub hosts 只读发现本机已装智能体与技能目录（文件系统优先，不读元忆；已核实 / 自动发现 / 桥接分类 + 状态细分：可用 / 残留（实体未确认）/ 未创建 / 仅标记）；hub hosts add/remove/list/mark 注册自定义宿主目录与手动标记（只注册不建目录、移除不删目录；残留清理 hub hosts remove --purge 默认预览、目录入回收站 7 天）；install-self / where 把元阁管理引擎独立安装（默认 ~/.yottaskills/yotta-skills，--dir 指定）并查看运行位置；hub install / update 把技能装到 ~/.yottaskills/hub 单点真源（清单 27 + 特殊家族 5，特殊家族跟随各自 npm latest）；hub link --all 用 Windows junction / POSIX symlink 分发到全部已核实宿主（默认范围；--include-discovered 显式纳入自动发现目录；锁 / 数据桥接目录永不链接），元技能在链接时收敛宿主旧副本（移入 ~/.yottaskills/trash 保留 7 天、版本闸门 Hub ≥ 宿主）；hub unlink 只删链接、fail-closed；非元技能不参与更新（用户自行处理）；hub status 显示来源、版本、链接与异常；view 启动本机技能枢纽面板（默认 127.0.0.1:8789，六视图 + 高级 CLI 页，写操作需页面令牌与确认）；兼容 agentskills.io 技能格式、Vercel Labs skills CLI 的 .agents/skills 通用目录与 .skill-lock.json v3（只读）。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；M1 记忆裁决层：usage enable/mark 本地结构化记录 + decide-memory / MCP decide_memory 输出 promote / hold / demote 只读建议（需授权 provider；只建议不删除、不自动写元忆）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request/decide_memory，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / usage 使用记录 / decide-memory 记忆裁决 / hub 技能 Hub / install-self 独立安装 / where 位置查看 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、单点安装并分发到多个智能体、查看本机装了哪些智能体与技能目录、接管非元技能、按场景组合多个元技能、路由或判断该用哪些技能、判断哪些技能值得长期记忆、查看或记录技能使用信号、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/记忆裁决/技能该不该记住/盘点技能/查看已装技能/技能 Hub/单点安装/链接分发/接管技能/技能枢纽面板/图形化面板/独立安装元阁/查看元阁位置/自定义宿主/残留清理/宿主状态 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + M1 记忆裁决只读建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + Hub 本机真源与链接分发 + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆、不自动删除技能或记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

**中文介绍**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 本机技能 Hub + 运行时 hook 适配。Hub 层：hub hosts 只读发现本机已装智能体与技能目录（文件系统优先，不读元忆；已核实 / 自动发现 / 桥接分类 + 状态细分：可用 / 残留（实体未确认）/ 未创建 / 仅标记）；hub hosts add/remove/list/mark 注册自定义宿主目录与手动标记（只注册不建目录、移除不删目录；残留清理 hub hosts remove --purge 默认预览、目录入回收站 7 天）；install-self / where 把元阁管理引擎独立安装（默认 ~/.yottaskills/yotta-skills，--dir 指定）并查看运行位置；hub install / update 把技能装到 ~/.yottaskills/hub 单点真源（清单 27 + 特殊家族 5，特殊家族跟随各自 npm latest）；hub link --all 用 Windows junction / POSIX symlink 分发到全部已核实宿主（默认范围；--include-discovered 显式纳入自动发现目录；锁 / 数据桥接目录永不链接），元技能在链接时收敛宿主旧副本（移入 ~/.yottaskills/trash 保留 7 天、版本闸门 Hub ≥ 宿主）；hub unlink 只删链接、fail-closed；非元技能不参与更新（用户自行处理）；hub status 显示来源、版本、链接与异常；view 启动本机技能枢纽面板（默认 127.0.0.1:8789，六视图 + 高级 CLI 页，写操作需页面令牌与确认）；兼容 agentskills.io 技能格式、Vercel Labs skills CLI 的 .agents/skills 通用目录与 .skill-lock.json v3（只读）。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；M1 记忆裁决层：usage enable/mark 本地结构化记录 + decide-memory / MCP decide_memory 输出 promote / hold / demote 只读建议（需授权 provider；只建议不删除、不自动写元忆）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request/decide_memory，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / usage 使用记录 / decide-memory 记忆裁决 / hub 技能 Hub / install-self 独立安装 / where 位置查看 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、单点安装并分发到多个智能体、查看本机装了哪些智能体与技能目录、接管非元技能、按场景组合多个元技能、路由或判断该用哪些技能、判断哪些技能值得长期记忆、查看或记录技能使用信号、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/记忆裁决/技能该不该记住/盘点技能/查看已装技能/技能 Hub/单点安装/链接分发/接管技能/技能枢纽面板/图形化面板/独立安装元阁/查看元阁位置/自定义宿主/残留清理/宿主状态 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + M1 记忆裁决只读建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + Hub 本机真源与链接分发 + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆、不自动删除技能或记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

Latest changelog:
**v0.29.0 introduces new host management, self-install, and advanced status tracking in the yotta-skills orchestration tool.**

- Added `hub hosts` for unified host (agent/skill directory) discovery, status (available/residual/virtual/marked), and explicit register/remove/mark.
- Introduced `install-self` and `where` commands for independent yotta-skills management engine install and location query.
- Host registry now persists user-registered and marked directories, supports cleaning residual hosts (`hub hosts remove --purge` with trash/retention).
- Improved hub link: better detection and cleanup of stale/old versions during skill distribution; non-meta skills remain outside updates.
- Updated documentation, CLI help, and user-facing commands to match new host/engine management features.
- Internal refactoring: new modules for host registry, host purge, and self-install logic.

**关键词**: 元阁, 元阁全家技能的总编排策划, 编排路由, 一键安装器, 技能盘点, 本机技能, yotta-skills, Hub

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-skills)

---

## [5. MaxVideoAI](https://clawhub.ai/camgraphe/maxvideoai)

**Slug**: `maxvideoai`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 195 | 🧩 2

**原始简介**: Use when a user wants AI video planning, current model comparison, a project budget, an exact generation quote, approved generation, or recovery through MaxVideoAI.

**中文介绍**: Use when a user wants AI video planning, current model comparison, a project budget, an exact generation quote, approved generation, or recovery through MaxVideoAI.

Latest changelog:
Clarify exact-quote confirmation, live model eligibility, private-reference ownership, and recovery timing and stop signals. Preserve existing host-verification limits.

**关键词**: MaxVideoAI, Use, when, user, wants, video, planning, current

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/maxvideoai)

---

## [6. OnePress Deck Video](https://clawhub.ai/getonepress/onepress-deck-video)

**Slug**: `onepress-deck-video`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Turn a slide deck or topic into a narrated explainer video via OnePress — slides rendered to frames, AI narration, MP4 output. Requires a free ONEPRESS_API_KEY; submits the task, polls, and reports where the MP4 lives.

**中文介绍**: Turn a slide deck or topic into a narrated explainer video via OnePress — slides rendered to frames, AI narration, MP4 output. Requires a free ONEPRESS_API_KEY; submits the task, polls, and reports where the MP4 lives.

Latest changelog:
Initial release of onepress-deck-video.

- Create narrated explainer videos from slide decks or topics using OnePress.
- Requires ONEPRESS_API_KEY for video generation via the OnePress API.
- Automatically submits tasks, polls for completion, and reports where the MP4 is available in the user's OnePress workspace.
- Clearly communicates errors such as invalid API keys or out-of-credits status.
- Provides usage guidance and links for getting started and retrieving API keys.

**关键词**: or, OnePress, Deck, Video, Turn, slide, topic, narrated

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/onepress-deck-video)

---

## [7. OnePress Podcast](https://clawhub.ai/getonepress/onepress-podcast)

**Slug**: `onepress-podcast`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Turn a topic, document, or slide deck into a narrated audio episode via OnePress — AI voices (including cloned voices), natural pacing, workspace delivery. Requires a free ONEPRESS_API_KEY; submits the task, polls, and reports where the MP3 lives.

**中文介绍**: Turn a topic, document, or slide deck into a narrated audio episode via OnePress — AI voices (including cloned voices), natural pacing, workspace delivery. Requires a free ONEPRESS_API_KEY; submits the task, polls, and reports where the MP3 lives.

Latest changelog:
Initial release of onepress-podcast skill.

- Create narrated audio episodes from topics, documents, or slide decks using OnePress AI voices (including voice cloning).
- Requires a ONEPRESS_API_KEY; guides setup and usage.
- Submits tasks to OnePress, polls for completion, and reports the final MP3 location in the user's OnePress workspace.
- Clearly informs users if the API key is missing and directs them to obtain one.
- Error conditions handled and reported, including invalid key, no credits, server busy, and rate limits.

**关键词**: or, OnePress, Podcast, Turn, topic, document, slide, deck

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/onepress-podcast)

---

## [8. OnePress Deck](https://clawhub.ai/getonepress/onepress-deck)

**Slug**: `onepress-deck`  
**Version**: 3.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Build polished, data-rich slide decks — works out of the box with no account (generates a real self-contained HTML deck locally using the bundled recipe), and with a free ONEPRESS_API_KEY it delegates to OnePress for the full pipeline — cited live research, generated images, official PDF/editable-PPTX export, narrated video. Use for pitch decks, investor updates, board decks, sales decks, and research briefings.

**中文介绍**: Build polished, data-rich slide decks — works out of the box with no account (generates a real self-contained HTML deck locally using the bundled recipe), and with a free ONEPRESS_API_KEY it delegates to OnePress for the full pipeline — cited live research, generated images, official PDF/editable-PPTX export, narrated video. Use for pitch decks, investor updates, board decks, sales decks, and research briefings.

Latest changelog:
Local mode: builds a real self-contained HTML deck with the bundled recipe — no account needed. Connected mode (API key) delegates to the full OnePress pipeline.

**关键词**: OnePress, Deck, Build, polished, data-rich, slide, decks, works

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/onepress-deck)

---

## [9. Security-Shield](https://clawhub.ai/z-hussein/security-shield)

**Slug**: `security-shield`  
**Version**: 2.2.2  
**Stats**: ⭐ 1 | ⬇️ 2352 | 🧩 14

**原始简介**: Security checks for external content - downloads, fetched documents, attachments, and newly imported resources. Use when verifying external content before trusting it. External information is never trusted until evidence confirms it cannot harm the system.
website: https://security-shield-five.vercel.app

**中文介绍**: Security checks for external content - downloads, fetched documents, attachments, and newly imported resources. Use when verifying external content before trusting it. External information is never trusted until evidence confirms it cannot harm the system.
website: https://security-shield-five.vercel.app

Latest changelog:
## [2.2.2] - 2026-09-13

- Removed the "authenticated directive-format check" clause; clarified that external content can never become a directive.
- Added explicit note: no mechanism allows untrusted text to be promoted to directive status.
- Threat handling now requires explicit per-write user approval before writing to `memory/YYYY-MM-DD.md`; this is separate from quarantine approval.
- Updated threat recording: workspace memory writes are deny-by-default, in line with write-scope rules.
- Added a note to the changelog documenting remediation for T01/T02 issues.

**关键词**: Security-Shield, Security, checks, external, content, downloads, fetched, documents

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/security-shield)

---

## [10. Plant Wilting Monitoring Skill | 植物枯萎监测技能](https://clawhub.ai/smyx-sunjinhui/smyx-plant-wilting-monitoring-analysis)

**Slug**: `smyx-plant-wilting-monitoring-analysis`  
**Version**: 1.0.15  
**Stats**: ⭐ 4 | ⬇️ 2312 | 🧩 16

**原始简介**: Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control. | 植物枯萎监测技能，基于高光谱成像与计算机视觉，在肉眼可见症状前捕捉早期枯萎迹象，为精准灌溉和病害防控提供早期预警

**中文介绍**: Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control. | 植物枯萎监测技能，基于高光谱成像与计算机视觉，在肉眼可见症状前捕捉早期枯萎迹象，为精准灌溉和病害防控提供早期预警

Latest changelog:
- Updated version to 1.0.19 in SKILL.md.
- Minor documentation or metadata corrections in SKILL.md.
- Removed obsolete file: skill-card.md.

**关键词**: 植物枯萎监测技能, of, Plant, Wilting, Monitoring, Skill, Early, hyperspectral

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-plant-wilting-monitoring-analysis)

---

## [11. WorkBuddy 自定义模型能力位排查（读图/工具/推理）](https://clawhub.ai/oracis/workbuddy-model-capability-flags)

**Slug**: `workbuddy-model-capability-flags`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 排查并修复 WorkBuddy 里自定义模型「不支持读图 / 不调用工具 / 不能推理」的能力位标错问题，以及新增自定义模型（OpenCode Zen、自建或其他厂商的 OpenAI 兼容端点）时一次性探测能力位并生成配置。当用户说「为什么说不支持读图」「模型读不了图片」「附件发不进去」「custom-local 模型能力不对」，或问「加新模型要测什么」「怎么知道这个模型支持读图/思考强度」时使用。含通用探测器 probe_model.py（一条命令测出读图/工具调用/effort 档位）、能力位定位法、直连端点自证法、以及「改完必须重启」这一必踩的坑。

**中文介绍**: 排查并修复 WorkBuddy 里自定义模型「不支持读图 / 不调用工具 / 不能推理」的能力位标错问题，以及新增自定义模型（OpenCode Zen、自建或其他厂商的 OpenAI 兼容端点）时一次性探测能力位并生成配置。当用户说「为什么说不支持读图」「模型读不了图片」「附件发不进去」「custom-local 模型能力不对」，或问「加新模型要测什么」「怎么知道这个模型支持读图/思考强度」时使用。含通用探测器 probe_model.py（一条命令测出读图/工具调用/effort 档位）、能力位定位法、直连端点自证法、以及「改完必须重启」这一必踩的坑。

Latest changelog:
首次发布；API key 改读环境变量，探针图缓存移到系统临时目录

**关键词**: 自定义模型能力位排查（读图, 推理）, 排查并修复, 里自定义模型「不支持读图, 不调用工具, 不能推理」的能力位标错问题, 以及新增自定义模型（OpenCode, WorkBuddy

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-model-capability-flags)

---

## [12. B站横屏视频转视频号竖屏切片](https://clawhub.ai/oracis/bilibili-to-shipinhao)

**Slug**: `bilibili-to-shipinhao`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把B站横屏中长视频(读书解读/知识类)自动改造为微信视频号9:16竖屏短视频切片。当用户说"B站视频转视频号""横屏转竖屏切片""读书视频切片""视频号短视频制作""横屏改竖屏"时使用。覆盖下载→转写→选段→横转竖→烧字幕→封面全流程, 含本机环境坑与画质/字幕优化。

**中文介绍**: 把B站横屏中长视频(读书解读/知识类)自动改造为微信视频号9:16竖屏短视频切片。当用户说"B站视频转视频号""横屏转竖屏切片""读书视频切片""视频号短视频制作""横屏改竖屏"时使用。覆盖下载→转写→选段→横转竖→烧字幕→封面全流程, 含本机环境坑与画质/字幕优化。

Latest changelog:
首次发布

**关键词**: B站横屏视频转视频号竖屏切片, 把B站横屏中长视频, 读书解读, 知识类, 自动改造为微信视频号9, 16竖屏短视频切片, 覆盖下载→转写→选段→横转竖→烧字幕→封面全流程, 含本机环境坑与画质

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bilibili-to-shipinhao)

---

## [13. 参考网站改 UI：抓设计 token 再落地](https://clawhub.ai/oracis/ref-site-ui-tokens)

**Slug**: `ref-site-ui-tokens`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 15 | 🧩 1

**原始简介**: 用户说「参考 X 网站改 UI / 照着 X 的风格做 / X 那种配色」时的落地流程。在没有浏览器的机器上（agent-browser、playwright 都没装，或 Chrome/Edge 不在标准路径）用 curl + 标准库 Python 抓下目标站的真实设计 token（颜色、圆角、字重、字号、间距），再据此改本地样式表。含一个可直接跑的抓取脚本 scripts/fetch_tokens.py，以及「借什么 / 不借什么」的取舍框架与常见坑。

**中文介绍**: 用户说「参考 X 网站改 UI / 照着 X 的风格做 / X 那种配色」时的落地流程。在没有浏览器的机器上（agent-browser、playwright 都没装，或 Chrome/Edge 不在标准路径）用 curl + 标准库 Python 抓下目标站的真实设计 token（颜色、圆角、字重、字号、间距），再据此改本地样式表。含一个可直接跑的抓取脚本 scripts/fetch_tokens.py，以及「借什么 / 不借什么」的取舍框架与常见坑。

Latest changelog:
首次发布

**关键词**: 参考网站改, UI, 抓设计, 再落地, 用户说「参考, 网站改, 照着, token

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ref-site-ui-tokens)

---

## [14. 国内网络环境下用 yt-dlp 下载视频](https://clawhub.ai/oracis/yt-dlp-cn-download)

**Slug**: `yt-dlp-cn-download`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 17 | 🧩 1

**原始简介**: 在中国大陆网络环境下用 yt-dlp 下载视频（含 Windows GUI 封装）。当用户要下载 YouTube、Bilibili、SoundCloud 等 yt-dlp 支持的站点内容，或遇到「yt-dlp 装不上 / 下载报 502 / Tunnel connection failed / ffmpeg not found / 缺 JS runtime / TLS fingerprint / watch?v=&list= 把整个列表都下了 / Sign in to confirm you're not a bot / The page needs to be reloaded / 下到一半突然下不动 / 下回来的视频糊、有拖影残影 / 下载速度特别慢」等问题时使用。

**中文介绍**: 在中国大陆网络环境下用 yt-dlp 下载视频（含 Windows GUI 封装）。当用户要下载 YouTube、Bilibili、SoundCloud 等 yt-dlp 支持的站点内容，或遇到「yt-dlp 装不上 / 下载报 502 / Tunnel connection failed / ffmpeg not found / 缺 JS runtime / TLS fingerprint / watch?v=&list= 把整个列表都下了 / Sign in to confirm you're not a bot / The page needs to be reloaded / 下到一半突然下不动 / 下回来的视频糊、有拖影残影 / 下载速度特别慢」等问题时使用。

Latest changelog:
首次发布

**关键词**: 国内网络环境下用, 下载视频, 在中国大陆网络环境下用, 下载视频（含, 封装）, yt-dlp, Windows, GUI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yt-dlp-cn-download)

---

## [15. 沙箱环境下的 git 安全操作与仓库恢复](https://clawhub.ai/oracis/git-sandbox-safe-ops)

**Slug**: `git-sandbox-safe-ops`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 17 | 🧩 1

**原始简介**: 在 WorkBuddy 沙箱安全执行 git fetch/push/reset 并修复 .git 缺失、引用丢失、push 被拒等常见问题。

**中文介绍**: 在 WorkBuddy 沙箱安全执行 git fetch/push/reset 并修复 .git 缺失、引用丢失、push 被拒等常见问题。

Latest changelog:
首次发布

**关键词**: 沙箱环境下的, 安全操作与仓库恢复, 沙箱安全执行, git, WorkBuddy, fetch, push, reset

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/git-sandbox-safe-ops)

---

## [16. 网盘资源聚合搜索（百度/夸克/阿里云盘）](https://clawhub.ai/oracis/netdisk-resource-search)

**Slug**: `netdisk-resource-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 15 | 🧩 1

**原始简介**: 聚合搜索百度网盘/夸克网盘/阿里云盘等网盘分享链接。当用户想按作者名、课程名、剧名、书名、软件名找网盘下载路径，或提到「网盘搜索」「PanSou」「盘搜」「找到下载链接」「夸克/百度/阿里网盘资源」时使用。包含已验证的 PanSou 协议端点、绕过系统代理的必要写法、以及可直接运行的本地 Web 应用 panradar.py。

**中文介绍**: 聚合搜索百度网盘/夸克网盘/阿里云盘等网盘分享链接。当用户想按作者名、课程名、剧名、书名、软件名找网盘下载路径，或提到「网盘搜索」「PanSou」「盘搜」「找到下载链接」「夸克/百度/阿里网盘资源」时使用。包含已验证的 PanSou 协议端点、绕过系统代理的必要写法、以及可直接运行的本地 Web 应用 panradar.py。

Latest changelog:
首次发布

**关键词**: 网盘资源聚合搜索（百度, 夸克, 阿里云盘）, 聚合搜索百度网盘, 夸克网盘, 阿里云盘等网盘分享链接, 百度, 阿里网盘资源」时使用

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/netdisk-resource-search)

---

## [17. 零依赖图片诊断与并排对照（无 Pillow）](https://clawhub.ai/oracis/zero-dep-image-inspect)

**Slug**: `zero-dep-image-inspect`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 20 | 🧩 1

**原始简介**: 不装 Pillow / OpenCV 也能读图和量图：用标准库 zlib 解码 PNG，做亮度与主色统计、相邻像素跳变（锐度代理）、非白外接框、双线性缩放、裁切、写 PNG、并排/上下对照图、联系表，并用「模拟暗部提亮」把色带暴露出来。当用户说「图片不清晰」「图好糊/发灰/有横条斜条」「颜色不对」「帮我对比这两张图」「从截图里把某块裁出来」「批量看图挑一张」，或需要诊断「生成出来的图为什么在别处变丑」时使用。

**中文介绍**: 不装 Pillow / OpenCV 也能读图和量图：用标准库 zlib 解码 PNG，做亮度与主色统计、相邻像素跳变（锐度代理）、非白外接框、双线性缩放、裁切、写 PNG、并排/上下对照图、联系表，并用「模拟暗部提亮」把色带暴露出来。当用户说「图片不清晰」「图好糊/发灰/有横条斜条」「颜色不对」「帮我对比这两张图」「从截图里把某块裁出来」「批量看图挑一张」，或需要诊断「生成出来的图为什么在别处变丑」时使用。

Latest changelog:
首次发布

**关键词**: 零依赖图片诊断与并排对照（无, 不装, 也能读图和量图, 用标准库, Pillow）, Pillow, OpenCV, zlib

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zero-dep-image-inspect)

---

## [18. 多平台发布编排（状态机 /幂等 / 门禁）](https://clawhub.ai/oracis/multiplatform-publish-core)

**Slug**: `multiplatform-publish-core`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 20 | 🧩 1

**原始简介**: 把一份内容分发到多个内容平台时的**编排层**：落盘清单状态机、幂等判据、 批量串行约束、以及三条质量门禁（回读校验、禁`| tail` 截断、平台合规预检）。 当用户说「发到几个平台」「批量发」「一条都没发成功但脚本报成功」 「重复发了」「草稿箱对不上」「点了保存但远端没变」「内容被判违规下架」 「多平台发布状态怎么对账」时使用。 ⚠ 只管编排，不管各平台的具体接口 —— 平台适配见 `cn-social-platform-adapters`。

**中文介绍**: 把一份内容分发到多个内容平台时的**编排层**：落盘清单状态机、幂等判据、 批量串行约束、以及三条质量门禁（回读校验、禁`| tail` 截断、平台合规预检）。 当用户说「发到几个平台」「批量发」「一条都没发成功但脚本报成功」 「重复发了」「草稿箱对不上」「点了保存但远端没变」「内容被判违规下架」 「多平台发布状态怎么对账」时使用。 ⚠ 只管编排，不管各平台的具体接口 —— 平台适配见 `cn-social-platform-adapters`。

Latest changelog:
首次发布

**关键词**: 多平台发布编排（状态机, 幂等, 门禁）, 把一份内容分发到多个内容平台时的, 编排层, 落盘清单状态机、幂等判据、, 批量串行约束、以及三条质量门禁（回读校验、禁, tail

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/multiplatform-publish-core)

---

## [19. aigate](https://clawhub.ai/psyb0t/aigate)

**Slug**: `aigate`  
**Version**: 9.0.0  
**Stats**: ⭐ 0 | ⬇️ 2254 | 🧩 44

**原始简介**: Self-hosted AI platform — one `docker-compose up`, one OpenAI-compatible endpoint at http://localhost:4000. Bundles inference (Groq/Cerebras/OpenRouter/HuggingFace/Mistral/Cohere/Ollama/vLLM/llama.cpp/claudebox/pibox-zai/Anthropic/OpenAI), MCP tool use, a stealth browser cluster, image generation (FLUX/DALL-E/SD), speech synthesis (Kokoro/Qwen3-TTS/Chatterbox/OpenAI TTS), transcription (Whisper/Parakeet), S3-compatible object storage, agentic code execution (Claude Code + pi-coding-agent + sandboxed piston), web search (SearXNG), an email gateway (mailbox), a Telegram client (Telethon), time-series forecasting + tabular ML (predictalot), audio/video production (audiolla/flickies), an async job queue (proxq), and a web UI (LibreChat) — all reachable through one bearer token and automatic per-model fallback routing. Use when the user wants a one-command self-hosted OpenAI-compatible stack that aggregates many providers/tools behind a single endpoint instead of wiring each service up individually.

**中文介绍**: Self-hosted AI platform — one `docker-compose up`, one OpenAI-compatible endpoint at http://localhost:4000. Bundles inference (Groq/Cerebras/OpenRouter/HuggingFace/Mistral/Cohere/Ollama/vLLM/llama.cpp/claudebox/pibox-zai/Anthropic/OpenAI), MCP tool use, a stealth browser cluster, image generation (FLUX/DALL-E/SD), speech synthesis (Kokoro/Qwen3-TTS/Chatterbox/OpenAI TTS), transcription (Whisper/Parakeet), S3-compatible object storage, agentic code execution (Claude Code + pi-coding-agent + sandboxed piston), web search (SearXNG), an email gateway (mailbox), a Telegram client (Telethon), time-series forecasting + tabular ML (predictalot), audio/video production (audiolla/flickies), an async job queue (proxq), and a web UI (LibreChat) — all reachable through one bearer token and automatic per-model fallback routing. Use when the user wants a one-command self-hosted OpenAI-compatible stack that aggregates many providers/tools behind a single endpoint instead of wiring each service up individually.

Latest changelog:
aigate 9.0.0

- Updated documentation in `references/setup.md`.
- Removed the `skill-card.md` file, streamlining documentation structure.

**关键词**: up, aigate, Self-hosted, platform, one, docker-compose, OpenAI-compatible, endpoint

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aigate)

---

## [20. 数据流水线字段名漂移排查](https://clawhub.ai/oracis/data-pipeline-field-drift)

**Slug**: `data-pipeline-field-drift`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 18 | 🧩 1

**原始简介**: 当数据流水线里某个字段「一直读不到」、某类条目静默消失、或下游把「有数据」当成「没数据」时，用契约名比对法定位字段名漂移（同一逻辑字段在采集/暂存/落盘/读取四处各有一个名字），并写「契约名回归测试」钉死。含 grep 排查模板、死变量识别、回填对账顺序。当用户说「这个字段怎么一直是空的」「数据明明有却读不到」「回填没效果」「某类记录莫名不见了」时使用。

**中文介绍**: 当数据流水线里某个字段「一直读不到」、某类条目静默消失、或下游把「有数据」当成「没数据」时，用契约名比对法定位字段名漂移（同一逻辑字段在采集/暂存/落盘/读取四处各有一个名字），并写「契约名回归测试」钉死。含 grep 排查模板、死变量识别、回填对账顺序。当用户说「这个字段怎么一直是空的」「数据明明有却读不到」「回填没效果」「某类记录莫名不见了」时使用。

Latest changelog:
首次发布

**关键词**: 数据流水线字段名漂移排查, 用契约名比对法定位字段名漂移（同一逻辑字段在采集, 暂存, 落盘, 读取四处各有一个名字）, 并写「契约名回归测试」钉死, 排查模板、死变量识别、回填对账顺序, grep

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/data-pipeline-field-drift)

---

## [21. VBot Skills Framework](https://clawhub.ai/vexify-build/vbot-skills-framework)

**Slug**: `vbot-skills-framework`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 22 | 🧩 2

**原始简介**: A comprehensive framework for building reusable AI agent skills. Includes template system and 7 production-ready skills.

**中文介绍**: A comprehensive framework for building reusable AI agent skills. Includes template system and 7 production-ready skills.

Latest changelog:
Added 4 new skills

**关键词**: Agent, VBot, Skills, Framework, comprehensive, building, reusable, Includes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vbot-skills-framework)

---

## [22. emoji-finder](https://clawhub.ai/vexify-build/emoji-finder)

**Slug**: `emoji-finder`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 20 | 🧩 1

**原始简介**: Use when user needs to find an emoji for their message or code.

**中文介绍**: Use when user needs to find an emoji for their message or code.

Latest changelog:
Initial release

**关键词**: an, emoji-finder, Use, when, user, needs, find, emoji

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/emoji-finder)

---

## [23. dep-check](https://clawhub.ai/vexify-build/dep-check)

**Slug**: `dep-check`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 18 | 🧩 1

**原始简介**: Use when user wants to check for outdated npm dependencies.

**中文介绍**: Use when user wants to check for outdated npm dependencies.

Latest changelog:
Initial release

**关键词**: dep-check, Use, when, user, wants, check, outdated, npm

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dep-check)

---

## [24. readme-gen](https://clawhub.ai/vexify-build/readme-gen)

**Slug**: `readme-gen`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 19 | 🧩 1

**原始简介**: Use when user wants to generate a README.md for their project.

**中文介绍**: Use when user wants to generate a README.md for their project.

Latest changelog:
Initial release

**关键词**: readme-gen, Use, when, user, wants, generate, README.md, their

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/readme-gen)

---

## [25. commit-ai](https://clawhub.ai/vexify-build/commit-ai)

**Slug**: `commit-ai`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 18 | 🧩 1

**原始简介**: Use when user wants to generate a good git commit message from their changes.

**中文介绍**: Use when user wants to generate a good git commit message from their changes.

Latest changelog:
Initial release

**关键词**: commit-ai, Use, when, user, wants, generate, good, git

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/commit-ai)

---

