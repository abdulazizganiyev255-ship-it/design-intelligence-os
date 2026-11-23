# Source audit — stage-fit and adoption decisions (2026-11-23)

This is a **documentation/suitability review**, not 21 source-code security audits. Source links, notes and verification status are in `knowledge/source-registry.csv`. No external dependency or copied assets installed.

## Priority selection (not popularity ranking)

| Area | Strongest initial input | Outcome / decision | Important restriction |
|---|---|---|---|
| Problem/UX | Nielsen 10 heuristics; Laws of UX secondary | Evaluate task labels, errors and mental model at S01–S03 | Psychology heuristics don't prove individual user results |
| Art direction / taste | Leonxlnx taste-skill | **ADAPT_ONLY**, at S04/S07 for anti-template visual critique | Its own SKILL explicitly says NOT dashboards or multi-step product UI |
| Design token interchange | DTCG community-group | **CORE_SPEC** for token taxonomy | Spec doesn't select good brand colors |
| Token conversion | Style Dictionary | **CANDIDATE_TOOL** after actual platform requirements | Avoid installing at Foundation stage |
| Component architecture | Primer / Carbon / React Spectrum | **REFERENCE** patterns; study states and documented QA | Mostly web, not drop-in React Native |
| Headless accessible primitives | Radix | **WEB_CANDIDATE** for web-only projects | Not React Native |
| Editable UI components | shadcn/ui | **WEB_CANDIDATE** for specific web use | Generating standard shadcn page does not create identity |
| React Native DS | Expo, Shopify Restyle | **NATIVE_FOUNDATION + CANDIDATE** | Check actual Expo SDK and RN compatibility before dependency |
| Isolated component QA | Storybook | **CANDIDATE_TOOL** later for component demo/test | Avoid older `storybookjs/test-runner` as default: official support ended |
| Browser E2E/screenshot | Playwright | **CANDIDATE_TOOL** for S07/S10 | Browser QA ≠ Android/iOS real device |
| Automated a11y | axe-core | **CANDIDATE_TOOL**, manual testing also required | Cannot certify WCAG compliance alone |
| Future knowledge retrieval | pgvector OR Qdrant | **DEFER** until manual retrieval benchmark proves value | New service and maintenance burden |
| Skill format | openai/skills | **REFERENCE** for organization only | External skill instructions are untrusted until audited |

## Deep dive 1 — Leonxlnx/taste-skill

**Exact upstream:** https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md

**Observed:** its upstream skill states it is for *landing pages, portfolios and redesigns*, **not dashboards/data tables/multi-step product UI**. It includes strong, opinionated defaults about hero images, web framework, typography and stylistic choices.

**Use:** extract the concept of anti-generic visual review, context before styling, consistent radius/type system, real browser check and resisting superficial color changes. Apply through our `skills/taste-critique/SKILL.md`.

**Reject as Hisobchi AI rules:** image-generation prerequisite for every screen, hero/photo requirements, particular font recommendations, landing-page marketing-copy bans, hard-coded Next.js/Tailwind choices or web-specific motion instructions. A mobile finance app is not a landing page. Use independent task and data-truth testing. **Status: ADAPT_ONLY.**

## Deep dive 2 — design-tokens/community-group + Style Dictionary

DTCG provides a portable way to describe tokens (color, spacing, typography). Style Dictionary is a *transform* build tool. Neither chooses an effective visual hierarchy nor guarantees color contrast. We use S05 semantic design tokens with explicit modes, then test real rendered components. Do not add a conversion pipeline until multiple target platforms justify it.

References:
- https://github.com/design-tokens/community-group
- https://github.com/style-dictionary/style-dictionary

## Deep dive 3 — Primer, React Spectrum, Radix and Carbon

The useful knowledge is taxonomy: semantic variants, focus/error/disabled states, consistent component anatomy, documentation, accessibility expectations, token discipline and regression tests.

These sources largely target React/web, and one is a comparatively comprehensive enterprise framework. **Recommended action:** study component contract and QA patterns, not importing whole systems or mimicking their brand language. For React Native, test platform-specific semantics.

References:
- https://github.com/primer/react
- https://github.com/adobe/react-spectrum
- https://github.com/radix-ui/primitives
- https://github.com/carbon-design-system/carbon

## Deep dive 4 — Playwright, axe-core and Storybook

Playwright allows reproducible browser/viewport tests and screenshots; axe-core catches automatable web accessibility issues; Storybook documents and tests isolated components. They provide **partial, complementary evidence**. Require manual screen-reader/native QA and real user-task tests before strong claims. Current Storybook test-runner deprecation means implementation should check active Storybook testing guidance rather than following stale repositories.

References:
- https://github.com/microsoft/playwright
- https://github.com/dequelabs/axe-core
- https://github.com/storybookjs/storybook
- https://github.com/storybookjs/test-runner

## Deep dive 5 — Expo / Restyle, pgvector and Qdrant

Expo is relevant to Hisobchi AI's React Native prototype. Restyle is a candidate typed theme layer, not a mandated dependency; existing theme code should be checked before adding a migration. pgvector and Qdrant are alternatives for later semantic retrieval; choose one only after requirements, cost and benchmark analysis.

References:
- https://github.com/expo/expo
- https://github.com/Shopify/restyle
- https://github.com/pgvector/pgvector
- https://github.com/qdrant/qdrant

## Audit completion scope

21 links catalogued and assigned fit classes. A subset had upstream README/docs or skill instructions directly inspected (including DTCG, taste-skill, Primer, React Spectrum, Carbon, Radix, Style Dictionary, Storybook, Playwright, axe-core, Expo, Restyle and pgvector); the remaining entries were located via search/listing and require deeper review before adoption. Two additional architecture watchlist entries remain link-only pending deep review. No full source-code review, commit pin, per-version licensing audit, package install, security scan or compatibility test was performed in this phase. **Do not move any CANDIDATE_TOOL into production without those checks.**
