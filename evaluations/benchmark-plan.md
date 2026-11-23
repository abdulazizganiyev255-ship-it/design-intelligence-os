# Benchmark Plan v0.1 — Design Intelligence OS improvements

**Status:** PROCEDURE_ONLY; no empirical before/after score.

## Hypothesis

Evidence-driven Design Council + visual targets + independent critique will reduce repeated severe UI problems and increase consistent visual quality compared with the previous ad-hoc design workflow.

## Baseline sample

Minimum one **real rejected** existing design artifact and one concrete primary task. Collect exact version, screenshots/prototype, device, and target user. Do not use synthetic mockups as evidence of previous releases.

## Test conditions

- Same task statement, content and platform for before vs after.
- 360px and 390px mobile + 1440px desktop where relevant; 320px reflow.
- Same rubric anchors and evaluator instructions.
- Reviewer sees evidence IDs and known limitations.
- Evidence from keyboard / touch / flow is separate from screenshots.

## Metrics

- Primary: total score delta only when all 7 categories have evidence.
- Safety: number of open P0/P1 (must be 0 for release).
- Behavior: top task success and number of steps, if real run observed.
- Process: repeated issue rate, decision traceability, number of revision cycles.
- Quality of learning: can new task retrieve a useful verified pattern and avoid a prior issue?

## Decision rule

No hard-coded claim of better quality based solely on first mockup. Improvement is meaningful if same-context scores increase, P0/P1 do not increase, task success is preserved or improved, and Owner agrees the visual outcome is better. If results conflict, record disagreement instead of forcing S+.

## Outputs

`baseline` vs `candidate` audit reports, issue trend, validated lesson, next iteration decision and open unknowns.
