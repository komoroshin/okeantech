# -*- coding: utf-8 -*-
"""Собирает finmodel-wif.xlsx на 36 месяцев из того же движка, что и finmodel-wif.md.

Листы: Рычаги · Модель (по месяцам) · Годы (отчёт о прибылях) · Оценка · Проверки.
Синие ячейки правятся руками, чёрные — формулы, зелёные — ссылки на другой лист,
жёлтая заливка — допущения, которых нет в стратегии.

Запуск: python3 _finmodel_wif_xlsx.py
После сборки книгу надо пересчитать (см. README-finmodel.md).
"""

from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import _finmodel_wif as M

HERE = Path(__file__).parent
MON = M.MONTHS
FIRST = 3
COLS = [get_column_letter(FIRST + i) for i in range(MON)]   # C … AL
YEARS = [(COLS[12 * y], COLS[12 * y + 11]) for y in range(MON // 12)]

FONT = "Arial"
BLUE = Font(name=FONT, size=10, color="0000FF")
BLACK = Font(name=FONT, size=10)
GREEN = Font(name=FONT, size=10, color="008000")
BOLD = Font(name=FONT, size=10, bold=True)
HEAD = Font(name=FONT, size=10, bold=True, color="FFFFFF")
TITLE = Font(name=FONT, size=13, bold=True)
NOTE = Font(name=FONT, size=9, color="666666", italic=True)
YELLOW = PatternFill("solid", fgColor="FFFF00")
DARK = PatternFill("solid", fgColor="333333")
GREY = PatternFill("solid", fgColor="F2F2F2")
THIN = Border(bottom=Side(style="thin", color="BFBFBF"))

CUR = '$#,##0;($#,##0);-'
NUM = '#,##0;(#,##0);-'
PCT = '0.0%'
MULT = '0.0"x"'


def put(ws, cell, value, font=BLACK, fmt=None, fill=None, align=None):
    c = ws[cell]
    c.value = value
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if align:
        c.alignment = Alignment(horizontal=align, wrap_text=False)
    return c


def header(ws, cols, labels):
    for col, name in zip(cols, labels):
        put(ws, f"{col}4", name, HEAD, fill=DARK, align="center" if col not in "AB" else None)


# ─────────────────────────────────────────────────────────────────────
# Рычаги
# ─────────────────────────────────────────────────────────────────────

LEVERS = [
    ("ТРУД · ИИ-СОТРУДНИКИ", None, None, None, False),
    ("labor_churn", "Отток компаний в месяц", PCT, "target-state-18m.md: не выше 1%", False),
    ("pilot_price", "Цена пилота, $ разово", CUR, "90-day-plan.md: $3–5 тыс.", False),
    ("ЛИЧНОСТЬ · ПЕРСОНАЖИ", None, None, None, False),
    ("ident_price", "Цена подписки, $/мес", CUR, "target-state-18m.md", False),
    ("ident_churn", "Отток подписчиков в месяц", PCT, "target-state-18m.md", False),
    ("ident_conversion", "Конверсия визита в подписку", PCT, "target-state-18m.md", False),
    ("brand_check", "Чек сделки с брендом, $", CUR, "target-state-18m.md", False),
    ("КАПИТАЛ · УЧЁТ РАСХОДОВ НА ИИ", None, None, None, False),
    ("cap_churn", "Отток компаний в месяц", PCT, "Допущение: в стратегии нет", True),
    ("КОМАНДА", None, None, None, False),
    ("fte_cost_year", "Полная стоимость ставки, $/год", CUR, "roles.md: вилка 120–200 тыс.", True),
    ("hire_cost", "Стоимость найма, $ на человека", CUR, "Допущение: рекрутинг и онбординг", True),
    ("СЕБЕСТОИМОСТЬ, ДОЛЯ ВЫРУЧКИ", None, None, None, False),
    ("cogs_labor", "Труд: инференс и проверка работы агента", PCT, "Допущение", True),
    ("cogs_subs", "Подписка: платформы, хостинг, поддержка", PCT, "Допущение", True),
    ("cogs_brand", "Бренды: производство под заказ", PCT, "Допущение", True),
    ("cogs_cap", "Капитал: инфраструктура биллинга", PCT, "Допущение", True),
    ("ПРИВЛЕЧЕНИЕ", None, None, None, False),
    ("commission", "Комиссия продажам, доля годового контракта Труда", PCT, "Допущение", True),
    ("cac_labor", "Маркетинг на одну компанию Труда, $", CUR, "Допущение", True),
    ("cac_cap", "Маркетинг на одну компанию Капитала, $", CUR, "Допущение", True),
    ("cost_per_visit", "Стоимость визита в Личности, $", '$0.00', "Допущение — самое непроверенное", True),
    ("ПОСТОЯННЫЕ, $ В МЕСЯЦ", None, None, None, False),
    ("content_monthly", "Производство выпусков Личности", CUR, "Допущение", True),
    ("platform_monthly", "Общая платформа: модели, хостинг, инструменты", CUR, "Допущение", True),
    ("legal_monthly", "Юрлица США/ЕС, аудит, комплаенс", CUR, "Допущение", True),
    ("ga_pct", "Офис, поездки, софт — доля ФОТ", PCT, "Допущение", True),
    ("ДЕНЬГИ", None, None, None, False),
    ("raise_total", "Раунд, $", CUR, "Дека v10", False),
    ("ОЦЕНКА — МУЛЬТИПЛИКАТОРЫ", None, None, None, False),
    ("mult_labor", "Труд, × ARR", MULT, "Допущение: проверить по сделкам-аналогам", True),
    ("mult_cap", "Капитал, × ARR", MULT, "Допущение", True),
    ("mult_subs", "Подписка, × ARR", MULT, "Допущение", True),
    ("mult_brand", "Бренды, × выручки за 12 месяцев", MULT, "Допущение", True),
]


def build_levers(ws):
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 48
    put(ws, "A1", "Рычаги финмодели WIF · 36 месяцев", TITLE)
    put(ws, "A2", "Синим — правится руками. Жёлтым — допущения, которых в стратегии нет: их первыми "
                  "заменить фактом. Поток клиентов, чеки и штат по месяцам — синие строки на листе «Модель».", NOTE)
    for col, name in (("A", "Рычаг"), ("B", "Значение"), ("C", "Откуда")):
        put(ws, f"{col}4", name, HEAD, fill=DARK)
    ref, r = {}, 5
    for key, label, fmt, src, guess in LEVERS:
        if label is None:
            for col in "ABC":
                put(ws, f"{col}{r}", key if col == "A" else "", BOLD, fill=GREY)
        else:
            put(ws, f"A{r}", label)
            put(ws, f"B{r}", M.BASE[key], BLUE, fmt, YELLOW if guess else None, "right").border = THIN
            put(ws, f"C{r}", src, NOTE)
            ref[key] = f"Рычаги!$B${r}"
        r += 1
    return ref


# ─────────────────────────────────────────────────────────────────────
# Модель по месяцам
# ─────────────────────────────────────────────────────────────────────

def build_model(ws, run, ref):
    ws.freeze_panes = "C5"
    ws.column_dimensions["A"].width = 42
    ws.column_dimensions["B"].width = 10
    for col in COLS:
        ws.column_dimensions[col].width = 11

    put(ws, "A1", "Модель по месяцам · базовый сценарий", TITLE)
    put(ws, "A2", "Синие строки — план: новые клиенты, визиты, сделки, чеки, штат. Остальное — формулы. "
                  "База = прошлый месяц − ROUND(прошлый × отток) + новые; все штуки целые.", NOTE)
    for y, (c0, c1) in enumerate(YEARS):
        put(ws, f"{c0}3", f"Год {y + 1}", BOLD, align="left")
    put(ws, "A4", "Месяц", HEAD, fill=DARK)
    put(ws, "B4", "Ед.", HEAD, fill=DARK)
    for i, col in enumerate(COLS):
        put(ws, f"{col}4", i + 1, HEAD, NUM, DARK, "center")

    rows, r = {}, [5]
    prev = lambda i: COLS[i - 1]

    def section(title):
        for col in ["A", "B"] + COLS:
            put(ws, f"{col}{r[0]}", title if col == "A" else "", BOLD, fill=GREY)
        r[0] += 1

    def line(key, label, unit, values=None, f=None, fmt=NUM, bold=False):
        row = r[0]
        put(ws, f"A{row}", label, BOLD if bold else BLACK)
        put(ws, f"B{row}", unit, NOTE)
        for i, c in enumerate(COLS):
            m = i + 1
            if f:
                put(ws, f"{c}{row}", f(m, c, i, row), BLACK, fmt, align="right")
            else:
                v = values[m]
                put(ws, f"{c}{row}", int(v) if float(v).is_integer() else round(v, 2), BLUE, fmt, align="right")
        rows[key] = row
        r[0] += 1
        return row

    def stock_f(adds_key, churn_ref):
        return lambda m, c, i, row: (f"={prev(i)}{row}-ROUND({prev(i)}{row}*{churn_ref},0)+{c}{rows[adds_key]}"
                                     if i else f"={c}{rows[adds_key]}")

    R = lambda k: rows[k]

    section("ТРУД · ИИ-СОТРУДНИКИ")
    line("labor_adds", "Новых компаний за месяц", "шт.", run["labor_adds"])
    line("labor_base", "Компаний", "шт.", f=stock_f("labor_adds", ref["labor_churn"]))
    line("labor_arpa", "Платёж компании", "$/мес", run["labor_arpa"], fmt=CUR)
    line("pilots", "Пилотов запущено", "шт.", run["pilots"])
    line("labor_rev", "Выручка Труда", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('labor_base')}*{c}{R('labor_arpa')}+{c}{R('pilots')}*{ref['pilot_price']}",
         fmt=CUR, bold=True)

    section("ЛИЧНОСТЬ · ПЕРСОНАЖИ")
    line("visits", "Визитов на платное предложение", "в мес.", run["visits"])
    line("subs_adds", "Новых подписчиков", "чел.",
         f=lambda m, c, i, row: f"=ROUND({c}{R('visits')}*{ref['ident_conversion']},0)")
    line("subs", "Подписчиков", "чел.", f=stock_f("subs_adds", ref["ident_churn"]))
    line("subs_rev", "Выручка подписки", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('subs')}*{ref['ident_price']}", fmt=CUR, bold=True)
    line("brand_deals", "Сделок с брендами", "шт.", run["brand_deals"])
    line("brand_rev", "Выручка от брендов", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('brand_deals')}*{ref['brand_check']}", fmt=CUR, bold=True)

    section("КАПИТАЛ · УЧЁТ РАСХОДОВ НА ИИ")
    line("cap_adds", "Новых компаний за месяц", "шт.", run["cap_adds"])
    line("cap_base", "Компаний", "шт.", f=stock_f("cap_adds", ref["cap_churn"]))
    line("cap_arpa", "Платёж компании", "$/мес", run["cap_arpa"], fmt=CUR)
    line("cap_rev", "Выручка Капитала", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('cap_base')}*{c}{R('cap_arpa')}", fmt=CUR, bold=True)

    section("ВЫРУЧКА")
    line("revenue", "Выручка всего", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('labor_rev')}+{c}{R('subs_rev')}+{c}{R('brand_rev')}+{c}{R('cap_rev')}",
         fmt=CUR, bold=True)
    line("labor_arr", "ARR Труда (без пилотов)", "$",
         f=lambda m, c, i, row: f"=({c}{R('labor_rev')}-{c}{R('pilots')}*{ref['pilot_price']})*12", fmt=CUR)
    line("arr", "ARR группы (без брендов и пилотов)", "$",
         f=lambda m, c, i, row: f"={c}{R('labor_arr')}+({c}{R('subs_rev')}+{c}{R('cap_rev')})*12", fmt=CUR, bold=True)

    section("СЕБЕСТОИМОСТЬ")
    line("cogs", "Себестоимость", "$/мес",
         f=lambda m, c, i, row: (f"={c}{R('labor_rev')}*{ref['cogs_labor']}+{c}{R('subs_rev')}*{ref['cogs_subs']}"
                                 f"+{c}{R('brand_rev')}*{ref['cogs_brand']}+{c}{R('cap_rev')}*{ref['cogs_cap']}"),
         fmt=CUR)
    line("gross", "Валовая прибыль", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('revenue')}-{c}{R('cogs')}", fmt=CUR, bold=True)

    section("ОПЕРАЦИОННЫЕ РАСХОДЫ")
    line("fte", "Штат", "ставок", run["fte"])
    line("payroll", "ФОТ", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('fte')}*{ref['fte_cost_year']}/12", fmt=CUR)
    line("hiring", "Найм", "$/мес",
         f=lambda m, c, i, row: (f"=MAX(0,{c}{R('fte')}-{prev(i)}{R('fte')})*{ref['hire_cost']}" if i else "=0"),
         fmt=CUR)
    line("commissions", "Комиссии продажам", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('labor_adds')}*{c}{R('labor_arpa')}*12*{ref['commission']}", fmt=CUR)
    line("acquisition", "Привлечение клиентов", "$/мес",
         f=lambda m, c, i, row: (f"={c}{R('labor_adds')}*{ref['cac_labor']}+{c}{R('cap_adds')}*{ref['cac_cap']}"
                                 f"+{c}{R('visits')}*{ref['cost_per_visit']}"), fmt=CUR)
    line("fixed", "Контент, платформа, юрлица", "$/мес",
         f=lambda m, c, i, row: f"={ref['content_monthly']}+{ref['platform_monthly']}+{ref['legal_monthly']}", fmt=CUR)
    line("ga", "Офис, поездки, софт", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('payroll')}*{ref['ga_pct']}", fmt=CUR)
    line("opex", "Операционные всего", "$/мес",
         f=lambda m, c, i, row: f"=SUM({c}{R('payroll')}:{c}{R('ga')})", fmt=CUR, bold=True)

    section("ПРИБЫЛЬ И ДЕНЬГИ")
    line("costs", "Расходы всего", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('cogs')}+{c}{R('opex')}", fmt=CUR)
    line("ebitda", "EBITDA", "$/мес",
         f=lambda m, c, i, row: f"={c}{R('gross')}-{c}{R('opex')}", fmt=CUR, bold=True)
    line("cash", "Деньги на счету", "$",
         f=lambda m, c, i, row: (f"={prev(i)}{row}+{c}{R('ebitda')}" if i
                                 else f"={ref['raise_total']}+{c}{R('ebitda')}"), fmt=CUR, bold=True)
    last = COLS[-1]
    line("in_plus", "В плюсе с этого месяца до конца", "1 = да",
         f=lambda m, c, i, row: f'=IF(COUNTIF({c}{R("ebitda")}:{last}{R("ebitda")},"<0")=0,1,0)')

    section("ОЦЕНКА — ПРОМЕЖУТОЧНЫЙ РЕЗУЛЬТАТ")
    line("valuation", "Оценка по мультипликаторам", "$",
         f=lambda m, c, i, row: (f"={c}{R('labor_arr')}*{ref['mult_labor']}"
                                 f"+{c}{R('cap_rev')}*12*{ref['mult_cap']}"
                                 f"+{c}{R('subs_rev')}*12*{ref['mult_subs']}"
                                 f"+SUM({COLS[max(0, i - 11)]}{R('brand_rev')}:{c}{R('brand_rev')})*{ref['mult_brand']}"),
         fmt=CUR, bold=True)
    return rows


# ─────────────────────────────────────────────────────────────────────
# Годы, оценка, проверки
# ─────────────────────────────────────────────────────────────────────

def build_years(ws, rows):
    ws.column_dimensions["A"].width = 38
    for col in "BCD":
        ws.column_dimensions[col].width = 16
    put(ws, "A1", "Отчёт о прибылях по годам · базовый сценарий", TITLE)
    put(ws, "A2", "Суммы по листу «Модель». До налогов, без капитальных затрат.", NOTE)
    header(ws, "ABCD", ["$", "Год 1", "Год 2", "Год 3"])

    def s(key):
        return [f"=SUM(Модель!{c0}{rows[key]}:{c1}{rows[key]})" for c0, c1 in YEARS]

    lines = [
        ("Труд", s("labor_rev"), False), ("Личность: подписка", s("subs_rev"), False),
        ("Личность: бренды", s("brand_rev"), False), ("Капитал", s("cap_rev"), False),
        ("Выручка", s("revenue"), True), ("Себестоимость", s("cogs"), False),
        ("Валовая прибыль", s("gross"), True), ("ФОТ", s("payroll"), False), ("Найм", s("hiring"), False),
        ("Комиссии продажам", s("commissions"), False), ("Привлечение клиентов", s("acquisition"), False),
        ("Контент, платформа, юрлица", s("fixed"), False), ("Офис, поездки, софт", s("ga"), False),
        ("Операционные всего", s("opex"), True), ("EBITDA", s("ebitda"), True),
        ("Касса на конец года", [f"=Модель!{c1}{rows['cash']}" for _, c1 in YEARS], True),
    ]
    at = {}
    r = 5
    for label, formulas, bold in lines:
        put(ws, f"A{r}", label, BOLD if bold else BLACK)
        for col, fml in zip("BCD", formulas):
            put(ws, f"{col}{r}", fml, GREEN, CUR, align="right")
        at[label] = r
        r += 1
    for label, num, den in (("Валовая маржа", "Валовая прибыль", "Выручка"), ("Маржа EBITDA", "EBITDA", "Выручка")):
        put(ws, f"A{r}", label)
        for col in "BCD":
            put(ws, f"{col}{r}", f"=IF({col}{at[den]}=0,0,{col}{at[num]}/{col}{at[den]})", BLACK, PCT, align="right")
        r += 1


def build_valuation(ws, rows):
    ws.column_dimensions["A"].width = 12
    for col in "BCDE":
        ws.column_dimensions[col].width = 20
    put(ws, "A1", "Оценка как промежуточный результат", TITLE)
    put(ws, "A2", "Оценка = ARR направлений × мультипликаторы с листа «Рычаги» + выручка брендов за 12 месяцев. "
                  "Мультипликаторы — допущение, их назначит рынок.", NOTE)
    header(ws, "ABCDE", ["Месяц", "ARR группы", "Оценка", "Для $1 млрд нужно", "Оценка / $1 млрд"])
    r = 5
    for m in (12, 18, 24, 30, 36):
        c = COLS[m - 1]
        put(ws, f"A{r}", m, BLACK, NUM, align="center")
        put(ws, f"B{r}", f"=Модель!{c}{rows['arr']}", GREEN, CUR, align="right")
        put(ws, f"C{r}", f"=Модель!{c}{rows['valuation']}", GREEN, CUR, align="right")
        put(ws, f"D{r}", f"=IF(B{r}=0,0,1000000000/B{r})", BLACK, MULT, align="right")
        put(ws, f"E{r}", f"=C{r}/1000000000", BLACK, PCT, align="right")
        r += 1


def build_checks(ws, rows):
    ws.column_dimensions["A"].width = 46
    for col in "BCD":
        ws.column_dimensions[col].width = 20
    put(ws, "A1", "Итоги и сверка со стратегией", TITLE)
    put(ws, "A2", "Итоги считаются по листу «Модель». Сверка — с target-state-18m.md и декой v10 на 18-й месяц.", NOTE)
    header(ws, "ABCD", ["Показатель", "В стратегии", "В модели", "Сходится"])

    last = COLS[-1]
    rng = lambda key: f"Модель!{COLS[0]}{rows[key]}:{last}{rows[key]}"
    cell = lambda key, m: f"Модель!{COLS[m - 1]}{rows[key]}"

    r = 5
    put(ws, f"A{r}", "ИТОГИ", BOLD, fill=GREY)
    r += 1
    for label, fml, fmt in (
        ("Выход в устойчивый плюс, месяц", f'=IFERROR(MATCH(1,{rng("in_plus")},0),"нет за 36 мес.")', NUM),
        ("Дно кассы, $", f"=MIN({rng('cash')})", CUR),
        ("Месяц дна кассы", f"=MATCH(MIN({rng('cash')}),{rng('cash')},0)", NUM),
        ("Касса к 36-му месяцу, $", f"={cell('cash', MON)}", CUR),
        ("Оценка к 36-му месяцу, $", f"={cell('valuation', MON)}", CUR),
    ):
        put(ws, f"A{r}", label)
        put(ws, f"C{r}", fml, GREEN, fmt, align="right")
        r += 1

    r += 1
    put(ws, f"A{r}", "СВЕРКА НА 18-Й МЕСЯЦ", BOLD, fill=GREY)
    r += 1
    checks = [
        ("ARR группы", 42_000_000, f"={cell('arr', 18)}", CUR, 1_500_000),
        ("Выручка 18-го месяца", 3_600_000, f"={cell('revenue', 18)}", CUR, 400_000),
        ("Расход 18-го месяца", 4_000_000, f"={cell('costs', 18)}", CUR, 400_000),
        ("Деньги на счету", 21_000_000, f"={cell('cash', 18)}", CUR, 2_000_000),
        ("Труд: компаний", 157, f"={cell('labor_base', 18)}", NUM, 5),
        ("Капитал: компаний", 256, f"={cell('cap_base', 18)}", NUM, 10),
        ("Личность: подписчиков", 63_500, f"={cell('subs', 18)}", NUM, 2_000),
        ("Штат", 135, f"={cell('fte', 18)}", NUM, 5),
    ]
    for (first, last_m, total), k in zip(M.BASE["stages"], range(1, 5)):
        checks.append((f"Расходы этапа {k}, мес. {first}–{last_m}", total,
                       f"=SUM(Модель!{COLS[first - 1]}{rows['costs']}:{COLS[last_m - 1]}{rows['costs']})", CUR,
                       total * 0.15))
    for label, plan, fml, fmt, tol in checks:
        put(ws, f"A{r}", label)
        put(ws, f"B{r}", plan, BLUE, fmt, align="right")
        put(ws, f"C{r}", fml, GREEN, fmt, align="right")
        put(ws, f"D{r}", f'=IF(ABS(C{r}-B{r})<={tol},"да","НЕТ")', BOLD, align="center")
        for col in "ABCD":
            ws[f"{col}{r}"].border = THIN
        r += 1
    put(ws, f"A{r + 1}", "Допуск — в формуле колонки «Сходится», под порядок величины. "
                         "Расходы этапов сверяются с допуском 15%.", NOTE)


def main():
    run = M.build(M.BASE)
    wb = Workbook()
    ws = wb.active
    ws.title = "Рычаги"
    ref = build_levers(ws)
    rows = build_model(wb.create_sheet("Модель"), run, ref)
    build_years(wb.create_sheet("Годы"), rows)
    build_valuation(wb.create_sheet("Оценка"), rows)
    build_checks(wb.create_sheet("Проверки"), rows)
    wb.save(HERE / "finmodel-wif.xlsx")
    print("записан finmodel-wif.xlsx")


if __name__ == "__main__":
    main()
