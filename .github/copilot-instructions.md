# Design Intelligence OS — repository instructions

This repository is the documented MVP-01 Foundation, **not** a deployed multi-agent application.
Read `AGENTS.md` and `README.md` before proposing changes.

## Rules
- Follow `governance/board-charter.md`, `governance/decision-policy.md`, `governance/workflow.md`, and `governance/quality-rubric.md`.
- Treat the four roles in `agents/` as **simulated perspectives in ChatGPT**, not independently deployed autonomous agents.
- Distinguish FACT, HYPOTHESIS, DESIGN_JUDGMENT, RECOMMENDATION, and UNKNOWN.
- Never invent user research, screenshots, benchmark scores, citations, visual reviews, completed tests, or approvals.
- For missing visual evidence, use `UNSCORED`; see `baseline/audit-protocol.md`.
- Keep reference provenance and respect source licensing. Reuse design principles, not unlicensed assets.
- For concept work, compare two meaningfully different directions; preserve already-validated features.
- Accessibility target is WCAG 2.2 AA, verified with relevant manual and automated tests.
- Do not mark a result `APPROVED_BY_OWNER` or `RELEASED` without owner sign-off.
- The quality gate defined by `tools/validate_foundation.py` is structural only; it is not a usability/visual test.

## Required workflow
1. Confirm the brief, constraints, and evidence.
2. Produce the role-based review and record competing viewpoints.
3. Write a decision record and follow `governance/decision-policy.md`.
4. Run `python tools/validate_foundation.py` for changes affecting Foundation.
5. Propose changes via a pull request; do not silently merge to `main`.
