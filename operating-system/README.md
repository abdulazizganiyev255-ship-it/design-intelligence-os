# Design Intelligence OS v0.3 — Sequential Production System

**State:** proposed/feature branch. **Execution:** ChatGPT role-play + GitHub records, **not** four autonomous services. **Source of truth:** `operating-system/stages.json`; existing Foundation rules remain authoritative if inconsistent.

## House-building analogy translated into gates

| Stage | Building analogue | Design output |
|---|---|---|
| S00 | Existing ground inspection | source evidence, visual baseline, preserve/reject |
| S01 | Requirements and site plan | user job, product brief, success metric |
| S02 | Blueprint | IA, navigation, complete flow map |
| S03 | Room placement, low-fi plans | wireframes, semantic content hierarchy |
| S04 | Architectural expression | **two different** creative concepts + Owner choice |
| S05 | Materials and dimensions | typography, color roles, spacing, icon/motion rules |
| S06 | Doors, windows and fixtures | buttons, fields, lists, dialogs, charts, states |
| S07 | Rooms assembled | full screens, realistic content, visual comparison |
| S08 | Walk-through | interactive prototype, actual task tests |
| S09 | Construction | source implementation + regression tests |
| S10 | Building inspection | multi-layer QA and evidence-based score |
| S11 | Handover | human Owner approval and release/rollback |
| S12 | Post-occupancy learning | defects, confirmed patterns, manual retrieval/RAG later |

**Non-negotiable order:** S02 must precede S03; S03 before S04; do **not** choose color/button details before IA and visual direction. Design references and constraint research may be collected **in parallel**, but their application follows stage gates. Iteration can return to a prior stage with a written reason; this is not a one-way waterfall.

## Workflow

1. Identify the earliest unapproved or failed stage, and gather its specified inputs.
2. Lead role produces artifact; all four roles review it under `operating-system/board-stage-contract.md`.
3. Record individual observations, critique, decision, evidence and failed gates in `operating-system/templates/stage-review.md`.
4. Status: `NOT_STARTED | IN_PROGRESS | NEEDS_EVIDENCE | REVISE | PASSED | BLOCKED`. No averaged magic score; each reviewer gives 0–5 **readiness with evidence** or null. A 100-point visual quality score only exists at S10 with full coverage.
5. If a hard gate fails, loop to that stage and preserve valid elements. At most 2 critique cycles without fresh evidence; then stop/escalate.
6. `owner_gate: true` demands explicit human selection/approval. Without it, progress is provisional.
7. After successful S10/S11, add a verified learning record; vector RAG is **not** installed in v0.3.

## Cross-stage rules

- `FACT` vs `HYPOTHESIS` vs `DESIGN_JUDGMENT` vs `UNKNOWN` labels.
- Content and financial truth outrank illustration; avoid fake charts, progress scores, AI advice and bank connections.
- Reuse *ideas* from third-party design systems, not unauthorized code, screenshots or assets.
- No production writes merely because a concept looks polished.
- Distinguish `stage readiness` from `product quality`, and `simulated Board perspectives` from genuine independent reviews.
- S00–S04 can use manual ChatGPT/GitHub for **$0 in additional API spend**; later coding tools incur usage or CI quota as applicable.

## Starting case: Hisobchi AI

The owner has rejected all previous visual styles. Source-backed partial audit is linked in `baseline/hisobchi-ai/BASELINE-001.md`. Two exploratory visual directions were produced; **neither was approved as a final target**. Preserve finance data/source semantics and tested transaction logic; reset visual direction. Track stage state in `operating-system/projects/hisobchi-ai.json`.

## Implementation references

- `operating-system/board-stage-contract.md` — every stage is reviewed.
- `operating-system/audit-v2.md` — critique and QA.
- `design-system/README.md` — foundations then components.
- `knowledge/source-registry.csv` — verified upstream references and readiness.
- `knowledge/research-policy.md` — source evaluation and RAG readiness.
- `tools/validate_operating_system.py` — structure gate (not actual aesthetic or usability testing).
