# S03 Low-Fidelity Review Checklist

**Scope:** User-approved first MVP A_RECORD_EXPENSE. **Status:** NOT_TESTED for actual rendered wireframes; text sketches are a first deliverable.  
**No selected palette, font, icon brand, motion or React Native implementation in S03.**

## Per-screen acceptance

| Screen | Minimum task hierarchy | Variant to inspect | Evidence state |
|---|---|---|---|
| HOME | `Xarajat qo‘shish` before supporting KPI; source-qualified net | normal, empty, long UZS, 320/390 | TEXT_SPEC_ONLY |
| EDITOR_NEW | expense context, amount, category, date, note, save, reversible back | invalid amount/category/date, keyboard open, 320/390 | TEXT_SPEC_ONLY |
| HISTORY | actual records accessible before filter overload; clear search/reset | populated, no match, empty, filtered, 320/390 | TEXT_SPEC_ONLY |
| ANALYTICS | period, expense/income/net and honest coverage; optional actual-data chart | all/month/no income/negative net/no data | TEXT_SPEC_ONLY |

## Global checks

- [ ] Real low-fi grayscale render at 320×640 and 390×844 for all four screens
- [ ] Action CTA above fold and not obstructed by tab bar/keyboard
- [ ] Long amount `999 999 999 999 so‘m` and long Uzbek text do not clip
- [ ] No false live balance or Safe-to-Spend computation
- [ ] Screen reader/keyboard reading order spec maps to visual reading order
- [ ] Errors, cancel, back, selected filters, empty states have clear placement
- [ ] Source-based dates (22/21/20/19 Nov) and amounts used correctly in rendered demo
- [ ] Side-by-side critical review of actual 320 and 390 renders
- [ ] Recorded Board decision with strengths, material objections and retest results

**Critical issue tracking:** a mismatched editor-back accessibility label needs source code fix later in S09, before accessibility/release gates. It does **not** justify declaring the S03 ASCII wireframe itself production-ready.

## Next gate behavior

If everything is supported by evidence, S03 may PASS for **low-fi layout composition** and open S04 art direction (two genuinely distinct visual directions). If visual hierarchy/readability fails, return to this S03 artifact rather than tweaking colors. If IA itself fails, reopen S02 and document why. Never skip directly to S05 tokens.
