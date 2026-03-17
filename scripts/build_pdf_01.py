"""
Build PDF for Edition 01 — What is AI?
Full production build following STYLE_TOKENS.yaml and DESIGN_GUIDELINES.md
"""

import os
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
pt = 1  # ReportLab uses points as native unit
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

# ─── Paths ───
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
DIAGRAM_DIR = os.path.join(BASE_DIR, "assets", "diagrams")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "edition_01_what-is-ai_v1.0.pdf")

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
PAGE_W, PAGE_H = A4  # 595.28 x 841.89
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


def callout_box(label_text, body_text, border_color, label_color):
    """Build a callout box as a styled table with left border."""
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

    # Wrap in outer table for left border effect
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
    """Build a styled data table."""
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

    # Alternating row backgrounds
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_SURFACE))
        else:
            style_commands.append(('BACKGROUND', (0, i), (-1, i), BG_PAGE))
        style_commands.append(('LINEBELOW', (0, i), (-1, i), 0.5, BORDER))

    t.setStyle(TableStyle(style_commands))
    return t


def step_item(number, text):
    """Build a step with numbered badge."""
    badge_style = ParagraphStyle(
        'Badge', fontName='Inter-Bold', fontSize=10, leading=14,
        textColor=TEXT_INVERSE, alignment=TA_CENTER,
    )
    text_style = STYLES['step_text']

    badge_para = Paragraph(str(number), badge_style)
    text_para = Paragraph(text, text_style)

    # Create a table with badge column and text column
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


def diagram_image(filename, caption_text, width=None):
    """Insert a diagram image with caption."""
    path = os.path.join(DIAGRAM_DIR, filename)
    if width is None:
        width = CONTENT_W
    img = Image(path, width=width, height=width * 0.46)  # Approximate aspect ratio
    img.hAlign = 'CENTER'
    caption = Paragraph(caption_text, STYLES['caption'])
    return [img, spacer(3), caption]


# ─── Cover Page ───

def draw_cover(canvas, doc):
    """Draw the cover page."""
    canvas.saveState()

    # Dark background for bottom 40%
    text_zone_h = PAGE_H * 0.40
    canvas.setFillColor(BG_DARK)
    canvas.rect(0, 0, PAGE_W, text_zone_h, fill=1, stroke=0)

    # Top 60%: light warm background (placeholder for cover art)
    image_zone_h = PAGE_H * 0.60
    canvas.setFillColor(HexColor("#F2D4C8"))
    canvas.rect(0, text_zone_h, PAGE_W, image_zone_h, fill=1, stroke=0)

    # Draw decorative AI-themed elements in image zone
    # Abstract circles and nodes
    import math
    canvas.setStrokeColor(HexColor("#CC785C"))
    canvas.setFillColor(HexColor("#FFFFFF"))
    canvas.setLineWidth(2)

    # Central brain-like network
    cx, cy = PAGE_W / 2, text_zone_h + image_zone_h * 0.5
    nodes = []
    for i in range(8):
        angle = i * math.pi * 2 / 8
        r = 120
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        nodes.append((x, y))
        canvas.circle(x, y, 18, fill=1, stroke=1)

    # Center node
    canvas.setFillColor(PRIMARY)
    canvas.circle(cx, cy, 30, fill=1, stroke=0)
    canvas.setFillColor(HexColor("#FFFFFF"))
    canvas.setFont('Inter-Bold', 16)
    canvas.drawCentredString(cx, cy - 6, "AI")

    # Connect nodes
    canvas.setStrokeColor(HexColor("#CC785C"))
    canvas.setLineWidth(1.5)
    for nx, ny in nodes:
        canvas.line(cx, cy, nx, ny)
    # Connect adjacent nodes
    for i in range(len(nodes)):
        j = (i + 1) % len(nodes)
        canvas.setStrokeAlpha(0.3)
        canvas.line(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])

    canvas.setStrokeAlpha(1.0)

    # Outer ring
    for i in range(16):
        angle = i * math.pi * 2 / 16
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

    # Edition title
    text_y -= 55
    canvas.setFillColor(PRIMARY)
    canvas.setFont('Inter-Bold', 36)
    canvas.drawString(pad, text_y, "Edition 01")

    text_y -= 44
    canvas.drawString(pad, text_y, "What is AI?")

    # Tagline
    text_y -= 35
    canvas.setFillColor(TEXT_INVERSE)
    canvas.setFont('Inter-Italic', 11)
    canvas.drawString(pad, text_y, "Making artificial intelligence accessible to everyone")

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
    # Top border line
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LEFT, y + 8*mm, PAGE_W - MARGIN_RIGHT, y + 8*mm)
    # Series name left
    canvas.setFillColor(TEXT_MUTED)
    canvas.setFont('Inter-Regular', 8)
    canvas.drawString(MARGIN_LEFT, y, "AI Education Series by Kelvin M")
    # Page number right
    canvas.setFont('Inter-Medium', 9)
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, y, str(doc.page))
    canvas.restoreState()


def on_first_page(canvas, doc):
    """Cover page — no footer."""
    draw_cover(canvas, doc)


def on_later_pages(canvas, doc):
    """Content pages — footer only."""
    draw_footer(canvas, doc)


# ─── Build the document ───

def build():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        title="Edition 01 — What is AI?",
        author="Kelvin M",
        subject="AI Education for Complete Beginners",
        creator="AI Education PDF Series Build System",
    )

    elements = []

    # ─── COVER PAGE (empty frame, drawn by on_first_page) ───
    # Use a small spacer — the cover is drawn by on_first_page callback
    elements.append(Spacer(1, 1))
    elements.append(PageBreak())

    # ─── LEARNING OBJECTIVES ───
    elements.append(h1("Learning Objectives"))
    elements.append(body("By the end of this edition, you will be able to:"))
    elements.append(spacer(2))

    objectives = [
        "Define artificial intelligence in one clear sentence that anyone can understand.",
        "Identify at least five ways AI already shows up in your daily life.",
        "Explain the key difference between AI and regular software.",
        "Describe why AI suddenly became accessible to everyone.",
        "Take your first step using an AI tool with confidence.",
    ]
    for obj in objectives:
        elements.append(Paragraph(f"\u2022  {obj}", STYLES['objectives']))

    elements.append(spacer(4))

    # ─── TABLE OF CONTENTS ───
    elements.append(h1("Table of Contents"))
    toc_items = [
        "1.  What is AI? (The One-Sentence Answer)",
        "2.  AI is Already in Your Life",
        "3.  How is AI Different from Regular Software?",
        "4.  Why is Everyone Talking About AI Now?",
        "5.  Try It Yourself: Your First AI Conversation",
        "6.  Key Takeaways",
        "7.  Glossary",
        "8.  Mini Quiz",
        "9.  Reflection Question",
        "10. What's Next",
    ]
    for item in toc_items:
        elements.append(Paragraph(item, STYLES['toc_item']))

    elements.append(PageBreak())

    # ─── HOOK / AHA MOMENT OPENER ───
    elements.append(h1("You Already Know More Than You Think"))
    elements.append(spacer(2))

    elements.append(body_lead(
        "Think about the last time you used your phone to type a message. Before you "
        "finished the word, your phone guessed what you were trying to say. It offered you "
        "the next word. Maybe it even predicted the entire sentence."
    ))

    elements.append(body(
        "You probably did not think twice about it. You tapped the suggestion and kept going."
    ))

    elements.append(body(
        "That was AI. You have already been using artificial intelligence \u2014 possibly dozens "
        "of times today \u2014 without realising it. When Netflix suggests a show you end up "
        "loving, when your email filters out spam before you see it, when your map app reroutes "
        "you around traffic in real time \u2014 all of that is AI working quietly in the background "
        "of your life."
    ))

    elements.append(body(
        "Here is the thing most people get wrong about AI: they think it is something new, "
        "something complicated, something that requires a computer science degree to understand. "
        "It is none of those things. AI has been around since the 1950s. What changed is not AI "
        "itself \u2014 it is that AI finally became powerful enough and simple enough for ordinary "
        "people like you and me to use it directly."
    ))

    elements.append(body(
        "One of the most common feelings people have about AI is being overwhelmed. New AI tools, "
        "updates, and announcements come out almost every day, and it can feel like you are already "
        "falling behind before you even start. That feeling is normal \u2014 and it is also unnecessary. "
        "You do not need to know everything about AI to benefit from it. Just like you do not need to "
        "understand how a car engine works to drive to the grocery store, you do not need to understand "
        "every new AI model to use AI effectively in your life."
    ))

    elements.append(body(
        "<b>This edition is your starting line.</b> No jargon. No prerequisites. If you can read this "
        "sentence, you can understand AI."
    ))

    elements.append(spacer(4))

    # ─── SECTION 1 ───
    elements.append(h1("Section 1: What is AI?"))
    elements.append(h2("The One-Sentence Answer"))
    elements.append(spacer(2))

    elements.append(body(
        "<b>Artificial intelligence is software that learns from examples instead of following "
        "fixed instructions.</b>"
    ))

    elements.append(body(
        "That is it. That is the entire concept at its core. Once you understand this single sentence, "
        "everything else in this series will build on top of it."
    ))

    elements.append(body(
        "Regular software does exactly what a programmer tells it to do. A calculator adds two numbers "
        "because someone wrote a specific rule: \"when the user presses the plus button, add these numbers "
        "together.\" The calculator cannot do anything it was not specifically programmed to do. It cannot "
        "guess what you might want to calculate next. It cannot learn your habits. It cannot get better "
        "over time. It simply follows its instructions, the same way, every single time."
    ))

    elements.append(body(
        "AI works differently. Instead of being given a rule for every possible situation, AI is given "
        "thousands \u2014 sometimes millions \u2014 of examples, and it figures out the patterns on its own. "
        "Then it uses those patterns to handle situations it has never seen before."
    ))

    elements.append(body(
        "Think of it this way: if you showed a child a thousand pictures of cats and a thousand pictures "
        "of dogs, eventually that child could tell the difference between a new cat and a new dog \u2014 even "
        "one they had never seen before. Nobody gave the child a written rule like \"cats have pointed ears "
        "and whiskers.\" The child figured out the pattern from the examples."
    ))

    elements.append(body(
        "AI does exactly the same thing, except it can process millions of examples in the time it takes "
        "you to blink."
    ))

    elements.append(body(
        "This distinction matters because it explains both AI's extraordinary power and its limitations. "
        "AI is remarkable at tasks where there are patterns to find \u2014 recognising faces in photos, "
        "translating languages, predicting what you might want to buy next. But it struggles with tasks "
        "that require genuine understanding, common sense, or creative leaps that go beyond any pattern it "
        "has ever seen. As you progress through this series, you will develop an intuition for what AI does "
        "well and where it falls short."
    ))

    elements.append(spacer(2))

    # Diagram 1
    diag1_path = os.path.join(DIAGRAM_DIR, "edition_01_diagram_01.png")
    if os.path.exists(diag1_path):
        from PIL import Image as PILImage
        pil_img = PILImage.open(diag1_path)
        aspect = pil_img.height / pil_img.width
        img_w = CONTENT_W
        img_h = img_w * aspect
        elements.append(Image(diag1_path, width=img_w, height=img_h))
        elements.append(spacer(3))
        elements.append(Paragraph(
            "Figure 1: Regular software follows fixed rules written by a programmer. "
            "AI learns patterns from examples and can handle new situations it was never "
            "specifically programmed for.",
            STYLES['caption']
        ))

    elements.append(spacer(2))

    elements.append(did_you_know(
        "The term \"artificial intelligence\" was first used in 1956 at a conference at Dartmouth College "
        "in the United States. Researchers have been working on AI for nearly 70 years \u2014 it is not "
        "the overnight sensation many people assume."
    ))

    elements.append(spacer(4))

    # ─── SECTION 2 ───
    elements.append(h1("Section 2: AI is Already in Your Life"))
    elements.append(spacer(2))

    elements.append(body(
        "Most people think AI is something futuristic \u2014 robots in factories, self-driving cars on empty "
        "test tracks, science fiction movies. But AI is already woven into the fabric of your everyday "
        "routine. You interact with it more often than you realise, and it has been this way for years."
    ))

    elements.append(body(
        "Here are real examples of AI you probably used today:"
    ))

    elements.append(spacer(2))

    # Table: AI in daily life
    elements.append(make_table(
        ["Where You Are", "What AI Does", "How It Works"],
        [
            ["Phone keyboard",
             "Predicts your next word",
             "Learned from billions of messages how people finish sentences"],
            ["Email inbox",
             "Filters spam before you see it",
             "Learned to recognise patterns that signal unwanted messages"],
            ["Streaming apps\n(Netflix, Spotify)",
             "Suggests what to watch or listen to",
             "Learned your preferences from your viewing and listening history"],
            ["Maps\n(Google Maps, Waze)",
             "Reroutes you around traffic",
             "Learned traffic patterns from millions of drivers reporting speed and location"],
            ["Social media",
             "Decides which posts appear first",
             "Learned what type of content keeps you engaged based on your behaviour"],
            ["Online shopping",
             "Shows \"you might also like\" suggestions",
             "Learned buying patterns from millions of customers with similar tastes"],
        ],
        col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.30, CONTENT_W * 0.48],
    ))

    elements.append(spacer(4))

    elements.append(body(
        "Here is a number that might surprise you: the vast majority of the world's population has never "
        "intentionally used an AI tool. Most people have interacted with AI without knowing it \u2014 through "
        "their phone, their email, their streaming apps \u2014 but they have never sat down and purposefully "
        "typed a question into an AI assistant."
    ))

    elements.append(body(
        "If you are reading this right now, you are not late. You are early. The current moment in AI is "
        "similar to the early days of the internet, when most small businesses did not even have a website "
        "and most people had never sent an email. The people who learned how the internet worked in the "
        "late 1990s had a decade-long head start. AI is in that same window right now."
    ))

    elements.append(body(
        "The people who learn AI today are the ones who will have the biggest advantage tomorrow. "
        "And here is the best part: you do not need to be a programmer, an engineer, or a maths genius "
        "to start. Some of the biggest technology companies in the world \u2014 including Google, "
        "Microsoft, and others \u2014 offer free materials and tools to help anyone get started. "
        "The door is wide open."
    ))

    elements.append(spacer(2))

    elements.append(key_fact(
        "AI is not one single technology. It is a collection of techniques that allow software to learn "
        "from data, recognise patterns, and make decisions \u2014 much like a human brain, but at machine speed."
    ))

    elements.append(spacer(4))

    # ─── SECTION 3 ───
    elements.append(h1("Section 3: How is AI Different from Regular Software?"))
    elements.append(spacer(2))

    elements.append(body(
        "This is one of the most important distinctions you will learn in this entire series, and it is "
        "simpler than you think."
    ))

    elements.append(body(
        "<b>Regular software follows rules written by humans. AI creates its own rules by studying "
        "examples.</b>"
    ))

    elements.append(body(
        "To truly understand why this matters, let us look at how they compare across five key dimensions:"
    ))

    elements.append(spacer(2))

    elements.append(make_table(
        ["", "Regular Software", "AI Software"],
        [
            ["How it learns",
             "Programmed by a human with specific instructions",
             "Trained on large amounts of data to find patterns"],
            ["Handling new situations",
             "Can only do what it was specifically told to do",
             "Can make reasonable guesses about things it has never seen"],
            ["Improving over time",
             "Stays the same until a human updates it",
             "Can get better as it sees more data"],
            ["Example",
             "Calculator \u2014 always follows the same math rules",
             "Spam filter \u2014 gets better at catching spam over time"],
            ["Best for",
             "Tasks with clear, fixed rules",
             "Tasks with patterns, preferences, or judgment calls"],
        ],
        col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.39, CONTENT_W * 0.39],
    ))

    elements.append(spacer(4))

    elements.append(body(
        "Think of a thermostat versus a smart assistant. A basic thermostat follows one rule: \"If the "
        "temperature drops below 20 degrees, turn on the heating.\" It does this forever, regardless of "
        "anything else. It does not know if you are home or away, asleep or awake, in summer or winter. "
        "It just follows its one rule, endlessly."
    ))

    elements.append(body(
        "A smart home assistant is different. It learns that you like the house warmer on weekday mornings "
        "but cooler at night. It adjusts automatically when you are away. It adapts to seasonal changes. "
        "Over time, it gets better at predicting your preferences \u2014 all without you reprogramming it. "
        "Nobody rewrites its code. It learns."
    ))

    elements.append(body(
        "That ability to learn and adapt is what makes AI fundamentally different from every piece of "
        "software that came before it. And it is why AI feels like such a big deal \u2014 because for the "
        "first time in the history of computing, software can improve itself."
    ))

    elements.append(spacer(2))

    elements.append(real_world(
        "Your email spam filter is one of the oldest and most successful AI systems in daily use. It has "
        "been learning what spam looks like for over two decades \u2014 and it catches roughly 99% of spam "
        "before you ever see it."
    ))

    elements.append(spacer(4))

    # ─── SECTION 4 ───
    elements.append(h1("Section 4: Why is Everyone Talking About AI Now?"))
    elements.append(spacer(2))

    elements.append(body(
        "If AI has existed since the 1950s, why does it feel like it appeared out of nowhere? Why were "
        "people not talking about AI ten years ago the way they are today?"
    ))

    elements.append(body(
        "The answer is that three things had to happen at the same time \u2014 and they all converged in "
        "the last few years."
    ))

    elements.append(spacer(2))

    elements.append(h2("1. Massive Amounts of Data Became Available"))
    elements.append(body(
        "The internet, social media, smartphones, and sensors created more data in the last decade than "
        "in all of previous human history combined. Every text message you send, every photo you upload, "
        "every product you browse online \u2014 all of it creates data. AI needs data the way a car needs "
        "fuel. Without enough data, AI could not learn enough to be useful. By the 2020s, there was more "
        "data available than AI could even process."
    ))

    elements.append(h2("2. Computers Became Powerful Enough"))
    elements.append(body(
        "Training AI requires enormous computing power. The kind of calculations that would have taken "
        "years in the 1990s now take hours. A critical breakthrough came from an unexpected place: "
        "graphics processing chips \u2014 originally built to render video game graphics \u2014 turned out "
        "to be perfectly suited for AI training. These chips could perform thousands of calculations "
        "simultaneously, which is exactly what AI needs. This hardware breakthrough made large-scale AI "
        "training practical and affordable for the first time."
    ))

    elements.append(h2("3. Breakthrough Methods Arrived"))
    elements.append(body(
        "Researchers developed new approaches \u2014 particularly something called \"deep learning\" \u2014 "
        "that allowed AI to tackle problems it could never solve before. Deep learning is inspired by "
        "the structure of the human brain: layers of artificial \"neurons\" that pass information to each "
        "other, each layer refining the understanding further. These methods let AI understand human "
        "language, recognise images, generate entirely new text and images, and even write code."
    ))

    elements.append(body(
        "When all three pieces came together \u2014 massive data, powerful computers, and breakthrough "
        "methods \u2014 AI went from a research lab curiosity that only academics knew about to something "
        "anyone with a phone could use. That is why it feels sudden. But the foundation was 70 years in "
        "the making."
    ))

    elements.append(spacer(2))

    # Diagram 2
    diag2_path = os.path.join(DIAGRAM_DIR, "edition_01_diagram_02.png")
    if os.path.exists(diag2_path):
        from PIL import Image as PILImage
        pil_img = PILImage.open(diag2_path)
        aspect = pil_img.height / pil_img.width
        img_w = CONTENT_W
        img_h = img_w * aspect
        elements.append(Image(diag2_path, width=img_w, height=img_h))
        elements.append(spacer(3))
        elements.append(Paragraph(
            "Figure 2: Three forces \u2014 massive data, powerful computers, and breakthrough methods \u2014 "
            "converged in the 2020s to make AI accessible to everyone. The foundation was decades in "
            "the making.",
            STYLES['caption']
        ))

    elements.append(spacer(2))

    elements.append(watch_out(
        "AI did not appear overnight. The \"sudden\" explosion is the result of 70 years of research "
        "reaching a tipping point. Understanding this helps you see AI as an evolution, not a revolution "
        "\u2014 and protects you from hype-driven panic."
    ))

    elements.append(spacer(4))

    # ─── SECTION 5 ───
    elements.append(h1("Section 5: Try It Yourself"))
    elements.append(h2("Your First AI Conversation"))
    elements.append(spacer(2))

    elements.append(body(
        "Reading about AI is useful. Using AI is transformational. There is a world of difference between "
        "understanding what a bicycle is and actually riding one. Right now, you are going to ride the bicycle."
    ))

    elements.append(body(
        "Here is how to have your very first AI conversation in under five minutes. You do not need to "
        "install anything, pay anything, or understand anything technical. All you need is a phone or "
        "computer with internet access."
    ))

    elements.append(spacer(2))

    steps = [
        ("<b>Open your phone or computer browser.</b> Any browser works \u2014 Chrome, Safari, Firefox, Edge.",

         ),
        ("<b>Go to any free AI chat tool.</b> Three popular options: ChatGPT (chat.openai.com), "
         "Claude (claude.ai), or Google Gemini (gemini.google.com). All three are free to start.",
         ),
        ("<b>Create a free account if prompted.</b> This typically takes about 60 seconds. You will "
         "need an email address.",
         ),
        ("<b>In the message box, type exactly this:</b> \"Explain artificial intelligence to me like I "
         "am 10 years old.\"",
         ),
        ("<b>Read the response.</b> Notice how the AI uses simple language, relatable examples, and "
         "a friendly tone \u2014 because you told it exactly what you needed. The quality of your "
         "question shaped the quality of the answer.",
         ),
        ("<b>Now try a follow-up.</b> Type: \"Give me three examples of AI I probably used today "
         "without realising it.\"",
         ),
        ("<b>Notice something important:</b> the AI remembered your previous message. It built on the "
         "conversation. This is one of the things that makes modern AI different from a search engine \u2014 "
         "it holds context. A search engine gives you a list of links. An AI gives you a direct, "
         "personalised answer and remembers what you said before.",
         ),
    ]

    for i, (text,) in enumerate(steps, 1):
        elements.append(step_item(i, text))

    elements.append(spacer(4))

    elements.append(body(
        "You have now had your first AI conversation. That is your starting line. From here, everything "
        "builds. A 54-year-old business consultant with zero coding experience recently built six working "
        "AI assistants in just three weeks \u2014 not because he suddenly became a programmer, but because "
        "AI itself helped him learn. If he can do it, so can you."
    ))

    elements.append(body(
        "The single best way to learn AI is not by reading about it \u2014 it is by using it. You learn to "
        "swim by getting in the water, not by reading a book about swimming. Every time you open an AI "
        "tool and ask it a question, you are building a skill that will serve you for the rest of your life."
    ))

    elements.append(spacer(2))

    elements.append(did_you_know(
        "The difference between searching Google and talking to AI is like the difference between looking "
        "something up in an encyclopedia and having a conversation with a knowledgeable friend. The search "
        "gives you links. The AI gives you answers."
    ))

    elements.append(PageBreak())

    # ─── KEY TAKEAWAYS ───
    elements.append(h1("Key Takeaways"))
    elements.append(spacer(2))

    takeaways = [
        "AI is software that learns from examples instead of following fixed instructions \u2014 and "
        "you have been using it for years without knowing.",
        "You do not need to understand how AI works under the hood to benefit from it. You do not need "
        "to understand a car engine to drive.",
        "AI is not here to replace you. It is here to amplify what you already bring to the table. "
        "Think of AI like a megaphone \u2014 it does not create your message, it makes it louder.",
        "The vast majority of people have never intentionally used an AI tool. You are not behind \u2014 "
        "you are early.",
        "The single best way to learn AI is to start using it. Open a free AI chat tool today and "
        "ask it one question. That first conversation teaches you more than any textbook.",
    ]
    for t in takeaways:
        elements.append(Paragraph(f"\u2022  {t}", STYLES['key_takeaway']))

    elements.append(spacer(6))

    # ─── GLOSSARY ───
    elements.append(h1("Glossary"))
    elements.append(spacer(2))

    glossary = [
        ("Artificial Intelligence (AI)",
         "Software that learns from examples and data to make decisions or predictions, rather than "
         "following fixed rules written by a programmer."),
        ("Algorithm",
         "A set of step-by-step instructions that a computer follows to solve a problem or complete "
         "a task. AI algorithms are special because they learn and improve from data."),
        ("Data",
         "Information that AI uses to learn \u2014 text, images, numbers, audio, or any other form of "
         "recorded information. The more relevant data AI has, the better it performs."),
        ("Machine Learning",
         "A type of AI where the software improves its performance by studying examples rather than "
         "being manually reprogrammed. Covered in depth in Edition 06."),
        ("Deep Learning",
         "An advanced form of machine learning inspired by the structure of the human brain. It is the "
         "breakthrough behind modern AI tools like ChatGPT and image generators. Covered in Edition 08."),
        ("Training",
         "The process of feeding large amounts of data to an AI system so it can learn patterns. Think "
         "of it like studying for an exam \u2014 the more relevant material the AI reviews, the better "
         "it performs."),
        ("Pattern Recognition",
         "AI's core ability \u2014 finding repeating structures, trends, and relationships in data that "
         "allow it to make predictions about new, unseen information."),
        ("Chatbot",
         "A software program that can have a text-based conversation with a human. Modern AI chatbots "
         "(like ChatGPT and Claude) use advanced language understanding to have natural, helpful "
         "conversations."),
        ("Prompt",
         "The text you type into an AI tool to tell it what you want. The clearer your prompt, the "
         "better the AI's response. You will learn much more about this in Edition 09."),
    ]

    for term, defn in glossary:
        elements.append(Paragraph(term, STYLES['glossary_term']))
        elements.append(Paragraph(defn, STYLES['glossary_def']))
        elements.append(HRFlowable(width="100%", thickness=0.5, color=BORDER,
                                    spaceAfter=1*mm, spaceBefore=1*mm))

    elements.append(PageBreak())

    # ─── MINI QUIZ ───
    elements.append(h1("Mini Quiz"))
    elements.append(spacer(2))

    # Q1
    elements.append(Paragraph("<b>1.</b> What is the simplest way to define artificial intelligence?",
                               STYLES['quiz_text']))
    for opt in ["A. A robot that looks and acts like a human",
                "B. Software that learns from examples instead of following fixed instructions",
                "C. Any computer program that runs automatically",
                "D. A machine that is smarter than every human"]:
        elements.append(Paragraph(opt, STYLES['quiz_option']))
    elements.append(spacer(5))

    # Q2
    elements.append(Paragraph("<b>2.</b> Which of the following is an example of AI in your daily life?",
                               STYLES['quiz_text']))
    for opt in ["A. A light switch turning on when you flip it",
                "B. A calculator adding two numbers",
                "C. Netflix recommending a show based on what you watched before",
                "D. A printed book displaying text on a page"]:
        elements.append(Paragraph(opt, STYLES['quiz_option']))
    elements.append(spacer(5))

    # Q3
    elements.append(Paragraph("<b>3.</b> What three things converged to make AI accessible to ordinary people?",
                               STYLES['quiz_text']))
    for opt in ["A. Robots, internet, smartphones",
                "B. Massive data, powerful computers, breakthrough methods",
                "C. Social media, cloud storage, faster WiFi",
                "D. New laws, cheaper phones, better screens"]:
        elements.append(Paragraph(opt, STYLES['quiz_option']))
    elements.append(spacer(5))

    # Q4
    elements.append(Paragraph(
        "<b>4.</b> True or False: AI is a brand-new technology that was invented in the 2020s.",
        STYLES['quiz_text']))
    elements.append(spacer(5))

    # Q5
    elements.append(Paragraph(
        "<b>5.</b> True or False: You need a computer science degree to use AI tools effectively.",
        STYLES['quiz_text']))
    elements.append(spacer(5))

    # Q6
    elements.append(Paragraph(
        "<b>6.</b> AI learns from ____________ instead of following fixed rules written by a programmer.",
        STYLES['quiz_text']))
    elements.append(spacer(5))

    # Q7
    elements.append(Paragraph(
        "<b>7.</b> The term \"artificial intelligence\" was first coined in ____________ at Dartmouth College.",
        STYLES['quiz_text']))
    elements.append(spacer(5))

    # Q8
    elements.append(Paragraph(
        "<b>8.</b> In your own words, explain one difference between regular software and AI software. "
        "(1\u20132 sentences)",
        STYLES['quiz_text']))
    # Lines for writing
    for _ in range(3):
        elements.append(HRFlowable(width="90%", thickness=0.5, color=BORDER,
                                    spaceAfter=5*mm, spaceBefore=2*mm))
    elements.append(spacer(3))

    # Q9
    elements.append(Paragraph(
        "<b>9.</b> Describe one way AI already shows up in your daily life that you might not have "
        "noticed before reading this edition. (1\u20132 sentences)",
        STYLES['quiz_text']))
    for _ in range(3):
        elements.append(HRFlowable(width="90%", thickness=0.5, color=BORDER,
                                    spaceAfter=5*mm, spaceBefore=2*mm))
    elements.append(spacer(3))

    # Q10
    elements.append(Paragraph(
        "<b>10.</b> Why do you think AI suddenly seems to be everywhere, even though researchers have "
        "been working on it since the 1950s? (1\u20132 sentences)",
        STYLES['quiz_text']))
    for _ in range(3):
        elements.append(HRFlowable(width="90%", thickness=0.5, color=BORDER,
                                    spaceAfter=5*mm, spaceBefore=2*mm))

    elements.append(PageBreak())

    # ─── REFLECTION QUESTION ───
    elements.append(h1("Reflection Question"))
    elements.append(spacer(2))

    elements.append(Paragraph(
        "<i>This is a Personal reflection (Edition 01).</i>",
        STYLES['body']))
    elements.append(spacer(2))

    elements.append(Paragraph(
        "<b>How does AI already show up in your daily life right now \u2014 and did you realise it was "
        "AI before reading this edition?</b>",
        STYLES['reflection']))

    elements.append(body(
        "Take a moment to think about the apps, tools, and services you use every day. Which ones use "
        "AI to work? Your phone's keyboard predictions, your email spam filter, your music recommendations, "
        "your social media feed \u2014 all of these are powered by AI. How does it feel to know you have "
        "already been using artificial intelligence without realising it?"
    ))

    elements.append(body(
        "There is no right or wrong answer here. This reflection is just for you. Write down your thoughts, "
        "share them with a friend, or simply sit with the realisation for a moment. Awareness is the first "
        "step."
    ))

    elements.append(spacer(6))

    # ─── CTA BLOCK ───
    elements.append(h1("Continue Your Journey"))
    elements.append(spacer(2))

    ctas = [
        "\u2776  <b>Follow Kelvin M</b> on social media for daily AI insights and updates.",
        "\u2777  <b>Found this useful?</b> Share this PDF with one person who needs to hear that AI "
        "is not as complicated as they think.",
        "\u2778  <b>Subscribe to the newsletter</b> so you never miss a new edition.",
        "\u2779  <b>Watch the video version</b> of this edition for a quick 3-minute visual walkthrough.",
        "\u277A  <b>Join our community</b> on WhatsApp or Telegram to discuss what you are learning "
        "and ask questions.",
        "\u277B  <b>Download the next edition</b> in the series \u2014 Edition 02: How AI Thinks.",
    ]
    for cta in ctas:
        elements.append(Paragraph(cta, STYLES['cta']))

    elements.append(spacer(6))

    # ─── NEXT EDITION TEASER ───
    elements.append(h1("Coming Next: Edition 02 \u2014 How AI Thinks"))
    elements.append(spacer(2))

    elements.append(Paragraph(
        "You now know what AI is and where it already shows up in your life. But here is a question "
        "that might keep you up tonight: <b>how does AI actually \"think\"?</b>",
        STYLES['teaser']))

    elements.append(Paragraph(
        "When you type a sentence into an AI tool, something remarkable happens behind the scenes. "
        "The AI does not read your words the way you do. It does something completely different \u2014 "
        "something that, once you understand it, will change the way you use every AI tool forever.",
        STYLES['teaser']))

    elements.append(Paragraph(
        "In the next edition, you will discover how AI processes language, why it sometimes gets things "
        "brilliantly right and occasionally gets things strangely wrong, and what this means for how you "
        "communicate with it. <b>Edition 02 \u2014 How AI Thinks \u2014 is where the real magic begins.</b>",
        STYLES['teaser']))

    # ─── BUILD ───
    doc.build(elements, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"\nPDF built successfully: {OUTPUT_FILE}")

    # Verify file size
    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"File size: {size_mb:.2f} MB")
    if size_mb > 10:
        print("WARNING: File exceeds 10MB limit!")
    else:
        print("File size OK (under 10MB)")


if __name__ == "__main__":
    build()
