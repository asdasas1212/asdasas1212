"""Rebuild the self-hosted profile artwork with Pillow and NumPy."""

from pathlib import Path
import html

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
W, H = 1000, 440
MINT, CYAN, PURPLE = (61, 245, 167), (52, 209, 255), (167, 139, 250)
FONT_DIR = Path("/System/Library/Fonts")


def font(size, bold=False, mono=False):
    candidates = (
        [FONT_DIR / "Menlo.ttc", Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")]
        if mono else [
            FONT_DIR / "Supplemental" / ("Trebuchet MS Bold.ttf" if bold else "Trebuchet MS.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


F_BIG, F_SUB = font(85, bold=True), font(21)
F_MONO, F_SMALL, F_BADGE = font(15, mono=True), font(12, mono=True), font(15, bold=True)
ygrid, xgrid = np.mgrid[0:H, 0:W]
rgb = np.zeros((H, W, 3), dtype=np.float32)
rgb[:] = [5, 10, 14]
for cx, cy, radius, color, strength in [
    (110, 50, 330, MINT, 0.12), (930, 180, 360, CYAN, 0.10),
    (600, 510, 280, PURPLE, 0.10),
]:
    falloff = np.exp(-((xgrid - cx) ** 2 + (ygrid - cy) ** 2) / radius**2) * strength
    rgb += falloff[:, :, None] * np.array(color)[None, None, :]
base = Image.fromarray(np.uint8(np.clip(rgb, 0, 255)))
draw = ImageDraw.Draw(base)
for x in range(18, W, 26):
    for y in range(18, H, 26):
        draw.ellipse((x, y, x + 1, y + 1), fill=(28, 45, 47))
draw.rounded_rectangle((1, 1, W - 2, H - 2), 20, outline=(33, 61, 61), width=1)
title_mask = Image.new("L", (W, H))
ImageDraw.Draw(title_mask).text((W / 2, 120), "See. Think. Move.", font=F_BIG, fill=255, anchor="mt")
colors = np.array([MINT, CYAN, PURPLE, MINT], dtype=float)
frames = []


def center_text(d, y, text, f, fill):
    d.text((W / 2, y), text, font=f, fill=fill, anchor="mt")


def box(d, rect, color, label, strength):
    x, y, bw, bh = rect
    c = tuple(int(v * strength) for v in color)
    dim = tuple(max(10, int(v * strength * 0.3)) for v in color)
    d.rectangle((x, y, x + bw, y + bh), outline=dim, width=1)
    for xx, yy, dx, dy in [
        (x, y, 1, 1), (x + bw, y, -1, 1),
        (x, y + bh, 1, -1), (x + bw, y + bh, -1, -1),
    ]:
        d.line((xx + dx * 13, yy, xx, yy, xx, yy + dy * 13), fill=c, width=2)
    d.rectangle((x, y - 17, x + len(label) * 7 + 10, y - 1), fill=c)
    d.text((x + 5, y - 16), label, font=F_SMALL, fill=(5, 10, 14))


for index in range(96):
    t = index / 12
    im = base.copy()
    d = ImageDraw.Draw(im)
    for rect, c, label, delay in [
        ((38, 89, 119, 94), MINT, "scene", 0.0),
        ((827, 70, 129, 118), CYAN, "goal", 1.2),
        ((73, 305, 98, 77), PURPLE, "robot", 3.2),
        ((853, 300, 100, 68), MINT, "path", 4.5),
    ]:
        phase = (t - delay) % 8
        strength = max(0, min(1, phase / 0.6, (4.7 - phase) / 0.8)) * 0.65
        if strength > 0:
            box(d, rect, c, label, strength)
    phase = ((np.arange(W) / 470 + t / 8) % 1) * 3
    slots = phase.astype(int)
    frac = (phase - slots)[:, None]
    line = colors[slots] * (1 - frac) + colors[slots + 1] * frac
    grad = Image.fromarray(np.uint8(np.repeat(line[None, :, :], H, axis=0)))
    im.paste(grad, (0, 0), title_mask)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((354, 54, 646, 91), radius=18, fill=(13, 26, 30), outline=(40, 64, 63))
    d.ellipse((371, 69, 378, 76), fill=MINT)
    d.text((392, 65), "hkx  /  @asdasas1212", font=F_BADGE, fill=(217, 236, 229))
    center_text(d, 233, "Robotics  /  Vision-Language Models  /  Navigation", F_SUB, (180, 205, 197))
    d.rounded_rectangle((224, 288, 776, 350), radius=12, fill=(7, 16, 21), outline=(37, 62, 62))
    d.text((244, 311), ">", font=F_MONO, fill=MINT)
    command = "robot.navigate('understand the world')"
    if t < 0.7:
        shown = command
    elif t < 1.3:
        shown = command[: max(0, int(len(command) * (1.3 - t) / 0.6))]
    elif t < 4.6:
        shown = command[: int(len(command) * (t - 1.3) / 3.3)]
    else:
        shown = command
    d.text((266, 311), shown, font=F_MONO, fill=(212, 232, 225))
    caret_x = 266 + d.textlength(shown, font=F_MONO)
    if index % 12 < 7:
        d.rectangle((caret_x + 3, 312, caret_x + 10, 326), fill=MINT)
    center_text(d, 388, "perceive  >  understand  >  plan  >  act", F_SMALL, (108, 145, 133))
    frames.append(im)

palette_sample = Image.new("RGB", (W, H * 4))
for j, idx in enumerate([0, 24, 48, 72]):
    palette_sample.paste(frames[idx], (0, H * j))
palette = palette_sample.quantize(colors=128)
indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
indexed[0].save(
    ASSETS / "profile-hero.gif", save_all=True, append_images=indexed[1:],
    duration=[80, 80, 90] * 32, loop=0, optimize=True, disposal=1,
)
frames[0].save(ASSETS / "profile-hero.png", optimize=True)

for slug, title, subtitle, desc, accent, label in [
    ("notes", "kx-public-notes", "AI, data & robotics", "Learning in public, one note at a time.", "#3df5a7", "notes"),
    ("cnn", "CNN1", "Computer vision", "Image recognition experiments in Python.", "#34d1ff", "vision"),
    ("llm", "LLM", "Large language models", "Play hard. Practice harder.", "#a78bfa", "language"),
    ("quote", "quote-skill", "JavaScript", "A public skill project, built with code.", "#ffc94d", "tools"),
]:
    (ASSETS / f"project-{slug}.svg").write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="250" viewBox="0 0 720 250" role="img" aria-label="{html.escape(title)}">
<defs><radialGradient id="g"><stop stop-color="{accent}" stop-opacity=".1"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>
<rect x=".5" y=".5" width="719" height="249" rx="16" fill="#091217" stroke="#24383b"/>
<ellipse cx="645" cy="30" rx="230" ry="180" fill="url(#g)"/>
<g font-family="Arial, sans-serif">
<text x="30" y="50" fill="{accent}" font-size="17">{html.escape(subtitle)}</text>
<text x="30" y="103" fill="#eaf4f0" font-size="35" font-weight="700">{html.escape(title)}</text>
<text x="30" y="149" fill="#a4bcb3" font-size="20">{html.escape(desc)}</text>
<text x="30" y="211" fill="#6c8a80" font-family="monospace" font-size="16">/{label}</text>
<path d="M654 194h23m-10-10 10 10-10 10" stroke="{accent}" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</g></svg>''', encoding="utf-8"
    )
print(f"GIF: {(ASSETS / 'profile-hero.gif').stat().st_size / 1024 / 1024:.2f} MiB; 96 frames / 8 seconds")
