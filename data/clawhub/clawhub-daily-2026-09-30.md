# ClawHub Skills Daily | 2026-09-30

> 共 25 个 skills

## [1. 数学解题教练](https://clawhub.ai/qizhitang/xiaozhi-math-problem-solving-coach)

**Slug**: `xiaozhi-math-problem-solving-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1402 | 🧩 25

**原始简介**: 初中到高中的数学单题解题教练（高中覆盖必修与选择性必修）：学生发来一道数学题说"卡住了""这道数学题我做错了""我不知道怎么列式"时，用追问帮学生找回思路，提示按 shared/hint-ladder.md 逐级升。也用于出同类题、考前梳理（"明天数学考试，帮我梳理这一章"；只在学生明确说考试在即时进入）。默认只在当前会话工作：不读档案、不归档、不排提醒，三项都要学生当轮明确开启；含全库统一的数据控制入口与危机例外。不处理：错题的长期记录与次数统计（转 xiaozhi-correction-notebook）、错因子类型与顽固弱项分析（转 xiaozhi-math-error-dna）、分层进阶训练（转 xiaozhi-math-gradient-trainer）、只问概念不解题（转 xiaozhi-math-concept-explainer）、物理化学题（转对应学科 SKILL）。

**中文介绍**: 初中到高中的数学单题解题教练（高中覆盖必修与选择性必修）：学生发来一道数学题说"卡住了""这道数学题我做错了""我不知道怎么列式"时，用追问帮学生找回思路，提示按 shared/hint-ladder.md 逐级升。也用于出同类题、考前梳理（"明天数学考试，帮我梳理这一章"；只在学生明确说考试在即时进入）。默认只在当前会话工作：不读档案、不归档、不排提醒，三项都要学生当轮明确开启；含全库统一的数据控制入口与危机例外。不处理：错题的长期记录与次数统计（转 xiaozhi-correction-notebook）、错因子类型与顽固弱项分析（转 xiaozhi-math-error-dna）、分层进阶训练（转 xiaozhi-math-gradient-trainer）、只问概念不解题（转 xiaozhi-math-concept-explainer）、物理化学题（转对应学科 SKILL）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 数学解题教练, 用追问帮学生找回思路, 提示按, 逐级升, 也用于出同类题、考前梳理（"明天数学考试, 帮我梳理这一章", shared, hint-ladder.md

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-math-problem-solving-coach)

---

## [2. 开卷答题教练](https://clawhub.ai/qizhitang/xiaozhi-openbook-coach)

**Slug**: `xiaozhi-openbook-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 315 | 🧩 7

**原始简介**: 开卷答题教练：教初中开卷考试的方法——考前怎么给教材建索引，考场上怎么快速定位，怎么把材料和教材原文组织成得分点；适用于道德与法治、历史、生物、地理等采用开卷形式的中考科目。触发语示例："开卷考试怎么准备""道法开卷怎么做索引""考场上翻书来不及怎么办""开卷题的答案怎么组织才得分"。只教方法：不讲具体题目的答案，不产出任何道德与法治的观点性内容，观点性表述一律指回教材原文。具体某一科的题目转对应学科技能（历史转历史技能；道德与法治的题目本身，本库不讲）。

**中文介绍**: 开卷答题教练：教初中开卷考试的方法——考前怎么给教材建索引，考场上怎么快速定位，怎么把材料和教材原文组织成得分点；适用于道德与法治、历史、生物、地理等采用开卷形式的中考科目。触发语示例："开卷考试怎么准备""道法开卷怎么做索引""考场上翻书来不及怎么办""开卷题的答案怎么组织才得分"。只教方法：不讲具体题目的答案，不产出任何道德与法治的观点性内容，观点性表述一律指回教材原文。具体某一科的题目转对应学科技能（历史转历史技能；道德与法治的题目本身，本库不讲）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 开卷答题教练, 教初中开卷考试的方法——考前怎么给教材建索引, 考场上怎么快速定位, 怎么把材料和教材原文组织成得分点, 触发语示例, 只教方法, 不讲具体题目的答案, 不产出任何道德与法治的观点性内容

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-openbook-coach)

---

## [3. 元阁 yotta-skills](https://clawhub.ai/yottameta/yotta-skills)

**Slug**: `yotta-skills`  
**Version**: 0.22.2  
**Stats**: ⭐ 0 | ⬇️ 1382 | 🧩 50

**原始简介**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 运行时 hook 适配。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；M1 记忆裁决层：usage enable/mark 本地结构化记录 + decide-memory / MCP decide_memory 输出 promote / hold / demote 只读建议（需授权 provider；只建议不删除、不自动写元忆）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request/decide_memory，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / usage 使用记录 / decide-memory 记忆裁决 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、判断哪些技能值得长期记忆、查看或记录技能使用信号、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/记忆裁决/技能该不该记住/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + M1 记忆裁决只读建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆、不自动删除技能或记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

**中文介绍**: 元阁 -- 元阁全家技能的总编排策划 + 编排路由 + 一键安装器 + 技能盘点 + 运行时 hook 适配。路由层：--route / route_request 按需求摘要给出候选组合、调用顺序、角色、置信度、依据、已装/缺失状态与安装命令，只建议不自动安装；非元阁家族已装技能按 frontmatter description 机械匹配作并列候选（标注来源与未扫描状态，只读不自动调用）；M1 记忆裁决层：usage enable/mark 本地结构化记录 + decide-memory / MCP decide_memory 输出 promote / hold / demote 只读建议（需授权 provider；只建议不删除、不自动写元忆）；策划层：按场景给出「该组合哪几个元技能、组合强在哪、怎么组合使用（安装与调用均由用户确认后执行）」；安装层：一条命令把 YottaMeta 已发布的全部 yotta-* 技能装进指定智能体或目录（默认 --pin 锁死清单精确版本）；盘点层：--inventory / --reindex 扫描本机已装技能生成/更新注册表，新装技能自动被发现（install/update 后自动 re-index，会话开工只建议跑本地 --reindex；更新检查走手动 --check 或后台 --check --scheduled）；运行时适配层：hook capabilities / evaluate / bind / unbind 按宿主能力矩阵执行六个统一事件并留证降级，元信 before_install 已接入安装管线；自包含零依赖，不依赖任何元技能；MCP 按需加载且需用户确认后写入配置（可选：list_installed_skills/describe_skill/reindex/route_request/decide_memory，不常驻，未加载降级 CLI）。支持 --list 清单 / --route 路由 / usage 使用记录 / decide-memory 记忆裁决 / install / update / update --check（只读检查）/ update --check --scheduled（后台周检）/ update --auto（家族自动更新）/ hook 适配 / --inventory / --reindex / --dry-run 预览 / --pin（默认）/ --range。触发：需要批量安装或更新元阁全家技能、按场景组合多个元技能、路由或判断该用哪些技能、判断哪些技能值得长期记忆、查看或记录技能使用信号、盘点或查看本机已装技能、重扫技能注册表、给某个智能体或目录一次性铺齐 yotta-* 技能、评估宿主 hook 能力、预览安装清单、锁版本安装、或用户说 元阁/装全家/一次装齐/yotta-skills/install-all/更新全家/检查更新/自动更新/hook 适配/该用哪个技能/路由技能/记忆裁决/技能该不该记住/盘点技能/查看已装技能 等。边界（Do NOT trigger）：只做「组合策划 + 静态路由建议 + M1 记忆裁决只读建议 + 清单 + 下载 + 落位 + 汇总 + 盘点 + re-index + hook 适配」，不含技能本体、不做技能内容开发、不 -g 污染全局、不自动安装缺失技能、不静默写宿主配置或全局记忆、不自动删除技能或记忆；家族安装先自举或调用元信装前门禁，DO NOT INSTALL 阻断，非元阁家族包不自动安装。

Latest changelog:
yotta-skills 0.22.2

- Documentation updates: improved/updated content in README, SKILL.md, and other docs.
- Removed obsolete skill-card.md file.
- Minor adjustments and clarifications in usage instructions and orchestration documentation.
- No breaking changes or functional changes to core features.

**关键词**: 元阁, 元阁全家技能的总编排策划, 编排路由, 一键安装器, 技能盘点, 运行时, yotta-skills, hook

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yotta-skills)

---

## [4. 学习DNA](https://clawhub.ai/qizhitang/xiaozhi-learning-dna)

**Slug**: `xiaozhi-learning-dna`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 2040 | 🧩 27

**原始简介**: 学生长期学习档案系统（敏感未成年人数据）：在明确授权下建立、查看、更正、导出、删除学生档案——学科强弱、错误模式、学习风格、成长轨迹，以及需各自单独开关的学习情绪、兴趣信号、家长可见输出、老师写回、跨 SKILL 共享、危机转介事实。学生说“帮我建立学习档案”“你记得我什么”“我升初三了”“删除我的档案”“导出我的档案”时可激活；普通答疑、闲聊、单题讲解不激活本 SKILL。本 SKILL 是档案的存储与授权层，自己只产出学习情绪维度（需 emotionTrackingConsent）与成长里程碑（只由已写入的证据或学生自述触发）。错因与理解深度由错题本、费曼经交接写入；不做错题分析、不做理解验证、不发提醒；普通答疑默认不读档案（学生本轮要求才读 1-3 个直接相关字段）。所有开关默认关闭；未获同意只用当前会话信息；约 14 周岁以下需监护人同意；说话人未确认时受限：不读不写不改授权。

**中文介绍**: 学生长期学习档案系统（敏感未成年人数据）：在明确授权下建立、查看、更正、导出、删除学生档案——学科强弱、错误模式、学习风格、成长轨迹，以及需各自单独开关的学习情绪、兴趣信号、家长可见输出、老师写回、跨 SKILL 共享、危机转介事实。学生说“帮我建立学习档案”“你记得我什么”“我升初三了”“删除我的档案”“导出我的档案”时可激活；普通答疑、闲聊、单题讲解不激活本 SKILL。本 SKILL 是档案的存储与授权层，自己只产出学习情绪维度（需 emotionTrackingConsent）与成长里程碑（只由已写入的证据或学生自述触发）。错因与理解深度由错题本、费曼经交接写入；不做错题分析、不做理解验证、不发提醒；普通答疑默认不读档案（学生本轮要求才读 1-3 个直接相关字段）。所有开关默认关闭；未获同意只用当前会话信息；约 14 周岁以下需监护人同意；说话人未确认时受限：不读不写不改授权。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 学生长期学习档案系统（敏感未成年人数据）, 共享、危机转介事实, 普通答疑、闲聊、单题讲解不激活本, 是档案的存储与授权层, 自己只产出学习情绪维度（需, 错因与理解深度由错题本、费曼经交接写入, 学习DNA, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-learning-dna)

---

## [5. 数学概念解释器](https://clawhub.ai/qizhitang/xiaozhi-math-concept-explainer)

**Slug**: `xiaozhi-math-concept-explainer`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1415 | 🧩 25

**原始简介**: 初中到高中的数学概念理解与重建（高中覆盖必修与选择性必修）：学生不是卡在某道题，而是卡在"这个数学概念本身没懂"时用。典型触发："这个数学公式我知道但不明白为什么""负负为什么得正""一次函数和正比例有什么区别""几何题我脑子里建不起图形""这两个数学概念我总是混""用生活例子讲讲这个概念"。核心方法：三种解释模型（生活类比 / 图解可视化 / 逐步拆分）+ 几何空间想象训练。不处理：具体某道题怎么做（转 xiaozhi-math-problem-solving-coach）、应用题列式（转 xiaozhi-math-word-problem-coach）、错题收录与统计（转 xiaozhi-correction-notebook）、分层进阶练习（转 xiaozhi-math-gradient-trainer）。

**中文介绍**: 初中到高中的数学概念理解与重建（高中覆盖必修与选择性必修）：学生不是卡在某道题，而是卡在"这个数学概念本身没懂"时用。典型触发："这个数学公式我知道但不明白为什么""负负为什么得正""一次函数和正比例有什么区别""几何题我脑子里建不起图形""这两个数学概念我总是混""用生活例子讲讲这个概念"。核心方法：三种解释模型（生活类比 / 图解可视化 / 逐步拆分）+ 几何空间想象训练。不处理：具体某道题怎么做（转 xiaozhi-math-problem-solving-coach）、应用题列式（转 xiaozhi-math-word-problem-coach）、错题收录与统计（转 xiaozhi-correction-notebook）、分层进阶练习（转 xiaozhi-math-gradient-trainer）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 数学概念解释器, 学生不是卡在某道题, 而是卡在"这个数学概念本身没懂"时用, 典型触发, 核心方法, 三种解释模型（生活类比, 图解可视化, 逐步拆分）+

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-math-concept-explainer)

---

## [6. 数学错误DNA](https://clawhub.ai/qizhitang/xiaozhi-math-error-dna)

**Slug**: `xiaozhi-math-error-dna`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1404 | 🧩 25

**原始简介**: 初中到高中的数学错题根因深度分析（高中覆盖必修与选择性必修）：把错题本判定的通用四维，细化为数学子类型（B/C/R/M + 两位编码）并做跨维度关联。典型触发："为什么我数学总在同一个地方错""帮我分析我的数学错误规律""帮我生成数学弱项月报""我数学太差了"。不处理：错题的收录与次数统计（由 xiaozhi-correction-notebook 唯一负责，本 SKILL 只接收它推送的交接）、单题当场讲解（转 xiaozhi-math-problem-solving-coach）、概念重建（转 xiaozhi-math-concept-explainer）、分层练习（转 xiaozhi-math-gradient-trainer）。未获同意时，不建立长期档案、不跨SKILL共享。

**中文介绍**: 初中到高中的数学错题根因深度分析（高中覆盖必修与选择性必修）：把错题本判定的通用四维，细化为数学子类型（B/C/R/M + 两位编码）并做跨维度关联。典型触发："为什么我数学总在同一个地方错""帮我分析我的数学错误规律""帮我生成数学弱项月报""我数学太差了"。不处理：错题的收录与次数统计（由 xiaozhi-correction-notebook 唯一负责，本 SKILL 只接收它推送的交接）、单题当场讲解（转 xiaozhi-math-problem-solving-coach）、概念重建（转 xiaozhi-math-concept-explainer）、分层练习（转 xiaozhi-math-gradient-trainer）。未获同意时，不建立长期档案、不跨SKILL共享。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 数学错误DNA, 把错题本判定的通用四维, 细化为数学子类型（B, 两位编码）并做跨维度关联, 典型触发, 不处理, 错题的收录与次数统计（由, 唯一负责

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-math-error-dna)

---

## [7. PlanetScale CLI Skills](https://clawhub.ai/vince-winkintel/planetscale-cli-skills)

**Slug**: `planetscale-cli-skills`  
**Version**: 1.0.31  
**Stats**: ⭐ 2 | ⬇️ 3461 | 🧩 27

**原始简介**: PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, read-only replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, keyspace, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

**中文介绍**: PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, read-only replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, keyspace, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

Latest changelog:
Refresh for pscale v0.340.0-v0.341.0: guarded disk storage, MoveTables ignore-source recovery, workflow/data-imports transition guidance, vtctl discovery, and inspect hint fixes.

**关键词**: PlanetScale, CLI, Skills, command, reference, workflows, Use, authentication

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/planetscale-cli-skills)

---

## [8. 30天学习计划制定师](https://clawhub.ai/qizhitang/xiaozhi-learning-plan)

**Slug**: `xiaozhi-learning-plan`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1389 | 🧩 25

**原始简介**: 把学习目标拆成可执行的 30 天方案（小学高段用周计划版），并在学生开启后跟进执行偏差。学生说"帮我制定学习计划"、"我不知道怎么安排时间"、"下次考试前怎么复习"、"帮我生成30天方案"、"我的计划总是坚持不下去"、"帮我做家庭学习看板"时可激活。它只管"什么时候做什么"：直接用错题本给出的弱项摘要来排任务，自己不做错因归类与深度归因（转错题本）；不讲题（转对应学科教练）、不发提醒（转 IM 智能提醒）。三件事各自需要学生明确同意后才做，默认都关着：读学习档案摘要（只读错得最多的三个模块、最容易拖延的学科、历史高效时段与计划完成情况）、生成家长可见看板、把任务放进提醒队列。

**中文介绍**: 把学习目标拆成可执行的 30 天方案（小学高段用周计划版），并在学生开启后跟进执行偏差。学生说"帮我制定学习计划"、"我不知道怎么安排时间"、"下次考试前怎么复习"、"帮我生成30天方案"、"我的计划总是坚持不下去"、"帮我做家庭学习看板"时可激活。它只管"什么时候做什么"：直接用错题本给出的弱项摘要来排任务，自己不做错因归类与深度归因（转错题本）；不讲题（转对应学科教练）、不发提醒（转 IM 智能提醒）。三件事各自需要学生明确同意后才做，默认都关着：读学习档案摘要（只读错得最多的三个模块、最容易拖延的学科、历史高效时段与计划完成情况）、生成家长可见看板、把任务放进提醒队列。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 30天学习计划制定师, 把学习目标拆成可执行的, 天方案（小学高段用周计划版）, 并在学生开启后跟进执行偏差, 它只管"什么时候做什么", 直接用错题本给出的弱项摘要来排任务, 自己不做错因归类与深度归因（转错题本）, 不讲题（转对应学科教练）、不发提醒（转

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-learning-plan)

---

## [9. 兴趣成长探索计划](https://clawhub.ai/qizhitang/xiaozhi-interest-explorer)

**Slug**: `xiaozhi-interest-explorer`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1349 | 🧩 25

**原始简介**: 用每周一次的探索，帮学生区分"浅层喜好"和"遇到困难还想继续的真正兴趣"。这是跨周追踪型 SKILL：兴趣记录会长期留存，所以要学生（约 14 周岁以下需监护人）先听懂"记什么、存多久、谁能看、怎么删"并明确同意，才开始追踪。触发语（须是明确要开始或继续探索）："帮我探索兴趣"、"开始这周的兴趣探索"、"我不知道自己喜欢什么，帮我找找"、"这个兴趣是真的吗"。不触发：随口说"我喜欢打游戏"、聊某个领域的知识、问某个爱好怎么入门——按普通对话回答，不建记录。记录四个维度：吸引我的内容、遇到困难时的反应、时间流逝感、外部反馈；判断依据是困难反应，不是喜好自评。不做学科辅导（转对应学科 SKILL）、不做生涯规划或专业推荐、不做升学建议。

**中文介绍**: 用每周一次的探索，帮学生区分"浅层喜好"和"遇到困难还想继续的真正兴趣"。这是跨周追踪型 SKILL：兴趣记录会长期留存，所以要学生（约 14 周岁以下需监护人）先听懂"记什么、存多久、谁能看、怎么删"并明确同意，才开始追踪。触发语（须是明确要开始或继续探索）："帮我探索兴趣"、"开始这周的兴趣探索"、"我不知道自己喜欢什么，帮我找找"、"这个兴趣是真的吗"。不触发：随口说"我喜欢打游戏"、聊某个领域的知识、问某个爱好怎么入门——按普通对话回答，不建记录。记录四个维度：吸引我的内容、遇到困难时的反应、时间流逝感、外部反馈；判断依据是困难反应，不是喜好自评。不做学科辅导（转对应学科 SKILL）、不做生涯规划或专业推荐、不做升学建议。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 兴趣成长探索计划, 用每周一次的探索, 这是跨周追踪型, 兴趣记录会长期留存, 所以要学生（约, 才开始追踪, 触发语（须是明确要开始或继续探索）, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-interest-explorer)

---

## [10. 时空线索构建器](https://clawhub.ai/qizhitang/xiaozhi-history-timeline-builder)

**Slug**: `xiaozhi-history-timeline-builder`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 307 | 🧩 7

**原始简介**: 时空线索构建器：帮学生把史事放进正确的时间和空间——纵向理清阶段与因果，横向对照同一时期的中外史事，并练公元纪年、世纪、年代的换算和历史地图的识读。触发语示例："帮我理一下近代史的时间线""公元前 221 年是几世纪""同一时期欧洲在发生什么""这几件事谁先谁后""这张历史地图怎么看"。学科判别：问时间先后、时段特征、同期中外对照、纪年换算、历史地图时归本 SKILL；给了史料要做概括、原因、影响的材料题转历史材料解析题教练；要"自拟观点、史论结合"的开放性论述转历史论述题教练。

**中文介绍**: 时空线索构建器：帮学生把史事放进正确的时间和空间——纵向理清阶段与因果，横向对照同一时期的中外史事，并练公元纪年、世纪、年代的换算和历史地图的识读。触发语示例："帮我理一下近代史的时间线""公元前 221 年是几世纪""同一时期欧洲在发生什么""这几件事谁先谁后""这张历史地图怎么看"。学科判别：问时间先后、时段特征、同期中外对照、纪年换算、历史地图时归本 SKILL；给了史料要做概括、原因、影响的材料题转历史材料解析题教练；要"自拟观点、史论结合"的开放性论述转历史论述题教练。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 时空线索构建器, 横向对照同一时期的中外史事, 并练公元纪年、世纪、年代的换算和历史地图的识读, 触发语示例, "帮我理一下近代史的时间线""公元前, 学科判别, SKILL, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-history-timeline-builder)

---

## [11. IM智能提醒](https://clawhub.ai/qizhitang/xiaozhi-im-reminder)

**Slug**: `xiaozhi-im-reminder`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1336 | 🧩 25

**原始简介**: 全库唯一的提醒发送方：把其他 SKILL 入队的复习、错题复测、计划任务、探索任务合并成每天一条摘要发出。只在学生说出**明确的提醒动词**时激活：“帮我设置提醒”“提醒我复习二次根式”“我今天该复习什么”“暂停提醒”“查看我的提醒”。提到“提醒”但不是要操作提醒的话（“老师提醒过我”“提醒一下自己要早睡”）不激活；其他 SKILL 完成任务后也不自动入队，要学生当轮说“要”。提醒内容本身不在这里生成——错题由错题本、词卡由英语词汇 DNA、任务由 30 天学习计划提供，本 SKILL 只做排期、合并与发送。未获授权时只给“建议提醒方案”，不创建实际提醒，也不做闲置唤醒。

**中文介绍**: 全库唯一的提醒发送方：把其他 SKILL 入队的复习、错题复测、计划任务、探索任务合并成每天一条摘要发出。只在学生说出**明确的提醒动词**时激活：“帮我设置提醒”“提醒我复习二次根式”“我今天该复习什么”“暂停提醒”“查看我的提醒”。提到“提醒”但不是要操作提醒的话（“老师提醒过我”“提醒一下自己要早睡”）不激活；其他 SKILL 完成任务后也不自动入队，要学生当轮说“要”。提醒内容本身不在这里生成——错题由错题本、词卡由英语词汇 DNA、任务由 30 天学习计划提供，本 SKILL 只做排期、合并与发送。未获授权时只给“建议提醒方案”，不创建实际提醒，也不做闲置唤醒。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: IM智能提醒, 全库唯一的提醒发送方, 把其他, 只在学生说出, 明确的提醒动词, 时激活, 其他, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-im-reminder)

---

## [12. smyx_infant_cry_cause_classification_analysis | 婴幼儿哭声原因分类](https://clawhub.ai/18072937735/smyx-infant-cry-cause-classification-analysis)

**Slug**: `smyx-infant-cry-cause-classification-analysis`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1934 | 🧩 14

**原始简介**: Using the built-in microphone of a baby monitor or smart camera to capture infant cry audio, AI acoustic analysis extracts cry features such as frequency, pitch, rhythm, and duration, and classifies the possible causes behind the cry (hunger, sleepiness, pain/discomfort, boredom/need for comfort, fear, etc.), outputting the most likely cause and its confidence. | 通过婴儿监护器或智能摄像头的内置麦克风采集婴儿哭声音频，利用AI声学分析技术提取哭声的频率、音调、节奏、持续时间等特征，分类识别婴儿哭声背后的可能原因（饥饿、困倦、疼痛/不适、无聊/需要安抚、恐惧等），输出最可能的原因类别及置信度。系统实时监测哭声，当检测到哭声时自动分析并在父母手机APP上推送结果（如'宝宝可能是饿了，建议喂奶'）。

**中文介绍**: Using the built-in microphone of a baby monitor or smart camera to capture infant cry audio, AI acoustic analysis extracts cry features such as frequency, pitch, rhythm, and duration, and classifies the possible causes behind the cry (hunger, sleepiness, pain/discomfort, boredom/need for comfort, fear, etc.), outputting the most likely cause and its confidence. | 通过婴儿监护器或智能摄像头的内置麦克风采集婴儿哭声音频，利用AI声学分析技术提取哭声的频率、音调、节奏、持续时间等特征，分类识别婴儿哭声背后的可能原因（饥饿、困倦、疼痛/不适、无聊/需要安抚、恐惧等），输出最可能的原因类别及置信度。系统实时监测哭声，当检测到哭声时自动分析并在父母手机APP上推送结果（如'宝宝可能是饿了，建议喂奶'）。

Latest changelog:
- Updated version number and metadata in SKILL.md.
- Removed the deprecated skill-card.md file.
- No changes to core functionality or usage instructions.

**关键词**: 婴幼儿哭声原因分类, smyx, infant, cry, cause, classification, analysis, built-in

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-infant-cry-cause-classification-analysis)

---

## [13. Workbuddy Usage Status](https://clawhub.ai/clancy-feng/workbuddy-usage-status)

**Slug**: `workbuddy-usage-status`  
**Version**: 1.5.0  
**Stats**: ⭐ 0 | ⬇️ 1125 | 🧩 14

**原始简介**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

**中文介绍**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

Latest changelog:
v1.5.0:Revised credit by per-call, other bug-fixes and enhancements.

**关键词**: 离线可视化, 本机使用数据, 消耗为主指标、credit, 为本地估算, Workbuddy, Usage, Status, token

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-usage-status)

---

## [14. 历史材料解析题教练](https://clawhub.ai/qizhitang/xiaozhi-history-source-analyzer)

**Slug**: `xiaozhi-history-source-analyzer`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 311 | 🧩 7

**原始简介**: 历史材料解析题教练：按"读出处 → 提取信息 → 结合所学 → 得出结论"四步，陪学生做当前这道材料题；同时持有历史错因维度表，负责历史错题的深度归因。触发语示例（须带上具体材料或题目）："这道材料题怎么答""这段史料说明了什么""这则材料可信吗""我材料题为什么总答不全""这道历史错题帮我分析一下错在哪"。学科判别：题目给了史料原文、历史图片、统计图表或历史地图，问概括、原因、影响、比较、评价时归本 SKILL；问文言字词怎么翻译转语文文言技能；问时间先后与同期中外对照转时空线索构建器；要"自拟观点、史论结合"的开放性论述转历史论述题教练。不处理：错题的初始收录与 28 天计数（由通用错题本唯一负责）；道德与法治的题目。

**中文介绍**: 历史材料解析题教练：按"读出处 → 提取信息 → 结合所学 → 得出结论"四步，陪学生做当前这道材料题；同时持有历史错因维度表，负责历史错题的深度归因。触发语示例（须带上具体材料或题目）："这道材料题怎么答""这段史料说明了什么""这则材料可信吗""我材料题为什么总答不全""这道历史错题帮我分析一下错在哪"。学科判别：题目给了史料原文、历史图片、统计图表或历史地图，问概括、原因、影响、比较、评价时归本 SKILL；问文言字词怎么翻译转语文文言技能；问时间先后与同期中外对照转时空线索构建器；要"自拟观点、史论结合"的开放性论述转历史论述题教练。不处理：错题的初始收录与 28 天计数（由通用错题本唯一负责）；道德与法治的题目。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 历史材料解析题教练, 按"读出处, 提取信息, 结合所学, 得出结论"四步, 陪学生做当前这道材料题, 同时持有历史错因维度表, 负责历史错题的深度归因

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-history-source-analyzer)

---

## [15. 历史论述题教练](https://clawhub.ai/qizhitang/xiaozhi-history-essay-coach)

**Slug**: `xiaozhi-history-essay-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 310 | 🧩 7

**原始简介**: 历史论述题教练：陪学生做"自拟观点、史论结合"的开放性试题——从材料中提炼观点或自拟论题、选取史实、组织论证、检查逻辑，初中与高中都适用。触发语示例："这道题要我自己拟一个观点，怎么拟""历史小论文怎么写""我的论述为什么只得了一半分""帮我看看这段论证有没有做到史论结合"。只检查和引导，不替学生拟定观点、不代写论述：观点由学生自己从史料中提炼。学科判别：要求"自拟论题、提炼观点、论述、小论文"的历史开放题归本 SKILL；材料题的概括、原因、影响等常规设问转历史材料解析题教练；语文议论文转语文写作教练。

**中文介绍**: 历史论述题教练：陪学生做"自拟观点、史论结合"的开放性试题——从材料中提炼观点或自拟论题、选取史实、组织论证、检查逻辑，初中与高中都适用。触发语示例："这道题要我自己拟一个观点，怎么拟""历史小论文怎么写""我的论述为什么只得了一半分""帮我看看这段论证有没有做到史论结合"。只检查和引导，不替学生拟定观点、不代写论述：观点由学生自己从史料中提炼。学科判别：要求"自拟论题、提炼观点、论述、小论文"的历史开放题归本 SKILL；材料题的概括、原因、影响等常规设问转历史材料解析题教练；语文议论文转语文写作教练。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 历史论述题教练, 初中与高中都适用, 触发语示例, "这道题要我自己拟一个观点, 只检查和引导, 不替学生拟定观点、不代写论述, 观点由学生自己从史料中提炼, 学科判别

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-history-essay-coach)

---

## [16. 地理读图教练](https://clawhub.ai/qizhitang/xiaozhi-geography-map-reader)

**Slug**: `xiaozhi-geography-map-reader`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 259 | 🧩 6

**原始简介**: 地理读图教练：陪学生读懂当前这道题里的地图和地理图表——先看图名、图例、比例尺和方向，再读经纬网、等高线、气温曲线与降水量柱状图；同时持有地理错因维度表，负责地理错题的深度归因。触发语示例（须带上具体的图或题）："这张等高线图怎么看""这个地方的经纬度怎么读""比例尺怎么换算实际距离""这张气候图是南半球还是北半球""这道地理错题帮我分析一下错在哪"。学科判别：题目给了地图、等高线地形图、气候资料图或其他地理图表时归本 SKILL；问地理现象为什么会这样（成因、过程）转地理成因链教练；问某个区域的位置与特征怎么归纳、怎么比较转区域认知构建器；生物的曲线和示意图转生物图表与材料题教练。不处理：绘制或修改国界与行政区划（以教材和标准地图为准）；错题的初始收录与 28 天计数（由通用错题本唯一负责）。

**中文介绍**: 地理读图教练：陪学生读懂当前这道题里的地图和地理图表——先看图名、图例、比例尺和方向，再读经纬网、等高线、气温曲线与降水量柱状图；同时持有地理错因维度表，负责地理错题的深度归因。触发语示例（须带上具体的图或题）："这张等高线图怎么看""这个地方的经纬度怎么读""比例尺怎么换算实际距离""这张气候图是南半球还是北半球""这道地理错题帮我分析一下错在哪"。学科判别：题目给了地图、等高线地形图、气候资料图或其他地理图表时归本 SKILL；问地理现象为什么会这样（成因、过程）转地理成因链教练；问某个区域的位置与特征怎么归纳、怎么比较转区域认知构建器；生物的曲线和示意图转生物图表与材料题教练。不处理：绘制或修改国界与行政区划（以教材和标准地图为准）；错题的初始收录与 28 天计数（由通用错题本唯一负责）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 地理读图教练, 再读经纬网、等高线、气温曲线与降水量柱状图, 同时持有地理错因维度表, 负责地理错题的深度归因, 触发语示例（须带上具体的图或题）, 学科判别, 生物的曲线和示意图转生物图表与材料题教练, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-geography-map-reader)

---

## [17. 区域认知构建器](https://clawhub.ai/qizhitang/xiaozhi-geography-region-builder)

**Slug**: `xiaozhi-geography-region-builder`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 260 | 🧩 6

**原始简介**: 区域认知构建器：陪学生按"定位 → 归纳特征 → 比较 → 联系"四步认识一个区域——大洲、地区、国家、中国的分区和家乡，把地图上零散的地名归纳成区域特征，并学会做区域比较。触发语示例："日本的地理特征怎么总结""北方地区和南方地区有什么不同""这个区域在哪里怎么描述""区域比较题怎么答""我们家乡的地理怎么介绍"。学科判别：问一个区域的位置与特征怎么描述、两个区域怎么比较、区域之间有什么联系时归本 SKILL；图还没读懂（图例、比例尺、等高线）转地理读图教练；问某个现象为什么会这样（成因、过程）转地理成因链教练；历史上的区域与疆域变化转时空线索构建器。不处理：绘制或修改国界与行政区划（以教材和标准地图为准）。

**中文介绍**: 区域认知构建器：陪学生按"定位 → 归纳特征 → 比较 → 联系"四步认识一个区域——大洲、地区、国家、中国的分区和家乡，把地图上零散的地名归纳成区域特征，并学会做区域比较。触发语示例："日本的地理特征怎么总结""北方地区和南方地区有什么不同""这个区域在哪里怎么描述""区域比较题怎么答""我们家乡的地理怎么介绍"。学科判别：问一个区域的位置与特征怎么描述、两个区域怎么比较、区域之间有什么联系时归本 SKILL；图还没读懂（图例、比例尺、等高线）转地理读图教练；问某个现象为什么会这样（成因、过程）转地理成因链教练；历史上的区域与疆域变化转时空线索构建器。不处理：绘制或修改国界与行政区划（以教材和标准地图为准）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 区域认知构建器, 陪学生按"定位, 归纳特征, 比较, 把地图上零散的地名归纳成区域特征, 并学会做区域比较, 触发语示例, 学科判别

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-geography-region-builder)

---

## [18. 地理成因链教练](https://clawhub.ai/qizhitang/xiaozhi-geography-causal-chain)

**Slug**: `xiaozhi-geography-causal-chain`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 264 | 🧩 6

**原始简介**: 地理成因链教练：陪学生把"为什么"连成一条完整的链——从纬度、海陆位置、地形或人类活动这些起点出发，一环一环连到要解释的现象，覆盖昼夜交替与四季变化、气候成因、地势对河流的影响、板块运动和人地关系。触发语示例："为什么会有四季""这里为什么降水多""地势西高东低有什么影响""这道原因题我总答不全""过度放牧为什么会导致荒漠化"。学科判别：问地理现象的成因、过程和影响，或原因类设问答不全时归本 SKILL；图还没读懂（图例、比例尺、等高线）转地理读图教练；区域的位置与特征怎么归纳、怎么比较转区域认知构建器；生物学概念之间的关系转生物概念网络构建器。

**中文介绍**: 地理成因链教练：陪学生把"为什么"连成一条完整的链——从纬度、海陆位置、地形或人类活动这些起点出发，一环一环连到要解释的现象，覆盖昼夜交替与四季变化、气候成因、地势对河流的影响、板块运动和人地关系。触发语示例："为什么会有四季""这里为什么降水多""地势西高东低有什么影响""这道原因题我总答不全""过度放牧为什么会导致荒漠化"。学科判别：问地理现象的成因、过程和影响，或原因类设问答不全时归本 SKILL；图还没读懂（图例、比例尺、等高线）转地理读图教练；区域的位置与特征怎么归纳、怎么比较转区域认知构建器；生物学概念之间的关系转生物概念网络构建器。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 地理成因链教练, 一环一环连到要解释的现象, 触发语示例, 学科判别, 问地理现象的成因、过程和影响, 或原因类设问答不全时归本, 图还没读懂（图例、比例尺、等高线）转地理读图教练, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-geography-causal-chain)

---

## [19. 费曼学习法](https://clawhub.ai/qizhitang/xiaozhi-feynman-learning)

**Slug**: `xiaozhi-feynman-learning`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1917 | 🧩 26

**原始简介**: 用"讲给小智听"来检验学生是否真的学会了某个概念（数学函数、物理受力、英语时态、语文文言实词都适用）。学生说“我来给你讲讲今天学的”“我觉得我懂了你测测我”“帮我检验一下我学没学会”“AI都讲明白了我应该会了吧”时可激活。产出是掌握度判定（会复述/会解释/真正掌握）与卡住位置，不做错因归档（转错题本）、不讲新知识（转对应学科教练）、不出成套练习。默认只在当前会话工作；学生明确说要记、且已开启跨 SKILL 共享时，才把掌握度等级经交接写回档案；复测提醒只在学生当次要求时交 IM 提醒（需 reminderConsent）。含全库统一的数据控制入口与危机例外，不是本 SKILL 特有的功能。

**中文介绍**: 用"讲给小智听"来检验学生是否真的学会了某个概念（数学函数、物理受力、英语时态、语文文言实词都适用）。学生说“我来给你讲讲今天学的”“我觉得我懂了你测测我”“帮我检验一下我学没学会”“AI都讲明白了我应该会了吧”时可激活。产出是掌握度判定（会复述/会解释/真正掌握）与卡住位置，不做错因归档（转错题本）、不讲新知识（转对应学科教练）、不出成套练习。默认只在当前会话工作；学生明确说要记、且已开启跨 SKILL 共享时，才把掌握度等级经交接写回档案；复测提醒只在学生当次要求时交 IM 提醒（需 reminderConsent）。含全库统一的数据控制入口与危机例外，不是本 SKILL 特有的功能。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 费曼学习法, 产出是掌握度判定（会复述, 会解释, 真正掌握）与卡住位置, 默认只在当前会话工作, 学生明确说要记、且已开启跨, 共享时, SKILL

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-feynman-learning)

---

## [20. 英语写作进化教练](https://clawhub.ai/qizhitang/xiaozhi-english-writing-coach)

**Slug**: `xiaozhi-english-writing-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1609 | 🧩 27

**原始简介**: 英语写作教练：从语法、用词、逻辑三个维度给整段/整篇反馈，用追问引导学生自己改；高中加应用文与续写的读题、衔接与语体。触发语（须是**整段或整篇**的写作反馈请求）："帮我批改英语作文"、"帮我看看这段英语"、"我的英语写作怎么提高"、"帮我检查这封邮件"、"读后续写怎么写"、"我想练英语写作"。不触发：单句语法对错（转英语语法突破教练）、"这个词什么意思"（直接回答）、口语与发音（转英语口语陪练）。核心功能：三维批改（语法+用词+逻辑）+ 写作档案（句式层级追踪）+ 低阶句式升级追问 + 五套真实场景练习。不处理：单句语法错误的逐步追问（转英语语法突破教练）、单词记忆与到期复习（转智能词汇DNA系统）、口语与发音（转英语口语陪练）。

**中文介绍**: 英语写作教练：从语法、用词、逻辑三个维度给整段/整篇反馈，用追问引导学生自己改；高中加应用文与续写的读题、衔接与语体。触发语（须是**整段或整篇**的写作反馈请求）："帮我批改英语作文"、"帮我看看这段英语"、"我的英语写作怎么提高"、"帮我检查这封邮件"、"读后续写怎么写"、"我想练英语写作"。不触发：单句语法对错（转英语语法突破教练）、"这个词什么意思"（直接回答）、口语与发音（转英语口语陪练）。核心功能：三维批改（语法+用词+逻辑）+ 写作档案（句式层级追踪）+ 低阶句式升级追问 + 五套真实场景练习。不处理：单句语法错误的逐步追问（转英语语法突破教练）、单词记忆与到期复习（转智能词汇DNA系统）、口语与发音（转英语口语陪练）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 英语写作进化教练, 英语写作教练, 从语法、用词、逻辑三个维度给整段, 整篇反馈, 用追问引导学生自己改, 高中加应用文与续写的读题、衔接与语体, 触发语（须是, 整段或整篇

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-english-writing-coach)

---

## [21. 智能词汇DNA系统](https://clawhub.ai/qizhitang/xiaozhi-english-vocabulary-dna)

**Slug**: `xiaozhi-english-vocabulary-dna`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1580 | 🧩 27

**原始简介**: 英语词汇复习：按间隔重复排到期日，每天把到期的词合并成一张词卡；初中按义教词表，高中按课标词表的三档（义教、必修、选择性必修）。触发语："帮我记单词"、"把这个词存进词汇库"、"我单词背了就忘"、"下周要学新课了"、"启动词汇预热"、"帮我复习词汇"、"我的词汇库里有什么"。核心功能：三种入库方式 + SM-2 间隔重复排到期日 + 每日一张到期词卡（提醒由 IM 提醒统一发送）+ 课前预热雷达 + 个人遗忘速度调整。不处理：句子语法错误的追问（转英语语法突破教练）、整段作文批改（转英语写作进化教练）、发音是否标准（转英语口语陪练）。

**中文介绍**: 英语词汇复习：按间隔重复排到期日，每天把到期的词合并成一张词卡；初中按义教词表，高中按课标词表的三档（义教、必修、选择性必修）。触发语："帮我记单词"、"把这个词存进词汇库"、"我单词背了就忘"、"下周要学新课了"、"启动词汇预热"、"帮我复习词汇"、"我的词汇库里有什么"。核心功能：三种入库方式 + SM-2 间隔重复排到期日 + 每日一张到期词卡（提醒由 IM 提醒统一发送）+ 课前预热雷达 + 个人遗忘速度调整。不处理：句子语法错误的追问（转英语语法突破教练）、整段作文批改（转英语写作进化教练）、发音是否标准（转英语口语陪练）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 智能词汇DNA系统, 英语词汇复习, 按间隔重复排到期日, 每天把到期的词合并成一张词卡, 初中按义教词表, 高中按课标词表的三档（义教、必修、选择性必修）, 触发语, 核心功能

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-english-vocabulary-dna)

---

## [22. 英语口语陪练](https://clawhub.ai/qizhitang/xiaozhi-english-speaking-coach)

**Slug**: `xiaozhi-english-speaking-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1584 | 🧩 27

**原始简介**: 英语口语陪练：陪你开口说，说完再一起复盘；在你允许时记住发音弱点；高中加概述、评判观点与介绍中国文化。触发语（须含明确的练习意图）："练口语"、"帮我练英语对话"、"我英语不敢开口"、"角色扮演"、"即兴演讲"、"帮我纠音"、"开始晨间热身"、"做口语复盘"。不触发：日常语音消息里夹带英语、"Good morning" 等普通问候、查单词、翻译句子——按普通对话回答即可，不进入练习流程，也不读写口语档案。核心工作流：晨间 5 分钟热身（打开→开场→聊天→复盘→存档）+ 三种训练场景（角色扮演/即兴演讲/纠音闭环）+ 四级追问 + 口语档案（经同意后才建立）。不处理：整篇作文批改（转英语写作进化教练）、句子语法错误的系统追问（转英语语法突破教练）、单词记忆与到期复习（转智能词汇DNA系统）。

**中文介绍**: 英语口语陪练：陪你开口说，说完再一起复盘；在你允许时记住发音弱点；高中加概述、评判观点与介绍中国文化。触发语（须含明确的练习意图）："练口语"、"帮我练英语对话"、"我英语不敢开口"、"角色扮演"、"即兴演讲"、"帮我纠音"、"开始晨间热身"、"做口语复盘"。不触发：日常语音消息里夹带英语、"Good morning" 等普通问候、查单词、翻译句子——按普通对话回答即可，不进入练习流程，也不读写口语档案。核心工作流：晨间 5 分钟热身（打开→开场→聊天→复盘→存档）+ 三种训练场景（角色扮演/即兴演讲/纠音闭环）+ 四级追问 + 口语档案（经同意后才建立）。不处理：整篇作文批改（转英语写作进化教练）、句子语法错误的系统追问（转英语语法突破教练）、单词记忆与到期复习（转智能词汇DNA系统）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 英语口语陪练, 陪你开口说, 说完再一起复盘, 在你允许时记住发音弱点, 高中加概述、评判观点与介绍中国文化, 触发语（须含明确的练习意图）, 不触发, 日常语音消息里夹带英语、"Good

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-english-speaking-coach)

---

## [23. 个性化英语听力训练师](https://clawhub.ai/qizhitang/xiaozhi-english-listening-trainer)

**Slug**: `xiaozhi-english-listening-trainer`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1512 | 🧩 27

**原始简介**: 英语听力训练：按你的词汇量和兴趣生成一段听力材料，练完帮你定位卡在哪一层；高中加意图与态度的听辨。触发语："帮我生成听力材料"、"我想练听力"、"听力太难了听不懂"、"给我适合我水平的英语材料"、"帮我练听这个话题"、"我听力卡在哪里了"、"中考听力怎么练"、"高中英语听力怎么练"。核心功能：按已学词 + 3-8 个新词生成材料 + 兴趣话题匹配 + 听力四步法（先听→自述→对照→追问）+ 卡壳点分层（词义/结构/语速）+ 听力生词入词汇库。不处理：单词记忆与到期复习（转智能词汇DNA系统）、发音与口语练习（转英语口语陪练）、句子语法错误的追问（转英语语法突破教练）。

**中文介绍**: 英语听力训练：按你的词汇量和兴趣生成一段听力材料，练完帮你定位卡在哪一层；高中加意图与态度的听辨。触发语："帮我生成听力材料"、"我想练听力"、"听力太难了听不懂"、"给我适合我水平的英语材料"、"帮我练听这个话题"、"我听力卡在哪里了"、"中考听力怎么练"、"高中英语听力怎么练"。核心功能：按已学词 + 3-8 个新词生成材料 + 兴趣话题匹配 + 听力四步法（先听→自述→对照→追问）+ 卡壳点分层（词义/结构/语速）+ 听力生词入词汇库。不处理：单词记忆与到期复习（转智能词汇DNA系统）、发音与口语练习（转英语口语陪练）、句子语法错误的追问（转英语语法突破教练）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 个性化英语听力训练师, 英语听力训练, 按你的词汇量和兴趣生成一段听力材料, 练完帮你定位卡在哪一层, 高中加意图与态度的听辨, 触发语, 核心功能, 按已学词

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-english-listening-trainer)

---

## [24. 英语语法突破教练](https://clawhub.ai/qizhitang/xiaozhi-english-grammar-coach)

**Slug**: `xiaozhi-english-grammar-coach`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1559 | 🧩 27

**原始简介**: 英语语法教练：用追问帮初中生与高中生自己发现语法错误，并在同意后记录语法弱项；高中覆盖必修与选择性必修。触发语："帮我检查这句英语的语法"、"我时态老是错"、"定语从句 who/which/where 怎么选"、"三单为什么要加 s"、"非谓语动词怎么判断"、"语法填空怎么做"、"帮我找出我的语法弱项"、"这句话哪里错了"。不处理：整篇作文的三维批改（转英语写作进化教练）、发音与口语练习（转英语口语陪练）、单词记忆与复习提醒（转智能词汇DNA系统）。

**中文介绍**: 英语语法教练：用追问帮初中生与高中生自己发现语法错误，并在同意后记录语法弱项；高中覆盖必修与选择性必修。触发语："帮我检查这句英语的语法"、"我时态老是错"、"定语从句 who/which/where 怎么选"、"三单为什么要加 s"、"非谓语动词怎么判断"、"语法填空怎么做"、"帮我找出我的语法弱项"、"这句话哪里错了"。不处理：整篇作文的三维批改（转英语写作进化教练）、发音与口语练习（转英语口语陪练）、单词记忆与复习提醒（转智能词汇DNA系统）。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 英语语法突破教练, 英语语法教练, 用追问帮初中生与高中生自己发现语法错误, 并在同意后记录语法弱项, 高中覆盖必修与选择性必修, 触发语, who, which

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-english-grammar-coach)

---

## [25. 跨学科侦探周](https://clawhub.ai/qizhitang/xiaozhi-cross-subject-detective)

**Slug**: `xiaozhi-cross-subject-detective`  
**Version**: 2.9.0  
**Stats**: ⭐ 0 | ⬇️ 1405 | 🧩 25

**原始简介**: 用一个真实主题在一周内串联多门学科，找出学科之间的联结。学生说"跨学科侦探周"、"帮我联系不同学科的知识"、"丝绸之路能串哪些学科"、"我想做一个主题研究"、"历史和地理有什么关系"时可激活。流程是选题→多视角→逐科深潜→建立联结→整理项目记录，产出写进概念图谱。它不做单科解题（转对应学科教练）、不做错题分析（转错题本）、不替学生写研究报告。

**中文介绍**: 用一个真实主题在一周内串联多门学科，找出学科之间的联结。学生说"跨学科侦探周"、"帮我联系不同学科的知识"、"丝绸之路能串哪些学科"、"我想做一个主题研究"、"历史和地理有什么关系"时可激活。流程是选题→多视角→逐科深潜→建立联结→整理项目记录，产出写进概念图谱。它不做单科解题（转对应学科教练）、不做错题分析（转错题本）、不替学生写研究报告。

Latest changelog:
v2.9.0：详见仓库 docs/changelog.md

**关键词**: 跨学科侦探周, 用一个真实主题在一周内串联多门学科, 找出学科之间的联结, 产出写进概念图谱, v2.9.0, 详见仓库, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaozhi-cross-subject-detective)

---

