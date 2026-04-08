# GitHub Trending 日榜 | 2026-04-08

> 共 10 个项目

## 📑 目录

- [C++](#Cplusplus) (1 个项目)
- [Go](#Go) (1 个项目)
- [Kotlin](#Kotlin) (1 个项目)
- [Python](#Python) (5 个项目)
- [Shell](#Shell) (1 个项目)
- [Unknown](#Unknown) (1 个项目)

---

## C++

## [1. google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)

**语言**: C++  
**Stars**: ⭐ 0 (+500 today) | **Forks**: 🔱 264

**原始描述**: 

**中文介绍（README总结）**: LiteRT-LM 是谷歌推出的面向边缘设备部署大语言模型的开源高性能推理框架，强调可用于生产环境并支持跨平台。它支持 GPU/NPU 硬件加速、多模态（视觉与音频）输入以及函数调用等工具使用能力，并兼容 Gemma、Llama、Phi-4、Qwen 等多种模型。资料提到已支持 Gemma 4 并提供 CLI，可在 Linux、macOS、Windows（WSL）与树莓派上体验，同时也用于 Chrome、Chromebook Plus、Pixel Watch 等设备上的端侧 GenAI。

**关键词**: 边缘端 LLM 推理, 端侧部署, 跨平台运行, 多模态推理, 视觉输入, 音频输入, 命令行工具, google-ai-edge

**评分**: 86

**项目地址**: [GitHub](https://github.com/google-ai-edge/LiteRT-LM)

---

## Go

## [2. goharbor/harbor](https://github.com/goharbor/harbor)

**语言**: Go  
**Stars**: ⭐ 0 (+23 today) | **Forks**: 🔱 5.2k

**原始描述**: An open source trusted cloud native registry project that stores, signs, and scans content.

**中文介绍（README总结）**: Harbor 是一个开源的云原生可信镜像仓库项目，可用于存储、签名并扫描内容，并在开源 Docker Distribution 基础上增强了安全、身份与管理等能力。它支持容器镜像与 Helm charts，提供基于项目的角色访问控制，以及按策略在多个仓库间复制同步镜像与制品。Harbor 由 CNCF 托管，并通过双周社区会议进行协作；开发分支可能不稳定，通常建议使用正式发布版本获取稳定二进制。

**关键词**: 云原生镜像仓库, 容器镜像分发, 内容签名, 漏洞扫描, 基于策略的复制, RBAC 权限控制, 访问控制, 活动审计, 身份认证

**评分**: 78

**项目地址**: [GitHub](https://github.com/goharbor/harbor)

---

## Kotlin

## [3. google-ai-edge/gallery](https://github.com/google-ai-edge/gallery)

**语言**: Kotlin  
**Stars**: ⭐ 0 (+853 today) | **Forks**: 🔱 1.8k

**原始描述**: A gallery that showcases on-device ML/GenAI use cases and allows people to try and use models locally.

**中文介绍（README总结）**: 这是一个展示并让用户在本地设备上试用机器学习/生成式 AI 用例的应用画廊，主打在手机端离线运行开源大语言模型，强调隐私与速度。它宣称已支持 Gemma 4，并提供如可扩展的 Agent Skills、带“Thinking Mode”的多轮聊天、图片问答、以及音频转写/翻译等功能；没有 Google Play 的用户可通过最新发布版本安装 APK。部分能力依赖所支持的模型，文中提到 Thinking Mode 目前从 Gemma 4 系列开始支持。

**关键词**: 端侧推理, 离线生成式AI, 多模态问图, 思维链可视化, 语音转写, 实时翻译, google-ai-edge, gallery

**评分**: 78

**项目地址**: [GitHub](https://github.com/google-ai-edge/gallery)

---

## Python

## [4. TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)

**语言**: Python  
**Stars**: ⭐ 0 (+645 today) | **Forks**: 🔱 679

**原始描述**: A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.

**中文介绍（README总结）**: 这是一个基于 Claude Code 的“SEO Machine”工作区，用于为各类企业创建长篇且 SEO 友好的博客内容，支持从调研、写作到分析与优化的完整流程。它包含自定义命令与多种专用智能体，可做搜索意图识别、关键词密度与聚类、可读性与质量评分，并可生成标题、元信息、内链与落地页优化建议。系统还能对接 GA4、Search Console 和 DataForSEO 等数据源获取实时表现洞察，同时依赖品牌语气与写作规范等上下文文件来保持内容一致性。使用前需安装 Claude Code 与相关 Python 依赖，并将模板化的品牌与示例内容补全为你的公司信息。

**关键词**: SEO 内容生成, 长文博客写作, 搜索意图识别, 关键词聚类, SEO 质量评分, 可读性评分, 内部链接优化, Meta 元素生成

**评分**: 64

**项目地址**: [GitHub](https://github.com/TheCraigHewitt/seomachine)

---

## [5. NVIDIA/personaplex](https://github.com/NVIDIA/personaplex)

**语言**: Python  
**Stars**: ⭐ 0 (+589 today) | **Forks**: 🔱 1.2k

**原始描述**: PersonaPlex code.

**中文介绍（README总结）**: 这段内容介绍了 PersonaPlex：一个基于 Moshi 架构与权重的实时全双工语音到语音对话模型，可通过文本角色提示控制人设，并用音频条件进行音色/声音风格控制。文中还概述了使用前置条件（如安装 Opus 编解码库、接受 Hugging Face 模型许可并配置认证）、启动服务器进行在线交互以及用离线脚本做 wav 输入输出评测等流程。它提到在显存不足时可用 CPU offload，并预置了一组更自然（NAT）或更多样（VAR）的语音嵌入供选择。

**关键词**: 全双工语音对话, 语音到语音生成, 实时低延迟, 人格控制, 角色提示词, 语音条件控制, 语音嵌入, 流式推理, GPU-CPU 混合推理, 离线语音评测

**评分**: 83

**项目地址**: [GitHub](https://github.com/NVIDIA/personaplex)

---

## [6. elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot)

**语言**: Python  
**Stars**: ⭐ 0 (+572 today) | **Forks**: 🔱 2.6k

**原始描述**: Create Reddit Videos with just✨ one command ✨

**中文介绍（README总结）**: 这是一个用“一条命令”自动生成 Reddit 风格短视频的项目，号称无需手动剪辑或整理素材，而是通过程序自动完成并输出视频文件。当前版本不会自动上传到平台，需要你手动上传以规避社区规范风险。运行大致需要 Python 3.10 和 Playwright，按步骤克隆仓库、安装依赖、配置 Reddit API（创建 script 应用）后即可使用，后续也可通过修改配置文件重新配置。

**关键词**: 视频自动生成, 内容抓取, 社媒短视频, 命令行工具, 视频渲染管线, 素材自动编排, 本地视频导出, elebumm

**评分**: 63

**项目地址**: [GitHub](https://github.com/elebumm/RedditVideoMakerBot)

---

## [7. newton-physics/newton](https://github.com/newton-physics/newton)

**语言**: Python  
**Stars**: ⭐ 0 (+67 today) | **Forks**: 🔱 411

**原始描述**: An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.

**中文介绍（README总结）**: Newton 是一个开源的 GPU 加速物理仿真引擎，构建在 NVIDIA Warp 之上，主要面向机器人与仿真研究人员。它扩展并泛化了 Warp 中已弃用的模块，以 MuJoCo Warp 作为主要后端，强调 GPU 计算、OpenUSD 支持、可微分能力与用户可扩展性，用于快速迭代与可扩展的机器人仿真。该项目由 Linux Foundation 社区维护，代码采用 Apache-2.0 许可、文档采用 CC-BY-4.0，最初由 Disney Research、Google DeepMind 与 NVIDIA 发起。

**关键词**: GPU物理仿真引擎, 机器人仿真, 可微分仿真, 多物理耦合, 碰撞与接触, 软体仿真, newton-physics, newton

**评分**: 78

**项目地址**: [GitHub](https://github.com/newton-physics/newton)

---

## [8. virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)

**语言**: Python  
**Stars**: ⭐ 0 (+123 today) | **Forks**: 🔱 8.8k

**原始描述**: An AI Hedge Fund Team

**中文介绍（README总结）**: 这是一个用于教育与概念验证的“AI 对冲基金”项目，目标是探索用 AI 辅助做交易决策，并不用于真实交易或投资。系统由多个代理协同工作，角色参考了多位知名投资人（如达摩达兰、格雷厄姆、巴菲特等）以及估值、情绪、基本面、技术等分析代理，共同产出交易信号。提供的信息仅说明了定位与代理构成，未包含具体策略细节、数据来源或实际回测结果。

**关键词**: Multi-Agent, AI对冲基金, 量化交易, 交易信号生成, 股票估值, 情绪分析, 基本面分析, 技术分析, 风险管理

**评分**: 62

**项目地址**: [GitHub](https://github.com/virattt/ai-hedge-fund)

---

## Shell

## [9. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.9k today) | **Forks**: 🔱 12.0k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: 这段文字介绍了名为 Superpowers 的“代理技能框架+软件开发方法论”，让编码代理先通过对话澄清真实目标并抽取规格说明，再以易读的分块形式让你确认设计。设计签署后，它会生成强调红/绿 TDD、YAGNI 和 DRY 的实施计划，并在你同意开始后用“子代理驱动开发”逐项执行、检查和评审以保持按计划推进。文末还提到如果该开源工具帮你赚钱可考虑赞助，并提示不同平台的安装方式不同（如 Claude Code/Cursor 有插件市场，Codex/OpenCode 需手动设置）。

**关键词**: 智能体工作流, 技能框架, 可组合技能, 规范澄清, 分块规格说明, 实现计划生成, 子智能体驱动开发, 代码代理插件, 插件市场集成

**评分**: 66

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## Unknown

## [10. forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

**语言**: Unknown  
**Stars**: ⭐ 0 (+686 today) | **Forks**: 🔱 584

**原始描述**: 

**中文介绍（README总结）**: 这份“Karpathy 启发的 Claude Code 指南”旨在纠正模型在编码时擅自假设、掩盖困惑、过度抽象与误改无关代码等问题，核心思路是写代码前先澄清不确定点并说明权衡，不要默选解释。它强调“简单优先”，只实现被要求的最小方案，避免为未来臆测的灵活性和臃肿设计。文中还提出“外科式改动”，即只触碰必要部分以减少副作用；其余原则在你提供的内容里被截断了，我无法完整复述。

**关键词**: LLM 编码指南, 假设显式化, 澄清提问, 权衡分析, 反向质疑, 极简实现, 避免过度工程, 最小变更, 代码清理, 注释保护

**评分**: 60

**项目地址**: [GitHub](https://github.com/forrestchang/andrej-karpathy-skills)

---

