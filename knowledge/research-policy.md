# Research, upstream code and RAG policy v0.3

**No automatic retrieval or learning service has been installed.** This repository is an evidence-first manually curated knowledge set; optional vector retrieval belongs only after S12 and acceptance of usefulness.

## Source intake — 7 checks before adoption

1. **Originality:** official upstream repository/spec vs fork, scraper, repost, community post.
2. **Relevance:** exact user task, device, stack, stage and dependency.
3. **Evidence:** code/docs actually inspected vs README-only vs search result; never claim source audit beyond reviewed scope.
4. **License:** inspect current upstream LICENSE and dependency license before copying *code or assets*. Link-only educational notes do not imply permission to redistribute screenshots.
5. **Maintenance:** check recent changes, release notes, breaking changes and documentation consistency when implementation is selected. Popularity stars are **not** quality evidence.
6. **Security/performance:** dependencies, permissions and runtime fit with the user's repo; never execute copied scripts blind.
7. **Version pinning:** record source branch/commit/tag, checked_at date, adapted sections and validation scenario.

## Acceptance categories

- `CORE_STANDARD`: use direct standard/guidance for evaluation (e.g. WCAG, DTCG).
- `REFERENCE`: study decision and implementation patterns; *not* drop-in code.
- `CANDIDATE_TOOL`: pilot on a separate branch only after license, maintenance and platform fit.
- `ADAPT_ONLY`: original domain differs; extract context-limited principles; no direct installation.
- `RESEARCH_ONLY`: useful reference but out of MVP scope.
- `LATER_RAG`: dependency deferred until manual retrieval demonstrably fails.

## Knowledge record state machine

`RAW_REFERENCE → RESEARCH_PENDING → REVIEWED_CANDIDATE → VALIDATED_PATTERN` or `REJECTED/STALE`. Promotion requires provenance, observed outcome, task/device context, reviewer rationale and human verification. A plausible model statement alone cannot reach VALIDATED_PATTERN.

For an anti-pattern, store `before_evidence`, `defect`, `root_cause_hypothesis`, `fix`, `after_evidence`, `retest` and `counterexample`. Source snapshots must redact secrets and personal data.

## Retrieval policy

Retrieve by `task + stage + platform + interaction + user context`, not by aesthetic keywords alone. Return the smallest handful of source cards with citations and confidence; require a counterexample. Re-rank by applicability and recency, not GitHub stars. Record when retrieval misled the project, then adjust prompts or source states.

## Measuring RAG's actual impact before deployment

Prepare 10 recurring design tasks with expected sources and decisions. Compare manual curated search vs later automated retrieval on citation accuracy, decision usefulness, ignored critical source risks and hallucinated patterns. Only add pgvector/Qdrant if the extra maintenance is justified by validated improvement.

## Copyright and privacy

Never upload proprietary screenshots, customer data, bank details, fonts or private source into public GitHub. Link to original material when allowed; do not bulk copy entire source repositories into this OS. Use license review before dependency/vendor incorporation. RAG storage is not permission to redistribute.
