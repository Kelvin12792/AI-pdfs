# CHANGELOG.md — Build Log

## How to Use This File

Every decision, change, and build event must be logged here. No exceptions. Log in reverse chronological order — newest entry at the top.

**Entry format:**
```
## [YYYY-MM-DD] — {Stage}: {Edition or Project Level}
**What changed:** {Description}
**Why:** {Reason}
**Decision made by:** Kelvin M
```

---

## Log

---

## [2026-03-17] — Stage 7: Edition 01 Expanded Build v2.0

**What changed:**
1. **Expanded build script** — `scripts/build_pdf_01.py` rewritten with all 10 diagrams integrated (previously only 2). Script expanded from ~1190 lines to ~1575 lines.
2. **Added 6 new content sections** — Types of AI (Narrow/General/Super pyramid), Brief History of AI (timeline table), How AI Actually Learns (5-step process), Myths vs Reality (5 myth/reality pairs), AI as Multiplier (amplification framing), Your AI Learning Path (4-level progression).
3. **Built Edition 01 v2.0 PDF** — 21-page production PDF at `output/edition_01_what-is-ai_v2.0.pdf` (0.79 MB). All 10 Pillow-generated diagrams placed with captions. All Inter fonts embedded.
4. **New visual elements** — Added pull quote style, section divider helper, and section intro style for richer page layout.
5. **Added glossary terms** — "Model" and "Narrow AI" added to glossary (11 terms total, up from 9).
6. **Updated EDITION_REGISTRY.md** — Edition 01 output filename and notes updated to reflect v2.0.

**Why:** The v1.0 build used only 2 of 10 available diagrams and covered 5 body sections. The expanded v2.0 integrates all diagram assets and adds sections that better prepare readers for the rest of the series (AI types, history, learning process, myths, multiplier concept, learning path).

**New files created:**
- `output/edition_01_what-is-ai_v2.0.pdf`

**Files updated:**
- `scripts/build_pdf_01.py` (expanded build with all 10 diagrams)
- `EDITION_REGISTRY.md` (Edition 01 updated to v2.0)
- `CHANGELOG.md` (this entry)

**Decision made by:** Kelvin M

---

## [2026-03-17] — Stage 6-7: Edition 01 Asset Production + PDF Build

**What changed:**
1. **Generated 2 body diagrams** — `assets/diagrams/edition_01_diagram_01.png` (Regular Software vs AI comparison flowchart, 1960x900px) and `assets/diagrams/edition_01_diagram_02.png` (Three Convergences timeline, 1960x1000px). Both generated with Python + Pillow at 300 DPI using exact STYLE_TOKENS.yaml colors and Inter font family.
2. **Created cover page** — Programmatic cover with AI network node illustration (no external image dependency), dark overlay text band with series name, edition title, tagline, and author line per DESIGN_GUIDELINES.md.
3. **Built Edition 01 PDF** — 14-page production PDF at `output/edition_01_what-is-ai_v1.0.pdf` (0.27 MB). All content expanded with detailed explanations integrating source material from Posts 10, 24, 27, 52, and supporting posts. All Inter fonts embedded. Follows STYLE_TOKENS.yaml for colors, spacing, typography. Includes all required sections per BUILD_FLOW.md Stage 4.
4. **Created build scripts** — `scripts/build_diagrams_01.py` and `scripts/build_pdf_01.py` for reproducible builds.
5. **Downloaded Inter font family** — All 5 weights (Regular, Medium, SemiBold, Bold, Italic) saved to `assets/fonts/`.
6. **Updated EDITION_REGISTRY.md** — Edition 01 status changed from [DRAFTED] to [BUILT].
7. **Created Edition 01 outline** — `structured/edition_01_what-is-ai/outline.md` with section-by-section breakdown, source post mappings, asset requirements, and viral readiness checklist.

**Why:** First complete PDF production run for the pilot edition. Validates the full build pipeline from draft content through diagram generation to final PDF output.

**New files created:**
- `output/edition_01_what-is-ai_v1.0.pdf`
- `assets/diagrams/edition_01_diagram_01.png`
- `assets/diagrams/edition_01_diagram_02.png`
- `assets/fonts/Inter-*.ttf` (5 files)
- `scripts/build_diagrams_01.py`
- `scripts/build_pdf_01.py`
- `structured/edition_01_what-is-ai/outline.md`

**Files updated:**
- `EDITION_REGISTRY.md` (Edition 01 status: [DRAFTED] → [BUILT])
- `CHANGELOG.md` (this entry)

**Decision made by:** Kelvin M

---

## [2026-03-17] — Fix: Batch 2 Edition Assignment Mismatch + Stage 4: Edition 01 Draft

**What changed:**
1. **Fixed batch 2 edition assignments** — All 38 posts in batch 2 (Posts 30–68) had incorrect edition names that did not match the established curriculum map and edition registry. For example, Edition 07 was labeled "Getting Started with AI Tools" instead of the correct "Neural Networks Explained"; Edition 14 was labeled "AI-Powered Marketing" instead of "AI in Healthcare." All edition references in `cleaned/master_cleaned_tweets.md` and `cleaned/cleaned_batch2_part0.md` through `cleaned/cleaned_batch2_part5.md` have been corrected to use the canonical edition titles from `EDITION_REGISTRY.md`.
2. **Created Edition 01 draft** — Full chapter draft for "What is AI?" following BUILD_FLOW.md Stage 4 exactly. Includes: hook/aha moment opener (predictive text analogy), 5 learning objectives, 5 body sections (definition, daily life examples, AI vs regular software, why now, try-it-yourself), key takeaways, 9-term glossary, 10-question quiz (3 MCQ + 2 T/F + 2 FIB + 3 SA), personal reflection question, all 6 CTAs, and next edition teaser with cliffhanger.
3. **Created answer key** — `structured/edition_01_what-is-ai/answer_key.md` with all quiz answers.
4. **Updated topic file** — Added batch 2 content (Post 52) to `structured/topics/01_what_is_ai.md`.
5. **Updated EDITION_REGISTRY.md** — Edition 01 status changed from [PLANNED] to [DRAFTED] with draft date 2026-03-17.

**Why:** Batch 2 content was cleaned using an alternative edition naming scheme that diverged from the canonical curriculum map established during batch 1 processing. This created inconsistency across the project. The correction ensures all files reference the same edition titles. The Edition 01 draft is the pilot chapter required before scaling to the full series.

**New files created:**
- `structured/edition_01_what-is-ai/draft.md`
- `structured/edition_01_what-is-ai/answer_key.md`

**Files updated:**
- `cleaned/master_cleaned_tweets.md` (38 edition assignment corrections)
- `cleaned/cleaned_batch2_part0.md` through `cleaned/cleaned_batch2_part5.md` (edition assignment corrections)
- `structured/topics/01_what_is_ai.md` (batch 2 content added)
- `EDITION_REGISTRY.md` (Edition 01 status updated)
- `CHANGELOG.md` (this entry)

**Decision made by:** Kelvin M

---

## [2026-03-16] — Infrastructure: Persistent Reference System + Topic Categories + Language Patterns

**What changed:**
1. Created `cleaned/master_cleaned_tweets.md` — persistent running file that accumulates all cleaned tweet content across all batches. Auto-updated every time a new batch is processed. Single source of truth for all source material.
2. Created 20 topic category files in `structured/topics/` (01–20), each containing assigned content from Batch 1, research-based additions, key analogies, quotable one-liners, and content gap analysis. Organized by hierarchy: Foundational (01–05) → Core Concepts (06–10) → Applications (11–15) → Advanced & Critical (16–20).
3. Updated `SERIES_BIBLE.md` with new "Source Language Patterns" section — captures the writing style, cadence, and energy of the source tweets for use in PDF writing. Includes patterns to adopt (direct address, analogy-first, numbers/specificity, conversational rhythm) and patterns to avoid (slang, hashtag language, unverified hype).
4. Updated `BUILD_FLOW.md` with new Stage 0.5 (Persistent Reference Update) — auto-triggered after every cleaning batch to update master file and route content to topic files.

**Why:** Kelvin requested a system that (a) keeps a running cleaned-tweets reference file updated with every batch, (b) auto-categorizes content into topic hierarchies, (c) captures the tweet language patterns for PDF voice, and (d) scales cleanly as new batches arrive.

**New files created:**
- `cleaned/master_cleaned_tweets.md`
- `structured/topics/01_what_is_ai.md` through `structured/topics/20_using_ai_responsibly.md` (20 files)

**Files updated:**
- `SERIES_BIBLE.md` (added Source Language Patterns section)
- `BUILD_FLOW.md` (added Stage 0.5)
- `CHANGELOG.md` (this entry)

**Decision made by:** Kelvin M

---

## [2026-03-16] — Planning: Project Level
**What changed:** Completed full 38-question planning interrogation. All canonical documentation files generated: CLAUDE.md, PRD.md, BUILD_FLOW.md, TECH_STACK.md, SERIES_BIBLE.md, DESIGN_GUIDELINES.md, STYLE_TOKENS.yaml, IMAGE_STRATEGY.md, EDITION_REGISTRY.md, DISTRIBUTION_CHECKLIST.md, CHANGELOG.md, IMPLEMENTATION_PLAN.md  
**Why:** Project kickoff — establishing zero-ambiguity foundation before any content production begins  
**Decisions locked:**
- Author: Kelvin M, AI Educator & Researcher
- Audience: Complete beginners, all ages 13–40+
- Tone: Academic but accessible
- Sequencing: Complexity-based (simple → advanced)
- Format: Portrait A4
- Color palette: Anthropic brand
- Release cadence: Bi-weekly
- Production approach: PDF 01 pilot first
- Series goal: 100 sales in month 1
- Reader feeling: Awakened
- Gap being filled: Step-by-step practical AI applications

**Decisions still open:**
- Series name (proposals pending)
- Video presenter format
- PDF access model (free / paid / mixed)
- PDF update policy
- Kelvin's personal AI analogy

**Decision made by:** Kelvin M

---

<!-- All future entries go above this line, newest first -->
