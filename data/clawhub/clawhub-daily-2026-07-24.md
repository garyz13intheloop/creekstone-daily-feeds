# ClawHub Skills Daily | 2026-07-24

> 共 25 个 skills

## [1. Optim Agent](https://clawhub.ai/optim-agent/optim-agent)

**Slug**: `optim-agent`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when the user wants to optimize configurable system parameters against a measurable scalar objective, especially for model training, inference, quantitat...

**中文介绍**: Use when the user wants to optimize configurable system parameters against a measurable scalar objective, especially for model training, inference, quantitat...

Latest changelog:
- Initial release of optim-agent skill for optimizing configurable system parameters against a measurable scalar objective.
- Provides a detailed workflow for configuring, running, and recording optimization trials, including ask/tell API usage.
- Designed for coding agents with project and shell access; supports model training, scientific workflows, and black-box evaluations.
- Introduces best practices for baseline measurement, recovery, artifact storage, and reproducibility.
- Includes clear rules to ensure auditable, unbiased, and safe optimization.

**关键词**: Agent, Optim, Use, when, user, wants, optimize, configurable

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/optim-agent)

---

## [2. Unified Research Finder](https://clawhub.ai/georgechou17/unified-research-finder)

**Slug**: `unified-research-finder`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 142 | 🧩 2

**原始简介**: 统一的学术文献检索助手。覆盖两大体系：(1) PubMed 官方 E-utilities API（esearch+efetch，真实 PMID/摘要/DOI）与 PubMed 网页检索；(2) Google Scholar 及其镜像站——灯塔学术搜索、烂番薯学术搜索、Google Scholar 香港镜像、Google Scholar 官方站，按「灯塔 → 烂番薯 → 香港镜像 → 官方」优先级自动回退（灯塔走 JSON API 最省内存最快）。当用户要找文献、查论文、搜 PubMed、查 Google 学术/谷歌学术、用学术镜像站、要影响因子或引用数据时启用。找不到就是找不到，绝不编造。

**中文介绍**: 统一的学术文献检索助手。覆盖两大体系：(1) PubMed 官方 E-utilities API（esearch+efetch，真实 PMID/摘要/DOI）与 PubMed 网页检索；(2) Google Scholar 及其镜像站——灯塔学术搜索、烂番薯学术搜索、Google Scholar 香港镜像、Google Scholar 官方站，按「灯塔 → 烂番薯 → 香港镜像 → 官方」优先级自动回退（灯塔走 JSON API 最省内存最快）。当用户要找文献、查论文、搜 PubMed、查 Google 学术/谷歌学术、用学术镜像站、要影响因子或引用数据时启用。找不到就是找不到，绝不编造。

Latest changelog:
# 更新日志 / Changelog

## [v1.1] — 2026-07-24

### 🐛 Bug Fixes

**#1 沙箱环境下 `unified_search.py` 被 SIGKILL（无任何输出）**

- **现象**：在某些受约束的沙箱环境（如 operitAI、WorkBuddy sandbox）中运行 `unified_search.py` 时，进程直接被杀死，不产生 stdout/stderr 任何输出。
- **根因**：旧版使用 `subprocess.run()` 串行执行 PubMed → Scholar。Scholar 需依次尝试 4 个源，每个源 HTTP 超时 25s，全程 2-3 分钟无任何 I/O。沙箱检测到进程长时间零输出后发送 SIGKILL，`print()` 永远走不到。
- **修复**：
  - 两路子进程改用 `concurrent.futures.ThreadPoolExecutor` 并行启动。
  - Scholar 设独立 60s 超时上限（≈ 走完 2-3 个源），超时直接出部分结果，不阻塞输出。
  - 所有 `print()` 后追加 `sys.stdout.flush()`，确保管道/沙箱立刻看到 I/O。
  - 即使 Scholar 超时，PubMed 结果仍正常合并输出。

**#2 operitAI 加载 skill 时三条启动报错**

- **现象**：在 operitAI（Android）加载本 skill 时，控制台出现三条错误：
  1. `tool_name must use packageName:toolName format`
  2. `Tool not found: unified-research-finder:unified_search`
  3. `Tool not found: unified-research-finder:terminal`
- **根因**：operitAI 自动扫描 `scripts/` 目录，试图把每个 `.py` 文件按 `{skill_name}:{script_basename}` 格式注册为工具。由于 SKILL.md 缺少显式 `tools` 声明，注册格式校验失败，后续工具查找全部落空。
- **修复**：在 SKILL.md frontmatter 中新增 `tools` 显式声明：
  ```yaml
  tools:
    - unified_search.py
    - pubmed_search.py
    - scholar_search.py
  ```

### 📝 文档改进

- README.md 项目结构段落地道化：去掉面向维护者的 "你需要上传/发布" 措辞，改为中性的「项目

**关键词**: 统一的学术文献检索助手, 覆盖两大体系, 官方, Unified, Research, Finder, PubMed, E-utilities

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/unified-research-finder)

---

## [3. synomega](https://clawhub.ai/zbc0315/synomega)

**Slug**: `synomega`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Retrosynthesis with the synomega Python package (pip install synomega) — single-step reactant prediction, multi-step route planning, and a continuous synthes...

**中文介绍**: Retrosynthesis with the synomega Python package (pip install synomega) — single-step reactant prediction, multi-step route planning, and a continuous synthes...

Latest changelog:
Package-based: uses the synomega PyPI package locally (Python API + CLI + a helper loading a local model/stock) instead of a hosted API.

**关键词**: synomega, Retrosynthesis, Python, package, pip, install, single-step, reactant

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/synomega)

---

## [4. 智慧芽-实用新型专利以图搜图](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-utility-patent-image-search)

**Slug**: `linkfox-zhihuiya-utility-patent-image-search`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 144 | 🧩 2

**原始简介**: 基于智慧芽的专利图片相似度搜索，支持通过图片URL检索实用新型专利。当用户提到实用新型专利图片搜索、实用新型专利侵权检查、实用新型专利搜索、以图搜专利、实用新型专利相似度检测、专利图片匹配、专利形状/图案/色彩匹配、检查产品结构是否侵犯已有实用新型专利、patent image search, utility m...

**中文介绍**: 基于智慧芽的专利图片相似度搜索，支持通过图片URL检索实用新型专利。当用户提到实用新型专利图片搜索、实用新型专利侵权检查、实用新型专利搜索、以图搜专利、实用新型专利相似度检测、专利图片匹配、专利形状/图案/色彩匹配、检查产品结构是否侵犯已有实用新型专利、patent image search, utility m...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-实用新型专利以图搜图, 基于智慧芽的专利图片相似度搜索, 支持通过图片URL检索实用新型专利, 图案, image, search, utility, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-utility-patent-image-search)

---

## [5. Actionbook](https://clawhub.ai/skills?q=actionbook)

**Slug**: `actionbook`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Activate when the user needs to interact with any website — browser automation, web scraping, screenshots, form filling, UI testing, monitoring, or building...

**中文介绍**: Activate when the user needs to interact with any website — browser automation, web scraping, screenshots, form filling, UI testing, monitoring, or building...

Latest changelog:
- Initial release of the actionbook skill (version 1.0.0).
- Added core documentation for browser automation, web scraping, form filling, UI testing, and more.
- Provides end-user guidance on using search and get commands for pre-verified page actions and selectors.
- Includes workflow examples, browser command references, and troubleshooting/fallback instructions.
- Added _meta.json file; removed skill-card.md for metadata update.

**关键词**: Actionbook, Activate, when, user, needs, interact, any, website

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/actionbook)

---

## [6. Career Success Predictor 职业匹配评估](https://clawhub.ai/tonytan10086/career-success-predictor)

**Slug**: `career-success-predictor`  
**Version**: 1.0.3  
**Stats**: ⭐ 1 | ⬇️ 285 | 🧩 3

**原始简介**: Career fit assessment through 10 occupation-specific questions. Estimates success likelihood and produces a personalized report. Trigger when users ask about career switches, job fit, success odds, or career transitions — including "Am I suited for X?", "Can I make it as X?", "Should I switch to X?"

**中文介绍**: Career fit assessment through 10 occupation-specific questions. Estimates success likelihood and produces a personalized report. Trigger when users ask about career switches, job fit, success odds, or career transitions — including "Am I suited for X?", "Can I make it as X?", "Should I switch to X?"

Latest changelog:
### Added
- Enhanced description with richer trigger keywords (中文, 日本語, 職業転換 variations)
- Keywords metadata field for better SEO/discoverability
- Support for multilingual trigger phrases
- GitHub repository for broader accessibility
- Comprehensive README with use-case examples and design highlights

### Improved
- Clearer explanation of fit vs. readiness layers
- Better documentation of question design principles
- Enhanced scoring methodology documentation
- More detailed edge-case handling guidance

### Changed
- Updated metadata structure to include version and keywords

**关键词**: 职业匹配评估, Career, Success, Predictor, fit, assessment, through, occupation-specific

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/career-success-predictor)

---

## [7. Tmp.FeG5X4EebW](https://clawhub.ai/chrischall/untappd-mcp)

**Slug**: `untappd-mcp`  
**Version**: 1.8.0  
**Stats**: ⭐ 0 | ⬇️ 1314 | 🧩 16

**原始简介**: Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and po...

**中文介绍**: Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and po...

Latest changelog:
- Added untappd_venue_menu tool to fetch a venue's full verified beer menu, providing more complete tap lists than venue_info.
- Updated documentation to describe the new untappd_venue_menu, including its paging and resumable behavior.
- Removed skill-card.md from the repository.

**关键词**: Tmp.FeG5X4EebW, Search, Untappd, beers, breweries, venues, read, user

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/untappd-mcp)

---

## [8. 智慧芽-专利参考文献查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-patent-forward-citation)

**Slug**: `linkfox-zhihuiya-patent-forward-citation`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 260 | 🧩 4

**原始简介**: 从智慧芽专利数据库查询专利的前向引用详情。当用户询问专利引用、被引用专利、引用文献、专利参考文献、前向引用、在先技术引用或想查看特定专利在申请过程中引用了哪些专利、非专利文献、patent cited references, forward citations, patent references, citati...

**中文介绍**: 从智慧芽专利数据库查询专利的前向引用详情。当用户询问专利引用、被引用专利、引用文献、专利参考文献、前向引用、在先技术引用或想查看特定专利在申请过程中引用了哪些专利、非专利文献、patent cited references, forward citations, patent references, citati...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利参考文献查询, 从智慧芽专利数据库查询专利的前向引用详情, cited, references, forward, citations, patent, citati

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-patent-forward-citation)

---

## [9. 智慧芽-外观专利以图搜图](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-patent-image-search)

**Slug**: `linkfox-zhihuiya-patent-image-search`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 665 | 🧩 5

**原始简介**: 基于智慧芽的专利图片相似度搜索，支持通过图片URL检索外观设计专利。当用户提到专利图片搜索、外观设计专利侵权检查、外观专利搜索、视觉专利查询、以图搜专利、专利相似度检测、专利图片匹配、洛迦诺分类搜索、检查产品设计是否侵犯已有专利、patent image search, design patent search,...

**中文介绍**: 基于智慧芽的专利图片相似度搜索，支持通过图片URL检索外观设计专利。当用户提到专利图片搜索、外观设计专利侵权检查、外观专利搜索、视觉专利查询、以图搜专利、专利相似度检测、专利图片匹配、洛迦诺分类搜索、检查产品设计是否侵犯已有专利、patent image search, design patent search,...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-外观专利以图搜图, 基于智慧芽的专利图片相似度搜索, 支持通过图片URL检索外观设计专利, image, search, design, patent, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-patent-image-search)

---

## [10. 智慧芽-专利被引用（前向引用）查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-patent-cited)

**Slug**: `linkfox-zhihuiya-patent-cited`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 249 | 🧩 4

**原始简介**: 从智慧芽（PatSnap）查询专利被引用数据，包括被引用次数和引用专利详情。当用户提到专利被引用、被引分析、专利影响力、引用频次、专利家族被引、前向引用、想了解哪些专利引用了某一专利、patent citations, citation count, patent influence, citation anal...

**中文介绍**: 从智慧芽（PatSnap）查询专利被引用数据，包括被引用次数和引用专利详情。当用户提到专利被引用、被引分析、专利影响力、引用频次、专利家族被引、前向引用、想了解哪些专利引用了某一专利、patent citations, citation count, patent influence, citation anal...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利被引用（前向引用）查询, 从智慧芽（PatSnap）查询专利被引用数据, 包括被引用次数和引用专利详情, citations, citation, count, patent, influence

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-patent-cited)

---

## [11. 智慧芽-专利全文附图获取](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-fulltext-image)

**Slug**: `linkfox-zhihuiya-fulltext-image`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 638 | 🧩 5

**原始简介**: 通过专利ID或公开号获取专利文件中的全文附图（图纸、示意图、图表）。当用户询问专利图片、专利图纸、专利示意图、专利插图、全文附图、专利图表、专利技术图或想查看、下载专利文件中的嵌入图片、patent fulltext drawings, patent diagrams, technical drawings, p...

**中文介绍**: 通过专利ID或公开号获取专利文件中的全文附图（图纸、示意图、图表）。当用户询问专利图片、专利图纸、专利示意图、专利插图、全文附图、专利图表、专利技术图或想查看、下载专利文件中的嵌入图片、patent fulltext drawings, patent diagrams, technical drawings, p...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利全文附图获取, fulltext, drawings, patent, diagrams, technical, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-fulltext-image)

---

## [12. 智慧芽-专利 PDF 下载](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-pdf-data)

**Slug**: `linkfox-zhihuiya-pdf-data`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 274 | 🧩 4

**原始简介**: 通过专利ID或公开号从智慧芽专利数据库下载专利PDF全文文档。当用户提到专利PDF下载、专利全文、专利文件获取、公开号查询、专利家族PDF替代、批量专利PDF导出、patent PDF download, patent full-text document, patent file download, PatSn...

**中文介绍**: 通过专利ID或公开号从智慧芽专利数据库下载专利PDF全文文档。当用户提到专利PDF下载、专利全文、专利文件获取、公开号查询、专利家族PDF替代、批量专利PDF导出、patent PDF download, patent full-text document, patent file download, PatSn...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利, 下载, PDF, download, patent, full-text, document, file

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-pdf-data)

---

## [13. 智慧芽-专利家族查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-patent-family)

**Slug**: `linkfox-zhihuiya-patent-family`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 671 | 🧩 5

**原始简介**: 通过专利ID或公开号查询智慧芽（PatSnap）的专利家族信息。当用户提到专利家族、专利家族搜索、简单同族、INPADOC同族、PatSnap家族、同族专利查找、专利等同、家族成员、查找跨国相关专利、patent family, family patents, patent equivalents, cross-...

**中文介绍**: 通过专利ID或公开号查询智慧芽（PatSnap）的专利家族信息。当用户提到专利家族、专利家族搜索、简单同族、INPADOC同族、PatSnap家族、同族专利查找、专利等同、家族成员、查找跨国相关专利、patent family, family patents, patent equivalents, cross-...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利家族查询, family, patents, patent, equivalents, cross, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-patent-family)

---

## [14. 智慧芽-专利法律状态查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-legal-status)

**Slug**: `linkfox-zhihuiya-legal-status`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 648 | 🧩 5

**原始简介**: 从智慧芽（PatSnap）数据库查询专利法律状态信息。当用户提到专利法律状态、专利有效性核查、专利状态查询、专利事件历史、简单法律状态、转让、许可、质押、异议、诉讼、复审等法律事件、patent legal status, patent validity, patent events, transfer/lice...

**中文介绍**: 从智慧芽（PatSnap）数据库查询专利法律状态信息。当用户提到专利法律状态、专利有效性核查、专利状态查询、专利事件历史、简单法律状态、转让、许可、质押、异议、诉讼、复审等法律事件、patent legal status, patent validity, patent events, transfer/lice...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利法律状态查询, legal, status, patent, validity, events, transfer, lice

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-legal-status)

---

## [15. 智慧芽-专利核心著录查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-simple-bibliography)

**Slug**: `linkfox-zhihuiya-simple-bibliography`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 647 | 🧩 5

**原始简介**: 从智慧芽专利数据库查询专利简要著录（书目）数据。当用户提到专利著录信息查询、专利基本信息获取、专利书目数据、专利公开详情、按专利号查询发明人、专利申请人信息、专利摘要获取、专利分类号（IPC/CPC）、专利引用查询或任何通过专利ID、公开号检索结构化元数据的请求、patent brief bibliography...

**中文介绍**: 从智慧芽专利数据库查询专利简要著录（书目）数据。当用户提到专利著录信息查询、专利基本信息获取、专利书目数据、专利公开详情、按专利号查询发明人、专利申请人信息、专利摘要获取、专利分类号（IPC/CPC）、专利引用查询或任何通过专利ID、公开号检索结构化元数据的请求、patent brief bibliography...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利核心著录查询, 从智慧芽专利数据库查询专利简要著录（书目）数据, brief, bibliography, Latest, changelog, Update

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-simple-bibliography)

---

## [16. 智慧芽-专利权利要求获取](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-claim-data)

**Slug**: `linkfox-zhihuiya-claim-data`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 644 | 🧩 5

**原始简介**: 从智慧芽（PatSnap）获取专利权利要求数据。当用户提到专利权利要求、权利要求文本、独立权利要求、从属权利要求、权利要求数量、权利要求树、权利要求分析、权利要求范围、权利要求语言、想查看特定专利的权利要求部分、patent claims, independent claims, dependent claims...

**中文介绍**: 从智慧芽（PatSnap）获取专利权利要求数据。当用户提到专利权利要求、权利要求文本、独立权利要求、从属权利要求、权利要求数量、权利要求树、权利要求分析、权利要求范围、权利要求语言、想查看特定专利的权利要求部分、patent claims, independent claims, dependent claims...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利权利要求获取, 从智慧芽（PatSnap）获取专利权利要求数据, claims, independent, dependent, Latest, changelog, Update

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-claim-data)

---

## [17. 中国专利.Skill](https://clawhub.ai/handsomestwei/patent-disclosure-skill)

**Slug**: `patent-disclosure-skill`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 1583 | 🧩 8

**原始简介**: 中国专利：从项目文档挖掘专利点并生成可交付技术交底书（查新、脱敏成文、自检与迭代）；或将已有专利解读为通俗笔记与 Obsidian 知识图谱（叙事故事线、公开线索辅助）。| China patents: draft technical disclosures from project docs, or read existing patents into plain-language notes and an Obsidian knowledge graph.

**中文介绍**: 中国专利：从项目文档挖掘专利点并生成可交付技术交底书（查新、脱敏成文、自检与迭代）；或将已有专利解读为通俗笔记与 Obsidian 知识图谱（叙事故事线、公开线索辅助）。| China patents: draft technical disclosures from project docs, or read existing patents into plain-language notes and an Obsidian knowledge graph.

Latest changelog:
2.0.0 adds patent plain-language reading and Obsidian graph tools, expands all workflows.

- 新增专利通俗解读模式：直接读懂已有专利，自动生成叙事笔记与 Obsidian Canvas 知识图谱，辅助公开线索抓取

**关键词**: 中国专利.Skill, 中国专利, 或将已有专利解读为通俗笔记与, 知识图谱（叙事故事线、公开线索辅助）, Obsidian, China, patents, draft

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/patent-disclosure-skill)

---

## [18. 智慧芽-专利说明书翻译](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-description-data-translated)

**Slug**: `linkfox-zhihuiya-description-data-translated`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 257 | 🧩 4

**原始简介**: 从智慧芽获取翻译后的专利说明书（描述）文本。当用户要求专利说明书翻译、其他语言的专利全文、翻译后的专利全文，或想查看中文、英文、日文版的专利说明书、patent specification translation, patent description translation, PatSnap, patent t...

**中文介绍**: 从智慧芽获取翻译后的专利说明书（描述）文本。当用户要求专利说明书翻译、其他语言的专利全文、翻译后的专利全文，或想查看中文、英文、日文版的专利说明书、patent specification translation, patent description translation, PatSnap, patent t...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利说明书翻译, 从智慧芽获取翻译后的专利说明书（描述）文本, specification, translation, patent, PatSnap, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-description-data-translated)

---

## [19. 智慧芽-专利说明书获取](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-description-data)

**Slug**: `linkfox-zhihuiya-description-data`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 254 | 🧩 4

**原始简介**: 通过专利ID或公开号从智慧芽专利数据库获取专利说明书（描述）数据。当用户提到专利说明书、专利全文、专利技术描述、专利实施方式详情、智慧芽说明书数据、patent specification, patent full text, technical description, embodiment details,...

**中文介绍**: 通过专利ID或公开号从智慧芽专利数据库获取专利说明书（描述）数据。当用户提到专利说明书、专利全文、专利技术描述、专利实施方式详情、智慧芽说明书数据、patent specification, patent full text, technical description, embodiment details,...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利说明书获取, specification, patent, full, text, technical, embodiment, details

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-description-data)

---

## [20. 智慧芽-专利权利要求翻译](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-claim-data-translated)

**Slug**: `linkfox-zhihuiya-claim-data-translated`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 258 | 🧩 4

**原始简介**: 从智慧芽专利数据库获取翻译后的专利权利要求。当用户询问专利权利要求、权利要求翻译、查看特定语言（中文、英文或日文）的权利要求、通过专利ID或公开号查询专利权利、分析权利要求文本、claim translation, patent claim translation, PatSnap, patent transla...

**中文介绍**: 从智慧芽专利数据库获取翻译后的专利权利要求。当用户询问专利权利要求、权利要求翻译、查看特定语言（中文、英文或日文）的权利要求、通过专利ID或公开号查询专利权利、分析权利要求文本、claim translation, patent claim translation, PatSnap, patent transla...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利权利要求翻译, 从智慧芽专利数据库获取翻译后的专利权利要求, translation, patent, claim, PatSnap, transla, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-claim-data-translated)

---

## [21. 智慧芽-专利详细著录信息查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-bibliography)

**Slug**: `linkfox-zhihuiya-bibliography`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 638 | 🧩 5

**原始简介**: 通过专利ID或公开号查询智慧芽专利数据库中的专利著录（书目）信息。当用户提到专利著录信息查询、专利书目信息、专利申请人查询、专利发明人查询、专利分类号、专利摘要获取、专利引用分析、专利优先权主张、专利申请引用、专利审查员信息、patent bibliographic data, inventor lookup,...

**中文介绍**: 通过专利ID或公开号查询智慧芽专利数据库中的专利著录（书目）信息。当用户提到专利著录信息查询、专利书目信息、专利申请人查询、专利发明人查询、专利分类号、专利摘要获取、专利引用分析、专利优先权主张、专利申请引用、专利审查员信息、patent bibliographic data, inventor lookup,...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利详细著录信息查询, bibliographic, data, inventor, lookup, Latest, changelog, Update

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-bibliography)

---

## [22. 智慧芽-专利标题与摘要翻译](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-abstract-data-translated)

**Slug**: `linkfox-zhihuiya-abstract-data-translated`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 259 | 🧩 4

**原始简介**: 从智慧芽（PatSnap）专利数据库获取专利标题和摘要的翻译版本。当用户要求专利摘要翻译、专利标题翻译、翻译后的专利摘要、其他语言的专利内容、中文/英文/日文的专利摘要，或需要通过专利ID或公开号查询特定专利的摘要、标题、patent abstract translation, patent title tran...

**中文介绍**: 从智慧芽（PatSnap）专利数据库获取专利标题和摘要的翻译版本。当用户要求专利摘要翻译、专利标题翻译、翻译后的专利摘要、其他语言的专利内容、中文/英文/日文的专利摘要，或需要通过专利ID或公开号查询特定专利的摘要、标题、patent abstract translation, patent title tran...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利标题与摘要翻译, 英文, 日文的专利摘要, translation, patent, tran, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-abstract-data-translated)

---

## [23. Conversation Logger](https://clawhub.ai/zhan5331/johnzhan-openclaw-skills)

**Slug**: `johnzhan-openclaw-skills`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Project-based conversation logging for OpenClaw. Use when setting up daily auto-logging across parallel projects, building conversational continuity between...

**中文介绍**: Project-based conversation logging for OpenClaw. Use when setting up daily auto-logging across parallel projects, building conversational continuity between...

Latest changelog:
Version 0.1.0 of conversation-logger skill introduces project-scoped conversation logging for OpenClaw workspaces.

- Adds structured daily conversation logging, with per-project folders and daily markdown log files.
- Automatically reads the previous day's log on the first turn each day for conversational continuity.
- Enables on-demand manual lookup of past logs and keyword search within project histories.
- Supports cross-platform directory structure and provides setup instructions for both Windows and Unix-based systems.
- Facilitates sub-agent logging and provides integration tips for multi-project, parallel workflows.

**关键词**: Conversation, Logger, Project-based, logging, OpenClaw, Use, when, setting

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/johnzhan-openclaw-skills)

---

## [24. 智慧芽-专利摘要附图查询](https://clawhub.ai/linkfox-ai/linkfox-zhihuiya-abstract-image)

**Slug**: `linkfox-zhihuiya-abstract-image`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 638 | 🧩 5

**原始简介**: 通过专利ID或公开号从智慧芽专利数据库获取专利摘要附图。当用户提到专利摘要附图、专利图纸、专利示意图、专利图片、摘要附图检索、专利图片查询、patent abstract images, patent drawings, patent illustrations, PatSnap, abstract image...

**中文介绍**: 通过专利ID或公开号从智慧芽专利数据库获取专利摘要附图。当用户提到专利摘要附图、专利图纸、专利示意图、专利图片、摘要附图检索、专利图片查询、patent abstract images, patent drawings, patent illustrations, PatSnap, abstract image...

Latest changelog:
Update from 1.0.4 to 1.0.5

**关键词**: 智慧芽-专利摘要附图查询, images, patent, drawings, illustrations, PatSnap, image, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/linkfox-zhihuiya-abstract-image)

---

## [25. Agenticflow Skill](https://clawhub.ai/cgreselin-create/agenticflow-skill)

**Slug**: `agenticflow-skill`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Créer la proposition du Skill AgenticFlow pour automatiser LinkedIn

**中文介绍**: Créer la proposition du Skill AgenticFlow pour automatiser LinkedIn

Latest changelog:
Initial release: Automate key LinkedIn interactions in a streamlined workflow.

- Publishes posts, articles, and videos; allows content scheduling
- Sends and replies to private messages; manages invitations and connections
- Retrieves engagement statistics (likes, comments, shares)
- Requires LinkedIn account and API/OAuth access
- Provides end-of-day summary and error handling for authentication and platform limits

**关键词**: la, du, Agenticflow, Skill, Créer, proposition, pour, automatiser

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agenticflow-skill)

---

