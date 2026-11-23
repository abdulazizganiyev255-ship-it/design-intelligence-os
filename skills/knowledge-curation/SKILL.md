---
name: knowledge-curation
description: Promote verified design patterns and failure cases into a searchable knowledge set without feedback-loop hallucinations.
---

# knowledge-curation — Design Intelligence OS v0.3

**Stage:** S12 and incremental. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Promote verified design patterns and failure cases into a searchable knowledge set without feedback-loop hallucinations.

## Inputs
actual source URLs, Board decisions, before/after evidence, Owner feedback, tests and context boundaries.

## Procedure
1. Record raw source URI/version, license, exact claim and observed context; keep hypothesis label.
2. Distill into a decision-relevant design principle with 'when useful' and 'when harmful' sections.
3. Require corroborated evidence and human review before status becomes VALIDATED_PATTERN.
4. Store examples and counterexamples with original links and failure/evaluation IDs.
5. Before future advice, retrieve by task/platform/stage, cite sources and reject stale or out-of-context matches.

## Outputs
reference card, pattern record, failure case or RESEARCH_PENDING queue; retrieval check case.

## Acceptance / Quality gate
No unverified output promoted to RAG truth; source provenance and license retained; recommendation acknowledges evidence limits.

## Sources and caution
https://github.com/pgvector/pgvector ; https://github.com/qdrant/qdrant ; https://github.com/design-tokens/community-group

Source-specific principles require verification and provenance; adapting a methodology is not copying third-party code. Board review records four viewpoints, limitations and next tests.
