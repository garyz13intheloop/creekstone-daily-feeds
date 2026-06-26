# ClawHub Skills Daily | 2026-06-26

> 共 25 个 skills

## [1. Growth Engineer](https://clawhub.ai/wotaso-dev/growth-engineer)

**Slug**: `growth-engineer`  
**Version**: 1.0.208  
**Stats**: ⭐ 0 | ⬇️ 2755 | 🧩 154

**原始简介**: Growth Engineer for mobile apps and agent runtimes including OpenClaw and Hermes. Correlate analytics, crashes, billing, feedback, store signals, and repo co...

**中文介绍**: Growth Engineer for mobile apps and agent runtimes including OpenClaw and Hermes. Correlate analytics, crashes, billing, feedback, store signals, and repo co...

Latest changelog:
- Updated skill metadata version to 1.0.208.
- Removed redundant file: `skill-card.md`.
- Minor maintenance updates across scripts and tests.
- No user-facing or runtime behavior changes.

**关键词**: Agent, Growth, Engineer, mobile, apps, runtimes, including, OpenClaw

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/growth-engineer)

---

## [2. Axion](https://clawhub.ai/eternis/axion)

**Slug**: `axion`  
**Version**: 1.0.2  
**Stats**: ⭐ 1 | ⬇️ 0 | 🧩 3

**原始简介**: Forecast the probability of a future event with the Axion API. Use when asked the odds, likelihood, or a prediction for an uncertain or future event.

**中文介绍**: Forecast the probability of a future event with the Axion API. Use when asked the odds, likelihood, or a prediction for an uncertain or future event.

Latest changelog:
- Clarified that the forecast ID is an opaque token rather than a prefixed string, and adjusted example output accordingly.
- Added a new pitfall: handle occasional 5xx responses with plain text bodies by checking HTTP status before attempting to parse as JSON, and retry if needed.
- Removed file: skill-card.md.

**关键词**: of, API, Axion, Forecast, probability, future, event, Use

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/axion)

---

## [3. 金蝶云星空二次开发](https://clawhub.ai/xiaoqishitou/kingdee-dev)

**Slug**: `kingdee-dev`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 380 | 🧩 2

**原始简介**: 金蝶二次开发全栈技能覆盖金蝶云星空（K3 Cloud）和金蝶云苍穹（Cosmic）的二次开发，重点聚焦插件开发。触发场景：金蝶、K3、星空、苍穹、BOS、BOS IDE、单据、插件开发、 表单插件、列表插件、操作插件、报表插件、单据转换插件、服务插件、审批流插件、WebAPI、DynamicObject、BusinessInfo、IIS、SQL Server、KingScript、表单......

**中文介绍**: 金蝶二次开发全栈技能覆盖金蝶云星空（K3 Cloud）和金蝶云苍穹（Cosmic）的二次开发，重点聚焦插件开发。触发场景：金蝶、K3、星空、苍穹、BOS、BOS IDE、单据、插件开发、 表单插件、列表插件、操作插件、报表插件、单据转换插件、服务插件、审批流插件、WebAPI、DynamicObject、BusinessInfo、IIS、SQL Server、KingScript、表单......

Latest changelog:
## 一、plugin-templates.md 语法与健壮性修复
### 1. 代码块语法统一修正
- 将文档内所有 `` `csharp`` 单行反引号代码标记，全局替换为标准多行代码块：``````csharp``````
- 修正所有不规范字符串包裹：`""... ""` 错误嵌套双引号统一修改为标准 `"..."`

### 2. 代码逻辑健壮性补充
1. 全模板补充**空值判断**：入参、实体字段、集合对象前置非空校验
2. 全局增加**try-catch 异常捕获**，配套日志打印、异常抛出、友好错误返回
3. 字段采用**防御式取值**：空兼容取值（`GetValueOrDefault`、空兜底默认值），杜绝空引用崩溃

## 二、SKILL.md 全文重写扩充要求
### 基础结构新增
1. 新增**if-else 业务需求决策树**，结构化拆解分支判断逻辑
2. 扩充业务场景触发关键词库：
    - 审批流：审批、驳回、加签、会签、转交、跳过审批、多级审批、代理审批
    - 多组织：跨组织隔离、组织权限、数据隔离、业务单元、法人主体
    - 性能：慢SQL、超时、死锁、并发阻塞、接口吞吐量、资源占用
    - 安全：SQL注入、越权访问、字段脱敏、参数校验、权限拦截、签名校验
3. 新增**参考文件映射表**，绑定知识点与对应参考文档路径
4. 补充**版本兼容性说明**：各接口、插件、脚本在不同苍穹版本适配范围、兼容断点、降级方案

### 配套新增3份独立Reference参考文档
| 文档文件名 | 核心覆盖内容 |
| ---- | ---- |
| workflow-plugin-dev.md | 审批流插件开发：动态审批人配置、审批跳过/转交/加签/会签、多级串行并行审批、审批代理规则 |
| multi-org-security.md | 多组织架构：组织数据隔离、字段级权限、数据行范围权限、SQL参数化防注入、跨组织访问白名单 |
| performance-debugging.md | 插件性能调优：业务逻辑优化、SQL索引优化、事务死锁排查、运行日志采集、Dump文件分析定位、并发限流 |

## 三、苍穹平台文档内容扩展
### 1. Java插件体系完善
- 整理**Java插件类型完整矩阵**，分类标注适用场景、生命周期、权限等级
- 补齐三类标准可复用模板：
  1. 列表插件标准开发模板
  2. 自定义对外API接口模板
  3. 后台定时任务调度完整模板
- KingScript：全量事件枚举+配套实操示例、钩子执行顺序、上下文取值规范
- OpenAPI：标准签名、验签、请求封装完整认证代码示例

### 2. 部署与发布规范
- K8s/Docker容器化部署配置模板
- 插件元数据打包、

**关键词**: 金蝶云星空二次开发, 金蝶二次开发全栈技能覆盖金蝶云星空（K3, 重点聚焦插件开发, 触发场景, 金蝶、K3、星空、苍穹、BOS、BOS, IDE、单据、插件开发、, Server、KingScript、表单, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/kingdee-dev)

---

## [4. Cat & Dog Health Diagnostic Analysis Tool | 猫狗宠物健康诊断分析工具](https://clawhub.ai/smyx-sunjinhui/smyx-pet-analysis)

**Slug**: `smyx-pet-analysis`  
**Version**: 1.0.4  
**Stats**: ⭐ 4 | ⬇️ 549 | 🧩 5

**原始简介**: Triggers when a user provides a video URL or file of a pet (cat/dog/bird) for analysis; supports local video uploads or network URLs to call server-side APIs...

**中文介绍**: Triggers when a user provides a video URL or file of a pet (cat/dog/bird) for analysis; supports local video uploads or network URLs to call server-side APIs...

Latest changelog:
- Skill workflow and documentation overhauled for clarity and user privacy—internal identity now handled automatically, never exposed to users.
- User is no longer prompted to provide open-id, username, or phone; all identity/association handled by backend logic.
- Strict prohibition on identity parameter display, request, or exposure in any output, example, or prompt.
- Usage, scenarios, and parameter docs updated for directness and reduced complexity; added data security and privacy statement.
- Internal structure changes: more modular, clearer resource structure; removed obsolete files (e.g. scripts/api_service.py).
- Historical report queries remain strictly cloud-based; all table outputs updated for consistency.

**关键词**: 猫狗宠物健康诊断分析工具, Cat, Dog, Health, Diagnostic, Analysis, Tool, Triggers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-pet-analysis)

---

## [5. Spec Workflow Guide](https://clawhub.ai/binggg/spec-workflow-guide)

**Slug**: `spec-workflow-guide`  
**Version**: 1.18.6  
**Stats**: ⭐ 0 | ⬇️ 1360 | 🧩 25

**原始简介**: Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unc...

**中文介绍**: Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unc...

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Spec, Workflow, Guide, Use, when, medium-to-large, changes, need

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/spec-workflow-guide)

---

## [6. Web Development](https://clawhub.ai/binggg/web-development)

**Slug**: `web-development`  
**Version**: 1.27.7  
**Stats**: ⭐ 0 | ⬇️ 2786 | 🧩 35

**原始简介**: Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for Re...

**中文介绍**: Use when users need to implement, integrate, debug, build, deploy, or validate a Web frontend after the product direction is already clear, especially for Re...

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Web, Development, Use, when, users, need, implement, integrate

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/web-development)

---

## [7. Ui Design Guide](https://clawhub.ai/binggg/ui-design-guide)

**Slug**: `ui-design-guide`  
**Version**: 1.18.6  
**Stats**: ⭐ 0 | ⬇️ 1650 | 🧩 25

**原始简介**: Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI.

**中文介绍**: Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI.

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Ui, Design, Guide, Use, when, users, need, visual

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ui-design-guide)

---

## [8. Cloudbase](https://clawhub.ai/binggg/cloudbase)

**Slug**: `cloudbase`  
**Version**: 1.92.9  
**Stats**: ⭐ 0 | ⬇️ 3654 | 🧩 102

**原始简介**: Use this skill when you develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase (腾讯云开发, 云开发, TCB, 微信云开发) projects. Covers Web apps (React,...

**中文介绍**: Use this skill when you develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase (腾讯云开发, 云开发, TCB, 微信云开发) projects. Covers Web apps (React,...

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Cloudbase, Use, skill, when, develop, design, build, deploy

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cloudbase)

---

## [9. Cloudbase Wechat Integration](https://clawhub.ai/binggg/cloudbase-wechat-integration)

**Slug**: `cloudbase-wechat-integration`  
**Version**: 1.2.6  
**Stats**: ⭐ 0 | ⬇️ 313 | 🧩 9

**原始简介**: CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, paym...

**中文介绍**: CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, paym...

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Cloudbase, Wechat, Integration, guide, Mini, Program, Pay, Official

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/cloudbase-wechat-integration)

---

## [10. Miniprogram Development](https://clawhub.ai/binggg/miniprogram-development)

**Slug**: `miniprogram-development`  
**Version**: 1.28.6  
**Stats**: ⭐ 2 | ⬇️ 2524 | 🧩 35

**原始简介**: WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects. This skill should be us...

**中文介绍**: WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects. This skill should be us...

Latest changelog:
Recent commits / 最近提交: | - chore(release): bump version to v2.23.5 | - chore(release): build artifacts for v2.23.5 | - feat(mcp): ✨ add CustomImage imageConfig support to manageFunctions for TCR→SCF deploy (#781) | - fix(mcp): 🔧 sync package-lock.json with package.json (#780) | - fix(issue-auto): 🤖 attempt fix for issue #771 (#776)

**关键词**: Miniprogram, Development, WeChat, Mini, Program, skill, building, debugging

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/miniprogram-development)

---

## [11. SynthClaw](https://clawhub.ai/ayakimovich/synthclaw)

**Slug**: `synthclaw`  
**Version**: 0.2.2  
**Stats**: ⭐ 0 | ⬇️ 403 | 🧩 6

**原始简介**: Render Blender files with agent-controlled procedural parameters for synthetic data generation. A key capability of this skill is returning dynamic quality m...

**中文介绍**: Render Blender files with agent-controlled procedural parameters for synthetic data generation. A key capability of this skill is returning dynamic quality m...

Latest changelog:
synthclaw v0.2.2

- Adds a new "Agent Rules & Guidelines" section, clarifying strict tool usage requirements for agents and prohibiting direct CLI or custom Python use.
- Requires that agents must call `analyze_blend` before rendering to correctly identify available parameters.
- Removes the `skill-card.md` file.
- Updates metadata version and documentation to reflect the new usage constraints and best practices.

**关键词**: SynthClaw, Render, Blender, files, agent-controlled, procedural, parameters, synthetic

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/synthclaw)

---

## [12. skill-standardization](https://clawhub.ai/ldxs001/skill-standardization)

**Slug**: `skill-standardization`  
**Version**: 2.98.0  
**Stats**: ⭐ 0 | ⬇️ 1732 | 🧩 69

**原始简介**: Skill 标准化规范引擎。支持 R-01~R-26 规范审查（audit / create / update / refactor / bump / readonly 六模式），含权限扫描、数据目录合规检查、渐进式加载、LLM 二次筛分类。

**中文介绍**: Skill 标准化规范引擎。支持 R-01~R-26 规范审查（audit / create / update / refactor / bump / readonly 六模式），含权限扫描、数据目录合规检查、渐进式加载、LLM 二次筛分类。

Latest changelog:
4项修复: _llm_only_fix_keys禁止分类绕过; _path_detector.py统一路径检测; R-23排除.standardization/路径; R-20移除R-23重复引用

**关键词**: 标准化规范引擎, 支持, R-01~R-26, 规范审查（audit, skill-standardization, Skill, update, refactor

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-standardization)

---

## [13. Design Systems Index](https://clawhub.ai/ezra-y/design-systems-index)

**Slug**: `design-systems-index`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: External-link index of major companies' design systems (Material, Fluent, Carbon, Polaris, Atlassian, Lightning), design-token tools and specs, pattern-libra...

**中文介绍**: External-link index of major companies' design systems (Material, Fluent, Carbon, Polaris, Atlassian, Lightning), design-token tools and specs, pattern-libra...

Latest changelog:
No file changes detected in this version.

- No functional or documentation changes were made.
- Version updated without modifications to any files.

**关键词**: of, Design, Systems, Index, External-link, major, companies', Material

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/design-systems-index)

---

## [14. Ios Motion Patterns Index](https://clawhub.ai/ezra-y/ios-motion-patterns-index)

**Slug**: `ios-motion-patterns-index`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Index of ready-to-run Swift animation code examples organized by category (Menu, Transition, Indicator, Alert, Animation, Tableview, Collectionview, UI) sour...

**中文介绍**: Index of ready-to-run Swift animation code examples organized by category (Menu, Transition, Indicator, Alert, Animation, Tableview, Collectionview, UI) sour...

Latest changelog:
No functional or content changes in this version.

- No file changes detected; SKILL.md content remains the same.
- Version bumped for maintenance or metadata update.

**关键词**: of, Ios, Motion, Patterns, Index, ready-to-run, Swift, animation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ios-motion-patterns-index)

---

## [15. Green Screen Cutout Assets](https://clawhub.ai/act-chao/green-screen-cutout-assets)

**Slug**: `green-screen-cutout-assets`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate green-screen raster subject assets with an image model and convert them into transparent PNGs with robust chroma-key cutout. Use when Codex needs pe...

**中文介绍**: Generate green-screen raster subject assets with an image model and convert them into transparent PNGs with robust chroma-key cutout. Use when Codex needs pe...

Latest changelog:
Initial release of green-screen-cutout-assets.

- Provides detailed workflow for generating transparent PNG assets from green-screen model images.
- Includes robust chroma-key cutout script with batch/solo options, QA report, and contact sheet generation.
- Offers prompt guidance to avoid common cutout issues and preserve subject details.
- Supplies explicit QA rules and troubleshooting steps for asset approval.
- Integration checklist ensures consistent asset management and quality.

**关键词**: Green, Screen, Cutout, Assets, Generate, green-screen, raster, subject

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/green-screen-cutout-assets)

---

## [16. Design Tools Index](https://clawhub.ai/ezra-y/design-tools-index)

**Slug**: `design-tools-index`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Categorized index of design tools by purpose — animation, color pickers, prototyping, design handoff, design-to-code, icons, fonts, gradients, illustration,...

**中文介绍**: Categorized index of design tools by purpose — animation, color pickers, prototyping, design handoff, design-to-code, icons, fonts, gradients, illustration,...

Latest changelog:
- Initial release of design-tools-index.
- Provides a categorized index of design tools for over 30 design tasks (e.g., animation, prototyping, icons, gradients, design-to-code).
- Each major category features 2–3 top tools and links to expanded reference lists.
- Includes references for additional categories such as accessibility, user research, media assets, 3D and AR, and more.
- Designed to help users quickly select appropriate tools for any design-related task.

**关键词**: of, Design, Tools, Index, Categorized, purpose, animation, color

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/design-tools-index)

---

## [17. Pet Drying Box Heat Stress Analysis | 宠物烘干箱内热应激预警](https://clawhub.ai/18072937735/smyx-pet-drying-box-heat-stress-analysis)

**Slug**: `smyx-pet-drying-box-heat-stress-analysis`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 369 | 🧩 3

**原始简介**: Triggers when a user provides a pet drying box area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for...

**中文介绍**: Triggers when a user provides a pet drying box area video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for...

Latest changelog:
**User identity parameter handling is now fully automated and never exposed to users.**

- Identity (open-id) handling is moved to the system/scripts and is no longer collected from or shown to users.
- Updated SKILL.md: all user instructions, workflows, and usage examples now omit identity parameter prompts or exposure.
- Instructions strictly prohibit requesting or displaying internal user identifiers.
- Revised scripts and configuration references to support the new identity automation.
- More structured skill documentation and formatting improvements.

**关键词**: 宠物烘干箱内热应激预警, Pet, Drying, Box, Heat, Stress, Analysis, Triggers

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-pet-drying-box-heat-stress-analysis)

---

## [18. Sentio Processor](https://clawhub.ai/skills?q=sentio-processor)

**Slug**: `sentio-processor`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Use when initializing Sentio projects, writing blockchain processor code, adding contracts/ABIs, testing processors, or deploying to the Sentio platform. Tri...

**中文介绍**: Use when initializing Sentio projects, writing blockchain processor code, adding contracts/ABIs, testing processors, or deploying to the Sentio platform. Tri...

Latest changelog:
sentio-processor 1.0.1

- Added a comprehensive SKILL.md documentation outlining project setup, contract/ABI registration, processor coding, testing, and deployment workflows for Sentio.
- Provides a full lifecycle guide: CLI commands, processor patterns across supported blockchains, and best practices.
- Describes progressive disclosure for advanced features with references to specialized documentation.
- Includes config examples for package.json and sentio.yaml to ease integration and address common issues.
- Details handler types, event filtering, and testing/deployment for multi-chain, DeFi, and points/position tracking use cases.

**关键词**: Sentio, Processor, Use, when, initializing, projects, writing, blockchain

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sentio-processor)

---

## [19. Ai Magic Tricks](https://clawhub.ai/ai-gaoqian/ai-magic-tricks)

**Slug**: `ai-magic-tricks`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 117 | 🧩 3

**原始简介**: AI魔术教程 — 近景魔术（硬币/纸牌/皮筋/海绵球/戒指/绳子）/舞台魔术/心灵魔术Mentalism（读心/预言/冷读术/Barnum效应）/手法Sleight of Hand（French Drop/Classic Palm/Pass/Double Lift/Force/False Shuffle）/错误引...

**中文介绍**: AI魔术教程 — 近景魔术（硬币/纸牌/皮筋/海绵球/戒指/绳子）/舞台魔术/心灵魔术Mentalism（读心/预言/冷读术/Barnum效应）/手法Sleight of Hand（French Drop/Classic Palm/Pass/Double Lift/Force/False Shuffle）/错误引...

Latest changelog:
- Removed the file skill-card.md.
- No changes to user-facing features or documentation content.
- Housekeeping update to clean up unused or redundant files.

**关键词**: AI魔术教程, 近景魔术（硬币, 纸牌, 皮筋, 海绵球, 戒指, Magic, Tricks

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-magic-tricks)

---

## [20. ClawSecCheck — OpenClaw Security Self-Audit](https://clawhub.ai/gl0di/clawseccheck)

**Slug**: `clawseccheck`  
**Version**: 1.22.0  
**Stats**: ⭐ 0 | ⬇️ 291 | 🧩 69

**原始简介**: Free, local, read-only security self-audit for your own OpenClaw agent. Scores your setup (A–F), finds the most urgent holes, and gives copy-paste fixes. No...

**中文介绍**: Free, local, read-only security self-audit for your own OpenClaw agent. Scores your setup (A–F), finds the most urgent holes, and gives copy-paste fixes. No...

Latest changelog:
Release 1.22.0 (180839e45c2a467f6e52407e87e6b1fb8fafefae)

**关键词**: ClawSecCheck, OpenClaw, Security, Self-Audit, Free, local, read-only, own

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawseccheck)

---

## [21. Ai Xiangqi Master](https://clawhub.ai/ai-gaoqian/ai-xiangqi-master)

**Slug**: `ai-xiangqi-master`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 88 | 🧩 3

**原始简介**: AI象棋大师 — 开局库/中局战术/残局精讲/杀法训练/名局复盘/棋软使用/等级提升。覆盖中国象棋/国际象棋双棋种，从业9到业9。全球象棋人口超3亿，ClawHub零覆盖。

**中文介绍**: AI象棋大师 — 开局库/中局战术/残局精讲/杀法训练/名局复盘/棋软使用/等级提升。覆盖中国象棋/国际象棋双棋种，从业9到业9。全球象棋人口超3亿，ClawHub零覆盖。

Latest changelog:
- Removed the skill-card.md file.  
- No changes to logic or user-facing features.  
- Documentation is now more streamlined, with fewer redundant files.

**关键词**: AI象棋大师, 开局库, 中局战术, 残局精讲, 杀法训练, 名局复盘, Xiangqi, Master

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-xiangqi-master)

---

## [22. Ai Tea Incense](https://clawhub.ai/ai-gaoqian/ai-tea-incense)

**Slug**: `ai-tea-incense`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 78 | 🧩 2

**原始简介**: Provides expertise on tea types, brewing, ceremonies, incense arts, aroma therapy, and zen lifestyle for mindfulness and sensory appreciation.

**中文介绍**: Provides expertise on tea types, brewing, ceremonies, incense arts, aroma therapy, and zen lifestyle for mindfulness and sensory appreciation.

Latest changelog:
- Removed the skill-card.md file.
- No changes to core functionality or documentation content.

**关键词**: Tea, Incense, Provides, expertise, types, brewing, ceremonies, arts

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-tea-incense)

---

## [23. Ai Stock Analysis](https://clawhub.ai/ai-gaoqian/ai-stock-analysis)

**Slug**: `ai-stock-analysis`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 85 | 🧩 2

**原始简介**: Provides comprehensive stock analysis including technical and fundamental evaluation, market trends, and portfolio strategy guidance for retail investors.

**中文介绍**: Provides comprehensive stock analysis including technical and fundamental evaluation, market trends, and portfolio strategy guidance for retail investors.

Latest changelog:
- Removed skill-card.md file from the repository.
- No changes were made to SKILL.md content or core functionality.

**关键词**: Stock, Analysis, Provides, comprehensive, including, technical, fundamental, evaluation

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-stock-analysis)

---

## [24. Ai Ski Snowboard](https://clawhub.ai/ai-gaoqian/ai-ski-snowboard)

**Slug**: `ai-ski-snowboard`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 81 | 🧩 3

**原始简介**: AI滑雪大师 — 双板/单板教学、装备选购、雪场攻略、刻滑/公园/野雪技术、安全与损伤预防。覆盖日韩/欧洲/北美/新疆/崇礼/东北全球雪场。中国滑雪人口超3000万，ClawHub零覆盖。

**中文介绍**: AI滑雪大师 — 双板/单板教学、装备选购、雪场攻略、刻滑/公园/野雪技术、安全与损伤预防。覆盖日韩/欧洲/北美/新疆/崇礼/东北全球雪场。中国滑雪人口超3000万，ClawHub零覆盖。

Latest changelog:
- Removed the file skill-card.md from the project.
- No other changes to functionality or documentation.

**关键词**: AI滑雪大师, 双板, 单板教学、装备选购、雪场攻略、刻滑, 公园, 野雪技术、安全与损伤预防, 覆盖日韩, Ski, Snowboard

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-ski-snowboard)

---

## [25. Ai Scuba Diving](https://clawhub.ai/ai-gaoqian/ai-scuba-diving)

**Slug**: `ai-scuba-diving`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 80 | 🧩 3

**原始简介**: AI潜水指南 — OW/AOW考证、自由潜水、技术潜水、装备选购、全球潜点、水下摄影、海洋生物识别、潜水安全。覆盖PADI/SSI/AIDA/Molchanovs体系。全球潜水人口超3000万，ClawHub零覆盖。

**中文介绍**: AI潜水指南 — OW/AOW考证、自由潜水、技术潜水、装备选购、全球潜点、水下摄影、海洋生物识别、潜水安全。覆盖PADI/SSI/AIDA/Molchanovs体系。全球潜水人口超3000万，ClawHub零覆盖。

Latest changelog:
- Removed the file skill-card.md from the project.
- No changes to features or user-facing documentation.

**关键词**: AI潜水指南, OW, Scuba, Diving, 覆盖PADI, SSI, AIDA, Molchanovs体系

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-scuba-diving)

---

