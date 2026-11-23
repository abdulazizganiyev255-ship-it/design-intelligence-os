# Hisobchi AI — S02 official screen map v0.1

**Gate:** S02 `PASSED` for specification only (see `S02-final-gate.md`); original source implementation/native QA not approved. **Owner-approved primary job:** `A_RECORD_EXPENSE`. **Source of truth:** `S00-S01-owner-decisions.md` and `S01-source-truth-contract.md`.  
**Stage:** Information Architecture ONLY — **no colors, typefaces, component skin, finished wireframe, actual app change or final S02 approval**.

## Primary question

After recording a real-world expense, can a person verify that the **session's** recorded transactions and Analytics changed correctly, without mistaking demo finance figures for bank data?

## Entities and their relationships

- **Transaction:** `id`, `amount` (negative expense, positive income), `category`, `occurredOn` (local ISO date), `note`; session-only memory in current demo.
- **Editor draft:** `kind`, positive integer `amountText`, category from approved options, valid nonfuture date, optional note. New, edit, invalid, cancelled, saved, delete-confirm.
- **History list:** session transactions with search, type and date/period filters; totals must state whether they describe visible rows.
- **Analytics report:** period-aggregated income, expense, net and turnover; chart may cover last 7 recorded days, while period KPI may cover more.
- **Sample-only dashboard:** fixed demo balance/allowance/month chart. It must not be represented as session-derived or an authenticated bank account.
- **UI source notice:** clear provenance label attached to the reported amount, not repeated tiny legal copy drowning out primary task.

## Navigational taxonomy — proposed IA A (selected for S02 development, not a visual direction)

| Screen ID | Proposed existing tab | Job | Primary action | Secondary/exit |
|---|---|---|---|---|
| `HOME` | `Bosh sahifa` | orient with accurate session state | `Xarajat qo‘shish` → `EDITOR_NEW` | recent entries → `HISTORY`, income entry, analytics |
| `HISTORY` | `Operatsiyalar` | find or correct a saved entry | select row → `EDITOR_EDIT` | search, period, category/type filters, new expense |
| `ANALYTICS` | `Tahlil` | verify aggregated session totals | period selection | custom range; show raw list in `HISTORY` |
| `PROFILE` | `Profil` | understand demo/local state, use help | view state/guide | optional reset confirmation |
| `EDITOR_NEW` | no bottom tabs (context screen) | create income/expense record | validate and save | cancel → origin tab |
| `EDITOR_EDIT` | no bottom tabs (context screen) | correct one existing record | validate and update | cancel, delete confirmation |
| `DATE_PICKER` | in editor or filter as contextual modal | choose an allowed ISO day/range | apply valid date | cancel/Back restores prior draft |
| `DELETE_CONFIRM` | editor overlay | guard destructive change | confirm delete | cancel → edit without mutation |

**Current source correspondence:** `App.tsx` has Home/Transactions/Analytics/Profile tabs and an editor route outside the tabs; no new navigation framework is required for the MVP. The screen map is a **design proposal**; exact copy/hierarchy must be validated in the actual UI.

## Screen priorities

**HOME**: one visible primary action; factual session metric with `Sessiya` or `DEMO` label; not a fake account balance. Recent records should remain recognizable. Secondary finance numbers must not compete visually with recording an expense. UI may place historical details below fold but never hide the primary action behind a fixed overlay.

**EDITOR_NEW / EDITOR_EDIT**: amount first in task flow, then known expense category, valid date and optional note. Form errors remain next to relevant field, not isolated global toast. Real keyboard behavior and focus order need S08/S10 runtime tests.

**HISTORY**: show signed amount, category/title and real recorded date; filter visibility and easy `Barchasi` recovery. `No results` from a search/filter is distinct from `no transactions` in the entire session.

**ANALYTICS**: distinguish `Sof farq` (income minus expense) from bank balance, respect period scope and chart coverage, provide no-data handling (not fake zero-growth line).

**PROFILE**: demo reset requires confirmation; no nonfunctional real account/password controls as present functionality.

## Tab and Back behavior (information architecture, not final UI skin)

- Bottom tabs are available only when not editing/onboarding. Current `App.tsx` uses `tab` and `editor` states rather than a separate navigation library.
- New entry from Home → cancel returns Home without mutation. From HISTORY → cancel returns HISTORY.
- Successful save returns HISTORY with new/updated row visible; Analytics reflects the same session on its selected period.
- Android hardware Back from editor exits editor; calendar/modal Back should dismiss the overlay first. iOS back/gesture behavior must be tested natively.
- A Profile/demo reset affects session-only entries and restores seed demo state, not an authenticated cloud account.

## Option check (structurally distinct, but not moving to S04)

- **IA A / Action-first ledger (selected for prototype architecture):** Home prioritizes expense action then session feedback; HISTORY handles retrieval and correction.
- **IA B / Date-first activity (deferred as alternative):** Home emphasizes timeline entry and date groups. It risks extra date decision before one-tap expense; may be useful for future timeline-first research. Do not conflate with visual concept B.
- IA A is chosen as a reversible working hypothesis aligned with Owner-approved first task. This is **NOT** Owner approval of typography, palette, components, or visual art direction.

## Hard constraints and exit gate

S02 can be considered for PASS only when `S02-task-flows.md`, `S02-state-matrix.csv`, `S02-navigation.json`, `S02-board-review.md` and `S02-acceptance-checks.md` agree; critical paths are reachable; cancel/error/recovery paths explicit; labels match source semantics; four Board perspectives evaluate and log dissent. S03 wireframes remain blocked until S02 pass is recorded.
