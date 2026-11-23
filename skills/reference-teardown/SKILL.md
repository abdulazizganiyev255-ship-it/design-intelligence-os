---
name: reference-teardown
description: Analyze a real UI reference from a verified URL or screenshot to extract visual and interaction principles with provenance and licensing caveats. Use when grounding art direction; never clone unlicensed assets.
---

# Reference Teardown Skill — v0.1

**Objective:** kuchli real dizaynni ko'rib, qayta ishlatish mumkin bo'lgan *prinsiplarni* ajratish, o'zlashtirish emas.

## Trigger / do not trigger

Use: reference URL/screenshot mavjud va yangi visual direction kerak. Do not use: original asset/source ko'rilmagan holda “falon sayt shunday” deb xulosa chiqarish.

## Inputs

`source_url_or_path`, `captured_at`, `viewport`, `product_category`, `task`, `screenshot_or_live_observation`, `rights_status`, `user_goal`.

## Procedure

1. URL, screenshot sanasi va ko'rilgan viewportni qayd et. Ko'rilmagan sahifa uchun `NOT_OBSERVED`.
2. Anatomy: visual hierarchy, grid, type, space, color roles, surfaces, navigation, micro-interactions, states.
3. Har kuzatuvni `OBSERVED`, `INFERRED`, `UNKNOWN` bilan belgila.
4. 3 strength, 3 tradeoff/weakness va 2 unsuitable context (topilmasa nega yo'q) aniqlang.
5. Qaysi prinsipni ko'chirmasdan *adapt* qilish mumkinligini tushuntir.
6. Source license/permission tekshirildi yoki `REVIEW_REQUIRED` deb yoz.
7. `templates/reference-card.md`ga yozing; reviewer approval bo'lmasa knowledge base'da `PENDING` qoldiring.

## Output

`reference_id`, `source`, `capture`, `visual_anatomy`, `interaction`, `strengths`, `tradeoffs`, `reusable_principles`, `not_for`, `rights`, `evidence`, `review_status`.

## Acceptance

- Original URL/path + observation scope bor.
- Har prinsip uning qanday user taskga xizmat qilishi bilan tushuntirilgan.
- Yalang'och “premium/minimal” sifatlari dalilsiz baho sifatida ishlatilmagan.
- Identik cloneni ruxsatli deb ko'rsatmagan.
- Har to'planadigan bilim validated bo'lishidan oldin review qilinadi.

## Negative example

“Linear UI juda zo'r, uni ko'chiramiz” — NOT ACCEPTED: na aniq page, na evidence, na reusable principle, na rights.
