# Hisobchi AI — S00 evidence closure (review draft)

**Date:** 2026-11-23  
**Stage:** S00 — Intake / baseline  
**Status:** `PASSED` for source-based first-MVP baseline only; native/user evidence still missing  
**Mode:** `SIMULATED_BOARD_REVIEW`  
**Owner visual verdict:** All earlier Hisobchi AI visual directions rejected. This **does not** reject verified arithmetic, navigation or validation behavior.

## Reviewed actual sources

- `E-OWNER-001`: Owner rejected all prior visual directions (conversation, November 23). Proves owner's aesthetic judgment, not measured user outcomes.
- `E-BASE-001`: `baseline/hisobchi-ai/BASELINE-001.md` plus the referenced [Chromium Actions screenshots](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/actions/runs/45051373294). Prior review covered selected web screenshots, **not every historic design or native device**.
- `E-DATA-001`: [src/data/demo.ts](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/demo.ts): five deterministic transactions and unrelated fixed demo balance/Safe-to-Spend.
- `E-DATA-002`: [src/data/transactions.ts](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/transactions.ts): category/amount/date validation, income/expense sign and search.
- `E-DATA-003`: [src/data/periods.ts](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/periods.ts): date windows, inclusive range validation and amount totals.
- `E-DATA-004`: [src/data/analytics.ts](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/data/analytics.ts): deterministic, session-derived income/expense/net/turnover, period and chart summary.
- `E-APP-001`: [App.tsx](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/App.tsx): Home/Transactions/Analytics/Profile tabs; Editor creation and mutation; demo reset and optional onboarding.
- `E-QA-001`: [Analytics visual gate](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/docs/design-os-splus/09_ANALYTICS_VISUAL_GATE.md) reports web CI/screenshots and unverified native accessibility. This is **a historical QA report**, not a newly rerun test.

## Facts vs conclusions

**Source-confirmed facts:**
- Current reference branch is `design/splus-living-ledger-analytics-v03`, **not automatically merged production main**.
- Demo `balance=12,850,000`, `safeToSpendToday=145,000`, and sample month chart are fixed; they do not follow session CRUD.
- Session seed = five records, income 3,000,000, expenses 259,000, net 2,741,000, turnover 3,259,000 (UZS).
- Transaction entry uses local memory; page restart can restore seed data. No user bank account or proven live finance engine from this source.
- `App.tsx` records a new transaction, returns to Transactions; list and Analytics derive from current session.

**Design judgments/hypotheses:** current hierarchy is too fragmented and branded styles are unacceptable to Owner. Exactly *which* alternative will satisfy the Owner or target users is not proven.

## Preserve (functional invariants)

1. Positive amount validation (integer UZS, max 999,999,999,999), required category, valid nonfuture date, field-specific error handling.
2. Expense amounts negative, income positive; correct net and totals.
3. Add/edit/delete with cancellation and destructive confirmation; filter/search/date-range contract.
4. `DEMO / sessiya` provenance on all prominent numbers; do not relabel fixed demo balance as live account balance.
5. No unverified AI insights, 78% stability score, growth forecast or real Safe-to-Spend claim.

## Reject / reset (visual only)

- Living Ledger aesthetic, old blue/card/glass experiments and Porcelain × Cobalt draft as *final visual direction*.
- Multiple unrelated competing KPI heroes and repeated UI cards as the default design pattern.
- Color/font/polish changes that keep the same unclear task hierarchy.

## Missing evidence

- Owner-confirmed primary user segment and ONE primary job for the next release.
- First-hand target-user comprehension/task study, if we want claims about usability.
- Native screenshots, TalkBack/VoiceOver, enlarged fonts, real-device keyboard behavior.
- Real data/backend/security contracts for production accounts and future Safe-to-Spend.
- Explicitly chosen visual direction after S01–S04 gates.

## S00 Board checkpoint — role perspectives (simulation)

| Perspective | Evidence-limited judgment | Rating 0–5 or null | Blocking issue |
|---|---|---:|---|
| UX Researcher | Task priority is not owner-approved; two product jobs are plausible | null | primary job needs decision |
| Creative Director | All rejected style constraints are known | 3 | no approved new visual target |
| Design Architect | Model/CRUD/data invariants have actual source evidence | 4 | current branch is draft, device runtime not rechecked |
| Critical Reviewer | Truthful partial evidence available; no scoreable real user baseline | 2 | full baseline evidence coverage missing |

No consensus, average or numeric S+ grade is implied.

**Updated gate decision (2026-11-23):** `PASSED` for the source-based, demonstrative expense-capture MVP scope. Owner signed off on the scope; see `S00-S01-owner-decisions.md`. Native and user-study evidence remain open for later quality gates.

## Owner decision and next gate

Owner explicitly approved `A_RECORD_EXPENSE` as the first MVP's primary task on 2026-11-23. S00 is PASSED **only for source-backed MVP intake**, S01 is PASSED **only for first-job strategy**, and S02 is IN_PROGRESS. See `S00-S01-owner-decisions.md`. The earlier four-role scores above are historical pre-approval perspectives, not real user study results.
