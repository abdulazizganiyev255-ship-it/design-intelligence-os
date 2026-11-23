# Hisobchi AI — S03 Low-Fidelity Wireframe Pack v0.1

**Stage:** S03 IN_PROGRESS, design **not yet approved**.  
**Source:** S02 passed (spec-only) in \`S02-final-gate.md\`.  
**Mode:** Monochrome, semantic hierarchy / layout proof. **NO approved color, typography, icon set, radius, brand illustration or animation.**  
**First MVP job:** Add an expense → save → verify it appears in History and Analytics.  
**Viewports:** 390×844 normal mobile and 320×640 compact mobile; these are **design target sizes**, not screenshots of an executed UI.  
**Evidence basis:** source-backed seeded session numbers, not actual bank data.

## Hierarchy rules

1. Primary action is identifiable before charts, demo fixed balance or decorative material.
2. Each major financial number has a truthful source: **DEMO · sessiya yozuvlari**; *net is not balance*.
3. Home's first viewport prioritizes \`Xarajat qo‘shish\` and the most useful follow-up view.
4. The editor has a clear field order: expense type → amount → category → date → optional note → save.
5. History prioritizes **records** over a wall of filters; show accessible progressive filters, visible total scope and an easy reset.
6. Analytics answers “this period: income, expense, net” then optionally charts *actual recorded* dates. No fake trends or AI.
7. Keep proper cancel, back, edit, delete, calendar and empty/error states. No text-only sketch proves actual interactions.
8. On 320px small phone, preserve a single column and text wrapping; no horizontally overflowing set of large cards.

## W-01 — HOME · 390×844 target structure

\`\`\`text
┌──────────────────────────────────┐
│ Hisobchi                  DEMO   │  1. App identity + truthful mode
│                                  │
│ Xarajatlaringizni kuzating       │  2. Job-oriented, not a fake forecast
│                                  │
│ ┌──────────────────────────────┐ │
│ │ +  Xarajat qo‘shish          │ │  3. PRIMARY ACTION
│ └──────────────────────────────┘ │
│                                  │
│ SESSIYA YAKUNI                   │
│ Sof farq        2 741 000 so‘m   │  4. Not bank balance
│ Kirim   3 000 000 so‘m           │
│ Chiqim    259 000 so‘m           │
│ [ Ushbu sessiya yozuvlaridan ]   │
│                                  │
│ So‘nggi operatsiyalar    Barchasi│  5. Supporting evidence, not KPI grid
│ -------------------------------- │
│ Oziq-ovqat      −85 000 so‘m      │
│ Transport       −12 000 so‘m      │
│ Kafe            −42 000 so‘m      │
│                                  │
│           scroll ↓               │
├──────────────────────────────────┤
│  Bosh   Tarix   Tahlil   Profil  │  6. Contextual bottom tabs
└──────────────────────────────────┘
\`\`\`

**Source note:** \`2,741,000\` is \`income - expense\` from 5 demo session records. It is not an authenticated account balance or “spendable today”. Do not display fixed \`145,000\` allowance as calculated money.

**Tab actions:** Bosh (current), Tarix (transaction list), Tahlil (period summary), Profil (demo help); use the source's existing functional tabs, not a new navigation library requirement.

**One proposed primary CTA:** \`Xarajat qo‘shish\`, consistent with Owner-selected first task. A secondary income action can be discoverable through the editor type switch or history, without a second competing primary button.

## W-02 — NEW EXPENSE · 390×844 (scroll-aware)

\`\`\`text
┌──────────────────────────────────┐
│ ‹ Orqaga       Yangi operatsiya  │  source-aware back label
│                                  │
│ [ Xarajat ● ] [ Daromad ○ ]      │  preserve source type semantics
│                                  │
│ SUMMA                            │
│ ┌──────────────────────────────┐ │
│ │  100 000              so‘m   │ │  current draft, not yet saved
│ └──────────────────────────────┘ │
│                                  │
│ Kategoriya                       │
│ [Oziq-ovqat] [Transport]         │
│ [Kafe]        [Salomatlik]       │
│ [Boshqa xarajat]                 │  wrap, no clipped labels
│                                  │
│ Sana                             │
│ [ 23.11.2026     ▾ ] [Bugun]     │  date modal, nonfuture only
│                                  │
│ Izoh (ixtiyoriy)                 │
│ [ Xarid haqida qisqa izoh ]      │
│                                  │
│ ┌──────────────────────────────┐ │
│ │ Operatsiyani qo‘shish        │ │  save when valid; scroll if needed
│ └──────────────────────────────┘ │
│ Demo · faqat ushbu sessiya       │
└──────────────────────────────────┘
\`\`\`

**Error variant:** invalid amount → clear inline help just below amount and **no mutation**; future date → field error + date picker recovery; missing/invalid category → field error. With keyboard visible, user must still reach the Save action without losing entered state. This is a **future native test**, not an implemented/verified behavior.

**Cancel:** if launched from Home, Back returns Home; if launched from History, Back returns History. The current source has an inaccurate fixed accessibility name for Back; S09 implementation must make that name source-aware.

**Edit variant:** same content hierarchy but clear \`O‘zgarishlarni saqlash\` and separate \`Operatsiyani o‘chirish\` with cancellation/confirmation; never delete on first tap.

## W-03 — HISTORY · 390×844

\`\`\`text
┌──────────────────────────────────┐
│ Operatsiyalar            DEMO    │
│ Faqat ushbu sessiya              │
│                                  │
│ [ + Xarajat qo‘shish ]           │  one direct action
│                                  │
│ [ Qidirish...     ] [ Muddat ▾ ] │
│ [Barchasi ●] [Xarajat] [Daromad] │
│                                  │
│ 5 ta yozuv              Tozalash │  Tozalash shown only with filters
│ -------------------------------- │
│ 23-noyabr                       │
│ Oziq-ovqat        −85 000 so‘m   │
│ Transport         −12 000 so‘m   │
│ -------------------------------- │
│ 22-noyabr                       │
│ Kafe              −42 000 so‘m   │
│ Salomatlik       −120 000 so‘m   │
│                                  │
│ [ Ko‘rinayotgan yozuvlar jami ]  │
│ Kirim 3 000 000 | Chiqim 259 000│  filtered-scope label required
│                                  │
├──────────────────────────────────┤
│  Bosh   Tarix   Tahlil   Profil  │
└──────────────────────────────────┘
\`\`\`

**Dates above are schematic labels, not verified seed chronology.** In the actual render, group dates must come from \`occurredOn\`; never copy these illustrative day labels into source test fixture. True totals must sum the **visible filtered rows**. A filtered result must not display all-record totals with the wrong scope label.

**Empty states:** \`Mos operatsiya topilmadi\` after a filter vs \`Operatsiyalar hali yo‘q\` when session empty; first offers clear/reset; second offers add operation.

## W-04 — ANALYTICS · 390×844

\`\`\`text
┌──────────────────────────────────┐
│ Tahlil                    DEMO   │
│ [ Davr: Barchasi ▾ ]            │
│                                  │
│ SESSIYA HISOBOTI                 │
│ Chiqim          259 000 so‘m     │  first question: what spent?
│ Kirim         3 000 000 so‘m     │
│ -------------------------------- │
│ Sof farq      2 741 000 so‘m     │  not balance
│ [Joriy sessiya yozuvlaridan]     │
│                                  │
│ Sana bo‘yicha yozuvlar           │
│ ┌──────────────────────────────┐ │
│ │ Actual data-only chart here │ │  no prediction, real coverage
│ │ or truthful no-data state   │ │
│ └──────────────────────────────┘ │
│                                  │
│ [ Operatsiyalarni ko‘rish ]      │
│                                  │
│     scroll for categories ↓      │
├──────────────────────────────────┤
│  Bosh   Tarix   Tahlil   Profil  │
└──────────────────────────────────┘
\`\`\`

**Chart source contract:** if a last-7-recorded-days chart is shown, its coverage label must be distinct from selected period KPI totals. If \`period=month\`, totals must follow actual selected month, not all-time seed fixture.

## Compact 320×640 reflow rules — W-05

\`\`\`text
HOME:                           EDITOR:
┌────────────────────────┐      ┌────────────────────────┐
│ Hisobchi         DEMO  │      │ ‹  Yangi operatsiya    │
│                        │      │ Xarajat ●  Daromad ○   │
│ [ + Xarajat qo‘shish ] │      │                        │
│                        │      │ Summa                  │
│ Sof farq (sessiya)     │      │ [ 100 000 so‘m       ] │
│ 2 741 000 so‘m         │      │ Kategoriya             │
│ Kirim / Chiqim         │      │ [Oziq-ovqat]           │
│                        │      │ [Transport] [Kafe]     │
│ So‘nggi yozuvlar       │      │ Sana [23.11.2026]      │
│ Oziq-ovqat  −85 000    │      │   scroll to note/save ↓│
├────────────────────────┤      └────────────────────────┘
│Bosh Tarix Tahlil Profil│
└────────────────────────┘
\`\`\`

**Compact rules:**
- Typography *roles* defined, but **no final typeface/scale** chosen before S05.
- Amounts wrap or reflow; avoid cutoff of \`2 741 000 so‘m\` and long Uzbek labels.
- Four bottom tabs remain distinguishable; do not squeeze labels to unusable microtype.
- Editor is scrollable; keyboard/safe-area behavior must later be tested on actual device.
- Charts and transaction details can be below fold. Do not force fixed-height giant content.
- Suggested reading order matches logical accessibility order and action intent.

## Explicit unresolved decisions (S03 gate)

- At 320px, is the user better served by the one-line CTA or icon+copy? Test monochrome variants, do **not** assume.
- After Save, is History enough to confirm action, or does an explicit ephemeral success status improve comprehension? Prototype at S08; no fake cloud sync.
- Is the default period \`Barchasi\` or \`Oy\`? Source initial state uses \`all\`; keep it until evidence justifies a change.
- Avoid assuming users recognize \`Sof farq\` as the same as balance; test source-label comprehension.
- Real seed dates must be loaded before an actual rendered final history wireframe; the example grouping above is illustrative only.

## Stage acceptance — NOT YET PASSED

S03 must demonstrate real content hierarchy in grayscale at 320 and 390 widths, expected error/empty states, no false financial promise, main task identifiable without palette, and explicit Board critique. These text sketches are **not** runnable native screens, user studies or polished visuals.
