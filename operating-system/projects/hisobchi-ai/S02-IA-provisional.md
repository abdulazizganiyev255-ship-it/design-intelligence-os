# Hisobchi AI — S02 Information Architecture (HYPOTHESIS ONLY)

**Status:** HISTORICAL PROVISIONAL DRAFT (superseded for active work by `S02-screen-map.md` and `S02-navigation.json`). S02 is now `IN_PROGRESS`, not PASSED.  
**Dependency update:** scoped S00 and S01 have passed after explicit Owner authorization; active S02 specification is in the files above. This older A/B comparison remains a research sketch, not a completed or approved design.  
**Source:** `S01-source-truth-contract.md`; actual navigation at [App.tsx](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/App.tsx).  
**Mode:** Planning by one ChatGPT, not independent designer agents.

## Principle: content and task hierarchy before design tokens

**Hypothesis:** a truthful finance UI should make action → confirmation → observable change more prominent than an unverified allowance. The two alternatives below differ by the starting mental model, not just color/icon shape. The recommended path **depends on Owner's S01 decision**.

## IA A — Action-first Ledger

```text
APP
├── Bosh
│   ├── Sessiya holati (sourced net and note; NO bank claim)
│   ├── [Xarajat qo‘shish] → Editor
│   ├── [Kirim qo‘shish] → Editor (income)
│   └── Oxirgi yozuvlar → Tarix
├── Tarix
│   ├── Operatsiyalar (visible session rows)
│   ├── Qidiruv / tur / davr / maxsus sana
│   └── Yozuvni ochish → Editor edit/delete
├── Tahlil
│   ├── Davr tanlash
│   ├── Sessiya kirim, chiqim, sof farq
│   └── Kategoriya/kunlik harakatlar (source-labelled)
└── Profil
    ├── Demo va maxfiylik ma’lumotlari
    ├── Demo reset confirmation
    └── Qo‘llanma / onboarding (optional)
```

**Primary job:** fast, correct expense entry and verification. **Benefit hypothesis:** fewer decisions before first meaningful action. **Risk:** a ledger overview may remain generic if visual language does not reflect product meaning.

## IA B — Recorded-activity Timeline

```text
APP
├── Bosh
│   ├── Bugungi qaydlar (source: recorded session)
│   ├── Vaqt o‘qi: mavjud operatsiyalar, not fabricated futures
│   ├── [+ Xarajat] → Editor
│   └── Sessiya sof farqi (secondary)
├── Tarix
│   ├── Butun davrlar / qidiruv / turlar
│   └── Sana bo‘yicha batafsil yozuvlar
├── Tahlil
│   ├── Davr metrikalari
│   └── Guruhlangan xarajatlar / izohlash
└── Profil
    ├── Demo mode
    └── Settings and help
```

**Primary job:** reconstruct what happened over time. **Benefit hypothesis:** recognizable temporal navigation and clearer event history. **Risk:** may add time-axis navigation work to a simple record task. Future planned commitments **not available** in current source; cannot draw them.

## Core state machine shared by both options

```text
HOME [DEMO/Sessiya]
   │ Add expense
   ▼
EDITOR.NEW ──invalid amount/date/category──▶ EDITOR.ERROR
   │ cancel                            │ edit value
   └────▶ HOME (unchanged) ◀────────────┘
   │ save(valid amount, category, nonfuture date)
   ▼
SESSION.TRANSACTIONS_CHANGED
   ▼
HISTORY (new row visible)
   │ select row
   ▼
EDITOR.EDIT ──cancel──▶ HISTORY (unchanged)
   │ save(updated) or confirm delete
   ▼
HISTORY (updated/removed)
   │ Tahlil
   ▼
ANALYTICS (recomputed from same session)
```

These transitions come from current source logic but **must be reverified** when a new UI is implemented. `Sof farq` is not a bank balance; demo sample balance and daily allowance remain fixed.

## Required screen and state matrix (provisional)

| Screen | Primary purpose | Minimum states | Error recovery / truth |
|---|---|---|---|
| Bosh | orient and act | demo, empty, update, hidden money | source tags; do not show live Safe-to-Spend |
| Editor | save expense/income | new, filled, invalid, cancel, save, edit, delete-confirm | field errors; keyboard/save behavior tested later |
| Tarix | locate and modify | list, search, no match, filter, period/calendar, edited, deleted | clear filters, preserve correct totals |
| Tahlil | explain actual transactions | populated, zero income, negative net, custom range, no data | chart coverage and period truth |
| Profil | settings and demo control | normal, confirmation, demo reset, help | explicit warning reset affects local session |
| Global navigation | move without losing context | selected, focus, back, modal open | Android Back and iOS gestures require native QA |

## Measurable acceptance scenarios (planning; NOT TESTED in this redesign)

- `UX-01`: from Home, locate `Xarajat qo‘shish`, enter 100,000 UZS with valid category/date and save; new row appears in History.
- `FIN-01`: session expenses 259,000 → 359,000; net 2,741,000 → 2,641,000; income remains 3,000,000; no fixed demo sample changes.
- `UX-02`: cancel new entry does not mutate records; edit changes the correct row; destructive delete requires confirmation.
- `UX-03`: invalid zero/negative text, unknown category and future date produce correct error states.
- `UX-04`: custom period keeps inclusive day boundaries; filters preserve clear/reset controls.
- `A11Y-01`: button names, focus order, modal Back/Close, 320px reflow, 200% text as relevant to device — **NOT YET VERIFIED**.
- `TRUST-01`: independent person can distinguish session net vs fixed sample account balance vs uncomputed real allowance — needs actual task-based comprehension study.

## Board concerns to resolve when S02 officially opens

- UX: which first action is most important to actual users and Owner?
- Creative: how to express a unique visual identity while preserving hierarchy, rather than default cards?
- Architect: can each screen use the exact current domain data without changing semantics?
- Reviewer: which assumptions can be tested on real device and where could the UI mislead?

**Gate update:** S02 is `IN_PROGRESS`, not PASSED. No component palette, screenshot, code merge or "passed QA" follows from this historical sketch.
