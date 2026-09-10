# 02. Фудсервис-дистрибуция и FMCG-оптовики (США/ЕС) — оценка как первой ниши для «ИИ-сотрудников»

Дата исследования: 2026-09-10. Фокус: независимые broadline/specialty дистрибьюторы (не Sysco/US Foods/PFG), 50–2000 сотрудников. Каждое число — с источником; «не найдено» = не нашёл проверяемой цифры.

## 1. Повторяющаяся работа

**Роли:** order desk / customer service rep (CSR), inside sales, торговые представители (DSR), которые сами вбивают заказы клиентов в ERP. Задачи: приём заказа, уточнение (нет товара → замена), ответ на вопросы по наличию/цене, ввод в ERP, кредит-ноты по возвратам и недовозам. Формулировка лидера рынка: «большинство дистрибьюторов до сих пор вводят заказы руками, потому что клиенты не хотят менять способ заказа: email, SMS, PDF, голосовая почта, WhatsApp, фото рукописных записок, факс» ([Choco, 17.11.2025](https://choco.com/us/stories/suppliers/orderagent-the-ai-order-processing-engine-thats-powering-the-future-of-food-distribution)).

**Объём/время:** ручной ввод одного заказа — 7–8 мин (Choco, там же); 5–8 мин ([Pepper, кейс Carolina Food Service, 24.04.2026](https://www.usepepper.com/case-studies/carolina-food-service-streamlines-order-entry-in-every-format-with-peppers-order-agent)); ~10 мин ([Burnt, пресс-релиз 25.09.2025](https://www.prnewswire.com/news-releases/burnt-raises-3-8m-in-seed-funding-to-accelerate-food-supply-chain-302567414.html)). Себестоимость ручного заказа $8–15 (вендорская оценка, без внешних ссылок — [Mirage Metrics, 30.03.2026](https://miragemetrics.com/blog/true-cost-manual-order-entry/)). Пример нагрузки: 50 заказов/день = 16 человеко-часов (Pepper, кейс Alpha Eagle — JanSan, не фуд, [usepepper.com](https://www.usepepper.com/case-studies/alpha-eagle-modernizing-jansan-orders-and-growing-margins-with-pepper)). Отдельная боль — ночная смена ввода заказов, пришедших после закрытия ресторанов: «дистрибьюторы не могут найти людей на ночной ввод» ([Choco × OpenAI, 04.12.2025](https://choco.com/us/press/choco-and-openai-join-forces-to-launch-the-first-ai-voice-agent-for-the-food-service-industry)).

**Каналы:** email, SMS, WhatsApp, голосовая почта, телефон, фото, PDF, факс (Choco, Pepper, Burnt — ссылки выше). Кейс Brown Foodservice: «поток звонков, SMS, email и голосовых на весь клиентский пул, всё вручную в ERP» ([Pepper, 24.10.2025](https://www.usepepper.com/case-studies/brown-foodservice-automates-orders-with-pepper-saving-reps-1-2-hours-each-day)).

**Что уже автоматизируют:** ~1/3 дистрибьюторов используют ИИ (12% в 2023), из них 56% — для e-commerce/заказов, 52% — офисная автоматизация, 48% — клиентский сервис/прогноз; почти треть говорит, что ИИ «менее эффективен, чем ожидали»; выборка 32 компании ([IFDA Technology Report, 24.07.2025](https://ifdaonline.org/ifda-releases-2025-technology-benchmarking-report-revealing-shifts-in-foodservice-distribution-tech-adoption/)).

## 2. Сколько людей и сколько стоят

- Отрасль в США: 431 000 сотрудников, 17 100 локаций, $382 млрд продаж; водители 31%, склад 42% → на офис/продажи/сервис остаётся ~27% (~116 тыс. чел., оценка из структуры) ([IFDA Industry Facts, данные 2023](https://ifdaonline.org/industry-facts/)).
- Вся NAICS 4244 (оптовики продуктов): 27 458 фирм, 846 963 занятых ([Census SUSB 2022](https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.txt)).
- Зарплаты (BLS, май 2025): CSR — медиана $21.53/ч, $44 770/год; в wholesale trade — $23.41/ч (~$48.7k) ([BLS OOH](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm)); order clerks — $22.20/ч, $46 170/год, 89 500 занятых ([O*NET по данным BLS 2025](https://www.onetonline.org/link/summary/43-4151.00)). Вакансия CSR у фуд-дистрибьютора: $65–75k + бонус ([Indeed](https://www.indeed.com/viewjob?jk=67ad04216a2f93ef)). Полная стоимость с налогами/льготами: ~$60–95k/год (оценка ×1.3, источника по отрасли не найдено).
- ЕС: средние расходы на работника в оптовой торговле продуктами (G46.3) — €38.0k/год (EU-27, 2023), Германия €47.3k, Франция €56.1k, Нидерланды €57.1k, Испания €30.7k ([Eurostat sbs_sc_ovw, 2023](https://ec.europa.eu/eurostat/databrowser/view/sbs_sc_ovw/default/table)).
- **Сколько order-desk людей у компании на 50–2000 сотрудников: не найдено.** Косвенно: кейс «240 клиентов/нед. на 4 человека → 1000 клиентов/нед. на 2» (Choco, ссылка выше); у дистрибьютора 50 заказов/день — 16 человеко-часов/день ≈ 2 FTE (Pepper). Оценка: 2–4 FTE ввода/сервиса на 50–100 сотрудников, 10–30 на 500–2000 (экстраполяция, не источник).

## 3. Системы у клиентов

- ERP: фрагментированы. NECS entrée — 500+ активных дистрибьюторов, mid-market ([LeadIQ/NECS](https://leadiq.com/c/necs-inc-software-for-food-distributors/5a1daa1b2300005c009e92ec)); Produce Pro, Aspen Systems, Sage, Acctivate, Dossier и др. — в списках рынка ([Software Connect](https://softwareconnect.com/roundups/best-food-distribution-software/)). Доли рынка — не найдено.
- Признак фрагментации: Choco заявляет «двустороннюю синхронизацию с 200+ ERP» ([choco.com/comparison](https://choco.com/us/comparison)); Pepper — «500+ ERP-интеграций за 5 лет», внедрение 1–3 мес ([AgFunderNews, 08.04.2026](https://agfundernews.com/inside-peppers-push-to-digitize-foodservices-long-tail-armed-with-50m-and-agentic-ai)); ранее «60+ систем» ([Pepper, 03.09.2025](https://www.usepepper.com/post/top-food-distribution-ai-tools)).
- Порталы заказов (Cut+Dry, Choco, Pepper) — это и есть конкуренты (п.4), они же владеют интеграцией. MarketMan — сторона ресторана. Вывод: стандартизации нет; каждое внедрение = кастомная интеграция с ERP, у IFDA «совместимость с существующими системами — главный фактор решений» (IFDA 2025).

## 4. Кто уже продаёт

| Игрок | Что | Деньги | Цены |
|---|---|---|---|
| **Choco** (Берлин/NY) | OrderAgent (email/voicemail/WhatsApp→ERP), Autopilot (~50% заказов автономно), Voice Agent на OpenAI Realtime (12.2025) | $111M Series B2, оценка $1.2B (04.2022, [tech.eu](https://tech.eu/2022/04/12/choco-chalks-up-111-million-punches-ticket-at-the-unicorn-club/)); всего ~$301M ([Tracxn](https://tracxn.com/d/companies/choco/__otHGiTPOXMhdmXvthh6B9pDh8O9jKayLeZQFBReSb0E)); рынки US, DE, FR, ES, AT, BE, UK, GCC | «ежемесячная плата по использованию», только через сейлз ([choco.com/pricing](https://choco.com/us/pricing)) |
| **Pepper** (US) | Order Agent + e-com + Sales/Finance Hub; 500+ дистрибьюторов, $30B GMV; купил Kimelo (2025) | $50M Series C (02.2026, Lead Edge; [BusinessWire](https://www.businesswire.com/news/home/20260220742173/en/)), $30M B (05.2024, ICONIQ; всего ~$60M на тот момент, [TechCrunch](https://techcrunch.com/2024/05/13/pepper-iconiq-startup-foodservice-ecommerce-30m/)) | годовые контракты, цена от размера/модулей (AgFunderNews) |
| **Cut+Dry** (US) | e-com + AI Order Desk (email/SMS/PDF/voicemail) | $12.9M всего, последний раунд 10.2022 ([Tracxn](https://tracxn.com/d/companies/cutdry/__ZNgWv3ZqLq1NuzurDfz8rr0mxFDs51wN2Y0OXHQy4BM)) | flat SaaS, без % от заказов, сумма не раскрыта ([cutanddry.com](https://cutanddry.com/distributors/pricing/)) |
| **REKKI** (Лондон) | «order processing robot», 99.99% точности, чтение email; клиенты Liberty Wines (130k заказов/год) | $59.9M ([PitchBook](https://pitchbook.com/profiles/company/343722-25)) / $23M ([StartupHub](https://www.startuphub.ai/startups/rekki)) — расходятся | не найдено |
| **Burnt** (SF) | агент ввода заказов из email/voicemail/WhatsApp/звонков в legacy-ERP; $10M заказов/мес | $3.8M seed (09.2025, Penny Jar) | не найдено |
| Прочие | Katoo (куплен Choco, 01.2023, [PitchBook](https://pitchbook.com/profiles/company/434091-52)); Ordana.ai, VoiceOrder Solutions, SimplyDepo, Percival, Seals — ранние ([Pepper-обзор 09.2025](https://www.usepepper.com/post/top-food-distribution-ai-tools), [Clinton Courier 13.08.2026](https://www.theclintoncourier.net/2026/08/13/order-taking-software-distributors/)) | мелкие | $60–429/мес у простых order-тулов (Clinton Courier) |

Notch/Ordermark: релевантных данных по ИИ-вводу заказов для дистрибьюторов не найдено (Ordermark — ресторанная агрегация). **Плотность: крупные $50M+ (две компании с суммарно >$350M) + 2–4 финансируемых стартапа + хвост.** Именно задача «email/voicemail → ERP» уже закрыта лидерами.

## 5. Доказательства, что платят

- North West Meat Company: 3 ч/день → <1 ч; экономия ~$22k/год; 1300+ SKU ([Choco, 26.10.2025](https://choco.com/us/stories/case-studies/north-west-meat-company-saving-hours-daily-with-ai)). Примечание: $22k/год — ниже планки $5k/мес за роль.
- Reach Foods: 96% точность, −90% труда на ввод; DeBragga: 94% точность, +50% скорость; Krystal F&V: 15 ч/нед ([choco.com/comparison](https://choco.com/us/comparison)).
- Brown Foodservice: 45 мин–2 ч/день на репа, 6–8 тыс. SKU, чемпион — COO ([Pepper, 24.10.2025](https://www.usepepper.com/case-studies/brown-foodservice-automates-orders-with-pepper-saving-reps-1-2-hours-each-day)).
- Pepper в целом: клиенты — +23% продаж, 93% retention, репы экономят >10 ч/нед; выручка ×20 с 2021 (TechCrunch, 05.2024).
- Цены сделок ($/мес за дистрибьютора) публично — **не найдено** ни у кого.

## 6. Размер и доступ

- США, NAICS 4244, фирмы 50–1999 сотрудников: **2 062 фирмы**, 274 901 занятых (сумма классов 50–74 … 1500–1999; [Census SUSB 2022](https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.txt)). Pepper оценивает 25 000 независимых дистрибьюторов US/Canada всех размеров (TechCrunch).
- ЕС-27, NACE G46.3, 2023: 50–249 чел. — **4 209 предприятий**; 250+ — 680 (включая гигантов); Германия 656/104, Франция 398/71, Испания 880/197, Италия 366/37, Нидерланды 206/40, Польша 251/46 ([Eurostat sbs_sc_ovw](https://ec.europa.eu/eurostat/databrowser/view/sbs_sc_ovw/default/table)). Великобритания, 03.2023: 50–249 — 505, 250+ — 95 ([ONS ad hoc 1607](https://www.ons.gov.uk/businessindustryandtrade/business/activitysizeandlocation/adhocs/1607foodwholesalebyemployeesize)).
- Кто покупает: владелец/президент, COO, VP Sales/Operations (кейсы Pepper/Choco). Где: IFDA Solutions Conference (13–15.09.2026, Сан-Антонио; 1500+ участников, 170 экспонентов, ~150 дистрибьюторов в списке — [IFDA](https://ifdaonline.org/events/ifda-solutions-conference/who-attends/)); закупочные кооперативы UniPro/Frosty Acres (численность — не найдено); в ЕС — Internorga, Anuga, Sirha (данные по посещаемости не собирал).

## 7. Риски

- **Маржа:** чистая маржа даже у PFG 1–2% ([Dealroom/PFG](https://app.dealroom.co/companies/performance_food_group)); у независимых — не найдено, но давление очевидно: бюджеты — второй фактор решений (IFDA 2025). $5k/мес = $60k/год ≈ 1 FTE — продать можно только как замещение явной ставки, а кейсы лидеров показывают экономию $22k/год (NWMC).
- **Конкуренция встроена в канал:** Choco/Pepper уже держат e-com-портал + ERP-интеграцию + обучение на 12 мес. истории; у новичка нет данных.
- **Качество данных/ERP:** «200+ ERP», внедрение 1–3 мес (Pepper), нестандартные каталоги, замены товаров — ошибка = недовоз в ресторан.
- **Сопротивление:** треть пользователей разочарована ИИ (IFDA); репы боятся потери комиссии.
- **Европа:** дробность (Испания/Италия — в основном <10 чел.), языки; Choco уже закрыл DE/FR/ES и заявляет «любой язык» для Voice Agent.

## 8. Оценка (1–5)

| Критерий | Балл | Комментарий |
|---|---|---|
| Объём повторяемой работы | 5 | 5–10 мин на заказ, мультиканально, ночная смена; подтверждено всеми игроками |
| Стоимость труда | 2 | CSR $45–49k медиана; ЕС €30–57k; дёшево относительно $5k/мес |
| Простота внедрения | 2 | 200+ ERP, 1–3 мес интеграции, нет стандартов |
| Слабость конкуренции | 1 | Два игрока с >$350M, unicorn, OpenAI-партнёрство + 3–5 стартапов |
| Доступность покупателя | 4 | ~2 тыс. US + ~4–5 тыс. ЕС/UK фирм нужного размера; одна ключевая выставка, ЛПР = владелец/COO |
| Доказанная готовность платить | 3 | Платят, но за SaaS «портал + ввод»; экономия в кейсах $22k/год, ценники $/мес не раскрыты |
| **Итого** | **17/30** | |

**Вердикт.** Как первая ниша — не годится: задача «email/voicemail → ERP» уже решена хорошо финансируемыми Choco и Pepper, которые владеют каналом (портал + интеграции) и продают дешевле нашей планки. Если всё же заходить — не в ввод заказов, а в соседний необслуженный процесс: кредит-ноты/претензии по недовозам и заменам, запросы спеков и сертификатов (allergens/COA) от клиентов, или работа с дебиторкой (Pepper только начинает «Finance Hub»). Лучший подсегмент: специализированные дистрибьюторы (мясо, рыба, produce, вино) в Европе вне DE/FR/ES (Бенилюкс, Скандинавия, Польша, UK-middle), 50–250 сотрудников, на локальных ERP — там Choco/Pepper слабее, а мультиязычность становится нашим плюсом, не минусом.
