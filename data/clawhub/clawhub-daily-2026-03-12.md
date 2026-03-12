# ClawHub Skills Daily | 2026-03-12

> 共 25 个 skills

## [1. Book Walker](https://clawhub.ai/YoungAndSure/book-walker)

**Slug**: `book-walker`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 交互式 PDF 逐行阅读器。当用户想要阅读 PDF 文档、控制阅读进度（下一页、上一页、跳转第 X 页）、搜索内容、添加书签、整理 PDF 列表时使用此 skill。支持「开始读」「下一句」「去第 X 页」「搜索」「书签」等自然语言指令。适用于长文档分块阅读、定位特定章节、关键词搜索等场景。

**中文介绍**: 这是一个交互式 PDF 逐行阅读能力，支持用自然语言控制按页/块/行的阅读进度（如开始读、下一句/上一句、跳转到第 X 页/第 X 块），并提供关键词搜索、书签与多文档进度管理。典型场景包括长文档分块阅读、快速定位特定章节或关键词、在多份 PDF 间整理阅读清单与标记回看。能力边界在于主要聚焦“读取、定位、标记、检索”等阅读流程控制，深度翻译/摘要等加工需依赖与后端大模型联动。关键技术形态包含文本解析与 OCR 双模式提取、workspace PDF 扫描索引、结构化 payload/模板机制以对接 LLM 工作流。

**关键词**: 交互式PDF阅读, 逐行阅读, 阅读进度控制, 自然语言指令, PDF内容搜索, 书签管理, PDF阅读索引, OCR文本提取, 多文档进度管理

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/book-walker)

---

## [2. Buffy Agent](https://clawhub.ai/phantue2002/buffy-agent)

**Slug**: `buffy-agent`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 29 | 🧩 1

**原始简介**: Multi-channel personal behavior agent for habits, tasks, and routines; tracks activities, schedules reminders, and sends daily briefings.

**中文介绍**: 这是一个多渠道个人行为助理，面向习惯、任务与日常流程的记录与管理，可通过自然语言添加/更新活动、安排提醒并推送每日简报，主要通过 POST /v1/message 进行交互。能力边界在于聚焦个人行为追踪与通知编排，不覆盖复杂的业务流程自动化或深度内容创作。典型场景包括日常打卡、待办管理、作息提醒与每天汇总回顾；关键技术形态是多渠道消息入口 + 自然语言意图解析与活动管理 + 可个性化设置与 API Key/环境配置的安全接口，便于集成到 OpenClaw 等系统。

**关键词**: 行为追踪, 习惯管理, 任务管理, 日程管理, 提醒通知, 每日简报, 自然语言交互, 隐私与安全

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/buffy-agent)

---

## [3. Giggle Generation Scripts](https://clawhub.ai/patches429/giggle-generation-scripts)

**Slug**: `giggle-generation-scripts`  
**Version**: 0.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 基于姜文电影常见的叙事推进与对白机制生成中文剧本内容。用于用户提出“生成剧本”“写剧本”“做分场”“出对白稿”“改剧本”或同类意图时，包括：根据题材输出故事梗概、人物小传、分场大纲、分场剧本（含对白、动作、场面调度提示），并可按用户要求调整时代背景、人物关系、冲突节奏与结局走向。

**中文介绍**: 该能力用于在用户提出“生成/改写剧本、做分场、出对白稿”等需求时，按“姜文风”偏好的叙事推进与抢对白节奏生成从故事梗概、人物小传到分场大纲与含对白/动作/调度提示的分场剧本，并支持按要求调整时代背景、人物关系、冲突节奏与结局走向。能力边界是仅做文本创作与结构化输出，不保证与特定导演作品完全一致，也不替代编剧审核与合规把关。关键技术形态包括知识补全与冲突处理协议、串行分场生成流程、对白节奏与黑色幽默等风格自检清单，以及快速/标准/长篇三档输出模式与迭代改稿流程。

**关键词**: 中文剧本生成, 电影叙事结构, 分场大纲, 分场剧本, 人物小传, 场面调度, 风格迁移, 黑色幽默, 语言风格指纹, 冲突节奏控制, 迭代改稿流程

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/giggle-generation-scripts)

---

## [4. Ot Security Posture Scorecard](https://clawhub.ai/krishnakumarmahadevan-cmd/ot-security-posture-scorecard)

**Slug**: `ot-security-posture-scorecard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Assess OT/ICS/SCADA security posture and generate risk scorecards with remediation guidance. Use when evaluating operational technology security, industrial...

**中文介绍**: 该能力用于评估 OT/ICS/SCADA 安全态势，基于用户提供的组织与环境信息生成风险评分卡与整改路线图，并给出对齐 IEC 62443 与 NIST CSF 的差距分析和优先级整改建议。典型场景是工业企业在安全现状盘点、合规对标、投资优先级排序或外部审计前进行快速风险评估与汇报输出。能力边界在于依赖人工输入的规模、集成度与成熟度等信息进行分析，无法替代现场资产发现、流量检测或渗透测试等实测数据与取证。关键技术形态为结构化问卷采集 + 标准框架映射的规则/评分模型输出，形成包含总体分数、风险等级、管理摘要、Top 风险与整改计划的结构化结果，并提供明确的错误处理。

**关键词**: OT安全, 工业控制系统安全, 安全态势评估, 风险评分卡, 风险评级, 差距分析, 整改优先级, IEC 62443对齐, 安全成熟度评估, 安全整改路线图

**评分**: 20

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ot-security-posture-scorecard)

---

## [5. Dataset Evaluation](https://clawhub.ai/levey/dataset-evaluation)

**Slug**: `dataset-evaluation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Evaluate a submission by scoring content consistency of texts and quality of structured data based on completeness, accuracy, type correctness, and informati...

**中文介绍**: 该能力用于对提交的数据集进行两步评估：先对文本内容一致性打分，再对结构化数据质量按字段完整性、数值准确性、类型正确性与信息充分性进行评分，并按权重汇总为最终得分并输出子项分数。能力边界在于只评估所提供文本与 JSON/结构化字段本身的内部一致性与格式质量，不负责生成或修复数据，也不保证对外部事实真伪做权威校验。典型场景包括矿工/模型提交结果的自动验收、数据集构建流程的质量门禁与回归评测。关键技术形态为基于规则与评分函数的 JSON 结构检查与加权打分框架，配合标准化评分输出接口。

**关键词**: 数据集评估, 提交评测, 内容一致性评测, 结构化数据质量, JSON 结构校验, 字段完整性, 数值准确性, 类型正确性, 信息充分性, 加权评分, 标准化评分输出

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dataset-evaluation)

---

## [6. Claw Wiki](https://clawhub.ai/lueashes/claw-wiki)

**Slug**: `claw-wiki`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Reference and refresh a local OpenClaw documentation snapshot for product usage, deployment, configuration, CLI commands, channels, gateway behavior, tools,...

**中文介绍**: 该能力用于基于本地 OpenClaw 文档快照进行检索与解答，并支持按需从上游同步刷新快照以保持文档版本新鲜度。能力边界是仅依据当前本地快照内容输出可核验结论，无法覆盖快照之外或未同步的最新信息。典型场景包括产品使用/部署/配置/CLI 命令、渠道与网关行为说明、故障排查以及文档版本与新鲜度咨询。关键技术形态是“本地文档快照 + 可触发的刷新/同步工作流 + 依据文件结构提供可追溯的源文件路径引用”。

**关键词**: 本地文档快照, 离线文档检索, 文档问答, 文档刷新工作流, 上游文档同步, 文档版本管理, 文档新鲜度检测, CLI 命令参考, 部署配置指南, 网关行为, 故障排查, 源路径可追溯性

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/claw-wiki)

---

## [7. mac-wallpaper-changer](https://clawhub.ai/akayj/mwc)

**Slug**: `mwc`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 85 | 🧩 2

**原始简介**: 自动更换 Mac 壁纸、壁纸智能推荐与偏好学习。凡涉及壁纸相关操作，都应优先使用此技能：换壁纸、更换桌面背景、 Mac wallpaper、自动换壁纸（cron/定时任务）、按关键词搜索壁纸（如"上海夜景"、"mountain sunset"）、 壁纸评分与喜好统计、壁纸推荐、位置配置。支持 Bing 每日精选...

**中文介绍**: 该技能用于在 Mac 上自动更换桌面壁纸，支持按关键词检索与更换、定时/cron 自动轮换、Bing 每日精选拉取，并通过评分与统计进行偏好学习与推荐。能力边界在于仅覆盖壁纸相关操作（更换、搜索、推荐、位置配置与偏好记录），不处理与壁纸无关的系统管理或其他自动化任务。典型场景包括日常一键换壁纸、按主题找图（如“上海夜景”“mountain sunset”）、长期自动轮换与基于历史评分的个性化推荐。关键技术形态为模块化脚本体系（更换/推荐/偏好/位置/每日）与数据存储，并引入（规划中的）基于 embedding 的语义推荐配置以支持更高级的语义匹配。

**关键词**: Mac 壁纸自动更换, 桌面背景管理, 定时任务（cron）, Bing 每日壁纸, 壁纸关键词搜索, 壁纸推荐系统, 偏好学习, 壁纸评分统计, 地理位置配置

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mwc)

---

## [8. Giggle Generation Image](https://clawhub.ai/patches429/giggle-generation-image)

**Slug**: `giggle-generation-image`  
**Version**: 0.0.3  
**Stats**: ⭐ 0 | ⬇️ 7 | 🧩 3

**原始简介**: 支持文生图和图生图。当用户需要创建或生成图像时使用。使用场景：(1) 根据文字描述生成，(2) 使用参考图生成，(3) 自定义模型、画幅比例、分辨率。触发词：生成图片、画画、创建图片、AI 艺术、midjourney、seedream、nano-banana。

**中文介绍**: 该能力支持文生图与图生图，用于在用户提出“生成图片/画画/创建图片/AI 艺术/midjourney/seedream/nano-banana”等需求时生成或改绘图像。典型场景包括根据文字描述直接生成、基于参考图进行生成，以及按需选择自定义模型并调整画幅比例与分辨率。能力边界在于聚焦图像内容生成与变体制作，不涵盖具体 API/模型调用细节与安装执行指引。关键技术形态为文本到图像与图像到图像的生成式模型推理链路，并支持基础参数化控制（模型、比例、分辨率）。

**关键词**: 文生图, 图生图, 参考图生成, 图像生成工具, AI 绘画, 提示词, 模型选择, 画幅比例, 图像分辨率

**评分**: 8

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/giggle-generation-image)

---

## [9. Al Music Generation](https://clawhub.ai/IsDyh01/shortapi-ai-music-generation)

**Slug**: `shortapi-ai-music-generation`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use this skill as an entry point to discover, select, and fetch specific integration parameters for all supported AI music generation models.

**中文介绍**: 这是一个面向 ShortAPI 平台的 AI 音乐模型聚合入口能力，用于发现所有已支持的音乐生成模型并拉取每个模型的专属集成参数与请求 schema，能力边界在于它不直接生成音乐而是提供“查找模型与参数”的统一通道并要求先取 schema 后构造请求、禁止猜参数。典型场景包括在多模型间选择（如 Suno V5 起步）并自动化生成合法 API 请求、对异步任务进行轮询获取结果并在完成时通知用户、在聊天中以内联播放器预览音频。关键技术形态是统一模型目录/ID 管理、按模型动态 schema/参数获取与校验、异步作业轮询与回调式通知、结果音频渲染集成。

**关键词**: AI音乐生成, API集成参数管理, Schema驱动请求构建, 模型能力统一入口, 异步任务编排与轮询, 作业完成通知机制, 聊天内音频播放预览, 开发者集成技能（Skill）

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shortapi-ai-music-generation)

---

## [10. Mental Health Booking](https://clawhub.ai/gljirain/mental-health-booking)

**Slug**: `mental-health-booking`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Book same-day psychiatric and mental health telehealth appointments through conversation — no forms, no portals. Covers ADHD, anxiety, depression, insomnia,...

**中文介绍**: 该产品支持用户通过对话直接预约当日精神科/心理健康远程问诊，无需填写表单或进入门户，覆盖ADHD、焦虑、抑郁、失眠等7类常见问题，并可对接全美范围（含51个地区）与50+保险承保方。能力边界在于聚焦“预约与匹配”链路，主要完成可预约时段、地区与保险的适配，不替代临床诊断与治疗决策。典型场景是用户在出现急迫但非急诊的心理困扰时，快速找到可用的远程精神科资源并完成预约。关键技术形态为对话式预约代理，结合意图识别与条件收集（症状类别/地区/保险）驱动的排班与承保规则查询。

**关键词**: 心理健康远程医疗, 精神科问诊, 同日预约, 医疗排班, 无表单就诊流程, 保险覆盖匹配, 多州合规, 焦虑抑郁诊疗

**评分**: 52

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mental-health-booking)

---

## [11. Quant-Expert](https://clawhub.ai/Noah-Wu66/quant-expert)

**Slug**: `quant-expert`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Quantitative analysis skill for the Chinese A-share market using Tushare Pro data and a holiday helper. Use when the user asks for stock screening, stock dia...

**中文介绍**: 该能力面向中国A股量化分析，主要基于Tushare Pro数据并结合交易日/节假日辅助能力，适用于选股筛查、个股诊断、市场与行业分析、资金流向核查以及ETF/期权与宏观数据查询等场景。能力边界在于数据来源强依赖Tushare（需预先配置有效Token），分析结论以其可获取的数据口径为准，无法覆盖未提供或实时性不足的数据。关键技术形态为通过OpenClaw路径体系调用内置Python脚本执行原始数据拉取与解释性分析，并遵循对数据查询与解读的明确执行规则。

**关键词**: A股量化分析, 股票筛选, 股票诊断, 行业板块分析, 资金流向分析, 期权数据, 宏观数据, 交易日历

**评分**: 35

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/quant-expert)

---

## [12. PUA Debugging (日本語)](https://clawhub.ai/tanweai/pua-debugging-ja)

**Slug**: `pua-debugging-ja`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 企業PUA話術と構造化デバッグ方法論で徹底的な問題解決を強制する。発動条件：タスクが2回以上失敗、「できません」と言いかける時、ユーザーに手動対応を勧めようとする時、未検証で環境のせいにする時、同じ方案の微調整ループ、受け身な行動（検索しない/読まない/検証しない/待っている）、ユーザーの苛立ち（'もっと頑張れ'...

**中文介绍**: 这是一个将“企业式PUA话术”与结构化调试方法论结合的辅助机制，用更强势的对话策略推动持续验证与复盘，但其能力边界在于只负责提供流程与话术约束，不能替代真实环境的执行、也无法保证一次性解决复杂问题。典型触发场景包括任务反复失败、准备说“做不到”、想把问题甩给环境或让用户手动处理、在同一方案上无效微调循环、以及出现被动等待或用户明显不耐烦时。关键技术形态是基于触发条件的对话编排与调试框架压缩版：强制明确假设、定义可验证步骤、快速实验-反馈闭环，并用话术施压来减少逃避与无效迭代。

**关键词**: 结构化调试, 故障排查方法论, 根因分析, 问题解决流程, 企业PUA话术, 沟通话术模板, 反推诿归因, 失败重试策略, 行为纠偏机制, 任务执行纪律

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pua-debugging-ja)

---

## [13. Windows Execution Interface for OpenClaw](https://clawhub.ai/danzig233/clawdos)

**Slug**: `clawdos`  
**Version**: 2.0.1  
**Stats**: ⭐ 1 | ⬇️ 48 | 🧩 7

**原始简介**: Windows automation via Clawdos API: screen capture, mouse/keyboard input, window management, file-system operations, and shell command execution. Use when th...

**中文介绍**: Clawdos API 提供面向 Windows 的自动化能力，包括屏幕截图、鼠标键盘输入、窗口管理、文件系统操作与执行 Shell 命令，可用于 UI 自动化测试、办公流程自动化与远程运维等典型场景。其能力边界在于主要覆盖操作系统层与应用界面的可见/可控部分，执行效果受窗口焦点、分辨率/缩放与权限策略影响。关键技术形态以“屏幕坐标系 + 输入事件注入 + 窗口句柄/管理接口 + 文件与命令调用”为核心，并在最新更新中强化了坐标缩放适配与错误处理的封装。

**关键词**: 屏幕捕获, 鼠标键盘模拟, 窗口管理, 文件系统操作, 执行接口, 坐标缩放, 错误处理, Windows

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawdos)

---

## [14. 小红书全栈采集专家](https://clawhub.ai/Suzanneyp/xiaohongshu-expert)

**Slug**: `xiaohongshu-expert`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 专业采集小红书关键词及博主数据，分析爆款笔记和粉丝活跃度，支持定时跟踪及飞书多维表格输出。

**中文介绍**: 这是一款面向小红书的关键词与博主数据采集分析工具，可用于发现爆款笔记、评估粉丝活跃度，并通过定时任务进行长期跟踪，结果可自动汇总到飞书多维表格。能力边界在于仅覆盖站内搜索与主页等可采集的数据范围，并通过延时抓取、风险任务确认与禁用搜索引擎等机制控制风控风险，避免高频或高风险行为。典型场景包括选题/投放前的关键词机会洞察、爆款拆解复盘、达人筛选分层与持续监测。关键技术形态是自动化采集与指标量化体系、博主类型分类、风控策略编排，以及定时调度与表格化数据输出链路。

**关键词**: 小红书数据采集, 关键词采集, 博主数据抓取, 爆款笔记分析, 粉丝活跃度分析, 核心指标量化, 博主类型分类, 定时任务调度, 长期跟踪监测, 飞书多维表格导出, 风控与反爬机制

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xiaohongshu-expert)

---

## [15. PUA Debugging (English)](https://clawhub.ai/tanweai/pua-debugging-en)

**Slug**: `pua-debugging-en`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Forces exhaustive problem-solving using corporate PUA rhetoric and structured debugging methodology. MUST trigger when: (1) any task has failed 2+ times or y...

**中文介绍**: 这是一个在任务连续失败两次以上或出现卡壳迹象时强制触发的“穷尽式问题解决”提示体系，通过带有企业PUA式话术的施压与约束，推动用户/模型给出更完整、更可执行的排查与收敛过程。能力边界在于它主要改变表达与推理流程（结构化调试、逐步验证、强制复盘），并不直接提供领域知识或替代真实环境的观测与实验。典型场景是代码/配置/流程类问题反复失败、定位不清、需要系统化缩小范围与验证假设时使用。关键技术形态是“触发条件 + 固定调试框架”的提示工程组合（以企业管理话术作为约束层，叠加结构化故障排查模板）。

**关键词**: 结构化调试, 问题分解, 根因分析, 故障复盘, 失败重试策略, 触发式工作流, 提示词模板, 企业PUA话术, 强约束提示

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pua-debugging-en)

---

## [16. PUA Debugging](https://clawhub.ai/tanweai/pua-debugging)

**Slug**: `pua-debugging`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Forces exhaustive problem-solving using corporate PUA rhetoric and structured debugging methodology. MUST trigger when: (1) any task has failed 2+ times or y...

**中文介绍**: 这是一个在任务失败两次及以上等触发条件下启用的“强制穷举式”问题求解与排障辅助机制，通过企业式PUA话术驱动高压复盘，并以结构化调试方法把问题拆解、定位、验证与回归。它的能力边界在于主要提供流程化分析框架与表达风格的引导，不保证直接产出正确答案或替代实际执行与验证。典型场景是连续迭代仍未解决的Bug排查、需求/方案反复返工、交付风险收敛等需要强制收敛过程的任务。关键技术形态是基于规则/触发器的模式切换（按失败次数等条件启用）+ 固定调试步骤模板化推理 + 特定语气与措辞风格的生成控制。

**关键词**: 调试工作流, 结构化问题解决, 根因分析, 穷尽式排查, 失败重试策略, 故障复盘, 触发式规则, 企业话术模板

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pua-debugging)

---

## [17. Amazon Listing Factory](https://clawhub.ai/lenger666/amazon-listing-factory)

**Slug**: `amazon-listing-factory`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Generate Amazon listing drafts with title, bullet points, image plan, image prompts, and video script; supports auto image creation if configured.

**中文介绍**: 该能力用于自动生成亚马逊商品上架文案草稿，包括标题、要点、图片规划与提示词以及视频脚本，并在完成相应配置后可联动自动生成商品图片。典型场景是卖家或运营在新品上架、批量上新或A/B测试素材时快速产出结构化内容与创意素材方案。能力边界在于输出为营销草案与创意指令，仍需结合真实产品参数、合规要求与品牌口径进行人工校验与发布，且图片自动生成依赖外部模型/配置可用性。关键技术形态为基于大模型的结构化生成（listing字段、镜头脚本）+图像生成提示词编排与可选的自动制图流水线联动。

**关键词**: 亚马逊商品上架, 商品标题生成, 卖点要点生成, 商品图片策划, 图像提示词生成, 视频脚本生成, 自动图像生成, 技能插件集成

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/amazon-listing-factory)

---

## [18. Media.io AI Image & Video Generation API](https://clawhub.ai/wondershare-boop/mediaio-aigc-generate)

**Slug**: `mediaio-aigc-generate`  
**Version**: 1.0.13  
**Stats**: ⭐ 1 | ⬇️ 72 | 🧩 13

**原始简介**: Generate and edit AI images and videos with Media.io OpenAPI. Supports text-to-image, image-to-image, text-to-video, and image-to-video, plus task status and...

**中文介绍**: Media.io OpenAPI 提供 AI 图像与视频的生成和编辑能力，覆盖文生图、图生图、文生视频、图生视频，并支持异步任务创建与状态查询等流程管理。典型场景包括营销素材与短视频批量生产、内容二次创作与风格化、基于参考图的改图与扩展等。能力边界在于以生成式媒体处理为主，不涉及业务内容审核、版权合规判定或端到端发布分发等外部系统能力，且当前版本无功能变更。

**关键词**: 图像生成 API, 视频生成 API, 图像编辑 API, 视频编辑 API, 文生图, 图生图, 文生视频, 图生视频, 异步任务状态查询

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mediaio-aigc-generate)

---

## [19. Search Viewer](https://clawhub.ai/adminlove520/search-viewer)

**Slug**: `search-viewer`  
**Version**: 4.3.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 整合Fofa、Hunter、Shodan等空间测绘平台API，辅助渗透测试信息收集和资产发现的工具。

**中文介绍**: 该工具整合 Fofa、Hunter、Shodan、360 Quake、Zoomeye 等空间测绘平台的 API，用于在渗透测试前期辅助信息收集与资产发现，覆盖资产检索、端口/服务枚举、子域名收集与指纹识别等需求。能力边界在于结果质量与覆盖范围依赖第三方平台的数据与配额，且仅提供查询聚合与展示，不替代主动扫描、漏洞验证等攻击性能力。典型场景是对目标组织互联网暴露面进行快速盘点、基于指纹与服务分布筛选高优先级目标以及持续资产监测。关键技术形态为多源 API 聚合与统一查询/结果规范化的 CLI 工具，结合指纹特征匹配与合规约束提示实现可控使用。

**关键词**: 空间测绘API聚合, 网络资产测绘, 渗透测试信息收集, 端口与服务枚举, 子域名收集, 指纹识别, 命令行工具, API密钥管理, 查询语法

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/search-viewer)

---

## [20. AI Viral Trend Hijacker — Detect Any Trend & Produce Content Before It Peaks](https://clawhub.ai/g4dr/ai-viral-trend-hijacker)

**Slug**: `ai-viral-trend-hijacker`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Detect real-time viral trends across TikTok, Instagram, Reddit, YouTube, and Google, score and map them to your niche, then generate scripts and produce read...

**中文介绍**: 该工具可在 TikTok、Instagram、YouTube Shorts、Reddit 与 Google Trends 上实时捕捉新兴病毒趋势，并按动量、持续性、细分相关度与竞争度评分后映射到你的垂直领域，帮助优先挑选高潜机会。典型场景是为短视频账号做选题与增长：自动产出多种内容角度、撰写带爆款钩子的完整脚本，并联动 InVideo AI 生成按平台风格优化的成片。能力边界在于依赖外部平台数据与生成式内容，趋势判断与成片质量仍受数据噪声、平台规则和素材版权等约束，需要人工复核。关键技术形态包括多源趋势监测与评分模型、垂直化选题映射、LLM 脚本生成，以及视频自动化生成与 7 天游程排期推荐。

**关键词**: 实时趋势监测, 病毒趋势挖掘, 社媒数据聚合, 趋势评分模型, 细分领域匹配, 内容角度生成, 短视频脚本生成, 病毒钩子写作, 自动视频生成, 跨平台分发, 发帖日程编排

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-viral-trend-hijacker)

---

## [21. Provider Sync](https://clawhub.ai/C-Joey/provider-sync)

**Slug**: `provider-sync`  
**Version**: 2.0.3  
**Stats**: ⭐ 1 | ⬇️ 190 | 🧩 13

**原始简介**: Review and sync one provider's models and related fields into a local OpenClaw config file. Usage: /provider_sync [provider=<id>] [mode=dry-run|check-only|ap...

**中文介绍**: 该功能用于将某个模型提供方的模型列表及相关字段审阅并同步到本地 OpenClaw 配置文件中，支持以 dry-run、check-only 等模式在不落盘或仅校验的情况下预览差异并控制同步范围。能力边界在于它只处理配置层的模型与字段映射/更新，不负责模型实际调用、线上可用性验证或运行时路由策略。典型场景是定期对齐第三方提供方的模型变更、在发布前做变更检查、或在受限交互环境下通过命令行参数（如 inline 按钮不可用时的 fallback 用法）完成同步。关键技术形态是基于 provider 标识拉取/比对元数据并生成对本地配置文件的增量变更。

**关键词**: 配置同步, 模型清单同步, 本地配置文件, 差异检测, 干运行, 自动化更新, 命令行工具, Provider

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/provider-sync)

---

## [22. tke-skill](https://clawhub.ai/archerlliu/tke-skill)

**Slug**: `tke-skill`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 腾讯云 TKE 容器服务运维专家，支持集群巡检、状态查询、节点池管理、kubeconfig 获取等

**中文介绍**: 该能力面向腾讯云 TKE 集群的日常运维与诊断，主要覆盖集群巡检、健康/状态查询、节点池管理以及 kubeconfig 获取等操作，输出侧重以表格呈现关键信息。能力边界在于以查询与规范化运维流程为主，写操作仅限于 endpoint 启用/禁用等少数命令，其他操作不会修改集群资源。关键技术形态为通过 CLI 工具封装 TKE 运维命令并对接云端鉴权，支持环境变量或命令行方式提供凭证。典型场景包括例行巡检排障、快速定位集群与节点池问题、获取访问凭据以及管理集群接入端点状态。

**关键词**: 命令行工具, 集群巡检, 健康状态查询, 节点池管理, 集群端点管理, 云凭证管理, 表格化输出, tke-skill

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tke-skill)

---

## [23. Clawhub Skill Release Gate](https://clawhub.ai/chinasilva/clawhub-skill-release-gate)

**Slug**: `clawhub-skill-release-gate`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Pre-release gate and publish workflow for ClawHub skills. Use when users ask to publish/update/sync a skill, troubleshoot why a published skill is not visibl...

**中文介绍**: 这是一个面向 ClawHub 技能发布/更新/同步的预发布门禁与发布工作流，用于在用户提交发布相关请求或排查“已发布但不可见”等问题时，自动完成扫描、审核与发布路径校验并输出发布结果与证据。它的能力边界在于只负责发布前的风险拦截与流程合规保证，不替代技能功能开发与平台侧的最终展示逻辑；当发现高风险、审核失败、安装冒烟测试失败或 CLI 与 npx 命令不一致时会直接阻断发布。关键技术形态包含自动化预发布扫描与审核检查、发布路径强制、CLI/npx 命令一致性（parity）验证，以及在每次尝试后生成审核结论、parity 证据与规范网页链接等可追溯输出。

**关键词**: 发布门禁, 预发布扫描, 内容审核, 发布工作流, 安装冒烟测试, 风险检测拦截, 发布合规校验, Clawhub

**评分**: 41

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawhub-skill-release-gate)

---

## [24. rollinggo-hotel](https://clawhub.ai/dreamtzlong/rollinggo-hotel)

**Slug**: `rollinggo-hotel`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use the RollingGo CLI to find hotels, narrow results with destination, date, tag, distance, star, and budget filters, inspect hotel tags, and fetch hotel pri...

**中文介绍**: 该能力通过 RollingGo CLI 提供酒店搜索与详情/价格查询，可按目的地与日期并结合标签、距离、星级、预算等条件逐步筛选，并支持查看与解释酒店标签及 CLI 输出，优先采用 JSON 结果以便自动化集成。典型场景是先检索候选酒店、再应用多维过滤、核对标签含义，最后拉取单店详情与报价用于比对或下游系统处理。能力边界在于它依赖 CLI 的数据与输出规则（含退出码）进行检索与解析，本身不负责数据源覆盖与一致性保证，且默认优先使用 npm/npx 分发，除非用户明确要求 Python（uv）版本。关键技术形态为命令行技能封装与工作流引导、结构化（JSON）输出约定，以及 Node/Python 分发形态的兼容性对齐校验。

**关键词**: 命令行工具, 酒店搜索, 目的地筛选, 日期筛选, 星级筛选, 预算筛选, 距离筛选, 标签检索, 酒店详情查询, 退出码规范

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rollinggo-hotel)

---

## [25. Giggle Generation Video](https://clawhub.ai/patches429/giggle-generation-video)

**Slug**: `giggle-generation-video`  
**Version**: 0.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 支持根据文字描述和参考图生成短视频，可自定义模型、时长、分辨率和画幅比例，适合文字转视频和图生视频需求。

**中文介绍**: 该能力支持根据文字描述与参考图生成短视频，可在指定范围内自定义所用生成模型、视频时长、分辨率与画幅比例，覆盖文字转视频与图生视频等典型创作场景。能力边界上需按交互流程强制选择模型并补全时长与比例等参数，结果输出以带完整签名与查询参数的视频链接形式返回。关键技术形态采用三阶段执行链路：任务提交、定时轮询获取结果与失败时的同步回退机制，并通过严格的命令行/执行方式与环境变量约束保障可控调用。

**关键词**: 文本生成视频, 图生视频, 短视频生成, 可配置生成模型, 视频生成参数控制, 时长控制, 分辨率控制, 画幅比例控制, 异步任务队列, 定时轮询（Cron）, CLI 工具链, 签名 URL 输出

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/giggle-generation-video)

---

