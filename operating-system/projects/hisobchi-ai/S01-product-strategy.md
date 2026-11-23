# Hisobchi AI — S01 Product Strategy v0.1 (OWNER REVIEW DRAFT)

**Stage:** S01 User, Job & Product Strategy. **Status:** `READY_FOR_OWNER_REVIEW`, **NOT APPROVED**.  
**Mode:** One ChatGPT simulating four Board perspectives.  
**Date:** 2026-11-23. **Data:** `S01-source-truth-contract.md`.  
**Prerequisite:** S00 is `NEEDS_EVIDENCE`, so this is provisional work only; **S02 and visual direction are not approved**.

## 1. Precise problem statement

**Owner-supported goals:** Uzbek-language personal finance application, mobile-friendly, stronger original iPhone-inspired visual craft, an understandable view of money, future trustworthy AI analysis and Safe-to-Spend ambitions. Owner rejects every previous Hisobchi AI visual direction. **No user interviews or market demand figures are provided**.

**Source-supported current implementation:** Local demonstration of transaction CRUD, period filtering and session-derived analytics; fixed sample dashboard figures independent of transaction changes, no live banking or proven daily Safe-to-Spend engine.

**Diagnosis — design hypothesis:** visually prioritizing multiple unrelated figures instead of ONE clear job makes information interpretation difficult. This is a design judgment based on selected screenshots plus owner rejection, **not** measured usability.

## 2. Target audience — assumptions, not established research

**Initial segment hypothesis:** Uzbek-speaking mobile users who want a fast and understandable way to record expenses and see where spending went. Age, banking penetration, actual financial literacy, willingness to pay and recurring pain frequency are **UNKNOWN**. Do not produce fictitious personas or demographic percentages.

**Platform:** React Native / Expo mobile prototype; use real Android and iOS constraints. Browser render is a development preview, not proof of native experience.

## 3. Which ONE primary user job?

### Option A — Expense capture & truthful feedback (recommended first MVP)

> “Xarajat qilganimda summani tez qayd etib, u operatsiyalar ro‘yxati va davr bo‘yicha jami xarajatga to‘g‘ri qo‘shilganini darhol ko‘rmoqchiman.”

- **Trigger:** a purchase/expense has occurred.
- **Entry:** Home or Transactions → clear `Xarajat qo‘shish`.
- **Main action:** amount, category and date; optional note.
- **Success:** record saved locally for the session; Transactions and Analytics show consistent new values and source notice.
- **Why now:** current source can support functional tests without pretending live balance exists.
- **Limitation:** this is an incremental utility job; it does not by itself prove distinctive product-market demand.

### Option B — Safe-to-Spend today (North-star product hypothesis; BLOCKED for live numeric MVP)

> “Bugun qancha sarflashim xavfsizligini majburiyatlarim, mavjud mablag‘im va yaqin xarajatlarimga qarab tushunmoqchiman.”

- **Real value hypothesis:** better daily spending decisions, beyond simply recording transactions.
- **Unmet dependencies:** verified cash balance, recurring/committed obligations, period horizon, deterministic finance rules, authenticated persistence, error/reconciliation tests.
- **Current state:** only a **fixed demo number**, not computed from source ledger.
- **UI until ready:** clearly show `Hozircha hisoblanmagan`; not a working allowance, AI promise or savings forecast.
- **Decision:** DO NOT ship Option B as a truthful live result yet.

**Recommendation:** Owner approves Option A as the **first testable UI vertical slice** while keeping Option B as a product strategy hypothesis pending engineering/research. The two tasks should not be combined into an overloaded Home hero.

## 4. Core scope for first visual + working slice

**In:** Home action clarity; one Expense Editor; correct required validation; session-only save; updated History row; period-based Analytics summary; source/provenance notices; empty/error/cancel. Retain income entry via existing editor but first acceptance script focuses expense.

**Out:** bank sync, real daily spend allowance, AI predictions, full Supabase integration, automatic expense import, subscriptions, push notifications and production rollout.

**Must preserve:** deterministic amount/sign/date validation, add/edit/delete invariants, session Analytics and original data provenance. Do not change backend/schema while only redesigning UI.

## 5. First user journey and acceptance definition

1. Open Home with explicit DEMO/session data state.
2. See an obvious `Xarajat qo‘shish` action; no invented daily allowance as primary.
3. Open editor; enter `100000` UZS, valid expense category and current nonfuture date; save.
4. Return to Transactions, new row visible; Analytics session expense changes from **259,000 → 359,000**, net **2,741,000 → 2,641,000**. Fixed sample balance 12,850,000 and fixed demo Safe-to-Spend 145,000 must not change.
5. Cancel/edit/delete paths correctly preserve or revert data, with suitable confirmation.

**Measurable test (proposal):** task success/error count; taps and elapsed time observed in a real run; can a participant identify what the main figure means and that it is not a bank balance? No observed statistics exist yet, and no arbitrary time/step targets are treated as facts.

## 6. Visual intent (not a design system yet)

- iPhone-inspired restraint, confident editorial hierarchy, distinctive identity rooted in a financial *task*.
- One obvious next action; reduce cosmetic KPI competition; Uzbek money strings remain readable.
- Actual icon, typeface, color palette, spacing scale and button shape **NOT SELECTED**. Those are S04–S06 decisions after Owner's concept selection.
- Old Living Ledger, cobalt and blue designs remain rejected. Do not copy screenshot style.

## 7. Risk register

| Risk ID | Risk | Severity / mode | Control |
|---|---|---|---|
| STR-01 | Showing demo Safe-to-Spend as live budget | P1 production risk | hide live claim, source label, finance engine gate |
| STR-02 | Demo balance mistaken for session net | P1 if misleading in production | separate `Sof farq` and sample balance; comprehension test |
| STR-03 | Screen renders beautiful but record action not functional | P1 for MVP user task | real event/validation and updated totals tests |
| STR-04 | Owner again rejects visual direction | Aesthetic gate | S04 two genuinely distinct renders + explicit approval |
| STR-05 | Too much IA before user need decided | Process blocker | do not approve S02 until Owner accepts S01 |

## 8. Owner decisions still required

1. Is **Option A** the correct first MVP primary job, or should another task lead?
2. Is the initial audience Uzbek-speaking individual budget trackers, or a narrower segment?
3. Do we treat a *live* Safe-to-Spend result as a **later separate engineering milestone**?

Until these are accepted: `owner_approved=false`; `S01=NOT_STARTED (documentation draft only; S00 gate pending)`, `S02=NOT_STARTED`, `S04 visual target NOT APPROVED`.

## Sources and evidence

See `S00-evidence-and-gate.md` and `S01-source-truth-contract.md`. Upstream implementation is draft branch `design/splus-living-ledger-analytics-v03`, not the repository's automatically released build. No interviews, external product research or native device tests are claimed.
