# ClawHub Skills Daily | 2026-09-17

> 共 25 个 skills

## [1. illustrated-story-reel](https://clawhub.ai/pruna-ai/illustrated-story-reel)

**Slug**: `illustrated-story-reel`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1146 | 🧩 11

**原始简介**: Use when someone wants a slideshow story with narration or music — picture-book illustrated frames with Ken Burns or gentle p-video motion.

**中文介绍**: Use when someone wants a slideshow story with narration or music — picture-book illustrated frames with Ken Burns or gentle p-video motion.

Latest changelog:
illustrated-story-reel 1.0.13

- Updated prerequisites: clarified descriptions for `p-video-2` and `p-video`, including limits on use (cinematic audio, 1080p, talking-head).
- Removed the file skill-card.md.
- No functional changes to workflow, gates, or intake questions.
- Internal documentation streamlined and improved clarity.

**关键词**: illustrated-story-reel, Use, when, someone, wants, slideshow, story, narration

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/illustrated-story-reel)

---

## [2. pruna](https://clawhub.ai/pruna-ai/pruna)

**Slug**: `pruna`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 765 | 🧩 7

**原始简介**: Use when installing the full Pruna generative media suite — all guides, tools, and workflows in one package.

**中文介绍**: Use when installing the full Pruna generative media suite — all guides, tools, and workflows in one package.

Latest changelog:
- Added new dependency: p-video-2-pro (for cinematic clip generation).
- Updated dependencies list and tool descriptions to include p-video-2-pro and clarify roles for p-video-2 and p-video.
- Bumped version to 1.0.13.
- Removed the file: skill-card.md.

**关键词**: pruna, Use, when, installing, full, generative, media, suite

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pruna)

---

## [3. music-video](https://clawhub.ai/skills?q=music-video)

**Slug**: `music-video`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1285 | 🧩 12

**原始简介**: Use when someone wants a full music video — original song or vocals, performance clips, B-roll, and lyric-synced edits.

**中文介绍**: Use when someone wants a full music video — original song or vocals, performance clips, B-roll, and lyric-synced edits.

Latest changelog:
music-video v1.0.13

- Clarified prerequisites with detailed installation steps for dependent skills.
- Updated workflow guidance, including mandatory naming and phase gate protocol in every reply.
- Enhanced intake and continuity guidance, emphasizing character consistency and cast handling.
- Provided explicit phase workflows and generation phase gates for user approval checkpoints.
- Linked reference resources, QA checklist, and model routing for different host types.
- Improved instructions for managing generation diversity and video assembly flow.

**关键词**: music-video, Use, when, someone, wants, full, music, video

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/music-video)

---

## [4. interactive-explainer](https://clawhub.ai/pruna-ai/interactive-explainer)

**Slug**: `interactive-explainer`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1157 | 🧩 11

**原始简介**: Use when someone wants an educational explainer with a host and characters — history or science shorts with dialogue, not voiceover-only B-roll.

**中文介绍**: Use when someone wants an educational explainer with a host and characters — history or science shorts with dialogue, not voiceover-only B-roll.

Latest changelog:
Version 1.0.13

- Updated SKILL.md with clarified descriptions for `p-video` and `p-video-2`, specifying use cases and output limitations.
- Removed the outdated skill-card.md file.
- No changes to workflow, feedback gates, or technical defaults.

**关键词**: an, interactive-explainer, Use, when, someone, wants, educational, explainer

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/interactive-explainer)

---

## [5. avatar-multi-scene](https://clawhub.ai/pruna-ai/avatar-multi-scene)

**Slug**: `avatar-multi-scene`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1201 | 🧩 11

**原始简介**: Use when someone wants the same person hosting several clips — multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

**中文介绍**: Use when someone wants the same person hosting several clips — multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

Latest changelog:
avatar-multi-scene 1.0.13

- Updated SKILL.md metadata to version 1.0.13.
- Removed the skill-card.md file.
- No changes to core features or workflow; documentation cleanup only.

**关键词**: avatar-multi-scene, Use, when, someone, wants, same, person, hosting

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/avatar-multi-scene)

---

## [6. drivethru-payable-matching](https://clawhub.ai/zmtucker/drivethru-payable-matching)

**Slug**: `drivethru-payable-matching`  
**Version**: 0.9.3  
**Stats**: ⭐ 0 | ⬇️ 1056 | 🧩 13

**原始简介**: Payable matching for BaconCo — reconcile vendor documents in Odoo's Documents app against their purchase orders and correct incorrect PO line pricing. Use for requests like "check the Purchasing folder against the POs and fix the pricing", "match the vendor invoice / order confirmation / acknowledgement to its PO", "AP price matching / invoice-to-PO matching / three-way match", "reconcile the vendor documents and mark the POs checked", or "go through the Purchasing folder". The flow: read every document in a Documents-app folder (extracting text out-of-context so large batches don't bloat the context window — falling back to a page render + OCR/vision for scanned or custom-encoded PDFs that won't extract as text), pull the PO number / line items / unit prices from each, compare to the purchase order line by line, correct any wrong `price_unit`, post a "checked" log note on the PO (internal, never a "Send message"), and FILE every document into the `Matched` or `Questions` subfolder — escalating genuine questions to a reviewer (default Zach Tucker). Also runs the buying-group payables flow: pull Sports Inc invoices from the SportsLink API (via the `sportsinc-sportslink` adapter), reconcile each to its PO, correct price variances, create the vendor bill and — when the bill total matches the invoice within tolerance — POST it, leaving any mismatch in draft for a human ("get the Sports Inc invoices and bill them", "match the SI invoices to POs and post the payables", "match the vendor invoice and post the bill if it matches"). Handles the multi-shipment case where one PO returns several Sports Inc invoices, splitting it into one vendor bill per shipment via `account.move.line` edits (the `ap_*_bill_line(s)` tools). Runs at volume on a low-cost model. Driven by the Odoo `drivethru_mcp` MCP server; complements the broader `drivethru-odoo` skill.

**中文介绍**: Payable matching for BaconCo — reconcile vendor documents in Odoo's Documents app against their purchase orders and correct incorrect PO line pricing. Use for requests like "check the Purchasing folder against the POs and fix the pricing", "match the vendor invoice / order confirmation / acknowledgement to its PO", "AP price matching / invoice-to-PO matching / three-way match", "reconcile the vendor documents and mark the POs checked", or "go through the Purchasing folder". The flow: read every document in a Documents-app folder (extracting text out-of-context so large batches don't bloat the context window — falling back to a page render + OCR/vision for scanned or custom-encoded PDFs that won't extract as text), pull the PO number / line items / unit prices from each, compare to the purchase order line by line, correct any wrong `price_unit`, post a "checked" log note on the PO (internal, never a "Send message"), and FILE every document into the `Matched` or `Questions` subfolder — escalating genuine questions to a reviewer (default Zach Tucker). Also runs the buying-group payables flow: pull Sports Inc invoices from the SportsLink API (via the `sportsinc-sportslink` adapter), reconcile each to its PO, correct price variances, create the vendor bill and — when the bill total matches the invoice within tolerance — POST it, leaving any mismatch in draft for a human ("get the Sports Inc invoices and bill them", "match the SI invoices to POs and post the payables", "match the vendor invoice and post the bill if it matches"). Handles the multi-shipment case where one PO returns several Sports Inc invoices, splitting it into one vendor bill per shipment via `account.move.line` edits (the `ap_*_bill_line(s)` tools). Runs at volume on a low-cost model. Driven by the Odoo `drivethru_mcp` MCP server; complements the broader `drivethru-odoo` skill.

Latest changelog:
drivethru-payable-matching 0.9.3

- Updated version to 0.9.3.
- Documentation and metadata updates in SKILL.md; no functional changes to documented features.
- No user-facing changes in scripts/paymatch.py.

**关键词**: Payable, matching, BaconCo, reconcile, vendor, documents, Odoo's, app

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/drivethru-payable-matching)

---

## [7. drivethru-odoo](https://clawhub.ai/zmtucker/drivethru-odoo)

**Slug**: `drivethru-odoo`  
**Version**: 0.9.2  
**Stats**: ⭐ 0 | ⬇️ 1734 | 🧩 11

**原始简介**: Talk to an Odoo ERP through its `drivethru_mcp` MCP server — discover the available Odoo tools at runtime and call them to look up eBay products/inventory, push eBay orders and read tracking, run the Accounts Payable PO→vendor-bill flow, review documents in the Documents app against their purchase orders and fix incorrect PO line pricing (the "check the Purchasing folder against the POs" / vendor-invoice pricing-review workflow, filing each document into Matched or Questions), schedule MRP production batches, drive vendor replenishment purchasing (run the replenishment report → curate lines → add to a PO → hand style/color/size/qty to the vendor's purchasing skill → write pricing + confirmation back and confirm the PO), and retrieve internal SOPs / best practices / policies from the Knowledge base scoped to the asking person's permissions. Use whenever the user needs to read from or write to Odoo, especially when you are answering a person inside an Odoo Discuss conversation.

**中文介绍**: Talk to an Odoo ERP through its `drivethru_mcp` MCP server — discover the available Odoo tools at runtime and call them to look up eBay products/inventory, push eBay orders and read tracking, run the Accounts Payable PO→vendor-bill flow, review documents in the Documents app against their purchase orders and fix incorrect PO line pricing (the "check the Purchasing folder against the POs" / vendor-invoice pricing-review workflow, filing each document into Matched or Questions), schedule MRP production batches, drive vendor replenishment purchasing (run the replenishment report → curate lines → add to a PO → hand style/color/size/qty to the vendor's purchasing skill → write pricing + confirmation back and confirm the PO), and retrieve internal SOPs / best practices / policies from the Knowledge base scoped to the asking person's permissions. Use whenever the user needs to read from or write to Odoo, especially when you are answering a person inside an Odoo Discuss conversation.

Latest changelog:
drivethru-odoo 0.9.2

- Updated SKILL.md version to 0.9.2 with minor metadata changes.
- Removed obsolete skill-card.md file.
- Minor internal updates to scripts/odoo_mcp.py (details not specified).

**关键词**: an, drivethru-odoo, Talk, Odoo, ERP, through, its, drivethru

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/drivethru-odoo)

---

## [8. visual-transition-reel](https://clawhub.ai/pruna-ai/visual-transition-reel)

**Slug**: `visual-transition-reel`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1162 | 🧩 12

**原始简介**: Use when someone wants a montage with transitions between shots — action-sequence reel or multi-scene piece where narration is optional.

**中文介绍**: Use when someone wants a montage with transitions between shots — action-sequence reel or multi-scene piece where narration is optional.

Latest changelog:
visual-transition-reel 1.0.13

- Updated skill dependencies and workflow to include the new `p-video-2-pro` for advanced cinematic video transitions.
- Clarified video skill selection: use `p-video-2-pro` for cinematic reels, `p-video-2` for 1080p or imported audio, and `p-video` for simpler clips.
- Adjusted guide language for video formats and audio track options.
- Removed the legacy `skill-card.md` documentation file.

**关键词**: visual-transition-reel, Use, when, someone, wants, montage, transitions, between

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/visual-transition-reel)

---

## [9. avatar-single-scene](https://clawhub.ai/pruna-ai/avatar-single-scene)

**Slug**: `avatar-single-scene`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1162 | 🧩 11

**原始简介**: Use when someone wants one polished host-on-camera beat — a speaking person with intake and approval gates before generation.

**中文介绍**: Use when someone wants one polished host-on-camera beat — a speaking person with intake and approval gates before generation.

Latest changelog:
- Version bump to 1.0.13.
- Documentation update in SKILL.md; version and content refined.
- skill-card.md file removed.

**关键词**: avatar-single-scene, Use, when, someone, wants, one, polished, host-on-camera

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/avatar-single-scene)

---

## [10. narrated-multi-scene](https://clawhub.ai/pruna-ai/narrated-multi-scene)

**Slug**: `narrated-multi-scene`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1203 | 🧩 12

**原始简介**: Use when someone wants a multi-part story with voiceover — episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue.

**中文介绍**: Use when someone wants a multi-part story with voiceover — episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue.

Latest changelog:
- Updated to version 1.0.13.
- Refined video skill descriptions for `p-video-2` and `p-video` in the prerequisites table, clarifying quality and audio support.
- Removed the `skill-card.md` file.

**关键词**: narrated-multi-scene, Use, when, someone, wants, multi-part, story, voiceover

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/narrated-multi-scene)

---

## [11. image-to-video](https://clawhub.ai/skills?q=image-to-video)

**Slug**: `image-to-video`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 315 | 🧩 11

**原始简介**: Use when someone wants one short film beat from images — a narrated scene, story moment, or cinematic B-roll with optional voiceover.

**中文介绍**: Use when someone wants one short film beat from images — a narrated scene, story moment, or cinematic B-roll with optional voiceover.

Latest changelog:
image-to-video 1.0.13

- Clarified intake questions, workflow stages, and agent behaviors for all video generation modes.
- Refined prerequisites and related skill handoff instructions.
- Expanded feedback gates and approval checkpoints to ensure review before each generation stage.
- Updated skill boundary to enforce one-scene-only use, with gating for longer projects.
- Detailed instructions for narration, stills creation, and optional background bed.
- Improved media handling, generation diversity, and delivery formatting guidance.

**关键词**: image-to-video, Use, when, someone, wants, one, short, film

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/image-to-video)

---

## [12. whisperx](https://clawhub.ai/skills?q=whisperx)

**Slug**: `whisperx`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 250 | 🧩 12

**原始简介**: Use when someone needs word-level timestamps from audio — lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video-editing.

**中文介绍**: Use when someone needs word-level timestamps from audio — lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video-editing.

Latest changelog:
- Adds detailed usage documentation to SKILL.md, including installation instructions, prerequisites, agent habits, and workflow integration.
- Clarifies required and optional input parameters for audio transcription and alignment.
- Defines specific scenarios when to use or not use this skill, with alternative recommendations.
- Provides environmental setup and typical next steps in a music-video production pipeline.

**关键词**: whisperx, Use, when, someone, needs, word-level, timestamps, audio

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/whisperx)

---

## [13. music-2.5](https://clawhub.ai/pruna-ai/music-2-5)

**Slug**: `music-2-5`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1126 | 🧩 11

**原始简介**: Use when someone wants an original AI song with vocals — sung lyrics, a style prompt track, or source audio for a music video.

**中文介绍**: Use when someone wants an original AI song with vocals — sung lyrics, a style prompt track, or source audio for a music video.

Latest changelog:
music-2-5 1.0.13 changelog:

- Updated SKILL.md with an incremented version and minor instruction/prompt tweaks.
- Improved `p-video` follow-on skill description for more precise guidance.
- Removed skill-card.md from the repository.

**关键词**: an, music-2.5, Use, when, someone, wants, original, song

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/music-2-5)

---

## [14. stable-audio-2.5](https://clawhub.ai/pruna-ai/stable-audio-2-5)

**Slug**: `stable-audio-2-5`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1163 | 🧩 12

**原始简介**: Use when someone wants light instrumental background music — an ambient bed under dialogue or underscore for reels and explainers.

**中文介绍**: Use when someone wants light instrumental background music — an ambient bed under dialogue or underscore for reels and explainers.

Latest changelog:
Stable-audio-2-5 v1.0.13

- Version updated to 1.0.13 in SKILL.md metadata.
- Removed redundant skill-card.md file.
- No changes to usage, features, or user workflow.

**关键词**: stable-audio-2.5, Use, when, someone, wants, light, instrumental, background

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stable-audio-2-5)

---

## [15. gemini-3.1-flash-tts](https://clawhub.ai/pruna-ai/gemini-3-1-flash-tts)

**Slug**: `gemini-3-1-flash-tts`  
**Version**: 1.0.13  
**Stats**: ⭐ 1 | ⬇️ 1157 | 🧩 11

**原始简介**: Use when someone needs spoken narration or voiceover — explainer tracks, documentary lines, or voice to pair with generated video.

**中文介绍**: Use when someone needs spoken narration or voiceover — explainer tracks, documentary lines, or voice to pair with generated video.

Latest changelog:
- Bumped version to 1.0.13.
- Updated the "Typical next steps" section for `p-video` to clarify use cases, adding more detail on limitations and suitable scenarios.
- Removed the redundant skill-card.md file.

**关键词**: or, gemini-3.1-flash-tts, Use, when, someone, needs, spoken, narration

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gemini-3-1-flash-tts)

---

## [16. p-video-replace](https://clawhub.ai/pruna-ai/p-video-replace)

**Slug**: `p-video-replace`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1219 | 🧩 13

**原始简介**: Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

**中文介绍**: Use when someone wants to swap a person, outfit, or product inside existing footage while keeping the camera move and audio.

Latest changelog:
- Version bump to 1.0.13.
- Documentation cleanup: removed outdated file `skill-card.md`.
- Updated SKILL.md metadata to reflect new version.
- No functional or interface changes to the skill itself.

**关键词**: p-video-replace, Use, when, someone, wants, swap, person, outfit

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-replace)

---

## [17. Workbuddy Usage Status](https://clawhub.ai/clancy-feng/workbuddy-usage-status)

**Slug**: `workbuddy-usage-status`  
**Version**: 1.4.1  
**Stats**: ⭐ 0 | ⬇️ 1000 | 🧩 13

**原始简介**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

**中文介绍**: 离线可视化 WorkBuddy 本机使用数据，以 token 消耗为主指标、credit 为本地估算，涵盖思考效率、模型分布与性价比、日期区间筛选、错误监控、用量高峰探查，生成本地使用信息看板。仅当用户**明确**想查看、生成或导出**自己 WorkBuddy 本机/本账号**的使用状态 / 使用统计 / 工作信...

Latest changelog:
v1.4.1:Enhancement for security audit.

**关键词**: 离线可视化, 本机使用数据, 消耗为主指标、credit, 为本地估算, Workbuddy, Usage, Status, token

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/workbuddy-usage-status)

---

## [18. p-video-edit](https://clawhub.ai/pruna-ai/p-video-edit)

**Slug**: `p-video-edit`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 211 | 🧩 3

**原始简介**: Use when someone wants to edit an existing video with a text instruction — recolor, restyle, remove or add objects, change environment or lighting, update on-screen text, or apply optional reference-guided product and accessory edits. Not for a new clip from scratch or ffmpeg assembly.

**中文介绍**: Use when someone wants to edit an existing video with a text instruction — recolor, restyle, remove or add objects, change environment or lighting, update on-screen text, or apply optional reference-guided product and accessory edits. Not for a new clip from scratch or ffmpeg assembly.

Latest changelog:
p-video-edit 1.0.13

- Updated guidance in SKILL.md for "When NOT to use" with latest recommended related skills, including new skill options and target use-cases.
- Removed redundant skill-card.md file.

**关键词**: an, p-video-edit, Use, when, someone, wants, edit, existing

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-edit)

---

## [19. p-video-avatar](https://clawhub.ai/pruna-ai/p-video-avatar)

**Slug**: `p-video-avatar`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1163 | 🧩 12

**原始简介**: Use when someone wants a person on camera speaking a script — lip-synced host, spokesperson, or narrated avatar from a portrait photo.

**中文介绍**: Use when someone wants a person on camera speaking a script — lip-synced host, spokesperson, or narrated avatar from a portrait photo.

Latest changelog:
- Updated skill suggestions in "When NOT to use": replaced `p-video-2` with new `p-video-2-pro` and clarified distinctions between video generation skills.
- Improved descriptions for similar skills to help users choose the correct workflow.
- No changes to API usage or primary workflow guidance.
- Removed `skill-card.md` file.

**关键词**: p-video-avatar, Use, when, someone, wants, person, camera, speaking

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-avatar)

---

## [20. p-video-animate](https://clawhub.ai/pruna-ai/p-video-animate)

**Slug**: `p-video-animate`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1168 | 🧩 12

**原始简介**: Use when someone wants a photo to move like another video — motion transfer, dance remixes, or performance variations from a template clip.

**中文介绍**: Use when someone wants a photo to move like another video — motion transfer, dance remixes, or performance variations from a template clip.

Latest changelog:
p-video-animate 1.0.13

- Updated SKILL.md version to 1.0.13 and related metadata.
- Removed redundant skill-card.md file to streamline documentation.
- No changes to functionality or user-facing behavior.

**关键词**: p-video-animate, Use, when, someone, wants, photo, move, like

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-animate)

---

## [21. p-video](https://clawhub.ai/pruna-ai/p-video)

**Slug**: `p-video`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1188 | 🧩 12

**原始简介**: Use when someone wants a simple short clip from text or images — quick B-roll, drafts, or start/end frame animation. Not when the brief needs cinematic generation, highest quality, tight lip-sync, or imported audio at 1080p.

**中文介绍**: Use when someone wants a simple short clip from text or images — quick B-roll, drafts, or start/end frame animation. Not when the brief needs cinematic generation, highest quality, tight lip-sync, or imported audio at 1080p.

Latest changelog:
**Expanded routing and clarified boundaries for p-video.**

- Improved the description and warnings to clarify when to use or route away from `p-video`, especially for cinematic, 1080p, and imported audio needs.
- Updated agent routing: direct cinematic generation with audio to `p-video-2-pro`; 1080p/imported audio/drafts to `p-video-2`.
- Added and adjusted "When NOT to use" section with new options (`p-video-2-pro`, updated `p-video-2`), with sharper role descriptions.
- Removed deprecated documentation file (`skill-card.md`).

**关键词**: p-video, Use, when, someone, wants, simple, short, clip

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video)

---

## [22. p-video-2](https://clawhub.ai/pruna-ai/p-video-2)

**Slug**: `p-video-2`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 103 | 🧩 2

**原始简介**: Use when someone wants a polished short clip from text, images, or imported audio — 1080p B-roll, start/end frame animation, or a motion shot with a mixed track. Not for cinematic generated-audio clips or talking-head-only hosts.

**中文介绍**: Use when someone wants a polished short clip from text, images, or imported audio — 1080p B-roll, start/end frame animation, or a motion shot with a mixed track. Not for cinematic generated-audio clips or talking-head-only hosts.

Latest changelog:
- Clarified the distinction between `p-video-2` and the new `p-video-2-pro` skill, including routing and feature differences (cinematic/HD, generated/imported audio).
- Updated skill boundaries and "When NOT to use" to direct cinematic or generated-audio use cases to `p-video-2-pro`.
- Refined the skill description to emphasize 1080p clips, imported audio support, and not for fully cinematic or talking-head clips.
- Minor guidance improvements for prompt craft and agent workflow.
- Removed redundant or legacy documentation file (`skill-card.md`).

**关键词**: p-video-2, Use, when, someone, wants, polished, short, clip

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-2)

---

## [23. p-image-try-on](https://clawhub.ai/pruna-ai/p-image-try-on)

**Slug**: `p-image-try-on`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1252 | 🧩 12

**原始简介**: Use when someone wants virtual try-on — dress a person in clothes from reference photos for fashion or ecommerce.

**中文介绍**: Use when someone wants virtual try-on — dress a person in clothes from reference photos for fashion or ecommerce.

Latest changelog:
p-image-try-on version 1.0.13

- Updated SKILL.md to version 1.0.13 with no major content changes.
- Removed skill-card.md file.
- Minor maintenance and metadata version bump.
- No changes to APIs, functionality, or user-facing behaviors.

**关键词**: p-image-try-on, Use, when, someone, wants, virtual, try-on, dress

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-image-try-on)

---

## [24. p-video-2-pro](https://clawhub.ai/pruna-ai/p-video-2-pro)

**Slug**: `p-video-2-pro`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Use when someone wants a cinematic clip from text or start/end frames — product ads, documentary shots, or dialogue with generated audio. Not for 1080p, imported audio tracks, or talking-head-only hosts.

**中文介绍**: Use when someone wants a cinematic clip from text or start/end frames — product ads, documentary shots, or dialogue with generated audio. Not for 1080p, imported audio tracks, or talking-head-only hosts.

Latest changelog:
p-video-2-pro v1.0.13 changelog:

- Clarified scope and agent habits for routing requests between video generation skills.
- Expanded prerequisites and setup instructions for required supporting skills.
- Refined prompt crafting guidance with detailed dos and don'ts, focusing on cinematic generation with generated audio.
- Updated "When NOT to use" section for clearer redirection to other video generation and editing skills.
- Consolidated and streamlined usage instructions and out-of-scope scenarios.

**关键词**: p-video-2-pro, Use, when, someone, wants, cinematic, clip, text

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-video-2-pro)

---

## [25. p-image-upscale](https://clawhub.ai/pruna-ai/p-image-upscale)

**Slug**: `p-image-upscale`  
**Version**: 1.0.13  
**Stats**: ⭐ 0 | ⬇️ 1173 | 🧩 12

**原始简介**: Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

**中文介绍**: Use when someone wants to upscale or sharpen an existing image for print, large crops, or higher-quality delivery.

Latest changelog:
- Bump version to 1.0.13.
- Remove redundant skill-card.md file.
- No functional or API changes; documentation-only update.

**关键词**: or, p-image-upscale, Use, when, someone, wants, upscale, sharpen

**评分**: 0

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/p-image-upscale)

---

