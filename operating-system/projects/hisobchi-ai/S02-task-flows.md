# Hisobchi AI S02 — Task flows and failure recovery (design specification)

**Mode:** `SIMULATED_BOARD_REVIEW`, no real task tests performed in this new redesign.  
**Scope:** source-supported session-only demo. **Owner job:** add and monitor expenses.  
**Identifiers:** `F-01` etc. Each test references `S02-acceptance-checks.md`.

## F-01 — primary happy path (expense entry)

```text
HOME (DEMO/session information visibly qualified)
  → tap "Xarajat qo‘shish"
EDITOR_NEW (kind=expense)
  → enter integer UZS >0 <= 999,999,999,999
  → choose recognized expense category
  → choose today or prior valid ISO date (nonfuture)
  → optional note (up to 180 chars retained)
  → Save
HISTORY (new signed-negative row visible, session persisted in runtime memory)
  → open Tahlil / period that includes recorded date
ANALYTICS (income=3,000,000; expense=359,000; net=2,641,000 for all seeded data)
```

The numbers come from existing deterministic demo fixture (five records, income 3,000,000, expense 259,000, net 2,741,000; add expense 100,000), **not an executed new UI test**. For `week/month/custom`, the reported total must reflect selected period; do **not** require all-data fixture under a narrow window.

## F-02 — cancel safely

- Enter new record from HOME; cancel before save → HOME, same record count/sums.
- Enter new record from HISTORY; cancel before save → HISTORY, same data.
- Open existing row to EDITOR_EDIT; modify draft; cancel → HISTORY, original record unchanged.
- Modal calendar cancel restores draft value; native Android Back closes modal before editing context.

## F-03 — invalid input / field recovery

- `amountText` empty, 0, negative, fractional, letters, above max → corresponding inline error; no mutation or false success.
- Invalid or unrecognized category → error; selecting a valid category clears/rechecks error.
- Invalid ISO date and tomorrow/future day → blocked/error; allowed current/past day validates.
- After correction → Save once. Source `parseUZS` rejects nonpositive or invalid integer.
- A disabled submit state cannot silently hide the reason or lose values.

## F-04 — edit and delete

- HISTORY row → EDITOR_EDIT → modify amount/category/date → Save → HISTORY updated row and totals.
- Delete must open confirmation with accessible cancel; cancel → editor unchanged.
- Confirm delete removes exactly selected row once; derived Analytics updates; no broader reset.
- Android Back/keyboard and VoiceOver focus return are **NOT_TESTED** here.

## F-05 — find / filter / date range

- HISTORY list query → matching rows; unmatched query → actionable `no result`; clear query recovers.
- Kind `Barchasi/Xarajat/Daromad` and period `Barchasi/Hafta/Oy/30 kun/Oraliq` determine visible set.
- Custom range must validate start<=end<=today, inclusive boundaries; calendar cancel does not apply incomplete range.
- Totals/labels must reflect **visible filtered rows**, not silently default all rows.
- Analytics selected range is separate and should identify period/chart coverage. Source logic handles inclusive date windows.

## F-06 — empty, no-income, reset and demo truth

- An empty session / filtered list / zero-income Analytics each has a truthful distinct state.
- Chart cannot fabricate a trend, future obligation, progress percentage or AI advice from absent values.
- Profile reset requires confirmation and resets **local session** demo entries; explicit source qualification stays visible.
- Fixed `demo.balance=12,850,000`, `safeToSpendToday=145,000` and fixed sample month expense `3,840,000` remain sample values independent of CRUD; must never be called live.

## F-07 — navigation and focus

- Tabs HOME/HISTORY/ANALYTICS/PROFILE; selected state and understandable labels.
- Editor shows no persistent bottom tabs; accessible close/back; on save → HISTORY; on cancel → origin.
- Keyboard focus goes to meaningful field and error; submit is not blocked behind keyboard (real device test later).
- Current source uses RN state screen switches; this spec should not imply a new installed navigation package.

## Evidence and test state

**FACT from code:** `App.tsx`, `src/data/demo.ts`, `src/data/transactions.ts`, `src/data/periods.ts`, `src/data/analytics.ts` on branch `design/splus-living-ledger-analytics-v03`.  
**DESIGN HYPOTHESIS:** more direct action-first flow will improve comprehension and cost fewer interactions.  
**NOT_TESTED:** new native flow implementation, user timing, screen-reader behavior and attractiveness.
