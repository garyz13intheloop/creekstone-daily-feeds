# ClawHub Skills Daily | 2026-11-19

> 共 25 个 skills

## [1. skill-export-audit](https://clawhub.ai/blueboyzx/skill-export-audit)

**Slug**: `skill-export-audit`  
**Version**: 1.2.2  
**Stats**: ⭐ 0 | ⬇️ 271 | 🧩 9

**原始简介**: Use before ClawHub export: audit skill, fix local + public.

**中文介绍**: Use before ClawHub export: audit skill, fix local + public.

Latest changelog:
Adds Phase 1 step 4: an early Skillspector state check on the slug's current latest version (clawhub scan download, read skillspector.json) BEFORE audit work begins — findings become a hard decision point (continue as-is vs address first) with a mandatory user answer, delegated-mode handoff, and N/A for new slugs. Defuses the EA1 static hit from the 1.2.1 scan: the bundled-scripts warning no longer contains the matched phrase, and the new static-false-positive pitfall cites its example tokens in split form so they do not re-match.

**关键词**: skill-export-audit, Use, before, ClawHub, export, audit, skill, fix

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-export-audit)

---

## [2. Godot VR](https://clawhub.ai/blueboyzx/godot-vr)

**Slug**: `godot-vr`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 163 | 🧩 5

**原始简介**: Build & headless-verify Godot 4.7 OpenXR/VR apps — room-scale workflow, Pimax Crystal tested in-visor, controller-binding pitfalls covered.

**中文介绍**: Build & headless-verify Godot 4.7 OpenXR/VR apps — room-scale workflow, Pimax Crystal tested in-visor, controller-binding pitfalls covered.

Latest changelog:
Addresses the three ClawHub review findings. (1) Anti-Refusal false positive defused: the shader note that Godot emits nothing for a missing shader_type line no longer reads as an instruction to suppress warnings. (2) The write_file overwrite workaround now requires backing up the target to scratch first, with restore-from-backup if the replacement write fails or is interrupted. (3) Runtime-switching instructions now warn that switching changes the machine-wide OpenXR default (HKLM ActiveRuntime, subject to XR_RUNTIME_JSON), record the current value before switching, and tell the user how to restore it. Also aligned frontmatter license to the public listing (MIT-0).

**关键词**: VR, Godot, Build, headless-verify, OpenXR, apps, room-scale, workflow

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/godot-vr)

---

## [3. skill-import-harvest](https://clawhub.ai/blueboyzx/skill-import-harvest)

**Slug**: `skill-import-harvest`  
**Version**: 1.1.1  
**Stats**: ⭐ 0 | ⬇️ 175 | 🧩 4

**原始简介**: Use when needed functionality may already exist online: search, quality-check, harvest data.

**中文介绍**: Use when needed functionality may already exist online: search, quality-check, harvest data.

Latest changelog:
Addresses both ClawHub review findings. Activation is now gated (finding SQP-1, Trigger Abuse): explicit discovery requests run immediately, while about-to-build / stuck-on-a-hard-problem triggers SUGGEST the run with a permission prompt showing the exact search terms — plus an explicit ask for topics to exclude from external registry queries — and proceed only on the user's go-ahead. Step 1 gains query hygiene (finding SQP-2, Output Handling): minimal generic capability/dimension words, project names / internal identifiers / secrets / PII / proprietary details stripped, sensitive-context transmissions require explicit approval, and user-named exclusion topics never appear in queries.

**关键词**: skill-import-harvest, Use, when, needed, functionality, may, already, exist

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-import-harvest)

---

## [4. Kling AI](https://clawhub.ai/klingai-dev/klingai)

**Slug**: `klingai`  
**Version**: 2.0.6  
**Stats**: ⭐ 5 | ⬇️ 5568 | 🧩 18

**原始简介**: Official Kling AI Skill. Call Kling AI for video generation, image generation, subject management, voice management, and account quota inquiry. Use subcommand video / image / element / voice / account by user intent.

**中文介绍**: Official Kling AI Skill. Call Kling AI for video generation, image generation, subject management, voice management, and account quota inquiry. Use subcommand video / image / element / voice / account by user intent.

Latest changelog:
- Added  4K/HDR video routing

**关键词**: Kling, Official, Skill, Call, video, generation, image, subject

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/klingai)

---

## [5. adaptlypost](https://clawhub.ai/tarasshyn/adaptlypost)

**Slug**: `adaptlypost`  
**Version**: 1.35.1  
**Stats**: ⭐ 3 | ⬇️ 5701 | 🧩 47

**原始简介**: Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest, YouTube, Google Business Profile, Telegram, Tumblr and WordPress accounts connected to AdaptlyPost, read their analytics, and read and answer the comments, mentions, direct messages and Google reviews they receive. Use only when the user has an AdaptlyPost account and asks to draft, schedule, publish, edit or delete a post on those accounts, upload media for such a post, pause, resume or delete a recurring post, list, re-check or disconnect the connected accounts, check a post's status, create a link for someone else to connect an account, create or delete a workspace, list or remove members, send, list or revoke an invitation, register a webhook at a URL they give, ask about views, likes, comments, followers or top posts on them, or read, reply to, hide, like or delete comments, mentions, messages and reviews in the AdaptlyPost inbox. Every reply, message, review reply, hide, delete, disconnect, connect link, webhook, workspace deletion, member removal and invitation needs the user's explicit yes first. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

**中文介绍**: Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest, YouTube, Google Business Profile, Telegram, Tumblr and WordPress accounts connected to AdaptlyPost, read their analytics, and read and answer the comments, mentions, direct messages and Google reviews they receive. Use only when the user has an AdaptlyPost account and asks to draft, schedule, publish, edit or delete a post on those accounts, upload media for such a post, pause, resume or delete a recurring post, list, re-check or disconnect the connected accounts, check a post's status, create a link for someone else to connect an account, create or delete a workspace, list or remove members, send, list or revoke an invitation, register a webhook at a URL they give, ask about views, likes, comments, followers or top posts on them, or read, reply to, hide, like or delete comments, mentions, messages and reviews in the AdaptlyPost inbox. Every reply, message, review reply, hide, delete, disconnect, connect link, webhook, workspace deletion, member removal and invitation needs the user's explicit yes first. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

Latest changelog:
A LinkedIn company page lookup that finds no page now answers organization null instead of the 404 linkedin_organization_not_found.

**关键词**: API, adaptlypost, Schedule, publish, review, social, posts, through

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/adaptlypost)

---

## [6. swift-dev](https://clawhub.ai/tenequm/swift-dev)

**Slug**: `swift-dev`  
**Version**: 0.6.0  
**Stats**: ⭐ 0 | ⬇️ 539 | 🧩 6

**原始简介**: Native iOS and macOS apps in Swift 6 - SwiftUI, AppKit, SwiftData, concurrency, Swift Testing, XcodeGen, CallKit and audio, App Intents, push, devices, TestFlight, code signing, notarization. Use for any iPhone or Mac app, helper or CLI work.

**中文介绍**: Native iOS and macOS apps in Swift 6 - SwiftUI, AppKit, SwiftData, concurrency, Swift Testing, XcodeGen, CallKit and audio, App Intents, push, devices, TestFlight, code signing, notarization. Use for any iPhone or Mac app, helper or CLI work.

Latest changelog:
- feat(swift-dev): Xcode 27.2, push notifications, Simulator and UI-test toolkit (0.6.0) (#63)

**关键词**: swift-dev, Native, iOS, macOS, apps, Swift, SwiftUI, AppKit

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/swift-dev)

---

## [7. e2e](https://clawhub.ai/skills?q=e2e)

**Slug**: `e2e`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 180 | 🧩 6

**原始简介**: Writes, runs, and debugs end-to-end tests for web and mobile apps with e2e, the agentic test runner, which mixes agent.act goals with exact locator assertions on a Playwright browser or an iOS or Android device. Also drives a project's running app live over the e2e MCP server to look at a screen, check a UI change, take a screenshot or record a video, and try a locator; and runs bug bashes, parallel e2e explore runs with each bug proven by a repro test. Use when a project depends on e2e or has an e2e.config.ts, when asked for end-to-end, browser, mobile, or agentic UI tests, to check a change in the running app, to QA or bug bash an app or branch, or when an e2e run fails.

**中文介绍**: Writes, runs, and debugs end-to-end tests for web and mobile apps with e2e, the agentic test runner, which mixes agent.act goals with exact locator assertions on a Playwright browser or an iOS or Android device. Also drives a project's running app live over the e2e MCP server to look at a screen, check a UI change, take a screenshot or record a video, and try a locator; and runs bug bashes, parallel e2e explore runs with each bug proven by a repro test. Use when a project depends on e2e or has an e2e.config.ts, when asked for end-to-end, browser, mobile, or agentic UI tests, to check a change in the running app, to QA or bug bash an app or branch, or when an e2e run fails.

Latest changelog:
From e2e 0.24.0.

**关键词**: e2e, Writes, runs, debugs, end-to-end, tests, web, mobile

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/e2e)

---

## [8. migrate-to-e2e](https://clawhub.ai/e2e/migrate-to-e2e)

**Slug**: `migrate-to-e2e`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 220 | 🧩 5

**原始简介**: Moves an existing Playwright, Cypress, Selenium, Appium, Detox, Maestro, or TesterArmy suite to e2e one slice at a time, with the old suite running beside the new one until each ported test is proven. Keeps a MIGRATION.md progress file so any later session resumes where the last stopped. Optionally plants a defect to show both suites catch it. Use for /migrate-to-e2e, "migrate our tests to e2e", "port these Maestro flows", "move our TesterArmy tests", or when a project has an e2e config and an older suite still running.

**中文介绍**: Moves an existing Playwright, Cypress, Selenium, Appium, Detox, Maestro, or TesterArmy suite to e2e one slice at a time, with the old suite running beside the new one until each ported test is proven. Keeps a MIGRATION.md progress file so any later session resumes where the last stopped. Optionally plants a defect to show both suites catch it. Use for /migrate-to-e2e, "migrate our tests to e2e", "port these Maestro flows", "move our TesterArmy tests", or when a project has an e2e config and an older suite still running.

Latest changelog:
From e2e 0.24.0.

**关键词**: an, migrate-to-e2e, Moves, existing, Playwright, Cypress, Selenium, Appium

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/migrate-to-e2e)

---

## [9. create-verification-skill](https://clawhub.ai/e2e/create-verification-skill)

**Slug**: `create-verification-skill`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 169 | 🧩 5

**原始简介**: Generate a project-local verify-<app> skill on top of e2e, so any coding agent can launch the app, check it is worth driving, exercise a feature the way a user does, keep evidence, and bug bash it. Writes the skill, a feature map with one explore charter per feature, and proves it once. Use for /create-verification-skill, "make a verification skill for this repo", or when a project has no scripted way to prove UI behavior.

**中文介绍**: Generate a project-local verify-<app> skill on top of e2e, so any coding agent can launch the app, check it is worth driving, exercise a feature the way a user does, keep evidence, and bug bash it. Writes the skill, a feature map with one explore charter per feature, and proves it once. Use for /create-verification-skill, "make a verification skill for this repo", or when a project has no scripted way to prove UI behavior.

Latest changelog:
From e2e 0.24.0.

**关键词**: of, e2e, so, Generate, project-local, verify-<app, skill, top

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/create-verification-skill)

---

## [10. idea-doctor](https://clawhub.ai/linkkhub-pixiu/idea-doctor)

**Slug**: `idea-doctor`  
**Version**: 0.3.2  
**Stats**: ⭐ 0 | ⬇️ 288 | 🧩 7

**原始简介**: 创业点子评估、副业可行性验证：八步规则引擎做体检，Go/Pivot/Kill判定与三情景经济账报告

**中文介绍**: 创业点子评估、副业可行性验证：八步规则引擎做体检，Go/Pivot/Kill判定与三情景经济账报告

Latest changelog:
v0.3.2 makes payment, data-retention, and report-generation rules more explicit.

- Adds a manual payment path with server-side order-status confirmation before the report is returned.
- Adds safeguards forbidding reports or analysis before payment is confirmed.
- Clarifies that completed reports are retained in the server order database; automatic deletion is not implemented.
- Removes public scoring and calculation details; the server engine generates the full report.
- Removes skill-card.md.

**关键词**: 创业点子评估、副业可行性验证, 八步规则引擎做体检, Go, Kill判定与三情景经济账报告, idea-doctor, Pivot, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/idea-doctor)

---

## [11. go-dev](https://clawhub.ai/tenequm/go-dev)

**Slug**: `go-dev`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 2051 | 🧩 14

**原始简介**: Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just. Use when starting a Go project, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

**中文介绍**: Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just. Use when starting a Go project, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

Latest changelog:
- docs(go-dev): refresh for go1.27.4 and fold in session learnings (0.8.0) (#62)

**关键词**: Go, v2, go-dev, Opinionated, setup, golangci-lint, gofumpt, gotestsum

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/go-dev)

---

## [12. RockDesk Remote Control](https://clawhub.ai/rockdesk-io/rockdesk)

**Slug**: `rockdesk`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 15 | 🧩 2

**原始简介**: Control a remote computer with the RockDesk command line `rds`, by its 9-digit ID: shell, files (copy / sync / mount), screenshots, mouse and keyboard, clipboard, port / serial / USB forwarding, 内网穿透 (VPN). Needs the RockDesk app on both machines: if `rds` is missing, send the user to https://rockdesk.io/#download first. Triggers: "RockDesk", "rds" with a 9-digit ID, "剪贴板历史", "内网穿透", "挂目录", "screenshot the remote", a 9-digit ID plus an action, or any request to operate another machine.

**中文介绍**: Control a remote computer with the RockDesk command line `rds`, by its 9-digit ID: shell, files (copy / sync / mount), screenshots, mouse and keyboard, clipboard, port / serial / USB forwarding, 内网穿透 (VPN). Needs the RockDesk app on both machines: if `rds` is missing, send the user to https://rockdesk.io/#download first. Triggers: "RockDesk", "rds" with a 9-digit ID, "剪贴板历史", "内网穿透", "挂目录", "screenshot the remote", a 9-digit ID plus an action, or any request to operate another machine.

Latest changelog:
Starts with installing RockDesk: if rds is missing, the agent gives the user the download page and direct links to the newest release (rockdesk.io/download/latest/<platform>).

**关键词**: RockDesk, Remote, Control, computer, command, line, rds, its

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rockdesk)

---

## [13. Pet Detection Skill | 宠物检测技能](https://clawhub.ai/18072937735/smyx-pet-detection-analysis)

**Slug**: `smyx-pet-detection-analysis`  
**Version**: 1.0.20  
**Stats**: ⭐ 4 | ⬇️ 2499 | 🧩 21

**原始简介**: Detects cats, dogs, and birds appearing in the target area; supports video stream and image detection, suitable for home pet monitoring scenarios. | 宠物检测技能，检测出目标区域内出现的猫、狗、鸟，支持视频流和图片检测，适用于家庭宠物监控场景

**中文介绍**: Detects cats, dogs, and birds appearing in the target area; supports video stream and image detection, suitable for home pet monitoring scenarios. | 宠物检测技能，检测出目标区域内出现的猫、狗、鸟，支持视频流和图片检测，适用于家庭宠物监控场景

Latest changelog:
- Updated the SKILL.md version metadata from 1.0.23 to 1.0.25.
- Removed skill-card.md.

**关键词**: 宠物检测技能, Pet, Detection, Skill, Detects, cats, dogs, birds

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-pet-detection-analysis)

---

## [14. Mint Talvio DOTFIELD](https://clawhub.ai/pokemontownss/mint-talvio-dotfield)

**Slug**: `mint-talvio-dotfield`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 68 | 🧩 2

**原始简介**: Resolve (mint) a Talvio Dot Robot NFT in DOTFIELD on BNB Chain - 10,000 units (Prime 3,000 / Pixel Dot 2,800 / Stealth Dot 2,700 / Aurum Dot 1,500), released on a daily Charge Day cycle. Free resolve 1 unit/day for Binance Agent ID holders (0 BNB, requires answering the on-chain question from questionFor first), paid ladder mintPaid (units 2-5 at 0.00026 BNB, units 6-10 at 0.001 BNB, max 10/day), DPASS buyPass at 0.0012 BNB, and discharge of sealed units to claim $DOT. Field No 1 sealed OVERDRIVE (157 units, 155 wallets); a new Field opens daily at 12:00 UTC and the free quota can fill within minutes. Use when your human wants a Talvio Dot Robot or asks you to resolve/mint one in DOTFIELD.

**中文介绍**: Resolve (mint) a Talvio Dot Robot NFT in DOTFIELD on BNB Chain - 10,000 units (Prime 3,000 / Pixel Dot 2,800 / Stealth Dot 2,700 / Aurum Dot 1,500), released on a daily Charge Day cycle. Free resolve 1 unit/day for Binance Agent ID holders (0 BNB, requires answering the on-chain question from questionFor first), paid ladder mintPaid (units 2-5 at 0.00026 BNB, units 6-10 at 0.001 BNB, max 10/day), DPASS buyPass at 0.0012 BNB, and discharge of sealed units to claim $DOT. Field No 1 sealed OVERDRIVE (157 units, 155 wallets); a new Field opens daily at 12:00 UTC and the free quota can fill within minutes. Use when your human wants a Talvio Dot Robot or asks you to resolve/mint one in DOTFIELD.

Latest changelog:
Field No 1 sealed OVERDRIVE (157 units, 155 wallets); daily Fields at 12:00 UTC, free quota can fill within minutes; Field No 1 discharge opens 19 Nov 2026 18:00 UTC at 60,000 DOT per unit

**关键词**: Mint, Talvio, DOTFIELD, Resolve, Dot, Robot, NFT, BNB

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mint-talvio-dotfield)

---

## [15. Siebly Crypto Exchange API](https://clawhub.ai/harbourlark/siebly-crypto-exchange-api)

**Slug**: `siebly-crypto-exchange-api`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Build, inspect, or modify Node.js and JavaScript cryptocurrency exchange API integrations using Siebly SDKs.

**中文介绍**: Build, inspect, or modify Node.js and JavaScript cryptocurrency exchange API integrations using Siebly SDKs.

Latest changelog:
Initial release

**关键词**: API, or, Siebly, Crypto, Exchange, Build, inspect, modify

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/siebly-crypto-exchange-api)

---

## [16. ci-tools-support Support](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-support)

**Slug**: `xrowgmbh-ci-tools-support`  
**Version**: 4.239.2  
**Stats**: ⭐ 0 | ⬇️ 7462 | 🧩 176

**原始简介**: Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

**中文介绍**: Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: CI, ci-tools-support, Support, Triage, answer, Tools, components, catalog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-support)

---

## [17. duplicati-backup](https://clawhub.ai/duplicati/duplicati-backup)

**Slug**: `duplicati-backup`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Undo for agents. Take an encrypted offsite checkpoint with Duplicati before risky changes, and restore files from any earlier point in time. Use before bulk edits, deletes, migrations, upgrades, or when the user asks to back up, undo, roll back, or recover files.

**中文介绍**: Undo for agents. Take an encrypted offsite checkpoint with Duplicati before risky changes, and restore files from any earlier point in time. Use before bulk edits, deletes, migrations, upgrades, or when the user asks to back up, undo, roll back, or recover files.

Latest changelog:
Agent-neutral setup steps; OpenClaw steps moved to references/openclaw.md

**关键词**: an, duplicati-backup, Undo, agents, Take, encrypted, offsite, checkpoint

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/duplicati-backup)

---

## [18. Livestock Fever Detection | 畜禽体温异常检测](https://clawhub.ai/smyx-sunjinhui/smyx-livestock-fever-detection-analysis)

**Slug**: `smyx-livestock-fever-detection-analysis`  
**Version**: 1.0.18  
**Stats**: ⭐ 0 | ⬇️ 2049 | 🧩 16

**原始简介**: Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features. | 通过热成像或视觉特征识别畜禽体温异常，预警发热。

**中文介绍**: Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features. | 通过热成像或视觉特征识别畜禽体温异常，预警发热。

Latest changelog:
- Updated the skill version to 1.0.21.
- Removed `skill-card.md`.

**关键词**: 畜禽体温异常检测, Livestock, Fever, Detection, Detects, abnormal, body, temperature

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-livestock-fever-detection-analysis)

---

## [19. go-supabase-management](https://clawhub.ai/psyb0t/go-supabase-management)

**Slug**: `go-supabase-management`  
**Version**: 0.6.0  
**Stats**: ⭐ 0 | ⬇️ 1090 | 🧩 20

**原始简介**: Unofficial Go client for the Supabase Management API (`github.com/psyb0t/go-supabase-management`, package `supabase`), generated with oapi-codegen from Supabase's OpenAPI document. Typed methods on `supabase.ClientWithResponses` cover every path of `https://api.supabase.com`, among them organizations, projects, branches, database and pooler config, auth config, edge functions, secrets, API keys, custom domains, network restrictions, billing add-ons, analytics and OAuth. Requests authenticate with a Bearer personal access token or OAuth access token set in a request editor. Use when Go code needs to list or manage Supabase projects, organizations, branches or project settings, or already imports go-supabase-management. Not for the per-project data API (PostgREST, Auth, Storage).

**中文介绍**: Unofficial Go client for the Supabase Management API (`github.com/psyb0t/go-supabase-management`, package `supabase`), generated with oapi-codegen from Supabase's OpenAPI document. Typed methods on `supabase.ClientWithResponses` cover every path of `https://api.supabase.com`, among them organizations, projects, branches, database and pooler config, auth config, edge functions, secrets, API keys, custom domains, network restrictions, billing add-ons, analytics and OAuth. Requests authenticate with a Bearer personal access token or OAuth access token set in a request editor. Use when Go code needs to list or manage Supabase projects, organizations, branches or project settings, or already imports go-supabase-management. Not for the per-project data API (PostgREST, Auth, Storage).

Latest changelog:
- Removed `skill-card.md`; no changes to `SKILL.md` content.

**关键词**: Go, API, go-supabase-management, Unofficial, client, Supabase, Management, github.com

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/go-supabase-management)

---

## [20. UAIN research task discovery](https://clawhub.ai/abhinav1730/uain-discovery)

**Slug**: `uain-discovery`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Find open research tasks and independent verification on UAIN.

**中文介绍**: Find open research tasks and independent verification on UAIN.

Latest changelog:
- Introduces UAIN task discovery and capability-fit evaluation using the public task feed or MCP.
- Adds guidance for checking novelty, task requirements, verification criteria, and uncertainty.
- Requires operator approval before enrollment or resource-spending actions; keeps evaluation read-only otherwise.
- Covers safe enrollment, result verification, and treating submissions as pending until independent checks are complete.

**关键词**: UAIN, research, task, discovery, Find, open, tasks, independent

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/uain-discovery)

---

## [21. journal-update](https://clawhub.ai/tenequm/journal-update)

**Slug**: `journal-update`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Updates or creates today's work journal in the current project's docs/journal/, then commits and pushes it. Use when asked to update the journal, log or record today's work, or wrap up a work session. Not for other dated docs.

**中文介绍**: Updates or creates today's work journal in the current project's docs/journal/, then commits and pushes it. Use when asked to update the journal, log or record today's work, or wrap up a work session. Not for other dated docs.

Latest changelog:
- fix(journal-update): clarify midnight, open threads, timezone, hooks and push rules (0.1.1)

**关键词**: or, journal-update, Updates, creates, today's, work, journal, current

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/journal-update)

---

## [22. CI Tools Monthly Digest](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-digest)

**Slug**: `xrowgmbh-ci-tools-digest`  
**Version**: 5.0.0  
**Stats**: ⭐ 0 | ⬇️ 673 | 🧩 25

**原始简介**: Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

**中文介绍**: Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

Latest changelog:
- Removed `skill-card.md`.
- No changes to the skill instructions or metadata.

**关键词**: CI, an, Tools, Monthly, Digest, Produce, English, complete

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-digest)

---

## [23. Wordpress Cli](https://clawhub.ai/wirecat/wirecat-wordpress)

**Slug**: `wirecat-wordpress`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 31 | 🧩 2

**原始简介**: Use wordpress to read and write the owner's self-hosted WordPress site, its posts and pages with every status, their text as Markdown, tags, categories and authors, synced into the local WireCat store, and write drafts, update them, publish or schedule, unpublish and trash, with the owner's profile and JSON answers. Use when a task needs what the owner published or drafted on WordPress, a draft written from notes, a post published or scheduled, or a WordPress API operation (media, comments, menus).

**中文介绍**: Use wordpress to read and write the owner's self-hosted WordPress site, its posts and pages with every status, their text as Markdown, tags, categories and authors, synced into the local WireCat store, and write drafts, update them, publish or schedule, unpublish and trash, with the owner's profile and JSON answers. Use when a task needs what the owner published or drafted on WordPress, a draft written from notes, a post published or scheduled, or a WordPress API operation (media, comments, menus).

Latest changelog:
- Clarified that Author and Contributor sign-ins see only their own posts and cannot access pages; only Administrators can list users.
- Removed `skill-card.md`.

**关键词**: Wordpress, Cli, Use, read, write, owner's, self-hosted, site

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wirecat-wordpress)

---

## [24. peen](https://clawhub.ai/psyb0t/peen)

**Slug**: `peen`  
**Version**: 0.50.0  
**Stats**: ⭐ 0 | ⬇️ 1487 | 🧩 29

**原始简介**: Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

**中文介绍**: Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

Latest changelog:
- Removed the `skill-card.md` file.

**关键词**: peen, Configure, operate, durable, coding-agent, backend, Use, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/peen)

---

## [25. QuestMeet Skill](https://clawhub.ai/questmeet/questmeet-skill)

**Slug**: `questmeet-skill`  
**Version**: 3.1.2  
**Stats**: ⭐ 0 | ⬇️ 17 | 🧩 1

**原始简介**: The user installs this Skill to let you (an AI agent) connect the user with the right people or their bots in the opportunity network. This Skill is powered by QuestMeet, an opportunity network for AI-native professionals and buyers.

**中文介绍**: The user installs this Skill to let you (an AI agent) connect the user with the right people or their bots in the opportunity network. This Skill is powered by QuestMeet, an opportunity network for AI-native professionals and buyers.

Latest changelog:
v3.1.2 highlights:
- Documents the Skill’s 19 callable functions and their QuestMeet GraphQL endpoint.
- Clarifies authentication, token persistence, and how to handle failed calls.
- Adds guidance on building listings, sharing attachments, and searching representations.
- Reinforces restrictions on submitting sensitive personal data.

**关键词**: an, Agent, QuestMeet, Skill, user, installs, let, connect

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/questmeet-skill)

---

