# IMAGE_STRATEGY.md — Visual Production Strategy

## Overview

Every edition contains two categories of visual assets:
1. **Cover art** — AI-generated full-bleed image (Midjourney primary, DALL·E 3 fallback)
2. **Body diagrams** — programmatically generated using Python + Pillow

No stock photography. No copied images. No screenshots from external sources. All visuals are original.

---

## Category 1 — Cover Art

### Purpose
The cover is the first thing a reader sees. It must:
- Communicate the topic of the edition visually before the reader reads a single word
- Feel modern, professional, and slightly aspirational
- Work at small sizes (WhatsApp thumbnail, Instagram preview)
- Pair with the dark overlay text band without clashing

### Production Tool
**Primary:** Midjourney (v6+)  
**Fallback:** DALL·E 3 via OpenAI  
**Upscaling (if needed):** Pillow bicubic upscale + sharpening filter

### Output Specifications
| Property | Value |
|----------|-------|
| Width | 2480px |
| Height | 3508px |
| DPI | 300 |
| Format | PNG |
| Color mode | RGB |
| File naming | `edition_{NN}_cover.png` |
| Save location | `assets/covers/` |

### Midjourney Prompt Template

```
[SUBJECT DESCRIPTION], conceptual digital illustration, clean minimal style, 
flat design aesthetic, muted warm tones, coral and cream color palette, 
professional educational visual, no text, no typography, no letters, 
no people, abstract but purposeful composition, 
high resolution, 2480x3508 --ar 5:7 --style raw --v 6
```

### Per-Edition Prompt Examples

**Edition 01 — What is AI?**
```
A glowing brain made of interconnected nodes and circuits, soft coral and cream 
tones, clean flat illustration style, minimal background, conceptual educational 
visual, no text, no people, warm professional atmosphere --ar 5:7 --style raw --v 6
```

**Edition 02 — How AI Learns**
```
Abstract concept of learning: stacked books transforming into flowing data streams, 
warm coral and cream palette, flat digital illustration, clean minimal composition, 
no text, no people, professional educational tone --ar 5:7 --style raw --v 6
```

**Edition 03 — Machine Learning**
```
A decision tree branching into multiple pathways, nodes connected by clean lines, 
coral accent colors on cream background, flat minimal illustration, 
conceptual and clean, no text, no people --ar 5:7 --style raw --v 6
```

### Rules for All Cover Prompts
- Always include: "no text, no typography, no letters"
- Always include: "no people" (avoids representation issues across global audience)
- Always include: "coral and cream color palette" (Anthropic brand alignment)
- Always include: "clean minimal style, flat design aesthetic"
- Always specify: `--ar 5:7` (A4 portrait ratio)
- Never use: photorealistic style, dark backgrounds, complex busy compositions
- After generation: crop to exactly 2480 × 3508px before saving

### DALL·E 3 Fallback Prompt Template

```
Conceptual digital illustration for an AI education document cover. Topic: [TOPIC]. 
Flat design aesthetic, muted warm tones with coral (#CC785C) and cream (#F2D4C8) 
color palette. Clean minimal composition. No text. No people. No typography. 
Professional educational visual. White/light background. Simple and purposeful.
```

---

## Category 2 — Body Diagrams

### Purpose
Body diagrams make abstract concepts visible. Every diagram must:
- Explain one idea only — no compound diagrams
- Be readable at half-page width on a printed A4 page
- Be readable on a smartphone screen
- Match the design system exactly (colors, fonts from STYLE_TOKENS.yaml)
- Have a caption below it

### Production Tool
**Python + Pillow**  
Script: `scripts/build_diagram.py`

### Output Specifications
| Property | Value |
|----------|-------|
| Width | 1960px (full content width at 300 DPI) |
| Height | Variable — minimum 400px, maximum 1200px |
| DPI | 300 |
| Format | PNG |
| Color mode | RGB |
| Background | White (#FFFFFF) |
| File naming | `edition_{NN}_diagram_{N}.png` |
| Save location | `assets/diagrams/` |

### Diagram Type Library

The following diagram types are approved for use. Each has a standard Pillow construction pattern.

---

#### Type 1 — Flowchart
**Use when:** Showing a process, sequence of steps, or decision path  
**Example:** How a neural network processes data  
**Construction:**
- Boxes: rounded rectangles, primary fill (#F2D4C8), primary border (#CC785C), 2pt border
- Arrows: single-headed, 1.5pt, color (#4A4A4A)
- Decision nodes: diamond shapes, secondary fill (#F9F6F3), secondary border (#E0D9D4)
- Labels: 10pt Inter Medium, centered in box
- Maximum 7 nodes per diagram
- Left-to-right or top-to-bottom flow only

---

#### Type 2 — Comparison Diagram
**Use when:** Showing how two things are different or similar  
**Example:** Human learning vs machine learning  
**Construction:**
- Two columns separated by a vertical center divider
- Left column: primary fill (#F2D4C8)
- Right column: secondary fill (#F9F6F3)
- Column headers: 12pt Inter Bold, centered
- Row items: 10pt Inter Regular, left-aligned with 8px padding
- Horizontal row dividers: 0.5pt (#E0D9D4)

---

#### Type 3 — Hierarchy / Pyramid
**Use when:** Showing levels, tiers, or a taxonomy  
**Example:** Types of AI — Narrow AI, General AI, Super AI  
**Construction:**
- Triangle divided into horizontal bands
- Top band (smallest): darkest primary (#9E4E2E)
- Middle band: primary (#CC785C)
- Bottom band (largest): primary light (#F2D4C8)
- Labels: white text on dark bands, primary dark text on light bands
- Caption below describing the hierarchy

---

#### Type 4 — Simple Labeled Diagram
**Use when:** Labeling the parts of a concept  
**Example:** Parts of a neural network — Input layer, Hidden layers, Output layer  
**Construction:**
- Central illustration built from basic shapes (circles, rectangles, lines)
- Labels connected to components with thin leader lines (0.5pt, #888888)
- Label text: 9pt Inter Regular, #4A4A4A
- Clean white background
- No border on the diagram itself

---

#### Type 5 — Before / After
**Use when:** Showing transformation or impact  
**Example:** A task without AI vs the same task with AI  
**Construction:**
- Two side-by-side panels separated by an arrow (→)
- Left panel: secondary fill (#F9F6F3), labeled "Before"
- Right panel: primary light (#F2D4C8), labeled "After" or "With AI"
- Panel header: 10pt Inter SemiBold
- Content: bullet points, 10pt Inter Regular

---

### Diagram Caption Rules
- Every diagram must have a caption
- Caption format: `Figure {N}: {Plain language description of what the diagram shows}`
- Caption style: 9pt Inter Italic, #4A4A4A, centered below diagram
- 3mm space between diagram bottom edge and caption
- 4mm space between caption and next body element

---

## File Naming Convention

| Asset Type | Naming Pattern | Example |
|------------|---------------|---------|
| Cover art | `edition_{NN}_cover.png` | `edition_01_cover.png` |
| Body diagram | `edition_{NN}_diagram_{N}.png` | `edition_01_diagram_01.png` |
| Diagram caption file | `edition_{NN}_diagram_{N}_caption.txt` | `edition_01_diagram_01_caption.txt` |

---

## Resolution Rules

| Use case | Minimum DPI | Format | Notes |
|----------|-------------|--------|-------|
| Cover art (print) | 300 DPI | PNG | Must be 2480×3508px |
| Cover art (web preview) | 72 DPI | JPG | Export separately from PNG |
| Body diagrams (print) | 300 DPI | PNG | Built at 300 DPI by Pillow script |
| Social media preview | 72 DPI | JPG/PNG | Export from cover PNG at 1200×1680px |

---

## Quality Checklist — Before Including Any Asset in a PDF

- [ ] Cover art is exactly 2480 × 3508px
- [ ] Cover art has no text, no people, no watermarks
- [ ] Cover art color palette includes coral/cream tones
- [ ] Diagram background is white (#FFFFFF)
- [ ] All diagram text uses Inter font family
- [ ] All diagram colors match STYLE_TOKENS.yaml exactly
- [ ] Diagram caption is present and follows naming convention
- [ ] All PNG files are RGB color mode (not CMYK)
- [ ] All files are saved in the correct `assets/` subdirectory
- [ ] All files follow the naming convention exactly
