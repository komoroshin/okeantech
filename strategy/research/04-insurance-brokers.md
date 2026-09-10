# 04 — Страховые брокеры, агентства и MGA (коммерческое P&C, США/ЕС)

*Дата исследования: 2026-09-10. Все цифры — с источником; где источник не найден — так и написано.*

## 1. Повторяющаяся работа

**Роли и задачи (брокер/агентство):**
- **Account Manager / CSR (commercial lines)** — входящие запросы по email/телефону: сертификаты страхования (COI, форма ACORD 25), эндорсменты, вопросы по продлению, переписка с страховщиком; между звонками — выпуск COI и обработка эндорсментов ([Sonant, 2026](https://www.sonant.ai/blog/insurance-account-manager-job-description)).
- **Submission intake (новый бизнес/продления)** — сбор данных клиента в ACORD 125 (обязательная «обложка» любой коммерческой заявки) + 126/140/127/130 по линиям, loss runs, рассылка по страховщикам, сравнение котировок, подготовка предложения ([Sonant ACORD guide](https://www.sonant.ai/blog/acord-forms); [SortSpoke](https://sortspoke.com/blog/acord-125-vs-126-vs-140)).
- **Underwriting assistant (MGA)** — очистка входящих заявок от брокеров, триаж по аппетиту, занесение в PAS.
- **Claims intake (FNOL)** — приём убытка, уточнение, передача страховщику/TPA.

**Объёмы:**
- COI: средняя агентская практика — ~120 запросов/мес на среднее агентство; 15–25 мин на рутинный запрос, до 45 мин при неполных данных; полный цикл ~52 мин, из них генерация формы 5–8 мин, остальное — сбор/проверка/логирование в AMS ([US Tech Automations, 2026-06-20](https://ustechautomations.com/resources/blog/certificate-of-insurance-request-handling-for-agencies-roi-analysis-2026); [там же](https://ustechautomations.com/resources/blog/insurance-certificate-of-insurance-issuance-pain-solution-2026)).
- Документирование звонков: 1–2 ч/день на CSR; «связующая» работа (перенабор в AMS, догон документов, голосовые) — 10–16 ч/день на сервис-команду из 4 человек ([Sonant, 2026-06-28](https://www.sonant.ai/blog/reduce-manual-workload-insurance)).
- Заявки (submissions): ~60% заявок у страховщика/MGA никогда не котируются, ~10% биндятся; 70%+ приходят неполными и требуют хотя бы один круг уточнений ([Canadian Underwriter, 2026-07-07](https://canadianunderwriter.ca/2026/07/07/handbook-what-makes-a-great-submission/)). Среднее время «очистки» заявки у крупного MGA до автоматизации — ~32 мин ([FurtherAI case](https://www.furtherai.com/customers/submissions-processing-ai)).
- Чистая заявка получает ответ за 5–10 рабочих дней, неполная — 2–4 недели ([Wells Insurance](https://www.wellsins.com/resources/understanding-the-commercial-insurance-submission-and-underwriting-process)).

**Что уже автоматизируют:** intake и извлечение данных из ACORD/SOV/loss runs (Sixfold, Cytora, FurtherAI, Kalepa, Roots), триаж заявок (Federato), голос/email-приём FNOL и сервисных запросов (Strada, Sonant), COI-генерация (Roots, V7, нишевые SaaS $49–499/мес), бухгалтерия брокера (Comulate). Prospecting-агенты — Zywave.

## 2. Люди и стоимость

| Показатель | Значение | Источник |
|---|---|---|
| Занятость, агентства и брокерские конторы (NAICS 524210) | 1 003 900 (2024) → 1 051 300 (2034, +4,7%) | [BLS EP via plainworkforce](https://plainworkforce.com/industry/insurance-agencies-and-brokerages) |
| В NAICS 524210: CSR | 109 800 чел., медиана $46 510 | [BLS OES May 2023](https://www.bls.gov/oes/2023/may/naics5_524210.htm) |
| В NAICS 524210: клерки по полисам/убыткам | 69 510, $49 320 | там же |
| В NAICS 524210: офис/админ всего | 295 770 (31% штата отрасли), $48 960 | там же |
| В NAICS 524210: андеррайтеры | 31 750, $83 420 | там же |
| Insurance sales agents (вся экономика) | 572 600 раб. мест, медиана $62 280 (May 2025), рост +3% к 2035 | [BLS OOH, обновл. 2026-08-27](https://www.bls.gov/ooh/sales/insurance-sales-agents.htm) |
| Claims & policy processing clerks (вся экономика) | медиана $49 230 (2025), занятость −4% к 2034 | [BLS OES](https://blsmon1.bls.gov/oes/current/oes439041.htm) |
| Insurance underwriters (вся экономика) | медиана $81 370 (May 2025), −4% к 2035 | [BLS OOH](https://www.bls.gov/ooh/business-and-financial/insurance-underwriters.htm) |
| Зарплата Commercial Lines Account Manager | не найдено в BLS (отдельного кода нет); прокси — CSR/агент выше | — |

**Оценка на агентство 50–2000 чел.:** по структуре отрасли ~31% штата — сервисно-административные роли → на 100 сотрудников ≈ 30 CSR/клерков/ассистентов с медианой ~$47–49K (полная стоимость с налогами/льготами ~$60K — *моя оценка, не источник*). Важно: $5K/мес = $60K/год ≈ 1 полностью загруженный CSR. Окупаемость требует замещения ≥1,5–2 FTE на процесс.

## 3. Системы и стандартизация

- **AMS у агентств:** Applied Epic (enterprise, 450+ IVANS-интеграций, $250–350/польз./мес), Vertafore AMS360 ($180–260), HawkSoft ($95–140; малые агентства), EZLynx, NowCerts ([InsuranceIndustry.ai](https://insuranceindustry.ai/property-casualty-agency-management-systems-a-comprehensive-guide-for-independent-insurance-agents/); [QuoteSweep, 2026-03-21](https://www.quotesweep.com/blog/ams-comparison-2026)). Доли рынка от первичного источника — **не найдено** (вендорские блоги ссылаются на опрос IIABA, проверить не удалось).
- **Стандарт данных:** формы ACORD (125/126/127/130/140, COI — ACORD 25) — единый формат обмена брокер↔страховщик↔MGA ([Sonant](https://www.sonant.ai/blog/acord-forms)). Это сильный плюс: intake структурирован. Минус: данные приходят PDF/Excel/email, в каждом страховщике — свой портал (двойной ввод) ([Covera](https://www.covera-agents.com/)).
- **Интеграция:** Applied купил Cytora (2025-09-10) для «digital roundtrip» — подачи/продления/убытки внутри своей экосистемы ([FinTech Global](https://fintech.global/2025/09/10/insurance-ai-boosted-as-applied-systems-buys-cytora/)); Zywave запускает MCP-сервер Apex для Claude/ChatGPT/Copilot ([FinTech Global, 2026-07-31](https://fintech.global/2026/07/31/zywave-expands-ai-platform-to-reshape-insurance-growth/)). PAS у MGA — разнородные; единого стандарта не найдено.

## 4. Кто уже продаёт

| Компания | Фокус | Раунд / дата | Покупатель |
|---|---|---|---|
| Federato | RiskOps, триаж заявок | Series D $100M, 2025-11-18 (Goldman), всего $180M+, выручка ×3 за год | страховщики/MGA ([GS](https://am.gs.com/en-us/advisors/news/press-release/2025/federato)) |
| Sixfold | «AI-андеррайтер», intake | Series B $30M, 2026-01-29 (Brewer Lane, Guidewire); >1M заявок; Zurich NA 200+ UW, до 2 ч/заявку; Skyward −35% время котировки | страховщики ([Sixfold](https://www.sixfold.ai/content/post/series-b-ai-underwriter)) |
| Gradient AI | UW/claims-предикция | Series C $56M, 2024-07-30 | страховщики ([BusinessWire](https://www.businesswire.com/news/home/20240730811573/en/)) |
| FurtherAI | intake, сравнение полисов, claims | Series A $25M, 2025-10-07 (a16z), всего $30M; клиенты Accelerant, MSI, Leavitt Group | MGA + брокеры ([IJ](https://www.insurancejournal.com/news/national/2025/10/09/843205.htm)) |
| Kalepa | Copilot для андеррайтеров | Series A $14M, 2021-09-03; James River 2026-02-10 | E&S-страховщики ([Kalepa](https://kalepa.com/news-posts/kalepa-raises-14m-series-a-led-by-inspired-capital)) |
| Roots Automation | Digital Coworker, COI, документы | Series B $22,2M, 2024-09-17; 35 клиентов-страховщиков | страховщики ([FinTech Global](https://fintech.global/2024/09/18/roots-automation-bags-22-2m-in-series-b-to-drive-ai-innovation-in-insurance/)) |
| Cytora | intake, digitised risk | куплена Applied Systems 2025-09-10; ранее £25M Series B | встроена в AMS |
| Comulate | бухгалтерия брокера | Series B $20M, 2025-02-11; 8-значная выручка; IMA, Baldwin, Hilb | крупные брокеры ([PRN](https://www.prnewswire.com/news-releases/comulate-adds-bond-and-workday-in-20m-series-b-to-transform-insurance-with-ai-302373362.html)) |
| Zywave (incumbent) | AI-агенты prospecting; quoting/renewal — в 2026 | 35+ early adopters, 2026-02-18 | брокеры ([IJ](https://www.insurancejournal.com/news/national/2026/02/23/858815.htm)) |
| Strada (YC S23) | voice/email FNOL, сервис, котировки | ~$4M (дата не найдена); Clearcover, Foxquilt | carriers/MGA/брокеры ([Strada](https://www.getstrada.com/)) |
| Sonant AI | AI-ресепшен для агентств | $4,7M к 2025-09; 100+ агентств | малые агентства ([Tracxn](https://tracxn.com/d/companies/sonant-ai/__Nk8qIUj2-7Hmif1ckrVlj61LtpFCAxriHOfzL-BViYg)) |
| Covera (YC F26), Mulligan, Panta | агенты для брокеров: intake, quoting, COI, collections | YC-стадия, команда 2 чел. | брокеры ([YC](https://www.ycombinator.com/companies/covera)) |
| Indemn | conversational агенты (чат/voice/email) для MGA/carriers | $3,8M всего | MGA/carriers ([IJ](https://www.insurancejournal.com/news/east/2024/02/01/758902.htm)) |
| Sedgwick (TPA) | Sidekick Agent — внутренний | +30% эффективность claims | — ([Sedgwick](https://www.sedgwick.com/press-release/sedgwick-optimizes-claim-workflows-with-ai-application-sidekick-and-microsoft-integration/)) |

*Nayya — benefits-навигация для HR, не P&C; EvenUp — юртех (Series E $150M, $2B+), не страхование.*

**Плотность:** сторона **страховщик/MGA (underwriting intake)** — **крупные $50M+** (Federato, Sixfold, Gradient, Roots, Cytora-in-Applied). Сторона **брокер/агентство (сервис: COI, intake-догон, продления, FNOL)** — **1–3 стартапа seed-стадии** (Covera, Strada, Sonant, Mulligan) + incumbents анонсировали, но quoting/renewal-агенты ещё не выпущены.

## 5. Доказательства оплаты

- MGA $1,5B премии: время очистки заявки 32 мин → 1 мин, 2 000+ часов за 3 мес, 99% точность; заявленный ROI 646% на SOV-intake ([FurtherAI](https://www.furtherai.com/customers/submissions-processing-ai)). Брокеры на FurtherAI: Cornerstone 240 ч/мес, Trustpoint 385 ч/мес, Excalibur 160 ч/мес ([FurtherAI blog](https://www.furtherai.com/blog/platforms-national-brokers-automate-submission-intake)) — цифры вендора.
- Comulate: 350 000 часов возвращено клиентам, выручка 8-значная ([PRN, 2025-02-11](https://www.prnewswire.com/news-releases/comulate-adds-bond-and-workday-in-20m-series-b-to-transform-insurance-with-ai-302373362.html)) — брокеры платят за back-office AI.
- Strada: 80% containment, −70% handle time (сайт вендора).
- Цены: COI-SaaS $49–499/мес; «базовые» AI-пакеты для агентств $5–15K/мес, продвинутые $15–50K ([Monetizely](https://www.getmonetizely.com/articles/how-much-does-an-insurance-ai-agent-cost-for-claims-processing)); рекомендация для агентств на 3–10 продюсеров — $400–1 500/мес ([Ascero](https://asceroai.com/guides/best-ai-tools-insurance-agents-2026)). Опубликованных цен Sixfold/Federato/FurtherAI — **не найдено**.
- Ручной COI у среднего агентства стоит всего $3,6–6K/год труда ([US Tech Automations](https://ustechautomations.com/resources/blog/certificate-of-insurance-request-handling-for-agencies-roi-analysis-2026)) — **один COI-процесс не окупает $5K/мес**; продавать надо пакет (intake + COI + продления).

## 6. Размер и где искать

- США: 39 000 независимых P&C-агентств, 76% — small/medium → ~9 400 large/jumbo (пороги Big I не найдены) ([Big I AUS 2024](https://www.independentagent.com/agency-universe-study/)). Независимый канал ≈ 60% коммерческих P&C-премий (Big I через [UTA](https://ustechautomations.com/resources/blog/automate-applied-epic-vs-ams360-for-mid-sized-agencies-2026)).
- MGA США: 850+ в статотчётности + ~250 малых ≈ 1 100; премии $128B (2025, +12%) ([Carrier Management, 2025-07-09](https://www.carriermanagement.com/news/2025/07/09/277134.htm); [Conning, 2026-07-28](https://www.conning.com/about-us/news/ir-pr---mga-2026)).
- Европа: ~800 000 посредников ЕС, подавляющее большинство — микро ([BIPAR](https://www.bipar.eu/en/intermediaries)); Германия — 46 885 Versicherungsmakler (2025-10-01) ([Pfefferminzia](https://www.pfefferminzia.de/top-thema-assekuranz-der-zukunft/dihk-statistik-vermittlerzahlen-2025-ein-vertriebszweig-mit-rekordhoch/)); UK — ~1 800 фирм BIBA, 100 000+ сотрудников ([BIBA](https://www.biba.org.uk/)).
- Покупатель: COO / Head of Operations / Director of Client Service у брокера; Chief Underwriting Officer / Head of Ops у MGA. Где искать: Insurance Journal Top 100, WSIA/Target Markets (MGA), Applied Net / Vertafore Accelerate, BIBA, списки агентств-консолидаторов (Hilb, Baldwin, IMA, Leavitt).

## 7. Риски

- **Регуляторика:** NAIC Model Bulletin по ИИ принят в 24 штатах (на 08.2025), требует у страховщика программу управления ИИ и надзор за third-party вендорами — MGA/carriers будут требовать документацию и аудит ([H&K, 2025-05-20](https://www.hklaw.com/en/insights/publications/2025/05/the-implications-and-scope-of-the-naic-model-bulletin)). EU AI Act: высокий риск — только life/health pricing; P&C-сервисные агенты вне Annex III, но дедлайн обязательств 2026-08-02 повышает требования к документации ([AI Act Annex III](https://artificialintelligenceact.eu/annex/3/)).
- **Лицензии:** выдача котировок/консультирование — лицензируемая деятельность продюсера; агент должен оставаться «ассистентом» с human-in-the-loop.
- **E&O:** ошибка в COI/лимитах — прямая ответственность агентства; количественных данных по E&O-претензиям от ИИ — **не найдено**.
- **Консерватизм и данные:** «pilot purgatory» у страховщиков ([Sedgwick via IB](https://www.insurancebusinessmag.com/us/news/technology/carriers-stuck-in-pilot-purgatory-as-ai-fails-to-graduate--sedgwick-567339.aspx)); доступ к AMS через API ограничен вендорами (Applied/Vertafore строят свои агенты — риск lock-in и конкуренции с платформой).

## 8. Оценка

| Критерий | Балл | Комментарий |
|---|---|---|
| Объём повторяемой работы | **5** | 31% штата — сервис/админ; ACORD-стандарт; 60% заявок тонут в неполноте |
| Стоимость труда | **3** | CSR $46–49K, андеррайтер $81K; $5K/мес ≈ 1 FTE — нужна замена ≥2 FTE |
| Простота внедрения | **3** | Формы стандартные, но AMS-интеграции закрыты, порталы страховщиков разные |
| Слабость конкуренции | **2** | MGA/UW intake — $50M+ игроки; брокер-сервис — seed-стартапы + incumbents |
| Доступность покупателя | **4** | ~9 400 крупных агентств + ~1 100 MGA в США, публичные рейтинги и конференции |
| Доказанная готовность платить | **4** | Federato ×3 выручка, Comulate 8-значная, FurtherAI Series A от a16z за 6 мес |
| **Итого** | **21/30** | |

**Вердикт.** Как первая ниша — **годится с оговоркой**: спрос и платёжеспособность доказаны, работа стандартизована ACORD, но underwriting-intake для страховщиков/MGA уже занят капиталом $100M+ и туда с $5K/мес не зайти. Лучший подсегмент — **средние и крупные независимые агентства/брокеры (50–500 чел.) в США с пакетной ролью «Commercial Lines Service Assistant»**: intake-догон недостающих данных + COI + подготовка продлений в Applied Epic/AMS360, где конкуренты — 2–3 seed-стартапа, а incumbents ещё не выпустили servicing-агентов. Европу (UK/DE) ставить вторым шагом: много микро-посредников, разные стандарты вместо ACORD.
