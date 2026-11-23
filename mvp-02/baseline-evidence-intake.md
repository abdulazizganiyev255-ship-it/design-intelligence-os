# Baseline Evidence Intake — DESIGN-001

**State: EVIDENCE_PENDING / UNSCORED**. Fill this file for a *real* rejected design before claiming improvement. The template contains no evidence or measurements.

| Field | Value |
|---|---|
| Product | \`PENDING\` |
| Version or commit | \`PENDING\` |
| Platform | \`PENDING\` |
| Primary task | \`PENDING\` |
| User segment | \`PENDING\` |
| Device & viewport | \`PENDING\` |
| UI language/content | \`PENDING\` |
| Date of capture | \`PENDING\` |
| Actual evidence | \`PENDING\` |

## Evidence required for each kind of claim

- **Visual claims:** unmodified screenshot, design file frame or reliable capture of the real version with E-ID.
- **Behavior claims:** tested interaction, screen recording, error reproduction or meaningful implementation proof.
- **Accessibility claims:** measured contrast, keyboard/focus behavior, semantic labels and relevant manual or automated checks.
- **User outcome:** actual task test data if available; otherwise only an explicit hypothesis.
- **Technical feasibility:** runtime/platform/stack or prototype evidence; otherwise unknown.

Update \`baseline/evidence-manifest.csv\` with E-ID, file or URL, screen, state, viewport, date and capture provenance. Redact personal information and secrets before uploading, particularly because the repository may be public.

## Screen matrix (to be filled)

| Screen ID | Main action | Default | Loading | Empty | Error | Success | Evidence |
|---|---|---|---|---|---|---|---|
| S-01 | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | NONE |

## Acceptance script (not executed)

1. Open original version at recorded viewport.
2. Attempt the top user task. Record which steps, errors and blockers actually occur.
3. Check readability, hierarchy, tap target, focus, empty/error/confirmation states.
4. Re-run same task/viewport/content for a candidate revision; compare only like with like.
5. Mark any not performed step \`NOT_TESTED\`.

## Audit output contract

- Evidence inventory with exact screenshots and observations
- Up to five most impactful findings with priority, repro and correction
- Seven-dimension scorecard; \`total_score=null\` if any required evidence absent
- Two materially different design paths only *after* the actual primary task is clear
- Board session, objection round, Owner decision PENDING
- Improvement comparison only after candidate render and matching tests exist

## No-score policy

Until actual design evidence exists, \`baseline_total_score=null\`, \`status=UNSCORED\`. A blank intake is not a negative result and not a completed audit.
