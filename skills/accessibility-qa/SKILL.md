---
name: accessibility-qa
description: Audit real rendered components and flows for WCAG-related barriers and native accessibility constraints.
---

# accessibility-qa — Design Intelligence OS v0.3

**Stage:** S06–S10. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Audit real rendered components and flows for WCAG-related barriers and native accessibility constraints.

## Inputs
actual rendered UI, target platform, device/viewport, interaction script, selectors and focus semantics.

## Procedure
1. Check contrast/labels/roles/focus/error/touch targets and 320px reflow with appropriate standard scope.
2. Use axe-core and Playwright for web automated issues, separately documenting what they cannot see.
3. Perform manual keyboard and focus-return checks; dynamic type, screen reader and native gestures need actual device/emulator evidence.
4. Link each finding to screenshot/log + severity + steps to reproduce.
5. Retest fixes at same task, viewport and content; do not declare universal WCAG compliance.

## Outputs
accessibility audit with E-IDs, P0–P3 issues, fixes and retest evidence, NOT_TESTED per platform.

## Acceptance / Quality gate
No critical access blocker for intended release, no unsupported 'fully accessible' claim, manual/native coverage disclosed.

## Sources and caution
https://www.w3.org/TR/WCAG22/ ; https://github.com/dequelabs/axe-core ; https://playwright.dev/docs/accessibility-testing

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
