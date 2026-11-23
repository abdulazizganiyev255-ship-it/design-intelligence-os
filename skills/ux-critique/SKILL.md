---
name: ux-critique
description: Perform evidence-tagged heuristic and visual UX critique of a supplied screenshot, prototype or flow with severity, corrective actions and an honest scored-or-unscored outcome. Use for audits, never fabricate tests.
---

# UX Critique Skill — v0.1

**Objective:** xatolarni qayta tiklash mumkin bo'lgan shaklda aniqlash va qayta testlash.

## Inputs

`screen_or_flow`, `evidence_manifest`, `approved_brief`, `task_scenario`, `device_state`, `rubric`, `prior_findings`.

## Procedure

1. Evidence preflight: mavjud fayl yoki URL haqiqatan ko'rildimi? yo'q bo'lsa `UNSCORED`.
2. Task walkthrough: start, action, feedback, error, recovery.
3. NN/g heuristics va visual craft check; a11y WCAG 2.2 AA target; responsive coverage.
4. Har issue: `id`, `severity`, `location`, `observation`, `impact`, `evidence_ids`, `steps`, `fix`, `retest`.
5. Rubric 7 ratings: evidence bo'lsa 0..5, bo'lmasa null; total null if any missing.
6. Prioritization P0 -> P1 -> P2 -> P3; yaxshi ishlayotgan elementlarni preservation list'ga yoz.
7. Report + accepted corrections, Owner sign-off status.

## Outputs

`templates/audit-report.md`ga mos audit report, evidence-tagged issues, scorer, not-tested list, release gate.

## Acceptance

- P0/P1 bor ekan release PASS emas.
- Scope, observation va inferences farqlangan.
- Screenshot -> keyboard proof emas; static mockup -> functional proof emas.
- Re-review result or `NOT_TESTED` to'g'ri qayd etilgan.
- Simulated reviewer mustaqil user test bilan aralashtirilmagan.

## Negative example

“10/10, WCAG compliant” deya faqat bitta screenshot asosida xulosa qilish = invalid.
