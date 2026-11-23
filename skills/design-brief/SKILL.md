---
name: design-brief
description: Create a decision-ready product design brief from an owner goal, user task and constraints. Use before concept ideation or when requirements drift; never invent user interviews.
---

# Design Brief Skill — v0.1

**Objective:** go'zal ekran haqidagi noaniq so'rovni foydalanuvchi vazifasi, scope, qabul mezoni va ochiq savollarga aylantirish.

## Trigger / do not trigger

Use: yangi ilova, yangi flow, redesign yoki katta konseptni o'zgartirish. Do not use: kichik kosmetik bugfix, allaqachon approved brief o'zgarmagan holat.

## Preconditions

Owner goal yoki muammoni tushunish. Platform ma'lum bo'lmasa `UNKNOWN`; taxmin bilan noaniqlik ajratilsin. Prior screens mavjud bo'lsa ularni dalil sifatida ko'rsatish, ko'rinmasa uydirmaslik.

## Input contract

`product`, `audience`, `primary_job`, `platform`, `current_state`, `constraints`, `available_evidence`, `out_of_scope`, `success_metric`, `owner_preferences`.

## Procedure

1. Muammoning root cause ehtimollari va isbotlangan faktni ajrat.
2. 1 primary job va 1-3 supporting tasks yoz.
3. Main flow va fail/empty/loading states aniqlang.
4. Tech/business/time constraints, explicit non-goals yoz.
5. Observable acceptance criteria va minimum test plan yarating.
6. Unknowns'ni `BLOCKING` va `NON_BLOCKING`ga ajrating; agar blocking bo'lmasa tavsiya qilingan defaultni belgilang.
7. `templates/design-brief.md` nusxasini to'ldiring va `READY_FOR_OWNER_REVIEW` sifatida saqlang.

## Output

`projects/<id>/brief.md`: `problem`, `facts`, `hypotheses`, `user_journey`, `scope_in/out`, `constraints`, `acceptance`, `evidence`, `risks`, `unknowns`, `status`.

## Quality gate

- User job va observable success qayd etilgan.
- Feature status/live/planned aniq.
- User testing va mavjud bo'lmagan analytics to'qilmagan.
- Non-goals va constraints bor.
- Owner review o'tmaguncha `APPROVED_BY_OWNER` deb e'lon qilinmaydi.

## Example

Input: “Dashboard professional bo'lsin.” Output: “10 soniya ichida asosiy holat va keyingi action topilishi kerak; 360px/1440px tekshiriladi; mavjud dark/light states UNKNOWN.”

## Escalation

Maqsad va platform o'rtasida jiddiy ziddiyat bo'lsa Owner qaroriga qayt.
