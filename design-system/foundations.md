# Foundation specification — S05

**Prerequisite:** S04 visual target selected by Owner. A palette is an *output* of accepted art direction, not the starting task.

## 1. Typography

Design roles, not arbitrary font sizes: `display` (rare high-value number), `title`, `heading`, `body`, `label`, `caption`, `numeric`. For each specify font family + fallback, optical size, weight, line height, wrapping, truncation, digit alignment, accessibility scale and multilingual test. Required strings: `12 850 000 so‘m`, `−120 000 so‘m`, longest Uzbek label, error message and 200% text. Use tabular numeral treatment for columns, not all headings.

## 2. Layout and rhythm

Start with visual hierarchy and content constraints from wireframe: viewport/safe area, min/max content width, spacing rhythm, grouping, dense/comfortable variants, scroll behavior. 320px compact and 390px normal mobile explicitly evaluated; desktop where relevant. Never rely on fixed height for long data or large fonts.

## 3. Color system

Separate raw palette values from semantic roles: `surface.base`, `surface.raised`, `text.primary`, `text.secondary`, `action.primary`, `action.on-primary`, `border.muted`, `feedback.error`, `feedback.success`, `focus.ring`, `chart.series.*`. State-specific colors and light/dark mapping must preserve meaning. Assess text 4.5:1 for ordinary and 3:1 for large (WCAG 2.2 AA relevant cases), 3:1 for meaningful nontext UI/focus where applicable. Check actual components, not just an isolated palette.

## 4. Shape and elevation

Define radius/elevation by functional layer (popover, modal, surface), not an arbitrary universal glass style. Use no more variants than the hierarchy requires; component families must stay consistent.

## 5. Iconography

One icon visual family; consistent optical weight, hit target and label. Icon-only buttons require accessible names. Brand mark is distinct from interface icons. Do not use unlicensed icon assets.

## 6. Motion

Define semantic transitions for navigation, selection, submission, errors and loading. Animations must not mask state or slow primary task. Include reduced-motion alternative; test device performance.

## 7. Money/data truth

Every prominent amount has provenance: DEMO, session-derived, synchronized, or not available. Balance, net difference, income, outflow and Safe-to-Spend are different concepts. Graph must not fake trends or future obligations.

## Gate before components

Reviewer requires: visual target + one full typography scale + contrast mapping + responsive grids + accessible statuses + icon/motion rules + example real content in selected language. Store Owner selection and risks; only then begin atomic components.
