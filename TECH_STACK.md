# TECH_STACK.md — Tools, Libraries, and Environment

## Language

**Python 3.10+**  
All build scripts are written in Python. No other language is used for automation.

---

## Core PDF Generation

### ReportLab (reportlab >= 3.6)
- **Purpose:** Primary PDF layout and generation engine
- **Used for:** Page layout, text rendering, tables, callout boxes, image embedding, metadata
- **Install:** `pip install reportlab`
- **Key modules used:**
  - `reportlab.platypus` — SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether
  - `reportlab.lib.pagesizes` — A4
  - `reportlab.lib.styles` — getSampleStyleSheet, ParagraphStyle
  - `reportlab.lib.colors` — HexColor
  - `reportlab.lib.units` — mm, cm
  - `reportlab.pdfgen.canvas` — canvas for custom drawing
- **Critical rule:** Never use Unicode subscript/superscript characters — use ReportLab XML tags `<sub>` and `<super>` inside Paragraph objects instead

### pypdf (pypdf >= 3.0)
- **Purpose:** PDF manipulation — merging, metadata reading, page extraction
- **Install:** `pip install pypdf`
- **Used for:** Post-build verification, merging cover pages if needed

---

## Image Processing

### Pillow (Pillow >= 9.0)
- **Purpose:** Generating all body diagrams and processing cover art
- **Install:** `pip install Pillow`
- **Used for:** Drawing flowcharts, labeled diagrams, comparison graphics, callout box graphics
- **Key modules:** `PIL.Image`, `PIL.ImageDraw`, `PIL.ImageFont`

---

## Content Processing

### Python Standard Library
- `re` — regex for cleaning raw tweet metadata (usernames, hashtags, timestamps)
- `json` — reading/writing structured content
- `os`, `pathlib` — file system operations
- `yaml` — reading STYLE_TOKENS.yaml

### PyYAML (pyyaml >= 6.0)
- **Purpose:** Reading STYLE_TOKENS.yaml in build scripts
- **Install:** `pip install pyyaml`

### markdown (markdown >= 3.4)
- **Purpose:** Converting approved draft `.md` files to structured content for ReportLab
- **Install:** `pip install markdown`

---

## AI Image Generation (Cover Art)

### Midjourney (primary)
- **Purpose:** Generating cover art for each edition
- **Access:** Via Discord bot or Midjourney web app
- **Output format:** PNG, minimum 2480 × 3508px (A4 at 300 DPI)
- **Prompt templates:** See IMAGE_STRATEGY.md

### DALL·E 3 (fallback)
- **Purpose:** Fallback cover art generation if Midjourney unavailable
- **Access:** Via OpenAI API or ChatGPT Plus
- **Output format:** PNG, 1024×1792px (upscale to 300 DPI with Pillow)

---

## Fonts

All fonts stored in `assets/fonts/`. All fonts must be embedded in every PDF.

| Font | File | Usage |
|------|------|-------|
| Inter Regular | `Inter-Regular.ttf` | Body text |
| Inter Medium | `Inter-Medium.ttf` | Subheadings, callout labels |
| Inter SemiBold | `Inter-SemiBold.ttf` | Section headings |
| Inter Bold | `Inter-Bold.ttf` | Chapter titles, cover title |
| Inter Italic | `Inter-Italic.ttf` | Glossary definitions, captions |

**Font source:** Google Fonts (Inter) — free, open license  
**Download:** https://fonts.google.com/specimen/Inter  
**Registration in ReportLab:**
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Inter-Regular', 'assets/fonts/Inter-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Inter-Bold', 'assets/fonts/Inter-Bold.ttf'))
```

---

## Version Control

### Git
- **Repository:** Local git repository, remote on GitHub (private)
- **Branch strategy:**
  - `main` — stable, published editions only
  - `draft/edition-{NN}` — active draft for each edition
  - `fix/{description}` — hotfixes on published editions
- **Commit message format:** `[edition-{NN}] {stage}: {description}`
  - Example: `[edition-01] draft: completed body sections 1-3`
  - Example: `[edition-01] build: v1.0 PDF generated`
  - Example: `[edition-01] fix: corrected glossary term for LLM`
- **Never commit to main directly** — always merge from draft branch
- **Tag every published release:** `git tag v{NN}.{version}` e.g. `v01.1`

---

## Directory Structure (Technical)

```
kelvin_ai_series/
├── scripts/
│   ├── clean_tweets.py       ← Stage 1: strips metadata from raw tweets
│   ├── fact_flag.py          ← Stage 2: flags [FACT-CHECK] items
│   ├── cluster_topics.py     ← Stage 3: groups content by topic
│   ├── build_pdf.py          ← Stage 7: assembles and exports PDF
│   └── build_diagram.py      ← Stage 6: generates diagrams with Pillow
├── source/                   ← Raw tweet files (input)
├── cleaned/                  ← Cleaned and verified content
├── structured/               ← Chapter drafts per edition
├── assets/
│   ├── covers/               ← AI-generated cover PNGs
│   ├── diagrams/             ← Pillow-generated diagram PNGs
│   └── fonts/                ← TTF font files
├── output/                   ← Final PDF files
└── docs/                     ← All .md and .yaml planning files
```

---

## Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install all dependencies
pip install reportlab pypdf Pillow pyyaml markdown

# Verify install
python -c "import reportlab, pypdf, PIL, yaml, markdown; print('All dependencies OK')"
```

### requirements.txt
```
reportlab>=3.6.0
pypdf>=3.0.0
Pillow>=9.0.0
pyyaml>=6.0.0
markdown>=3.4.0
```

---

## File Naming Conventions

| File type | Format | Example |
|-----------|--------|---------|
| Raw tweets | `raw_tweets_batch{N}_{YYYY-MM}.txt` | `raw_tweets_batch01_2026-03.txt` |
| Cleaned content | `cleaned_batch{N}_{YYYY-MM}_verified.txt` | `cleaned_batch01_2026-03_verified.txt` |
| Draft | `edition_{NN}_{slug}/draft.md` | `edition_01_what-is-ai/draft.md` |
| Approved draft | `edition_{NN}_{slug}/draft_approved.md` | `edition_01_what-is-ai/draft_approved.md` |
| Cover art | `edition_{NN}_cover.png` | `edition_01_cover.png` |
| Diagram | `edition_{NN}_diagram_{N}.png` | `edition_01_diagram_01.png` |
| Final PDF | `edition_{NN}_{slug}_v{version}.pdf` | `edition_01_what-is-ai_v1.0.pdf` |
| Answer key | `edition_{NN}_{slug}/answer_key.md` | `edition_01_what-is-ai/answer_key.md` |
