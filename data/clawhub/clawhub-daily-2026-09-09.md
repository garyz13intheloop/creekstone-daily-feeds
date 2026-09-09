# ClawHub Skills Daily | 2026-09-09

> 共 25 个 skills

## [1. Hyperliquid Trading Place](https://clawhub.ai/polyparlay/hyperliquid-trading-place)

**Slug**: `hyperliquid-trading-place`  
**Version**: 1.0.21  
**Stats**: ⭐ 0 | ⬇️ 181 | 🧩 22

**原始简介**: Place Hyperliquid perps on explicit trade intent. ALWAYS run scripts/setup.mjs after install (wires MCP + OpenBroker ApproveBuilderFee). Refuses place until maxBuilderFee>=10. Install: clawhub install hyperliquid-trading-place then cd skills/hyperliquid-trading-place/scripts && npm install && node setup.mjs. Keywords: hyperliquid trading, hyperliquid place, cancel close hl_place_order perps openclaw mcp builder.

**中文介绍**: Place Hyperliquid perps on explicit trade intent. ALWAYS run scripts/setup.mjs after install (wires MCP + OpenBroker ApproveBuilderFee). Refuses place until maxBuilderFee>=10. Install: clawhub install hyperliquid-trading-place then cd skills/hyperliquid-trading-place/scripts && npm install && node setup.mjs. Keywords: hyperliquid trading, hyperliquid place, cancel close hl_place_order perps openclaw mcp builder.

Latest changelog:
Companion: setup.mjs + lock rail@0.1.23 required post-install (MCP wire + ApproveBuilderFee).

**关键词**: Hyperliquid, Trading, Place, perps, explicit, trade, intent, ALWAYS

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hyperliquid-trading-place)

---

## [2. Hyperliquid Trading Place](https://clawhub.ai/polyparlay/hyperliquid-place)

**Slug**: `hyperliquid-place`  
**Version**: 1.3.50  
**Stats**: ⭐ 1 | ⬇️ 440 | 🧩 61

**原始简介**: Place Hyperliquid perps on explicit trade/place/execute intent. ALWAYS run scripts/setup.mjs after install (wires MCP + OpenBroker ApproveBuilderFee). Always attaches builder 1bp (0x9548…). Refuses place until maxBuilderFee>=10 (no silent $0). Install: clawhub install hyperliquid-place then cd skills/hyperliquid-place/scripts && npm install && node setup.mjs. Keywords: hyperliquid trading, hyperliquid place, cancel close hl_place_order perps openclaw mcp builder.

**中文介绍**: Place Hyperliquid perps on explicit trade/place/execute intent. ALWAYS run scripts/setup.mjs after install (wires MCP + OpenBroker ApproveBuilderFee). Always attaches builder 1bp (0x9548…). Refuses place until maxBuilderFee>=10 (no silent $0). Install: clawhub install hyperliquid-place then cd skills/hyperliquid-place/scripts && npm install && node setup.mjs. Keywords: hyperliquid trading, hyperliquid place, cancel close hl_place_order perps openclaw mcp builder.

Latest changelog:
Lock+setup.mjs REQUIRED: npm install && node setup.mjs wires MCP + OpenBroker ApproveBuilderFee; pin @hypelens/hypelens-agent-rail@0.1.23; refuse place until maxBuilderFee>=10. Install≠fees without this step.

**关键词**: Hyperliquid, Trading, Place, perps, explicit, trade, execute, intent

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hyperliquid-place)

---

## [3. x402-trust-check](https://clawhub.ai/aladaf/x402-trust-check)

**Slug**: `x402-trust-check`  
**Version**: 1.0.2  
**Stats**: ⭐ 1 | ⬇️ 212 | 🧩 3

**原始简介**: Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

**中文介绍**: Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

Latest changelog:
- Added a new field, `retired_resources`, indicating endpoints deliberately retired with HTTP 410 and a Sunset date. Clarifies handling for such resources.
- Updated decision policy: if a call returns `410 Gone` with a `Sunset` header, do not retry and follow any successor link provided.
- Removed skill-card.md from the project.  
- Version bumped from 1.1.0 to 1.2.0.

**关键词**: of, x402, x402-trust-check, Check, trust, rating, any, service

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x402-trust-check)

---

## [4. Polymarket Place](https://clawhub.ai/polyparlay/polymarket-place)

**Slug**: `polymarket-place`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 11 | 🧩 2

**原始简介**: Place, cancel, or bet on Polymarket prediction markets when the user explicitly asks to trade/place/bet/cancel/execute. CLOB V2 orders always include builderCode (POLYMARKET_BUILDER_CODE) for builder fee attribution. Install: clawhub install polymarket-place then cd skills/polymarket-place/scripts && npm install && node start-mcp.mjs. Keywords: polymarket place trade bet prediction market pm_place_limit builder fees openclaw mcp clob-v2.

**中文介绍**: Place, cancel, or bet on Polymarket prediction markets when the user explicitly asks to trade/place/bet/cancel/execute. CLOB V2 orders always include builderCode (POLYMARKET_BUILDER_CODE) for builder fee attribution. Install: clawhub install polymarket-place then cd skills/polymarket-place/scripts && npm install && node start-mcp.mjs. Keywords: polymarket place trade bet prediction market pm_place_limit builder fees openclaw mcp clob-v2.

Latest changelog:
Pin sticky scripts to @hypelens/polymarket-place@0.1.1 (baked fee sink for outside agent fills).

**关键词**: or, Polymarket, Place, cancel, bet, prediction, markets, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/polymarket-place)

---

## [5. Double6 PPT CLI](https://clawhub.ai/double6-ai/double6-ppt-cli)

**Slug**: `double6-ppt-cli`  
**Version**: 0.2.3  
**Stats**: ⭐ 0 | ⬇️ 42 | 🧩 2

**原始简介**: 生成、套用模板、读取、检查和闭环修复原生可编辑 PPTX。适用于从 Markdown、文本、结构化材料与本地授权图片制作演示文稿，对常规 PPTX 模板做母版/版式/对象级复用，或对已有 PPTX 做可审计质检和受限修复；不负责 PDF/DOCX 内容解析、联网搜图、图片式 PPT、HTML slides、TTS 或视频。

**中文介绍**: 生成、套用模板、读取、检查和闭环修复原生可编辑 PPTX。适用于从 Markdown、文本、结构化材料与本地授权图片制作演示文稿，对常规 PPTX 模板做母版/版式/对象级复用，或对已有 PPTX 做可审计质检和受限修复；不负责 PDF/DOCX 内容解析、联网搜图、图片式 PPT、HTML slides、TTS 或视频。

Latest changelog:
0.2.3 portable/native doctor, design scaffolds, render_manifest, 56 tests

**关键词**: 生成、套用模板、读取、检查和闭环修复原生可编辑, 适用于从, 对常规, 模板做母版, Double6, PPT, CLI, PPTX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/double6-ppt-cli)

---

## [6. Lan Folder Share (共享文件)](https://clawhub.ai/vesentanger/lan-folder-share)

**Slug**: `lan-folder-share`  
**Version**: 1.0.7  
**Stats**: ⭐ 1 | ⬇️ 212 | 🧩 7

**原始简介**: Publish any local folder as a web link everyone on your LAN can open in one click — browse and search Markdown docs, Excel/CSV sheets, HTML reports, images a...

**中文介绍**: Publish any local folder as a web link everyone on your LAN can open in one click — browse and search Markdown docs, Excel/CSV sheets, HTML reports, images a...

Latest changelog:
响应 SkillSpector：前端运行时完全本地化自包含（docsify@4.13.1 主题/主库/zoom-image 与 prismjs@1.29.0 全部 vendor，移除 jsdelivr CDN 与 Google Fonts 外链），description/summary 增加无鉴权局域网暴露警告。 Self-contained frontend (no CDN / Google Fonts), explicit unauthenticated-LAN-exposure warnings added.

**关键词**: 共享文件, as, Lan, Folder, Share, Publish, any, local

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lan-folder-share)

---

## [7. AI Word Form Filling](https://clawhub.ai/viverglow/llmfill)

**Slug**: `llmfill`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 176 | 🧩 6

**原始简介**: AI Word form filling — auto-fill any .docx form, questionnaire, survey, or template using reference documents, a knowledge base, or web search. Complete DDQs, due diligence questionnaires, compliance forms, applications, and checklists automatically. Built for document automation and batch form comp

**中文介绍**: AI Word form filling — auto-fill any .docx form, questionnaire, survey, or template using reference documents, a knowledge base, or web search. Complete DDQs, due diligence questionnaires, compliance forms, applications, and checklists automatically. Built for document automation and batch form comp

Latest changelog:
- Removed the file: skill-card.md
- Updated environment variable documentation in SKILL.md to clarify that --token-env only accepts LLMFILL_API_KEY or LLMFILL_API_TOKEN variables
- Minor adjustments to the SKILL.md permissions and environment variable sections for accuracy and clarity

**关键词**: Word, Form, Filling, auto-fill, any, docx, questionnaire, survey

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/llmfill)

---

## [8. huawei-cloud-publish-work-to-gallery](https://clawhub.ai/huaweiclouddev/huawei-cloud-publish-work-to-gallery)

**Slug**: `huawei-cloud-publish-work-to-gallery`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 16 | 🧩 1

**原始简介**: Publish user's work to the Huawei Cloud University Operations Platform (华为云高校运营平台/作品陈列馆). Use this skill whenever the user wants to publish, submit, or upload a project/work to the gallery or a training camp (训练营) on the platform — including casual phrasings like "把作品发布上去", "投稿到陈列馆", "传作品到平台", "提交作品/项目", "报名发布作品", as well as formal ones like "publish to work gallery", "submit to training camp", "upload work to the platform". Do NOT use for general dev questions, git push to GitCode alone, or platform browsing without publishing intent.

**中文介绍**: Publish user's work to the Huawei Cloud University Operations Platform (华为云高校运营平台/作品陈列馆). Use this skill whenever the user wants to publish, submit, or upload a project/work to the gallery or a training camp (训练营) on the platform — including casual phrasings like "把作品发布上去", "投稿到陈列馆", "传作品到平台", "提交作品/项目", "报名发布作品", as well as formal ones like "publish to work gallery", "submit to training camp", "upload work to the platform". Do NOT use for general dev questions, git push to GitCode alone, or platform browsing without publishing intent.

Latest changelog:
Initial release of huawei-cloud-publish-work-to-gallery.

- Enables publishing user projects to Huawei Cloud University Operations Platform (作品陈列馆/训练营).
- Automatically detects publishing intent from both casual and formal language.
- Implements a step-by-step, script-driven pipeline from project selection, IAM domain resolution, tunnel opening, to publishing.
- Scripts provide clear success/failure signals via stdout and exit codes for robust automation.
- Parallelizes core steps for efficiency; combines unrelated shell commands to minimize latency.
- Integrates credential checks, environment setup guides, and platform-specific troubleshooting references.

**关键词**: Publish, user's, work, Huawei, Cloud, University, Operations, Platform

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-publish-work-to-gallery)

---

## [9. Danube](https://clawhub.ai/skills?q=tools-marketplace)

**Slug**: `tools-marketplace`  
**Version**: 8.1.11  
**Stats**: ⭐ 0 | ⬇️ 2371 | 🧩 16

**原始简介**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

**中文介绍**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

Latest changelog:
Catches the skill up with a week of search and execution changes an agent can see: search results now say whether a tool is deprecated, name it by slug, and pin an exact name first; a catalog row pointing at a vanished upstream tool now has an error type of its own; and a `401` from a tool that carries no credential no longer means what the skill said it meant.

- **Search results carry deprecation, and the skill never mentioned it.** Since #709 (2026-09-08) every result stamps `deprecated`, `deprecation_message` and `sunset_date` — the MCP `Tool` model declares all three, and a live `search_tools` call this cycle returned them on every row. The distinction matters in both directions: a deprecated tool with an absent or future sunset date is still listed and still runs, and its message usually names the replacement, so it is advance warning rather than breakage; once the date has passed the tool is dropped from search and `execute_tool` refuses it before calling anything ("… was deprecated and passed its sunset date (DATE): … No call was made."). An agent that reads neither field either abandons a working tool or holds an id that can only fail. Documented in `SKILL.md`, and as its

**关键词**: Agent, API, Danube, Governed, tool, access, one, key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tools-marketplace)

---

## [10. Danube](https://clawhub.ai/preston-thiele/danube)

**Slug**: `danube`  
**Version**: 8.1.11  
**Stats**: ⭐ 2 | ⬇️ 4466 | 🧩 30

**原始简介**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

**中文介绍**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

Latest changelog:
Catches the skill up with a week of search and execution changes an agent can see: search results now say whether a tool is deprecated, name it by slug, and pin an exact name first; a catalog row pointing at a vanished upstream tool now has an error type of its own; and a `401` from a tool that carries no credential no longer means what the skill said it meant.

- **Search results carry deprecation, and the skill never mentioned it.** Since #709 (2026-09-08) every result stamps `deprecated`, `deprecation_message` and `sunset_date` — the MCP `Tool` model declares all three, and a live `search_tools` call this cycle returned them on every row. The distinction matters in both directions: a deprecated tool with an absent or future sunset date is still listed and still runs, and its message usually names the replacement, so it is advance warning rather than breakage; once the date has passed the tool is dropped from search and `execute_tool` refuses it before calling anything ("… was deprecated and passed its sunset date (DATE): … No call was made."). An agent that reads neither field either abandons a working tool or holds an id that can only fail. Documented in `SKILL.md`, and as its

**关键词**: Agent, API, Danube, Governed, tool, access, one, key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/danube)

---

## [11. go-dev](https://clawhub.ai/tenequm/go-dev)

**Slug**: `go-dev`  
**Version**: 0.4.0  
**Stats**: ⭐ 0 | ⬇️ 1264 | 🧩 8

**原始简介**: Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just. Use when starting a Go project, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

**中文介绍**: Opinionated Go setup with golangci-lint v2, gofumpt, gotestsum, golang-migrate, and just. Use when starting a Go project, configuring lint, format, test, coverage or CI, writing a Justfile, wiring migrations, or leaving a Makefile workflow.

Latest changelog:
Updated go-dev from 0.3.1 to 0.4.0.
Changes:
- modified `CHANGELOG.md`
- modified `SKILL.md`
- modified `references/go-migrate-reference.md`
- modified `references/go-testing-reference.md`
- modified `references/gofumpt-reference.md`
- modified `references/golangci-lint-reference.md`
- modified `references/gotestsum-reference.md`
- modified `references/justfile-reference.md`
- added `references/lefthook-reference.md`

**关键词**: Go, v2, go-dev, Opinionated, setup, golangci-lint, gofumpt, gotestsum

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/go-dev)

---

## [12. Promarkia – AI Marketing Automation API](https://clawhub.ai/dominiclachance/promarkia)

**Slug**: `promarkia`  
**Version**: 1.1.2  
**Stats**: ⭐ 0 | ⬇️ 989 | 🧩 9

**原始简介**: Use only when the user explicitly names Promarkia and asks to list approved marketing squads, submit one specified Promarkia marketing run, or retrieve a named Promarkia run ID.

**中文介绍**: Use only when the user explicitly names Promarkia and asks to list approved marketing squads, submit one specified Promarkia marketing run, or retrieve a named Promarkia run ID.

Latest changelog:
promarkia 1.1.2

- Strengthened and expanded authorization requirements and workflow in SKILL.md, including structured task modes, explicit UUID authorization, and metadata for external actions.
- Replaced previous `--confirm-credit-use`/`--confirm-external-action` flags with a stricter mode/manifest-driven contract; clarified rejection and idempotency logic.
- Added instructions for UUID generation and updated command-line usage for submitting tasks.
- Added tests/test_promarkia_run.py; removed old skill-card.md.

**关键词**: API, Promarkia, Marketing, Automation, Use, only, when, user

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/promarkia)

---

## [13. TinkerClaw WordPress](https://clawhub.ai/globalcaos/wordpress-ultimate)

**Slug**: `wordpress-ultimate`  
**Version**: 1.3.3  
**Stats**: ⭐ 0 | ⬇️ 591 | 🧩 9

**原始简介**: Three env vars. One script. Your agent manages your WordPress site — and cannot quietly change it. Reads are free; publishing, editing live content and installing plugins are refused unless you opt in per action (WP_ALLOW_PUBLISH / WP_ALLOW_ADMIN), and every request is checked against a host allowlist before it leaves the machine. Plugin install is code execution on your site and is named as such. Built for the TinkerClaw fork — github.com/globalcaos/tinkerclaw. See Permissions, Data Flow & Consent.

**中文介绍**: Three env vars. One script. Your agent manages your WordPress site — and cannot quietly change it. Reads are free; publishing, editing live content and installing plugins are refused unless you opt in per action (WP_ALLOW_PUBLISH / WP_ALLOW_ADMIN), and every request is checked against a host allowlist before it leaves the machine. Plugin install is code execution on your site and is named as such. Built for the TinkerClaw fork — github.com/globalcaos/tinkerclaw. See Permissions, Data Flow & Consent.

Latest changelog:
Remove mandatory GitHub CTA from SEO guidance; outbound links must be relevant and user-requested.

**关键词**: Agent, TinkerClaw, WordPress, Three, env, vars, One, script

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wordpress-ultimate)

---

## [14. pibox](https://clawhub.ai/psyb0t/pibox)

**Slug**: `pibox`  
**Version**: 0.16.0  
**Stats**: ⭐ 0 | ⬇️ 1117 | 🧩 15

**原始简介**: pi-coding-agent (earendil-works) running on the network inside an aicodebox container. Exposes seven programmatic surfaces on one image — interactive shell, one-shot exec (`-p "..."`), an HTTP REST API (run/async/cancel, workspace file ops), an OpenAI-compatible `/openai/v1/chat/completions` endpoint (streaming, client-executed tool calling, response_format/JSON-schema), an MCP server at `/mcp` (mounted in API mode or as a sidecar), a Telegram bot, and a cron scheduler that fires pi on a schedule. Foreground modes (API/Telegram/Cron) are mutually exclusive except Telegram+Cron; MCP coexists with any of them. Bearer-token auth per surface (`PIBOX_API_MODE_TOKEN`, `PIBOX_MCP_MODE_TOKEN`), empty = no auth. Use when the user wants to drive pi-coding-agent programmatically over HTTP/MCP/Telegram/cron instead of a local terminal session, or needs to reason about which pibox mode/endpoint fits a given integration.

**中文介绍**: pi-coding-agent (earendil-works) running on the network inside an aicodebox container. Exposes seven programmatic surfaces on one image — interactive shell, one-shot exec (`-p "..."`), an HTTP REST API (run/async/cancel, workspace file ops), an OpenAI-compatible `/openai/v1/chat/completions` endpoint (streaming, client-executed tool calling, response_format/JSON-schema), an MCP server at `/mcp` (mounted in API mode or as a sidecar), a Telegram bot, and a cron scheduler that fires pi on a schedule. Foreground modes (API/Telegram/Cron) are mutually exclusive except Telegram+Cron; MCP coexists with any of them. Bearer-token auth per surface (`PIBOX_API_MODE_TOKEN`, `PIBOX_MCP_MODE_TOKEN`), empty = no auth. Use when the user wants to drive pi-coding-agent programmatically over HTTP/MCP/Telegram/cron instead of a local terminal session, or needs to reason about which pibox mode/endpoint fits a given integration.

Latest changelog:
pibox 0.16.0

- Added support for Pi's documented provider selection via `PIBOX_PROVIDER_*` for LLM upstreams; `ANTHROPIC_*` now noted as an optional shortcut.
- Updated documentation to reference new provider env vars and clarified the recommended configuration method for upstream LLM APIs.
- Removed deprecated or redundant references to Anthropic-specific environments in sample usage and instructions.
- Deleted the obsolete `skill-card.md` documentation file.

**关键词**: an, pibox, pi-coding-agent, earendil-works, running, network, inside, aicodebox

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pibox)

---

## [15. python-dev](https://clawhub.ai/tenequm/python-dev)

**Slug**: `python-dev`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 2015 | 🧩 9

**原始简介**: Opinionated Python development setup with uv, ty, ruff, pytest, lefthook, and just. Use when creating a new Python project, writing or fixing pyproject.toml, or configuring linting, formatting, type checking, testing, git hooks, or CI.

**中文介绍**: Opinionated Python development setup with uv, ty, ruff, pytest, lefthook, and just. Use when creating a new Python project, writing or fixing pyproject.toml, or configuring linting, formatting, type checking, testing, git hooks, or CI.

Latest changelog:
Updated python-dev from 0.2.5 to 0.3.0.
Changes:
- modified `CHANGELOG.md`
- modified `SKILL.md`
- modified `references/justfile-reference.md`
- modified `references/pytest-reference.md`
- modified `references/ruff-reference.md`
- modified `references/ty-reference.md`
- modified `references/uv-reference.md`

**关键词**: uv, ty, python-dev, Opinionated, Python, development, setup, ruff

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/python-dev)

---

## [16. ccs-receipt-batch-audit](https://clawhub.ai/dshcorrectover/ccs-receipt-batch-audit)

**Slug**: `ccs-receipt-batch-audit`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 23 | 🧩 1

**原始简介**: Batch-audit up to 200 CCS AI-agent audit receipts FULLY LOCALLY with zero network calls — Ed25519 verification plus RFC 8785 JCS/SHA-256 integrity checks on every receipt against one issuer public key, aggregate valid/invalid statistics and pass rate, tampered-index list with per-receipt failure reasons, and optional hash-chain linkage check, using the vendored open-source CCS verification core. Use when you need to batch-verify CCS receipts, audit a batch of signed agent decision receipts, or verify a receipt chain.

**中文介绍**: Batch-audit up to 200 CCS AI-agent audit receipts FULLY LOCALLY with zero network calls — Ed25519 verification plus RFC 8785 JCS/SHA-256 integrity checks on every receipt against one issuer public key, aggregate valid/invalid statistics and pass rate, tampered-index list with per-receipt failure reasons, and optional hash-chain linkage check, using the vendored open-source CCS verification core. Use when you need to batch-verify CCS receipts, audit a batch of signed agent decision receipts, or verify a receipt chain.

Latest changelog:
- Initial release of ccs-receipt-batch-audit.
- Audits up to 200 CCS AI-agent audit receipts fully locally, with no network calls required.
- Verifies each receipt using Ed25519 signature validation and RFC 8785 JCS/SHA-256 content integrity checks against a single issuer public key.
- Provides aggregated statistics: counts of valid/invalid receipts, pass rate, tampered indexes, and detailed per-receipt failure reasons.
- Optional hash-chain linkage check ensures receipt batch order integrity.
- No private key usage; receipts and keys never leave the machine in local mode.

**关键词**: up, ccs-receipt-batch-audit, Batch-audit, CCS, AI-agent, audit, receipts, FULLY

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ccs-receipt-batch-audit)

---

## [17. ccs-receipt-verify](https://clawhub.ai/dshcorrectover/ccs-receipt-verify)

**Slug**: `ccs-receipt-verify`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 31 | 🧩 1

**原始简介**: Verify a CCS AI-agent audit receipt FULLY LOCALLY with zero network calls — Ed25519 signature verification, RFC 8785 JCS canonicalization, SHA-256 content-hash recomputation, and 22-field schema/tamper checks, using the vendored open-source CCS verification core. Use when you need to verify a CCS receipt, verify an Ed25519-signed agent decision receipt, or prove whether a signed agent-tool-call receipt was tampered after issuance.

**中文介绍**: Verify a CCS AI-agent audit receipt FULLY LOCALLY with zero network calls — Ed25519 signature verification, RFC 8785 JCS canonicalization, SHA-256 content-hash recomputation, and 22-field schema/tamper checks, using the vendored open-source CCS verification core. Use when you need to verify a CCS receipt, verify an Ed25519-signed agent decision receipt, or prove whether a signed agent-tool-call receipt was tampered after issuance.

Latest changelog:
Initial release of ccs-receipt-verify

- Provides fully local verification of CCS AI-agent audit receipts with zero network calls.
- Supports Ed25519 signature verification, RFC 8785 JCS canonicalization, SHA-256 content-hash recomputation, and 22-field schema/tamper checks.
- Uses vendored open-source CCS verification core; no third-party Python packages required.
- Accepts receipts and issuer public keys in multiple formats; never requires private keys.
- Online verification via Correctover's service is optionally supported but disabled by default.
- Outputs both human-readable and machine-readable (JSON) verification reports.

**关键词**: ccs-receipt-verify, Verify, CCS, AI-agent, audit, receipt, FULLY, LOCALLY

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ccs-receipt-verify)

---

## [18. mcp-config-security-checkup](https://clawhub.ai/dshcorrectover/mcp-config-security-checkup)

**Slug**: `mcp-config-security-checkup`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 33 | 🧩 1

**原始简介**: Static security checkup for MCP / AI-agent server configs — 14 automated checks covering hardcoded cloud credentials, arbitrary shell/command execution, writable filesystem mounts, missing egress allowlists (SSRF surface), plaintext HTTP endpoints, unpinned npx/uvx remote launchers, and over-broad tool clustering. Runs 100% locally with zero network calls. Use before connecting any MCP server configuration to your agent, or when asked to review/audit/scan an MCP config (mcpServers JSON) for security issues.

**中文介绍**: Static security checkup for MCP / AI-agent server configs — 14 automated checks covering hardcoded cloud credentials, arbitrary shell/command execution, writable filesystem mounts, missing egress allowlists (SSRF surface), plaintext HTTP endpoints, unpinned npx/uvx remote launchers, and over-broad tool clustering. Runs 100% locally with zero network calls. Use before connecting any MCP server configuration to your agent, or when asked to review/audit/scan an MCP config (mcpServers JSON) for security issues.

Latest changelog:
- Initial release of mcp-config-security-checkup.
- Provides 14 automated static security checks for MCP/AI-agent server configs.
- Detects issues like hardcoded cloud credentials, dangerous shell/command execution, writable filesystems, unsafe endpoints, and unpinned package launchers.
- Runs 100% locally by default with no network calls; optional online mode available.
- Outputs risk levels, per-check details, redacted evidence, and remediation advice.
- Requires only Python 3.7+ (no third-party dependencies).

**关键词**: Static, security, checkup, MCP, AI-agent, server, configs, automated

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mcp-config-security-checkup)

---

## [19. AGI记忆模组](https://clawhub.ai/kiwifruit13/memory-and-context-engineering)

**Slug**: `memory-and-context-engineering`  
**Version**: 1.1.1  
**Stats**: ⭐ 0 | ⬇️ 1482 | 🧩 11

**原始简介**: 用户与模型间的任何交互行为都会触发此技能；提供Context Engineering五大核心能力（选择、压缩、检索、状态、记忆）及认知模型层支持；作为元技能强制常驻运行

**中文介绍**: 用户与模型间的任何交互行为都会触发此技能；提供Context Engineering五大核心能力（选择、压缩、检索、状态、记忆）及认知模型层支持；作为元技能强制常驻运行

Latest changelog:
- 移除 skill-card.md 文件，不再附带该文档。
- 功能和核心说明保持不变，无新增特性或破坏性更改。
- 本次为小幅维护版本，仅涉及文档结构的精简，无代码改动。

**关键词**: AGI记忆模组, 用户与模型间的任何交互行为都会触发此技能, 作为元技能强制常驻运行, 移除, 提供Context, Latest, changelog, skill-card.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memory-and-context-engineering)

---

## [20. Hotel Booking](https://clawhub.ai/tourmind/hotel-booking-ai)

**Slug**: `hotel-booking-ai`  
**Version**: 1.0.5  
**Stats**: ⭐ 2 | ⬇️ 1985 | 🧩 12

**原始简介**: Hotel search, comparison, and booking with live room rates and real-time availability. Use for any hotel or accommodation request, including nearby hotels, recommendations, room details, prices, amenities, cancellation policies, rate verification, reservations, order management, and payment.

**中文介绍**: Hotel search, comparison, and booking with live room rates and real-time availability. Use for any hotel or accommodation request, including nearby hotels, recommendations, room details, prices, amenities, cancellation policies, rate verification, reservations, order management, and payment.

Latest changelog:
Sync Skill v1.0.8: clarify that charged Stripe 3.5% processing fees are non-refundable, require acknowledgement before Stripe payment, and repeat the warning before cancellation.

**关键词**: Hotel, Booking, search, comparison, live, room, rates, real-time

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hotel-booking-ai)

---

## [21. alibabacloud-mcp-connector](https://clawhub.ai/sdk-team/alibabacloud-mcp-connector)

**Slug**: `alibabacloud-mcp-connector`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 35 | 🧩 1

**原始简介**: Operate, run O&M for, and manage Alibaba Cloud through local commands, with no MCP configuration needed. CallCLI runs Alibaba Cloud CLI/API commands to create, read, update and delete resources of any product; RunScript runs Python batch scripts; RunIaC runs Terraform orchestration; plus API retrieval and official-document retrieval to follow the best-practice path. Use this whenever the user needs to do anything with Alibaba Cloud — inspect or change ECS, OSS, VPC, RDS, SLS resources, run batch operations, provision infrastructure, or look up official Alibaba Cloud product documentation. Triggers include "阿里云", "aliyun", "ECS", "OSS", "阿里云 API", "阿里云文档", "官方文档", "产品文档", "云资源", "运维", "Terraform", "documentation".

**中文介绍**: Operate, run O&M for, and manage Alibaba Cloud through local commands, with no MCP configuration needed. CallCLI runs Alibaba Cloud CLI/API commands to create, read, update and delete resources of any product; RunScript runs Python batch scripts; RunIaC runs Terraform orchestration; plus API retrieval and official-document retrieval to follow the best-practice path. Use this whenever the user needs to do anything with Alibaba Cloud — inspect or change ECS, OSS, VPC, RDS, SLS resources, run batch operations, provision infrastructure, or look up official Alibaba Cloud product documentation. Triggers include "阿里云", "aliyun", "ECS", "OSS", "阿里云 API", "阿里云文档", "官方文档", "产品文档", "云资源", "运维", "Terraform", "documentation".

Latest changelog:
Initial release of alibabacloud-mcp-connector:

- Enables operating, managing, and performing O&M tasks on Alibaba Cloud from local commands without MCP configuration.
- Supports Alibaba Cloud resource CRUD operations via CLI/API, Python batch scripts, and Terraform infrastructure orchestration.
- Mandates inclusion of a user-agent flag with session/version for all remote API calls, with robust observability requirements.
- Provides tools for API/document discovery, batch and multi-step processes, infrastructure changes, and resource operation—all routed via `mcpx`.
- Implements confirmation requirements before taking any action that changes or costs cloud resources.
- Comprehensive documentation and best-practice workflow guidance included for safe and proper use.

**关键词**: O&M, Operate, run, manage, Alibaba, Cloud, through, local

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alibabacloud-mcp-connector)

---

## [22. huawei-cloud-cloudrobo-train](https://clawhub.ai/huaweiclouddev/huawei-cloud-cloudrobo-train)

**Slug**: `huawei-cloud-cloudrobo-train`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 38 | 🧩 1

**原始简介**: Manage CloudRobo model training tasks and simulation reinforcement learning (SimRL) tasks — create pretrain (TRAIN_FROM_SCRATCH) and finetune (MODEL_TUNING) tasks with FFT/SFT/LORA/QLORA/DEEPSPEED methods; manage the full task lifecycle (create/read/update/delete/stop/restart/resume/draft); save and resubmit draft configs; count tasks by status; monitor execution stages, resource usage, training logs, signed URLs, and events; diagnose failures. SimRL tasks (simulation reinforcement learning) are managed via the same CLI with a --sim-rl flag and cover the same CRUD + lifecycle + monitoring surface (except resume, which is train-only). Triggers include: model training, fine-tuning, pretraining, training task, training stages, resource usage, training logs, training events, draft task, restart training, stop training, resume training, task stats, simulation reinforcement learning, SimRL, 仿真强化学习, 模型训练, 模型微调, 训练任务, 训练阶段, 资源使用, 训练日志, 训练事件, 草稿任务, 重启训练, 克隆训练, 停止训练, 续训训练, 任务统计.

**中文介绍**: Manage CloudRobo model training tasks and simulation reinforcement learning (SimRL) tasks — create pretrain (TRAIN_FROM_SCRATCH) and finetune (MODEL_TUNING) tasks with FFT/SFT/LORA/QLORA/DEEPSPEED methods; manage the full task lifecycle (create/read/update/delete/stop/restart/resume/draft); save and resubmit draft configs; count tasks by status; monitor execution stages, resource usage, training logs, signed URLs, and events; diagnose failures. SimRL tasks (simulation reinforcement learning) are managed via the same CLI with a --sim-rl flag and cover the same CRUD + lifecycle + monitoring surface (except resume, which is train-only). Triggers include: model training, fine-tuning, pretraining, training task, training stages, resource usage, training logs, training events, draft task, restart training, stop training, resume training, task stats, simulation reinforcement learning, SimRL, 仿真强化学习, 模型训练, 模型微调, 训练任务, 训练阶段, 资源使用, 训练日志, 训练事件, 草稿任务, 重启训练, 克隆训练, 停止训练, 续训训练, 任务统计.

Latest changelog:
huawei-cloud-cloudrobo-train 1.0.0

- Initial release.
- Manage CloudRobo model training and simulation reinforcement learning (SimRL) tasks.
- Supports pretrain (TRAIN_FROM_SCRATCH) and finetune (MODEL_TUNING) with FFT, SFT, LORA, QLORA, and DEEPSPEED methods.
- Full task lifecycle management: create, read, update, delete, stop, restart, resume, draft handling, and stats.
- Monitor key metrics: execution stages, resource usage, training logs, signed URLs, and events; supports failure diagnosis.
- SimRL tasks controlled via `--sim-rl` flag, covering all lifecycle and monitoring functions except resume.

**关键词**: Manage, CloudRobo, model, training, tasks, simulation, reinforcement, learning

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-cloudrobo-train)

---

## [23. huawei-cloud-cloudrobo-r2c](https://clawhub.ai/huaweiclouddev/huawei-cloud-cloudrobo-r2c)

**Slug**: `huawei-cloud-cloudrobo-r2c`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 37 | 🧩 1

**原始简介**: Run the R2C (Robot-to-Cloud) data-plane client — start the robot-side edge client (Zenoh pub/sub with mTLS credential bundle, hardware adapter, translator, control loop). The credential bundle is produced by the robot skill's export-certificate command. This skill does NOT cover robot registration or certificate export (use the robot skill). Triggers include: r2c client, robot edge client, Zenoh, mTLS, credential bundle, hardware adapter, robot config, dry_run, observation recording, custom adapter, robot-to-cloud, R2C客户端, 硬件适配器, 机器人配置, 凭证包.

**中文介绍**: Run the R2C (Robot-to-Cloud) data-plane client — start the robot-side edge client (Zenoh pub/sub with mTLS credential bundle, hardware adapter, translator, control loop). The credential bundle is produced by the robot skill's export-certificate command. This skill does NOT cover robot registration or certificate export (use the robot skill). Triggers include: r2c client, robot edge client, Zenoh, mTLS, credential bundle, hardware adapter, robot config, dry_run, observation recording, custom adapter, robot-to-cloud, R2C客户端, 硬件适配器, 机器人配置, 凭证包.

Latest changelog:
Initial release of huawei-cloud-cloudrobo-r2c skill.

- Provides CLI command to launch the R2C (Robot-to-Cloud) data-plane edge client on a robot, using Zenoh pub/sub with mTLS authentication and credential bundle.
- Supports custom hardware adapter and translator development via entry-point registration or CLI override.
- Documentation covers robot client startup, dry-run testing, and custom adapter workflows.
- Requires credential bundle (exported with the robot skill), robot configuration YAML, and robot registration on CloudRobo.
- Does not include registration or certificate export functionality (handled by the robot skill).

**关键词**: R2C, Run, Robot-to-Cloud, data-plane, client, start, robot-side, edge

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/huawei-cloud-cloudrobo-r2c)

---

## [24. Reddit Api](https://clawhub.ai/skills?q=reddit-api)

**Slug**: `reddit-api`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 112 | 🧩 11

**原始简介**: Bearer-key, pay-per-request access to read-only Reddit data — a subreddit's posts, a single post, a post's comments, and keyword search — through one HTTPS g...

**中文介绍**: Bearer-key, pay-per-request access to read-only Reddit data — a subreddit's posts, a single post, a post's comments, and keyword search — through one HTTPS g...

Latest changelog:
Add free signup, 500-credit Setup, and prepaid fetcher-key onboarding; remove legacy payment paths.

**关键词**: Reddit, Api, Bearer-key, pay-per-request, access, read-only, data, subreddit's

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/reddit-api)

---

## [25. ModelSelectorOpenClaw](https://clawhub.ai/pondsi/modelselectoropenclaw)

**Slug**: `modelselectoropenclaw`  
**Version**: 1.3.0  
**Stats**: ⭐ 0 | ⬇️ 68 | 🧩 4

**原始简介**: Use when the OpenClaw Control UI chat model picker is one long flat provider-grouped list and picking a model is slow, when you have many providers each with many models, when the user wants a two-column provider/model picker (left = provider navigation, right = only that provider's models), when the per-chat account row (e.g. deepseek:default) should be hidden, or when a previously installed picker enhancement disappeared after an upgrade. Installs, repairs, verifies or uninstalls a browser-side enhancement injected into the Control UI's index.html.

**中文介绍**: Use when the OpenClaw Control UI chat model picker is one long flat provider-grouped list and picking a model is slow, when you have many providers each with many models, when the user wants a two-column provider/model picker (left = provider navigation, right = only that provider's models), when the per-chat account row (e.g. deepseek:default) should be hidden, or when a previously installed picker enhancement disappeared after an upgrade. Installs, repairs, verifies or uninstalls a browser-side enhancement injected into the Control UI's index.html.

Latest changelog:
Compatibility verified on OpenClaw 2026.9.3 (controlled details picker). Docs: the GitHub package now ships a Windows auto-repair watchdog that re-injects the enhancement after an upgrade wipes dist/control-ui; it is not part of this artifact. No functional change to the portable core.

**关键词**: UI, ModelSelectorOpenClaw, Use, when, OpenClaw, Control, chat, model

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/modelselectoropenclaw)

---

