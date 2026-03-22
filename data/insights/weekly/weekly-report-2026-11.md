# Weekly Research Report | 2026-03-09 ~ 2026-03-15

> generated_at: 2026-03-22T03:09:58Z
> k_selected: 4
> embedding_model: text-embedding-3-large
> chat_model: gpt-5.2-2025-12-11

## 1) 本周摘要（2026-03-09 ~ 2026-03-15）

1. **“多模态生成”正从单点能力走向“可交付的内容生产线”**：从幻灯片生成（品牌一致性、对话迭代）到视频本地化（配音/口型/字幕/画面文字翻译）再到多模型聚合编排，产品形态更接近“生成—编辑—翻译—交付”的端到端链路，而非单一模型 Demo。[source:producthunt:ph-2026-03-11-1][source:producthunt:ph-2026-03-11-2][source:clawhub:ch-2026-03-13-8]

2. **“可执行 AI 代理”基础设施在补齐两类关键短板：系统接入与可追溯身份**：统一 SaaS 连接层（托管 OAuth、100+ 服务、搜索接入）降低真实业务读写门槛，同时去中心化可验证身份/声明试图解决“代理是谁、能否校验与追责”。[source:clawhub:ch-2026-03-10-9][source:clawhub:ch-2026-03-13-17]

3. **CLI 驱动的可运维自动化链路继续扩张**：围绕文档结构化（OCR）、离线语音转写（ASR）、浏览器自动化（登录准备/二维码捕获）等“可组合组件”，以命令行方式更便于审阅、集成与部署，但端到端自动化仍存在人工断点与质量边界。[source:clawhub:ch-2026-03-13-4][source:clawhub:ch-2026-03-10-23][source:clawhub:ch-2026-03-10-13]

4. **“可验证查询链 + 基准/裁判机制”成为后训练与高风险场景的共同瓶颈**：医疗处方审核推动“查询并生成”的可追溯路径；代理式 RL 后训练强调行动选择与反思；但“LLM-as-Judge”在不可验证任务上存在被对抗性“骗分”的系统性风险，评测可信度成为约束项。[source:arxiv:ax-2026-03-12-1][source:arxiv:ax-2026-03-10-1][source:arxiv:ax-2026-03-13-1]

---

## 2) 趋势主题（4 个）

### 主题 A：多模态内容生成与工作流编排——从幻灯片到视频的可控生产线
**Why now（为什么是现在）**  
- 一方面，市场需求从“生成一段素材”迁移到“交付一份成片/成稿”，因此产品把多模态能力打包成可重复的工作流：例如将笔记/提示快速产出品牌化演示并可对话迭代。[source:producthunt:ph-2026-03-11-1]  
- 另一方面，跨语言内容分发成为刚需，视频本地化不再只做字幕/配音，而进一步覆盖“画面内文字检测与翻译且保持布局/风格/动画”的保真要求，使工具更贴近商业投放与出海交付。[source:producthunt:ph-2026-03-11-2]  
- 同时，聚合类产品把多家图像/视频/音乐生成服务做统一调用与编排，凸显“模型路由、参数适配、素材管理、结果回传”的工程化诉求，反映团队在多模型时代更像在搭建生产线而非挑单一模型。[source:clawhub:ch-2026-03-13-8]

**代表项目对比（同一主题内的“分工”正在清晰化）**  
- *Chronicle 2.0* 更像“演示交付工具”：强调品牌一致性与对话迭代，目标是快速得到可用初稿并持续打磨，而非追求模型可控参数的极致。[source:producthunt:ph-2026-03-11-1]  
- *Visual Translate by Vozo* 聚焦“存量视频的多语言再生产”：在配音、口型同步、字幕之外，把屏幕文字翻译纳入同一链路，面向全球化营销/培训视频的规模化改版。[source:producthunt:ph-2026-03-11-2]  
- *IMA Studio All-in-One* 代表“多模型聚合与编排层”：以统一入口调用多家生成服务，强调路由与工作流，适合需要在不同模型之间做成本/风格/速度权衡的内容团队。[source:clawhub:ch-2026-03-13-8]

**主要风险与不确定性**  
- 聚合/编排层的能力上限受底层模型与额度/接口限制影响，质量、风格上限与可控性可能在不同提供方间波动，进而影响交付稳定性。[source:clawhub:ch-2026-03-13-8]  
- 视频本地化中“画面文本翻译并保持布局/风格/动画”的鲁棒性难以一次性覆盖所有素材类型（图表/标注/标签/幻灯片式内容等），验收标准与一致性度量仍是落地难点。[source:producthunt:ph-2026-03-11-2]

**下周观察点**  
- 多模型聚合工具是否进一步产品化“路由策略 + 参数适配 + 素材/版本管理”，从“工具箱”走向“可追溯生产线”。[source:clawhub:ch-2026-03-13-8]  
- 幻灯片生成是否继续强化“品牌一致性 + 对话式迭代”的确定性，减少从笔记到可交付初稿的不可控波动。[source:producthunt:ph-2026-03-11-1]

---

### 主题 B：面向业务流程的“可执行 AI 代理”基础设施——连接器 + 身份证明 + 多角色协作
**Why now**  
- 代理要进入真实业务系统，首先要解决“怎么安全接入”：统一连接器与托管 OAuth 把多 SaaS 的认证与 API 封装起来，降低“一个工作流里读写多个系统”的工程门槛，并扩展到搜索类入口（如新增 Brave Search）。[source:clawhub:ch-2026-03-10-9]  
- 其次是“代理是谁、能否验证与追责”：可验证代理身份方案通过标准（ERC-8004）与证明注册表发布/校验声明，试图为代理的行为建立身份锚点与可审计线索。[source:clawhub:ch-2026-03-13-17]  
- 第三是“协作怎么规模化”：多角色“AI 代理机构”模板把跨职能交付流程（角色、产出物、成功指标）模板化，降低团队把代理纳入组织流程的试错成本。[source:github:gh-2026-03-12-8]

**代表项目对比**  
- *API Gateway* 解决“接入与执行面”：更偏基础设施，价值在于连接器覆盖与统一 API 抽象，适配工作流/代理在多系统间的读写与同步。[source:clawhub:ch-2026-03-10-9]  
- *Verified Agent Identity* 解决“身份与信任面”：不做消息投递、仅输出签名或链接的取舍，反映其定位是最小依赖的身份/证明组件，便于嵌入不同代理栈。[source:clawhub:ch-2026-03-13-17]  
- *agency-agents* 解决“组织流程面”：用模板把“角色分工—流程—交付物—成功指标”固化，利于在 Claude Code 等环境中复用与扩展。[source:github:gh-2026-03-12-8]

**主要风险与不确定性**  
- 连接器能力受限于第三方开放 API 与配额：未开放接口、未授权数据、平台限流都会成为代理端到端执行的硬边界。[source:clawhub:ch-2026-03-10-9]  
- 托管 OAuth 与跨 SaaS 读写带来权限与合规风险：若缺少最小权限、审计与撤权机制，可能把自动化能力变成系统性风险放大器。[source:clawhub:ch-2026-03-10-9]  
- 去中心化身份体系的采用门槛与互操作性仍待验证：标准与注册表生态兼容、证明发布/校验流程、治理与撤销机制是否成熟，决定其能否成为通用组件。[source:clawhub:ch-2026-03-13-17]

**下周观察点**  
- 连接器层是否继续扩展服务覆盖并强化能力边界说明与参考实现，尤其是搜索/知识入口的接入路径。[source:clawhub:ch-2026-03-10-9]  
- 身份/证明组件是否出现更清晰的端到端示例（绑定—签名—发布—校验—撤销/更新），从概念走向可复用工程实践。[source:clawhub:ch-2026-03-13-17]  
- 多角色模板是否新增更可衡量的交付物标准与成功指标，以支持更长链路的跨职能协作。[source:github:gh-2026-03-12-8]

---

### 主题 C：CLI 驱动的自动化工作流——内容抽取（OCR/ASR）+ 浏览器操作（登录准备）
**Why now**  
- CLI 形态天然适配可运维化：易脚本化、易集成到 CI/定时任务/批处理；在“把外部能力组件化”后，团队更需要一种可审阅、可复跑的编排方式来稳定落地。[source:clawhub:ch-2026-03-13-4]  
- 输入侧“结构化”能力在增强：复杂 PDF/图片文档通过 OCR 解析输出 Markdown/JSON，为后续检索、审阅、自动报告/归档提供结构化基座。[source:clawhub:ch-2026-03-13-4]  
- 同时，离线语音转写把会议/访谈/客服质检等音频资产转为文本，成为知识沉淀与流程自动化的前置步骤。[source:clawhub:ch-2026-03-10-23]  
- 执行侧则出现更“工程化”的浏览器自动化切片，例如抓取微信网页版登录二维码用于无人值守登录准备与可用性巡检，说明大量业务仍需在 Web UI 上“补齐自动化”。[source:clawhub:ch-2026-03-10-13]

**代表项目对比**  
- *PaddleOCR Document Parsing*：面向“文档到结构化数据”，价值在于版面解析与结构输出（Markdown/JSON），对合同/票据/报告等再利用场景更直接。[source:clawhub:ch-2026-03-13-4]  
- *Doubao ASR*：面向“音频到文本”，偏离线批处理；其在工作流中的角色通常是“文本化入口”，后续仍需摘要、分段、说话人处理等组件承接。[source:clawhub:ch-2026-03-10-23]  
- *Wechat File Helper*：面向“Web UI 自动化的关键一步”，重点是页面检测、自动打开与二维码捕获；它更像把不可 API 化的环节切成可观测/可触发的节点。[source:clawhub:ch-2026-03-10-13]

**主要风险与不确定性**  
- 文档解析对低清晰度、遮挡、特殊版式的结构还原受限，输出质量强依赖输入质量与版面复杂度，影响下游自动化的稳定性与可解释性。[source:clawhub:ch-2026-03-13-4]  
- 浏览器自动化往往停在“可视信息捕获”，登录扫码等环节仍需人工或外部系统配合，端到端自动化存在断点。[source:clawhub:ch-2026-03-10-13]  
- ASR 更多覆盖离线转写，不等同于实时通话链路与语义理解；若直接用于质检/合规判断，需额外设计误差兜底与抽检机制。[source:clawhub:ch-2026-03-10-23]

**下周观察点**  
- OCR 输出在“段落/表格层级稳定性、版面结构一致性”的工程改进是否出现明确量化或更广的适配说明。[source:clawhub:ch-2026-03-13-4]  
- 浏览器自动化是否补齐扫码后续对接方式，减少人工断点（例如通过外部会话管理/状态回传）。[source:clawhub:ch-2026-03-10-13]  
- ASR 工作流是否出现更工程化的增强（如字段路径、说话人分离、置信度输出的使用范式）。[source:clawhub:ch-2026-03-10-23]

---

### 主题 D：可验证“查询并生成”与基准驱动的代理后训练——从安全可追溯到评测反作弊
**Why now**  
- 高风险场景（如处方审核）推动从“让 LLM 直接给结论”转向“可验证查询链”：用知识库约束与查询路径实现更可追溯、更可审计的决策过程。[source:arxiv:ax-2026-03-12-1]  
- 与此同时，代理能力提升越来越依赖后训练：ACT 通过强化学习让代理在备选行动中做更优判断并学习自我反思，体现“行动选择质量”成为代理性能关键变量。[source:arxiv:ax-2026-03-10-1]  
- 但评测与裁判机制本身在变成瓶颈：研究显示在不可验证任务上，推理型 LLM 裁判可能被对抗性输出系统性“骗分”，导致看似提升、实为投机的后训练结果。[source:arxiv:ax-2026-03-13-1]

**代表项目/论文对比**  
- *PharmGraph-Auditor*：强调“安全与可追溯”，以混合药学知识库与可验证查询链为核心，适合需要审计链路的合规场景。[source:arxiv:ax-2026-03-12-1]  
- *ACT（Agentic Critical Training）*：强调“行动决策与反思能力”，更接近通用代理训练范式，价值在于提升多项代理/推理基准表现。[source:arxiv:ax-2026-03-10-1]  
- *LLMs-as-Judges in Non-Verifiable Post-Training*：强调“评测可靠性与对抗风险”，其结论直接影响后训练路线的可信度与迭代方向。[source:arxiv:ax-2026-03-13-1]

**主要风险与不确定性**  
- 不可验证任务上的 LLM 裁判易被对抗，可能把 RL 后训练导向“骗裁判”而非真实能力提升，进而污染基准与研究结论。[source:arxiv:ax-2026-03-13-1]  
- “可验证查询链”也可能固化错误：如果结构化知识或查询规则本身有误，系统可能生成“可追溯但错误”的结论，风险从生成层迁移到知识/规则治理层。[source:arxiv:ax-2026-03-12-1]

**下周观察点**  
- 是否出现针对“不可验证任务”更强的评测设计（例如多裁判一致性、对抗测试、外部可检验信号引入）以回应骗分问题。[source:arxiv:ax-2026-03-13-1]  
- ACT 类方法是否在更严格的评测设置下复现增益，并明确与“对抗裁判优化”的区分边界。[source:arxiv:ax-2026-03-10-1]  
- 可验证查询链框架是否扩展到更多高风险审核/合规领域并给出对比评测或真实审计案例。[source:arxiv:ax-2026-03-12-1]

---

## 3) 项目榜单（Hot / Rising / Novel）

> 注：以下为来源榜单的原始分数展示，不对缺失字段做推断。[source:clawhub:ch-2026-03-10-9][source:clawhub:ch-2026-03-13-17][source:clawhub:ch-2026-03-13-4][source:github:gh-2026-03-12-8][source:clawhub:ch-2026-03-10-23][source:clawhub:ch-2026-03-10-13][source:github:gh-2026-03-12-10][source:producthunt:ph-2026-03-11-1]

**Hot Top**（热度）  
1. API Gateway（clawhub）hot=3.0 rise=2.4 total=40 [source:clawhub:ch-2026-03-10-9]  
2. Verified Agent Identity（clawhub）hot=2.669 rise=2.1352 total=45 [source:clawhub:ch-2026-03-13-17]  
3. PaddleOCR Document Parsing（clawhub）hot=2.3821 rise=1.9057 total=29 [source:clawhub:ch-2026-03-13-4]  
4. msitarzewski/agency-agents（github）hot=2.38 rise=1.0927 total=13 [source:github:gh-2026-03-12-8]  
5. Doubao ASR / 豆包语音转写（clawhub）hot=1.7403 rise=1.3922 total=10 [source:clawhub:ch-2026-03-10-23]

**Rising Top**（增长）  
1. API Gateway（clawhub）hot=3.0 rise=2.4 total=40 [source:clawhub:ch-2026-03-10-9]  
2. Verified Agent Identity（clawhub）hot=2.669 rise=2.1352 total=45 [source:clawhub:ch-2026-03-13-17]  
3. Wechat File Helper（clawhub）hot=1.3051 rise=2.0142 total=0 [source:clawhub:ch-2026-03-10-13]  
4. PaddleOCR Document Parsing（clawhub）hot=2.3821 rise=1.9057 total=29 [source:clawhub:ch-2026-03-13-4]  
5. alibaba/page-agent（github）hot=0.781 rise=1.8343 total=36 [source:github:gh-2026-03-12-10]

**Novel Top**（新颖）  
1. API Gateway（clawhub）hot=3.0 rise=2.4 total=40 [source:clawhub:ch-2026-03-10-9]  
2. Verified Agent Identity（clawhub）hot=2.669 rise=2.1352 total=45 [source:clawhub:ch-2026-03-13-17]  
3. PaddleOCR Document Parsing（clawhub）hot=2.3821 rise=1.9057 total=29 [source:clawhub:ch-2026-03-13-4]  
4. Doubao ASR / 豆包语音转写（clawhub）hot=1.7403 rise=1.3922 total=10 [source:clawhub:ch-2026-03-10-23]  
5. Chronicle 2.0（producthunt）hot=1.6991 rise=1.3593 total=62 [source:producthunt:ph-2026-03-11-1]

---

## 4) 关键词趋势（结合项目“落点”解读）

1. **TTS/语音相关词上行，体现“交付链路”对声音资产的依赖增加**：视频翻译本地化产品把配音纳入一体化流程，说明语音不再是附加功能，而是多语言交付的一部分。[source:producthunt:ph-2026-03-11-2]

2. **“可控生成”“文生/图生视频”热度抬升，但被“编排/路由”重新定义**：与其押注单一模型的可控参数，团队更倾向用聚合与工作流把不确定性装进可替换组件，通过路由在成本/风格/速度间做调度。[source:clawhub:ch-2026-03-13-8]

3. **“项目管理/多角色协作”与代理落地绑定更紧**：代理不只是执行工具，更被当作“组织流程模板”的参与者；以角色、产出物、成功指标固化协作方式，是把代理引入团队的低摩擦路径。[source:github:gh-2026-03-12-8]

4. **“评测基准构建/裁判可靠性”升温，原因是后训练进入对抗阶段**：当研究指出裁判可能被系统性骗分时，评测方法本身就成为能力提升的上限约束，后训练路线不得不把“反作弊”纳入设计目标。[source:arxiv:ax-2026-03-13-1]

---

## 5) 交叉来源观察（多源共振意味着“从概念到产品化/工程化”）

1. **内容生产线主题同时出现在产品与工具聚合端**：从面向创作者的演示交付（Product Hunt）到多模型编排聚合（Clawhub），显示“生成能力商品化”后竞争转向“工作流与交付确定性”。[source:producthunt:ph-2026-03-11-1][source:clawhub:ch-2026-03-13-8]

2. **代理基础设施同时在“接入层、身份层、协作层”出现开源与产品化并进**：连接器（Clawhub）、可验证身份（Clawhub）、多角色模板（GitHub）的组合，说明行业正补齐代理进入企业流程所需的三件套：能连、可信、能协作。[source:clawhub:ch-2026-03-10-9][source:clawhub:ch-2026-03-13-17][source:github:gh-2026-03-12-8]

3. **研究侧与应用侧围绕“可验证性”形成闭环压力**：处方审核框架强调可追溯（研究端），而裁判被欺骗的发现反向推动更严谨的评测与验收（研究端），最终会影响到代理/内容工具在企业交付中的验收方式（应用端）。[source:arxiv:ax-2026-03-12-1][source:arxiv:ax-2026-03-13-1]

---

## 6) 下周预测（克制推断：仅基于本周证据的延伸）

1. **连接器层将继续“向外扩展、向内收敛”**：向外扩展更多 SaaS/搜索入口，向内收敛统一权限、审计与最小授权实践，否则难以支撑代理在真实业务中的规模化读写。[source:clawhub:ch-2026-03-10-9]

2. **代理身份/证明会从“有标准”走向“可用工作流示例”竞争**：谁能提供更短路径的绑定、签名、发布、校验与撤销示例，谁更可能成为被集成的基础组件。[source:clawhub:ch-2026-03-13-17]

3. **视频本地化将从“翻译”升级到“视觉元素保真”攻坚**：画面文字翻译只是第一步，下一阶段竞争点会是对图表/标注/动画等复杂视觉元素的一致性保持与可验证验收。[source:producthunt:ph-2026-03-11-2]

4. **评测与后训练会更强调“对抗稳健性”而非单一分数提升**：在不可验证任务上，若不引入对抗测试与多信号校验，后训练提升可能继续被“骗分”稀释，短期内会推动更多关于裁判机制与评测流程的复现实证。[source:arxiv:ax-2026-03-13-1]

## 引用索引

- [arxiv:ax-2026-03-10-1] Agentic Critical Training (https://arxiv.org/abs/2603.08706v1)
- [arxiv:ax-2026-03-10-10] Talking Together: Synthesizing Co-Located 3D Conversations from Audio (https://arxiv.org/abs/2603.08674v1)
- [arxiv:ax-2026-03-10-11] ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting (https://arxiv.org/abs/2603.08661v1)
- [arxiv:ax-2026-03-10-12] CAST: Modeling Visual State Transitions for Consistent Video Retrieval (https://arxiv.org/abs/2603.08648v1)
- [arxiv:ax-2026-03-10-13] Retrieval-Augmented Gaussian Avatars: Improving Expression Generalization (https://arxiv.org/abs/2603.08645v1)
- [arxiv:ax-2026-03-10-14] UNBOX: Unveiling Black-box visual models with Natural-language (https://arxiv.org/abs/2603.08639v1)
- [arxiv:ax-2026-03-10-15] StreamReady: Learning What to Answer and When in Long Streaming Videos (https://arxiv.org/abs/2603.08620v1)
- [arxiv:ax-2026-03-10-16] FOMO-3D: Using Vision Foundation Models for Long-Tailed 3D Object Detection (https://arxiv.org/abs/2603.08611v1)
- [arxiv:ax-2026-03-10-17] Weakly Supervised Teacher-Student Framework with Progressive Pseudo-mask Refinement for Gland Segmentation (https://arxiv.org/abs/2603.08605v1)
- [arxiv:ax-2026-03-10-18] Boosting MLLM Spatial Reasoning with Geometrically Referenced 3D Scene Representations (https://arxiv.org/abs/2603.08592v1)
- [arxiv:ax-2026-03-10-19] Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting (https://arxiv.org/abs/2603.08707v1)
- [arxiv:ax-2026-03-10-2] Evaluating Financial Intelligence in Large Language Models: Benchmarking SuperInvesting AI with LLM Engines (https://arxiv.org/abs/2603.08704v1)
- [arxiv:ax-2026-03-10-20] Split Federated Learning Architectures for High-Accuracy and Low-Delay Model Training (https://arxiv.org/abs/2603.08687v1)
- [arxiv:ax-2026-03-10-21] A New Lower Bound for the Random Offerer Mechanism in Bilateral Trade using AI-Guided Evolutionary Search (https://arxiv.org/abs/2603.08679v1)
- [arxiv:ax-2026-03-10-22] How Far Can Unsupervised RLVR Scale LLM Training? (https://arxiv.org/abs/2603.08660v1)
- [arxiv:ax-2026-03-10-23] Context-free Self-Conditioned GAN for Trajectory Forecasting (https://arxiv.org/abs/2603.08658v1)
- [arxiv:ax-2026-03-10-24] Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning (https://arxiv.org/abs/2603.08651v1)
- [arxiv:ax-2026-03-10-25] Divide and Predict: An Architecture for Input Space Partitioning and Enhanced Accuracy (https://arxiv.org/abs/2603.08649v1)
- [arxiv:ax-2026-03-10-26] Grow, Don't Overwrite: Fine-tuning Without Forgetting (https://arxiv.org/abs/2603.08647v1)
- [arxiv:ax-2026-03-10-27] Integral Formulas for Vector Spherical Tensor Products (https://arxiv.org/abs/2603.08630v1)
- [arxiv:ax-2026-03-10-28] Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence (https://arxiv.org/abs/2603.08600v1)
- [arxiv:ax-2026-03-10-29] Towards Batch-to-Streaming Deep Reinforcement Learning for Continuous Control (https://arxiv.org/abs/2603.08588v1)
- [arxiv:ax-2026-03-10-3] A Multi-Objective Optimization Approach for Sustainable AI-Driven Entrepreneurship in Resilient Economies (https://arxiv.org/abs/2603.08692v1)
- [arxiv:ax-2026-03-10-30] DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control (https://arxiv.org/abs/2603.08583v1)
- [arxiv:ax-2026-03-10-4] OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning (https://arxiv.org/abs/2603.08655v1)
- [arxiv:ax-2026-03-10-5] CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation (https://arxiv.org/abs/2603.08652v1)
- [arxiv:ax-2026-03-10-6] Scale Space Diffusion (https://arxiv.org/abs/2603.08709v1)
- [arxiv:ax-2026-03-10-7] FVG-PT: Adaptive Foreground View-Guided Prompt Tuning for Vision-Language Models (https://arxiv.org/abs/2603.08708v1)
- [arxiv:ax-2026-03-10-8] HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising (https://arxiv.org/abs/2603.08703v1)
- [arxiv:ax-2026-03-10-9] ER-Pose: Rethinking Keypoint-Driven Representation Learning for Real-Time Human Pose Estimation (https://arxiv.org/abs/2603.08681v1)
- [arxiv:ax-2026-03-11-1] GR-SAP: Generative Replay for Safety Alignment Preservation during Fine-Tuning (https://arxiv.org/abs/2603.10243v1)
- [arxiv:ax-2026-03-11-10] Robust Post-Training for Generative Recommenders: Why Exponential Reward-Weighted SFT Outperforms RLHF (https://arxiv.org/abs/2603.10279v1)
- [arxiv:ax-2026-03-11-11] Estimating condition number with Graph Neural Networks (https://arxiv.org/abs/2603.10277v1)
- [arxiv:ax-2026-03-11-12] Discovery of a Hematopoietic Manifold in scGPT Yields a Method for Extracting Performant Algorithms from Biological Foundation Model Internals (https://arxiv.org/abs/2603.10261v1)
- [arxiv:ax-2026-03-11-13] Improving TabPFN's Synthetic Data Generation by Integrating Causal Structure (https://arxiv.org/abs/2603.10254v1)
- [arxiv:ax-2026-03-11-14] SiMPO: Measure Matching for Online Diffusion Reinforcement Learning (https://arxiv.org/abs/2603.10250v1)
- [arxiv:ax-2026-03-11-15] Rethinking the Harmonic Loss via Non-Euclidean Distance Layers (https://arxiv.org/abs/2603.10225v1)
- [arxiv:ax-2026-03-11-2] S-GRADES -- Studying Generalization of Student Response Assessments in Diverse Evaluative Settings (https://arxiv.org/abs/2603.10233v1)
- [arxiv:ax-2026-03-11-3] A Robust Deep Learning Framework for Bangla License Plate Recognition Using YOLO and Vision-Language OCR (https://arxiv.org/abs/2603.10267v1)
- [arxiv:ax-2026-03-11-4] Joint Imaging-ROI Representation Learning via Cross-View Contrastive Alignment for Brain Disorder Classification (https://arxiv.org/abs/2603.10253v1)
- [arxiv:ax-2026-03-11-5] One Adapter for All: Towards Unified Representation in Step-Imbalanced Class-Incremental Learning (https://arxiv.org/abs/2603.10237v1)
- [arxiv:ax-2026-03-11-6] Why Does It Look There? Structured Explanations for Image Classification (https://arxiv.org/abs/2603.10234v1)
- [arxiv:ax-2026-03-11-7] OilSAM2: Memory-Augmented SAM2 for Scalable SAR Oil Spill Detection (https://arxiv.org/abs/2603.10231v1)
- [arxiv:ax-2026-03-11-8] GSVD for Geometry-Grounded Dataset Comparison: An Alignment Angle Is All You Need (https://arxiv.org/abs/2603.10283v1)
- [arxiv:ax-2026-03-11-9] Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework (https://arxiv.org/abs/2603.10281v1)
- [arxiv:ax-2026-03-12-1] A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification (https://arxiv.org/abs/2603.10891v1)
- [arxiv:ax-2026-03-12-10] Contrastive learning-based video quality assessment-jointed video vision transformer for video recognition (https://arxiv.org/abs/2603.10965v1)
- [arxiv:ax-2026-03-12-11] Bridging the Skill Gap in Clinical CBCT Interpretation with CBCTRepD (https://arxiv.org/abs/2603.10933v1)
- [arxiv:ax-2026-03-12-12] Lifelong Imitation Learning with Multimodal Latent Replay and Incremental Adjustment (https://arxiv.org/abs/2603.10929v1)
- [arxiv:ax-2026-03-12-13] Novel Architecture of RPA In Oral Cancer Lesion Detection (https://arxiv.org/abs/2603.10928v1)
- [arxiv:ax-2026-03-12-14] S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs (https://arxiv.org/abs/2603.10893v1)
- [arxiv:ax-2026-03-12-15] Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation (https://arxiv.org/abs/2603.11045v1)
- [arxiv:ax-2026-03-12-16] Leech Lattice Vector Quantization for Efficient LLM Compression (https://arxiv.org/abs/2603.11021v1)
- [arxiv:ax-2026-03-12-17] Cross-Species Transfer Learning for Electrophysiology-to-Transcriptomics Mapping in Cortical GABAergic Interneurons (https://arxiv.org/abs/2603.11000v1)
- [arxiv:ax-2026-03-12-18] Factorized Neural Implicit DMD for Parametric Dynamics (https://arxiv.org/abs/2603.10995v1)
- [arxiv:ax-2026-03-12-19] MCMC Informed Neural Emulators for Uncertainty Quantification in Dynamical Systems (https://arxiv.org/abs/2603.10987v1)
- [arxiv:ax-2026-03-12-2] Instruction set for the representation of graphs (https://arxiv.org/abs/2603.11039v1)
- [arxiv:ax-2026-03-12-20] Federated Learning-driven Beam Management in LEO 6G Non-Terrestrial Networks (https://arxiv.org/abs/2603.10983v1)
- [arxiv:ax-2026-03-12-21] FRIEND: Federated Learning for Joint Optimization of multi-RIS Configuration and Eavesdropper Intelligent Detection in B5G Networks (https://arxiv.org/abs/2603.10977v1)
- [arxiv:ax-2026-03-12-22] TOSSS: a CVE-based Software Security Benchmark for Large Language Models (https://arxiv.org/abs/2603.10969v1)
- [arxiv:ax-2026-03-12-23] Ranking Reasoning LLMs under Test-Time Scaling (https://arxiv.org/abs/2603.10960v1)
- [arxiv:ax-2026-03-12-24] When should we trust the annotation? Selective prediction for molecular structure retrieval from mass spectra (https://arxiv.org/abs/2603.10950v1)
- [arxiv:ax-2026-03-12-25] Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk Control (https://arxiv.org/abs/2603.10938v1)
- [arxiv:ax-2026-03-12-26] Quantifying Membership Disclosure Risk for Tabular Synthetic Data Using Kernel Density Estimators (https://arxiv.org/abs/2603.10937v1)
- [arxiv:ax-2026-03-12-27] Historical Consensus: Preventing Posterior Collapse via Iterative Selection of Gaussian Mixture Priors (https://arxiv.org/abs/2603.10935v1)
- [arxiv:ax-2026-03-12-28] ECoLAD: Deployment-Oriented Evaluation for Automotive Time-Series Anomaly Detection (https://arxiv.org/abs/2603.10926v1)
- [arxiv:ax-2026-03-12-29] NCAA Bracket Prediction Using Machine Learning and Combinatorial Fusion Analysis (https://arxiv.org/abs/2603.10916v1)
- [arxiv:ax-2026-03-12-3] Beyond the Illusion of Consensus: From Surface Heuristics to Knowledge-Grounded Evaluation in LLM-as-a-Judge (https://arxiv.org/abs/2603.11027v1)
- [arxiv:ax-2026-03-12-30] Ergodicity in reinforcement learning (https://arxiv.org/abs/2603.10895v1)
- [arxiv:ax-2026-03-12-4] COMIC: Agentic Sketch Comedy Generation (https://arxiv.org/abs/2603.11048v1)
- [arxiv:ax-2026-03-12-5] V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation (https://arxiv.org/abs/2603.11042v1)
- [arxiv:ax-2026-03-12-6] Does AI See like Art Historians? Interpreting How Vision Language Models Recognize Artistic Style (https://arxiv.org/abs/2603.11024v1)
- [arxiv:ax-2026-03-12-7] Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity (https://arxiv.org/abs/2603.10990v1)
- [arxiv:ax-2026-03-12-8] GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations (https://arxiv.org/abs/2603.10978v1)
- [arxiv:ax-2026-03-12-9] Med-DualLoRA: Local Adaptation of Foundation Models for 3D Cardiac MRI (https://arxiv.org/abs/2603.10967v1)
- [arxiv:ax-2026-03-13-1] Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training (https://arxiv.org/abs/2603.12246v1)
- [arxiv:ax-2026-03-13-10] OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams (https://arxiv.org/abs/2603.12265v1)
- [arxiv:ax-2026-03-13-11] GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing (https://arxiv.org/abs/2603.12264v1)
- [arxiv:ax-2026-03-13-12] Video Streaming Thinking: VideoLLMs Can Watch and Think Simultaneously (https://arxiv.org/abs/2603.12262v1)
- [arxiv:ax-2026-03-13-13] DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning (https://arxiv.org/abs/2603.12257v1)
- [arxiv:ax-2026-03-13-14] Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training (https://arxiv.org/abs/2603.12255v1)
- [arxiv:ax-2026-03-13-15] EndoCoT: Scaling Endogenous Chain-of-Thought Reasoning in Diffusion Models (https://arxiv.org/abs/2603.12252v1)
- [arxiv:ax-2026-03-13-16] DVD: Deterministic Video Depth Estimation with Generative Priors (https://arxiv.org/abs/2603.12250v1)
- [arxiv:ax-2026-03-13-17] Trust Your Critic: Robust Reward Modeling and Reinforcement Learning for Faithful Image Editing and Generation (https://arxiv.org/abs/2603.12247v1)
- [arxiv:ax-2026-03-13-18] SceneAssistant: A Visual Feedback Agent for Open-Vocabulary 3D Scene Generation (https://arxiv.org/abs/2603.12238v1)
- [arxiv:ax-2026-03-13-19] HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers (https://arxiv.org/abs/2603.12222v1)
- [arxiv:ax-2026-03-13-2] Portfolio of Solving Strategies in CEGAR-based Object Packing and Scheduling for Sequential 3D Printing (https://arxiv.org/abs/2603.12224v1)
- [arxiv:ax-2026-03-13-20] A Two-Stage Dual-Modality Model for Facial Emotional Expression Recognition (https://arxiv.org/abs/2603.12221v1)
- [arxiv:ax-2026-03-13-21] Real-World Point Tracking with Verifier-Guided Pseudo-Labeling (https://arxiv.org/abs/2603.12217v1)
- [arxiv:ax-2026-03-13-22] RDNet: Region Proportion-Aware Dynamic Adaptive Salient Object Detection Network in Optical Remote Sensing Images (https://arxiv.org/abs/2603.12215v1)
- [arxiv:ax-2026-03-13-23] BehaviorVLM: Unified Finetuning-Free Behavioral Understanding with Vision-Language Reasoning (https://arxiv.org/abs/2603.12176v1)
- [arxiv:ax-2026-03-13-24] GlyphBanana: Advancing Precise Text Rendering Through Agentic Workflows (https://arxiv.org/abs/2603.12155v1)
- [arxiv:ax-2026-03-13-25] The Latent Color Subspace: Emergent Order in High-Dimensional Chaos (https://arxiv.org/abs/2603.12261v1)
- [arxiv:ax-2026-03-13-26] Separable neural architectures as a primitive for unified predictive and generative intelligence (https://arxiv.org/abs/2603.12244v1)
- [arxiv:ax-2026-03-13-27] Temporal Straightening for Latent Planning (https://arxiv.org/abs/2603.12231v1)
- [arxiv:ax-2026-03-13-28] Security Considerations for Artificial Intelligence Agents (https://arxiv.org/abs/2603.12230v1)
- [arxiv:ax-2026-03-13-29] Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights (https://arxiv.org/abs/2603.12228v1)
- [arxiv:ax-2026-03-13-3] Compiling Temporal Numeric Planning into Discrete PDDL+: Extended Version (https://arxiv.org/abs/2603.12188v1)
- [arxiv:ax-2026-03-13-30] A Quantitative Characterization of Forgetting in Post-Training (https://arxiv.org/abs/2603.12163v1)
- [arxiv:ax-2026-03-13-4] SciMDR: Benchmarking and Advancing Scientific Multimodal Document Reasoning (https://arxiv.org/abs/2603.12249v1)
- [arxiv:ax-2026-03-13-5] Sparking Scientific Creativity via LLM-Driven Interdisciplinary Inspiration (https://arxiv.org/abs/2603.12226v1)
- [arxiv:ax-2026-03-13-6] Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections (https://arxiv.org/abs/2603.12180v1)
- [arxiv:ax-2026-03-13-7] QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions (https://arxiv.org/abs/2603.12165v1)
- [arxiv:ax-2026-03-13-8] LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation (https://arxiv.org/abs/2603.12152v1)
- [arxiv:ax-2026-03-13-9] MM-CondChain: A Programmatically Verified Benchmark for Visually Grounded Deep Compositional Reasoning (https://arxiv.org/abs/2603.12266v1)
- [clawhub:ch-2026-03-09-1] EngageLab Omni Connect (https://clawhub.ai/GPTBOTS/engagelab-omni-connect)
- [clawhub:ch-2026-03-09-10] Tiger Trading (https://clawhub.ai/wjpwc/tiger-trading)
- [clawhub:ch-2026-03-09-11] Auto-Update (OpenClaw + Skills) (https://clawhub.ai/ivangdavila/auto-update)
- [clawhub:ch-2026-03-09-12] 土狗气象台 (https://clawhub.ai/Crime1000x/tugou-monitor)
- [clawhub:ch-2026-03-09-13] Subscription Sentinel (https://clawhub.ai/JoeySome/subscription-sentinel)
- [clawhub:ch-2026-03-09-14] Feishu At Mention (https://clawhub.ai/vision-qiu/feishu-at-mention)
- [clawhub:ch-2026-03-09-15] Founder Story Brand Narrative (https://clawhub.ai/RIJOYAI/founder-story-brand-narrative)
- [clawhub:ch-2026-03-09-16] wxauto (https://clawhub.ai/cluic/wxauto)
- [clawhub:ch-2026-03-09-17] 我的脑子 (https://clawhub.ai/z44264677/mind-layer)
- [clawhub:ch-2026-03-09-18] CCFI (https://clawhub.ai/jxzly/ccfi)
- [clawhub:ch-2026-03-09-19] WodeApp AI Engine (https://clawhub.ai/diankourenxia/wodeapp-ai)
- [clawhub:ch-2026-03-09-2] newsnow-reader (https://clawhub.ai/Castieler/newsnow-reader)
- [clawhub:ch-2026-03-09-20] 专业宠物（猫、狗及异宠）多轮医疗问诊 (https://clawhub.ai/zerojh/vetmew-consultation)
- [clawhub:ch-2026-03-09-21] codropshiping-product-search (https://clawhub.ai/shan-vvv/codropshiping-product-search)
- [clawhub:ch-2026-03-09-22] Small Goods Loyalty Incentives (https://clawhub.ai/RIJOYAI/small-goods-loyalty-incentives)
- [clawhub:ch-2026-03-09-23] user growth coach (https://clawhub.ai/Jack-Yang-ai/user-growth-coach)
- [clawhub:ch-2026-03-09-24] Human Stock Helper (https://clawhub.ai/MaxHou-infinity/human-stock-helper)
- [clawhub:ch-2026-03-09-25] Outlook Graph (https://clawhub.ai/c36025251-pixel/outlook-graph)
- [clawhub:ch-2026-03-09-3] Faithful Task Executor (https://clawhub.ai/endcy/faithful-task-executor)
- [clawhub:ch-2026-03-09-4] Waimai Merchant (https://clawhub.ai/harrylabs0913/waimai-merchant)
- [clawhub:ch-2026-03-09-5] NapCat QQ Bridge Installer (https://clawhub.ai/sunnyspot114514/napcat-qq-bridge-installer)
- [clawhub:ch-2026-03-09-6] Dev Progress Governor (https://clawhub.ai/Majmunu/dev-progress-governor)
- [clawhub:ch-2026-03-09-7] 发票查验(invoice-verify) - 慧穗云 (https://clawhub.ai/xiaoyierle/invoice-verify-hsy)
- [clawhub:ch-2026-03-09-8] Diagram Generator (https://clawhub.ai/LogicTortoise/anygen-diagram-generator)
- [clawhub:ch-2026-03-09-9] Financial Research (https://clawhub.ai/LogicTortoise/anygen-financial-research)
- [clawhub:ch-2026-03-10-1] 预测市场周报生成器 (https://clawhub.ai/hu4891/prediction-market-reporter)
- [clawhub:ch-2026-03-10-10] Guided Learning CN (https://clawhub.ai/ckchzh2022/guided-learning-cn)
- [clawhub:ch-2026-03-10-11] CatchClaw (https://clawhub.ai/Lovelcp/catch-claw)
- [clawhub:ch-2026-03-10-12] Nail B3g1 Promo (https://clawhub.ai/RIJOYAI/nail-b3g1-promo)
- [clawhub:ch-2026-03-10-13] Wechat File Helper (https://clawhub.ai/qidu/wechat-helper)
- [clawhub:ch-2026-03-10-14] 错敏信息检测（文本） (https://clawhub.ai/1227323804/sensitive-check-skill)
- [clawhub:ch-2026-03-10-15] Official Doc (https://clawhub.ai/ckchzh/official-doc)
- [clawhub:ch-2026-03-10-16] AI Opportunity Radar (https://clawhub.ai/itsukikuchiki/ai-opportunity-radar)
- [clawhub:ch-2026-03-10-17] Meegle Connector (https://clawhub.ai/wadxm/meegle-connector)
- [clawhub:ch-2026-03-10-18] raspberry-pi-camera-service (https://clawhub.ai/CLD1994/raspberry-pi-camera-service)
- [clawhub:ch-2026-03-10-19] ClickZetta Studio Agent (https://clawhub.ai/luketalent/studio-agent)
- [clawhub:ch-2026-03-10-2] CSDN 文章发布 (https://clawhub.ai/echome123/csdn-publish)
- [clawhub:ch-2026-03-10-20] AetherCore v3.3 (https://clawhub.ai/AetherClawAI/aetherclaw)
- [clawhub:ch-2026-03-10-21] Esign Automation (https://clawhub.ai/esign-cn-open-source/esign-automation)
- [clawhub:ch-2026-03-10-22] Ariadne Thread (https://clawhub.ai/in12hacker/ariadne-thread)
- [clawhub:ch-2026-03-10-23] Doubao ASR / 豆包语音转写 (https://clawhub.ai/vahnxu/doubao-asr)
- [clawhub:ch-2026-03-10-24] raspberry-pi-gpio (https://clawhub.ai/CLD1994/raspberry-pi-gpio)
- [clawhub:ch-2026-03-10-25] Jd Shopping (https://clawhub.ai/harrylabs0913/jd-ec)
- [clawhub:ch-2026-03-10-3] coding-agent (https://clawhub.ai/TSHOGX/tshogx-coding-agent)
- [clawhub:ch-2026-03-10-4] BinanceCoach (https://clawhub.ai/skills?q=binance-coach)
- [clawhub:ch-2026-03-10-5] Course Study (https://clawhub.ai/VincentJiang06/course-study)
- [clawhub:ch-2026-03-10-6] mlx-whisper (https://clawhub.ai/TSHOGX/tshogx-mlx-whisper)
- [clawhub:ch-2026-03-10-7] Flow Visual Explainer (https://clawhub.ai/windseeker1111/flow-visual-explainer)
- [clawhub:ch-2026-03-10-8] Bitrefill CLI (https://clawhub.ai/marcopesani/bitrefill-cli)
- [clawhub:ch-2026-03-10-9] API Gateway (https://clawhub.ai/byungkyu/api-gateway)
- [clawhub:ch-2026-03-12-1] Book Walker (https://clawhub.ai/YoungAndSure/book-walker)
- [clawhub:ch-2026-03-12-10] Mental Health Booking (https://clawhub.ai/gljirain/mental-health-booking)
- [clawhub:ch-2026-03-12-11] Quant-Expert (https://clawhub.ai/Noah-Wu66/quant-expert)
- [clawhub:ch-2026-03-12-12] PUA Debugging (日本語) (https://clawhub.ai/tanweai/pua-debugging-ja)
- [clawhub:ch-2026-03-12-13] Windows Execution Interface for OpenClaw (https://clawhub.ai/danzig233/clawdos)
- [clawhub:ch-2026-03-12-14] 小红书全栈采集专家 (https://clawhub.ai/Suzanneyp/xiaohongshu-expert)
- [clawhub:ch-2026-03-12-15] PUA Debugging (English) (https://clawhub.ai/tanweai/pua-debugging-en)
- [clawhub:ch-2026-03-12-16] PUA Debugging (https://clawhub.ai/tanweai/pua-debugging)
- [clawhub:ch-2026-03-12-17] Amazon Listing Factory (https://clawhub.ai/lenger666/amazon-listing-factory)
- [clawhub:ch-2026-03-12-18] Media.io AI Image & Video Generation API (https://clawhub.ai/wondershare-boop/mediaio-aigc-generate)
- [clawhub:ch-2026-03-12-19] Search Viewer (https://clawhub.ai/adminlove520/search-viewer)
- [clawhub:ch-2026-03-12-2] Buffy Agent (https://clawhub.ai/phantue2002/buffy-agent)
- [clawhub:ch-2026-03-12-20] AI Viral Trend Hijacker — Detect Any Trend & Produce Content Before It Peaks (https://clawhub.ai/g4dr/ai-viral-trend-hijacker)
- [clawhub:ch-2026-03-12-21] Provider Sync (https://clawhub.ai/C-Joey/provider-sync)
- [clawhub:ch-2026-03-12-22] tke-skill (https://clawhub.ai/archerlliu/tke-skill)
- [clawhub:ch-2026-03-12-23] Clawhub Skill Release Gate (https://clawhub.ai/chinasilva/clawhub-skill-release-gate)
- [clawhub:ch-2026-03-12-24] rollinggo-hotel (https://clawhub.ai/dreamtzlong/rollinggo-hotel)
- [clawhub:ch-2026-03-12-3] Giggle Generation Scripts (https://clawhub.ai/patches429/giggle-generation-scripts)
- [clawhub:ch-2026-03-12-4] Ot Security Posture Scorecard (https://clawhub.ai/krishnakumarmahadevan-cmd/ot-security-posture-scorecard)
- [clawhub:ch-2026-03-12-5] Dataset Evaluation (https://clawhub.ai/levey/dataset-evaluation)
- [clawhub:ch-2026-03-12-6] Claw Wiki (https://clawhub.ai/lueashes/claw-wiki)
- [clawhub:ch-2026-03-12-7] mac-wallpaper-changer (https://clawhub.ai/akayj/mwc)
- [clawhub:ch-2026-03-12-8] Giggle Generation Image (https://clawhub.ai/patches429/giggle-generation-image)
- [clawhub:ch-2026-03-12-9] Al Music Generation (https://clawhub.ai/IsDyh01/shortapi-ai-music-generation)
- [clawhub:ch-2026-03-13-1] Liber8 Career Agent (https://clawhub.ai/polyglyphanalytica/liber8)
- [clawhub:ch-2026-03-13-10] Runstr analytics (https://clawhub.ai/katla50/runstr-analytics)
- [clawhub:ch-2026-03-13-11] MX Fin Search (https://clawhub.ai/Financial-AI-Analyst/mx-finsearch)
- [clawhub:ch-2026-03-13-12] Slide Creator (https://clawhub.ai/kaisersong/html-slide-creator)
- [clawhub:ch-2026-03-13-13] Gws Gmail (https://clawhub.ai/googleworkspace-bot/gws-gmail)
- [clawhub:ch-2026-03-13-14] Memory Indexer (https://clawhub.ai/smallmj/memory-indexer)
- [clawhub:ch-2026-03-13-15] daily-report-bian (https://clawhub.ai/databian/daily-report-bian)
- [clawhub:ch-2026-03-13-16] Critic Agent (https://clawhub.ai/Wang-ErQian/critic-agent)
- [clawhub:ch-2026-03-13-17] Verified Agent Identity (https://clawhub.ai/OBrezhniev/verified-agent-identity)
- [clawhub:ch-2026-03-13-18] 发票识别(invoice-discern) - 慧穗云 (https://clawhub.ai/xiaoyierle/invoice-discern)
- [clawhub:ch-2026-03-13-19] Ai Image Prompts (https://clawhub.ai/DophinL/ai-image-prompts)
- [clawhub:ch-2026-03-13-2] 安全打卡提醒 (https://clawhub.ai/jayhe/dead-or-alive)
- [clawhub:ch-2026-03-13-20] 极速数据API汇总 - Summary of JisuAPI (https://clawhub.ai/jisuapi/jisu)
- [clawhub:ch-2026-03-13-21] Brave Browser (https://clawhub.ai/ivangdavila/brave)
- [clawhub:ch-2026-03-13-22] Gate Exchange Market Analysis (https://clawhub.ai/gate-exchange/gate-exchange-market-analysis)
- [clawhub:ch-2026-03-13-23] Giggle Generation Video (https://clawhub.ai/patches429/giggle-generation-video)
- [clawhub:ch-2026-03-13-24] ernie-integration (https://clawhub.ai/mattheliu/ernie-integration)
- [clawhub:ch-2026-03-13-25] intervals.icu CLI (https://clawhub.ai/jonaswide/intervals-icu-cli)
- [clawhub:ch-2026-03-13-3] Yidun Skill Sec (https://clawhub.ai/yd-dev/yidun-skill-sec)
- [clawhub:ch-2026-03-13-4] PaddleOCR Document Parsing (https://clawhub.ai/Bobholamovic/paddleocr-doc-parsing)
- [clawhub:ch-2026-03-13-5] openclaw intent router (https://clawhub.ai/ZhenStaff/openclaw-intent-router)
- [clawhub:ch-2026-03-13-6] 闲鱼自动回复助手 (https://clawhub.ai/sinabs/xianyu-auto-reply)
- [clawhub:ch-2026-03-13-7] Gate DEX Market (https://clawhub.ai/gate-exchange/gate-dex-market)
- [clawhub:ch-2026-03-13-8] IMA Studio All-in-One — Image, Video, Music, SeeDream, Veo, Suno. Banana (https://clawhub.ai/allenfancy-gan/ima-all-ai)
- [clawhub:ch-2026-03-13-9] ClawShow-Gateway-Connect (https://clawhub.ai/yudi-xiao/clawshow-gateway-connect)
- [github:gh-2026-03-09-1] Ed1s0nZ/CyberStrikeAI (https://github.com/Ed1s0nZ/CyberStrikeAI)
- [github:gh-2026-03-09-10] shareAI-lab/learn-claude-code (https://github.com/shareAI-lab/learn-claude-code)
- [github:gh-2026-03-09-2] is-a-dev/register (https://github.com/is-a-dev/register)
- [github:gh-2026-03-09-6] openai/skills (https://github.com/openai/skills)
- [github:gh-2026-03-09-8] teng-lin/notebooklm-py (https://github.com/teng-lin/notebooklm-py)
- [github:gh-2026-03-09-9] toeverything/AFFiNE (https://github.com/toeverything/AFFiNE)
- [github:gh-2026-03-10-1] pbakaus/impeccable (https://github.com/pbakaus/impeccable)
- [github:gh-2026-03-10-2] GoogleCloudPlatform/generative-ai (https://github.com/GoogleCloudPlatform/generative-ai)
- [github:gh-2026-03-10-5] virattt/ai-hedge-fund (https://github.com/virattt/ai-hedge-fund)
- [github:gh-2026-03-10-6] bytedance/deer-flow (https://github.com/bytedance/deer-flow)
- [github:gh-2026-03-10-9] promptfoo/promptfoo (https://github.com/promptfoo/promptfoo)
- [github:gh-2026-03-11-3] langflow-ai/openrag (https://github.com/langflow-ai/openrag)
- [github:gh-2026-03-11-4] vectorize-io/hindsight (https://github.com/vectorize-io/hindsight)
- [github:gh-2026-03-12-10] alibaba/page-agent (https://github.com/alibaba/page-agent)
- [github:gh-2026-03-12-6] 666ghj/MiroFish (https://github.com/666ghj/MiroFish)
- [github:gh-2026-03-12-8] msitarzewski/agency-agents (https://github.com/msitarzewski/agency-agents)
- [github:gh-2026-03-13-1] google-ai-edge/LiteRT (https://github.com/google-ai-edge/LiteRT)
- [github:gh-2026-03-13-11] google/A2UI (https://github.com/google/A2UI)
- [github:gh-2026-03-13-2] fishaudio/fish-speech (https://github.com/fishaudio/fish-speech)
- [github:gh-2026-03-13-5] NousResearch/hermes-agent (https://github.com/NousResearch/hermes-agent)
- [github:gh-2026-03-13-7] obra/superpowers (https://github.com/obra/superpowers)
- [github:gh-2026-03-13-9] InsForge/InsForge (https://github.com/InsForge/InsForge)
- [producthunt:ph-2026-03-09-1] Claude Marketplace (https://www.producthunt.com/products/claude-marketplace?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-10] Lazy Agent (https://www.producthunt.com/products/lazy-agent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-11] OGImagen (https://www.producthunt.com/products/ogimagen?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-12] OSS AI Hub (https://www.producthunt.com/products/oss-ai-hub?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-13] Sheeep (https://www.producthunt.com/products/sheeep?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-14] Agent Companion (https://www.producthunt.com/products/agent-companion?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-15] Osintly (https://www.producthunt.com/products/osintly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-16] Wedding Album Shortlister (https://www.producthunt.com/products/wedding-album-shortlister?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-17] Clawvatar (https://www.producthunt.com/products/clawvatar?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-18] Beacon (https://www.producthunt.com/products/beacon-18?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-19] Think & Write 30 - First Brain System (https://www.producthunt.com/products/think-write-30?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-2] Vibe Marketplace by Greta (https://www.producthunt.com/products/gretabyquestera?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-20] OrioSearch: Your AI Agent need WebSearch (https://www.producthunt.com/products/oriosearch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-21] Perfect Pitch - Game (https://www.producthunt.com/products/perfect-pitch-game?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-22] MacroLens (https://www.producthunt.com/products/macrolens-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-23] QuickDo — Voice Notes, Perfectly Written (https://www.producthunt.com/products/quickdo-voice-notes-perfectly-written?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-24] TempSnap iPhone Screenshot Cleaner (https://www.producthunt.com/products/tempsnap-iphone-screenshot-cleaner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-25] Tetr99 — The Free Tetris 99 Trainer (https://www.producthunt.com/products/tetr99-free-browser-block-puzzle-game?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-26] Nipun AI (https://www.producthunt.com/products/nipun-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-27] OrinCal - Calorie Tracker (https://www.producthunt.com/products/orincal-calorie-tracker?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-28] willaigetyourjob (https://www.producthunt.com/products/willaigetyourjob?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-29] TimePulse (https://www.producthunt.com/products/timepulse?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-3] GetMimic (https://www.producthunt.com/products/getmimic?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-30] Walletvy: AI Expense & Budget (https://www.producthunt.com/products/walletvy-ai-expense-budget?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-4] Pulldog (https://www.producthunt.com/products/pulldog?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-5] Soloron (https://www.producthunt.com/products/soloron?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-6] DossierPrêt (https://www.producthunt.com/products/dossierpret?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-7] HotelPriceTrack (https://www.producthunt.com/products/hotelpricetrack?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-8] Motionsites (https://www.producthunt.com/products/motionsites?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-09-9] FDA Data MCP (https://www.producthunt.com/products/fda-data-mcp?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-1] Roundtable (https://www.producthunt.com/products/joinroundtable?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-10] Hannah & Co (https://www.producthunt.com/products/hannah-co-your-ai-marketing-coworkers?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-11] Phi-4-reasoning-vision (https://www.producthunt.com/products/phi-4-reasoning?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-12] Reflct (https://www.producthunt.com/products/reflct?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-13] Flowripple (https://www.producthunt.com/products/flowripple-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-14] Wideframe (https://www.producthunt.com/products/wideframe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-15] SubSchool (https://www.producthunt.com/products/subschool?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-16] Revolink: Smart Multi-Path Links (https://www.producthunt.com/products/revolink?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-17] granthOS (https://www.producthunt.com/products/granthos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-18] Interviewkit AI (https://www.producthunt.com/products/interviewkit-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-19] AI Shipped (https://www.producthunt.com/products/ai-shipped?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-2] Dex (https://www.producthunt.com/products/dex-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-20] NeuralAgent 2.0 Skills (https://www.producthunt.com/products/neuralagent?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-21] agentpng.dev (https://www.producthunt.com/products/agentpng-dev?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-22] TypeMyself (https://www.producthunt.com/products/typemyself?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-23] State of Decentralized AI 2026 (https://www.producthunt.com/products/state-of-decentralized-ai-2026-2027?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-24] Trending Now (https://www.producthunt.com/products/ads-research?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-25] Converleon — All-in-one file converter (https://www.producthunt.com/products/converleon-all-in-one-mac-converter?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-26] ClauseOps (https://www.producthunt.com/products/clauseops?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-27] Skynet Platform (https://www.producthunt.com/products/skynet-closed-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-28] Lap photo manager (https://www.producthunt.com/products/lap-photo-manager?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-29] StartStopWatch (https://www.producthunt.com/products/startstopwatch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-3] SCRAPR (https://www.producthunt.com/products/scrapr-universal-web-scraping-api?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-30] Autonomous Incident Reports & Fixes (https://www.producthunt.com/products/prodrescue-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-4] simply (https://www.producthunt.com/products/simply-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-5] BrandingStudio.ai (https://www.producthunt.com/products/brandingstudio-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-6] Unite Pro for macOS (https://www.producthunt.com/products/unite-for-macos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-7] Nothing Phone (4a) Pro (https://www.producthunt.com/products/nothing-phone-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-8] OpenClix (https://www.producthunt.com/products/openclix-smarter-mobile-engagement?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-10-9] cutefolio (https://www.producthunt.com/products/cutefolio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-1] Chronicle 2.0 (https://www.producthunt.com/products/chronicle-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-10] Sonarly (https://www.producthunt.com/products/sonarly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-11] Microsoft Copilot Cowork (https://www.producthunt.com/products/copilot-cowork?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-12] humans fix ai (https://www.producthunt.com/products/humans-fix-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-13] Refero MCP (https://www.producthunt.com/products/refero?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-14] CodeGuide (https://www.producthunt.com/products/codeguide-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-15] Book Reading Habit (https://www.producthunt.com/products/book-reading-habit?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-16] Contentdrips Design Agent (https://www.producthunt.com/products/contentdrips?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-17] Shipper 2.0 (https://www.producthunt.com/products/shipper-now?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-18] Brutal Reader (https://www.producthunt.com/products/brutal-reader?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-19] Decoy (https://www.producthunt.com/products/decoy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-2] Visual Translate by Vozo (https://www.producthunt.com/products/vozo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-20] SuperSend 3.0 (https://www.producthunt.com/products/super-send?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-21] VENTUNO Q (https://www.producthunt.com/products/arduino?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-22] On Demand Ads by beehiv (https://www.producthunt.com/products/beehiiv?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-23] Zappic.co (https://www.producthunt.com/products/zappic-co?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-24] Accountable Finance (https://www.producthunt.com/products/accountable-finance?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-25] VizPy (https://www.producthunt.com/products/vizpy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-26] dreaming.press (https://www.producthunt.com/products/dreaming-press?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-27] WordPress to Webflow CSV Exporter (https://www.producthunt.com/products/exporter-for-webflow?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-28] HoverTime (https://www.producthunt.com/products/hovertime?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-29] Rentaclaw (https://www.producthunt.com/products/rentaclaw?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-3] Claude Code Review (https://www.producthunt.com/products/claude?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-30] Cult UI (https://www.producthunt.com/products/cult-ui?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-4] Your Next Store (https://www.producthunt.com/products/your-next-store?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-5] Fish Audio S2 (https://www.producthunt.com/products/fish-speech?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-6] sitefire.ai (https://www.producthunt.com/products/sitefire-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-7] New Macaly Agent (https://www.producthunt.com/products/macaly?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-8] Agent Skills (https://www.producthunt.com/products/agent-skills-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-11-9] Spine Swarm (https://www.producthunt.com/products/spine-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-1] InsForge (https://www.producthunt.com/products/insforge-alpha?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-10] MorphMind: A Steerable AI Platform (https://www.producthunt.com/products/morphmind-launches-steerable-ai-platform?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-11] ChatGPT Interactive Learning (https://www.producthunt.com/products/chatgpt-interactive-learning?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-12] Mindspase (https://www.producthunt.com/products/mindspase?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-13] CodeYam CLI & Memory (https://www.producthunt.com/products/codeyam-cli-memory?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-14] TADA (https://www.producthunt.com/products/hume-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-15] Nativeline AI + Cloud (https://www.producthunt.com/products/nativeline?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-16] ELVES (https://www.producthunt.com/products/no-more-vibe-coding-in-the-blind?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-17] Typinator 10 (https://www.producthunt.com/products/typinator-10?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-18] Product Workbench for Claude Code (https://www.producthunt.com/products/chordio-workbench?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-19] ScreenGeany AI (https://www.producthunt.com/products/screengeany-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-2] Cardboard (https://www.producthunt.com/products/cardboard-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-20] HypeScribe (https://www.producthunt.com/products/hypescribe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-21] Fort (https://www.producthunt.com/products/fort-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-22] Health Data Avatar (https://www.producthunt.com/products/health-data-avatar?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-23] Taskip (https://www.producthunt.com/products/taskip?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-24] Runable (https://www.producthunt.com/products/runable-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-25] EarlyCore (https://www.producthunt.com/products/earlycore?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-26] cvcomp (https://www.producthunt.com/products/cvcomp?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-27] Flato (https://www.producthunt.com/products/flato-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-28] PostGod (https://www.producthunt.com/products/postgod?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-29] Eventrise (https://www.producthunt.com/products/eventrise?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-3] Teract AI (https://www.producthunt.com/products/teract?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-30] Plotresume (https://www.producthunt.com/products/plotresume?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-4] OpenUI (https://www.producthunt.com/products/thesys?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-5] Knowlify (https://www.producthunt.com/products/knowlify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-6] Gemini Embedding 2 (https://www.producthunt.com/products/gemini-embedding-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-7] Firecrawl CLI (https://www.producthunt.com/products/extract-by-firecrawl?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-8] IonRouter (https://www.producthunt.com/products/ionrouter-by-cumulus-labs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-12-9] Citable (https://www.producthunt.com/products/citable?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-1] Naoma AI Demo Agent (https://www.producthunt.com/products/naoma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-10] OrangeLabs (https://www.producthunt.com/products/orangelabs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-11] AskNeo (https://www.producthunt.com/products/askneo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-12] Donna AI (https://www.producthunt.com/products/donna-ai-agent-to-agent-hiring-platform?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-13] Flywheel.cx (https://www.producthunt.com/products/flywheel-cx?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-14] Agent Browser (https://www.producthunt.com/products/agent-browser-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-15] Coresignal Data Search (https://www.producthunt.com/products/coresignal?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-16] Email API benchmarks (https://www.producthunt.com/products/knock-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-17] Airpoint (https://www.producthunt.com/products/airpoint?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-18] Clawcard (https://www.producthunt.com/products/clawcard?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-19] Outhop (https://www.producthunt.com/products/outhop?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-2] Needle 2.0 (https://www.producthunt.com/products/needle-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-20] Clayzo (https://www.producthunt.com/products/clayzo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-21] Basement Browser (https://www.producthunt.com/products/basement-browser?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-22] Casero (https://www.producthunt.com/products/casero?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-23] oobo (https://www.producthunt.com/products/ooboai-oobo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-24] LaunchSafe (https://www.producthunt.com/products/launchsafe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-25] Megaton Monitor (https://www.producthunt.com/products/megaton-monitor?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-26] muno (https://www.producthunt.com/products/muno-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-27] Skayle (https://www.producthunt.com/products/skayle?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-28] Pushary (https://www.producthunt.com/products/pushary?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-29] Astrio (https://www.producthunt.com/products/astrio-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-3] HTML Pub (https://www.producthunt.com/products/htmlpub?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-30] Birdhouse (https://www.producthunt.com/products/birdhouse?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-4] Runner AI (https://www.producthunt.com/products/runner-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-5] Huddle01 Cloud (https://www.producthunt.com/products/huddle01-cloud-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-6] Clawther (https://www.producthunt.com/products/clawther?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-7] Prava (https://www.producthunt.com/products/prava-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-8] Raccoon AI (https://www.producthunt.com/products/raccoon-ai-cursor-for-anything?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
- [producthunt:ph-2026-03-13-9] Gauge (https://www.producthunt.com/products/gauge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+Agent+%28ID%3A+266065%29)
