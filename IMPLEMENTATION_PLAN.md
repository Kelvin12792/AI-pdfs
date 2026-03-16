# IMPLEMENTATION_PLAN.md — Phased Implementation Plan

## Philosophy

This plan is designed to get Kelvin M from zero to a published first edition as fast as possible, without skipping any foundational step that would cause problems later. Every phase has a clear goal, a defined set of tasks, and a clear deliverable that signals the phase is complete.

**Production approach:** PDF 01 pilot first. Validate everything. Then scale.

---

## Phase 0 — Environment Setup
**Goal:** Working technical environment, all tools installed, all files in place  
**Estimated time:** 2–4 hours  
**Prerequisite for:** Everything else

### Tasks

- [ ] **0.1** Create project directory structure exactly as specified in CLAUDE.md
  ```
  kelvin_ai_series/
  ├── source/
  ├── cleaned/
  ├── structured/
  ├── assets/covers/
  ├── assets/diagrams/
  ├── assets/fonts/
  ├── output/
  └── scripts/
  ```

- [ ] **0.2** Install Python 3.10+ (verify: `python3 --version`)

- [ ] **0.3** Create and activate Python virtual environment
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- [ ] **0.4** Install all Python dependencies
  ```bash
  pip install reportlab pypdf Pillow pyyaml markdown
  ```

- [ ] **0.5** Verify all dependencies installed correctly
  ```bash
  python -c "import reportlab, pypdf, PIL, yaml, markdown; print('All OK')"
  ```

- [ ] **0.6** Download Inter font family from Google Fonts (all 5 weights)
  - Inter-Regular.ttf
  - Inter-Medium.ttf
  - Inter-SemiBold.ttf
  - Inter-Bold.ttf
  - Inter-Italic.ttf
  - Save all to `assets/fonts/`

- [ ] **0.7** Initialise git repository
  ```bash
  git init
  git add .
  git commit -m "project: initial setup — all canonical docs created"
  ```

- [ ] **0.8** Create GitHub private repository and push
  ```bash
  git remote add origin https://github.com/[username]/kelvin-ai-series.git
  git push -u origin main
  ```

- [ ] **0.9** Set up Midjourney account (if not already active)

- [ ] **0.10** Decide and confirm: series name — choose from proposals before proceeding

**Phase 0 complete when:** All directories exist, all dependencies installed, fonts downloaded, git initialised, series name confirmed

---

## Phase 1 — Content Pipeline Setup
**Goal:** Raw Twitter content cleaned, verified, and mapped to curriculum  
**Estimated time:** 3–6 hours  
**Prerequisite for:** Phase 2

### Tasks

- [ ] **1.1** Paste all 60+ raw Twitter posts into `source/raw_tweets_batch01_2026-03.txt`

- [ ] **1.2** Write `scripts/clean_tweets.py` — script that:
  - Strips @usernames
  - Strips #hashtags
  - Strips timestamps and dates
  - Strips engagement metrics (likes, retweets, replies)
  - Strips URLs (unless URL is the subject)
  - Labels each item [TWEET] or [THREAD]
  - Flags items with statistics as [FACT-CHECK]
  - Outputs to `cleaned/cleaned_batch01_2026-03.txt`

- [ ] **1.3** Run `clean_tweets.py` on the raw file. Review output manually.

- [ ] **1.4** Manually fact-check every [FACT-CHECK] flagged item:
  - Verify against reliable source, or
  - Remove the claim if unverifiable
  - Document all verified sources in `cleaned/sources_batch01.md`

- [ ] **1.5** Save verified cleaned file as `cleaned/cleaned_batch01_2026-03_verified.txt`

- [ ] **1.6** Read all cleaned content and manually group by topic cluster:
  - AI basics / What is AI
  - Machine Learning
  - LLMs / ChatGPT
  - AI tools & productivity
  - AI ethics & safety
  - AI and jobs
  - AI in education
  - AI in business
  - Deep learning

- [ ] **1.7** Create `structured/curriculum_map.md` — assign each content item to its target edition number

- [ ] **1.8** Confirm Edition 01 (What is AI?) has enough verified content to write a full chapter

- [ ] **1.9** Log completion in CHANGELOG.md

**Phase 1 complete when:** `structured/curriculum_map.md` exists with all 60+ content items assigned to edition numbers

---

## Phase 2 — PDF 01 Draft (Pilot Edition)
**Goal:** Complete draft of Edition 01 — "What is AI?"  
**Estimated time:** 4–8 hours  
**Prerequisite for:** Phase 3

### Tasks

- [ ] **2.1** Create directory `structured/edition_01_what-is-ai/`

- [ ] **2.2** Develop Kelvin's personal AI analogy — the one real-life comparison that will anchor Edition 01's hook. (Craft together — this is the soul of the first impression)

- [ ] **2.3** Write Edition 01 draft following BUILD_FLOW.md Stage 4 exactly:
  - 2.3a — Hook / Aha moment (personal analogy, 150–250 words)
  - 2.3b — Learning objectives (3–5 bullet points)
  - 2.3c — Table of contents
  - 2.3d — Body Section 1: What is AI? (with example + [DIAGRAM] placeholder + callout)
  - 2.3e — Body Section 2: How is AI different from regular software? (with comparison table)
  - 2.3f — Body Section 3: Where do you already encounter AI? (step-by-step practical section)
  - 2.3g — Key takeaways (3–5 standalone sentences, each a potential video one-liner)
  - 2.3h — Glossary (every technical term defined)
  - 2.3i — Mini quiz (exactly 10 questions: 3 MCQ + 2 T/F + 2 FIB + 3 SA)
  - 2.3j — Reflection question (Edition 01 = Personal)
  - 2.3k — CTA block (all 6 CTAs)
  - 2.3l — Next edition teaser (Edition 02: "How AI Thinks")

- [ ] **2.4** Save as `structured/edition_01_what-is-ai/draft.md`

- [ ] **2.5** Save answer key as `structured/edition_01_what-is-ai/answer_key.md`

- [ ] **2.6** Check draft against SERIES_BIBLE.md:
  - No forbidden phrases
  - Voice and tone correct
  - Viral elements present (hook sentence, one-liners, arc, cliffhanger)
  - Word count within 1,200–2,500 word range

- [ ] **2.7** Kelvin reviews and approves draft

- [ ] **2.8** Save approved draft as `structured/edition_01_what-is-ai/draft_approved.md`

- [ ] **2.9** Log completion in CHANGELOG.md

**Phase 2 complete when:** `draft_approved.md` exists and Kelvin has signed off on content

---

## Phase 3 — Asset Production (Edition 01)
**Goal:** Cover art and all body diagrams ready for Edition 01  
**Estimated time:** 2–4 hours  
**Prerequisite for:** Phase 4

### Tasks

- [ ] **3.1** Generate Edition 01 cover art using Midjourney
  - Use prompt template from IMAGE_STRATEGY.md
  - Edition 01 prompt: brain/neural nodes, coral and cream palette, no text, no people
  - Upscale to 2480 × 3508px
  - Save as `assets/covers/edition_01_cover.png`

- [ ] **3.2** Write `scripts/build_diagram.py` — reusable Pillow diagram generator

- [ ] **3.3** Build all diagrams specified in `draft_approved.md`:
  - Identify all `[DIAGRAM: ...]` placeholders
  - Build each diagram using correct diagram type from IMAGE_STRATEGY.md
  - Save each as `assets/diagrams/edition_01_diagram_{N}.png`

- [ ] **3.4** Quality check all assets against IMAGE_STRATEGY.md quality checklist

- [ ] **3.5** Log completion in CHANGELOG.md

**Phase 3 complete when:** All cover and diagram PNGs exist, quality-checked, correctly named

---

## Phase 4 — PDF Build (Edition 01)
**Goal:** Production-quality PDF for Edition 01  
**Estimated time:** 4–8 hours  
**Prerequisite for:** Phase 5

### Tasks

- [ ] **4.1** Write `scripts/build_pdf.py`:
  - Reads STYLE_TOKENS.yaml for all design values
  - Assembles all sections in correct page order
  - Applies all callout box, table, heading, footer styles
  - Inserts cover art and diagrams
  - Embeds PDF metadata
  - Exports to `output/`

- [ ] **4.2** Run build script for Edition 01
  - Output: `output/edition_01_what-is-ai_v1.0.pdf`

- [ ] **4.3** QA pass:
  - Open on smartphone — readable?
  - Open on laptop — layout correct?
  - Print page 1 — crisp?
  - All fonts embedded?
  - File size under 10MB?
  - All images render correctly?

- [ ] **4.4** Fix any issues and rebuild — version as `v1.1`, `v1.2` etc. until QA passes

- [ ] **4.5** Final approved build saved as `output/edition_01_what-is-ai_v1.0.pdf`

- [ ] **4.6** Confirm: is the video script section needed? (Decision deferred to pilot review) — decide now and add if needed

- [ ] **4.7** Log completion in CHANGELOG.md

**Phase 4 complete when:** QA-approved PDF exists at `output/edition_01_what-is-ai_v1.0.pdf`

---

## Phase 5 — Pilot Review & Series Confirmation
**Goal:** Validate the pilot edition before scaling to the full series  
**Estimated time:** 1–2 hours  
**Prerequisite for:** Phase 6

### Tasks

- [ ] **5.1** Kelvin reviews the complete PDF — does it feel right?
- [ ] **5.2** Confirm or update: series name decision
- [ ] **5.3** Confirm or update: video script section format (full script vs bullet points)
- [ ] **5.4** Confirm or update: PDF access model (free / email capture / paid / mixed)
- [ ] **5.5** Confirm or update: video presenter format (on camera / voiceover / AI avatar)
- [ ] **5.6** Update STYLE_TOKENS.yaml if any design adjustments needed
- [ ] **5.7** Update SERIES_BIBLE.md if any voice/tone adjustments needed
- [ ] **5.8** Rebuild Edition 01 if changes require it
- [ ] **5.9** Sign off: "Series template approved — ready to scale"
- [ ] **5.10** Log all decisions in CHANGELOG.md

**Phase 5 complete when:** Kelvin has signed off on Edition 01 as the validated template for the full series

---

## Phase 6 — Distribution Setup & Edition 01 Launch
**Goal:** Edition 01 live on all platforms, Kelvin's channels set up for distribution  
**Estimated time:** 3–5 hours  
**Prerequisite for:** Phase 7

### Tasks

- [ ] **6.1** Create Selar account and product listing for Edition 01
- [ ] **6.2** Create Gumroad account and product listing for Edition 01
- [ ] **6.3** Run through DISTRIBUTION_CHECKLIST.md for Selar — upload Edition 01
- [ ] **6.4** Run through DISTRIBUTION_CHECKLIST.md for Gumroad — upload Edition 01
- [ ] **6.5** Decide: KDP listing needed for Edition 01? If yes, run KDP checklist
- [ ] **6.6** Set up WhatsApp group or broadcast list for distribution
- [ ] **6.7** Set up Telegram channel for distribution
- [ ] **6.8** Prepare LinkedIn announcement post
- [ ] **6.9** Prepare Twitter/X thread
- [ ] **6.10** Prepare Instagram post and story
- [ ] **6.11** Prepare email newsletter announcement (if list exists)
- [ ] **6.12** Publish Edition 01 on all channels simultaneously
- [ ] **6.13** Update EDITION_REGISTRY.md — mark Edition 01 as [PUBLISHED]
- [ ] **6.14** Log launch in CHANGELOG.md

**Phase 6 complete when:** Edition 01 is live and publicly accessible

---

## Phase 7 — Series Scaling (Editions 02–20+)
**Goal:** Maintain bi-weekly release cadence for the full series  
**Ongoing from:** 2 weeks after Edition 01 launch

### Recurring Production Cycle (Repeat for each edition)

For each new edition, repeat Phases 2–6 using the validated template from the pilot:

**Week 1 of each 2-week cycle:**
- [ ] Pull content from `structured/curriculum_map.md` for the target edition
- [ ] Write draft (BUILD_FLOW.md Stage 4)
- [ ] Editorial review (BUILD_FLOW.md Stage 5)
- [ ] Generate cover art and diagrams (BUILD_FLOW.md Stage 6)

**Week 2 of each 2-week cycle:**
- [ ] Build PDF (BUILD_FLOW.md Stage 7)
- [ ] QA pass (BUILD_FLOW.md Stage 8)
- [ ] Upload to platforms (DISTRIBUTION_CHECKLIST.md)
- [ ] Publish and announce on all channels
- [ ] Update EDITION_REGISTRY.md and CHANGELOG.md

### Scaling Milestones

| Milestone | Target Date | Goal |
|-----------|-------------|------|
| Edition 01 published | TBD | Pilot live |
| Edition 05 published | TBD + 8 weeks | Foundational arc complete |
| 100 sales | TBD + ~30 days | Month 1 business goal |
| Edition 10 published | TBD + 18 weeks | Core Concepts arc complete |
| Edition 20 published | TBD + 38 weeks | Full initial series complete |
