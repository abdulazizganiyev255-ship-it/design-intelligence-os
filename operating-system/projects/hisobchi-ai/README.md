# Hisobchi AI — stage-first design project

**Source product:** [hisobchi-ai-mobile](https://github.com/abdulazizganiyev255-ship-it/hisobchi-ai-mobile). **Review mode:** SIMULATED_BOARD_REVIEW (one ChatGPT model, not 4 autonomous agents). All prior visual directions rejected, but source-domain behavior must be preserved.

## Current gate state

| Stage | Status | Output / next decision |
|---|---|---|
| S00 Evidence & baseline | **NEEDS_EVIDENCE** | `S00-evidence-and-gate.md`; owner to confirm scope/top-task |
| S01 Strategy | **NOT_STARTED** (draft prepared) | `S01-product-strategy.md`, `S01-board-review.md`; owner review, not approval |
| S02 IA | **NOT_STARTED** (candidate sketch only) | `S02-IA-provisional.md`; cannot mark PASSED until S01 approved |
| S03–S12 | NOT_STARTED | No visual tokens, components, implementation or release authorized |

The **current project state** is stored in `../hisobchi-ai.json`. `S01-decision-proposal.json` is a review proposal with **owner_approved=false**, not a runtime product configuration.

## Reading order

1. `S00-evidence-and-gate.md` — which previous visual directions failed and what is untested.
2. `S01-source-truth-contract.md` — authoritative **demo/session** arithmetic and clear UI labels.
3. `S01-product-strategy.md` — two distinct user jobs and recommended first slice.
4. `S01-board-review.md` — 4 simulated perspectives, conflicts, open risks.
5. `S01-decision-proposal.json` — machine-readable unapproved decision and test fixture.
6. `S02-IA-provisional.md` — **only** a candidate, NOT a finished S02.

## Owner decision

**Choose the first release's one primary job**:
- `A_RECORD_EXPENSE`: a testable demo/session workflow; Home → add → correct list and Analytics.
- `B_SAFE_TO_SPEND`: differentiated vision, **currently blocked** for live numeric promises by missing finance engine and verified balance.
- `OTHER`: owner-proposed user job, requiring reworked S01.

If Owner approves A for a **development prototype**, complete S00 decision record and S01 signoff, then make official S02 IA and S03 wireframes. Do not automatically claim owner approval from the existence of a GitHub PR.

## Validation

After merging the reviewed PR, GitHub Actions → `Validate Hisobchi Strategy` → Run workflow (manual). Locally: `python3 tools/validate_hisobchi_strategy.py` at repository root. Structural pass is **not** approval, real UX evidence, Android/iOS accessibility compliance, finance engine verification or an S+ grade.

## Change restrictions

- This package changes **documentation, test and GitHub config only**, not `hisobchi-ai-mobile` source or a production database.
- The actual reference source branch is `design/splus-living-ledger-analytics-v03` (a development branch); `main` of Hisobchi AI may differ.
- Never add banking/real money secrets to public GitHub.
