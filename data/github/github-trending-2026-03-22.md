# GitHub Trending 日榜 | 2026-03-22

> 共 8 个项目

## 📑 目录

- [C](#C) (1 个项目)
- [C++](#Cplusplus) (1 个项目)
- [Go](#Go) (1 个项目)
- [Java](#Java) (1 个项目)
- [Python](#Python) (2 个项目)
- [Rust](#Rust) (1 个项目)
- [TypeScript](#TypeScript) (1 个项目)

---

## C

## [1. systemd/systemd](https://github.com/systemd/systemd)

**语言**: C  
**Stars**: ⭐ 0 (+58 today) | **Forks**: 🔱 4.4k

**原始描述**: The systemd System and Service Manager

**中文介绍（README总结）**: systemd 是 Linux 的系统与服务管理器，用于启动与管理系统进程、服务及其依赖关系，并提供统一的运行时管理能力。它面向 Linux 发行版维护者、系统管理员以及需要与系统服务集成的开发者。关键能力围绕服务单元与依赖编排、进程生命周期管理、以及与系统启动流程的整合，典型场景是在服务器或桌面系统中管理开机启动、守护进程运行与故障重启等。

**关键词**: Linux 初始化系统, 服务管理器, 单元文件（unit）, udev 设备管理, 启动流程（boot）, C 语言, systemd, System

**评分**: 18

**项目地址**: [GitHub](https://github.com/systemd/systemd)

---

## C++

## [2. protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf)

**语言**: C++  
**Stars**: ⭐ 0 (+7 today) | **Forks**: 🔱 16.1k

**原始描述**: Protocol Buffers - Google's data interchange format

**中文介绍（README总结）**: Protocol Buffers（protobuf）是 Google 提供的一种与语言和平台无关、可扩展的结构化数据序列化与交换格式，用于把数据高效编码成二进制并在系统间传输或存储。它面向需要跨语言、跨服务通信的开发者与分布式系统场景，通过 .proto 定义消息结构，并借助协议编译器生成各语言的数据类型与序列化/反序列化代码。典型用于微服务/ RPC 通信、日志与配置的结构化存储、以及移动端与后端之间的高效数据传输。

**关键词**: 结构化数据序列化, 二进制编码格式, 接口描述语言（IDL）, 代码生成, 多语言运行时, Bazel 构建集成, protocolbuffers, protobuf

**评分**: 15

**项目地址**: [GitHub](https://github.com/protocolbuffers/protobuf)

---

## Go

## [3. aquasecurity/trivy](https://github.com/aquasecurity/trivy)

**语言**: Go  
**Stars**: ⭐ 0 (+39 today) | **Forks**: 🔱 137

**原始描述**: Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more

**中文介绍（README总结）**: Trivy 是一款通用安全扫描器，用于在容器镜像、文件系统、Git 仓库、虚拟机镜像、Kubernetes 与云环境中发现已知漏洞（CVE）、配置错误与 IaC 问题、泄露的敏感信息/密钥，并生成软件依赖与 OS 包的 SBOM 及识别许可证风险。它面向开发者、安全团队和 DevSecOps 流水线，支持多种语言与操作系统，可集成到 CI/CD、集群扫描与本地开发工具中。典型场景包括镜像发布前的安全门禁、K8s 集群与基础设施配置审计、代码与依赖的持续漏洞与密钥泄露检测。

**关键词**: 容器镜像扫描, 漏洞扫描（CVE）, IaC配置审计, 密钥泄露检测, 软件许可证合规, 依赖项分析, 代码仓库扫描, 虚拟机镜像扫描, CI/CD安全集成, 文件系统扫描

**评分**: 28

**项目地址**: [GitHub](https://github.com/aquasecurity/trivy)

---

## Java

## [4. opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)

**语言**: Java  
**Stars**: ⭐ 0 (+950 today) | **Forks**: 🔱 547

**原始描述**: PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

**中文介绍（README总结）**: OpenDataLoader PDF 是一个开源的 PDF 解析器，面向需要把 PDF 转成可用于 AI/RAG 的结构化数据的开发者与团队，可从 PDF 提取 Markdown、带版面坐标的 JSON 和 HTML，并提供本地确定性解析与 AI 混合模式以处理复杂版面。它支持扫描件 OCR（多语言）以及表格、公式、图片/图表等内容抽取，适用于多栏文档、科研论文、低质量扫描等场景。项目也将同一版面分析能力用于 PDF 无障碍自动化，计划生成 Tagged PDF 以降低人工修复成本并提升合规效率。

**关键词**: PDF结构化解析, 文档版面分析, 表格结构识别, 公式识别, 坐标框标注, 多模态内容抽取, AI混合解析, RAG数据预处理, PDF可访问性自动标记

**评分**: 43

**项目地址**: [GitHub](https://github.com/opendataloader-project/opendataloader-pdf)

---

## Python

## [5. FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)

**语言**: Python  
**Stars**: ⭐ 0 (+283 today) | **Forks**: 🔱 1.9k

**原始描述**: Automate the process of making money online.

**中文介绍（README总结）**: MoneyPrinter V2 是一个用来自动化“线上赚钱”流程的应用，面向想通过社媒内容与营销获客变现的个人或小团队。它提供可定时运行的 Twitter 机器人与 YouTube Shorts 自动化发布，并支持 Amazon 联盟营销（结合 Twitter）以及本地商家线索挖掘与冷启动外联。项目强调模块化架构与可脚本化调用，典型场景包括社媒引流带货、短视频矩阵运营和自动化搜集商家名单后批量触达。

**关键词**: 社交媒体自动化, 联盟营销, 亚马逊联盟, 冷邮件外联, 本地商家爬取, 定时任务（CRON）, Python 自动化脚本, 邮件营销自动化

**评分**: 8

**项目地址**: [GitHub](https://github.com/FujiwaraChoki/MoneyPrinterV2)

---

## [6. vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)

**语言**: Python  
**Stars**: ⭐ 0 (+71 today) | **Forks**: 🔱 596

**原始描述**: A framework for efficient model inference with omni-modality models

**中文介绍（README总结）**: vLLM-Omni 是一个面向全模态（文本、图像/视频扩散生成、音频与 TTS 等）模型的高效推理与服务框架，目标是让模型部署更快、更省、更易用。它主要面向需要在生产环境提供多模态能力的开发者与平台方，扩展了 vLLM 在分布式执行、内存效率与稳定性上的能力，并提供更成熟的服务接口（含 OpenAI 兼容方向）与 profiling/benchmarking 支持。典型场景包括为 Qwen3-Omni/Qwen3-TTS、GLM-Image 以及 DiT 扩散图像/视频等模型提供统一的在线推理与生成服务，并覆盖 CUDA/ROCm/NPU/XPU 等多种硬件后端。

**关键词**: 多模态模型服务, 高效推理引擎, 分布式执行, 显存优化, DiT 图像视频生成, 音频生成, 异构硬件加速, 性能剖析与基准测试

**评分**: 47

**项目地址**: [GitHub](https://github.com/vllm-project/vllm-omni)

---

## Rust

## [7. louis-e/arnis](https://github.com/louis-e/arnis)

**语言**: Rust  
**Stars**: ⭐ 0 (+690 today) | **Forks**: 🔱 1.0k

**原始描述**: Generate any location from the real world in Minecraft with a high level of detail.

**中文介绍（README总结）**: Arnis 是一个将真实世界地点高精度生成到 Minecraft（Java 1.17+ 与基岩版）中的开源项目，面向想在游戏里复刻家乡、城市或自然地貌的玩家与创作者。它整合并处理 OpenStreetMap 的地理要素数据与高程数据，生成符合真实地形起伏、道路与建筑分布的世界，并支持调整比例、出生点及建筑内部等生成参数。典型场景是快速生成大范围城市地图用于探索、建造参考、跑酷/生存服务器地图或地理教学展示。

**关键词**: 真实世界地图生成, 程序化内容生成, 地理空间数据处理, 数字高程模型, 地形生成, 建筑生成, 大规模地图生成, louis-e

**评分**: 21

**项目地址**: [GitHub](https://github.com/louis-e/arnis)

---

## TypeScript

## [8. Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+2.0k today) | **Forks**: 🔱 721

**原始描述**: Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere.

**中文介绍（README总结）**: Project N.O.M.A.D 是一个离线优先、可自托管的“生存/应急知识与工具电脑（服务器）”，把关键资料库、教育内容与本地 AI 集成在一套浏览器可访问的系统里，适合断网环境下仍需获取信息的人群（如应急准备、偏远地区、野外/救灾场景）。它通过一个管理界面与 API 编排多种容器化服务（基于 Docker）来统一安装、配置与更新。关键能力包括基于 Ollama 的本地 AI 对话、文档上传与语义检索的知识库问答（RAG，使用 Qdrant），以及通过 Kiwix 提供的离线 Wikipedia/医疗参考/电子书等信息库与教育资源。典型场景是在没有公网或不稳定网络下搭建本地“知识与工具站”，供多设备通过浏览器访问查询与学习。

**关键词**: 离线优先, 本地知识库, 应急生存计算, 自托管知识服务器, 容器编排管理, RAG检索增强生成, 离线内容镜像（Kiwix）, 浏览器端管理控制台

**评分**: 21

**项目地址**: [GitHub](https://github.com/Crosstalk-Solutions/project-nomad)

---

