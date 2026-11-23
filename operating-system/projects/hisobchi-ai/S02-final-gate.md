# S02 Final Gate — Hisobchi AI UX Architecture

**Decision ID:** GATE-HISOBCHI-S02-001  
**Review mode:** SIMULATED_BOARD_REVIEW — four role perspectives from one ChatGPT instance, **not** autonomous expert reviewers.  
**Date:** 2026-11-23  
**Stage decision:** `PASSED` **for architecture specification only**; S03 can start with *wireframes only*.  
**Owner approval:** A_RECORD_EXPENSE was explicitly approved as first MVP task; no separate owner approval was given for this exact IA, visual style, or release.

## Gate evidence and uncertainty

- `E-OWNER-001`: Owner accepted A — xarajatni qayd etish va nazorat qilish as the first MVP task, recorded in `S00-S01-owner-decisions.md`.
- `E-SOURCE-001`: current source `App.tsx`, `src/data/transactions.ts`, `src/data/periods.ts` supports session CRUD, signed amounts, valid categories and periods (development branch).
- `E-IA-001`: `S02-navigation.json` — 9 named screens/dialogs, 30 transitions, primary `HOME → EDITOR_NEW → HISTORY → ANALYTICS` route and reversible cancel paths.
- `E-IA-002`: `S02-state-matrix.csv` — 31 specified states; `S02-acceptance-checks.md` labels all real UI executions `NOT_TESTED`.
- `E-STRUCT-001`: repository JSON read-back structural checks previously confirmed unique nodes/edges, all nodes reachable, cancel semantics and demo finance arithmetic. These **are not real native UI tests**.
- `E-CI-OWNER-001`: Owner wrote that the manual **Validate Hisobchi Strategy** workflow was green. This is **USER_REPORTED_PASS**; this session did not independently retrieve an exact GitHub run ID/log from the connector. Do not misstate as provider-verified job execution.

## Simulated four-perspective Board — final pass

| Role | Readiness (0–5) | Evidence-based position | Remaining risk |
|---|---:|---|---|
| UX Researcher | 4 | Task sequence and recoverable failure routes documented; no color styling constrains IA | Real user findability/time not tested |
| Creative Director | 4 | Main action hierarchy clear enough to start grayscale wireframe composition | Generic app language remains a visual risk for S04 |
| Design Architect | 4 | Source-data constraints and navigation states preserved in spec; no backend change | Actual Android Back, selected-tab and screen-reader behavior need later QA |
| Critical Reviewer | 4 | No fabricated live finance state; warnings and no-score status maintained | User-reported CI green lacks independently fetched run details |

These ratings assess **readiness of S02 documentation**, not 100-point design quality, measured usability, S+ status or production readiness.

## Debate and corrective conditions

1. **Creative → UX:** Action-first IA may create a generic ledger. **UX answer:** preserve primary action and source truth; allow S03 grayscale composition and later S04 two distinct visual directions. **Residual risk:** Owner may reject both; do not prematurely freeze style.
2. **Critical Reviewer → Architect:** The current source editor back button always announces "Operatsiyalar ro‘yxatiga qaytish" even if launched from Home; `App.tsx` can launch editor from both tabs. **Architect answer:** spec must require origin-aware accessible label, while app code stays untouched until S09. **Status:** implementation issue OPEN, not a blocker for a corrected IA specification.
3. **Architect → UX:** Existing source displays demo balance and fixed Safe-to-Spend independent of session totals. **UX answer:** wireframes must prioritize sourced session figures and never imply an actual bank account or a computed allowance. **Status:** design truth gate mandatory.
4. **Reviewer → Board:** User's green run is reported but exact logs unavailable in current connector. **Resolution:** record as owner-reported validation; stage spec can progress with explicit evidence limitations, but avoid claiming independent CI verification.

## Scoped acceptance

- [x] Owner-approved first user job and S00/S01 scope.
- [x] Core task and cancellation/error/recovery paths documented in IA.
- [x] Screen map, state matrix, navigation machine, Board critique and test plan linked.
- [x] Deterministic demo source truth preserved (5→6 records, expense 259,000→359,000, net 2,741,000→2,641,000 for all-period scenario).
- [x] User reports manual Actions run green; exact provider run ID/log not fetched here.
- [ ] Native interaction tests, audience comprehension, real Safe-to-Spend, accessibility audit — **later stages**, not prerequisites to spec-only S02 pass.
- [ ] Implementation mismatch for contextual editor-back label — S09 before release.

**Decision:** S02 **PASSED for design documentation and move to S03 low-fidelity wireframes**. This is **not** a production release or a guarantee of UI usability. An observed UX regression may reopen S02.

## Next stage contract

**S03 = IN_PROGRESS.** Work strictly grayscale/unstyled layout and reading order for `HOME`, `EDITOR_NEW`, `HISTORY`, `ANALYTICS`, with 320 and 390 CSS-width equivalents, error/empty states and source-truth labels. **NO** font family, accent palette, brand effects, animated components, RN refactor or S04 approval.

**S03 gate:** UX hierarchy survives without color; real Uzbek content fits compact layout; critical user task is discernible; reviewers record dissent and issue list. Owner's next explicit **visual concept** selection happens later at S04.
