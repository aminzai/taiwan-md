#!/usr/bin/env python3
"""Taiwan.md 品牌 logo 生成器 — navbar lockup 版
來源規格 = taiwan-md/src/components/BrandMark.astro（SSOT）:
  Taiwan  → Noto Serif TC 700
  .md     → Noto Sans TC 600, accent #00d4aa
  icon    → favicon.png（256px 地形島嶼）, 高度 ≈ 1.08 × font-size, gap 0.4rem
色票：dark-bg 文字 #FFFFFF / light-bg 文字 #1a1a2e / accent #00d4aa
"""
import base64, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

SP = pathlib.Path(__file__).parent
OUT = SP / "brand-out"; OUT.mkdir(exist_ok=True)
ICON_PNG = pathlib.Path.home() / "Projects/taiwan-md/public/favicon.png"

ACCENT_DARKBG = "#4fd1b0"  # 站上深色態 --green-accent
ACCENT_LIGHTBG = "#007864" # 站上淺色態 --green-mid
DARKTEXT = "#1a1a2e"; WHITE = "#FFFFFF"

def load(path, wght):
    f = TTFont(str(path))
    instantiateVariableFont(f, {"wght": wght}, inplace=True)
    return f

serif = load(SP/"fonts/NotoSerifTC.ttf", 700)
sans  = load(SP/"fonts/NotoSansTC.ttf", 600)

def text_paths(font, text, x0, fs):
    """回傳 [(path_d, advance_x)] 與結束 x。座標：y 向下、baseline=0，字級 fs px。"""
    upm = font["head"].unitsPerEm
    scale = fs / upm
    cmap = font.getBestCmap(); glyphset = font.getGlyphSet()
    hmtx = font["hmtx"]
    out = []; x = x0
    for ch in text:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(glyphset)
        # y 翻轉 + 縮放 + 平移
        tpen = TransformPen(pen, Transform(scale, 0, 0, -scale, x, 0))
        glyphset[gname].draw(tpen)
        d = pen.getCommands()
        if d: out.append(d)
        x += hmtx[gname][0] * scale
    return out, x

def metrics(font, fs):
    upm = font["head"].unitsPerEm
    os2 = font["OS/2"]
    return {"capH": os2.sCapHeight * fs/upm, "asc": os2.sTypoAscender * fs/upm,
            "desc": abs(os2.sTypoDescender) * fs/upm}

FS = 100.0                      # wordmark 字級（px）
GAP_WORD = 0.4 * FS             # BrandMark gap: 0.4rem
ICON = 1.08 * FS                # BrandMark icon: 1.08 × font-size
PAD = 0.35 * FS                 # 四周留白（clear space 內建最小值）

m = metrics(serif, FS)
capH = m["capH"]

# --- 文字外框 ---
taiwan_paths, x_end = text_paths(serif, "Taiwan", 0, FS)
md_paths, x_md_end = text_paths(sans, ".md", x_end + 0.04*FS, FS)

# --- 版面（baseline y=0；icon 垂直置中對齊 cap-height 區）---
icon_x = 0.0
text_x0 = ICON + GAP_WORD
icon_top = -capH/2 - ICON/2     # icon 中心對齊大寫字高中心
W = text_x0 + x_md_end + 0.0
top = min(icon_top, -m["asc"])
bot = max(icon_top + ICON, m["desc"])
H = bot - top

icon_b64 = base64.b64encode(ICON_PNG.read_bytes()).decode()

def svg(variant, text_fill, accent, with_icon=True, bg=None):
    tx = text_x0 if with_icon else 0.0
    w = (W if with_icon else x_md_end) + 2*PAD
    h = H + 2*PAD
    ox = PAD + (0 if with_icon else 0)
    oy = PAD - top
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.1f}" height="{h:.1f}" role="img" aria-label="Taiwan.md">']
    if bg: parts.append(f'<rect width="{w:.1f}" height="{h:.1f}" fill="{bg}"/>')
    parts.append(f'<g transform="translate({ox:.1f},{oy:.1f})">')
    if with_icon:
        parts.append(f'<image x="{icon_x:.1f}" y="{icon_top:.1f}" width="{ICON:.1f}" height="{ICON:.1f}" '
                     f'href="data:image/png;base64,{icon_b64}" preserveAspectRatio="xMidYMid meet"/>')
    parts.append(f'<g transform="translate({tx:.1f},0)">')
    for d in taiwan_paths: parts.append(f'<path d="{d}" fill="{text_fill}"/>')
    for d in md_paths:     parts.append(f'<path d="{d}" fill="{accent}"/>')
    parts.append('</g></g></svg>')
    return "\n".join(parts)

files = {
    "taiwanmd-logo-horizontal-dark.svg":   svg("dark",  WHITE,    ACCENT_DARKBG,  True),            # 深底用（透明底、白字、薄荷綠）
    "taiwanmd-logo-horizontal-light.svg":  svg("light", DARKTEXT, ACCENT_LIGHTBG, True),            # 淺底用（透明底、深字、深綠）
    "taiwanmd-logo-horizontal-darkbg.svg": svg("darkbg", WHITE,   ACCENT_DARKBG,  True, "#0f1a14"), # 自帶深綠底（navbar 情境）
    "taiwanmd-wordmark-dark.svg":  svg("wm-d", WHITE,    ACCENT_DARKBG,  False),
    "taiwanmd-wordmark-light.svg": svg("wm-l", DARKTEXT, ACCENT_LIGHTBG, False),
}
for name, content in files.items():
    (OUT/name).write_text(content)
    print("✅", name, f"{len(content)/1024:.0f} KB")
print(f"版面：FS={FS} capH={capH:.1f} icon={ICON:.1f} W={W:.1f} H={H:.1f}")
