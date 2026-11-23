---
name: information-architecture
description: Build task-first information architecture, navigation and failure-aware user journeys before any visual styling.
---

# information-architecture — Design Intelligence OS v0.3

**Stage:** S02. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Build task-first information architecture, navigation and failure-aware user journeys before any visual styling.

## Inputs
approved brief, user segment, top task, real content inventory, platform, domain constraints.

## Procedure
1. Map entities/content; separate primary task, secondary tasks and admin/settings.
2. Draft screen/navigation map with entry, transitions, back, cancel and success destination.
3. For each action define input, expected result, ownership, error, empty, offline and loading states.
4. Check naming against user vocabulary; avoid labels that merely describe internal technical structures.
5. Review with four roles: can user find action, is hierarchy original with purpose, are states implementable, what evidence is missing?

## Outputs
screen-map.md, flows.md, state-matrix.csv and candidate navigation test.

## Acceptance / Quality gate
Every core task has an unbroken reachable happy path and a recoverable failure path; no styling decision made to hide an IA defect.

## Sources and caution
https://www.nngroup.com/articles/ten-usability-heuristics/

Link and extract principles with source provenance; do not import external code/skill text or claim tests that have not run. Every Board use logs four role positions with documented dissent.
