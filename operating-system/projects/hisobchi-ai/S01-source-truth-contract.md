# Hisobchi AI — source truth and finance invariants for strategy

**Source ref:** `design/splus-living-ledger-analytics-v03` in [hisobchi-ai-mobile](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile). These examples are **DEMO/session**, not user's live money. 2026-11-23 source read.

## Distinct values and provenance

| Metric | Source | Current example (UZS) | Changes after session CRUD? | UI rule |
|---|---|---:|---|---|
| Sample balance | `demo.balance` | 12,850,000 | **No** | `DEMO BALANS`, not bank-account current |
| Sample daily Safe-to-Spend | `demo.safeToSpendToday` | 145,000 | **No** | `NAMUNA`, **not computed daily allowance** |
| Sample monthly chart | `demo.months.current.total` | 3,840,000 | **No** | sample chart unrelated to session ledger |
| Session income | signed transaction sums | 3,000,000 | **Yes** | label as session-derived / selected period |
| Session expense | absolute sum of negative transactions | 259,000 | **Yes** | label as session-derived |
| Session net difference | income − expense | 2,741,000 | **Yes** | `Sof farq` is **not account balance** |
| Session turnover | income + expense | 3,259,000 | **Yes** | do not call turnover a bank balance |

**Seed records:** +3,000,000 income, −85,000 groceries, −12,000 transport, −42,000 café, −120,000 health. Five entries; sum expenses = 259,000.

**Deterministic acceptance fixture:** add expense `100,000 UZS` to the current session, resulting in **6 records**, expenses = **359,000**, income remains **3,000,000**, net = **2,641,000**, turnover = **3,359,000**. Fixed balance, Safe-to-Spend sample and fixed monthly chart **must not change**. If edited to 50,000, expenses = 309,000; confirmed deletion restores 259,000.

## Source implementation contracts

- `src/data/transactions.ts`: valid whole positive amount, recognized kind/category, ISO date, no future date. Amount range 1…999,999,999,999; note truncated to 180 chars. Expense stored negative.
- `src/data/periods.ts`: `week/month/last30/custom/all`, inclusive custom boundaries; custom end <= current day and start <= end.
- `src/data/analytics.ts`: derived summaries and chart. Last seven *recorded days* chart can differ from whole selected-period KPI coverage; state the coverage explicitly.
- `App.tsx`: current session state initially seeded with `demo.transactions`, Add/Edit/Delete mutate memory and return to Transactions. Profile may reset the demo.
- Native React, Expo/Web implementation requires independent QA; prior browser CI results should not be overstated.

## UX language contract

Use only precise labels:
- `Sof farq — ushbu sessiya yozuvlari bo‘yicha` instead of `Hisobingizda` for derived net.
- `Demo balans — namuna` instead of `Bankdagi balans`.
- `Kunlik xarajat limiti hisoblanmagan` if deterministic Safe-to-Spend engine is not integrated.
- `Operatsiya saqlandi (shu sessiyada)` rather than cloud-synced success.

Never generate fabricated forecasts, savings goals, stability scores, synced account icons, historical growth or AI financial advice.

## Non-negotiable release gates

No authenticated production finance claim until Supabase/Auth/RLS, persistence, reconciliation and data access are separately audited; no real Safe-to-Spend number before deterministic engine and validation. Visual approval alone must not authorize backend functionality.

## Evidence

- [Demo data and formatter](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/demo.ts)
- [Transaction validation/CRUD model](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/transactions.ts)
- [Date periods](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/periods.ts)
- [Analytics derived values](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/analytics.ts)
- [Application navigation and local state](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/App.tsx)
