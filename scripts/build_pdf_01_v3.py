"""
Build PDF for Edition 01 — What is AI?
v3.0: Full 15-chapter book built from markdown source files.
"""

import os
import re
import math
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable, Flowable
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.units import mm
pt = 1
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

# ─── Paths ───
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
DIAGRAM_DIR = os.path.join(BASE_DIR, "assets", "diagrams")
COVER_DIR = os.path.join(BASE_DIR, "assets", "covers")
CHAPTER_DIR = os.path.join(BASE_DIR, "structured", "edition_01_what-is-ai")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "edition_01_what-is-ai_v3.0.pdf")

# ─── Colors from STYLE_TOKENS.yaml ───
PRIMARY = HexColor("#CC785C")
PRIMARY_DARK = HexColor("#9E4E2E")
PRIMARY_LIGHT = HexColor("#F2D4C8")
BG_PAGE = HexColor("#FFFFFF")
BG_SURFACE = HexColor("#F9F6F3")
BG_DARK = HexColor("#1A1A1A")
TEXT_PRIMARY = HexColor("#1A1A1A")
TEXT_SECONDARY = HexColor("#4A4A4A")
TEXT_MUTED = HexColor("#888888")
TEXT_INVERSE = HexColor("#FFFFFF")
BORDER = HexColor("#E0D9D4")
ACCENT_TEAL = HexColor("#2A9D8F")
ACCENT_AMBER = HexColor("#E9C46A")
ACCENT_CORAL = HexColor("#E76F51")
ACCENT_GREEN = HexColor("#57A773")

# ─── Page dimensions ───
PAGE_W, PAGE_H = A4
MARGIN_TOP = 20 * mm
MARGIN_BOTTOM = 20 * mm
MARGIN_LEFT = 22 * mm
MARGIN_RIGHT = 22 * mm
CONTENT_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

# ─── Register Fonts ───
pdfmetrics.registerFont(TTFont('Inter-Regular', os.path.join(FONT_DIR, 'Inter-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Medium', os.path.join(FONT_DIR, 'Inter-Medium.ttf')))
pdfmetrics.registerFont(TTFont('Inter-SemiBold', os.path.join(FONT_DIR, 'Inter-SemiBold.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Bold', os.path.join(FONT_DIR, 'Inter-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Italic', os.path.join(FONT_DIR, 'Inter-Italic.ttf')))


# ─── Paragraph Styles ───
def make_styles():
    s = {}
    s['h1'] = ParagraphStyle(
        'H1', fontName='Inter-Bold', fontSize=22, leading=26.4,
        textColor=PRIMARY, spaceBefore=8*mm, spaceAfter=4*mm,
        borderWidth=0.5, borderColor=BORDER, borderPadding=(0, 0, 4, 0),
    )
    s['h2'] = ParagraphStyle(
        'H2', fontName='Inter-SemiBold', fontSize=17, leading=20.4,
        textColor=TEXT_PRIMARY, spaceBefore=6*mm, spaceAfter=3*mm,
    )
    s['h3'] = ParagraphStyle(
        'H3', fontName='Inter-Medium', fontSize=14, leading=16.8,
        textColor=TEXT_SECONDARY, spaceBefore=4*mm, spaceAfter=2*mm,
    )
    s['body'] = ParagraphStyle(
        'Body', fontName='Inter-Regular', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, spaceAfter=3*mm, alignment=TA_JUSTIFY,
    )
    s['body_lead'] = ParagraphStyle(
        'BodyLead', fontName='Inter-Regular', fontSize=13, leading=20.8,
        textColor=TEXT_PRIMARY, spaceAfter=4*mm, alignment=TA_JUSTIFY,
    )
    s['bullet'] = ParagraphStyle(
        'Bullet', fontName='Inter-Regular', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, spaceAfter=2*mm, leftIndent=12,
        bulletIndent=0, bulletFontSize=11,
    )
    s['callout_label'] = ParagraphStyle(
        'CalloutLabel', fontName='Inter-SemiBold', fontSize=9, leading=10.8,
        spaceAfter=2*mm,
    )
    s['callout_body'] = ParagraphStyle(
        'CalloutBody', fontName='Inter-Medium', fontSize=10, leading=12,
        textColor=TEXT_PRIMARY,
    )
    s['caption'] = ParagraphStyle(
        'Caption', fontName='Inter-Italic', fontSize=9, leading=12,
        textColor=TEXT_SECONDARY, alignment=TA_CENTER, spaceAfter=4*mm,
    )
    s['glossary_term'] = ParagraphStyle(
        'GlossaryTerm', fontName='Inter-SemiBold', fontSize=10, leading=14,
        textColor=TEXT_PRIMARY,
    )
    s['glossary_def'] = ParagraphStyle(
        'GlossaryDef', fontName='Inter-Regular', fontSize=10, leading=14,
        textColor=TEXT_SECONDARY, leftIndent=6*mm, spaceAfter=3*mm,
    )
    s['quiz_num'] = ParagraphStyle(
        'QuizNum', fontName='Inter-Bold', fontSize=10, leading=14,
        textColor=PRIMARY,
    )
    s['quiz_text'] = ParagraphStyle(
        'QuizText', fontName='Inter-Regular', fontSize=10, leading=14,
        textColor=TEXT_PRIMARY, spaceAfter=2*mm,
    )
    s['quiz_option'] = ParagraphStyle(
        'QuizOption', fontName='Inter-Regular', fontSize=10, leading=14,
        textColor=TEXT_PRIMARY, leftIndent=6*mm,
    )
    s['step_text'] = ParagraphStyle(
        'StepText', fontName='Inter-Regular', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, leftIndent=10*mm, spaceAfter=4*mm,
    )
    s['cta'] = ParagraphStyle(
        'CTA', fontName='Inter-Medium', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, spaceAfter=3*mm, leftIndent=8,
    )
    s['teaser'] = ParagraphStyle(
        'Teaser', fontName='Inter-Regular', fontSize=12, leading=18,
        textColor=TEXT_PRIMARY, spaceAfter=3*mm, alignment=TA_JUSTIFY,
    )
    s['cover_title'] = ParagraphStyle(
        'CoverTitle', fontName='Inter-Bold', fontSize=36, leading=43.2,
        textColor=PRIMARY, alignment=TA_LEFT,
    )
    s['cover_series'] = ParagraphStyle(
        'CoverSeries', fontName='Inter-Regular', fontSize=14, leading=18,
        textColor=TEXT_INVERSE, alignment=TA_LEFT,
    )
    s['cover_author'] = ParagraphStyle(
        'CoverAuthor', fontName='Inter-Medium', fontSize=12, leading=16,
        textColor=TEXT_MUTED, alignment=TA_LEFT,
    )
    s['cover_tagline'] = ParagraphStyle(
        'CoverTagline', fontName='Inter-Italic', fontSize=11, leading=15,
        textColor=TEXT_INVERSE, alignment=TA_LEFT,
    )
    s['toc_item'] = ParagraphStyle(
        'TOCItem', fontName='Inter-Regular', fontSize=11, leading=18,
        textColor=TEXT_PRIMARY, leftIndent=8, spaceAfter=1*mm,
    )
    s['objectives'] = ParagraphStyle(
        'Objectives', fontName='Inter-Regular', fontSize=11, leading=17,
        textColor=TEXT_PRIMARY, leftIndent=14, bulletIndent=0, spaceAfter=2*mm,
    )
    s['reflection'] = ParagraphStyle(
        'Reflection', fontName='Inter-Italic', fontSize=12, leading=18,
        textColor=TEXT_SECONDARY, spaceAfter=3*mm, alignment=TA_JUSTIFY,
    )
    s['key_takeaway'] = ParagraphStyle(
        'KeyTakeaway', fontName='Inter-Medium', fontSize=11, leading=16,
        textColor=TEXT_PRIMARY, leftIndent=14, bulletIndent=0, spaceAfter=3*mm,
    )
    s['pull_quote'] = ParagraphStyle(
        'PullQuote', fontName='Inter-SemiBold', fontSize=14, leading=20,
        textColor=PRIMARY_DARK, alignment=TA_CENTER,
        spaceBefore=6*mm, spaceAfter=6*mm,
    )
    s['section_intro'] = ParagraphStyle(
        'SectionIntro', fontName='Inter-Medium', fontSize=11, leading=16,
        textColor=TEXT_SECONDARY, spaceAfter=4*mm, alignment=TA_JUSTIFY,
    )
    return s


STYLES = make_styles()


# ─── Helper builders ───

def h1(text):
    return Paragraph(text, STYLES['h1'])

def h2(text):
    return Paragraph(text, STYLES['h2'])

def h3(text):
    return Paragraph(text, STYLES['h3'])

def body(text):
    return Paragraph(text, STYLES['body'])

def body_lead(text):
    return Paragraph(text, STYLES['body_lead'])

def bullet(text):
    return Paragraph(f"\u2022  {text}", STYLES['bullet'])

def spacer(h_mm=4):
    return Spacer(1, h_mm * mm)

def pull_quote(text):
    return Paragraph(f"\u201c{text}\u201d", STYLES['pull_quote'])

def section_divider():
    return HRFlowable(
        width="40%", thickness=1, color=PRIMARY_LIGHT,
        spaceAfter=4*mm, spaceBefore=4*mm, hAlign='CENTER',
    )


def callout_box(label_text, body_text, border_color, label_color):
    label_style = ParagraphStyle(
        'CL', parent=STYLES['callout_label'], textColor=label_color,
    )
    label = Paragraph(label_text, label_style)
    body_para = Paragraph(body_text, STYLES['callout_body'])
    t = Table(
        [[label], [body_para]],
        colWidths=[CONTENT_W - 16*mm],
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_SURFACE),
        ('TOPPADDING', (0, 0), (-1, -1), 8*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 10*mm),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8*mm),
        ('TOPPADDING', (0, 0), (0, 0), 8*mm),
        ('BOTTOMPADDING', (0, 0), (0, 0), 0),
        ('TOPPADDING', (0, 1), (0, 1), 2*mm),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    outer = Table([[t]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ('LINEBEFOREDECOR', (0, 0), (0, -1), 1.5, border_color),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return outer


def did_you_know(text):
    return callout_box("DID YOU KNOW?", text, ACCENT_TEAL, ACCENT_TEAL)

def key_fact(text):
    return callout_box("KEY FACT", text, ACCENT_AMBER, ACCENT_AMBER)

def real_world(text):
    return callout_box("IN THE REAL WORLD", text, ACCENT_GREEN, ACCENT_GREEN)

def watch_out(text):
    return callout_box("WATCH OUT", text, ACCENT_CORAL, ACCENT_CORAL)


def make_table(headers, rows, col_widths=None):
    if col_widths is None:
        n = len(headers)
        col_widths = [CONTENT_W / n] * n
    header_style = ParagraphStyle('TH', fontName='Inter-SemiBold', fontSize=10,
                                   leading=14, textColor=TEXT_PRIMARY)
    cell_style = ParagraphStyle('TD', fontName='Inter-Regular', fontSize=10,
                                 leading=14, textColor=TEXT_PRIMARY)
    data = [[Paragraph(h, header_style) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), cell_style) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_LIGHT),
        ('TEXTCOLOR', (0, 0), (-1, 0), TEXT_PRIMARY),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 3*mm),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3*mm),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, BORDER),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_SURFACE))
        else:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_PAGE))
        style_commands.append(('LINEBELOW', (0, i), (-1, i), 0.5, BORDER))
    t.setStyle(TableStyle(style_commands))
    return t


def step_item(number, text):
    badge_style = ParagraphStyle(
        'Badge', fontName='Inter-Bold', fontSize=10, leading=14,
        textColor=TEXT_INVERSE, alignment=TA_CENTER,
    )
    text_style = STYLES['step_text']
    badge_para = Paragraph(str(number), badge_style)
    text_para = Paragraph(text, text_style)
    badge_table = Table(
        [[badge_para]],
        colWidths=[18*pt], rowHeights=[18*pt],
    )
    badge_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), PRIMARY),
        ('ROUNDEDCORNERS', [9, 9, 9, 9]),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('TOPPADDING', (0, 0), (0, 0), 1),
        ('BOTTOMPADDING', (0, 0), (0, 0), 1),
        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 0),
    ]))
    row = Table(
        [[badge_table, text_para]],
        colWidths=[30*pt, CONTENT_W - 30*pt],
    )
    row.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return row


def diagram_with_caption(filename, caption_text, width=None):
    path = os.path.join(DIAGRAM_DIR, filename)
    if not os.path.exists(path):
        return [body(f"[Diagram not found: {filename}]")]
    from PIL import Image as PILImage
    pil_img = PILImage.open(path)
    aspect = pil_img.height / pil_img.width
    if width is None:
        width = CONTENT_W
    height = width * aspect
    img = Image(path, width=width, height=height)
    img.hAlign = 'CENTER'
    caption = Paragraph(caption_text, STYLES['caption'])
    return [img, spacer(3), caption]


# ─── Diagram placement config ───
# Maps chapter number -> list of (insert_after_heading, diagram_file, caption)
CHAPTER_DIAGRAMS = {
    1: [
        ("What Counts as", "edition_01_diagram_03.png",
         "Figure: AI touches dozens of everyday interactions"),
        ("AI Is a Megaphone", "edition_01_diagram_09.png",
         "Figure: AI as a multiplier for existing skills"),
    ],
    3: [
        ("The Thermostat", "edition_01_diagram_07.png",
         "Figure: How a thermostat illustrates the difference"),
        ("So What Makes AI Different", "edition_01_diagram_01.png",
         "Figure: AI vs regular software"),
    ],
    4: [
        ("How AI Learns", "edition_01_diagram_06.png",
         "Figure: The AI learning process"),
    ],
    5: [
        ("Types of AI", "edition_01_diagram_04.png",
         "Figure: The spectrum of AI types"),
    ],
    6: [
        ("Three Convergences", "edition_01_diagram_02.png",
         "Figure: The three convergences that made AI accessible"),
        ("Timeline", "edition_01_diagram_05.png",
         "Figure: Key moments in AI history"),
    ],
    11: [
        ("Myth", "edition_01_diagram_08.png",
         "Figure: AI myths vs reality"),
    ],
    13: [
        ("Learning Path", "edition_01_diagram_10.png",
         "Figure: Your AI learning roadmap"),
    ],
}


# ─── Text processing utilities ───

def escape_xml(text):
    """Escape text for ReportLab XML, preserving intentional tags."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def format_inline(text):
    """Convert markdown inline formatting to ReportLab XML.
    Handles **bold**, *italic*, and escapes XML special chars.
    """
    # First escape XML special characters
    text = escape_xml(text)

    # Convert -- to em dash
    text = text.replace(" -- ", " \u2014 ")

    # Bold: **text** -> <b>text</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)

    # Italic: *text* -> <i>text</i>
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)

    return text


# ─── Markdown Parser ───

def parse_markdown_to_elements(md_text, styles, chapter_num=0):
    """Convert a markdown chapter file into a list of ReportLab flowables."""
    lines = md_text.split('\n')
    elements = []
    i = 0
    last_heading = ""

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Horizontal rule / section divider
        if stripped == '---':
            elements.append(section_divider())
            i += 1
            # Check if we should insert a diagram after a heading
            continue

        # Chapter title: # Heading
        if stripped.startswith('# ') and not stripped.startswith('## '):
            heading_text = format_inline(stripped[2:].strip())
            elements.append(h1(heading_text))
            last_heading = stripped[2:].strip()
            i += 1
            _maybe_insert_diagrams(elements, chapter_num, last_heading)
            continue

        # H2: ## Heading
        if stripped.startswith('## '):
            heading_text = format_inline(stripped[3:].strip())
            elements.append(h2(heading_text))
            last_heading = stripped[3:].strip()
            i += 1
            _maybe_insert_diagrams(elements, chapter_num, last_heading)
            continue

        # H3: ### Heading
        if stripped.startswith('### '):
            heading_text = format_inline(stripped[4:].strip())
            elements.append(h3(heading_text))
            last_heading = stripped[4:].strip()
            i += 1
            _maybe_insert_diagrams(elements, chapter_num, last_heading)
            continue

        # Blockquote / callout boxes
        if stripped.startswith('> '):
            block_lines = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                block_lines.append(lines[i].strip()[2:].strip())
                i += 1

            block_text = ' '.join(block_lines)

            # Determine callout type
            if block_text.startswith('**DID YOU KNOW?**'):
                content = block_text[len('**DID YOU KNOW?**'):].strip()
                elements.append(spacer(2))
                elements.append(did_you_know(format_inline(content)))
                elements.append(spacer(2))
            elif block_text.startswith('**KEY FACT**'):
                content = block_text[len('**KEY FACT**'):].strip()
                elements.append(spacer(2))
                elements.append(key_fact(format_inline(content)))
                elements.append(spacer(2))
            elif block_text.startswith('**IN THE REAL WORLD**'):
                content = block_text[len('**IN THE REAL WORLD**'):].strip()
                elements.append(spacer(2))
                elements.append(real_world(format_inline(content)))
                elements.append(spacer(2))
            elif block_text.startswith('**WATCH OUT**'):
                content = block_text[len('**WATCH OUT**'):].strip()
                elements.append(spacer(2))
                elements.append(watch_out(format_inline(content)))
                elements.append(spacer(2))
            else:
                # Generic blockquote as pull quote
                elements.append(pull_quote(format_inline(block_text)))
            continue

        # Table: lines starting with |
        if stripped.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                elements.append(spacer(2))
                elements.append(_parse_table(table_lines))
                elements.append(spacer(2))
            continue

        # Bullet list: - text
        if stripped.startswith('- '):
            bullet_text = format_inline(stripped[2:].strip())
            elements.append(bullet(bullet_text))
            i += 1
            continue

        # Numbered list: 1. text (check for step items)
        num_match = re.match(r'^(\d+)\.\s+(.+)', stripped)
        if num_match:
            num = int(num_match.group(1))
            item_text = format_inline(num_match.group(2))
            # Use step_item for numbered lists with bold content
            if '**' in lines[i] or '<b>' in item_text:
                elements.append(step_item(num, item_text))
            else:
                elements.append(step_item(num, item_text))
            i += 1
            continue

        # Italic-only line (teaser at end of chapter): *text*
        if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
            teaser_text = format_inline(stripped)
            elements.append(spacer(2))
            elements.append(Paragraph(teaser_text, styles['teaser']))
            i += 1
            continue

        # Regular paragraph
        # Collect consecutive non-special lines into one paragraph
        para_lines = []
        while i < len(lines):
            cur = lines[i].strip()
            if not cur:
                i += 1
                break
            if cur == '---':
                break
            if cur.startswith('#'):
                break
            if cur.startswith('> '):
                break
            if cur.startswith('|'):
                break
            if cur.startswith('- '):
                break
            if re.match(r'^\d+\.\s+', cur):
                break
            if cur.startswith('*') and cur.endswith('*') and not cur.startswith('**'):
                break
            para_lines.append(cur)
            i += 1

        if para_lines:
            full_text = ' '.join(para_lines)
            elements.append(body(format_inline(full_text)))

    return elements


def _maybe_insert_diagrams(elements, chapter_num, heading):
    """Insert diagrams after matching headings."""
    if chapter_num not in CHAPTER_DIAGRAMS:
        return
    for trigger, filename, caption in CHAPTER_DIAGRAMS[chapter_num]:
        if trigger.lower() in heading.lower():
            elements.append(spacer(4))
            elements.extend(diagram_with_caption(filename, caption))
            elements.append(spacer(2))


def _parse_table(table_lines):
    """Parse markdown table lines into a make_table() call."""
    # First line: headers
    headers = [cell.strip() for cell in table_lines[0].strip('|').split('|')]
    headers = [format_inline(h) for h in headers]

    # Skip separator line (second line with ---)
    rows = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        cells = [format_inline(c) for c in cells]
        rows.append(cells)

    return make_table(headers, rows)


# ─── Cover Page ───

def draw_cover(canvas, doc):
    """Draw the cover page with cover image or fallback."""
    canvas.saveState()

    # Dark background for bottom 40%
    text_zone_h = PAGE_H * 0.40
    canvas.setFillColor(BG_DARK)
    canvas.rect(0, 0, PAGE_W, text_zone_h, fill=1, stroke=0)

    # Top 60%: cover image or fallback
    image_zone_h = PAGE_H * 0.60
    cover_path = os.path.join(COVER_DIR, "edition_01_cover.png")

    if os.path.exists(cover_path):
        # Use the generated cover image
        canvas.drawImage(
            cover_path, 0, text_zone_h, PAGE_W, image_zone_h,
            preserveAspectRatio=True, anchor='c', mask='auto',
        )
    else:
        # Fallback: light warm background with network drawing
        canvas.setFillColor(HexColor("#F2D4C8"))
        canvas.rect(0, text_zone_h, PAGE_W, image_zone_h, fill=1, stroke=0)

        canvas.setStrokeColor(HexColor("#CC785C"))
        canvas.setFillColor(HexColor("#FFFFFF"))
        canvas.setLineWidth(2)

        cx, cy = PAGE_W / 2, text_zone_h + image_zone_h * 0.5
        nodes = []
        for idx in range(8):
            angle = idx * math.pi * 2 / 8
            r = 120
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            nodes.append((x, y))
            canvas.circle(x, y, 18, fill=1, stroke=1)

        canvas.setFillColor(PRIMARY)
        canvas.circle(cx, cy, 30, fill=1, stroke=0)
        canvas.setFillColor(HexColor("#FFFFFF"))
        canvas.setFont('Inter-Bold', 16)
        canvas.drawCentredString(cx, cy - 6, "AI")

        canvas.setStrokeColor(HexColor("#CC785C"))
        canvas.setLineWidth(1.5)
        for nx, ny in nodes:
            canvas.line(cx, cy, nx, ny)
        for idx in range(len(nodes)):
            j = (idx + 1) % len(nodes)
            canvas.setStrokeAlpha(0.3)
            canvas.line(nodes[idx][0], nodes[idx][1], nodes[j][0], nodes[j][1])
        canvas.setStrokeAlpha(1.0)

        for idx in range(16):
            angle = idx * math.pi * 2 / 16
            r = 180
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            canvas.setFillColor(PRIMARY_LIGHT)
            canvas.circle(x, y, 6, fill=1, stroke=0)

    # Text in dark zone
    pad = 22 * mm
    text_y = text_zone_h - 40

    # Series name
    canvas.setFillColor(TEXT_INVERSE)
    canvas.setFont('Inter-Regular', 14)
    canvas.drawString(pad, text_y, "AI Education Series by Kelvin M")

    # Book title
    text_y -= 55
    canvas.setFillColor(ACCENT_CORAL)
    canvas.setFont('Inter-Bold', 36)
    canvas.drawString(pad, text_y, "The AI Basics")
    text_y -= 44
    canvas.drawString(pad, text_y, "Nobody Made Clear")

    # Subtitle
    text_y -= 35
    canvas.setFillColor(TEXT_INVERSE)
    canvas.setFont('Inter-Italic', 11)
    canvas.drawString(pad, text_y, "A Beginner's Guide to AI")

    # Author
    text_y -= 30
    canvas.setFillColor(TEXT_MUTED)
    canvas.setFont('Inter-Medium', 12)
    canvas.drawString(pad, text_y, "by Kelvin M \u2014 AI Educator & Researcher")

    canvas.restoreState()


def draw_footer(canvas, doc):
    """Draw footer on content pages."""
    canvas.saveState()
    y = MARGIN_BOTTOM - 6*mm
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LEFT, y + 8*mm, PAGE_W - MARGIN_RIGHT, y + 8*mm)
    canvas.setFillColor(TEXT_MUTED)
    canvas.setFont('Inter-Regular', 8)
    canvas.drawString(MARGIN_LEFT, y, "The AI Basics Nobody Made Clear \u2014 by Kelvin M")
    canvas.setFont('Inter-Medium', 9)
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, y, str(doc.page))
    canvas.restoreState()


def on_first_page(canvas, doc):
    draw_cover(canvas, doc)


def on_later_pages(canvas, doc):
    draw_footer(canvas, doc)


# ─── Chapter titles for TOC ───

CHAPTER_TITLES = [
    "You Already Use AI",
    "What AI Actually Means",
    "AI vs Regular Software",
    "How AI Learns",
    "Types of AI",
    "Why AI Exploded Now",
    "Your First AI Conversation",
    "The Art of Prompting",
    "Building Your AI Workflow",
    "What AI Gets Wrong",
    "AI Myths vs Reality",
    "How AI Fits Into Work and School",
    "Your AI Starter Toolkit",
    "The Ethics of AI",
    "Where You Go from Here",
]


# ─── Build the document ───

def build():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        title="The AI Basics Nobody Made Clear",
        author="Kelvin M",
        subject="AI Education for Complete Beginners",
        creator="AI Education PDF Series Build System v3.0",
    )

    elements = []

    # ═══ COVER PAGE (drawn by on_first_page callback) ═══
    elements.append(Spacer(1, 1))
    elements.append(PageBreak())

    # ═══ TITLE PAGE ═══
    elements.append(spacer(40))
    elements.append(Paragraph(
        "The AI Basics Nobody Made Clear",
        STYLES['cover_title'],
    ))
    elements.append(spacer(6))
    elements.append(Paragraph(
        "A Beginner\u2019s Guide to AI",
        ParagraphStyle('SubTitle', fontName='Inter-Medium', fontSize=16,
                       leading=22, textColor=TEXT_SECONDARY, alignment=TA_LEFT),
    ))
    elements.append(spacer(10))
    elements.append(Paragraph(
        "by Kelvin M \u2014 AI Educator &amp; Researcher",
        STYLES['cover_author'],
    ))
    elements.append(PageBreak())

    # ═══ TABLE OF CONTENTS ═══
    elements.append(h1("Table of Contents"))
    elements.append(spacer(4))
    for idx, title in enumerate(CHAPTER_TITLES, 1):
        toc_text = f"{idx:2d}.  {title}"
        elements.append(Paragraph(toc_text, STYLES['toc_item']))
    elements.append(PageBreak())

    # ═══ CHAPTERS ═══
    for i in range(1, 16):
        chapter_path = os.path.join(CHAPTER_DIR, f"chapter_{i:02d}.md")
        if not os.path.exists(chapter_path):
            elements.append(body(f"[Chapter {i} file not found]"))
            elements.append(PageBreak())
            continue

        with open(chapter_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        chapter_elements = parse_markdown_to_elements(md_text, STYLES, chapter_num=i)
        elements.extend(chapter_elements)
        elements.append(PageBreak())

    # ═══ BUILD ═══
    print(f"Building PDF: {OUTPUT_FILE}")
    doc.build(elements, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"Done! PDF saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    build()
