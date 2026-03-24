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

## [2026-03-21] — Book Naming and Cover Design Decisions Confirmed

**What changed:**
1. **Book title confirmed:** "The AI Basics Nobody Made Clear" with subtitle "A Beginner's Guide to AI."
2. **Cover layout confirmed:** Keeping existing 60/40 structure (60% abstract illustration, 40% dark text band). Cover text elements updated from series format (series name + edition title + tagline) to book format (title + subtitle + author).
3. **Cover image style confirmed:** Abstract conceptual illustration, coral and cream palette, flat minimal design, no people, no text in image.
4. **Updated PRD.md** with confirmed product name (was "To be confirmed").
5. **Updated DESIGN_GUIDELINES.md** cover section with new text elements.
6. **Updated STYLE_TOKENS.yaml** cover section with title, subtitle, and author text values.
7. **Created assets/covers/COVER_BRIEF.md** with four Midjourney prompt options, two DALL-E 3 fallback prompts, post-generation checklist, and recommended approach.

**Why:** The product has evolved from a series of standalone PDFs to a 15-chapter book. The naming and cover design needed to reflect this shift. Title chosen by Kelvin M for its directness and alignment with the reader's frustration ("nobody made this clear before").

**Decision made by:** Kelvin M

---

## [2026-03-21] — Stage 4: Edition 01 Chapters 13-15 Written — Book Complete

**What changed:**
1. **Wrote Chapter 13 — Your AI Starter Toolkit.** 30-day learning path (week-by-week from first conversation to permanent habit), five habits of effective AI users, six common beginner mistakes, personal AI learning journal framework with step-by-step setup and example table. Sources: Posts 24 (beginner advice, 5 tips), 11 (30-day roadmap concepts), 43 (performative productivity/mistakes), 60 (productivity habits), 10 (don't keep up with everything), 12 (using vs reading about AI).
2. **Wrote Chapter 14 — The Ethics of AI: Bias, Privacy, and Your Responsibility.** Megaphone analogy (Post 27) as central frame. AI bias with three verified case studies (Amazon recruiting 2018, US hospital algorithm racial disparities, criminal justice risk assessment tools). Privacy checklist for AI users. Deepfakes and misinformation (2024 NH robocall case). Fairness and access gap. Five-question ethical responsibility framework. Sources: Post 27 (ethical judgment, megaphone/multiplier concept). Primarily external verified knowledge — source posts were thin on ethics content.
3. **Wrote Chapter 15 — Where You Go from Here.** Closing chapter bringing all 14 prior chapters together. Three core principles (AI amplifies you, tools change but skills don't, start before you're ready). Recap comparison table (what most people believe vs what the reader now knows). Five concrete next steps. Final word on human relevance in the age of AI.
4. **All 15 chapters of Edition 01 are now complete.** Book is ready for editorial review, asset production, and PDF build.

**Why:** Completing the full 15-chapter book as planned. Chapters 14-15 were written with minimal source post material (ethics content was thin across all 68 posts) and relied primarily on verified external knowledge anchored by Post 27's megaphone/multiplier framing.

**Decision made by:** Kelvin M

---

## [2026-03-18] — Stage 4: Edition 01 Chapters 6-10 Written + Chapter 9 Pivot

**What changed:**
1. **Wrote Chapter 6 — The Three Reasons AI Exploded Now.** Covers the convergence of data (2 ZB in 2010 to 220+ ZB in 2026), computing power (NVIDIA GPU history from 1993 gaming startup through CUDA 2006 to AI supercomputers, AlexNet 2012), and methods (deep learning, Transformer architecture 2017). Full timeline table 1956-2026. Web-researched GPU history and global data statistics. Sources: Posts 11, 16, 52.
2. **Wrote Chapter 7 — AI Tools You Can Try Today.** Four tool categories (chat, image, writing, productivity). Deep profiles of ChatGPT, Claude, Gemini with 2026 features/pricing. Image tools (DALL-E, Microsoft Designer, Adobe Firefly, Ideogram). AI in everyday software (Google Search, Microsoft 365 Copilot, Apple Intelligence, Gmail). 13-tool comparison table. "Patient teacher" concept. Sources: Posts 24, 2, 1, 50, 12. All tool info web-researched for 2026 accuracy.
3. **Wrote Chapter 8 — Your First AI Conversation — Step by Step.** 10-step walkthrough from account creation to saving conversations. Search engine vs AI comparison table. Restaurant analogy (Post 5). Quiet room principle (Post 6). Three-part prompt formula intro (Post 50). Five starter prompts. Troubleshooting six bad-answer scenarios. Sources: Posts 24, 12, 5, 6, 4.
4. **Pivoted Chapter 9 from "What AI Gets Right" to "How to Talk to AI — The Art of Prompting"** per Kelvin's direction. Deep prompt engineering dive: Context/Task/Rules formula (Post 50), seven techniques (role assignment, few-shot prompting, chain-of-thought, output formatting, revision loop, constraints, task decomposition), five before/after prompt transformations, six common mistakes. Sources: Posts 5, 6, 50, 8, 4, 62. Web-researched for 2026 prompt engineering best practices.
5. **Wrote Chapter 10 — What AI Gets Wrong.** Six limitations with verified evidence: hallucination (five real court cases 2023-2025, Anthropic 2025 circuit research), bias (Amazon hiring, iTutorGroup $365K EEOC settlement, MIT Gender Shades, healthcare disparities), no real understanding (Chinese Room adapted as "Translation Room"), logic/math struggles, no cross-conversation memory, training data cutoff. First Pancake Principle (Post 8). Three-step fact-checking framework. Sources: Posts 4, 11, 27, 8, 68.
6. **Fixed Chapter 8 teaser** to point to the new Chapter 9 (prompt engineering) instead of the original "What AI Gets Right."
7. **Updated expanded_outline.md** — All 10 chapters marked [WRITTEN], Chapter 9 entry fully rewritten to reflect the prompt engineering pivot, Chapter 10 entry fully rewritten with verified content summary, chapter status summary table added.

**Why:** Continuing the chapter-by-chapter writing process for Edition 01's expanded 15-chapter book format. Chapter 9 pivot creates a stronger pedagogical arc: tools (Ch7) → first use (Ch8) → mastering prompts (Ch9) → understanding limitations (Ch10). The original Ch9 AI strengths content remains available for later chapters or future editions.

**New files created:**
- `structured/edition_01_what-is-ai/chapter_06.md`
- `structured/edition_01_what-is-ai/chapter_07.md`
- `structured/edition_01_what-is-ai/chapter_08.md`
- `structured/edition_01_what-is-ai/chapter_09.md`
- `structured/edition_01_what-is-ai/chapter_10.md`

**Files updated:**
- `structured/edition_01_what-is-ai/expanded_outline.md` (Ch1-10 marked [WRITTEN], Ch9 + Ch10 entries rewritten, status summary added)
- `structured/edition_01_what-is-ai/chapter_08.md` (teaser fixed for Ch9 pivot)
- `CHANGELOG.md` (this entry)
- `EDITION_REGISTRY.md` (Edition 01 status updated)
- `IMPLEMENTATION_PLAN.md` (progress updated)

**Decision made by:** Kelvin M

---

## [2026-03-18] — Stage 4: Edition 01 Chapters 1-5 Written + Expanded Outline Created

**What changed:**
1. **Created expanded_outline.md** — Full 15-chapter book outline for Edition 01 expanding from the original 5-section draft to a ~150-page book. Each chapter mapped to specific source posts with detailed content descriptions, callout box assignments, and diagram placeholders. Front matter (6 pages) and back matter (8 pages) specified.
2. **Wrote Chapter 1 — You Already Use AI.** Morning routine AI touchpoints, 15+ daily AI examples, adoption statistics (Post 52), "you are absurdly early" reassurance. Sources: Posts 10, 52, 12, 6.
3. **Wrote Chapter 2 — What AI Actually Means.** One-sentence definition, child learning cats analogy, examples → patterns → predictions framework, three AI task types (recognise, predict, generate), feedback loop (Post 3), what AI is NOT. Sources: Posts 10, 27, 3, 6.
4. **Wrote Chapter 3 — AI vs. Regular Software.** Calculator vs AI comparison, thermostat vs smart home, 10-dimension comparison table, software spectrum (simple automation → deep learning), 10 paired traditional vs AI tool examples. Sources: Posts 6, 10, 11.
5. **Wrote Chapter 4 — How AI Learns.** Extended child-learning analogy, three learning stages (training/testing/using), supervised (flashcards), unsupervised (sorting laundry), reinforcement (training a dog), feedback loop detail, training data explanation, "does AI understand?" question. Sources: Posts 3, 6, 11.
6. **Wrote Chapter 5 — Types of AI.** Narrow/General/Super AI pyramid, current tool placement, AI winter history (two winters with causes and consequences), capability spectrum, managing expectations. Sources: Posts 11, 27.

**Why:** Beginning the chapter-by-chapter writing process for Edition 01's expanded 15-chapter book format. Each chapter written as a standalone unit, reviewed and approved before proceeding to the next.

**New files created:**
- `structured/edition_01_what-is-ai/expanded_outline.md`
- `structured/edition_01_what-is-ai/chapter_01.md`
- `structured/edition_01_what-is-ai/chapter_02.md`
- `structured/edition_01_what-is-ai/chapter_03.md`
- `structured/edition_01_what-is-ai/chapter_04.md`
- `structured/edition_01_what-is-ai/chapter_05.md`

**Files updated:**
- `CHANGELOG.md` (this entry)

**Decision made by:** Kelvin M

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
