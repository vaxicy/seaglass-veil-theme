<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/seaglass-veil-theme/main/logo/logo.png" width="128" alt="Seaglass Veil Theme logo">
</p>

<h1 align="center">Seaglass Veil Theme</h1>

<p align="center">
  A calm aqua Chrome theme built on one seaglass value ladder — pale frosted teal over deep water.
</p>

Seaglass Veil pairs a deep teal frame with a slightly lighter teal toolbar, then opens onto a soft mist New Tab Page. Pale mint ink keeps every tab, bookmark and toolbar icon crisp against the deep chrome, deep teal ink keeps the pale page readable, and a single-row shortcut layout with a color-matched Google logo keeps the New Tab Page clean.

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/seaglass-veil-theme/main/store-assets/promo/1400x560.png" alt="Seaglass Veil Theme promo" width="700">
</p>

## Design Concept

Seaglass Veil uses one cool teal hue pulled into five values — mist, pale aqua, light aqua, aqua and seaglass — plus a deeper teal for the browser chrome. Every colour shares the same hue, so the whole browser reads as a single piece of frosted glass: calm, cooling and quiet. Contrast is carried by value rather than hue: the deepest teals take the frame and toolbar, the palest mist takes the page.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Mist | `#E7F5F4` | 231, 245, 244 | New Tab background / pale ink |
| Pale Aqua | `#D0EBE9` | 208, 235, 233 | New Tab header / buttons |
| Light Aqua | `#B9E2DE` | 185, 226, 222 | Secondary buttons |
| Aqua | `#A2D8D3` | 162, 216, 211 | Soft accent |
| Seaglass | `#8BCFC8` | 139, 207, 200 | New Tab buttons / logo accent |
| Deep Teal | `#2F6B66` | 47, 107, 102 | Frame / New Tab links |
| Toolbar Teal | `#38736E` | 56, 115, 110 | Toolbar |
| Deep Ink | `#1F4A47` | 31, 74, 71 | New Tab text |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Single-hue seaglass ladder: mist, aqua and deep teal in one family
- Deep teal chrome over a mist page — strong contrast, cool and calm
- Tab text, bookmark text and toolbar icons all share the same pale mint ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/seaglass-veil-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" alt="Seaglass Veil New Tab preview" width="640">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/seaglass-veil-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" alt="Seaglass Veil palette" width="640">
</p>

## Installation

### Load Unpacked (Development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable "Developer mode" in the top right.
4. Click "Load unpacked" and select this folder (`seaglass-veil-theme`).
5. The theme is now active.

### Web Store Packaging

```
chrome://extensions → Pack extension → select this folder → seaglass-veil-theme.zip
```

Upload the resulting `.zip` to the Chrome Web Store developer dashboard.

## Files

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build the contact sheets, and export `logo/logo.png` from the `SELECTED` candidate |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## License

Seaglass Veil Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
