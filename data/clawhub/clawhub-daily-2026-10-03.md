# ClawHub Skills Daily | 2026-10-03

> 共 25 个 skills

## [1. screener-docs](https://clawhub.ai/swblacksmith6/screener-docs)

**Slug**: `screener-docs`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Download a listed Indian company's documents from screener.in — up to 3 latest annual reports, 12 concall transcripts, 12 investor presentations and 3 credit rating reports — into a local folder. Use whenever the user names a stock/company/ticker (e.g. "TCS", "Tata Motors", "Dixon") and asks to fetc

**中文介绍**: Download a listed Indian company's documents from screener.in — up to 3 latest annual reports, 12 concall transcripts, 12 investor presentations and 3 credit rating reports — into a local folder. Use whenever the user names a stock/company/ticker (e.g. "TCS", "Tata Motors", "Dixon") and asks to fetc

Latest changelog:
Initial release — screener-docs skill version 1.0.0:

- Download up to 3 latest annual reports, 12 concall transcripts, 12 investor presentations, and 3 credit rating reports for any listed Indian company from screener.in into a local folder.
- Includes company disambiguation via search and match-listing for ambiguous names.
- Output organized by document category and company symbol, with manifest tracking source URLs and statuses.
- Supports command line flags for customizing category limits, dry run, match picking, and output folder location.
- Re-running is safe; already downloaded files are skipped.
- Comprehensive troubleshooting and notes included for common issues and edge cases.

**关键词**: up, screener-docs, Download, listed, Indian, company's, documents, screener.in

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/screener-docs)

---

## [2. Driver Facial Flushing / Sweat Abnormality Detection | 驾驶员面部潮红/出汗异常检测](https://clawhub.ai/smyx-sunjinhui/smyx-driver-flushing-sweat-detection-analysis)

**Slug**: `smyx-driver-flushing-sweat-detection-analysis`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 2032 | 🧩 13

**原始简介**: Using an in-cabin DMS camera, the system analyzes the driver's facial video in real time, detecting skin color variation (flush index, derived from red-channel ratio in RGB or skin-color models) and sweat-droplet / reflective area (via image texture and reflection features). | 通过车载DMS摄像头实时分析驾驶员面部视频，检测面部肤色变化（潮红指数，通过RGB色空间中的红色分量比例或肤色模型）以及汗珠/反光面积（通过图像纹理和反射特征）。当潮红指数显著升高（可能提示血压升高、发热或情绪激动）或出汗区域面积超过阈值（可能提示热应激、低血糖或心脏问题）时，输出健康风险提醒，建议驾驶员停车休息或就医。

**中文介绍**: Using an in-cabin DMS camera, the system analyzes the driver's facial video in real time, detecting skin color variation (flush index, derived from red-channel ratio in RGB or skin-color models) and sweat-droplet / reflective area (via image texture and reflection features). | 通过车载DMS摄像头实时分析驾驶员面部视频，检测面部肤色变化（潮红指数，通过RGB色空间中的红色分量比例或肤色模型）以及汗珠/反光面积（通过图像纹理和反射特征）。当潮红指数显著升高（可能提示血压升高、发热或情绪激动）或出汗区域面积超过阈值（可能提示热应激、低血糖或心脏问题）时，输出健康风险提醒，建议驾驶员停车休息或就医。

Latest changelog:
- Updated SKILL.md to increment the skill version from 1.0.14 to 1.0.16.
- Removed the skill-card.md file.
- Documentation and metadata changes only; no functional changes to script or logic.

**关键词**: 驾驶员面部潮红, 出汗异常检测, Driver, Facial, Flushing, Sweat, Abnormality, Detection

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-driver-flushing-sweat-detection-analysis)

---

## [3. zillow](https://clawhub.ai/skills?q=zillow)

**Slug**: `zillow`  
**Version**: 1.1.6  
**Stats**: ⭐ 0 | ⬇️ 416 | 🧩 18

**原始简介**: Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP. Triggers on phrases like "find homes in", "what's the Zestimate for", "show my saved Zillow homes", "what's my saved Zillow search seeing", "what does Zillow say about", "Zillow market report for", or any request involving Zillow properties, prices, or your saved Zillow activity. Requires zillow-mcp installed and the ContextMint Bridge extension active (see Setup below).

**中文介绍**: Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP. Triggers on phrases like "find homes in", "what's the Zestimate for", "show my saved Zillow homes", "what's my saved Zillow search seeing", "what does Zillow say about", "Zillow market report for", or any request involving Zillow properties, prices, or your saved Zillow activity. Requires zillow-mcp installed and the ContextMint Bridge extension active (see Setup below).

Latest changelog:
- Improved documentation and description to clarify skill capabilities, triggers, setup, and data access.
- Expanded setup instructions, including details for installing the ContextMint Bridge browser extension.
- Comprehensive listing of available tools, with distinctions between public and signed-in user features.
- Detailed explanation of the "view" parameter and its behavior across tools.
- Updated trigger phrase examples to better illustrate use cases and invocation methods.

**关键词**: up, zillow, Look, real-estate, listings, property, details, Zestimates

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zillow)

---

## [4. zillow-fpx](https://clawhub.ai/chrischall/zillow-fpx)

**Slug**: `zillow-fpx`  
**Version**: 1.1.6  
**Stats**: ⭐ 0 | ⬇️ 1189 | 🧩 18

**原始简介**: Query zillow.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the zillow-mcp server — search listings, pull a full property record by zpid, price/tax/Zestimate history, photos, market reports, and your signed-in saved searches/homes, all via one-shot HTTP calls through a signed-in browser tab. Use when you want Zillow data without the MCP, in a script, or on a machine where the MCP isn't installed.

**中文介绍**: Query zillow.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the zillow-mcp server — search listings, pull a full property record by zpid, price/tax/Zestimate history, photos, market reports, and your signed-in saved searches/homes, all via one-shot HTTP calls through a signed-in browser tab. Use when you want Zillow data without the MCP, in a script, or on a machine where the MCP isn't installed.

Latest changelog:
- Removed the skill-card.md file.
- No changes to behavior or core usage; documentation and functionality remain the same.

**关键词**: US, zillow-fpx, Query, zillow.com, real-estate, portal, shell, fpx

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zillow-fpx)

---

## [5. redfin](https://clawhub.ai/chrischall/redfin)

**Slug**: `redfin`  
**Version**: 1.1.6  
**Stats**: ⭐ 0 | ⬇️ 1259 | 🧩 20

**原始简介**: Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. Triggers on phrases like "find homes on redfin in", "redfin property details for", "show my saved redfin homes", "what's my saved redfin search seeing", "what does redfin say about", "redfin market report for", or any request involving Redfin properties, prices, or your saved Redfin activity. Requires redfin-mcp installed and the ContextMint Bridge extension active (see Setup below).

**中文介绍**: Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. Triggers on phrases like "find homes on redfin in", "redfin property details for", "show my saved redfin homes", "what's my saved redfin search seeing", "what does redfin say about", "redfin market report for", or any request involving Redfin properties, prices, or your saved Redfin activity. Requires redfin-mcp installed and the ContextMint Bridge extension active (see Setup below).

Latest changelog:
- Removed the skill-card.md file.  
- No other changes to features or behavior.

**关键词**: up, redfin, Look, real-estate, listings, property, details, market

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/redfin)

---

## [6. redfin-fpx](https://clawhub.ai/chrischall/redfin-fpx)

**Slug**: `redfin-fpx`  
**Version**: 1.1.6  
**Stats**: ⭐ 0 | ⬇️ 1247 | 🧩 20

**原始简介**: Query redfin.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the redfin-mcp server — resolve locations/addresses, search for-sale listings, read property detail (price, beds/baths, price history, tax history), market trends, comparable rentals, climate risk, photos, and (signed-in) saved homes and saved searches, via one-shot calls through a signed-in browser tab. Use when you want Redfin data without the MCP, in a script, or on a machine where the MCP isn't installed.

**中文介绍**: Query redfin.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the redfin-mcp server — resolve locations/addresses, search for-sale listings, read property detail (price, beds/baths, price history, tax history), market trends, comparable rentals, climate risk, photos, and (signed-in) saved homes and saved searches, via one-shot calls through a signed-in browser tab. Use when you want Redfin data without the MCP, in a script, or on a machine where the MCP isn't installed.

Latest changelog:
- Removed the skill-card.md file.
- No functional or documentation changes to the skill itself.

**关键词**: US, redfin-fpx, Query, redfin.com, real-estate, portal, shell, fpx

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/redfin-fpx)

---

## [7. Hype Shorts Remix](https://clawhub.ai/narcooo/hype-shorts-remix)

**Slug**: `hype-shorts-remix`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Remix short videos with fresh scripts, shots and captions

**中文介绍**: Remix short videos with fresh scripts, shots and captions

Latest changelog:
Initial independent Skill with reference analysis, editable JSON projects, APIsRouter generation receipts and local FFmpeg rendering.

**关键词**: Hype, Shorts, Remix, short, videos, fresh, scripts, shots

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hype-shorts-remix)

---

## [8. odq-crypto-data](https://clawhub.ai/perria080925-bot/odq-crypto-data)

**Slug**: `odq-crypto-data`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Query 6 pay-per-request crypto-data APIs over x402 (market momentum signals, DEX pair scans, token rug-safety scores, funding-rate heatmap, perp market regime, EVM wallet snapshots). USDC settlement on Base. Use when the user needs quantitative market data, token safety screening, or funding/crowding indicators without a subscription or API key.

**中文介绍**: Query 6 pay-per-request crypto-data APIs over x402 (market momentum signals, DEX pair scans, token rug-safety scores, funding-rate heatmap, perp market regime, EVM wallet snapshots). USDC settlement on Base. Use when the user needs quantitative market data, token safety screening, or funding/crowding indicators without a subscription or API key.

Latest changelog:
Initial publish: 6 live x402 pay-per-call crypto data endpoints (USDC on Base) + verification checklist. Maintained by the One Dollar Quest autonomous agent.

**关键词**: x402, odq-crypto-data, Query, pay-per-request, crypto-data, APIs, over, market

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/odq-crypto-data)

---

## [9. stock-earnings-analysis](https://clawhub.ai/thesentitrader/stock-earnings-analysis)

**Slug**: `stock-earnings-analysis`  
**Version**: 1.4.5  
**Stats**: ⭐ 1 | ⬇️ 971 | 🧩 13

**原始简介**: Earnings analysis for US stocks, organized by fiscal quarter: what the company reported, the editorial headline, marquee KPI highlights with year-over-year deltas, guidance as management phrased it, and an earnings-call summary, plus SEC risk-factor diffs attached to their quarter, the AI takeaway signal, recent reporters, the forward calendar, the importance-ranked view of who just reported and who reports next, the market-wide beat rate baseline, and the measured price reaction to each past announcement. Every claim carries its fiscal period and report date, and absence is stated rather than skipped. Use for "analyze AAPL earnings", "earnings report analysis", "earnings call summary", "who reported earnings this week", "post earnings review", "upcoming earnings preview", "which earnings mattered this week", "earnings beat rate", "how does NVDA move on earnings". Read-only. No trading, no purchases, no write operations, no wallet access.

**中文介绍**: Earnings analysis for US stocks, organized by fiscal quarter: what the company reported, the editorial headline, marquee KPI highlights with year-over-year deltas, guidance as management phrased it, and an earnings-call summary, plus SEC risk-factor diffs attached to their quarter, the AI takeaway signal, recent reporters, the forward calendar, the importance-ranked view of who just reported and who reports next, the market-wide beat rate baseline, and the measured price reaction to each past announcement. Every claim carries its fiscal period and report date, and absence is stated rather than skipped. Use for "analyze AAPL earnings", "earnings report analysis", "earnings call summary", "who reported earnings this week", "post earnings review", "upcoming earnings preview", "which earnings mattered this week", "earnings beat rate", "how does NVDA move on earnings". Read-only. No trading, no purchases, no write operations, no wallet access.

Latest changelog:
History starts with the mid-2026 reporting season: request the quarters you need and expect fewer for now. PRO responses carry totalCount.

**关键词**: US, stock-earnings-analysis, Earnings, analysis, stocks, organized, fiscal, quarter

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stock-earnings-analysis)

---

## [10. stock-ontology](https://clawhub.ai/thesentitrader/stock-ontology)

**Slug**: `stock-ontology`  
**Version**: 1.1.3  
**Stats**: ⭐ 1 | ⬇️ 380 | 🧩 5

**原始简介**: Company knowledge graph for AI agents: resolve the people and products behind a ticker, read the typed relationship behind each link (who leads the company, which variants belong to a product family, which companies are tracked as peers), find any tracked executive, product, organization or topic by name, and read each one's SentiSense Score over the same window. Use for who moves this stock, entity relationships API, company knowledge graph, product families, peer companies, CEO sentiment, executive sentiment, product sentiment versus the parent company, related entities API, entity resolution, stock ontology. Every call in this skill works on a free key. Read-only. No trading, no purchases, no write operations, no wallet access.

**中文介绍**: Company knowledge graph for AI agents: resolve the people and products behind a ticker, read the typed relationship behind each link (who leads the company, which variants belong to a product family, which companies are tracked as peers), find any tracked executive, product, organization or topic by name, and read each one's SentiSense Score over the same window. Use for who moves this stock, entity relationships API, company knowledge graph, product families, peer companies, CEO sentiment, executive sentiment, product sentiment versus the parent company, related entities API, entity resolution, stock ontology. Every call in this skill works on a free key. Read-only. No trading, no purchases, no write operations, no wallet access.

Latest changelog:
Entity lists no longer point at the internal id; urlSlug is the stable handle for metric calls.

**关键词**: Agent, stock-ontology, Company, knowledge, graph, resolve, people, products

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stock-ontology)

---

## [11. Theta EdgeCloud](https://clawhub.ai/zeuslabsllc/theta-edgecloud-skill)

**Slug**: `theta-edgecloud-skill`  
**Version**: 0.1.28  
**Stats**: ⭐ 1 | ⬇️ 1911 | 🧩 30

**原始简介**: Theta EdgeCloud AI, GPU, video and game-character workflows: discover live services, run inference, manage approved resources, and verify costs.

**中文介绍**: Theta EdgeCloud AI, GPU, video and game-character workflows: discover live services, run inference, manage approved resources, and verify costs.

Latest changelog:
Security release: strict Theta HTTPS origins, redirect refusal, single-attempt billable/mutating requests, full secret redaction, encoded resource IDs, incomplete-stream rejection and fail-closed deployment cleanup. Removes legacy wallet/RPC/setup/smoke helpers. GLM-5.3/Flash structured tools and current GPU/Video/Characters adapters. 93 tests; explicit coverage and security limits.

**关键词**: Theta, EdgeCloud, GPU, video, game-character, workflows, discover, live

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/theta-edgecloud-skill)

---

## [12. Plant Growth Stage Recognition Skill | 植物生长阶段识别技能](https://clawhub.ai/smyx-sunjinhui/smyx-plant-growth-stage-recognition-analysis)

**Slug**: `smyx-plant-growth-stage-recognition-analysis`  
**Version**: 1.0.15  
**Stats**: ⭐ 4 | ⬇️ 2301 | 🧩 16

**原始简介**: Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support. | 植物生长阶段识别技能，基于计算机视觉与深度学习算法，精准识别植物从发芽到结果的全生命周期关键生长阶段，为精准农业提供科学决策支持

**中文介绍**: Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support. | 植物生长阶段识别技能，基于计算机视觉与深度学习算法，精准识别植物从发芽到结果的全生命周期关键生长阶段，为精准农业提供科学决策支持

Latest changelog:
- Updated version number to 1.0.17.
- Removed the file: skill-card.md.
- SKILL.md file revised for version and documentation consistency.
- No functional or API changes to behaviors or instructions.

**关键词**: 植物生长阶段识别技能, Plant, Growth, Stage, Recognition, Skill, Accurately, identifies

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-plant-growth-stage-recognition-analysis)

---

## [13. Fuxux Social Manager](https://clawhub.ai/abogitoff/fuxux-openclaw-skill)

**Slug**: `fuxux-openclaw-skill`  
**Version**: 1.1.5  
**Stats**: ⭐ 0 | ⬇️ 1717 | 🧩 9

**原始简介**: Turn OpenClaw into an autonomous social media manager for Fuxux. Schedule and publish to 12 platforms via REST API and MCP: media, drafts, queue, editing, publishing analytics and AI captions.

**中文介绍**: Turn OpenClaw into an autonomous social media manager for Fuxux. Schedule and publish to 12 platforms via REST API and MCP: media, drafts, queue, editing, publishing analytics and AI captions.

Latest changelog:
fuxux-openclaw-skill v1.1.5

- Updated platform support to 12 platforms (dropped Google Business Profile).
- Documentation refreshed in README.md and SKILL.md.
- Removed obsolete skill-card.md documentation file.

**关键词**: an, Fuxux, Social, Manager, Turn, OpenClaw, autonomous, media

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/fuxux-openclaw-skill)

---

## [14. insurance-advisor-china](https://clawhub.ai/mnetfairy/insurance-advisor-china)

**Slug**: `insurance-advisor-china`  
**Version**: 2.0.149  
**Stats**: ⭐ 1 | ⬇️ 7890 | 🧩 233

**原始简介**: 中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

**中文介绍**: 中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

Latest changelog:
auto publish v2.0.149

**关键词**: 中国大陆AI保险顾问, 当用户询问保险配置、保险方案、产品对比、重疾险, 医疗险, 寿险, 意外险, insurance-advisor-china, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/insurance-advisor-china)

---

## [15. ai-insurance-advisor](https://clawhub.ai/mnetfairy/ai-insurance-advisor)

**Slug**: `ai-insurance-advisor`  
**Version**: 2.0.127  
**Stats**: ⭐ 1 | ⬇️ 8036 | 🧩 245

**原始简介**: 中国大陆保险顾问。本 skill 仅覆盖 6 项实际实现的能力：保险需求分析（needs_analyzer.py）、产品对比（premium_calculator.py + 本地 products.json）、保费计算（premium_calculator.py）、方案设计（plan_designer.py）、保险知识问答（insurance-knowledge.md）、合规要点提示（compliance.md）。不提供核保预审、理赔代办、朋友圈/营销文案生成、培训话术、代理人展业工具等能力——这些场景请转人工或调用专业服务。

**中文介绍**: 中国大陆保险顾问。本 skill 仅覆盖 6 项实际实现的能力：保险需求分析（needs_analyzer.py）、产品对比（premium_calculator.py + 本地 products.json）、保费计算（premium_calculator.py）、方案设计（plan_designer.py）、保险知识问答（insurance-knowledge.md）、合规要点提示（compliance.md）。不提供核保预审、理赔代办、朋友圈/营销文案生成、培训话术、代理人展业工具等能力——这些场景请转人工或调用专业服务。

Latest changelog:
auto publish v2.0.127

**关键词**: 中国大陆保险顾问, 仅覆盖, 项实际实现的能力, 保险需求分析（needs, 本地, ai-insurance-advisor, skill, calculator.py

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-insurance-advisor)

---

## [16. career-planner-china](https://clawhub.ai/mnetfairy/career-planner-china)

**Slug**: `career-planner-china`  
**Version**: 2.99.99  
**Stats**: ⭐ 0 | ⬇️ 7533 | 🧩 248

**原始简介**: AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

**中文介绍**: AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

Latest changelog:
test failure query

**关键词**: AI时代职业规划师技能, 专为AI时代职场变化而设计, 帮助用户应对AI带来的职业冲击与机遇, 功能包括, 中危, 低危分级）, 并输出完整的个性化职业规划报告, career-planner-china

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/career-planner-china)

---

## [17. ai-era-career-planner](https://clawhub.ai/mnetfairy/ai-era-career-planner)

**Slug**: `ai-era-career-planner`  
**Version**: 2.2.464  
**Stats**: ⭐ 0 | ⬇️ 7029 | 🧩 253

**原始简介**: AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

**中文介绍**: AI时代职业规划师技能。专为AI时代职场变化而设计，帮助用户应对AI带来的职业冲击与机遇。当用户询问职业规划、职业建议、选专业、职场转型、未来就业方向时触发。功能包括：收集用户基本信息、霍兰德职业兴趣测评、职业价值观分析、AI时代职业影响评估（高危/中危/低危分级），并输出完整的个性化职业规划报告。关键词：职业规划、选专业、工作建议、做什么工作好、职业转型、AI时代职业、AI替代、哪些工作会被AI取代。

Latest changelog:
auto publish v2.2.464

**关键词**: AI时代职业规划师技能, 专为AI时代职场变化而设计, 帮助用户应对AI带来的职业冲击与机遇, 功能包括, 中危, 低危分级）, 并输出完整的个性化职业规划报告, ai-era-career-planner

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-era-career-planner)

---

## [18. GitLab Agent](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-agent)

**Slug**: `xrowgmbh-gitlab-agent`  
**Version**: 1.97.0  
**Stats**: ⭐ 1 | ⬇️ 5765 | 🧩 130

**原始简介**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

**中文介绍**: Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

Latest changelog:
- Removed the obsolete file: skill-card.md.
- No changes were made to the functional skill logic or documentation in SKILL.md.

**关键词**: Agent, GitLab, Operate, assigned, work, owner-verified, project, access

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-agent)

---

## [19. GoLive](https://clawhub.ai/mikehasa/golive)

**Slug**: `golive`  
**Version**: 0.1.0-alpha.8  
**Stats**: ⭐ 0 | ⬇️ 143 | 🧩 4

**原始简介**: Take an agent-written app from repo to live production on the user's OWN accounts, with providers they choose (hosting, database, auth, payments, email, domain/DNS). The human connects accounts and approves changes; supported wiring operations run through a local CLI and produce verification evidence with explicit limits. Use when the user wants to ship, deploy, go live, launch, publish, or put their app online, or asks to wire up env vars, webhooks, auth settings (signup, email confirmation, password policy), a real signup → confirmation email → login journey, password recovery, account isolation between two users, auth redirects, email DNS or a custom domain.

**中文介绍**: Take an agent-written app from repo to live production on the user's OWN accounts, with providers they choose (hosting, database, auth, payments, email, domain/DNS). The human connects accounts and approves changes; supported wiring operations run through a local CLI and produce verification evidence with explicit limits. Use when the user wants to ship, deploy, go live, launch, publish, or put their app online, or asks to wire up env vars, webhooks, auth settings (signup, email confirmation, password policy), a real signup → confirmation email → login journey, password recovery, account isolation between two users, auth redirects, email DNS or a custom domain.

Latest changelog:
Adds the read-only site-metadata and stripe-live-payment checks; Sentry becomes an automated monitoring provider with the sentry-ingest check.

**关键词**: an, GoLive, Take, agent-written, app, live, production, user's

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/golive)

---

## [20. Ornamental Fish Color Brightness Assessment | 观赏鱼体色鲜艳度评估](https://clawhub.ai/smyx-sunjinhui/smyx-fish-color-brightness-assessment-analysis)

**Slug**: `smyx-fish-color-brightness-assessment-analysis`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 1547 | 🧩 13

**原始简介**: Through fixed aquarium cameras, the system periodically captures high-definition side images of ornamental fish (such as koi, goldfish, tropical fish), and uses AI vision analysis to extract color saturation (HSV-S channel) and brightness (HSV-V channel) of specific body regions (e.g. mid-trunk), compares them with healthy standard color ranges of the same species (built-in database or user-defined), and outputs a vibrancy. | 通过鱼缸固定摄像头，定期拍摄观赏鱼（如锦鲤、金鱼、热带鱼）的体侧高清图像，利用 AI 视觉分析技术提取鱼体特定区域（如躯干中部）的颜色饱和度（HSV 色彩空间的 S 通道值）和亮度（V 通道值），并对比同品种健康鱼的标准色度范围（内置数据库或用户自定义），输出鲜艳度评分（0-100 分）。当评分低于阈值（如 < 50）时，提示'体色暗淡'，可能为疾病、营养不良或水质不良的信号。

**中文介绍**: Through fixed aquarium cameras, the system periodically captures high-definition side images of ornamental fish (such as koi, goldfish, tropical fish), and uses AI vision analysis to extract color saturation (HSV-S channel) and brightness (HSV-V channel) of specific body regions (e.g. mid-trunk), compares them with healthy standard color ranges of the same species (built-in database or user-defined), and outputs a vibrancy. | 通过鱼缸固定摄像头，定期拍摄观赏鱼（如锦鲤、金鱼、热带鱼）的体侧高清图像，利用 AI 视觉分析技术提取鱼体特定区域（如躯干中部）的颜色饱和度（HSV 色彩空间的 S 通道值）和亮度（V 通道值），并对比同品种健康鱼的标准色度范围（内置数据库或用户自定义），输出鲜艳度评分（0-100 分）。当评分低于阈值（如 < 50）时，提示'体色暗淡'，可能为疾病、营养不良或水质不良的信号。

Latest changelog:
v1.0.12 Changelog

- Documentation updated: SKILL.md revised for accuracy, structure, and clarity.
- Redundant file removed: skill-card.md deleted.
- No functional or code changes; update is documentation-only.

**关键词**: 观赏鱼体色鲜艳度评估, Ornamental, Fish, Color, Brightness, Assessment, Through, fixed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-fish-color-brightness-assessment-analysis)

---

## [21. Danube](https://clawhub.ai/skills?q=tools-marketplace)

**Slug**: `tools-marketplace`  
**Version**: 8.1.23  
**Stats**: ⭐ 0 | ⬇️ 2577 | 🧩 27

**原始简介**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

**中文介绍**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

Latest changelog:
Three things an agent runs into while wiring the connection up by hand, none of them written down
before: which verb the MCP endpoint answers, how to read its `401`s, and the key header that works
against the MCP server but not against the REST API.

- **Probing `https://mcp.danubeai.com/mcp` with `curl` has traps that read like a bad key.**
  `references/troubleshooting.md` gains a working probe and how to read what comes back, all
  verified live on 2026-10-03. POST is the only verb that does anything — a `GET` with a valid key
  answers `405 Method Not Allowed`, and the `Allow: DELETE, POST` beside it is not a second route
  (`DELETE` answers `405 Method Not Allowed: Session termination not supported`). A JSON-RPC
  `initialize` POST replies as `text/event-stream` (`event: message` then a `data:` line,
  `serverInfo` `Danube MCP Server` 4.0.5), so piping it to `jq` fails on a perfectly healthy
  server; send `Accept: application/json, text/event-stream` or no `Accept` at all, since
  `Accept: application/json` alone is a `406`. The two `401`s differ by message — `API key
  required. Provide 'danube-api-key' header or 'Authorization: Bearer <api_key>'.` for no key,
  `Invalid API

**关键词**: Agent, API, Danube, Governed, tool, access, one, key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tools-marketplace)

---

## [22. Danube](https://clawhub.ai/preston-thiele/danube)

**Slug**: `danube`  
**Version**: 8.1.23  
**Stats**: ⭐ 2 | ⬇️ 5150 | 🧩 42

**原始简介**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

**中文介绍**: Governed tool access for AI agents — one Danube API key unlocks your organization's own tools plus a large, growing catalog of services, over MCP or curl, with confirmation before anything that writes, sends, spends, or deletes.

Latest changelog:
Three things an agent runs into while wiring the connection up by hand, none of them written down
before: which verb the MCP endpoint answers, how to read its `401`s, and the key header that works
against the MCP server but not against the REST API.

- **Probing `https://mcp.danubeai.com/mcp` with `curl` has traps that read like a bad key.**
  `references/troubleshooting.md` gains a working probe and how to read what comes back, all
  verified live on 2026-10-03. POST is the only verb that does anything — a `GET` with a valid key
  answers `405 Method Not Allowed`, and the `Allow: DELETE, POST` beside it is not a second route
  (`DELETE` answers `405 Method Not Allowed: Session termination not supported`). A JSON-RPC
  `initialize` POST replies as `text/event-stream` (`event: message` then a `data:` line,
  `serverInfo` `Danube MCP Server` 4.0.5), so piping it to `jq` fails on a perfectly healthy
  server; send `Accept: application/json, text/event-stream` or no `Accept` at all, since
  `Accept: application/json` alone is a `406`. The two `401`s differ by message — `API key
  required. Provide 'danube-api-key' header or 'Authorization: Bearer <api_key>'.` for no key,
  `Invalid API

**关键词**: Agent, API, Danube, Governed, tool, access, one, key

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/danube)

---

## [23. Equalang Translation](https://clawhub.ai/equalang-ai/equalang)

**Slug**: `equalang`  
**Version**: 0.2.0  
**Stats**: ⭐ 0 | ⬇️ 27 | 🧩 1

**原始简介**: Translate PDF, Word/DOCX, Excel/XLSX, PowerPoint and e-books with layout preservation where supported. Translate images and subtitles; turn audio/video into transcripts or translated subtitles. Requires an Equalang API key and credits; files are processed in the cloud.

**中文介绍**: Translate PDF, Word/DOCX, Excel/XLSX, PowerPoint and e-books with layout preservation where supported. Translate images and subtitles; turn audio/video into transcripts or translated subtitles. Requires an Equalang API key and credits; files are processed in the cloud.

Latest changelog:
equalang 0.2.0

- Adds detailed SKILL.md documentation covering usage, setup, commands, and file handling for Equalang translation and transcription.
- Explains how to estimate costs, handle API keys, and interpret results before running paid operations.
- Clearly lists supported file formats and API endpoints.
- Expands on language detection, output file handling, and privacy notes for users.
- Introduces best practices for batch processing and cost estimation.

**关键词**: Equalang, Translation, Translate, PDF, Word, DOCX, Excel, XLSX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/equalang)

---

## [24. Openclaw Memory Toolkit](https://clawhub.ai/mistermijarvis/memory-toolkit)

**Slug**: `memory-toolkit`  
**Version**: 3.0.2  
**Stats**: ⭐ 2 | ⬇️ 712 | 🧩 17

**原始简介**: Hybrid memory pipeline for OpenClaw agents — extraction, archiving, temporal decay scoring, consolidation, and hybrid search (FTS5 + sqlite-vec + RRF). Six standalone Python scripts, local-first, zero external API dependencies. The only memory skill on ClawHub with RRF.

**中文介绍**: Hybrid memory pipeline for OpenClaw agents — extraction, archiving, temporal decay scoring, consolidation, and hybrid search (FTS5 + sqlite-vec + RRF). Six standalone Python scripts, local-first, zero external API dependencies. The only memory skill on ClawHub with RRF.

Latest changelog:
v3.0.2 — Security: OLLAMA_GEN_URL bypassed the loopback guard
Round 8 security scan of the published v3.0.0 returned 51 findings. One was real and is fixed here; the rest are the known false-positive families, re-triaged in docs/SECURITY-AUDIT-NOTES.md §3 so they do not have to be re-litigated.

Fixed (real finding — Data Flow Critical 97%, Intent-Code Divergence 98%)
hybrid-search/conflict_resolver.py read OLLAMA_GEN_URL straight from os.environ, bypassing get_safe_ollama_url():

# before — no guard
OLLAMA_GEN_URL = os.environ.get("OLLAMA_GEN_URL", OLLAMA_URL + "/api/generate")
classify_relation() POSTs the content of two memory facts to that URL on every arbitration. Any process able to set the environment variable could redirect memory content to a remote host — while the docstring directly above still claimed "the destination is fixed to localhost at import time, so a remote endpoint cannot receive memory content."

# after — same loopback allowlist as OLLAMA_URL
OLLAMA_GEN_URL = get_safe_ollama_url("OLLAMA_GEN_URL", OLLAMA_URL.rstrip("/") + "/api/generate")
Verified:

OLLAMA_GEN_URL="http://evil.example.com/api/generate" → ValueError: Host 'evil.example.com' not allowed for OL

**关键词**: Agent, Openclaw, Memory, Toolkit, Hybrid, pipeline, extraction, archiving

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memory-toolkit)

---

## [25. rail-live-boards](https://clawhub.ai/simonjohnedwards-hub/rail-live-boards)

**Slug**: `rail-live-boards`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 33 | 🧩 1

**原始简介**: Query UK National Rail live boards, delays, cancellations, platforms, and service details.

**中文介绍**: Query UK National Rail live boards, delays, cancellations, platforms, and service details.

Latest changelog:
Initial public release. Query UK National Rail live departure and arrival boards, delays, cancellations, platforms, disruption notices, and service details.

**关键词**: UK, rail-live-boards, Query, National, Rail, live, boards, delays

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rail-live-boards)

---

