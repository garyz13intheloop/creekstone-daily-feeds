# ClawHub Skills Daily | 2026-10-13

> 共 25 个 skills

## [1. Paper Polisher Pro — AI Detector & Academic Polishing](https://clawhub.ai/docsor1212/paper-polisher-pro)

**Slug**: `paper-polisher-pro`  
**Version**: 5.4.0  
**Stats**: ⭐ 1 | ⬇️ 1940 | 🧩 26

**原始简介**: AI-rate self-check for academic writing, polish guidance (style, terminology, translation-smell), metaphor audit, quality report, AIGC compliance label check (China 2025-09 labeling rules), paragraph-level attribution, journal precheck, sentence-level rewrite suggestions (locates and advises, never auto-rewrites), plus `--batch DIR` for thesis-scale batch rewriting (per-file AI-rate scores directory-wide). Bilingual CN/EN, 100% local, zero upload, zero credentials; bundled unit-test suite + AST-based zero-network self-verification. v3 delivers a recalibrated multi-layer rule engine (11 core layers + discourse/smoothness heuristics) + token-spectrum layer + length-routed fusion + optional supervised Qwen3-0.6B ONNX layer (AUROC 1.0 on held-out test) + LLM fingerprint attribution (GLM/DeepSeek/Qwen/Kimi/MiniMax/GPT/Claude/Gemini) + freshness pipeline. Base-engine numbers reproduce from the bundled held-out evaluation; supervised columns are author-side measurements (model not bundled).

**中文介绍**: AI-rate self-check for academic writing, polish guidance (style, terminology, translation-smell), metaphor audit, quality report, AIGC compliance label check (China 2025-09 labeling rules), paragraph-level attribution, journal precheck, sentence-level rewrite suggestions (locates and advises, never auto-rewrites), plus `--batch DIR` for thesis-scale batch rewriting (per-file AI-rate scores directory-wide). Bilingual CN/EN, 100% local, zero upload, zero credentials; bundled unit-test suite + AST-based zero-network self-verification. v3 delivers a recalibrated multi-layer rule engine (11 core layers + discourse/smoothness heuristics) + token-spectrum layer + length-routed fusion + optional supervised Qwen3-0.6B ONNX layer (AUROC 1.0 on held-out test) + LLM fingerprint attribution (GLM/DeepSeek/Qwen/Kimi/MiniMax/GPT/Claude/Gemini) + freshness pipeline. Base-engine numbers reproduce from the bundled held-out evaluation; supervised columns are author-side measurements (model not bundled).

Latest changelog:
v5.4.0: journal-context release — journal precheck 2.0 (discipline detection with --discipline override plus per-discipline reading guide; the 20-25% reference line stays the cross-discipline convention and the tool states it does not invent per-discipline numbers); fingerprint freshness status (--status: last run, latest eval record, bit-exact drift check against the four published baselines, due indicator; pp.py freshness); binary-input guard (PDF/image/zip rejected with conversion advice instead of silent mojibake). 觉得有用的话，欢迎 Star（GitHub）或收藏（SkillHub 技能页）。

**关键词**: Paper, Polisher, Pro, Detector, Academic, Polishing, AI-rate, self-check

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paper-polisher-pro)

---

## [2. pubmed-verifier](https://clawhub.ai/docsor1212/pubmed-verifier)

**Slug**: `pubmed-verifier`  
**Version**: 4.4.0  
**Stats**: ⭐ 1 | ⬇️ 2185 | 🧩 33

**原始简介**: Reference checker for AI-fabricated citations: batch-verify PMIDs against PubMed and catch the hallucination existence checks miss — a REAL PMID pointing to a DIFFERENT paper. Five-state citation verification (correct / mismatch / partial / invalid / unknown), citation-context parsing, Crossref DOI cross-check, retraction detection (capped at partial), correct-PMID suggestion, arXiv ID verification, plain-text reference list parsing, formatted reference lists (GB/T 7714 / Vancouver / APA / AMA), OpenAlex DOI fallback for non-Crossref registries, Chinese-reference title search, CSV/JSON claims, HTML/JSON/text reports. Four data sources: NCBI, Europe PMC fallback, Crossref, OpenAlex. Network failures are honestly reported as unverified, never as "not found". Zero dependencies, runs fully local. Triggers: verify PMIDs, check citations, citation audit, reference check, PMID check, batch verify references, AI hallucination detection, verify DOI, DOI check, citation formatting, reference formatter, GB/T 7714.

**中文介绍**: Reference checker for AI-fabricated citations: batch-verify PMIDs against PubMed and catch the hallucination existence checks miss — a REAL PMID pointing to a DIFFERENT paper. Five-state citation verification (correct / mismatch / partial / invalid / unknown), citation-context parsing, Crossref DOI cross-check, retraction detection (capped at partial), correct-PMID suggestion, arXiv ID verification, plain-text reference list parsing, formatted reference lists (GB/T 7714 / Vancouver / APA / AMA), OpenAlex DOI fallback for non-Crossref registries, Chinese-reference title search, CSV/JSON claims, HTML/JSON/text reports. Four data sources: NCBI, Europe PMC fallback, Crossref, OpenAlex. Network failures are honestly reported as unverified, never as "not found". Zero dependencies, runs fully local. Triggers: verify PMIDs, check citations, citation audit, reference check, PMID check, batch verify references, AI hallucination detection, verify DOI, DOI check, citation formatting, reference formatter, GB/T 7714.

Latest changelog:
Submission evidence pack: --report-bundle DIR writes everything a journal or reviewer may ask for in one command — audit.json (replayable working-paper) + report.html + verified-refs.bib/.ris + audit-table.csv + references-gbt.txt + a self-describing manifest.txt; bundle files are byte-identical to their --export-* counterparts. The full 20-release history moved to references/CHANGELOG.md (main doc a third shorter). OpenAlex 429 retries back off at least 5s. 227 offline + 33 real-network tests green. 觉得有用的话，欢迎 Star（GitHub）或收藏（SkillHub 技能页）。

**关键词**: pubmed-verifier, Reference, checker, AI-fabricated, citations, batch-verify, PMIDs, against

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pubmed-verifier)

---

## [3. planetscale-cli-skills](https://clawhub.ai/vince-winkintel/planetscale-cli-skills)

**Slug**: `planetscale-cli-skills`  
**Version**: 1.0.33  
**Stats**: ⭐ 2 | ⬇️ 3704 | 🧩 29

**原始简介**: PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, keyspace parameters, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, dedicated read replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, keyspace, keyspace parameters, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, dedicated read replica, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

**中文介绍**: PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, keyspace parameters, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, dedicated read replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, keyspace, keyspace parameters, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, dedicated read replica, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

Latest changelog:
Cumulative pscale v0.344.0/v0.345.0 refresh: approved Postgres extension toggles, VTGate parameter rollouts, failed-operation retry, per-request aggressive cutover, schema-readiness recovery, parameter/size/auth guidance. All five review findings addressed, including whole-catalog single-document guards and timeout-stage distinctions.

**关键词**: planetscale-cli-skills, PlanetScale, CLI, command, reference, workflows, Use, authentication

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/planetscale-cli-skills)

---

## [4. HookPulse](https://clawhub.ai/wrpbr/hookpulse)

**Slug**: `hookpulse`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Monitor cron jobs, webhooks, backups and scheduled GitHub Actions workflows with HookPulse (hookpulse.net), a dead man's switch. Create a monitor with an interval or a cron schedule, import a crontab, send start, success and failure signals with the exit code, instrument a fleet with one setup key, and read monitor state, check-ins and the public status page. A missed or failed run alerts by e-mail or webhook. Use when a task mentions a cron job, crontab, scheduled task, heartbeat, dead man's switch, missed run, backup that stopped, or a GitHub Actions schedule.

**中文介绍**: Monitor cron jobs, webhooks, backups and scheduled GitHub Actions workflows with HookPulse (hookpulse.net), a dead man's switch. Create a monitor with an interval or a cron schedule, import a crontab, send start, success and failure signals with the exit code, instrument a fleet with one setup key, and read monitor state, check-ins and the public status page. A missed or failed run alerts by e-mail or webhook. Use when a task mentions a cron job, crontab, scheduled task, heartbeat, dead man's switch, missed run, backup that stopped, or a GitHub Actions schedule.

Latest changelog:
HookPulse 1.0.0. Source: https://github.com/wrpbr/hookpulse

**关键词**: HookPulse, Monitor, cron, jobs, webhooks, backups, scheduled, Actions

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hookpulse)

---

## [5. PageAudit](https://clawhub.ai/wrpbr/pageaudit)

**Slug**: `pageaudit`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Audit a web page's technical SEO with PageAudit (pageaudit.online) and get the fix. Check title, meta description, canonical, robots and sitemap, Open Graph, headings, structured data (JSON-LD), security headers and page delivery, with evidence and a ready patch for each finding. Compare a deploy preview with production by finding code, keep pages in tabs with history and a daily watch, and run a Lighthouse lab test. Use when a task mentions SEO, meta tags, Open Graph, JSON-LD, schema.org, canonical, robots.txt, a site audit, a page that dropped from search, or checking a preview deploy.

**中文介绍**: Audit a web page's technical SEO with PageAudit (pageaudit.online) and get the fix. Check title, meta description, canonical, robots and sitemap, Open Graph, headings, structured data (JSON-LD), security headers and page delivery, with evidence and a ready patch for each finding. Compare a deploy preview with production by finding code, keep pages in tabs with history and a daily watch, and run a Lighthouse lab test. Use when a task mentions SEO, meta tags, Open Graph, JSON-LD, schema.org, canonical, robots.txt, a site audit, a page that dropped from search, or checking a preview deploy.

Latest changelog:
PageAudit 1.0.0. Source: https://github.com/wrpbr/pageaudit

**关键词**: PageAudit, Audit, web, page's, technical, SEO, pageaudit.online, get

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pageaudit)

---

## [6. Pkg Paper Rewriter Claw](https://clawhub.ai/docsor1212/paper-rewriter)

**Slug**: `paper-rewriter`  
**Version**: 3.4.0  
**Stats**: ⭐ 0 | ⬇️ 1019 | 🧩 23

**原始简介**: Academic writing style toolkit, bilingual CN/EN: AI flavor scan and style-pattern self-check reports (scan reports are detection only), deterministic text cleanup (model artifacts, punctuation, filler phrases), integrity guardrails (numbers, DOIs, PMIDs, terminology must survive untouched), and agent-guided style naturalization for clearer, more natural academic prose (de-templating, de-translationese, rhythm, concreteness). Built for scholars whose formal writing reads stiff, templated or machine-flavored — especially non-native (ESL) authors. Includes AIGC-disclosure compliance checks (China 2025-09 labeling rules) and academic-integrity guardrails: this tool improves writing quality for self-review; it does not help misrepresent authorship, conceal required AI disclosure, or defeat integrity review. 100% local, zero upload, Python stdlib only. Related: paper-polisher-pro (broad polishing), pubmed-verifier, cite-holmes, academic-figures, cn-med-oa, doc-holmes.

**中文介绍**: Academic writing style toolkit, bilingual CN/EN: AI flavor scan and style-pattern self-check reports (scan reports are detection only), deterministic text cleanup (model artifacts, punctuation, filler phrases), integrity guardrails (numbers, DOIs, PMIDs, terminology must survive untouched), and agent-guided style naturalization for clearer, more natural academic prose (de-templating, de-translationese, rhythm, concreteness). Built for scholars whose formal writing reads stiff, templated or machine-flavored — especially non-native (ESL) authors. Includes AIGC-disclosure compliance checks (China 2025-09 labeling rules) and academic-integrity guardrails: this tool improves writing quality for self-review; it does not help misrepresent authorship, conceal required AI disclosure, or defeat integrity review. 100% local, zero upload, Python stdlib only. Related: paper-polisher-pro (broad polishing), pubmed-verifier, cite-holmes, academic-figures, cn-med-oa, doc-holmes.

Latest changelog:
v3.4.0: submission self-check bundle edition. New pipeline --bundle DIR generates a dated self-check package in one command - six files: style self-check report, revision audit log, before/after profile comparison, statistical consistency, terminology consistency, and the integrity verdict, plus a README - ready to hand to a supervisor or editor. The skill description is rewritten to match what you actually search for; --rewrite x --deep combination fixed; bundle failures now degrade gracefully without affecting the main report. 500+ offline tests green across fourteen suites, zero dependencies. Star on GitHub or bookmark the SkillHub page if you find it useful.

**关键词**: Pkg, Paper, Rewriter, Claw, Academic, writing, style, toolkit

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paper-rewriter)

---

## [7. Google Trends (fast API)](https://clawhub.ai/heocoi/heocoi-google-trends)

**Slug**: `heocoi-google-trends`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Get Google Trends data (interest over time, interest by region, related queries, Trending Now) for up to 5 keywords. Web, YouTube, News, Images or Shopping search. Use when the user asks what is trending, compares search interest, or checks demand for a keyword.

**中文介绍**: Get Google Trends data (interest over time, interest by region, related queries, Trending Now) for up to 5 keywords. Web, YouTube, News, Images or Shopping search. Use when the user asks what is trending, compares search interest, or checks demand for a keyword.

Latest changelog:
First release: interest over time, by region, related queries, Trending Now via the heocoi/google-trends-api Apify Actor.

**关键词**: API, Google, Trends, fast, Get, data, interest, over

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/heocoi-google-trends)

---

## [8. google-trends](https://clawhub.ai/skills?q=google-trends)

**Slug**: `google-trends`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Get Google Trends data (interest over time, interest by region, related queries, Trending Now) for up to 5 keywords. Web, YouTube, News, Images or Shopping search. Use when the user asks what is trending, compares search interest, or checks demand for a keyword.

**中文介绍**: Get Google Trends data (interest over time, interest by region, related queries, Trending Now) for up to 5 keywords. Web, YouTube, News, Images or Shopping search. Use when the user asks what is trending, compares search interest, or checks demand for a keyword.

Latest changelog:
First release: interest over time, by region, related queries, Trending Now via the heocoi/google-trends-api Apify Actor.

**关键词**: google-trends, Get, Google, Trends, data, interest, over, time

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/google-trends)

---

## [9. gitlab-cli-skills](https://clawhub.ai/vince-winkintel/gitlab-cli-skills)

**Slug**: `gitlab-cli-skills`  
**Version**: 1.13.32  
**Stats**: ⭐ 7 | ⬇️ 8927 | 🧩 51

**原始简介**: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

**中文介绍**: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

Latest changelog:
glab v1.123.0: subgroup clone exclusions, guarded SSH-key replacement, issue time tracking, JSON API input, token registry-domain persistence, list totals/visibility, fail-closed Dependency Firewall, and curated remote Orbit skills. Includes all 10 validated review remediations.

**关键词**: gitlab-cli-skills, Comprehensive, GitLab, CLI, glab, command, reference, workflows

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gitlab-cli-skills)

---

## [10. Iterate](https://clawhub.ai/jingzhao-l/iterate-skill)

**Slug**: `iterate-skill`  
**Version**: 3.5.0  
**Stats**: ⭐ 0 | ⬇️ 2640 | 🧩 55

**原始简介**: Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

**中文介绍**: Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

Latest changelog:
**Major update with significant codebase reorganization and kernel removal.**

- Removed all kernel-related files and legacy fixtures, consolidating the codebase and reducing maintenance overhead.
- Refined and updated documentation, including README, contribution, design, and release files.
- Several scripts, tests, and outdated utility files removed or streamlined.
- Schema and configuration management improved for better consistency.
- Version bumped to 3.5.0 to reflect major internal changes.

**关键词**: Iterate, Fully, automated, multi-round, code, iteration, configurable, N-dimension

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iterate-skill)

---

## [11. agentshield](https://clawhub.ai/bartelmost/agentshield-audit)

**Slug**: `agentshield-audit`  
**Version**: 1.5.13  
**Stats**: ⭐ 0 | ⬇️ 2899 | 🧩 37

**原始简介**: Privacy-First security audit with 77 local tests (52 live + 25 static). Works with OpenClaw, Hermes Agent, n8n (auto-detected), LangChain, and any AI agent platform. Ed25519 private keys stay local. All scripts bundled.

**中文介绍**: Privacy-First security audit with 77 local tests (52 live + 25 static). Works with OpenClaw, Hermes Agent, n8n (auto-detected), LangChain, and any AI agent platform. Ed25519 private keys stay local. All scripts bundled.

Latest changelog:
v1.5.13 handshake and verify fixes

**关键词**: agentshield, Privacy-First, security, audit, local, tests, live, static

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentshield-audit)

---

## [12. Loboot](https://clawhub.ai/whitekiwi/loboot)

**Slug**: `loboot`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Safely manage and diagnose Loboot native user services.

**中文介绍**: Safely manage and diagnose Loboot native user services.

Latest changelog:
Initial release of the loboot skill.

- Provides safe preview, inspection, creation, update, enable/disable, start/stop, removal, and diagnosis workflows for Loboot-managed user services on macOS (launchd) or Linux (systemd).
- Strictly separates definitions, activation preferences, and live runtime state; requires explicit authorization for any change.
- Mandates dry-run previews, direct argument specification, and manifest validation for all mutations.
- Supports offline sandbox operations for cross-platform planning or testing.
- Includes detailed guidance for error handling, platform quirks, and separate reporting of evidence for each workflow step.

**关键词**: Loboot, Safely, manage, diagnose, native, user, services, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/loboot)

---

## [13. phd-research-companion](https://clawhub.ai/yue123161/phd-research-companion)

**Slug**: `phd-research-companion`  
**Version**: 1.0.3  
**Stats**: ⭐ 1 | ⬇️ 994 | 🧩 4

**原始简介**: Full-lifecycle research management for CS PhD students — literature search over real APIs, LaTeX skeletons that compile, proof ledgers, priority checks, exact-arithmetic certificates, revision tracking and pre-submission audit. Use when a research project needs to be set up, tracked, checked for nov

**中文介绍**: Full-lifecycle research management for CS PhD students — literature search over real APIs, LaTeX skeletons that compile, proof ledgers, priority checks, exact-arithmetic certificates, revision tracking and pre-submission audit. Use when a research project needs to be set up, tracked, checked for nov

Latest changelog:
**Major update: Skill refactored for cross-platform compatibility, expanded theory tooling, and stricter traceability.**

- Replaces bash-only `./run` with cross-platform `python run.py`, ensuring compatibility on all systems.
- Adds and documents the theory track: proof ledger, novelty (priority) checker, certificate generation, claim auditing, and session persistence.
- Enforces NO placeholder output: every failure or missing data is explicitly reported; nothing is silently fabricated or skipped.
- All command scripts now located and listed clearly; output and project directory conventions standardized (`-p`, `-o`).
- Literature search, analysis, experiment design, LaTeX template generation, and revision tools now guarantee explicit error reporting and integrity checks.
- Removed unused files; all new commands have associated scripts and documentation.

**关键词**: CS, phd-research-companion, Full-lifecycle, research, management, PhD, students, literature

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phd-research-companion)

---

## [14. hd2-mod-authoring](https://clawhub.ai/cavadus/hd2-mod-authoring)

**Slug**: `hd2-mod-authoring`  
**Version**: 0.1.8  
**Stats**: ⭐ 0 | ⬇️ 302 | 🧩 9

**原始简介**: Helldivers 2 mod, Arsenal install, Bingus lua patch, Wwise sound-bank swap, Nexus unlink, an HD2 Mod Manager install that dies on the manifest Name, translating on-screen text in a glyph-atlas HUD, drawing a live HUD overlay with the game font, a bundled .patch_0 whose type at 0x50 is not Lua, the whole HUD freezes after the stratagem list and death does not clear it, Bingus reports more than 200 local variables or more than 60 upvalues, the realistic log says 4 spare magazines while the gun still shows 6, the weapon search ends a round at 256 MB after ProjectileWeapon, the magazine write refuses because capacity reads 0, the log says explosion table not found, the log says explosion on impact 0 -> 388 while a close SAFE shot still detonates, black squares after the impact id moves onto a spare explosion slot, the Dominator thumbnail still lists only the 380 m/s specs, a pytest check of the magazine index or explosion tail without launching the game, or statically vetting a downloaded HD2 mod manager/tool for malware before running it: classify the install, conflict-check writers of the same value, then edit, pack, and verify from the game log.

**中文介绍**: Helldivers 2 mod, Arsenal install, Bingus lua patch, Wwise sound-bank swap, Nexus unlink, an HD2 Mod Manager install that dies on the manifest Name, translating on-screen text in a glyph-atlas HUD, drawing a live HUD overlay with the game font, a bundled .patch_0 whose type at 0x50 is not Lua, the whole HUD freezes after the stratagem list and death does not clear it, Bingus reports more than 200 local variables or more than 60 upvalues, the realistic log says 4 spare magazines while the gun still shows 6, the weapon search ends a round at 256 MB after ProjectileWeapon, the magazine write refuses because capacity reads 0, the log says explosion table not found, the log says explosion on impact 0 -> 388 while a close SAFE shot still detonates, black squares after the impact id moves onto a spare explosion slot, the Dominator thumbnail still lists only the 380 m/s specs, a pytest check of the magazine index or explosion tail without launching the game, or statically vetting a downloaded HD2 mod manager/tool for malware before running it: classify the install, conflict-check writers of the same value, then edit, pack, and verify from the game log.

Latest changelog:
Forward-declared local shadowed by a later local function (the Dominator late-traits root cause); SHODAN chain-walk census; VG-70 label via LoadoutEntry locator.

**关键词**: hd2-mod-authoring, Helldivers, mod, Arsenal, install, Bingus, lua, patch

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hd2-mod-authoring)

---

## [15. Bird Recognition Tool | 鸟类识别工具](https://clawhub.ai/18072937735/smyx-bird-recognition-analysis)

**Slug**: `smyx-bird-recognition-analysis`  
**Version**: 1.0.23  
**Stats**: ⭐ 5 | ⬇️ 2336 | 🧩 24

**原始简介**: Identifies bird species in images/videos of target areas. Supports recognition of no less than 500 common bird species, supports customized model training, suitable for ecological observation, garden bird watching and other scenarios. | 鸟类识别工具，识别目标区域图片/视频中的鸟类种类，支持不低于500种常见鸟类识别，支持定制化模型训练，适用于生态观测、庭院观鸟等场景

**中文介绍**: Identifies bird species in images/videos of target areas. Supports recognition of no less than 500 common bird species, supports customized model training, suitable for ecological observation, garden bird watching and other scenarios. | 鸟类识别工具，识别目标区域图片/视频中的鸟类种类，支持不低于500种常见鸟类识别，支持定制化模型训练，适用于生态观测、庭院观鸟等场景

Latest changelog:
Version 1.0.23 Changelog

- Updated skill documentation (SKILL.md) with minor metadata changes (version field updated from 1.0.17 to 1.0.19).
- Removed the skill-card.md file from the repository.
- No core functionality changes; documentation only.

**关键词**: 鸟类识别工具, Bird, Recognition, Tool, Identifies, species, images, videos

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-bird-recognition-analysis)

---

## [16. vps-lite-boot](https://clawhub.ai/thinhbuiii/vps-lite-boot)

**Slug**: `vps-lite-boot`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Tối ưu máy chủ: hạ tải + chống OOM cho VPS yếu (2GB RAM), hạ maxConcurrent, thêm swap, chống OOM killer giết gateway.

**中文介绍**: Tối ưu máy chủ: hạ tải + chống OOM cho VPS yếu (2GB RAM), hạ maxConcurrent, thêm swap, chống OOM killer giết gateway.

Latest changelog:
vps-lite-boot 1.0.2

- No code or documentation changes detected in this release.
- The SKILL.md remains unchanged compared to the previous version.
- Content, instructions, and usage scope are consistent with version 1.0.1.

**关键词**: Tối, ưu, máy, chủ, hạ, tải, vps-lite-boot, chống

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vps-lite-boot)

---

## [17. fix-plan](https://clawhub.ai/drumrobot/fix-plan)

**Slug**: `fix-plan`  
**Version**: 0.17.2  
**Stats**: ⭐ 0 | ⬇️ 2369 | 🧩 27

**原始简介**: fix_plan.md / checklist.md schema and lifecycle management. Topics — format ([ ]/[x]/[BLOCKED] markers, Progress/Completed sections), priority (P0-P3 BLOCKED suffix + external/selfable classification), add (Action/Why/How authoring), update (flip marker / note / `[KEY:VALUE]` attr), upsert (dup-check → update in place or fall back to add), draft (deferred plan stub → promote via code-workflow), move ([x] → Completed summary, subtree partial completion), sync (gh pr/issue state polling → auto-check), issue-drafts (write → publish → archive → delete), model-triage (fit + dedicated section), completion-criteria (DoD + marker rules). Default (no args): move (or archive-receiver) → format → sync → priority → flowchart-sync (incl. pinned-mission liveness check), scoped by role-profile (--role=pm|deep|impl). Use when: "fix_plan", "checklist", "BLOCKED priority", "triage blocked", "fix-plan sync", "issue draft cleanup", "fix-plan draft", "fix-plan default", "fix-plan archive", "model triage", "completion criteria", "role profile", "--role", "orca session launch", "fix-plan upsert", "dup check tracker", "pinned mission liveness", "pinned-backing", "set-attr".

**中文介绍**: fix_plan.md / checklist.md schema and lifecycle management. Topics — format ([ ]/[x]/[BLOCKED] markers, Progress/Completed sections), priority (P0-P3 BLOCKED suffix + external/selfable classification), add (Action/Why/How authoring), update (flip marker / note / `[KEY:VALUE]` attr), upsert (dup-check → update in place or fall back to add), draft (deferred plan stub → promote via code-workflow), move ([x] → Completed summary, subtree partial completion), sync (gh pr/issue state polling → auto-check), issue-drafts (write → publish → archive → delete), model-triage (fit + dedicated section), completion-criteria (DoD + marker rules). Default (no args): move (or archive-receiver) → format → sync → priority → flowchart-sync (incl. pinned-mission liveness check), scoped by role-profile (--role=pm|deep|impl). Use when: "fix_plan", "checklist", "BLOCKED priority", "triage blocked", "fix-plan sync", "issue draft cleanup", "fix-plan draft", "fix-plan default", "fix-plan archive", "model triage", "completion criteria", "role profile", "--role", "orca session launch", "fix-plan upsert", "dup check tracker", "pinned mission liveness", "pinned-backing", "set-attr".

Latest changelog:
fix-plan 0.17.2

- Removed obsolete skill-card.md file.
- Updated pinned liveness check script and its test to reflect recent changes.
- Minor updates to the changelog and documentation files.

**关键词**: fix-plan, fix, plan.md, checklist.md, schema, lifecycle, management, Topics

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/fix-plan)

---

## [18. consolidate](https://clawhub.ai/drumrobot/consolidate)

**Slug**: `consolidate`  
**Version**: 0.8.1  
**Stats**: ⭐ 0 | ⬇️ 2745 | 🧩 27

**原始简介**: Consolidate and respond to external feedback on PRs/issues. Topics — pr (workflow entrypoint + skip conditions), collect (gather AI reviews + superpowers load), internal (Internal Code Review fallback + UI capture), classify (dual-label Type|Severity + diff scope check), decide (user decision: findings + Formal Review), post (Summary + Formal Review + status + deferred), next (post-summary next-action ask). Use when: "review consolidate", "PR review", "AI review", "CodeRabbit review", "Copilot review", "review check", "review summary", "merge ready", "internal review", "code-reviewer", "inline review", "line-level comment", "PR line review".

**中文介绍**: Consolidate and respond to external feedback on PRs/issues. Topics — pr (workflow entrypoint + skip conditions), collect (gather AI reviews + superpowers load), internal (Internal Code Review fallback + UI capture), classify (dual-label Type|Severity + diff scope check), decide (user decision: findings + Formal Review), post (Summary + Formal Review + status + deferred), next (post-summary next-action ask). Use when: "review consolidate", "PR review", "AI review", "CodeRabbit review", "Copilot review", "review check", "review summary", "merge ready", "internal review", "code-reviewer", "inline review", "line-level comment", "PR line review".

Latest changelog:
consolidate v0.8.1

- Updated documentation in SKILL.md, clarifying interactive review flows and keyword-triggered auto-activation.
- Removed obsolete file: skill-card.md.
- Minor adjustments to supporting scripts and process documentation for maintainability and accuracy.
- No user-facing feature changes.

**关键词**: pr, consolidate, respond, external, feedback, PRs, issues, Topics

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/consolidate)

---

## [19. github-flow](https://clawhub.ai/drumrobot/github-flow)

**Slug**: `github-flow`  
**Version**: 0.11.4  
**Stats**: ⭐ 0 | ⬇️ 2658 | 🧩 24

**原始简介**: GitHub issue/PR workflow automation. Topics — auth-scope (gh CLI priority + account mapping + batch scope refresh + 404 checklist), commit-message-discipline (commit message authoring + amend refresh + PUBLIC English enforcement), dependencies (blocked-by/sub-issues via GraphQL), epic-bundle (deferred findings → Epic + sub-issues), expand (expand-vs-split mid-work), identity-auth (gh account map + scope refresh + GH_TOKEN fallback), merge (CI/review gates + no autonomous push), plan-to-issue (MD → issue body), pr (PR with test plan), publish (branch + draft PR + CI watch + ready + merge, one topic), push-guards (branch/push-reject/force-push/main-push), register (dup check + strategy), review (structured comments), review-apply (deferred feedback apply), sanitize (PUBLIC repo personal data scan), upstream-issue (external OSS feature/bug). Use when: "plan to issue", "issue register", "create PR", "PR body", "code review", "merge PR", "PR squash", "sanitize", "PII", "expand PR", "blocked by", "epic bundle", "upstream issue", "review apply", "sub-issue", "gh auth", "force push", "push reject", "branch change forbid", "auth scope", "account mapping", "scope refresh", "commit message", "PUBLIC repo English".

**中文介绍**: GitHub issue/PR workflow automation. Topics — auth-scope (gh CLI priority + account mapping + batch scope refresh + 404 checklist), commit-message-discipline (commit message authoring + amend refresh + PUBLIC English enforcement), dependencies (blocked-by/sub-issues via GraphQL), epic-bundle (deferred findings → Epic + sub-issues), expand (expand-vs-split mid-work), identity-auth (gh account map + scope refresh + GH_TOKEN fallback), merge (CI/review gates + no autonomous push), plan-to-issue (MD → issue body), pr (PR with test plan), publish (branch + draft PR + CI watch + ready + merge, one topic), push-guards (branch/push-reject/force-push/main-push), register (dup check + strategy), review (structured comments), review-apply (deferred feedback apply), sanitize (PUBLIC repo personal data scan), upstream-issue (external OSS feature/bug). Use when: "plan to issue", "issue register", "create PR", "PR body", "code review", "merge PR", "PR squash", "sanitize", "PII", "expand PR", "blocked by", "epic bundle", "upstream issue", "review apply", "sub-issue", "gh auth", "force push", "push reject", "branch change forbid", "auth scope", "account mapping", "scope refresh", "commit message", "PUBLIC repo English".

Latest changelog:
- Updated documentation in CHANGELOG.md and merge.md to clarify workflow or rules.
- Removed the file skill-card.md.
- No behavioral changes; modifications are limited to documentation updates and cleanup.

**关键词**: PR, gh, github-flow, issue, workflow, automation, Topics, auth-scope

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/github-flow)

---

## [20. orca](https://clawhub.ai/drumrobot/orca)

**Slug**: `orca`  
**Version**: 0.5.1  
**Stats**: ⭐ 0 | ⬇️ 652 | 🧩 7

**原始简介**: Launch and coordinate agent sessions inside the Orca IDE runtime (stablyai/orca). Topics: send - find a running Orca terminal by title/preview/worktree and deliver a prompt to it, always disambiguating with a question when more than one candidate matches and never targeting the caller's own pane [send.md]. launch - start a new agent session (claude, antigravity, openclaw, codex, and 30+ other supported agents) in a fresh or existing worktree [launch.md]. install - install the stablyai/orca skill bundle into Claude Code, OpenClaw, or Antigravity, asking whether to ghq-clone + symlink or use a plain marketplace install [install.md]. Use when: "send this to the claude session working on X", "hand this off to another agent in Orca", "spawn a new codex/antigravity worktree", "which Orca terminal is running Y", "install the orca skills into openclaw/antigravity", "Orca worktree", "Orca terminal send".

**中文介绍**: Launch and coordinate agent sessions inside the Orca IDE runtime (stablyai/orca). Topics: send - find a running Orca terminal by title/preview/worktree and deliver a prompt to it, always disambiguating with a question when more than one candidate matches and never targeting the caller's own pane [send.md]. launch - start a new agent session (claude, antigravity, openclaw, codex, and 30+ other supported agents) in a fresh or existing worktree [launch.md]. install - install the stablyai/orca skill bundle into Claude Code, OpenClaw, or Antigravity, asking whether to ghq-clone + symlink or use a plain marketplace install [install.md]. Use when: "send this to the claude session working on X", "hand this off to another agent in Orca", "spawn a new codex/antigravity worktree", "which Orca terminal is running Y", "install the orca skills into openclaw/antigravity", "Orca worktree", "Orca terminal send".

Latest changelog:
orca 0.5.1

- Added new scripts and tests for handling "ask" and "split" options when blocking Orca new tab behavior.
- Removed the deprecated skill-card.md documentation file.
- Updated existing scripts and tests for improved handling of split/ask logic in tab checks.
- Added dedicated test coverage for pending behavioral issues (test_pr623_orca_pending.py).

**关键词**: Agent, orca, Launch, coordinate, sessions, inside, IDE, runtime

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/orca)

---

## [21. cleanup](https://clawhub.ai/drumrobot/cleanup)

**Slug**: `cleanup`  
**Version**: 0.10.0  
**Stats**: ⭐ 0 | ⬇️ 809 | 🧩 11

**原始简介**: Run the self-improving loop before session end. config - enable/disable individual tasks [config.md], hook-review - review hook errors and suggest improvements [hook-review.md], rag-store - persist to RAG before session end + sync fix_plan completed items to RAG (medium matrix fallback) [rag-store.md], run - 5-step sequential execution pipeline, entry point and Steps 0-1 [run.md]; its step bodies live in run-self-improve.md (Step 2), run-knowledge-persist.md (Step 3), run-checklist-sync.md (Steps 4/4.5) and run-wip-handoff.md (Steps 5/5.5). Mistake recording (retrospect) and FA pruning moved to the fa skill — invoke Skill("fa") / Skill("fa", "fa-prune"). Supports Ralph mode (records to improvements.md instead of AskUserQuestion). Use on "wrap up", "session cleanup", "end session", "cleanup", "record mistake", "save feedback", "improve", "retrospect", "hook error", "next action", "RAG store", "qdrant store", "fix_plan sync", "cleanup --auto", "cleanup --ralph", "auto mode", "ralph mode".

**中文介绍**: Run the self-improving loop before session end. config - enable/disable individual tasks [config.md], hook-review - review hook errors and suggest improvements [hook-review.md], rag-store - persist to RAG before session end + sync fix_plan completed items to RAG (medium matrix fallback) [rag-store.md], run - 5-step sequential execution pipeline, entry point and Steps 0-1 [run.md]; its step bodies live in run-self-improve.md (Step 2), run-knowledge-persist.md (Step 3), run-checklist-sync.md (Steps 4/4.5) and run-wip-handoff.md (Steps 5/5.5). Mistake recording (retrospect) and FA pruning moved to the fa skill — invoke Skill("fa") / Skill("fa", "fa-prune"). Supports Ralph mode (records to improvements.md instead of AskUserQuestion). Use on "wrap up", "session cleanup", "end session", "cleanup", "record mistake", "save feedback", "improve", "retrospect", "hook error", "next action", "RAG store", "qdrant store", "fix_plan sync", "cleanup --auto", "cleanup --ralph", "auto mode", "ralph mode".

Latest changelog:
cleanup 0.10.0

- Added resources/graph-stop-evaluator.sh script.
- Updated CHANGELOG.md and block-cleanup-without-rag.sh.
- Removed skill-card.md.

**关键词**: cleanup, Run, self-improving, loop, before, session, end, config

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cleanup)

---

## [22. cc-plugin](https://clawhub.ai/drumrobot/cc-plugin)

**Slug**: `cc-plugin`  
**Version**: 0.8.2  
**Stats**: ⭐ 0 | ⬇️ 2133 | 🧩 18

**原始简介**: Claude Code plugin lifecycle management. cache - clean old cache versions (cleanup only — NOT for cache miss diagnosis) [cache.md], clustering - skill affinity scoring (coupling/dep/hook-ownership) → plugin bundle membership [clustering.md], create - plugin authoring guide (structure, plugin.json, components) [create.md], dev-reflect - reflect local dev repo into marketplace clone for pre-push testing [dev-reflect.md], hud - OMC HUD statusline (omcHud elements, omcLabel, wrapper sed fallback) [hud.md], marketplace - clone/list/update marketplace repos [marketplace.md], troubleshoot - cache miss/error, install fail, cache sync, HUD diagnostics — ALL plugin errors route here [troubleshoot.md]. "plugin", "marketplace", "plugin install", "plugin not installed", "cache miss", "cache error", "plugin error", "load error", "reload errors", "dev reflect", "plugin clustering", "bundle skills", "skill affinity", "OMC HUD", "omcHud", "omcLabel", "statusline", "[OMC#" triggers.

**中文介绍**: Claude Code plugin lifecycle management. cache - clean old cache versions (cleanup only — NOT for cache miss diagnosis) [cache.md], clustering - skill affinity scoring (coupling/dep/hook-ownership) → plugin bundle membership [clustering.md], create - plugin authoring guide (structure, plugin.json, components) [create.md], dev-reflect - reflect local dev repo into marketplace clone for pre-push testing [dev-reflect.md], hud - OMC HUD statusline (omcHud elements, omcLabel, wrapper sed fallback) [hud.md], marketplace - clone/list/update marketplace repos [marketplace.md], troubleshoot - cache miss/error, install fail, cache sync, HUD diagnostics — ALL plugin errors route here [troubleshoot.md]. "plugin", "marketplace", "plugin install", "plugin not installed", "cache miss", "cache error", "plugin error", "load error", "reload errors", "dev reflect", "plugin clustering", "bundle skills", "skill affinity", "OMC HUD", "omcHud", "omcLabel", "statusline", "[OMC#" triggers.

Latest changelog:
- Updated CHANGELOG.md and scripts/dev-reflect.sh
- Removed skill-card.md file
- No changes to user-facing functionality or documentation

**关键词**: cc-plugin, Claude, Code, plugin, lifecycle, management, cache, clean

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cc-plugin)

---

## [23. ArcBounty / BaseBounty / NadBounty](https://clawhub.ai/sofiia7/arcbounty)

**Slug**: `arcbounty`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 292 | 🧩 3

**原始简介**: Work with NadBounty (Monad), BaseBounty (Base) and ArcBounty (Arc), one on-chain USDC bounty marketplace (ERC-8183 escrow + ERC-8004 identity/reputation) where humans and AI agents take the same paid tasks; NadBounty adds encrypted contests and identity-owner payouts. Use when discovering open bounties, taking/submitting work as an agent, entering or running a contest, posting a bounty, checking payout/dispute status, or integrating the arcbounty-agent-sdk / nadbounty-mcp / basebounty-mcp / arcbounty-mcp / facade API. Triggers on "NadBounty", "nadbounty.app", "BaseBounty", "ArcBounty", "basebounty.app", "arcbounty.app", "bounty on Monad", "bounty on Base", "bounty on Arc", "BountyAdapter", or a request to find/complete paid tasks for an AI agent.

**中文介绍**: Work with NadBounty (Monad), BaseBounty (Base) and ArcBounty (Arc), one on-chain USDC bounty marketplace (ERC-8183 escrow + ERC-8004 identity/reputation) where humans and AI agents take the same paid tasks; NadBounty adds encrypted contests and identity-owner payouts. Use when discovering open bounties, taking/submitting work as an agent, entering or running a contest, posting a bounty, checking payout/dispute status, or integrating the arcbounty-agent-sdk / nadbounty-mcp / basebounty-mcp / arcbounty-mcp / facade API. Triggers on "NadBounty", "nadbounty.app", "BaseBounty", "ArcBounty", "basebounty.app", "arcbounty.app", "bounty on Monad", "bounty on Base", "bounty on Arc", "BountyAdapter", or a request to find/complete paid tasks for an AI agent.

Latest changelog:
Adds NadBounty on Monad: encrypted contests, identity-owner payouts, nadbounty-mcp

**关键词**: ArcBounty, BaseBounty, NadBounty, Work, Monad, Base, Arc, one

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/arcbounty)

---

## [24. BulkPublish: Check Quota](https://clawhub.ai/azeemkafridi/bulkpublish-check-quota)

**Slug**: `bulkpublish-check-quota`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Check BulkPublish plan limits and current usage. Use when the user asks about their plan, limits, or remaining quota.

**中文介绍**: Check BulkPublish plan limits and current usage. Use when the user asks about their plan, limits, or remaining quota.

Latest changelog:
- Initial release of the BulkPublish quota checking skill.
- Lets users check their current plan, usage, and all relevant limits in BulkPublish.
- Returns detailed information about: plan type, resource limits, current usage, and subscription status.
- Supports free, Pro, LTD, and Business plans with resource-specific quotas.
- Includes a full reference table for plan limits and features.

**关键词**: BulkPublish, Check, Quota, plan, limits, current, usage, Use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bulkpublish-check-quota)

---

## [25. BulkPublish: Manage Inbox](https://clawhub.ai/azeemkafridi/bulkpublish-manage-inbox)

**Slug**: `bulkpublish-manage-inbox`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Read, triage and answer BulkPublish Inbox conversations (DMs, reviews, comment threads) and comments on published posts. Use when the user asks about messages, DMs, reviews, comments, replies, or wants to clear, assign or moderate their inbox.

**中文介绍**: Read, triage and answer BulkPublish Inbox conversations (DMs, reviews, comment threads) and comments on published posts. Use when the user asks about messages, DMs, reviews, comments, replies, or wants to clear, assign or moderate their inbox.

Latest changelog:
- Initial release of the BulkPublish Inbox management skill.
- Enables reading, triaging, and replying to conversations (DMs, reviews, comment threads) and moderating comments from connected accounts.
- Strict confirmation required for every sent reply or deletion—always show details and seek user approval.
- Supports filtering, assignment, archiving, and moderation actions (like, hide, delete) on conversations and post comments.
- Clear user guidance provided on permission, plan, and network limitations.

**关键词**: BulkPublish, Manage, Inbox, Read, triage, answer, conversations, DMs

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bulkpublish-manage-inbox)

---

