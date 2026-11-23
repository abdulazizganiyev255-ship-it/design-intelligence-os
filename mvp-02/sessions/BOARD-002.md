# BOARD-002 — Design Council Workspace (SIMULATED_BOARD_REVIEW)

**Date:** 2026-11-23
**Project:** pilot-01
**Source:** \`projects/pilot-01/brief.md\` and \`projects/pilot-01/board-simulation.md\`
**Mode:** one ChatGPT model simulates perspectives; no independent agents or observed users.
**Evidence:** E-OWNER-001 = initial owner-requested brief. This proves *requirements were stated*, not usability or visual quality.
**Review status:** concept discussion only; \`UNSCORED\` / \`total_score=null\`.
**Owner approval:** PENDING.

## Decision question

Which information architecture is more promising for the first Design Council Workspace screen, given the user task to track brief → concept → critique → decision?

## Round 1 — Four different role positions

**UX Researcher — HYPOTHESIS.** A decision-first structure could be easier for one active project; however, no evidence demonstrates brief discovery in three actions. Create an observable test and handle pending/no-decision states.

**Creative Director — DESIGN_JUDGMENT.** Favor an editorial hierarchy: one primary decision, its why, one next action, and a restrained critique timeline. A distinctive composition must express meaningful information, not ornamental effects.

**Design Architect — DESIGN_JUDGMENT.** Do not use a fixed-height hero. Define adaptable decision, review and action components, with a desktop rail collapsing to mobile content order. Missing focus, loading and error contracts are engineering risks.

**Critical Reviewer — UNKNOWN / NOT_TESTED.** No screenshot, prototype or behavior recording exists. It would be false to say this interface is premium, compliant, usable or S+. All seven quality dimensions remain \`UNSCORED\` until appropriate evidence exists.

## Two alternatives

**Option A — Editorial Decision Canvas:** Decision-first editorial composition; desktop context rail, mobile first-action hierarchy. Strength: focus and identity. Risk: future multi-project overview.

**Option B — Mission Control Workspace:** Status-first project board with filters/activity queue. Strength: operational oversight. Risk: density and generic admin presentation for a one-project pilot.

These differ by task model, hierarchy and layout; they are not palette variations.

## Round 2 — challenge and response

1. **UX → Creative:** A large visual header could move the next action below the first viewport. **Response:** keep active decision and CTA visible above decoration; confirm at 360px with real render. **Unresolved:** actual speed is unmeasured.
2. **Reviewer → Architect:** A hypothetical responsive contract is not proof of keyboard or mobile correctness. **Response:** create a state/viewport matrix and perform actual tests before QA approval. **Resolved as a plan, not as a tested product.**

**Dissent:** UX Researcher does not endorse speed claims until the three-action test is performed. Reviewer does not endorse a numeric aesthetic score on an absent UI.

## Resolution — recommendation only

**\`ACCEPTED_FOR_PROTOTYPE\` (recommendation).** Choose **Option A** to create the first visual target, preserving a clear current decision, explanation and next action. Keep Option B as a future multi-project comparison. This is reversible and **not** an Owner approval or software release.

**Owner approval:** \`false\` · **Score:** \`null\` · **Functional tests:** \`NOT_TESTED\`.

## Next tests and acceptance

1. Render consistent content at 360px, 390px, 1440px; capture screenshots.
2. Test whether a person can open the active brief and next action within three actions, recording real steps.
3. Verify focus order, error, empty, pending states and contrast; log observed results.
4. Obtain explicit Owner concept selection after comparing the actual render to requirements.

## Learning policy

Candidate insight: decision-first hierarchy can provide clarity for a one-project workflow. **Status:** \`REVIEW_PENDING\`, not VALIDATED_PATTERN. No automatic RAG update is claimed.

Machine-readable record: [BOARD-002.json](BOARD-002.json).
