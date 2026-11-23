# S01 Board Session — Hisobchi AI Strategy

**Session:** STAGE-HISOBCHI-S01-001  
**Mode:** `SIMULATED_BOARD_REVIEW` — four viewpoints from one model, not autonomous agents.  
**Date:** 2026-11-23  
**Input:** `S00-evidence-and-gate.md`, `S01-source-truth-contract.md`, `S01-product-strategy.md`  
**Current status:** `APPROVED_BY_OWNER` for first-MVP primary task **only** (2026-11-23); earlier Board comments below represent pre-approval review.

## Round 1 — separate role positions

**UX Researcher — HYPOTHESIS (readiness: null).** One task must take priority over multiple large KPIs. Expense capture is an observable first job and can be tested without invented banking context. But the actual *first-choice* user job is not proven by target-user research. **Risk:** Owner may intend real Safe-to-Spend as the product's most important differentiated use case. **Action:** obtain Owner choice and write a task comprehension test.

**Creative Director — DESIGN_JUDGMENT (readiness: 3/5, scope limited to brief completeness).** Starting with expense capture gives compositional hierarchy to work from, rather than an arbitrary premium palette. But a conventional ledger still risks looking generic. **Risk:** a familiar expense editor can be visually competent but not feel like a new product. **Action:** after S03, develop two genuinely different art-direction concepts tied to the selected top job.

**Design Architect — SOURCE-GROUNDED TECHNICAL_JUDGMENT (readiness: 4/5 for demo feasibility).** Current `App.tsx` and `src/data/*` support expense CRUD and session Analytics calculations. They do not support a real balance or computed spending allowance. **Risk:** visual work inadvertently breaks financial truth. **Action:** treat the data-truth matrix as a critical implementation invariant.

**Critical Reviewer — FACT/UNKNOWN (readiness: 2/5).** Source constraints are documented, but there is neither Owner authorization for the primary job nor live user evidence. **Risk:** promoting a strategy hypothesis to a chosen product direction. **Action:** mark S01 unapproved, S02 drafts provisional; no invented S+ score or human user research.

These are stage-readiness opinions, not the final 100-point design quality score. No averaging.

## Round 2 — substantive objections

1. **UX → Architect:** Selecting the easiest implemented task might optimize for code convenience instead of product value. **Reply:** Option A is a first proof-of-work vertical slice, *not* a claim that it is the product's permanent North Star. **Dissent remains:** actual users might prioritize budget foresight, so investigate after MVP.
2. **Creative → UX:** Fast ledger entry alone may recreate generic budget-app UI. **Reply:** the distinction must come from an approved information architecture, meaningful visual identity and real task clarity, not fabricated AI visuals or financial KPIs. **Dissent remains:** visual differentiation cannot yet be measured.
3. **Reviewer → all:** No evidence that new target users need Safe-to-Spend, nor that today's demo number is safe. **Resolution:** keep daily allowance `NOT_COMPUTED` and block production promises.

## Decision options

- **A (recommendation, not approval):** Expense capture as first end-to-end MVP acceptance test, then session report. Product positioning remains under study.
- **B:** Safe-to-Spend-first product. Rejected as **current truthful implementation scope**, not rejected as a product vision; requires real authenticated finance model and user validation.

## Proposed resolution / gate

**Reconciled with Owner's explicit decision:** `S01=PASSED` (first-MVP task only), `S02=IN_PROGRESS`. The recommendation above was not an approval when written; Owner later approved A explicitly. See `S00-S01-owner-decisions.md`. **No S02 PASS, S03 wireframe lock or S04 creative selection is implied.**

**Next observable action after Owner approval:** conduct S02 IA review, record navigation/failed-state coverage and evaluate evidence. Audience remains a hypothesis; finance data contracts stay unchanged; no numeric quality score is claimed.
