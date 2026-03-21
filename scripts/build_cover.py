"""
Build cover image for: The AI Basics Nobody Made Clear
Layout: 60% abstract illustration (top) / 40% dark text band (bottom)
Design: Nodes transitioning from tangled/complex (left) to clean/organized (right)
Palette: Anthropic brand - coral, cream, dark
"""

import random
import math
from PIL import Image, ImageDraw, ImageFont

# === DIMENSIONS ===
WIDTH = 2480
HEIGHT = 3508
DPI = 300

# === COLORS (from STYLE_TOKENS.yaml) ===
CORAL = (204, 120, 92)           # #CC785C
CORAL_DARK = (158, 78, 46)      # #9E4E2E
CORAL_LIGHT = (242, 212, 200)   # #F2D4C8
CREAM_BG = (249, 246, 243)      # #F9F6F3
WHITE = (255, 255, 255)
DARK = (26, 26, 26)             # #1A1A1A
TEXT_MUTED = (136, 136, 136)    # #888888
TEXT_INVERSE = (255, 255, 255)
BORDER_COLOR = (224, 217, 212)  # #E0D9D4

# === LAYOUT ===
IMAGE_ZONE_HEIGHT = int(HEIGHT * 0.60)
TEXT_ZONE_HEIGHT = HEIGHT - IMAGE_ZONE_HEIGHT
PADDING = 66  # ~22mm at 300 DPI

# === FONTS ===
FONT_DIR = "/home/user/AI-pdfs/assets/fonts"
font_bold = ImageFont.truetype(f"{FONT_DIR}/Inter-Bold.ttf", 144)      # 36pt at 300 DPI ~= 144px
font_regular = ImageFont.truetype(f"{FONT_DIR}/Inter-Regular.ttf", 56)  # 14pt ~= 56px
font_medium = ImageFont.truetype(f"{FONT_DIR}/Inter-Medium.ttf", 48)   # 12pt ~= 48px

# Create canvas
img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# ============================================================
# TOP 60%: Abstract illustration - complexity to clarity
# ============================================================

# Gradient background: white to soft cream
for y in range(IMAGE_ZONE_HEIGHT):
    t = y / IMAGE_ZONE_HEIGHT
    r = int(WHITE[0] + (CREAM_BG[0] - WHITE[0]) * t * 0.5)
    g = int(WHITE[1] + (CREAM_BG[1] - WHITE[1]) * t * 0.5)
    b = int(WHITE[2] + (CREAM_BG[2] - WHITE[2]) * t * 0.5)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

random.seed(42)

# --- Generate nodes across the illustration ---
# Left side: dense, tangled, overlapping (complex)
# Right side: clean, organized, spaced (clarity)

nodes = []
connections = []

# Vertical center of illustration zone
cy = IMAGE_ZONE_HEIGHT // 2

# LEFT ZONE: Chaotic cluster (x: 150 to 900)
for i in range(55):
    x = random.randint(150, 900)
    y = random.randint(cy - 500, cy + 500)
    size = random.randint(18, 50)
    opacity_factor = random.uniform(0.3, 1.0)
    nodes.append({"x": x, "y": y, "size": size, "zone": "left", "opacity": opacity_factor})

# MIDDLE ZONE: Transition (x: 900 to 1600)
for i in range(30):
    x = random.randint(900, 1600)
    spread = int(400 * (1 - (x - 900) / 700))
    y = random.randint(cy - max(spread, 150), cy + max(spread, 150))
    size = random.randint(22, 42)
    nodes.append({"x": x, "y": y, "size": size, "zone": "mid", "opacity": random.uniform(0.5, 1.0)})

# RIGHT ZONE: Clean grid-like arrangement (x: 1600 to 2350)
grid_positions = []
cols = 5
rows = 5
x_start, x_end = 1700, 2300
y_start, y_end = cy - 350, cy + 350
for row in range(rows):
    for col in range(cols):
        x = x_start + col * ((x_end - x_start) // (cols - 1))
        y = y_start + row * ((y_end - y_start) // (rows - 1))
        # Small jitter for organic feel
        x += random.randint(-15, 15)
        y += random.randint(-15, 15)
        size = random.randint(26, 36)
        nodes.append({"x": x, "y": y, "size": size, "zone": "right", "opacity": 1.0})
        grid_positions.append(len(nodes) - 1)

# --- Draw connections ---

# Left zone: messy tangled lines
left_nodes = [n for n in nodes if n["zone"] == "left"]
for i, n1 in enumerate(left_nodes):
    num_connections = random.randint(1, 4)
    targets = random.sample(left_nodes, min(num_connections, len(left_nodes)))
    for n2 in targets:
        if n1 is not n2:
            dist = math.sqrt((n1["x"] - n2["x"])**2 + (n1["y"] - n2["y"])**2)
            if dist < 400:
                alpha = random.uniform(0.15, 0.4)
                line_color = (
                    int(CORAL_LIGHT[0] * alpha + WHITE[0] * (1 - alpha)),
                    int(CORAL_LIGHT[1] * alpha + WHITE[1] * (1 - alpha)),
                    int(CORAL_LIGHT[2] * alpha + WHITE[2] * (1 - alpha)),
                )
                draw.line([(n1["x"], n1["y"]), (n2["x"], n2["y"])], fill=line_color, width=2)

# Middle zone: fewer, cleaner connections
mid_nodes = [n for n in nodes if n["zone"] == "mid"]
for i, n1 in enumerate(mid_nodes):
    targets = random.sample(mid_nodes, min(2, len(mid_nodes)))
    for n2 in targets:
        if n1 is not n2:
            dist = math.sqrt((n1["x"] - n2["x"])**2 + (n1["y"] - n2["y"])**2)
            if dist < 350:
                line_color = CORAL_LIGHT
                draw.line([(n1["x"], n1["y"]), (n2["x"], n2["y"])], fill=line_color, width=2)

# Right zone: clean organized grid connections
right_nodes = [n for n in nodes if n["zone"] == "right"]
for i, n1 in enumerate(right_nodes):
    for n2 in right_nodes:
        if n1 is not n2:
            dist = math.sqrt((n1["x"] - n2["x"])**2 + (n1["y"] - n2["y"])**2)
            if dist < 220:
                draw.line([(n1["x"], n1["y"]), (n2["x"], n2["y"])], fill=CORAL_LIGHT, width=3)

# Transition connections: bridge from mid to right
for n1 in mid_nodes[-8:]:
    closest = min(right_nodes, key=lambda n2: math.sqrt((n1["x"] - n2["x"])**2 + (n1["y"] - n2["y"])**2))
    draw.line([(n1["x"], n1["y"]), (closest["x"], closest["y"])], fill=CORAL_LIGHT, width=2)

# --- Draw nodes on top ---
for n in nodes:
    x, y, size = n["x"], n["y"], n["size"]
    opacity = n["opacity"]

    if n["zone"] == "left":
        # Muted, smaller, some barely visible
        fill_r = int(CORAL_LIGHT[0] * opacity + WHITE[0] * (1 - opacity))
        fill_g = int(CORAL_LIGHT[1] * opacity + WHITE[1] * (1 - opacity))
        fill_b = int(CORAL_LIGHT[2] * opacity + WHITE[2] * (1 - opacity))
        fill = (fill_r, fill_g, fill_b)
        border = BORDER_COLOR
        border_w = 1
    elif n["zone"] == "mid":
        # Transitioning to coral
        fill = CORAL_LIGHT
        border = CORAL
        border_w = 2
    else:
        # Right: strong coral, clean
        fill = CORAL_LIGHT
        border = CORAL
        border_w = 3

    draw.ellipse(
        [x - size, y - size, x + size, y + size],
        fill=fill,
        outline=border,
        width=border_w,
    )

# A few prominent nodes on the right with darker coral fill
for n in right_nodes[::4]:
    x, y, size = n["x"], n["y"], n["size"]
    inner = size - 8
    if inner > 5:
        draw.ellipse(
            [x - inner, y - inner, x + inner, y + inner],
            fill=CORAL,
        )

# ============================================================
# BOTTOM 40%: Dark text band
# ============================================================

draw.rectangle(
    [(0, IMAGE_ZONE_HEIGHT), (WIDTH, HEIGHT)],
    fill=DARK,
)

# --- Text positioning within dark band ---
band_top = IMAGE_ZONE_HEIGHT
band_height = TEXT_ZONE_HEIGHT
text_x = PADDING + 20

# Title: "The AI Basics Nobody Made Clear"
# Split into two lines for impact
title_line1 = "The AI Basics"
title_line2 = "Nobody Made Clear"

title_y = band_top + int(band_height * 0.18)

draw.text((text_x, title_y), title_line1, fill=CORAL, font=font_bold)
bbox1 = font_bold.getbbox(title_line1)
line1_height = bbox1[3] - bbox1[1]

draw.text((text_x, title_y + line1_height + 20), title_line2, fill=CORAL, font=font_bold)
bbox2 = font_bold.getbbox(title_line2)
line2_height = bbox2[3] - bbox2[1]

# Subtitle: "A Beginner's Guide to AI"
subtitle_y = title_y + line1_height + 20 + line2_height + 60
draw.text((text_x, subtitle_y), "A Beginner's Guide to AI", fill=TEXT_INVERSE, font=font_regular)

# Author line
author_y = HEIGHT - PADDING - 80
draw.text((text_x, author_y), "by Kelvin M, AI Educator & Researcher", fill=TEXT_MUTED, font=font_medium)

# Thin accent line between subtitle and author
line_y = subtitle_y + 100
draw.line([(text_x, line_y), (text_x + 300, line_y)], fill=CORAL, width=4)

# ============================================================
# SAVE
# ============================================================
output_path = "/home/user/AI-pdfs/assets/covers/edition_01_cover.png"
img.save(output_path, "PNG", dpi=(DPI, DPI))
print(f"Cover saved: {output_path}")
print(f"Size: {img.size[0]}x{img.size[1]}px")
