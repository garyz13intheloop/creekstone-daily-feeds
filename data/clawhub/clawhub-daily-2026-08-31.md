# ClawHub Skills Daily | 2026-08-31

> 共 25 个 skills

## [1. Handoff Installer](https://clawhub.ai/snowsonz/agent-handoff)

**Slug**: `agent-handoff`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Install or update a repository handoff protocol

**中文介绍**: Install or update a repository handoff protocol

Latest changelog:
Initial public release

**关键词**: or, Handoff, Installer, Install, update, protocol, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-handoff)

---

## [2. honeybook](https://clawhub.ai/chrischall/honeybook)

**Slug**: `honeybook`  
**Version**: 0.7.1  
**Stats**: ⭐ 0 | ⬇️ 1134 | 🧩 15

**原始简介**: This skill should be used when the user asks about HoneyBook client-portal data. Triggers on phrases like "check HoneyBook", "sign contract", "pay invoice", "HoneyBook vendors", "unsigned contracts", "open invoices", or any request involving wedding-vendor contracts, invoices, brochures, proposals, or payments via HoneyBook.

**中文介绍**: This skill should be used when the user asks about HoneyBook client-portal data. Triggers on phrases like "check HoneyBook", "sign contract", "pay invoice", "HoneyBook vendors", "unsigned contracts", "open invoices", or any request involving wedding-vendor contracts, invoices, brochures, proposals, or payments via HoneyBook.

Latest changelog:
- Removed the skill-card.md file.
- No user-facing functionality changes; all skill features remain the same.

**关键词**: be, honeybook, skill, should, used, when, user, asks

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/honeybook)

---

## [3. honeybook-fpx](https://clawhub.ai/chrischall/honeybook-fpx)

**Slug**: `honeybook-fpx`  
**Version**: 0.7.1  
**Stats**: ⭐ 0 | ⬇️ 117 | 🧩 4

**原始简介**: Read HoneyBook client-portal data (contracts, invoices, proposals, payment methods, workspace status) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the honeybook-mcp server — capture a vendor session once via the signed-in browser tab, then curl api.honeybook.com directly. Use when you want HoneyBook data without the MCP, in a script, or on a machine where the MCP isn't installed.

**中文介绍**: Read HoneyBook client-portal data (contracts, invoices, proposals, payment methods, workspace status) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the honeybook-mcp server — capture a vendor session once via the signed-in browser tab, then curl api.honeybook.com directly. Use when you want HoneyBook data without the MCP, in a script, or on a machine where the MCP isn't installed.

Latest changelog:
- Removed the sample file skill-card.md.
- No changes were made to the implementation or documentation in SKILL.md.

**关键词**: honeybook-fpx, Read, HoneyBook, client-portal, data, contracts, invoices, proposals

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/honeybook-fpx)

---

## [4. Nano (XNO)](https://clawhub.ai/casualsecurityinc/nano)

**Slug**: `nano`  
**Version**: 4.7.5  
**Stats**: ⭐ 0 | ⬇️ 3010 | 🧩 58

**原始简介**: Nano (XNO) cryptocurrency wallet operations, transaction analysis, and explorer lookups. Use for send/receive, balances, pending funds, address validation, unit conversion, tx/hash/account lookup, explorer links, and Nano block-lattice questions. Prefer xno-mcp first; use xno-skills CLI as fallback. Configured OWS wallets ARE the assistant's own wallets — never claim you cannot receive or hold Nano.

**中文介绍**: Nano (XNO) cryptocurrency wallet operations, transaction analysis, and explorer lookups. Use for send/receive, balances, pending funds, address validation, unit conversion, tx/hash/account lookup, explorer links, and Nano block-lattice questions. Prefer xno-mcp first; use xno-skills CLI as fallback. Configured OWS wallets ARE the assistant's own wallets — never claim you cannot receive or hold Nano.

Latest changelog:
Automated publish from 70ccb75a35430047c7ed3a6bb692e127e79c135b

**关键词**: Nano, XNO, cryptocurrency, wallet, operations, transaction, analysis, explorer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nano)

---

## [5. 元阁 yotta-skills](https://clawhub.ai/skills?q=yotta-skills)

**Slug**: `yotta-skills`  
**Version**: 0.5.0  
**Stats**: ⭐ 0 | ⬇️ 125 | 🧩 9

**原始简介**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么自动装+自动用」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工可先跑 --reindex；自包含零依赖，不依赖任何元技能）；MCP 按需加载（可选：list_installed_skills/describe_skill/reindex/route_request，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / install / update / --inventory / --reindex / --dry-run 预览 / --pin 锁版本。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/该用哪个技能/路由技能/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能；装前摘要仅供参考，安装决策由用户确认。

**中文介绍**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么自动装+自动用」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工可先跑 --reindex；自包含零依赖，不依赖任何元技能）；MCP 按需加载（可选：list_installed_skills/describe_skill/reindex/route_request，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / install / update / --inventory / --reindex / --dry-run 预览 / --pin 锁版本。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/该用哪个技能/路由技能/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能；装前摘要仅供参考，安装决策由用户确认。

Latest changelog:
yotta-skills 0.5.0

- --route / route_request 输出新增「其他已装技能候选」：注册表中非元阁家族已装技能按 frontmatter description 与需求文本本地机械匹配（英文词项 + 中文二字组交集），Top N 默认 3，标注来源/得分/命中词项/扫描状态（未扫描）；只读不自动调用。
- 7 个静态编排组合输出不变；候选仅供参考、装前决策由用户确认。
- 测试 41/41 全绿。

**关键词**: 元阁, 元阁全家技能的总编排策划, 编排路由, 一键安装器, 技能盘点, 路由层, yotta-skills, route

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-skills)

---

## [6. file-organizer](https://clawhub.ai/zoeee886/file-organizer)

**Slug**: `file-organizer`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Sort and organize files in a directory by type or by modification date, with dry-run preview, duplicate-name handling, and an auto-generated organization report. Use when the user wants to clean up, sort, categorize, or organize files in a folder, or asks for a file classification/overview report.

**中文介绍**: Sort and organize files in a directory by type or by modification date, with dry-run preview, duplicate-name handling, and an auto-generated organization report. Use when the user wants to clean up, sort, categorize, or organize files in a folder, or asks for a file classification/overview report.

Latest changelog:
Version 0.1.1

- No changes detected from the previous version.
- Functionality and documentation remain the same as in version 1.0.0.

**关键词**: or, file-organizer, Sort, organize, files, directory, type, modification

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/file-organizer)

---

## [7. 微信连接](https://clawhub.ai/skills?q=wechat)

**Slug**: `wechat`  
**Version**: 2.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Install OpenClaw's official WeChat plugin and complete account pairing via QR code scan. Triggers when the user says "install WeChat plugin", "connect WeChat", or "WeChat QR code". No command-line interaction required.

**中文介绍**: Install OpenClaw's official WeChat plugin and complete account pairing via QR code scan. Triggers when the user says "install WeChat plugin", "connect WeChat", or "WeChat QR code". No command-line interaction required.

Latest changelog:
安装OpenClaw官方微信插件并扫码配对

**关键词**: 微信连接, Install, OpenClaw's, official, WeChat, plugin, complete, account

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/wechat)

---

## [8. 手机操控](https://clawhub.ai/skills?q=phone-agent)

**Slug**: `phone-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 手机操控技能。通过 USB ADB 连接安卓手机，捕获屏幕、分析 UI 元素、执行点击/滑动/输入等操作。当用户要求操控手机、执行 App 操作、打开应用、发送消息时使用。

**中文介绍**: 手机操控技能。通过 USB ADB 连接安卓手机，捕获屏幕、分析 UI 元素、执行点击/滑动/输入等操作。当用户要求操控手机、执行 App 操作、打开应用、发送消息时使用。

Latest changelog:
通过 USB ADB 控制安卓手机:截图/UI分析/点击滑动/输入

**关键词**: 手机操控, 手机操控技能, 通过, 连接安卓手机, 捕获屏幕、分析, UI, USB, ADB

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/phone-agent)

---

## [9. 3X-UI代理面板](https://clawhub.ai/lanlan314/3x-ui)

**Slug**: `3x-ui`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 3x-ui面板REST API交互。用于管理Xray代理面板的入站/出站配置、客户端(用户)管理、节点管理、服务器状态监控、订阅管理、备份等功能。当用户需要操作3x-ui面板、查询代理服务器状态、管理用户/流量/订阅链接时使用。支持Bearer Token和Session Cookie两种认证方式。

**中文介绍**: 3x-ui面板REST API交互。用于管理Xray代理面板的入站/出站配置、客户端(用户)管理、节点管理、服务器状态监控、订阅管理、备份等功能。当用户需要操作3x-ui面板、查询代理服务器状态、管理用户/流量/订阅链接时使用。支持Bearer Token和Session Cookie两种认证方式。

Latest changelog:
3x-ui 面板 REST API 交互技能:管理入站/出站、用户、节点、订阅、备份

**关键词**: 3X-UI代理面板, 用于管理Xray代理面板的入站, 出站配置、客户端, 用户, 流量, 订阅链接时使用, 3x-ui面板REST, API交互

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/3x-ui)

---

## [10. Weekly Report](https://clawhub.ai/zoeee886/weekly-report-2)

**Slug**: `weekly-report-2`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Generate structured weekly work reports from Git commit history and file-change statistics. Use when the user asks for a weekly report, work summary, progress review, or sprint recap based on repository activity, or when they need a Markdown report of what changed in a project over a time range.

**中文介绍**: Generate structured weekly work reports from Git commit history and file-change statistics. Use when the user asks for a weekly report, work summary, progress review, or sprint recap based on repository activity, or when they need a Markdown report of what changed in a project over a time range.

Latest changelog:
Initial release: Generate structured weekly work reports from Git history.

- Supports Markdown reports summarizing project activity over a given time range.
- Collects commit history, file-change statistics, and contributor summaries.
- Works with filters for repository path, days to cover, and author.
- Provides a fallback method for non-Git folders, using file modification times.
- Includes a ready-made PowerShell script for automated report generation on Windows.
- Uses a standardized, bilingual report template for consistency.

**关键词**: Weekly, Report, Generate, structured, work, reports, Git, commit

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/weekly-report-2)

---

## [11. 盘前雷达](https://clawhub.ai/xiyanjun/hectorlee-global-risk-signal)

**Slug**: `hectorlee-global-risk-signal`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 93 | 🧩 3

**原始简介**: A股盘前外围风险信号雷达。聚合外围行情(A50期货/纳指期货/离岸人民币/美元指数/VIX/美债10Y)、地缘事件(GDELT)、财经日历(华尔街见闻)、中国资金面(两融/龙虎榜/沪深港通)、国内新闻(中新网/东财快讯/新浪滚动)、宏观数据(东财PMI/CPI/PPI+World Bank)六大维度，做多空情景推演打分，输出方向判断+1-5级风险分级+可分享信号卡，支持推送飞书群。MIT开源免费、零第三方依赖、无key开箱即用。触发词：盘前雷达、盘前信号、外围风险、全球风险、外围市场、今晚外围、盘前外围、风险信号、今日外围、外围异动。

**中文介绍**: A股盘前外围风险信号雷达。聚合外围行情(A50期货/纳指期货/离岸人民币/美元指数/VIX/美债10Y)、地缘事件(GDELT)、财经日历(华尔街见闻)、中国资金面(两融/龙虎榜/沪深港通)、国内新闻(中新网/东财快讯/新浪滚动)、宏观数据(东财PMI/CPI/PPI+World Bank)六大维度，做多空情景推演打分，输出方向判断+1-5级风险分级+可分享信号卡，支持推送飞书群。MIT开源免费、零第三方依赖、无key开箱即用。触发词：盘前雷达、盘前信号、外围风险、全球风险、外围市场、今晚外围、盘前外围、风险信号、今日外围、外围异动。

Latest changelog:
- Removed the file skill-card.md.
- No user-facing changes or feature updates.

**关键词**: 盘前雷达, A股盘前外围风险信号雷达, 聚合外围行情, A50期货, 纳指期货, 离岸人民币, 美元指数, VIX

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/hectorlee-global-risk-signal)

---

## [12. 小米MiMo语音](https://clawhub.ai/skills?q=mimo-tts)

**Slug**: `mimo-tts`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 小米MiMo语音合成（TTS）技能，支持将文本转换为自然语音。当用户要求朗读、语音合成、文字转语音、TTS、读一段话、把文字转成声音时使用（作为千问TTS的备选方案）。

**中文介绍**: 小米MiMo语音合成（TTS）技能，支持将文本转换为自然语音。当用户要求朗读、语音合成、文字转语音、TTS、读一段话、把文字转成声音时使用（作为千问TTS的备选方案）。

Latest changelog:
小米 MiMo V2.5 TTS 语音合成技能,中文/英文音色

**关键词**: 小米MiMo语音合成（TTS）技能, 支持将文本转换为自然语音, 小米, V2.5, 小米MiMo语音, Latest, changelog, MiMo

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mimo-tts)

---

## [13. 千问语音合成](https://clawhub.ai/skills?q=qwen-tts)

**Slug**: `qwen-tts`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 阿里云千问语音合成（TTS）技能。**核心用途**：将文字结果转换为语音并发送出去（每次输出结果前必须使用）。首选千问 TTS（qwen3-tts-flash + Nofish 音色），失败时使用 Edge TTS。

**中文介绍**: 阿里云千问语音合成（TTS）技能。**核心用途**：将文字结果转换为语音并发送出去（每次输出结果前必须使用）。首选千问 TTS（qwen3-tts-flash + Nofish 音色），失败时使用 Edge TTS。

Latest changelog:
Alibaba 通义千问 TTS 语音合成技能,支持多种中文/英文音色

**关键词**: 千问语音合成, 阿里云千问语音合成（TTS）技能, 核心用途, 首选千问, 音色）, 失败时使用, TTS（qwen3-tts-flash, Nofish

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qwen-tts)

---

## [14. n8n工作流管理](https://clawhub.ai/skills?q=n8n-mcp)

**Slug**: `n8n-mcp`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 通过 n8n MCP server (http://localhost:5678/mcp-server/http) 用 n8n Workflow SDK 创建/校验/发布/管理工作流

**中文介绍**: 通过 n8n MCP server (http://localhost:5678/mcp-server/http) 用 n8n Workflow SDK 创建/校验/发布/管理工作流

Latest changelog:
通过 n8n MCP 以编程方式创建/校验/管理工作流

**关键词**: n8n工作流管理, 通过, n8n, SDK, 创建, MCP, server, Workflow

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/n8n-mcp)

---

## [15. 千问生图](https://clawhub.ai/skills?q=qwen-image-gen)

**Slug**: `qwen-image-gen`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 阿里云千问文生图模型（Qwen-Image）技能，支持图像生成。当用户要求AI生成图片、画图、文生图、text-to-image，或提到千问、阿里云生图时使用。支持中英文提示词，可指定画面尺寸、风格参数等。

**中文介绍**: 阿里云千问文生图模型（Qwen-Image）技能，支持图像生成。当用户要求AI生成图片、画图、文生图、text-to-image，或提到千问、阿里云生图时使用。支持中英文提示词，可指定画面尺寸、风格参数等。

Latest changelog:
Alibaba 通义千问图像生成技能

**关键词**: 千问生图, 阿里云千问文生图模型（Qwen-Image）技能, 支持图像生成, 或提到千问、阿里云生图时使用, 支持中英文提示词, 可指定画面尺寸、风格参数等, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/qwen-image-gen)

---

## [16. 高德地图](https://clawhub.ai/skills?q=amap)

**Slug**: `amap`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 高德地图 API 技能，支持路径规划、距离计算、地理位置搜索等。用于查询两地之间的骑行/驾车/步行路线、距离、时间等实时信息。需要配置高德地图 API Key（AMAP_API_KEY）。

**中文介绍**: 高德地图 API 技能，支持路径规划、距离计算、地理位置搜索等。用于查询两地之间的骑行/驾车/步行路线、距离、时间等实时信息。需要配置高德地图 API Key（AMAP_API_KEY）。

Latest changelog:
高德地图 API 技能:路线规划/地理编码/POI搜索

**关键词**: 高德地图, API, 技能, 支持路径规划、距离计算、地理位置搜索等, 用于查询两地之间的骑行, 驾车, 步行路线、距离、时间等实时信息, 需要配置高德地图

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/amap)

---

## [17. bus-servo-arm-calibrate](https://clawhub.ai/sharinchan233/bus-servo-arm-calibrate)

**Slug**: `bus-servo-arm-calibrate`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Calibrate a multi-DOF bus-servo robotic arm (Hiwonder-style, I2C/servo channels, no position readback) when you cannot read servo angles back and must confirm by eye. Provides the channel-to-joint mapping, the lift-hold-confirm interactive tuning loop, a place-and-home placement test, per-slot param

**中文介绍**: Calibrate a multi-DOF bus-servo robotic arm (Hiwonder-style, I2C/servo channels, no position readback) when you cannot read servo angles back and must confirm by eye. Provides the channel-to-joint mapping, the lift-hold-confirm interactive tuning loop, a place-and-home placement test, per-slot param

Latest changelog:
Initial release of bus-servo-arm-calibrate skill.

- Provides methodology to calibrate Hiwonder-style multi-DOF bus-servo arms without servo angle readback.
- Includes interactive lift-hold-confirm tuning loop for manual grasp verification.
- Details channel-to-joint mapping and direction pitfalls.
- Describes placement calibration, per-slot parameter storage, and diagnosis of common grasping/placement failures.
- Offers guidance for handling multi-row slot layouts and finalizing calibration data.

**关键词**: I2C, bus-servo-arm-calibrate, Calibrate, multi-DOF, bus-servo, robotic, arm, Hiwonder-style

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bus-servo-arm-calibrate)

---

## [18. paste-safe-pi](https://clawhub.ai/sharinchan233/paste-safe-pi)

**Slug**: `paste-safe-pi`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Emit shell commands that survive being pasted into a remote terminal (e.g. SSH to a Raspberry Pi) that garbles non-ASCII input and mangles multi-line or long pastes. Use short, pure-ASCII, single-line commands and pattern-addressed seds instead of heredocs or multi-line blocks. Use when the user pas

**中文介绍**: Emit shell commands that survive being pasted into a remote terminal (e.g. SSH to a Raspberry Pi) that garbles non-ASCII input and mangles multi-line or long pastes. Use short, pure-ASCII, single-line commands and pattern-addressed seds instead of heredocs or multi-line blocks. Use when the user pas

Latest changelog:
Initial release of paste-safe-pi: robust shell commands for error-prone pasting into remote terminals.

- Emits pure ASCII, single-line shell commands safe for hand-pasting into remote Pi/SSH terminals.
- Avoids non-ASCII, heredocs, and multi-line blocks; edits files with short, pattern-addressed `sed -i` commands.
- Provides verification steps by reading back changes after each edit.
- Instructions tailored for scenarios where pasting multi-line or non-ASCII input fails.

**关键词**: paste-safe-pi, Emit, shell, commands, survive, being, pasted, remote

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paste-safe-pi)

---

## [19. skill-studio](https://clawhub.ai/skills?q=skill-studio)

**Slug**: `skill-studio`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 用 5种设计模式诊断并生成 Agent Skill。触发：创建/新建/重构/审计 skill。覆盖诊断→架构→起草→校验→打包。

**中文介绍**: 用 5种设计模式诊断并生成 Agent Skill。触发：创建/新建/重构/审计 skill。覆盖诊断→架构→起草→校验→打包。

Latest changelog:
Initial public release of skill-studio — a meta-skill for designing, generating, and auditing Agent Skills using 5 core design patterns.

- Guides users through a full SOP: diagnosis, pattern selection, architecture, drafting, validation, packaging, and installation.
- Provides detailed rules, anti-patterns, and scripts for deterministic skill creation and review.
- Enforces strict compliance via scripts (`validate.py`, `diagnose.py`, `audit.py`, etc.), moving beyond prompt-based enforcement.
- Includes modular design references and templates for Tool Wrapper, Generator, Reviewer, Inversion, and Pipeline patterns.
- Designed for self-bootstrapping: skill-studio itself follows all enforced conventions.

**关键词**: 5种设计模式诊断并生成, Agent, 触发, 创建, 新建, 重构, skill-studio, Skill

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-studio)

---

## [20. house-skills-kit](https://clawhub.ai/danfeistar/house-skills-kit)

**Slug**: `house-skills-kit`  
**Version**: 1.4.1  
**Stats**: ⭐ 0 | ⬇️ 132 | 🧩 6

**原始简介**: 房产AI技能仓库总览：按身份分技能（房开企业/经纪公司/渠道分销/购房者业主/二手经纪人/一手销售/房产自媒体）。已发布calc-toolkit公共计算工具包（19件收官：房贷月供/二手房全成本/一手房成本/购房能力/提前还款/首套二套认定/楼层折扣/公积金额度/佣金提成/得房率换算/租金回报/LPR变动影响/持有成本/买房vs理财/面积误差补退/违约金定金/房龄贷款年限/楼面价货值/日照楼间距，35城规则库四层引擎，每个数字可追溯）；template/为品牌顾问技能生成骨架（4类角色原型×29业务模块）。Use when 需要房产相关AI技能的安装、使用、生成或按身份选型。

**中文介绍**: 房产AI技能仓库总览：按身份分技能（房开企业/经纪公司/渠道分销/购房者业主/二手经纪人/一手销售/房产自媒体）。已发布calc-toolkit公共计算工具包（19件收官：房贷月供/二手房全成本/一手房成本/购房能力/提前还款/首套二套认定/楼层折扣/公积金额度/佣金提成/得房率换算/租金回报/LPR变动影响/持有成本/买房vs理财/面积误差补退/违约金定金/房龄贷款年限/楼面价货值/日照楼间距，35城规则库四层引擎，每个数字可追溯）；template/为品牌顾问技能生成骨架（4类角色原型×29业务模块）。Use when 需要房产相关AI技能的安装、使用、生成或按身份选型。

Latest changelog:
安全加固: 规则模板路径收敛到my_templates/内(防目录穿越与任意文件读); render.py输出/配置限定仓库内

**关键词**: 房产AI技能仓库总览, 按身份分技能（房开企业, 经纪公司, 渠道分销, 购房者业主, 二手经纪人, 一手销售, house-skills-kit

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/house-skills-kit)

---

## [21. Flowering Date Prediction | 开花植物花期预测](https://clawhub.ai/18072937735/smyx-flowering-date-prediction-analysis)

**Slug**: `smyx-flowering-date-prediction-analysis`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 1123 | 🧩 8

**原始简介**: AI-powered flowering-date prediction for ornamental/cut-flower plants. From fixed greenhouse cameras or drones, captures images of flower-bud developmental stages, combines environmental sensor data — cumulative temperature (Growing Degree Days, GDD) and accumulated light (PAR or daylight hours) — and uses a pre-trained phenology model to predict the full-bloom date within the next 3-7 days. Helps growers precisely schedule pollination, harvesting and tourism activities. Scenarios: smart-agriculture greenhouses, cut-flower production bases, botanical gardens, flower tourism parks. | 通过智慧农业温室中的固定摄像头或无人机拍摄植物花蕾发育阶段的图像，并结合环境传感器提供的温度累积（生长度日，GDD）、光照累积（光合有效辐射或日照时长）等数据，利用预训练的物候模型预测未来3-7天内的开花日期（花朵完全开放）。该技能有助于温室种植者精准安排授粉、采收或观光活动。应用场景：智慧农业温室、切花生产基地、植物园、花卉观光园区。

**中文介绍**: AI-powered flowering-date prediction for ornamental/cut-flower plants. From fixed greenhouse cameras or drones, captures images of flower-bud developmental stages, combines environmental sensor data — cumulative temperature (Growing Degree Days, GDD) and accumulated light (PAR or daylight hours) — and uses a pre-trained phenology model to predict the full-bloom date within the next 3-7 days. Helps growers precisely schedule pollination, harvesting and tourism activities. Scenarios: smart-agriculture greenhouses, cut-flower production bases, botanical gardens, flower tourism parks. | 通过智慧农业温室中的固定摄像头或无人机拍摄植物花蕾发育阶段的图像，并结合环境传感器提供的温度累积（生长度日，GDD）、光照累积（光合有效辐射或日照时长）等数据，利用预训练的物候模型预测未来3-7天内的开花日期（花朵完全开放）。该技能有助于温室种植者精准安排授粉、采收或观光活动。应用场景：智慧农业温室、切花生产基地、植物园、花卉观光园区。

Latest changelog:
- Updated version and metadata in SKILL.md.
- Minor documentation and formatting adjustments in SKILL.md.
- Removed redundant file: skill-card.md.
- Kept configuration (config.yaml) and documentation in sync with skill updates.

**关键词**: 开花植物花期预测, Flowering, Date, Prediction, AI-powered, flowering-date, ornamental, cut-flower

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-flowering-date-prediction-analysis)

---

## [22. nv-segment-ct-finetune](https://clawhub.ai/nvidia/nv-segment-ct-finetune)

**Slug**: `nv-segment-ct-finetune`  
**Version**: -  
**Stats**: ⭐ 0 | ⬇️ 263 | 🧩 0

**原始简介**: Runs standard or fixed-channel softmax finetuning of NV-Segment-CT VISTA3D on CT NIfTI image/label datasets, with optional MONAI-native MLflow tracking and checkpoint evidence. Uses softmax for predefined, mutually exclusive classes; keeps the standard workflow when point prompts or runtime-variable classes are needed. Not for clinical validation.

**中文介绍**: Runs standard or fixed-channel softmax finetuning of NV-Segment-CT VISTA3D on CT NIfTI image/label datasets, with optional MONAI-native MLflow tracking and checkpoint evidence. Uses softmax for predefined, mutually exclusive classes; keeps the standard workflow when point prompts or runtime-variable classes are needed. Not for clinical validation.

**关键词**: or, of, nv-segment-ct-finetune, Runs, standard, fixed-channel, softmax, finetuning

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nv-segment-ct-finetune)

---

## [23. nv-generate-mr-brain-finetune](https://clawhub.ai/nvidia/nv-generate-mr-brain-finetune)

**Slug**: `nv-generate-mr-brain-finetune`  
**Version**: -  
**Stats**: ⭐ 0 | ⬇️ 613 | 🧩 0

**原始简介**: Used for finetuning NV-Generate-CTMR MR-Brain v1 for T1, T2, FLAIR, SWI, or MRA data from a NIfTI datalist. Not for clinical or production data approval.

**中文介绍**: Used for finetuning NV-Generate-CTMR MR-Brain v1 for T1, T2, FLAIR, SWI, or MRA data from a NIfTI datalist. Not for clinical or production data approval.

**关键词**: v1, T1, T2, Used, finetuning, NV-Generate-CTMR, MR-Brain, FLAIR

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nv-generate-mr-brain-finetune)

---

## [24. dicom-series-preflight](https://clawhub.ai/nvidia/dicom-series-preflight)

**Slug**: `dicom-series-preflight`  
**Version**: -  
**Stats**: ⭐ 0 | ⬇️ 579 | 🧩 0

**原始简介**: Used for header-only preflight of one DICOM series folder before conversion or inference. Not for de-identification or clinical clearance.

**中文介绍**: Used for header-only preflight of one DICOM series folder before conversion or inference. Not for de-identification or clinical clearance.

**关键词**: of, dicom-series-preflight, Used, header-only, preflight, one, DICOM, series

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dicom-series-preflight)

---

## [25. nv-generate-mr-brain](https://clawhub.ai/nvidia/nv-generate-mr-brain)

**Slug**: `nv-generate-mr-brain`  
**Version**: -  
**Stats**: ⭐ 0 | ⬇️ 617 | 🧩 0

**原始简介**: Used for generating synthetic T1, T2, FLAIR, SWI, or MRA brain MRI volumes with NV-Generate-CTMR MR-Brain v1. Not for production training data.

**中文介绍**: Used for generating synthetic T1, T2, FLAIR, SWI, or MRA brain MRI volumes with NV-Generate-CTMR MR-Brain v1. Not for production training data.

**关键词**: T1, T2, nv-generate-mr-brain, Used, generating, synthetic, FLAIR, SWI

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nv-generate-mr-brain)

---

