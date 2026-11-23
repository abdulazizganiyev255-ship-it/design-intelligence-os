# Design Board Charter v0.1

## Vakolat va vazifa

Board'ning vazifasi: loyiha brief'i, dalil, UX, vizual ifoda, dizayn tizimi va sifat bo'yicha **asoslangan** qaror chiqarish. Board yaratgan narsasini avtomatik ma'qullaydigan marketing mexanizmi emas.

## Ijro rejimi

**MVP-01:** bitta ChatGPT modelida rollarni navbatma-navbat ovozlantirish — faqat *strukturaviy simulyatsiya*. Har bir rolning alohida xotirasi, API seansi yoki haqiqiy mustaqilligi yo'q. `SIMULATED_BOARD_REVIEW` muhri bo'lishi shart.

**Kelajak:** real alohida agent sessiyalari va audit izi bo'lgandagina `MULTI_AGENT_REVIEW` deyish mumkin.

## Board tarkibi (5 pozitsiya)

| Pozitsiya | Mandat | Saylov / rol | Veto chegarasi |
|---|---|---|---|
| Owner/Chair (inson) | Maqsad, scope, budget, release | Real inson | Yakuniy approval; xavfsizlik/huquqiy talablarni bekor qilmaydi |
| Creative Director | Art direction, originality, brand expression | Creative rol | Konsept qayta ishlanishini so'raydi |
| UX Research Lead | User task, evidence, flow, comprehension | UX rol | Foydalanuvchi vazifasi isbotsiz o'zgarsa block tavsiya qiladi |
| Design Systems / Engineering Lead | Tokenlar, component contract, feasibility | Architect rol | Texnik amalga oshmaslik va regressiya haqida veto tavsiya qiladi |
| Quality Chair | Audit integrity, accessibility, evidence | Reviewer rol | P0/P1 borida release'ni bloklaydi |

**Haqiqiy blocking gate:** P0/P1 ochiq bo'lsa Board yoki Owner istagi bilan `APPROVED`ga o'tish mumkin emas. Istisnolarni kamaytirilgan scope, test va yangi qayta ko'rib chiqish bilan yozma o'zgartirish kerak.

## Mustaqil ish va qaramlikni kamaytirish

- Har bir rol *birinchi round*da boshqa rol javobini takrorlamasdan taklif beradi; boshqa ekspert fikrlari keyingi roundda ochiladi.
- Ikkinchi roundda kritik e'tiroz va muqobil yo'l ko'rsatiladi.
- Uchinchi roundda qaror: accept/revise/reject/defer.
- Tanqid qilish *majburiy*, lekin sun'iy konflikt yasash taqiqlanadi.
- Reviewer yaratgan agentning yakuniy score'ini dalilsiz qabul qilmaydi.
- Bir xil modelning turli rollari mustaqil inson expert review o'rnini bosa olmaydi.

## Board yuritish qoidalari

- Quorum (MVP simulyatsiya): 4 rol fikri va Owner uchun yozilgan taklif. Bu haqiqiy 4 shaxs bor degani emas.
- Ikkita mazmunan farqli konsept kamida qisqa taqqoslanishi shart.
- Decision log: D-ID, alternatives, evidence IDs, dissent, costs, risks, validation, status.
- Dalil yo'q joyda qaror `HYPOTHESIS`, ko'pincha `DEFER` bo'ladi.
- Dizayn freeze nuqtasidan keyin kutilmagan katta yo'nalish o'zgarishi alohida decision talab qiladi.

## Eskalatsiya

1. P0/P1: avtomatik hold; Owner xabardor, repro majburiy.
2. Design/UX ziddiyati: foydalanuvchi vazifasi va dalilga ustuvorlik.
3. Vaqt/harajat ziddiyati: scope qisqartirish, blocker yashirmaslik.
4. Estetik muammo: ko'pi bilan 2 strukturali review round, keyin aniq reference yoki Owner yo'nalishi olinadi.

## Qabul mezonlari

- Muhokama kamida bitta real qarorni o'zgartirgan yoki nega saqlanganini yozgan.
- Har muhim qarorda alternativ, trade-off, dalil ID yoki `UNVERIFIED` bor.
- Reviewer baho/QA ni 'o'tdi' deb uydirmagan.
- Human approval alohida belgilangan.
