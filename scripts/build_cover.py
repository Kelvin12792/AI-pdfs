"""
Build cover: The AI Basics Nobody Made Clear
Full-bleed bright futuristic AI scene — text merged into illustration.
"""

import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 2480
HEIGHT = 3508
DPI = 300

# === PALETTE ===
CORAL = (204, 120, 92)
CORAL_BRIGHT = (240, 155, 120)
CORAL_HOT = (255, 180, 140)
CORAL_PALE = (255, 225, 208)
WHITE = (255, 255, 255)
CREAM = (252, 248, 244)
DARK = (26, 26, 26)
TEAL = (100, 220, 215)
TEAL_BRIGHT = (160, 245, 240)

FONT_DIR = "/home/user/AI-pdfs/assets/fonts"
font_title = ImageFont.truetype(f"{FONT_DIR}/Inter-Bold.ttf", 165)
font_subtitle = ImageFont.truetype(f"{FONT_DIR}/Inter-Medium.ttf", 62)
font_author = ImageFont.truetype(f"{FONT_DIR}/Inter-Medium.ttf", 44)
font_hud = ImageFont.truetype(f"{FONT_DIR}/Inter-Regular.ttf", 28)
font_data = ImageFont.truetype(f"{FONT_DIR}/Inter-Regular.ttf", 24)

random.seed(88)

# ============================================================
# BACKGROUND — warm gradient, bright center
# ============================================================
img = Image.new("RGB", (WIDTH, HEIGHT), (55, 40, 36))
draw = ImageDraw.Draw(img)

core_x, core_y = WIDTH // 2, int(HEIGHT * 0.36)

# Warm vertical gradient
for y in range(HEIGHT):
    t = y / HEIGHT
    # Brighter in the upper-middle portion
    brightness = math.exp(-((t - 0.36) ** 2) / 0.12)
    r = int(55 + 110 * brightness)
    g = int(40 + 70 * brightness)
    b = int(36 + 55 * brightness)
    draw.line([(0, y), (WIDTH, y)], fill=(min(255, r), min(255, g), min(255, b)))

# Radial brightening around core
for rad in range(800, 0, -4):
    t = rad / 800
    alpha = (1 - t) ** 2 * 0.4  # additive brightness
    # Read center color and brighten
    add_r = int(140 * alpha)
    add_g = int(95 * alpha)
    add_b = int(75 * alpha)
    base = img.getpixel((min(WIDTH-1, core_x), min(HEIGHT-1, max(0, core_y - rad + 1))))
    fill = (min(255, base[0] + add_r), min(255, base[1] + add_g), min(255, base[2] + add_b))
    draw.ellipse([core_x - rad, core_y - rad, core_x + rad, core_y + rad], fill=fill)

# ============================================================
# PERSPECTIVE GRID
# ============================================================
horizon_y = int(HEIGHT * 0.46)
floor_bottom = int(HEIGHT * 0.80)

for i in range(35):
    t = (i / 35) ** 1.8
    y = int(horizon_y + (floor_bottom - horizon_y) * t)
    alpha = t * 0.45
    draw.line([(120, y), (WIDTH - 120, y)],
              fill=(int(CORAL_BRIGHT[0] * alpha), int(CORAL_BRIGHT[1] * alpha), int(CORAL_BRIGHT[2] * alpha)),
              width=1)

for i in range(-16, 17):
    bottom_x = WIDTH // 2 + i * 140
    alpha = max(0.05, 0.4 - abs(i) * 0.022)
    draw.line([(WIDTH // 2, horizon_y), (bottom_x, floor_bottom)],
              fill=(int(CORAL_BRIGHT[0] * alpha), int(CORAL_BRIGHT[1] * alpha), int(CORAL_BRIGHT[2] * alpha)),
              width=1)

# ============================================================
# AI CORE — bright radiant sphere (no dark ring)
# ============================================================

# Wide soft glow — only adds brightness
for r in range(500, 0, -3):
    t = r / 500
    intensity = (1 - t) ** 1.5
    add = int(120 * intensity)
    cx1, cy1 = core_x - r, core_y - r
    cx2, cy2 = core_x + r, core_y + r
    # Sample background and add light
    try:
        bg = img.getpixel((core_x, max(0, core_y - r + 2)))
    except:
        bg = (100, 70, 60)
    fill = (min(255, bg[0] + add), min(255, bg[1] + int(add * 0.7)), min(255, bg[2] + int(add * 0.55)))
    draw.ellipse([cx1, cy1, cx2, cy2], fill=fill)

# Bright inner sphere
for r in range(180, 0, -2):
    t = r / 180
    cr = int(CORAL_HOT[0] * t + WHITE[0] * (1 - t))
    cg = int(CORAL_HOT[1] * t + WHITE[1] * (1 - t))
    cb = int(CORAL_HOT[2] * t + WHITE[2] * (1 - t))
    draw.ellipse([core_x - r, core_y - r, core_x + r, core_y + r], fill=(cr, cg, cb))

# White-hot center
for r in range(60, 0, -1):
    t = r / 60
    c = int(255 - 3 * t)
    draw.ellipse([core_x - r, core_y - r, core_x + r, core_y + r], fill=(c, c, c))

# Rings
for radius in [210, 280, 380]:
    alpha = 0.5 - radius / 1200
    rr = int(CORAL_PALE[0] * alpha)
    rg = int(CORAL_PALE[1] * alpha)
    rb = int(CORAL_PALE[2] * alpha)
    draw.ellipse([core_x - radius, core_y - radius, core_x + radius, core_y + radius],
                 outline=(min(255, rr + 60), min(255, rg + 40), min(255, rb + 35)), width=2)

# ============================================================
# CIRCUIT TRACES
# ============================================================
for i in range(18):
    angle = (2 * math.pi * i) / 18 + random.uniform(-0.1, 0.1)
    px = core_x + int(195 * math.cos(angle))
    py = core_y + int(195 * math.sin(angle))

    for seg in range(random.randint(3, 5)):
        seg_len = random.randint(50, 130)
        if seg % 2 == 0:
            nx = px + int(seg_len * math.cos(angle))
            ny = py + int(seg_len * math.sin(angle))
        else:
            perp = angle + math.pi / 2 * random.choice([-1, 1])
            nx = px + int(seg_len * 0.5 * math.cos(perp))
            ny = py + int(seg_len * 0.5 * math.sin(perp))

        dist = math.sqrt((nx - core_x)**2 + (ny - core_y)**2)
        alpha = max(0.1, 0.9 - dist / 600)
        color = (int(CORAL_BRIGHT[0] * alpha), int(CORAL_BRIGHT[1] * alpha), int(CORAL_BRIGHT[2] * alpha))
        draw.line([(px, py), (nx, ny)], fill=color, width=2)
        ns = random.randint(3, 7)
        draw.ellipse([nx - ns, ny - ns, nx + ns, ny + ns], fill=color)
        px, py = nx, ny

# ============================================================
# HOLOGRAPHIC PANELS — bright teal with glow effect
# ============================================================

def draw_panel(draw, x, y, w, h, tilt=0, alpha=0.7):
    pts = [(x + tilt, y), (x + w + tilt, y), (x + w - tilt, y + h), (x - tilt, y + h)]

    # Bright fill
    fill = (int(20 + TEAL[0] * alpha * 0.12),
            int(30 + TEAL[1] * alpha * 0.12),
            int(30 + TEAL[2] * alpha * 0.12))
    draw.polygon(pts, fill=fill)

    # Bright border
    border = (int(TEAL_BRIGHT[0] * alpha),
              int(TEAL_BRIGHT[1] * alpha),
              int(TEAL_BRIGHT[2] * alpha))
    draw.line([pts[0], pts[1]], fill=border, width=3)
    draw.line([pts[1], pts[2]], fill=border, width=2)
    draw.line([pts[2], pts[3]], fill=border, width=3)
    draw.line([pts[3], pts[0]], fill=border, width=2)

    # Bright inner bars
    for ly in range(y + 22, y + h - 12, 24):
        bar_w = random.randint(int(w * 0.25), int(w * 0.8))
        bar_alpha = alpha * 0.55
        bar_color = (int(TEAL[0] * bar_alpha), int(TEAL[1] * bar_alpha), int(TEAL[2] * bar_alpha))
        draw.line([(x + 18, ly), (x + 18 + bar_w, ly)], fill=bar_color, width=3)

    # Corner dots
    for p in pts:
        draw.ellipse([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill=border)

# Left side
draw_panel(draw, 90, 180, 420, 310, tilt=22, alpha=0.75)
draw_panel(draw, 130, 560, 370, 240, tilt=16, alpha=0.55)
draw_panel(draw, 70, 870, 400, 270, tilt=18, alpha=0.40)

# Right side
draw_panel(draw, 1970, 220, 420, 290, tilt=-22, alpha=0.75)
draw_panel(draw, 2010, 580, 370, 250, tilt=-14, alpha=0.55)
draw_panel(draw, 1990, 900, 390, 240, tilt=-16, alpha=0.40)

# ============================================================
# HEXAGON PATTERN — subtle background texture
# ============================================================
hex_size = 60
for row in range(-2, 30):
    for col in range(-2, 22):
        hx = col * hex_size * 1.75 + (row % 2) * hex_size * 0.875
        hy = row * hex_size * 1.5

        if hy > HEIGHT * 0.65 or hy < 0:
            continue

        dist = math.sqrt((hx - core_x)**2 + (hy - core_y)**2)
        if dist < 450 or dist > 1200:
            continue

        alpha = max(0, 0.12 - abs(dist - 800) / 5000)
        hex_color = (int(CORAL_BRIGHT[0] * alpha + 5), int(CORAL_BRIGHT[1] * alpha + 3), int(CORAL_BRIGHT[2] * alpha + 3))

        hex_pts = []
        for a in range(6):
            ang = math.pi / 3 * a + math.pi / 6
            hex_pts.append((hx + hex_size * 0.4 * math.cos(ang),
                           hy + hex_size * 0.4 * math.sin(ang)))
        draw.polygon(hex_pts, outline=hex_color)

# ============================================================
# DATA STREAMS
# ============================================================
for sx in [150, 260, 2220, 2330]:
    for idx in range(random.randint(10, 22)):
        sy = 50 + idx * random.randint(45, 70)
        if sy > HEIGHT * 0.60:
            break
        char = random.choice("0011010011")
        alpha = random.uniform(0.2, 0.5)
        color = (int(TEAL[0] * alpha), int(TEAL[1] * alpha), int(TEAL[2] * alpha))
        draw.text((sx + random.randint(-3, 3), sy), char, fill=color, font=font_data)

# ============================================================
# PARTICLES — bright sparks
# ============================================================
for _ in range(250):
    px = random.randint(20, WIDTH - 20)
    py = random.randint(20, int(HEIGHT * 0.70))
    dist = math.sqrt((px - core_x)**2 + (py - core_y)**2)
    size = random.randint(2, 7)

    if dist < 250:
        color = (255, 240, 230)
    elif dist < 500:
        alpha = random.uniform(0.5, 1.0)
        color = (int(CORAL_HOT[0] * alpha), int(CORAL_HOT[1] * alpha), int(CORAL_HOT[2] * alpha))
    else:
        alpha = random.uniform(0.15, 0.45)
        base = random.choice([CORAL_BRIGHT, TEAL])
        color = (int(base[0] * alpha + 20), int(base[1] * alpha + 15), int(base[2] * alpha + 15))

    draw.ellipse([px - size, py - size, px + size, py + size], fill=color)

# ============================================================
# GLOW PASS
# ============================================================
glow = img.copy().filter(ImageFilter.GaussianBlur(radius=14))
img = Image.blend(img, glow, alpha=0.22)
draw = ImageDraw.Draw(img)

# ============================================================
# BOTTOM TEXT OVERLAY — smooth gradient fade
# ============================================================
overlay_start = int(HEIGHT * 0.58)
for y in range(overlay_start, HEIGHT):
    t = (y - overlay_start) / (HEIGHT - overlay_start)
    alpha = min(0.94, t ** 0.7)
    bg_y = img.getpixel((WIDTH // 2, y))
    nr = int(bg_y[0] * (1 - alpha) + DARK[0] * alpha)
    ng = int(bg_y[1] * (1 - alpha) + DARK[1] * alpha)
    nb = int(bg_y[2] * (1 - alpha) + DARK[2] * alpha)
    draw.line([(0, y), (WIDTH, y)], fill=(nr, ng, nb))

# ============================================================
# TEXT
# ============================================================
text_x = 110
title_y = int(HEIGHT * 0.68)

draw.text((text_x, title_y), "The AI Basics", fill=CORAL_HOT, font=font_title)
bbox1 = font_title.getbbox("The AI Basics")
h1 = bbox1[3] - bbox1[1]

draw.text((text_x, title_y + h1 + 28), "Nobody Made Clear", fill=CORAL_HOT, font=font_title)
bbox2 = font_title.getbbox("Nobody Made Clear")
h2 = bbox2[3] - bbox2[1]

# Accent line
accent_y = title_y + h1 + 28 + h2 + 55
draw.line([(text_x, accent_y), (text_x + 450, accent_y)], fill=CORAL_BRIGHT, width=5)

# Subtitle
draw.text((text_x, accent_y + 45), "A Beginner's Guide to AI", fill=CREAM, font=font_subtitle)

# Author
draw.text((text_x, HEIGHT - 130), "by Kelvin M  |  AI Educator & Researcher",
          fill=(170, 160, 155), font=font_author)

# HUD
draw.text((60, 40), "AI SERIES  //  EDITION 01", fill=(140, 130, 122), font=font_hud)
draw.line([(60, 76), (370, 76)], fill=(110, 100, 95), width=1)
draw.text((WIDTH - 440, 40), "BASICS  //  FUNDAMENTALS", fill=(140, 130, 122), font=font_hud)

# ============================================================
# SAVE
# ============================================================
output_path = "/home/user/AI-pdfs/assets/covers/edition_01_cover.png"
img.save(output_path, "PNG", dpi=(DPI, DPI))
print(f"Cover saved: {output_path}")
print(f"Size: {img.size[0]}x{img.size[1]}px")
