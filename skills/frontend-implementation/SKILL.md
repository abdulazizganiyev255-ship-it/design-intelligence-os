---
name: frontend-implementation
description: Implement only an approved visual target with reusable components, truthful data contracts and regression checks.
---

# frontend-implementation — Design Intelligence OS v0.3

**Stage:** S09. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Implement only an approved visual target with reusable components, truthful data contracts and regression checks.

## Inputs
Owner-selected visual, S05/S06 tokens/components, S08 prototype, source repository, actual API/data contracts.

## Procedure
1. Inspect current code and tests; record what must stay untouched including finance arithmetic and security.
2. Make a narrow implementation branch with explicit approved acceptance criteria.
3. Use platform-appropriate components and tokens, avoid unsupported web-to-native direct copy.
4. Run type/build/functional tests; capture actual renderer screenshots at target viewports.
5. Compare with selected visual, log differences and request targeted fixes instead of arbitrary redesign.

## Outputs
proposed PR, code diff, test log, screenshot evidence, known limitations and rollback plan.

## Acceptance / Quality gate
No production merge without Owner approval; no claimed CI/device tests unless run and recorded; finance and auth unchanged outside scope.

## Sources and caution
https://github.com/expo/expo ; https://github.com/microsoft/playwright

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
