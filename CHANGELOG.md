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
