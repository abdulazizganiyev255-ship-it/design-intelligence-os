---
name: interaction-motion
description: Specify purposeful interaction states, feedback and motion with focus/keyboard/touch and reduced-motion constraints.
---

# interaction-motion — Design Intelligence OS v0.3

**Stage:** S08. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Specify purposeful interaction states, feedback and motion with focus/keyboard/touch and reduced-motion constraints.

## Inputs
S07 approved screen target, task transitions, platform, real copy and available event behavior.

## Procedure
1. Map trigger, action, loading, validation, success/failure, cancellation and recoverability.
2. Explain why animation helps comprehension; omit purely ornamental movement if it delays task.
3. Ensure state feedback cannot be confused with live backend confirmation unless service actually succeeded.
4. Test keyboard/focus and native hardware back/gesture where platform applies.
5. Measure perceived and actual responsiveness where possible; respect reduced-motion settings.

## Outputs
interaction specification, state transitions, event/recovery table, observable test checklist.

## Acceptance / Quality gate
Every visible control has real action or explicitly labelled demo; no dead CTA/false success or trapped modal.

## Sources and caution
https://www.w3.org/TR/WCAG22/ ; https://github.com/adobe/react-spectrum

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
