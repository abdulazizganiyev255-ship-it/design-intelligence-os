# Component Contract v0.3

**Prerequisite:** S05 tokens and a screen/task map. Templates are reusable but actual component implementation comes after visual freeze.

## Required fields

```yaml
id: CMP-001
name: Button
purpose: one observable action
stage: S06
depends_on: [semantic-tokens, interaction-contract]
platform: [web, native-if-supported]
variants: [primary, secondary, destructive, quiet]
sizes: [compact, regular]
states: [default, pressed, focus-visible, disabled, loading, error-or-success-feedback]
content:
  label_required: true
  min_hit_target: platform-specific
  long_text_strategy: wrap-or-expand-without-clipping
interaction:
  on_press: documented handler
  loading: repeated submission guarded
  success: resulting UI changes or explicit confirmation
accessibility:
  name: meaningful label
  semantics: button
  keyboard: activation and focus where available
  color_not_only_signal: true
source_truth:
  fake_action_prohibited: true
qa:
  - tap/keyboard works on actual platform
  - focus and error state visible
  - 320px and long Uzbek label do not clip
  - disabled and loading states valid
owner_visual_approval: PENDING
```

## States (all composite controls)

- default / hover (web) / pressed / focus-visible / selected / disabled / loading / error / success / empty (when relevant).
- Modal: escape/back close, cancel, focus return, heading, keyboard; destructive action confirmation.
- Filter/search: visible applied filters and reset; date-range bounds and inclusive logic.
- Charts: explicit axes, series meaning, zero/no-data handling, accessible numeric summary, source legend; never misleading percentages.
- Navigation: current destination and back behavior; avoid hidden/unreachable actions.

## Atomic → composite → screen

`token → primitive → composite → screen → full flow`. Each component has **source of truth** and avoids arbitrary local values. A verified fix propagates to dependent screens with screenshot regression checks.

## Acceptance

1. Does it serve a named user task?
2. Are all variants/states and actions specified and executed where claimed?
3. Does the component comply with approved semantic tokens?
4. Is it usable on mobile and with enlarged text?
5. Are real labels, warnings, and errors readable?
6. Has QA actually run and been documented, or honestly NOT_TESTED?
7. Have CR and Architect independently challenged it as **role perspectives**?
