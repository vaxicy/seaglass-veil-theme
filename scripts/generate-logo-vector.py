#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Seaglass Veil Theme — vector logo candidates (SVG rendered by headless Chromium).

Each candidate is inline SVG in its own 512px cell; Playwright screenshots every
cell with omit_background=True (true transparency) and PIL only composes the
contact sheets, the inline strip and the official logo/logo.png exported from
the SELECTED candidate.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "02"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


DEEP = hx(_C["frame"])                    # #2F6B66
TOOLBAR = hx(_C["toolbar"])               # #38736E
PALE = hx(_C["ntp_background"])           # #E7F5F4
PALE2 = hx(_C["button_background"])       # #D0EBE9
PALE3 = hx(_C["button_background_secondary"])  # #B9E2DE
GLASS = hx(_P["ntp_button_background"])   # #8BCFC8
INK = hx(_C["ntp_text"])                  # #1F4A47


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="sh1" x1="0.1" y1="0" x2="0.9" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.45" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
</defs>
<path d="M128 28 C170 36 202 66 210 112 C218 158 198 200 164 218 C140 231 112 230 88 216
         C54 198 36 158 44 112 C52 66 86 36 128 28 Z" fill="url(#sh1)"/>
<path d="M96 80 C120 62 158 64 178 86" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="8"
      fill="none" stroke-linecap="round"/>
<path d="M68 156 C86 190 118 208 150 202" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="7"
      fill="none" stroke-linecap="round"/>
""" % (PALE3, GLASS, TOOLBAR))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="wv2" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
</defs>
<path d="M30 170 C64 110 100 152 128 170 C156 188 192 186 226 150"
      stroke="url(#wv2)" stroke-width="25" fill="none" stroke-linecap="round"/>
<path d="M54 112 C82 78 106 104 128 120 C150 136 176 136 200 112"
      stroke="url(#wv2)" stroke-width="16" fill="none" stroke-linecap="round" stroke-opacity=".8"/>
""" % (DEEP, GLASS, TOOLBAR))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="dp3" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.6" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
</defs>
<path d="M128 34 C170 92 198 126 198 156 C198 196 167 222 128 222 C89 222 58 196 58 156
         C58 126 86 92 128 34 Z" fill="url(#dp3)"/>
<path d="M70 178 L188 118" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="15" stroke-linecap="round"/>
<path d="M84 208 L196 150" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="10" stroke-linecap="round"/>
""" % (PALE3, GLASS, TOOLBAR))

SVG_04 = svg_open("""
<circle cx="128" cy="128" r="86" fill="none" stroke="%s" stroke-width="13" stroke-opacity=".55"/>
<circle cx="128" cy="128" r="58" fill="none" stroke="%s" stroke-width="13" stroke-opacity=".85"/>
<circle cx="128" cy="128" r="30" fill="none" stroke="%s" stroke-width="13"/>
<circle cx="128" cy="128" r="9" fill="%s"/>
""" % (GLASS, GLASS, TOOLBAR, DEEP))

SVG_05 = svg_open("""
<circle cx="128" cy="128" r="102" fill="%s"/>
<circle cx="128" cy="128" r="102" fill="none" stroke="%s" stroke-opacity=".25" stroke-width="4"/>
<path d="M48 158 C78 116 100 142 128 158 C156 174 182 170 208 140"
      stroke="%s" stroke-width="21" fill="none" stroke-linecap="round"/>
<circle cx="128" cy="90" r="15" fill="%s"/>
""" % (DEEP, PALE, PALE2, GLASS))

SVG_06 = svg_open("""
<g transform="rotate(-16 128 128)">
  <rect x="44" y="88" width="98" height="98" rx="20" fill="%s" fill-opacity=".50"/>
  <rect x="80" y="72" width="98" height="98" rx="20" fill="%s" fill-opacity=".70"/>
  <rect x="116" y="88" width="98" height="98" rx="20" fill="%s" fill-opacity=".82"/>
</g>
""" % (GLASS, PALE3, TOOLBAR))

CANDIDATES = [
    ("01", "glass-shard", "Polished seaglass pebble with a light streak — most literal", SVG_01),
    ("02", "wave-curl", "Two wave crests in a teal gradient — fluid and calm", SVG_02),
    ("03", "drop-veil", "Water drop crossed by a veil band — soft and airy", SVG_03),
    ("04", "ripple-rings", "Concentric ripples — cleanest, spa-like", SVG_04),
    ("05", "glass-badge", "Wave in a deep-teal badge — boldest at 32px", SVG_05),
    ("06", "veil-panes", "Three translucent glass panes — most abstract", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            # bundled headless shell may be missing after a Playwright update
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 8 and bbox[1] > 8 and bbox[2] < PREVIEW - 8 and bbox[3] < PREVIEW - 8, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (240, 249, 248))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(31, 74, 71))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (240, 249, 248), (31, 74, 71), (110, 134, 132),
                  CAND_DIR / "contact-light.png", "Seaglass Veil — vector logo candidates (light)")
    contact_sheet(rendered, (26, 56, 54), (231, 245, 244), (150, 184, 181),
                  CAND_DIR / "contact-dark.png", "Seaglass Veil — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
