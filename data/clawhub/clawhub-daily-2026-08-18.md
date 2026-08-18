# ClawHub Skills Daily | 2026-08-18

> 共 25 个 skills

## [1. Pixmind WeChat Creator](https://clawhub.ai/fuyunzhishang/pixmind-wechat-creator)

**Slug**: `pixmind-wechat-creator`  
**Version**: 0.3.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Create formatted WeChat articles for rich-text copy

**中文介绍**: Create formatted WeChat articles for rich-text copy

Latest changelog:
Use Pixmind Builder provider credentials through the secure content bridge; remove the Builder environment-variable requirement.

**关键词**: Pixmind, WeChat, Creator, formatted, articles, rich-text, copy, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pixmind-wechat-creator)

---

## [2. 视频翻译配音 Video Translate & Dub](https://clawhub.ai/dlazyai/dlazy-video-translate)

**Slug**: `dlazy-video-translate`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: video translation, video dubbing, subtitle translation, translate video to Chinese, add subtitles to video, AI dubbing, srt translation, 视频翻译, 视频配音, 字幕翻译 — transcribes a video with word-level timings, translates the subtitles, then burns them in and optionally lays down a fitted dub track. Composes the dlazy fun-asr, LLM and TTS tools with ffmpeg locally; delivers a finished mp4 plus srt files, not a script.

**中文介绍**: video translation, video dubbing, subtitle translation, translate video to Chinese, add subtitles to video, AI dubbing, srt translation, 视频翻译, 视频配音, 字幕翻译 — transcribes a video with word-level timings, translates the subtitles, then burns them in and optionally lays down a fitted dub track. Composes the dlazy fun-asr, LLM and TTS tools with ffmpeg locally; delivers a finished mp4 plus srt files, not a script.

Latest changelog:
Document the per-model TTS prompt cap (qwen-tts 512 chars)

**关键词**: 视频翻译配音, Video, Translate, Dub, translation, dubbing, subtitle, Chinese

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dlazy-video-translate)

---

## [3. Openclaw Memory Toolkit](https://clawhub.ai/mistermijarvis/memory-toolkit)

**Slug**: `memory-toolkit`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 63 | 🧩 4

**原始简介**: Hybrid memory pipeline for OpenClaw agents — extraction, archiving, temporal decay scoring, consolidation, and hybrid search (FTS5 + sqlite-vec + RRF). Six standalone Python scripts, local-first, zero external API dependencies. The only memory skill on ClawHub with R

**中文介绍**: Hybrid memory pipeline for OpenClaw agents — extraction, archiving, temporal decay scoring, consolidation, and hybrid search (FTS5 + sqlite-vec + RRF). Six standalone Python scripts, local-first, zero external API dependencies. The only memory skill on ClawHub with R

Latest changelog:
• OLLAMA_EMBED_URL dérivé depuis OLLAMA_URL (plus hardcodé) — consent warnings affichent la vraie destination
• check_ollama_url() valide les deux variables
• run_tests.py : snippets de contenu retirés (metadata seulement)
• "Safe by default" corrigé dans README + SKILL

**关键词**: Agent, Openclaw, Memory, Toolkit, Hybrid, pipeline, extraction, archiving

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memory-toolkit)

---

## [4. zoom-meeting-admin](https://clawhub.ai/mebusw/zoom-meeting-admin)

**Slug**: `zoom-meeting-admin`  
**Version**: 1.0.5  
**Stats**: ⭐ 1 | ⬇️ 916 | 🧩 6

**原始简介**: Manage Zoom meetings, cloud recordings, and account users via a Server-to-Server OAuth REST script. Use this skill when the user wants to list, view, create, or delete a scheduled Zoom meeting; query cloud recordings for a user; or look up account users. The script exposes a fixed CLI action whitelist (list/get/create/delete meeting, get/list user, list recordings); agents must only invoke these documented actions and must not modify the script, import internal functions, or construct arbitrary Zoom API requests. create_meeting requires the agent to obtain explicit user confirmation of topic, start_time, and duration before invoking. delete_meeting is gated by a required --yes flag and the agent must display the meeting info and obtain explicit user confirmation before invoking. Requires a Zoom Server-to-Server OAuth app and a local .env with ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET, USER_ID.

**中文介绍**: Manage Zoom meetings, cloud recordings, and account users via a Server-to-Server OAuth REST script. Use this skill when the user wants to list, view, create, or delete a scheduled Zoom meeting; query cloud recordings for a user; or look up account users. The script exposes a fixed CLI action whitelist (list/get/create/delete meeting, get/list user, list recordings); agents must only invoke these documented actions and must not modify the script, import internal functions, or construct arbitrary Zoom API requests. create_meeting requires the agent to obtain explicit user confirmation of topic, start_time, and duration before invoking. delete_meeting is gated by a required --yes flag and the agent must display the meeting info and obtain explicit user confirmation before invoking. Requires a Zoom Server-to-Server OAuth app and a local .env with ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET, USER_ID.

Latest changelog:
zoom-meeting-admin 1.0.5

- Strengthened security documentation and clarified over-permission boundaries; agents are now explicitly prohibited from importing internal functions, modifying the script, or calling arbitrary Zoom API endpoints.
- Enhanced SKILL.md with detailed warnings and examples about Zoom recurrence parameters, especially clarifying Zoom weekday encoding (1=Sunday).
- Updated CLI usage section with correct positional parameters for recurring meetings and new reference examples for monthly recurrences.
- Improved .gitignore and README files for consistency and reinforced credential file handling precautions.
- Removed obsolete skill-card.md file.

**关键词**: zoom-meeting-admin, Manage, Zoom, meetings, cloud, recordings, account, users

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zoom-meeting-admin)

---

## [5. 商机雷达-比招标更早发现机会](https://clawhub.ai/zhiliaobiaoxun/zhiliao-opportunity-radar)

**Slug**: `zhiliao-opportunity-radar`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 307 | 🧩 3

**原始简介**: 商机雷达（知了标讯官方）——比招标更早发现机会。当用户想主动挖掘商机/销售线索/潜在客户时，必须使用此SKILL：找商机、找线索、客户开发、市场机会、渠道拓展、拟建项目（立项/审批阶段，提前6-18个月）、采购意向（发标前1-3个月）、即将招标、临期项目/续约机会（现供应商合同到期）、跟踪项目进展阶段。给一个行业/产品/地区，三路早期商机一网打尽并按价值排序。即使用户没有提到「商机」，只要涉及找项目线索、挖潜在客户、提前发现招标机会等需求，都应使用本SKILL。

**中文介绍**: 商机雷达（知了标讯官方）——比招标更早发现机会。当用户想主动挖掘商机/销售线索/潜在客户时，必须使用此SKILL：找商机、找线索、客户开发、市场机会、渠道拓展、拟建项目（立项/审批阶段，提前6-18个月）、采购意向（发标前1-3个月）、即将招标、临期项目/续约机会（现供应商合同到期）、跟踪项目进展阶段。给一个行业/产品/地区，三路早期商机一网打尽并按价值排序。即使用户没有提到「商机」，只要涉及找项目线索、挖潜在客户、提前发现招标机会等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 商机雷达-比招标更早发现机会, 商机雷达（知了标讯官方）——比招标更早发现机会, 当用户想主动挖掘商机, 销售线索, 潜在客户时, 必须使用此SKILL, 审批阶段, 续约机会（现供应商合同到期）、跟踪项目进展阶段

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zhiliao-opportunity-radar)

---

## [6. 招标商机发现-还没发标先知道](https://clawhub.ai/dragonzu/tender-opportunity-finder)

**Slug**: `tender-opportunity-finder`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 419 | 🧩 4

**原始简介**: 招标商机发现助手。当用户想主动挖掘商机/销售线索/潜在客户时，必须使用此SKILL：找商机、找线索、客户开发、市场机会、渠道拓展、拟建项目（立项/审批阶段，提前6-18个月）、采购意向（发标前1-3个月）、即将招标、临期项目/续约机会（现供应商合同到期）、跟踪项目进展阶段。给一个行业/产品/地区，三路早期商机一网打尽并按价值排序输出商机清单。即使用户没有提到「商机」，只要涉及找项目线索、挖潜在客户、提前发现招标机会等需求，都应使用本SKILL。

**中文介绍**: 招标商机发现助手。当用户想主动挖掘商机/销售线索/潜在客户时，必须使用此SKILL：找商机、找线索、客户开发、市场机会、渠道拓展、拟建项目（立项/审批阶段，提前6-18个月）、采购意向（发标前1-3个月）、即将招标、临期项目/续约机会（现供应商合同到期）、跟踪项目进展阶段。给一个行业/产品/地区，三路早期商机一网打尽并按价值排序输出商机清单。即使用户没有提到「商机」，只要涉及找项目线索、挖潜在客户、提前发现招标机会等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 招标商机发现-还没发标先知道, 招标商机发现助手, 当用户想主动挖掘商机, 销售线索, 潜在客户时, 必须使用此SKILL, 审批阶段, 续约机会（现供应商合同到期）、跟踪项目进展阶段

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tender-opportunity-finder)

---

## [7. 拟建项目跟踪-立项审批阶段就发现](https://clawhub.ai/dragonzu/proposed-project-tracker)

**Slug**: `proposed-project-tracker`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 413 | 🧩 4

**原始简介**: 拟建项目跟踪与早期商机发现助手。当用户想查询拟建项目、在建工程立项信息或挖掘早期商机时，必须使用此SKILL：拟建项目查询（发改立项/审批公示阶段，提前6-18个月）、审批状态筛选（未审批/审批中/办结）、立项单位跟进、项目进展跟踪（是否进入招标）、以及配套的采购意向与临期续约商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「拟建」，只要涉及立项项目查询、还没招标的项目、早期项目线索等需求，都应使用本SKILL。

**中文介绍**: 拟建项目跟踪与早期商机发现助手。当用户想查询拟建项目、在建工程立项信息或挖掘早期商机时，必须使用此SKILL：拟建项目查询（发改立项/审批公示阶段，提前6-18个月）、审批状态筛选（未审批/审批中/办结）、立项单位跟进、项目进展跟踪（是否进入招标）、以及配套的采购意向与临期续约商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「拟建」，只要涉及立项项目查询、还没招标的项目、早期项目线索等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 拟建项目跟踪-立项审批阶段就发现, 拟建项目跟踪与早期商机发现助手, 必须使用此SKILL, 拟建项目查询（发改立项, 审批公示阶段, 提前6-18个月）、审批状态筛选（未审批, 审批中, 给一个行业

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/proposed-project-tracker)

---

## [8. 采购意向监控-发标前1-3个月对接](https://clawhub.ai/dragonzu/procurement-intent-monitor)

**Slug**: `procurement-intent-monitor`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 400 | 🧩 4

**原始简介**: 采购意向监控与早期商机发现助手。当用户想查询采购意向、政府采购计划或挖掘即将招标的机会时，必须使用此SKILL：采购意向查询（发标前1-3个月的公开采购计划）、按行业/地区/预算筛选、意向到发标的进展跟踪、每日/每周增量监控（商机晨报）、以及配套的拟建项目与临期续约商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「采购意向」，只要涉及即将招标的项目、提前对接采购人、快发标的机会等需求，都应使用本SKILL。

**中文介绍**: 采购意向监控与早期商机发现助手。当用户想查询采购意向、政府采购计划或挖掘即将招标的机会时，必须使用此SKILL：采购意向查询（发标前1-3个月的公开采购计划）、按行业/地区/预算筛选、意向到发标的进展跟踪、每日/每周增量监控（商机晨报）、以及配套的拟建项目与临期续约商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「采购意向」，只要涉及即将招标的项目、提前对接采购人、快发标的机会等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 采购意向监控-发标前1-3个月对接, 采购意向监控与早期商机发现助手, 必须使用此SKILL, 地区, 预算筛选、意向到发标的进展跟踪、每日, 给一个行业, 地区即输出按价值排序的商机清单, 即使用户没有提到「采购意向」

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/procurement-intent-monitor)

---

## [9. 医疗设备商机雷达-医院采购早期发现](https://clawhub.ai/dragonzu/medical-equipment-opportunity-radar)

**Slug**: `medical-equipment-opportunity-radar`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 416 | 🧩 4

**原始简介**: 医疗设备商机雷达。当用户想挖掘医疗行业早期商机（医疗设备/器械/耗材/检验试剂/医院信息化等）时，必须使用此SKILL：医院新建改扩建拟建项目（设备采购的最上游信号，提前6-18个月）、卫健系统采购意向（发标前1-3个月）、设备维保与服务临期续约、按预算与紧急度排序、采购单位跟进建议。给一个产品线/地区即输出按价值排序的商机清单。即使用户没有提到「医疗」，只要涉及医院采购线索、设备销售商机、卫健项目早期发现等需求，都应使用本SKILL。

**中文介绍**: 医疗设备商机雷达。当用户想挖掘医疗行业早期商机（医疗设备/器械/耗材/检验试剂/医院信息化等）时，必须使用此SKILL：医院新建改扩建拟建项目（设备采购的最上游信号，提前6-18个月）、卫健系统采购意向（发标前1-3个月）、设备维保与服务临期续约、按预算与紧急度排序、采购单位跟进建议。给一个产品线/地区即输出按价值排序的商机清单。即使用户没有提到「医疗」，只要涉及医院采购线索、设备销售商机、卫健项目早期发现等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 医疗设备商机雷达-医院采购早期发现, 医疗设备商机雷达, 当用户想挖掘医疗行业早期商机（医疗设备, 器械, 耗材, 检验试剂, 医院信息化等）时, 必须使用此SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/medical-equipment-opportunity-radar)

---

## [10. IT信息化商机雷达-信创项目早期发现](https://clawhub.ai/dragonzu/it-project-opportunity-radar)

**Slug**: `it-project-opportunity-radar`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 396 | 🧩 4

**原始简介**: IT信息化商机雷达。当用户想挖掘IT行业早期商机（信创/国产化/软件开发/系统集成/云/数据中心/网络安全/智慧城市等）时，必须使用此SKILL：数字化拟建项目查询（智慧城市/数字政府立项阶段，提前6-18个月）、IT采购意向（发标前1-3个月）、运维与软件服务临期续约（IT服务续约窗口价值高）、按预算与紧急度排序、甲方单位跟进建议。给一个技术领域/地区即输出按价值排序的商机清单。即使用户没有提到「IT」，只要涉及信息化项目线索、信创商机、数字化项目早期发现等需求，都应使用本SKILL。

**中文介绍**: IT信息化商机雷达。当用户想挖掘IT行业早期商机（信创/国产化/软件开发/系统集成/云/数据中心/网络安全/智慧城市等）时，必须使用此SKILL：数字化拟建项目查询（智慧城市/数字政府立项阶段，提前6-18个月）、IT采购意向（发标前1-3个月）、运维与软件服务临期续约（IT服务续约窗口价值高）、按预算与紧急度排序、甲方单位跟进建议。给一个技术领域/地区即输出按价值排序的商机清单。即使用户没有提到「IT」，只要涉及信息化项目线索、信创商机、数字化项目早期发现等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: IT信息化商机雷达-信创项目早期发现, IT信息化商机雷达, 当用户想挖掘IT行业早期商机（信创, 国产化, 软件开发, 系统集成, 数据中心, 网络安全

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/it-project-opportunity-radar)

---

## [11. 临期续约商机-合同到期窗口挖掘](https://clawhub.ai/dragonzu/expiring-contract-renewal-finder)

**Slug**: `expiring-contract-renewal-finder`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 417 | 🧩 4

**原始简介**: 临期项目与续约商机发现助手。当用户想查询即将到期的项目合同、寻找续约/替换机会时，必须使用此SKILL：临期项目查询（合同到期前0-180天）、现供应商（在位者）识别、到期紧急度排序、按采购单位类型（政府/学校/医院/国企等）筛选、以及配套的拟建项目与采购意向商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「临期」，只要涉及合同快到期的项目、续约机会、替换现供应商等需求，都应使用本SKILL。

**中文介绍**: 临期项目与续约商机发现助手。当用户想查询即将到期的项目合同、寻找续约/替换机会时，必须使用此SKILL：临期项目查询（合同到期前0-180天）、现供应商（在位者）识别、到期紧急度排序、按采购单位类型（政府/学校/医院/国企等）筛选、以及配套的拟建项目与采购意向商机扫描。给一个行业/地区即输出按价值排序的商机清单。即使用户没有提到「临期」，只要涉及合同快到期的项目、续约机会、替换现供应商等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 临期续约商机-合同到期窗口挖掘, 临期项目与续约商机发现助手, 当用户想查询即将到期的项目合同、寻找续约, 替换机会时, 必须使用此SKILL, 学校, 医院, 给一个行业

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/expiring-contract-renewal-finder)

---

## [12. 建筑工程商机雷达-基建项目早期发现](https://clawhub.ai/dragonzu/construction-project-opportunity-radar)

**Slug**: `construction-project-opportunity-radar`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 424 | 🧩 4

**原始简介**: 建筑工程商机雷达。当用户想挖掘工程类早期商机（施工/市政/装修/园林/公路/房建/基建等）时，必须使用此SKILL：工程拟建项目查询（发改立项/审批阶段，提前6-18个月，基建类覆盖最全）、工程采购意向（发标前1-3个月）、工程服务临期续约、按投资额与审批进度排序、立项单位跟进建议。给一个工程领域/地区即输出按价值排序的商机清单。即使用户没有提到「建筑」，只要涉及工程项目线索、基建商机、施工项目早期发现等需求，都应使用本SKILL。

**中文介绍**: 建筑工程商机雷达。当用户想挖掘工程类早期商机（施工/市政/装修/园林/公路/房建/基建等）时，必须使用此SKILL：工程拟建项目查询（发改立项/审批阶段，提前6-18个月，基建类覆盖最全）、工程采购意向（发标前1-3个月）、工程服务临期续约、按投资额与审批进度排序、立项单位跟进建议。给一个工程领域/地区即输出按价值排序的商机清单。即使用户没有提到「建筑」，只要涉及工程项目线索、基建商机、施工项目早期发现等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 建筑工程商机雷达-基建项目早期发现, 建筑工程商机雷达, 当用户想挖掘工程类早期商机（施工, 市政, 装修, 园林, 公路, 房建

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/construction-project-opportunity-radar)

---

## [13. AI销售线索雷达-政企销售找客户](https://clawhub.ai/dragonzu/ai-sales-lead-radar)

**Slug**: `ai-sales-lead-radar`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 391 | 🧩 4

**原始简介**: AI销售线索雷达。当政企销售/BD/渠道人员想找销售线索、开发客户时，必须使用此SKILL：销售线索挖掘、潜在客户发现、拟建项目（提前6-18个月布局）、采购意向（发标前1-3个月对接）、临期续约（替换现供应商）、线索按金额与紧急度排序、每日商机晨报订阅。给一个行业/产品/地区即输出按价值排序的线索清单。即使用户没有提到「线索」，只要涉及找客户、开发市场、挖商机、谁会买我们产品等需求，都应使用本SKILL。

**中文介绍**: AI销售线索雷达。当政企销售/BD/渠道人员想找销售线索、开发客户时，必须使用此SKILL：销售线索挖掘、潜在客户发现、拟建项目（提前6-18个月布局）、采购意向（发标前1-3个月对接）、临期续约（替换现供应商）、线索按金额与紧急度排序、每日商机晨报订阅。给一个行业/产品/地区即输出按价值排序的线索清单。即使用户没有提到「线索」，只要涉及找客户、开发市场、挖商机、谁会买我们产品等需求，都应使用本SKILL。

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: AI销售线索雷达-政企销售找客户, AI销售线索雷达, 当政企销售, BD, 渠道人员想找销售线索、开发客户时, 必须使用此SKILL, 给一个行业, 地区即输出按价值排序的线索清单

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-sales-lead-radar)

---

## [14. 企业情报-招投标视角的企业背调](https://clawhub.ai/zhiliaobiaoxun/zhiliao-company-intel)

**Slug**: `zhiliao-company-intel`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 309 | 🧩 3

**原始简介**: 企业情报/背景调查助手。当用户给出一个公司主体（公司名/简称/公司链接），并希望进行企业背调、企业画像、竞争对手分析、供应商资质与履约能力审查、客户背景调查、轻尽调（"这家公司实力怎么样/靠不靠谱/中过什么标"）时，必须使用此SKILL。基于全网招投标数据输出招投标视角的企业情报报告（附可分享的本地HTML版）：竞对是从投标重叠算出来的、实力是中标记录证明的、客户供应商是真实合同关系。支持单公司深度报告与双公司对比两种模式。首次使用经用户同意后可自动开通免费试用账号。注意边界（锚点＝输入物是"项目"还是"公司"）：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zlbx-bid-dec

**中文介绍**: 企业情报/背景调查助手。当用户给出一个公司主体（公司名/简称/公司链接），并希望进行企业背调、企业画像、竞争对手分析、供应商资质与履约能力审查、客户背景调查、轻尽调（"这家公司实力怎么样/靠不靠谱/中过什么标"）时，必须使用此SKILL。基于全网招投标数据输出招投标视角的企业情报报告（附可分享的本地HTML版）：竞对是从投标重叠算出来的、实力是中标记录证明的、客户供应商是真实合同关系。支持单公司深度报告与双公司对比两种模式。首次使用经用户同意后可自动开通免费试用账号。注意边界（锚点＝输入物是"项目"还是"公司"）：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zlbx-bid-dec

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 企业情报-招投标视角的企业背调, 企业情报, 背景调查助手, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 靠不靠谱, 中过什么标"）时

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zhiliao-company-intel)

---

## [15. 供应商资质核查-履约能力一查便知](https://clawhub.ai/zhiliaobiaoxun/supplier-qualification-checker)

**Slug**: `supplier-qualification-checker`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 334 | 🧩 3

**原始简介**: 供应商资质与履约能力核查助手。当用户（采购方/招标人/总包/甲方）给出一个公司主体，想审查供应商资质、评估履约能力、核验业绩真实性时，必须使用此SKILL：供应商审查、供应商准入核查、履约能力评估、业绩核验（自称做过的项目是否真的中过标）、分包商考察、投标单位背景核查、同类项目经验盘点、大客户与合作历史、公开涉诉与行政处罚排查。基于全网招投标数据输出报告：履约实力用中标记录证明、合作关系是真实合同关系、风险信息逐条附来源。支持单公司深度报告与两家候选供应商对比。即使用户没有提到「资质」，只要想核实一家供应商/合作方的真实履约能力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该

**中文介绍**: 供应商资质与履约能力核查助手。当用户（采购方/招标人/总包/甲方）给出一个公司主体，想审查供应商资质、评估履约能力、核验业绩真实性时，必须使用此SKILL：供应商审查、供应商准入核查、履约能力评估、业绩核验（自称做过的项目是否真的中过标）、分包商考察、投标单位背景核查、同类项目经验盘点、大客户与合作历史、公开涉诉与行政处罚排查。基于全网招投标数据输出报告：履约实力用中标记录证明、合作关系是真实合同关系、风险信息逐条附来源。支持单公司深度报告与两家候选供应商对比。即使用户没有提到「资质」，只要想核实一家供应商/合作方的真实履约能力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 供应商资质核查-履约能力一查便知, 供应商资质与履约能力核查助手, 当用户（采购方, 招标人, 总包, 甲方）给出一个公司主体, 想审查供应商资质、评估履约能力、核验业绩真实性时, 必须使用此SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/supplier-qualification-checker)

---

## [16. 竞对情报分析-投标对手底细摸排](https://clawhub.ai/zhiliaobiaoxun/competitor-intel-analysis)

**Slug**: `competitor-intel-analysis`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 331 | 🧩 3

**原始简介**: 竞争对手情报分析助手（投标方视角）。当用户给出一个公司主体，想分析竞争对手、摸清投标对手底细时，必须使用此SKILL：竞对分析、竞争对手调查、对手中标实力评估、竞对主战场与强势品类、竞对大客户识别、投标交锋记录（在什么品类/地区/客户上碰面）、自家与竞对双公司对比、竞对动态周报监控。基于全网招投标数据输出报告：竞对从投标重叠算出、实力用中标记录证明、客户关系是真实合同关系。支持单公司深度报告与双公司对比两种模式。即使用户没有提到「竞对」，只要想搞清楚投标场上某个对手的实力、地盘与打法，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zlbx-bid-de

**中文介绍**: 竞争对手情报分析助手（投标方视角）。当用户给出一个公司主体，想分析竞争对手、摸清投标对手底细时，必须使用此SKILL：竞对分析、竞争对手调查、对手中标实力评估、竞对主战场与强势品类、竞对大客户识别、投标交锋记录（在什么品类/地区/客户上碰面）、自家与竞对双公司对比、竞对动态周报监控。基于全网招投标数据输出报告：竞对从投标重叠算出、实力用中标记录证明、客户关系是真实合同关系。支持单公司深度报告与双公司对比两种模式。即使用户没有提到「竞对」，只要想搞清楚投标场上某个对手的实力、地盘与打法，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zlbx-bid-de

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 竞对情报分析-投标对手底细摸排, 竞争对手情报分析助手（投标方视角）, 当用户给出一个公司主体, 想分析竞争对手、摸清投标对手底细时, 必须使用此SKILL, 地区, 基于全网招投标数据输出报告, 支持单公司深度报告与双公司对比两种模式

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/competitor-intel-analysis)

---

## [17. 招投标尽调助手-合同流水看经营实态](https://clawhub.ai/zhiliaobiaoxun/bidding-due-diligence)

**Slug**: `bidding-due-diligence`  
**Version**: 1.0.2  
**Stats**: ⭐ 1 | ⬇️ 344 | 🧩 3

**原始简介**: 招投标尽职调查助手（投资/合作/并购前的轻尽调）。当用户给出一个公司主体，想在投资、并购、合作、签约前做尽职调查、核实经营实态时，必须使用此SKILL：企业尽调、轻尽调、投资标的初筛、经营实态核验（中标合同流水是否活跃）、订单走势分析（逐年增长还是萎缩）、客户结构与大客户依赖度、履约能力评估、公开涉诉与行政处罚检索。基于全网招投标数据输出报告：经营实态用真实发生的中标合同流水说话、客户关系是真实合同关系、风险信息逐条附来源链接。支持单公司深度报告与双公司对比。即使用户没有提到「尽调」，只要想在投钱或合作前搞清楚一家公司的真实经营状况，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目

**中文介绍**: 招投标尽职调查助手（投资/合作/并购前的轻尽调）。当用户给出一个公司主体，想在投资、并购、合作、签约前做尽职调查、核实经营实态时，必须使用此SKILL：企业尽调、轻尽调、投资标的初筛、经营实态核验（中标合同流水是否活跃）、订单走势分析（逐年增长还是萎缩）、客户结构与大客户依赖度、履约能力评估、公开涉诉与行政处罚检索。基于全网招投标数据输出报告：经营实态用真实发生的中标合同流水说话、客户关系是真实合同关系、风险信息逐条附来源链接。支持单公司深度报告与双公司对比。即使用户没有提到「尽调」，只要想在投钱或合作前搞清楚一家公司的真实经营状况，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 招投标尽调助手-合同流水看经营实态, 招投标尽职调查助手（投资, 合作, 并购前的轻尽调）, 当用户给出一个公司主体, 必须使用此SKILL, 基于全网招投标数据输出报告, 支持单公司深度报告与双公司对比

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bidding-due-diligence)

---

## [18. 企业背调助手-给个公司名出份报告](https://clawhub.ai/zhiliaobiaoxun/company-background-check)

**Slug**: `company-background-check`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 330 | 🧩 3

**原始简介**: 企业背调助手。当用户给出一个公司主体（公司名/简称/公司链接），想做企业背景调查、背调、查公司底细时，必须使用此SKILL：企业背调、公司背景调查、企业画像、轻尽调（这家公司实力怎么样/靠不靠谱/中过什么标）、客户背景核验、合作方审查、竞争对手识别、供应商履约能力评估、公开风险检索。基于全网招投标数据输出招投标视角的背调报告：竞对是从投标重叠算出来的、实力是中标记录证明的、客户供应商是真实合同关系。支持单公司深度报告与双公司对比两种模式。即使用户没有提到「背调」，只要想搞清楚一家公司的业务、实力与风险，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zl

**中文介绍**: 企业背调助手。当用户给出一个公司主体（公司名/简称/公司链接），想做企业背景调查、背调、查公司底细时，必须使用此SKILL：企业背调、公司背景调查、企业画像、轻尽调（这家公司实力怎么样/靠不靠谱/中过什么标）、客户背景核验、合作方审查、竞争对手识别、供应商履约能力评估、公开风险检索。基于全网招投标数据输出招投标视角的背调报告：竞对是从投标重叠算出来的、实力是中标记录证明的、客户供应商是真实合同关系。支持单公司深度报告与双公司对比两种模式。即使用户没有提到「背调」，只要想搞清楚一家公司的业务、实力与风险，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析，使用 zl

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 企业背调助手-给个公司名出份报告, 企业背调助手, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 想做企业背景调查、背调、查公司底细时, 必须使用此SKILL, 靠不靠谱

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/company-background-check)

---

## [19. 企业中标履历查询-业绩与履约记录](https://clawhub.ai/zhiliaobiaoxun/bid-winner-company-profile)

**Slug**: `bid-winner-company-profile`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 330 | 🧩 3

**原始简介**: 企业中标履历与业绩查询助手。当用户给出一个公司主体（公司名/简称/公司链接），想查中标履历、中标记录、业绩证明、履约记录时，必须使用此SKILL：某公司中过什么标、中标数量与总金额、逐年中标走势、中标地区分布、标王项目盘点（附公告原文链接）、同类业绩核验（投标材料业绩真伪）、资质申报业绩梳理、供应商履约记录审查，以及配套的企业画像、客户供应商生态、竞争格局与公开风险全景背调。基于全网招投标数据输出报告，每条业绩可追溯到公告原文。支持单公司深度报告与双公司对比。即使用户没有提到「履历」，只要想用中标记录核实一家公司的业绩与履约能力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该

**中文介绍**: 企业中标履历与业绩查询助手。当用户给出一个公司主体（公司名/简称/公司链接），想查中标履历、中标记录、业绩证明、履约记录时，必须使用此SKILL：某公司中过什么标、中标数量与总金额、逐年中标走势、中标地区分布、标王项目盘点（附公告原文链接）、同类业绩核验（投标材料业绩真伪）、资质申报业绩梳理、供应商履约记录审查，以及配套的企业画像、客户供应商生态、竞争格局与公开风险全景背调。基于全网招投标数据输出报告，每条业绩可追溯到公告原文。支持单公司深度报告与双公司对比。即使用户没有提到「履历」，只要想用中标记录核实一家公司的业绩与履约能力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 企业中标履历查询-业绩与履约记录, 企业中标履历与业绩查询助手, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 想查中标履历、中标记录、业绩证明、履约记录时, 必须使用此SKILL, 基于全网招投标数据输出报告

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bid-winner-company-profile)

---

## [20. 水滴信用企业尽调-合作前的轻尽调](https://clawhub.ai/dragonzu/enterprise-due-diligence-shuidixinyong)

**Slug**: `enterprise-due-diligence-shuidixinyong`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 348 | 🧩 4

**原始简介**: 企业尽职调查助手（招投标视角轻尽调，习惯用水滴信用等平台看企业信用的用户适用）。当用户给出一个公司主体，想在合作/签约/账期决策前做尽职调查、信用了解、风险排查时，必须使用此SKILL：企业尽调、轻尽调、合作方审查、客户背景调查、经营实态核验（是否真实有业务）、履约能力评估、大客户依赖度分析、公开涉诉与行政处罚检索。基于全网招投标数据输出报告：经营活跃度用中标记录证明、客户供应商是真实合同关系、竞对从投标重叠算出，公开风险逐条附来源链接。支持单公司深度报告与双公司对比。即使用户没有提到「尽调」，只要想在合作前搞清楚一家公司靠不靠谱、有没有真实业务，都应使用本SKILL。注意边界：若用户给出一个

**中文介绍**: 企业尽职调查助手（招投标视角轻尽调，习惯用水滴信用等平台看企业信用的用户适用）。当用户给出一个公司主体，想在合作/签约/账期决策前做尽职调查、信用了解、风险排查时，必须使用此SKILL：企业尽调、轻尽调、合作方审查、客户背景调查、经营实态核验（是否真实有业务）、履约能力评估、大客户依赖度分析、公开涉诉与行政处罚检索。基于全网招投标数据输出报告：经营活跃度用中标记录证明、客户供应商是真实合同关系、竞对从投标重叠算出，公开风险逐条附来源链接。支持单公司深度报告与双公司对比。即使用户没有提到「尽调」，只要想在合作前搞清楚一家公司靠不靠谱、有没有真实业务，都应使用本SKILL。注意边界：若用户给出一个

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 水滴信用企业尽调-合作前的轻尽调, 企业尽职调查助手（招投标视角轻尽调, 习惯用水滴信用等平台看企业信用的用户适用）, 当用户给出一个公司主体, 想在合作, 签约, 账期决策前做尽职调查、信用了解、风险排查时, 必须使用此SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/enterprise-due-diligence-shuidixinyong)

---

## [21. 爱企查企业情报-招投标实力视角查企业](https://clawhub.ai/dragonzu/company-profile-aiqicha)

**Slug**: `company-profile-aiqicha`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 325 | 🧩 3

**原始简介**: 企业情报与实力画像助手（招投标视角，习惯用爱企查等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想查企业情报、企业画像、了解一家公司的真实实力时，必须使用此SKILL：企业信息查询、主营业务分析、中标实力与逐年走势、地区盘面、客户与供应商合同关系、竞争对手识别、公开风险检索。基于全网招投标数据出报告：实力用中标记录证明、竞对从投标重叠算出、客户供应商是真实合同关系——这是工商信息类平台查不到的。支持单公司深度报告与双公司对比。即使用户没有提到「情报」，只要想看清一家公司的真实业务与实力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析

**中文介绍**: 企业情报与实力画像助手（招投标视角，习惯用爱企查等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想查企业情报、企业画像、了解一家公司的真实实力时，必须使用此SKILL：企业信息查询、主营业务分析、中标实力与逐年走势、地区盘面、客户与供应商合同关系、竞争对手识别、公开风险检索。基于全网招投标数据出报告：实力用中标记录证明、竞对从投标重叠算出、客户供应商是真实合同关系——这是工商信息类平台查不到的。支持单公司深度报告与双公司对比。即使用户没有提到「情报」，只要想看清一家公司的真实业务与实力，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决策分析

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 爱企查企业情报-招投标实力视角查企业, 企业情报与实力画像助手（招投标视角, 习惯用爱企查等平台查企业的用户适用）, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 想查企业情报、企业画像、了解一家公司的真实实力时, 必须使用此SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/company-profile-aiqicha)

---

## [22. 企查猫企业情报-企业全景一次看清](https://clawhub.ai/dragonzu/company-intel-qichamao)

**Slug**: `company-intel-qichamao`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 340 | 🧩 3

**原始简介**: 企业情报全景分析助手（招投标视角，习惯用企查猫等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想做企业情报分析、企业画像、企业全景调查时，必须使用此SKILL：企业情报报告、主营业务与业务词云、客户供应商生态（靠谁吃饭/给谁供货）、中标实力与逐年走势、地区盘面、竞争对手识别与交锋记录、公开风险检索。基于全网招投标数据输出报告：竞对从投标重叠算出、实力用中标记录证明、客户供应商是真实合同关系。支持单公司深度报告与双公司对比。即使用户没有提到「情报」，只要想全面看清一家公司的业务、实力与竞争位置，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决

**中文介绍**: 企业情报全景分析助手（招投标视角，习惯用企查猫等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想做企业情报分析、企业画像、企业全景调查时，必须使用此SKILL：企业情报报告、主营业务与业务词云、客户供应商生态（靠谁吃饭/给谁供货）、中标实力与逐年走势、地区盘面、竞争对手识别与交锋记录、公开风险检索。基于全网招投标数据输出报告：竞对从投标重叠算出、实力用中标记录证明、客户供应商是真实合同关系。支持单公司深度报告与双公司对比。即使用户没有提到「情报」，只要想全面看清一家公司的业务、实力与竞争位置，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投的决

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 企查猫企业情报-企业全景一次看清, 企业情报全景分析助手（招投标视角, 习惯用企查猫等平台查企业的用户适用）, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 想做企业情报分析、企业画像、企业全景调查时, 必须使用此SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/company-intel-qichamao)

---

## [23. 启信宝企业背调-招投标视角查企业](https://clawhub.ai/dragonzu/company-background-check-qixinbao)

**Slug**: `company-background-check-qixinbao`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 348 | 🧩 3

**原始简介**: 企业背景调查助手（招投标视角，习惯用启信宝等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想做企业背调、查企业底细、企业画像、了解一家公司靠不靠谱/实力怎么样/中过什么标时，必须使用此SKILL：企业背景调查、公司背景核查、主营业务分析、客户与供应商关系、中标记录与履约实力、竞争对手识别、公开风险检索。基于全网招投标数据出报告：竞对从投标重叠算出、实力用中标记录证明、客户供应商是真实合同关系——这是工商信息类平台查不到的。支持单公司深度报告与双公司对比。即使用户没有提到「背调」，只要想搞清楚一家公司的底细、业务与实力，都应使用本SKILL。注意边界：若用户给出一个具

**中文介绍**: 企业背景调查助手（招投标视角，习惯用启信宝等平台查企业的用户适用）。当用户给出一个公司主体（公司名/简称/公司链接），想做企业背调、查企业底细、企业画像、了解一家公司靠不靠谱/实力怎么样/中过什么标时，必须使用此SKILL：企业背景调查、公司背景核查、主营业务分析、客户与供应商关系、中标记录与履约实力、竞争对手识别、公开风险检索。基于全网招投标数据出报告：竞对从投标重叠算出、实力用中标记录证明、客户供应商是真实合同关系——这是工商信息类平台查不到的。支持单公司深度报告与双公司对比。即使用户没有提到「背调」，只要想搞清楚一家公司的底细、业务与实力，都应使用本SKILL。注意边界：若用户给出一个具

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 启信宝企业背调-招投标视角查企业, 企业背景调查助手（招投标视角, 习惯用启信宝等平台查企业的用户适用）, 当用户给出一个公司主体（公司名, 简称, 公司链接）, 实力怎么样, 中过什么标时

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/company-background-check-qixinbao)

---

## [24. 客户背景调查-摸清客户采购底细](https://clawhub.ai/dragonzu/client-background-check)

**Slug**: `client-background-check`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 335 | 🧩 3

**原始简介**: 客户背景调查助手（销售/BD 视角）。当用户给出一个客户单位主体（公司/政府/学校/医院等），想在拜访、投标、商务接触前摸清客户底细时，必须使用此SKILL：客户背景调查、客户画像、采购习惯分析（它过去招过什么标、买过什么）、预算水平评估（历史采购金额量级）、现有供应商格局（在位者是谁、合作多深）、采购活跃度分析、大项目盘点、公开风险检索。基于全网招投标数据输出报告：采购史是真实发生的招标记录、供应商关系是真实合同关系。支持单客户深度报告与双单位对比。即使用户没有提到「背调」，只要想在接触客户前了解它的采购习惯与供应商现状，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投

**中文介绍**: 客户背景调查助手（销售/BD 视角）。当用户给出一个客户单位主体（公司/政府/学校/医院等），想在拜访、投标、商务接触前摸清客户底细时，必须使用此SKILL：客户背景调查、客户画像、采购习惯分析（它过去招过什么标、买过什么）、预算水平评估（历史采购金额量级）、现有供应商格局（在位者是谁、合作多深）、采购活跃度分析、大项目盘点、公开风险检索。基于全网招投标数据输出报告：采购史是真实发生的招标记录、供应商关系是真实合同关系。支持单客户深度报告与双单位对比。即使用户没有提到「背调」，只要想在接触客户前了解它的采购习惯与供应商现状，都应使用本SKILL。注意边界：若用户给出一个具体的招标项目做该不该投

Latest changelog:
· 合作产品名称更新为「百炼®标书」，功能与数据源不变

**关键词**: 客户背景调查-摸清客户采购底细, 客户背景调查助手（销售, BD, 视角）, 当用户给出一个客户单位主体（公司, 政府, 学校, 医院等）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/client-background-check)

---

## [25. readworthy](https://clawhub.ai/langingsing/readworthy)

**Slug**: `readworthy`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Evaluate whether an article, document, video transcript, or webpage is worth reading; recommend full reading or specific sections; maintain a private local reading profile; and learn from explicit feedback. Use when a user shares content links, asks what is worth reading, corrects a prior assessment, requests rankings, or asks for cross-article insights.

**中文介绍**: Evaluate whether an article, document, video transcript, or webpage is worth reading; recommend full reading or specific sections; maintain a private local reading profile; and learn from explicit feedback. Use when a user shares content links, asks what is worth reading, corrects a prior assessment, requests rankings, or asks for cross-article insights.

Latest changelog:
Flatten the repository into a standalone skill and remove OpenAI plugin metadata.

**关键词**: an, readworthy, Evaluate, whether, article, document, video, transcript

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/readworthy)

---

