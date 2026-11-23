---
name: visual-regression
description: Compare true before/after renders and approved design target using reproducible screenshots and explicit mismatch tolerances.
---

# visual-regression — Design Intelligence OS v0.3

**Stage:** S07–S10. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Compare true before/after renders and approved design target using reproducible screenshots and explicit mismatch tolerances.

## Inputs
baseline screenshots, selected target, same content/viewport/browser or native capture, build reference.

## Procedure
1. Freeze a reference capture with viewport, DPR, content/date, locale, OS/browser and source version.
2. Capture candidate at the same conditions, including errors, long values, empty and loading states.
3. Compare geometry, hierarchy, clipping, text legibility, overlap and action position; noise alone is not design failure.
4. For detected mismatch, log before/after E-ID, severity, likely CSS/component root cause and smallest correction.
5. Retest affected screens; distinguish acceptable intentional changes from accidental regressions.

## Outputs
visual diff report, screenshot ledger, reproducible failure and retest decision.

## Acceptance / Quality gate
Required states compared to actual source, no critical clipping/overlap; snapshots do not replace task or accessibility testing.

## Sources and caution
https://github.com/microsoft/playwright ; https://github.com/storybookjs/storybook

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
