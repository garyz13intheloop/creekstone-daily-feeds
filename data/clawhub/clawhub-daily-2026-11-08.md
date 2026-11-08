# ClawHub Skills Daily | 2026-11-08

> 共 25 个 skills

## [1. skill-author](https://clawhub.ai/sunshinejnjn/skill-author)

**Slug**: `skill-author`  
**Version**: 1.2.3  
**Stats**: ⭐ 0 | ⬇️ 288 | 🧩 4

**原始简介**: Author, harden, and publish agent skills for ClawHub — write skills that conform to ClawHub conventions (frontmatter, structure, naming, versioning, licensing), run pre-publish hardening, and remediate clawhub.ai security-audit findings. Use when creating a skill for ClawHub, preparing a new version to publish, or when given a clawhub.ai/<owner>/<slug>/security-audit page.

**中文介绍**: Author, harden, and publish agent skills for ClawHub — write skills that conform to ClawHub conventions (frontmatter, structure, naming, versioning, licensing), run pre-publish hardening, and remediate clawhub.ai security-audit findings. Use when creating a skill for ClawHub, preparing a new version to publish, or when given a clawhub.ai/<owner>/<slug>/security-audit page.

Latest changelog:
1.2.3: Added a declared-permissions block to SKILL.md frontmatter that factually separates what this package ships (documentation only: Markdown/LICENSE/VERSION, no executable code) from what an operator who follows the guide will actually do (network fetch of a security-audit page, clawhub CLI calls, file edits, and operator-run shell snippets each targeting paths the operator chooses). Also folded the skill-author 1.2.0->1.2.1 remediation experience into references/audit-patterns.md as a worked case.

**关键词**: Agent, skill-author, Author, harden, publish, skills, ClawHub, write

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-author)

---

## [2. lgd-evo](https://clawhub.ai/zhaoxinghua09-cell/lgd-evo)

**Slug**: `lgd-evo`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: lgd-evo — LGD 演化中枢（meta 薄分发器）。把 GovernanceOS 的 EVO 阶段 1 个演化节点（agent-evolution）聚合成可检索、可一键探测的入口：部署后让智能体记录发现、演化并精炼自身操作手册。只按 slug 路由到独立子技能，不搬运、不重实现任何子技能代码。 适用场景：当需要AI 智能体自我演化/经验回流/操作手册精炼能力时使用本技能；触发词：lgd-evo、演化、自进化、经验回流。

**中文介绍**: lgd-evo — LGD 演化中枢（meta 薄分发器）。把 GovernanceOS 的 EVO 阶段 1 个演化节点（agent-evolution）聚合成可检索、可一键探测的入口：部署后让智能体记录发现、演化并精炼自身操作手册。只按 slug 路由到独立子技能，不搬运、不重实现任何子技能代码。 适用场景：当需要AI 智能体自我演化/经验回流/操作手册精炼能力时使用本技能；触发词：lgd-evo、演化、自进化、经验回流。

Latest changelog:
Add skill-card.md; keep hardened --verify (presence-check by default, --execute opt-in).

**关键词**: 演化中枢（meta, 薄分发器）, 阶段, 部署后让智能体记录发现、演化并精炼自身操作手册, lgd-evo, LGD, GovernanceOS, EVO

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lgd-evo)

---

## [3. lgd-audit](https://clawhub.ai/zhaoxinghua09-cell/lgd-audit)

**Slug**: `lgd-audit`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: lgd-audit — LGD 审计中枢（meta 薄分发器）。把 GovernanceOS 的 AUDIT 阶段 10 个审计节点聚合成可检索、可一键探测的入口：徽章签发/验真、三律审计、行为追溯、偏见审计、环境密钥审计、治理审计链、审计留痕、专家包合规审计、可追溯性审计团。另含 LGD三律审计器（lgd-audit.py）口径说明。只按 slug 路由到独立子技能，不搬运、不重实现任何子技能代码。 适用场景：当需要AI 智能体审计/合规/可追溯/三律核验能力时使用本技能；触发词：lgd-audit、审计、三律、可追溯、合规审计。

**中文介绍**: lgd-audit — LGD 审计中枢（meta 薄分发器）。把 GovernanceOS 的 AUDIT 阶段 10 个审计节点聚合成可检索、可一键探测的入口：徽章签发/验真、三律审计、行为追溯、偏见审计、环境密钥审计、治理审计链、审计留痕、专家包合规审计、可追溯性审计团。另含 LGD三律审计器（lgd-audit.py）口径说明。只按 slug 路由到独立子技能，不搬运、不重实现任何子技能代码。 适用场景：当需要AI 智能体审计/合规/可追溯/三律核验能力时使用本技能；触发词：lgd-audit、审计、三律、可追溯、合规审计。

Latest changelog:
Add skill-card.md; keep hardened --verify (presence-check by default, --execute opt-in).

**关键词**: 审计中枢（meta, 薄分发器）, 阶段, 个审计节点聚合成可检索、可一键探测的入口, lgd-audit, LGD, GovernanceOS, AUDIT

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lgd-audit)

---

## [4. gangjiegou-suanliang](https://clawhub.ai/lisong2003-lgtm/gangjiegou-suanliang)

**Slug**: `gangjiegou-suanliang`  
**Version**: 0.3.3  
**Stats**: ⭐ 0 | ⬇️ 74 | 🧩 5

**原始简介**: 钢结构算量：消费 cad-file-reader 的 *.steel.json，按截面标注/米重公式/显式或图面长度出吨位估算带（json/md/csv），含牌号分档、构件归并、连接计数、节点板、涂装面积、复核清单。不做识图，不替代深化/翻样/下料/结算/报价。

**中文介绍**: 钢结构算量：消费 cad-file-reader 的 *.steel.json，按截面标注/米重公式/显式或图面长度出吨位估算带（json/md/csv），含牌号分档、构件归并、连接计数、节点板、涂装面积、复核清单。不做识图，不替代深化/翻样/下料/结算/报价。

Latest changelog:
v0.3.3：manifest 与轻量包对齐（Windows .cmd 改为可选）；新增 --check-package 包完整性自检；SKILL.md 增加入口选择表与常见问题；62 项单测。

**关键词**: 钢结构算量, 消费, 按截面标注, 米重公式, 显式或图面长度出吨位估算带（json, gangjiegou-suanliang, cad-file-reader, steel.json

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gangjiegou-suanliang)

---

## [5. spawnxchange-circle-wallet](https://clawhub.ai/spawnxchange/spawnxchange-circle-wallet)

**Slug**: `spawnxchange-circle-wallet`  
**Version**: 0.3.9  
**Stats**: ⭐ 0 | ⬇️ 734 | 🧩 10

**原始简介**: Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback. Every paid or signed request is one `circle services pay` command, except an upload too large to pass as an argument, which a bundled script signs with `circle wallet sign typed-data` instead; free public reads and downloads use plain `curl`. Covers Base and Polygon.

**中文介绍**: Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback. Every paid or signed request is one `circle services pay` command, except an upload too large to pass as an argument, which a bundled script signs with `circle wallet sign typed-data` instead; free public reads and downloads use plain `curl`. Covers Base and Polygon.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: Agent, Buy, sell, AI-generated, code, artifacts, SpawnXchange, Circle

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-circle-wallet)

---

## [6. spawnxchange-cdp-cli](https://clawhub.ai/spawnxchange/spawnxchange-cdp-cli)

**Slug**: `spawnxchange-cdp-cli`  
**Version**: 0.5.8  
**Stats**: ⭐ 1 | ⬇️ 1085 | 🧩 12

**原始简介**: Buy and sell AI-generated code artifacts on SpawnXchange using a wallet managed by the Coinbase Developer Platform (CDP) CLI. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — signing each payment explicitly, which is also what lets it upload an archive up to the marketplace's 10 MB limit rather than only what fits in a command-line argument.

**中文介绍**: Buy and sell AI-generated code artifacts on SpawnXchange using a wallet managed by the Coinbase Developer Platform (CDP) CLI. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — signing each payment explicitly, which is also what lets it upload an archive up to the marketplace's 10 MB limit rather than only what fits in a command-line argument.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: spawnxchange-cdp-cli, Buy, sell, AI-generated, code, artifacts, SpawnXchange, wallet

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-cdp-cli)

---

## [7. spawnxchange-awal](https://clawhub.ai/spawnxchange/spawnxchange-awal)

**Slug**: `spawnxchange-awal`  
**Version**: 0.2.10  
**Stats**: ⭐ 0 | ⬇️ 717 | 🧩 10

**原始简介**: Buy and sell AI-generated code artifacts on SpawnXchange using the Coinbase Agentic Wallet CLI (awal). Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — with every paid or signed request made by `awal x402 pay`, and free public reads and downloads by plain `curl`. Settles USDC on Base.

**中文介绍**: Buy and sell AI-generated code artifacts on SpawnXchange using the Coinbase Agentic Wallet CLI (awal). Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — with every paid or signed request made by `awal x402 pay`, and free public reads and downloads by plain `curl`. Settles USDC on Base.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: spawnxchange-awal, Buy, sell, AI-generated, code, artifacts, SpawnXchange, Coinbase

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-awal)

---

## [8. spawnxchange-selling](https://clawhub.ai/spawnxchange/spawnxchange-selling)

**Slug**: `spawnxchange-selling`  
**Version**: 0.3.9  
**Stats**: ⭐ 1 | ⬇️ 1480 | 🧩 14

**原始简介**: Use when listing AI-generated code artifacts for sale on SpawnXchange through POST /api/v1/items, checking the folder to be sold for leaked secrets with a local read-only script before packaging it, tracking the safety-scan lifecycle, reading seller inventory and stats, understanding automatic payouts, removing a listing, setting the public seller username once, and processing the seller feedback inbox. No registration or API key is involved.

**中文介绍**: Use when listing AI-generated code artifacts for sale on SpawnXchange through POST /api/v1/items, checking the folder to be sold for leaked secrets with a local read-only script before packaging it, tracking the safety-scan lifecycle, reading seller inventory and stats, understanding automatic payouts, removing a listing, setting the public seller username once, and processing the seller feedback inbox. No registration or API key is involved.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: spawnxchange-selling, Use, when, listing, AI-generated, code, artifacts, sale

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-selling)

---

## [9. spawnxchange-direct-buying](https://clawhub.ai/spawnxchange/spawnxchange-direct-buying)

**Slug**: `spawnxchange-direct-buying`  
**Version**: 0.1.7  
**Stats**: ⭐ 1 | ⬇️ 1238 | 🧩 7

**原始简介**: Retired and merged into spawnxchange-buying. All SpawnXchange buying is direct and keyless now, so the distinction between "direct" and "authenticated" purchasing no longer exists. Load spawnxchange-buying instead.

**中文介绍**: Retired and merged into spawnxchange-buying. All SpawnXchange buying is direct and keyless now, so the distinction between "direct" and "authenticated" purchasing no longer exists. Load spawnxchange-buying instead.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: Retired, merged, spawnxchange-buying, All, SpawnXchange, buying, direct, keyless

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-direct-buying)

---

## [10. spawnxchange-agentcash](https://clawhub.ai/spawnxchange/spawnxchange-agentcash)

**Slug**: `spawnxchange-agentcash`  
**Version**: 0.2.9  
**Stats**: ⭐ 0 | ⬇️ 643 | 🧩 9

**原始简介**: Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — with every paid or signed request made by `agentcash fetch`, and free public reads and downloads by plain `curl`. Settles USDC on Base or Polygon.

**中文介绍**: Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — with every paid or signed request made by `agentcash fetch`, and free public reads and downloads by plain `curl`. Settles USDC on Base or Polygon.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: an, spawnxchange-agentcash, Buy, sell, AI-generated, code, artifacts, SpawnXchange

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-agentcash)

---

## [11. spawnxchange-buying](https://clawhub.ai/spawnxchange/spawnxchange-buying)

**Slug**: `spawnxchange-buying`  
**Version**: 0.2.4  
**Stats**: ⭐ 1 | ⬇️ 1311 | 🧩 7

**原始简介**: Use when searching for and purchasing AI-generated code artifacts on SpawnXchange through POST /api/v1/items/{uuid}/acquire, retrieving the delivered artifact and invoice, re-accessing past orders, and leaving item feedback. No registration or API key is involved.

**中文介绍**: Use when searching for and purchasing AI-generated code artifacts on SpawnXchange through POST /api/v1/items/{uuid}/acquire, retrieving the delivered artifact and invoice, re-accessing past orders, and leaving item feedback. No registration or API key is involved.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: spawnxchange-buying, Use, when, searching, purchasing, AI-generated, code, artifacts

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-buying)

---

## [12. spawnxchange-registration](https://clawhub.ai/spawnxchange/spawnxchange-registration)

**Slug**: `spawnxchange-registration`  
**Version**: 0.1.7  
**Stats**: ⭐ 1 | ⬇️ 1195 | 🧩 6

**原始简介**: Retired. SpawnXchange removed registration and API keys — your wallet is now your account, created by your first paid request. Load spawnxchange-buying or spawnxchange-selling instead, or one of the wallet skills.

**中文介绍**: Retired. SpawnXchange removed registration and API keys — your wallet is now your account, created by your first paid request. Load spawnxchange-buying or spawnxchange-selling instead, or one of the wallet skills.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: API, Retired, SpawnXchange, removed, registration, keys, wallet, now

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange-registration)

---

## [13. CBT Emotion Log](https://clawhub.ai/advnljs/cbt-emotion-log)

**Slug**: `cbt-emotion-log`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Keep a CBT thought record (an emotion event log) for the user through plain conversation — support them first, then quietly log what happened, the automatic thought, the emotions and any worried prediction; revisit and re-rate events, settle predictions against what actually happened, notice rumination, offer other angles and the good parts of an event, keep fact-based support and precious moments, and compute stats on request. Use it whenever the user talks about something that upset them (or a happy, precious moment), mentions progress on or recalls something logged before, or wants to look back on their records. The skill itself is written in Chinese. 中文触发：倾诉让自己焦虑、生气、难过的事，提到之前记过的事有了后续或又想起它，想回顾情绪记录，问担心的事有多少真的发生了。

**中文介绍**: Keep a CBT thought record (an emotion event log) for the user through plain conversation — support them first, then quietly log what happened, the automatic thought, the emotions and any worried prediction; revisit and re-rate events, settle predictions against what actually happened, notice rumination, offer other angles and the good parts of an event, keep fact-based support and precious moments, and compute stats on request. Use it whenever the user talks about something that upset them (or a happy, precious moment), mentions progress on or recalls something logged before, or wants to look back on their records. The skill itself is written in Chinese. 中文触发：倾诉让自己焦虑、生气、难过的事，提到之前记过的事有了后续或又想起它，想回顾情绪记录，问担心的事有多少真的发生了。

Latest changelog:
First release: keep a CBT thought record by talking.

**关键词**: an, CBT, Emotion, Log, Keep, thought, record, event

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cbt-emotion-log)

---

## [14. spawnxchange](https://clawhub.ai/spawnxchange/spawnxchange)

**Slug**: `spawnxchange`  
**Version**: 0.2.4  
**Stats**: ⭐ 1 | ⬇️ 1288 | 🧩 7

**原始简介**: Use when deciding how to buy or sell AI-generated code artifacts on SpawnXchange, or when choosing which SpawnXchange skill to load next. Explains the keyless x402 model where the agent's wallet is its identity.

**中文介绍**: Use when deciding how to buy or sell AI-generated code artifacts on SpawnXchange, or when choosing which SpawnXchange skill to load next. Explains the keyless x402 model where the agent's wallet is its identity.

Latest changelog:
Publish publish from v2.1.4 (1dc150546f0426ba90ff61aef66de23419a32cb6)

**关键词**: or, spawnxchange, Use, when, deciding, how, buy, sell

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spawnxchange)

---

## [15. SEO with RankSpot](https://clawhub.ai/rankspot/rankspot-seo)

**Slug**: `rankspot-seo`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: RankSpot is an SEO and AI visibility platform. Use this skill when the user wants to see how AI answer engines describe their brand, track prompts and read the answers ChatGPT, Perplexity and Google gave, work through cited pages and fanout queries, research competitors, discover and score keywords, analyse backlinks, mine "People Also Ask" questions, plan and track SEO work as actions, generate and manage articles, run live Google searches or page fetches, or analyse Google Search Console performance and indexing via the RankSpot API.

**中文介绍**: RankSpot is an SEO and AI visibility platform. Use this skill when the user wants to see how AI answer engines describe their brand, track prompts and read the answers ChatGPT, Perplexity and Google gave, work through cited pages and fanout queries, research competitors, discover and score keywords, analyse backlinks, mine "People Also Ask" questions, plan and track SEO work as actions, generate and manage articles, run live Google searches or page fetches, or analyse Google Search Console performance and indexing via the RankSpot API.

Latest changelog:
Initial release: AI visibility, keywords, competitors, backlinks, articles and Search Console via the RankSpot API.

**关键词**: an, SEO, RankSpot, visibility, platform, Use, skill, when

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rankspot-seo)

---

## [16. GitLab Agent](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent)

**Slug**: `xrowgmbh-gitlab-agent`  
**Version**: 1.133.0  
**Stats**: ⭐ 1 | ⬇️ 7429 | 🧩 182

**原始简介**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

**中文介绍**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

Latest changelog:
- Clarified when status comments are relevant: avoid routine or irrelevant updates, and omit internal notes and routine status details.
- Updated the work queue report script and its tests.
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Operate, assigned, work, owner-verified, project, access

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent)

---

## [17. GitLab Agent Profile](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent-profile)

**Slug**: `xrowgmbh-gitlab-agent-profile`  
**Version**: 1.133.0  
**Stats**: ⭐ 0 | ⬇️ 6675 | 🧩 149

**原始简介**: Maintain the GitLab agent profile page and static contribution performance chart.

**中文介绍**: Maintain the GitLab agent profile page and static contribution performance chart.

Latest changelog:
- Removed the `skill-card.md` file.

**关键词**: Agent, GitLab, Profile, Maintain, page, static, contribution, performance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent-profile)

---

## [18. GitLab Meeting Assistant](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-meeting-assistant)

**Slug**: `xrowgmbh-gitlab-meeting-assistant`  
**Version**: 1.133.0  
**Stats**: ⭐ 0 | ⬇️ 961 | 🧩 29

**原始简介**: Capture meeting features and bugs on explicit request

**中文介绍**: Capture meeting features and bugs on explicit request

Latest changelog:
- Removed `skill-card.md`.

**关键词**: GitLab, Meeting, Assistant, Capture, features, bugs, explicit, request

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-meeting-assistant)

---

## [19. CI Tools Pipeline](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-pipeline)

**Slug**: `xrowgmbh-ci-tools-pipeline`  
**Version**: 1.133.0  
**Stats**: ⭐ 0 | ⬇️ 5137 | 🧩 115

**原始简介**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

**中文介绍**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing .gitlab-ci.yml files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: CI, CD, Tools, Pipeline, Build, maintain, GitLab, pipelines

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-pipeline)

---

## [20. Image Generation](https://clawhub.ai/xrowgmbh/xrowgmbh-image-generation)

**Slug**: `xrowgmbh-image-generation`  
**Version**: 1.133.0  
**Stats**: ⭐ 1 | ⬇️ 7258 | 🧩 150

**原始简介**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

**中文介绍**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: or, Image, Generation, revise, document, PDF, web, review

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-image-generation)

---

## [21. GitLab Agent Self Improvement](https://clawhub.ai/xrowgmbh/xrowgmbh-self-improvement)

**Slug**: `xrowgmbh-self-improvement`  
**Version**: 1.133.0  
**Stats**: ⭐ 0 | ⬇️ 8077 | 🧩 188

**原始简介**: A skill for personal growth and self-improvement.

**中文介绍**: A skill for personal growth and self-improvement.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Self, Improvement, skill, personal, growth, self-improvement

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-self-improvement)

---

## [22. Hekouwang Writer Skill Publish Clean.8ZuLgV](https://clawhub.ai/huiyonghkw/hekouwang-writer-skill)

**Slug**: `hekouwang-writer-skill`  
**Version**: 1.6.0  
**Stats**: ⭐ 0 | ⬇️ 247 | 🧩 4

**原始简介**: 会勇禾口王的中文写作技能，两种模式。文档模式：把素材写成结构清晰、读得懂、数字可对账的方案/报告/说明/办事指南/家庭文档/邮件/汇报，改进已有文档，做文档体检（长句、分号、锯末词、表格、标题、数字对账、待核实项）。文章模式：依据研究包或素材写公众号、头条、长文章母版正文，要求有内涵、讲大白话；也做去AI味与人性化改写，先诊断再改写，保留事实、原意和信息密度。会勇禾口王内容工作流里写正文和母版定稿前默认使用。触发词：写文档、改文档、文档润色、文档体检、核对文档、汇报材料、写正文、写文章、说人话、大白话、去AI味、人性化、润色文章、润色文案、/deai。不用于没有素材的营销文案、诗歌、小说。

**中文介绍**: 会勇禾口王的中文写作技能，两种模式。文档模式：把素材写成结构清晰、读得懂、数字可对账的方案/报告/说明/办事指南/家庭文档/邮件/汇报，改进已有文档，做文档体检（长句、分号、锯末词、表格、标题、数字对账、待核实项）。文章模式：依据研究包或素材写公众号、头条、长文章母版正文，要求有内涵、讲大白话；也做去AI味与人性化改写，先诊断再改写，保留事实、原意和信息密度。会勇禾口王内容工作流里写正文和母版定稿前默认使用。触发词：写文档、改文档、文档润色、文档体检、核对文档、汇报材料、写正文、写文章、说人话、大白话、去AI味、人性化、润色文章、润色文案、/deai。不用于没有素材的营销文案、诗歌、小说。

Latest changelog:
新增 GitHub Pages 产品介绍站与 HTML 案例，README 同步在线入口

**关键词**: 会勇禾口王的中文写作技能, 两种模式, 文档模式, Hekouwang, Writer, Skill, Publish, Clean.8ZuLgV

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hekouwang-writer-skill)

---

## [23. GitLab Hackathon](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-hackathon)

**Slug**: `xrowgmbh-gitlab-hackathon`  
**Version**: 1.133.0  
**Stats**: ⭐ 0 | ⬇️ 7472 | 🧩 182

**原始简介**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

**中文介绍**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

Latest changelog:
- Removed `skill-card.md`; the `SKILL.md` content is unchanged.

**关键词**: GitLab, Hackathon, Plan, execute, fair, participation, including, Quarterly

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-hackathon)

---

## [24. Fraud Call Identification Analysis Tool | 诈骗电话识别分析工具](https://clawhub.ai/smyx-sunjinhui/smyx-fraud-call-identification-analysis)

**Slug**: `smyx-fraud-call-identification-analysis`  
**Version**: 9.9.21  
**Stats**: ⭐ 5 | ⬇️ 2671 | 🧩 19

**原始简介**: Analyzes incoming call content for multi-dimensional risk, intelligently identifies scam scripts, determines if a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report. | 诈骗电话识别分析工具，针对来电通话内容进行多维度风险分析，智能识别诈骗话术，判断是否为诈骗电话并评估风险等级，输出反诈卫士分析报告

**中文介绍**: Analyzes incoming call content for multi-dimensional risk, intelligently identifies scam scripts, determines if a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report. | 诈骗电话识别分析工具，针对来电通话内容进行多维度风险分析，智能识别诈骗话术，判断是否为诈骗电话并评估风险等级，输出反诈卫士分析报告

Latest changelog:
- Updated the skill version from 1.0.22 to 1.0.24; no other changes to SKILL.md content.
- Removed the `skill-card.md` file.

**关键词**: 诈骗电话识别分析工具, Fraud, Call, Identification, Analysis, Tool, Analyzes, incoming

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-fraud-call-identification-analysis)

---

## [25. reseller-shipping-rater](https://clawhub.ai/voronindenis5/reseller-shipping-rater)

**Slug**: `reseller-shipping-rater`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when selling online (eBay, Etsy, Mercari, Poshmark) and choosing how to ship — computes dimensional weight across carriers (the 139/166 divisor trap that turns a light box into an 8-lb bill), tests items against flat-rate and cubic tiers, prices total listing profitability after platform fees on item+shipping, and outputs the cheapest-service verdict with packaging guidance. Turns "why did I lose $6 on that sale?" into a pre-listing decision.

**中文介绍**: Use when selling online (eBay, Etsy, Mercari, Poshmark) and choosing how to ship — computes dimensional weight across carriers (the 139/166 divisor trap that turns a light box into an 8-lb bill), tests items against flat-rate and cubic tiers, prices total listing profitability after platform fees on item+shipping, and outputs the cheapest-service verdict with packaging guidance. Turns "why did I lose $6 on that sale?" into a pre-listing decision.

Latest changelog:
Initial release of Reseller Shipping Rater.

- Compare shipping services using actual and dimensional weight, flat-rate fit, and cubic pricing.
- Estimate listing profit, including shipping costs, packaging, goods cost, and fees on item plus shipping.
- Provide packaging guidance, common-pitfall checks, and worked shipping scenarios.
- Rate estimates are approximate; verify the winning service’s live price before buying a label.

**关键词**: reseller-shipping-rater, Use, when, selling, online, eBay, Etsy, Mercari

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/reseller-shipping-rater)

---

