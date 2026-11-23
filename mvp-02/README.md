# MVP-02 — ChatGPT Design Council Execution v0.1

**State:** IMPLEMENTATION_PROPOSAL · **Mode:** SIMULATED_BOARD_REVIEW · **Owner approval:** PENDING
**Scope:** ChatGPT + GitHub. Hermes, external agent runtimes, vector RAG, unattended work and live design generation are **not** provided by this package.

## Result to achieve

A real product owner can submit a design brief or a rejected screen, receive four role-specific critiques and a recorded decision, and trace each claim back to evidence. Output must be reproducible by following the same protocol; any absent evidence is explicit.

MVP-01 documented roles. MVP-02 makes a **repeatable operating procedure**, not four independent models.

## First launch (no API cost)

1. Keep repository as source of truth. In ChatGPT create a Project named **Design Intelligence OS**; add instructions from [chatgpt-project-instructions.md](chatgpt-project-instructions.md). ChatGPT Projects do **not** automatically pull all GitHub updates. Add the relevant documents manually or supply direct source content in chat.
2. Supply the core files: \`AGENTS.md\`, \`governance/board-charter.md\`, \`governance/decision-policy.md\`, \`governance/quality-rubric.md\`, \`mvp-02/board-protocol.md\`, the four \`agents/*.md\` and selected \`skills/*/SKILL.md\`. Keep version/source references in the session.
3. Use [launch-prompts.md](launch-prompts.md), starting with **A: real baseline**. Use one rejected screenshot/flow, not a fictional app.
4. Store screenshot/evidence pointers in \`baseline/evidence-manifest.csv\`; complete [baseline-evidence-intake.md](baseline-evidence-intake.md). Do not put secrets, live financial details or personally identifying data into a public repository.
5. Run a structured council session. Save the role outputs and decision in \`mvp-02/sessions/\` and a corresponding \`templates/decision-record.md\` copy. Board is simulated, so \`owner_approval=PENDING\`.
6. Fill a scorecard only if each criterion is actually evidenced. Otherwise \`UNSCORED\` and \`total_score=null\`. No visual screenshot means no real visual audit score.
7. Verify local artifacts with \`python tools/validate_foundation.py\` and \`python tools/validate_board_session.py\`. The second command validates **board-session structure only**, not UX performance.
8. Owner reviews the decision and either approves a prototype scope, requests revision, or supplies missing evidence. Visual concept approval and production release approval are different decisions.

## The two entry modes

| Mode | Input | Output | Stop condition |
|---|---|---|---|
| Baseline audit | A real screenshot, prototype, or recorded interaction plus product/task context | Evidence-tagged findings, blocker priorities, \`UNSCORED\` if lacking coverage | No screenshots, unknown flow or unsupported claims |
| Pilot concept | Approved requirements and reference evidence | Two materially distinct direction proposals, Board disagreement, decision recommendation | No owner selection, no visual target, no tested prototype |

The existing \`projects/pilot-01/brief.md\` is a **working hypothesis**, not a user-tested product brief.

## Roles and gates

- UX Researcher: user job, task clarity, hypotheses, observable acceptance checks.
- Creative Director: two composition-level visual directions, not palette swaps.
- Design Architect: tokens, states, responsiveness, feasibility and known technical risks.
- Critical Reviewer: strongest counterarguments, source gaps, accessible design risks; no unsupported rating.

Every session goes through **intake → four-role first pass → objections → resolution → validation plan → human decision**. Detailed controls: [board-protocol.md](board-protocol.md).

## Definition of done for MVP-02

- [x] Reusable runbook and ChatGPT Project operating instructions.
- [x] Session format and deterministic structural validator.
- [x] Clearly identified simulated demonstration using existing pilot assumptions.
- [ ] A rejected real design captured as evidence with device, task and states.
- [ ] Before-scorecard or honest \`UNSCORED\` report from that artifact.
- [ ] A materially improved visual target reviewed by Owner.
- [ ] External human visual/UX review where S+ is claimed.

A structurally valid session is **not proof that the design is better**. That requires the last four items.

## Status language

\`SIMULATED_BOARD_REVIEW\`: one ChatGPT model alternates expert perspectives. \`ACCEPTED_FOR_PROTOTYPE\`: recommendation, **not** Owner approval. \`RELEASE_BLOCKED\`: open P0/P1 or failed top task. \`UNSCORED\`: incomplete evidence.

## Existing assets

- Foundation: \`README.md\`, \`AGENTS.md\`, \`baseline/\`, \`governance/\`, \`agents/\`, \`skills/\`.
- Example: \`projects/pilot-01/board-simulation.md\` and [sessions/BOARD-002.md](sessions/BOARD-002.md).
- Session record: [sessions/BOARD-002.json](sessions/BOARD-002.json).
- Validator: \`tools/validate_board_session.py\`.

**Cost:** no model API keys or third-party services are needed for the documentation and local validator. GitHub Actions is manual-only; account quotas can still apply.
