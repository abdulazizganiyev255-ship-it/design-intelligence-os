# Board Decision Policy v0.1

## Statuslar

`PROPOSED`, `NEEDS_EVIDENCE`, `REVISE`, `ACCEPTED_FOR_PROTOTYPE`, `REJECTED`, `APPROVED_BY_OWNER`, `SUPERSEDED`.

`ACCEPTED_FOR_PROTOTYPE` — concept ishlab ko'rishga ruxsat, **release approval emas**.

## Qaror algoritmi

1. **Problem statement:** foydalanuvchi vazifasi va biznes zarurati.
2. **Options:** kamida 2 mazmunan farqli yo'l yoki nega bittagina yo'l qolganining isboti.
3. **Evidence:** E-ID bilan tasdiqlangan narsa; yo'q bo'lsa `UNKNOWN`.
4. **Individual perspectives:** Creative → UX → Architect → Reviewer (birinchi roundda mustaqil pozitsiya ko'rinishi).
5. **Objection round:** zaif nuqta, xavf, javob; shaxsga emas yechimga tanqid.
6. **Resolution:** Owner uchun tavsiya, dissent, ochiq risk va validation.
7. **Recording:** `templates/decision-record.md` to'ldiriladi.

## Eskalatsiya/stop qoidalari

- P0 yoki P1 unresolved = `RELEASE_BLOCKED`.
- Testdan o'tmagan yangi feature = `PLANNED/DEMO/UNVERIFIED` deb belgilansin.
- 2 review rounddan keyin muammo turib qolsa: ko'proq test/ref yoki Owner qarorini kutish; cheksiz iteratsiya yo'q.
- Owner fikriga zid dalil bo'lsa ochiq aytish, kontekstni yo'qotmaslik.

## Vizual tanlov strategiyasi

Standart tasodifiy A/B/C rang o'zgartirish emas. Ikki konsept kompozitsiya, iyerarxiya va interaksiya modeli bo'yicha haqiqiy alternativ bo'lsin. Biri tanlangandan so'ng 'visual freeze' — muvaffaqiyatli elementlar saqlanadi, aniqlangan muammo uchun targetli rework.

## Approval chegaralari

Board faqat recommendation beradi; Owner `APPROVED_BY_OWNER` deydi. Code merge/deploy, real user validation yoki huquqiy risklar uchun alohida amalga oshirish va tekshirish talab qilinadi. Simulyatsiya mustaqil audit yoki user research'ning ekvivalenti emas.
