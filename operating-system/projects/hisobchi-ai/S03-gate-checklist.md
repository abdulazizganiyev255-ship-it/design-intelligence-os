# S03 Low-Fidelity Review Checklist

**Scope:** User-approved first MVP A_RECORD_EXPENSE. **Status:** 14 actual Chromium renders produced and layout geometry checked; stage remains IN_PROGRESS for unresolved readability/keyboard/native evidence. See `S03-render-audit.md` and `S03-browser-qa.json`.  
**No selected palette, font, icon brand, motion or React Native implementation in S03.**

## Per-screen acceptance

| Screen | Minimum task hierarchy | Variant to inspect | Evidence state |
|---|---|---|---|
| HOME | `Xarajat qo‘shish` before supporting KPI; source-qualified net | normal 320/390; empty/long money still open | RENDER_CHECKED_PARTIAL |
| EDITOR_NEW | expense context, amount, category, date, note, save, reversible back | normal/invalid amount at 320/390; keyboard other errors open | RENDER_CHECKED_PARTIAL |
| HISTORY | actual records accessible before filter overload; clear search/reset | normal/filtered-empty 320/390; true zero-record state open | RENDER_CHECKED_PARTIAL |
| ANALYTICS | period, expense/income/net and honest coverage; optional actual-data chart | all/empty 320/390; negative net/real chart open | RENDER_CHECKED_PARTIAL |

## Global checks

- [x] Real low-fi grayscale render at 320×640 and 390×844 for all four screens, plus editor error/history-empty/analytics-empty = 14 screenshots
- [x] Home/History primary CTA above bottom tab bar in browser viewports
- [ ] CTA/save control reachable with a **real native keyboard open**
- [ ] Long amount `999 999 999 999 so‘m` and long Uzbek text do not clip
- [ ] No false live balance or Safe-to-Spend computation
- [ ] Screen reader/keyboard reading order spec maps to visual reading order
- [ ] Errors, cancel, back, selected filters, empty states have clear placement
- [x] Source-based dates (22/21/20/19 Nov) and amounts used correctly in rendered demo
- [x] Side-by-side initial Board/visual audit of actual 320 and 390 renders in `S03-render-audit.md`
- [x] 320px bottom-tab caption concern identified and 12px targeted revision applied; **14/14 geometry rerun passed**
- [ ] Readable with enlarged text and on native screen reader
- [ ] Recorded Board decision with strengths, material objections and retest results

**Critical issue tracking:** a mismatched editor-back accessibility label needs source code fix later in S09, before accessibility/release gates. It does **not** justify declaring the S03 ASCII wireframe itself production-ready.

## Next gate behavior

If everything is supported by evidence, S03 may PASS for **low-fi layout composition** and open S04 art direction (two genuinely distinct visual directions). If visual hierarchy/readability fails, return to this S03 artifact rather than tweaking colors. If IA itself fails, reopen S02 and document why. Never skip directly to S05 tokens.

## Evidence pointer

[Deterministic HTML wireframe source](S03-wireframe-render.html) · [machine-readable geometry manifest](S03-browser-qa.json) · [visual critique](S03-render-audit.md). Captured PNGs and runnable capture script are in the **conversation ZIP**, not stored as GitHub binary assets. The new GitHub Actions manifest guard checks source digest and case records; it does **not** reproduce browser rendering in CI.
