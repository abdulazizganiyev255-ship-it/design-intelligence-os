# Owner decisions — Hisobchi AI S00 and S01

**Decision ID:** DR-HISOBCHI-2026-11-23-A  
**Date:** 2026-11-23  
**Decision maker:** Product Owner (user in this conversation)  
**Mode of Board review:** `SIMULATED_BOARD_REVIEW` (one ChatGPT model, not four autonomous agents).

## Exact Owner authorization and scope

> “Hisobchi AI uchun A — xarajatni qayd etish va nazorat qilish birinchi MVPning asosiy vazifasi sifatida tasdiqlandi. S00/S01 qarorlarini GitHub’da qayd etib, S02 UX arxitekturasini rasmiy ishlab chiqishni boshlagin.”

This is **explicit approval of the first MVP's primary job**, not approval of a final visual direction, detailed S02 topology, a production release, full target-market proof, real Safe-to-Spend, or an autonomous AI team.

## S00 — scoped baseline acceptance

**Gate:** `PASSED` for **S00_SOURCE_BASED_FIRST_MVP_SCOPE** only.

- Existing code and selected Chromium screenshots were inspected; prior visual directions are rejected by Owner.
- Keep valid session CRUD, date/amount validation, derived Analytics and provenance from `S00-evidence-and-gate.md` / `S01-source-truth-contract.md`.
- Absence of native screenshots, real user interviews, external human UX tests and production finance model remains **OPEN**; these missing items are not silently declared completed.
- This scoped gate is sufficient to proceed with information architecture **for a demonstrative vertical slice**, not to certify product aesthetics or release readiness.

**Evidence:** `E-OWNER-001` and source/E-DATA/E-APP IDs in the S00 record.  
**Owner approval:** `APPROVED_FOR_FIRST_MVP_SCOPE`.

## S01 — product strategy approval

**Gate:** `PASSED` for **FIRST_MVP_TASK_ONLY**.

**Approved primary task:** after a user incurs an expense, they record its amount/category/date and confirm that the expense appears in history and recalculated session totals. In Uzbek: **“Xarajatni qayd etish va nazorat qilish.”**

**Acceptance fixture** (source-derived, not newly executed UI test): five seed transactions → add 100,000 UZS valid expense → six transactions; expense 259,000→359,000; net 2,741,000→2,641,000; income remains 3,000,000. Fixed demo balance/Safe-to-Spend/month chart must not change.

**Proposed target segment:** Uzbek-speaking mobile individuals keeping personal expense records; **HYPOTHESIS ONLY**, no evidence of actual segment demand, age or willingness to pay. Research and positioning can be refined later without invalidating the first task.

**Explicitly NOT approved:** real daily spending allowance, bank-connected balance, AI insights, user validation claims, the previous visual designs, or production security/monetization.

## S02 — authorized start, not automatic completion

**Gate:** `IN_PROGRESS`. UX Researcher leads. Work is now allowed on named screens, routes, event/invalid/cancel flows, states, error recovery, source-truth labels and acceptance scenarios. Every deliverable goes to four-role *simulated* Board review, after which S02 can be recommended for PASS.

**Not authorized:** S03–S12 stage passing; fonts/colors/buttons, new visual rendering, React Native implementation or release. S02 completion requires evidence-backed navigation and recovery assessment, not Owner's prior selection of task alone.

## Board perspectives — response to Owner decision

- **UX Researcher:** supports narrowed first job; prioritizes add → save → verify and meaningful errors. Primary audience remains an untested hypothesis.
- **Creative Director:** accepts task-driven hierarchy but cautions against prematurely reproducing a generic expense app. Distinctive visual art direction belongs to S04.
- **Design Architect:** confirms current draft/source branch supports session CRUD and Analytics; preserves demo/live data labels and existing category/date semantics.
- **Critical Reviewer:** allows scoped S00/S01 gates with explicit limitations; blocks claims of native usability, live Safe-to-Spend, audience demand, high design score or release.

**Resolution:** S00 = PASSED (scoped); S01 = PASSED (first task only); S02 = IN_PROGRESS; S03–S12 = NOT_STARTED. No S02 owner signoff implied.

## Next stage deliverables

`S02-screen-map.md`, `S02-task-flows.md`, `S02-state-matrix.csv`, `S02-navigation.json`, `S02-board-review.md`, `S02-acceptance-checks.md`.  
No UI score: `UNSCORED`; no actual user test: `NOT_CONDUCTED`.
