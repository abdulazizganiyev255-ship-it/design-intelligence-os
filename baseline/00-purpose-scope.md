# 00 — Baseline Audit: maqsad, scope va success criteria

## Bosqich holati

`PROTOCOL_READY / EVIDENCE_PENDING`. Bu hujjat **dizayn auditi bajarildi** degani emas. Joriy screenshot, source yoki prototip to'plami hali ushbu paketga kiritilmagan.

## Asosiy savol

Oldingi dizaynlar nimada zaif va yangi Design Intelligence OS ularni aynan qaysi ko'rsatkichlarda yaxshilashi kerak?

## Muammo formulasi

Ilgari dizaynga baho berishda estetik yo'nalish ko'p o'zgargan, aniq birlashgan referens/brief/quality gate yetarli bo'lmagan bo'lishi mumkin. Bular **tekshiriladigan gipotezalar**, tasdiqlangan nuqsonlar emas.

## Scope A: artefaktlar

- Rejected baseline: oldingi 1–3 real dizayn namunasi (screenshot + ekran nomi + versiya + ishlab turgan/yolg'on demo holati).
- Flow: onboarding, asosiy vazifa, qo'shish/tahrirlash, confirmation, empty, loading, error, permission, offline (tegishli bo'lsa).
- Platforma: 320 CSS px reflow, 360/390 mobil, 768 tablet, 1440 desktop; native ilovada kamida bitta haqiqiy qurilma.
- Interaction: click/tap/keyboard/focus, disabled/error/success va back navigation.
- Texnik real holat: linklar, yo'q yoki mavjud funksiyalar, kod va test mavjudligi (dalil bo'lsa).

## Scope B: jarayon

1. Maqsad/brief aniq bo'lganmi?
2. Foydalanuvchi vazifasi va qabul sharti tasdiqlanganmi?
3. Qaysi vizual referenslar nima sabab bilan tanlangan?
4. Konseptlar mazmunan farqlanganmi?
5. Mustaqil tanqid bormi yoki generatsiya o'zini tasdiqlaganmi?
6. Design tokenlar, komponentlar va platforma cheklovlari kelishilganmi?
7. Visual QA qaysi qurilmalarda va qaysi dalil bilan o'tkazilgan?
8. Topilgan nuqsonning qayta tuzatilishi tekshirilganmi?

## Audit bo'yicha o'lchanadigan ma'lumotlar

- 100 ballik quality rubric (faqat barcha 7 mezon uchun dalil bo'lsa).
- P0/P1/P2/P3 soni va dalillari.
- Eng muhim foydalanuvchi vazifasining completion holati: `PASS/FAIL/NOT_TESTED`.
- Ekran/flow/state coverage: tekshirilgan / rejalangan.
- Qayta ishlash soni va har iteratsiyadagi score delta (bir xil mezonda).
- UX audit, screenshot inspection va user testni alohida tasniflash.

## Definition of Done — baseline o'lchandi deyish uchun

- [ ] Kamida bitta real eski versiya tasviri yoki ishlaydigan prototip aniqlangan.
- [ ] Dalil manbasi va timestamp `evidence-manifest.csv`ga yozilgan.
- [ ] Kamida asosiy flow va barcha uning kritik state'lari tekshirilgan yoki `UNVERIFIED` sifatida qayd etilgan.
- [ ] Yetti mezon bo'yicha dalil bor; bo'lmasa yakuniy ball berilmaydi.
- [ ] Har P0/P1 muammo uchun aniq repro, impact va hal etish mezoni yozilgan.
- [ ] Owner baseline xulosasini ko'rib chiqqan.

## Baseline'dan keyingi maqsad

Yangi dizaynni eski dizayn bilan **bir xil vazifa, bir xil qurilma/viewport, bir xil baholash qoidasi** asosida solishtirish. S+ ichki yorlig'i >=85/100, blocker yo'q, acceptance tests va Owner tasdig'idan keyingina beriladi. Ushbu chegaraning o'zi ham dizayn sifati empirik isboti emas.

## Hozirgi fakt va noma'lumlar

- FAKT: foydalanuvchi dizayn natijalari sifatidan qoniqmagan, nazoratli dizayn tizimini istaydi.
- FAKT: dastlab ChatGPT ishlatiladi, Hermes keyingi bosqichga qoldirilgan.
- NOMA'LUM: barcha eski screenshotlarning yakuniy versiyasi, joriy linklar, ekranlar soni, haqiqiy mobile test va foydalanuvchi test natijalari.
- QOIDA: noma'lumlarni faktga aylantirmang.
