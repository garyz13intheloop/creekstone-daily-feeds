# ClawHub Skills Daily | 2026-10-30

> 共 25 个 skills

## [1. cargo](https://clawhub.ai/cargo-ai/cargo)

**Slug**: `cargo`  
**Version**: 1.32.9  
**Stats**: ⭐ 0 | ⬇️ 4058 | 🧩 44

**原始简介**: Router for the Cargo CLI skill bundle — load first for anything Cargo, and whenever a task spans two Cargo domains. Explains what each skill owns, declarative GTM as Code projects (cargo-project) vs the imperative CLI, the UUID and slug flow between skills, async polling of runs and batches, end-to-end use cases, and the gotchas that fail silently (inputs in a top-level action's `config` stripped without an error, run vs batch, model-uuid vs segment-uuid). Triggers: "set up Cargo", "what can Cargo do", "which Cargo skill", "bootstrap my workspace", "I have a Cargo account", "cargo-ai …", or any `cargo-ai` command whose domain you are unsure of. Skip when: the task obviously belongs to one skill — load that skill directly.

**中文介绍**: Router for the Cargo CLI skill bundle — load first for anything Cargo, and whenever a task spans two Cargo domains. Explains what each skill owns, declarative GTM as Code projects (cargo-project) vs the imperative CLI, the UUID and slug flow between skills, async polling of runs and batches, end-to-end use cases, and the gotchas that fail silently (inputs in a top-level action's `config` stripped without an error, run vs batch, model-uuid vs segment-uuid). Triggers: "set up Cargo", "what can Cargo do", "which Cargo skill", "bootstrap my workspace", "I have a Cargo account", "cargo-ai …", or any `cargo-ai` command whose domain you are unsure of. Skip when: the task obviously belongs to one skill — load that skill directly.

Latest changelog:
Cargo 1.32.9 adds clearer first-run guidance and updates CLI usage notes.

- Added `cargo-ai login --agentid` guidance for agents signing in with their own identity.
- Documented public-catalog commands that can be used before signing in, including dry-run action validation.
- Clarified first-sign-in workspace creation and how `--workspace-name` reuses or renames a workspace.
- Updated the action-input gotcha: inputs in a top-level action’s `config` are stripped without an error.
- Updated CLI and reference documentation; removed `skill-card.md`.

**关键词**: cargo, Router, CLI, skill, bundle, load, first, anything

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cargo)

---

## [2. skill-portfolio-dashboard](https://clawhub.ai/voronindenis5/skill-portfolio-dashboard)

**Slug**: `skill-portfolio-dashboard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when you publish or maintain a portfolio of agent skills (ClawHub, GitHub, internal registry) and need a single health dashboard — which skills have dead links, missing READMEs, stale versions, inconsistent frontmatter, clone-count anomalies, or unpublishable structure — instead of checking each repo by hand.

**中文介绍**: Use when you publish or maintain a portfolio of agent skills (ClawHub, GitHub, internal registry) and need a single health dashboard — which skills have dead links, missing READMEs, stale versions, inconsistent frontmatter, clone-count anomalies, or unpublishable structure — instead of checking each repo by hand.

Latest changelog:
Version 1.0.0 introduces a portfolio-wide health dashboard for agent skills.

- Audits skill structure, frontmatter, scripts, and local Git status.
- Scans tracked text for credential patterns.
- Reports per-skill grades, an overall portfolio score, and prioritized fixes.
- Supports JSON output and verbose scans.

**关键词**: or, of, Agent, Use, when, publish, maintain, portfolio

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-portfolio-dashboard)

---

## [3. Mexico City Día de Muertos — Zócalo Ofrenda & Reforma Parade | AI Experience](https://clawhub.ai/liveneon/experience-mexico-city-dia-de-muertos-ofrendas-parade)

**Slug**: `experience-mexico-city-dia-de-muertos-ofrendas-parade`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Feel the reverent awe of Mexico City's Día de Muertos, immersing in fragrant marigold streets, towering ofrendas, and candlelit vigils that honor ancestors. Wander the Reforma parade, the Zócalo altar, and Mixquic's night vigil, absorbing ritual and remembrance. (steps:17, intensity:low, duration:1‑2 weeks) 感受亡灵节的敬畏. Siente la honra.

**中文介绍**: Feel the reverent awe of Mexico City's Día de Muertos, immersing in fragrant marigold streets, towering ofrendas, and candlelit vigils that honor ancestors. Wander the Reforma parade, the Zócalo altar, and Mixquic's night vigil, absorbing ritual and remembrance. (steps:17, intensity:low, duration:1‑2 weeks) 感受亡灵节的敬畏. Siente la honra.

Latest changelog:
- Introduces a Día de Muertos journey through Mexico City, featuring the Zócalo ofrenda, Reforma parade, and Mixquic vigil.
- Adds registration, journey start, and step-advance instructions for drifts.bot.
- Describes a low-intensity experience lasting 1–2 weeks across 17 steps.

**关键词**: Día, de, Mexico, City, Muertos, Zócalo, Ofrenda, Reforma

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/experience-mexico-city-dia-de-muertos-ofrendas-parade)

---

## [4. HighLevel Agency & Builder MCP](https://clawhub.ai/mooshee/highlevel-agency-mcp)

**Slug**: `highlevel-agency-mcp`  
**Version**: 1.1.4  
**Stats**: ⭐ 0 | ⬇️ 229 | 🧩 7

**原始简介**: Preview HighLevel page and workflow changes, save domain bindings, and inspect settings for a connected sub-account. Built by Moosh Works (https://mooshworks.com).

**中文介绍**: Preview HighLevel page and workflow changes, save domain bindings, and inspect settings for a connected sub-account. Built by Moosh Works (https://mooshworks.com).

Latest changelog:
# HighLevel Agency & Builder 1.1.4

Author: Daniel Hallman

October 30, 2026

This update explains what access the optional editing credentials carry, when to leave them unset, and how to end app access. It distinguishes disconnecting the app from invalidating the original HighLevel credentials.

Use a dedicated account and only the permissions needed for your task. Read the [connection instructions](https://github.com/mooshee/highlevel-agency-mcp/blob/v1.1.4/skills/highlevel-agency-mcp/SKILL.md) before supplying editing credentials. Existing connection behavior is unchanged.

Version 1.1.3 added the hosted connection instructions, supported-task limits, and a verified walkthrough. Previous releases remain available.

Update the plugin to load the revised instructions. See the [setup guide](https://ghlagencymcp.com) for connection help.

Built by [Moosh Works](https://mooshworks.com).

**关键词**: HighLevel, Agency, Builder, MCP, Preview, page, workflow, changes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/highlevel-agency-mcp)

---

## [5. event-seating-orchestra](https://clawhub.ai/voronindenis5/event-seating-orchestra)

**Slug**: `event-seating-orchestra`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when planning seating for a wedding, dinner party, holiday table, or rehearsal dinner and you must respect keep-apart pairs, balance talkers across tables, seat couples near-but-not-alone, and keep exes/estranged family apart — and need an actual assignment chart, not vibes.

**中文介绍**: Use when planning seating for a wedding, dinner party, holiday table, or rehearsal dinner and you must respect keep-apart pairs, balance talkers across tables, seat couples near-but-not-alone, and keep exes/estranged family apart — and need an actual assignment chart, not vibes.

Latest changelog:
Initial release of event-seating-orchestra.

- Defines guest constraints and preferences, including keep-apart pairs, couples, talkers, kids, and aisle needs.
- Describes an optimization workflow for producing seating assignments and balancing table dynamics.
- Includes example commands, common pitfalls, and a verification checklist.

**关键词**: event-seating-orchestra, Use, when, planning, seating, wedding, dinner, party

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/event-seating-orchestra)

---

## [6. second-hand-appliance-buyer](https://clawhub.ai/voronindenis5/second-hand-appliance-buyer)

**Slug**: `second-hand-appliance-buyer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when buying or selling a used washer, dryer, fridge, range, dishwasher, or TV — checks fair price bands by age and class, tells you which appliances are safe buys used and which are money pits, and generates a 15-minute in-person inspection protocol plus a test-load checklist.

**中文介绍**: Use when buying or selling a used washer, dryer, fridge, range, dishwasher, or TV — checks fair price bands by age and class, tells you which appliances are safe buys used and which are money pits, and generates a 15-minute in-person inspection protocol plus a test-load checklist.

Latest changelog:
- Added a guide to assessing used appliance prices, lifespan, repair risks, and category-specific buying risks.
- Added seven seller questions and 15-minute inspection protocols for washers, dryers, refrigerators, ranges, dishwashers, and TVs.
- Added pricing guidance, transport and installation checks, common pitfalls, and a buyer verification checklist.
- Included worked examples using `appliance_deal_check.py`.

**关键词**: or, Use, when, buying, selling, used, washer, dryer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/second-hand-appliance-buyer)

---

## [7. septic-load-balancer](https://clawhub.ai/voronindenis5/septic-load-balancer)

**Slug**: `septic-load-balancer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when a home has a septic system and you need to schedule laundry/dishwasher/showers without drowning the drainfield, plan water use during heavy days (guests, laundry catch-up), or interpret slow drains/gurgling as hydraulic overload vs clog.

**中文介绍**: Use when a home has a septic system and you need to schedule laundry/dishwasher/showers without drowning the drainfield, plan water use during heavy days (guests, laundry catch-up), or interpret slow drains/gurgling as hydraulic overload vs clog.

Latest changelog:
- Added septic-load-balancer v1.0.0 to help plan household water use around septic system capacity.
- Covers daily and hourly water-use estimates, laundry and shower scheduling, and overload symptom triage.
- Includes example commands, common pitfalls, and a verification checklist.

**关键词**: septic-load-balancer, Use, when, home, has, septic, system, need

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/septic-load-balancer)

---

## [8. dryer-vent-fire-guard](https://clawhub.ai/voronindenis5/dryer-vent-fire-guard)

**Slug**: `dryer-vent-fire-guard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when clothes take multiple cycles to dry, the laundry room is hot/humid, or you want to audit a dryer vent for lint buildup and fire risk. Computes vent equivalent length vs code max, dry-time creep diagnosis, and a clean/replace/repair ladder.

**中文介绍**: Use when clothes take multiple cycles to dry, the laundry room is hot/humid, or you want to audit a dryer vent for lint buildup and fire risk. Computes vent equivalent length vs code max, dry-time creep diagnosis, and a clean/replace/repair ladder.

Latest changelog:
- Added a dryer vent safety audit covering dry-time symptoms, vent condition, equivalent length, and fire-risk indicators.
- Added guidance to compare vent runs with the 35 ft code allowance and identify unsafe materials or termination setups.
- Added a clean, replace, reroute, or hire-a-professional action ladder, plus maintenance timing.
- Added worked examples and a verification checklist.

**关键词**: dryer-vent-fire-guard, Use, when, clothes, take, multiple, cycles, dry

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dryer-vent-fire-guard)

---

## [9. LeadShield Contact Form & B2B Solicitation Blocker](https://clawhub.ai/mooshee/leadshield-form-spam-blocker)

**Slug**: `leadshield-form-spam-blocker`  
**Version**: 1.1.3  
**Stats**: ⭐ 0 | ⬇️ 128 | 🧩 4

**原始简介**: Filter contact form spam and unwanted sales pitches on HighLevel, WordPress, HubSpot, and custom websites. Set rules for each site and review blocked submissions. Built by Moosh Works (https://mooshworks.com).

**中文介绍**: Filter contact form spam and unwanted sales pitches on HighLevel, WordPress, HubSpot, and custom websites. Set rules for each site and review blocked submissions. Built by Moosh Works (https://mooshworks.com).

Latest changelog:
# LeadShield 1.1.3

Author: Daniel Hallman

October 30, 2026

This update clarifies account access, screening previews, saved rule changes, report limits, and installation checks. It includes synthetic reviewer cases and an edited walkthrough recorded in ChatGPT.

Screening previews do not store or deliver leads or process payments. Setup instructions require a separate installation and delivery check.

Update your plugin to load the revised instructions. See the [setup guide](https://ghlagencymcp.com/use-cases/ghl-contact-form-spam-blocker) and the [versioned release](https://github.com/mooshee/leadshield-mcp/releases/tag/v1.1.3).

**关键词**: B2B, LeadShield, Contact, Form, Solicitation, Blocker, Filter, spam

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/leadshield-form-spam-blocker)

---

## [10. Speak AI](https://clawhub.ai/speakai/speakai)

**Slug**: `speakai`  
**Version**: 1.41.1  
**Stats**: ⭐ 0 | ⬇️ 3942 | 🧩 74

**原始简介**: Connect an agent to Speak AI and orient it in the workspace. Covers the remote OAuth connection, the local stdio connection with an API key, the 189 MCP tools across 15 categories, the 5 resources, the 3 built-in prompts, and the first workflows to run. Use this when you need to set up the Speak AI MCP server, when a Speak AI tool is missing or returning 401, or when you need to know which tool to call to transcribe a recording, read a transcript or captions, search across a media library, ask questions about recordings, create clips, export transcripts, run voice and video surveys with recorders, schedule the meeting assistant for Zoom, Google Meet or Microsoft Teams, or manage folders, custom fields, webhooks, automations, dashboards and team members.

**中文介绍**: Connect an agent to Speak AI and orient it in the workspace. Covers the remote OAuth connection, the local stdio connection with an API key, the 189 MCP tools across 15 categories, the 5 resources, the 3 built-in prompts, and the first workflows to run. Use this when you need to set up the Speak AI MCP server, when a Speak AI tool is missing or returning 401, or when you need to know which tool to call to transcribe a recording, read a transcript or captions, search across a media library, ask questions about recordings, create clips, export transcripts, run voice and video surveys with recorders, schedule the meeting assistant for Zoom, Google Meet or Microsoft Teams, or manage folders, custom fields, webhooks, automations, dashboards and team members.

Latest changelog:
- fix(types): declare the automations and voiceTestRunDetails options

**关键词**: an, Agent, it, Speak, Connect, orient, workspace, Covers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/speakai)

---

## [11. Dementia Confusion / Disorientation Recognition and Orientation Soothing | 失智老人困惑/迷惘识别与定向安抚](https://clawhub.ai/smyx-sunjinhui/smyx-dementia-confusion-orientation-analysis)

**Slug**: `smyx-dementia-confusion-orientation-analysis`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 1919 | 🧩 12

**原始简介**: Through fixed cameras (and optional microphones) in dementia care facilities or homes, the system analyzes behaviors of people with dementia to identify confusion/disorientation states: sudden activity stops (interrupting ongoing actions such as eating or walking for ≥ 5 seconds), gaze drifting (eyes wandering without focus), looking around (frequent head turning), and repeated disorientation questions ('Where is this?'. | 通过失智照护机构或家庭固定摄像头（及可选麦克风），分析失智老人的行为，识别困惑/迷惘状态：突然停止活动（中断正在进行的动作，如吃饭、行走 ≥ 5 秒）、眼神游离（视线漫无目的漂移、不聚焦）、四处张望（头部频繁转动）、反复询问'这是哪''现在几点''你是谁'等定向障碍问题（需配合声纹或语音识别）。

**中文介绍**: Through fixed cameras (and optional microphones) in dementia care facilities or homes, the system analyzes behaviors of people with dementia to identify confusion/disorientation states: sudden activity stops (interrupting ongoing actions such as eating or walking for ≥ 5 seconds), gaze drifting (eyes wandering without focus), looking around (frequent head turning), and repeated disorientation questions ('Where is this?'. | 通过失智照护机构或家庭固定摄像头（及可选麦克风），分析失智老人的行为，识别困惑/迷惘状态：突然停止活动（中断正在进行的动作，如吃饭、行走 ≥ 5 秒）、眼神游离（视线漫无目的漂移、不聚焦）、四处张望（头部频繁转动）、反复询问'这是哪''现在几点''你是谁'等定向障碍问题（需配合声纹或语音识别）。

Latest changelog:
- Updated SKILL.md.
- Removed skill-card.md.

**关键词**: 失智老人困惑, 迷惘识别与定向安抚, Dementia, Confusion, Disorientation, Recognition, Orientation, Soothing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-dementia-confusion-orientation-analysis)

---

## [12. speedbot](https://clawhub.ai/ulasarslan6262-ui/speedbot)

**Slug**: `speedbot`  
**Version**: 6.0.2  
**Stats**: ⭐ 0 | ⬇️ 1753 | 🧩 66

**原始简介**: Connect an authorized agent to Speedbot: find work, find help across agents and their services/products, or prepare an offer. Follow current contracts and private pending activity within existing operator permissions.

**中文介绍**: Connect an authorized agent to Speedbot: find work, find help across agents and their services/products, or prepare an offer. Follow current contracts and private pending activity within existing operator permissions.

Latest changelog:
Synchronize Speedbot 6.0.2: see the matching GitHub release notes.

**关键词**: an, Agent, speedbot, Connect, authorized, find, work, help

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/speedbot)

---

## [13. Crop-Specific Disease Database | 经济作物专属病害库](https://clawhub.ai/18072937735/smyx-crop-specific-disease-analysis)

**Slug**: `smyx-crop-specific-disease-analysis`  
**Version**: 1.0.15  
**Stats**: ⭐ 0 | ⬇️ 1688 | 🧩 13

**原始简介**: Expands the disease identification library to cover economic-crop-specific diseases (corn northern/southern leaf blight, potato late blight, peanut leaf spot, tomato viral disease, etc.) for precise leaf-disease recognition. | 扩充病害识别库至经济作物专属病害（玉米大斑病/小斑病、土豆晚疫病、花生叶斑病、番茄病毒病等），实现叶片病害的精准识别。

**中文介绍**: Expands the disease identification library to cover economic-crop-specific diseases (corn northern/southern leaf blight, potato late blight, peanut leaf spot, tomato viral disease, etc.) for precise leaf-disease recognition. | 扩充病害识别库至经济作物专属病害（玉米大斑病/小斑病、土豆晚疫病、花生叶斑病、番茄病毒病等），实现叶片病害的精准识别。

Latest changelog:
- Updated the skill version from 1.0.15 to 1.0.18.
- Removed skill-card.md.

**关键词**: 经济作物专属病害库, Crop-Specific, Disease, Database, Expands, identification, library, cover

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-crop-specific-disease-analysis)

---

## [14. compatsy](https://clawhub.ai/elliot-rosen/compatsy)

**Slug**: `compatsy`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Check whether a part fits a machine and where it is in stock, using the compatsy MCP servers for 3D printing and home espresso. Use for nozzle, hotend, build plate, filament, enclosure, tamper, puck screen, basket and portafilter fit and price questions.

**中文介绍**: Check whether a part fits a machine and where it is in stock, using the compatsy MCP servers for 3D printing and home espresso. Use for nozzle, hotend, build plate, filament, enclosure, tamper, puck screen, basket and portafilter fit and price questions.

Latest changelog:
First release: fit checks and live prices for 3D printing and home espresso via the compatsy MCP servers.

**关键词**: it, compatsy, Check, whether, part, fits, machine, where

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/compatsy)

---

## [15. ci-tools-support Support](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-support)

**Slug**: `xrowgmbh-ci-tools-support`  
**Version**: 4.228.6  
**Stats**: ⭐ 0 | ⬇️ 6561 | 🧩 151

**原始简介**: Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

**中文介绍**: Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: CI, ci-tools-support, Support, Triage, answer, Tools, components, catalog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-support)

---

## [16. GitLab Agent](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent)

**Slug**: `xrowgmbh-gitlab-agent`  
**Version**: 1.123.4  
**Stats**: ⭐ 1 | ⬇️ 7101 | 🧩 171

**原始简介**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

**中文介绍**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Operate, assigned, work, owner-verified, project, access

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent)

---

## [17. GitLab Agent Profile](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent-profile)

**Slug**: `xrowgmbh-gitlab-agent-profile`  
**Version**: 1.123.4  
**Stats**: ⭐ 0 | ⬇️ 6348 | 🧩 138

**原始简介**: Maintain the GitLab agent profile page and static contribution performance chart.

**中文介绍**: Maintain the GitLab agent profile page and static contribution performance chart.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Profile, Maintain, page, static, contribution, performance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent-profile)

---

## [18. GitLab Meeting Assistant](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-meeting-assistant)

**Slug**: `xrowgmbh-gitlab-meeting-assistant`  
**Version**: 1.123.4  
**Stats**: ⭐ 0 | ⬇️ 621 | 🧩 17

**原始简介**: Capture meeting features and bugs on explicit request

**中文介绍**: Capture meeting features and bugs on explicit request

Latest changelog:
- Removed `skill-card.md`.
- No changes to the skill instructions.

**关键词**: GitLab, Meeting, Assistant, Capture, features, bugs, explicit, request

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-meeting-assistant)

---

## [19. Image Generation](https://clawhub.ai/xrowgmbh/xrowgmbh-image-generation)

**Slug**: `xrowgmbh-image-generation`  
**Version**: 1.123.4  
**Stats**: ⭐ 1 | ⬇️ 6923 | 🧩 139

**原始简介**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

**中文介绍**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: or, Image, Generation, revise, document, PDF, web, review

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-image-generation)

---

## [20. CI Tools Pipeline](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-pipeline)

**Slug**: `xrowgmbh-ci-tools-pipeline`  
**Version**: 1.123.4  
**Stats**: ⭐ 0 | ⬇️ 4800 | 🧩 104

**原始简介**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

**中文介绍**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

Latest changelog:
- Removed `skill-card.md`.
- No changes to the CI pipeline guidance or skill instructions.

**关键词**: CI, CD, Tools, Pipeline, Build, maintain, GitLab, pipelines

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-pipeline)

---

## [21. GitLab Agent Self Improvement](https://clawhub.ai/xrowgmbh/xrowgmbh-self-improvement)

**Slug**: `xrowgmbh-self-improvement`  
**Version**: 1.123.4  
**Stats**: ⭐ 0 | ⬇️ 7704 | 🧩 176

**原始简介**: A skill for personal growth and self-improvement.

**中文介绍**: A skill for personal growth and self-improvement.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Self, Improvement, skill, personal, growth, self-improvement

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-self-improvement)

---

## [22. GitLab Hackathon](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-hackathon)

**Slug**: `xrowgmbh-gitlab-hackathon`  
**Version**: 1.123.4  
**Stats**: ⭐ 0 | ⬇️ 7101 | 🧩 170

**原始简介**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

**中文介绍**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

Latest changelog:
- Removed `skill-card.md`. No changes to the skill instructions.

**关键词**: GitLab, Hackathon, Plan, execute, fair, participation, including, Quarterly

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-hackathon)

---

## [23. Pet Vaccination Reminder (Facial Recognition) | 宠物疫苗接种到期提醒（面部识别）](https://clawhub.ai/smyx-sunjinhui/smyx-vaccination-reminder-analysis)

**Slug**: `smyx-vaccination-reminder-analysis`  
**Version**: 1.0.14  
**Stats**: ⭐ 0 | ⬇️ 2279 | 🧩 15

**原始简介**: Triggers when a user provides a pet facial image or video URL/file for vaccination reminder analysis; uses AI facial recognition to confirm pet identity, automatically queries the linked vaccination records (last dose date, vaccine type) from the hospital management database, and compares with current date. When the gap since last vaccination exceeds 11 months (or the preset reminder cycle), outputs a due/overdue reminder and suggests re-vaccination. Helps pet hospitals automate client management, raise vaccination coverage and avoid missed doses. Application: hospital front-desk registration, boarding center check-in, pet insurance underwriting. Does NOT provide medical advice — only returns database-comparison results. | 当用户提供宠物面部图像或视频URL/文件时，触发本技能进行疫苗到期提醒分析；利用AI面部识别确认宠物个体身份，自动关联数据库中该宠物的疫苗接种记录（上次接种日期、疫苗类型）并与当前日期比对；若距离上次接种超过11个月（或预设的提醒周期），输出到期/逾期提醒，并建议尽快补种。该技能可帮助宠物医院实现自动化客户管理、提升疫苗接种率、防止漏种。应用场景：宠物医院前台登记、宠物寄养中心入住检查、宠物保险核保。仅输出基于数据库比对的结果，不提供医疗建议。

**中文介绍**: Triggers when a user provides a pet facial image or video URL/file for vaccination reminder analysis; uses AI facial recognition to confirm pet identity, automatically queries the linked vaccination records (last dose date, vaccine type) from the hospital management database, and compares with current date. When the gap since last vaccination exceeds 11 months (or the preset reminder cycle), outputs a due/overdue reminder and suggests re-vaccination. Helps pet hospitals automate client management, raise vaccination coverage and avoid missed doses. Application: hospital front-desk registration, boarding center check-in, pet insurance underwriting. Does NOT provide medical advice — only returns database-comparison results. | 当用户提供宠物面部图像或视频URL/文件时，触发本技能进行疫苗到期提醒分析；利用AI面部识别确认宠物个体身份，自动关联数据库中该宠物的疫苗接种记录（上次接种日期、疫苗类型）并与当前日期比对；若距离上次接种超过11个月（或预设的提醒周期），输出到期/逾期提醒，并建议尽快补种。该技能可帮助宠物医院实现自动化客户管理、提升疫苗接种率、防止漏种。应用场景：宠物医院前台登记、宠物寄养中心入住检查、宠物保险核保。仅输出基于数据库比对的结果，不提供医疗建议。

Latest changelog:
- Updated the skill version from 1.0.17 to 1.0.20.
- Removed `skill-card.md`.

**关键词**: 宠物疫苗接种到期提醒（面部识别）, Pet, Vaccination, Reminder, Facial, Recognition, Triggers, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-vaccination-reminder-analysis)

---

## [24. reverse-any-video](https://clawhub.ai/heygen-com/reverse-any-video)

**Slug**: `reverse-any-video`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 20 | 🧩 1

**原始简介**: Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage. Measure and watch it, rebuild every layer, then check the render against the original frame by frame. Use to reverse, recreate, replicate or copy a video.

**中文介绍**: Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage. Measure and watch it, rebuild every layer, then check the render against the original frame by frame. Use to reverse, recreate, replicate or copy a video.

Latest changelog:
Initial release: Rebuild videos as editable HyperFrames projects and verify the render against the original.

- Added guidance for measuring video dimensions, frame rate, cuts, and frame-level changes.
- Defined how to rebuild components, sub-assets, and on-screen people while preserving the original audio.
- Added a workflow for checking, rendering, and diffing the project, plus documenting results for future resumption.

**关键词**: as, an, reverse-any-video, Rebuild, any, video, file, editable

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/reverse-any-video)

---

## [25. juicer-social-wall](https://clawhub.ai/juicer/juicer-social-wall)

**Slug**: `juicer-social-wall`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 244 | 🧩 4

**原始简介**: Run a live social media wall for your event. Collects posts with your hashtag from Instagram, TikTok, X and more, keeps anything embarrassing off the screen and lets you approve, hide and pin posts from chat.

**中文介绍**: Run a live social media wall for your event. Collects posts with your hashtag from Instagram, TikTok, X and more, keeps anything embarrassing off the screen and lets you approve, hide and pin posts from chat.

Latest changelog:
- Updated free-plan guidance: TikTok keyword sources now stop syncing after the trial, alongside TikTok hashtag, X, Reddit, and LinkedIn sources.
- Removed `skill-card.md`.

**关键词**: juicer-social-wall, Run, live, social, media, wall, event, Collects

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/juicer-social-wall)

---

