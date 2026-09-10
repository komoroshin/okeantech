# 03 · Грузовые брокеры, экспедиторы, таможенные брокеры — оценка как первой ниши для «ИИ-сотрудников»

Дата сбора: 2026-09-10. Все суммы в $. «Не найдено» = источник не получен в ходе поиска, число не выдумано.

## 1. Повторяющаяся работа

| Роль | Что делает | Канал | Объём | Источник |
|---|---|---|---|---|
| Quote desk / pricing | Разбор входящего запроса (email), извлечение маршрута/веса/дат, расчёт ставки, ответ | Email, порталы шипперов | 150–200 котировок/день на репа | Vooma case study, https://www.vooma.com/case-studies/worldwide-logistics (2025) |
| Carrier sales | Поиск перевозчика, переговоры по ставке, букинг, rate confirmation | Телефон, доски загрузок (DAT/Truckstop), email | 100–300 звонков/день у брокеров | https://www.freightframeworks.com/guides/freight-broker-cold-calling (2026) |
| Track & trace | Check calls: статус, ETA, исключения, обновление TMS | Телефон, SMS, email, ELD-порталы | Пример: C.H. Robinson — 2 агента закрывают пропущенные LTL-забор у 11 000 шипперов, 95% проверок, экономия 350 ч/день | Dealroom note, https://app.dealroom.co/news/note/nine-of-the-top-10-us-freight-brokers-inside-happyrobot-s-agentic-ai-land-grab (06.2026) |
| Документооборот (экспедитор) | BOL, инвойсы, коммерческие счета, сверка счетов поставщиков, ввод в TMS | Email + PDF, EDI | Raft: до 2 ч экономии на отправку, 300 тыс. отправок/мес на платформе | https://www.raft.ai/resources/press-releases/raft-raises-30m-in-series-b-funding-to-transform-global-supply-chain-execution-with-ai (07.2023) |
| Customs entry clerk | HS-классификация, сборка декларации, подача в ACE/CDS, запросы недостающих данных | Email, ACE/ABI, CDS | Digicust: 3–4 ч → 10–15 мин на декларацию; 16 000 деклараций за 3 мес у одного клиента | https://techstartups.com/2025/12/18/austrian-ai-startup-digicust-raises-e2-3m-to-automate-customs-clearance-across-europe-using-ai/ (18.12.2025) |

Что уже автоматизируют: классификация email и извлечение данных из PDF в TMS (Levity, Drumkit), котировки (Vooma), голосовые check calls и переговоры с перевозчиками (HappyRobot, FleetWorks), сверка счетов и биллинг (Expedock, Augment), декларации (Raft, Digicust). У средних брокерств в 2026 автоматизируется 80%+ входящих писем перевозчиков — https://blog.gettransport.com/trends-in-logistic/ai-agents-freight-brokers-2026-quote-automation/ (2026).

## 2. Сколько людей и сколько стоят

- **Cargo and Freight Agents (SOC 43-5011), США:** 105 220 занятых, средняя зарплата $52 460/год (BLS OEWS, май 2023) — https://www.bls.gov/oes/2023/may/oes435011.htm. Данные за май 2024/2025 по этой профессии: не получены (страница BLS не отдалась).
- **Отрасль NAICS 4885 (Freight Transportation Arrangement), США:** 21 832 заведения, 301 772 работника (Census CBP 2020) — https://samsearch.co/naics-ai-lookup/4885. Более свежий год: не найдено.
- **Лицензированные таможенные брокеры США:** ≈11 000–11 400 активных лицензий (CBP) — https://customsbrokerindex.com/blog/us-customs-broker-list-find-licensed/ (2026).
- **Customs entry clerk:** $19,47/ч в среднем, диапазон $16,35–21,88 (ZipRecruiter, 09.2025) — https://www.ziprecruiter.com/Salaries/Customs-Entry-Clerk-Salary. Customs entry writer: $49 132/год (Payscale, 2026) — https://www.payscale.com/research/US/Job=Customs_Entry_Writer/Salary. Лицензированный брокер: $75 242/год (ZipRecruiter, 07.2026) — https://www.ziprecruiter.com/Salaries/Licensed-Customs-Broker-Salary; медиана $80 730 (BLS OEWS май 2025, цит. по https://nuecareer.com/careers/customs-broker).
- **Продуктивность брокера:** ≈$1,27 млн валовой выручки на сотрудника, маржа 10–15% → $127–190 тыс. gross profit на голову — https://www.freightcaviar.com/freight-brokerages-1-2m-revenue-per-employee/ (2025).
- **Сколько на компанию:** брокер 50–2000 чел. при $52 тыс. средней зарплате и типичной структуре (carrier sales + ops + T&T) — десятки–сотни ролей с повторяемой работой; точная доля по ролям: не найдено.
- **Европа:** CLECAT представляет >19 000 компаний и >1 млн сотрудников в экспедировании/таможне — https://www.clecat.org/organisation/objectives (дата страницы не указана). DSLV (Германия): ≈3 000 компаний, 605 000 сотрудников — https://euagenda.eu/organisers/federal-association-for-freight-forwarding-and-logistics-germany. Зарплаты по ЕС: не найдено.

Вывод: труд дешёвый ($45–55 тыс. у клерков/агентов), т.е. $5 тыс./мес за роль = ~1 FTE с налогами. Продать можно только там, где агент заменяет 1,5–3 FTE или закрывает круглосуточность.

## 3. Системы и стандартизация

- **Брокеры (США):** рынок TMS фрагментирован — McLeod, Turvo, Revenova, Tai, Aljex (Descartes), Rose Rocket, Alvys, MVMNT, 3Gtms и др.; долей по вендорам в открытых источниках нет — https://pmarketresearch.com/worldwide-freight-broker-transportation-management-software-tms-market-research/ (2026). Рынок брокерского ПО $1,35 млрд (2025) — там же. Следствие: интеграция под каждого клиента отдельная (API McLeod/Turvo есть, у малых TMS — слабые).
- **Экспедиторы/таможня:** CargoWise ≈70% рынка forwarding-софта, >17 000 организаций, 24 из топ-25 глобальных экспедиторов — https://btw.media/en/wisetechglobal-makes-logistics-data-hard-to-move-once-trade-is-flowing и https://www.wisetechglobal.com/media/i4ib0p11/wtc-fy25-results-investor-presentation.pdf (FY25). Альтернативы — Magaya, Descartes. Высокая стандартизация = одна интеграция покрывает большую часть рынка, но WiseTech жёстко контролирует экосистему.
- **Таможня:** единые гос-интерфейсы — ACE/ABI (США), CDS (UK), национальные системы ЕС + ICS2 (полный охват к 06.2026) — https://taxation-customs.ec.europa.eu/customs/customs-security/import-control-system-2_en.

## 4. Кто уже продаёт ИИ-агентов

| Компания | Сегмент | Раунд | Дата | Источник |
|---|---|---|---|---|
| HappyRobot | Голос/email агенты, брокеры, перевозчики, экспедиторы | Series C $150 млн, оценка $1,2 млрд; всего ≈$200 млн; 150+ клиентов, 9 из топ-10 брокеров США, 5 из топ-10 экспедиторов | 08.2026 | https://finance.yahoo.com/technology/ai/articles/happyrobot-series-c-mints-freighttech-165732635.html; Series B $44 млн 09.2025 https://www.happyrobot.ai/blog/series-b-announcement |
| Augment (Augie) | «AI teammate» для 3PL: котировки, диспетч, T&T, биллинг | Series A $85 млн (всего $110 млн) | 09.2025 | https://www.businesswire.com/news/home/20250904472410/en/ |
| Raft (ex-Vector.ai) | Экспедиторы + таможенные брокеры, документы, декларации | Series B $30 млн | 07.2023 | https://techcrunch.com/2023/07/11/raft-which-services-freight-forwarders-closes-30m-series-b-led-by-eight-roads-vc |
| Vooma | Котировки, load building, voice для брокеров | Seed+A $16,6 млн; новых раундов нет 19 мес | 12.2024 | https://www.businesswire.com/news/home/20241202150186/en/ |
| FleetWorks | Голосовой AI-диспетчер, букинг перевозчиков | $17 млн (A $15 млн) | 2025 | https://www.freightwaves.com/?p=566727 |
| Parade | Capacity management; куплена Mudflap | всего $36 млн | 04.2026 | https://www.freightwaves.com/news/parade-secures-17m-from-i-squared-capital-for-ai-endeavors |
| Greenscreens.ai | Прайсинг; куплена Triumph Financial за $140 млн cash + акции | 05.2025 | https://www.globenewswire.com/news-release/2025/05/08/3077732/28528/en/ |
| Expedock | Экспедиторы, документы/счета, офшоринг | Series A $13,5 млн (всего $17,5 млн) | 08.2022 | https://www.prnewswire.com/news-releases/expedock-raises-13-5m-series-a-led-by-insight-partners-to-solve-and-accelerate-the-global-supply-chain-301601828.html |
| Drumkit | Email-автоматизация брокеров | Seed $2,6 млн | 06.2022 | https://www.crunchbase.com/organization/drumkit |
| Levity (Берлин) | Email-автоматизация, клиенты Hellmann, Gebrüder Weiss | сумма не найдена | — | https://levity.ai/logistics |
| Cargofy (ЕС) | «Digital workers» для freight ops | Series A €9,5 млн | 06.2026 | https://www.eu-startups.com/2026/06/cargofy-raises-e9-5-million-series-a-to-deploy-ai-digital-workers-across-freight-operations/ |
| 5U AI (Мюнхен) | AI Workers для экспедиторов (котировки, букинг, T&T, сверка) | Pre-seed $3,2 млн | 07.2026 | https://tech.eu/2026/07/28/5u-ai-lands-32m-pre-seed-for-ai-freight-workforce-platform/ |
| Nexcade (Лондон) | Экспедиторы | Seed $6 млн | 07.2026 | там же (tech.eu) |
| Digicust (Вена) | Таможенные декларации ЕС | Pre-A €2,3 млн | 12.2025 | https://techstartups.com/2025/12/18/ |
| Caspian (США) | Таможня/duty drawback, сам лицензированный брокер | Seed $5,4 млн | 07.2025 | https://www.businesswire.com/news/home/20250729878632/en/ |
| Amari AI (США) | Customs compliance агент, 30+ клиентов | $4,5 млн | 02.2026 | https://techcrunch.com/2026/02/19/ |
| KlearNow | Таможенная очистка | не найдено | — | https://klearnow.ai/ |

**Цены конкурентов:** HappyRobot — оплата за действие, минимальный годовой контракт ≈$250 тыс. — https://rapidclaw.dev/blog/ai-agent-pricing-models-compared (2026). Vooma, Levity, Raft, Augment — цены не публикуют (не найдено).

**Плотность:** брокеры США — **крупные $50M+** (HappyRobot $200 млн, Augment $110 млн) плюс 5–8 средних. Экспедиторы — Raft $30 млн+ и волна европейских seed/A 2026 г. (1–3 стартапа на страну). Таможня — только seed-стадия ($2–5 млн), ни одного игрока с $50M+.

## 5. Доказательства, что платят

- HappyRobot: 150+ enterprise-клиентов (DHL, Uber Freight, Kuehne+Nagel, LKW Walter), рост 5× после Series B, контракты от $250 тыс./год — https://finance.yahoo.com/technology/ai/articles/happyrobot-series-c-mints-freighttech-165732635.html (08.2026).
- Augment: клиенты сообщают −40% задержек счетов, биллинг быстрее на 8 дней, +5% маржи на груз, «миллионы» экономии на T&T-зарплатах — https://www.businesswire.com/news/home/20250904472410/en/ (09.2025).
- Vooma: выручка ×12,5, объём ×32; 300 тыс. котировок и 50 млн писем в месяц; WorldWide Logistics −95% времени ответа на котировку, Sunset −66% — https://www.vooma.com/resources/new-funding-and-products-launch; https://www.vooma.com/case-studies/sunset-transportation.
- Raft: Masterpiece — 1 000 чел.-часов/мес экономии, эффективность до +93%; ALS — 700 специалистов в 50 офисах — https://raft.ai/resources (2025).
- Levity: −61% времени на котировку у брокера — https://levity.ai/logistics.
- Greenscreens куплена за $140 млн при $10,8 млн привлечённых — стратеги платят за freight-AI.

## 6. Размер и доступ

- **Брокеры США:** 25 271 активных лицензий FMCSA (01.2025, −9,9% г/г; в 2024 закрылось 3 104) — https://magazine.factoring.org/magazine-articles/carrier-amp-broker-failures-in-20242025-and-why-2026-may-bring-one-last-wave. Доля компаний 50–2000 чел.: не найдено (по структуре рынка — сотни, не тысячи).
- **Таможенные брокеры США:** ≈11 400 лицензий (индивидуальные + корпоративные); корпоративных фирм — не найдено.
- **Европа:** CLECAT >19 000 компаний; DSLV ≈3 000; BIFA >1 600 — https://en.wikipedia.org/wiki/British_International_Freight_Association. UK: 91 млн деклараций в 2025, импорт из не-ЕС — 41,7 млн деклараций через 2 820 декларантов — https://www.gov.uk/government/statistics/customs-declarants-and-declaration-volumes-for-international-trade-in-2025. Рынок таможенного брокеража Европы $28,8 млрд (2025), Германия 20,65% — https://www.mordorintelligence.com/industry-reports/europe-customs-brokerage-market.
- **Рынок:** US 3PL gross $307,9 млрд (2024), DTM (брокераж) −4,2% — https://www.logisticsmgmt.com/article/u.s_3pl_market_rebounded_in_2024_says_new_armstrong_associates_report.
- **Кто покупает:** VP Operations / COO, Head of Pricing, Director of Carrier Sales; в таможне — Brokerage Manager / Compliance Director. **Где найти:** TIA (>1 700 членов; Capital Ideas Conference) — https://tianet.org/; FIATA (5 959 индивидуальных членов) — https://www.lobbyfacts.eu/datacard/international-federation-of-freight-forwarders-associations; NCBFAA (таможня США); CLECAT/DSLV/BIFA; выставки Transport Logistic Munich, Manifest, FreightWaves F3.

## 7. Риски

- **Волатильность:** «великая фрахтовая рецессия» 2023–2025, волна банкротств брокеров, прогноз новой волны в 2026 — https://www.freightwaves.com/news/the-perfect-storm-why-freight-brokerages-face-a-wave-of-failures-in-2026. Покупатель сокращает людей, а не добавляет софт; при этом Cass Index +3% м/м в мае 2026 — признаки разворота — https://www.cassinfo.com/freight-audit-payment/cass-transportation-indexes/may-2026.
- **Регуляторика (плюс и минус):** отмена de minimis с 29.08.2025 — резкий рост числа формальных деклараций — https://www.cbp.gov/newsroom/national-media-release/cbp-modernizes-low-value-shipment-processing; ICS2 полный охват к 06.2026; реформа UCC ЕС и Customs Data Hub с 2028 — https://www.consilium.europa.eu/en/policies/modernising-the-eu-customs-union/. Рост нагрузки = спрос на автоматизацию, но ошибки в декларациях = штрафы и ответственность лицензиата; ИИ не может быть «брокером записи».
- **Интеграции:** у брокеров — десяток TMS без единого API; у экспедиторов — один CargoWise, но закрытая экосистема WiseTech; телефония/голос требует отдельного стека.
- **Конкуренция за enterprise:** HappyRobot уже у 9 из 10 топ-брокеров; средний сегмент — единственное окно.

## 8. Оценка (1–5)

| Критерий | Балл | Обоснование |
|---|---|---|
| Объём повторяемой работы | 5 | 150–200 котировок/день, сотни звонков, декларации часами |
| Стоимость труда | 2 | $45–55 тыс./год у агентов и клерков; $5 тыс./мес ≈ 1 FTE |
| Простота внедрения | 3 | Экспедиторы/таможня — CargoWise + гос-API (хорошо); брокеры — зоопарк TMS + голос (плохо) |
| Слабость конкуренции | 2 | Брокеры США — $50M+ игроки; экспедиторы — 1–3 на страну; таможня — только seed |
| Доступность покупателя | 4 | Плотные ассоциации (TIA, NCBFAA, CLECAT, BIFA), выставки, открытые реестры лицензий |
| Доказанная готовность платить | 5 | Контракты от $250 тыс./год, 150+ enterprise-клиентов, M&A $140 млн |

**Вердикт.** Как общая первая ниша «freight brokerage США» не годится: HappyRobot ($1,2 млрд) и Augment уже закрыли верх рынка, труд дешёвый, а рынок брокеров сжимается и хоронит покупателей. Однако категория доказала платёжеспособность лучше большинства вертикалей, и есть два незанятых подсегмента: (1) **таможенные брокеры и таможенные отделы экспедиторов в США/UK/ЕС** — взрыв деклараций после отмены de minimis и ICS2, конкуренты только на seed-стадии ($2–5 млн), единые гос-интерфейсы (ACE/CDS), а роль entry clerk ($40–50 тыс.) заменяется целиком с контролем лицензиата; (2) **средние экспедиторы континентальной Европы на CargoWise**, где европейские стартапы появились лишь в 2026 и ещё не имеют enterprise-референсов. Рекомендация: идти через (1) с позиционированием «ИИ-сотрудник таможенного отдела», целить на компании 50–500 человек через NCBFAA/BIFA/CLECAT; брокерский сегмент США оставить на потом.
