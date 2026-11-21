# ClawHub Skills Daily | 2026-11-21

> 共 25 个 skills

## [1. web-checker](https://clawhub.ai/z-hussein/web-checker)

**Slug**: `web-checker`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 109 | 🧩 5

**原始简介**: Low-volume web configuration auditor with JS-bundle security analysis: probes headers, DNS, TLS, config exposure, and client-side XSS/secrets. Zero runtime dependencies.

**中文介绍**: Low-volume web configuration auditor with JS-bundle security analysis: probes headers, DNS, TLS, config exposure, and client-side XSS/secrets. Zero runtime dependencies.

Latest changelog:
web-checker 1.0.5

- Expanded declared permissions to include general network, shell, and file read/write access.
- Clarified that agents should confirm authorization before running active checks.
- Added recon-cli build and package metadata files.

**关键词**: web-checker, Low-volume, web, configuration, auditor, JS-bundle, security, analysis

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/web-checker)

---

## [2. Test Fix](https://clawhub.ai/winsoftlabs30/test-fix)

**Slug**: `test-fix`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 27 | 🧩 2

**原始简介**: Fix failing tests without weakening them — run the suite once, rerun only the failing files to separate flaky from real failures, classify each real failure as source bug or wrong test, then propose minimal diffs for approval. Use when asked to fix failing tests or make the suite green.

**中文介绍**: Fix failing tests without weakening them — run the suite once, rerun only the failing files to separate flaky from real failures, classify each real failure as source bug or wrong test, then propose minimal diffs for approval. Use when asked to fix failing tests or make the suite green.

Latest changelog:
Fix README install commands and handle

**关键词**: Test, Fix, failing, tests, without, weakening, them, run

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/test-fix)

---

## [3. DebugBundle](https://clawhub.ai/debugbundle/debugbundle)

**Slug**: `debugbundle`  
**Version**: 1.29.0  
**Stats**: ⭐ 1 | ⬇️ 2333 | 🧩 39

**原始简介**: Runtime error reporting and incident response for live apps with DebugBundle. Use it for crash reporting, incident monitoring, production monitoring, endpoint health checks, debug bundles and product analytics. Investigate runtime failures, exceptions, logs and observability signals through the CLI primarily, with MCP where needed. Covers application incidents, not generic infrastructure metrics.

**中文介绍**: Runtime error reporting and incident response for live apps with DebugBundle. Use it for crash reporting, incident monitoring, production monitoring, endpoint health checks, debug bundles and product analytics. Investigate runtime failures, exceptions, logs and observability signals through the CLI primarily, with MCP where needed. Covers application incidents, not generic infrastructure metrics.

Latest changelog:
DebugBundle skill release 1.29.0

**关键词**: DebugBundle, Runtime, error, reporting, incident, response, live, apps

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/debugbundle)

---

## [4. custom-infographic](https://clawhub.ai/j3ffyang/custom-infographic)

**Slug**: `custom-infographic`  
**Version**: 1.56.7  
**Stats**: ⭐ 0 | ⬇️ 1011 | 🧩 11

**原始简介**: Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

**中文介绍**: Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Original author 宝玉 (JimLiu); ported & customized by j3ffyang. Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

Latest changelog:
- Updated the infographic skill and image-generation script.
- Removed `skill-card.md`.

**关键词**: an, custom-infographic, Generate, professional, infographic, article, document, URL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/custom-infographic)

---

## [5. md-to-linkedin](https://clawhub.ai/j3ffyang/md-to-linkedin)

**Slug**: `md-to-linkedin`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 200 | 🧩 3

**原始简介**: Convert a Markdown article into rich text for LinkedIn's article editor, which has no Markdown and renders no tables. Headings, bold, italics, lists, quotes, links and fenced code become real HTML; tables become bullet lists, because the editor cannot draw one, or screenshot to PNG when the grid matters. Writes an HTML file beside the article for the browser copy path. Use when the user wants to publish a markdown draft as a LinkedIn article, asks for LinkedIn rich text, or needs the article editor formatting preserved.

**中文介绍**: Convert a Markdown article into rich text for LinkedIn's article editor, which has no Markdown and renders no tables. Headings, bold, italics, lists, quotes, links and fenced code become real HTML; tables become bullet lists, because the editor cannot draw one, or screenshot to PNG when the grid matters. Writes an HTML file beside the article for the browser copy path. Use when the user wants to publish a markdown draft as a LinkedIn article, asks for LinkedIn rich text, or needs the article editor formatting preserved.

Latest changelog:
- Updated `scripts/md2rich.py`.
- Removed `skill-card.md`.

**关键词**: md-to-linkedin, Convert, Markdown, article, rich, text, LinkedIn's, editor

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/md-to-linkedin)

---

## [6. md-to-twitter](https://clawhub.ai/j3ffyang/md-to-twitter)

**Slug**: `md-to-twitter`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 86 | 🧩 2

**原始简介**: Convert a Markdown article into an X (Twitter) thread, and optionally post it with its images attached. X renders no rich text and cannot carry an image in a paste, so the equivalent of a "paste payload" is a numbered thread script plus an API path that uploads each image and posts the thread in order. Counting follows X's weighted rules: 1 per character, 2 for CJK and emoji, 23 per URL. Use when the user wants to publish a markdown draft to X or Twitter, asks for a thread, asks how to get an article's images onto X, or wants a long article turned into posts.

**中文介绍**: Convert a Markdown article into an X (Twitter) thread, and optionally post it with its images attached. X renders no rich text and cannot carry an image in a paste, so the equivalent of a "paste payload" is a numbered thread script plus an API path that uploads each image and posts the thread in order. Counting follows X's weighted rules: 1 per character, 2 for CJK and emoji, 23 per URL. Use when the user wants to publish a markdown draft to X or Twitter, asks for a thread, asks how to get an article's images onto X, or wants a long article turned into posts.

Latest changelog:
- Updated the `md2twitter.py` script.
- Removed `skill-card.md`.

**关键词**: an, md-to-twitter, Convert, Markdown, article, Twitter, thread, optionally

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/md-to-twitter)

---

## [7. md-to-medium](https://clawhub.ai/j3ffyang/md-to-medium)

**Slug**: `md-to-medium`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 84 | 🧩 2

**原始简介**: Convert a Markdown article into an HTML fragment Medium's story editor accepts on paste. Medium deletes any image whose source is a data: URI, silently, so this converter never inlines bytes: every image is pointed at a public URL and the script refuses to pass until those images are pushed. Tables become hosted PNGs, because Medium draws no table. The article's H1 is dropped for the Title field. Use when the user wants to publish a markdown draft to Medium, asks for Medium rich text, or reports that a LinkedIn payload pasted into Medium lost its images.

**中文介绍**: Convert a Markdown article into an HTML fragment Medium's story editor accepts on paste. Medium deletes any image whose source is a data: URI, silently, so this converter never inlines bytes: every image is pointed at a public URL and the script refuses to pass until those images are pushed. Tables become hosted PNGs, because Medium draws no table. The article's H1 is dropped for the Title field. Use when the user wants to publish a markdown draft to Medium, asks for Medium rich text, or reports that a LinkedIn payload pasted into Medium lost its images.

Latest changelog:
- Updated `scripts/md2medium.py`; behavioral changes aren’t specified in the provided details.
- Removed `skill-card.md`.

**关键词**: an, md-to-medium, Convert, Markdown, article, HTML, fragment, Medium's

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/md-to-medium)

---

## [8. imap-smtp-email](https://clawhub.ai/troioi-vn/imap-smtp-email-maddy-fix)

**Slug**: `imap-smtp-email-maddy-fix`  
**Version**: 0.0.15  
**Stats**: ⭐ 0 | ⬇️ 808 | 🧩 2

**原始简介**: Read and send email via IMAP/SMTP. Check for new/unread messages, fetch content, search mailboxes, mark as read/unread, and send emails with attachments. Supports multiple accounts. Works with any IMAP/SMTP server including Gmail, Outlook, 163.com, vip.163.com, 126.com, vip.126.com, 188.com, and vip.188.com.

**中文介绍**: Read and send email via IMAP/SMTP. Check for new/unread messages, fetch content, search mailboxes, mark as read/unread, and send emails with attachments. Supports multiple accounts. Works with any IMAP/SMTP server including Gmail, Outlook, 163.com, vip.163.com, 126.com, vip.126.com, 188.com, and vip.188.com.

Latest changelog:
Add create-mailbox, copy and move commands; IMAP_PASS/SMTP_PASS accept passbolt://RESOURCE_ID references resolved through the local passbolt CLI.

**关键词**: imap-smtp-email, Read, send, email, via, IMAP, SMTP, Check

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/imap-smtp-email-maddy-fix)

---

## [9. Meo Mai Moi MCP](https://clawhub.ai/troioi-vn/meo-mai-moi-mcp)

**Slug**: `meo-mai-moi-mcp`  
**Version**: 0.4.1  
**Stats**: ⭐ 0 | ⬇️ 766 | 🧩 5

**原始简介**: Connect Meo Mai Moi via MCP OAuth presets.

**中文介绍**: Connect Meo Mai Moi via MCP OAuth presets.

Latest changelog:
Litters and listing-question scopes; reaching tool projection in Codex; tools without idempotency keys are read-checked, not blindly retried; description rewritten as a trigger.

**关键词**: Meo, Mai, Moi, MCP, Connect, via, OAuth, presets

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/meo-mai-moi-mcp)

---

## [10. Visual Emotion Recognition Skill | 人体视觉情绪识别技能](https://clawhub.ai/18072937735/smyx-human-emotion-recognition-analysis)

**Slug**: `smyx-human-emotion-recognition-analysis`  
**Version**: 1.0.20  
**Stats**: ⭐ 5 | ⬇️ 2709 | 🧩 21

**原始简介**: Uses visual AI on frontal faces to recognize multi-dimensional emotions like happiness, sadness, depression, calmness, anger, surprise, and fear in real-time. Supports emotion intensity quantification and abnormal emotion marking, suitable for human-computer interaction and mental health monitoring. | 人体视觉情绪识别技能，基于正面人脸视觉AI实时识别快乐、悲伤、抑郁、平静、愤怒、惊讶、恐惧等多维度情绪状态，支持情绪强度量化与异常情绪标记，适配人机交互、心理健康监测场景

**中文介绍**: Uses visual AI on frontal faces to recognize multi-dimensional emotions like happiness, sadness, depression, calmness, anger, surprise, and fear in real-time. Supports emotion intensity quantification and abnormal emotion marking, suitable for human-computer interaction and mental health monitoring. | 人体视觉情绪识别技能，基于正面人脸视觉AI实时识别快乐、悲伤、抑郁、平静、愤怒、惊讶、恐惧等多维度情绪状态，支持情绪强度量化与异常情绪标记，适配人机交互、心理健康监测场景

Latest changelog:
- Updated the skill version to 1.0.25.
- Removed `skill-card.md`.

**关键词**: 人体视觉情绪识别技能, Visual, Emotion, Recognition, Skill, Uses, frontal, faces

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-human-emotion-recognition-analysis)

---

## [11. Bias Lens Skill](https://clawhub.ai/troioi-vn/bias-lens)

**Slug**: `bias-lens`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 63 | 🧩 4

**原始简介**: Highlight reasoning that resembles a catalog bias

**中文介绍**: Highlight reasoning that resembles a catalog bias

Latest changelog:
Order findings by strength and by whether the main conclusion rests on them; check every side is held to the same standard; respond first when someone shares painful thoughts; skip news-outlet bias ratings and fact-checking.

**关键词**: Bias, Lens, Skill, Highlight, reasoning, resembles, catalog, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bias-lens)

---

## [12. dikciz-launcher](https://clawhub.ai/psyb0t/dikciz-launcher)

**Slug**: `dikciz-launcher`  
**Version**: 0.35.0  
**Stats**: ⭐ 0 | ⬇️ 1296 | 🧩 43

**原始简介**: Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

**中文介绍**: Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

Latest changelog:
- Removed the `skill-card.md` file.

**关键词**: an, dikciz-launcher, Install, operate, Dikciz, Launcher, owner-selected, Android

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dikciz-launcher)

---

## [13. docker-modembox](https://clawhub.ai/psyb0t/docker-modembox)

**Slug**: `docker-modembox`  
**Version**: 0.2.3  
**Stats**: ⭐ 0 | ⬇️ 121 | 🧩 6

**原始简介**: Control a configured ModemBox gateway for USB modem discovery, SMS, calls, WAV playback, caller audio and AT commands. Use when the user has a running ModemBox instance.

**中文介绍**: Control a configured ModemBox gateway for USB modem discovery, SMS, calls, WAV playback, caller audio and AT commands. Use when the user has a running ModemBox instance.

Latest changelog:
- Removed skill-card.md.

**关键词**: docker-modembox, Control, configured, ModemBox, gateway, USB, modem, discovery

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/docker-modembox)

---

## [14. ironheights](https://clawhub.ai/skills?q=ironheights)

**Slug**: `ironheights`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 11 | 🧩 1

**原始简介**: Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

**中文介绍**: Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

Latest changelog:
- Added `_meta.json` metadata.
- Removed `skill-card.md`.

**关键词**: Agent, ironheights, immune, system, protects, any, bot, installs

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ironheights)

---

## [15. Elderly Medication Compliance (Pick-up / To-mouth / Swallow) | 老年人服药动作确认（取药/入口/吞咽）](https://clawhub.ai/18072937735/smyx-elderly-medication-compliance-analysis)

**Slug**: `smyx-elderly-medication-compliance-analysis`  
**Version**: 1.0.18  
**Stats**: ⭐ 0 | ⬇️ 2614 | 🧩 19

**原始简介**: Using a fixed camera installed above or beside the home medication area, the system monitors the elderly person's full medication process in real time. With pose estimation and object detection, it recognizes three key steps: (1) picking up — hand takes a tablet/capsule out of the pill box; (2) to-mouth — hand brings the medication to the lips; (3) swallowing — throat/jaw movement indicating a swallow. | 通过家庭药箱区域上方或侧方的固定摄像头，实时监测老年人取药、服药的全过程，利用姿态估计和目标检测技术识别以下三个关键步骤：①取药（手从药盒中取出药片/胶囊）、②送入口中（手部将药物送至嘴边）、③吞咽（喉部运动或颈部吞咽动作）。当系统检测到缺步骤（例如取药后未送入口中，或送入口中后无吞咽）时，记录为'未完成服药'，并向家属或护理人员推送提醒。

**中文介绍**: Using a fixed camera installed above or beside the home medication area, the system monitors the elderly person's full medication process in real time. With pose estimation and object detection, it recognizes three key steps: (1) picking up — hand takes a tablet/capsule out of the pill box; (2) to-mouth — hand brings the medication to the lips; (3) swallowing — throat/jaw movement indicating a swallow. | 通过家庭药箱区域上方或侧方的固定摄像头，实时监测老年人取药、服药的全过程，利用姿态估计和目标检测技术识别以下三个关键步骤：①取药（手从药盒中取出药片/胶囊）、②送入口中（手部将药物送至嘴边）、③吞咽（喉部运动或颈部吞咽动作）。当系统检测到缺步骤（例如取药后未送入口中，或送入口中后无吞咽）时，记录为'未完成服药'，并向家属或护理人员推送提醒。

Latest changelog:
- Updated the skill version to 1.0.18.
- Removed `skill-card.md`.

**关键词**: 老年人服药动作确认（取药, 入口, Elderly, Medication, Compliance, Pick-up, To-mouth, Swallow

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-elderly-medication-compliance-analysis)

---

## [16. MERCATOR Address Evidence](https://clawhub.ai/arzuo/mercator-address-evidence)

**Slug**: `mercator-address-evidence`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 530 | 🧩 4

**原始简介**: Before you send a transaction, check that the chain and contract address you are about to use is the one the entity publishes for that purpose. Not a scam or rug assessment - provenance. You supply the entity, the chain, the candidate address and what you believe it is for. The answer says whether the entity's own published deployment record states that exact address, whether its own on-chain registry still points at it, and what the entity's own source says the contract does - each with the URL and a verbatim excerpt - plus a derived transact true/false. Disagreeing sources return no address at all. Covered eight protocol-and-chain cases when measured on 2026-11-21 (Lido, Aave V3, SparkLend, Uniswap V3 pool creation, ether.fi, Morpho Blue); the free preflight lists what is covered now and says whether yours is. $0.25 USDC per call over x402 on Base, charged once and only when the target is verified. Every other answer is returned in full as HTTP 404, and THIS ONE HOLDS: the x402 middleware cancels settlement on any status of 400 or above, so nothing is captured for it. You pay from your own wallet — see "Who pays" below. Triggers: "is this the official contract for X", "verify this address before I trade", "did X publish this address", "which chain is this contract on and who says it's theirs".

**中文介绍**: Before you send a transaction, check that the chain and contract address you are about to use is the one the entity publishes for that purpose. Not a scam or rug assessment - provenance. You supply the entity, the chain, the candidate address and what you believe it is for. The answer says whether the entity's own published deployment record states that exact address, whether its own on-chain registry still points at it, and what the entity's own source says the contract does - each with the URL and a verbatim excerpt - plus a derived transact true/false. Disagreeing sources return no address at all. Covered eight protocol-and-chain cases when measured on 2026-11-21 (Lido, Aave V3, SparkLend, Uniswap V3 pool creation, ether.fi, Morpho Blue); the free preflight lists what is covered now and says whether yours is. $0.25 USDC per call over x402 on Base, charged once and only when the target is verified. Every other answer is returned in full as HTTP 404, and THIS ONE HOLDS: the x402 middleware cancels settlement on any status of 400 or above, so nothing is captured for it. You pay from your own wallet — see "Who pays" below. Triggers: "is this the official contract for X", "verify this address before I trade", "did X publish this address", "which chain is this contract on and who says it's theirs".

Latest changelog:
Coverage restated: eight protocol-and-chain cases as measured on 2026-11-21 (ether.fi ETH deposit and Morpho Blue market supply added), with the current list at the free preflight. The pilot's 8 of 8 and the fixed sweep's 5 of 24 are reported separately.

**关键词**: MERCATOR, Address, Evidence, Before, send, transaction, check, chain

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mercator-address-evidence)

---

## [17. tereno](https://clawhub.ai/tereno-xyz/tereno)

**Slug**: `tereno`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 165 | 🧩 3

**原始简介**: Pre-action onchain security cache, exit simulation, cabal detection, oracle dispute auditing, and cooperative dividend economy on Base (x402 / USDC). Use before interacting with unfamiliar Base contracts or newly launched tokens, before placing prediction market bets, when seeking open verification bounties (+$0.005 bonus + 20% reuse dividends), or when enforcing ERC-8183 escrow and ERC-7579 smart account guard proofs. Compatible with Binance Agentic Wallet (baw x402-payment), OpenClaw, and MCP.

**中文介绍**: Pre-action onchain security cache, exit simulation, cabal detection, oracle dispute auditing, and cooperative dividend economy on Base (x402 / USDC). Use before interacting with unfamiliar Base contracts or newly launched tokens, before placing prediction market bets, when seeking open verification bounties (+$0.005 bonus + 20% reuse dividends), or when enforcing ERC-8183 escrow and ERC-7579 smart account guard proofs. Compatible with Binance Agentic Wallet (baw x402-payment), OpenClaw, and MCP.

Latest changelog:
- Removed `skill-card.md`; no behavior or endpoint changes are indicated.

**关键词**: tereno, Pre-action, onchain, security, cache, exit, simulation, cabal

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tereno)

---

## [18. code-crawler](https://clawhub.ai/nithin554/code-crawler)

**Slug**: `code-crawler`  
**Version**: 0.1.86  
**Stats**: ⭐ 0 | ⬇️ 561 | 🧩 21

**原始简介**: Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph. Use when the question is about how symbols connect (who calls this, what breaks if I change it, where does a request enter, is this reachable) rather than about text you can find by searching. Do not crawl a repository just to answer a question about a single file you already have open.

**中文介绍**: Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph. Use when the question is about how symbols connect (who calls this, what breaks if I change it, where does a request enter, is this reachable) rather than about text you can find by searching. Do not crawl a repository just to answer a question about a single file you already have open.

Latest changelog:
Release v0.1.96

**关键词**: an, code-crawler, Answer, questions, about, code, relationships, indexed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/code-crawler)

---

## [19. Just One API](https://clawhub.ai/oomol/oo-justoneapi)

**Slug**: `oo-justoneapi`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 303 | 🧩 3

**原始简介**: Just One API (justoneapi.com). Use this skill for ANY Just One API request — searching and reading data. Whenever a task involves Just One API, use this skill instead of calling the API directly.

**中文介绍**: Just One API (justoneapi.com). Use this skill for ANY Just One API request — searching and reading data. Whenever a task involves Just One API, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-justoneapi** v1.0.3.

Source: `oomol-lab/skills@3da2adf`

**关键词**: API, Just, One, justoneapi.com, Use, skill, ANY, request

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-justoneapi)

---

## [20. SendCloud](https://clawhub.ai/oomol/oo-sendcloud)

**Slug**: `oo-sendcloud`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 38 | 🧩 1

**原始简介**: SendCloud (sendcloud.net). Use this skill for ANY SendCloud request — reading, creating, updating, and deleting data. Whenever a task involves SendCloud, use this skill instead of calling the API directly.

**中文介绍**: SendCloud (sendcloud.net). Use this skill for ANY SendCloud request — reading, creating, updating, and deleting data. Whenever a task involves SendCloud, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-sendcloud** v1.0.0.

Source: `oomol-lab/skills@3da2adf`

**关键词**: SendCloud, sendcloud.net, Use, skill, ANY, request, reading, creating

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-sendcloud)

---

## [21. OOMOL Fusion API](https://clawhub.ai/oomol/oo-fusion-api)

**Slug**: `oo-fusion-api`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 1287 | 🧩 9

**原始简介**: OOMOL Fusion API (oomol.com). Use this skill for ANY OOMOL Fusion API request — reading, creating, updating, and deleting data. Whenever a task involves OOMOL Fusion API, use this skill instead of calling the API directly.

**中文介绍**: OOMOL Fusion API (oomol.com). Use this skill for ANY OOMOL Fusion API request — reading, creating, updating, and deleting data. Whenever a task involves OOMOL Fusion API, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-fusion-api** v1.0.12.

Source: `oomol-lab/skills@3da2adf`

**关键词**: API, OOMOL, Fusion, oomol.com, Use, skill, ANY, request

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-fusion-api)

---

## [22. Datacircle](https://clawhub.ai/oomol/oo-datacircle)

**Slug**: `oo-datacircle`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 1

**原始简介**: Datacircle (datacircle.dev). Use this skill for ANY Datacircle request — searching and reading data. Whenever a task involves Datacircle, use this skill instead of calling the API directly.

**中文介绍**: Datacircle (datacircle.dev). Use this skill for ANY Datacircle request — searching and reading data. Whenever a task involves Datacircle, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-datacircle** v1.0.0.

Source: `oomol-lab/skills@3da2adf`

**关键词**: Datacircle, datacircle.dev, Use, skill, ANY, request, searching, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-datacircle)

---

## [23. Shopify](https://clawhub.ai/oomol/oo-shopify)

**Slug**: `oo-shopify`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 951 | 🧩 5

**原始简介**: Shopify (shopify.com). Use this skill for ANY Shopify request — reading, creating, updating, and deleting data. Whenever a task involves Shopify, use this skill instead of calling the API directly.

**中文介绍**: Shopify (shopify.com). Use this skill for ANY Shopify request — reading, creating, updating, and deleting data. Whenever a task involves Shopify, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-shopify** v1.0.7.

Source: `oomol-lab/skills@3da2adf`

**关键词**: Shopify, shopify.com, Use, skill, ANY, request, reading, creating

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-shopify)

---

## [24. Football Charts](https://clawhub.ai/oomol/oo-football-charts)

**Slug**: `oo-football-charts`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 1

**原始简介**: Football Charts (football-charts.com). Use this skill for ANY Football Charts request — searching and reading data. Whenever a task involves Football Charts, use this skill instead of calling the API directly.

**中文介绍**: Football Charts (football-charts.com). Use this skill for ANY Football Charts request — searching and reading data. Whenever a task involves Football Charts, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-football-charts** v1.0.0.

Source: `oomol-lab/skills@3da2adf`

**关键词**: Football, Charts, football-charts.com, Use, skill, ANY, request, searching

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-football-charts)

---

## [25. WPS MCP](https://clawhub.ai/oomol/oo-wps-mcp)

**Slug**: `oo-wps-mcp`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 645 | 🧩 5

**原始简介**: WPS MCP (wps.cn). Use this skill for ANY WPS MCP request — reading, creating, updating, and deleting data. Whenever a task involves WPS MCP, use this skill instead of calling the API directly.

**中文介绍**: WPS MCP (wps.cn). Use this skill for ANY WPS MCP request — reading, creating, updating, and deleting data. Whenever a task involves WPS MCP, use this skill instead of calling the API directly.

Latest changelog:
Automated publish of **oo-wps-mcp** v1.0.6.

Source: `oomol-lab/skills@3da2adf`

**关键词**: WPS, MCP, wps.cn, Use, skill, ANY, request, reading

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/oo-wps-mcp)

---

