---
name: design-tokens
description: Specify platform-neutral semantic design tokens and verify aliases/roles after visual freeze.
---

# design-tokens — Design Intelligence OS v0.3

**Stage:** S05. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Specify platform-neutral semantic design tokens and verify aliases/roles after visual freeze.

## Inputs
selected concept, typography/color/layout specifications, brand identity, intended web/native platforms.

## Procedure
1. Define token taxonomy: primitive palette/type/space, semantic role names and component-specific aliases.
2. Use current DTCG $type/$value style where supported; record converter version and limitations before production.
3. Map light/dark/focus/status modes and state inheritance; avoid arbitrary inline values.
4. Test conversion for each target platform only when actual platform build tools exist.
5. Review tokens with UX/Creative/Architect/Reviewer and prohibit design-system signoff without rendered usage.

## Outputs
versioned design-token set, semantic alias inventory, platform mapping, conversion/contrast tests.

## Acceptance / Quality gate
No unresolved semantic ambiguity or unsupported syntax; sample tokens cannot be silently treated as approved brand tokens.

## Sources and caution
https://github.com/design-tokens/community-group ; https://github.com/style-dictionary/style-dictionary

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
