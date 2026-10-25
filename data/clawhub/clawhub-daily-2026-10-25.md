# ClawHub Skills Daily | 2026-10-25

> 共 25 个 skills

## [1. Excalidraw Diagrams for Obsidian](https://clawhub.ai/ricardodpalmeida/excalidraw-diagrams)

**Slug**: `excalidraw-diagrams`  
**Version**: 1.1.0  
**Stats**: ⭐ 3 | ⬇️ 1511 | 🧩 4

**原始简介**: Create Excalidraw drawing files from a list of boxes and connections: an Obsidian Excalidraw note (.excalidraw.md) or a .excalidraw file for excalidraw.com. A bundled script does the layout, labels and arrow bindings. Use only when the user explicitly asks for an Excalidraw drawing or an Excalidraw file in Obsidian.

**中文介绍**: Create Excalidraw drawing files from a list of boxes and connections: an Obsidian Excalidraw note (.excalidraw.md) or a .excalidraw file for excalidraw.com. A bundled script does the layout, labels and arrow bindings. Use only when the user explicitly asks for an Excalidraw drawing or an Excalidraw file in Obsidian.

Latest changelog:
- New `scripts/build_diagram.py`. It builds a drawing from a JSON spec of nodes, edges and groups. It does the layered layout (with cycle support and detours around nodes), label sizing, two-way text and arrow bindings and deterministic IDs, and writes either the Obsidian or the standard format. It refuses to overwrite without `--force`.
- New `scripts/validate.py`, which checks structure, bindings, fonts, font sizes and overlapping shapes.
- `SKILL.md` and `references/excalidraw-format.md` now agree with each other. Fixed the "Default" mode contradiction and the `frameId`/`versionNonce`/`updated` rules, documented `fontFamily` 5 (Excalifont) and the other current fonts, and populated `## Text Elements` in Obsidian files. The 1200x800 canvas limit is gone.
- Narrowed the description to explicit Excalidraw requests, per the ClawHub security audit (Vague Triggers).
- Examples, unit tests and GitHub Actions CI.

**关键词**: of, Excalidraw, Diagrams, Obsidian, drawing, files, list, boxes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/excalidraw-diagrams)

---

## [2. book-capture-obsidian](https://clawhub.ai/ricardodpalmeida/book-capture-obsidian)

**Slug**: `book-capture-obsidian`  
**Version**: 1.3.0  
**Stats**: ⭐ 1 | ⬇️ 1085 | 🧩 12

**原始简介**: Add books to an Obsidian vault as notes: from a photo of the cover or barcode, from an ISBN or title, or in bulk from a Goodreads CSV export, then refresh a library dashboard. Use when the user wants to catalogue, log or import books into Obsidian.

**中文介绍**: Add books to an Obsidian vault as notes: from a photo of the cover or barcode, from an ISBN or title, or in bulk from a Goodreads CSV export, then refresh a library dashboard. Use when the user wants to catalogue, log or import books into Obsidian.

Latest changelog:
- Quota-aware metadata: Open Library first, Google Books only for missing fields, SQLite cache, per-run Google budget and a persisted cooldown after HTTP 429. Goodreads dry runs make no network calls; `--limit` for small batches.
- Open Library ISBN lookups now return a description: the `jscmd=data` response has no work link, so the resolver follows the edition record to the work. Before this, almost every ISBN fell through to Google Books for the description, which is what exhausted the free quota.
- Title searches (Open Library and Google Books) only accept a result whose title and author match the query, and never adopt an edition ISBN. Checked against live Open Library data, where "The Three-Body Problem" by Liu Cixin otherwise resolves to its sequel or to an unrelated physics book.
- When an ISBN has no Open Library record (common for Portuguese and other non-English editions), the resolver tries the Open Library title and author search before Google. Work-level search results no longer set a publisher, because the list belongs to other editions.
- Descriptions with Windows line endings no longer make every re-run rewrite the note.
- Goodreads rows without an ISBN are imported

**关键词**: an, as, book-capture-obsidian, Add, books, Obsidian, vault, notes

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/book-capture-obsidian)

---

## [3. Microsoft Learn MCP](https://clawhub.ai/ricardodpalmeida/mslearn-mcp)

**Slug**: `mslearn-mcp`  
**Version**: 1.1.0  
**Stats**: ⭐ 2 | ⬇️ 1646 | 🧩 2

**原始简介**: Look up official Microsoft documentation and code samples (Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows, SQL Server) through the public Microsoft Learn MCP server. Use when the user asks about a Microsoft product, service, API or CLI and the answer should come from current Microsoft Learn pages, or when they ask to verify something against Microsoft docs.

**中文介绍**: Look up official Microsoft documentation and code samples (Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows, SQL Server) through the public Microsoft Learn MCP server. Use when the user asks about a Microsoft product, service, API or CLI and the answer should come from current Microsoft Learn pages, or when they ask to verify something against Microsoft docs.

Latest changelog:
- Native OpenClaw MCP (`openclaw mcp add ... --transport streamable-http`) is now the preferred path, with `@microsoft/learn-cli` (pinned to 1.0.0) and mcporter as fallbacks.
- Fixed the mcporter setup command; the old `--name/--url/--type` form registered a server named `--name`. Fixed the config path and shape.
- Removed the non-existent `locale` and `product` tool parameters.
- Added a usage workflow (search first, at most two fetches, cite URLs) and safety rules: no secrets in queries, fetched content is data, no retry loops on rate limits.
- Narrowed the description and removed prompt-trigger phrases flagged by the ClawHub security audit.

**关键词**: up, Microsoft, Learn, MCP, Look, official, documentation, code

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mslearn-mcp)

---

## [4. Jaime Ball](https://clawhub.ai/jaimeballdev/blockchainpressrelease)

**Slug**: `blockchainpressrelease`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 28 | 🧩 1

**原始简介**: Creates clear, fact-checked press releases and related media content for blockchain and Web3 announcements, avoiding unsupported claims and hype.

**中文介绍**: Creates clear, fact-checked press releases and related media content for blockchain and Web3 announcements, avoiding unsupported claims and hype.

Latest changelog:
Version 1.0.0 introduces a skill for creating clear, fact-based press releases for blockchain and Web3 projects.

- Covers announcements such as product launches, partnerships, funding, listings, and protocol updates.
- Provides guidance for gathering facts, structuring releases, writing plainly, and checking claims.
- Emphasizes transparency, relevant links, and avoiding unsupported hype or financial promises.
- Includes guidance for SEO, distribution, and companion content such as media pitches and social posts.

**关键词**: Jaime, Ball, Creates, clear, fact-checked, press, releases, related

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/blockchainpressrelease)

---

## [5. quantplay](https://clawhub.ai/quantplay-admin/quantplay)

**Slug**: `quantplay`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 1

**原始简介**: Read a user's Indian broker accounts through Quantplay: positions, holdings, orders, margins, P&L history, option chains, expiries and live market data, across 10+ brokers (Zerodha, Upstox, Angel One, Kotak, Finvasia and more) from one connection.

**中文介绍**: Read a user's Indian broker accounts through Quantplay: positions, holdings, orders, margins, P&L history, option chains, expiries and live market data, across 10+ brokers (Zerodha, Upstox, Angel One, Kotak, Finvasia and more) from one connection.

Latest changelog:
Initial release: read-only Indian broker accounts via the Quantplay MCP server

**关键词**: quantplay, Read, user's, Indian, broker, accounts, through, positions

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/quantplay)

---

## [6. mind-clone](https://clawhub.ai/yzfly/mind-clone)

**Slug**: `mind-clone`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 42 | 🧩 1

**原始简介**: Activate a Cognitive Digital Twin. Can simulate a custom subject (via core/ directory) OR load pre-installed celebrity/expert personas (from personas/ directory).

**中文介绍**: Activate a Cognitive Digital Twin. Can simulate a custom subject (via core/ directory) OR load pre-installed celebrity/expert personas (from personas/ directory).

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: mind-clone, Activate, Cognitive, Digital, Twin, Can, simulate, custom

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mind-clone)

---

## [7. ui-engineering](https://clawhub.ai/yzfly/ui-engineering)

**Slug**: `ui-engineering`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 44 | 🧩 1

**原始简介**: Expert system for creating high-quality, brand-aligned user interfaces. Use this skill when asked to design websites, create components, or implement specific visual styles. It contains specifications for major tech companies, design trends, and specific site types like blogs or presentations.

**中文介绍**: Expert system for creating high-quality, brand-aligned user interfaces. Use this skill when asked to design websites, create components, or implement specific visual styles. It contains specifications for major tech companies, design trends, and specific site types like blogs or presentations.

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: ui-engineering, Expert, system, creating, high-quality, brand-aligned, user, interfaces

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ui-engineering)

---

## [8. taste-pm](https://clawhub.ai/yzfly/taste-pm)

**Slug**: `taste-pm`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 43 | 🧩 1

**原始简介**: Use when designing a product's structure, information architecture, page layout, entry points, or user-experience flow — turning a business or feature need into a product design for web or app. Triggers include 'design a product', 'how should this feature be laid out', 'where does the entry point go', 'product structure', 'information architecture', 'how to design the pages', 'what's the user flow', or doing product-manager work for a web product. Not for visual styling (use a UI skill) or backend implementation.

**中文介绍**: Use when designing a product's structure, information architecture, page layout, entry points, or user-experience flow — turning a business or feature need into a product design for web or app. Triggers include 'design a product', 'how should this feature be laid out', 'where does the entry point go', 'product structure', 'information architecture', 'how to design the pages', 'what's the user flow', or doing product-manager work for a web product. Not for visual styling (use a UI skill) or backend implementation.

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: taste-pm, Use, when, designing, product's, structure, information, architecture

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/taste-pm)

---

## [9. ai-first-cli](https://clawhub.ai/yzfly/ai-first-cli)

**Slug**: `ai-first-cli`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 43 | 🧩 1

**原始简介**: This skill should be used when designing, building, or reviewing a command-line tool that AI agents will call, not just humans. Use it when deciding output format (JSON vs text), error handling, exit codes, flags, discoverability, dependencies and packaging, or autonomous-operation safety for a CLI. Also use it when asked how to make an existing CLI agent-friendly, or to evaluate a tool against the agent-first design philosophy. Grounded in Vercel's cloud-for-agents methodology.

**中文介绍**: This skill should be used when designing, building, or reviewing a command-line tool that AI agents will call, not just humans. Use it when deciding output format (JSON vs text), error handling, exit codes, flags, discoverability, dependencies and packaging, or autonomous-operation safety for a CLI. Also use it when asked how to make an existing CLI agent-friendly, or to evaluate a tool against the agent-first design philosophy. Grounded in Vercel's cloud-for-agents methodology.

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: be, ai-first-cli, skill, should, used, when, designing, building

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-first-cli)

---

## [10. GitLab Agent Self Improvement](https://clawhub.ai/xrowgmbh/xrowgmbh-self-improvement)

**Slug**: `xrowgmbh-self-improvement`  
**Version**: 1.121.0  
**Stats**: ⭐ 0 | ⬇️ 7366 | 🧩 168

**原始简介**: A skill for personal growth and self-improvement.

**中文介绍**: A skill for personal growth and self-improvement.

Latest changelog:
- Removed `skill-card.md`.

**关键词**: Agent, GitLab, Self, Improvement, skill, personal, growth, self-improvement

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-self-improvement)

---

## [11. GitLab Hackathon](https://clawhub.ai/xrowgmbh/xrowgmbh-gitlab-hackathon)

**Slug**: `xrowgmbh-gitlab-hackathon`  
**Version**: 1.121.0  
**Stats**: ⭐ 0 | ⬇️ 6744 | 🧩 162

**原始简介**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

**中文介绍**: Plan and execute fair GitLab hackathon participation, including Quarterly and Transcend Hackathons, by analyzing rules, selecting qualifying issues/MRs, tracking scoring levers, and keeping an exploit watchlist.

Latest changelog:
- Removed `skill-card.md`. No changes to `SKILL.md`.

**关键词**: GitLab, Hackathon, Plan, execute, fair, participation, including, Quarterly

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xrowgmbh-gitlab-hackathon)

---

## [12. 去 AI 味界面文案](https://clawhub.ai/yzfly/anti-ai-copy)

**Slug**: `anti-ai-copy`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 39 | 🧩 1

**原始简介**: 软件界面文案（UI copy / microcopy / UX writing）写作与去 AI 味。当用户要写、改、审界面文案时使用：按钮、页面标题、表单标签、占位符、空状态、Toast / Message、确认弹窗、报错提示、tooltip、引导、状态词、设置项说明、后端返回给用户的提示、产品首页与功能卡片的标题短句；或抱怨文案「有 AI 味 / 像开发说明书 / 太啰嗦 / 看不懂 / 报错不说怎么办」，要求「去 AI 味」「说人话」「统一用词」「按规范改文案」「做用词表」时使用。中文为主，兼顾英文。不写营销长文、公众号文章和广告创意（文章去 AI 味请用通用 humanizer 类 skill）。

**中文介绍**: 软件界面文案（UI copy / microcopy / UX writing）写作与去 AI 味。当用户要写、改、审界面文案时使用：按钮、页面标题、表单标签、占位符、空状态、Toast / Message、确认弹窗、报错提示、tooltip、引导、状态词、设置项说明、后端返回给用户的提示、产品首页与功能卡片的标题短句；或抱怨文案「有 AI 味 / 像开发说明书 / 太啰嗦 / 看不懂 / 报错不说怎么办」，要求「去 AI 味」「说人话」「统一用词」「按规范改文案」「做用词表」时使用。中文为主，兼顾英文。不写营销长文、公众号文章和广告创意（文章去 AI 味请用通用 humanizer 类 skill）。

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: 味界面文案, 软件界面文案（UI, UX, 当用户要写、改、审界面文案时使用, 或抱怨文案「有, copy, microcopy, writing）写作与去

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/anti-ai-copy)

---

## [13. 像素精灵](https://clawhub.ai/yzfly/pixel-sprite)

**Slug**: `pixel-sprite`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 41 | 🧩 1

**原始简介**: 将参考图或文字描述的主体转换为低分辨率像素插画 / 像素图标（Low Resolution Pixel Sprite）。当用户上传一张图并说「做成像素风 / 像素画 / pixel art / 8-bit / 16-bit / sprite / 游戏图标 / 像素头像」，或想把 logo、吉祥物、产品、宠物、人物变成复古游戏像素素材时使用。严格保留原主体设计，只转换表现形式；输出 32×32 规格、硬边像素、有限色板、纯白背景的单主体居中图。不适用于像素风海报排版、点阵印刷海报或需要文字 / 场景的整图设计。

**中文介绍**: 将参考图或文字描述的主体转换为低分辨率像素插画 / 像素图标（Low Resolution Pixel Sprite）。当用户上传一张图并说「做成像素风 / 像素画 / pixel art / 8-bit / 16-bit / sprite / 游戏图标 / 像素头像」，或想把 logo、吉祥物、产品、宠物、人物变成复古游戏像素素材时使用。严格保留原主体设计，只转换表现形式；输出 32×32 规格、硬边像素、有限色板、纯白背景的单主体居中图。不适用于像素风海报排版、点阵印刷海报或需要文字 / 场景的整图设计。

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: 像素精灵, 将参考图或文字描述的主体转换为低分辨率像素插画, 像素图标（Low, 当用户上传一张图并说「做成像素风, 像素画, Resolution, Pixel, Sprite）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pixel-sprite)

---

## [14. 几何情绪窗口海报](https://clawhub.ai/yzfly/photo-window-poster)

**Slug**: `photo-window-poster`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 41 | 🧩 1

**原始简介**: 把照片做成上下 1:1 的 3:4 高级设计海报：上半原图轻调色，下半「真实物象穿越几何情绪窗口」的极简几何色块海报，自动从画面提炼标题与文案排版。当用户上传照片想要「高级感海报」「几何色块 + 留白」「像高端地产 / 奢侈品 / 美学杂志 / 节气视觉」的编辑设计，或提到「几何情绪窗口」「主体越界破框」时使用。每张照片单独输出，不拼图。不适用于手绘重绘、像素风或纯抽象色块（分别见 xxd-panel-070、pixel-sprite、photo-abstract-editorial）。

**中文介绍**: 把照片做成上下 1:1 的 3:4 高级设计海报：上半原图轻调色，下半「真实物象穿越几何情绪窗口」的极简几何色块海报，自动从画面提炼标题与文案排版。当用户上传照片想要「高级感海报」「几何色块 + 留白」「像高端地产 / 奢侈品 / 美学杂志 / 节气视觉」的编辑设计，或提到「几何情绪窗口」「主体越界破框」时使用。每张照片单独输出，不拼图。不适用于手绘重绘、像素风或纯抽象色块（分别见 xxd-panel-070、pixel-sprite、photo-abstract-editorial）。

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: 几何情绪窗口海报, 把照片做成上下, 高级设计海报, 上半原图轻调色, 自动从画面提炼标题与文案排版, 当用户上传照片想要「高级感海报」「几何色块, 留白」「像高端地产, 奢侈品

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/photo-window-poster)

---

## [15. 品牌叙事](https://clawhub.ai/skills?q=brand-narrative)

**Slug**: `brand-narrative`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 11 | 🧩 1

**原始简介**: 品牌叙事策略。当用户要做品牌叙事 / 品牌故事 / 品牌定位 / 品牌策略、问「我们的品牌到底围绕什么」「该讲产品还是讲文化」、想判断某个新品 / 联名 / 内容「符不符合品牌」、或为 0–1 与规模化阶段的品牌选择叙事重点时使用。基于六种叙事类型（产品、能力、身份、生活方式、社群、文化）与三个构件（叙事中心、叙事命题、叙事逻辑）产出品牌叙事文档与判断准则。不做视觉设计（见 breathing-brand）与文案排版（见 mp-layout）。

**中文介绍**: 品牌叙事策略。当用户要做品牌叙事 / 品牌故事 / 品牌定位 / 品牌策略、问「我们的品牌到底围绕什么」「该讲产品还是讲文化」、想判断某个新品 / 联名 / 内容「符不符合品牌」、或为 0–1 与规模化阶段的品牌选择叙事重点时使用。基于六种叙事类型（产品、能力、身份、生活方式、社群、文化）与三个构件（叙事中心、叙事命题、叙事逻辑）产出品牌叙事文档与判断准则。不做视觉设计（见 breathing-brand）与文案排版（见 mp-layout）。

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: 品牌叙事, 品牌叙事策略, 当用户要做品牌叙事, 品牌故事, 品牌定位, 联名, 内容「符不符合品牌」、或为, 0–1

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/brand-narrative)

---

## [16. 呼吸感品牌全案](https://clawhub.ai/yzfly/breathing-brand)

**Slug**: `breathing-brand`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 40 | 🧩 1

**原始简介**: 出海 / 国际化品牌的极简呼吸感视觉全案。当用户说要做品牌 VI、品牌视觉、logo 与周边、独立站视觉、社区 / 组织 / 产品的品牌形象，或抱怨自己的品牌「看起来廉价」「太满太乱」「不够国际化 / 高级」，或想要「留白」「呼吸感」「高级感」的品牌设计时使用。产出定位洞察、色彩 + 留白系统、线条链接母题、线条 Emoji 表情集、应用物料（独立站 UI、名片、帆布袋、PIN、社媒封面）的生图提示词与全案展示文案。不适用于单张海报、照片风格化或纯 UI 页面编码（后者用 hallmark 等）。

**中文介绍**: 出海 / 国际化品牌的极简呼吸感视觉全案。当用户说要做品牌 VI、品牌视觉、logo 与周边、独立站视觉、社区 / 组织 / 产品的品牌形象，或抱怨自己的品牌「看起来廉价」「太满太乱」「不够国际化 / 高级」，或想要「留白」「呼吸感」「高级感」的品牌设计时使用。产出定位洞察、色彩 + 留白系统、线条链接母题、线条 Emoji 表情集、应用物料（独立站 UI、名片、帆布袋、PIN、社媒封面）的生图提示词与全案展示文案。不适用于单张海报、照片风格化或纯 UI 页面编码（后者用 hallmark 等）。

Latest changelog:
Sync from yzfly GitHub source.

**关键词**: 呼吸感品牌全案, 出海, 国际化品牌的极简呼吸感视觉全案, 当用户说要做品牌, VI、品牌视觉、logo, 与周边、独立站视觉、社区, 组织, 产品的品牌形象

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/breathing-brand)

---

## [17. claimcheck](https://clawhub.ai/normandmickey/claimcheck)

**Slug**: `claimcheck`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 145 | 🧩 3

**原始简介**: Sanitize PII/secrets (FEIN, SSN, names, credentials) from text or files with the local ClaimCheck CLI before anything leaves the machine; reversible via the local vault.

**中文介绍**: Sanitize PII/secrets (FEIN, SSN, names, credentials) from text or files with the local ClaimCheck CLI before anything leaves the machine; reversible via the local vault.

Latest changelog:
- Added the `ClaimCheck status` command to check proxy, NER, vault, and MCP wiring, with optional machine-readable JSON output.
- Updated the homepage link to claimcheck.saasclaw.ai.
- Removed the `skill-card.md` file.

**关键词**: claimcheck, Sanitize, PII, secrets, FEIN, SSN, names, credentials

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/claimcheck)

---

## [18. HeyReach Integration](https://clawhub.ai/superagnt/heyreach-outreach)

**Slug**: `heyreach-outreach`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 614 | 🧩 8

**原始简介**: Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

**中文介绍**: Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

Latest changelog:
- Updated the MCP setup instructions to use the shared install guide at https://www.superagnt.com/install.
- Removed the `skill-card.md` file.

**关键词**: HeyReach, Integration, Manage, LinkedIn, outreach, campaigns, leads, lists

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/heyreach-outreach)

---

## [19. Attio Integration](https://clawhub.ai/superagnt/attio-crm)

**Slug**: `attio-crm`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 657 | 🧩 8

**原始简介**: Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

**中文介绍**: Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

Latest changelog:
- Updated the MCP client setup link to https://www.superagnt.com/install.
- Removed the `skill-card.md` file.

**关键词**: Attio, Integration, Manage, CRM, records, lists, notes, tasks

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/attio-crm)

---

## [20. Exa Integration](https://clawhub.ai/skills?q=exa-search)

**Slug**: `exa-search`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 360 | 🧩 8

**原始简介**: Neural web search, parsed page contents, find-similar, and agentic Q&amp;A over the live web through the superagnt unified API.

**中文介绍**: Neural web search, parsed page contents, find-similar, and agentic Q&amp;A over the live web through the superagnt unified API.

Latest changelog:
- Expanded Exa integration documentation for neural and keyword search, page contents, similar-link discovery, and cited Q&A.
- Added MCP server connection instructions as an alternative to curl-based API calls.
- Documented setup, authentication, connection verification, endpoint schemas, and safety requirements.

**关键词**: Exa, Integration, Neural, web, search, parsed, page, contents

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/exa-search)

---

## [21. company-enrichment](https://clawhub.ai/superagnt/company-enrichment)

**Slug**: `company-enrichment`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 605 | 🧩 8

**原始简介**: Company firmographics, tech stack, headcount, and intelligence from a domain — agent-ready account research.

**中文介绍**: Company firmographics, tech stack, headcount, and intelligence from a domain — agent-ready account research.

Latest changelog:
- Updated the scoped MCP server setup link.
- Bumped the skill version to 2.0.8.
- Removed skill-card.md.

**关键词**: company-enrichment, Company, firmographics, tech, stack, headcount, intelligence, domain

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/company-enrichment)

---

## [22. email-finder](https://clawhub.ai/skills?q=email-finder)

**Slug**: `email-finder`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 367 | 🧩 8

**原始简介**: Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

**中文介绍**: Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

Latest changelog:
- Version 2.0.8 documents three endpoints: find a professional email, verify an address, and list emails on a domain.
- Includes API-key setup and install verification instructions.
- Documents an optional scoped MCP server alongside curl-based usage.

**关键词**: email-finder, Find, verify, work, emails, name, company, waterfall

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/email-finder)

---

## [23. lead-enrichment](https://clawhub.ai/skills?q=lead-enrichment)

**Slug**: `lead-enrichment`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 372 | 🧩 8

**原始简介**: Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

**中文介绍**: Enrich people and companies from a name, domain, or LinkedIn URL — emails, titles, firmographics, and mobile numbers for agents.

Latest changelog:
- Documents six lead-enrichment endpoints for people and companies, including bulk enrichment, search, mobile lookup, and email finding.
- Adds setup guidance for API-key authentication and an initial credits check.
- Describes an optional scoped MCP server alongside curl-based access.

**关键词**: or, lead-enrichment, Enrich, people, companies, name, domain, LinkedIn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lead-enrichment)

---

## [24. facebook-data](https://clawhub.ai/superagnt/facebook-data)

**Slug**: `facebook-data`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 674 | 🧩 8

**原始简介**: Facebook pages, posts, and group data for agents — brand and market research without scraping.

**中文介绍**: Facebook pages, posts, and group data for agents — brand and market research without scraping.

Latest changelog:
- Updated the MCP client setup link to https://www.superagnt.com/install?facet=facebook.
- Removed `skill-card.md`.

**关键词**: Agent, facebook-data, Facebook, pages, posts, group, data, brand

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/facebook-data)

---

## [25. YouTube Data](https://clawhub.ai/skills?q=youtube-data)

**Slug**: `youtube-data`  
**Version**: 2.0.8  
**Stats**: ⭐ 1 | ⬇️ 1201 | 🧩 11

**原始简介**: YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

**中文介绍**: YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

Latest changelog:
Expanded YouTube Data access and setup guidance in version 2.0.8.

- Added an alternative scoped MCP server connection, alongside curl-based API access.
- Documented setup, API key authentication, and an install verification request.
- Listed endpoints and tool schemas for video, channel, audio, search, trending, comments, subtitles, and recommendations.

**关键词**: Agent, YouTube, Data, channels, videos, transcripts, comments, content

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/youtube-data)

---

