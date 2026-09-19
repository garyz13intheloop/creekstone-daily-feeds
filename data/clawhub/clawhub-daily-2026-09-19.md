# ClawHub Skills Daily | 2026-09-19

> 共 25 个 skills

## [1. redfin](https://clawhub.ai/chrischall/redfin)

**Slug**: `redfin`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 890 | 🧩 13

**原始简介**: Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. Triggers on phrases like "find homes on redfin in", "redfin property details for", "show my saved redfin homes", "what's my saved redfin search seeing", "what does redfin say about", "redfin market report for", or any request involving Redfin properties, prices, or your saved Redfin activity. Requires redfin-mcp installed and the fetchproxy extension active (see Setup below).

**中文介绍**: Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. Triggers on phrases like "find homes on redfin in", "redfin property details for", "show my saved redfin homes", "what's my saved redfin search seeing", "what does redfin say about", "redfin market report for", or any request involving Redfin properties, prices, or your saved Redfin activity. Requires redfin-mcp installed and the fetchproxy extension active (see Setup below).

Latest changelog:
- Removed the skill-card.md file.
- No user-facing changes to functionality or features.
- Documentation and server setup instructions remain unchanged.

**关键词**: up, redfin, Look, real-estate, listings, property, details, market

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/redfin)

---

## [2. redfin-fpx](https://clawhub.ai/chrischall/redfin-fpx)

**Slug**: `redfin-fpx`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 880 | 🧩 13

**原始简介**: Query redfin.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the redfin-mcp server — resolve locations/addresses, search for-sale listings, read property detail (price, beds/baths, price history, tax history), market trends, comparable rentals, climate risk, photos, and (signed-in) saved homes and saved searches, via one-shot calls through a signed-in browser tab. Use when you want Redfin data without the MCP, in a script, or on a machine where the MCP isn't installed.

**中文介绍**: Query redfin.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the redfin-mcp server — resolve locations/addresses, search for-sale listings, read property detail (price, beds/baths, price history, tax history), market trends, comparable rentals, climate risk, photos, and (signed-in) saved homes and saved searches, via one-shot calls through a signed-in browser tab. Use when you want Redfin data without the MCP, in a script, or on a machine where the MCP isn't installed.

Latest changelog:
- Removed the file: skill-card.md.
- No user-facing or functional changes; documentation and main usage remain unchanged.

**关键词**: US, redfin-fpx, Query, redfin.com, real-estate, portal, shell, fpx

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/redfin-fpx)

---

## [3. skylight-mcp](https://clawhub.ai/chrischall/skylight-mcp)

**Slug**: `skylight-mcp`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 1949 | 🧩 24

**原始简介**: Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans. Triggers on phrases like "check Skylight", "what's on the family calendar", "add an event to Skylight", "what chores does [kid] have", "mark [chore] done", "add milk to the grocery list", "what's on our shopping list", "what's for dinner", "what's on the meal plan", "who's on the Skylight frame", or any request involving the Skylight frame, family calendar, chores, rewards, shared lists, or meals. Works against your own signed-in Skylight account via email + password.

**中文介绍**: Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans. Triggers on phrases like "check Skylight", "what's on the family calendar", "add an event to Skylight", "what chores does [kid] have", "mark [chore] done", "add milk to the grocery list", "what's on our shopping list", "what's for dinner", "what's on the meal plan", "who's on the Skylight frame", or any request involving the Skylight frame, family calendar, chores, rewards, shared lists, or meals. Works against your own signed-in Skylight account via email + password.

Latest changelog:
Version 1.0.1 of skylight-mcp contains no code or documentation changes.

- No file changes detected in this release.
- Functionality and documentation remain unchanged from the previous version.

**关键词**: skylight-mcp, Read, manage, Skylight, Calendar, family, hub, events

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skylight-mcp)

---

## [4. 论衡 — 严肃长文流水线](https://clawhub.ai/zuoyunlai/lunheng-article-pipeline)

**Slug**: `lunheng-article-pipeline`  
**Version**: 2.12.63  
**Stats**: ⭐ 1 | ⬇️ 2753 | 🧩 128

**原始简介**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

**中文介绍**: 学术论文/深度长文/行业分析流水线：含同行评审与期刊/发布渠道匹配建议（advisory）。不调用执行类工具（exec/process/code_execution，声明式）；主控持有会话编排与状态类工具（多 Agent 派发/收报告的设计内必需面）。标准架构 = 多 Agent 九角色；worker 不可用按节点接管并披露（详正文）。Routine 写盘（status.md / audits/）已声明；心跳为 opt-in「Operational Telemetry」。

Latest changelog:
- 发布面泄漏热修（P0）
- ① P0 · 维护者工程内档一直随发布包出厂（references/_shared/论衡仓库内教训.md）
- ② P1 · 净化规则误删「主控必读清单」的层 1 整行（同批实证）
- ③ 配套 6 条单测
- ④ 验收（实测回填 · 最终态）
- ⑤ changelog 分层轮转（同批收尾）
- 本批范围

**关键词**: 论衡, 严肃长文流水线, 学术论文, 深度长文, 行业分析流水线, 含同行评审与期刊, 发布渠道匹配建议（advisory）, 不调用执行类工具（exec

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lunheng-article-pipeline)

---

## [5. pmo-talk-skills](https://clawhub.ai/forrestneo/pmo-talk-skills)

**Slug**: `pmo-talk-skills`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把项目管理场景中的对话、聊天记录、邮件、会议纪要整理成有理有据的回怼与说服话术。自动诊断冲突场景，从7大沟通框架（PREP / RIDE / LEAPS / FFC / 30秒电梯演讲 / STAR / SCQA）中选型，生成可直接发送或说出的话术，附强硬备用版与对方反扑预案。Use whenever the user says 回怼、怼回去、怼他、怎么反驳、怎么回复、帮我回、说服对方、应对质疑、争取资源或预算、被甩锅、被甲方/领导/外包/跨部门施压，或 push back / persuade stakeholders——即使没有明说要用沟通框架。

**中文介绍**: 把项目管理场景中的对话、聊天记录、邮件、会议纪要整理成有理有据的回怼与说服话术。自动诊断冲突场景，从7大沟通框架（PREP / RIDE / LEAPS / FFC / 30秒电梯演讲 / STAR / SCQA）中选型，生成可直接发送或说出的话术，附强硬备用版与对方反扑预案。Use whenever the user says 回怼、怼回去、怼他、怎么反驳、怎么回复、帮我回、说服对方、应对质疑、争取资源或预算、被甩锅、被甲方/领导/外包/跨部门施压，或 push back / persuade stakeholders——即使没有明说要用沟通框架。

Latest changelog:
pmo-talk-skills 0.1.0

- 首发版本：自动将项目管理相关的对话、邮件、会议纪要等，结构化生成专业、可用的回怼与说服话术。
- 支持 7 大沟通框架（PREP / RIDE / LEAPS / FFC / 30秒电梯演讲 / STAR / SCQA），自动精准选型，按完整决策表匹配场景。
- 提供主话术、备用强硬/缓和版及反扑应对预案，覆盖专业、敏感及高压场景。
- 完善的证据核验流程，保证话术有理有据，无假设、无编造。
- 智能交互，自动提示信息缺失及补充证据，输出清晰明了，便于直接发送或口头表达。

**关键词**: 自动诊断冲突场景, 从7大沟通框架（PREP, 30秒电梯演讲, pmo-talk-skills, RIDE, LEAPS, FFC, STAR

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pmo-talk-skills)

---

## [6. SkillHub/ClawHub 技能发布](https://clawhub.ai/oracis/skillhub-publish-skill)

**Slug**: `skillhub-publish-skill`  
**Version**: 1.7.3  
**Stats**: ⭐ 1 | ⬇️ 77 | 🧩 13

**原始简介**: 把本地 Skill 打包并发布到 SkillHub（腾讯 skillhub.cn）与 ClawHub，覆盖预检、发布、状态回读与竞品对标全链路，并在上传被拒时用二分/ddmin 脚本把「服务端 WAF 拦内容（566）」与「包结构/字段问题」精确区分开。当用户说「发布技能到市场」「上架 skill」「SkillHub 提交失败」「Failed to fetch」「566」「上传 zip 报错」「技能审核状态」「版本号被拒」时使用。

**中文介绍**: 把本地 Skill 打包并发布到 SkillHub（腾讯 skillhub.cn）与 ClawHub，覆盖预检、发布、状态回读与竞品对标全链路，并在上传被拒时用二分/ddmin 脚本把「服务端 WAF 拦内容（566）」与「包结构/字段问题」精确区分开。当用户说「发布技能到市场」「上架 skill」「SkillHub 提交失败」「Failed to fetch」「566」「上传 zip 报错」「技能审核状态」「版本号被拒」时使用。

Latest changelog:
移除 slug 冲突自动换 slug/回写本地文件逻辑以通过安全扫描（T09），并补 ClawHub 分类（development）与话题

**关键词**: 技能发布, 把本地, 打包并发布到, SkillHub, ClawHub, Skill, SkillHub（腾讯, skillhub.cn）与

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skillhub-publish-skill)

---

## [7. 阿里云 OSS 静态站点部署](https://clawhub.ai/oracis/aliyun-oss-static-deploy-skill)

**Slug**: `aliyun-oss-static-deploy-skill`  
**Version**: 1.1.2  
**Stats**: ⭐ 0 | ⬇️ 154 | 🧩 4

**原始简介**: 把纯静态站点（dist/ 或 web/）部署到阿里云 OSS + 自定义域名 + HTTPS 证书，并打通 GitHub Actions 自动部署与证书自动续期。当用户说「推到阿里云 / 上线 / 部署到 OSS / 绑自定义域名 / 签 SSL 证书 / 配置 Actions 自动部署 / 静态站 HTTPS」时使用。

**中文介绍**: 把纯静态站点（dist/ 或 web/）部署到阿里云 OSS + 自定义域名 + HTTPS 证书，并打通 GitHub Actions 自动部署与证书自动续期。当用户说「推到阿里云 / 上线 / 部署到 OSS / 绑自定义域名 / 签 SSL 证书 / 配置 Actions 自动部署 / 静态站 HTTPS」时使用。

Latest changelog:
补 ClawHub 分类标签（operations）与话题

**关键词**: 阿里云, 静态站点部署, 把纯静态站点（dist, ）部署到阿里云, 自定义域名, OSS, web, HTTPS

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aliyun-oss-static-deploy-skill)

---

## [8. 阿里云通配证书自动续期](https://clawhub.ai/oracis/aliyun-oidc-cert-renew)

**Slug**: `aliyun-oidc-cert-renew`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 161 | 🧩 3

**原始简介**: 用 GitHub Actions + 阿里云 RAM OIDC 自动续期 Let's Encrypt 通配证书并分发到 OSS/FC/CDN，仓库零长期 AK。当用户说「自动续期证书」「不想存 AK」「GitHub Actions 操作阿里云」「SSL 证书过期」「新增子域自动上 HTTPS」「免密钥访问阿里云」时使用。

**中文介绍**: 用 GitHub Actions + 阿里云 RAM OIDC 自动续期 Let's Encrypt 通配证书并分发到 OSS/FC/CDN，仓库零长期 AK。当用户说「自动续期证书」「不想存 AK」「GitHub Actions 操作阿里云」「SSL 证书过期」「新增子域自动上 HTTPS」「免密钥访问阿里云」时使用。

Latest changelog:
补 ClawHub 分类标签（security）与话题

**关键词**: 阿里云通配证书自动续期, 阿里云, 自动续期, Actions, RAM, OIDC, Let's, Encrypt

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/aliyun-oidc-cert-renew)

---

## [9. 网页后台 CDP 自动上传](https://clawhub.ai/oracis/web-console-cdp-upload)

**Slug**: `web-console-cdp-upload`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 61 | 🧩 2

**原始简介**: 平台只有网页后台、没有上传 API 时，用本机已装的 Chrome/Edge + CDP 自动化走完上传/发布/填表流程——复用真实登录态、零安装（不下载 500MB Chromium）、能给文件选择框塞文件。当用户说「只能网页上传」「后台发布」「网页填表自动提交」「发布到技能市场/各平台控制台」「复用已登录的浏览器」时使用。

**中文介绍**: 平台只有网页后台、没有上传 API 时，用本机已装的 Chrome/Edge + CDP 自动化走完上传/发布/填表流程——复用真实登录态、零安装（不下载 500MB Chromium）、能给文件选择框塞文件。当用户说「只能网页上传」「后台发布」「网页填表自动提交」「发布到技能市场/各平台控制台」「复用已登录的浏览器」时使用。

Latest changelog:
补 ClawHub 分类标签（automation）与话题

**关键词**: 网页后台, 自动上传, 平台只有网页后台、没有上传, API, 用本机已装的, CDP, Chrome, Edge

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/web-console-cdp-upload)

---

## [10. 微信文件自动归类](https://clawhub.ai/oracis/wechat-file-organizer)

**Slug**: `wechat-file-organizer`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 208 | 🧩 3

**原始简介**: 微信文件自动归类（无头版）——扫描微信接收文件目录，按类型/月份归类、去重、生成报告。零依赖、默认只读（dry-run）、绝不永久删除源文件。扫描逻辑与 GUI 应用 wechat-file-organizer-gui（main.py）同步。

**中文介绍**: 微信文件自动归类（无头版）——扫描微信接收文件目录，按类型/月份归类、去重、生成报告。零依赖、默认只读（dry-run）、绝不永久删除源文件。扫描逻辑与 GUI 应用 wechat-file-organizer-gui（main.py）同步。

Latest changelog:
补 ClawHub 分类标签（productivity）

**关键词**: 微信文件自动归类, 按类型, 月份归类、去重、生成报告, 扫描逻辑与, 应用, GUI, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat-file-organizer)

---

## [11. WorkBuddy 每日签到领积分](https://clawhub.ai/skills?q=workbuddy-checkin)

**Slug**: `workbuddy-checkin`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 14 | 🧩 3

**原始简介**: 自动领取 WorkBuddy（原 CodeBuddy）每日签到积分。当用户说"领积分""自动领积分""签到""每日礼包""checkin""领取今日积分"，或定时任务要执行每日签到时使用。接口规格与脚本已固化，无需重新逆向客户端。

**中文介绍**: 自动领取 WorkBuddy（原 CodeBuddy）每日签到积分。当用户说"领积分""自动领积分""签到""每日礼包""checkin""领取今日积分"，或定时任务要执行每日签到时使用。接口规格与脚本已固化，无需重新逆向客户端。

Latest changelog:
补 ClawHub 分类标签（automation）与话题

**关键词**: 每日签到领积分, 自动领取, 或定时任务要执行每日签到时使用, 接口规格与脚本已固化, 无需重新逆向客户端, WorkBuddy, WorkBuddy（原, CodeBuddy）每日签到积分

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-checkin)

---

## [12. hyperframes-core](https://clawhub.ai/heygen-com/hyperframes-core)

**Slug**: `hyperframes-core`  
**Version**: 1.0.32  
**Stats**: ⭐ 0 | ⬇️ 2576 | 🧩 33

**原始简介**: The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.

**中文介绍**: The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.

Latest changelog:
Synced from 09aadd8 (main)

**关键词**: hyperframes-core, HyperFrames, composition, contract, build, one, renderable, project

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hyperframes-core)

---

## [13. 零依赖图标生成器](https://clawhub.ai/oracis/zero-dep-icon-gen)

**Slug**: `zero-dep-icon-gen`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 48 | 🧩 5

**原始简介**: 在完全不装任何三方库（无 Pillow / cairosvg / ImageMagick）的前提下，用标准库 zlib+struct 手写 PNG 编码器生成应用图标：圆角方形渐变底 + 白色实心剪影符号。当用户要"给工具/技能/应用生成图标""换个 icon""没有 Pillow 怎么画图""批量生成 favicon / 应用图标""icon 生成器"时使用。内置 10 个矢量符号（浏览器/云/盾牌/文件夹/对勾/下载/箭头/齿轮/放大镜/锁）+ 5x7 点阵文字，支持任意尺寸与超采样抗锯齿。

**中文介绍**: 在完全不装任何三方库（无 Pillow / cairosvg / ImageMagick）的前提下，用标准库 zlib+struct 手写 PNG 编码器生成应用图标：圆角方形渐变底 + 白色实心剪影符号。当用户要"给工具/技能/应用生成图标""换个 icon""没有 Pillow 怎么画图""批量生成 favicon / 应用图标""icon 生成器"时使用。内置 10 个矢量符号（浏览器/云/盾牌/文件夹/对勾/下载/箭头/齿轮/放大镜/锁）+ 5x7 点阵文字，支持任意尺寸与超采样抗锯齿。

Latest changelog:
补充分类（Development）与话题标签；修正发布说明

**关键词**: 零依赖图标生成器, 在完全不装任何三方库（无, 用标准库, 手写, Pillow, cairosvg, ImageMagick）的前提下, zlib+struct

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/zero-dep-icon-gen)

---

## [14. anti-ai-foolish](https://clawhub.ai/forrestneo/anti-ai-foolish)

**Slug**: `anti-ai-foolish`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 18 | 🧩 1

**原始简介**: Pre-publish AI-flavor gatekeeper for Chinese long-form articles (公众号/自媒体评论). Detects and removes AI-writing tells using 1,108 rules that were A/B-validated on 52 real Tencent Zhuque detector-labeled fragments. Use whenever the user asks to 去AI味, 去AI, 降AI率, 终检/检查一篇文章 before publishing, or mentions an article was flagged or rejected by WeChat (微信打回) or Zhuque (朱雀) as AI-generated — even if they only say "这篇文章帮我看看".

**中文介绍**: Pre-publish AI-flavor gatekeeper for Chinese long-form articles (公众号/自媒体评论). Detects and removes AI-writing tells using 1,108 rules that were A/B-validated on 52 real Tencent Zhuque detector-labeled fragments. Use whenever the user asks to 去AI味, 去AI, 降AI率, 终检/检查一篇文章 before publishing, or mentions an article was flagged or rejected by WeChat (微信打回) or Zhuque (朱雀) as AI-generated — even if they only say "这篇文章帮我看看".

Latest changelog:
- Initial release of anti-ai-foolish, a pre-publish gatekeeper for Chinese long-form articles to detect and remove AI-writing indicators.
- Uses 1,108 evidence-backed, A/B-validated rules tested against 52 Tencent Zhuque detector-labeled fragments.
- Introduces a two-step workflow: mechanical gates (punctuation, quoting, Z-score) and human judgment checks.
- Provides clear workflow for detection, repair ("七刀手术"), and final platform testing.
- Designed for Chinese commentary genres, not for fiction, academic, or English-language texts.

**关键词**: 公众号, anti-ai-foolish, Pre-publish, AI-flavor, gatekeeper, Chinese, long-form, articles

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/anti-ai-foolish)

---

## [15. OpenClaw Token Optimizer](https://clawhub.ai/asif2bd/openclaw-token-optimizer)

**Slug**: `openclaw-token-optimizer`  
**Version**: 4.0.1  
**Stats**: ⭐ 30 | ⬇️ 12900 | 🧩 22

**原始简介**: Audit OpenClaw model routes, context and automations; produce read-only, evidence-based optimization plans without guessing savings or changing configuration.

**中文介绍**: Audit OpenClaw model routes, context and automations; produce read-only, evidence-based optimization plans without guessing savings or changing configuration.

Latest changelog:
v4.0.1: Includes the v4 native read-only audit core and ships registry-compatible LICENSE.txt and SHA256SUMS.txt. Pinned installation example; no runtime behavior changes from v4.0.0.

**关键词**: OpenClaw, Token, Optimizer, Audit, model, routes, context, automations

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-token-optimizer)

---

## [16. 关联方资金占用与往来清理核对（免费版）](https://clawhub.ai/chenqg618/related-party-fund-occupation-check-free)

**Slug**: `related-party-fund-occupation-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 103 | 🧩 3

**原始简介**: 关联方往来台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 关联方资金占用与往来清理核对、关联方往来台账对不上。

**中文介绍**: 关联方往来台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 关联方资金占用与往来清理核对、关联方往来台账对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 关联方资金占用与往来清理核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/related-party-fund-occupation-check-free)

---

## [17. 销售返利与渠道返点核对（免费版）](https://clawhub.ai/chenqg618/sales-rebate-check-free)

**Slug**: `sales-rebate-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 102 | 🧩 3

**原始简介**: 返利台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 销售返利与渠道返点核对、返利台账对不上。

**中文介绍**: 返利台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 销售返利与渠道返点核对、返利台账对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 销售返利与渠道返点核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 销售返利与渠道返点核对、返利台账对不上, 正文新增「免费网页版」入口, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/sales-rebate-check-free)

---

## [18. 研发费用辅助账与高新指标核对（免费版）](https://clawhub.ai/chenqg618/rd-auxiliary-ledger-check-free)

**Slug**: `rd-auxiliary-ledger-check-free`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 98 | 🧩 3

**原始简介**: 研发费用辅助账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 研发费用辅助账与高新指标核对、研发费用辅助账对不上。

**中文介绍**: 研发费用辅助账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 研发费用辅助账与高新指标核对、研发费用辅助账对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 研发费用辅助账与高新指标核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rd-auxiliary-ledger-check-free)

---

## [19. 研发支出资本化与费用化划分核对（免费版）](https://clawhub.ai/chenqg618/rd-capitalization-check-free)

**Slug**: `rd-capitalization-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 114 | 🧩 4

**原始简介**: 研发支出明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 研发支出资本化与费用化划分核对、研发支出明细表对不上。

**中文介绍**: 研发支出明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 研发支出资本化与费用化划分核对、研发支出明细表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 研发支出资本化与费用化划分核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rd-capitalization-check-free)

---

## [20. 实收资本与股东出资核对（免费版）](https://clawhub.ai/chenqg618/paid-in-capital-check-free)

**Slug**: `paid-in-capital-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 62 | 🧩 3

**原始简介**: 股东出资明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 实收资本与股东出资核对、股东出资明细表对不上。

**中文介绍**: 股东出资明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 实收资本与股东出资核对、股东出资明细表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 实收资本与股东出资核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 实收资本与股东出资核对、股东出资明细表对不上, 正文新增「免费网页版」入口, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paid-in-capital-check-free)

---

## [21. 非经常性损益与扣非净利润核对（免费版）](https://clawhub.ai/chenqg618/non-recurring-gain-loss-check-free)

**Slug**: `non-recurring-gain-loss-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 61 | 🧩 3

**原始简介**: 非经常性损益明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 非经常性损益与扣非净利润核对、非经常性损益明细表对不上。

**中文介绍**: 非经常性损益明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 非经常性损益与扣非净利润核对、非经常性损益明细表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 非经常性损益与扣非净利润核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/non-recurring-gain-loss-check-free)

---

## [22. 低值易耗品与周转材料摊销核对（免费版）](https://clawhub.ai/chenqg618/low-value-consumables-check-free)

**Slug**: `low-value-consumables-check-free`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 114 | 🧩 5

**原始简介**: 低值易耗品台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 低值易耗品与周转材料摊销核对、低值易耗品台账对不上。

**中文介绍**: 低值易耗品台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 低值易耗品与周转材料摊销核对、低值易耗品台账对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 低值易耗品与周转材料摊销核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/low-value-consumables-check-free)

---

## [23. 存货盘点差异与账实调整核对（免费版）](https://clawhub.ai/chenqg618/inventory-count-variance-check-free)

**Slug**: `inventory-count-variance-check-free`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 113 | 🧩 4

**原始简介**: 存货盘点表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 存货盘点差异与账实调整核对、存货盘点表对不上。

**中文介绍**: 存货盘点表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 存货盘点差异与账实调整核对、存货盘点表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 存货盘点差异与账实调整核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 存货盘点差异与账实调整核对、存货盘点表对不上, 正文新增「免费网页版」入口, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/inventory-count-variance-check-free)

---

## [24. 个税年度汇算（综合所得）核对（免费版）](https://clawhub.ai/chenqg618/iit-annual-settlement-check-free)

**Slug**: `iit-annual-settlement-check-free`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 106 | 🧩 4

**原始简介**: 个税年度汇算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 个税年度汇算（综合所得）核对、个税年度汇算表对不上。

**中文介绍**: 个税年度汇算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 个税年度汇算（综合所得）核对、个税年度汇算表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 个税年度汇算（综合所得）核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 正文新增「免费网页版」入口, 名称取自, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/iit-annual-settlement-check-free)

---

## [25. 长期股权投资权益法核对（免费版）](https://clawhub.ai/chenqg618/equity-method-investment-check-free)

**Slug**: `equity-method-investment-check-free`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 67 | 🧩 4

**原始简介**: 权益法核算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 长期股权投资权益法核对、权益法核算表对不上。

**中文介绍**: 权益法核算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 长期股权投资权益法核对、权益法核算表对不上。

Latest changelog:
正文新增「免费网页版」入口；名称取自 SKILL.md

**关键词**: 长期股权投资权益法核对（免费版）, 每条结论引用原文, 本免费版执行引擎声明的免费检查项, 触发词包括, 长期股权投资权益法核对、权益法核算表对不上, 正文新增「免费网页版」入口, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/equity-method-investment-check-free)

---

