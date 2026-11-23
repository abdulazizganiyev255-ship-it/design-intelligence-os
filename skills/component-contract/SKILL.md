---
name: component-contract
description: Define accessible design system component anatomy, variant/state/interaction contracts and exact acceptance tests.
---

# component-contract — Design Intelligence OS v0.3

**Stage:** S06. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Define accessible design system component anatomy, variant/state/interaction contracts and exact acceptance tests.

## Inputs
S05 foundations, S02 flow states, selected concept and platform-specific interaction constraints.

## Procedure
1. Start with atomic controls: text, button, input, icon, feedback, focus then composite filters/nav/transaction/graph.
2. Specify purpose, variants, disabled/loading/error/selected/focus states, content lengths and action outcomes.
3. Use headless accessibility patterns as reference on web; do not assume web Radix runs in React Native.
4. Review screen-reader label, keyboard/touch, confirmation and error recovery for each component.
5. Create component evidence specimen and record downstream screens that could regress when changed.

## Outputs
component-contract record, state matrix, screenshot variants and test plan.

## Acceptance / Quality gate
No fake buttons or missing primary state; component consistent with semantics, tested in chosen platform where implementation is claimed.

## Sources and caution
https://github.com/adobe/react-spectrum ; https://github.com/radix-ui/primitives ; https://github.com/Shopify/restyle

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
