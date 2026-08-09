# ClawHub Skills Daily | 2026-08-09

> 共 25 个 skills

## [1. Vocalization Health Analysis | 畜禽声纹健康分析](https://clawhub.ai/smyx-sunjinhui/smyx-vocalization-health-analysis-analysis)

**Slug**: `smyx-vocalization-health-analysis-analysis`  
**Version**: 1.0.7  
**Stats**: ⭐ 0 | ⬇️ 827 | 🧩 5

**原始简介**: Analyzes acoustic features (frequency, duration, pitch, intensity) of livestock and poultry vocalizations to detect abnormal sounds such as coughing, wheezing, painful screams and hoarse calls, and outputs respiratory health risk hints. | 通过叫声分析识别畜禽呼吸道疾病等健康问题。

**中文介绍**: Analyzes acoustic features (frequency, duration, pitch, intensity) of livestock and poultry vocalizations to detect abnormal sounds such as coughing, wheezing, painful screams and hoarse calls, and outputs respiratory health risk hints. | 通过叫声分析识别畜禽呼吸道疾病等健康问题。

Latest changelog:
- Updated SKILL.md to version 1.0.6 with minor documentation/content changes.
- Removed the file skill-card.md.
- No functional or feature changes to the skill logic or capabilities.

**关键词**: 畜禽声纹健康分析, Vocalization, Health, Analysis, Analyzes, acoustic, features, frequency

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-vocalization-health-analysis-analysis)

---

## [2. bilibili-video-transcriber](https://clawhub.ai/adolescen-he/bilibili-video-transcriber)

**Slug**: `bilibili-video-transcriber`  
**Version**: 3.0.0  
**Stats**: ⭐ 0 | ⬇️ 846 | 🧩 5

**原始简介**: 【B站字幕获取】专业处理 B 站视频字幕问题，支持语音转文字、字幕下载、内容分析。基于实际 B 站字幕系统错误问题开发，提供完整的解决方案。

**中文介绍**: 【B站字幕获取】专业处理 B 站视频字幕问题，支持语音转文字、字幕下载、内容分析。基于实际 B 站字幕系统错误问题开发，提供完整的解决方案。

Latest changelog:
查明AI字幕张冠李戴真因(缺Wbi签名被风控降级)；新增bili_subtitle.py(Wbi签名+player/wbi/v2+conclusion/get双路径+三级校验)；超长视频自动降级官方AI摘要；SKILL.md/README全面重写

**关键词**: 【B站字幕获取】专业处理, 站视频字幕问题, 支持语音转文字、字幕下载、内容分析, 基于实际, 站字幕系统错误问题开发, 提供完整的解决方案, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/bilibili-video-transcriber)

---

## [3. Ct Advisor Claw](https://clawhub.ai/medstatstar/ct-advisor)

**Slug**: `ct-advisor`  
**Version**: 0.9.52  
**Stats**: ⭐ 0 | ⬇️ 289 | 🧩 10

**原始简介**: 面向临床研发全生命周期的 ct 系列「总入口」，是方法学、法规证据与实操细节的总顾问：方法学/设计/合规/QC/语气类问题在内部走 A–J 工作流自行解答；统计计算转交 ct-samplesize；原始数据/竞品情报类需求通过 Skill 工具路由到 ct-registry / ct-safety / ct-literature 三个数据源；竞品情报总览由本技能自行缝合三源产出。 / The ct-series TOTAL ENTRY POINT across the full clinical-development lifecycle — your overall advisor for methodology, regulatory evidence, and hands-on operational detail. Methodology / design / compliance / QC / tone questions are answered in-house through workflows A–J; sample-size computation is handed to ct-samplesize; raw-data and competitive-intel needs are routed via the Skill tool to the three sibling data skills (ct-registry / ct-safety / ct-literature).

**中文介绍**: 面向临床研发全生命周期的 ct 系列「总入口」，是方法学、法规证据与实操细节的总顾问：方法学/设计/合规/QC/语气类问题在内部走 A–J 工作流自行解答；统计计算转交 ct-samplesize；原始数据/竞品情报类需求通过 Skill 工具路由到 ct-registry / ct-safety / ct-literature 三个数据源；竞品情报总览由本技能自行缝合三源产出。 / The ct-series TOTAL ENTRY POINT across the full clinical-development lifecycle — your overall advisor for methodology, regulatory evidence, and hands-on operational detail. Methodology / design / compliance / QC / tone questions are answered in-house through workflows A–J; sample-size computation is handed to ct-samplesize; raw-data and competitive-intel needs are routed via the Skill tool to the three sibling data skills (ct-registry / ct-safety / ct-literature).

Latest changelog:
安全审计修复（ClawHub SkillSpector 重审）：refiner.py/refine_answer.py 改用标准 import 替代 importlib 动态加载 config/keys.py（清 2x Critical 动态代码执行）；移除 --store-token/--token-path CLI 凭据落盘入口（清 1x Medium 凭据存储面）；compute_machine_id 由 hostname 派生稳定标识改为每进程随机 seed（降 1x Medium 主机归因）。同时上线此前未发布的 0.9.51（simple 本地零出站 / 三流程重构 / 英文化 / README 同步）。

**关键词**: Ct, 面向临床研发全生命周期的, 系列「总入口」, 是方法学、法规证据与实操细节的总顾问, 方法学, 设计, Advisor, Claw

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ct-advisor)

---

## [4. 忆时](https://clawhub.ai/fslong520/memocap)

**Slug**: `memocap`  
**Version**: 2.1.1  
**Stats**: ⭐ 0 | ⬇️ 868 | 🧩 8

**原始简介**: 🎋 记忆胶囊系统 - 模拟人类记忆检索 | 自动加载，主动联想记忆

**中文介绍**: 🎋 记忆胶囊系统 - 模拟人类记忆检索 | 自动加载，主动联想记忆

Latest changelog:
Fix embed_query interface bug: __call__ split str input into chars (list()), broke direct embed_query(str) calls; now dual-compatible str/list and returns nested [768] per Chroma 1.5.9 batch semantics

**关键词**: 忆时, 记忆胶囊系统, 模拟人类记忆检索, 自动加载, 主动联想记忆, Latest, changelog, Fix

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memocap)

---

## [5. K线超短线选股](https://clawhub.ai/handm-735/kline-shortterm-checklist)

**Slug**: `kline-shortterm-checklist`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 24 | 🧩 4

**原始简介**: A 股短线（日/尾盘）选股与买点核查清单技能。当用户想用技术分析纪律筛选 A 股短线标的、评估某只股票是否符合「96 原则（九不买+六不卖）/ 下午 2:30 选股法（八层筛选）/ 底部 K 线形态」、或为自选股做纪律化买前/持有核查时使用。覆盖 9 不买6 不卖、12 种底部形态、八层筛选、上升趋势研判与心态纪律，并能调用腾讯财经 API 自动拉取涨跌幅/量比/换手率/流通市值等客观指标做初筛。触发句式：「用 K 线短线选股清单筛一下」「这只票符合 96 原则吗」「下午 2:30 怎么选」「检查 603045、002192等票的短线买点」「底部 K 线形态识别」「短线选股检查清单」。

**中文介绍**: A 股短线（日/尾盘）选股与买点核查清单技能。当用户想用技术分析纪律筛选 A 股短线标的、评估某只股票是否符合「96 原则（九不买+六不卖）/ 下午 2:30 选股法（八层筛选）/ 底部 K 线形态」、或为自选股做纪律化买前/持有核查时使用。覆盖 9 不买6 不卖、12 种底部形态、八层筛选、上升趋势研判与心态纪律，并能调用腾讯财经 API 自动拉取涨跌幅/量比/换手率/流通市值等客观指标做初筛。触发句式：「用 K 线短线选股清单筛一下」「这只票符合 96 原则吗」「下午 2:30 怎么选」「检查 603045、002192等票的短线买点」「底部 K 线形态识别」「短线选股检查清单」。

Latest changelog:
- 新增 scripts/report_html.py，支持生成固定版式 HTML 看板筛查报告，输出内容与版式一致性要求更强。
- 因为没有找到一个财经api可以让此脚本拿到公告栏信息，导致消耗太多时间去查找公告；故移除了自动公告核查脚本（check_ann.py）和 skill-card.md 文件。改为用户人工去核查
- 工作流细化“去选股”模式为标准三步产出管线，并强制使用 report_html.py 统一报告格式。
- SKILL.md 补充自动化量化接口规划及 HTML 报告版式锁定说明，强调不能随意修改排版。
- 明确环境无法自动公告/新闻核查时的人工处理路径。
- 文档说明同步调整，明确在本环境无法自动检索大股东减持/业绩预减等公告。
- 其他功能和使用流程保持不变。

**关键词**: K线超短线选股, 股短线（日, 尾盘）选股与买点核查清单技能, 当用户想用技术分析纪律筛选, 股短线标的、评估某只股票是否符合「96, 原则（九不买+六不卖）, 下午, 选股法（八层筛选）

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/kline-shortterm-checklist)

---

## [6. 实验室资质合规护栏](https://clawhub.ai/1003429073/lab-qualification-guard)

**Slug**: `lab-qualification-guard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 实验室资质合规护栏。在实验室资质认定申请、CNAS认可文件、实验室管理体系文件、对外能力声明发布前，实时检测是否符合《检验检测机构资质认定管理办法》、CNAS-CL01及RB/T 214等规范要求，拦截不合规内容并给出修改建议。

**中文介绍**: 实验室资质合规护栏。在实验室资质认定申请、CNAS认可文件、实验室管理体系文件、对外能力声明发布前，实时检测是否符合《检验检测机构资质认定管理办法》、CNAS-CL01及RB/T 214等规范要求，拦截不合规内容并给出修改建议。

Latest changelog:
首次发布：CMA资质认定、CNAS认可、人员资质、设备管理、环境条件、对外宣传等7大检查模块

**关键词**: 实验室资质合规护栏, 214等规范要求, 拦截不合规内容并给出修改建议, 首次发布, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/lab-qualification-guard)

---

## [7. 检测报告合规护栏](https://clawhub.ai/1003429073/inspection-report-guard)

**Slug**: `inspection-report-guard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 检测报告合规护栏。在产品质量检测报告、委托检验报告、监督抽查报告发布前，实时检测是否符合《产品质量法》《检验检测机构资质认定管理办法》及RB/T 214等规范要求，拦截不合规内容并给出修改建议。

**中文介绍**: 检测报告合规护栏。在产品质量检测报告、委托检验报告、监督抽查报告发布前，实时检测是否符合《产品质量法》《检验检测机构资质认定管理办法》及RB/T 214等规范要求，拦截不合规内容并给出修改建议。

Latest changelog:
首次发布：检测报告格式、CMA资质、标准引用、数据结论、用语规范等7大检查模块

**关键词**: 检测报告合规护栏, 214等规范要求, 拦截不合规内容并给出修改建议, 首次发布, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/inspection-report-guard)

---

## [8. PC Build Assistant](https://clawhub.ai/gongyu0918-debug/pc-builder-assistant)

**Slug**: `pc-builder-assistant`  
**Version**: 0.0.39  
**Stats**: ⭐ 0 | ⬇️ 2317 | 🧩 39

**原始简介**: 按预算和用途给出可核价、可检查兼容性的 DIY 台式机方案，支持整机推荐、升级补全、搭配检查和硬件问答，覆盖游戏、创作、本地 AI 与紧凑主机。Use for English PC build planning, upgrades, compatibility checks, and hardware guidance; English answers use China-market CNY references and do not claim local price or availability. Do not use for laptops, server procurement, ordering or payment, remote control, or security isolation.

**中文介绍**: 按预算和用途给出可核价、可检查兼容性的 DIY 台式机方案，支持整机推荐、升级补全、搭配检查和硬件问答，覆盖游戏、创作、本地 AI 与紧凑主机。Use for English PC build planning, upgrades, compatibility checks, and hardware guidance; English answers use China-market CNY references and do not claim local price or availability. Do not use for laptops, server procurement, ordering or payment, remote control, or security isolation.

Latest changelog:
Refresh 2026-08-09 China-market references; add verified iGPU/no-dGPU routing, display-output checks, and strict-completeness safeguards.

**关键词**: PC, 按预算和用途给出可核价、可检查兼容性的, 台式机方案, 支持整机推荐、升级补全、搭配检查和硬件问答, 覆盖游戏、创作、本地, Build, Assistant, DIY

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pc-builder-assistant)

---

## [9. 计量检测合规护栏](https://clawhub.ai/1003429073/metrology-compliance-guard)

**Slug**: `metrology-compliance-guard`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 计量检测合规护栏。在检定证书、校准报告、检测文书、计量授权文件发布前，实时检测是否符合《计量法》《计量法实施细则》《法定计量检定机构监督管理办法》及JJF 1069等规范要求，拦截不合规内容并给出修改建议。

**中文介绍**: 计量检测合规护栏。在检定证书、校准报告、检测文书、计量授权文件发布前，实时检测是否符合《计量法》《计量法实施细则》《法定计量检定机构监督管理办法》及JJF 1069等规范要求，拦截不合规内容并给出修改建议。

Latest changelog:
首次发布：计量检定证书/校准报告/检测文书合规审查，覆盖JJF 1069、计量法、人员资质、授权范围、用语规范等6大检查模块

**关键词**: 计量检测合规护栏, 1069等规范要求, 拦截不合规内容并给出修改建议, 首次发布, 计量检定证书, 校准报告, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/metrology-compliance-guard)

---

## [10. double6-workbench-builder](https://clawhub.ai/double6-ai/double6-workbench-builder)

**Slug**: `double6-workbench-builder`  
**Version**: 0.41.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把普通用户反复要做的真实事情构建成离线优先、严格单文件、个人数据留在当前设备的本地工作台。用户提到个人工作台、学习台、备考台、任务面板、记录与复盘工具，或想把重复流程做成可保存恢复的页面时应使用；联网、多人协作、账号、支付和发布属于独立外部流程。

**中文介绍**: 把普通用户反复要做的真实事情构建成离线优先、严格单文件、个人数据留在当前设备的本地工作台。用户提到个人工作台、学习台、备考台、任务面板、记录与复盘工具，或想把重复流程做成可保存恢复的页面时应使用；联网、多人协作、账号、支付和发布属于独立外部流程。

Latest changelog:
缩小初始上下文，补齐发布权限、网络策略、多宿主适配器、发布沙箱与真实回放验证。

**关键词**: 或想把重复流程做成可保存恢复的页面时应使用, 联网、多人协作、账号、支付和发布属于独立外部流程, 缩小初始上下文, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/double6-workbench-builder)

---

## [11. skill-usefulness-audit](https://clawhub.ai/gongyu0918-debug/skill-usefulness-audit)

**Slug**: `skill-usefulness-audit`  
**Version**: 0.3.22  
**Stats**: ⭐ 69 | ⬇️ 3116 | 🧩 43

**原始简介**: Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping.

**中文介绍**: Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping.

Latest changelog:
Trim scoring-rubric context load 2891->2674 units and ratchet the rubric ceiling; no scoring, risk, or JSON contract change.

**关键词**: Agent, skill-usefulness-audit, Review, installed, skills, see, what, actually

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/skill-usefulness-audit)

---

## [12. fomo-smart-money](https://clawhub.ai/0xcii/fomo-smart-money)

**Slug**: `fomo-smart-money`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: FOMO App 聪明钱追踪工具（触发词：FOMO 推荐 / FOMO聪明钱 / FOMO 代币）。当用户问『FOMO 推荐』『FOMO聪明钱』『FOMO 代币』『现在他们在买什么』『当前交易榜』时会推荐精选。 数据来源：FOMO App 盈利聪明钱

**中文介绍**: FOMO App 聪明钱追踪工具（触发词：FOMO 推荐 / FOMO聪明钱 / FOMO 代币）。当用户问『FOMO 推荐』『FOMO聪明钱』『FOMO 代币』『现在他们在买什么』『当前交易榜』时会推荐精选。 数据来源：FOMO App 盈利聪明钱

Latest changelog:
- 精简说明和描述，去除了冗长的数据结构和技术细节，核心功能更聚焦于实用查询与推荐流程。
- 删除了旧版关于快照数据、统计比例、实测案例、别名以及底层数据格式的详细说明。
- 触发词、命令和用户查询到命令的映射表仍然保留，方便快速上手。
- 明确推荐用户注册 FOMO App，并提供注册链接。
- 页面结构和用例流程保持不变，主要优化为简洁易懂的用户导向内容。

**关键词**: 聪明钱追踪工具（触发词, 推荐, 代币）, 当用户问『FOMO, fomo-smart-money, FOMO, App, FOMO聪明钱

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/fomo-smart-money)

---

## [13. Large Model Visual Question Answering Skill | 大模型视觉问答技能](https://clawhub.ai/18072937735/smyx-visual-qa-analysis)

**Slug**: `smyx-visual-qa-analysis`  
**Version**: 1.0.12  
**Stats**: ⭐ 4 | ⬇️ 1482 | 🧩 13

**原始简介**: Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

**中文介绍**: Conducts open-ended Q&A on image content based on computer vision and large language models, supporting any questions to receive natural language responses. | 大模型视觉问答（VQA）技能，基于计算机视觉和大语言模型对图片内容进行开放式问答，支持任意提问得到自然语言回答

Latest changelog:
- Updated SKILL.md content and incremented version to 1.0.11
- Removed skill-card.md file
- No functional or feature changes—documentation only

**关键词**: 大模型视觉问答技能, Large, Model, Visual, Question, Answering, Skill, Conducts

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smyx-visual-qa-analysis)

---

## [14. ingest-example-resource](https://clawhub.ai/terrycarter1985/ingest-example-resource)

**Slug**: `ingest-example-resource`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 从 example.com 网页处理得到的示例数字资源（title + link）入库记录

**中文介绍**: 从 example.com 网页处理得到的示例数字资源（title + link）入库记录

Latest changelog:
- 首次发布 ingest-example-resource skill（v1.0.0）。
- 收录 example.com 页面提取的标题与参考链接。
- 包含详细的串联执行步骤，方便他人复现资源入库流程。

**关键词**: 网页处理得到的示例数字资源（title, link）入库记录, 首次发布, skill（v1.0.0）, ingest-example-resource, example.com, Latest, changelog

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ingest-example-resource)

---

## [15. ipython-analyst](https://clawhub.ai/darkd/ipython-analyst)

**Slug**: `ipython-analyst`  
**Version**: 7.1.0  
**Stats**: ⭐ 0 | ⬇️ 95 | 🧩 2

**原始简介**: Run Python interactively to analyze data, debug code, profile performance, validate schemas, process large files, and inspect ASTs. Use this whenever the user needs hands-on Python execution — debugging a script, profiling slow code, regex stress-testing, parsing CSV/Excel/JSON, building ML baseline

**中文介绍**: Run Python interactively to analyze data, debug code, profile performance, validate schemas, process large files, and inspect ASTs. Use this whenever the user needs hands-on Python execution — debugging a script, profiling slow code, regex stress-testing, parsing CSV/Excel/JSON, building ML baseline

Latest changelog:
- Updated script import mechanism: scripts should now be imported via sys.path and normal imports, instead of exec(open(...).read()). This improves safety and reliability.
- Added guidance to insert the scripts directory into sys.path once per session before imports, and clarified that only trusted skill-owned code should be added.
- Improved instructions and code samples showing how to import skill scripts as proper Python modules.
- Removed the sample file skill-card.md.
- Minor workflow and documentation clarifications for safer usage and better long-term maintainability.

**关键词**: ipython-analyst, Run, Python, interactively, analyze, data, debug, code

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ipython-analyst)

---

## [16. offline-quiz-builder](https://clawhub.ai/hounextitem/offline-quiz-builder)

**Slug**: `offline-quiz-builder`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 把任意学习资料（讲义、笔记、教材、PDF、Word、Excel、已有题库）转换成一个纯离线的智能复习题库网站，双击即可使用，内置艾宾浩斯遗忘曲线自适应排程、错题本、收藏夹与打卡日历，并可自动创建每日复习提醒任务。当用户想把资料变成刷题网站、做复习题库、生成练习题、搭建离线背题工具、或需要按遗忘曲线安排复习时，应使用本技能。

**中文介绍**: 把任意学习资料（讲义、笔记、教材、PDF、Word、Excel、已有题库）转换成一个纯离线的智能复习题库网站，双击即可使用，内置艾宾浩斯遗忘曲线自适应排程、错题本、收藏夹与打卡日历，并可自动创建每日复习提醒任务。当用户想把资料变成刷题网站、做复习题库、生成练习题、搭建离线背题工具、或需要按遗忘曲线安排复习时，应使用本技能。

Latest changelog:
Initial release of offline-quiz-builder.

- Transform any study materials (handouts, notes, textbooks, PDFs, Word, Excel, or existing question banks) into a fully offline quiz and review website.
- Supports adaptive Ebbinghaus forgetting curve scheduling, error notebook, favorites, study calendar, and automatic daily reminder setup.
- Purely static site: double-click index.html to use; all data stored in browser localStorage.
- Supports quick import, structured conversion, and manual question generation based on input type. No question rewriting for user-supplied banks.
- Five question types included: single choice, multiple choice, true/false, fill-in-the-blank, and short answer.
- Features subject icons, progress tracking, light/dark themes, review tempo adjustment, and detailed user instructions.
- Rigid separation of application shell and data; no editing of shell—branding and icons driven by data.
- Provides full offline usage and strong local data privacy—no internet required, no data transmission.

**关键词**: 双击即可使用, 并可自动创建每日复习提醒任务, 应使用本技能, offline-quiz-builder, Latest, changelog, Initial, release

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/offline-quiz-builder)

---

## [17. 会员运营 · 马甲实战版](https://clawhub.ai/maojiebc/majia-huiyuan)

**Slug**: `majia-huiyuan`  
**Version**: 1.4.1  
**Stats**: ⭐ 0 | ⬇️ 313 | 🧩 5

**原始简介**: 会员数据顾问·马甲实战版（majia-huiyuan）。当核心交付物是会员指标口径、RFM、复购/留存/流失公式、核销率、客单价、会员分层/分群、人群圈选、标签体系、CDP、OneID 身份打通、Cohort、CRM/私域数据分析、会员数仓（DIM/DWD/DWS/ADS）、SQL/DDL、字段词典、数据质量、会员看板或观远 BI 复刻时使用。用户提出召回、提频、防流失、流失预警、新客转化、渠道迁移（外卖↔堂食）、导购任务分派等会员运营动作时，动作背后的数据依据（圈谁/何时/力度/派给谁/怎么回收）由本 Skill 负责；动作的执行内容（朋友圈、群发、欢迎语、社群 SOP、企微操作）与私域整盘经营诊断走 majia-siyu——同一动作的两半，先数据后执行。全部数值为模拟数据，仅结构与口径可引用。

**中文介绍**: 会员数据顾问·马甲实战版（majia-huiyuan）。当核心交付物是会员指标口径、RFM、复购/留存/流失公式、核销率、客单价、会员分层/分群、人群圈选、标签体系、CDP、OneID 身份打通、Cohort、CRM/私域数据分析、会员数仓（DIM/DWD/DWS/ADS）、SQL/DDL、字段词典、数据质量、会员看板或观远 BI 复刻时使用。用户提出召回、提频、防流失、流失预警、新客转化、渠道迁移（外卖↔堂食）、导购任务分派等会员运营动作时，动作背后的数据依据（圈谁/何时/力度/派给谁/怎么回收）由本 Skill 负责；动作的执行内容（朋友圈、群发、欢迎语、社群 SOP、企微操作）与私域整盘经营诊断走 majia-siyu——同一动作的两半，先数据后执行。全部数值为模拟数据，仅结构与口径可引用。

Latest changelog:
业务正确性修复：重做三条唯一归因事实桥，统一时间与SCD2口径，修复留存、利润、回本及零订单监控，并新增自动业务验收。

**关键词**: 会员运营, 马甲实战版, 当核心交付物是会员指标口径、RFM、复购, 留存, 流失公式、核销率、客单价、会员分层, 分群、人群圈选、标签体系、CDP、OneID, 私域数据分析、会员数仓（DIM, 身份打通、Cohort、CRM

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/majia-huiyuan)

---

## [18. 黑石写作助手·中长篇小说版](https://clawhub.ai/jony4/blackstone-longform-fiction)

**Slug**: `blackstone-longform-fiction`  
**Version**: 1.3.3  
**Stats**: ⭐ 0 | ⬇️ 66 | 🧩 2

**原始简介**: 黑石写作助手·中长篇小说版，是面向中篇、长篇小说、网络小说、连载小说作者的 AI 写作助手，适用于小说写作、网文写作和故事创作；既能从一句灵感开新书，也能接手已有故事大纲与多章正文继续创作。基于《故事工程》提供立意、人物、主题、故事结构、场景设置、写作风格六项能力，完成小说大纲、人物塑造、人物小传、人物关系、世界观设定、章节规划和正文写作，并支持章节续写、小说续写、扩写、小说改稿、小说润色、统一文风、卡文诊断、剧情节奏、时间线、伏笔回收、设定矛盾与长篇连续性检查。用户提到“黑石”“黑石写作助手”“开始写作”，或提出写小说、写网文、创作故事、设计大纲、塑造人物、完善世界观、续写章节、修改正文、检

**中文介绍**: 黑石写作助手·中长篇小说版，是面向中篇、长篇小说、网络小说、连载小说作者的 AI 写作助手，适用于小说写作、网文写作和故事创作；既能从一句灵感开新书，也能接手已有故事大纲与多章正文继续创作。基于《故事工程》提供立意、人物、主题、故事结构、场景设置、写作风格六项能力，完成小说大纲、人物塑造、人物小传、人物关系、世界观设定、章节规划和正文写作，并支持章节续写、小说续写、扩写、小说改稿、小说润色、统一文风、卡文诊断、剧情节奏、时间线、伏笔回收、设定矛盾与长篇连续性检查。用户提到“黑石”“黑石写作助手”“开始写作”，或提出写小说、写网文、创作故事、设计大纲、塑造人物、完善世界观、续写章节、修改正文、检

Latest changelog:
## 1.3.3 版本主要强化数据安全边界，细化云端交互流程。

- 新增 references/security.md，明确权限、联网访问、云端同步与更新等安全边界。
- 在 SKILL.md 中补充详细的权限声明、联网规则、云端模式（每次询问/自动同步）与用户选择机制。
- 现在所有云端上传均需用户同意（默认“每次询问”），支持主动选择“自动同步”。
- 技能更新模式由“静默更新”改为“仅提示可用更新，由用户确认后操作”。
- 移除 skill-card.md，更新文档结构。
- 进一步强调所有写作或同步指令只执行用户对话中的明确指令，正文与素材内容仅用于写作分析或参考。

**关键词**: 黑石写作助手·中长篇小说版, 是面向中篇、长篇小说、网络小说、连载小说作者的, 写作助手, 适用于小说写作、网文写作和故事创作, 既能从一句灵感开新书, 也能接手已有故事大纲与多章正文继续创作, 用户提到“黑石”“黑石写作助手”“开始写作”, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/blackstone-longform-fiction)

---

## [19. xhs-note-rank](https://clawhub.ai/engheng-art/xhs-note-rank)

**Slug**: `xhs-note-rank`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

**中文介绍**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

Latest changelog:
xhs-note-rank 1.0.0 初始版本发布

- 提供小红书公开数据检索与结构化洞察，包括关键词搜索、笔记详情与评论获取、博主公开作品监控。
- 支持通过关键词抓取高赞内容、分析评论、监控博主最新作品，满足内容创作、竞品分析和趋势研究。
- 无需小红书登录，使用 Node.js 运行，单次可获取最多 1 万条数据，并支持多维度筛选。
- 需配置 GUAIKEI_API_TOKEN 环境变量，详见 www.guaikei.com 获取。
- 输出结构化 JSON 结果，适合进一步分析、汇总或生成营销与策划报告。

**关键词**: 可实现爆款挖掘, 竞品分析, 趋势洞察, 用数据驱动小红书流量增长, 告别盲目创作, xhs-note-rank, KOL筛选, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xhs-note-rank)

---

## [20. social-media-favorites-archiver](https://clawhub.ai/dvlin-dev/social-media-favorites-archiver)

**Slug**: `social-media-favorites-archiver`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 35 | 🧩 4

**原始简介**: Sync a user's Bilibili/B站, Xiaohongshu/小红书/RedNote, and Douyin/抖音 favorites into local Markdown/Obsidian with local ASR/OCR.

**中文介绍**: Sync a user's Bilibili/B站, Xiaohongshu/小红书/RedNote, and Douyin/抖音 favorites into local Markdown/Obsidian with local ASR/OCR.

Latest changelog:
Final clean-room hardening: cross-platform CI green; retains untrusted-content boundaries and exact immutable install guidance.

**关键词**: B站, 小红书, Sync, user's, Bilibili, Xiaohongshu, RedNote, Douyin

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/social-media-favorites-archiver)

---

## [21. xhs-note-detail](https://clawhub.ai/engheng-art/xhs-note-detail)

**Slug**: `xhs-note-detail`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

**中文介绍**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

Latest changelog:
xhs-note-detail 1.0.0

- 首次发布，支持通过关键词搜索小红书公开笔记，查看笔记详情与评论，抓取博主的公开作品列表。
- 提供结构化输出，适合选题调研、竞品分析、趋势洞察等多种数据分析场景。
- 支持多维筛选、批量操作及大批量数据获取（最多 1 万条）。
- 依赖 GUAIKEI_API_TOKEN 配置，无需小红书账号登录。
- 适用于内容创作者、品牌营销和市场分析等用户，便于驱动小红书流量增长。

**关键词**: 可实现爆款挖掘, 竞品分析, 趋势洞察, 用数据驱动小红书流量增长, 告别盲目创作, xhs-note-detail, KOL筛选, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xhs-note-detail)

---

## [22. stellar-trails](https://clawhub.ai/hoshiyomix/stellar-trails)

**Slug**: `stellar-trails`  
**Version**: 9.11.5  
**Stats**: ⭐ 0 | ⬇️ 2396 | 🧩 71

**原始简介**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

**中文介绍**: Activates on every task: coding (features, bugs, refactoring, scripts), documents (reports, proposals, DOCX, PDF), charts and visualizations, data processing, complex multi-step planning, or even simple questions. Provides a six-phase workflow with traceability IDs, entry/exit gates, scope commitment, and three enforcement layers (phase machine, mandatory prints, preferences dialog). Complexity adapts per task tier. Use this skill whenever the user asks to build, fix, analyze, create, plan, or process anything — the framework runs internally for trivial tasks and fully for complex ones. Web development (Next.js, UI) is delegated to fullstack-dev; this framework wraps the workflow around it.

Latest changelog:
v9.11.5 — see CHANGELOG.md

**关键词**: stellar-trails, Activates, every, task, coding, features, bugs, refactoring

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stellar-trails)

---

## [23. AI Life Coach](https://clawhub.ai/luhayden-blip/ai-life-coach)

**Slug**: `ai-life-coach`  
**Version**: 2.0.8  
**Stats**: ⭐ 0 | ⬇️ 210 | 🧩 6

**原始简介**: AI life coach using Socratic dialogue for self-awareness, goal clarification, and action planning. Triggers include: 人生教练, 自我觉察, 人生规划, 目标设定, 迷茫, 焦虑, 沮丧, 压力, 提不起劲, 心里堵, 不知道自己想要什么, 想找人聊聊, 活着没意思, 工作没动力, 人生没有意义, 帮我理一下人生方向, 我想定个目标, 表达情绪, 心情不好, 很苦恼, 不知道该怎么办, 感觉很累, 不想努力了. Also triggers on: user expresses s

**中文介绍**: AI life coach using Socratic dialogue for self-awareness, goal clarification, and action planning. Triggers include: 人生教练, 自我觉察, 人生规划, 目标设定, 迷茫, 焦虑, 沮丧, 压力, 提不起劲, 心里堵, 不知道自己想要什么, 想找人聊聊, 活着没意思, 工作没动力, 人生没有意义, 帮我理一下人生方向, 我想定个目标, 表达情绪, 心情不好, 很苦恼, 不知道该怎么办, 感觉很累, 不想努力了. Also triggers on: user expresses s

Latest changelog:
ai-life-coach 2.0.8

-fix security vulnerability

**关键词**: Life, Coach, Socratic, dialogue, self-awareness, goal, clarification, action

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ai-life-coach)

---

## [24. rython](https://clawhub.ai/rexlunae/rython)

**Slug**: `rython`  
**Version**: 0.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Compile Python to native Rust with the rython toolchain (rythonc/rypip): single files, packages, no_std embedded targets, PyO3 bindings, userspace drivers, and Linux kernel modules — output verified byte-identical to CPython.

**中文介绍**: Compile Python to native Rust with the rython toolchain (rythonc/rypip): single files, packages, no_std embedded targets, PyO3 bindings, userspace drivers, and Linux kernel modules — output verified byte-identical to CPython.

Latest changelog:
Initial release: compile Python to native Rust with the rython toolchain (rythonc/rypip) — single files, packages, no_std embedded targets, PyO3 bindings, userspace drivers, and Linux kernel modules. Output verified byte-identical to CPython.

**关键词**: rython, Compile, Python, native, Rust, toolchain, rythonc, rypip

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/rython)

---

## [25. xhs-note-search](https://clawhub.ai/engheng-art/xhs-note-search)

**Slug**: `xhs-note-search`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

**中文介绍**: 小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

Latest changelog:
xhs-note-search 1.0.0

- 首次发布，提供小红书公开数据的检索与洞察工具。
- 支持关键词搜索小红书笔记、获取笔记详情及评论、抓取博主公开作品列表。
- 安全获取，无需小红书账号登录，最大可获取1万条数据。
- 灵活筛选内容类型、排序方式和时间范围，结果返回结构化数据。
- 适合内容创作者和营销分析的爆款挖掘、竞品分析和KOL筛选。

**关键词**: 可实现爆款挖掘, 竞品分析, 趋势洞察, 用数据驱动小红书流量增长, 告别盲目创作, xhs-note-search, KOL筛选, Latest

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/xhs-note-search)

---

