#!/usr/bin/env python3
"""Hisobchi AI S00/S01 source-truth + sequential stage integrity (stdlib only).

This reads documentation and proposed decisions. Passing it DOES NOT mean
visual UX, finance-engine, mobile accessibility, or human user tests passed.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROPOSAL = ROOT / "operating-system/projects/hisobchi-ai/S01-decision-proposal.json"
PROJECT = ROOT / "operating-system/projects/hisobchi-ai.json"
STAGES = ROOT / "operating-system/stages.json"


def ensure(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def validate(p: dict, project: dict, stages: dict) -> None:
    ensure(p.get("project_id") == project.get("project_id") == "hisobchi-ai", "Wrong project")
    ensure(p.get("mode") == project.get("mode") == "SIMULATED_BOARD_REVIEW", "No autonomous agent claim")
    ensure(p.get("source_repo") == "abdulazizganiyev255-ship-it/hisobchi-ai-mobile", "Unknown source repo")
    ensure(p.get("source_branch") == "design/splus-living-ledger-analytics-v03", "Source branch mismatch")
    ensure(p.get("decision_status") == "NEEDS_OWNER_DECISION", "Proposal cannot silently become an approval")
    ensure(p.get("owner_approved") is False and p["first_mvp_job"].get("owner_selected") is False, "No human approval")
    ensure(project.get("visual_target_approved") is False and project.get("production_release_approved") is False, "Unapproved product status")
    ensure(project.get("visual_score") is None, "No fabricated visual score")

    # S00 still lacks full scope approval. S01 is only a DRAFT artifact, NOT an unlocked stage.
    ensure(p.get("stage_S00") == project["stage_status"]["S00"] == "NEEDS_EVIDENCE", "S00 gate status mismatch")
    ensure(p.get("stage_S01") == project["stage_status"]["S01"] == "NOT_STARTED", "S01 cannot start before S00 gate")
    ensure(p.get("stage_S02") == project["stage_status"]["S02"] == "NOT_STARTED", "S02 cannot pass before S01")
    ensure(project.get("workflow_stage") == "S00", "Wrong current gated stage")
    ensure(len(stages.get("stages", [])) == 13, "Expected thirteen stages")
    ensure(stages["stages"][1]["depends_on"] == ["S00"], "S01 dependency missing")
    ensure(stages["stages"][2]["depends_on"] == ["S01"], "S02 dependency missing")

    # A user segment and usability claims are still hypotheses.
    seg = p.get("target_user_segment", {})
    ensure(seg.get("status") == "HYPOTHESIS" and seg.get("user_research_evidence") == [], "Cannot invent market/user study")
    ensure(p.get("first_mvp_job", {}).get("id") == "A_RECORD_EXPENSE", "Unexpected first MVP candidate")
    ensure(p["first_mvp_job"].get("status") == "RECOMMENDATION_ONLY", "Candidate is not approved")
    north = p.get("north_star_job", {})
    ensure(north.get("id") == "B_SAFE_TO_SPEND", "Missing north-star option")
    ensure(north.get("status") == "NOT_IMPLEMENTED" and north.get("ready_for_live_claim") is False,
           "Real Safe-to-Spend falsely presented as available")
    ensure(len(north.get("requirements", [])) >= 4, "Missing finance engine prerequisites")

    t = p.get("demo_truth", {})
    ensure(t.get("currency") == "UZS", "Wrong currency")
    ensure(t.get("record_count_before") == 5 and t.get("record_count_after") == 6, "Unexpected fixture count")
    ensure(t.get("income_before") == 3_000_000 and t.get("expense_before") == 259_000, "Seed source changed")
    ensure(t.get("example_added_expense") == 100_000, "Expected example expense")
    ensure(t.get("net_before") == t["income_before"] - t["expense_before"], "Wrong initial net")
    ensure(t.get("turnover_before") == t["income_before"] + t["expense_before"], "Wrong initial turnover")
    ensure(t.get("income_after") == t["income_before"], "Expense changes income incorrectly")
    ensure(t.get("expense_after") == t["expense_before"] + t["example_added_expense"], "Wrong expense-after")
    ensure(t.get("net_after") == t["income_after"] - t["expense_after"], "Wrong net-after")
    ensure(t.get("turnover_after") == t["income_after"] + t["expense_after"], "Wrong turnover-after")
    ensure(t.get("fixed_sample_balance") == 12_850_000, "Sample balance changed")
    ensure(t.get("fixed_sample_safe_to_spend") == 145_000, "Demo Safe-to-Spend changed")
    ensure(t.get("fixed_sample_monthly_expense") == 3_840_000, "Sample chart changed")

    q = p.get("quality", {})
    ensure(q.get("visual_total_score") is None and q.get("user_study_status") == "NOT_CONDUCTED",
           "Fabricated visual/user review result")
    ensure(q.get("native_accessibility_status") == "NOT_TESTED" and q.get("ui_release_status") == "NOT_APPROVED",
           "Fabricated native/release result")

    artifact_paths = p.get("artifacts", {})
    ensure(len(artifact_paths) >= 5, "Required strategy deliverables missing")
    for key, relative_path in artifact_paths.items():
        ensure(isinstance(relative_path, str) and (ROOT / relative_path).is_file(),
               f"Missing {key}: {relative_path}")


def negative_tests(p: dict, project: dict, stages: dict) -> None:
    changes = [
        lambda x: x.update(owner_approved=True),
        lambda x: x.update(stage_S02="PASSED"),
        lambda x: x["first_mvp_job"].update(owner_selected=True),
        lambda x: x["north_star_job"].update(ready_for_live_claim=True),
        lambda x: x["demo_truth"].update(expense_after=123_456),
        lambda x: x["quality"].update(visual_total_score=99),
        lambda x: x["target_user_segment"].update(status="FACT"),
    ]
    for index, mutate in enumerate(changes, 1):
        bad = copy.deepcopy(p)
        mutate(bad)
        try:
            validate(bad, project, stages)
        except ValueError:
            continue
        raise AssertionError(f"False-positive: bad fixture {index} accepted")


def main() -> None:
    p = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    project = json.loads(PROJECT.read_text(encoding="utf-8"))
    stages = json.loads(STAGES.read_text(encoding="utf-8"))
    validate(p, project, stages)
    negative_tests(p, project, stages)
    print("PASS: Hisobchi strategy proposal, source finance arithmetic and dependency gates.")
    print("PASS: 7 negative fixtures blocked false owner approval, stage skip, fake finance and score.")
    print("NOT TESTED: React Native UI, independent agents, actual users, live Safe-to-Spend, native a11y.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, AssertionError, OSError, KeyError, TypeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
