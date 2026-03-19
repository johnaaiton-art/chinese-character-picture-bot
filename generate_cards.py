import json, math, os, zipfile
import cairosvg

T = {1:"#E24B4A", 2:"#3B6D11", 3:"#185FA5", 4:"#7F77DD", 0:"#888780"}
BG, WHITE, STROKE = "#F5F4F0", "#FFFFFF", "#D8D7CF"
PRI, SEC, TER = "#1A1A18", "#6B6A63", "#9B9A93"
FONT = "Noto Sans CJK SC"
CENTER_FILLS = {1:"#FCEBEB", 2:"#EAF3DE", 3:"#E6F1FB", 4:"#EEEDFE", 0:"#F0EFE8"}
CCW, CCH = 210, 136

def sat_positions(n, cx, cy):
    if n <= 5:   radius = 295
    elif n <= 7: radius = 316
    elif n <= 9: radius = 345
    else:        radius = 372
    angles = [270 + i*(360/n) for i in range(n)]
    return [(cx + radius*math.cos(math.radians(a)),
             cy + radius*math.sin(math.radians(a))) for a in angles]

def build_svg(card):
    root_char = card["char"]
    root_tone = card["tone"]
    root_color = T[root_tone]
    cfill = CENTER_FILLS[root_tone]
    sats = card["satellites"]
    n = len(sats)
    label = "collocation card" if card.get("type","collocation")=="collocation" else "phonetic / radical family"

    W = 1080
    H = 1120 if n > 8 else 1080
    CX = 540
    CY = 560 if n > 8 else 530

    if n <= 6:   CW, CH = 290, 120
    elif n <= 8: CW, CH = 272, 114
    else:        CW, CH = 250, 108

    L = []; A = L.append
    A(f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">')
    A(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    A(f'<text x="{W//2}" y="50" text-anchor="middle" font-family="{FONT}" font-size="21" fill="{TER}">{label}</text>')

    positions = sat_positions(n, CX, CY)

    for sx, sy in positions:
        A(f'<line x1="{CX}" y1="{CY}" x2="{sx:.1f}" y2="{sy:.1f}" '
          f'stroke="{STROKE}" stroke-width="1.8" stroke-dasharray="7 5"/>')

    x0, y0 = CX-CCW//2, CY-CCH//2
    A(f'<rect x="{x0}" y="{y0}" width="{CCW}" height="{CCH}" rx="20" '
      f'fill="{cfill}" stroke="{root_color}" stroke-width="2.5"/>')
    A(f'<text x="{CX}" y="{CY-10}" text-anchor="middle" dominant-baseline="central" '
      f'font-family="{FONT}" font-size="78" font-weight="900" fill="{root_color}">{root_char}</text>')
    A(f'<text x="{CX}" y="{y0+CCH-18}" text-anchor="middle" '
      f'font-family="{FONT}" font-size="19" fill="{root_color}">'
      f'{card["pinyin"]} · {card["meaning"]}</text>')

    for i, (sx, sy) in enumerate(positions):
        sat = sats[i]
        rx, ry = sx - CW//2, sy - CH//2
        A(f'<rect x="{rx:.1f}" y="{ry:.1f}" width="{CW}" height="{CH}" rx="12" '
          f'fill="{WHITE}" stroke="{STROKE}" stroke-width="1.2"/>')

        word = sat["word"]
        nc = len(word)
        char_size = 50 if nc <= 2 else (40 if nc == 3 else 33)
        char_w = char_size * 0.96
        cx_start = rx + 14 + char_w * 0.5

        for j, (ch, tone) in enumerate(word):
            col = T[int(tone)]
            cxj = cx_start + j * char_w
            A(f'<text x="{cxj:.1f}" y="{ry+CH//2}" text-anchor="middle" '
              f'dominant-baseline="central" font-family="{FONT}" '
              f'font-size="{char_size}" font-weight="bold" fill="{col}">{ch}</text>')

        total_char_w = char_w * nc
        tx_mid = (rx + 14 + total_char_w + 12 + rx + CW - 8) / 2
        fs_en = 17 if CW >= 272 else 15
        fs_py = 14; fs_bk = 13

        A(f'<text x="{tx_mid:.1f}" y="{ry+20}" text-anchor="middle" '
          f'font-family="{FONT}" font-size="{fs_py}" fill="{SEC}">{sat["pinyin"]}</text>')
        A(f'<text x="{tx_mid:.1f}" y="{ry+43}" text-anchor="middle" '
          f'font-family="{FONT}" font-size="{fs_en}" font-weight="bold" fill="{PRI}">{sat["english"]}</text>')
        A(f'<text x="{tx_mid:.1f}" y="{ry+66}" text-anchor="middle" '
          f'font-family="{FONT}" font-size="{fs_bk}" fill="{TER}">{sat["breakdown"]}</text>')

    A('</svg>')
    return "\n".join(L), W, H

def generate_all(json_dir="cards_json", out_dir="output_png"):
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(f for f in os.listdir(json_dir) if f.endswith(".json"))
    print(f"Generating {len(files)} cards...")
    generated = []
    for fname in files:
        with open(os.path.join(json_dir, fname)) as f:
            card = json.load(f)
        svg, W, H = build_svg(card)
        slug = fname.replace(".json","")
        svg_path = os.path.join(out_dir, slug+".svg")
        png_path = os.path.join(out_dir, slug+".png")
        with open(svg_path,"w") as f: f.write(svg)
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=W, output_height=H)
        print(f"  ✓ {slug}.png  ({W}x{H})")
        generated.append(png_path)
    zip_path = "vasilina_cards.zip"
    with zipfile.ZipFile(zip_path,"w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in generated:
            zf.write(p, os.path.basename(p))
        for f in os.listdir(json_dir):
            if f.endswith(".json"):
                zf.write(os.path.join(json_dir,f), f"json/{f}")
        zf.write("patch_generator.py", "generate_cards.py")
        if os.path.exists("write_json.py"):
            zf.write("write_json.py", "write_json.py")
    print(f"\n✓ Done! {len(generated)} cards → {zip_path}")

if __name__ == "__main__":
    generate_all()
