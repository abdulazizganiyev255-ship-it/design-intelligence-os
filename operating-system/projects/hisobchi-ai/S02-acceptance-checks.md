# S02 — Evidence-based acceptance and QA plan

**Status:** NOT_EXECUTED in new design. These are scripted acceptance scenarios, NOT observed passes.  
**Unit under test:** first MVP's task-first IA, not generated visual design.  
**Data:** Five deterministic demo records; source branch `design/splus-living-ledger-analytics-v03`. Use device/viewport evidence once implementation starts.

| ID | Scenario | Expected observables | Evidence to capture | Test status |
|---|---|---|---|---|
| S02-FLOW | Home → add expense → save → History | action visible; editor knows origin; saved row in History | video + row ID + source commit | NOT_TESTED |
| S02-FIN | Add 100,000 UZS expense to 5-seed demo | 6 rows; expense 359,000, net 2,641,000, income 3,000,000; sample balance 12,850,000 and demo Safe-to-Spend 145,000 unchanged | state diff, actual app totals | NOT_TESTED |
| S02-VALID | Empty/0/negative/decimal/oversized amount, invalid category/future date | field-specific errors, no committed mutation, valid correction works | screenshots/validation logs | NOT_TESTED |
| S02-RECOVERY | New/edit cancel, reset cancel, date modal cancel | no mutation and correct origin return | before/after counts plus navigation trace | NOT_TESTED |
| S02-EDIT | Edit existing transaction and update | same record ID updated once; correct totals | state diff and screenshot | NOT_TESTED |
| S02-DELETE | Delete opens confirmation; cancel vs confirm | cancel unchanged; confirm removes exactly one selected record | recording/state ID | NOT_TESTED |
| S02-HISTORY | Search/filter vs clear and truly empty session | distinguish `no matching results` from no rows | screenshots at 320/390 widths | NOT_TESTED |
| S02-FILTER | Period/custom dates and visible totals | inclusive start/end; future and reverse ranges rejected; filtered totals sum visible set | test data and calculation | NOT_TESTED |
| S02-DATE | Calendar selection / cancellation | valid day applied; cancel restores old date | UI recording | NOT_TESTED |
| S02-EMPTY | No-income range, zero data and negative net | honest labels, no fabricated growth or trend | screenshots and totals | NOT_TESTED |
| S02-TRUST | Distinguish session net vs demo balance vs uncomputed live allowance | user can say what each amount means; source labels remain visible | human task comprehension test | NOT_TESTED |
| S02-NAV | Tab switching, editor return and selected tab | no unreachable page; back/cancel preserves context | navigation trace | NOT_TESTED |
| S02-A11Y | Android/iOS dynamic type, focus, keyboard/modal/back | field remains usable; focus, labels and recovery work | device/emulator test logs | NOT_TESTED |

## Test design

**Stage S02 structural inspection:** parse `S02-navigation.json`, verify valid screen IDs/transition endpoints, reachable flow, recovery of destructive/invalid actions and finance values. This is source/spec integrity only.

**Later S08/S09/S10 execution:** run actual React Native / Expo UI or accessible browser prototype. Record device, OS, build SHA, seed dataset, timezone, calendar today, operator, steps, expected/observed result, screenshot/recording and failure severity. Use user studies only when actual participants provide evidence.

**Data scope caveat:** `S02-FIN` fixture applies to `all` period or a date range that includes all seeded entries. A filtered week or month is not expected to show this same all-time total. Never confuse source-backed fixture with execution result.

## S02 approval conditions

- User task passes *spec-level* walkthrough: every required state/action has a route or explicit conditional guard.
- No broken graph IDs or unreachable main route; overlays have reversible cancel.
- Four-role Board responds with evidence, dissent and resolution.
- Source truth preserved; no fake live budget.
- If all structural checks pass, Board may recommend scoped S02 PASS; implementation/user-study still pending and no S+ rating.

## S03 dependency

S03 wireframe construction may start only after S02 stage is marked `PASSED` by a separate recorded Board gate. This file does not grant that permission.
