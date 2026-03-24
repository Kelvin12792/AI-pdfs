#!/usr/bin/env python3
"""
Cover art generator for AI Education Series — Edition 01: What is AI?
Recreates the circuit-brain cover design matching Kelvin M's provided cover image.
Output: assets/covers/cover_01.png  (2480 x 3508 px @ 300 DPI)

To use your own cover image instead, just place it at assets/covers/cover_01.png
and this script will be skipped by build_pdf.py.
"""

import math
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ── Output spec ──────────────────────────────────────────────────────────────
W, H   = 2480, 3508   # A4 @ 300 DPI
DPI    = 300
OUT    = "assets/covers/cover_01.png"

# ── Palette (matching the provided design) ───────────────────────────────────
BG_TOP      = (20, 15, 60)      # deep indigo top
BG_MID      = (30, 20, 80)      # mid purple
BG_BOT_IMG  = (18, 12, 48)      # bottom of image zone
TEXT_BAND   = (16, 10, 42)      # very dark band behind text
CORAL       = (204, 120, 92)    # #CC785C series label
WHITE       = (255, 255, 255)
MUTED       = (160, 155, 185)   # muted author line

HEX_GLOW    = (220, 100, 60)    # central hexagon glow (coral-orange)
HEX_CORE    = (180, 80, 50)
TEAL        = (42, 157, 143)    # #2A9D8F circuit dots
AMBER       = (233, 196, 106)   # #E9C46A circuit dots
PURPLE_LINE = (100, 70, 160)    # circuit line base

DIVIDER_LINE = (204, 120, 92)   # coral horizontal rule


def hex_corners(cx, cy, r):
    """Return 6 corners of a flat-top hexagon."""
    pts = []
    for i in range(6):
        angle = math.radians(60 * i)
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return pts


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def draw_glow_circle(draw, cx, cy, r_max, color, steps=40):
    for i in range(steps, 0, -1):
        t = i / steps
        r = int(r_max * t)
        alpha = int(60 * (1 - t))
        c = (*color, alpha)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)


def generate_cover():
    os.makedirs("assets/covers", exist_ok=True)

    img  = Image.new("RGB", (W, H), BG_TOP)
    draw = ImageDraw.Draw(img, "RGBA")

    # ── Background gradient (top → bottom) ───────────────────────────────────
    for y in range(H):
        t = y / H
        if t < 0.65:
            c = lerp_color(BG_TOP, BG_MID, t / 0.65)
        else:
            c = lerp_color(BG_MID, BG_BOT_IMG, (t - 0.65) / 0.35)
        draw.line([(0, y), (W, y)], fill=c)

    # ── Circuit traces radiating from centre ──────────────────────────────────
    cx, cy = W // 2, int(H * 0.36)   # centre of the brain hexagon
    random.seed(42)

    dot_colors = [TEAL, AMBER, CORAL, PURPLE_LINE, (180, 120, 200)]
    n_traces   = 36

    for i in range(n_traces):
        angle  = math.radians(i * (360 / n_traces) + random.uniform(-4, 4))
        length = random.randint(350, 800)
        col    = random.choice(dot_colors)

        # orthogonal L-shaped trace (circuit board style)
        x0 = cx + int(250 * math.cos(angle))
        y0 = cy + int(250 * math.sin(angle))

        # first leg: horizontal or vertical depending on quadrant
        leg1 = random.randint(100, 300)
        if abs(math.cos(angle)) > 0.5:
            x1, y1 = x0 + int(leg1 * math.cos(angle)), y0
        else:
            x1, y1 = x0, y0 + int(leg1 * math.sin(angle))

        # second leg: continue outward
        x2 = x1 + int((length - leg1) * math.cos(angle))
        y2 = y1 + int((length - leg1) * math.sin(angle))

        line_col = (*col, 140)
        draw.line([(x0, y0), (x1, y1)], fill=line_col, width=4)
        draw.line([(x1, y1), (x2, y2)], fill=line_col, width=4)

        # endpoint dot
        r = random.randint(12, 24)
        draw.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=(*col, 220))

        # small square notch at bend
        draw.rectangle([x1 - 6, y1 - 6, x1 + 6, y1 + 6], fill=(*col, 180))

    # ── Central glow ─────────────────────────────────────────────────────────
    glow_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd       = ImageDraw.Draw(glow_img)
    draw_glow_circle(gd, cx, cy, 520, HEX_GLOW, steps=60)
    blurred  = glow_img.filter(ImageFilter.GaussianBlur(radius=60))
    img.paste(Image.alpha_composite(img.convert("RGBA"), blurred).convert("RGB"))
    draw = ImageDraw.Draw(img, "RGBA")

    # ── Hexagon outline ───────────────────────────────────────────────────────
    for r_off, alpha, width in [(240, 40, 3), (220, 80, 3), (200, 160, 5)]:
        pts = hex_corners(cx, cy, r_off)
        poly = [p for pt in pts for p in pt]
        draw.polygon(pts, fill=(*HEX_CORE, alpha))
        draw.line(pts + [pts[0]], fill=(*HEX_GLOW, 200), width=width)

    # ── Brain silhouette (geometric approximation) ────────────────────────────
    # Left hemisphere
    bx, by = cx - 40, cy
    for dx, dy, rx, ry in [
        (-60, -30, 70, 60), (-90, 10, 55, 50), (-40, 50, 65, 45),
        (20, -70, 50, 40),  (60, -20, 45, 55), (80, 40, 50, 40),
        (10, 70, 60, 40),
    ]:
        col_a = (*HEX_GLOW, 100)
        draw.ellipse([bx+dx-rx, by+dy-ry, bx+dx+rx, by+dy+ry], outline=col_a, width=5)

    # Midline
    draw.line([(cx, cy - 160), (cx, cy + 160)], fill=(*HEX_GLOW, 140), width=4)

    # ── Small circuit nodes on hexagon face ───────────────────────────────────
    for _ in range(12):
        nx = cx + random.randint(-160, 160)
        ny = cy + random.randint(-140, 140)
        nr = random.randint(8, 18)
        draw.ellipse([nx-nr, ny-nr, nx+nr, ny+nr], fill=(*HEX_GLOW, 160))
        draw.line([(nx, ny), (nx + random.randint(-50, 50), ny + random.randint(-50, 50))],
                  fill=(*HEX_GLOW, 100), width=3)

    # ── Text band (bottom 40%) ────────────────────────────────────────────────
    band_y = int(H * 0.62)

    # Dark overlay for text area
    draw.rectangle([0, band_y, W, H], fill=(*TEXT_BAND, 240))

    # ── Typography ─────────────────────────────────────────────────────────
    # Fall back gracefully through available system fonts
    font_paths = {
        "bold":   "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "regular":"/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "italic": "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
        "bolditalic": "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
    }

    try:
        f_series  = ImageFont.truetype(font_paths["bold"], 80)
        f_title   = ImageFont.truetype(font_paths["bold"], 320)
        f_tagline = ImageFont.truetype(font_paths["bolditalic"], 85)
        f_author  = ImageFont.truetype(font_paths["regular"], 80)
    except Exception:
        f_series = f_title = f_tagline = f_author = ImageFont.load_default()

    draw_rl = ImageDraw.Draw(img)   # standard draw (no alpha)

    # Series label — "AI EDUCATION SERIES — EDITION 01"
    series_text = "AI EDUCATION SERIES — EDITION 01"
    bbox = draw_rl.textbbox((0, 0), series_text, font=f_series)
    tw   = bbox[2] - bbox[0]
    sx   = (W - tw) // 2
    sy   = band_y + 90
    draw_rl.text((sx, sy), series_text, font=f_series, fill=CORAL)

    # Main title — "What is AI?"
    title_text = "What is AI?"
    bbox  = draw_rl.textbbox((0, 0), title_text, font=f_title)
    tw    = bbox[2] - bbox[0]
    tx    = (W - tw) // 2
    ty    = sy + 110
    draw_rl.text((tx, ty), title_text, font=f_title, fill=WHITE)

    # Tagline (two lines)
    tag1 = "The complete beginner's guide to"
    tag2 = "understanding artificial intelligence"
    for line_idx, line in enumerate([tag1, tag2]):
        bbox = draw_rl.textbbox((0, 0), line, font=f_tagline)
        tw   = bbox[2] - bbox[0]
        lx   = (W - tw) // 2
        ly   = ty + 360 + line_idx * 100
        draw_rl.text((lx, ly), line, font=f_tagline, fill=WHITE)

    # Coral divider line
    div_y = ty + 600
    draw_rl.rectangle([200, div_y, W - 200, div_y + 6], fill=CORAL)

    # Author line
    author_text = "by Kelvin M — AI Educator & Researcher"
    bbox = draw_rl.textbbox((0, 0), author_text, font=f_author)
    tw   = bbox[2] - bbox[0]
    ax   = (W - tw) // 2
    ay   = div_y + 60
    draw_rl.text((ax, ay), author_text, font=f_author, fill=MUTED)

    # Small diamond icon (bottom-right)
    dx, dy = W - 160, H - 160
    diamond = [(dx, dy - 55), (dx + 55, dy), (dx, dy + 55), (dx - 55, dy)]
    draw_rl.polygon(diamond, fill=CORAL)

    # ── Save ─────────────────────────────────────────────────────────────────
    img.save(OUT, "PNG", dpi=(DPI, DPI))
    size_kb = os.path.getsize(OUT) // 1024
    print(f"Cover saved → {OUT}  ({W}×{H}px, {size_kb} KB)")


if __name__ == "__main__":
    generate_cover()
