# 05. Производство под заказ и контрактное производство (job shops, EMS, упаковка, печать)

Дата исследования: 2026-09-10. Рынок: США + ЕС. Процесс: RFQ → котировка → приём заказа → подтверждение сроков → статусы клиентам.

## 1. Какая повторяющаяся работа

**Роли:** estimator / cost estimator (расценка по чертежу), inside sales / quoting specialist (приём RFQ, ответ клиенту), customer service / order entry (ввод PO в ERP, подтверждение срока, статусы), production planner (сроки).

**Задачи и объём:**
- Разбор входящих RFQ-писем с чертежами (PDF/STEP), раскладка файлов по позициям, ввод в систему — «самые опытные люди цеха тратят сотни часов в год на повторяющуюся админ-работу»; бета-клиент Paperless Parts обрабатывал «30–40 квот-пакетов по 5–15 файлов на позицию», настройка одной позиции 2–5 мин ([Paperless Parts, 20.02.2024](https://www.paperlessparts.com/press/paperless-parts-cuts-quote-setup-time-by-90-with-new-ai-supported-workflow/)).
- Расценка: «до двух часов на квоту по одной детали» ([Modern Machine Shop, 01.11.2021](https://www.mmsonline.com/articles/when-it-comes-to-rfq-response-time-is-money)). Типичный win-rate 20–30 % → 7 из 10 квот — впустую ([Paperless Parts blog](https://www.paperlessparts.com/blog/overengineering-the-quote-part-1/)).
- Давление по скорости: опрос 400+ закупщиков США — 67 % ждут квоту < 24 ч, лишь 6 % готовы ждать > 3 дней ([Paperless Parts](https://www.paperlessparts.com/blog/machine-shop-estimating-quoting-a-complete-guide/)); Top Shops отвечают за 1 день и имеют на 19 % выше quote-to-book ([MMS Top Shops](https://www.mmsonline.com/articles/top-shops-by-the-numbers)).
- Приём заказа: ручной ввод PO из email/PDF в ERP (Workist: «90 % экономии времени, 80 % меньше ошибок» на 200+ клиентах — [workist.com](https://www.workist.com/en/order-entry)).
- Объём RFQ в день на цех — **не найдено** в открытых источниках (только анекдоты: Jax Precision после автоматизации котирует в 2,5 раза больше работ/мес — [кейс](https://www.paperlessparts.com/case-studies/jax-precision-grows-revenue-by-300-triples-customer-base-with-paperless-parts/)).

**Каналы:** email с вложениями (основной), порталы закупщиков (Ariba/Coupa у крупных OEM), телефон; маркетплейсы (Xometry) — отдельный канал.

**Что уже автоматизируют:** разбор RFQ-писем и извлечение позиций (Paperless Parts Wingman, Uptool), извлечение GD&T/допусков с чертежей (Requirements Review, GA окт. 2025 — [Paperless Parts, 08.09.2025](https://www.paperlessparts.com/press/paperless-parts-new-ai-features-surface-critical-requirements-helping-shops-quote-faster-with-confidence/)), AI BOM Builder в JobBOSS² ([ECI](https://www.ecisolutions.com/products/jobboss2/)), ввод PO (Workist). Сама инженерная расценка остаётся за человеком — все игроки это подчёркивают.

## 2. Сколько людей и сколько стоят (США, BLS OOH, данные май 2025)

| Роль | Занятость (все отрасли) | Медиана $/год | Источник |
|---|---|---|---|
| Cost estimators | 226 400; 12 % в производстве (~27 тыс.) | 78 740 (в производстве 75 940) | [BLS OOH](https://www.bls.gov/ooh/business-and-financial/cost-estimators.htm) |
| Sales reps, wholesale & mfg | 1 571 400; 18 % в производстве | 72 080 (нетехн.) / 104 920 (техн.) | [BLS OOH](https://www.bls.gov/ooh/sales/wholesale-and-manufacturing-sales-representatives.htm) |
| Customer service reps | 2 666 000 | 44 770 | [BLS OOH](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm) |
| Order clerks | в составе 1 287 600 information clerks | 46 170 | [BLS OOH](https://www.bls.gov/ooh/office-and-administrative-support/information-clerks.htm) |

Полная стоимость в производстве: $30,94/ч зарплата + $15,36/ч льготы (BLS ECEC, июнь 2025, через [bls.gov](https://www.bls.gov/news.release/ocwage.htm)) → estimator стоит работодателю ≈ $110–120 тыс./год. NTMA Wage & Fringe Survey — платный ($750 не членам) ([ntma.org/reports](https://ntma.org/reports/)); цифры **не найдены**.

**На предприятие 50–2000 чел.:** прямой статистики нет. Оценка по структуре: фронт-офис (estimating + inside sales + order entry/CS) в цехе 50–100 чел. — обычно 2–4 человека, в 200–500 чел. — 5–15. **Источник — не найдено; оценка.** Итого фонд замещаемой работы на целевом предприятии ≈ $200–800 тыс./год.

## 3. Системы и стандартизация

ERP-зоопарк для job shops: ECI JobBOSS² (E2+JobBOSS; «тысячи цехов», 10–100 чел. — [ECI](https://www.ecisolutions.com/products/jobboss2/), [ERP Research](https://www.erpresearch.com/en-us/jobboss-erp)), ProShop, Epicor Kinetic (внедрение $100–500 тыс., mid-market — [SelectHub](https://www.selecthub.com/manufacturing-software/proshop-erp-vs-epicor-kinetic/)), Global Shop, Infor SyteLine/VISUAL, Plex, Fulcrum, Genius, M1, MIE Trak, Made2Manage, StartProto — именно такой список интеграций у Paperless Parts ([integrations](https://www.paperlessparts.com/integrations/)) — 15 ERP + HubSpot/Salesforce/QuickBooks/Autodesk Fusion. CAD: STEP/PDF-чертежи повсеместно; SolidWorks/Fusion/Mastercam. EMS: CalcuQuote (350+ клиентов, [Elisa IndustrIQ](https://www.elisaindustriq.com/calcuquote)), Luminovo (300+, [luminovo.com](https://luminovo.com/)).

**Степень стандартизации: низкая-средняя.** Формат входа (email + PDF + STEP) един, но ERP — 10–15 систем, часто on-prem (E2). Плюс: у большинства есть API/коннекторы через Paperless Parts — значит, доступ технически решён.

## 4. Кто уже продаёт сюда

| Игрок | Что | Деньги | Дата/источник |
|---|---|---|---|
| Paperless Parts (США) | Quoting-платформа + AI Wingman; 800+ цехов; 10 млн стр. чертежей/год | $45,5M всего, Series B $30M (2021), последний $5M 12.2023; тарифы от $300/мес, Professional $750/мес | [Tracxn](https://tracxn.com/d/companies/paperless-parts/__kTremmc3tJVLvxszjo_NxkZaZdSl8XfoMF8_APjQQXA), [Facts](https://www.paperlessparts.com/facts/), [SpotSaaS, 06.2026](https://www.spotsaas.com/product/paperless-parts/pricing) |
| Uptool (США) | AI-квотинг для SMB-цехов, внедрение за час, «без предоплаты» | Seed $6M (Khosla, Eclipse, Bessemer, KP) | [Pulse2, 10.02.2026](https://pulse2.com/uptool-6-million-seed-funding-closed-for-helping-u-s-shops-quote-10x-faster/) |
| Atira (Мюнхен) | ИИ-агенты для RFQ→техпредложение у крупных промышленников (ABB E-mobility, Chiron, Robel); 15 клиентов, −80 % времени, 95 ч/заявку | Seed $15M (Accel) + pre-seed $2,5M | [Fortune, 03.09.2026](https://fortune.com/2026/09/03/exclusive-german-ai-startup-atira-raises-17-5-million-to-unclog-the-paperwork-bottleneck-in-industrial-dealmaking/) |
| CADDi (Япония/США) | AI по чертежам + CADDi Quote (RFQ-платформа), 100+ крупных клиентов | $38M ext., оценка $470M, всего ~$202M | [SiliconANGLE, 27.03.2025](https://siliconangle.com/2025/03/27/ai-startup-caddi-nabs-38m-help-manufacturers-optimize-supply-chains/) |
| Roadrunner (США) | Агентный CPQ для enterprise (не цеха) | $27M (KP + Founders Fund) | [GlobeNewswire, 12.05.2026](https://www.globenewswire.com/news-release/2026/05/12/3293309/0/en/roadrunner-raises-27m-to-rebuild-quote-to-cash-from-the-ground-up.html) |
| Luminovo (Мюнхен/NYC) | EMS-квотинг и BOM, 300+ клиентов, «−90 % RFQ-время» | $23M+ (seed $13M, 06.2022) | [luminovo.com/about](https://luminovo.com/about) |
| Workist (Берлин) | ИИ-агент ввода заказов в ERP, 200+ клиентов | раунды **не найдено** | [workist.com](https://www.workist.com/en/order-entry) |
| Axya (Монреаль) | Закупки/RFQ для aerospace | $4,28M | [CB Insights](https://www.cbinsights.com/company/quotebeam) / [Startup Intros](https://startupintros.com/orgs/axya) |
| Quotebeam | Закупка компонентов автоматики (не цеха) | $3,57M | [CB Insights](https://www.cbinsights.com/company/quotebeam) |
| FAB.AI | LLM для фабрикации и квот | раунды **не найдено** | [F&M](https://fabricatingandmetalworking.com/ai-quoting-software-uptool/) |
| Маркетплейсы | Xometry $686,6M выручки 2025 (+26 %); Protolabs ~$501M; Fictiv куплен MISUMI за $350M | — | [StockAnalysis](https://stockanalysis.com/stocks/xmtr/revenue/), [3DPrint.com, 13.02.2026](https://3dprint.com/323826/3d-printing-financials-protolabs-reports-a-steady-2025-as-digital-manufacturing-and-metal-printing-gain-ground/), [FreightWaves, 17.04.2025](https://www.freightwaves.com/news/fictiv-acquired-for-350m-by-japanese-components-supplier) |

**Плотность:** квотинг для machine/fab shops — **несколько стартапов + один укоренившийся ($45M) + маркетплейсы**; за 2026 г. пришли венчурные деньги (Uptool, Atira, Roadrunner). Order entry/статусы заказов для цехов как «ИИ-сотрудник» — почти пусто (Workist работает с крупными, Esker/Conexiom — enterprise).

## 5. Доказательства готовности платить

- Paperless Parts: 800+ платящих цехов, позиционирует цену как «минимум 3x ROI» ([Facts](https://www.paperlessparts.com/facts/)). Кейсы: Jax Precision — квота 2 дня → ~1 час, +300 % выручки, 8+ ч/нед экономии ([кейс](https://www.paperlessparts.com/case-studies/jax-precision-grows-revenue-by-300-triples-customer-base-with-paperless-parts/)); Harris Mfg — неделя → день, 3–5 ч/нед, 5x пропускная способность ([кейс](https://www.paperlessparts.com/case-studies/harris-manufacturing-doubles-quote-turnaround-speed-reveals-critical-profit-margin-insights/)); Vaupell — «20 квот за время одной» ([MMS, 2021](https://www.mmsonline.com/articles/when-it-comes-to-rfq-response-time-is-money)).
- Atira: Robel экономит 95 ч инженеров на квоту; 5 клиентов со 100+ пользователями ([Fortune, 03.09.2026](https://fortune.com/2026/09/03/exclusive-german-ai-startup-atira-raises-17-5-million-to-unclog-the-paperwork-bottleneck-in-industrial-dealmaking/)).
- CalcuQuote: PRIDE Industries −40 % время RFQ; MW.FEP +33 % объём квот ([Elisa IndustrIQ](https://www.elisaindustriq.com/calcuquote)).
- Ценовой потолок: SaaS-квотинг стоит $300–750/мес за команду — ориентир Океан Тех $5 тыс./мес в 7–15 раз выше; оправдать можно только замещением ставки ($110–120 тыс./год), а не «софтом».

## 6. Размер рынка и покупатель

**США — заведения с 50–999 сотр.** (Census CBP 2023, [cbp23us.zip](https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip), выпуск 05.2025):
- Machine shops 332710: 17 156 заведений, 223 тыс. занятых; 50–999 сотр. — **880** (614 / 245 / 16 / 5).
- Fabricated metal 332 целиком: 53 790; 50–999 — **6 876**.
- Plastics 3261: 9 636; 50–999 — **3 410**.
- Converted paper/упаковка 3222: 3 411; 50–999 — **1 606**.
- Printing 323: 22 301; 50–999 — **1 591**.
- Semiconductor & electronic components 3344 (вкл. PCB/EMS): 3 686; 50–999 — **986**.
- **Итого США ≈ 14 500 заведений 50–999 сотр.** (установления, не фирмы).

**ЕС-27, предприятия 50+ сотр.** (Eurostat sbs_sc_ovw, 2023, обновл. 01.09.2026, [API](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_sc_ovw?geo=EU27_2020&nace_r2=C25&indic_sbs=ENT_NR&size_emp=50-249&time=2023&format=JSON)): C25 металл — 10 937 (50–249) + 1 444 (250+); C22 пластик — 4 900 + 1 430; C26 электроника — 2 120 + 685; C18 печать — 1 309 + 180. **Итого ≈ 23 000.** Всего предприятий C25 — 412 707, занятых 3,7 млн ([sbs_ovw_act](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?geo=EU27_2020&nace_r2=C25&indic_sbs=ENT_NR&time=2023&format=JSON)).

**Кто покупает:** в цехах до 150 чел. — владелец/GM (он же часто главный estimator); 150–2000 — VP Sales / Director of Sales Ops, COO; в EMS — VP Supply Chain + Quoting Manager.

**Где искать:** NTMA — 1 200 компаний, $8B продаж ([ntma.org/about](https://ntma.org/about/)); PMPA — число членов **не найдено**; IMTS 14–19.09.2026, Чикаго — 90 000 посетителей, 2 000+ экспонентов (план, [imts.com](https://www.imts.com/show/abouttheshow.cfm)); FABTECH 2025 — 42 000 посетителей, 1 500+ экспонентов ([SME, 09.2025](https://www.advancedmanufacturing.org/news-desk/events/fabtech-2025-in-chicago-was-an-overwhelming-success/article_56abf3b1-e407-4e31-935f-aa4dcbc3ebc0.html)); EMO Hannover 2025 — 80 000 посетителей, 1 600+ экспонентов ([OEM Update](https://www.oemupdate.com/emo-hannover-2025/emo-2025-in-hannover-showcases-automation-ai-and-global-manufacturing-innovations/)); MMS Top Shops; пользовательские группы ECI/Epicor.

## 7. Риски

1. **Чертежи и инженерная оценка.** Цена зависит от допусков, материала, крепления, станочного времени — LLM/vision ошибается, ошибка = убыточный заказ. Все игроки (Paperless, Uptool, Atira) оставляют цену человеку; агент реально закрывает «до» и «после» расценки. Для сложной механообработки полный цикл агентом пока недоказуем.
2. **Консервативность.** Владельцы-инженеры 55+, недоверие к облаку, on-prem ERP; 10–12 недель типичного внедрения даже у Paperless ([Facts](https://www.paperlessparts.com/facts/)). Цикл продажи долгий, чек $5 тыс./мес для цеха 50–100 чел. — заметная часть фонда.
3. **Разнородность ERP.** 15 систем, старые версии, on-prem — каждая интеграция отдельный проект; без интеграции нет «обновить ERP и передать дальше».
4. **Конкуренция усиливается:** за 8 месяцев 2026 г. $50M+ венчурных денег в квотинг (Uptool, Roadrunner, Atira) плюс AI-фичи у самих ERP (JobBOSS² AI BOM).
5. **Низкий ценовой якорь** софта ($300–750/мес) — придётся продавать «роль», а не инструмент.

## 8. Оценка (1–5)

| Критерий | Балл | Комментарий |
|---|---|---|
| Объём повторяемой работы | 4 | Разбор RFQ, ввод PO, статусы — ежедневно, измеримо; но ядро (расценка) агенту не отдать |
| Стоимость труда | 3 | Estimator $79k медиана, CS/order entry $45–46k; фронт-офис цеха 50–100 чел. — 2–4 ставки |
| Простота внедрения | 2 | 15 ERP, on-prem, чертежи, 10–12 нед. внедрения у лидера |
| Слабость конкуренции | 2 | Квотинг: укоренившийся игрок + 3 свежих раунда 2026; order entry/статусы — свободнее (3–4) |
| Доступность покупателя | 4 | Владелец решает сам; NTMA, IMTS, FABTECH, MMS — плотные каналы |
| Доказанная готовность платить | 3 | 800+ цехов платят за квотинг, но $300–750/мес; чек $5k/мес не подтверждён ни у кого в SMB-сегменте |
| **Итого** | **18/30** | |

**Вердикт.** Как первая ниша — **условно годится, но не для «квотинга по чертежам»**: там уже есть Paperless Parts и свежие венчурные стартапы, а ценность упирается в инженерную расценку, которую агент не заменит. Лучший подсегмент — **EMS и контрактная электроника 100–1000 сотр.** (RFQ = BOM в Excel, а не чертёж; структурированные данные, уже есть квотинг-софт, высокая частота RFQ и перекотировок) и/или **роль «order entry + подтверждение сроков + статусы»** для цехов 100–500 чел. на JobBOSS²/Epicor/ProShop, где конкуренции с ИИ-агентами почти нет. Чек $5 тыс./мес реалистичен только для предприятий от ~150 сотр.; ниже — рынок приучен к $300–750/мес за софт.
