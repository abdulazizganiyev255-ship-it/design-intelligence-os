# Baseline Audit — amaliy SOP

## 0. Kirish materiallarini tekshirish

Kerakli kirishlar: product/version, platform, target user, 1–3 muhim vazifa, mavjud ekranlar yoki prototip URL, davriy test sanasi, viewport/device, asosiy state'lar, ma'lum funksional cheklovlar.

Agar screenshot mavjud bo'lmasa: `EVIDENCE_PENDING`, baseline total score = `null`. Hamma nuqsonni "tekshirilsin" sifatida ifodalang; 'ko'rdim' demang.

## 1. Evidence manifest

`baseline/evidence-manifest.csv`da har bir E-ID uchun fayl yoki URL, sahifa, ekran, vaqt, muallif/licensing va kuzatuv rejimi saqlanadi. Istalmagan PII, token yoki real maxfiy balansni kiritmang.

## 2. Inventory & journey

- Ekran -> komponent -> UI state (default/focus/disabled/loading/empty/error/success) ro'yxati.
- User journey: trigger, niyat, asosiy CTA, branch, edge-case, natija.
- Har talab: `OBSERVED/NOT_OBSERVED/NOT_APPLICABLE`.

## 3. Heuristic evaluation

Nielsen 10 heuristics'dan xarita: status visibility, real-world match, user control, consistency, error prevention, recognition, flexibility, minimalism, error recovery, help. Har bir topilmaga evidence ID va foydalanuvchi impactini bog'lang.

## 4. Visual craft evaluation

Asosiy savollar: first-glance hierarchy? semantic CTA? grid/spacing ritm? tipografiya kontrasti? rang semantikasi? vizual muvozanat? brendning o'ziga xos elementi? text clipping? shovqin/kartalar soni? light/dark consistency?

Mazmunan farqli bitta emas, **ikki** reference yo'nalish yarating, ularning foydalanuvchi vazifasiga xizmatini taqqoslang. Inspiratsiya isbotlanmagan effektlarni qo'shish emas.

## 5. Accessibility & responsive

WCAG 2.2 AA maqsad: normal text >=4.5:1, large text >=3:1; non-text UI contrast >=3:1 (tegishli holatlarda); faqat rang bilan ma'no bermaslik; keyboard, focus, labels, error identification; 320 CSS px reflow; kamida 360px va 390px mobile visual QA. Bir kriteriy automat testdan o'tishi to'liq WCAG compliance emas.

## 6. Finding severity

- `P0 BLOCKER`: xavfsizlik, noto'g'ri kritik data/qaror, asosiy oqimni tugata olmaslik, sezilarli zarar.
- `P1 HIGH`: asosiy flow jiddiy qiyin, o'qilmaslik, asosiy CTA yopilgan, muhim a11y to'siq.
- `P2 MEDIUM`: iyerarxiya, consistency, state va yaqin-ikkinchi oqim xatosi.
- `P3 LOW`: polish, mayda notekislik, jiddiy bo'lmagan detal.

A11y yetishmovchiligi impactiga qarab P0/P1 bo'lishi mumkin; har bir WCAG xatosi avtomatik P0 emas.

## 7. Score & issue triage

Yetti kriteriyga `0..5` ball, dalil ID va reasoning bering; `evaluations/scorecard.schema.json`ga mos yozing. Dalil yo'q mezonni null qoldiring, total null; ma'lumot yo'qni 0 deb hisoblamang. Barcha mezonlar dalilli bo'lsa 100 ball hisoblanadi; score kutilgan yo'nalish va blockers'dan alohida tekshiriladi.

## 8. Board review

ChatGPT rollari navbat bilan avval mustaqil fikr, keyin e'tiroz, oxirida rezolyutsiya beradi. Har bir fikr `FACT/HYPOTHESIS/JUDGMENT` deb belgilanadi; bu *simulyatsiya*. Qaror uchun `templates/decision-record.md`dan foydalaning.

## 9. Comparison protocol

Oldingi va yangi versiyani bir xil: user task, content dataset, platform/device, viewport, reviewer rubrikasi, test script va acceptance criteria bilan taqqoslang. Oldindan ma'lum natija bo'lishini xohlagan holda score bermang. O'zgarishlar: before/after IDs, score delta, blocker counts, UX outcome.

## 10. Output pack

- `templates/audit-report.md` to'ldirilgan nusxasi
- issues + screenshots/repro + severity
- weighted scorecard (yoki `UNSCORED`)
- top 3 fix recommendation: expected effect, effort, risk, owner, validation
- Board decision + Owner sign-off yoki `PENDING`

## Hujjatdagi manbalar

`/sources/references.md` — NN/g heuristic evaluation, W3C WCAG 2.2.
