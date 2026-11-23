# Hisobchi AI — S02 Board review 001 (official in-progress review)

**Date:** 2026-11-23  
**Mode:** `SIMULATED_BOARD_REVIEW` — four separate professional viewpoints from **one ChatGPT model**, not autonomous experts and not a real user study.  
**Stage:** `S02 IN_PROGRESS`. **Prerequisites:** S00 and S01 scoped PASSED per `S00-S01-owner-decisions.md`.  
**Input:** `S02-screen-map.md`, `S02-task-flows.md`, `S02-state-matrix.csv`, `S02-navigation.json`, source truth contract.  
**Owner approved:** first job `A_RECORD_EXPENSE`, **not** this specific navigation topology.

## Round 1 — role positions and rationale

| Perspective | Basis | Readiness | Recommendation | Risk |
|---|---|---:|---|---|
| UX Researcher | DESIGN_HYPOTHESIS + source-constrained flows | 4/5 (spec only) | Keep `Bosh sahifa` action-first and post-save verification in `Operatsiyalar`; include clear origin-aware cancel | Tab naming and task findability not yet tested with people |
| Creative Director | DESIGN_JUDGMENT | 3/5 | Top task and information density are now defined; S04 should find an expressive composition without generic KPI stacks | Action-first ledger can become another templated finance UI |
| Design Architect | SOURCE_DOCUMENT | 4/5 (flow feasibility) | Preserve existing RN tabs, editor state switch, session arithmetic, date validation and source labels; no early navigation-library migration | Mobile Back/modal behavior and keyboard need native proof |
| Critical Reviewer | FACT/UNKNOWN | 3/5 | Accept IA specification for continued review only, not for UX-performance claims | Missing observed user task results and actual prototype; some modal/cancel paths need systematic QA |

The values are **stage readiness opinion** (0–5) within inspected scope, **not** a 100-point product quality score. No automatic averaging.

## Round 2 — objections and replies

1. **UX → Creative:** An elaborate financial status hero may obscure the approved `Xarajat qo‘shish` action. **Creative reply:** S04 originality must respect the task sequence. **Open risk:** until actual wireframe/render, relative visual prominence cannot be verified.
2. **Critical Reviewer → UX:** Choosing `Bosh sahifa` as the first expense entry is plausible but its real findability has not been measured. **UX reply:** mark as a design hypothesis and include a task success test with source context. **Dissent retained:** one model simulation does not validate this with humans.
3. **Architect → UX:** Calendar and destructive confirmation are contextual overlays, not new top-level screens; changing their behavior could regress tested CRUD. **UX reply:** keep transitions explicit and cancel reversible; use current RN flow as implementation constraint. **Follow-up:** verify Android Back, iOS focus and enlarged text on the running app.
4. **Creative → Architect:** Reusing old navigation mechanics must not force reuse of a rejected aesthetic. **Architect reply:** reuse data/behaviors, not old look. **Resolution:** topology semantics stay separate from S04 visual design.

## Options and decision

**IA A — Action-first Ledger (working choice):** Home highlights record expense, then verifies in History and Analytics. Directly serves Owner's approved initial task. Cost: low relative to new navigation; risk: visual genericness.

**IA B — Date-first Activity:** Home groups by date and timeline before exposing entry; potentially compelling for users revisiting past events, but may add an unnecessary decision to the first-task path. Research not available to prefer this for MVP.

**Board recommendation:** continue with IA A for S02 specification, retain IA B as counterexample. This is a *reversible architectural recommendation* — NOT Owner approval of visual identity or actual task efficiency.

## Gate and dissent

**S02 status:** `IN_PROGRESS` / `REVIEW_REQUIRED`, **not PASSED**. Once route graph, state coverage and acceptance script pass structural validation and Board resolves the missing paths, S02 can be considered for a scoped PASS into S03 wireframes. Native and user tests still need to occur later, and if actual user evidence contradicts architecture, return to S02.

**No S03/S04 output is approved.** User study: NOT_CONDUCTED. Android/iOS QA: NOT_TESTED. 100-point design score: UNSCORED.

## Next exact actions

1. Complete all cancel/Back overlay paths and validate route reachability + no silent data mutation.
2. Trace 31 state entries to testable acceptance IDs.
3. Run source-grounded structural validator, including negative fixtures for illegal stage skips, wrong net arithmetic and dead-end recovery.
4. Conduct S02 final Board gate review. If pass, authorize S03 *wireframes only*; visual styling is an S04/S05 concern.

## Knowledge state

Candidate pattern: one direct expense action + immediate truthful confirmation may reduce decision friction for session-based budget capture. **REVIEW_PENDING**, not VALIDATED_PATTERN.
