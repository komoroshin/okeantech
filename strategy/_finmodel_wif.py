# -*- coding: utf-8 -*-
"""Финмодель WIF (Океан Тех) на 36 месяцев — бюджетный вид.

Устроена по образцу модели, которую коллеги дали как референс: штат по ролям
с окладами и месяцами найма, каждая статья расходов отдельной строкой, главный
лист — бюджет М1…М36 с итогом, внизу денежный поток, накопленный поток («яма»)
и распределение прибыли.

Выручка считается от потока новых клиентов с оттоком (месяцы 1–18 — из
стратегии, 19–36 — поток держится на уровне 18-го). Оценка — промежуточный
вывод из ARR, а не цель.

Оклады команды — уровня распределённой команды из референса ($2,5–9 тыс. в
месяц); пять руководителей направлений — по roles.md ($150 тыс. в год).
Исходная Excel-модель от 10.09.2026 в репозиторий не передавалась.

Запуск: python3 _finmodel_wif.py        → finmodel-wif.md
        python3 _finmodel_wif_xlsx.py   → finmodel-wif.xlsx
"""

import math
from pathlib import Path

HERE = Path(__file__).parent
MONTHS = 36

# ─────────────────────────────────────────────────────────────────────
# ВЫРУЧКА: рычаги
# Опоры {месяц: значение}: между ними линейно, после последней уровень держится.
# None — подбирается под базу клиентов, названную в стратегии.
# ─────────────────────────────────────────────────────────────────────

BASE = {
    # Труд
    "labor_flow": {3: 0, 6: None, 9: None, 12: 12, 18: 21, 36: 21},
    "labor_fit": [(6, 6, 10), (9, 12, 60)],
    "labor_arpa": {6: 5_000, 18: 15_000, 36: 15_000},
    "labor_churn": 0.01,
    "pilots": {2: 1, 3: 2, 4: 2, 5: 2},
    "pilot_price": 4_000,
    # Личность
    "ident_visits": {8: 0, 12: None, 15: None, 18: 1_600_000, 36: 1_600_000},
    "ident_fit": [(12, 12, 10_000), (15, 15, 25_000)],
    "ident_price": 10,
    "ident_churn": 0.08,
    "ident_conversion": 0.01,
    "brand_flow": {3: 1, 6: 1, 9: 4, 12: 4, 18: 8, 36: 8},
    "brand_check": 50_000,
    # Капитал
    "cap_flow": {3: 2, 6: None, 12: 20, 18: 45, 36: 45},
    "cap_fit": [(6, 12, 100)],
    "cap_arpa": {3: 800, 18: 2_000, 36: 2_000},
    "cap_churn": 0.015,

    # Штат: общие рычаги
    "salary_scale": 1.0,          # множитель ко всем окладам: 2.0 — рынок США/ЕС
    "payroll_tax": 0.10,          # налоги и взносы сверх оклада
    "hire_cost_lead": 20_000,     # найм руководителя направления
    "hire_cost": 2_000,           # найм остальных
    "tools_per_head": 150,        # софт на человека в месяц
    "unexpected": 0.05,           # непредвиденные, доля всех расходов

    # Деньги и распределение
    "raise_total": 50_000_000,
    "stages": [(1, 3, 3_710_000), (4, 6, 5_700_000), (7, 12, 14_200_000), (13, 18, 18_400_000)],
    "reserve": 8_000_000,
    "to_growth": 1.0,             # доля положительного потока на развитие
    "to_dividends": 0.0,          # доля на дивиденды

    # Оценка
    "mult_labor": 10.0, "mult_cap": 10.0, "mult_subs": 4.0, "mult_brand": 1.5,
}

# ─────────────────────────────────────────────────────────────────────
# ШТАТ: роль, оклад $/мес, число людей по опорам {месяц: человек}
# lead=True — руководитель направления: найм дороже, из roles.md
# ─────────────────────────────────────────────────────────────────────

ROSTER = [
    # группа, роль, оклад, опоры, lead
    ("Руководство", "Основатели (CEO и партнёры)", 7_000, {1: 3}, False),
    ("Руководство", "Технический директор (CTO)", 12_500, {1: 1}, True),
    ("Руководство", "Руководитель Труда", 12_500, {1: 1}, True),
    ("Руководство", "Руководитель Личности, продюсер", 12_500, {2: 1}, True),
    ("Руководство", "Руководитель Капитала", 12_500, {2: 1}, True),
    ("Руководство", "Руководитель финансов и операций", 12_500, {3: 1}, True),

    ("Платформа", "ML- и ИИ-инженеры: агенты, модели", 6_000, {1: 2, 3: 4, 6: 12, 12: 16, 18: 17, 36: 20}, False),
    ("Платформа", "Бэкенд-разработчики", 5_000, {1: 2, 3: 4, 6: 11, 12: 13, 18: 14, 36: 16}, False),
    ("Платформа", "Фронтенд и фулстек", 4_500, {2: 1, 3: 2, 6: 6, 12: 7, 18: 7, 36: 8}, False),
    ("Платформа", "Интеграции с системами клиентов", 5_000, {3: 1, 6: 4, 12: 6, 18: 7, 36: 10}, False),
    ("Платформа", "DevOps и безопасность", 5_500, {2: 1, 6: 3, 12: 4, 18: 4, 36: 5}, False),
    ("Платформа", "Тестирование", 2_500, {3: 1, 6: 3, 12: 4, 18: 5, 36: 6}, False),

    ("Труд", "Продавцы в США и Европе", 9_000, {3: 1, 6: 3, 12: 5, 18: 7, 36: 7}, False),
    ("Труд", "Лидогенерация", 3_500, {4: 1, 6: 2, 12: 4, 18: 5, 36: 5}, False),
    ("Труд", "Внедрение у клиентов", 5_000, {3: 1, 6: 3, 12: 6, 18: 8, 36: 12}, False),
    ("Труд", "Сопровождение клиентов", 3_500, {6: 1, 12: 3, 18: 5, 36: 14}, False),

    ("Личность", "Продюсеры и шоураннеры", 4_500, {2: 1, 3: 2, 6: 3, 12: 4, 18: 4, 36: 4}, False),
    ("Личность", "Сценаристы", 3_000, {2: 1, 3: 1, 6: 3, 12: 4, 18: 4, 36: 4}, False),
    ("Личность", "Художники и аниматоры", 2_500, {2: 1, 3: 2, 6: 5, 12: 6, 18: 6, 36: 6}, False),
    ("Личность", "Монтаж и звук", 2_500, {3: 1, 6: 2, 12: 3, 18: 3, 36: 3}, False),
    ("Личность", "Комьюнити и соцсети", 2_500, {3: 1, 6: 2, 12: 3, 18: 3, 36: 5}, False),
    ("Личность", "Партнёрства с брендами", 5_000, {4: 1, 6: 1, 12: 2, 18: 3, 36: 3}, False),
    ("Личность", "Маркетинг подписки", 4_000, {8: 1, 12: 2, 18: 3, 36: 3}, False),

    ("Капитал", "Разработчики биллинга", 5_500, {3: 1, 6: 3, 12: 5, 18: 6, 36: 7}, False),
    ("Капитал", "Интеграции с платформами агентов", 4_500, {4: 1, 6: 1, 12: 2, 18: 3, 36: 3}, False),
    ("Капитал", "Поддержка клиентов", 2_500, {9: 1, 12: 1, 18: 2, 36: 4}, False),

    ("Общие", "Финансы и бухгалтерия", 4_000, {3: 1, 6: 2, 12: 3, 18: 3, 36: 4}, False),
    ("Общие", "Юрист", 6_000, {6: 1, 18: 2, 36: 2}, False),
    ("Общие", "Рекрутинг и HR", 3_000, {2: 1, 6: 3, 12: 3, 18: 2, 36: 2}, False),
    ("Общие", "Маркетинг группы и PR", 4_000, {4: 1, 12: 2, 36: 2}, False),
    ("Общие", "Администрирование", 2_000, {3: 1, 12: 2, 36: 2}, False),
]

# ─────────────────────────────────────────────────────────────────────
# СТАТЬИ РАСХОДОВ
# тип: monthly {месяц: $} — линейно/уровень; oneoff {месяц: $};
#      per_unit (драйвер, $ за единицу); pct (база выручки, доля)
# ─────────────────────────────────────────────────────────────────────

ITEMS = [
    # раздел, статья, тип, параметры, откуда
    ("Себестоимость", "Инференс моделей для клиентов Труда", "pct", ("labor_rec", 0.12), "допущение"),
    ("Себестоимость", "Проверка работы агентов людьми", "pct", ("labor_rec", 0.18), "допущение"),
    ("Себестоимость", "Комиссии магазинов и платёжных систем, подписка", "pct", ("subs_rev", 0.15), "допущение"),
    ("Себестоимость", "Хостинг и поддержка подписки", "pct", ("subs_rev", 0.10), "допущение"),
    ("Себестоимость", "Производство под бренды", "pct", ("brand_rev", 0.40), "допущение"),
    ("Себестоимость", "Инфраструктура биллинга, Капитал", "pct", ("cap_rev", 0.15), "допущение"),

    ("Софт и инфраструктура", "Облако и хостинг", "monthly", {1: 1_000, 6: 8_000, 12: 15_000, 18: 20_000, 36: 30_000}, "допущение"),
    ("Софт и инфраструктура", "Модели ИИ для разработки и своих агентов", "monthly", {1: 3_000, 6: 10_000, 18: 15_000, 36: 20_000}, "допущение"),
    ("Софт и инфраструктура", "Инструменты на сотрудника", "per_unit", ("fte", "tools_per_head"), "допущение"),
    ("Софт и инфраструктура", "Генерация видео и голоса, Личность", "monthly", {2: 5_000, 9: 15_000, 18: 20_000, 36: 25_000}, "допущение"),

    ("Юрлица и финансы", "Регистрация группы и юрлиц в США и ЕС", "oneoff", {2: 40_000}, "90-day-plan: оформить в первом квартале"),
    ("Юрлица и финансы", "Обслуживание юрлиц, бухгалтерия, аудит", "monthly", {3: 8_000, 12: 12_000, 36: 15_000}, "допущение"),
    ("Юрлица и финансы", "Внешние юристы: контракты, права", "monthly", {1: 5_000, 6: 10_000}, "допущение"),
    ("Юрлица и финансы", "Права на персонажей и товарные знаки", "oneoff", {4: 18_000, 12: 6_000, 24: 6_000}, "допущение"),
    ("Юрлица и финансы", "Сертификация безопасности SOC 2", "oneoff", {9: 60_000, 21: 30_000, 33: 30_000}, "допущение: требование корпоративных клиентов"),
    ("Юрлица и финансы", "Страхование ответственности и киберрисков", "monthly", {6: 3_000, 36: 5_000}, "допущение"),

    ("Маркетинг и продажи", "Реклама подписки Личности", "per_unit", ("visits", 0.20), "допущение: $0,20 за визит"),
    ("Маркетинг и продажи", "Маркетинг Труда: кейсы, контент, мероприятия", "per_unit", ("labor_adds", 5_000), "допущение: $5 тыс. на компанию"),
    ("Маркетинг и продажи", "Маркетинг Капитала", "per_unit", ("cap_adds", 300), "допущение"),
    ("Маркетинг и продажи", "Комиссии продажам Труда", "per_unit", ("labor_new_acv", 0.10), "допущение: 10% годового контракта"),
    ("Маркетинг и продажи", "Конференции и командировки", "monthly", {4: 10_000, 12: 20_000, 36: 25_000}, "допущение"),
    ("Маркетинг и продажи", "Сайт и бренд группы", "oneoff", {3: 30_000}, "допущение"),
    ("Маркетинг и продажи", "Поддержка сайта и бренда", "monthly", {4: 2_000}, "допущение"),
]

SCENARIOS = {"консервативный": 0.60, "базовый": 1.00, "оптимистичный": 1.35}

# ─────────────────────────────────────────────────────────────────────
# ДВИЖОК
# ─────────────────────────────────────────────────────────────────────


def flow(anchors, months=MONTHS):
    """Ряд по месяцам: линейно между опорами, ноль до первой, уровень после последней."""
    pts = sorted(anchors.items())
    out = [0.0] * (months + 1)
    for (m0, v0), (m1, v1) in zip(pts, pts[1:]):
        for m in range(m0, m1 + 1):
            out[m] = v0 + (v1 - v0) * (m - m0) / (m1 - m0)
    last_m, last_v = pts[-1]
    for m in range(last_m, months + 1):
        out[m] = last_v
    return out


def xround(x):
    """Округление до целого как у ROUND в Excel: половина — вверх."""
    return float(math.floor(x + 0.5))


def whole(xs):
    return [xround(x) for x in xs]


def stock(adds, churn):
    """База: прошлый месяц минус ушедшие (целое число) плюс новые."""
    out = [0.0] * len(adds)
    for m in range(1, len(adds)):
        out[m] = out[m - 1] - xround(out[m - 1] * churn) + adds[m]
    return out


def solve(f, target, lo=0.0, hi=1e8):
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return hi


def fit_flow(anchors, fits, churn, conversion=1.0):
    a = dict(anchors)
    for anchor_m, target_m, target in fits:
        later = [k for k, v in a.items() if v is None and k != anchor_m]

        def base_at(v, anchor_m=anchor_m, target_m=target_m, later=later):
            trial = dict(a)
            trial[anchor_m] = v
            for k in later:
                trial[k] = v
            return stock(whole(x * conversion for x in flow(trial)), churn)[target_m]

        a[anchor_m] = solve(base_at, target)
    return a


def oneoff(d, months=MONTHS):
    out = [0.0] * (months + 1)
    for m, v in d.items():
        out[m] = float(v)
    return out


def build(L, scale=1.0, roster=None, items=None):
    roster = ROSTER if roster is None else roster
    items = ITEMS if items is None else items
    N = MONTHS + 1
    r = {}

    # ── Выручка ─────────────────────────────────────────────────────
    r["labor_anchors"] = fit_flow(L["labor_flow"], L["labor_fit"], L["labor_churn"])
    r["labor_adds"] = whole(x * scale for x in flow(r["labor_anchors"]))
    r["labor_base"] = stock(r["labor_adds"], L["labor_churn"])
    r["labor_arpa"] = flow(L["labor_arpa"])
    r["labor_rec"] = [r["labor_base"][m] * r["labor_arpa"][m] for m in range(N)]
    r["pilots"] = [float(L["pilots"].get(m, 0)) for m in range(N)]
    r["pilot_rev"] = [r["pilots"][m] * L["pilot_price"] for m in range(N)]
    r["labor_new_acv"] = [r["labor_adds"][m] * r["labor_arpa"][m] * 12 for m in range(N)]

    r["ident_anchors"] = fit_flow(L["ident_visits"], L["ident_fit"], L["ident_churn"], L["ident_conversion"])
    r["visits"] = whole(x * scale for x in flow(r["ident_anchors"]))
    r["subs_adds"] = whole(v * L["ident_conversion"] for v in r["visits"])
    r["subs"] = stock(r["subs_adds"], L["ident_churn"])
    r["subs_rev"] = [s * L["ident_price"] for s in r["subs"]]
    r["brand_deals"] = whole(x * scale for x in flow(L["brand_flow"]))
    r["brand_rev"] = [d * L["brand_check"] for d in r["brand_deals"]]

    r["cap_anchors"] = fit_flow(L["cap_flow"], L["cap_fit"], L["cap_churn"])
    r["cap_adds"] = whole(x * scale for x in flow(r["cap_anchors"]))
    r["cap_base"] = stock(r["cap_adds"], L["cap_churn"])
    r["cap_arpa"] = flow(L["cap_arpa"])
    r["cap_rev"] = [r["cap_base"][m] * r["cap_arpa"][m] for m in range(N)]

    r["revenue"] = [r["labor_rec"][m] + r["pilot_rev"][m] + r["subs_rev"][m] + r["brand_rev"][m] + r["cap_rev"][m]
                    for m in range(N)]
    r["arr"] = [(r["labor_rec"][m] + r["subs_rev"][m] + r["cap_rev"][m]) * 12 for m in range(N)]

    # ── Штат ────────────────────────────────────────────────────────
    r["roles"] = []
    fte = [0.0] * N
    payroll = [0.0] * N
    recruiting = [0.0] * N
    for group, role, salary, anchors, lead in roster:
        count = whole(flow(anchors))
        cost = [count[m] * salary * L["salary_scale"] for m in range(N)]
        hires = [max(0.0, count[m] - count[m - 1]) if m else 0.0 for m in range(N)]
        rec = [hires[m] * (L["hire_cost_lead"] if lead else L["hire_cost"]) for m in range(N)]
        r["roles"].append({"group": group, "role": role, "salary": salary, "lead": lead,
                           "count": count, "cost": cost, "hires": hires, "recruiting": rec})
        for m in range(N):
            fte[m] += count[m]
            payroll[m] += cost[m]
            recruiting[m] += rec[m]
    r["fte"] = fte
    r["payroll"] = payroll
    r["payroll_tax"] = [p * L["payroll_tax"] for p in payroll]
    r["recruiting"] = recruiting

    # ── Статьи ──────────────────────────────────────────────────────
    drivers = {"fte": fte, "visits": r["visits"], "labor_adds": r["labor_adds"],
               "cap_adds": r["cap_adds"], "labor_new_acv": r["labor_new_acv"]}
    r["items"] = []
    for section, name, kind, params, src in items:
        if kind == "monthly":
            vals = flow(params)
        elif kind == "oneoff":
            vals = oneoff(params)
        elif kind == "per_unit":
            driver, rate = params
            rate = L[rate] if isinstance(rate, str) else rate
            vals = [drivers[driver][m] * rate for m in range(N)]
        elif kind == "pct":
            base, share = params
            vals = [r[base][m] * share for m in range(N)]
        vals[0] = 0.0
        r["items"].append({"section": section, "name": name, "kind": kind, "params": params, "vals": vals})

    def section_sum(sec):
        return [sum(it["vals"][m] for it in r["items"] if it["section"] == sec) for m in range(N)]

    r["cogs"] = section_sum("Себестоимость")
    r["gross"] = [r["revenue"][m] - r["cogs"][m] for m in range(N)]
    r["sec"] = {s: section_sum(s) for s in ("Софт и инфраструктура", "Юрлица и финансы", "Маркетинг и продажи")}
    before_unexp = [r["cogs"][m] + payroll[m] + r["payroll_tax"][m] + recruiting[m]
                    + sum(v[m] for v in r["sec"].values()) for m in range(N)]
    r["unexpected"] = [before_unexp[m] * L["unexpected"] for m in range(N)]
    r["costs"] = [before_unexp[m] + r["unexpected"][m] for m in range(N)]
    r["opex"] = [r["costs"][m] - r["cogs"][m] for m in range(N)]
    r["ebitda"] = [r["revenue"][m] - r["costs"][m] for m in range(N)]

    cum = [0.0] * N
    cash = [0.0] * N
    cash[0] = L["raise_total"]
    for m in range(1, N):
        cum[m] = cum[m - 1] + r["ebitda"][m]
        cash[m] = cash[m - 1] + r["ebitda"][m]
    r["cum"] = cum
    r["cash"] = cash
    r["free"] = [max(0.0, e) for e in r["ebitda"]]
    r["to_growth"] = [f * L["to_growth"] for f in r["free"]]
    r["to_dividends"] = [f * L["to_dividends"] for f in r["free"]]

    def valuation(m):
        t12 = sum(r["brand_rev"][max(1, m - 11):m + 1])
        return (r["labor_rec"][m] * 12 * L["mult_labor"] + r["cap_rev"][m] * 12 * L["mult_cap"]
                + r["subs_rev"][m] * 12 * L["mult_subs"] + t12 * L["mult_brand"])
    r["valuation"] = [valuation(m) if m else 0.0 for m in range(N)]
    return r


def summary(r):
    N = MONTHS + 1
    be = next((m for m in range(1, N) if all(r["ebitda"][k] >= 0 for k in range(m, N))), None)
    pit_m = min(range(1, N), key=lambda m: r["cum"][m])
    payback = next((m for m in range(pit_m, N) if r["cum"][m] >= 0), None)
    years = []
    for y in range(MONTHS // 12):
        ms = range(12 * y + 1, 12 * y + 13)
        yy = {k: sum(r[k][m] for m in ms) for k in
              ("labor_rec", "pilot_rev", "subs_rev", "brand_rev", "cap_rev", "revenue", "cogs", "gross",
               "payroll", "payroll_tax", "recruiting", "unexpected", "opex", "costs", "ebitda")}
        for s, v in r["sec"].items():
            yy[s] = sum(v[m] for m in ms)
        yy["cash_end"] = r["cash"][12 * y + 12]
        yy["fte_end"] = r["fte"][12 * y + 12]
        years.append(yy)
    return {"breakeven": be, "pit": r["cum"][pit_m], "pit_m": pit_m, "payback": payback,
            "low_cash": min(r["cash"][1:]), "years": years}


# ─────────────────────────────────────────────────────────────────────
# ФОРМАТ
# ─────────────────────────────────────────────────────────────────────

def mln(x):
    return f"{x / 1e6:,.1f}".replace(",", " ").replace(".", ",")


def tys(x):
    return f"{x / 1e3:,.0f}".replace(",", " ")


def plural(n, one, few, many):
    n = abs(round(n))
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def num(x):
    return f"{round(x):,}".replace(",", " ")


def pct(x):
    return f"{x * 100:.0f}%"


def dec(x, digits=1):
    return f"{x:.{digits}f}".replace(".", ",")


# ─────────────────────────────────────────────────────────────────────
# ОТЧЁТ
# ─────────────────────────────────────────────────────────────────────

def main():
    L = BASE
    runs = {n: build(L, s) for n, s in SCENARIOS.items()}
    sums = {n: summary(r) for n, r in runs.items()}
    b, sb = runs["базовый"], sums["базовый"]
    Y = sb["years"]
    stages_total = sum(t for _, _, t in L["stages"])
    stage_scale = solve(lambda k: sum(build({**L, "salary_scale": k})["costs"][1:19]), stages_total, 0.5, 6.0)
    stage_scale = round(stage_scale, 1)
    avg18 = b["payroll"][18] / b["fte"][18]
    out = []
    w = out.append

    w("# Финмодель WIF · бюджет на 36 месяцев\n")
    w("Устроена по образцу референса: штат по ролям с окладами и месяцами найма,\n"
      "каждая статья расходов отдельной строкой, бюджет М1…М36 с итогом, внизу\n"
      "денежный поток и накопленный поток. Главное — сколько денег реально нужно\n"
      "(глубина ямы) и когда они возвращаются. Оценка — промежуточный вывод.\n")
    w("Книга с формулами — `finmodel-wif.xlsx`, главный лист «Бюджет». Генератор —\n"
      "`_finmodel_wif.py`: штат, статьи и рычаги вверху файла.\n")
    w("---\n")

    # ── главное ─────────────────────────────────────────────────────
    w("## Главное\n")
    worst_pit = -summary(build({**L, "salary_scale": stage_scale,
                                "labor_arpa": {6: 5_000, 18: 10_000, 36: 10_000}}, 0.6))["pit"]
    pit_stage = -summary(build({**L, "salary_scale": stage_scale}))["pit"]
    w(f"- **Яма — {mln(-sb['pit'])} млн $** при окладах распределённой команды, как в "
      f"референсе. Столько бизнес тратит сверх заработанного до разворота: минимум "
      f"накопленного потока на {sb['pit_m']}-м месяце, окупается к {sb['payback']}-му.")
    w(f"- **Размер ямы определяют оклады, а не план продаж.** Бюджет этапов в деке "
      f"($42 млн на 18 месяцев) получается при окладах ×{dec(stage_scale)} к референсу — "
      f"около ${num(avg18 * stage_scale * 12 / 1000)} тыс. в год на человека. Похоже, исходная "
      f"модель считала по ставке США и Европы всю команду, а не только пятерых руководителей. "
      f"При таких окладах яма — {mln(pit_stage)} млн $.")
    w(f"- **Из $50 млн реально нужно от {mln(-sb['pit'])} до {mln(pit_stage)} млн** в "
      f"зависимости от того, где нанимаем, и {mln(worst_pit)} млн в худшем сочетании: оклады "
      f"США, чек $10 тыс. вместо $15 тыс., продажи 60% плана. Это отвечает на вопрос Дмитрия "
      f"с разбора 14.09, что сумма гибкая.")
    w(f"- **Устойчивый плюс с {sb['breakeven']}-го месяца.** За третий год выручка "
      f"{mln(Y[2]['revenue'])} млн $, денежный поток {mln(Y[2]['ebitda'])} млн $ — "
      f"{pct(Y[2]['ebitda'] / Y[2]['revenue'])} выручки, до налогов.")
    w(f"- **Штат {num(b['fte'][3])} → {num(b['fte'][6])} → {num(b['fte'][18])} → "
      f"{num(b['fte'][36])} человек** (мес. 3, 6, 18, 36), {len(ROSTER)} "
      f"{plural(len(ROSTER), 'роль', 'роли', 'ролей')}, средний оклад к 18-му месяцу "
      f"${num(avg18)} в месяц.\n")

    # ── годовой бюджет ──────────────────────────────────────────────
    w("## Бюджет по годам · базовый сценарий\n")
    w("Тыс. $.\n")
    w("| | Год 1 | Год 2 | Год 3 | Итого |")
    w("|---|---|---|---|---|")

    def row(label, fn, bold=False):
        vals = [fn(y) for y in Y]
        cells = [tys(v) for v in vals] + [tys(sum(vals))]
        lab = f"**{label}**" if bold else label
        w(f"| {lab} | " + " | ".join(cells) + " |")

    row("Выручка", lambda y: y["revenue"], True)
    row("   Труд", lambda y: y["labor_rec"] + y["pilot_rev"])
    row("   Личность: подписка", lambda y: y["subs_rev"])
    row("   Личность: бренды", lambda y: y["brand_rev"])
    row("   Капитал", lambda y: y["cap_rev"])
    row("Расходы", lambda y: y["costs"], True)
    row("   Себестоимость", lambda y: y["cogs"])
    row("   ФОТ", lambda y: y["payroll"])
    row("   Налоги и взносы на ФОТ", lambda y: y["payroll_tax"])
    row("   Найм", lambda y: y["recruiting"])
    for s in ("Софт и инфраструктура", "Юрлица и финансы", "Маркетинг и продажи"):
        row(f"   {s}", lambda y, s=s: y[s])
    row("   Непредвиденные", lambda y: y["unexpected"])
    row("Денежный поток", lambda y: y["ebitda"], True)
    w("| Накопленный поток на конец года | " + " | ".join(tys(b["cum"][12 * (i + 1)]) for i in range(3)) + " | |")
    w("| Деньги на счету на конец года | " + " | ".join(tys(y["cash_end"]) for y in Y) + " | |")
    w("| Штат на конец года | " + " | ".join(num(y["fte_end"]) for y in Y) + " | |")
    w("")

    # ── штат ────────────────────────────────────────────────────────
    w("## Штат\n")
    w("Оклад — полная месячная стоимость человека до налогов на ФОТ. Уровни — как в\n"
      "референсе для распределённой команды; руководители направлений — по roles.md.\n"
      "Состав подобран под опоры стратегии: 25–40 человек к 3-му месяцу, 70+ и 40+\n"
      "инженеров к 6-му, 130–140 к 18-му.\n")
    w("| Группа | Роль | Оклад, $ | Мес. 3 | Мес. 6 | Мес. 12 | Мес. 18 | Мес. 36 |")
    w("|---|---|---|---|---|---|---|---|")
    for ro in b["roles"]:
        w(f"| {ro['group']} | {ro['role']} | {num(ro['salary'])} | " +
          " | ".join(num(ro["count"][m]) for m in (3, 6, 12, 18, 36)) + " |")
    w("| | **Всего** | | " + " | ".join(f"**{num(b['fte'][m])}**" for m in (3, 6, 12, 18, 36)) + " |")
    w("")

    # ── статьи ──────────────────────────────────────────────────────
    w("## Статьи расходов, кроме штата\n")
    w("| Раздел | Статья | Как считается | Итого за 36 мес., тыс. $ |")
    w("|---|---|---|---|")
    for it, (_, _, kind, params, src) in zip(b["items"], ITEMS):
        if kind == "pct":
            how = f"{pct(params[1])} от выручки"
        elif kind == "per_unit":
            rate = L[params[1]] if isinstance(params[1], str) else params[1]
            unit = {"fte": "на человека в мес.", "visits": "за визит", "labor_adds": "на новую компанию",
                    "cap_adds": "на новую компанию", "labor_new_acv": "годового контракта"}[params[0]]
            how = f"{pct(rate)} {unit}" if rate < 1 and params[0] == "labor_new_acv" else f"${dec(rate, 2) if rate < 1 else num(rate)} {unit}"
        elif kind == "oneoff":
            how = "разово: " + ", ".join(f"мес. {m} — ${num(v)}" for m, v in params.items())
        else:
            pts = sorted(params.items())
            how = f"${num(pts[0][1])} → ${num(pts[-1][1])} в мес."
        w(f"| {it['section']} | {it['name']} | {how} | {tys(sum(it['vals']))} |")
    w(f"| Штат | Налоги и взносы на ФОТ | {pct(L['payroll_tax'])} от ФОТ | {tys(sum(b['payroll_tax']))} |")
    w(f"| Штат | Найм | ${num(L['hire_cost_lead'])} на руководителя, ${num(L['hire_cost'])} на остальных | {tys(sum(b['recruiting']))} |")
    w(f"| Прочее | Непредвиденные | {pct(L['unexpected'])} от всех расходов | {tys(sum(b['unexpected']))} |")
    w("")

    # ── сценарии ────────────────────────────────────────────────────
    w("## Сценарии\n")
    w("Масштабируют поток новых клиентов на весь срок. Штат и постоянные статьи — по\n"
      "плану, переменные (себестоимость, реклама, комиссии) идут за выручкой.\n")
    w("| | консервативный | базовый | оптимистичный |")
    w("|---|---|---|---|")
    for label, fn in [
        ("Яма, млн $", lambda r, s: f"{mln(-s['pit'])} (мес. {s['pit_m']})"),
        ("Окупается к месяцу", lambda r, s: str(s["payback"]) if s["payback"] else "нет за 36 мес."),
        ("Устойчивый плюс с месяца", lambda r, s: str(s["breakeven"]) if s["breakeven"] else "нет за 36 мес."),
        ("Выручка год 3, млн $", lambda r, s: mln(s["years"][2]["revenue"])),
        ("Денежный поток год 3, млн $", lambda r, s: mln(s["years"][2]["ebitda"])),
        ("ARR к 36-му месяцу, млн $", lambda r, s: mln(r["arr"][MONTHS])),
    ]:
        w(f"| {label} | " + " | ".join(fn(runs[n], sums[n]) for n in SCENARIOS) + " |")
    w("")

    # ── чувствительность ────────────────────────────────────────────
    w("## Что, если ошибаемся\n")
    w("Одно допущение против базового сценария, остальное как было.\n")
    w("| Что, если | Яма, млн $ | Окупается к месяцу | Поток год 3, млн $ |")
    w("|---|---|---|---|")
    res = []

    def variant(label, **ch):
        rv = build({**L, **ch})
        sv = summary(rv)
        w(f"| {label} | {mln(-sv['pit'])} | {sv['payback'] or 'нет за 36'} | {mln(sv['years'][2]['ebitda'])} |")
        res.append((label, sv))

    visit_050 = [(s, n, k, (p[0], 0.50) if n == "Реклама подписки Личности" else p, src)
                 for s, n, k, p, src in ITEMS]
    arpa_10 = {6: 5_000, 18: 10_000, 36: 10_000}
    variants = [
        ("Базовый сценарий", {}, 1.0, None),
        ("Оклады ×2", {"salary_scale": 2.0}, 1.0, None),
        (f"Оклады ×{dec(stage_scale)} — уровень бюджета этапов деки", {"salary_scale": stage_scale}, 1.0, None),
        ("Чек Труда $10 тыс., а не $15 тыс.", {"labor_arpa": arpa_10}, 1.0, None),
        ("Отток Труда 2%, а не 1%", {"labor_churn": 0.02}, 1.0, None),
        ("Визит в Личности $0,50, а не $0,20", {}, 1.0, visit_050),
        ("Продажи 60% от плана", {}, 0.6, None),
        ("Продажи 30% от плана", {}, 0.3, None),
        (f"Всё плохое: оклады ×{dec(stage_scale)}, чек $10 тыс., продажи 60%",
         {"salary_scale": stage_scale, "labor_arpa": arpa_10}, 0.6, None),
    ]
    for label, ch, sc_k, its in variants:
        sv = summary(build({**L, **ch}, sc_k, items=its))
        res.append((label, sv))
        w(f"| {label} | {mln(-sv['pit'])} | {sv['payback'] or 'нет за 36'} | {mln(sv['years'][2]['ebitda'])} |")
    worst = res[-1][1]
    w("")
    if -worst["pit"] <= L["raise_total"]:
        w(f"Даже в худшем сочетании яма — {mln(-worst['pit'])} млн $, в пределах $50 млн. "
          f"Раунд такого размера покрывает не выживание, а одновременную ошибку в окладах, "
          f"чеке и продажах.\n")
    else:
        w(f"В худшем сочетании яма — {mln(-worst['pit'])} млн $, больше $50 млн: такой "
          f"сценарий раунд не покрывает.\n")

    # ── оценка ──────────────────────────────────────────────────────
    w("## Оценка как промежуточный результат\n")
    w(f"ARR направлений × мультипликатор: Труд и Капитал {dec(L['mult_labor'], 0)}×, подписка "
      f"{dec(L['mult_subs'], 0)}×, бренды {dec(L['mult_brand'])}× выручки за год. Допущение — "
      f"проверить по сделкам-аналогам.\n")
    w("| Месяц | ARR, млн $ | Оценка, млн $ | Для $1 млрд нужно |")
    w("|---|---|---|---|")
    for m in (12, 18, 24, 36):
        w(f"| {m} | {mln(b['arr'][m])} | {mln(b['valuation'][m])} | {dec(1e9 / b['arr'][m])}× ARR |")
    w("")

    # ── сверка ──────────────────────────────────────────────────────
    w("## Сверка со стратегией\n")
    checks = [
        ("Штат к 3-му месяцу", "25–40", num(b["fte"][3]), 25 <= b["fte"][3] <= 40),
        ("Штат к 6-му месяцу", "70+", num(b["fte"][6]), b["fte"][6] >= 70),
        ("Инженеров к 6-му месяцу", "40+", num(sum(ro["count"][6] for ro in b["roles"]
                                                   if ro["group"] == "Платформа") + 1), None),
        ("Штат к 18-му месяцу", "130–140", num(b["fte"][18]), 130 <= b["fte"][18] <= 140),
        ("ARR к 18-му месяцу", "$42 млн", f"{mln(b['arr'][18])} млн $", abs(b["arr"][18] - 42e6) < 1.5e6),
        ("Труд: компаний к 18-му", "157", num(b["labor_base"][18]), abs(b["labor_base"][18] - 157) <= 5),
        ("Капитал: компаний к 18-му", "256", num(b["cap_base"][18]), abs(b["cap_base"][18] - 256) <= 10),
        ("Личность: подписчиков к 18-му", "63 500", num(b["subs"][18]), abs(b["subs"][18] - 63_500) <= 2_000),
        ("Расходы за 18 месяцев", "$42 млн (этапы деки)", f"{mln(sum(b['costs'][1:19]))} млн $",
         abs(sum(b["costs"][1:19]) - 42e6) < 5e6),
        ("Деньги на счету к 18-му", "$21 млн", f"{mln(b['cash'][18])} млн $", abs(b["cash"][18] - 21e6) < 3e6),
    ]
    eng6 = sum(ro["count"][6] for ro in b["roles"] if ro["group"] == "Платформа") + 1
    checks[2] = ("Инженеров к 6-му месяцу, с CTO", "40+", num(eng6), eng6 >= 40)
    w("| Что | В стратегии | В модели | Сходится |")
    w("|---|---|---|---|")
    for n, p, g, ok in checks:
        w(f"| {n} | {p} | {g} | {'да' if ok else '**нет**'} |")
    w("")
    spend18 = sum(b["costs"][1:19])
    w(f"**Главное расхождение — расходы.** При окладах распределённой команды 18 месяцев стоят "
      f"{mln(spend18)} млн $ против {mln(stages_total)} млн $ в бюджете этапов, и на счету к "
      f"18-му месяцу {mln(b['cash'][18])} млн $ вместо $21 млн. Бюджет этапов сходится при "
      f"окладах ×{dec(stage_scale)} — это средняя полная стоимость около "
      f"${num(avg18 * stage_scale * 12 / 1000)} тыс. в год на человека, уровень найма в США "
      f"и Европе. Это решение, а не ошибка счёта: где нанимаем команду, определяет и размер "
      f"раунда.\n")
    w(f"**Капитал и Личность** расходятся со стратегией так же, как в прошлой версии: поток "
      f"новых компаний Капитала даёт {num(b['cap_base'][18])} вместо 256 (сходится при оттоке "
      f"около 4,7%), 1,6 млн визитов дают {num(b['subs'][18])} подписчиков вместо 63,5 тыс.\n")

    # ── помесячно ───────────────────────────────────────────────────
    w("## Приложение: помесячно\n")
    w("Тыс. $; накопленный поток и касса — млн $.\n")
    w("| Мес. | Штат | Выручка | Расходы | Поток | Накопленный | Касса |")
    w("|---|---|---|---|---|---|---|")
    for m in range(1, MONTHS + 1):
        w(f"| {m} | {num(b['fte'][m])} | {tys(b['revenue'][m])} | {tys(b['costs'][m])} | "
          f"{tys(b['ebitda'][m])} | {mln(b['cum'][m])} | {mln(b['cash'][m])} |")
    w("")

    (HERE / "finmodel-wif.md").write_text("\n".join(out), encoding="utf-8")
    print("finmodel-wif.md записан")
    print(f"штат м3/м6/м12/м18/м36: {[num(b['fte'][m]) for m in (3, 6, 12, 18, 36)]}; "
          f"ФОТ м18 {tys(b['payroll'][18])} тыс., средний оклад {num(b['payroll'][18] / b['fte'][18])}")
    print(f"яма {mln(sb['pit'])} млн (мес. {sb['pit_m']}), окупается к {sb['payback']}, плюс с {sb['breakeven']}")
    for i, y in enumerate(Y, 1):
        print(f"  год {i}: выручка {mln(y['revenue'])}, расходы {mln(y['costs'])}, поток {mln(y['ebitda'])}, касса {mln(y['cash_end'])}")
    print(f"  расходы 18 мес {mln(spend18)} (этапы 42,0); касса м18 {mln(b['cash'][18])}")
    for n in SCENARIOS:
        s = sums[n]
        print(f"  {n}: яма {mln(s['pit'])} (м{s['pit_m']}), окупается {s['payback']}, плюс с {s['breakeven']}")
    print(f"  оклады ×2: яма {mln(summary(build({**L, 'salary_scale': 2.0}))['pit'])}")


if __name__ == "__main__":
    main()
