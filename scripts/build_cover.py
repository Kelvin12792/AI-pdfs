"""
Build cover image for: The AI Basics Nobody Made Clear
Layout: 60% illustration (top) / 40% dark text band (bottom)
Concept: A glowing circular lens/portal at center radiating light outward.
         Scattered symbols (?, !, 0, 1) float in the outer darkness/haze,
         but dissolve into clarity near the bright center.
         Invokes curiosity: "What's at the center? What will I discover?"
Palette: Anthropic brand - coral, cream, dark
"""

import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# === DIMENSIONS ===
WIDTH = 2480
HEIGHT = 3508
DPI = 300

# === COLORS ===
CORAL = (204, 120, 92)
CORAL_DARK = (158, 78, 46)
CORAL_LIGHT = (242, 212, 200)
CORAL_GLOW = (230, 160, 130)
CREAM_BG = (249, 246, 243)
WHITE = (255, 255, 255)
DARK = (26, 26, 26)
DARK_MID = (40, 36, 34)
TEXT_MUTED = (136, 136, 136)
TEXT_INVERSE = (255, 255, 255)

# === LAYOUT ===
IMAGE_ZONE_HEIGHT = int(HEIGHT * 0.60)
TEXT_ZONE_HEIGHT = HEIGHT - IMAGE_ZONE_HEIGHT
PADDING = 66

# === FONTS ===
FONT_DIR = "/home/user/AI-pdfs/assets/fonts"
font_bold = ImageFont.truetype(f"{FONT_DIR}/Inter-Bold.ttf", 144)
font_regular = ImageFont.truetype(f"{FONT_DIR}/Inter-Regular.ttf", 56)
font_medium = ImageFont.truetype(f"{FONT_DIR}/Inter-Medium.ttf", 48)
font_symbol_large = ImageFont.truetype(f"{FONT_DIR}/Inter-Bold.ttf", 96)
font_symbol_med = ImageFont.truetype(f"{FONT_DIR}/Inter-Bold.ttf", 64)
font_symbol_small = ImageFont.truetype(f"{FONT_DIR}/Inter-Medium.ttf", 40)

random.seed(77)

# ============================================================
# TOP 60%: CURIOSITY PORTAL — dark background with glowing center
# ============================================================

img = Image.new("RGB", (WIDTH, HEIGHT), DARK)
draw = ImageDraw.Draw(img)

cx = WIDTH // 2
cy = IMAGE_ZONE_HEIGHT // 2

# --- STEP 1: Dark-to-warm radial gradient background for illustration zone ---
max_radius = int(math.sqrt(cx**2 + cy**2))
for r in range(max_radius, 0, -1):
    t = r / max_radius  # 1 at edge, 0 at center
    # Edge: dark charcoal. Center: warm cream/coral glow
    bg_r = int(DARK_MID[0] * t + CREAM_BG[0] * (1 - t))
    bg_g = int(DARK_MID[1] * t + CREAM_BG[1] * (1 - t))
    bg_b = int(DARK_MID[2] * t + CREAM_BG[2] * (1 - t))
    draw.ellipse(
        [cx - r, cy - r, cx + r, cy + r],
        fill=(bg_r, bg_g, bg_b),
    )

# --- STEP 2: Radiating lines from center (light rays) ---
num_rays = 48
for i in range(num_rays):
    angle = (2 * math.pi * i) / num_rays + random.uniform(-0.02, 0.02)
    ray_length = random.randint(500, 900)

    x1 = cx + int(120 * math.cos(angle))
    y1 = cy + int(120 * math.sin(angle))
    x2 = cx + int(ray_length * math.cos(angle))
    y2 = cy + int(ray_length * math.sin(angle))

    # Rays fade: bright coral near center, transparent at tips
    for step in range(20):
        t = step / 20
        sx = int(x1 + (x2 - x1) * t)
        sy = int(y1 + (y2 - y1) * t)
        ex = int(x1 + (x2 - x1) * (t + 0.06))
        ey = int(y1 + (y2 - y1) * (t + 0.06))
        alpha = 1 - t  # fades out
        ray_r = int(CORAL_GLOW[0] * alpha + DARK_MID[0] * (1 - alpha))
        ray_g = int(CORAL_GLOW[1] * alpha + DARK_MID[1] * (1 - alpha))
        ray_b = int(CORAL_GLOW[2] * alpha + DARK_MID[2] * (1 - alpha))
        width = max(1, int(4 * alpha))
        draw.line([(sx, sy), (ex, ey)], fill=(ray_r, ray_g, ray_b), width=width)

# --- STEP 3: Concentric rings (lens/portal rings) ---
ring_radii = [140, 200, 280, 400, 560]
for i, radius in enumerate(ring_radii):
    t = i / len(ring_radii)
    alpha = 1 - t * 0.7
    ring_r = int(CORAL[0] * alpha + DARK_MID[0] * (1 - alpha))
    ring_g = int(CORAL[1] * alpha + DARK_MID[1] * (1 - alpha))
    ring_b = int(CORAL[2] * alpha + DARK_MID[2] * (1 - alpha))
    width = max(2, int(5 * (1 - t * 0.5)))
    draw.ellipse(
        [cx - radius, cy - radius, cx + radius, cy + radius],
        outline=(ring_r, ring_g, ring_b),
        width=width,
    )

# --- STEP 4: Bright glowing core ---
# Multiple overlapping circles for glow effect
for r in range(150, 0, -2):
    t = r / 150  # 1 at edge, 0 at center
    core_r = int(CORAL[0] * t + WHITE[0] * (1 - t))
    core_g = int(CORAL[1] * t + WHITE[1] * (1 - t))
    core_b = int(CORAL[2] * t + WHITE[2] * (1 - t))
    draw.ellipse(
        [cx - r, cy - r, cx + r, cy + r],
        fill=(core_r, core_g, core_b),
    )

# Inner bright white-hot center
for r in range(50, 0, -1):
    t = r / 50
    c = int(255 * (1 - t * 0.15))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(c, c, c))

# --- STEP 5: Floating symbols in the outer zone ---
# Symbols: ?, 0, 1, ! — scattered in darkness, fading toward center
symbols = ["?", "?", "?", "0", "1", "1", "0", "?", "!", "?", "0", "1",
           "?", "1", "0", "?", "?", "0", "1", "!", "?", "0", "1", "?",
           "?", "0", "1", "0", "1", "?", "!", "0", "1", "?", "0", "1"]

for sym in symbols:
    # Place in outer zone (distance 350-1100 from center)
    angle = random.uniform(0, 2 * math.pi)
    dist = random.randint(400, 1100)
    sx = cx + int(dist * math.cos(angle))
    sy = cy + int(dist * math.sin(angle))

    # Skip if outside illustration zone
    if sy < 30 or sy > IMAGE_ZONE_HEIGHT - 30 or sx < 30 or sx > WIDTH - 30:
        continue

    # Opacity based on distance: far = more visible, near center = fading
    t = min(1, (dist - 350) / 700)
    alpha = t * random.uniform(0.3, 0.8)

    sym_r = int(CORAL_LIGHT[0] * alpha + DARK_MID[0] * (1 - alpha))
    sym_g = int(CORAL_LIGHT[1] * alpha + DARK_MID[1] * (1 - alpha))
    sym_b = int(CORAL_LIGHT[2] * alpha + DARK_MID[2] * (1 - alpha))

    font_choice = random.choice([font_symbol_large, font_symbol_med, font_symbol_small])
    draw.text((sx, sy), sym, fill=(sym_r, sym_g, sym_b), font=font_choice, anchor="mm")

# --- STEP 6: Small orbiting dots (like particles drawn to the light) ---
for _ in range(80):
    angle = random.uniform(0, 2 * math.pi)
    dist = random.randint(160, 700)
    px = cx + int(dist * math.cos(angle))
    py = cy + int(dist * math.sin(angle))

    if py < 10 or py > IMAGE_ZONE_HEIGHT - 10:
        continue

    t = (dist - 160) / 540
    dot_size = random.randint(3, int(8 + t * 8))
    alpha = 0.4 + t * 0.5
    dot_r = int(CORAL[0] * alpha + CREAM_BG[0] * (1 - alpha))
    dot_g = int(CORAL[1] * alpha + CREAM_BG[1] * (1 - alpha))
    dot_b = int(CORAL[2] * alpha + CREAM_BG[2] * (1 - alpha))

    draw.ellipse(
        [px - dot_size, py - dot_size, px + dot_size, py + dot_size],
        fill=(dot_r, dot_g, dot_b),
    )

# --- STEP 7: Subtle arc paths (orbital trails) ---
for i in range(6):
    orbit_r = random.randint(250, 650)
    start_angle = random.uniform(0, 2 * math.pi)
    arc_length = random.uniform(0.4, 1.2)

    points = []
    for step in range(60):
        t = step / 60
        a = start_angle + arc_length * t
        ox = cx + int(orbit_r * math.cos(a))
        oy = cy + int(orbit_r * math.sin(a) * 0.85)  # slight vertical compression
        points.append((ox, oy))

    if len(points) > 1:
        alpha = 0.3
        trail_r = int(CORAL_LIGHT[0] * alpha + DARK_MID[0] * (1 - alpha))
        trail_g = int(CORAL_LIGHT[1] * alpha + DARK_MID[1] * (1 - alpha))
        trail_b = int(CORAL_LIGHT[2] * alpha + DARK_MID[2] * (1 - alpha))
        draw.line(points, fill=(trail_r, trail_g, trail_b), width=2)

# ============================================================
# Soft blur on the illustration for a dreamy glow
# ============================================================
illustration = img.crop((0, 0, WIDTH, IMAGE_ZONE_HEIGHT))
# Blend original with slightly blurred version for glow
blurred = illustration.filter(ImageFilter.GaussianBlur(radius=6))
illustration = Image.blend(illustration, blurred, alpha=0.35)
img.paste(illustration, (0, 0))

# Redraw on the composited image
draw = ImageDraw.Draw(img)

# ============================================================
# BOTTOM 40%: Dark text band
# ============================================================

draw.rectangle(
    [(0, IMAGE_ZONE_HEIGHT), (WIDTH, HEIGHT)],
    fill=DARK,
)

# Subtle gradient transition at the top of text band
for y in range(40):
    t = y / 40
    tr_r = int(DARK_MID[0] * (1 - t) + DARK[0] * t)
    tr_g = int(DARK_MID[1] * (1 - t) + DARK[1] * t)
    tr_b = int(DARK_MID[2] * (1 - t) + DARK[2] * t)
    draw.line([(0, IMAGE_ZONE_HEIGHT + y), (WIDTH, IMAGE_ZONE_HEIGHT + y)], fill=(tr_r, tr_g, tr_b))

band_top = IMAGE_ZONE_HEIGHT
band_height = TEXT_ZONE_HEIGHT
text_x = PADDING + 20

# Title
title_line1 = "The AI Basics"
title_line2 = "Nobody Made Clear"
title_y = band_top + int(band_height * 0.18)

draw.text((text_x, title_y), title_line1, fill=CORAL, font=font_bold)
bbox1 = font_bold.getbbox(title_line1)
line1_height = bbox1[3] - bbox1[1]

draw.text((text_x, title_y + line1_height + 20), title_line2, fill=CORAL, font=font_bold)
bbox2 = font_bold.getbbox(title_line2)
line2_height = bbox2[3] - bbox2[1]

# Subtitle
subtitle_y = title_y + line1_height + 20 + line2_height + 60
draw.text((text_x, subtitle_y), "A Beginner's Guide to AI", fill=TEXT_INVERSE, font=font_regular)

# Author line
author_y = HEIGHT - PADDING - 80
draw.text((text_x, author_y), "by Kelvin M, AI Educator & Researcher", fill=TEXT_MUTED, font=font_medium)

# Accent line
line_y = subtitle_y + 100
draw.line([(text_x, line_y), (text_x + 300, line_y)], fill=CORAL, width=4)

# ============================================================
# SAVE
# ============================================================
output_path = "/home/user/AI-pdfs/assets/covers/edition_01_cover.png"
img.save(output_path, "PNG", dpi=(DPI, DPI))
print(f"Cover saved: {output_path}")
print(f"Size: {img.size[0]}x{img.size[1]}px")
