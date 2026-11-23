# Critical Audit Engine v0.3 — do not confuse checks with taste

The system needs an audit **before each dependency gate**, rather than an ungrounded final 92/100. Four independent *dimensions* of scrutiny, reviewed by the simulated Board, with reproducible issues and evidence.

## Audit layers and cadence

1. **Evidence & reality (S00–S01):** verify screenshots, version, user statements, original source URL, licenses, business/data claims. Reject invented user statistics, fake AI advice or unsupported trends.
2. **Information architecture & psychology (S02–S03):** task priority, labels, flow, back/cancel/error, missing states, real choices, Fitts/Hick/Gestalt heuristics as *hypotheses*, actual test plan.
3. **Taste & visual craft (S04–S07):** uniqueness serving meaning, composition and rhythm, hierarchy, type/color roles, clutter, repeated generic cards, brand fit; don't assume gradients or glass effect = premium. Compare real screenshots at identical viewports.
4. **Implementation & accessibility (S06–S10):** component states, click/touch/keyboard, focus, large font, contrast, reflow, images/content licensing, data sourcing, performance. Web axe + Playwright do **not** equal native TalkBack/VoiceOver coverage.
5. **Release & long-term regressions (S10–S12):** error paths, finance invariants, P0/P1 closure, owner review, rollback and lessons captured.

## Four reviewer critiques on every gate

For each stage UR checks task completion and mental-model cost; CD checks whether form and visual expression suit meaning; DA checks states, tokens, responsiveness and data truth; CR challenges evidence, assumptions and hidden blockers. **Every critic must supply** observation, scope, evidence/unknown, severity, effect, minimum viable correction and re-test.

## Issue severity (evidence-based)

P0: critical user harm/data/security/irrecoverable action; release stop.
P1: primary task blocked, major a11y barrier or deceptive financial claim; release stop.
P2: meaningful friction, visual hierarchy failure, inconsistent component states; target fix.
P3: polish or minor deviations with negligible task effect; batch if useful.

Owner simply disliking a theme is a **strong visual rejection/selection signal** but not automatically P0/P1. A design may pass automation and still fail Owner acceptance.

## The score conflict

- **Stage readiness** 0–5 per reviewer = limited decision aid, NOT visually validated product score. A null means unknown, not failure.
- **Existing 100-point rubric** `governance/quality-rubric.md` ONLY at scored product QA when all seven dimensions have evidence. Score missing one? `UNSCORED`; don't secretly reweight.
- **S+** requires the original release gates, real external human review and explicit Owner approval; never simulate those in one ChatGPT response.
- **Cognitive psychology / taste** are diagnostic lenses, not scientific numeric generators.

## Real iteration discipline

Freeze a chosen layout before implementation. Each failed check creates a `finding_id`, root-cause hypothesis, precise smallest revision, before/after evidence, changed tests and reviewer. Work on the **top three impact/effort fixes**, don't blindly rewrite everything.

If the owner rejects all visual directions: preserve confirmed functional flows and truth contracts, return to S01–S04. Do not "improve" the same layout with another color palette.

## Evaluation metrics and efficiency

Track: **critical issue escape rate** (# post-approval P0/P1 / # inspected flows), **rework cycle count**, **task success** (# actual passes / attempted tasks), **acceptance lead time**, **visual acceptance by Owner** (explicit yes/no + reasons), **repeated known defect rate**, **evidence coverage** (evidenced required assertions / required assertions). Define denominators and capture context; no fabricated measurement.

The user's 'useful coefficient' is NOT a universal number. As a management dashboard, show separate useful outcome and resource measures: accepted artifact / review cycles; proven task success; regression count; direct spend/CI minutes. **Do not optimize for a single gamified score** that rewards shallow design.

## Release checklist

- All P0/P1 resolved and retested
- Source truth, demo/live states and permissions accurately shown
- Product task acceptance tests run on relevant platform
- Visual render inspected at target breakpoints
- WCAG-related checks + real native accessibility when required
- Owner approved final chosen visual and release scope
- Failure/rollback and data migration risk assessed
