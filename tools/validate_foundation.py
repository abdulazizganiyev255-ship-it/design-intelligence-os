#!/usr/bin/env python3
"""Zero-dependency structural check and score gate for MVP-01 Foundation.

No network, browser, AI inference or product usability testing is performed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = {'V': 25, 'U': 20, 'T': 20, 'D': 10, 'A': 10, 'I': 10, 'F': 5}
REQUIRED = [
    'README.md', 'AGENTS.md', '.github/copilot-instructions.md',
    '.github/workflows/validate.yml',
    'baseline/00-purpose-scope.md', 'baseline/audit-protocol.md',
    'baseline/evidence-manifest.csv', 'baseline/baseline-register.csv',
    'governance/board-charter.md', 'governance/decision-policy.md',
    'governance/workflow.md', 'governance/quality-rubric.md',
    'agents/creative-director.md', 'agents/ux-researcher.md',
    'agents/design-architect.md', 'agents/critical-reviewer.md',
    'skills/design-brief/SKILL.md', 'skills/reference-teardown/SKILL.md',
    'skills/art-direction/SKILL.md', 'skills/ux-critique/SKILL.md',
    'templates/design-brief.md', 'templates/reference-card.md',
    'templates/audit-report.md', 'templates/decision-record.md',
    'evaluations/scorecard.schema.json', 'evaluations/example-unscored.json',
    'projects/pilot-01/brief.md', 'projects/pilot-01/board-simulation.md',
    'sources/references.md', 'tools/validate_foundation.py',
]


def validate_scorecard(card: dict) -> tuple[float | None, str, bool]:
    if set(card['criteria']) != set(WEIGHTS):
        raise AssertionError('Expected exactly seven rubric criteria')
    values = []
    for key, weight in WEIGHTS.items():
        item = card['criteria'][key]
        rating = item['rating']
        if rating is None:
            values.append(None)
            continue
        if not isinstance(rating, int) or isinstance(rating, bool) or not 0 <= rating <= 5:
            raise AssertionError(f'Invalid rating for {key}')
        if not item.get('evidence_ids'):
            raise AssertionError(f'Rating without evidence: {key}')
        if len(item.get('rationale', '').strip()) < 10:
            raise AssertionError(f'Rating lacks rationale: {key}')
        values.append(weight * rating / 5)
    calculated = round(sum(values), 2) if None not in values else None
    recorded = card['total_score']
    if (calculated is None) != (recorded is None):
        raise AssertionError('Total must be null if ANY criterion unscored')
    if calculated is not None and abs(calculated - recorded) > 0.001:
        raise AssertionError(f'Invalid total score: expected {calculated}, got {recorded}')
    blockers = [i for i in card['open_issues'] if i['severity'] in ('P0', 'P1')]
    eligible = bool(
        calculated is not None and calculated >= 85 and not blockers
        and card['acceptance_test']['status'] == 'PASS'
        and card['acceptance_test'].get('evidence_ids')
        and card['owner_approved']
        and card['review_mode'] == 'EXTERNAL_HUMAN_REVIEW'
    )
    if card['status'] == 'APPROVED_BY_OWNER' and not eligible:
        raise AssertionError('Approval requires all quality gates')
    if calculated is None and card['status'] != 'UNSCORED':
        raise AssertionError('Unscored report must be marked UNSCORED')
    return calculated, card['status'], eligible


def main() -> int:
    assert sum(WEIGHTS.values()) == 100, 'Rubric weights must sum to 100'
    missing = [f for f in REQUIRED if not (ROOT / f).is_file()]
    if missing:
        raise AssertionError('Missing: ' + ', '.join(missing))
    for path in REQUIRED:
        if not (ROOT / path).read_text(encoding='utf-8').strip():
            raise AssertionError('Empty file: ' + path)
    for name in ('design-brief','reference-teardown','art-direction','ux-critique'):
        raw = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
        assert raw.startswith('---\n'), f'Missing YAML frontmatter: {name}'
        sections = raw.split('---\n', 2)
        assert len(sections) >= 3, f'Unclosed frontmatter: {name}'
        assert f'name: {name}' in sections[1]
        assert 'description:' in sections[1]
        assert '## Inputs' in raw or '## Input contract' in raw, f'Input contract missing in {name}'
        assert '## Acceptance' in raw or '## Quality gate' in raw, f'Quality gate missing in {name}'
    schema = json.loads((ROOT / 'evaluations/scorecard.schema.json').read_text(encoding='utf-8'))
    assert set(schema['properties']['criteria']['required']) == set(WEIGHTS)
    example = json.loads((ROOT / 'evaluations/example-unscored.json').read_text(encoding='utf-8'))
    total, status, eligible = validate_scorecard(example)
    assert total is None and status == 'UNSCORED' and not eligible
    sim = (ROOT / 'projects/pilot-01/board-simulation.md').read_text(encoding='utf-8')
    assert 'SIMULATED_BOARD_REVIEW' in sim and 'APPROVED_BY_OWNER = false' in sim
    # Self-check: a fully evidenced 5/5 score would be 100, but Owner approval is still required.
    fake = json.loads(json.dumps(example))
    for item in fake['criteria'].values():
        item['rating'] = 5
        item['evidence_ids'] = ['E-TEST']
        item['rationale'] = 'Fixture rating; synthetic only, NOT an actual product review.'
    fake['total_score'] = 100
    fake['status'] = 'DRAFT'
    assert validate_scorecard(fake)[0] == 100
    assert not validate_scorecard(fake)[2], 'Missing owner approval must block S+'
    fake['owner_approved'] = True
    fake['acceptance_test'] = {'status': 'PASS', 'evidence_ids': ['E-TEST']}
    assert not validate_scorecard(fake)[2], 'Simulated Board cannot claim independent S+'
    fake['review_mode'] = 'EXTERNAL_HUMAN_REVIEW'
    assert validate_scorecard(fake)[2], 'Full external review fixture should pass eligibility'
    fake['open_issues'] = [{'id':'ISSUE-TEST','severity':'P1','evidence_ids':['E-TEST'],'summary':'Fixture blocker'}]
    assert not validate_scorecard(fake)[2], 'P1 must block even at 100 points'
    print(f'PASS: {len(REQUIRED)} required nonempty files; 4 skills; 7 weights=100; score gate fixtures')
    print('STATUS: Baseline artifacts remain UNSCORED; no visual/user tests performed.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (AssertionError, KeyError, ValueError, OSError) as exc:
        print('FAIL:', str(exc), file=sys.stderr)
        sys.exit(1)
