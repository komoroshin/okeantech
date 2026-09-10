# 06. Дистрибуция медизделий, расходников, стоматологии, ветеринарии и фармы (независимые дистрибьюторы и производители среднего размера)

*Исследование для выбора первой отрасли «ИИ-сотрудников» Океан Тех. Дата: 2026-09-10. Все ссылки проверены в эту дату. Где данных нет — «не найдено».*

## 1. Какая повторяющаяся работа

**Роли:** customer service representative (CSR) / order entry clerk / inside sales. Задачи: приём заказа (email с PDF/Excel, факс, телефон, портал), сверка артикула и цены по контракту/GPO, проверка наличия и лицензии покупателя, ввод в ERP, подтверждение, статус/трекинг, возвраты и претензии, комплаенс-документы (сертификаты, лоты/UDI, DSCSA-транзакции в фарме).

**Объём:**
- Фарма-дистрибьюторы США (HDA Factbook 2024): в среднем **4 132 заказа на распредцентр в рабочий день**, 12 строк на заказ; 68% компаний используют автоматизированные методы (склад) — https://www.hda.org/newsroom/2025/september/hda-factbook-healthcare-distributors-continue-to-achieve-efficient-operations-in-2024/
- Mediq (европейский дистрибьютор медрасходников): **4 000 заказов в неделю** через Go Autonomous без роста штата — https://goautonomous.io/industries/medtech-and-healthcare/
- MEDRAD (Bayer): **70 000 заказов в год** в SAP, ~40% входящих PO автоматизировано Esker (2010) — https://www.newswire.com/news/esker-strengthens-its-presence-in-the-pharmaceutical-and-medical-171769
- Норма CSR: **один CSR — 10 минут на заказ из 50 строк**, максимум ~48 заказов за смену; в ERP ввод заказа — до 40 кликов и 10 экранов; >80% заказов у дистрибьюторов — повторные — https://distributionstrategy.com/transform-distributor-order-entry-with-ai/

**Каналы:** email+PDF, факс, телефон, EDI (у крупных клиентов и GPO), порталы. Доля факса именно в заказах дистрибьюторам — **не найдено**; общие цифры по здравоохранению США: факс ≈70% коммуникаций, 9 млрд факс-страниц в год — https://www.etherfax.net/why-healthcare-still-relies-on-fax-in-2025-security-compliance-and-integration/ ; Esker в 2010 писал, что фарма/мед получают «тысячи заказов в день по факсу и почте» (ссылка выше).

**Что уже автоматизируют:** захват PO из email/PDF/факса в ERP (Esker, Conexiom), складской пикинг (50% строк через автоматику в фарме, HDA), EDI с крупными клиентами. Телефонные заказы, уточнения, возвраты и комплаенс-документы — в основном руками.

## 2. Сколько людей и сколько стоят

BLS OEWS, май 2023, NAICS 4234 (Professional & Commercial Equipment Wholesalers — ближайший публичный срез, включает мед/стомат/госпитальные оптовики 423450): всего 735 860 занятых; **CSR — 34 950 чел. (4,75% штата), медиана $45 760, среднее $48 270**; order clerks — 3 100, медиана $43 408; sales reps (non-technical) — 48 820, медиана $66 664 — https://www.bls.gov/oes/2023/may/naics4_423400.htm

Средняя недельная зарплата в 423450 — $1 647 (≈$85,7K/год, все профессии, апрель 2023) — https://naicslist.com/naics/423450

Оценка на компанию 50–2000 человек (доля CSR 4,75% + order clerks 0,4% ≈ 5%): **3–100 CSR/операторов**, полная стоимость ≈ $60–65K/чел в год с налогами (расчёт от медианы $45,8K × ~1,35; коэффициент — допущение). Компания на 300 человек → ~15 CSR ≈ $0,9–1,0M/год ФОТ на рутину.

Отраслевых данных HIDA/HDA о численности CSR — **не найдено** (страница HIDA «By the numbers» закрыта 403).

## 3. Системы и регуляторика

**ERP:** SAP — 15,2% рынка ERP медизделий США (OpenPR/исследование, 2026) — https://www.openpr.com/news/4597512/sap-se-takes-15-2-share-as-u-s-medical-device-medtech-erp ; у средних дистрибьюторов — NetSuite, Epicor (Prophet 21, с поддержкой GPO-прайсинга), Acumatica, Infor SX.e/CloudSuite Distribution — https://www.erpresearch.com/en-us/medical-devices-erp ; https://expandable.com/12-best-medical-device-erp-systems-ranked/ Стандартизация низкая: 5–6 ERP-семейств плюс кастом, контрактные цены GPO, лоты/серии.

**Регуляторика:**
- UDI: обязанности лежат на маркировщике (производителе), GUDID; дистрибьютор обязан сохранять UDI в цепочке — https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/unique-device-identification-system-udi-system
- DSCSA (фарма): дедлайны принуждения прошли — производители 27.05.2025, **оптовики 27.08.2025**, диспенсеры ≥26 FTE 27.11.2025; нужны TI/TS на каждую транзакцию, верификация, ежегодная отчётность о лицензии — https://intuitionlabs.ai/articles/dscsa-vs-eu-fmd-serialization-traceability ; https://www.fda.gov/drugs/drug-supply-chain-integrity/drug-supply-chain-security-act-dscsa
- Фарма дополнительно: DEA-регистрации, контролируемые вещества, лицензии штатов у каждого покупателя — проверка при каждом заказе — https://www.workd.com/industries/pharmaceutical/
- ЕС: MDR (обязанности дистрибьютора, EUDAMED), FMD-сериализация — детали по ссылке IntuitionLabs выше.

## 4. Кто уже продаёт сюда

| Игрок | Что | Деньги | Медицина |
|---|---|---|---|
| **Conexiom** (Ванкувер) | email/PDF-заказы → ERP, «до 85% touchless» | $170M всего, $130M PE от Warburg Pincus 09.2021; >$100B транзакций/год; ARR ~$28,7M (оценка Latka, 2024) | клиентов из медицины публично не найдено — https://www.cbinsights.com/research/conexiom-private-equity-funding/ ; https://getlatka.com/companies/conexiom |
| **Esker** (Франция) | order management, фокус life sciences | публичная/выкуплена; цена — по запросу, «flat + per-document» | Aspen Medical (2,3→3 заказа/мин, точность 99,5%), Siemens Healthineers (85% авто), St. Jude, Bayer/MEDRAD, Fresenius, Roche Italia — https://cloud.esker.com/fm/others/002-esker-order-management-case-study-aspen-medical-us.pdf ; https://sharedserviceslink.com/news/siemens-healthineers-implement-esker-s-order-management-solution |
| **Go Autonomous** (Копенгаген) | ИИ читает email, создаёт заказ/квоту в SAP/Infor/Dynamics | seed €3,1M (2022), Series A €10M 02.2024 (Octopus, Ridge), всего $18,1M | **Mediq** 4 000 заказов/нед., отдельная страница MedTech — https://www.eu-startups.com/2024/02/copenhagen-based-go-autonomous-gets-e10-million-series-a-to-accelerate-adoption-of-autonomous-commerce/ |
| **Endeavor AI** (SF) | агенты order entry/quoting/voice для дистрибьюторов | seed $7M 31.10.2024 (Craft, BoxGroup, Contrary) | вертикаль мед — не заявлена — https://www.startuphub.ai/startups/endeavor |
| **Workd** (США) | CRM+AI для дистрибьюторов, отдельно фарма: ИИ принимает звонок аптеки, проверяет NDC/DEA, заказ за 3 мин | раунды не раскрыты | да, фарма — https://www.workd.com/industries/pharmaceutical/ |
| **virtualworkforce.ai** (Роттердам) | email-агенты для мед-дистрибьюторов, 14-дневный триал | не найдено | да, маркетинг нишевый — https://virtualworkforce.ai/ai-agents-for-medical-device-distributors/ |
| **InTech Ideas**, **nuVizz**, **GHX** | агентства/логистика/EDI-сеть | — | https://intechideas.ai/industries/medical-supply |

Стоматология: ИИ-агенты идут в клиники (Planet DDS DentalOS 02.2026, Rondah $1,8M, HeyDonto $20M seed 04.2026), а не к дилерам; Caviti.ai — агент закупок на стороне клиники — https://caviti.ai/ ; https://www.planetdds.com/newsroom/planet-dds-unveils-dentalos-ai-agents/ Ветеринария: специализированных игроков **не найдено**.

**Плотность:** крупные горизонтальные ($50M+: Conexiom, Esker) + 1–3 стартапа с медицинским позиционированием (Go Autonomous/Mediq, Workd-фарма, virtualworkforce). Не пусто, но «ИИ-сотрудника как роль по подписке» для независимого дистрибьютора 50–500 чел. никто явно не продаёт.

## 5. Доказательства готовности платить

- Esker: Aspen Medical +30% скорости при сохранении точности 99,5%; Siemens Healthineers 85% заказов автоматически, расширение на США/ЕС/ЮАР; Esker заявляет снижение стоимости обработки заказа на 40–60% и экономию >$30 на переобработке заказа — https://checkthat.ai/brands/esker/pricing
- Go Autonomous: Mediq — 4 000 заказов/нед. без нового штата; ~30% экономии времени CSR — https://goautonomous.io/press-releases/go-autonomous-closes-series-a-to-accelerate-adoption-of-autonomous-commerce/
- Conexiom: Graybar 83 000 документов / 9,5 млн строк за 6 месяцев (электрика, не мед) — https://conexiom.com/resource-center/case-study-graybar
- Цены: у всех по запросу; публичных прайсов — **не найдено**. Ориентир «$5K/мес за роль» = ~1 CSR по полной стоимости — продаётся только при замещении ≥2 FTE или ночной/пиковой смены.

## 6. Размер и где искать

- США, NAICS 423450: **8 539 компаний / 10 846 локаций** (Census 2020); ~9 754 активных компаний, ~241K занятых (наиcslist) — https://naicslist.com/naics/423450 ; порог SBA — 200 чел., т.е. большинство — малые.
- Фарма США: HDA — **37** национальных/региональных/специализированных дистрибьюторов; Big 3 >90% выручки — https://www.hda.org/about/ ; https://intuitionlabs.ai/articles/drug-wholesaler-market-concentration → целей мало, ~30 компаний.
- Европа: **3 662** компании-дистрибьютора медизделий (Tracxn) — https://tracxn.com/d/explore/medical-device-distributors-startups-in-europe/__u6sjVICpUG1Vk9v2naLeTmVshwUYwEWQgIMYqkqRO38/companies ; рынок услуг дистрибуции ЕС $14,2B (2024) — https://www.researchandmarkets.com/reports/6214734/europe-medical-device-distribution-services
- Стоматология/ветеринария: число независимых дилеров — **не найдено** (Dental Trade Alliance недоступен, 403).
- **Кто покупает:** VP Operations / Director Customer Service / COO, у производителей — Head of Order-to-Cash.
- **Где:** HIDA (Streamlining Healthcare Expo, Executive Conference — https://www.hida.org/), HDA (фарма), Medtrade (HME), MEDICA Дюссельдорф (статистика посещаемости — не найдено, страницы 403/404), LogiMed (Esker там выставлялся).

## 7. Риски

1. **Ответственность за ошибку**: неверный лот/размер импланта/дозировка — клинический риск и отзыв; нужен human-in-the-loop на нестандартных позициях.
2. **Регуляторика фармы**: DSCSA (с 08.2025 у оптовиков), DEA, лицензии штатов — каждый заказ = комплаенс-проверка; ошибка — штрафы/лицензия.
3. **EDI-доминирование у крупных клиентов** (госпитали, GPO через GHX) — там заказы уже электронные; ручная работа сосредоточена на малых клиниках/стоматологиях/ветклиниках и на исключениях.
4. **Маржа**: фарма-дистрибьюторы работают с чистой маржой 0,2% (HDA) — бюджеты на софт узкие, решения принимаются долго.
5. **Конкуренция «в лоб» с Esker/Conexiom** на захвате PO; дифференцироваться нужно телефоном, уточнениями, возвратами и документами, а не OCR.
6. Консервативность и фрагментация ERP → длинные внедрения, кастом под каждого.

## 8. Оценка (1–5)

| Критерий | Балл | Почему |
|---|---|---|
| Объём повторяемой работы | **4** | тысячи заказов/день на РЦ, 80% повторных, ручной ввод 10 мин/заказ |
| Стоимость труда | **3** | CSR медиана $45,8K — ниже, чем в IT/финансах; $5K/мес ≈ 1 FTE |
| Простота внедрения | **2** | 5–6 ERP, GPO-цены, лоты/UDI, лицензии; фарма — ещё DSCSA/DEA |
| Слабость конкуренции | **2** | Esker/Conexiom ($170M) + Go Autonomous ($18M, Mediq) + Workd/virtualworkforce |
| Доступность покупателя | **4** | 8,5K компаний в США, 3,7K в ЕС, сильные ассоциации (HIDA/HDA), выставки |
| Доказанная готовность платить | **3** | кейсы Esker/Go Autonomous есть, но цены скрыты, маржа отрасли низкая |
| **Итого** | **18/30** | |

**Вердикт.** Как *первая* ниша — условно: работа реально рутинная и массовая, покупатель достижим через HIDA, но регуляторная ответственность и занятая крупными игроками автоматизация email-заказов делают старт дорогим. Если брать — то **не фарму** (37 целей, DSCSA/DEA, маржа 0,2%), а **независимых дистрибьюторов медрасходников, стоматологии и ветеринарии на 50–500 сотрудников (NetSuite/Epicor/Acumatica)**, где заказы идут телефоном/email/факсом от малых клиник и где никто не продаёт «ИИ-CSR» как роль. Позиционировать против Esker/Conexiom через телефонные заказы, уточнения, возвраты и комплаенс-документы, с обязательным подтверждением человеком по нестандартным позициям.
