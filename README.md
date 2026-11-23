# Design Intelligence OS — Foundation v0.1

**Holat:** MVP-01 dokumentatsiya va tekshirish poydevori. Bu repository hozircha avtonom AI jamoa, RAG xizmati yoki dizayn generatsiya serveri **emas**.

## Missiya

Real foydalanuvchi vazifalariga mos, estetik jihatdan o'ziga xos, foydalanish uchun aniq, texnik jihatdan bajariladigan interfeyslarni **dalil → qaror → konsept → tekshiruv → o'rganish** sikli orqali yaratish. "S+" — tashqi sertifikat emas, ichki sifat darajasi.

## Boshqaruv modeli

- **Owner (inson):** loyiha maqsadi, cheklovlar, estetik yo'nalish va yakuniy release qarori.
- **Board (5 qarash):** Owner/Chair; Creative; UX; Systems/Engineering; Quality. Boshlang'ich rejimda ular bitta ChatGPT suhbatida alohida ekspert perspektivalari sifatida *simulyatsiya* qilinadi.
- **4 rol kontrakti:** Creative Director, UX Researcher, Design Architect, Critical Reviewer. Rollarni mustaqil avtonom agentlar deb atamang.
- **4 skill:** design-brief, reference-teardown, art-direction, ux-critique; har biri `SKILL.md` formatida.
- **Evidence:** real screenshot, Figma frame, prototip URL, ekran yozuvi, kod va test natijasi. Kuzatilmagan narsaga ball qo'yilmaydi.

## Foydalanish tartibi (ChatGPT + GitHub, Hermes ishlatilmaydi)

1. GitHub'da `design-intelligence-os` nomli **private** repository yarating. Ushbu fayllarni to'liq yuklang (yashirin `.github/` papkasi ham).
2. ChatGPT Project yarating. `AGENTS.md`, `governance/board-charter.md`, `governance/quality-rubric.md` va zarur agent/skill fayllarini loyiha kontekstiga kiriting. ChatGPT Project GitHub'dagi barcha o'zgarishlarni avtomatik sinxronlaydi deb hisoblamang.
3. `baseline/00-purpose-scope.md` va `baseline/audit-protocol.md` bo'yicha dizayn dalillarini to'plang. `baseline/evidence-manifest.csv`ga manbalarini yozing.
4. `templates/design-brief.md` yordamida brief tayyorlang; bilim yetishmasa fakt va taxminni ajrating.
5. `governance/workflow.md` bo'yicha rol almashish, Board debate va qaror yozuvini yuring. Yakuniy S+ uchun mustaqil inson auditi alohida talab qilinadi. Qarorlar uchun `templates/decision-record.md`dan foydalaning.
6. `templates/audit-report.md` va `evaluations/scorecard.schema.json`ga mos baholang. To'liq dalil bo'lmasa `UNSCORED` qoldiring.
7. Tasdiqlangan learning yozuvlarini keyingi vazifalarda qayta ishlating. Hozircha avtomatik RAG yo'q.

## Bepul ishlash tamoyili

MVP-01 Markdown/JSON/CSV/Python standart kutubxonasi bilan ishlaydi. Pullik AI API, GitHub Copilot yoki host talab qilinmaydi. GitHub Actions workflow faqat **qo'lda** (`workflow_dispatch`) ishga tushadi; private repository'dagi Actions ishlatilishi tarif/kvota bilan bog'liq bo'lishi mumkin. Lokal tekshirish tavsiya qilinadi:

```bash
python tools/validate_foundation.py
```

Windows PowerShell:

```powershell
py -3 tools/validate_foundation.py
```

## Repository xaritasi

```text
design-intelligence-os/
├── AGENTS.md
├── README.md
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/validate.yml
├── baseline/
│   ├── 00-purpose-scope.md
│   ├── audit-protocol.md
│   ├── evidence-manifest.csv
│   └── baseline-register.csv
├── governance/
│   ├── board-charter.md
│   ├── decision-policy.md
│   ├── workflow.md
│   └── quality-rubric.md
├── agents/
│   ├── creative-director.md
│   ├── ux-researcher.md
│   ├── design-architect.md
│   └── critical-reviewer.md
├── skills/
│   ├── design-brief/SKILL.md
│   ├── reference-teardown/SKILL.md
│   ├── art-direction/SKILL.md
│   └── ux-critique/SKILL.md
├── templates/
│   ├── design-brief.md
│   ├── reference-card.md
│   ├── audit-report.md
│   ├── decision-record.md
│   └── board-session.md
├── evaluations/
│   ├── scorecard.schema.json
│   ├── example-unscored.json
│   └── benchmark-plan.md
├── projects/pilot-01/
│   ├── brief.md
│   └── board-simulation.md
├── sources/
│   ├── references.md
│   └── open-source-catalog.md
├── knowledge/README.md
└── tools/validate_foundation.py
```

## MVP-01 Definition of Done

- [x] Baseline maqsadi, chegarasi, dalil standarti va test protokoli yozilgan.
- [x] Board charter, veto va qaror yozuvi qoidalari yozilgan.
- [x] To'rt agent role contract va to'rt SKILL.md yozilgan.
- [x] Brief, reference card, audit, decision shablonlari va pilot brief yozilgan.
- [x] 100 ballik auditi va bloklovchi gate ta'riflangan.
- [x] Board debatining **simulyatsiyasi** hujjatlashtirilgan.
- [ ] Haqiqiy oldingi ekranlar dalili kiritilgan, baseline ball o'lchangan.
- [ ] Mustaqil inson ko'rigi yoki real foydalanuvchi testi o'tkazilgan.
- [ ] Haqiqiy parallel agentlar, orkestrator, RAG va produktiv CI/CD ishga tushgan.

## Ko'p takrorlanadigan xatolardan himoya

- Chiroyli maketni ishlab turgan mahsulot deb ko'rsatmang.
- Bir xil modelning turli rollarda gapirishi haqiqiy mustaqil ekspertlar degani emas.
- Eski ekranni ko'rmasdan uning vizual xatolarini fakt deb yozmang.
- Real referensdan foydalanilsa manba, sana, foydalanish huquqi va aynan qaysi prinsip olinganini yozing.
- Avvalgi yaxshi ishlagan qismlar faqat yaxshilash maqsadida, dalilsiz qayta buzilmasin.

## Manbalar

`/sources/references.md`ga qarang: W3C WCAG 2.2, Nielsen Norman Group, Agent Skills specification, GitHub documentation.
