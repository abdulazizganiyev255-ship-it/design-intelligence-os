# Design Quality Rubric v0.1 — 100 ball

## Metod

Har kriteriy `rating: 0..5` oladi. Kriteriy bo'yicha ball = `weight * rating / 5`. Yakuniy ball = barcha 7 kriteriy yig'indisi, maksimum 100. `null` (dalil yetishmaydi) 0 emas; bitta mezon `null` bo'lsa **total_score = null, status = UNSCORED**.

Ball ekspert judgmentidir, o'lchov vositasi yoki universal sertifikat emas. Har rating uchun `evidence_ids`, reason va tekshirilgan scope talab etiladi.

## 7 kriteriy

| ID | Kriteriy | Weight | Nima kuzatiladi |
|---|---|---:|---|
| V | Visual originality & art direction | 25 | O'ziga xos vizual til; mahsulotga xoslik, vizual nishon, va asossiz effektlardan voz kechish |
| U | UX clarity & usability | 20 | Top task, mental model, action feedback, recovery, user control |
| T | Composition & typography | 20 | Hierarchy, grid, whitespace rhythm, readable type and data |
| D | Design system consistency | 10 | Semantic tokens, component rules, same behavior across states |
| A | Accessibility | 10 | WCAG 2.2 AA tekshiruvlari; keyboard/focus/contrast/reflow |
| I | Responsive & interactions | 10 | Small device, desktop, states, input modality, animation purpose |
| F | Technical feasibility | 5 | Implementation risk, platform constraints, performance/data truth |
|  | **Total** | **100** | |

## Global 0–5 anchors

- **0 — Major failure (dalil mavjud):** asosiy kutilgan vazifa keskin buzilgan. 0 = no evidence emas.
- **1 — Weak:** sezilarli muammolar, ayrim qismlar ishlaydi.
- **2 — Below bar:** asosiy strukturasi bor, muammolar ko'p.
- **3 — Adequate:** ishlatishga yaroqli, lekin o'ziga xoslik/craft yoki qulaylik chegaralangan.
- **4 — Strong:** ko'p jihatdan yetuk, kam sonli aniq nuqsonlar.
- **5 — Excellent:** dalillar bilan puxta, izchil va kamchiliksizga yaqin (hamon test scope bilan cheklangan).

## Kriteriy bo'yicha qo'shimcha anchorlar

### V — originality (25)
0: generic copied layout yoki mahsulotni noto'g'ri ifoda etadi; 3: aniq, lekin farqlanmaydi; 5: maqsadga xizmat qiladigan o'ziga xos composition/brand language, kerakli joyda kreativlik.

### U — UX (20)
0: core task bajarilmaydi; 3: task ishlaydi, ayrim yo'llar noaniq; 5: top task tez tushuniladi, feedback/recovery ravshan; foydalanuvchi dalillari mavjud bo'lsa yanada ishonchli.

### T — composition (20)
0: o'qib bo'lmaydigan iyerarxiya; 3: standart grid bilan muvozanat; 5: izchil tipografik ritm, density, data priority va viewport moslashuvi.

### D — design system (10)
0: semantik token va komponent holatlari buzilgan; 3: asosiy tokenlar izchil; 5: barcha ko'rilgan states/variants uchun contract, aloqador xatolar yo'q.

### A — accessibility (10)
0: core use uchun jiddiy to'siq; 3: bazaviy keyboard/contrast ishlaydi, ayrim xatolar; 5: ko'rilgan scope'da WCAG 2.2 AA texnik audit va manual check o'tgan. Yuqori ball universal compliance yoki user testing emas.

### I — responsive (10)
0: asosiy qurilmada broken; 3: default responsive holatlar ishlaydi; 5: asosiy breakpoints + keyboard/touch + edge states ko'rilgan va dalilli.

### F — feasibility (5)
0: ko'zlangan platformada amalda mumkin emas; 3: texnik yo'l va cheklovlar aniq; 5: amalda prototip ishlagan, performance/data/complexity tradeoffs tekshirilgan.

## Evidence coverage

`scorecard.criteria.*.evidence_ids` to'ldiriladi. `Screenshot` faqat ko'rinishni isbotlaydi; keyboard, screen reader, functional truth uchun real sinov kerak. Assumption yoki fikr screenshot kabi evidence emas.

## S+ eligibility (ichki)

1. Barcha 7 mezon rated, 7 tasi uchun evidence ID mavjud.
2. `total_score >= 85`.
3. `open_P0 == 0 && open_P1 == 0`.
4. Top task uchun documented acceptance run = PASS, accessibility kritik checklar PASS; qolgan holatlar izohlangan.
5. `owner_approval == true`.
6. Yakuniy S+ uchun haqiqiy mustaqil inson reviewi (`EXTERNAL_HUMAN_REVIEW`) qayd etilgan bo'lishi kerak. Bitta ChatGPT modelidagi Board simulyatsiyasi faqat `S+ CANDIDATE` ishlab chiqarishi mumkin.

Ushbu shartlardan biri bajarilmasa S+ berilmaydi, lekin ichki ball qayd etilishi mumkin.

## Severity

P0 blocker; P1 high; P2 medium; P3 low. Severity mas'uliyatli impact va reproducibility asosida. "Yomon ko'rindi" avtomatik P1 emas, "asosiy CTA bosilmaydi" P1 yoki P0 bo'lishi mumkin.

## Comparison

`delta = new_total - baseline_total` faqat ikkala total valid va bir xil task/device/scoring scope bo'lsa. Aks holda `not_comparable`.
