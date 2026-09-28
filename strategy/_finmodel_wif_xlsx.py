# -*- coding: utf-8 -*-
"""Собирает finmodel-wif.xlsx в формате референса: главный лист — бюджет М1…М36 с итогом.

Листы:
  Бюджет   — выручка, штат по ролям, статьи расходов, денежный поток, накопленный
             поток («яма»), деньги на счету, распределение прибыли
  Штат     — число людей по ролям и месяцам, оклады
  Выручка  — поток клиентов, база с оттоком, платежи, ARR, оценка
  Рычаги   — общие допущения
  Годы     — бюджет по годам
  Проверки — итоги и сверка со стратегией

Синие ячейки — план, правится руками. Чёрные — формулы. Зелёные — ссылки на
другой лист. Жёлтая заливка — допущения, которых нет в стратегии.
Запуск: python3 _finmodel_wif_xlsx.py; затем пересчёт (README-finmodel.md).
"""

from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import _finmodel_wif as M

HERE = Path(__file__).parent
MON = M.MONTHS
COLS = [get_column_letter(3 + i) for i in range(MON)]     # C … AL — М1 … М36
TOTAL = get_column_letter(3 + MON)                           # AM — Итого
RATE = get_column_letter(4 + MON)                            # AN — ставка строки
FIRST, LAST = COLS[0], COLS[-1]
YEARS = [(COLS[12 * y], COLS[12 * y + 11]) for y in range(MON // 12)]

F = "Arial"
BLUE, BLACK, GREEN = Font(name=F, size=10, color="0000FF"), Font(name=F, size=10), Font(name=F, size=10, color="008000")
BOLD, BOLDW = Font(name=F, size=10, bold=True), Font(name=F, size=10, bold=True, color="FFFFFF")
TITLE, NOTE = Font(name=F, size=13, bold=True), Font(name=F, size=9, color="666666", italic=True)
YELLOW, DARK = PatternFill("solid", fgColor="FFFF00"), PatternFill("solid", fgColor="333333")
GREY, LIGHT = PatternFill("solid", fgColor="D9D9D9"), PatternFill("solid", fgColor="F2F2F2")
TOPLINE = Border(top=Side(style="thin", color="808080"))

CUR = '#,##0;(#,##0);-'
CUR2 = '$#,##0;($#,##0);-'
NUM = '#,##0;(#,##0);-'
PCT = '0%'
PCT1 = '0.0%'
MULT = '0.0"x"'


def put(ws, ref, value, font=BLACK, fmt=None, fill=None, align=None):
    c = ws[ref]
    c.value = value
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if align:
        c.alignment = Alignment(horizontal=align)
    return c


def month_header(ws, row, first_label="Статья", with_total=True, with_rate=False):
    put(ws, f"A{row}", "", BOLDW, fill=DARK)
    put(ws, f"B{row}", first_label, BOLDW, fill=DARK)
    for i, c in enumerate(COLS):
        put(ws, f"{c}{row}", f"М{i + 1}", BOLDW, fill=DARK, align="center")
    if with_total:
        put(ws, f"{TOTAL}{row}", "Итого", BOLDW, fill=DARK, align="center")
    if with_rate:
        put(ws, f"{RATE}{row}", "Ставка", BOLDW, fill=DARK, align="center")
    for y, (c0, _) in enumerate(YEARS):
        put(ws, f"{c0}{row - 1}", f"Год {y + 1}", BOLD)


def widths(ws, a=4, b=46, month=10):
    ws.column_dimensions["A"].width = a
    ws.column_dimensions["B"].width = b
    for c in COLS:
        ws.column_dimensions[c].width = month
    ws.column_dimensions[TOTAL].width = 13
    ws.column_dimensions[RATE].width = 9


class Sheet:
    """Строки листа по порядку; запоминает номер строки по ключу."""

    def __init__(self, ws, start):
        self.ws, self.r, self.rows = ws, start, {}

    def section(self, title, fill=GREY):
        for col in ["A", "B"] + COLS + [TOTAL]:
            put(self.ws, f"{col}{self.r}", title if col == "B" else "", BOLD, fill=fill)
        self.r += 1

    def line(self, key, label, values=None, f=None, fmt=CUR, bold=False, total="sum",
             rate=None, rate_fmt=PCT, rate_guess=True, indent=1, font=None):
        ws, row = self.ws, self.r
        put(ws, f"B{row}", ("   " * indent) + label, BOLD if bold else BLACK)
        for i, c in enumerate(COLS):
            if f is not None:
                put(ws, f"{c}{row}", f(i, c, row), font or BLACK, fmt, align="right")
            else:
                v = values[i + 1]
                v = int(v) if float(v).is_integer() else round(v, 2)
                put(ws, f"{c}{row}", v if v else None, BLUE, fmt, align="right")
        if total == "sum":
            put(ws, f"{TOTAL}{row}", f"=SUM({FIRST}{row}:{LAST}{row})", BOLD if bold else BLACK, fmt, align="right")
        elif total == "last":
            put(ws, f"{TOTAL}{row}", f"={LAST}{row}", BOLD if bold else BLACK, fmt, align="right")
        if rate is not None:
            put(ws, f"{RATE}{row}", rate, BLUE, rate_fmt, YELLOW if rate_guess else None, "right")
        if bold:
            for col in ["B"] + COLS + [TOTAL]:
                ws[f"{col}{row}"].border = TOPLINE
        if key:
            self.rows[key] = row
        self.r += 1
        return row


# ─────────────────────────────────────────────────────────────────────
# Рычаги
# ─────────────────────────────────────────────────────────────────────

LEVERS = [
    ("ВЫРУЧКА", None, None, None, False),
    ("labor_churn", "Труд: отток компаний в месяц", PCT1, "target-state-18m.md", False),
    ("pilot_price", "Труд: цена пилота, $", CUR2, "90-day-plan.md: $3–5 тыс.", False),
    ("ident_price", "Личность: цена подписки, $/мес", CUR2, "target-state-18m.md", False),
    ("ident_churn", "Личность: отток подписчиков в месяц", PCT1, "target-state-18m.md", False),
    ("ident_conversion", "Личность: конверсия визита в подписку", PCT1, "target-state-18m.md", False),
    ("brand_check", "Личность: чек сделки с брендом, $", CUR2, "target-state-18m.md", False),
    ("cap_churn", "Капитал: отток компаний в месяц", PCT1, "допущение, в стратегии нет", True),
    ("ШТАТ", None, None, None, False),
    ("salary_scale", "Множитель ко всем окладам", MULT, "1 — оклады референса; 3 — уровень бюджета этапов деки", True),
    ("hire_cost_lead", "Найм руководителя направления, $", CUR2, "допущение", True),
    ("hire_cost", "Найм остальных, $ на человека", CUR2, "допущение", True),
    ("ДЕНЬГИ", None, None, None, False),
    ("raise_total", "Раунд, $", CUR2, "дека v10", False),
    ("ОЦЕНКА — МУЛЬТИПЛИКАТОРЫ", None, None, None, False),
    ("mult_labor", "Труд, × ARR", MULT, "допущение", True),
    ("mult_cap", "Капитал, × ARR", MULT, "допущение", True),
    ("mult_subs", "Подписка, × ARR", MULT, "допущение", True),
    ("mult_brand", "Бренды, × выручки за 12 месяцев", MULT, "допущение", True),
]


def build_levers(ws):
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 56
    put(ws, "A1", "Рычаги", TITLE)
    put(ws, "A2", "Общие допущения. Ставки по отдельным статьям — в колонке «Ставка» на листе «Бюджет». "
                  "Жёлтым — допущения, которых нет в стратегии.", NOTE)
    for col, name in (("A", "Рычаг"), ("B", "Значение"), ("C", "Откуда")):
        put(ws, f"{col}4", name, BOLDW, fill=DARK)
    ref, r = {}, 5
    for key, label, fmt, src, guess in LEVERS:
        if label is None:
            for col in "ABC":
                put(ws, f"{col}{r}", key if col == "A" else "", BOLD, fill=LIGHT)
        else:
            put(ws, f"A{r}", label)
            put(ws, f"B{r}", M.BASE[key], BLUE, fmt, YELLOW if guess else None, "right")
            put(ws, f"C{r}", src, NOTE)
            ref[key] = f"Рычаги!$B${r}"
        r += 1
    return ref


# ─────────────────────────────────────────────────────────────────────
# Штат
# ─────────────────────────────────────────────────────────────────────

def build_staff(ws, run):
    ws.freeze_panes = "C5"
    widths(ws, a=12, b=40, month=6)
    put(ws, "A1", "Штат по ролям", TITLE)
    put(ws, "A2", "Число людей по месяцам — план найма, правится руками. Оклад — полная месячная стоимость "
                  "человека до налогов на ФОТ. «Рук.» — руководитель направления: найм дороже.", NOTE)
    month_header(ws, 4, "Роль", with_total=False)
    put(ws, "A4", "Оклад, $", BOLDW, fill=DARK)
    put(ws, f"{TOTAL}4", "Рук.", BOLDW, fill=DARK, align="center")
    rows, r, group = [], 5, None
    for ro in run["roles"]:
        if ro["group"] != group:
            group = ro["group"]
            for col in ["A", "B"] + COLS + [TOTAL]:
                put(ws, f"{col}{r}", group if col == "B" else "", BOLD, fill=LIGHT)
            r += 1
        put(ws, f"A{r}", ro["salary"], BLUE, CUR, align="right")
        put(ws, f"B{r}", ro["role"])
        for i, c in enumerate(COLS):
            v = int(ro["count"][i + 1])
            put(ws, f"{c}{r}", v if v else None, BLUE, NUM, align="center")
        put(ws, f"{TOTAL}{r}", "да" if ro["lead"] else None, BLACK, align="center")
        rows.append((ro, r))
        r += 1
    first_row, last_row = rows[0][1] - 1, rows[-1][1]
    put(ws, f"B{r}", "Всего людей", BOLD)
    for c in COLS:
        put(ws, f"{c}{r}", f"=SUM({c}{first_row}:{c}{last_row})", BOLD, NUM, align="center")
    total_row = r
    r += 1
    # новых людей за месяц: разница с прошлым месяцем по каждой роли, только прирост
    for label, flag in (("Нанято руководителей", '="да"'), ("Нанято остальных", '<>"да"')):
        put(ws, f"B{r}", label)
        for i, c in enumerate(COLS):
            rng_now = f"{c}{first_row}:{c}{last_row}"
            lead = f"${TOTAL}${first_row}:${TOTAL}${last_row}"
            cond = f'({lead}="да")' if flag == '="да"' else f'({lead}<>"да")'
            if i == 0:
                fml = f"=SUMPRODUCT(({rng_now})*{cond})"
            else:
                p = COLS[i - 1]
                rng_prev = f"{p}{first_row}:{p}{last_row}"
                fml = f"=SUMPRODUCT((({rng_now})-({rng_prev})>0)*(({rng_now})-({rng_prev}))*{cond})"
            put(ws, f"{c}{r}", fml, BLACK, NUM, align="center")
        if flag == '="да"':
            hires_lead = r
        else:
            hires_other = r
        r += 1
    return {"roles": rows, "total": total_row, "hires_lead": hires_lead, "hires_other": hires_other}


# ─────────────────────────────────────────────────────────────────────
# Выручка
# ─────────────────────────────────────────────────────────────────────

def build_revenue(ws, run, ref):
    ws.freeze_panes = "C5"
    widths(ws, b=40, month=10)
    put(ws, "A1", "Выручка: поток клиентов и база", TITLE)
    put(ws, "A2", "Синие строки — план: новые клиенты, визиты, сделки, платежи. База = прошлый месяц − "
                  "ROUND(прошлый × отток) + новые; все штуки целые.", NOTE)
    month_header(ws, 4, "Показатель")
    s = Sheet(ws, 5)
    prev = lambda i: COLS[i - 1]

    def stock(adds_key, churn):
        return lambda i, c, row: (f"={prev(i)}{row}-ROUND({prev(i)}{row}*{churn},0)+{c}{s.rows[adds_key]}"
                                  if i else f"={c}{s.rows[adds_key]}")

    R = lambda k: s.rows[k]
    s.section("ТРУД · ИИ-СОТРУДНИКИ")
    s.line("labor_adds", "Новых компаний", run["labor_adds"], fmt=NUM)
    s.line("labor_base", "Компаний", f=stock("labor_adds", ref["labor_churn"]), fmt=NUM, total="last")
    s.line("labor_arpa", "Платёж компании, $/мес", run["labor_arpa"], total=None)
    s.line("pilots", "Пилотов", run["pilots"], fmt=NUM)
    s.line("labor_rec", "Выручка: подписка компаний", f=lambda i, c, row: f"={c}{R('labor_base')}*{c}{R('labor_arpa')}", bold=True)
    s.line("pilot_rev", "Выручка: пилоты", f=lambda i, c, row: f"={c}{R('pilots')}*{ref['pilot_price']}", bold=True)
    s.section("ЛИЧНОСТЬ · ПЕРСОНАЖИ")
    s.line("visits", "Визитов на платное предложение", run["visits"], fmt=NUM)
    s.line("subs_adds", "Новых подписчиков", f=lambda i, c, row: f"=ROUND({c}{R('visits')}*{ref['ident_conversion']},0)", fmt=NUM)
    s.line("subs", "Подписчиков", f=stock("subs_adds", ref["ident_churn"]), fmt=NUM, total="last")
    s.line("subs_rev", "Выручка: подписка", f=lambda i, c, row: f"={c}{R('subs')}*{ref['ident_price']}", bold=True)
    s.line("brand_deals", "Сделок с брендами", run["brand_deals"], fmt=NUM)
    s.line("brand_rev", "Выручка: бренды", f=lambda i, c, row: f"={c}{R('brand_deals')}*{ref['brand_check']}", bold=True)
    s.section("КАПИТАЛ · УЧЁТ РАСХОДОВ НА ИИ")
    s.line("cap_adds", "Новых компаний", run["cap_adds"], fmt=NUM)
    s.line("cap_base", "Компаний", f=stock("cap_adds", ref["cap_churn"]), fmt=NUM, total="last")
    s.line("cap_arpa", "Платёж компании, $/мес", run["cap_arpa"], total=None)
    s.line("cap_rev", "Выручка: Капитал", f=lambda i, c, row: f"={c}{R('cap_base')}*{c}{R('cap_arpa')}", bold=True)
    s.section("ARR И ОЦЕНКА")
    s.line("arr", "ARR группы (без брендов и пилотов)",
           f=lambda i, c, row: f"=({c}{R('labor_rec')}+{c}{R('subs_rev')}+{c}{R('cap_rev')})*12", total="last")
    s.line("valuation", "Оценка по мультипликаторам", total="last", bold=True,
           f=lambda i, c, row: (f"={c}{R('labor_rec')}*12*{ref['mult_labor']}+{c}{R('cap_rev')}*12*{ref['mult_cap']}"
                                f"+{c}{R('subs_rev')}*12*{ref['mult_subs']}"
                                f"+SUM({COLS[max(0, i - 11)]}{R('brand_rev')}:{c}{R('brand_rev')})*{ref['mult_brand']}"))
    return s.rows


# ─────────────────────────────────────────────────────────────────────
# Бюджет — главный лист
# ─────────────────────────────────────────────────────────────────────

def build_budget(ws, run, ref, staff, rev):
    ws.freeze_panes = "C5"
    widths(ws, b=52, month=10)
    put(ws, "A1", "Бюджет WIF · 36 месяцев · $", TITLE)
    put(ws, "A2", "Синие — план, правится руками; колонка «Ставка» — параметр строки. Штат — на листе «Штат», "
                  "поток клиентов — на листе «Выручка».", NOTE)
    month_header(ws, 4, "Статья", with_rate=True)
    s = Sheet(ws, 5)
    V = lambda key, c: f"Выручка!{c}{rev[key]}"

    # ── выручка ─────────────────────────────────────────────────────
    s.section("ВЫРУЧКА")
    rev_lines = [("labor_rec", "Труд: подписка компаний"), ("pilot_rev", "Труд: пилоты"),
                 ("subs_rev", "Личность: подписка"), ("brand_rev", "Личность: бренды"), ("cap_rev", "Капитал")]
    first_rev = s.r
    for key, label in rev_lines:
        s.line(key, label, f=lambda i, c, row, key=key: f"={V(key, c)}", font=GREEN)
    s.line("revenue", "Выручка всего", f=lambda i, c, row: f"=SUM({c}{first_rev}:{c}{row - 1})", bold=True, indent=0)

    # ── расходы ─────────────────────────────────────────────────────
    s.section("РАСХОДЫ")
    sections = []

    def block(title, items):
        s.section(title, fill=LIGHT)
        first = s.r
        for it in items:
            it()
        key = "sec_" + title
        s.line(key, f"Итого: {title.lower()}", f=lambda i, c, row: f"=SUM({c}{first}:{c}{row - 1})", bold=True)
        sections.append(key)

    def item_row(it):
        kind, params, name = it["kind"], it["params"], it["name"]
        if kind in ("monthly", "oneoff"):
            return lambda: s.line(None, name, it["vals"])
        if kind == "pct":
            base, share = params
            return lambda: s.line(None, name, rate=share,
                                  f=lambda i, c, row: f"={V(base, c)}*${RATE}{row}")
        driver, rate = params
        rate_v = M.BASE[rate] if isinstance(rate, str) else rate
        if driver == "fte":
            return lambda: s.line(None, name, rate=rate_v, rate_fmt=CUR2,
                                  f=lambda i, c, row: f"=Штат!{c}{staff['total']}*${RATE}{row}")
        if driver == "labor_new_acv":
            return lambda: s.line(None, name, rate=rate_v,
                                  f=lambda i, c, row: f"={V('labor_adds', c)}*{V('labor_arpa', c)}*12*${RATE}{row}")
        fmt = '$0.00' if rate_v < 1 else CUR2
        return lambda: s.line(None, name, rate=rate_v, rate_fmt=fmt,
                              f=lambda i, c, row: f"={V(driver, c)}*${RATE}{row}")

    by_sec = {}
    for it in run["items"]:
        by_sec.setdefault(it["section"], []).append(item_row(it))

    block("Себестоимость", by_sec["Себестоимость"])

    # штат: роль за ролью, как в референсе
    staff_rows = []
    for ro, srow in staff["roles"]:
        staff_rows.append(lambda ro=ro, srow=srow: s.line(
            None, ro["role"], f=lambda i, c, row: f"=Штат!{c}{srow}*Штат!$A${srow}*{ref['salary_scale']}"))
    block("ФОТ", staff_rows)
    s.line("payroll_tax", "Налоги и взносы на ФОТ", rate=M.BASE["payroll_tax"],
           f=lambda i, c, row: f"={c}{s.rows['sec_ФОТ']}*${RATE}{row}")
    s.line("recruiting", "Найм",
           f=lambda i, c, row: (f"=Штат!{c}{staff['hires_lead']}*{ref['hire_cost_lead']}"
                                f"+Штат!{c}{staff['hires_other']}*{ref['hire_cost']}"))
    sections += ["payroll_tax", "recruiting"]

    for sec in ("Софт и инфраструктура", "Юрлица и финансы", "Маркетинг и продажи"):
        block(sec, by_sec[sec])

    before = lambda c: "+".join(f"{c}{s.rows[k]}" for k in sections)
    s.line("unexpected", "Непредвиденные", rate=M.BASE["unexpected"],
           f=lambda i, c, row: f"=({before(c)})*${RATE}{row}")
    s.line("costs", "Расходы всего", f=lambda i, c, row: f"={before(c)}+{c}{s.rows['unexpected']}", bold=True, indent=0)

    # ── деньги ──────────────────────────────────────────────────────
    s.section("ДЕНЬГИ")
    s.line("flow", "Денежный поток", f=lambda i, c, row: f"={c}{s.rows['revenue']}-{c}{s.rows['costs']}", bold=True, indent=0)
    s.line("cum", "Накопленный поток", total="last", bold=True, indent=0,
           f=lambda i, c, row: f"={COLS[i - 1]}{row}+{c}{s.rows['flow']}" if i else f"={c}{s.rows['flow']}")
    s.line("cash", "Деньги на счету", total="last", indent=0,
           f=lambda i, c, row: f"={ref['raise_total']}+{c}{s.rows['cum']}")
    s.line("in_plus", "В плюсе с этого месяца до конца, 1 = да", total=None, fmt=NUM,
           f=lambda i, c, row: f'=IF(COUNTIF({c}{s.rows["flow"]}:{LAST}{s.rows["flow"]},"<0")=0,1,0)')

    cum_rng = f"${FIRST}${s.rows['cum']}:${LAST}${s.rows['cum']}"
    s.line("paid_back", "Окупилось после ямы, 1 = да", total=None, fmt=NUM,
           f=lambda i, c, row: f"=IF(AND({i + 1}>=MATCH(MIN({cum_rng}),{cum_rng},0),{c}{s.rows['cum']}>=0),1,0)")

    s.section("РАСПРЕДЕЛЕНИЕ ПРИБЫЛИ")
    s.line("free", "Положительный поток месяца", f=lambda i, c, row: f"=MAX(0,{c}{s.rows['flow']})")
    s.line("to_growth", "На развитие", rate=M.BASE["to_growth"], rate_guess=False,
           f=lambda i, c, row: f"={c}{s.rows['free']}*${RATE}{row}")
    s.line("to_dividends", "Дивиденды", rate=M.BASE["to_dividends"], rate_guess=False,
           f=lambda i, c, row: f"={c}{s.rows['free']}*${RATE}{row}")
    return s.rows


# ─────────────────────────────────────────────────────────────────────
# Годы и проверки
# ─────────────────────────────────────────────────────────────────────

def build_years(ws, bud, staff):
    ws.column_dimensions["A"].width = 40
    for col in "BCDE":
        ws.column_dimensions[col].width = 16
    put(ws, "A1", "Бюджет по годам", TITLE)
    put(ws, "A2", "Суммы по листу «Бюджет», $. Денежный поток — до налогов на прибыль.", NOTE)
    for col, name in zip("ABCDE", ["", "Год 1", "Год 2", "Год 3", "Итого"]):
        put(ws, f"{col}4", name, BOLDW, fill=DARK, align="center" if col != "A" else None)
    lines = [("Выручка", "revenue", True), ("Себестоимость", "sec_Себестоимость", False),
             ("ФОТ", "sec_ФОТ", False), ("Налоги и взносы на ФОТ", "payroll_tax", False),
             ("Найм", "recruiting", False), ("Софт и инфраструктура", "sec_Софт и инфраструктура", False),
             ("Юрлица и финансы", "sec_Юрлица и финансы", False),
             ("Маркетинг и продажи", "sec_Маркетинг и продажи", False), ("Непредвиденные", "unexpected", False),
             ("Расходы всего", "costs", True), ("Денежный поток", "flow", True)]
    r = 5
    for label, key, bold in lines:
        put(ws, f"A{r}", label, BOLD if bold else BLACK)
        for col, (c0, c1) in zip("BCD", YEARS):
            put(ws, f"{col}{r}", f"=SUM(Бюджет!{c0}{bud[key]}:{c1}{bud[key]})", GREEN, CUR2, align="right")
        put(ws, f"E{r}", f"=SUM(B{r}:D{r})", BOLD if bold else BLACK, CUR2, align="right")
        r += 1
    for label, key, fmt in (("Накопленный поток на конец года", "cum", CUR2), ("Деньги на счету на конец года", "cash", CUR2)):
        put(ws, f"A{r}", label)
        for col, (_, c1) in zip("BCD", YEARS):
            put(ws, f"{col}{r}", f"=Бюджет!{c1}{bud[key]}", GREEN, fmt, align="right")
        r += 1
    put(ws, f"A{r}", "Штат на конец года")
    for col, (_, c1) in zip("BCD", YEARS):
        put(ws, f"{col}{r}", f"=Штат!{c1}{staff['total']}", GREEN, NUM, align="right")


def build_checks(ws, bud, staff, rev):
    ws.column_dimensions["A"].width = 44
    for col in "BCD":
        ws.column_dimensions[col].width = 20
    put(ws, "A1", "Итоги и сверка со стратегией", TITLE)
    for col, name in zip("ABCD", ["Показатель", "В стратегии", "В модели", "Сходится"]):
        put(ws, f"{col}4", name, BOLDW, fill=DARK)
    rng = lambda key: f"Бюджет!{FIRST}{bud[key]}:{LAST}{bud[key]}"
    cell = lambda sheet, row, m: f"{sheet}!{COLS[m - 1]}{row}"
    r = 5
    for col in "ABCD":
        put(ws, f"{col}{r}", "ИТОГИ" if col == "A" else "", BOLD, fill=LIGHT)
    r += 1
    summary = [
        ("Яма: минимум накопленного потока, $", f"=MIN({rng('cum')})", CUR2),
        ("Месяц ямы", f"=MATCH(MIN({rng('cum')}),{rng('cum')},0)", NUM),
        ("Окупается к месяцу", None, NUM),
        ("Устойчивый плюс с месяца", f'=IFERROR(MATCH(1,{rng("in_plus")},0),"нет за 36 мес.")', NUM),
        ("Деньги на счету к 36-му месяцу, $", f"={cell('Бюджет', bud['cash'], MON)}", CUR2),
        ("ARR к 36-му месяцу, $", f"={cell('Выручка', rev['arr'], MON)}", CUR2),
        ("Оценка к 36-му месяцу, $", f"={cell('Выручка', rev['valuation'], MON)}", CUR2),
    ]
    for label, fml, fmt in summary:
        put(ws, f"A{r}", label)
        if fml is None:
            fml = f'=IFERROR(MATCH(1,{rng("paid_back")},0),"нет за 36 мес.")'
        put(ws, f"C{r}", fml, GREEN, fmt, align="right")
        r += 1
    r += 1
    for col in "ABCD":
        put(ws, f"{col}{r}", "СВЕРКА СО СТРАТЕГИЕЙ" if col == "A" else "", BOLD, fill=LIGHT)
    r += 1
    st = staff["total"]
    checks = [
        ("Штат к 3-му месяцу, не меньше 25", 25, f"={cell('Штат', st, 3)}", NUM, "ge"),
        ("Штат к 3-му месяцу, не больше 40", 40, f"={cell('Штат', st, 3)}", NUM, "le"),
        ("Штат к 6-му месяцу, не меньше", 70, f"={cell('Штат', st, 6)}", NUM, "ge"),
        ("Штат к 18-му месяцу", 135, f"={cell('Штат', st, 18)}", NUM, 5),
        ("ARR к 18-му месяцу, $", 42_000_000, f"={cell('Выручка', rev['arr'], 18)}", CUR2, 1_500_000),
        ("Труд: компаний к 18-му", 157, f"={cell('Выручка', rev['labor_base'], 18)}", NUM, 5),
        ("Капитал: компаний к 18-му", 256, f"={cell('Выручка', rev['cap_base'], 18)}", NUM, 10),
        ("Личность: подписчиков к 18-му", 63_500, f"={cell('Выручка', rev['subs'], 18)}", NUM, 2_000),
        ("Расходы за 18 месяцев, $ (этапы деки)", 42_000_000,
         f"=SUM(Бюджет!{FIRST}{bud['costs']}:{COLS[17]}{bud['costs']})", CUR2, 5_000_000),
        ("Деньги на счету к 18-му, $", 21_000_000, f"={cell('Бюджет', bud['cash'], 18)}", CUR2, 3_000_000),
    ]
    for label, plan, fml, fmt, tol in checks:
        put(ws, f"A{r}", label)
        put(ws, f"B{r}", plan, BLUE, fmt, align="right")
        put(ws, f"C{r}", fml, GREEN, fmt, align="right")
        test = {"ge": f'=IF(C{r}>=B{r},"да","НЕТ")', "le": f'=IF(C{r}<=B{r},"да","НЕТ")'}.get(
            tol, f'=IF(ABS(C{r}-B{r})<={tol},"да","НЕТ")')
        put(ws, f"D{r}", test, BOLD, align="center")
        r += 1


def main():
    run = M.build(M.BASE)
    wb = Workbook()
    ws_bud = wb.active
    ws_bud.title = "Бюджет"
    ws_staff = wb.create_sheet("Штат")
    ws_rev = wb.create_sheet("Выручка")
    ws_lev = wb.create_sheet("Рычаги")
    ws_years = wb.create_sheet("Годы")
    ws_chk = wb.create_sheet("Проверки")
    ref = build_levers(ws_lev)
    staff = build_staff(ws_staff, run)
    rev = build_revenue(ws_rev, run, ref)
    bud = build_budget(ws_bud, run, ref, staff, rev)
    build_years(ws_years, bud, staff)
    build_checks(ws_chk, bud, staff, rev)
    wb.save(HERE / "finmodel-wif.xlsx")
    print("записан finmodel-wif.xlsx")


if __name__ == "__main__":
    main()
