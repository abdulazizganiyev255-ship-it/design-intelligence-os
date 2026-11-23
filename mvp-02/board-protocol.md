# Board Session Protocol v0.1 — controlled, auditable simulation

**Execution:** one ChatGPT instance plays four perspectives **sequentially**, never four independent workers. Board is not a real jury or human test. Source of rules: \`governance/board-charter.md\`, \`governance/decision-policy.md\`.

## Session contract

**Required input:** \`session_id\`, \`project_id\`, \`artifact_kind\` (BASELINE_AUDIT or CONCEPT_REVIEW), brief/source identifiers, main user task, known evidence and unknowns, explicit owner goal and constraints.

**Required output:** a session Markdown report and a matching JSON record, all four role perspectives, alternative paths, objection/resolution pairs, dissent, recommendation, status, test plan, and evidence gate.

### Round 0 — preflight

- Check that source files/screenshots/prototype are actually available. Identify E-IDs and categorize evidence: OWNER_STATEMENT, SOURCE_DOCUMENT, SCREENSHOT, INTERACTION_RECORD, CODE, TEST_LOG, REFERENCE.
- An owner statement supports what the owner requested, **not** what real users did.
- For unknown measurements, write \`UNKNOWN\`. Never supply invented metrics or fake screenshots.
- If a real baseline is requested but there is no observable UI evidence, stop the *audit scoring*, output \`UNSCORED\`, and request the smallest useful screen/flow source. You may still document an intake or design proposal.

### Round 1 — perspective-first

Show roles in this exact order for consistent records. Prompt each role to avoid building on prior role praise; it must contribute a **distinct domain-specific question**. This is a method to structure one model's thinking, not a claim of independent inference.

1. UX Researcher: job, user task, mental model, errors and falsifiable task checks.
2. Creative Director: unique art direction; if ideating, give two different hierarchy/composition/interaction approaches.
3. Design Architect: component contracts, states, adaptive rules, technical constraints; mark unknown stack.
4. Critical Reviewer: strongest counterexample, missing evidence, P0/P1 if and only if reproducible, audit feasibility.

Every role produces: \`position\`, \`basis\` (FACT/HYPOTHESIS/DESIGN_JUDGMENT/UNKNOWN), \`evidence_ids\`, \`risk\`, \`proposed_action\`.

### Round 2 — debate

- Record at least two meaningful objections: who challenges whom, problem and observable impact, response, and remaining uncertainty.
- No fake conflict. If positions substantially agree, identify limitations and competing constraints rather than inventing animosity.
- Discuss potential regressions, especially what validated working elements must be preserved.
- If the decision has no empirical support, label it a reversible design hypothesis.

### Round 3 — resolution

- Compare \`Option A\` and \`Option B\` on hierarchy, flow, distinctness, effort and risk.
- Allowed decision statuses: PROPOSED, NEEDS_EVIDENCE, REVISE, ACCEPTED_FOR_PROTOTYPE, REJECTED, APPROVED_BY_OWNER, SUPERSEDED.
- \`ACCEPTED_FOR_PROTOTYPE\` is a Board *recommendation* in simulated mode. Owner approval stays PENDING until explicitly confirmed.
- Include dissent even if resolved (record as "resolved", do not erase the argument); cite reasons.
- Do not choose a concept as if mockup/implementation was tested if it was not.

### Round 4 — QA and learning gate

- For design auditing, evidence must support each rated criterion; use null for absent visual/interaction/accessibility data. No score inflation.
- Record P0/P1 blockers separately from presentation quality. With P0/P1 outstanding, release is blocked.
- For every accepted recommendation, give a testable next action, expected observation, scope, and approver.
- Record a knowledge candidate as REVIEW_PENDING. Mark validated only after actual verification by an appropriate reviewer.

## Stop and escalation

If contradictory source facts appear, mark NEEDS_EVIDENCE. If UX and creativity trade off, use the primary task to prioritize, then verify. After two review cycles without actionable evidence, stop and request a reference/owner decision. Do not run indefinite loops.

## Quality checks

The \`tools/validate_board_session.py\` check ensures required structure, role participation, real uncertainty labels, and correct status relationships. It **cannot** detect subtle aesthetic mistakes or verify citations. A screenshot is not proof that buttons work, and passing a JSON checker is not a product release gate.

## Persist

- Report: \`mvp-02/sessions/BOARD-XXX.md\`
- JSON: \`mvp-02/sessions/BOARD-XXX.json\`
- Owner decision: \`templates/decision-record.md\` copied into the project folder after explicit confirmation
- Validated lesson: \`knowledge/\` only after proof; otherwise REVIEW_PENDING
