# ClawHub Skills Daily | 2026-08-15

> 共 25 个 skills

## [1. Fish Flashing & Scraping Detection (Ectoparasite Warning) | 鱼类擦缸/蹭底行为识别（外寄）](https://clawhub.ai/18072937735/smyx-fish-flashing-scraping-detection-analysis)

**Slug**: `smyx-fish-flashing-scraping-detection-analysis`  
**Version**: 1.0.8  
**Stats**: ⭐ 0 | ⬇️ 1070 | 🧩 9

**原始简介**: Through fixed aquarium cameras, the system analyzes fish behavior videos and detects abnormal frictional actions between fish bodies and tank walls, substrate, or rockwork — 'flashing' (fish flipping sideways and brushing tank walls rapidly) and 'scraping' (fish belly/flank rubbing on substrate). The system counts abnormal contact frequency per minute. | 通过鱼缸固定摄像头，分析鱼类的行为视频，检测鱼体与缸壁、底砂、造景石等物体的异常摩擦动作（擦缸：鱼体侧身快速蹭过缸壁；蹭底：鱼体腹部或侧面贴底砂摩擦）。统计每分钟的异常接触频次，当频次超过阈值（默认 5 次/分钟）且持续时间超过 10 秒时，输出'外寄风险提示'，提醒用户检查是否有寄生虫（如小瓜虫、车轮虫、三代虫）感染或皮肤不适。

**中文介绍**: Through fixed aquarium cameras, the system analyzes fish behavior videos and detects abnormal frictional actions between fish bodies and tank walls, substrate, or rockwork — 'flashing' (fish flipping sideways and brushing tank walls rapidly) and 'scraping' (fish belly/flank rubbing on substrate). The system counts abnormal contact frequency per minute. | 通过鱼缸固定摄像头，分析鱼类的行为视频，检测鱼体与缸壁、底砂、造景石等物体的异常摩擦动作（擦缸：鱼体侧身快速蹭过缸壁；蹭底：鱼体腹部或侧面贴底砂摩擦）。统计每分钟的异常接触频次，当频次超过阈值（默认 5 次/分钟）且持续时间超过 10 秒时，输出'外寄风险提示'，提醒用户检查是否有寄生虫（如小瓜虫、车轮虫、三代虫）感染或皮肤不适。

Latest changelog:
smyx-fish-flashing-scraping-detection-analysis 1.0.8

- Updated documentation in SKILL.md.
- Removed redundant skill-card.md file.
- Modified configuration in skills/smyx_common/scripts/config.yaml.

**关键词**: 鱼类擦缸, 蹭底行为识别（外寄）, Fish, Flashing, Scraping, Detection, Ectoparasite, Warning

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-fish-flashing-scraping-detection-analysis)

---

## [2. cn-ecommerce-ops](https://clawhub.ai/g305595965/cn-ecommerce-ops)

**Slug**: `cn-ecommerce-ops`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 181 | 🧩 3

**原始简介**: 国内电商全链路运营专家技能，覆盖淘宝、天猫、京东、拼多多、抖音电商、小红书、视频号六大平台。提供选品评分、定价与利润测算、广告投放ROI测算、店铺转化漏斗诊断、广告法违禁词合规检查五个可计算工具，以及一个实时数据桥接器(live.py)——先用 WebSearch/WebFetch 拉取当前真实佣金率、类目退货率、1688进货价、关键词搜索量，再一键灌入各计算器，实现"实时可用"的决策。当用户涉及国内电商选品、定价、算利润、算ROI、投直通车或千川、做店铺诊断、优化标题主图详情页、写商品文案、直播运营、检查文案是否违反广告法、平台规则与流量玩法，或需要查最新费率/获取实时行情来辅助决策时，应使用本技能。

**中文介绍**: 国内电商全链路运营专家技能，覆盖淘宝、天猫、京东、拼多多、抖音电商、小红书、视频号六大平台。提供选品评分、定价与利润测算、广告投放ROI测算、店铺转化漏斗诊断、广告法违禁词合规检查五个可计算工具，以及一个实时数据桥接器(live.py)——先用 WebSearch/WebFetch 拉取当前真实佣金率、类目退货率、1688进货价、关键词搜索量，再一键灌入各计算器，实现"实时可用"的决策。当用户涉及国内电商选品、定价、算利润、算ROI、投直通车或千川、做店铺诊断、优化标题主图详情页、写商品文案、直播运营、检查文案是否违反广告法、平台规则与流量玩法，或需要查最新费率/获取实时行情来辅助决策时，应使用本技能。

Latest changelog:
**重大更新：引入实时数据支持与脚本结构优化**

- 增加了 live.py 实时数据桥接脚本，实现从公开数据源获取类目佣金率、退货率、进货价和关键词搜索量，一键灌入各计算器，实现运营决策“实时可用”。
- 改进脚本结构，拆分脚本目录，增加 shared 数据模块（platform_fees.py），提升可维护性和数据一致性。
- README.md、SKILL.md 等文档全面更新，增加实时数据桥接、工作流 E、严明数据链路和入参合理性约束。
- 新增 examples、assets、references、tests 等目录和示例数据，支持自检与快速上手。
- skill-card.md 删除，统一文档入口和结构。

**关键词**: 国内电商全链路运营专家技能, 以及一个实时数据桥接器, ——先用, 再一键灌入各计算器, cn-ecommerce-ops, live.py, WebSearch, WebFetch

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cn-ecommerce-ops)

---

## [3. jf-open-pro-ai-smart-search](https://clawhub.ai/jftech/jf-open-pro-ai-smart-search)

**Slug**: `jf-open-pro-ai-smart-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: JF Tech Pro AI 智搜技能。根据语义内容（如"带帽子的人"、"车"、"狗"）搜索杰峰云存报警视频，获取匹配的视频片段列表。使用场景：智能视频检索、AI 事件搜索、语义化视频查找。

**中文介绍**: JF Tech Pro AI 智搜技能。根据语义内容（如"带帽子的人"、"车"、"狗"）搜索杰峰云存报警视频，获取匹配的视频片段列表。使用场景：智能视频检索、AI 事件搜索、语义化视频查找。

Latest changelog:
Initial release of jf-open-pro-ai-smart-search.

- Enables semantic AI search for cloud-stored event videos by keywords such as “person with hat,” “car,” or “dog.”
- Provides Python-based tools for searching, playback URL retrieval, and complete search-to-playback workflows.
- Credentials are securely required via environment variables only; API access is restricted to official JF endpoints.
- Supports multiple query types, including people, vehicles, animals, and behaviors.
- Includes detailed setup instructions, example usage scenarios, and troubleshooting for common errors.

**关键词**: JF, 智搜技能, 获取匹配的视频片段列表, 使用场景, 智能视频检索、AI, 事件搜索、语义化视频查找, Tech, Pro

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jf-open-pro-ai-smart-search)

---

## [4. baoyu-infographic](https://clawhub.ai/skills?q=baoyu-infographic)

**Slug**: `baoyu-infographic`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 14 | 🧩 2

**原始简介**: Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

**中文介绍**: Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system (21 layouts x 21 styles). Use when the user asks to create an infographic, 信息图, visual summary, 可视化, or a high-density information image, or wants an article turned into a visual poster.

Latest changelog:
- Initial opencode port of baoyu-infographic (from upstream v1.56.1 by 宝玉/JimLiu).
- Generates professional infographics from articles, URLs, or topics using 21 layouts × 21 styles.
- Auto-selects layouts/styles from user keywords (信息图, 可视化, 高密度信息大图, etc.) for fast workflow.
- Produces image and editable Markdown files: analysis, structured content, and infographic prompts.
- Requires OPENROUTER_API_KEY for image generation; gracefully degrades if unavailable.

**关键词**: an, baoyu-infographic, Generate, professional, infographic, article, document, URL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/baoyu-infographic)

---

## [5. translate-to-chn](https://clawhub.ai/j3ffyang/translate-to-chn)

**Slug**: `translate-to-chn`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 136 | 🧩 3

**原始简介**: Translate a specific article from ai-thoughts/docs/ into Simplified Chinese, writing the output to an exactly-same-filename "-chn.md" file. Use when the user names a specific article and asks to translate it (e.g. "translate 260803-ollama-to-llamacpp", "翻译 xxx", "make a -chn.md version"). Never runs automatically; only acts on an explicitly chosen article.

**中文介绍**: Translate a specific article from ai-thoughts/docs/ into Simplified Chinese, writing the output to an exactly-same-filename "-chn.md" file. Use when the user names a specific article and asks to translate it (e.g. "translate 260803-ollama-to-llamacpp", "翻译 xxx", "make a -chn.md version"). Never runs automatically; only acts on an explicitly chosen article.

Latest changelog:
- Added support for a "bilingual-gloss" style: all Simplified Chinese outputs now include inline English glosses for technical terms and section titles, plus plain-language explanations for unfamiliar concepts.
- Updated procedures and verification steps to require glossing of technical vocabulary and explanatory additions for clarity.
- Removed skill-card.md (no longer used).
- Quality and error handling sections remain unchanged except for references to the new glossing requirements.

**关键词**: translate-to-chn, Translate, specific, article, ai-thoughts, docs, Simplified, Chinese

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/translate-to-chn)

---

## [6. Job Agent for AgentMesh360](https://clawhub.ai/jiyangnan/job-agent)

**Slug**: `job-agent`  
**Version**: 0.5.26  
**Stats**: ⭐ 0 | ⬇️ 2381 | 🧩 49

**原始简介**: Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

**中文介绍**: Use AgentMesh Job Agent for resume-driven job discovery, signed review, user-confirmed delivery and audit on Boss直聘, 猎聘, 智联招聘 and 51Job.

Latest changelog:
Bounded 51Job reconciliation now preserves cumulative delivered, unavailable, and unresolved outcomes, prevents repeat clicks, and completes safely into audit.

**关键词**: Agent, Job, AgentMesh360, Use, AgentMesh, resume-driven, discovery, signed

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/job-agent)

---

## [7. Clawhub Package](https://clawhub.ai/vnbochkarev-netizen/vibo-memory)

**Slug**: `vibo-memory`  
**Version**: 1.0.10  
**Stats**: ⭐ 0 | ⬇️ 163 | 🧩 11

**原始简介**: Use when the agent needs persistent memory (L1/L2/L3), web-search savings (compress articles up to 96%), or thread memory (compress long conversations, resto...

**中文介绍**: Use when the agent needs persistent memory (L1/L2/L3), web-search savings (compress articles up to 96%), or thread memory (compress long conversations, resto...

Latest changelog:
v1.0.10: Living Archive (Product 4) + L3 secret vault (vibo setup/reveal) + fixed email trial activation

**关键词**: Agent, Clawhub, Package, Use, when, needs, persistent, memory

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vibo-memory)

---

## [8. AI人生教练](https://clawhub.ai/luhayden-blip/ai-life-coach)

**Slug**: `ai-life-coach`  
**Version**: 2.1.4  
**Stats**: ⭐ 0 | ⬇️ 401 | 🧩 9

**原始简介**: AI 人生教练：用对话陪你把当下活明白。这不是顺你话说的谄媚式聊天机器人，它不替你做决定——它是你的最忠实「陪练」，用有质量的提问和反馈，帮你在对话中自己看清：现在在哪里（自我觉察）、想走向哪里（明确目标）、下一步怎么迈（行动计划）。基于斯坦福《人生设计课》、积极心理学与心流理论，融合焦点解决提问（SFBT）、叙事外化、奥德赛计划等教练方法。适用场景：迷茫 ·心里堵 ·提不起劲 ·工作没动力 ·不知道自己想要什么 ·想找人聊聊 ·自我觉察 ·明确目标 ·制定行动计划。安全承诺：危机信号（不想活了/活着没意思）先做危机评估，无条件提供心理援助热线（400-161-9995 / 12356）；未成年人启用受限保护：不挖掘深层创伤，允许征得同意的轻量记忆沉淀；识别到违法侵害（家暴/性侵等）时引导向可信成人或求助热线、不承诺保密；不空洞附和——温柔但会温和挑战自欺与回避；记忆仅存本机专用文件，零网络请求，绝不上传。说「我想做一次人生教练对话」或输入 /ai-life-coach 即可开始。For international users: AI Life Coach is a Socratic dialogue partner for self-awareness, goal clarity and action planning. Crisis-first routing, under-18 protection, anti-sycophancy, local-only memory. See README.md for full English description.

**中文介绍**: AI 人生教练：用对话陪你把当下活明白。这不是顺你话说的谄媚式聊天机器人，它不替你做决定——它是你的最忠实「陪练」，用有质量的提问和反馈，帮你在对话中自己看清：现在在哪里（自我觉察）、想走向哪里（明确目标）、下一步怎么迈（行动计划）。基于斯坦福《人生设计课》、积极心理学与心流理论，融合焦点解决提问（SFBT）、叙事外化、奥德赛计划等教练方法。适用场景：迷茫 ·心里堵 ·提不起劲 ·工作没动力 ·不知道自己想要什么 ·想找人聊聊 ·自我觉察 ·明确目标 ·制定行动计划。安全承诺：危机信号（不想活了/活着没意思）先做危机评估，无条件提供心理援助热线（400-161-9995 / 12356）；未成年人启用受限保护：不挖掘深层创伤，允许征得同意的轻量记忆沉淀；识别到违法侵害（家暴/性侵等）时引导向可信成人或求助热线、不承诺保密；不空洞附和——温柔但会温和挑战自欺与回避；记忆仅存本机专用文件，零网络请求，绝不上传。说「我想做一次人生教练对话」或输入 /ai-life-coach 即可开始。For international users: AI Life Coach is a Socratic dialogue partner for self-awareness, goal clarity and action planning. Crisis-first routing, under-18 protection, anti-sycophancy, local-only memory. See README.md for full English description.

Latest changelog:
v2.1.4: 未成年红线微调——允许征得同意的轻量记忆沉淀；新增识别违法侵害(家暴/性侵等)处置机制(安全优先/接住不评判/不承诺保密/连上现实力量)，蒸馏自国家卫健委心理援助热线指南与强制报告制度

**关键词**: AI人生教练, 人生教练, 用对话陪你把当下活明白, 这不是顺你话说的谄媚式聊天机器人, 它不替你做决定——它是你的最忠实「陪练」, 用有质量的提问和反馈, 帮你在对话中自己看清, 基于斯坦福《人生设计课》、积极心理学与心流理论

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-life-coach)

---

## [9. agentic-wine](https://clawhub.ai/vbaulin/agentic-wine)

**Slug**: `agentic-wine`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 230 | 🧩 2

**原始简介**: Turn a brand, luxury product or event into an original regenerative wine concept, constructor dossier and producer-ready commission through Vin-Q.

**中文介绍**: Turn a brand, luxury product or event into an original regenerative wine concept, constructor dossier and producer-ready commission through Vin-Q.

Latest changelog:
Nine-gate Vin-Q Method; live constructor and A2A discovery; deterministic decision-system metadata; current privacy, adult-use and alcohol-delivery controls.

**关键词**: or, an, agentic-wine, Turn, brand, luxury, product, event

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentic-wine)

---

## [10. eve-esi](https://clawhub.ai/burnshall-ui/eve-esi)

**Slug**: `eve-esi`  
**Version**: 1.3.3  
**Stats**: ⭐ 2 | ⬇️ 2528 | 🧩 18

**原始简介**: Query and manage EVE Online characters via the ESI (EVE Swagger Interface) REST API. Performs OAuth2/PKCE browser login and stores plus auto-refreshes long-lived OAuth tokens locally in ~/.openclaw/eve-tokens.json. Read-only by default and can reach any ESI endpoint, including non-character public data; state-changing writes (mail, fittings, market orders, planetary interaction) happen only when explicitly invoked with --allow-write. Use when the user asks about EVE Online character data, wallet balance, ISK transactions, assets, skill queue, skill points, clone locations, implants, fittings, contracts, market orders, mail, industry jobs, killmails, planetary interaction, loyalty points, or any other EVE account management task.

**中文介绍**: Query and manage EVE Online characters via the ESI (EVE Swagger Interface) REST API. Performs OAuth2/PKCE browser login and stores plus auto-refreshes long-lived OAuth tokens locally in ~/.openclaw/eve-tokens.json. Read-only by default and can reach any ESI endpoint, including non-character public data; state-changing writes (mail, fittings, market orders, planetary interaction) happen only when explicitly invoked with --allow-write. Use when the user asks about EVE Online character data, wallet balance, ISK transactions, assets, skill queue, skill points, clone locations, implants, fittings, contracts, market orders, mail, industry jobs, killmails, planetary interaction, loyalty points, or any other EVE account management task.

Latest changelog:
- Added new user_agent.py script to manage User-Agent headers.
- Updated bulk lookup endpoint documentation to match upstream ESI API changes.
- scripts/token_store.py was restored or added to skill includes.
- Removed __pycache__ artifacts and obsolete skill-card.md.
- Documentation updates to authentication and endpoint references.
- Regression tests and core scripts updated for consistency with the latest ESI API and token handling.

**关键词**: eve-esi, Query, manage, EVE, Online, characters, via, ESI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/eve-esi)

---

## [11. ctr-json-normalizer](https://clawhub.ai/rawven/ctr-json-normalizer)

**Slug**: `ctr-json-normalizer`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Normalize the final JSON output of a single-session CTR product-card click diagnosis. Use after the diagnosis draft is complete and before replying, whenever the report must contain exactly the agreed query, clicked item, unclicked items, five fixed dimensions, structured suggestions, and limitations.

**中文介绍**: Normalize the final JSON output of a single-session CTR product-card click diagnosis. Use after the diagnosis draft is complete and before replying, whenever the report must contain exactly the agreed query, clicked item, unclicked items, five fixed dimensions, structured suggestions, and limitations.

Latest changelog:
Initial release of ctr-json-normalizer Skill.

- Normalizes and validates JSON output for CTR product-card click diagnosis.
- Ensures the report contains exactly the required fields: query, clicked item, unclicked items, five fixed dimensions, structured suggestions, and limitations.
- Designed as the final step after diagnosis drafting, before responding.
- Automatic error handling: script returns "error" if the output does not meet requirements.
- Does not fetch images, infer causes, or generate new business suggestions.

**关键词**: of, ctr-json-normalizer, Normalize, final, JSON, output, single-session, CTR

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ctr-json-normalizer)

---

## [12. Pet Social Interaction Analysis | 宠物社交行为分析（与其他宠物互动）](https://clawhub.ai/smyx-sunjinhui/smyx-social-interaction-analysis-analysis)

**Slug**: `smyx-social-interaction-analysis-analysis`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 860 | 🧩 7

**原始简介**: AI-powered pet social interaction analysis for multi-pet households. Uses pose recognition and behavior classification to detect cat-cat, dog-dog, and cat-dog interactions—sniffing, chasing, biting, fleeing, hiding, playing—then records duration, frequency, initiator and receiver to generate a social-behavior report. Helps owners understand pet relationships, spot aggression or stress sources, and promote harmonious cohabitation. Scenarios: multi-pet homes, pet boarding centers, pet daycare, animal behavior clinics. | 通过多宠家庭固定摄像头，分析宠物之间（猫-猫、狗-狗、猫-狗等）的互动视频，利用姿态识别和行为分类模型检测嗅闻、追逐、撕咬、逃跑、躲避、玩耍等行为类型，记录每种行为的持续时间、频次以及发起者，生成社交行为报告。帮助主人了解宠物间的社交关系，识别潜在的攻击行为或压力源，促进多宠和谐共处。应用场景：多宠家庭（多猫/多狗/猫狗混养）、宠物寄养中心、宠物日托班、宠物行为诊所。

**中文介绍**: AI-powered pet social interaction analysis for multi-pet households. Uses pose recognition and behavior classification to detect cat-cat, dog-dog, and cat-dog interactions—sniffing, chasing, biting, fleeing, hiding, playing—then records duration, frequency, initiator and receiver to generate a social-behavior report. Helps owners understand pet relationships, spot aggression or stress sources, and promote harmonious cohabitation. Scenarios: multi-pet homes, pet boarding centers, pet daycare, animal behavior clinics. | 通过多宠家庭固定摄像头，分析宠物之间（猫-猫、狗-狗、猫-狗等）的互动视频，利用姿态识别和行为分类模型检测嗅闻、追逐、撕咬、逃跑、躲避、玩耍等行为类型，记录每种行为的持续时间、频次以及发起者，生成社交行为报告。帮助主人了解宠物间的社交关系，识别潜在的攻击行为或压力源，促进多宠和谐共处。应用场景：多宠家庭（多猫/多狗/猫狗混养）、宠物寄养中心、宠物日托班、宠物行为诊所。

Latest changelog:
- Updated SKILL.md to version 1.0.10 with minor content changes and version bump.
- Removed the file skill-card.md.
- Updated configuration details in skills/smyx_common/scripts/config.yaml.
- No changes to core functionality or user-facing features.

**关键词**: 宠物社交行为分析（与其他宠物互动）, Pet, Social, Interaction, Analysis, AI-powered, multi-pet, households

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-social-interaction-analysis-analysis)

---

## [13. Skill Vitals — Skill Audit](https://clawhub.ai/gold3bear/skill-vitals)

**Slug**: `skill-vitals`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 237 | 🧩 8

**原始简介**: Audit installed skills, cost, conflicts, and risk

**中文介绍**: Audit installed skills, cost, conflicts, and risk

Latest changelog:
English: Adds the doctor, explain, list, overlap, snapshot, and diff commands. doctor turns scan facts into cause, impact, and action with SV001-SV902 codes and states what it deliberately does not judge; explain reports why one skill never triggered and how to fix it. SKILL.md is now a driver that routes to those commands, with per-host evidence and judgment guidance moved into on-demand references. Internals were split from a single 3,394-line script into an importable package with no behaviour change: golden snapshots remain byte-identical. Publishing now verifies that the tag, the packaged CLI version, and the SKILL.md reference links all agree.

中文：新增 doctor、explain、list、overlap、snapshot、diff 六个命令。doctor 把扫描事实翻成「原因 → 影响 → 行动」并给出 SV001–SV902 编号，同时声明哪些它故意不判；explain 解释某个 skill 为什么没触发、怎么修。SKILL.md 改为驱动器，宿主证据与判断方法移入按需加载的 references。内部由单个 3394 行脚本拆成可导入的包，行为不变，golden 快照逐字节一致。发布流程新增校验：tag、打包后 CLI 的版本号、SKILL.md 的引用链接三者必须一致。

**关键词**: Skill, Vitals, Audit, installed, skills, cost, conflicts, risk

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-vitals)

---

## [14. deeply](https://clawhub.ai/komako-workshop/deeply)

**Slug**: `deeply`  
**Version**: 1.1.2  
**Stats**: ⭐ 0 | ⬇️ 124 | 🧩 5

**原始简介**: 召回经权威筛选的人物针对某个判断说过的一手观点，逐字原话带日期与出处， 语料取自访谈、文章、播客转写与研报（中英混合），覆盖财经/科技/商业/思想。 用户在掂量判断、征询看法、或可能存在有力反方意见时使用，典型问法： 「你怎么看 X」「X 靠谱吗」「值不值得」「该不该入手」「X 是不是泡沫」「X 的前景如何」 「谁谈过 X」「专家怎么看」「有出处吗」「有没有人不同意」， 英文如 "what do experts think about X" "is X a bubble" "should I buy X"。 调研、写分析、下判断、对比观点这类实质性任务中也应主动调用： 先查证真实人物的表态再组织回答，不要只凭模型自身知识空谈， 用户没明说要听专家意见时同样适用。 语料池不联网：今日价格、刚发生的新闻等时效事实不在射程； 健康、玄学、情感等池外领域没有语料。

**中文介绍**: 召回经权威筛选的人物针对某个判断说过的一手观点，逐字原话带日期与出处， 语料取自访谈、文章、播客转写与研报（中英混合），覆盖财经/科技/商业/思想。 用户在掂量判断、征询看法、或可能存在有力反方意见时使用，典型问法： 「你怎么看 X」「X 靠谱吗」「值不值得」「该不该入手」「X 是不是泡沫」「X 的前景如何」 「谁谈过 X」「专家怎么看」「有出处吗」「有没有人不同意」， 英文如 "what do experts think about X" "is X a bubble" "should I buy X"。 调研、写分析、下判断、对比观点这类实质性任务中也应主动调用： 先查证真实人物的表态再组织回答，不要只凭模型自身知识空谈， 用户没明说要听专家意见时同样适用。 语料池不联网：今日价格、刚发生的新闻等时效事实不在射程； 健康、玄学、情感等池外领域没有语料。

Latest changelog:
description 改用字面问法触发：列举「你怎么看 X」「X 是不是泡沫」「有没有人不同意」等 13 个中英问法，替换原来的抽象条件（真实提问往往语义命中、字面不沾，宿主 agent 会静默跳过）。同时按 Anthropic 规范改为第三人称，并移除会过期的语料规模数字。正文未变。

**关键词**: 召回经权威筛选的人物针对某个判断说过的一手观点, 逐字原话带日期与出处, 语料取自访谈、文章、播客转写与研报（中英混合）, 覆盖财经, 科技, 商业, 思想, deeply

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/deeply)

---

## [15. payaion-transfer](https://clawhub.ai/jan-blockbites/payaion-transfer)

**Slug**: `payaion-transfer`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 384 | 🧩 5

**原始简介**: Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. Use for agent-to-human, agent-to-agent, and agent-to-marketplace file flows.

**中文介绍**: Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. Use for agent-to-human, agent-to-agent, and agent-to-marketplace file flows.

Latest changelog:
Keyless selling is documented end to end: X-Payout-Address on the upload routes, the /m/ market link, and the 95/5 split.

**关键词**: API, payaion-transfer, Transfer, files, via, Payaion, REST, set

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/payaion-transfer)

---

## [16. score-leads](https://clawhub.ai/cargo-ai/score-leads)

**Slug**: `score-leads`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Score a list of companies against your ideal customer profile and rank them, powered by Cargo — every row gets a number, the reason behind it, and a tier, so the bottom of the list can be dropped before anyone spends time on it. Triggers: "score these leads", "which of these fit our ICP", "rank this list", "prioritise these accounts", "who should we go after first", "disqualify the bad ones", "tier this list". Firmographic fit, thresholds, tiering, prioritisation. Skip when: you have no list yet and need one built — use build-tam-list or find-b2b-leads; or you want people inside an account rather than a verdict on the account — use find-stakeholders.

**中文介绍**: Score a list of companies against your ideal customer profile and rank them, powered by Cargo — every row gets a number, the reason behind it, and a tier, so the bottom of the list can be dropped before anyone spends time on it. Triggers: "score these leads", "which of these fit our ICP", "rank this list", "prioritise these accounts", "who should we go after first", "disqualify the bad ones", "tier this list". Firmographic fit, thresholds, tiering, prioritisation. Skip when: you have no list yet and need one built — use build-tam-list or find-b2b-leads; or you want people inside an account rather than a verdict on the account — use find-stakeholders.

Latest changelog:
- Initial release of the score-leads skill for ranking companies by ideal customer fit.
- Scores and tiers company lists based on user-specified firmographic criteria and cut-offs.
- Provides clear reasons and missing data for each score, improving transparency.
- Designed to integrate with Cargo, using @cargo-ai/cli for enrichment and account management.
- Costs are transparent and sampling is recommended before running on large lists.
- For full GTM flows and advanced features, upgrading to the complete Cargo pack is recommended.

**关键词**: of, score-leads, Score, list, companies, against, ideal, customer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/score-leads)

---

## [17. monitor-buying-signals](https://clawhub.ai/cargo-ai/monitor-buying-signals)

**Slug**: `monitor-buying-signals`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Watch a list of target accounts for the public events that mean someone is in market, powered by Cargo — hiring for the role you sell into, saying something new, or turning up in a detection feed, each with a date and a link. Triggers: "tell me when these accounts do something", "what changed at my target accounts", "who is in market right now", "set up intent monitoring", "watch these companies for me", "any triggers on this list". Intent, triggers, watchlist, timing, freshness. Skip when: you have no account list yet — use build-tam-list; or you want a verdict on fit rather than on timing — use score-leads.

**中文介绍**: Watch a list of target accounts for the public events that mean someone is in market, powered by Cargo — hiring for the role you sell into, saying something new, or turning up in a detection feed, each with a date and a link. Triggers: "tell me when these accounts do something", "what changed at my target accounts", "who is in market right now", "set up intent monitoring", "watch these companies for me", "any triggers on this list". Intent, triggers, watchlist, timing, freshness. Skip when: you have no account list yet — use build-tam-list; or you want a verdict on fit rather than on timing — use score-leads.

Latest changelog:
Initial release: skill to monitor target accounts for buying signals and market intent.

- Detects key public events such as relevant new hires, company posts, and detection feed entries, each with timing and source link.
- Guides setup, free and paid signal checks, and emphasizes separating timing from fit.
- Supports watchlist and trigger-based queries; covers credit costs and usage guidance.
- Requires @cargo-ai/cli (npm) for operation and authentication.
- Includes sample code and best practices to maximize effectiveness and minimize unnecessary runs.

**关键词**: of, monitor-buying-signals, Watch, list, target, accounts, public, events

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/monitor-buying-signals)

---

## [18. research-account](https://clawhub.ai/cargo-ai/research-account)

**Slug**: `research-account`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Research one company before a meeting and hand back a briefing, powered by Cargo — what it does, what it publicly says is hard right now, and who it names as competition, each line traceable to where it came from. Triggers: "research this company", "brief me on this account", "prep me for this meeting", "what should I know about them", "write me a one-pager on", "what are they struggling with", "who do they compete with". Meeting prep, briefing, dossier, talking points. Skip when: you want many companies filtered rather than one understood — use build-tam-list; or you want the people to contact there — use find-stakeholders.

**中文介绍**: Research one company before a meeting and hand back a briefing, powered by Cargo — what it does, what it publicly says is hard right now, and who it names as competition, each line traceable to where it came from. Triggers: "research this company", "brief me on this account", "prep me for this meeting", "what should I know about them", "write me a one-pager on", "what are they struggling with", "who do they compete with". Meeting prep, briefing, dossier, talking points. Skip when: you want many companies filtered rather than one understood — use build-tam-list; or you want the people to contact there — use find-stakeholders.

Latest changelog:
Initial release of research-account: one-company briefing tool

- Generates a traceable, one-page company briefing for meeting prep.
- Gathers information on company profile, current public statements, challenges, competitors, and open roles, each line linked to a source.
- Requires @cargo-ai/cli (npm); setup starts with 100 free credits, no card needed.
- Includes strict discipline: every statement sourced or clearly marked as inferred or unknown.
- Outlines step-by-step command-line usage and cost per action.
- Lists scenarios for use and when to use alternative skills.

**关键词**: research-account, Research, one, company, before, meeting, hand, back

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/research-account)

---

## [19. Smart Baby Cry Analysis Skill | 婴儿哭声智能解析技能](https://clawhub.ai/smyx-sunjinhui/smyx-infant-cry-analysis)

**Slug**: `smyx-infant-cry-analysis`  
**Version**: 1.0.9  
**Stats**: ⭐ 3 | ⬇️ 1239 | 🧩 10

**原始简介**: Detects baby cries via audio AI in real-time, analyzes causes, and precisely identifies needs like hunger, tiredness, pain, discomfort, or irritability to assist new parents. | 婴儿哭声智能解析技能，通过音频AI实时检测婴儿哭声，自动解析哭声成因，精准识别饥饿、困倦、疼痛、身体不适、情绪烦躁等不同需求，辅助新手爸妈科学育婴

**中文介绍**: Detects baby cries via audio AI in real-time, analyzes causes, and precisely identifies needs like hunger, tiredness, pain, discomfort, or irritability to assist new parents. | 婴儿哭声智能解析技能，通过音频AI实时检测婴儿哭声，自动解析哭声成因，精准识别饥饿、困倦、疼痛、身体不适、情绪烦躁等不同需求，辅助新手爸妈科学育婴

Latest changelog:
- Updated skill version to 1.0.13.
- Updated documentation in SKILL.md, including version, minor content, and formatting changes.
- Removed the skill-card.md file.
- Made adjustments in the configuration file (config.yaml).
- No changes to core functionality; housekeeping and doc improvements.

**关键词**: 婴儿哭声智能解析技能, Smart, Baby, Cry, Analysis, Skill, Detects, cries

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-infant-cry-analysis)

---

## [20. ShieldCortex](https://clawhub.ai/jarvis-drakon/shieldcortex)

**Slug**: `shieldcortex`  
**Version**: 4.52.2  
**Stats**: ⭐ 2 | ⬇️ 5892 | 🧩 147

**原始简介**: Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

**中文介绍**: Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

Latest changelog:
Sync from npm publish v4.52.2

**关键词**: Agent, ShieldCortex, Memory, defence, semantic, recall, knowledge, graph

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shieldcortex)

---

## [21. cargo-gtm](https://clawhub.ai/cargo-ai/cargo-gtm)

**Slug**: `cargo-gtm`  
**Version**: 1.15.0  
**Stats**: ⭐ 0 | ⬇️ 1640 | 🧩 16

**原始简介**: Do business-to-business go-to-market work on Cargo — research accounts and buying committees, enrich and verify B2B contact records from licensed data providers, score and qualify leads, draft permission-based outreach for the user's own sequencer, sync to CRM, and monitor buying signals. Consent basis, suppression lists, and volume limits gate every step that touches a person (`references/acceptable-use.md`); bulk unsolicited messaging, purchased or scraped lists, and consumer targeting are refused. Triggers: "build me a list of", "find 50 <title> at <segment>", "who works at", "find work emails for these accounts", "enrich this CSV", "verify these emails", "build a TAM", "who fits our ICP", "who actually buys from us", "what data points should we collect on accounts", "our outbound is reaching the wrong people", "score these leads", "write a first-touch email", "push these to my CRM", "who changed jobs", "who just raised funding", "companies using <tech>", "who is hiring <role>", "find the buying committee", "portfolio companies of <investor>", "upload this audience to Google/Meta/LinkedIn ads". Providers: aiArk, anthropic, apolloio, bouncer, builtwith, cargo, cleon1, companyEnrich, contactOut, datagma, dropcontact, enrichCrm, enrichley, enrowio, exa, findyMail, firecrawl, forager, FullEnrich, g2, gemini, hunter, icypeas, kitt, leadMagic, linkedin, linkup, mixrank, neverBounce, oceanio, openAi, parallel, peopleDataLabs, perplexity, piloterr, prospeo, reverseContact, rocketreach, salesNavigator, serper, sillage, snitcher, societeInfo, theirStack, theSwarm, waterfall, x, zeroBounce. Reads phase guides, recipes, and per-provider playbooks before any paid call. Skip when: a run already happened and misbehaved — use cargo-diagnostics.

**中文介绍**: Do business-to-business go-to-market work on Cargo — research accounts and buying committees, enrich and verify B2B contact records from licensed data providers, score and qualify leads, draft permission-based outreach for the user's own sequencer, sync to CRM, and monitor buying signals. Consent basis, suppression lists, and volume limits gate every step that touches a person (`references/acceptable-use.md`); bulk unsolicited messaging, purchased or scraped lists, and consumer targeting are refused. Triggers: "build me a list of", "find 50 <title> at <segment>", "who works at", "find work emails for these accounts", "enrich this CSV", "verify these emails", "build a TAM", "who fits our ICP", "who actually buys from us", "what data points should we collect on accounts", "our outbound is reaching the wrong people", "score these leads", "write a first-touch email", "push these to my CRM", "who changed jobs", "who just raised funding", "companies using <tech>", "who is hiring <role>", "find the buying committee", "portfolio companies of <investor>", "upload this audience to Google/Meta/LinkedIn ads". Providers: aiArk, anthropic, apolloio, bouncer, builtwith, cargo, cleon1, companyEnrich, contactOut, datagma, dropcontact, enrichCrm, enrichley, enrowio, exa, findyMail, firecrawl, forager, FullEnrich, g2, gemini, hunter, icypeas, kitt, leadMagic, linkedin, linkup, mixrank, neverBounce, oceanio, openAi, parallel, peopleDataLabs, perplexity, piloterr, prospeo, reverseContact, rocketreach, salesNavigator, serper, sillage, snitcher, societeInfo, theirStack, theSwarm, waterfall, x, zeroBounce. Reads phase guides, recipes, and per-provider playbooks before any paid call. Skip when: a run already happened and misbehaved — use cargo-diagnostics.

Latest changelog:
cargo-gtm 1.15.0

- Added five new provider playbooks: builtwith, exa, parallel, sillage, and x.
- Provider list expanded to include builtwith, exa, parallel, sillage, and x.
- Updated documentation and references to reflect new and updated providers.
- Removed deprecated skill-card.md file.
- Improved references and provider mapping in supporting docs.

**关键词**: Do, cargo-gtm, business-to-business, go-to-market, work, Cargo, research, accounts

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cargo-gtm)

---

## [22. code-risk-agent](https://clawhub.ai/a9320/code-risk-agent)

**Slug**: `code-risk-agent`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 16 | 🧩 1

**原始简介**: 当用户需要扫描代码安全漏洞、审计代码、分析 C/Python 风险、检查依赖漏洞、或生成安全报告时触发。支持云端 LLM 语义分析和本地 GPU 回退。

**中文介绍**: 当用户需要扫描代码安全漏洞、审计代码、分析 C/Python 风险、检查依赖漏洞、或生成安全报告时触发。支持云端 LLM 语义分析和本地 GPU 回退。

Latest changelog:
Initial release with advanced code security auditing and vulnerability scanning for C and Python:

- Scans code for vulnerabilities, audits projects, analyzes risk, checks dependencies, and generates security reports.
- Supports both semantic cloud LLM analysis and local GPU fallback.
- Exposes two tools: code scan and CVE lookup.
- Returns structured JSON reports with clear Markdown rendering guidelines for results and recommendations.
- Automatic fallback to pure static analysis if cloud LLM/semgrep unavailable.
- Strict privacy controls and downgrade strategies for environments lacking cloud or database support.

**关键词**: 当用户需要扫描代码安全漏洞、审计代码、分析, 风险、检查依赖漏洞、或生成安全报告时触发, 支持云端, LLM, 语义分析和本地, code-risk-agent, Python, GPU

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/code-risk-agent)

---

## [23. typhoon-tracker](https://clawhub.ai/firefljay/typhoon-tracker)

**Slug**: `typhoon-tracker`  
**Version**: 1.1.2  
**Stats**: ⭐ 0 | ⬇️ 217 | 🧩 4

**原始简介**: 台风实时追踪与影响研判。当用户询问台风路径、登陆预测、风雨影响、出行安全、交通停运、活动能否举办等问题时加载；当用户询问航班/高铁/交通出行与行程规划时也**必须加载**——即使未明确提及台风，也要排查台风及其残余环流、冷空气等系统性天气背景对交通的影响（避免仅看当日天气预报导致误判，如台风残涡'回马枪'）。覆盖数据源体系、预测变化规律、影响评估公式、报告模板和决策框架。适用于西北太平洋台风逼近华东沿海及残涡滞留影响的场景。

**中文介绍**: 台风实时追踪与影响研判。当用户询问台风路径、登陆预测、风雨影响、出行安全、交通停运、活动能否举办等问题时加载；当用户询问航班/高铁/交通出行与行程规划时也**必须加载**——即使未明确提及台风，也要排查台风及其残余环流、冷空气等系统性天气背景对交通的影响（避免仅看当日天气预报导致误判，如台风残涡'回马枪'）。覆盖数据源体系、预测变化规律、影响评估公式、报告模板和决策框架。适用于西北太平洋台风逼近华东沿海及残涡滞留影响的场景。

Latest changelog:
v1.1.2: 触发条件重构+用户信息验证协议+航旅纵横P1信源

**关键词**: 台风实时追踪与影响研判, 当用户询问航班, 高铁, 交通出行与行程规划时也, 必须加载, ——即使未明确提及台风, 如台风残涡'回马枪'）, typhoon-tracker

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/typhoon-tracker)

---

## [24. Image Quality Assessment Analysis Tool | 图像质量检测分析工具](https://clawhub.ai/smyx-sunjinhui/smyx-image-quality-detection-analysis)

**Slug**: `smyx-image-quality-detection-analysis`  
**Version**: 1.0.9  
**Stats**: ⭐ 4 | ⬇️ 1283 | 🧩 10

**原始简介**: Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness. Suitable for security surveillance and camera self-check scenarios. | 图像质量检测分析工具，检测摄像头画面出现的全黑、全白、偏色、条纹、雪花、模糊等质量问题，适用于安防监控、摄像头自检等场景

**中文介绍**: Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness. Suitable for security surveillance and camera self-check scenarios. | 图像质量检测分析工具，检测摄像头画面出现的全黑、全白、偏色、条纹、雪花、模糊等质量问题，适用于安防监控、摄像头自检等场景

Latest changelog:
- Updated version to 1.0.10.
- Revised configuration file(s) and documentation.
- Removed obsolete skill-card.md file.
- No changes to core analysis functionality; documentation and config streamlined.

**关键词**: 图像质量检测分析工具, Image, Quality, Assessment, Analysis, Tool, Detects, issues

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-image-quality-detection-analysis)

---

## [25. 全平台内容同步发布引擎](https://clawhub.ai/mikogeyu-cell/omnipub-content-engine)

**Slug**: `omnipub-content-engine`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 19 | 🧩 1

**原始简介**: AI驱动的全平台内容生命周期管理，从选题、生成、查证到发布和复盘，实现公众号与今日头条同步优化发布。

**中文介绍**: AI驱动的全平台内容生命周期管理，从选题、生成、查证到发布和复盘，实现公众号与今日头条同步优化发布。

Latest changelog:
首次发布。10阶段闭环工作流，12个CLI命令，3套主题，9篇方法论文档，端到端测试全部通过。

**关键词**: 全平台内容同步发布引擎, AI驱动的全平台内容生命周期管理, 从选题、生成、查证到发布和复盘, 实现公众号与今日头条同步优化发布, 首次发布, 10阶段闭环工作流, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/omnipub-content-engine)

---

