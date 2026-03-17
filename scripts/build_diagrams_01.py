"""
Generate diagrams for Edition 01 — What is AI?
Diagram 1: Regular Software vs AI (Comparison/Flowchart)
Diagram 2: Three Convergences Timeline
"""

from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
OUT_DIR = os.path.join(BASE_DIR, "assets", "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

# Colors from STYLE_TOKENS.yaml
PRIMARY = "#CC785C"
PRIMARY_DARK = "#9E4E2E"
PRIMARY_LIGHT = "#F2D4C8"
BG_SURFACE = "#F9F6F3"
BG_WHITE = "#FFFFFF"
TEXT_PRIMARY = "#1A1A1A"
TEXT_SECONDARY = "#4A4A4A"
TEXT_MUTED = "#888888"
BORDER = "#E0D9D4"
ARROW_COLOR = "#4A4A4A"
TEAL = "#2A9D8F"

# Fonts
def font(name, size):
    path = os.path.join(FONT_DIR, f"Inter-{name}.ttf")
    return ImageFont.truetype(path, size)


def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_arrow(draw, start, end, color=ARROW_COLOR, width=3, head_size=12):
    """Draw an arrow from start to end."""
    import math
    draw.line([start, end], fill=color, width=width)
    # Arrowhead
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    x1 = end[0] - head_size * math.cos(angle - math.pi / 6)
    y1 = end[1] - head_size * math.sin(angle - math.pi / 6)
    x2 = end[0] - head_size * math.cos(angle + math.pi / 6)
    y2 = end[1] - head_size * math.sin(angle + math.pi / 6)
    draw.polygon([end, (x1, y1), (x2, y2)], fill=color)


def text_center(draw, text, font_obj, xy, fill=TEXT_PRIMARY):
    """Draw centered text at position."""
    bbox = draw.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = xy[0] - tw // 2
    y = xy[1] - th // 2
    draw.text((x, y), text, fill=fill, font=font_obj)


def build_diagram_1():
    """Diagram 1: Regular Software vs AI — Comparison Flowchart"""
    W, H = 1960, 900
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)

    title_font = font("Bold", 42)
    header_font = font("SemiBold", 34)
    body_font = font("Regular", 28)
    label_font = font("Medium", 26)

    # Title
    text_center(draw, "How Regular Software and AI Work Differently", title_font, (W // 2, 50), TEXT_PRIMARY)

    # --- LEFT SIDE: Regular Software ---
    left_x = W // 4
    # Header
    draw_rounded_rect(draw, (60, 110, W // 2 - 40, 170), 12, PRIMARY_LIGHT, PRIMARY, 3)
    text_center(draw, "Regular Software", header_font, (left_x, 140), PRIMARY_DARK)

    # Flow boxes
    boxes_left = [
        ("Programmer writes\nfixed rules", 240),
        ("Input arrives", 390),
        ("Follows exact\ninstructions", 540),
        ("Predictable output", 690),
    ]
    box_w, box_h = 340, 100
    for text, y in boxes_left:
        bx = left_x - box_w // 2
        draw_rounded_rect(draw, (bx, y, bx + box_w, y + box_h), 10, BG_SURFACE, BORDER, 2)
        text_center(draw, text, body_font, (left_x, y + box_h // 2), TEXT_PRIMARY)

    # Arrows between boxes
    for i in range(len(boxes_left) - 1):
        y1 = boxes_left[i][1] + box_h
        y2 = boxes_left[i + 1][1]
        draw_arrow(draw, (left_x, y1 + 5), (left_x, y2 - 5), TEXT_MUTED, 3, 10)

    # Example label
    draw.rounded_rectangle((left_x - 160, 810, left_x + 160, 870), radius=8, fill=PRIMARY_LIGHT, outline=PRIMARY, width=1)
    text_center(draw, "Example: Calculator", label_font, (left_x, 840), PRIMARY_DARK)

    # --- DIVIDER ---
    for y in range(120, H - 40, 16):
        draw.line([(W // 2, y), (W // 2, y + 8)], fill=BORDER, width=2)
    text_center(draw, "VS", font("Bold", 36), (W // 2, H // 2), PRIMARY)

    # --- RIGHT SIDE: AI ---
    right_x = 3 * W // 4
    # Header
    draw_rounded_rect(draw, (W // 2 + 40, 110, W - 60, 170), 12, PRIMARY, PRIMARY_DARK, 3)
    text_center(draw, "Artificial Intelligence", header_font, (right_x, 140), BG_WHITE)

    boxes_right = [
        ("Learns from thousands\nof examples", 240),
        ("New input arrives", 390),
        ("Finds patterns and\nmakes predictions", 540),
        ("Handles situations it\nhas never seen before", 690),
    ]
    for text, y in boxes_right:
        bx = right_x - box_w // 2
        draw_rounded_rect(draw, (bx, y, bx + box_w, y + box_h), 10, PRIMARY_LIGHT, PRIMARY, 2)
        text_center(draw, text, body_font, (right_x, y + box_h // 2), TEXT_PRIMARY)

    for i in range(len(boxes_right) - 1):
        y1 = boxes_right[i][1] + box_h
        y2 = boxes_right[i + 1][1]
        draw_arrow(draw, (right_x, y1 + 5), (right_x, y2 - 5), PRIMARY, 3, 10)

    # Example label
    draw.rounded_rectangle((right_x - 160, 810, right_x + 160, 870), radius=8, fill=PRIMARY, outline=PRIMARY_DARK, width=1)
    text_center(draw, "Example: Spam Filter", label_font, (right_x, 840), BG_WHITE)

    out_path = os.path.join(OUT_DIR, "edition_01_diagram_01.png")
    img.save(out_path, dpi=(300, 300))
    print(f"Saved: {out_path}")
    return out_path


def build_diagram_2():
    """Diagram 2: Three Convergences — Why AI Became Accessible"""
    W, H = 1960, 1000
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)

    title_font = font("Bold", 42)
    header_font = font("SemiBold", 32)
    body_font = font("Regular", 26)
    label_font = font("Medium", 28)
    small_font = font("Regular", 22)
    year_font = font("Bold", 28)

    # Title
    text_center(draw, "Why AI Became Accessible to Everyone", title_font, (W // 2, 50), TEXT_PRIMARY)

    # Three convergence boxes
    box_data = [
        ("Massive Data", "Internet, social media,\nand smartphones created\nmore data than ever", TEAL, 160),
        ("Powerful Computers", "Graphics chips made\nAI training practical\nand affordable", PRIMARY, 540),
        ("Breakthrough Methods", "Deep learning allowed\nAI to understand language\nand images", "#E76F51", 920),
    ]

    box_w, box_h = 420, 200
    center_y = 260

    for title, desc, color, cx in box_data:
        bx = cx - box_w // 2
        # Box
        draw_rounded_rect(draw, (bx, center_y, bx + box_w, center_y + box_h), 12, BG_SURFACE, color, 3)
        # Icon circle
        draw.ellipse((cx - 30, center_y - 35, cx + 30, center_y + 25), fill=color)
        # Number/icon text
        idx = [d[0] for d in box_data].index(title) + 1
        text_center(draw, str(idx), font("Bold", 28), (cx, center_y - 5), BG_WHITE)
        # Title
        text_center(draw, title, header_font, (cx, center_y + 55), TEXT_PRIMARY)
        # Description
        lines = desc.split("\n")
        for i, line in enumerate(lines):
            text_center(draw, line, small_font, (cx, center_y + 100 + i * 30), TEXT_SECONDARY)

    # Convergence arrows pointing down to center
    center_x = W // 2
    converge_y = center_y + box_h + 40

    for cx_box in [160, 540, 920]:
        # Arrow from bottom of each box to convergence point
        draw_arrow(draw, (cx_box, center_y + box_h + 10), (center_x, converge_y + 60), PRIMARY, 3, 12)

    # Central convergence circle
    circle_r = 80
    cy_circle = converge_y + 60 + circle_r + 20
    draw.ellipse(
        (center_x - circle_r, cy_circle - circle_r,
         center_x + circle_r, cy_circle + circle_r),
        fill=PRIMARY, outline=PRIMARY_DARK, width=3
    )
    text_center(draw, "AI Becomes", font("Bold", 24), (center_x, cy_circle - 14), BG_WHITE)
    text_center(draw, "Accessible", font("Bold", 24), (center_x, cy_circle + 14), BG_WHITE)

    # Timeline bar at bottom
    timeline_y = cy_circle + circle_r + 60
    bar_y = timeline_y + 15
    draw.line([(100, bar_y), (W - 100, bar_y)], fill=BORDER, width=3)

    # Timeline points
    points = [
        (250, "1956", "AI coined at\nDartmouth"),
        (620, "1960s-2010s", "Decades of\nresearch"),
        (980, "2020s", "Three forces\nconverge"),
        (1400, "Today", "Anyone can\nuse AI"),
    ]

    for px, year, desc in points:
        # Dot
        draw.ellipse((px - 8, bar_y - 8, px + 8, bar_y + 8), fill=PRIMARY)
        # Year
        text_center(draw, year, year_font, (px, bar_y + 35), TEXT_PRIMARY)
        # Description
        lines = desc.split("\n")
        for i, line in enumerate(lines):
            text_center(draw, line, small_font, (px, bar_y + 65 + i * 26), TEXT_SECONDARY)

    out_path = os.path.join(OUT_DIR, "edition_01_diagram_02.png")
    img.save(out_path, dpi=(300, 300))
    print(f"Saved: {out_path}")
    return out_path


if __name__ == "__main__":
    build_diagram_1()
    build_diagram_2()
    print("All diagrams generated.")
