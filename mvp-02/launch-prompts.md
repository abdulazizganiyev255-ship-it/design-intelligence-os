# Launch Prompts — ChatGPT Design Council

Each prompt assumes the files listed in \`mvp-02/README.md\` are available to ChatGPT. Paste one prompt into the Project chat together with the relevant task artifact.

## A — First real baseline audit (recommended)

\`\`\`text
Design Intelligence OS: start BASELINE AUDIT in SIMULATED_BOARD_REVIEW mode.

Read AGENTS.md, governance/board-charter.md, governance/quality-rubric.md,
baseline/audit-protocol.md, mvp-02/board-protocol.md and 4 role contracts.

Evaluate ONLY the provided actual screenshot(s), flow or prototype evidence.
Context: product = [name]; platform = [mobile/web]; main user task = [task];
viewport/device = [device]; version = [version].
Evidence assets: [screenshot(s)/URL/recording].
Known functional limitations: [notes or UNKNOWN].

1) Create an E-ID evidence inventory. Do not infer hidden functionality.
2) Each of four role perspectives must give a distinct independent-looking
   first response (one model simulation, not real independent agents).
3) Challenge conflicts with a specific impact and corrective direction.
4) Produce P0-P3 findings and a prioritized top-three fix list.
5) Use the 100-point rubric ONLY for evidenced dimensions, otherwise UNSCORED.
6) Recommend what to preserve, revise, validate, and record in GitHub.
7) No approval or real test assertions without evidence.
\`\`\`

## B — Board review of two design concepts

\`\`\`text
Start a structured SIMULATED_BOARD_REVIEW on the provided approved brief.
Follow mvp-02/board-protocol.md.
Propose two materially different designs (information hierarchy, composition,
interaction, and component architecture), not merely different colors.
Give each of the four roles a distinct first-pass finding.
Debate the strongest UX-vs-originality and engineering-vs-aesthetics trade-offs.
Produce a proposed Decision Record with risks, dissent, and test plan.
Do not claim that a visual target or code was implemented. Owner approval=PENDING.
\`\`\`

## C — Verify a revision

\`\`\`text
Compare two versions of the SAME design task using baseline/audit-protocol.md.
List explicit before and after evidence IDs, matching device and content scope.
For each changed issue state: reproduced / fixed / regressed / not tested.
Compute score delta only if all seven criteria are covered for BOTH versions.
Produce targeted follow-ups; keep any unsupported claim UNKNOWN.
\`\`\`

## D — Record validated knowledge for future RAG (manual)

\`\`\`text
From this review, identify candidate learnings for knowledge/.
For each: source E-ID, context where valid, observed behavior, exception,
counterexample, reviewer status and required verification.
Only human-verified observations may be labeled VALIDATED_PATTERN.
Everything else is REVIEW_PENDING. Do not claim an automatic RAG index exists.
\`\`\`

## Session saving

Record the full conversation result in \`mvp-02/sessions/BOARD-<ID>.md\`, with a machine-readable JSON record if useful. Do not commit private screenshots or API keys to a public repository. For approval, have Owner review the session and fill an explicit decision record.
