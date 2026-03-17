"""
Generate ALL diagrams for Edition 01 (150-page version) — What is AI?
10 diagrams total, all following STYLE_TOKENS.yaml
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
OUT_DIR = os.path.join(BASE_DIR, "assets", "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

# Colors
PRIMARY = "#CC785C"
PRIMARY_DARK = "#9E4E2E"
PRIMARY_LIGHT = "#F2D4C8"
BG_SURFACE = "#F9F6F3"
BG_WHITE = "#FFFFFF"
TEXT_PRIMARY = "#1A1A1A"
TEXT_SECONDARY = "#4A4A4A"
TEXT_MUTED = "#888888"
BORDER = "#E0D9D4"
TEAL = "#2A9D8F"
AMBER = "#E9C46A"
CORAL = "#E76F51"
GREEN = "#57A773"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, f"Inter-{name}.ttf"), size)

def text_center(draw, text, f, xy, fill=TEXT_PRIMARY):
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((xy[0] - tw // 2, xy[1] - th // 2), text, fill=fill, font=f)

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_arrow(draw, start, end, color=TEXT_SECONDARY, width=3, head_size=12):
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    x1 = end[0] - head_size * math.cos(angle - math.pi / 6)
    y1 = end[1] - head_size * math.sin(angle - math.pi / 6)
    x2 = end[0] - head_size * math.cos(angle + math.pi / 6)
    y2 = end[1] - head_size * math.sin(angle + math.pi / 6)
    draw.polygon([end, (x1, y1), (x2, y2)], fill=color)


# ─── Diagram 1: Regular Software vs AI ───
def diagram_01():
    W, H = 1960, 900
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    title_f = font("Bold", 42)
    header_f = font("SemiBold", 34)
    body_f = font("Regular", 28)
    label_f = font("Medium", 26)

    text_center(draw, "How Regular Software and AI Work Differently", title_f, (W//2, 50))
    left_x, right_x = W//4, 3*W//4
    draw_rounded_rect(draw, (60, 110, W//2-40, 170), 12, PRIMARY_LIGHT, PRIMARY, 3)
    text_center(draw, "Regular Software", header_f, (left_x, 140), PRIMARY_DARK)
    draw_rounded_rect(draw, (W//2+40, 110, W-60, 170), 12, PRIMARY, PRIMARY_DARK, 3)
    text_center(draw, "Artificial Intelligence", header_f, (right_x, 140), BG_WHITE)

    boxes_l = [("Programmer writes\nfixed rules", 240), ("Input arrives", 390),
               ("Follows exact\ninstructions", 540), ("Predictable output", 690)]
    boxes_r = [("Learns from thousands\nof examples", 240), ("New input arrives", 390),
               ("Finds patterns and\nmakes predictions", 540), ("Handles situations it\nhas never seen before", 690)]
    bw, bh = 340, 100
    for text, y in boxes_l:
        draw_rounded_rect(draw, (left_x-bw//2, y, left_x+bw//2, y+bh), 10, BG_SURFACE, BORDER, 2)
        text_center(draw, text, body_f, (left_x, y+bh//2))
    for text, y in boxes_r:
        draw_rounded_rect(draw, (right_x-bw//2, y, right_x+bw//2, y+bh), 10, PRIMARY_LIGHT, PRIMARY, 2)
        text_center(draw, text, body_f, (right_x, y+bh//2))
    for i in range(len(boxes_l)-1):
        draw_arrow(draw, (left_x, boxes_l[i][1]+bh+5), (left_x, boxes_l[i+1][1]-5), TEXT_MUTED, 3, 10)
        draw_arrow(draw, (right_x, boxes_r[i][1]+bh+5), (right_x, boxes_r[i+1][1]-5), PRIMARY, 3, 10)
    for y in range(120, H-40, 16):
        draw.line([(W//2, y), (W//2, y+8)], fill=BORDER, width=2)
    text_center(draw, "VS", font("Bold", 36), (W//2, H//2), PRIMARY)
    draw.rounded_rectangle((left_x-160, 810, left_x+160, 870), radius=8, fill=PRIMARY_LIGHT, outline=PRIMARY, width=1)
    text_center(draw, "Example: Calculator", label_f, (left_x, 840), PRIMARY_DARK)
    draw.rounded_rectangle((right_x-160, 810, right_x+160, 870), radius=8, fill=PRIMARY, outline=PRIMARY_DARK, width=1)
    text_center(draw, "Example: Spam Filter", label_f, (right_x, 840), BG_WHITE)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_01.png"), dpi=(300,300))
    print("  Diagram 01: Regular Software vs AI")


# ─── Diagram 2: Three Convergences ───
def diagram_02():
    W, H = 1960, 1000
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    title_f = font("Bold", 42)
    header_f = font("SemiBold", 32)
    small_f = font("Regular", 22)
    year_f = font("Bold", 28)

    text_center(draw, "Why AI Became Accessible to Everyone", title_f, (W//2, 50))
    box_data = [("Massive Data", "Internet, social media,\nand smartphones created\nmore data than ever", TEAL, 160),
                ("Powerful Computers", "Graphics chips made\nAI training practical\nand affordable", PRIMARY, 540),
                ("Breakthrough Methods", "Deep learning allowed\nAI to understand language\nand images", CORAL, 920)]
    bw, bh, cy = 420, 200, 260
    for title, desc, color, cx in box_data:
        draw_rounded_rect(draw, (cx-bw//2, cy, cx+bw//2, cy+bh), 12, BG_SURFACE, color, 3)
        draw.ellipse((cx-30, cy-35, cx+30, cy+25), fill=color)
        idx = [d[0] for d in box_data].index(title) + 1
        text_center(draw, str(idx), font("Bold", 28), (cx, cy-5), BG_WHITE)
        text_center(draw, title, header_f, (cx, cy+55))
        for i, line in enumerate(desc.split("\n")):
            text_center(draw, line, small_f, (cx, cy+100+i*30), TEXT_SECONDARY)
    conv_y = cy + bh + 40
    for cx_b in [160, 540, 920]:
        draw_arrow(draw, (cx_b, cy+bh+10), (W//2, conv_y+60), PRIMARY, 3, 12)
    cr = 80
    cy_c = conv_y + 60 + cr + 20
    draw.ellipse((W//2-cr, cy_c-cr, W//2+cr, cy_c+cr), fill=PRIMARY, outline=PRIMARY_DARK, width=3)
    text_center(draw, "AI Becomes", font("Bold", 24), (W//2, cy_c-14), BG_WHITE)
    text_center(draw, "Accessible", font("Bold", 24), (W//2, cy_c+14), BG_WHITE)
    tl_y = cy_c + cr + 60
    bar_y = tl_y + 15
    draw.line([(100, bar_y), (W-100, bar_y)], fill=BORDER, width=3)
    points = [(250, "1956", "AI coined at\nDartmouth"), (620, "1960s-2010s", "Decades of\nresearch"),
              (980, "2020s", "Three forces\nconverge"), (1400, "Today", "Anyone can\nuse AI")]
    for px, year, desc in points:
        draw.ellipse((px-8, bar_y-8, px+8, bar_y+8), fill=PRIMARY)
        text_center(draw, year, year_f, (px, bar_y+35))
        for i, line in enumerate(desc.split("\n")):
            text_center(draw, line, small_f, (px, bar_y+65+i*26), TEXT_SECONDARY)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_02.png"), dpi=(300,300))
    print("  Diagram 02: Three Convergences")


# ─── Diagram 3: AI in Daily Life (Icon Grid) ───
def diagram_03():
    W, H = 1960, 800
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "AI is Already Everywhere in Your Life", font("Bold", 42), (W//2, 50))
    items = [
        ("Phone", "Word\nprediction", PRIMARY),
        ("Email", "Spam\nfiltering", TEAL),
        ("Music", "Song\nrecommendations", GREEN),
        ("Maps", "Traffic\nrerouting", CORAL),
        ("Shopping", "Product\nsuggestions", AMBER),
        ("Social", "Feed\ncuration", PRIMARY_DARK),
    ]
    start_x = 100
    gap = (W - 200) // len(items)
    for i, (label, desc, color) in enumerate(items):
        cx = start_x + gap * i + gap // 2
        cy_top = 180
        # Circle icon
        draw.ellipse((cx-60, cy_top, cx+60, cy_top+120), fill=color)
        text_center(draw, label, font("Bold", 24), (cx, cy_top+60), BG_WHITE)
        # Description box
        draw_rounded_rect(draw, (cx-120, cy_top+150, cx+120, cy_top+310), 10, BG_SURFACE, BORDER, 2)
        for j, line in enumerate(desc.split("\n")):
            text_center(draw, line, font("Regular", 24), (cx, cy_top+200+j*32), TEXT_PRIMARY)
        # Connector
        draw.line([(cx, cy_top+120), (cx, cy_top+150)], fill=color, width=2)
    # Bottom bar
    text_center(draw, "You interact with AI dozens of times every day — usually without realizing it",
                font("Medium", 26), (W//2, H-100), TEXT_SECONDARY)
    draw.line([(100, H-140), (W-100, H-140)], fill=BORDER, width=1)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_03.png"), dpi=(300,300))
    print("  Diagram 03: AI in Daily Life")


# ─── Diagram 4: Types of AI Pyramid ───
def diagram_04():
    W, H = 1960, 900
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "Three Levels of Artificial Intelligence", font("Bold", 42), (W//2, 50))

    # Pyramid
    peak_x, peak_y = W//2, 160
    base_y = 700
    left_base = W//2 - 500
    right_base = W//2 + 500

    # Three bands
    bands = [
        (0.0, 0.25, PRIMARY_DARK, "Super AI", "Hypothetical AI that surpasses\nhuman intelligence in every way", BG_WHITE),
        (0.25, 0.55, PRIMARY, "General AI", "AI that can do any intellectual\ntask a human can do", BG_WHITE),
        (0.55, 1.0, PRIMARY_LIGHT, "Narrow AI", "AI designed for one specific task\n(This is ALL AI that exists today)", TEXT_PRIMARY),
    ]
    total_h = base_y - peak_y
    for frac_start, frac_end, color, title, desc, text_color in bands:
        y_top = peak_y + total_h * frac_start
        y_bot = peak_y + total_h * frac_end
        # Calculate trapezoid widths
        w_top = (y_top - peak_y) / total_h * (right_base - left_base)
        w_bot = (y_bot - peak_y) / total_h * (right_base - left_base)
        x_tl = W//2 - w_top//2
        x_tr = W//2 + w_top//2
        x_bl = W//2 - w_bot//2
        x_br = W//2 + w_bot//2
        draw.polygon([(x_tl, y_top), (x_tr, y_top), (x_br, y_bot), (x_bl, y_bot)], fill=color)
        cy = (y_top + y_bot) / 2
        text_center(draw, title, font("Bold", 30), (W//2, cy - 20), text_color)
        for i, line in enumerate(desc.split("\n")):
            text_center(draw, line, font("Regular", 20), (W//2, cy + 14 + i * 26), text_color)

    # Status labels
    draw_rounded_rect(draw, (W//2+520, 200, W//2+780, 260), 8, CORAL, CORAL, 0)
    text_center(draw, "Does not exist yet", font("Medium", 20), (W//2+650, 230), BG_WHITE)
    draw_rounded_rect(draw, (W//2+520, 380, W//2+780, 440), 8, AMBER, AMBER, 0)
    text_center(draw, "Does not exist yet", font("Medium", 20), (W//2+650, 410), BG_WHITE)
    draw_rounded_rect(draw, (W//2+520, 560, W//2+780, 620), 8, GREEN, GREEN, 0)
    text_center(draw, "Exists today!", font("Medium", 20), (W//2+650, 590), BG_WHITE)

    # Arrows
    draw.line([(W//2+500, 230), (W//2+520, 230)], fill=CORAL, width=2)
    draw.line([(W//2+500, 410), (W//2+520, 410)], fill=AMBER, width=2)
    draw.line([(W//2+500, 590), (W//2+520, 590)], fill=GREEN, width=2)

    text_center(draw, "Every AI tool you use today — ChatGPT, Siri, Google Translate — is Narrow AI",
                font("Medium", 24), (W//2, H-110), TEXT_SECONDARY)

    img.save(os.path.join(OUT_DIR, "edition_01_diagram_04.png"), dpi=(300,300))
    print("  Diagram 04: Types of AI Pyramid")


# ─── Diagram 5: AI Timeline ───
def diagram_05():
    W, H = 1960, 700
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "Key Moments in the History of AI", font("Bold", 42), (W//2, 50))

    bar_y = 250
    draw.line([(80, bar_y), (W-80, bar_y)], fill=PRIMARY, width=4)

    events = [
        (180, "1956", "AI is born", "Dartmouth\nconference"),
        (440, "1966", "First chatbot", "ELIZA talks\nto humans"),
        (700, "1997", "Chess victory", "Deep Blue\nbeats Kasparov"),
        (960, "2011", "Voice AI", "Siri launches\non iPhone"),
        (1220, "2016", "Game master", "AlphaGo beats\nworld champion"),
        (1480, "2022", "Chat revolution", "ChatGPT launches\nto the public"),
        (1740, "2024+", "AI for everyone", "AI becomes\naccessible"),
    ]
    for i, (px, year, title, desc) in enumerate(events):
        # Dot
        draw.ellipse((px-12, bar_y-12, px+12, bar_y+12), fill=PRIMARY)
        # Alternating above/below
        if i % 2 == 0:
            text_center(draw, year, font("Bold", 24), (px, bar_y-50), PRIMARY_DARK)
            text_center(draw, title, font("SemiBold", 20), (px, bar_y-85), TEXT_PRIMARY)
            for j, line in enumerate(desc.split("\n")):
                text_center(draw, line, font("Regular", 18), (px, bar_y+50+j*24), TEXT_SECONDARY)
        else:
            for j, line in enumerate(desc.split("\n")):
                text_center(draw, line, font("Regular", 18), (px, bar_y-60-j*24), TEXT_SECONDARY)
            text_center(draw, title, font("SemiBold", 20), (px, bar_y-100 if '\n' not in desc else bar_y - 110), TEXT_PRIMARY)
            text_center(draw, year, font("Bold", 24), (px, bar_y+50), PRIMARY_DARK)

    text_center(draw, "70 years of research led to the AI moment we are living through right now",
                font("Medium", 24), (W//2, H-80), TEXT_SECONDARY)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_05.png"), dpi=(300,300))
    print("  Diagram 05: AI Timeline")


# ─── Diagram 6: How AI Learns from Data ───
def diagram_06():
    W, H = 1960, 800
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "How AI Learns: The Simplified Process", font("Bold", 42), (W//2, 50))

    steps = [
        ("Collect Data", "Thousands of\nexamples gathered", TEAL),
        ("Find Patterns", "AI looks for\nrepeating structures", PRIMARY),
        ("Build a Model", "Patterns become\nrules the AI follows", AMBER),
        ("Test & Improve", "Check results and\nadjust until accurate", GREEN),
        ("Deploy", "Ready to handle\nnew situations", PRIMARY_DARK),
    ]
    start_x = 100
    gap = (W - 200) // len(steps)
    for i, (title, desc, color) in enumerate(steps):
        cx = start_x + gap * i + gap // 2
        # Step number circle
        draw.ellipse((cx-35, 140, cx+35, 210), fill=color)
        text_center(draw, str(i+1), font("Bold", 30), (cx, 175), BG_WHITE)
        # Title
        text_center(draw, title, font("SemiBold", 26), (cx, 240), TEXT_PRIMARY)
        # Box
        draw_rounded_rect(draw, (cx-140, 280, cx+140, 400), 10, BG_SURFACE, color, 2)
        for j, line in enumerate(desc.split("\n")):
            text_center(draw, line, font("Regular", 22), (cx, 315+j*30), TEXT_SECONDARY)
        # Arrow to next
        if i < len(steps) - 1:
            next_cx = start_x + gap * (i+1) + gap // 2
            draw_arrow(draw, (cx+140+10, 340), (next_cx-140-10, 340), color, 3, 12)

    # Analogy box
    draw_rounded_rect(draw, (200, 480, W-200, 620), 12, BG_SURFACE, TEAL, 2)
    text_center(draw, "Think of it like learning to cook:", font("SemiBold", 26), (W//2, 520), TEAL)
    analogy_lines = [
        "1. Collect recipes (data)    2. Notice what works (patterns)    3. Develop your own style (model)",
        "4. Taste and adjust (test)    5. Cook confidently for guests (deploy)"
    ]
    for i, line in enumerate(analogy_lines):
        text_center(draw, line, font("Regular", 22), (W//2, 560+i*30), TEXT_SECONDARY)

    text_center(draw, "AI repeats this process millions of times — but the core idea is the same as how humans learn",
                font("Medium", 22), (W//2, H-80), TEXT_SECONDARY)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_06.png"), dpi=(300,300))
    print("  Diagram 06: How AI Learns")


# ─── Diagram 7: Thermostat vs Smart Home (Before/After) ───
def diagram_07():
    W, H = 1960, 700
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "Regular Software vs. AI: The Thermostat Example", font("Bold", 42), (W//2, 50))

    # Left panel: Basic Thermostat
    lx = W//4
    draw_rounded_rect(draw, (60, 120, W//2-40, 600), 12, BG_SURFACE, BORDER, 2)
    text_center(draw, "Basic Thermostat", font("Bold", 30), (lx, 165), TEXT_PRIMARY)
    text_center(draw, "(Regular Software)", font("Regular", 22), (lx, 200), TEXT_MUTED)
    draw.line([(120, 230), (W//2-100, 230)], fill=BORDER, width=1)
    left_items = [
        "One fixed rule: \"Below 20°, turn on heat\"",
        "Does not know if you are home or away",
        "Cannot tell if it is summer or winter",
        "Does not learn your preferences",
        "Same behaviour forever",
        "Must be manually reprogrammed",
    ]
    for i, item in enumerate(left_items):
        y = 270 + i * 50
        draw.ellipse((140, y-6, 152, y+6), fill=CORAL)
        draw.text((170, y-12), item, fill=TEXT_PRIMARY, font=font("Regular", 20))

    # Right panel: Smart Home
    rx = 3*W//4
    draw_rounded_rect(draw, (W//2+40, 120, W-60, 600), 12, PRIMARY_LIGHT, PRIMARY, 2)
    text_center(draw, "Smart Home Assistant", font("Bold", 30), (rx, 165), TEXT_PRIMARY)
    text_center(draw, "(AI-Powered)", font("Regular", 22), (rx, 200), PRIMARY_DARK)
    draw.line([(W//2+100, 230), (W-120, 230)], fill=PRIMARY, width=1)
    right_items = [
        "Learns you like it warm on weekday mornings",
        "Knows when you leave and adjusts",
        "Adapts to seasonal changes automatically",
        "Gets better at predicting your comfort",
        "Improves over time without reprogramming",
        "Anticipates your needs proactively",
    ]
    for i, item in enumerate(right_items):
        y = 270 + i * 50
        draw.ellipse((W//2+120, y-6, W//2+132, y+6), fill=GREEN)
        draw.text((W//2+150, y-12), item, fill=TEXT_PRIMARY, font=font("Regular", 20))

    # VS circle
    draw.ellipse((W//2-30, 340, W//2+30, 400), fill=PRIMARY)
    text_center(draw, "VS", font("Bold", 22), (W//2, 370), BG_WHITE)

    text_center(draw, "The key difference: AI learns and adapts. Regular software just follows orders.",
                font("Medium", 24), (W//2, H-50), TEXT_SECONDARY)
    img.save(os.path.join(OUT_DIR, "edition_01_diagram_07.png"), dpi=(300,300))
    print("  Diagram 07: Thermostat vs Smart Home")


# ─── Diagram 8: Myths vs Reality ───
def diagram_08():
    W, H = 1960, 1000
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "AI Myths vs. Reality", font("Bold", 42), (W//2, 50))

    myths = [
        ("AI will take all our jobs", "AI changes jobs more than it eliminates them.\nNew roles are being created every day."),
        ("AI is smarter than humans", "AI is powerful at patterns, but has no common\nsense, emotions, or true understanding."),
        ("AI thinks like a human brain", "AI processes math and statistics — it does\nnot actually think, feel, or understand."),
        ("You need to be a genius to use AI", "If you can type a question, you can\nuse AI. No technical skills required."),
        ("AI appeared out of nowhere", "Researchers have worked on AI since 1956.\nIt took 70 years to reach this moment."),
    ]

    for i, (myth, reality) in enumerate(myths):
        y = 130 + i * 170
        # Myth side (left)
        draw_rounded_rect(draw, (60, y, W//2-30, y+130), 10, "#FDE8E8", CORAL, 2)
        draw.text((90, y+15), "MYTH", fill=CORAL, font=font("Bold", 18))
        draw.text((90, y+45), myth, fill=TEXT_PRIMARY, font=font("SemiBold", 22))

        # Arrow
        draw_arrow(draw, (W//2-20, y+65), (W//2+20, y+65), GREEN, 3, 10)

        # Reality side (right)
        draw_rounded_rect(draw, (W//2+30, y, W-60, y+130), 10, "#E8F5E9", GREEN, 2)
        draw.text((W//2+60, y+15), "REALITY", fill=GREEN, font=font("Bold", 18))
        for j, line in enumerate(reality.split("\n")):
            draw.text((W//2+60, y+45+j*28), line, fill=TEXT_PRIMARY, font=font("Regular", 21))

    img.save(os.path.join(OUT_DIR, "edition_01_diagram_08.png"), dpi=(300,300))
    print("  Diagram 08: Myths vs Reality")


# ─── Diagram 9: AI as a Megaphone / Amplifier ───
def diagram_09():
    W, H = 1960, 600
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "AI is a Multiplier, Not a Replacement", font("Bold", 42), (W//2, 50))

    # Person icon (left)
    px = 300
    # Head
    draw.ellipse((px-40, 180, px+40, 260), fill=PRIMARY)
    # Body
    draw.rounded_rectangle((px-50, 270, px+50, 380), radius=10, fill=PRIMARY)
    text_center(draw, "Your Skills", font("SemiBold", 22), (px, 420), TEXT_PRIMARY)
    text_center(draw, "Ideas, creativity,", font("Regular", 18), (px, 450), TEXT_SECONDARY)
    text_center(draw, "judgment, empathy", font("Regular", 18), (px, 474), TEXT_SECONDARY)

    # Multiplication sign
    text_center(draw, "x", font("Bold", 60), (W//2-200, 280), PRIMARY)

    # AI circle
    ax = W//2
    draw.ellipse((ax-70, 200, ax+70, 340), fill=PRIMARY_LIGHT, outline=PRIMARY, width=3)
    text_center(draw, "AI", font("Bold", 40), (ax, 260), PRIMARY_DARK)
    text_center(draw, "AI Tools", font("SemiBold", 22), (ax, 380), TEXT_PRIMARY)
    text_center(draw, "Speed, scale,", font("Regular", 18), (ax, 410), TEXT_SECONDARY)
    text_center(draw, "data processing", font("Regular", 18), (ax, 434), TEXT_SECONDARY)

    # Equals sign
    text_center(draw, "=", font("Bold", 60), (W//2+200, 280), PRIMARY)

    # Result (bigger)
    rx = W - 300
    draw.ellipse((rx-90, 180, rx+90, 360), fill=GREEN, outline="#3D8B5E", width=3)
    text_center(draw, "10x", font("Bold", 50), (rx, 255), BG_WHITE)
    text_center(draw, "Impact", font("Bold", 28), (rx, 310), BG_WHITE)
    text_center(draw, "Amplified Output", font("SemiBold", 22), (rx, 400), TEXT_PRIMARY)
    text_center(draw, "Better results, faster,", font("Regular", 18), (rx, 430), TEXT_SECONDARY)
    text_center(draw, "at greater scale", font("Regular", 18), (rx, 454), TEXT_SECONDARY)

    # Bottom quote
    draw.line([(200, H-100), (W-200, H-100)], fill=BORDER, width=1)
    text_center(draw, "\"AI does not create your message — it makes it louder.\"",
                font("Medium", 26), (W//2, H-55), PRIMARY_DARK)

    img.save(os.path.join(OUT_DIR, "edition_01_diagram_09.png"), dpi=(300,300))
    print("  Diagram 09: AI as Multiplier")


# ─── Diagram 10: Your AI Learning Path ───
def diagram_10():
    W, H = 1960, 700
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    text_center(draw, "Your AI Learning Journey — Where to Start", font("Bold", 42), (W//2, 50))

    levels = [
        ("Level 1", "Try It", "Have your first\nAI conversation", PRIMARY_LIGHT, TEXT_PRIMARY),
        ("Level 2", "Use It", "Use AI for one\nreal task", PRIMARY, BG_WHITE),
        ("Level 3", "Learn It", "Understand how\nAI actually works", PRIMARY_DARK, BG_WHITE),
        ("Level 4", "Master It", "Customise AI to\nfit your life", "#6B3A2A", BG_WHITE),
    ]
    start_x = 140
    gap = (W - 280) // len(levels)
    for i, (level, title, desc, color, tcolor) in enumerate(levels):
        cx = start_x + gap * i + gap // 2
        # Stair step effect
        y_top = 400 - i * 60
        # Box
        draw_rounded_rect(draw, (cx-160, y_top, cx+160, y_top+220), 14, color, None, 0)
        text_center(draw, level, font("Regular", 20), (cx, y_top+30), tcolor)
        text_center(draw, title, font("Bold", 30), (cx, y_top+70), tcolor)
        for j, line in enumerate(desc.split("\n")):
            text_center(draw, line, font("Regular", 20), (cx, y_top+120+j*28), tcolor)
        # Arrow
        if i < len(levels) - 1:
            next_cx = start_x + gap * (i+1) + gap // 2
            mid_y = y_top + 110
            draw_arrow(draw, (cx+165, mid_y), (next_cx-165, mid_y-60), PRIMARY, 3, 12)

    # YOU ARE HERE marker
    first_cx = start_x + gap // 2
    draw_rounded_rect(draw, (first_cx-80, 400+220+15, first_cx+80, 400+220+55), 8, GREEN, GREEN, 0)
    text_center(draw, "YOU ARE HERE", font("Bold", 16), (first_cx, 400+220+35), BG_WHITE)
    draw.polygon([(first_cx, 400+220+10), (first_cx-10, 400+220+18), (first_cx+10, 400+220+18)], fill=GREEN)

    img.save(os.path.join(OUT_DIR, "edition_01_diagram_10.png"), dpi=(300,300))
    print("  Diagram 10: Learning Path")


if __name__ == "__main__":
    print("Generating Edition 01 diagrams (150-page version)...")
    diagram_01()
    diagram_02()
    diagram_03()
    diagram_04()
    diagram_05()
    diagram_06()
    diagram_07()
    diagram_08()
    diagram_09()
    diagram_10()
    print("All 10 diagrams generated.")
