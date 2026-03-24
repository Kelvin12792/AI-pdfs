# DESIGN_GUIDELINES.md — Visual System

## Design Philosophy

Every visual decision serves one purpose: **make complex ideas feel clear and accessible to a complete beginner reading on any device.** The design must feel professional enough to be credible and warm enough to be approachable. It must never intimidate.

All values defined here are implemented exactly as specified in `STYLE_TOKENS.yaml`. Do not hardcode any value in build scripts — always read from STYLE_TOKENS.yaml.

---

## Color Palette — Anthropic Brand

| Token Name | Hex | Usage |
|------------|-----|-------|
| `color.primary` | #CC785C | Primary accent — cover title, section headings, callout borders |
| `color.primary.dark` | #9E4E2E | Hover states, strong emphasis |
| `color.primary.light` | #F2D4C8 | Callout box backgrounds, highlight fills |
| `color.bg.page` | #FFFFFF | Page background |
| `color.bg.surface` | #F9F6F3 | Callout box backgrounds, table alternating rows |
| `color.bg.dark` | #1A1A1A | Cover page background, footer bar |
| `color.text.primary` | #1A1A1A | All body text |
| `color.text.secondary` | #4A4A4A | Captions, glossary entries, secondary labels |
| `color.text.muted` | #888888 | Page numbers, footer text |
| `color.text.inverse` | #FFFFFF | Text on dark backgrounds (cover, footer) |
| `color.border` | #E0D9D4 | Table borders, section dividers, callout box borders |
| `color.accent.teal` | #2A9D8F | "Did You Know?" callout accent |
| `color.accent.amber` | #E9C46A | "Key Fact" callout accent |
| `color.accent.coral` | #E76F51 | "Watch Out" callout accent |
| `color.accent.green` | #57A773 | "In the Real World" callout accent |

---

## Typography

All fonts are from the Inter family. All fonts must be embedded in every PDF.

| Token Name | Font | Weight | Size | Usage |
|------------|------|--------|------|-------|
| `type.cover.title` | Inter Bold | 700 | 36pt | Cover edition title |
| `type.cover.series` | Inter Regular | 400 | 14pt | Cover series name |
| `type.cover.author` | Inter Medium | 500 | 12pt | Cover author line |
| `type.cover.tagline` | Inter Italic | 400 | 11pt | Cover tagline |
| `type.h1` | Inter Bold | 700 | 22pt | Chapter/section headings |
| `type.h2` | Inter SemiBold | 600 | 17pt | Sub-section headings |
| `type.h3` | Inter Medium | 500 | 14pt | Callout box labels, table headers |
| `type.body` | Inter Regular | 400 | 11pt | All body text |
| `type.body.lead` | Inter Regular | 400 | 13pt | Hook / opening paragraph |
| `type.caption` | Inter Italic | 400 | 9pt | Diagram captions, image credits |
| `type.callout` | Inter Medium | 500 | 10pt | Callout box body text |
| `type.label` | Inter SemiBold | 600 | 9pt | Callout box type labels (DID YOU KNOW?, etc.) |
| `type.quiz` | Inter Regular | 400 | 10pt | Quiz question body text |
| `type.glossary.term` | Inter SemiBold | 600 | 10pt | Glossary term |
| `type.glossary.def` | Inter Regular | 400 | 10pt | Glossary definition |
| `type.footer` | Inter Regular | 400 | 8pt | Footer — page number, series name |
| `type.page.number` | Inter Medium | 500 | 9pt | Page numbers |

**Line spacing:** 1.4 for body text, 1.2 for callout boxes, 1.6 for lead paragraph  
**Letter spacing:** Default (0) for all body text. Labels and callout type labels: 0.05em tracking

---

## Page Layout — Portrait A4

**Page size:** A4 — 210mm × 297mm (595pt × 842pt in ReportLab)

| Element | Value |
|---------|-------|
| Margin top | 20mm |
| Margin bottom | 20mm |
| Margin left | 22mm |
| Margin right | 22mm |
| Content width | 166mm |
| Content height | 257mm |
| Gutter (multi-column) | 8mm |

---

## Cover Page Layout

The cover occupies the full A4 page with no margins. Structure from top to bottom:

| Zone | Height | Content |
|------|--------|---------|
| Cover image | 60% of page height | AI-generated full-bleed image |
| Dark overlay band | 40% of page height | Background: `color.bg.dark` |
| Book title | Within dark band | "The AI Basics Nobody Made Clear", 36pt, `color.primary`, Inter Bold |
| Subtitle | Within dark band | "A Beginner's Guide to AI", 14pt, `color.text.inverse`, Inter Regular |
| Author line | Bottom of dark band | "by Kelvin M, AI Educator & Researcher", 12pt, `color.text.muted` |

---

## Section Heading Style

| Level | Style |
|-------|-------|
| H1 | 22pt Inter Bold, `color.primary`, 8mm space above, 4mm space below, full-width bottom border 0.5pt `color.border` |
| H2 | 17pt Inter SemiBold, `color.text.primary`, 6mm space above, 3mm space below, no border |
| H3 | 14pt Inter Medium, `color.text.secondary`, 4mm space above, 2mm space below, no border |

---

## Callout Box Specifications

All callout boxes share the same base structure. Only the accent color and label change per type.

**Base dimensions:**
- Full content width (166mm)
- Padding: 8mm all sides
- Border radius: 4pt
- Border: 1.5pt solid, left side only (accent color)
- Background: `color.bg.surface`
- Bottom margin: 6mm

| Callout Type | Label | Left Border Color | Label Color |
|-------------|-------|-------------------|-------------|
| Did You Know? | DID YOU KNOW? | `color.accent.teal` | `color.accent.teal` |
| Key Fact | KEY FACT | `color.accent.amber` | `color.accent.amber` |
| In the Real World | IN THE REAL WORLD | `color.accent.green` | `color.accent.green` |
| Watch Out | WATCH OUT | `color.accent.coral` | `color.accent.coral` |

**Label:** 9pt Inter SemiBold, all caps, letter-spacing 0.05em, above body text, 2mm margin below label  
**Body text:** 10pt Inter Medium, `color.text.primary`, line height 1.2  
**Maximum 3 lines of body text per callout box**

---

## Table Style

| Property | Value |
|----------|-------|
| Width | Full content width (166mm) |
| Header row background | `color.primary.light` |
| Header row text | 10pt Inter SemiBold, `color.text.primary` |
| Body row text | 10pt Inter Regular, `color.text.primary` |
| Alternating row background | White / `color.bg.surface` |
| Cell padding | 3mm horizontal, 2.5mm vertical |
| Border | 0.5pt `color.border`, horizontal lines only |
| No vertical cell borders | — |
| Bottom margin | 6mm |

---

## Step-by-Step Section Style

Each step uses a numbered badge + body text layout:

| Property | Value |
|----------|-------|
| Step number badge | Circle, 18pt diameter, background `color.primary`, text `color.text.inverse`, 10pt Inter Bold |
| Step text | 11pt Inter Regular, `color.text.primary`, vertically aligned to badge center |
| Left indent from badge | 8mm |
| Spacing between steps | 4mm |

---

## Diagram Style

All diagrams generated with Pillow follow these rules:

| Property | Value |
|----------|-------|
| Background | White (#FFFFFF) |
| Primary shape fill | `color.primary.light` (#F2D4C8) |
| Primary shape border | 2pt `color.primary` (#CC785C) |
| Secondary shape fill | `color.bg.surface` (#F9F6F3) |
| Secondary shape border | 1pt `color.border` (#E0D9D4) |
| Connector arrows | 1.5pt `color.text.secondary` (#4A4A4A) |
| Label text | 10pt Inter Medium, `color.text.primary` |
| Caption text | 9pt Inter Italic, `color.text.secondary` |
| Diagram resolution | 300 DPI |
| Maximum diagram width | Full content width (1960px at 300 DPI) |
| Diagram border | None |
| Bottom margin | 4mm below diagram + 3mm below caption |

---

## Footer Style

Every page except the cover has a footer:

| Property | Value |
|----------|-------|
| Height | 8mm |
| Background | Transparent |
| Top border | 0.5pt `color.border` |
| Left content | Series name, 8pt Inter Regular, `color.text.muted` |
| Center content | Empty |
| Right content | Page number, 9pt Inter Medium, `color.text.muted` |

---

## Quiz Section Style

| Property | Value |
|----------|-------|
| Section heading | H1 style: "Mini Quiz" |
| Question number | 10pt Inter Bold, `color.primary` |
| Question text | 10pt Inter Regular, `color.text.primary` |
| MCQ options | 10pt Inter Regular, indented 6mm, labeled A. B. C. D. |
| T/F options | 10pt Inter Regular, indented 6mm |
| Fill-in-the-blank line | Underline, 40mm wide, `color.border` |
| Short answer lines | 3 ruled lines, 0.5pt `color.border` |
| Spacing between questions | 5mm |

---

## Glossary Style

| Property | Value |
|----------|-------|
| Section heading | H1 style: "Glossary" |
| Term | 10pt Inter SemiBold, `color.text.primary` |
| Definition | 10pt Inter Regular, `color.text.secondary`, 6mm left indent |
| Separator | 0.5pt `color.border` line between entries |
| Spacing between entries | 3mm |

---

## Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `space.xs` | 2mm | Minimum internal padding |
| `space.sm` | 4mm | Tight component spacing |
| `space.md` | 6mm | Standard component spacing |
| `space.lg` | 8mm | Section breathing room |
| `space.xl` | 12mm | Major section breaks |
| `space.xxl` | 20mm | Page margins |
