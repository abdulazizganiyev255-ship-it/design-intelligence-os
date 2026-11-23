# Efficiency & bottleneck management — initially metrics only, not fabricated stats

## Expected bottlenecks (architectural audit)

| Bottleneck | Root cause | Preventive control | Signal |
|---|---|---|---|
| Endless prompt revisions | No approved visual target / bad brief | S01→S04 owner freeze, no late random redesign | repeated concept rejections |
| Generic AI aesthetics | Stock card grid and palette-first workflow | reference teardown, alternative composition, taste critique at S04 | near-identical A/B, owner reject |
| Early component polishing | No IA/wireframe dependency | S02/S03 gates before S05/S06 | buttons designed before task |
| Board self-praise | One model debates itself | mandatory distinct positions, dissent, critique first and explicit simulation | no substantive objections |
| RAG self-contamination | Unverified output added as a 'pattern' | REVIEW_PENDING, evidence+human promotion | pattern lacking source/result |
| Source overload | indiscriminate GitHub cloning | fit/maintainer/license assessment; only adopt stage-relevant ideas | unused repositories, unclear ownership |
| Visual vs functional truth | fake numbers/AI progress in mockups | demo/source labels, finance truth gate at each stage | unsupported metrics shown |
| Web/native mismatch | relying on browser screens alone | independent native gate at S10 | unreadable native keyboard/VoiceOver |
| Automation expense | heavy agent/tool chain before proving value | ChatGPT+files first, no API dependency in v0.3 | cost per accepted artifact ↑ |

## Minimum observation log per project

`project_id, stage_id, iteration, issue_ids, source_evidence, output_artifact, owner_acceptance, reviewer_result, qa_passed, approximate_effort_minutes, paid_usage, next_stage`

Metrics without real observations = `NOT_MEASURED`. Compare before/after only at same task, data, viewport and platform. Have the Critical Reviewer attack the metric for Goodhart effects: if the number rose but user outcomes fell, reject the claimed improvement.

## Stop rule

If two cycles give no measurable progress, do not generate another arbitrary design. Revisit brief, references or information hierarchy and document the reason. This protects cost and attention.
