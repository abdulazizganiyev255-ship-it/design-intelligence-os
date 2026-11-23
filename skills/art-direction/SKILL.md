---
name: art-direction
description: Generate and compare two meaningfully different high-quality visual directions grounded in a design brief and evidence. Use before visual target selection or for a major redesign; preserve validated working parts.
---

# Art Direction Skill — v0.1

**Objective:** asosli, bir-biridan kompozitsiya va mahsulot ifodasi bilan farqlanadigan ikki konsept taklif etish.

## Inputs

`approved_or_working_brief`, `reference_cards`, `visual_constraints`, `functional_constraints`, `prior_successes`, `platform`.

## Procedure

1. Brand/product meaning va asosiy user taskni 1 jumlada ifodala.
2. 2 creative principles va 2 anti-principles belgilash (masalan hierarchy vs decorative clutter).
3. Direction 01: layout archetype, information density, typography rhythm, color roles, signature interaction, tradeoffs.
4. Direction 02: mazmunan farqli composition, hierarchy, navigation/interaction, tradeoffs. Faqat rangni almashtirish yetarli emas.
5. Har konseptni UX task, accessibility, feasibility va source inspiration bilan solishtir.
6. Creative/UX/Architect/Reviewer board debate olib bor; dissentni yoz.
7. Owner qarorisiz concept freeze qilma; tanlangandan keyin faqat nuqsonga yo'naltirilgan revisions.

## Output

`concept-01`, `concept-02`, `contrast_table`, `design_signature`, `tokens_proposal`, `risks`, `board_recommendation`, `unknowns`.

## Acceptance

- Concepts materially different and task-aligned.
- 360px mobile va desktopda bosh iyerarxiya qanday ishlashi tushuntirilgan.
- Copycat/neon/glassmorphism optional emas, zarurat bilan asoslanadi.
- No fake working interaction claims.
- Board approval `ACCEPTED_FOR_PROTOTYPE` only.

## Failure mode

Qayta-qayta ranglarni almashtirish bilan “10/10 redesign” deyish mumkin emas. Aniqlangan zaif sababni tuzatish kerak.
