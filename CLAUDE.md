# CLAUDE.md — Project Context for Claude Code

## Who You Are Working With

**Author:** Kelvin M  
**Title on all documents:** Kelvin M  
**Tagline:** AI Educator & Researcher  
**Website:** Not yet live — omit URL from PDFs until further notice  
**Knowledge Level:** Intermediate AI — understands concepts well, not deeply technical  
**Role:** Academic professional tutor building a self-directed AI education series  

---

## What This Project Is

An open-ended series of 20+ educational PDF documents that teach Artificial Intelligence to complete beginners — people with no technical background. The series is designed to be:

- Self-directed — readers learn without a teacher
- Complexity-sequenced — every PDF builds on the last, from simple to advanced
- Practically focused — not theory only; step-by-step real-world applications
- Viral-ready — every PDF is written so it can be directly converted into a 2–5 minute explainer video

The content source is 60+ raw Twitter posts from multiple AI enthusiasts (6+ authors). These posts are raw — they contain usernames, hashtags, timestamps, and retweet metadata. They must be cleaned, fact-checked (uncertain which contain stats), paraphrased to avoid plagiarism, and restructured into pedagogically sound chapters.

---

## Decisions Already Made — Do Not Re-ask

| Decision | Value |
|----------|-------|
| Audience | Complete beginners, all ages 13–40+, all life contexts |
| Tone | Academic but accessible |
| Language | English only (translations later) |
| Page format | Portrait A4 |
| Sequencing logic | Complexity-based (simple → advanced) |
| Series length | 20+ PDFs, open-ended |
| Release cadence | Bi-weekly (every 2 weeks) |
| Color palette | Anthropic brand colors |
| PDF naming | Both number + name — e.g. "01 — What is AI?" |
| Cover tagline | Consistent series tagline, adapted slightly per topic |
| Quiz questions per PDF | 10 questions |
| Quiz formats | MCQ + True/False + Fill in the blank + Short answer |
| Reflection style | Alternating — Personal / Conceptual / Practical across series |
| Production approach | PDF 01 pilot first, then series continues |
| Reader's biggest fear | "AI is too complicated to understand" |
| What readers should feel | Awakened |
| What's missing online | Step-by-step practical applications of AI |
| Success metric | 100 sales in the first month |

---

## Decisions Still Open — Ask Kelvin Before Proceeding

| Decision | Status |
|----------|--------|
| Video presenter format | Not decided — on camera / voiceover / AI avatar |
| Video script section format | To confirm at PDF 01 pilot review |
| PDF access model | Not decided — free / email capture / mixed |
| PDF update policy | Not decided — fixed or living documents |
| Kelvin's personal AI analogy | Not yet developed — craft together during PDF 01 |

---

## How to Behave Each Session

1. **Never re-ask questions that are already answered above.** All decisions in the "Decisions Already Made" table are locked. Reference them directly.
2. **Always address the author as Kelvin** in responses.
3. **Assume the reader has zero technical background.** Every explanation must pass the "could a 13-year-old understand this?" test.
4. **Paraphrase all Twitter source content.** Never reproduce original tweet wording directly. Rewrite entirely in original voice.
5. **Fact-check all statistics and data claims** before including them in any PDF. Flag uncertain claims rather than publishing them.
6. **Follow SERIES_BIBLE.md for voice and tone.** Follow DESIGN_GUIDELINES.md for all visual decisions. Follow BUILD_FLOW.md for all production steps.
7. **Every PDF must pass the viral check** — it must contain a hook sentence, quotable one-liners, a storytelling arc, and a cliffhanger ending suitable for 2–5 min video conversion.
8. **Do not deviate from STYLE_TOKENS.yaml** for any color, font size, or spacing decision.
9. **Log every build decision in CHANGELOG.md** — date, what changed, why.
10. **Register every new edition in EDITION_REGISTRY.md** the moment it is created.
11. **When in doubt, refer to PRD.md** for the north star of what this project is and why it exists.

---

## File Structure

```
kelvin_ai_series/
├── CLAUDE.md                  ← You are here
├── PRD.md                     ← Product requirements
├── BUILD_FLOW.md              ← How raw tweets become a PDF
├── TECH_STACK.md              ← Tools and libraries
├── SERIES_BIBLE.md            ← Editorial identity and voice
├── DESIGN_GUIDELINES.md       ← Visual system
├── STYLE_TOKENS.yaml          ← Machine-readable design tokens
├── IMAGE_STRATEGY.md          ← How visuals are produced
├── EDITION_REGISTRY.md        ← Log of all editions
├── DISTRIBUTION_CHECKLIST.md  ← Pre-upload checklist
├── CHANGELOG.md               ← Build-by-build log
├── IMPLEMENTATION_PLAN.md     ← Phased task list
├── source/                    ← Raw Twitter content (input)
├── cleaned/                   ← Cleaned and paraphrased content
├── structured/                ← Chapter-structured content per edition
├── assets/
│   ├── covers/                ← AI-generated cover art
│   ├── diagrams/              ← Python/Pillow generated diagrams
│   └── fonts/                 ← Licensed fonts
└── output/                    ← Final PDF files ready for distribution
```
