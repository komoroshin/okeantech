# 01. B2B-дистрибуция промтоваров/MRO/электрики/сантехники/стройматериалов — quote-to-order

Дата: 2026-09-10. Все цифры — с источником; «не найдено» = источник не обнаружен.

## 1. Повторяющаяся работа

**Роли:** inside sales rep, customer service rep (CSR), order entry / order clerk, quoting specialist. **Задачи:** принять заказ/запрос (PO в PDF, письмо, Excel, голос), найти позиции в каталоге (часто по описанию, без артикула), подобрать замену, применить клиентскую цену, завести заказ/котировку в ERP, подтвердить клиенту, отработать исключения EDI.

**Каналы:** email/PDF/Excel, телефон и голосовая почта, факс, рукописные заявки, EDI-исключения, порталы — перечень каналов у Canals ([canals.ai/products/distributor-order-entry](https://www.canals.ai/products/distributor-order-entry), б/д) и Ordermatic ([ordermatic.co](https://ordermatic.co/), б/д). Доли каналов: **не найдено** (опрос с разбивкой email/EDI/портал не обнаружен).

**Объёмы:** 50-строчный заказ — 10 мин, до 40 кликов и 10 экранов; теоретический максимум 48 заказов/смену на CSR ([DSG, 2023-08-09](https://distributionstrategy.com/transform-distributor-order-entry-with-ai/)). Бенчмарк Esker по «сотням» служб клиентского сервиса: ручная обработка 11 мин/заказ, ошибки 9%, автоматизация — 3 мин и <1%, средняя доля «безконтактных» заказов 67%, лучшие >90% ([Esker, 2025-09-23](https://www.esker.com/blog/customer-service/how-order-management-benchmarks-can-guide-smarter-business-decisions/)). Индустриальный базис WizCommerce: 20 мин и $10–12 на заказ, у среднего дистрибьютора $250–550 тыс./год на ручной ввод ([GlobeNewswire, 2026-05-28](https://www.globenewswire.com/news-release/2026/05/28/3303038/0/en/WizCommerce-launches-Ella-an-AI-order-entry-tool-that-processes-distributor-POs-in-under-2-minutes.html)). Пример Conexiom: 15 заказов/день × 10 мин = 12,5 ч/нед на CSR ([Conexiom, 2025-07-15](https://conexiom.com/blog/measuring-the-roi-of-order-automation-what-to-track-and-why)).

**Что уже автоматизируют:** ввод заказов из email/PDF (Conexiom, Esker — 10+ лет), с 2024–2026 — котировки по описанию, подбор замен, голосовые заказы (Canals, Proton, Prokeep, WizCommerce). По опросу DSG (233 руководителя, Q1 2026): 93% считают ИИ стратегическим приоритетом, но лишь 16% внедрили в несколько функций ([DSG, 2026-09-09](http://distributionstrategy.com/2026/09/ai-top-25-reveals-a-wide-execution-gap-across-wholesale-distribution/)). NAW: автоматизация заказов внедрена у 60%, прайсинг/котировки — 34% ([naw.org/ai-in-distribution](https://www.naw.org/ai-in-distribution/), дата не указана).

## 2. Люди и их стоимость

| Роль (BLS OEWS, май 2022) | США всего | В оптовой торговле (NAICS 42) | В durable goods (423) |
|---|---|---|---|
| CSR 43-4051 | 2 879 840; ср. $41 190 | 180 370 (3,09% занятых), ср. $46 420 | 107 130 (3,33%), ср. $46 610 |
| Order clerks 43-4151 | 113 500; ср. $40 540 | 29 870 (0,51%), $42 810 | 17 410 (0,54%), $44 280 |
| Sales reps 41-4012 | 1 273 400; ср. $76 890 | 816 040 (13,97%), $76 440 | 425 780 (13,22%), $75 000 |

Источники: [oes434051](https://blsmon1.bls.gov/oes/current/oes434051.htm), [oes434151](https://blsmon1.bls.gov/oes/current/oes434151.htm), [oes414012](https://blsmon1.bls.gov/oes/current/oes414012.htm), [naics2_42](https://blsmon1.bls.gov/oes/current/naics2_42.htm), [naics3_423000](https://blsmon1.bls.gov/oes/current/naics3_423000.htm) (зеркало BLS, данные May 2022). Медианы May 2025: CSR $44 770 (занятость 2024 — 2 814 000), order clerks $46 170 (89 500), sales reps $72 080 (1 310 500) — [O*NET по данным BLS 2025](https://www.onetonline.org/link/summary/43-4051.00), [43-4151](https://www.onetonline.org/link/summary/43-4151.00), [41-4012](https://www.onetonline.org/link/summary/41-4012.00). Занятость CSR May 2025 по API BLS: 2 595 750 ([api.bls.gov, серия OEUN000000000000043405101](https://api.bls.gov/publicAPI/v2/timeseries/data/OEUN000000000000043405101)).

**Полная стоимость:** льготы — 30,1% компенсации в частном секторе ([BLS ECEC, март 2026](https://www.bls.gov/news.release/ecec.nr0.htm)) → CSR в оптовике ≈ $46,4 тыс./0,699 ≈ **$66 тыс./год**, sales rep ≈ **$107 тыс.** Glassdoor: inside sales rep в Grainger — $105 089 общий доход, 131 анкета ([Glassdoor, янв. 2026](https://www.glassdoor.com/Salary/Grainger-Inside-Sales-Representative-Salaries-E711_D_KO9,36.htm)). **Германия:** Sachbearbeiter Vertriebsinnendienst — медиана €37 400 (2 824 вакансий, [StepStone 2026](https://www.stepstone.de/gehalt/Sachbearbeiter-in-Vertriebsinnendienst.html)); Vertriebsinnendienst €45 500 ([Glassdoor DE, июнь 2026](https://www.glassdoor.de/Geh%C3%A4lter/vertriebsinnendienst-gehalt-SRCH_KO0,20.htm)). **ЕС:** оптовая торговля G46 — 9 722 244 занятых, зарплаты €334 млрд (2023) ([Eurostat sbs_ovw_act](https://ec.europa.eu/eurostat/databrowser/view/sbs_ovw_act/)); доля CSR по ЕС — **не найдено**.

**Сколько у типичного дистрибьютора:** прямых данных **не найдено**; по долям BLS (423) на 200 сотрудников ≈ 7 CSR + 1 order clerk + 26 sales reps; на 1000 — ≈ 33 / 5 / 132. Пример: Sonepar USA (15 опер. компаний, 400+ филиалов) автоматизирует 200 000 строк/мес, экономя >1 000 часов/мес ≈ 6 FTE ([Conexiom PDF, создан 2023-01-09](https://conexiom.com/wp-content/uploads/2022/10/Sonepar.pdf)).

**Вывод по цене:** $5 тыс./мес = $60 тыс./год ≈ один загруженный CSR в США и ≈1,3 в Германии. Роль окупается только если закрывает ≥1,5–2 FTE.

## 3. Системы

- **Epicor Prophet 21** — >1 700 компаний; 41% из топ-50 дистрибьюторов ([top10erp, б/д](https://www.top10erp.org/blog/epicor-prophet-21)). **Epicor Eclipse** — >700 клиентов, 60 000 пользователей; электрика, сантехника, HVAC, PVF ([top10erp](https://www.top10erp.org/products/epicor-eclipse), б/д). **Infor SX.e** — 289 компаний ([Landbase, 2025](https://data.landbase.com/technology/infor-distribution-sx-e/)); Infor CloudSuite Distribution — число клиентов **не найдено**. Также SAP B1/S4, NetSuite, Dynamics, AS/400-самописы.
- Стандартизация средняя-высокая для целевого сегмента: Canals интегрируется с Eclipse, P21, Infor CSD/SX.e, SAP S/4, Dynamics; внедрение «меньше недели» для типовых ERP, до 30 дней для прочих ([canals.ai](https://www.canals.ai/products/distributor-order-entry)); Ordermatic — включая AS/400 и «зелёные экраны» ([ordermatic.co](https://ordermatic.co/)). Кейс Regency Supply (электрика, 5 филиалов, P21): 2 недели до запуска ([Canals, б/д](https://www.canals.ai/case-studies/regency-supply-faster-smarter-quoting)). 55% дистрибьюторов купили ERP/CRM/e-com/аналитику, но не интегрировали ([DSG, Q1 2026](https://distributionstrategy.com/report/state-of-distributor-technology-2026/)).

## 4. Конкуренты

| Игрок | Что делает | Деньги | Дата |
|---|---|---|---|
| **Conexiom** | ввод заказов email/PDF → ERP; Grainger, Sonepar, USESI | $130M от Warburg Pincus, всего $170M; >$100B транзакций/год | [2021-09-30](https://www.cbinsights.com/research/conexiom-private-equity-funding/) |
| **Esker** (публичная) | order management, 67% touchless | выручка 2024 €205,3M (+15%), SaaS 82% | [2025-01-14](https://www.esker.com/sites/default/files/press_releases/esker_q4_2024_jan_2025.pdf) |
| **Canals** (Майами, осн. 2023) | заказы, котировки, голос, AP/AR для дистрибьюторов; 100+ клиентов, 8 млн заказов/год | Series A $35M (Base10) | [2026-05-28](https://www.fifthrow.com/blog/ai-workflow-automation-raises-the-stakes-canals-35-m-funding-signals-a-new-era-for-outcome-driven-manufacturing-ventures) |
| **Prokeep** | мессенджинг + Order Engine (сток-чек, котировка, заказ); 8 500 локаций | Series A $25M (Dahlia) [2024-11-12](https://www.prnewswire.com/news-releases/prokeep-secures-25-million-in-series-a-funding-to-accelerate-growth-and-expand-its-demand-generation-capabilities-for-distributors-302300215.html); всего $34M ([CB Insights](https://www.cbinsights.com/company/prokeep)) | Order Engine — [2025-09-15](https://www.prokeep.com/prokeep-news/prokeep-launches-its-order-engine-simplifying-distribution-and-unlocking-more-orders) |
| **Proton.ai** | CRM для дистрибьюторов + Order & Quote Entry (GA) | Series A $20M (Felicis) [2022-01-18](https://www.mdm.com/news/operations/finance/proton-ai-closes-20m-in-funding/) | GA — [2026-07-21](https://distributionstrategy.com/2026/07/proton-ai-launches-ai-platform-to-automate-order-and-quote-entry-for-distributors/) |
| **WizCommerce Ella** | AI order entry, PO <2 мин | финансирование — не найдено | [2026-05-28](https://www.globenewswire.com/news-release/2026/05/28/3303038/0/en/WizCommerce-launches-Ella-an-AI-order-entry-tool-that-processes-distributor-POs-in-under-2-minutes.html) |
| **Ordermatic** (Кливленд) | order entry для промдистрибьюторов, legacy ERP | не найдено | [ordermatic.co](https://ordermatic.co/) |
| Также | Rossum, Workist (DE), Distro, Commerce Vision Lucy, Tungsten, Kodaris, StackCube | — | [WizCommerce, б/д](https://wizcommerce.com/blog/top-ai-order-entry-automation-software/), [StackCube, 2026-07-08](https://blog.stackcube.io/ai-order-entry-software-for-distributors) |

**Не в этой вертикали:** Pace — страхование ($46M Series B, [2026-05-27](https://fintech.global/2026/05/27/thrive-and-sequoia-back-pace-in-46m-series-b-round/)); Endgame — продажи SaaS ($47,5M, [Dealroom](https://app.dealroom.co/companies/endgame_3)); Ordergrid — фуд-ретейл/replenishment ([ordergrid.com](https://www.ordergrid.com/help-center)); Lumi AI — аналитика, $3,7M seed ([2025-03-27](https://theaiinsider.tech/2025/03/27/lumi-ai-secures-3-7m-seed-funding-to-redefine-data-analytics-for-brands-retailers-and-supply-chain/)); Pactum — переговоры с поставщиками, $54M Series C ([2025-06](https://pactum.com/blog/news-pactum-secures-54-million-in-series-c-funding-to-scale-agentic-ai-in-procurement)); Zoovu — product discovery, $169M ([2022-06-15](https://techcrunch.com/2022/06/15/zoovu-lands-169m-to-drive-online-product-discovery-experiences/)); Solidus — крипто/GPU, не релевантен.

**Плотность: крупные игроки с $50M+ (Conexiom, Esker) + 4 профильных стартапа с раундами/запусками в 2024–2026.** Публичных цен нет ни у кого ([StackCube, 2026-07-08](https://blog.stackcube.io/ai-order-entry-software-for-distributors)); Esker — подписка + плата за документ; Canals — usage-based tiers.

## 5. Доказательства оплаты

- Sonepar: 200 000 строк/мес, >1 000 ч/мес, 15 опер. компаний ([Conexiom PDF, 2023](https://conexiom.com/wp-content/uploads/2022/10/Sonepar.pdf)).
- Canals: Turtle — конверсия котировок 20% → 57%; Puget Sound Pipe — до 90% экономии времени на котировках; 59% меньше возвратов ([canals.ai](https://www.canals.ai/products/distributor-order-entry), б/д); 100+ платящих дистрибьюторов ([2026-05-28](https://www.fifthrow.com/blog/ai-workflow-automation-raises-the-stakes-canals-35-m-funding-signals-a-new-era-for-outcome-driven-manufacturing-ventures)).
- WizCommerce/Howard Elliott: ручной ввод с ~4 ч/день до ~15 мин ([2026-05-28](https://www.globenewswire.com/news-release/2026/05/28/3303038/0/en/WizCommerce-launches-Ella-an-AI-order-entry-tool-that-processes-distributor-POs-in-under-2-minutes.html)).
- Proton (PoV у промдистрибьютора): подбор товара по описанию в 3 раза точнее, подготовка списков −75% (не проверено независимо) ([DSG, 2026-07-21](https://distributionstrategy.com/2026/07/proton-ai-launches-ai-platform-to-automate-order-and-quote-entry-for-distributors/)).
- DSG: автоматизация заказов/котировок даёт рост продуктивности 25–70% ([DSG 2025 State of AI, PDF, 2025-03](https://distributionstrategy.com/wp-content/uploads/2025/03/DSG-Report-The-2025-State-of-AI-in-Distribution.pdf)).
- Публичные цены: **не найдено**.

## 6. Размер и доступ к покупателю

**США (SUSB 2022, фирмы с 50–1 999 сотрудников):** вся оптовая торговля NAICS 42 — 17 948 фирм (2,33 млн занятых); durable goods 423 — 11 146; целевые подсектора: 4238 машины/оборудование/MRO — 3 020; 4236 электрика — 1 370; 4233 стройматериалы — 1 039; 4237 сантехника/отопление/hardware — 976; 4235 металлы — 689 → **≈7 100 целевых фирм** ([Census SUSB 2022, us_6digitnaics](https://www.census.gov/data/datasets/2022/econ/susb/2022-susb.html)). **ЕС-27 (2023, G46):** 1 624 343 предприятия; 50–249 сотрудников — 21 000 (2,02 млн занятых); ≥250 — ≈3 059 (расчёт: итог минус прочие классы; 2,57 млн занятых) ([Eurostat sbs_sc_ovw](https://ec.europa.eu/eurostat/databrowser/view/sbs_sc_ovw/)); разбивка по подсекторам — **не найдено**.

**Кто покупает:** владелец/CEO (сегмент семейный — Sonepar USA, Regency Supply), VP Sales / директор inside sales, директор по e-commerce и цифровизации (у Sonepar решение вёл Director of eCommerce & Digitalization), COO.

**Где обитают:** NAW Executive Summit (26–28 янв. 2026, Вашингтон, [naw.org](https://www.naw.org/events/executive-summit-2026/)); NAW Innovators Summit (там Prokeep запускал Order Engine); Applied AI for Distributors (23–25 июня 2026, Чикаго, 4-й год, 40 техноспонсоров, [phcppros, 2026-05-04](https://www.phcppros.com/articles/23330-applied-ai-for-distributors-2026)); STAFDA (15–17 нояб. 2026, Анахайм, [stafda.org](https://stafda.org/conventions/); >4 300 участников по [ForConstructionPros](https://www.forconstructionpros.com/events/event/22236329/stafda-annual-convention-tradeshow), б/д); NAED Lead/National, ISA Fall Summit; медиа MDM, DSG, Industrial Distribution, Supply House Times. Доступность высокая, но эти же площадки уже заняты конкурентами.

## 7. Риски

- **Каталог и данные:** десятки тысяч SKU, клиентские артикулы, запросы по описанию без номера; уверенность в ROI — 81% у компаний с хорошими данными против 18% с плохими ([DSG, 2026-09-09](http://distributionstrategy.com/2026/09/ai-top-25-reveals-a-wide-execution-gap-across-wholesale-distribution/)).
- **Люди:** 52% называют кадровые барьеры (навыки, сопротивление) (там же); DSG прогнозирует −30–40% персонала к 2030 — CSR понимают, что автоматизируют их ([DSG 2025](https://distributionstrategy.com/wp-content/uploads/2025/03/DSG-Report-The-2025-State-of-AI-in-Distribution.pdf)).
- **EDI и legacy ERP:** исключения EDI и AS/400 без API удлиняют внедрение (Ordermatic: «недели» против «дней» у Canals — [сравнение](https://ordermatic.co/ordermatic-vs-canals)).
- **Цена:** $5 тыс./мес ≈ 1 FTE CSR; конкуренты берут за документ и не публикуют цены — сравнение будет не в пользу фиксированной «роли» у малых объёмов.
- **Сезонность:** стройматериалы/HVAC/сантехника завязаны на стройсезон — численно **не найдено**.
- **Платформенный риск:** Epicor/Infor встраивают ИИ в ERP (роадмап — не проверен).

## 8. Оценка

| Критерий | Балл |
|---|---|
| Объём повторяемой работы | **5** |
| Стоимость заменяемого труда | **3** ($64–66 тыс. CSR США; €37–45 тыс. DE) |
| Простота внедрения | **3** (5–6 ERP покрывают сегмент, но каталоги/legacy) |
| Слабость конкуренции (5 = пусто) | **1** |
| Доступность покупателя | **4** |
| Доказанная готовность платить | **5** |

**Вердикт.** Спрос и платёжеспособность доказаны, но именно поэтому ниша уже занята: два игрока с $50M+ и четыре стартапа с раундами и запусками в 2024–2026, а цена $5 тыс./мес равна одному CSR, что слабо против «платы за документ». Как **первая** ниша для лобовой автоматизации order entry — **не годится**. Если всё же идти — брать узкий подсегмент, где свежие игроки ещё только стартуют (Proton GA июль 2026): **RFQ → котировка по описанию с подбором замен и телефонный/голосовой канал у электро- и PVF-дистрибьюторов на 100–500 человек на Eclipse/P21**, либо **немецкоязычная Европа** (зарплаты ниже, из профильных — Workist и Esker; плотность там в этом ресёрче не проверена).
