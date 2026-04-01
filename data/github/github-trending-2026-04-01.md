# GitHub Trending 日榜 | 2026-04-01

> 共 6 个项目

## 📑 目录

- [HTML](#HTML) (1 个项目)
- [Python](#Python) (3 个项目)
- [Rust](#Rust) (1 个项目)
- [Shell](#Shell) (1 个项目)

---

## HTML

## [1. shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

**语言**: HTML  
**Stars**: ⭐ 0 (+2.5k today) | **Forks**: 🔱 2.6k

**原始描述**: practice made claude perfect

**中文介绍（README总结）**: 这段内容像是在汇总“Claude Code 最佳实践”的资料索引，核心强调以 Command→Agent→Skill 的编排模式，以及通用的 Research→Plan→Execute→Review→Ship 开发流程。它还罗列了多位作者/从业者的工作流与大量分类技巧条目（如提示、规划、CLAUDE.md、调试、Git/PR 等），并提出关于 CLAUDE.md 该写什么、是否需要额外规则文件、何时更新、为何会被忽略等问题。由于缺少完整上下文与链接，我只能判断它是一个指南目录或资源集合的片段。

**关键词**: 代理模式, 命令系统, 技能库, 编排工作流, 提示工程, 需求规格与规划, 跨模型协作, 开发闭环流程, 调试技巧

**评分**: 72

**项目地址**: [GitHub](https://github.com/shanraisshan/claude-code-best-practice)

---

## Python

## [2. microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)

**语言**: Python  
**Stars**: ⭐ 0 (+1.7k today) | **Forks**: 🔱 3.8k

**原始描述**: Open-Source Frontier Voice AI

**中文介绍（README总结）**: 这段信息介绍了开源语音 AI 项目 VibeVoice 的进展：2026-01-21 开源了可一次处理 60 分钟音频的 VibeVoice-ASR，支持 50+ 语言、可输出带说话人/时间戳/内容的结构化转写并支持自定义上下文，同时提供微调代码、vLLM 推理与技术报告。2026-03-06 起该 ASR 已纳入 Hugging Face Transformers，便于直接集成使用，社区也在此基础上做了语音输入法 Vibing（提供 macOS/Windows 下载）。此外在 2025-12 开源了实时 TTS 模型 VibeVoice‑Realtime‑0.5B，并加入多语言与多风格的实验说话人。最后一条 2025-09 的说明被截断，只能看出其提到发现不符合初衷的使用案例并与微软的负责任 AI 原则相关，但具体措施未给全。

**关键词**: 语音识别, 长音频转写, 结构化转录, 说话人分离, 时间戳对齐, 多语言识别, 上下文定制, 实时语音合成, 流式文本转语音, 微调训练代码

**评分**: 71

**项目地址**: [GitHub](https://github.com/microsoft/VibeVoice)

---

## [3. google-research/timesfm](https://github.com/google-research/timesfm)

**语言**: Python  
**Stars**: ⭐ 0 (+495 today) | **Forks**: 🔱 956

**原始描述**: TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting.

**中文介绍（README总结）**: TimesFM（Time Series Foundation Model）是 Google Research 提出的预训练时间序列基础模型，用于时间序列预测，并在 ICML 2024 以 decoder-only 架构发布。最新版本为 TimesFM 2.5，相比 2.0 参数量从 500M 降到 200M，最大上下文长度提升到 16k，并可选配约 30M 的分位数头以支持最长约 1k 预测步长。该模型在 Hugging Face 提供权重集合，也可在 BigQuery 以官方产品形式使用，但这里提到的开源版本不属于官方支持的 Google 产品。

**关键词**: 时间序列预测, 时间序列基础模型, 预训练模型, 长上下文建模, 分位数预测, 协变量回归（XReg）, google-research, timesfm

**评分**: 86

**项目地址**: [GitHub](https://github.com/google-research/timesfm)

---

## [4. luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)

**语言**: Python  
**Stars**: ⭐ 0 (+3.3k today) | **Forks**: 🔱 1.7k

**原始描述**: A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**中文介绍（README总结）**: 这段文案在推广一份以示例和可视化为主的 Claude Code 学习指南，主打用可复制的模板把功能组合成能省时间的真实工作流。它强调官方文档偏“功能说明”但缺少整合用法与学习路径，导致用户只会基础提示词，难以掌握 hooks、memory、子代理和 MCP 等进阶能力。该指南宣称提供模块化教程、配置与脚本模板、Mermaid 图解以及循序渐进的路线，帮助从入门快速进阶到能编排代理团队。

**关键词**: 多 Agent 团队, MCP 服务器, 记忆管理（Memory）, 工作流自动化, 代码审查流水线, 安全扫描集成, luongnv89, claude-howto

**评分**: 74

**项目地址**: [GitHub](https://github.com/luongnv89/claude-howto)

---

## Rust

## [5. openai/codex](https://github.com/openai/codex)

**语言**: Rust  
**Stars**: ⭐ 0 (+2.3k today) | **Forks**: 🔱 9.9k

**原始描述**: Lightweight coding agent that runs in your terminal

**中文介绍（README总结）**: Codex CLI 是 OpenAI 的轻量级编码代理，可在你的终端里本地运行；想在 VS Code、Cursor、Windsurf 等编辑器里用则安装对应 IDE 版本，想要桌面应用体验可运行 codex app 或访问 Codex App 页面，云端版本 Codex Web 在 chatgpt.com/codex。它可通过常用包管理器全局安装后直接运行，也可从 GitHub Release 下载适合平台的二进制（如 Apple Silicon/arm64、x86_64），解压后通常需要把带平台名的可执行文件重命名为 codex。运行后可选择“Sign in with ChatGPT”用你的 Plus/Pro/Team/Edu/Enterprise 计划登录使用，也可用 API key 但需要额外配置；该仓库采用 Apache-2.0 许可证。

**关键词**: 终端编码 Agent, 本地运行, 预编译二进制发布, 开发者工作流, openai, codex, Lightweight, coding

**评分**: 86

**项目地址**: [GitHub](https://github.com/openai/codex)

---

## Shell

## [6. anthropics/claude-code](https://github.com/anthropics/claude-code)

**语言**: Shell  
**Stars**: ⭐ 0 (+3.9k today) | **Forks**: 🔱 14.2k

**原始描述**: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**中文介绍（README总结）**: Claude Code 是一款在终端中使用的代理式编码工具，能理解你的代码库，通过自然语言指令执行日常任务、解释复杂代码并处理 git 工作流，也可在 IDE 中使用或在 GitHub 上通过 @claude 触发。仓库还包含可扩展功能的插件，并提供在工具内或通过 GitHub Issues 反馈问题的方式。官方说明提到会收集包含使用情况与对话在内的反馈数据，并采取一定隐私保护措施且声明不将反馈用于模型训练，具体以其服务条款与隐私政策为准。

**关键词**: 终端编码助手, 自然语言命令, Git 工作流, 任务自动化, 插件系统, 命令行工具, anthropics, claude-code

**评分**: 78

**项目地址**: [GitHub](https://github.com/anthropics/claude-code)

---

