"""
Circuit Glow Theme Preview — 3 pages: cover, title, sample chapter page.
"""
import os
import math
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable, Flowable
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
pt = 1
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
COVER_DIR = os.path.join(BASE_DIR, "assets", "covers")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "theme_preview.pdf")

# ─── Circuit Glow Palette ───
NAVY = HexColor("#2D2640")
NAVY_LIGHT = HexColor("#3D3555")
ORANGE = HexColor("#E8834A")
ORANGE_LIGHT = HexColor("#FDF0E8")
GOLD = HexColor("#E9A84C")
GOLD_LIGHT = HexColor("#FDF5E6")
TEAL = HexColor("#2A9D8F")
TEAL_LIGHT = HexColor("#E6F5F3")
CORAL = HexColor("#E76F51")
CORAL_LIGHT = HexColor("#FDEDEA")
GREEN = HexColor("#57A773")
GREEN_LIGHT = HexColor("#EAF5EE")

BG_PAGE = HexColor("#FFFFFF")
BG_SURFACE = HexColor("#F5F3F0")
TEXT_PRIMARY = HexColor("#1A1A1A")
TEXT_SECONDARY = HexColor("#4A4A4A")
TEXT_MUTED = HexColor("#888888")
TEXT_INVERSE = HexColor("#FFFFFF")
BORDER = HexColor("#E0D9D4")

PAGE_W, PAGE_H = A4
MARGIN_TOP = 20 * mm
MARGIN_BOTTOM = 20 * mm
MARGIN_LEFT = 22 * mm
MARGIN_RIGHT = 22 * mm
CONTENT_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

pdfmetrics.registerFont(TTFont('Inter-Regular', os.path.join(FONT_DIR, 'Inter-Regular.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Medium', os.path.join(FONT_DIR, 'Inter-Medium.ttf')))
pdfmetrics.registerFont(TTFont('Inter-SemiBold', os.path.join(FONT_DIR, 'Inter-SemiBold.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Bold', os.path.join(FONT_DIR, 'Inter-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Inter-Italic', os.path.join(FONT_DIR, 'Inter-Italic.ttf')))


# ─── Chapter Banner Flowable ───
class ChapterBanner(Flowable):
    """Dark navy banner with white chapter title and teal accent line."""
    def __init__(self, chapter_num, chapter_title, width=None):
        Flowable.__init__(self)
        self.chapter_num = chapter_num
        self.chapter_title = chapter_title
        self.width = width or CONTENT_W
        self.height = 38 * mm

    def draw(self):
        c = self.canv
        # Navy banner — extend to page edges
        overshoot = MARGIN_LEFT
        c.setFillColor(NAVY)
        c.roundRect(-overshoot, 0, self.width + overshoot + MARGIN_RIGHT,
                     self.height, 0, fill=1, stroke=0)

        # Teal accent line at bottom
        c.setStrokeColor(TEAL)
        c.setLineWidth(2.5)
        c.line(-overshoot, 0, self.width + MARGIN_RIGHT, 0)

        # Chapter number (gold)
        c.setFillColor(GOLD)
        c.setFont('Inter-Medium', 12)
        c.drawString(8, self.height - 14, f"CHAPTER {self.chapter_num}")

        # Chapter title (white)
        c.setFillColor(TEXT_INVERSE)
        c.setFont('Inter-Bold', 24)
        c.drawString(8, 10)  # placeholder
        # Use a paragraph for wrapping
        from reportlab.platypus import Paragraph as P
        style = ParagraphStyle('BT', fontName='Inter-Bold', fontSize=24,
                               leading=28, textColor=TEXT_INVERSE)
        p = P(self.chapter_title, style)
        w, h = p.wrap(self.width - 16, self.height)
        p.drawOn(c, 8, 6)


# ─── Styles ───

def make_styles():
    s = {}
    # H1: orange text with navy left bar
    s['h1'] = ParagraphStyle(
        'H1', fontName='Inter-Bold', fontSize=22, leading=26.4,
        textColor=ORANGE, spaceBefore=8*mm, spaceAfter=4*mm,
    )
    # H2: gold
    s['h2'] = ParagraphStyle(
        'H2', fontName='Inter-SemiBold', fontSize=17, leading=20.4,
        textColor=GOLD, spaceBefore=6*mm, spaceAfter=3*mm,
    )
    # H3: teal
    s['h3'] = ParagraphStyle(
        'H3', fontName='Inter-Medium', fontSize=14, leading=16.8,
        textColor=TEAL, spaceBefore=4*mm, spaceAfter=2*mm,
    )
    s['body'] = ParagraphStyle(
        'Body', fontName='Inter-Regular', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, spaceAfter=3*mm, alignment=TA_JUSTIFY,
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
    s['toc_num'] = ParagraphStyle(
        'TOCNum', fontName='Inter-Bold', fontSize=12, leading=18,
        textColor=GOLD,
    )
    s['toc_item'] = ParagraphStyle(
        'TOCItem', fontName='Inter-Regular', fontSize=11, leading=18,
        textColor=NAVY, leftIndent=8, spaceAfter=1*mm,
    )
    s['step_text'] = ParagraphStyle(
        'StepText', fontName='Inter-Regular', fontSize=11, leading=15.4,
        textColor=TEXT_PRIMARY, leftIndent=10*mm, spaceAfter=4*mm,
    )
    s['pull_quote'] = ParagraphStyle(
        'PullQuote', fontName='Inter-SemiBold', fontSize=14, leading=20,
        textColor=TEXT_INVERSE, alignment=TA_LEFT,
    )
    return s


STYLES = make_styles()


# ─── Helpers ───

def spacer(h_mm=4):
    return Spacer(1, h_mm * mm)


def section_divider():
    return HRFlowable(
        width="40%", thickness=1.5, color=TEAL,
        spaceAfter=4*mm, spaceBefore=4*mm, hAlign='CENTER',
    )


def callout_box(label_text, body_text, border_color, label_color, bg_color):
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
        ('BACKGROUND', (0, 0), (-1, -1), bg_color),
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
        ('LINEBEFOREDECOR', (0, 0), (0, -1), 2.5, border_color),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return outer


def pull_quote_box(text):
    """Navy background pull quote with orange left bar."""
    style = ParagraphStyle(
        'PQ', fontName='Inter-SemiBold', fontSize=13, leading=19,
        textColor=TEXT_INVERSE, alignment=TA_LEFT,
    )
    para = Paragraph(f"\u201c{text}\u201d", style)
    t = Table([[para]], colWidths=[CONTENT_W - 16*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 10*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 10*mm),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8*mm),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    outer = Table([[t]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ('LINEBEFOREDECOR', (0, 0), (0, -1), 3, ORANGE),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return outer


def make_table(headers, rows, col_widths=None):
    if col_widths is None:
        n = len(headers)
        col_widths = [CONTENT_W / n] * n
    header_style = ParagraphStyle('TH', fontName='Inter-SemiBold', fontSize=10,
                                   leading=14, textColor=TEXT_INVERSE)
    cell_style = ParagraphStyle('TD', fontName='Inter-Regular', fontSize=10,
                                 leading=14, textColor=TEXT_PRIMARY)
    data = [[Paragraph(h, header_style) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), cell_style) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_commands = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), TEXT_INVERSE),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 3*mm),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3*mm),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, TEAL),
        ('LINEBELOW', (0, -1), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_SURFACE))
        else:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_PAGE))
        style_commands.append(('LINEBELOW', (0, i), (-1, i), 0.5, BORDER))
    # Gold left accent
    style_commands.append(('LINEBEFOREDECOR', (0, 0), (0, -1), 2, GOLD))
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
        ('BACKGROUND', (0, 0), (0, 0), NAVY),
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


# ─── Cover + Footer ───

def draw_cover(canvas, doc):
    canvas.saveState()
    cover_path = os.path.join(COVER_DIR, "Final Cover page.png")
    if os.path.exists(cover_path):
        canvas.drawImage(cover_path, 0, 0, PAGE_W, PAGE_H,
                         preserveAspectRatio=False, mask='auto')
    else:
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


def draw_footer(canvas, doc):
    canvas.saveState()
    y = MARGIN_BOTTOM - 6*mm
    # Navy top line
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LEFT, y + 8*mm, PAGE_W - MARGIN_RIGHT, y + 8*mm)
    # Series name
    canvas.setFillColor(TEXT_MUTED)
    canvas.setFont('Inter-Regular', 8)
    canvas.drawString(MARGIN_LEFT, y, "What is AI? \u2014 AI Education Series by Kelvin M")
    # Teal page number
    canvas.setFillColor(TEAL)
    canvas.setFont('Inter-Medium', 9)
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, y, str(doc.page))
    canvas.restoreState()


def on_first_page(canvas, doc):
    draw_cover(canvas, doc)

def on_later_pages(canvas, doc):
    draw_footer(canvas, doc)


# ─── Chapter Banner (implemented as a simpler approach) ───

class ChapterBannerFlowable(Flowable):
    """Full-width navy banner for chapter openers."""
    def __init__(self, chapter_num, chapter_title):
        Flowable.__init__(self)
        self.chapter_num = chapter_num
        self.chapter_title = chapter_title
        self.width = CONTENT_W
        self.height = 32 * mm
        self.spaceAfter = 6 * mm

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        overshoot = MARGIN_LEFT
        total_w = self.width + overshoot + MARGIN_RIGHT

        # Navy background
        c.setFillColor(NAVY)
        c.roundRect(-overshoot, 0, total_w, self.height, 0, fill=1, stroke=0)

        # Teal accent line at bottom
        c.setStrokeColor(TEAL)
        c.setLineWidth(2.5)
        c.line(-overshoot, 0, -overshoot + total_w, 0)

        # Chapter number in gold
        c.setFillColor(GOLD)
        c.setFont('Inter-Medium', 11)
        c.drawString(6, self.height - 12, f"CHAPTER {self.chapter_num}")

        # Chapter title in white
        c.setFillColor(TEXT_INVERSE)
        c.setFont('Inter-Bold', 22)
        c.drawString(6, 8, self.chapter_title)


# ─── Build Preview ───

def build():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        title="Circuit Glow Theme Preview",
        author="Kelvin M",
    )

    elements = []

    # ═══ PAGE 1: COVER ═══
    elements.append(Spacer(1, 1))
    elements.append(PageBreak())

    # ═══ PAGE 2: TITLE PAGE ═══
    elements.append(spacer(40))
    elements.append(Paragraph(
        "AI EDUCATION SERIES \u2014 EDITION 01",
        ParagraphStyle('SeriesLabel', fontName='Inter-Medium', fontSize=12,
                       leading=16, textColor=GOLD, spaceAfter=4*mm),
    ))
    elements.append(Paragraph(
        "What is AI?",
        ParagraphStyle('Title', fontName='Inter-Bold', fontSize=42, leading=50,
                       textColor=NAVY),
    ))
    elements.append(spacer(4))
    elements.append(Paragraph(
        "The complete beginner\u2019s guide to understanding artificial intelligence",
        ParagraphStyle('Sub', fontName='Inter-Regular', fontSize=14, leading=20,
                       textColor=TEXT_SECONDARY),
    ))
    elements.append(spacer(10))
    elements.append(Paragraph(
        "by Kelvin M \u2014 AI Educator &amp; Researcher",
        ParagraphStyle('Auth', fontName='Inter-Medium', fontSize=12, leading=16,
                       textColor=TEXT_MUTED),
    ))
    elements.append(spacer(20))

    # TOC preview
    elements.append(Paragraph("Table of Contents", STYLES['h1']))
    elements.append(spacer(3))
    toc_chapters = [
        "You Already Use AI", "What AI Actually Means", "AI vs Regular Software",
        "How AI Learns", "Types of AI", "Why AI Exploded Now",
    ]
    for idx, title in enumerate(toc_chapters, 1):
        toc_style = ParagraphStyle('TOC', fontName='Inter-Regular', fontSize=11,
                                    leading=18, textColor=NAVY, leftIndent=8, spaceAfter=1*mm)
        elements.append(Paragraph(
            f"<font color='#E9A84C'><b>{idx:2d}.</b></font>  {title}", toc_style
        ))
    elements.append(Paragraph("...", STYLES['body']))

    elements.append(PageBreak())

    # ═══ PAGE 3+: SAMPLE CHAPTER ═══

    # Chapter banner
    elements.append(ChapterBannerFlowable(1, "You Already Use AI"))
    elements.append(spacer(4))

    # H2
    elements.append(Paragraph("This Is Not the Future. This Is Right Now", STYLES['h2']))
    elements.append(Paragraph(
        "That story might sound unusual. It is not. Here are more people who "
        "shared their experiences with AI publicly, in their own words, within "
        "the past few months.",
        STYLES['body'],
    ))

    # H3
    elements.append(Paragraph("Real People, Real Results", STYLES['h3']))
    elements.append(Paragraph(
        "A fifty-four-year-old business consultant with zero coding experience "
        "built six working AI assistants in just three weeks. Not because he "
        "suddenly became a programmer, but because AI itself helped him learn.",
        STYLES['body'],
    ))

    # Bullets
    elements.append(Paragraph(
        "\u2022  AI is already part of your daily life through your phone, email, maps, and streaming",
        STYLES['bullet'],
    ))
    elements.append(Paragraph(
        "\u2022  Real people, not tech experts, are using AI to transform their work",
        STYLES['bullet'],
    ))
    elements.append(Paragraph(
        "\u2022  Most people have not started yet \u2014 and that gap is your opportunity",
        STYLES['bullet'],
    ))

    elements.append(spacer(2))

    # Table
    elements.append(make_table(
        ["Where You Are", "What AI Does", "You Might Not Have Known"],
        [
            ["Phone keyboard", "Predicts your next word", "Adapts to YOUR writing style over time"],
            ["Email inbox", "Filters spam, suggests replies", "Oldest AI system still running: 20+ years"],
            ["Streaming", "Recommends what to watch", "Every item in your feed was chosen by AI"],
            ["Maps", "Reroutes you around traffic", "Analyses millions of drivers' phones in real time"],
        ]
    ))

    elements.append(spacer(3))

    # Steps
    elements.append(Paragraph("Your First Three Steps", STYLES['h2']))
    elements.append(step_item(1, "<b>Open any AI tool</b> \u2014 ChatGPT, Claude, or Gemini. All are free to start."))
    elements.append(step_item(2, "<b>Ask a real question</b> \u2014 something you would normally search for on Google."))
    elements.append(step_item(3, "<b>Compare the result</b> \u2014 is the AI answer more useful than a list of links?"))

    elements.append(spacer(2))

    # Pull quote
    elements.append(pull_quote_box(
        "You do not need to understand how a car engine works to drive to the shops. "
        "You just need to know where you want to go."
    ))

    elements.append(spacer(3))

    # Section divider
    elements.append(section_divider())

    # Callout boxes
    elements.append(callout_box(
        "DID YOU KNOW?",
        "Your email spam filter is one of the oldest AI systems in everyday use. "
        "It has been learning what spam looks like for over twenty years.",
        TEAL, TEAL, TEAL_LIGHT,
    ))
    elements.append(spacer(3))
    elements.append(callout_box(
        "KEY FACT",
        "Government data shows that fewer than one in five American businesses "
        "use AI in any meaningful way. The biggest barrier is the skills gap.",
        GOLD, GOLD, GOLD_LIGHT,
    ))
    elements.append(spacer(3))
    elements.append(callout_box(
        "IN THE REAL WORLD",
        "A forty-three-year-old consultant with no coding experience built an AI "
        "system that runs his morning operations automatically in thirty-six hours.",
        GREEN, GREEN, GREEN_LIGHT,
    ))
    elements.append(spacer(3))
    elements.append(callout_box(
        "WATCH OUT",
        "AI can produce confident, articulate, completely wrong answers. This is "
        "called hallucination. Always verify factual claims independently.",
        CORAL, CORAL, CORAL_LIGHT,
    ))

    # Build
    print(f"Building preview: {OUTPUT_FILE}")
    doc.build(elements, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"Done! Preview saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    build()
