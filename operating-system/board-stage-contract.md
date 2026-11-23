# Stage-by-stage Board Review v0.3

**Board = structured perspectives in ChatGPT, not four independent agents.** `Owner/Chair` is a human decision-maker. Four mandatory reviewers: UX Researcher (UR), Creative Director (CD), Design Architect (DA), Critical Reviewer (CR). At S00, S01, S02, S03 UX leads; S04, S07 Creative leads; S05, S06, S09 Architect leads; S10, S11 Reviewer leads; S12 UX curates. All **four** review every gate.

## Meeting protocol

0. **Preflight:** stage ID, inputs, linked artifacts, owner statements, evidence E-IDs, unknowns, dependencies passed?
1. **Blind-perspective first pass (simulation):** role speaks without echoing approval. In a single model this is role separation, *not independent reasoning*. Each reports: `position`, `basis`, `evidence_ids`, `readiness_rating: 0..5|null`, `most_material_risk`, `corrective_action`.
2. **Critical cross-examination:** 2 substantive objections, including at least one alternate interpretation, strongest potential regression and how to test it. Do not manufacture conflict for theater.
3. **Decision proposal:** `PASS | REVISE | BLOCKED | NEEDS_EVIDENCE`; dissent preserved; reason, owner gate and specific next action. A stage can pass without unanimous taste agreement if critical evidence is sound; a missing safety/financial-truth gate blocks.
4. **Evidence check:** separate observed behavior from visual judgment, UX hypothesis, recommendation. No ratings without evidence and a clear rating scope.
5. **Record:** `operating-system/templates/stage-review.md` copied into project review folder; Owner approves S00/S01/S04/S07/S11 as indicated by stages.json.

## Readiness anchors (NOT the product's 100-point S+ rubric)

- null: not inspected / required evidence absent.
- 0: stage outcome unusable against known requirement (proven).
- 1: fundamental contradiction or missing core deliverable.
- 2: major revisions needed; some correct elements.
- 3: plausible but incomplete; needs targeted fixes before next gate.
- 4: substantively ready with documented minor risks.
- 5: meets stage acceptance in reviewed evidence scope, no open gate blocker.

**Decision rule**: required artifacts complete + each critical reviewer reports evidence or null reason + no P0/P1 design/financial-truth hazard + no unresolved high-risk contradiction + owner gate if required. Readiness figures are **not averaged**, and a median/mean cannot automatically pass. Differing ratings by >=2 trigger a written Board dissent review. A null rating on a required critical dimension blocks rather than being treated as zero.

## Each member's responsibility at every stage

| Reviewer | Consistent question | Special attention |
|---|---|---|
| UR | Can the target person accomplish the intended task? | cognitive load, IA, findability, language, flow |
| CD | Does form, hierarchy and visual character serve the task? | taste, contrast, composition, originality |
| DA | Can the solution be represented as reusable, accessible, testable components? | tokens, states, stack, data contracts |
| CR | What is wrong, unproven, misleading or unsafe? | evidence, severity, regressions, blind spots |

**Veto policy**: CR flags P0/P1, missing truth, or no evidence. It is a gate recommendation documented in decision log, not arbitrary personal override. Owner cannot reinterpret untested product as tested; reduce scope or collect evidence instead.

## Escalation

Two cycles without new evidence → mark `BLOCKED` or `NEEDS_EVIDENCE`; request minimum missing asset/decision. No infinite polishing. A broad aesthetic rejection after S04 returns to S03/S04, **not** to random button colors in S06. Unexpected code regression returns to S09 while preserving an approved design target.

## Opinion format

```yaml
role: creative-director
position: "..."
basis: DESIGN_JUDGMENT
evidence_ids: ["E-..."]
readiness_rating: 3
most_material_risk: "..."
corrective_action: "..."
dissent: "..."
```

When an actual independent human or multiple independent agents later exist, record the true mode and provenance explicitly. Never label an internal simulation as external validation.
