# BUILD_FLOW.md — From Raw Tweet to Finished PDF

## Overview

Every edition of the series follows the same 8-stage pipeline. No stage may be skipped. Each stage has a defined input, a defined process, and a defined output. Outputs from one stage become inputs to the next.

---

## Stage 0 — Raw Content Intake

**Input:** Raw Twitter posts (60+ posts, 6+ authors, standalone tweets and threads)  
**Format:** Copy-pasted text containing usernames, hashtags, timestamps, retweet counts, and reply chains  
**Location:** `source/raw_tweets.txt` or `source/raw_tweets_{batch_number}.txt`  

**Process:**
1. Paste all raw Twitter content into a single `.txt` file in the `source/` directory
2. Label the file with the batch number and date — e.g. `raw_tweets_batch01_2026-03.txt`
3. Do not edit, clean, or alter at this stage — preserve exactly as copied

**Output:** `source/raw_tweets_batch{N}_{date}.txt`  
**Status tag:** `[RAW]`

---

## Stage 1 — Content Cleaning

**Input:** `source/raw_tweets_batch{N}_{date}.txt`  
**Tool:** Python script `scripts/clean_tweets.py` or manual cleaning  

**Process:**
1. Strip all usernames (e.g. @username)
2. Strip all hashtags (e.g. #AItools)
3. Strip all timestamps and dates
4. Strip retweet counts, like counts, reply counts
5. Strip URLs unless the URL is the subject of the tweet
6. Remove duplicate content (same idea expressed multiple times)
7. Separate threads — label each thread with [THREAD] and number the posts within it
8. Label standalone tweets with [TWEET]
9. Flag any tweet that contains a statistic, number, or factual claim with [FACT-CHECK]
10. Save cleaned output

**Output:** `cleaned/cleaned_batch{N}_{date}.txt`  
**Status tag:** `[CLEANED]`

---

## Stage 2 — Fact-Checking

**Input:** `cleaned/cleaned_batch{N}_{date}.txt` — specifically all items flagged `[FACT-CHECK]`  

**Process:**
1. Extract all `[FACT-CHECK]` flagged items into a separate list
2. Verify each claim against a reliable source (Wikipedia, peer-reviewed papers, official AI company blogs, reputable news outlets)
3. For each claim: either VERIFY (add source URL) or REMOVE (delete the claim)
4. Never publish an unverified statistic — if uncertain, remove entirely
5. Document all verified sources in `cleaned/sources_batch{N}.md`

**Output:**  
- `cleaned/cleaned_batch{N}_verified.txt` — cleaned content with all facts verified or removed  
- `cleaned/sources_batch{N}.md` — list of all verified sources with URLs  
**Status tag:** `[VERIFIED]`

---

## Stage 3 — Topic Clustering & Curriculum Mapping

**Input:** `cleaned/cleaned_batch{N}_verified.txt`  

**Process:**
1. Read all cleaned content and group each item by topic:
   - What is AI / AI basics
   - Machine Learning
   - Large Language Models (LLMs) / ChatGPT
   - AI tools & productivity
   - AI ethics & safety
   - AI and jobs / future of work
   - AI in education
   - AI in business
   - Deep learning / neural networks
2. Within each topic, sort content by complexity — introductory ideas first, advanced ideas last
3. Identify which topic has enough content for a full PDF (minimum 800 words of paraphrased content)
4. Map topics to edition numbers following the complexity-based sequence:
   - Editions 01–05: Foundational (What is AI, How AI thinks, History of AI, Types of AI, AI vs Human Intelligence)
   - Editions 06–10: Core Concepts (Machine Learning, Neural Networks, Deep Learning, LLMs, Training Data)
   - Editions 11–15: Applications (AI tools & productivity, AI in business, AI in education, AI in healthcare, AI in daily life)
   - Editions 16–20+: Advanced & Critical (AI ethics, AI and jobs, AI safety, Future of AI, How to use AI responsibly)
5. Assign each verified content item to its target edition number

**Output:** `structured/curriculum_map.md` — full series map with edition numbers, titles, and content assigned  
**Status tag:** `[MAPPED]`

---

## Stage 4 — Chapter Drafting

**Input:** `structured/curriculum_map.md` — content assigned to the target edition  
**Output location:** `structured/edition_{NN}_{slug}/draft.md`  

**Process — write each section in order:**

### 4.1 — Hook (Aha Moment Opener)
- Write a 2–3 sentence opening using a relatable real-life analogy
- The analogy must require zero technical knowledge to understand
- Must make the reader feel: "Oh — I already understand this"
- Example structure: "You already know how to do X. AI does the same thing, just with Y."
- This line also serves as the first 3 seconds of the video script

### 4.2 — Learning Objectives
- Write 3–5 bullet points stating exactly what the reader will understand by the end
- Use plain language — no jargon
- Frame each objective as "By the end of this edition, you will be able to..."

### 4.3 — Table of Contents
- List all section headings in order
- Auto-generated from section headings in the draft

### 4.4 — Body Sections
Write each body section following this internal structure:
1. **Explanatory text** — paraphrase source content entirely in original voice, no direct quotes
2. **Real-world example** — one concrete example the reader can picture
3. **Diagram placeholder** — write `[DIAGRAM: description of what the diagram shows]` — diagrams are generated in Stage 6
4. **Callout box** — one "Did You Know?" or "Key Fact" callout per major section
5. **Step-by-step breakdown** — at least one practical application section per edition
6. **Comparison table** — at least one before/after or A-vs-B table per edition

### 4.5 — Key Takeaways
- Write 3–5 bullet points summarising the most important ideas
- Each takeaway must be a complete, standalone sentence
- These also serve as quotable one-liners for video text overlays

### 4.6 — Glossary
- List every technical term used in the edition
- Each definition: term, plain-language definition (1–2 sentences maximum)

### 4.7 — Mini Quiz (10 Questions)
- 3 Multiple Choice questions (A, B, C, D)
- 2 True / False questions
- 2 Fill in the blank questions
- 3 Short answer questions (1–2 sentences)
- Write an answer key and save separately in `structured/edition_{NN}_{slug}/answer_key.md` — never include in published PDF

### 4.8 — Reflection Question
- Alternate across editions: Personal → Conceptual → Practical → Personal → ...
- Edition 01: Personal ("How does AI show up in your daily life right now?")
- Edition 02: Conceptual ("What assumption about AI did this edition challenge?")
- Edition 03: Practical ("What will you try differently after reading this?")
- Continue rotating

### 4.9 — CTA Block
Include all six CTAs in this order:
1. Follow Kelvin M on social media
2. Share this PDF with someone who needs it
3. Subscribe to the newsletter
4. Watch the video version
5. Join the community (WhatsApp / Telegram)
6. Download the next edition in the series

### 4.10 — Next Edition Teaser
- 2–3 sentences previewing the next PDF
- End with a cliffhanger — "In the next edition, you'll discover why..."
- This also serves as the video cliffhanger ending

**Output:** `structured/edition_{NN}_{slug}/draft.md`  
**Status tag:** `[DRAFTED]`

---

## Stage 5 — Editorial Review

**Input:** `structured/edition_{NN}_{slug}/draft.md`  

**Process:**
1. Read the full draft aloud (mentally) — does it flow naturally?
2. Check every sentence against the Series Bible — does it match voice and tone?
3. Check all forbidden phrases list in SERIES_BIBLE.md — remove any violations
4. Confirm the hook creates a genuine aha moment in the first paragraph
5. Confirm every technical term appears in the glossary
6. Confirm the quiz has exactly 10 questions in the correct format mix
7. Confirm the reflection question matches the correct rotation for this edition number
8. Confirm all six CTAs are present
9. Confirm the next edition teaser ends on a cliffhanger
10. Mark any sections that need diagrams — confirm `[DIAGRAM: ...]` placeholders are specific enough for Stage 6
11. Approve or send back for revision

**Output:** `structured/edition_{NN}_{slug}/draft_approved.md`  
**Status tag:** `[APPROVED]`

---

## Stage 6 — Asset Production

**Input:** `structured/edition_{NN}_{slug}/draft_approved.md` — all `[DIAGRAM: ...]` placeholders  

**Process:**

### 6.1 — Cover Art
- Generate cover using AI image tool (Midjourney or equivalent)
- Follow IMAGE_STRATEGY.md for prompt templates and specs
- Save as: `assets/covers/edition_{NN}_cover.png`
- Resolution: 2480 × 3508px (A4 at 300 DPI)

### 6.2 — Body Diagrams
- Generate each diagram using Python + Pillow
- Follow IMAGE_STRATEGY.md for diagram specs
- Save each as: `assets/diagrams/edition_{NN}_diagram_{N}.png`
- Resolution: 1654 × 1240px (half-page width at 300 DPI) or as specified

### 6.3 — Font Assets
- Confirm all required fonts are present in `assets/fonts/`
- See TECH_STACK.md for required font files

**Output:**  
- `assets/covers/edition_{NN}_cover.png`  
- `assets/diagrams/edition_{NN}_diagram_{N}.png`  
**Status tag:** `[ASSETS READY]`

---

## Stage 7 — PDF Build

**Input:**  
- `structured/edition_{NN}_{slug}/draft_approved.md`  
- `assets/covers/edition_{NN}_cover.png`  
- `assets/diagrams/edition_{NN}_diagram_{N}.png`  
- `STYLE_TOKENS.yaml`  

**Tool:** Python + ReportLab  
**Script:** `scripts/build_pdf.py`  

**Process:**
1. Load `STYLE_TOKENS.yaml` — all colors, fonts, sizes read from here
2. Assemble pages in order: Cover → Hook → Objectives → TOC → Body → Takeaways → Glossary → Quiz → Reflection → CTA → Teaser
3. Apply all design rules from DESIGN_GUIDELINES.md
4. Insert cover art on page 1
5. Insert diagrams at `[DIAGRAM: ...]` positions
6. Apply callout box styles to all callout sections
7. Apply comparison table styles to all tables
8. Embed metadata: Title, Author (Kelvin M), Subject, Keywords
9. Export PDF
10. Verify file size — must be under 10MB for email distribution

**Output:** `output/edition_{NN}_{slug}_v{version}.pdf`  
**Status tag:** `[BUILT]`

---

## Stage 8 — QA & Distribution

**Input:** `output/edition_{NN}_{slug}_v{version}.pdf`  

**Process:**
1. Open PDF on smartphone — check readability on small screen
2. Open PDF on laptop — check all page layouts
3. Print one page — check print readability
4. Check all diagrams render correctly
5. Check cover art is crisp at A4 size
6. Check all fonts are embedded
7. Check all hyperlinks in CTAs are active
8. Run through DISTRIBUTION_CHECKLIST.md for each platform
9. Register edition in EDITION_REGISTRY.md
10. Log the build in CHANGELOG.md
11. Upload to distribution platforms
12. Publish and promote

**Output:** Live published PDF on all distribution channels  
**Status tag:** `[PUBLISHED]`

---

## Stage Summary Table

| Stage | Name | Input | Output | Status Tag |
|-------|------|-------|--------|------------|
| 0 | Raw Content Intake | Twitter copy-paste | `source/raw_tweets_batch{N}.txt` | [RAW] |
| 1 | Content Cleaning | Raw file | `cleaned/cleaned_batch{N}.txt` | [CLEANED] |
| 2 | Fact-Checking | Cleaned file | `cleaned/cleaned_batch{N}_verified.txt` | [VERIFIED] |
| 3 | Topic Clustering | Verified file | `structured/curriculum_map.md` | [MAPPED] |
| 4 | Chapter Drafting | Curriculum map | `structured/edition_{NN}/draft.md` | [DRAFTED] |
| 5 | Editorial Review | Draft | `structured/edition_{NN}/draft_approved.md` | [APPROVED] |
| 6 | Asset Production | Approved draft | Cover PNG + Diagram PNGs | [ASSETS READY] |
| 7 | PDF Build | Approved draft + assets | `output/edition_{NN}_v{N}.pdf` | [BUILT] |
| 8 | QA & Distribution | Built PDF | Live published PDF | [PUBLISHED] |
