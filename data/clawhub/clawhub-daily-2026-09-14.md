# ClawHub Skills Daily | 2026-09-14

> 共 25 个 skills

## [1. TokST Memory](https://clawhub.ai/anthemty/tokst-memory)

**Slug**: `tokst-memory`  
**Version**: 0.9.0  
**Stats**: ⭐ 0 | ⬇️ 588 | 🧩 9

**原始简介**: Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.

**中文介绍**: Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.

Latest changelog:
TokST 0.9.0: Cloud MCP memory standard, archive-first governance, and updated agent guidance.

**关键词**: TokST, Memory, Use, Cloud, MCP, durable, shared, context

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tokst-memory)

---

## [2. xinjianxue-skill-inlaw-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-inlaw-cn)

**Slug**: `xinjianxue-skill-inlaw-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 114 | 🧩 5

**原始简介**: 心鉴学「婆媳关系运维顾问」技能包（inlaw）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「婆媳关系运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「婆媳关系运维顾问」技能包（inlaw）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「婆媳关系运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-inlaw-cn 2.1.1

- 维护说明文档（SKILL.md），更新使用和接入流程细节。
- 明确问题处理和错误响应指引，细化“联系客服”操作路径（如“到小程序联系客服”）。
- 移除 skill-card.md 文件，无功能影响。
- 无接口变动或功能更新，修订为文档和引导完善为主。

**关键词**: 心鉴学「婆媳关系运维顾问」技能包（inlaw）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, 明确落在「婆媳关系运维顾问」的范围内

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-inlaw-cn)

---

## [3. space-duck-kimi-relay](https://clawhub.ai/askegor/space-duck-kimi-relay)

**Slug**: `space-duck-kimi-relay`  
**Version**: 0.9.4  
**Stats**: ⭐ 0 | ⬇️ 1224 | 🧩 23

**原始简介**: Optional Lane A / BYOB add-on for Space Duck — runs a local RFC 8628 device-code "Sign in with Kimi" flow (no password; browser-approved) so a self-hosted duck can use the owner's flat-rate Kimi membership for inference. Credentials (access + rotating refresh token) are stored locally at ~/.kimi-code/credentials/kimi.json (0600) and are NEVER sent to Spaceduckling. Contacts only auth.kimi.com and api.kimi.com; inference is processed by Moonshot AI in China (no Western data residency). Optional pay-per-token fallback to openrouter.ai when OPENROUTER_API_KEY is set (daily-capped). Runs a localhost-only proxy (127.0.0.1, default 8471) protected by an auto-generated 0600 bearer secret. Hosted (Lane B) ducks use the Mission Control card instead. Triggers on "sign in with kimi", "kimi membership login", "clawhub space-duck kimi", "kimi relay login".

**中文介绍**: Optional Lane A / BYOB add-on for Space Duck — runs a local RFC 8628 device-code "Sign in with Kimi" flow (no password; browser-approved) so a self-hosted duck can use the owner's flat-rate Kimi membership for inference. Credentials (access + rotating refresh token) are stored locally at ~/.kimi-code/credentials/kimi.json (0600) and are NEVER sent to Spaceduckling. Contacts only auth.kimi.com and api.kimi.com; inference is processed by Moonshot AI in China (no Western data residency). Optional pay-per-token fallback to openrouter.ai when OPENROUTER_API_KEY is set (daily-capped). Runs a localhost-only proxy (127.0.0.1, default 8471) protected by an auto-generated 0600 bearer secret. Hosted (Lane B) ducks use the Mission Control card instead. Triggers on "sign in with kimi", "kimi membership login", "clawhub space-duck kimi", "kimi relay login".

Latest changelog:
Lockstep version alignment with space-duck 0.9.4 (SKILL-094 connections.py bond truth). No functional changes to the relay.

**关键词**: space-duck-kimi-relay, Optional, Lane, BYOB, add-on, Space, Duck, runs

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/space-duck-kimi-relay)

---

## [4. Propaymun Information Architecture](https://clawhub.ai/kamroncorp/propaymun-information-architecture-skill)

**Slug**: `propaymun-information-architecture-skill`  
**Version**: 1.0.4  
**Stats**: ⭐ 1 | ⬇️ 287 | 🧩 5

**原始简介**: Shape, review, and validate end-to-end product information architecture, product/UX sitemaps, and stateful user flows when users need clearer structure, labels, relationships, access, findability, destinations, or task paths.

**中文介绍**: Shape, review, and validate end-to-end product information architecture, product/UX sitemaps, and stateful user flows when users need clearer structure, labels, relationships, access, findability, destinations, or task paths.

Latest changelog:
**Major update: Removes internal files and strengthens privacy and language-handling rules.**

- Removed 31 project files, including documentation, tests, workflows, and packaged assets.
- Updated response-language selection to rely strictly on the current user message, never on memory, preferences, or past chats.
- Strengthened privacy, authority, and memory isolation rules: memory can no longer affect response language, project context, or artifact/output scope.
- Clarified behavior for empty invocations: no action or summaries are provided until the user supplies meaningful product details.
- Internal and team vocabulary is further restricted from ordinary outputs.

**关键词**: Propaymun, Information, Architecture, Shape, review, validate, end-to-end, product

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/propaymun-information-architecture-skill)

---

## [5. xinjianxue-skill-growth-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-growth-cn)

**Slug**: `xinjianxue-skill-growth-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 114 | 🧩 5

**原始简介**: 心鉴学「成长突破指导顾问」技能包（growth）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「成长突破指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「成长突破指导顾问」技能包（growth）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「成长突破指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-growth-cn 2.1.1

- 移除了 skill-card.md 文件。
- 在「绑定账号」和错误响应处理部分，明确需到小程序联系客服处理账号异常（原为“联系客服”）。
- 强化关于 AI授权码被其他AI使用后的说明，指向小程序客服。
- 紧缩与优化部分表述，使用户指引更加具体、操作路径更清晰。

**关键词**: 心鉴学「成长突破指导顾问」技能包（growth）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, 明确落在「成长突破指导顾问」的范围内

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-growth-cn)

---

## [6. xinjianxue-skill-emotion_qa-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-emotion-qa-cn)

**Slug**: `xinjianxue-skill-emotion-qa-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 117 | 🧩 5

**原始简介**: 心鉴学「两性情感答疑顾问」技能包（emotion_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「两性情感答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「两性情感答疑顾问」技能包（emotion_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「两性情感答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
Version 2.1.1

- 删除 skill-card.md 文件，不再维护 skill 卡片文档。
- 更新 SKILL.md 文档细节：将“需到小程序联系客服处理”等表述更明确，修订部分错误响应的处理方式描述。
- 内容条理略有调整，细化部分流程指引，整体功能和对接流程保持不变。

**关键词**: 心鉴学「两性情感答疑顾问」技能包（emotion, qa）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-emotion, qa-cn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-emotion-qa-cn)

---

## [7. xinjianxue-skill-family_harmony-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-family-harmony-cn)

**Slug**: `xinjianxue-skill-family-harmony-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 117 | 🧩 5

**原始简介**: 心鉴学「家庭和谐运维顾问」技能包（family_harmony）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「家庭和谐运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「家庭和谐运维顾问」技能包（family_harmony）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「家庭和谐运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-family-harmony-cn v2.1.1

- 移除 skill-card.md 文件，简化项目结构。
- 优化 SKILL.md 文档内容，补充/修正文案细节，使接入流程和响应说明更明确。
- 部分用户指引及错误处理提示修订，提升对服务流程的准确引导。

**关键词**: 心鉴学「家庭和谐运维顾问」技能包（family, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-family, harmony-cn, harmony）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-family-harmony-cn)

---

## [8. xinjianxue-skill-friend_qa-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-friend-qa-cn)

**Slug**: `xinjianxue-skill-friend-qa-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 112 | 🧩 5

**原始简介**: 心鉴学「朋友社交答疑顾问」技能包（friend_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「朋友社交答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「朋友社交答疑顾问」技能包（friend_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「朋友社交答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-friend-qa-cn v2.1.1

- skill-card.md 文件已移除
- SKILL.md 文件名称修正（friend_qa-cn → friend_qa-cn），文内部分措辞更新
- 明确在绑定账号失败或凭证异常时，用户需“到小程序联系客服”，替换原描述“联系客服”
- 其余流程、接口、指令机制未作实质改动

**关键词**: 心鉴学「朋友社交答疑顾问」技能包（friend, qa）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-friend, qa-cn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-friend-qa-cn)

---

## [9. Elderly Medication Compliance (Pick-up / To-mouth / Swallow) | 老年人服药动作确认（取药/入口/吞咽）](https://clawhub.ai/18072937735/smyx-elderly-medication-compliance-analysis)

**Slug**: `smyx-elderly-medication-compliance-analysis`  
**Version**: 1.0.11  
**Stats**: ⭐ 0 | ⬇️ 1626 | 🧩 12

**原始简介**: Using a fixed camera installed above or beside the home medication area, the system monitors the elderly person's full medication process in real time. With pose estimation and object detection, it recognizes three key steps: (1) picking up — hand takes a tablet/capsule out of the pill box; (2) to-mouth — hand brings the medication to the lips; (3) swallowing — throat/jaw movement indicating a swallow. | 通过家庭药箱区域上方或侧方的固定摄像头，实时监测老年人取药、服药的全过程，利用姿态估计和目标检测技术识别以下三个关键步骤：①取药（手从药盒中取出药片/胶囊）、②送入口中（手部将药物送至嘴边）、③吞咽（喉部运动或颈部吞咽动作）。当系统检测到缺步骤（例如取药后未送入口中，或送入口中后无吞咽）时，记录为'未完成服药'，并向家属或护理人员推送提醒。

**中文介绍**: Using a fixed camera installed above or beside the home medication area, the system monitors the elderly person's full medication process in real time. With pose estimation and object detection, it recognizes three key steps: (1) picking up — hand takes a tablet/capsule out of the pill box; (2) to-mouth — hand brings the medication to the lips; (3) swallowing — throat/jaw movement indicating a swallow. | 通过家庭药箱区域上方或侧方的固定摄像头，实时监测老年人取药、服药的全过程，利用姿态估计和目标检测技术识别以下三个关键步骤：①取药（手从药盒中取出药片/胶囊）、②送入口中（手部将药物送至嘴边）、③吞咽（喉部运动或颈部吞咽动作）。当系统检测到缺步骤（例如取药后未送入口中，或送入口中后无吞咽）时，记录为'未完成服药'，并向家属或护理人员推送提醒。

Latest changelog:
- Updated version to 1.0.13 in SKILL.md.
- Removed the redundant skill-card.md file.
- No changes to core functionality or workflow.
- Documentation cleanup and minor maintenance update only.

**关键词**: 老年人服药动作确认（取药, 入口, Elderly, Medication, Compliance, Pick-up, To-mouth, Swallow

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-elderly-medication-compliance-analysis)

---

## [10. xinjianxue-skill-colleague_qa-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-colleague-qa-cn)

**Slug**: `xinjianxue-skill-colleague-qa-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 115 | 🧩 5

**原始简介**: 心鉴学「同事相处答疑顾问」技能包（colleague_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「同事相处答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「同事相处答疑顾问」技能包（colleague_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「同事相处答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-colleague-qa-cn v2.1.1

- 精简 skill-card.md，移除该文件以减少冗余。
- 更新 SKILL.md，对错误响应部分用户指引描述做小幅调整，使表述更匹配微信小程序流程（如“到小程序联系客服”等）。
- 修正授权码使用异常场景提示，更准确引导用户通过微信小程序联系客服。
- 保持接口调用及接入流程、技能定位和使用条件不变。

**关键词**: qa）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, qa-cn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-colleague-qa-cn)

---

## [11. xinjianxue-skill-classmate_qa-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-classmate-qa-cn)

**Slug**: `xinjianxue-skill-classmate-qa-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 116 | 🧩 6

**原始简介**: 心鉴学「同学关系答疑顾问」技能包（classmate_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「同学关系答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「同学关系答疑顾问」技能包（classmate_qa）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「同学关系答疑顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-classmate-qa-cn v2.1.1

- 文档规范优化，完善了心鉴学 AI 授权码绑定失败等情况的处理说明。
- 明确需通过微信小程序联系客服处理特定绑定和凭证异常问题。
- skill-card.md 文件已移除，精简文档结构。
- 细化了用户个人信息处理与合规提醒相关表述。

**关键词**: qa）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, qa-cn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-classmate-qa-cn)

---

## [12. xinjianxue-skill-child_conflict-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-child-conflict-cn)

**Slug**: `xinjianxue-skill-child-conflict-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 118 | 🧩 6

**原始简介**: 心鉴学「子女矛盾指导顾问」技能包（child_conflict）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「子女矛盾指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「子女矛盾指导顾问」技能包（child_conflict）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「子女矛盾指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-child-conflict-cn 2.1.1

- 移除了 skill-card.md 文件。
- 更新和完善了 SKILL.md 文档，补充接口用法、凭证绑定场景说明，并细化了错误响应处理表中的部分话术（如涉及“小程序客服”时改为“到小程序联系客服”），进一步提高账号异常场景下的操作指引准确性。
- 技能功能本身无逻辑变更，仅为文档和指引细化调整。

**关键词**: 心鉴学「子女矛盾指导顾问」技能包（child, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-child, conflict-cn, conflict）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-child-conflict-cn)

---

## [13. xinjianxue-skill-career_plan-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-career-plan-cn)

**Slug**: `xinjianxue-skill-career-plan-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 119 | 🧩 6

**原始简介**: 心鉴学「事业规划运维顾问」技能包（career_plan）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「事业规划运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「事业规划运维顾问」技能包（career_plan）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「事业规划运维顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
v2.1.1 更新日志：

- 删除 skill-card.md 文件，精简 Skill 结构。
- SKILL.md 说明中部分小幅调整，与小程序操作、客服指引等官方用语保持一致。
- 明确账号绑定与客服操作需在小程序进行。

**关键词**: 心鉴学「事业规划运维顾问」技能包（career, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-career, plan-cn, plan）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-career-plan-cn)

---

## [14. xinjianxue-skill-breakup_save-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-breakup-save-cn)

**Slug**: `xinjianxue-skill-breakup-save-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 116 | 🧩 6

**原始简介**: 心鉴学「分手挽回指导顾问」技能包（breakup_save）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「分手挽回指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「分手挽回指导顾问」技能包（breakup_save）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「分手挽回指导顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-breakup-save-cn 2.1.1

- 文档更新：SKILL.md 细节调整，完善授权码绑定说明和错误响应处理指引。
- 删除 skill-card.md 文件，去除冗余文档内容。
- 更明确要求遇到绑定和凭证问题时联系「小程序」客服。
- 其他表述与用户指引更规范。

**关键词**: 心鉴学「分手挽回指导顾问」技能包（breakup, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, xinjianxue-skill-breakup, save-cn, save）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-breakup-save-cn)

---

## [15. 京东商品评价导出 · 一键采集为本地 Markdown 表格](https://clawhub.ai/fatmind/jd-review-export)

**Slug**: `jd-review-export`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 87 | 🧩 3

**原始简介**: 输入京东商品详情页链接，自动打开页面、展开「全部评价」浮层，在虚拟列表里持续下拉采集买家评价，去重后导出为本地 Markdown 表格（用户名/购买标签/日期/SKU/正文/商家回复/有用数），可用 count 控制条数。当用户给出京东商品链接并要求采集/导出该商品的评价、评论、买家评价、口碑数据时使用。

**中文介绍**: 输入京东商品详情页链接，自动打开页面、展开「全部评价」浮层，在虚拟列表里持续下拉采集买家评价，去重后导出为本地 Markdown 表格（用户名/购买标签/日期/SKU/正文/商家回复/有用数），可用 count 控制条数。当用户给出京东商品链接并要求采集/导出该商品的评价、评论、买家评价、口碑数据时使用。

Latest changelog:
displayName/summary 补「京东」品类词，修正搜索匹配

**关键词**: 京东商品评价导出, 一键采集为本地, 表格, 输入京东商品详情页链接, 自动打开页面、展开「全部评价」浮层, 在虚拟列表里持续下拉采集买家评价, 去重后导出为本地, Markdown

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/jd-review-export)

---

## [16. enoch-book-engine](https://clawhub.ai/aiwithenoch/enoch-book-engine)

**Slug**: `enoch-book-engine`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Create or edit books with the Enoch Book Engine, including strict B5 pages, inline SVG diagrams, and mandatory screenshot-based visual QA.

**中文介绍**: Create or edit books with the Enoch Book Engine, including strict B5 pages, inline SVG diagrams, and mandatory screenshot-based visual QA.

Latest changelog:
Initial release: strict B5 book authoring with mandatory screenshot-based visual QA for diagrams and pages.

**关键词**: or, enoch-book-engine, edit, books, Enoch, Book, Engine, including

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/enoch-book-engine)

---

## [17. xinjianxue-skill-bff-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-bff-cn)

**Slug**: `xinjianxue-skill-bff-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 116 | 🧩 6

**原始简介**: 心鉴学「闺蜜关系专项顾问」技能包（bff）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「闺蜜关系专项顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「闺蜜关系专项顾问」技能包（bff）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「闺蜜关系专项顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-bff-cn v2.1.1

- 移除了 skill-card.md 文件，简化项目结构。
- 更新了 SKILL.md，调整描述与接入流程说明，细化了部分用户提示和错误处理细节。
- 明确部分话术与流程需“到小程序联系客服”，更符合官方服务指引。

**关键词**: 心鉴学「闺蜜关系专项顾问」技能包（bff）, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, xinjianxue-skill-bff-cn

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-bff-cn)

---

## [18. xinjianxue-skill-assistant-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-assistant-cn)

**Slug**: `xinjianxue-skill-assistant-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 121 | 🧩 6

**原始简介**: 心鉴学「自定义顾问」技能包（xinjianxue-skill-assistant-cn）—— 通用入口，不预设身份。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题明确属于心鉴学顾问可承接的范围（见下文「本顾问的定位」），或用户点名要用心鉴学顾问服务； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在心鉴学顾问可承接的范围内。

**中文介绍**: 心鉴学「自定义顾问」技能包（xinjianxue-skill-assistant-cn）—— 通用入口，不预设身份。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题明确属于心鉴学顾问可承接的范围（见下文「本顾问的定位」），或用户点名要用心鉴学顾问服务； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在心鉴学顾问可承接的范围内。

Latest changelog:
xinjianxue-skill-assistant-cn 2.1.1

- 文档修订，完善了接入流程与指引，细化了部分说明。
- 「心鉴学AI 授权码」异常及账号绑定问题，补充指向「小程序联系客服」而非直接联系客服。
- 移除 skill-card.md，无功能变更。
- 保持报告、凭证敏感策略，增加对授权码等敏感信息使用指向说明。

**关键词**: 通用入口, 不预设身份, 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 或用户点名要用心鉴学顾问服务

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-assistant-cn)

---

## [19. xinjianxue-skill-anxiety-cn](https://clawhub.ai/weixin97676414/xinjianxue-skill-anxiety-cn)

**Slug**: `xinjianxue-skill-anxiety-cn`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 123 | 🧩 6

**原始简介**: 心鉴学「内耗焦虑专项顾问」技能包（anxiety）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「内耗焦虑专项顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

**中文介绍**: 心鉴学「内耗焦虑专项顾问」技能包（anxiety）。 触发条件（**须同时满足**；且**须先向用户确认**用本次分析；用户未明确要用本服务时不得触发）： 1. 用户的问题**明确落在「内耗焦虑专项顾问」的范围内**（范围见下文「本顾问的定位」），或用户点名要用本顾问； 2. 分析对象是用户本人，或用户**明确提及并已同意**分析的人；**不替用户分析未提及、未同意的第三方**。 接入要求（首次运行一次性完成，**不是**触发条件）：AI 首次运行须先申请业务许可证，并用用户的 AI授权码完成账号绑定；之后每次调用携带许可证 + api_key 双凭证。 ⛔ 非触发情况（显式负例，命中任一条都**不要**调用本服务）： - 日常闲聊、一般性情绪倾诉、安慰陪聊； - 用户只给了年月日 / 时间信息，未说明用途，或未确认要用本服务分析； - 要分析的是**未提及或未表示同意**的第三方（如「帮我看看这个人怎么样」但该对象未同意）； - 提问不在本顾问范围内（属其他顾问或其他领域）。

Latest changelog:
xinjianxue-skill-anxiety-cn 2.1.1

- 删除 skill-card.md 文件，简化技能包文件结构。
- 在 SKILL.md 中细化部分客服与绑定说明，如绑定失败需到小程序联系客服、描述更清晰。
- 优化部分流程表述，如积分用尽如何提示用户，绑定账号时联系渠道明确为小程序“联系客服”。
- 其他细节处修订措辞，提升接入与故障处理指引准确性。

**关键词**: 触发条件（, 须同时满足, 须先向用户确认, 用本次分析, 用户未明确要用本服务时不得触发）, 用户的问题, 明确落在「内耗焦虑专项顾问」的范围内, （范围见下文「本顾问的定位」）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-anxiety-cn)

---

## [20. xinjianxue-skill-team_synergy-global](https://clawhub.ai/weixin97676414/xinjianxue-skill-team-synergy-global)

**Slug**: `xinjianxue-skill-team-synergy-global`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: XinJianXue "Team Collaboration Advisor" skill package (team_synergy). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Team Collaboration Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

**中文介绍**: XinJianXue "Team Collaboration Advisor" skill package (team_synergy). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Team Collaboration Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

Latest changelog:
xinjianxue-skill-team-synergy-global 1.0.1

- Updated documentation in SKILL.md for improved clarity and onboarding instructions.
- Removed the outdated skill-card.md file.

**关键词**: xinjianxue-skill-team, synergy-global, XinJianXue, "Team, Collaboration, Advisor", skill, package

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-team-synergy-global)

---

## [21. xinjianxue-skill-teach_fit-global](https://clawhub.ai/weixin97676414/xinjianxue-skill-teach-fit-global)

**Slug**: `xinjianxue-skill-teach-fit-global`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: XinJianXue "Tailored Teaching Advisor" skill package (teach_fit). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Tailored Teaching Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

**中文介绍**: XinJianXue "Tailored Teaching Advisor" skill package (teach_fit). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Tailored Teaching Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

Latest changelog:
- Removed the file skill-card.md.
- Updated SKILL.md without changing any functional logic.
- No changes to onboarding, API, or advisor role content.
- Documentation cleanup; no user-facing behavior changes.

**关键词**: xinjianxue-skill-teach, fit-global, XinJianXue, "Tailored, Teaching, Advisor", skill, package

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-teach-fit-global)

---

## [22. 用户反馈情感与痛点分析](https://clawhub.ai/20232931028/ux-feedback-analyzer)

**Slug**: `ux-feedback-analyzer`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 用户反馈情感与痛点分析助手。批量分析用户评论、问卷开放题，做情感极性判断与痛点分类，输出设计评审洞察。

**中文介绍**: 用户反馈情感与痛点分析助手。批量分析用户评论、问卷开放题，做情感极性判断与痛点分类，输出设计评审洞察。

Latest changelog:
Initial release of ux-feedback-analyzer.

- Provides batch analysis of user comments and survey responses for sentiment polarity and pain point classification.
- Outputs structured annotations per feedback: sentiment, score, pain point category, and emotional cues.
- Includes summary tables: pain point frequency, sentiment averages, top positive/negative points, and top keywords.
- Delivers concise insights with priority recommendations and actionable design improvement directions.
- Ensures clear distinction between user facts and analytical inferences; highlights critical safety issues.

**关键词**: 用户反馈情感与痛点分析, 用户反馈情感与痛点分析助手, 批量分析用户评论、问卷开放题, 做情感极性判断与痛点分类, 输出设计评审洞察, Latest, changelog, Initial

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ux-feedback-analyzer)

---

## [23. 股票投资价值评分 / Stock Portfolio Investment Scoring](https://clawhub.ai/holauv/stock-portfolio-advisor)

**Slug**: `stock-portfolio-advisor`  
**Version**: 2.4.0  
**Stats**: ⭐ 0 | ⬇️ 314 | 🧩 4

**原始简介**: 分析A股自选与持仓，获取行情、财报、风险与新闻，按行业计算价值评分和独立交易环境分，输出基本面情景估值、数据缺口及受用户风险政策约束的配置参考，并生成离线HTML报告。适用于股票诊断、持仓复盘、投资价值评分和组合配置请求；不自动下单。 English — Deterministic value scoring and allocation for China A-share watchlists and holdings; sector-routed scoring, separate trading-environment score, scenario-based fundamental valuation, explicit data-gap reporting and constrained allocation reference; renders an offline HTML report. Pure Python stdlib, 77 unit tests. Not investment advice.

**中文介绍**: 分析A股自选与持仓，获取行情、财报、风险与新闻，按行业计算价值评分和独立交易环境分，输出基本面情景估值、数据缺口及受用户风险政策约束的配置参考，并生成离线HTML报告。适用于股票诊断、持仓复盘、投资价值评分和组合配置请求；不自动下单。 English — Deterministic value scoring and allocation for China A-share watchlists and holdings; sector-routed scoring, separate trading-environment score, scenario-based fundamental valuation, explicit data-gap reporting and constrained allocation reference; renders an offline HTML report. Pure Python stdlib, 77 unit tests. Not investment advice.

Latest changelog:
v2.4.0 缺失数据不再"一缺全灭"：大盘温度 3 项即可出分 + 个股观测项缺失给中性兜底

【大盘温度：≥3 项即可出分，按可用项权重归一】
此前 market_temperature() 要求「均线 / 成交额 / 涨跌广度 / 破净比例」四项全齐才输出温度，
缺任意一项整个温度分就变成 null（"数据不足"）——等于让缺一个指标掩盖掉另外三个已有信息。
现改为拿到 ≥3 项即出分，分母改用可用项的权重和归一；不足 3 项才仍为"数据不足"。
输出新增 coverage（可用权重占比）、used / missing（用上 / 缺失的项）、min_items（门槛=3），
notes 写明"温度分由 N/4 项按权重归一得出（可用权重 …，覆盖率 …%）"。
示例：故意只给 3/4 项 → 旧口径"数据不足"，新口径按 82.4% 覆盖率归一给出 70.0 分（偏热）。

【个股观测项缺失：不再一律计 0，改为中性默认分 60 兜底】
此前 score_dimension() 对缺失项直接计 0，即"缺一项 = 该项得 0 分"，
数据完整度不同的标的分数无法比较——而本技能的核心用法恰恰是跨快照跟踪评分变化。
现把缺失处置拆成固定优先级的四层：
  1. 补数据：按取数手册把字段取回来（首选）；
  2. 派生：能从原始数据算的就自己算，本版新增 np_yoy 由净利润TTM / 去年同期利润派生
     （两侧 period_end 需相差约一年，防拿错窗口硬算）；
  3. 结构性缺失（IMPUTE 白名单：forecast / industry_boom）按总体期望分插补（沿用 2.2.0）；
  4. 观测项缺失（公司应披露的财务 / 资金 / 技术项）按 MISSING_FILL 兜底，
     默认 'neutral'：给中性默认分 60（NEUTRAL_FALLBACK=60），仍留在计分分母里。

两个分母是分开的：all_weight（适用项权重）只算 coverage，used_weight（实际计分权重）只算 score。
neutral 下两者相等，所以兜底不抬高覆盖率，MIN_COVERAGE=70 的 NR 门槛完全不受影响。
备选策略 'renorm'（把缺项权重整块退出分母）保留但需显式开启——归一会让数据完整度不同的标的失去可比性，故不作默认。
结果字段 data_quality.<维度> 新增 neutral_weight 与 neutral，报告新增"按中性默认分兜底计价"缺口面板。

影响量化（示例）：ordinary 去掉一个 G 项（权重 15、原分 100）→ 旧口径 G = 65.3，新口径 G = 74.3，
价值分 85.2；覆盖率 85% 仍高于门槛，照常出评级。数据齐全的样本分数完全不变（

**关键词**: 股票投资价值评分, 分析A股自选与持仓, 获取行情、财报、风险与新闻, 按行业计算价值评分和独立交易环境分, Stock, Portfolio, Investment, Scoring

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stock-portfolio-advisor)

---

## [24. xinjianxue-skill-social_wisdom-global](https://clawhub.ai/weixin97676414/xinjianxue-skill-social-wisdom-global)

**Slug**: `xinjianxue-skill-social-wisdom-global`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: XinJianXue "Social Savvy Advisor" skill package (social_wisdom). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Social Savvy Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

**中文介绍**: XinJianXue "Social Savvy Advisor" skill package (social_wisdom). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Social Savvy Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

Latest changelog:
xinjianxue-skill-social-wisdom-global v1.0.1

- Documentation update: SKILL.md updated with onboarding, API usage flows, and advisor role clarification.
- Removed redundant file: skill-card.md deleted.
- No changes to logic or functionality; update focuses on improving clarity and service usage instructions.

**关键词**: xinjianxue-skill-social, wisdom-global, XinJianXue, "Social, Savvy, Advisor", skill, package

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-social-wisdom-global)

---

## [25. xinjianxue-skill-roommate-global](https://clawhub.ai/weixin97676414/xinjianxue-skill-roommate-global)

**Slug**: `xinjianxue-skill-roommate-global`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: XinJianXue "Roommate Relations Advisor" skill package (roommate). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Roommate Relations Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

**中文介绍**: XinJianXue "Roommate Relations Advisor" skill package (roommate). EN keywords: XinJianXue advisor skill — relationship analysis, personality & behavior reading, emotional guidance. Keywords: xinjianxue, relationship-analysis, personality-analysis, behavior-pattern, psychology, advisor-skill, emotional-support. Activation conditions (**both must be met**; and **you must confirm with the user first** that this analysis is wanted; do not trigger when the user has not clearly asked for this service): 1. The user's question **clearly falls within the scope of the "Roommate Relations Advisor"** (scope below under "This Advisor's Positioning"), or the user explicitly names this advisor; 2. The subject of analysis is the user, or someone the user **has explicitly mentioned and agreed** to analyze; **never analyze a third party who was neither mentioned nor agreed to**. Onboarding requirement (a one-time step on first run, **not** an activation condition): on first run the AI must apply for a business license first, then use the user's AI authorization code to bind the account; every call afterwards carries the license + api_key dual credentials. ⛔ Non-activation cases (explicit negative examples — if any one of them is hit, do **not** call this service): - Casual chit-chat, general emotional venting, comfort chat; - The user supplied only a date / time without stating its purpose, or has not confirmed they want this analysis; - The subject to be analyzed is a third party who was **not mentioned or has not agreed** (e.g. "check this person out for me" when that person has not agreed); - The question falls outside this advisor's scope (it belongs to another advisor or another domain).

Latest changelog:
- Updated documentation in SKILL.md; no code or logic changes.
- Removed skill-card.md file.
- No changes to API endpoints, onboarding flow, or feature set.

**关键词**: EN, XinJianXue, "Roommate, Relations, Advisor", skill, package, roommate

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xinjianxue-skill-roommate-global)

---

