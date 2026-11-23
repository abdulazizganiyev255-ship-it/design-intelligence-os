# BASELINE-001 — Hisobchi AI: previous visual directions rejected

**Date:** 2026-11-23
**Product:** Hisobchi AI / mobile finance UI
**Source repository:** https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile
**Owner verdict:** All prior Hisobchi AI designs are rejected as visual directions.
**Outcome:** VISUAL_DIRECTION_REJECTED; baseline numerical score = **UNSCORED**; product logic is **NOT** automatically rejected.
**Review mode:** SOURCE_AND_SCREENSHOT_ASSISTED + SIMULATED_BOARD_REVIEW (one ChatGPT, not autonomous agents)
**Scope:** visual information hierarchy and composition of real **Expo Web/Chromium** screenshots, plus source/docs. No native device usability test or final iOS/Android audit took place here.

## 1. Source and evidence inventory

| Evidence ID | Type | Precise source | What it supports | Limit |
|---|---|---|---|---|
| E-OWNER-001 | Owner statement | Conversation, 2026-11-23: all previous Hisobchi AI designs rejected | Visual direction lacks owner acceptance | Does not prove all engineering/UX behavior fails |
| E-SHOT-001 | Actual render | GitHub Actions run https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/actions/runs/45051373294 ; artifact \`living-ledger-responsive-screens\`, ID \`14766165755\`, \`393x852-home.png\` | Home hierarchy, visible copy, CTAs, spacing, colors | Web screenshot only; no navigation test performed by this reviewer |
| E-SHOT-002 | Actual render | Same artifact, \`393x852-ledger-transactions.png\`, \`320x640-ledger-transactions.png\` | Transaction list/filter/control layout | Actual touch & screen-reader behavior untested in this audit |
| E-SHOT-003 | Actual render | Same artifact, \`393x852-ledger-editor.png\`, \`320x640-ledger-editor.png\` | Amount, categories, date and editor hierarchy | Below-fold content and native keyboard untested |
| E-SHOT-004 | Actual render | Same artifact, \`393x852-analytics-initial.png\`, \`320x640-analytics-initial.png\`, \`393x852-analytics-chart.png\` | Analytics KPIs, metric controls and chart presentation | Real comprehension, chart readability for users and screen-reader behavior untested |
| E-SHOT-005 | Actual render | Same artifact, \`393x852-ledger-calendar.png\`, \`393x852-analytics-calendar.png\`, \`393x852-explanation.png\` | Overlay and calendar visual states | Only captured frames |
| E-CODE-001 | Source | https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/src/theme/livingLedger.ts | Current Living Ledger palette/token structure | Code does not prove user aesthetic preference |
| E-DOC-001 | Repo PR & QA | https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/pull/29 and /pull/30 and /pull/31 | Home, ledger and analytics feature/test descriptions, known demo-state limitations | Historical CI reports, not independent present native audit |
| E-DOC-002 | Draft native PR | https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/pull/32 | Porcelain × Cobalt is a **draft native preview**, not main production | Native render not inspected in this baseline |
| E-DOC-003 | Analytics QA report | https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile/blob/design/splus-living-ledger-analytics-v03/docs/design-os-splus/09_ANALYTICS_VISUAL_GATE.md | Reported test scope/data provenance | Claims by prior PR; do not convert to new usability scores |

**Screenshot availability:** reviewed six representative screens at 393×852 and 320×640 plus contact sheet of 12 views from the 42 captured browser PNGs. Not all 42 inspected at full resolution; no native screenshot is included in this report.

## 2. What actually appears in the web captures (FACT)

1. Home: a green-highlighted DEMO notice above a large \`145 000 so‘m\` headline; a separate \`12 850 000 so‘m\` sample balance; orange \`Xarajat qo‘shish\` action; and a green monthly expenses sample chart. Multiple small explanatory and provenance labels compete with financial figures. (E-SHOT-001)
2. Transactions: an orange \`Yangi operatsiya\` action, search + date controls, three-way segmented type filter, income/expense summary, and transaction feed. At 320px the first screen prioritizes filters and summary over scrolling through entries. (E-SHOT-002)
3. Editor: large number entry box, segmented expense/income, multiple category pills, date selection and an additional note below the visible first fold. (E-SHOT-003)
4. Analytics: top net/total amounts, period selector, daily chart controls, chart and category summary (below fold). Several labels use small overlines and repeated section dividers. (E-SHOT-004)
5. Existing code uses ivory/forest/sage/coral role colors, and previous iterations have also explored blue/native styling. (E-CODE-001, E-DOC-002)
6. Product is demonstrative: existing documents explicitly state no authenticated live account or verified Safe-to-Spend engine. Dashboard's sample data and session-derived analytics have different provenance. (E-DOC-001, E-DOC-003)

## 3. Initial visual diagnosis (DESIGN_JUDGMENT, not user-test fact)

| ID | Area | Evidence | Finding / user impact hypothesis | Priority | Direction |
|---|---|---|---|---|---|
| H-01 | Home | E-SHOT-001 | Large daily figure, balance, action and month figure each seek attention. The screen does not present a clearly articulated financial **decision**. Hypothesis: high glance cost. | P2 | Define one primary user job and tier information accordingly |
| H-02 | Home | E-SHOT-001, E-DOC-001 | Honest repeated DEMO explanation occupies prominent visual real estate; trust communication competes with decision support. | P2 | Keep one explicit demo-state treatment + contextual info, never disguise unverified calculations |
| H-03 | Home/Analytics | E-SHOT-001, E-SHOT-004 | The same dense, rule-separated presentation repeats without a distinctive information visualization that would make this *Hisobchi AI*, not a finance template. This is a design judgment corroborated by owner's rejection. | P2 | Build a new composition system tied to financial action, not a palette swap |
| H-04 | Transactions | E-SHOT-002 | The first viewport gives considerable space to filters, header, totals and create control before transaction content. Risk of task delay for frequent history lookup. | P2 | Progressive disclosure/filter density, preserve reliable create/edit/delete flows |
| H-05 | Editor | E-SHOT-003 | Many category chips + prominent amount form can push save/date context down and raise visible density on compact screens. Need actual native keyboard tests before concluding obstruction. | P2 | One clear amount-first flow and contextual category selection; test keyboard/save visibility |
| H-06 | Analytics | E-SHOT-004 | Metric tabs + chart + explanatory microcopy risk overwhelming the core question "what changed and what can I do?" | P2 | Reduce simultaneous choices; add meaning/action without invented forecasts |
| H-07 | Cross-screen | E-DOC-001, E-DOC-002 | Stacked branches use different visual systems. Do not freeze a mixture into the final experience. | P1 if merged together without resolution; currently a **release risk**, not an observed production fault | Freeze a single approved system after a real visual selection |
| H-08 | Financial trust | E-DOC-001, E-DOC-003 | Safe-to-Spend is a fixed demonstration while other numbers derive from session transactions. This is disclosed, but a real finance release must not present it as live truth. | P1 **production gate only**; current screenshot is explicitly marked DEMO | Retain source/provenance contract; implement deterministic finance-engine validation before real claims |

**Severity note:** Aesthetic dislikes are NOT P0/P1 defects by default. H-07/H-08 are conditional production gates; the current draft web captures are not declared broken production apps. User preference is decisive for visual selection even if other QA passes.

## 4. Preserve / remove / reinvent

### Preserve, subject to regression tests
- Validated financial arithmetic, source labels and distinction between demo, session, account balance and true Safe-to-Spend.
- Transaction create, edit, delete confirmations; period filter and date constraints.
- Accessible labels, explicit empty/error state intent and tested responsive behavior.
- Domain concepts, data models, existing app logic and backend security boundaries.

### Reject as visual baseline
- Existing Living Ledger color/composition combination, old blue/glass/card aesthetics, and the Porcelain × Cobalt native preview as a final look.
- Another round of merely resizing cards, swapping accent colors or adding decorative gradients.
- A dashboard that simultaneously screams balance, Safe-to-Spend, monthly graph and unrelated CTAs.

### Reinvent
- Information architecture from the single highest-value financial question and next action.
- Home's signature visual model; content density and navigation/interaction hierarchy.
- Consistent typography and icon language; component states; whitespace/density rhythm.
- AI surfaces only where there is a real, sourced function (not staged recommendations).

## 5. Quality rubric (honest status)

| Criterion | Weight | Current rating |
|---|---:|---|
| V — Originality / art direction | 25 | Not calibrated across all versions; owner rejection recorded |
| U — UX clarity & usability | 20 | Actual user testing NOT PROVIDED |
| T — Composition & typography | 20 | Visual concerns documented, no multi-review calibration |
| D — Design system | 10 | Token source exists; cross-branch integration unresolved |
| A — Accessibility | 10 | Selected contrast reported; native/reader verification absent |
| I — Responsive & interaction | 10 | Browser CI evidence available; native interaction unverified |
| F — Feasibility | 5 | Existing code/prototype evidence, production finance contracts open |

**total_score = null; status = UNSCORED.** Do not report a fabricated 45/100 or "S+" improvement. 100-point rubric applies when full evidence criteria are satisfied.

## 6. Actionable next step

1. Use the Board session in \`mvp-02/sessions/BOARD-HISOBCHI-001.md\` to compare **two distinct structural** alternatives, not a new color swatch.
2. Produce and review full-resolution Home concepts, with actual user content and realistic source truth. Ask Owner to select/modify, and record the rejection reasons.
3. Extend the chosen information hierarchy to Transactions, Editor, Analytics and Profile, checking same content/viewport before/after.
4. Run real visual/device/accessibility QA and collect evidence. No design gets \`APPROVED_BY_OWNER\` automatically.

## 7. Provenance and limitations

Source images are from the user's GitHub Actions artifact. This report reviewed representative real web renders, **not every historic design version or native device**. The owner's rejection of all prior visual directions is recorded as an explicit constraint. Browser test pass does not imply aesthetic acceptance or native release readiness.
