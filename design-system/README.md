# Design System Workshop — Build from foundations, not button colors

**Status:** SPECIFICATION_ONLY until an Owner-approved S04 visual direction exists. This does NOT install a UI library or commit Hisobchi AI brand colors.

## Dependency order

1. **S01–S03: structure first.** User tasks → navigation → information hierarchy → wireframes. No forced color or generic preselected cards.
2. **S04: visual target.** Two distinct concepts, image/render comparison and actual Owner decision. A screenshot is not a code implementation.
3. **S05: foundations.** Identity principles → typography → grid/spacing → semantic color roles & contrast → iconography → elevation/motion. Token values reflect the chosen direction, never arbitrary AI taste.
4. **S06: primitives.** Text, button, input, icon, surface, divider, feedback, focus ring, loading, error/empty/disabled; full state contracts.
5. **S06: composites.** Bottom tabs/navigation, search/filter, date picker, transaction row, data summary, charts, confirmation/modal, cards only where meaningful.
6. **S07: screens and patterns.** Home, History, Entry, Analytics, Profile composed from real content and reusable contracts. 320/390/1440 viewport targets where applicable.
7. **S08–S10: verify actual interactions.** Form validation, navigation, focus/keyboard, long currency strings, dynamic type, dark/light modes and accessibility. Fixes regenerate tokens/components before screen-level overrides.

## Rules for choosing frameworks

- *React web:* Radix, React Aria and Primer are reference architectures; shadcn is web component code, not a visual identity.
- *React Native:* Expo/React Native and native-tested components; Shopify Restyle is a **candidate**, not a selected dependency. Web Radix components don't run natively by swapping imports.
- Cross-platform: semantic token meanings can be shared; actual HTML/CSS vs native controls and accessibility must be tested separately.
- Do not invent style values before Owner approves the chosen visual target. `design-system/tokens/example.tokens.json` is explicitly illustrative.

## Required Foundation spec

`type-scale` (readability and truncation) · `grid and spacing` (density and alignments) · `semantic color` (surface, foreground, action, status) · `icon rules` (same optical weight) · `radius/elevation` (hierarchy, not default) · `motion` (meaning, reduced-motion) · `data visualization` (true quantities, axes, provenance).

## Component minimum contract

Every component identifies `purpose`, `dependencies`, `variants`, `states`, `content constraints`, `accessibility`, `responsive`, `actions`, `QA` and `source truth`. See [component-contract.md](component-contract.md) and [component-inventory.csv](component-inventory.csv).

## Board checkpoints

S05 all four roles review type/color/spacing for goal and contrast; S06 validate behaviors/states/tokens; S07 check full visual against selected target; S08 verify interactions. Record opinions 0–5 or null using `operating-system/templates/stage-review.md`. Owner still approves visual freeze.

## Anti-patterns

- A new accent color every iteration
- Card inside card inside card without informational reason
- Floating CTA obscuring content
- One font size for the entire page / 10px key metadata
- Dense KPI dashboard with no top task
- Chart depicting an unverified metric
- Screenshot-perfect visual with dead buttons
- Using a website-oriented taste skill as proof of a good React Native experience
