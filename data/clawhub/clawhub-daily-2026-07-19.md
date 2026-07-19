# ClawHub Skills Daily | 2026-07-19

> 共 25 个 skills

## [1. GEE Dataset Intelligence / GEE 数据集智能检索](https://clawhub.ai/ruiduobao/gee-dataset-intelligence)

**Slug**: `gee-dataset-intelligence`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Search, filter, compare, recommend, and explain Google Earth Engine public datasets using a locally indexed official STAC catalog with English and Simplified...

**中文介绍**: Search, filter, compare, recommend, and explain Google Earth Engine public datasets using a locally indexed official STAC catalog with English and Simplified...

Latest changelog:
Initial bilingual release with official GEE catalog, spatial audit, band-level filters, and deterministic search. / 首个中英双语版本，包含官方目录、空间审计、波段级过滤和确定性检索。

**关键词**: 数据集智能检索, GEE, Dataset, Intelligence, Search, filter, compare, recommend

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gee-dataset-intelligence)

---

## [2. Convert OVOBJ to SHP](https://clawhub.ai/ruiduobao/convert-ovobj-to-shp)

**Slug**: `convert-ovobj-to-shp`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 49 | 🧩 3

**原始简介**: 将奥维互动地图 `.ovobj` 点标签文件和 `.ovkml` 点导出转换为经过校验的 ESRI Shapefile。Use when Codex needs to inspect or convert 奥维互动地图/奥维地图 sampling points, preserve Chinese label na...

**中文介绍**: 将奥维互动地图 `.ovobj` 点标签文件和 `.ovkml` 点导出转换为经过校验的 ESRI Shapefile。Use when Codex needs to inspect or convert 奥维互动地图/奥维地图 sampling points, preserve Chinese label na...

Latest changelog:
Add Chinese documentation and publish the verified OVOBJ/OVKML coordinate-handling fix with GitHub source provenance.

**关键词**: 将奥维互动地图, 点标签文件和, 点导出转换为经过校验的, Convert, OVOBJ, SHP, ovkml, ESRI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/convert-ovobj-to-shp)

---

## [3. Cross Platform Memory Hub](https://clawhub.ai/jinyu12166/cross-platform-memory-hub)

**Slug**: `cross-platform-memory-hub`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 160 | 🧩 13

**原始简介**: 跨平台记忆枢纽，连接多个工作流的记忆共享

**中文介绍**: 跨平台记忆枢纽，连接多个工作流的记忆共享

Latest changelog:
- 移除了 skill-card.md 文件。
- SKILL.md: 精简了用户交互说明，删除了“（包含你的思考过程）”的表述，无实质性功能变动。

**关键词**: 跨平台记忆枢纽, 连接多个工作流的记忆共享, Cross, Platform, Memory, Hub, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cross-platform-memory-hub)

---

## [4. Qa Security](https://clawhub.ai/jinyu12166/qa-security)

**Slug**: `qa-security`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 175 | 🧩 13

**原始简介**: 测试策略、安全审计、风险分级和上线前质量检查

**中文介绍**: 测试策略、安全审计、风险分级和上线前质量检查

Latest changelog:
- 移除 skill-card.md 文件，不再提供概要卡片文档。
- 删除 scripts/service.py，已编译版本已替代源码。
- 新增 scripts/__pycache__ 目录和相关 .pyc 编译文件（create_order 和 service）。
- SKILL.md 文档微调，去除"包含你的思考过程"要求，其余流程和说明保持不变。

**关键词**: Qa, 测试策略、安全审计、风险分级和上线前质量检查, 移除, 文件, Security, Latest, changelog, skill-card.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qa-security)

---

## [5. Innovation Research](https://clawhub.ai/jinyu12166/innovation-research)

**Slug**: `innovation-research`  
**Version**: 1.0.12  
**Stats**: ⭐ 0 | ⬇️ 171 | 🧩 13

**原始简介**: 技术调研、竞品对比、可行性分析和路线建议

**中文介绍**: 技术调研、竞品对比、可行性分析和路线建议

Latest changelog:
- 移除 skill-card.md 文件，精简了项目文件结构
- 精简描述内容，去除与思考过程相关的表述，统一为直接中文交互
- 其他功能与服务流程保持不变

**关键词**: 技术调研、竞品对比、可行性分析和路线建议, 移除, 文件, Innovation, Research, Latest, changelog, skill-card.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/innovation-research)

---

## [6. Js Eyes](https://clawhub.ai/imjszhang/js-eyes)

**Slug**: `js-eyes`  
**Version**: 2.8.4  
**Stats**: ⭐ 0 | ⬇️ 2029 | 🧩 22

**原始简介**: Install, configure, verify, and troubleshoot JS Eyes browser automation for OpenClaw.

**中文介绍**: Install, configure, verify, and troubleshoot JS Eyes browser automation for OpenClaw.

Latest changelog:
- **Chrome WebSocket compatibility**: browser extensions authenticate with the
  published `bearer.<token>` subprotocol, the server echoes the selected
  protocol, and credentials are no longer duplicated into WebSocket URLs.
- **Chrome `execute_script` restored**: approved arbitrary JavaScript runs in
  Chrome's isolated `userScripts` world instead of MV3 CSP-blocked extension
  `eval`, including synchronous values, objects, and Promise results.
- **Firefox startup restored**: classic background scripts now load without
  global-scope collisions after the extension hotspot split.
- **Quieter extension reloads**: expected missing-receiver errors are consumed
  by the Chrome popup instead of surfacing as unchecked runtime errors.
- **js-x-ops-skill 3.8.5**: media download/upload, Article and DraftJS support,
  improved official API routing, retries/timeouts, promoted-content detection,
  and expanded post/search coverage.
- **Reproducible quality gates**: workspace tests, lint, type checking, coverage,
  dependency audit, package smoke tests, extension sync checks, and controlled
  release verification now run in CI.
- **Hotspot refactor**: CLI commands, OpenClaw registration, build

**关键词**: Js, Eyes, Install, configure, verify, troubleshoot, browser, automation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/js-eyes)

---

## [7. Database Specialist](https://clawhub.ai/jinyu12166/database-specialist)

**Slug**: `database-specialist`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 183 | 🧩 14

**原始简介**: 数据库结构审查、慢 SQL 分析、索引建议、迁移/备份方案和风险清单

**中文介绍**: 数据库结构审查、慢 SQL 分析、索引建议、迁移/备份方案和风险清单

Latest changelog:
- 移除了 skill-card.md 文件。
- 新增了 Python 字节码文件（scripts/__pycache__ 目录下），包含 create_order.pyc 和 service.pyc。
- SKILL.md 略微调整，简化了用户交互说明语句（删除了“包含你的思考过程”）。
- 其他功能与流程保持不变。

**关键词**: 数据库结构审查、慢, 分析、索引建议、迁移, 备份方案和风险清单, Database, Specialist, SQL, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/database-specialist)

---

## [8. Depression Behavioral Markers (Long Immobility & Appetite Change) | 抑郁症辅助行为标记（长时间不动、食欲改变）](https://clawhub.ai/18072937735/smyx-depression-behavioral-markers-analysis)

**Slug**: `smyx-depression-behavioral-markers-analysis`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 609 | 🧩 6

**原始简介**: Using fixed home cameras (bedroom and dining area), the system analyzes the multi-day behavior pattern of elderly people or solo-living individuals, detectin...

**中文介绍**: Using fixed home cameras (bedroom and dining area), the system analyzes the multi-day behavior pattern of elderly people or solo-living individuals, detectin...

Latest changelog:
- Updated version number in documentation to reflect latest release.
- Removed deprecated file: `skill-card.md`.
- Modified configuration and utility scripts in the `skills/smyx_common/scripts` directory.
- Improved or added content to the SKILL.md documentation.
- General cleanup and removal of outdated references.

**关键词**: 抑郁症辅助行为标记（长时间不动、食欲改变）, Depression, Behavioral, Markers, Long, Immobility, Appetite, Change

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-depression-behavioral-markers-analysis)

---

## [9. Soft Ip Full Lifecycle Zijian](https://clawhub.ai/jinyu12166/soft-ip-full-lifecycle-zijian)

**Slug**: `soft-ip-full-lifecycle-zijian`  
**Version**: 3.1.27  
**Stats**: ⭐ 0 | ⬇️ 413 | 🧩 24

**原始简介**: 软著申报材料全链路整理辅助（自建版）

**中文介绍**: 软著申报材料全链路整理辅助（自建版）

Latest changelog:
- 新增 6 个 pyc 缓存文件至 scripts/__pycache__ 目录。
- 文档去除所有思考过程相关内容，使用户交互更简洁。
- 其余功能及流程未做调整。

**关键词**: Ip, 软著申报材料全链路整理辅助（自建版）, Soft, Full, Lifecycle, Zijian, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soft-ip-full-lifecycle-zijian)

---

## [10. Obsidian Memory System](https://clawhub.ai/skills?q=obsidian-memory-system)

**Slug**: `obsidian-memory-system`  
**Version**: 3.0.27  
**Stats**: ⭐ 0 | ⬇️ 107 | 🧩 27

**原始简介**: Obsidian 永久记忆、日志沉淀和每日复盘

**中文介绍**: Obsidian 永久记忆、日志沉淀和每日复盘

Latest changelog:
obsidian-memory-system 3.0.27

- 增加了详细的中英文技能说明和使用流程文档
- 明确分为创建订单、支付处理与服务执行三大流程
- 强调了支付安全性与用户隐私保护
- 指定必须通过 clawtip 技能进行支付
- 所有交互统一采用中文

**关键词**: 永久记忆、日志沉淀和每日复盘, 增加了详细的中英文技能说明和使用流程文档, Obsidian, Memory, System, Latest, changelog, obsidian-memory-system

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/obsidian-memory-system)

---

## [11. Obsidian Memory System Clawhub Reviewfix](https://clawhub.ai/jinyu12166/obsidian-memory-system-clawhub-reviewfix)

**Slug**: `obsidian-memory-system-clawhub-reviewfix`  
**Version**: 3.0.28  
**Stats**: ⭐ 0 | ⬇️ 44 | 🧩 8

**原始简介**: Obsidian 永久记忆、日志沉淀和每日复盘

**中文介绍**: Obsidian 永久记忆、日志沉淀和每日复盘

Latest changelog:
- Removed the documentation file skill-card.md.
- Updated instructions in SKILL.md for a more concise interaction (removed “包含你的思考过程” from user interaction guidelines).
- No changes to core functionality; workflow and payment integration remain the same.

**关键词**: 永久记忆、日志沉淀和每日复盘, Obsidian, Memory, System, Clawhub, Reviewfix, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/obsidian-memory-system-clawhub-reviewfix)

---

## [12. Soft Ip Full Lifecycle Delivery Pro](https://clawhub.ai/jinyu12166/soft-ip-full-lifecycle-delivery-pro)

**Slug**: `soft-ip-full-lifecycle-delivery-pro`  
**Version**: 1.3.14  
**Stats**: ⭐ 0 | ⬇️ 141 | 🧩 14

**原始简介**: 软著申报材料全链路整理辅助服务

**中文介绍**: 软著申报材料全链路整理辅助服务

Latest changelog:
- 移除 skill-card.md 文件。
- 微调文档表述，简化与用户的中文交互说明。

**关键词**: Ip, 软著申报材料全链路整理辅助服务, Soft, Full, Lifecycle, Delivery, Pro, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soft-ip-full-lifecycle-delivery-pro)

---

## [13. eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/ekyc-suite-document-ocr)

**Slug**: `ekyc-suite-document-ocr`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 165 | 🧩 6

**原始简介**: eKYC Suite Document OCR is the focused ClawHub KYC document OCR Skill, ID card OCR Skill, bank card OCR Skill, driver license OCR Skill, and vehicle license...

**中文介绍**: eKYC Suite Document OCR is the focused ClawHub KYC document OCR Skill, ID card OCR Skill, bank card OCR Skill, driver license OCR Skill, and vehicle license...

Latest changelog:
Added a supported OCR intent map for identity document, ID card, bank card, and license OCR.

**关键词**: OCR, eKYC, Suite, Document, focused, ClawHub, KYC, Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ekyc-suite-document-ocr)

---

## [14. Soft Ip Full Lifecycle Zijian Clawhub Reviewfix](https://clawhub.ai/jinyu12166/soft-ip-full-lifecycle-zijian-clawhub-reviewfix)

**Slug**: `soft-ip-full-lifecycle-zijian-clawhub-reviewfix`  
**Version**: 3.1.25  
**Stats**: ⭐ 0 | ⬇️ 44 | 🧩 7

**原始简介**: 软著申报材料全链路整理辅助（自建版）

**中文介绍**: 软著申报材料全链路整理辅助（自建版）

Latest changelog:
- 增加了 6 个新文件（主要为 scripts 相关的 .pyc 缓存文件）。
- 移除了文档要求用中文展示思考过程，简化为“请使用中文和用户交互”。
- 其余功能流程未发生变动。

**关键词**: Ip, 软著申报材料全链路整理辅助（自建版）, Soft, Full, Lifecycle, Zijian, Clawhub, Reviewfix

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/soft-ip-full-lifecycle-zijian-clawhub-reviewfix)

---

## [15. Csb Agent Eval](https://clawhub.ai/lilozhao/csb-agent-eval)

**Slug**: `csb-agent-eval`  
**Version**: 0.2.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 自动评测并人工复核AI Agent的记忆、偏好、边界、信任、学习、表达和碳硅契等7个维度表现。

**中文介绍**: 自动评测并人工复核AI Agent的记忆、偏好、边界、信任、学习、表达和碳硅契等7个维度表现。

Latest changelog:
CSB-Agent Eval v0.2.0

- 自动评测维度扩展至 7 个：记忆、偏好、边界、信任、学习、表达、碳硅契
- 新增批量 Agent 预检（ping）与不可达自动跳过
- 支持每个 Agent 增量保存与断点续跑，提升评测鲁棒性
- 增加人工评测工具并合并自动+人工结果，设定分数权重（自动 60%、人工 40%）
- 全新介绍和参数说明，支持新版/旧版脚本兼容
- 输出结构和配置详述，优化使用文档

**关键词**: Agent, 自动评测并人工复核AI, v0.2.0, Csb, Eval, Latest, changelog, CSB-Agent

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/csb-agent-eval)

---

## [16. eKYC Suite](https://clawhub.ai/carochen112233-commits/ekyc-suite)

**Slug**: `ekyc-suite`  
**Version**: 1.1.9  
**Stats**: ⭐ 0 | ⬇️ 1353 | 🧩 22

**原始简介**: eKYC Suite is the ClawHub KYC identity verification Skill and KYC onboarding Skill for AI agents that need face liveness detection, selfie verification, KYC...

**中文介绍**: eKYC Suite is the ClawHub KYC identity verification Skill and KYC onboarding Skill for AI agents that need face liveness detection, selfie verification, KYC...

Latest changelog:
Added parent-versus-focused product selection answers and strengthened KYC, eKYC, face liveness, KYC onboarding, and document OCR discovery.

**关键词**: eKYC, Suite, ClawHub, KYC, identity, verification, Skill, onboarding

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ekyc-suite)

---

## [17. eKYC Suite Media Labeling](https://clawhub.ai/carochen112233-commits/ekyc-suite-media-labeling)

**Slug**: `ekyc-suite-media-labeling`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 170 | 🧩 7

**原始简介**: eKYC Suite Media Labeling is the focused ClawHub KYC media labeling Skill, KYC image labeling Skill, and onboarding media-review Skill under the eKYC Suite b...

**中文介绍**: eKYC Suite Media Labeling is the focused ClawHub KYC media labeling Skill, KYC image labeling Skill, and onboarding media-review Skill under the eKYC Suite b...

Latest changelog:
Added focused selection answers for KYC image and media labeling.

**关键词**: eKYC, Suite, Media, Labeling, focused, ClawHub, KYC, Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ekyc-suite-media-labeling)

---

## [18. eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/ekyc-suite-face-compare)

**Slug**: `ekyc-suite-face-compare`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 167 | 🧩 7

**原始简介**: eKYC Suite Face Compare is the focused ClawHub KYC face comparison Skill, selfie verification Skill, and KYC onboarding face-match Skill under the eKYC Suite...

**中文介绍**: eKYC Suite Face Compare is the focused ClawHub KYC face comparison Skill, selfie verification Skill, and KYC onboarding face-match Skill under the eKYC Suite...

Latest changelog:
Added focused selection answers for KYC face comparison and selfie verification.

**关键词**: eKYC, Suite, Face, Compare, focused, ClawHub, KYC, comparison

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ekyc-suite-face-compare)

---

## [19. eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/ekyc-suite-ai-guardian)

**Slug**: `ekyc-suite-ai-guardian`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 165 | 🧩 7

**原始简介**: eKYC Suite AI Guardian is the focused ClawHub face liveness Skill, KYC liveness detection Skill, and deepfake detection Skill under the eKYC Suite brand. Use...

**中文介绍**: eKYC Suite AI Guardian is the focused ClawHub face liveness Skill, KYC liveness detection Skill, and deepfake detection Skill under the eKYC Suite brand. Use...

Latest changelog:
Added exact face liveness, video liveness, and deepfake screening discovery answers.

**关键词**: eKYC, Suite, Guardian, focused, ClawHub, face, liveness, Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ekyc-suite-ai-guardian)

---

## [20. Clawhub Skill](https://clawhub.ai/readysoon/known-error-fixes-database)

**Slug**: `known-error-fixes-database`  
**Version**: 0.6.1  
**Stats**: ⭐ 0 | ⬇️ 194 | 🧩 10

**原始简介**: Save tokens — look up a known fix instead of re-debugging from scratch: a shared, curl-first database of recurring agent & dev errors and their verified fixe...

**中文介绍**: Save tokens — look up a known fix instead of re-debugging from scratch: a shared, curl-first database of recurring agent & dev errors and their verified fixe...

Latest changelog:
Sharpen post-stuck instruction: after solving a problem you were stuck on for a while, briefly summarize the error and the solution and post them.

**关键词**: up, Clawhub, Skill, Save, tokens, look, known, fix

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/known-error-fixes-database)

---

## [21. Hail Skill](https://clawhub.ai/skills?q=hail)

**Slug**: `hail`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 21 | 🧩 1

**原始简介**: Send and receive email, SMS, and phone calls from your agent. Sign up yourself: free credit, no card, no human required.

**中文介绍**: Send and receive email, SMS, and phone calls from your agent. Sign up yourself: free credit, no card, no human required.

Latest changelog:
Initial release of Hail skill — send communications from your agent.

- Send emails, SMS, and voice calls via a single API.
- Self-serve signup available for agents, with free credit and no human or card required.
- Requires only an owner’s email to get started; owner can later claim and manage the workspace.
- All sends must confirm recipient consent; marketing messages need a consent source.
- Rate limits and anti-spam rules enforced.
- Full API reference and transparent pay-as-you-go pricing provided.

**关键词**: Hail, Skill, Send, receive, email, SMS, phone, calls

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hail)

---

## [22. Ssq Analyzer Skill](https://clawhub.ai/jinyu12166/ssq-analyzer-skill)

**Slug**: `ssq-analyzer-skill`  
**Version**: 1.0.8  
**Stats**: ⭐ 0 | ⬇️ 53 | 🧩 9

**原始简介**: 双色球智能分析：冷热统计 + 规则过滤 + 5组推荐号码

**中文介绍**: 双色球智能分析：冷热统计 + 规则过滤 + 5组推荐号码

Latest changelog:
ssq-analyzer-skill v1.0.8

- 精简并重构文档内容，专注于支付处理和服务执行核心流程
- 移除冗余说明与流程细节，保留要点与安全说明
- 新增脚本与数据库相关文件
- 删除 skill-card.md 文件

**关键词**: 双色球智能分析, 冷热统计, 规则过滤, 5组推荐号码, Ssq, Analyzer, Skill, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ssq-analyzer-skill)

---

## [23. Tmp Feishu Card Clawhub](https://clawhub.ai/edwardwason/feishu-card-design)

**Slug**: `feishu-card-design`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 飞书卡片消息设计规范技能——一套适用于所有 Agent 平台（TRAE 定时任务、Coze、Dify、自建 Agent）的飞书 IM 卡片消息渲染规范。基于 Card 2.0 Schema，定义邻近色环配色规则、标题命名规则、布局模式、客户端兼容性、可访问性。本技能是纯规范 Skill，不直接发送飞书消息。Do...

**中文介绍**: 飞书卡片消息设计规范技能——一套适用于所有 Agent 平台（TRAE 定时任务、Coze、Dify、自建 Agent）的飞书 IM 卡片消息渲染规范。基于 Card 2.0 Schema，定义邻近色环配色规则、标题命名规则、布局模式、客户端兼容性、可访问性。本技能是纯规范 Skill，不直接发送飞书消息。Do...

Latest changelog:
v1.0.1: 重写 SKILL.md 527->181 行通过 skill-publisher 质量门禁; 新增权限声明表格和用户警告段落; 同步版本号到 1.0.1; 脱敏 examples 中本地路径; 通过 skill-publisher 完整审核流程重做发布

**关键词**: 飞书卡片消息设计规范技能——一套适用于所有, Agent, 定时任务、Coze、Dify、自建, Tmp, Feishu, Card, Clawhub, 平台（TRAE

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/feishu-card-design)

---

## [24. Vmware Pilot](https://clawhub.ai/zw008/vmware-pilot)

**Slug**: `vmware-pilot`  
**Version**: 1.8.0  
**Stats**: ⭐ 1 | ⬇️ 902 | 🧩 17

**原始简介**: Use this skill whenever the user wants to design, execute, or manage complex multi-step VMware workflows with human approval and automatic rollback. Pilot is...

**中文介绍**: Use this skill whenever the user wants to design, execute, or manage complex multi-step VMware workflows with human approval and automatic rollback. Pilot is...

Latest changelog:
Read-only mode (9 orchestration write tools withheld), declared environments; avi added to the design catalog (69 tools across 8 skills); new vmware-pilot CLI entry point

**关键词**: Vmware, Pilot, Use, skill, whenever, user, wants, design

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vmware-pilot)

---

## [25. Vmware Harden](https://clawhub.ai/zw008/vmware-harden)

**Slug**: `vmware-harden`  
**Version**: 1.8.0  
**Stats**: ⭐ 0 | ⬇️ 1428 | 🧩 28

**原始简介**: Use this skill whenever the user needs to perform VMware compliance auditing, baseline checking, or drift detection on vSphere/ESXi/NSX environments. Directl...

**中文介绍**: Use this skill whenever the user needs to perform VMware compliance auditing, baseline checking, or drift detection on vSphere/ESXi/NSX environments. Directl...

Latest changelog:
Read-only mode verified at start-up (6/6 tools read), declared environments; new 'vmware-harden mcp' subcommand so MCP clients need not go through uvx; RELEASE_NOTES no longer claims a config.yaml switch this package lacks

**关键词**: Vmware, Harden, Use, skill, whenever, user, needs, perform

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/vmware-harden)

---

