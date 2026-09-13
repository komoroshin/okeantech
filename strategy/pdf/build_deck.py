"""Собирает deck-v6-text.md в чёрно-белый PDF 16:9 через Chromium.
Запуск: python3 strategy/pdf/build_deck.py
"""
import re, html, subprocess, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "deck-v6-text.md"
OUT_HTML = ROOT / "pdf" / "deck-v6.html"
OUT_PDF = ROOT / "pdf" / "deck-v6-bw.pdf"

text = SRC.read_text(encoding="utf-8")
parts = re.split(r"\n## ", "\n" + text)
slides = []
for p in parts[1:]:
    title, _, body = p.partition("\n")
    if title.startswith("Что не вошло"):
        continue
    slides.append((title.strip(), body.strip()))

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s

def render_body(body):
    out, lines = [], body.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln or ln == "---":
            i += 1; continue
        if ln.startswith(">"):  # внутренняя заметка, в PDF не идёт
            i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"-+", c) for c in cells):
                    rows.append(cells)
                i += 1
            t = ["<table>"]
            nowrap = {j for j, h in enumerate(rows[0]) if h in ("Деньги", "Годовая выручка (ARR)", "Атрибут", "Направление", "Этап")}
            for r_i, r in enumerate(rows):
                tag = "th" if r_i == 0 else "td"
                cells = []
                for j, c in enumerate(r):
                    attr = ' style="white-space:nowrap"' if j in nowrap else ''
                    cells.append(f"<{tag}{attr}>{inline(c)}</{tag}>")
                t.append("<tr>" + "".join(cells) + "</tr>")
            t.append("</table>")
            out.append("".join(t)); continue
        if ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if ln.startswith("Вывод:"):
            t = ln[len("Вывод:"):].strip(); t = t[:1].upper() + t[1:]
            out.append(f'<p class="takeaway">{inline(t)}</p>'); i += 1; continue
        out.append(f"<p>{inline(ln)}</p>"); i += 1
    return "\n".join(out)

CSS = """
@page { size: 338.67mm 190.5mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #000;
  font-family: "Liberation Sans", Arial, Helvetica, sans-serif; }
.slide { width: 338.67mm; height: 190.5mm; padding: 16mm 22mm 22mm 22mm; page-break-after: always;
  display: flex; flex-direction: column; position: relative; }
.slide:last-child { page-break-after: auto; }
.num { position: absolute; right: 22mm; bottom: 9mm; font-size: 10pt; color: #000; }
.brand { position: absolute; left: 22mm; bottom: 9mm; font-size: 10pt; letter-spacing: .12em; }
h1 { font-size: 38pt; font-weight: 700; margin: 0 0 9mm 0; line-height: 1.15; }
.body { flex: 1; display: flex; flex-direction: column; font-size: 20pt; line-height: 1.35; }
.body p { margin: 0 0 4mm 0; }
.body ul { margin: 0 0 4mm 0; padding-left: 7mm; }
.body li { margin: 0 0 3.5mm 0; }
table { border-collapse: collapse; width: 100%; margin: 0 0 5mm 0; font-size: 17pt; }
th, td { border: 0.4pt solid #000; padding: 2mm 3.5mm; text-align: left; vertical-align: top; }
th { font-weight: 700; background: #000; color: #fff; }
.takeaway { margin-top: auto; padding-top: 5mm; border-top: 1.2pt solid #000; font-size: 20pt; font-weight: 700; }
.title .body { display: flex; flex-direction: column; justify-content: center; }
.title .wif { font-size: 96pt; font-weight: 700; letter-spacing: .04em; line-height: 1; margin: 0 0 8mm 0; }
.title .desc { font-size: 26pt; margin: 0 0 12mm 0; }
.title .sub { font-size: 16pt; margin: 0 0 3mm 0; }
.title .sub.small { font-size: 13pt; }
"""

pages = []
for idx, (title, body) in enumerate(slides, 1):
    m = re.match(r"(\d+)\.\s+(.*)", title)
    if m and m.group(1) == "1":
        # титул собираем отдельно
        lines = [l for l in body.split("\n") if l.strip()]
        name = re.sub(r"\*\*", "", lines[0])
        desc, trio, ask, org = lines[1], lines[2], lines[3], lines[4]
        pages.append(f'''<section class="slide title"><div class="body">
<div class="wif">{inline(name)}</div>
<div class="desc">{inline(desc)}</div>
<div class="sub">{inline(trio)}</div>
<div class="sub">{inline(ask)}</div>
<div class="sub small">{inline(org)}</div>
</div></section>''')
        continue
    heading = m.group(2) if m else title
    pages.append(f'''<section class="slide"><h1>{inline(heading)}</h1>
<div class="body">{render_body(body)}</div>
<div class="brand">WIF</div><div class="num">{idx}</div></section>''')

OUT_HTML.write_text(f"<!doctype html><html lang='ru'><head><meta charset='utf-8'><title>WIF deck v6</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>", encoding="utf-8")

chrome = shutil.which("chromium") or "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri()], check=True, capture_output=True)
print("ok", OUT_PDF, OUT_PDF.stat().st_size)
