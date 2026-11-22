# ClawHub Skills Daily | 2026-11-22

> 共 25 个 skills

## [1. x402-layer](https://clawhub.ai/ivaavimusic/x402-layer)

**Slug**: `x402-layer`  
**Version**: 1.17.0  
**Stats**: ⭐ 7 | ⬇️ 4480 | 🧩 35

**原始简介**: x402-layer helps agents pay for APIs with USDC, deploy monetized endpoints, manage credits/webhooks/marketplace listings, and handle wallet-first ERC-8004 registration/discovery/management/reputation on Base, Ethereum, Polygon, BSC, Monad, and Solana. Optional credentialed flows may use private keys, Solana signer keys, endpoint API keys, PATs, AWAL, or OWS depending on the exact runbook; read-only discovery requires no secrets. Only ask for or use privileged credentials after choosing a runbook that actually needs signing or owner-scoped writes. Use this skill when the user asks to "create x402 endpoint", "deploy monetized API", "pay for API with USDC", "check x402 credits", "consume API credits", "list endpoint on marketplace", "buy API credits", "topup endpoint", "browse x402 marketplace", "plan a flow of x402 services", "set up webhook", "receive payment notifications", "manage endpoint webhook", "verify webhook payment", "verify payment genuineness", "integrate crypto payments into my app", "add USDC payments to my platform", "sell with x402", "build a paywall with webhooks", "register ERC-8004 agent", "register Solana 8004 agent", "submit on-chain reputation feedback", "rate ERC-8004 agent", "use World AgentKit", "unlock human-backed agent wallet discount", "check if an endpoint has an AgentKit benefit", "add API schema to endpoint", "document my API routes", "auto-detect OpenAPI schema", "open support chat", use "Coinbase Agentic Wallet (AWAL)", "OpenWallet", "OWS", "openwallet.sh", or use optional Singularity MCP access with a dashboard PAT to manage x402 Singularity Layer operations on Base, Ethereum, Polygon, BSC, Monad, or Solana networks. Also use this skill to stake $SGL agentically: "stake SGL", "stake $SGL", "unstake SGL", "claim staking rewards", "check my staking position", "stake to run a node", "agentic staking" — sign and submit on-chain Solana staking transactions with a wallet keypair.

**中文介绍**: x402-layer helps agents pay for APIs with USDC, deploy monetized endpoints, manage credits/webhooks/marketplace listings, and handle wallet-first ERC-8004 registration/discovery/management/reputation on Base, Ethereum, Polygon, BSC, Monad, and Solana. Optional credentialed flows may use private keys, Solana signer keys, endpoint API keys, PATs, AWAL, or OWS depending on the exact runbook; read-only discovery requires no secrets. Only ask for or use privileged credentials after choosing a runbook that actually needs signing or owner-scoped writes. Use this skill when the user asks to "create x402 endpoint", "deploy monetized API", "pay for API with USDC", "check x402 credits", "consume API credits", "list endpoint on marketplace", "buy API credits", "topup endpoint", "browse x402 marketplace", "plan a flow of x402 services", "set up webhook", "receive payment notifications", "manage endpoint webhook", "verify webhook payment", "verify payment genuineness", "integrate crypto payments into my app", "add USDC payments to my platform", "sell with x402", "build a paywall with webhooks", "register ERC-8004 agent", "register Solana 8004 agent", "submit on-chain reputation feedback", "rate ERC-8004 agent", "use World AgentKit", "unlock human-backed agent wallet discount", "check if an endpoint has an AgentKit benefit", "add API schema to endpoint", "document my API routes", "auto-detect OpenAPI schema", "open support chat", use "Coinbase Agentic Wallet (AWAL)", "OpenWallet", "OWS", "openwallet.sh", or use optional Singularity MCP access with a dashboard PAT to manage x402 Singularity Layer operations on Base, Ethereum, Polygon, BSC, Monad, or Solana networks. Also use this skill to stake $SGL agentically: "stake SGL", "stake $SGL", "unstake SGL", "claim staking rewards", "check my staking position", "stake to run a node", "agentic staking" — sign and submit on-chain Solana staking transactions with a wallet keypair.

Latest changelog:
x402 v2 payments: when a 402 carries a PAYMENT-REQUIRED header the payment scripts pay with x402 v2 (PAYMENT-SIGNATURE), otherwise v1 exactly as before. X402_WIRE=v1 forces v1. A 202, 5xx or timeout after paying is reported as pending, never as failed, so agents do not pay twice. consume_product.py fixed (base64 header, current URL). Endpoint create/top-up docs: pending (202) and one payment = one use (409).

**关键词**: Agent, x402-layer, helps, pay, APIs, USDC, deploy, monetized

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/x402-layer)

---

## [2. Agentreeve BTC Intelligence](https://clawhub.ai/shakeelamjid/btc-intelligence)

**Slug**: `btc-intelligence`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 166 | 🧩 3

**原始简介**: Crypto market data for agents from AgentReeve - prices, candles, derivatives (funding, basis, open interest), long/short positioning, order-book liquidity and a one-call snapshot for any coin on Binance, Bybit, OKX and Hyperliquid, scanners for extreme funding and crowded trades, and Bitcoin depth (options, liquidations, whales, similar setups). Paid per request over x402, free samples.

**中文介绍**: Crypto market data for agents from AgentReeve - prices, candles, derivatives (funding, basis, open interest), long/short positioning, order-book liquidity and a one-call snapshot for any coin on Binance, Bybit, OKX and Hyperliquid, scanners for extreme funding and crowded trades, and Bitcoin depth (options, liquidations, whales, similar setups). Paid per request over x402, free samples.

Latest changelog:
- Expanded from Bitcoin-only intelligence to crypto market data for any supported coin, including stock, forex, and commodity perpetuals.
- Updated endpoints and product list; added a markets lookup for 900+ coins and any-coin price, candles, derivatives, positioning, liquidity, and snapshot products.
- Refocused Bitcoin-specific options, liquidation, whale, and similar-setup data as BTC products.
- Updated product pricing and MCP tool names. Payment safeguards and data-quality guidance remain.

**关键词**: Agent, Agentreeve, BTC, Intelligence, Crypto, market, data, prices

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/btc-intelligence)

---

## [3. No Slop UI](https://clawhub.ai/leostehlik/no-slop-ui)

**Slug**: `no-slop-ui`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 1859 | 🧩 11

**原始简介**: Build or review frontend UI for clean, restrained, human-designed interfaces without generic AI visual patterns.

**中文介绍**: Build or review frontend UI for clean, restrained, human-designed interfaces without generic AI visual patterns.

Latest changelog:
Add proven Astro/React-islands/Tailwind v4/Base UI-coss stack recipes plus shipped WrenLore and DoubleMint screenshots and implementation notes.

**关键词**: No, UI, or, Slop, Build, review, frontend, clean

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/no-slop-ui)

---

## [4. logicpot](https://clawhub.ai/logic/logicpot)

**Slug**: `logicpot`  
**Version**: 2.4.0  
**Stats**: ⭐ 0 | ⬇️ 227 | 🧩 7

**原始简介**: An open exchange where AI agents ask each other for help and earn by answering, on LogicPot. Search problems agents already solved (with verified answers), post a new problem free (just an api_key) and collect answers; or find problems other agents posted, some free puzzles and some with USDC rewards paid on-chain for verified answers (checker, hidden tests, sealed answer or the setter's pick). Also a free daily reasoning puzzle with a USDC prize. Use when you are stuck on a sub-problem and want other agents' answers, when your owner asks you to earn money solving problems, to post a puzzle or bounty, or to play today's puzzle.

**中文介绍**: An open exchange where AI agents ask each other for help and earn by answering, on LogicPot. Search problems agents already solved (with verified answers), post a new problem free (just an api_key) and collect answers; or find problems other agents posted, some free puzzles and some with USDC rewards paid on-chain for verified answers (checker, hidden tests, sealed answer or the setter's pick). Also a free daily reasoning puzzle with a USDC prize. Use when you are stuck on a sub-problem and want other agents' answers, when your owner asks you to earn money solving problems, to post a puzzle or bounty, or to play today's puzzle.

Latest changelog:
Open exchange: search solved problems first (search_solved, /api/knowledge), set topics (watch_topics), find_problems lists problems for you, answering earns extra daily-puzzle answers. Posting without a kind defaults to best answer.

**关键词**: An, Agent, logicpot, open, exchange, where, ask, each

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/logicpot)

---

## [5. GitLab Agent](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent)

**Slug**: `xrowgmbh-gitlab-agent`  
**Version**: 1.151.2  
**Stats**: ⭐ 1 | ⬇️ 8436 | 🧩 218

**原始简介**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

**中文介绍**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

Latest changelog:
- Removed the `skill-card.md` file.

**关键词**: Agent, GitLab, Operate, assigned, work, owner-verified, project, access

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent)

---

## [6. GitLab Agent Profile](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent-profile)

**Slug**: `xrowgmbh-gitlab-agent-profile`  
**Version**: 1.151.2  
**Stats**: ⭐ 0 | ⬇️ 7766 | 🧩 191

**原始简介**: Maintain the GitLab agent profile page and static contribution performance chart.

**中文介绍**: Maintain the GitLab agent profile page and static contribution performance chart.

Latest changelog:
- Removed the unused `skill-card.md` file.

**关键词**: Agent, GitLab, Profile, Maintain, page, static, contribution, performance

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent-profile)

---

## [7. GitLab Meeting Assistant](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-meeting-assistant)

**Slug**: `xrowgmbh-gitlab-meeting-assistant`  
**Version**: 1.151.2  
**Stats**: ⭐ 0 | ⬇️ 2022 | 🧩 71

**原始简介**: Capture meeting features and bugs on explicit request

**中文介绍**: Capture meeting features and bugs on explicit request

Latest changelog:
- Removed `skill-card.md`.

**关键词**: GitLab, Meeting, Assistant, Capture, features, bugs, explicit, request

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-meeting-assistant)

---

## [8. GitLab Hackathon](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-hackathon)

**Slug**: `xrowgmbh-gitlab-hackathon`  
**Version**: 1.151.2  
**Stats**: ⭐ 0 | ⬇️ 8597 | 🧩 224

**原始简介**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

**中文介绍**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

Latest changelog:
- Removed `skill-card.md`. No changes to `SKILL.md`.

**关键词**: GitLab, Hackathon, Plan, execute, fair, participation, including, Quarterly

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-hackathon)

---

## [9. Image Generation](https://clawhub.ai/xrowgmbh/xrowgmbh-image-generation)

**Slug**: `xrowgmbh-image-generation`  
**Version**: 1.151.2  
**Stats**: ⭐ 1 | ⬇️ 8355 | 🧩 192

**原始简介**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

**中文介绍**: Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: or, Image, Generation, revise, document, PDF, web, review

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-image-generation)

---

## [10. CI Tools Pipeline](https://clawhub.ai/xrowgmbh/xrowgmbh-ci-tools-pipeline)

**Slug**: `xrowgmbh-ci-tools-pipeline`  
**Version**: 4.242.1  
**Stats**: ⭐ 0 | ⬇️ 6270 | 🧩 161

**原始简介**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing GitLab pipeline files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

**中文介绍**: Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. Use when creating or fixing GitLab pipeline files, choosing CI Tools components, validating component inputs, or designing continuous delivery pipelines for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps.

Latest changelog:
- Removed `skill-card.md`.
- No changes to the pipeline guidance in `SKILL.md`.

**关键词**: CI, CD, Tools, Pipeline, Build, maintain, GitLab, pipelines

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-ci-tools-pipeline)

---

## [11. GitLab Agent Self Improvement](https://clawhub.ai/xrowgmbh/xrowgmbh-self-improvement)

**Slug**: `xrowgmbh-self-improvement`  
**Version**: 1.151.2  
**Stats**: ⭐ 0 | ⬇️ 9192 | 🧩 230

**原始简介**: A skill for personal growth and self-improvement.

**中文介绍**: A skill for personal growth and self-improvement.

Latest changelog:
- Removed the `skill-card.md` file. The skill instructions are unchanged.

**关键词**: Agent, GitLab, Self, Improvement, skill, personal, growth, self-improvement

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-self-improvement)

---

## [12. btc-derivatives-check](https://clawhub.ai/shakeelamjid/btc-derivatives-check)

**Slug**: `btc-derivatives-check`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 173 | 🧩 3

**原始简介**: Before a Bitcoin trade, check the derivatives picture across exchanges - funding and basis, open interest, long/short positioning, recent liquidations and where the large order-book walls are. Live data from AgentReeve; free samples, live data per request over x402 (USDC on Base).

**中文介绍**: Before a Bitcoin trade, check the derivatives picture across exchanges - funding and basis, open interest, long/short positioning, recent liquidations and where the large order-book walls are. Live data from AgentReeve; free samples, live data per request over x402 (USDC on Base).

Latest changelog:
- Updated API endpoints for derivatives, positioning, and liquidity data.
- Derivatives data now includes open interest, options, and term structure; liquidity data includes depth and slippage alongside order-book walls.
- Added support for checking other coins, while noting that liquidations data remains Bitcoin-only.
- Removed `skill-card.md`.

**关键词**: btc-derivatives-check, Before, Bitcoin, trade, check, derivatives, picture, across

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/btc-derivatives-check)

---

## [13. Plant Wilting Quantification (Underwatering / Overwatering) | 植物萎蔫程度量化（缺水/水多）](https://clawhub.ai/18072937735/smyx-plant-wilting-quantification-analysis)

**Slug**: `smyx-plant-wilting-quantification-analysis`  
**Version**: 1.0.21  
**Stats**: ⭐ 0 | ⬇️ 2408 | 🧩 19

**原始简介**: AI-powered plant wilting quantification from full-plant images via smart pots or fixed cameras. Detects leaf-stem angle (leaf droop), stem straightness, and leaf turgidity to quantify wilting severity (0-100%). Optionally fuses soil-moisture sensor data to discriminate dehydration (underwatering) vs. waterlogging (root hypoxia), and auto-triggers watering or drainage prompts for precision irrigation. Scenarios: smart pots, home gardening, greenhouses, plant factories. | 通过智能花盆或固定摄像头拍摄植物整体图像，利用AI视觉分析技术检测叶片与茎秆的夹角（叶片下垂角度）、茎秆挺直程度以及叶片舒展度，量化萎蔫程度（0-100%）。可选结合土壤湿度传感器数据，综合判断萎蔫原因是缺水还是水涝（根部缺氧导致）。可自动触发灌溉或排水提示，帮助用户精准浇水。应用场景：智能花盆、家庭园艺、温室大棚、植物工厂。

**中文介绍**: AI-powered plant wilting quantification from full-plant images via smart pots or fixed cameras. Detects leaf-stem angle (leaf droop), stem straightness, and leaf turgidity to quantify wilting severity (0-100%). Optionally fuses soil-moisture sensor data to discriminate dehydration (underwatering) vs. waterlogging (root hypoxia), and auto-triggers watering or drainage prompts for precision irrigation. Scenarios: smart pots, home gardening, greenhouses, plant factories. | 通过智能花盆或固定摄像头拍摄植物整体图像，利用AI视觉分析技术检测叶片与茎秆的夹角（叶片下垂角度）、茎秆挺直程度以及叶片舒展度，量化萎蔫程度（0-100%）。可选结合土壤湿度传感器数据，综合判断萎蔫原因是缺水还是水涝（根部缺氧导致）。可自动触发灌溉或排水提示，帮助用户精准浇水。应用场景：智能花盆、家庭园艺、温室大棚、植物工厂。

Latest changelog:
- Updated the skill version from 1.0.21 to 1.0.23.
- Removed `skill-card.md`.
- No changes to `SKILL.md` content.

**关键词**: 植物萎蔫程度量化（缺水, 水多）, Plant, Wilting, Quantification, Underwatering, Overwatering, AI-powered

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-plant-wilting-quantification-analysis)

---

## [14. Odds-API.io](https://clawhub.ai/odds-api-io/odds-api-io)

**Slug**: `odds-api-io`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use the Odds-API.io MCP server to answer questions about sports betting odds, events, results, value bets, arbitrage, dropping odds, closing lines, bet settlement and golf outrights. Covers which tool to call first, how to keep responses small, quotas and error handling.

**中文介绍**: Use the Odds-API.io MCP server to answer questions about sports betting odds, events, results, value bets, arbitrage, dropping odds, closing lines, bet settlement and golf outrights. Covers which tool to call first, how to keep responses small, quotas and error handling.

Latest changelog:
Initial release: agent guide for the Odds-API.io MCP server

**关键词**: Odds-API.io, Use, MCP, server, answer, questions, about, sports

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/odds-api-io)

---

## [15. karman](https://clawhub.ai/logic/karman)

**Slug**: `karman`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Query Karman, a monitor for small Solar System bodies whose motion gravity does not explain (non-gravitational accelerations, interstellar visitors). Use when the user asks which asteroids or comets move anomalously, why an object got its label, how the evidence compares with JPL, what the watch has seen lately, or how the method was validated.

**中文介绍**: Query Karman, a monitor for small Solar System bodies whose motion gravity does not explain (non-gravitational accelerations, interstellar visitors). Use when the user asks which asteroids or comets move anomalously, why an object got its label, how the evidence compares with JPL, what the watch has seen lately, or how the method was validated.

Latest changelog:
- Clarified that the interstellar visitor watch runs on demand.
- Removed `skill-card.md`.

**关键词**: karman, Query, monitor, small, Solar, System, bodies, whose

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/karman)

---

## [16. Obscurify.ai](https://clawhub.ai/obscurify/obscurify)

**Slug**: `obscurify`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 161 | 🧩 2

**原始简介**: Use Obscurify.ai as a model provider through its OpenAI-compatible API (200+ models, an account code instead of email). Use when asked to add, configure or troubleshoot Obscurify.ai in an agent or tool.

**中文介绍**: Use Obscurify.ai as a model provider through its OpenAI-compatible API (200+ models, an account code instead of email). Use when asked to add, configure or troubleshoot Obscurify.ai in an agent or tool.

Latest changelog:
Account codes and CLI sign-up, corrected privacy and plan limits, Claude Code setup, secret scrubbing and private sessions

**关键词**: as, Obscurify.ai, Use, model, provider, through, its, OpenAI-compatible

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/obscurify)

---

## [17. postfast](https://clawhub.ai/peturgeorgievv/postfast)

**Slug**: `postfast`  
**Version**: 1.21.1  
**Stats**: ⭐ 8 | ⬇️ 6857 | 🧩 40

**原始简介**: Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API. Use when the user wants to schedule social media posts, upload media for social posting, list connected social accounts, check scheduled posts (filtered by account, platform, status or date), delete posts one at a time or up to 100 per call, cross-post content to multiple platforms, manage Google Business Profile posts, geotag posts with real-world places, pick trending pre-cleared TikTok sounds, read or reply to the comments on their posts (social inbox on TikTok, Instagram, Facebook, Threads), triage or moderate comment conversations, generate a connect link so an agency client or their own app's user can connect accounts without a PostFast account, get webhooks when a post publishes or fails or an account disconnects, or automate their social media workflow. PostFast is a SaaS tool, no self-hosting required.

**中文介绍**: Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API. Use when the user wants to schedule social media posts, upload media for social posting, list connected social accounts, check scheduled posts (filtered by account, platform, status or date), delete posts one at a time or up to 100 per call, cross-post content to multiple platforms, manage Google Business Profile posts, geotag posts with real-world places, pick trending pre-cleared TikTok sounds, read or reply to the comments on their posts (social inbox on TikTok, Instagram, Facebook, Threads), triage or moderate comment conversations, generate a connect link so an agency client or their own app's user can connect accounts without a PostFast account, get webhooks when a post publishes or fails or an account disconnects, or automate their social media workflow. PostFast is a SaaS tool, no self-hosting required.

Latest changelog:
TikTok privacy wording now matches the API docs: tiktokPrivacy is deprecated, do not rely on it to choose who sees a post, send a draft to post privately. X first-comment examples carry no link, since a link on X needs an active paid plan. Example post dates moved into the future. Reference regenerated from the docs.

**关键词**: postfast, Schedule, manage, social, media, posts, across, TikTok

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/postfast)

---

## [18. Zeli — Hacker News Summaries in Your Language](https://clawhub.ai/mazzzystar/zeli-hacker-news)

**Slug**: `zeli-hacker-news`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 746 | 🧩 3

**原始简介**: Read Hacker News with AI summaries in your human's language (7 supported) via zeli.app. Fetch the daily front-page digest as markdown or JSON, link permanent per-story summary pages, or subscribe via RSS. Use when your human wants Hacker News coverage, a daily tech briefing, or HN in a language other than English.

**中文介绍**: Read Hacker News with AI summaries in your human's language (7 supported) via zeli.app. Fetch the daily front-page digest as markdown or JSON, link permanent per-story summary pages, or subscribe via RSS. Use when your human wants Hacker News coverage, a daily tech briefing, or HN in a language other than English.

Latest changelog:
Add per-story markdown (/story/{id}.md, /{lang}/story/{id}.md) with canonical Link, noindex and ETag; clarify when a story's markdown becomes available and caching etiquette for young stories.

**关键词**: Zeli, Hacker, News, Summaries, Language, Read, human's, supported

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zeli-hacker-news)

---

## [19. Galleon DefiLlama Yield Screen](https://clawhub.ai/galleonlabs/galleon-defillama-yield-screen)

**Slug**: `galleon-defillama-yield-screen`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 288 | 🧩 3

**原始简介**: Screen yields by token, chain and base return

**中文介绍**: Screen yields by token, chain and base return

Latest changelog:
Compare a market mark with an exact timestamped Coinbase Exchange trade.

**关键词**: Galleon, DefiLlama, Yield, Screen, yields, token, chain, base

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-defillama-yield-screen)

---

## [20. Galleon DeFi Market Snapshot](https://clawhub.ai/galleonlabs/galleon-defi-market-snapshot)

**Slug**: `galleon-defi-market-snapshot`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 290 | 🧩 3

**原始简介**: Collect sourced prices and validated daily history

**中文介绍**: Collect sourced prices and validated daily history

Latest changelog:
Compare a market mark with an exact timestamped Coinbase Exchange trade.

**关键词**: Galleon, DeFi, Market, Snapshot, Collect, sourced, prices, validated

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-defi-market-snapshot)

---

## [21. Nextrap Attack Intelligence](https://clawhub.ai/nextrap-net/nextrap-cli)

**Slug**: `nextrap-cli`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Use Nextrap CLI to investigate public attack intelligence by IP, URL, or product name. Search the product catalog and request logs, inspect context and path statistics, or manage CLI authentication and updates.

**中文介绍**: Use Nextrap CLI to investigate public attack intelligence by IP, URL, or product name. Search the product catalog and request logs, inspect context and path statistics, or manage CLI authentication and updates.

Latest changelog:
English summary and bilingual CLI installation guide, matching the GitHub v1.0.6 release.

**关键词**: IP, Nextrap, Attack, Intelligence, Use, CLI, investigate, public

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nextrap-cli)

---

## [22. Galleon CoinGecko Token Research](https://clawhub.ai/galleonlabs/galleon-coingecko-token-research)

**Slug**: `galleon-coingecko-token-research`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 279 | 🧩 3

**原始简介**: Resolve token contracts and dated market evidence

**中文介绍**: Resolve token contracts and dated market evidence

Latest changelog:
Compare a market mark with an exact timestamped Coinbase Exchange trade.

**关键词**: Galleon, CoinGecko, Token, Research, Resolve, contracts, dated, market

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-coingecko-token-research)

---

## [23. Galleon DeFi Data](https://clawhub.ai/galleonlabs/galleon-defi-data)

**Slug**: `galleon-defi-data`  
**Version**: 0.8.0  
**Stats**: ⭐ 0 | ⬇️ 292 | 🧩 3

**原始简介**: Connect and validate DeFi market data sources

**中文介绍**: Connect and validate DeFi market data sources

Latest changelog:
Compare a market mark with an exact timestamped Coinbase Exchange trade.

**关键词**: Galleon, DeFi, Data, Connect, validate, market, sources, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-defi-data)

---

## [24. Sablier streams](https://clawhub.ai/galleonlabs/galleon-sablier-streams)

**Slug**: `galleon-sablier-streams`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 284 | 🧩 2

**原始简介**: Sablier streams workflow and evidence

**中文介绍**: Sablier streams workflow and evidence

Latest changelog:
Compare invoice terms with transfer logs and canonical RPC evidence.

**关键词**: Sablier, streams, workflow, evidence, Latest, changelog, Compare, invoice

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-sablier-streams)

---

## [25. ERC-20 payment receipt](https://clawhub.ai/galleonlabs/galleon-erc20-payment-receipt)

**Slug**: `galleon-erc20-payment-receipt`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Check transfer parties, raw amount and block finality

**中文介绍**: Check transfer parties, raw amount and block finality

Latest changelog:
Compare invoice terms with transfer logs and canonical RPC evidence.

**关键词**: ERC-20, payment, receipt, Check, transfer, parties, raw, amount

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/galleon-erc20-payment-receipt)

---

