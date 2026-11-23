# BOARD-HISOBCHI-001 — Resetting Hisobchi AI visual direction

**Mode:** SIMULATED_BOARD_REVIEW (one ChatGPT model, four roles, not autonomous agents)
**Date:** 2026-11-23
**Reference baseline:** \`baseline/hisobchi-ai/BASELINE-001.md\`
**Owner constraint:** none of the earlier Hisobchi AI visual directions is acceptable as final.
**Decision state:** \`PROPOSED\`; Owner approval \`PENDING\`.
**Actual review coverage:** six representative full-resolution web screenshots at 393×852 and 320×640, with other thumbnails and source descriptions; native UX and direct user tests absent.

## Board question

How should the design team reset Hisobchi AI visually without destroying verified finance behavior, and what should be the **first real visual experiment**?

## Round 1 — four distinct expert perspectives (simulated)

### UX Researcher — HYPOTHESIS + FACTS
**FACT:** Home shows sample daily amount, sample balance, add-expense CTA, and separate monthly graphic, all prominently. Multiple labels disclose the data is demo. Evidence: E-SHOT-001.
**HYPOTHESIS:** a person opening the app likely needs to know *what financial decision is safe next*, and then record an action. But actual priority must be validated against target users rather than asserted.
**Proposed action:** task-first IA; do not show a numeric "safe to spend" as a live entitlement without deterministic data proof. Maintain accessible explanation and transaction capture.
**Risk:** reducing information may bury an important secondary task.

### Creative Director — DESIGN_JUDGMENT
**Position:** this is not a color problem. The screens have competent but conventional finance-app grammar: stacked KPIs, segmented pills, cards, short bar charts. Their sequence does not communicate a singular, ownable visual identity.
**Proposed action:** create two structural concepts with different layouts, priorities and interaction models. No repeat of old forest/coral, saturated blue, neon, or arbitrary glass effects. Colors remain undecided until side-by-side visual comparison.
**Risk:** visual experimentation could become novelty without clarity.

### Design Architect — SOURCE-GROUNDED ENGINEERING JUDGMENT
**FACT:** the code maintains session-derived transactions/analytics and separately fixed demo dashboard numbers. Prior PRs report browser E2E passes, but native QA is incomplete (E-DOC-001).
**Proposed action:** keep existing domain models and tested flows behind a replaceable visual layer; specify new semantic tokens, state matrix, Dynamic Type and no-data UI. Ensure the UI never implies that sample finance data is live.
**Risk:** interface visual choices could accidentally change critical financial semantics.

### Critical Reviewer — INTEGRITY GATE
**FACT:** Owner rejected the visual outcomes, while web browser CI results do not measure the user's aesthetic acceptance. Only selected web screenshots were directly reviewed here.
**Proposed action:** give no total score. Record visual findings and independent-looking but **simulated** dissent; test a genuinely new concept against the same concrete task before developing all screens.
**Risk:** inventing a "10/10" grade or claiming four independent agents would make this Design OS untrustworthy.

## Round 2 — genuinely different structural directions

### Option A — Decision Surface (recommended for an experiment)
**Primary interaction model:** a focused financial question + one next action; secondary account facts on demand.
- Home begins with one sourced status: financial position, or a truthful "not calculated" state.
- One explicit input action (record income/expense) and one context-aware recommendation **only if evidence-backed**.
- A compact spending/commitment strip; simple change-trail and source/last-updated affordance.
- Transaction history has privileged space: an amount/date ledger, with controls progressively disclosed.
- Visual signature: an **information architecture** centered on a single decision. Typography and open space carry emphasis, not decorative cards.
- Engineering dependency: don't fill financial truth gaps with fabricated outputs.
**Expected benefit (hypothesis):** faster top-task orientation and lower visual noise.
**Main risk:** too little overview for advanced multi-account planning.

### Option B — Cashflow Horizon
**Primary interaction model:** time-forward money map, not a tile-based dashboard.
- Home organizes recorded events and future commitments on a horizontal/vertical time axis, with present position and coming obligations distinguished.
- Primary action attaches to a point in the timeline; period summaries are revealed contextually.
- Visual signature: meaningful temporal structure, not a row of KPIs.
- Needs a reliable model for due dates, recurring expenses, planned obligations and "unknown future" handling.
**Expected benefit (hypothesis):** useful mental model for a user focused on upcoming cashflow.
**Main risk:** adds cognitive and data complexity; must not invent future spending.

**Crucial difference:** A organizes by *decision/action now*; B by *time/change through future*. These are not two colorways or old template remixes.

## Round 3 — objections, rebuttals, unresolved dissent

1. **UX → Creative:** a signature composition can still sacrifice financial scanning. **Reply:** show one sourced financial position, adjacent source qualifier and one obvious next action; test recognition and task steps. **Unresolved:** actual top user job, not yet empirically measured.
2. **Architect → Option B:** timeline requires reliable commitments. **Reply:** show only recorded events and explicitly unknown dates until data contracts exist. **Unresolved:** if no future commitment data exists, Option B may be less useful in first version.
3. **Reviewer → whole Board:** using owner's visual rejection is not proof that a specific alternative will work. **Reply:** no S+ rating or selection until actual 360/393 screenshots and owner comparison. **Status:** hard gate retained.

## Proposed decision

**Status:** PROPOSED. **Recommendation:** test Option A first because it fits a minimal data-truth-safe MVP, but create Option B as a meaningful structural foil so visual selection is not predetermined.
**Owner approval:** PENDING. **Release:** BLOCKED_PENDING_REAL_VISUAL.
**Preserve:** transaction CRUD, analytics logic, date validation, semantic financial labels, access control and test paths.
**Do not preserve:** old visual palette/composition, dashboard block hierarchy, unselected card/icon treatment or artificial AI descriptions.

## Next visual experiment (not implemented here)

- Deliver two visual targets for Home, 390×844 and 320×640, with realistic Uzbek labels and **explicitly demonstrative** numeric states when live truth absent.
- Accompany each with transaction-create flow sketch and a source label for every major financial number.
- Ask: Can a viewer instantly say what this number means, what to do next, and where the data came from?
- Owner ranks originality, comprehension, trust and usability without a forced fixed palette.
- Only after selection, create semantic type/color/spacing tokens and build one vertical slice.

## Scoring

The actual historical screenshots show demonstrable compositional issues, but not full user-task outcomes, native accessibility, engineering completeness across variants, or owner calibration. Therefore \`total_score=null\`, \`UNSCORED\`, no owner approval.

## Learning status

Candidate anti-pattern: A finance Home with multiple unrelated headline KPIs and repeated demo labels can fail to communicate a single financial decision. \`REVIEW_PENDING\` until a controlled before/after test. No automatic RAG indexing is claimed.
