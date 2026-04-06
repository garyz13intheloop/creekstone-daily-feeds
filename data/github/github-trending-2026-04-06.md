# GitHub Trending 日榜 | 2026-04-06

> 共 12 个项目

## 📑 目录

- [C++](#Cplusplus) (2 个项目)
- [Go](#Go) (1 个项目)
- [Kotlin](#Kotlin) (1 个项目)
- [Python](#Python) (2 个项目)
- [Rust](#Rust) (1 个项目)
- [Swift](#Swift) (1 个项目)
- [TypeScript](#TypeScript) (3 个项目)
- [Unknown](#Unknown) (1 个项目)

---

## C++

## [1. google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)

**语言**: C++  
**Stars**: ⭐ 0 (+124 today) | **Forks**: 🔱 198

**原始描述**: 

**中文介绍（README总结）**: LiteRT-LM 是谷歌推出的面向端侧设备部署大语言模型的开源高性能推理框架，强调可用于生产环境。它支持 Android/iOS/Web/桌面与物联网等多平台，并可利用 GPU/NPU 加速，且提供视觉与音频多模态输入和函数调用等能力。资料称其已用于 Chrome、Chromebook Plus、Pixel Watch 等产品，并提供 CLI、语言指南与从源码构建方式，版本更新提到 v0.9.0 改进函数调用、v0.8.0 增加桌面 GPU 与多模态、v0.7.0 为 Gemma 提供 NPU 加速。

**关键词**: 边缘端LLM推理, 端侧模型部署, 跨平台运行, GPU硬件加速, NPU硬件加速, 多模态推理, 多模型兼容, google-ai-edge

**评分**: 88

**项目地址**: [GitHub](https://github.com/google-ai-edge/LiteRT-LM)

---

## [2. ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

**语言**: C++  
**Stars**: ⭐ 0 (+244 today) | **Forks**: 🔱 16.4k

**原始描述**: LLM inference in C/C++

**中文介绍（README总结）**: 这段内容概述了 llama.cpp 作为一个用纯 C/C++ 实现的本地/云端 LLM 推理项目，强调无需额外依赖、覆盖多种硬件平台并提供量化与多后端加速能力。它还提到一些近期动态与指南，例如 Hugging Face 缓存迁移、新 WebUI 使用、以及多模态支持与扩展插件等。文中给出安装与运行的快速入口（brew/nix/winget、Docker、预编译包或源码构建），并提示安装后需要获取或量化模型才能使用。

**关键词**: 本地部署, C/C++实现, 低比特量化, ggml-org, llama.cpp, LLM, inference, C++

**评分**: 72

**项目地址**: [GitHub](https://github.com/ggml-org/llama.cpp)

---

## Go

## [3. ollama/ollama](https://github.com/ollama/ollama)

**语言**: Go  
**Stars**: ⭐ 0 (+164 today) | **Forks**: 🔱 15.4k

**原始描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**中文介绍（README总结）**: 这段内容是在介绍 Ollama：可以快速在本地运行并集成多种模型（如 Kimi-K2.5、GLM-5、MiniMax、DeepSeek、Qwen、Gemma 等），并提供下载、手动安装和官方 Docker 镜像。它还列出可用的开发库（ollama-python、ollama-js）、REST API、CLI/文档以及支持的集成（如 Claude Code、Codex 等）和大量社区聊天界面项目。若要查看完整模型列表与接口细节，文中提示到 ollama.com/library 和 API 文档。

**关键词**: 本地LLM推理, 模型运行时, 模型管理, 命令行工具, 模型导入, 自托管聊天界面, ollama, Get

**评分**: 43

**项目地址**: [GitHub](https://github.com/ollama/ollama)

---

## Kotlin

## [4. google-ai-edge/gallery](https://github.com/google-ai-edge/gallery)

**语言**: Kotlin  
**Stars**: ⭐ 0 (+389 today) | **Forks**: 🔱 1.6k

**原始描述**: A gallery that showcases on-device ML/GenAI use cases and allows people to try and use models locally.

**中文介绍（README总结）**: Google AI Edge Gallery 是一个展示并让用户在本地设备上试用机器学习/生成式 AI 用例的应用，主打离线、隐私和高性能地运行开源大模型。它已支持 Gemma 4 系列，并提供如 Agent Skills 工具扩展、可查看推理过程的对话模式、图片问答以及语音转写/翻译等功能。没有 Google Play 的用户可以通过最新发布版本的 APK 安装。

**关键词**: 端侧推理, 多模态问图, 相机/相册输入, 语音转写, 实时翻译, 模块化技能加载, 事实校验, 推理过程可视化

**评分**: 82

**项目地址**: [GitHub](https://github.com/google-ai-edge/gallery)

---

## Python

## [5. NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**语言**: Python  
**Stars**: ⭐ 0 (+1.3k today) | **Forks**: 🔱 3.5k

**原始描述**: The agent that grows with you

**中文介绍（README总结）**: 这段文案在介绍 Nous Research 的 Hermes Agent：一个带“学习闭环”的自我改进 AI 代理，能从使用经验中生成与优化技能、做跨会话记忆与检索，并逐步建立对用户的长期画像。它强调可在多种算力环境运行（VPS、GPU 集群或低空闲成本的无服务器），且支持通过 Telegram 等远程交互。还宣称可自由切换多家模型与自建端点而无需改代码，并提供终端式界面、定时自动化、并行子代理与多种运行后端等能力。

**关键词**: 技能生成, 技能自优化, 记忆管理, FTS5 搜索, 定时任务调度, 多后端运行, 模型路由切换, NousResearch

**评分**: 78

**项目地址**: [GitHub](https://github.com/NousResearch/hermes-agent)

---

## [6. NVIDIA/personaplex](https://github.com/NVIDIA/personaplex)

**语言**: Python  
**Stars**: ⭐ 0 (+295 today) | **Forks**: 🔱 1.0k

**原始描述**: PersonaPlex code.

**中文介绍（README总结）**: 这段内容是在介绍 PersonaPlex 的代码与使用说明：它是一个基于 Moshi 架构与权重的实时全双工语音到语音对话模型，可用文字角色提示和音频声线条件来控制人设与声音，并强调低延迟与一致的对话风格。文档包含依赖安装（如 Opus 编码库）、从仓库安装、接受 HuggingFace 模型许可与登录鉴权、启动服务器并通过 Web UI 交互，以及用离线脚本对输入 wav 生成同长度输出 wav 的评测方式。还提到显存不足时可用 CPU offload，以及模型提供预置的 NAT/VAR 声音嵌入供选择。

**关键词**: 全双工语音对话, 语音到语音生成, 实时低延迟, 人格控制, 角色提示词, 语音条件控制, 语音嵌入, Opus音频编解码

**评分**: 82

**项目地址**: [GitHub](https://github.com/NVIDIA/personaplex)

---

## Rust

## [7. block/goose](https://github.com/block/goose)

**语言**: Rust  
**Stars**: ⭐ 0 (+882 today) | **Forks**: 🔱 3.6k

**原始描述**: an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

**中文介绍（README总结）**: goose 是一个本地运行、可扩展的开源 AI agent，目标是自动化完成从建项目、写代码到执行、调试和测试等工程任务，而不仅是给出代码建议。它可与任意 LLM 搭配并支持多模型配置以平衡性能与成本，还能集成 MCP 服务器，并提供桌面应用与 CLI 形式使用。文中也提到可通过自定义发行版预配置提供方、扩展和品牌，但具体支持范围与细节需参考其文档。

**关键词**: 开发自动化, 代码执行, 调试与测试, 工作流编排, 多模型配置, 插件扩展, block, goose

**评分**: 78

**项目地址**: [GitHub](https://github.com/block/goose)

---

## Swift

## [8. TelegramMessenger/Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS)

**语言**: Swift  
**Stars**: ⭐ 0 (+14 today) | **Forks**: 🔱 2.5k

**原始描述**: Telegram-iOS

**中文介绍（README总结）**: 这段内容是 Telegram iOS 源码编译指南摘要：开发者需要自己申请 api_id，不要用“Telegram”名称或官方纸飞机 logo，并遵循安全与隐私规范且按许可公开自己的代码。编译流程大致是获取源码、安装 Xcode、生成随机标识并新建工程，找到证书里的 Team ID 后编辑配置文件，再生成 Xcode 工程进行构建。还提到两类常见构建问题：遇到 “build-request.json not updated yet” 可取消后重建，出现 “Telegram_xcodeproj: no such package” 则需要重新生成/运行项目。

**关键词**: iOS 客户端, 源码编译, 代码签名, Xcode 项目生成, 隐私与安全, TelegramMessenger, Telegram-iOS, Telegram

**评分**: 68

**项目地址**: [GitHub](https://github.com/TelegramMessenger/Telegram-iOS)

---

## TypeScript

## [9. immich-app/immich](https://github.com/immich-app/immich)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+155 today) | **Forks**: 🔱 5.3k

**原始描述**: High performance self-hosted photo and video management solution.

**中文介绍（README总结）**: 这段内容介绍了一个高性能、自托管的照片和视频管理解决方案，并提醒用户务必遵循 3-2-1 备份原则以保护珍贵数据。它提供了主要文档与安装指南的入口，并列出功能、翻译等信息，且支持多种语言。文中还提到有在线演示与移动端相关信息，但具体账号凭据在此片段中未给出。

**关键词**: 自托管, 照片管理, 视频管理, 媒体库, 高性能, 备份策略, immich-app, immich

**评分**: 63

**项目地址**: [GitHub](https://github.com/immich-app/immich)

---

## [10. KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+703 today) | **Forks**: 🔱 3.8k

**原始描述**: Shannon Lite is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production.

**中文介绍（README总结）**: Shannon Lite 是 Keygraph 开发的面向 Web 应用和 API 的自主白盒 AI 渗透测试工具，会分析源代码寻找攻击面，并通过浏览器自动化与命令行工具对运行中的系统执行真实利用来验证漏洞。它只在最终报告中包含有可复现 PoC 的已证实可利用问题，覆盖注入、认证绕过、SSRF、XSS 等类型。文中还提到 Shannon 现已通过某个平台/渠道提供，但具体入口信息在摘录里不完整。

**关键词**: 白盒渗透测试, 源码安全分析, API 安全测试, 浏览器自动化, 命令行工具链, 可复现 PoC, CI/CD 安全测试, 认证绕过

**评分**: 73

**项目地址**: [GitHub](https://github.com/KeygraphHQ/shannon)

---

## [11. tobi/qmd](https://github.com/tobi/qmd)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+298 today) | **Forks**: 🔱 1.1k

**原始描述**: mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local

**中文介绍（README总结）**: 这段内容介绍了一个名为 QMD（Query Markup Documents）的本地迷你 CLI 搜索引擎，用于索引并检索你的 Markdown 笔记、会议记录、文档和知识库，可用关键词或自然语言搜索，并面向 agentic 工作流。它在本地结合 BM25 全文检索、向量语义检索与 LLM 重排，LLM 通过 node-llama-cpp 运行 GGUF 模型。QMD 还提供 MCP（Model Context Protocol）服务器与 HTTP 传输模式，支持搜索、按路径/ID 取文档、批量取回以及索引健康信息，并可作为 Node.js/Bun 的 SDK/库使用。

**关键词**: 本地文档搜索, 命令行工具, 混合检索, BM25, LLM 重排序, tobi, qmd, mini

**评分**: 73

**项目地址**: [GitHub](https://github.com/tobi/qmd)

---

## Unknown

## [12. kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

**语言**: Unknown  
**Stars**: ⭐ 0 (+281 today) | **Forks**: 🔱 1.3k

**原始描述**: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.

**中文介绍（README总结）**: 这段内容介绍了一套面向 Obsidian 的 Agent Skills，教智能体使用 Markdown、Bases、JSON Canvas，并能通过 CLI 工作，且遵循 Agent Skills 规范，可用于 Claude Code、Codex CLI 等兼容工具。安装方式包括用 npx skills 从 Marketplace 获取，或手动将仓库内容放入 Obsidian vault 根目录（Claude Code）、复制到 Codex 的 skills 路径，或在 OpenCode 中将整个仓库克隆到其 skills 目录并重启后自动发现生效。文中未给出 Codex/OpenCode 的具体默认路径细节。

**关键词**: 技能规范, kepano, obsidian-skills, Agent, skills, Obsidian, Teach, use

**评分**: 72

**项目地址**: [GitHub](https://github.com/kepano/obsidian-skills)

---

