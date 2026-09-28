# -*- coding: utf-8 -*-
"""Собирает finmodel-wif.xlsx из того же движка, что и finmodel-wif.md.

В книге живые формулы: меняешь рычаг или траекторию клиентов — пересчитывается
всё остальное, включая проверки на сходимость со стратегией.

Синий текст — то, что правится руками. Чёрный — формулы. Жёлтая заливка —
ключевые допущения. Запуск: python3 _finmodel_wif_xlsx.py
"""

from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import _finmodel_wif as M

HERE = Path(__file__).parent
MON = M.MONTHS
FIRST = 3           # первая колонка месяца (C)
COLS = [get_column_letter(FIRST + i) for i in range(MON)]

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
CUR2 = '$#,##0.0;($#,##0.0);-'
NUM = '#,##0;(#,##0);-'
PCT = '0.0%'


def put(ws, cell, value, font=BLACK, fmt=None, fill=None, align=None):
    c = ws[cell]
    c.value = value
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if align:
        c.alignment = Alignment(horizontal=align)
    return c


def build_levers(ws):
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 62
    put(ws, "A1", "Рычаги финмодели WIF", TITLE)
    put(ws, "A2", "Синим — то, что правится руками. Жёлтым — допущения, которых в стратегии нет "
                  "и которые первыми надо заменить фактом.", NOTE)
    for col, name in (("A", "Рычаг"), ("B", "Значение"), ("C", "Откуда")):
        put(ws, f"{col}4", name, HEAD, fill=DARK)

    L = M.BASE
    rows = [
        ("ТРУД · ИИ-СОТРУДНИКИ", None, None, False),
        ("Средний платёж на старте, $/мес", L["labor_arpa_start"], "target-state-18m.md, roles.md: первые контракты от $5 тыс.", False),
        ("Средний платёж к мес. 18, $/мес", L["labor_arpa_end"], "target-state-18m.md", False),
        ("Отток компаний в месяц", L["labor_churn"], "target-state-18m.md: не выше 1%", False),
        ("Цена пилота, $ разово", L["pilot_price"], "90-day-plan.md: $3–5 тыс., оплата вперёд", False),
        ("Месяц выхода на платящих", 6, "roles.md: мес. 6 — первые контракты $5 тыс./мес", False),
        ("ЛИЧНОСТЬ · ПЕРСОНАЖИ", None, None, False),
        ("Цена подписки, $/мес", L["ident_price"], "target-state-18m.md", False),
        ("Отток подписчиков в месяц", L["ident_churn"], "target-state-18m.md", False),
        ("Конверсия посетителя в подписку", L["ident_conversion"], "target-state-18m.md", False),
        ("Средний чек сделки с брендом, $", L["brand_check"], "target-state-18m.md", False),
        ("КАПИТАЛ · УЧЁТ РАСХОДОВ НА ИИ", None, None, False),
        ("Средний платёж на старте, $/мес", L["cap_arpa_start"], "Допущение: в стратегии нет. Ориентир — оффер $500–2000/мес из 90-day-plan.md", True),
        ("Средний платёж к мес. 18, $/мес", L["cap_arpa_end"], "target-state-18m.md", False),
        ("Отток компаний в месяц", L["cap_churn"], "Допущение: в стратегии нет. Самообслуживание, отток выше, чем в Труде", True),
        ("КОМАНДА", None, None, False),
        ("Полная стоимость ставки, $/год", L["fte_cost_year"], "roles.md: вилка $120–200 тыс. Взята середина — допущение", True),
        ("ДЕНЬГИ", None, None, False),
        ("Раунд, $", L["raise_total"], "Дека v10, слайд 12", False),
        ("Этап 1, мес. 1–3, $", L["stages"][0][2], "90-day-plan.md, дека v10 слайд 14", False),
        ("Этап 2, мес. 4–6, $", L["stages"][1][2], "Дека v10, слайд 14", False),
        ("Этап 3, мес. 7–12, $", L["stages"][2][2], "Дека v10, слайд 14", False),
        ("Этап 4, мес. 13–18, $", L["stages"][3][2], "Дека v10, слайд 14", False),
        ("Резерв, $", L["reserve"], "Дека v10, слайд 14", False),
    ]
    r = 5
    order = []
    for label, value, src, is_guess in rows:
        if value is None:
            put(ws, f"A{r}", label, BOLD, fill=GREY)
            put(ws, f"B{r}", "", BOLD, fill=GREY)
            put(ws, f"C{r}", "", BOLD, fill=GREY)
        else:
            put(ws, f"A{r}", label, BLACK)
            fmt = PCT if isinstance(value, float) and value < 1 else CUR if value >= 100 else NUM
            c = put(ws, f"B{r}", value, BLUE, fmt, YELLOW if is_guess else None, "right")
            put(ws, f"C{r}", src, NOTE)
            order.append((label, f"Рычаги!$B${r}"))
            c.border = THIN
        r += 1
    return order


def build_model(ws, run, ref):
    ws.freeze_panes = "C6"
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 11
    for col in COLS:
        ws.column_dimensions[col].width = 10

    put(ws, "A1", "Модель по месяцам · базовый сценарий", TITLE)
    put(ws, "A2", "Синие строки — вводные: траектория клиентов и план расхода. Всё остальное — "
                  "формулы. Траектория проведена через контрольные точки target-state-18m.md "
                  "(мес. 6, 12, 15, 18), между ними экспонента.", NOTE)
    put(ws, "A4", "Месяц", HEAD, fill=DARK)
    put(ws, "B4", "Единица", HEAD, fill=DARK)
    for i, col in enumerate(COLS):
        put(ws, f"{col}4", i + 1, HEAD, NUM, DARK, "center")

    rows = {}
    r = [5]

    def section(title):
        put(ws, f"A{r[0]}", title, BOLD, fill=GREY)
        put(ws, f"B{r[0]}", "", BOLD, fill=GREY)
        for col in COLS:
            put(ws, f"{col}{r[0]}", "", BOLD, fill=GREY)
        r[0] += 1

    def line(label, unit, values=None, formula=None, fmt=NUM, font=None, key=None, bold=False):
        row = r[0]
        put(ws, f"A{row}", label, BOLD if bold else BLACK)
        put(ws, f"B{row}", unit, NOTE)
        for i, col in enumerate(COLS):
            m = i + 1
            if formula:
                put(ws, f"{col}{row}", formula(m, col, i), font or BLACK, fmt, align="right")
            else:
                put(ws, f"{col}{row}", round(values[m], 4), font or BLUE, fmt, align="right")
        if key:
            rows[key] = row
        r[0] += 1
        return row

    prev = lambda i: COLS[i - 1] if i > 0 else None

    # ── Труд ────────────────────────────────────────────────────────
    section("ТРУД · ИИ-СОТРУДНИКИ")
    ra = line("Активных компаний", "шт.", values=run["labor_actives"], key="labor_act")
    line("Новых компаний за месяц", "шт.",
         formula=lambda m, c, i: (f"={c}{ra}-{prev(i)}{ra}*(1-{ref['Отток компаний в месяц']})"
                                  if i else f"={c}{ra}"))
    rarpa = line("Средний платёж", "$/мес",
                 formula=lambda m, c, i: (
                     f"=IF({m}<{ref['Месяц выхода на платящих']},0,"
                     f"MIN({ref['Средний платёж к мес. 18, $/мес']},"
                     f"{ref['Средний платёж на старте, $/мес']}+"
                     f"({ref['Средний платёж к мес. 18, $/мес']}-{ref['Средний платёж на старте, $/мес']})"
                     f"*({m}-{ref['Месяц выхода на платящих']})/(18-{ref['Месяц выхода на платящих']})))"),
                 fmt=CUR)
    rpil = line("Пилотов запущено", "шт.", values=run.get("_pilots", [0] * (MON + 1)))
    for i, col in enumerate(COLS):
        ws[f"{col}{rpil}"] = M.BASE["pilots"].get(i + 1, 0)
    rlab = line("Выручка Труда", "$/мес",
                formula=lambda m, c, i: f"={c}{ra}*{c}{rarpa}+{c}{rpil}*{ref['Цена пилота, $ разово']}",
                fmt=CUR, key="labor_rev", bold=True)

    # ── Личность ────────────────────────────────────────────────────
    section("ЛИЧНОСТЬ · ПЕРСОНАЖИ")
    rs = line("Платных подписчиков", "чел.", values=run["ident_subs"], key="subs")
    rsa = line("Новых подписчиков за месяц", "чел.",
               formula=lambda m, c, i: (f"=MAX(0,{c}{rs}-{prev(i)}{rs}*(1-{ref['Отток подписчиков в месяц']}))"
                                        if i else f"={c}{rs}"))
    line("Визитов на платное предложение", "чел./мес",
         formula=lambda m, c, i: f"={c}{rsa}/{ref['Конверсия посетителя в подписку']}", key="visits")
    rsub = line("Выручка подписки", "$/мес",
                formula=lambda m, c, i: f"={c}{rs}*{ref['Цена подписки, $/мес']}", fmt=CUR)
    rbd = line("Сделок с брендами", "шт./мес", values=run["brand_deals"])
    rbr = line("Выручка от брендов", "$/мес",
               formula=lambda m, c, i: f"={c}{rbd}*{ref['Средний чек сделки с брендом, $']}", fmt=CUR)

    # ── Капитал ─────────────────────────────────────────────────────
    section("КАПИТАЛ · УЧЁТ РАСХОДОВ НА ИИ")
    rc = line("Платящих компаний", "шт.", values=run["cap_actives"], key="cap_act")
    line("Новых компаний за месяц", "шт.",
         formula=lambda m, c, i: (f"=MAX(0,{c}{rc}-{prev(i)}{rc}*(1-{ref['Отток компаний в месяц2']}))"
                                  if i else f"={c}{rc}"))
    rcarpa = line("Средний платёж", "$/мес",
                  formula=lambda m, c, i: (
                      f"=IF({m}<3,0,MIN({ref['Средний платёж к мес. 18, $/мес2']},"
                      f"{ref['Средний платёж на старте, $/мес2']}+"
                      f"({ref['Средний платёж к мес. 18, $/мес2']}-{ref['Средний платёж на старте, $/мес2']})"
                      f"*({m}-3)/15))"),
                  fmt=CUR)
    rcap = line("Выручка Капитала", "$/мес",
                formula=lambda m, c, i: f"={c}{rc}*{c}{rcarpa}", fmt=CUR, bold=True)

    # ── Итог ────────────────────────────────────────────────────────
    section("ВЫРУЧКА")
    rrev = line("Выручка всего", "$/мес",
                formula=lambda m, c, i: f"={c}{rlab}+{c}{rsub}+{c}{rbr}+{c}{rcap}",
                fmt=CUR, key="revenue", bold=True)
    rarr = line("ARR (без сделок с брендами)", "$",
                formula=lambda m, c, i: f"=({c}{rlab}-{c}{rpil}*{ref['Цена пилота, $ разово']}+{c}{rsub}+{c}{rcap})*12",
                fmt=CUR, key="arr")

    # ── Расходы ─────────────────────────────────────────────────────
    section("РАСХОДЫ И ДЕНЬГИ")
    rf = line("Штат", "ставок", values=run["fte"], key="fte")
    rp = line("ФОТ", "$/мес",
              formula=lambda m, c, i: f"={c}{rf}*{ref['Полная стоимость ставки, $/год']}/12", fmt=CUR)
    rcost = line("Расход всего", "$/мес", values=run["costs"], fmt=CUR, key="costs")
    line("В том числе всё, кроме людей", "$/мес",
         formula=lambda m, c, i: f"={c}{rcost}-{c}{rp}", fmt=CUR)
    rnet = line("Чистый поток", "$/мес",
                formula=lambda m, c, i: f"={c}{rrev}-{c}{rcost}", fmt=CUR, key="net", bold=True)
    rcash = line("Деньги на счету", "$",
                 formula=lambda m, c, i: (f"={prev(i)}{rcash_ph}+{c}{rnet}" if i
                                          else f"={ref['Раунд, $']}+{c}{rnet}"),
                 fmt=CUR, key="cash", bold=True)
    return rows, rcash


rcash_ph = 0  # заполняется ниже: строка «Деньги на счету» ссылается сама на себя


def build_checks(ws, rows, model_sheet="Модель"):
    ws.column_dimensions["A"].width = 46
    for col in "BCD":
        ws.column_dimensions[col].width = 20
    put(ws, "A1", "Сходимость со стратегией", TITLE)
    put(ws, "A2", "Модель считает по своим формулам, колонка «В стратегии» — то, что написано "
                  "в target-state-18m.md и деке v10. Расхождение означает, что в одном из двух "
                  "мест цифру надо поправить.", NOTE)
    for col, name in (("A", "Что сверяем"), ("B", "В стратегии"), ("C", "В модели"), ("D", "Сходится")):
        put(ws, f"{col}4", name, HEAD, fill=DARK)

    last = COLS[-1]
    checks = [
        ("ARR группы в 18-м месяце", 42_000_000, f"={model_sheet}!{last}{rows['arr']}", CUR, 1_500_000),
        ("Выручка 18-го месяца", 3_600_000, f"={model_sheet}!{last}{rows['revenue']}", CUR, 400_000),
        ("Расход 18-го месяца", 4_000_000, f"={model_sheet}!{last}{rows['costs']}", CUR, 400_000),
        ("Чистый поток 18-го месяца", -350_000, f"={model_sheet}!{last}{rows['net']}", CUR, 300_000),
        ("Деньги на счету в 18-м месяце", 21_000_000, f"={model_sheet}!{last}{rows['cash']}", CUR, 2_000_000),
        ("Платящих компаний, Труд", 157, f"={model_sheet}!{last}{rows['labor_act']}", NUM, 5),
        ("Подписчиков, Личность", 63_500, f"={model_sheet}!{last}{rows['subs']}", NUM, 2_000),
        ("Платящих компаний, Капитал", 256, f"={model_sheet}!{last}{rows['cap_act']}", NUM, 10),
        ("Визитов на оплату в месяц, Личность", 1_600_000, f"={model_sheet}!{last}{rows['visits']}", NUM, 300_000),
        ("Штат к 18-му месяцу", 135, f"={model_sheet}!{last}{rows['fte']}", NUM, 5),
    ]
    r = 5
    for label, plan, formula, fmt, tol in checks:
        put(ws, f"A{r}", label, BLACK)
        put(ws, f"B{r}", plan, BLUE, fmt, align="right")
        put(ws, f"C{r}", formula, GREEN, fmt, align="right")
        put(ws, f"D{r}", f'=IF(ABS(C{r}-B{r})<={tol},"да","НЕТ")', BOLD, align="center")
        for col in "ABCD":
            ws[f"{col}{r}"].border = THIN
        r += 1
    put(ws, f"A{r + 1}", "Допуск подобран под порядок величины показателя; он в формуле колонки «Сходится».", NOTE)


def main():
    global rcash_ph
    run = M.build(M.BASE, 1.0)
    wb = Workbook()

    ws_l = wb.active
    ws_l.title = "Рычаги"
    order = build_levers(ws_l)
    # у Труда и Капитала одинаковые подписи рычагов — второй по порядку получает суффикс 2
    ref = {}
    for k, v in order:
        ref[k + "2" if k in ref else k] = v
    # второй блок «Средний платёж …» и «Отток компаний в месяц» — это Капитал
    for key in ("Средний платёж на старте, $/мес", "Средний платёж к мес. 18, $/мес",
                "Отток компаний в месяц"):
        if key + "2" not in ref:
            raise SystemExit(f"не найден парный рычаг для {key}")

    ws_m = wb.create_sheet("Модель")
    # строка «Деньги на счету» ссылается на предыдущий месяц самой себя,
    # поэтому её номер нужен до записи — считаем заранее
    rcash_ph = 32
    rows, actual = build_model(ws_m, run, ref)
    if actual != rcash_ph:
        raise SystemExit(f"строка «Деньги на счету» {actual}, а формулы ссылаются на {rcash_ph}")

    ws_c = wb.create_sheet("Проверки")
    build_checks(ws_c, rows)

    path = HERE / "finmodel-wif.xlsx"
    wb.save(path)
    print("записан", path.name, "· строка cash:", actual)


if __name__ == "__main__":
    main()
