# 07. B2B-туризм и гостеприимство (туроператоры/DMC, TMC, MICE, отельные group sales)

Дата: 2026-09-10. Все ссылки открыты в этот день, если не указано иное. «Не найдено» = источник с числом не найден, оценка не делалась.

## 1. Повторяющаяся работа

| Роль | Что делает (по O*NET/вендорам) | Объём | Каналы |
|---|---|---|---|
| Reservations / ticket agent (TMC, туроператор) | Принимает запрос, подбирает рейс/отель, считает тариф, бронирует в GDS, делает изменения/возвраты, выставляет счёт ([O*NET 43-4181](https://www.onetonline.org/link/summary/43-4181.00)) | Агенты тратят **>8 ч/нед** на ручную обработке email-запросов; пилот Sabre у крупного TMC — **~3 500 email-запросов/мес** ([Sabre Agency Concierge](https://www.sabre.com/agency-mosaic/experience-suite/agency-concierge/)) | Email (основной), телефон, Slack/WhatsApp ([Amgine](https://amgine.ai/)), GDS |
| Travel consultant / туроператор, DMC | Уточняет даты/бюджет, собирает маршрут, считает стоимость, продаёт пакет, ведёт клиента и поставщиков ([O*NET 41-3041](https://www.onetonline.org/link/summary/41-3041.00)) | Кол-во запросов/день — не найдено. Кейс Maya: Adventura Colombia −70% времени на создание маршрута ([Maya blog](https://www.mayatravel.ai/blog/8-tech-tools-dmcs-should-know-about-in-2026)) | Email, сайт-чат, WhatsApp, B2B-порталы |
| Group sales coordinator / RFP responder (отель) | Читает RFP, проверяет доступность залов/номеров, готовит предложение, ведёт follow-up, вносит в S&C | **50–100 входящих RFP/мес** на сейлз-менеджера; **55% RFP** остаются без ответа (данные Groups360) ([Hippo Rev, 15.04.2026](https://hipporev.ai/blog/4-stage-leak-analysis-hotel-rfp-response)); 83% планировщиков ждут ответ ≤4 дней ([Cvent, 07.11.2024](https://www.hospitalitynet.org/news/4124537.html)) | Cvent Supplier Network, email, веб-формы, телефон |
| Meeting/event planner (сторона покупателя) | Составляет RFP, сравнивает биды, договаривается с отелями ([O*NET 13-1121](https://www.onetonline.org/link/summary/13-1121.00)) | 54% уже используют AI при сорсинге: сравнение бидов 53%, создание RFP 47% (там же, Cvent) | Cvent, email |

Что уже автоматизируют: черновики ответов на RFP из профиля CSN (Cvent Response Assistant), автоответы на email-запросы бронирования (Sabre Agency Concierge, Amgine), чат-ответы туристам 24/7 (Maya), пост-букинг изменения (Navan Ava — 60% обращений).

## 2. Люди и стоимость труда (США)

| Роль (SOC) | Занятость | Медиана $/год | Источник |
|---|---|---|---|
| Travel agents 41-3041 | 65 700 (2024, проекция); 55 110 (OEWS май 2025) | $50 160 (2025) | [O*NET](https://www.onetonline.org/link/summary/41-3041.00), [NueCareer/BLS](https://nuecareer.com/careers/travel-agent) |
| Reservation & ticket agents 43-4181 | 131 900 (2024) | $44 390 (2025) | [O*NET](https://www.onetonline.org/link/summary/43-4181.00) |
| Meeting/event planners 13-1121 | 155 800 (2024) | $61 160 (2025) | [O*NET](https://www.onetonline.org/link/summary/13-1121.00) |
| Hotel group coordinator | — | $46 000 (медиана, 5 309 профилей, обновлено 06.12.2023) | [PayScale](https://www.payscale.com/research/US/Job=Hotel_Group_Coordinator/Salary) |
| Hotel sales manager | — | ~$61 700 медиана, 25–75 перцентиль $53 500–72 000 (по выдаче поиска, страница не открылась) | [ZipRecruiter](https://www.ziprecruiter.com/Salaries/Hotel-Sales-Manager-Salary) |

Европа: в ЕС в турагентствах/туроператорах (NACE N79) занято **~0,4 млн**, в размещении (I55) **>2,1 млн** (2021) ([Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Tourism_industries_-_employment)); оборот N79 — **€159 млрд** (2023) ([Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Tourism_industries_-_economic_analysis)). GBTA: 86% бизнес-тревел-профи получили рост базовой зарплаты, но 54% называют «непривлекательные зарплаты» барьером найма ([GBTA/BTM, 30.04.2024](https://thebusinesstravelmag.com/gbta-survey-shows-committed-workforce-and-rising-salaries/)).

Сколько на компанию 50–2000 чел.: точных отраслевых бенчмарков не найдено. Ориентир из вендоров: один сейлз-менеджер отеля = 50–100 RFP/мес; full-service отель 400+ номеров — отдел продаж из нескольких человек ([Hippo Rev](https://hipporev.ai/)).

Вывод по стоимости: медианы $44–61 тыс. — целевая цена $5 тыс./мес ($60 тыс./год) равна одной полной ставке. Окупаемость есть только при замещении ≥2 FTE или при аргументе «выигранные сделки» (ниже).

## 3. Системы и стандартизация

- **GDS**: Amadeus, Sabre, Travelport — в O*NET перечислены Amadeus Altea/CRS, Sabre, Worldspan, Apollo ([O*NET 43-4181](https://www.onetonline.org/link/summary/43-4181.00), [41-3041](https://www.onetonline.org/link/summary/41-3041.00)). Sabre выпустил **MCP-сервер и agentic-API** (переиздание билетов, обмены), первый прод-деплой — Linex Travel, 17.06.2026 ([Sabre](https://www.sabre.com/resources/newsroom/sabre-scales-agentic-ai-deployment-as-ultra-group-expands-globally-under-linex/)). Это снижает барьер интеграции, но одновременно даёт Sabre собственный AI-слой.
- **TMC-платформы**: Navan, Spotnana (на нём построен Otto), Amadeus Cytric, SAP Concur. Amgine интегрируется «поверх существующих систем» у BCD, FCM, CTM, JTB, Christopherson ([Amgine](https://amgine.ai/)).
- **Отели**: Cvent Supplier Network (155 тыс. планировщиков, 8,3 млн событий; ([Cvent](https://www.cvent.com/en/supplier-venue))), S&C-системы Opera/Amadeus Delphi, Thynk, Cendyn, Tripleseat, Event Temple; RFP-инструменты Proposales, MeetingPackage, Sertifi ([HotelTechReport](https://hoteltechreport.com/meetings-and-events/hotel-rfp-software)). RFP приходят через Cvent, email и веб-формы одновременно — единого формата нет.
- **DMC/туроператоры**: Tourplan, Ezus, FareHarbor, Ventrata, Zaui, Rezdy ([TourConnect](https://www.tourconnect.ai/resources/which-type-of-ai-is-best-for-inbound-travel-operators), [O*NET](https://www.onetonline.org/link/summary/41-3041.00)) — самый фрагментированный сегмент, много закрытых API.

Степень стандартизации: TMC — высокая (GDS + структурированные PNR), отели — средняя (Cvent как хаб, но собственные S&C), DMC — низкая.

## 4. Кто уже продаёт ИИ-агентов

| Игрок | Сегмент | Деньги/дата | Цена |
|---|---|---|---|
| **Navan (Ava)** | TMC/корп. тревел | IPO окт. 2025; Q2 FY27 выручка $233 млн (+35%), Ava — 60% обращений, 12 500 клиентов ([Investing.com, 09.09.2026](https://www.investing.com/news/company-news/navan-q2-fy27-slides-35-revenue-growth-ai-drives-margins-93CH-4894707)) | внутри платформы |
| **Sabre Agency Concierge / MCP** | TMC | публичная компания; пилот 3 500 email/мес ([Sabre](https://www.sabre.com/agency-mosaic/experience-suite/agency-concierge/)) | не раскрыта |
| **Amgine** | TMC (email/Slack/group air → бронь) | клиенты BCD, FCM, CTM, JTB и др. ([Amgine](https://amgine.ai/)); фандинг — не найдено | не раскрыта |
| **Otto** | unmanaged бизнес-тревел | seed $6 млн, Madrona + Direct Travel, 02.09.2024 ([FinTech Global](https://fintech.global/2024/09/02/ai-travel-assistant-startup-otto-secures-6m-seed-round-led-by-madrona-ventures/)) | не найдено |
| **Mindtrip** | B2C-планирование + Mindtrip for Hotels | $19 млн всего (seed $7 млн 2023, A $12 млн 2024); Capital One/United Ventures 08.12.2025 ([Yahoo](https://finance.yahoo.com/news/mindtrip-unveils-ai-travel-events-140300012.html)); партнёрство с Sabre/PayPal по agentic-бронированию, февр. 2026 ([Skift](https://skift.com/2026/02/12/sabre-paypal-mindtrip-agentic-ai-travel-booking-announcement/)) | — |
| **Cvent (CventIQ Response Assistant)** | отельные RFP | часть Cvent, AI-ответы на custom questions с 11.06.2024 ([Cvent](https://www.cvent.com/en/press-release/cvent-unveils-new-ai-innovations-hoteliers-and-hospitality-professionals)); в 2026 — предзаполнение предложений, бейдж Top Responder | в подписке |
| **Hippo Rev** | отельные group sales (inquiry→proposal) | фандинг не найдено; 6-нед. бесплатный пилот, custom pricing ([Hippo Rev](https://hipporev.ai/)) | custom |
| **Mikla.ai** | лиды/RFP для отелей и venue | 200+ клиентов, фандинг не найдено ([Mikla](https://mikla.ai/)) | $149–499/мес |
| **Maya (Бельгия)** | туроператоры/DMC, чат + email | 35+ клиентов в 20 странах, субсидия Flanders; VC-раунд не найдено ([Maya](https://www.mayatravel.ai/)) | не раскрыта |
| **TourConnect AI** | DMC/inbound: Itinerary Assist, Booking Automation | фандинг не найдено ([TourConnect](https://www.tourconnect.ai/resources/which-type-of-ai-is-best-for-inbound-travel-operators)) | не раскрыта |
| Proposales, MeetingPackage, Thynk и др. | RFP/proposal SaaS для отелей | Proposales — $410 тыс., 2018 | $1–11 за номер/мес ([HotelTechReport](https://hoteltechreport.com/meetings-and-events/hotel-rfp-software)) |

Контекст: за апр. 2025 – март 2026 40 hospitality-tech стартапов привлекли >$1 млрд, но лидеры — PMS (Mews $300 млн) и гостевые платформы (Canary, Duve и др. $152,6 млн); стартапов по group sales/RFP в списке нет ([Hotel Dive, 14.04.2026](https://www.hoteldive.com/news/hospitality-tech-attracts-1b-in-funding-pms-ai-leaders/817439/)).

**Плотность конкуренции:** TMC — крупные $50M+ (Navan, Sabre, Amgine с топ-TMC). Отельные RFP — Cvent (платформенный владелец канала) + 2–3 стартапа. DMC/туроператоры — 2–3 небольших стартапа без раскрытых раундов.

## 5. Доказательства, что платят

- Navan: маржа non-GAAP выросла на 200 б.п. до 75% за счёт Ava ([Investing.com, 09.09.2026](https://www.investing.com/news/company-news/navan-q2-fy27-slides-35-revenue-growth-ai-drives-margins-93CH-4894707)) — платит сама платформа, не TMC-клиент.
- Hippo Rev, Wyndham Indianapolis West (400+ номеров): ответ на RFP 45 → 3 мин, +25% win rate, −70% админ-времени ([Hippo Rev](https://hipporev.ai/)). Цены не раскрыты.
- Mikla: $149–499/мес, «+40% бронирований за 90 дней, 10+ ч/нед экономии» ([Mikla](https://mikla.ai/)) — низкий чек, венью/свадьбы.
- Maya: 90% вопросов закрыты автономно (Frenchly), 3x конверсия (Zoover) ([Maya](https://www.mayatravel.ai/)).
- Аргумент скорости: 72% сделок уходят первому ответившему; автоматизация RFP сократила контракт с 45 до 14 дней ([Infor/HospitalityNet](https://www.hospitalitynet.org/opinion/4133323/how-ai-is-transforming-the-hotel-commercial-engine-group-sales-revenue-management-and-unified-strategy)); ответ в 24 ч — +70% к вероятности выигрыша ([Hippo Rev, 15.04.2026](https://hipporev.ai/blog/4-stage-leak-analysis-hotel-rfp-response)).
- Кейсов с оплатой $5 тыс./мес за «роль» — не найдено; рынок привык к цене за номер/за лид.

## 6. Размер и где искать

- США: number of travel agencies/hotels по Census — не найдено (API требует ключ). AHLA представляет 32 000+ отелей ([AHLA](https://www.ahla.com/about-ahla)); Groups360 — «200 тыс. объектов по миру» ([Groups360](https://www.groups360.com/)). Занятость по ролям — п. 2.
- Европа: ECTAA заявляет ~70 000 турагентств и туроператоров, ~500 000 сотрудников, €170 млрд оборота (по выдаче поиска, [ECTAA membership](https://www.ectaa.org/en/membership)); Eurostat: 0,4 млн занятых в N79.
- Число компаний 50–2000 чел. — не найдено (Apollo на бесплатном плане закрыт).
- Кто покупает: отель — Director of Sales / DOSM, управляющая компания; TMC — COO/Head of Operations; DMC — владелец/GM.
- Где найти: IMEX America, Лас-Вегас, 13–15.10.2026 ([IMEX](https://america.imexevents.com/)); WTM London, 3–5.11.2026, 4 000+ экспонентов, 5 500+ байеров ([WTM](https://www.wtm.com/london/en-gb.html)); ITB Berlin, 16–18.03.2027 ([ITB](https://www.itb.com/en/)); GBTA Convention, Чикаго, 3–5.08 ([GBTA](https://www.gbta.org/convention/)); HSMAI Commercial Strategy, Cvent Connect.

## 7. Риски

- **Сезонность**: в ЕС треть ночёвок — июль-август, пик/дно = 3,7x ([Eurostat 2024](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Seasonality_in_tourism_demand)) — нагрузка и бюджеты DMC волнообразны, помесячная подписка «за роль» тяжела в низкий сезон.
- **Низкая маржа/чеки**: RFP-софт для отелей стоит $1–11 за номер/мес; Mikla $149–499/мес — $5 тыс./мес выглядит дорого для одиночного отеля, реалистично только для управляющих компаний/сетей и TMC.
- **Фрагментация систем**: Cvent — закрытый канал с собственным AI; GDS требуют сертификации; DMC сидят на Tourplan/Ezus с ограниченными API.
- **Ответственность за ошибки**: неверный тариф в предложении или ошибочная бронь = прямой убыток; статистика ADM/штрафов не найдена (IATA-страница недоступна). Планировщики жалуются на «шаблонные» AI-ответы — статья Costar/Hotel-Online недоступна (403), тезис не проверен.
- **Платформенный риск**: Cvent, Sabre и Navan встраивают агентов в канал — независимому вендору остаётся ниша «между системами».

## 8. Оценка

| Критерий | Балл |
|---|---|
| Объём повторяемой работы | 4 |
| Стоимость труда | 2 |
| Простота внедрения | 2 |
| Слабость конкуренции (5 = пусто) | 2 |
| Доступность покупателя | 4 |
| Доказанная готовность платить | 3 |
| **Итого** | **17/30** |

**Вердикт.** Как первая ниша — не годится: труд дешёвый (медиана $44–61 тыс.), а канал уже занят платформами (Cvent, Sabre, Navan) и 2–3 стартапами с ценой в разы ниже $5 тыс./мес. Лучший подсегмент, если всё же заходить, — **group sales / RFP-responder для управляющих компаний и full-service отелей с несколькими объектами** (боль измерима: 55% RFP без ответа, 72% сделок первому ответившему, 50–100 RFP/мес на менеджера), с продажей на уровне УК, а не отеля. Второй кандидат — **квотирование у инкаминг-DMC в Европе** (конкуренция слабее), но там сезонность, низкие чеки и закрытые системы. Держать как нишу №2–3 после проверки более дорогих отраслей.
