# BOARD-HISOBCHI-VISUAL-002 — Two real rendered concept directions

**Mode:** SIMULATED_BOARD_REVIEW; one ChatGPT model, NOT four autonomous agents.
**Date:** 2026-11-23
**Status:** VISUAL_CONCEPTS_RENDERED; OWNER_APPROVAL_PENDING; USABILITY_UNTESTED.
**Source baseline:** `baseline/hisobchi-ai/BASELINE-001.md`.
**Preceding discussion:** `mvp-02/sessions/BOARD-HISOBCHI-001.md`.

## Real visual outputs

Two **original layout prototypes** were generated as deterministic HTML/CSS and captured by headless Chromium, each at **390×844** and **320×640** CSS pixels at 2× device scale.

- `A_Decision_Surface_390x844.png` and `A_Decision_Surface_320x640.png`.
- `B_Cashflow_Horizon_390x844.png` and `B_Cashflow_Horizon_320x640.png`.
- Matching HTML sources and `qa-results.json` exist in the accompanying conversation deliverable package `Hisobchi_AI_Visual_Experiment_001.zip`. **Image assets are not committed to GitHub by this document**; do not treat this file as a hosted screenshot reference.

### Financial truth contract

Both render the **same** known session example: 5 entries, income 3,000,000 UZS; expense 259,000 UZS; net 2,741,000 UZS. These are demo session figures and **not** bank balance, live Safe-to-Spend or predicted analytics. The visible transaction subset uses previously recorded demo entries: Transport −12,000 on 22-Nov; Groceries −85,000 on 22-Nov; Cafe −42,000 on 21-Nov. Three shown of five entries. No fabricated 78% financial stability, 12% growth, AI insights, upcoming obligations or goals.

## Structural differences

**Option A — Decision Surface**: neutral editorial page. A single net figure with explicit provenance is the main focus, followed by income/expense context, one clear primary CTA and three recent transaction rows. Strong first action, weak uniqueness: potentially resembles conventional digital banking.

**Option B — Cashflow Horizon**: time-oriented personal finance reading. Compact provenance-safe net summary, immediate record-action button and dated event timeline. The chronological structure, rather than the hero balance, is the signature. This design intentionally shows recorded history only; future obligations are not invented.

## Simulated Board Round 1

- **UX Researcher (HYPOTHESIS):** A prioritizes today's action at a glance. B has stronger chronological recognition for users who think by dates. No real user task tests yet; neither wins usability.
- **Creative Director (DESIGN_JUDGMENT):** B is more meaningfully different from older rejected card/KPI compositions. A is cleaner but still close to a generic financial overview.
- **Design Architect (OBSERVATION + RISK):** Both prototypes use the same numbers and visible demo qualifications. B's time axis needs accessible order, variable dates and event detail interaction. A's income/expense rail is derived from the displayed aggregates but must be properly labelled when implemented.
- **Critical Reviewer (EVIDENCE GATE):** Neither static HTML mockup proves functional navigation, actual transaction editor, live bank data, screen reader support or performance. No S+ or 92/100 claim is allowed.

## Objections and targeted revisions

1. **UX → Creative:** B's CTA was originally below the timeline and inaccessible at first glance on 320×640. **Correction applied:** CTA relocated immediately after the net summary; browser DOM confirms it is initially visible at 320×640 and 390×844.
2. **Reviewer → Both directions:** Early generated image ideas contained made-up progress/trend numbers. **Correction:** these rejected renders were discarded; the deterministic prototypes contain no such unsupported metric.
3. **Architect → Both:** Some small metadata labels were difficult to read. **Correction applied:** text-size adjustments to the most prominent overlines, dates and transaction descriptors; native Dynamic Type testing remains open.
4. **Creative → UX:** A is a meaningful baseline but still reads like a standard balance-and-list screen. **Unresolved:** Owner preference for a stronger visual signature must be determined by actual visual comparison.

## Structural QA performed (not UX QA)

- Four Chromium renders at 2× DPR: A and B × 390×844 and 320×640.
- No page-level horizontal overflow at either viewport.
- Primary add-action CTA within the initial viewport above bottom navigation in both concepts at both widths; minimum prototype button height A=54px, B=48px.
- Text invariants verified: 2,741,000; 3,000,000; 259,000; DEMO; four navigation labels.
- Invalid generated 78% stability and +12% growth claims absent.
- Vertical scroll is available where content exceeds the initial viewport.
- **Not tested:** real button functionality, touch interactions, iOS/Android native runtime, keyboard focus sequence, screen readers, 2× Dynamic Type, actual user task completion, production finance data.

## Recommendation (NOT a final design choice)

**Develop B — Cashflow Horizon as the primary next-round creative experiment** because its information architecture is more distinctive, while retain A as an operational comparison. This recommendation has **no numeric quality score**: `UNSCORED`, Owner approval pending. Prototype-first, not deployment.

### Next gate

Owner compares actual A and B visuals; record precise liked/disliked elements and may reject both. After visual selection, implement one React Native vertical slice preserving source data contracts, then run native and usability QA. Do not copy the old look or merge source app PRs without review.

**Knowledge state:** REVIEW_PENDING. No RAG ingestion until validated.
