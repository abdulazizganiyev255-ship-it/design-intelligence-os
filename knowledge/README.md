# Knowledge Engine — MVP-01 rules (no RAG service yet)

## Purpose

Validated design principles, negative examples, evidence-tagged decisions and repeatable fixes should remain useful across projects. At Foundation v0.1 only *rules* and templates exist; the curated pattern library is not yet populated and vector search is not installed.

## Data classes

- `REFERENCE_PENDING`: source URL/capture without approved teardown.
- `PATTERN_CANDIDATE`: principle extracted from reference, needs review.
- `VALIDATED_PATTERN`: principle with evidence and successful case of use.
- `FAILURE_CASE`: reproduced defect, root cause, accepted fix and retest.
- `DECISION_RECORD`: trade-off, dissent and Owner decision.

## Promotion policy

1. Capture provenance and screenshot/flow evidence IDs.
2. Reviewer checks correctness and licensing.
3. If validated, link exact task/context and when pattern should **not** be used.
4. Keep version history, do not silently rewrite decisions.
5. On conflicting evidence, downgrade to `REVIEW_REQUIRED` and retest.

## Retrieval rules for future RAG

Search by user goal, platform, component, pattern and failure signature; return original source and review status. Do not include unreviewed candidate as proven knowledge. Measure retrieval quality with held-out task examples before deploying vector search.
