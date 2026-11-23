# Pilot-01 Design Brief — Design Council Workspace

**Status:** WORKING_HYPOTHESIS. Ilova haqiqiy interfeys sifatida qurilmagan.
**Ma'lumot manbasi:** Owner tomonidan berilgan Design Intelligence OS ni ChatGPT+GitHub'da boshlash talabi va Foundation maqsadlari.

## Product goal

Designer yoki product owner bitta loyiha uchun brief, reference, board critique, decision va audit natijalarini yo'qotmasdan boshqarsin. Birinchi workflow: `brief → concept → critique → decision`.

## Target user

Dizaynni nazorat qiluvchi bitta builder / product owner (birinchi pilot). Haqiqiy foydalanish chastotasi yoki boshqa segmentlar hali o'lchanmagan.

## Job-to-be-done

“Yangi dizayn ishini boshlaganimda sifat mezonlari, referens va ekspert e'tirozlarini bir joyda ko'rib, qarorlarni qayta topa olsam.”

## Platform

Birinchi demonstratsiya responsive web: 360–390px mobile hamda 1440px desktop. Native iOS klon emas; iPhone-inspired clarity (axborot ustuvorligi, okunarlilik, minimal vizual shovqin).

## UI philosophy

Clarity first, originality with purpose, semantic color, readable typography; unnecessary gradients/glassmorphism/neon, kartalar orqali haddan ziyod segmentlash va fake AI controls yo'q. Mobile-first. Minimalism funksiyani kamaytirish emas.

## Scope In

Project status, active brief, 2 concept summaries, decision log, reviewer dissent, outstanding issues, single next action. Asosiy vazifa: brief'dan qarorgacha yo'lni kuzatish.

## Scope Out

Live multi-agent messages, vector RAG, background job, real design generation, pixel-level implementation, payments, push notifications, advanced analytics.

## Acceptance Criteria (pilot prototip uchun)

- User 3 ta action ichida aktiv loyiha briefini topadi.
- User qaysi qaror qabul qilinganini va kim/nega e'tiroz bildirganini topa oladi.
- Empty/loading/error holatlar tushuntirilgan; fake aktiv CTA yo'q.
- 360px va 1440px viewportga mos; keyboard-focus yo'qolmaydi.
- Vizual yo'nalish ikki mazmunan farqli konsept orqali ishlab chiqiladi.
- Owner konsept va kritik auditdan so'ng qabul qiladi.

## Open Questions

Real usability test, dizayn referenslarining yakuniy to'plami, haqiqiy source app structure va Figma/React implementatsiya hali yo'q.
