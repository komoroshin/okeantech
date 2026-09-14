"""Собирает markdown-деку в чёрно-белый PDF 16:9 через Chromium.
Запуск: python3 strategy/pdf/build_deck.py [deck-v7-text.md]
Обозначения в markdown: `§ РАЗДЕЛ` метка в углу; `### Заголовок` колонка; `cols: arrows` стрелки между колонками;
`Вывод:` строка внизу; `_курсив_` сноска; таблица с пустой первой строкой без шапки.
"""
import re, html, subprocess, pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "deck-v7-text.md")
STEM = SRC.stem.replace("-text", "")
OUT_HTML = ROOT / "pdf" / f"{STEM}.html"
OUT_PDF = ROOT / "pdf" / f"{STEM}-bw.pdf"

text = SRC.read_text(encoding="utf-8")
parts = re.split(r"\n## ", "\n" + text)
slides = []
for p in parts[1:]:
    title, _, body = p.partition("\n")
    if title.startswith("Что не вошло") or title.startswith("Что изменено"):
        continue
    slides.append((title.strip(), body.strip()))

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s

NOWRAP = {"Деньги", "Сумма", "Годовая выручка (ARR)", "Атрибут", "Направление", "Этап", "Бизнес", "Компания", "Модель"}

def render_table(rows):
    headerless = all(c == "" for c in rows[0])
    if headerless:
        rows = rows[1:]
    nowrap = set() if headerless else {j for j, h in enumerate(rows[0]) if h in NOWRAP}
    t = ['<table class="%s">' % ("labels" if headerless else "grid")]
    for r_i, r in enumerate(rows):
        tag = "td" if headerless or r_i else "th"
        cells = []
        for j, c in enumerate(r):
            attr = ' style="white-space:nowrap"' if j in nowrap else ""
            cells.append(f"<{tag}{attr}>{inline(c)}</{tag}>")
        t.append("<tr>" + "".join(cells) + "</tr>")
    t.append("</table>")
    return "".join(t)

def render_body(body):
    out, notes, cols, section = [], [], [], ""
    arrows = False
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln or ln == "---" or ln.startswith(">"):
            i += 1; continue
        if ln.startswith("§ "):
            section = ln[2:].strip(); i += 1; continue
        if ln.strip() == "cols: arrows":
            arrows = True; i += 1; continue
        if ln.startswith("### "):
            head = ln[4:].strip(); i += 1; buf = []
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("Вывод:"):
                if lines[i].strip() and lines[i].strip() != "---":
                    buf.append(f"<p>{inline(lines[i].strip())}</p>")
                i += 1
            cols.append(f'<div class="col"><h2>{inline(head)}</h2>{"".join(buf)}</div>')
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"-+", c) for c in cells):
                    rows.append(cells)
                i += 1
            out.append(render_table(rows)); continue
        if ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if ln.startswith("Вывод:"):
            t = ln[len("Вывод:"):].strip(); t = t[:1].upper() + t[1:]
            out.append(f'<p class="takeaway">{inline(t)}</p>'); i += 1; continue
        if re.fullmatch(r"_.+_", ln):
            notes.append(f'<p class="note">{inline(ln[1:-1])}</p>'); i += 1; continue
        if re.fullmatch(r"\*\*.+\*\*", ln):
            out.append(f'<p class="lead">{inline(ln[2:-2])}</p>'); i += 1; continue
        out.append(f"<p>{inline(ln)}</p>"); i += 1
    if cols:
        sep = '<div class="arrow">→</div>' if arrows else ""
        out.insert(0, '<div class="cols">' + sep.join(cols) + "</div>")
    return "\n".join(out), "".join(notes), section

CSS = """
@page { size: 338.67mm 190.5mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #000;
  font-family: "Liberation Sans", Arial, Helvetica, sans-serif; }
.slide { width: 338.67mm; height: 190.5mm; padding: 15mm 22mm 24mm 22mm; page-break-after: always; overflow: hidden;
  display: flex; flex-direction: column; position: relative; }
.slide:last-child { page-break-after: auto; }
.num { position: absolute; right: 22mm; bottom: 9mm; font-size: 10pt; }
.brand { position: absolute; left: 22mm; bottom: 9mm; font-size: 10pt; letter-spacing: .12em; }
.section { position: absolute; right: 22mm; top: 9mm; font-size: 10pt; letter-spacing: .12em; }
h1 { font-size: 36pt; font-weight: 700; margin: 0 0 9mm 0; line-height: 1.15; }
.body { flex: 1; display: flex; flex-direction: column; font-size: 19pt; line-height: 1.35; }
.body p { margin: 0 0 4.5mm 0; }
.body p.lead { font-weight: 700; font-size: 21pt; margin-bottom: 6mm; }
.body ul { margin: 0 0 4mm 0; padding-left: 7mm; }
.body li { margin: 0 0 3.5mm 0; }
.cols { display: flex; gap: 12mm; margin-top: 4mm; }
.col { flex: 1; }
.arrow { flex: 0 0 auto; align-self: flex-start; margin-top: 14mm; font-size: 40pt; line-height: 1; font-weight: 700; }
.col h2 { font-size: 22pt; margin: 0 0 6mm 0; }
.col p { font-size: 19pt; }
table { border-collapse: collapse; width: 100%; margin: 0 0 5mm 0; font-size: 17pt; }
th, td { border: 0.4pt solid #000; padding: 2mm 3.5mm; text-align: left; vertical-align: top; }
th { font-weight: 700; background: #000; color: #fff; }
table.labels td { border: 0; border-bottom: 0.4pt solid #000; padding: 2.5mm 4mm 2.5mm 0; }
table.labels td:first-child { width: 28%; white-space: normal; }
.takeaway { margin-top: auto; padding-top: 5mm; border-top: 1.2pt solid #000; font-size: 19pt; font-weight: 700; }
.note { font-size: 11pt; margin: 2mm 0 0 0; color: #000; }
.title .body { justify-content: center; }
.title .wif { font-size: 96pt; font-weight: 700; letter-spacing: .04em; line-height: 1; margin: 0 0 8mm 0; }
.title .desc { font-size: 26pt; margin: 0 0 12mm 0; }
.title .sub { font-size: 16pt; margin: 0 0 3mm 0; }
"""

pages = []
for idx, (title, body) in enumerate(slides, 1):
    m = re.match(r"(\d+)\.\s+(.*)", title)
    if m and m.group(1) == "1":
        lines = [l for l in body.split("\n") if l.strip() and l != "---"]
        name = re.sub(r"\*\*", "", lines[0])
        subs = "".join(f'<div class="sub">{inline(l)}</div>' for l in lines[2:])
        pages.append(f'''<section class="slide title"><div class="body">
<div class="wif">{inline(name)}</div><div class="desc">{inline(lines[1])}</div>{subs}
</div></section>''')
        continue
    heading = m.group(2) if m else title
    content, notes, section = render_body(body)
    pages.append(f'''<section class="slide"><div class="section">{inline(section)}</div><h1>{inline(heading)}</h1>
<div class="body">{content}{notes}</div>
<div class="brand">WIF</div><div class="num">{idx}</div></section>''')

OUT_HTML.write_text(f"<!doctype html><html lang='ru'><head><meta charset='utf-8'><title>{STEM}</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>", encoding="utf-8")

chrome = shutil.which("chromium") or "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri()], check=True, capture_output=True)
print("ok", OUT_PDF, OUT_PDF.stat().st_size)

# Проверка переполнения: текст ниже линии подвала (кроме самого подвала) означает, что слайд не влез.
try:
    import pymupdf
    doc = pymupdf.open(str(OUT_PDF))
    bad = []
    for i, page in enumerate(doc, 1):
        h = page.rect.height
        for b in page.get_text("blocks"):
            x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4].strip()
            if y1 > h - 32 and txt.replace("\n", " ").split() not in (["WIF"], [str(i)], ["WIF", str(i)]):
                bad.append((i, txt[:60]))
    if bad:
        print("ПЕРЕПОЛНЕНИЕ на слайдах:", sorted(set(n for n, _ in bad)))
        for n, t in bad: print(f"  {n}: {t}")
    else:
        print("переполнений нет")
except Exception as e:
    print("проверка переполнения не выполнена:", e)
