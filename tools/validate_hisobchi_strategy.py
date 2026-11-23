#!/usr/bin/env python3
"""Hisobchi AI S00/S01 owner approval, S02 route + data integrity (stdlib only).

Structural and source-fixture consistency only. Does NOT test mobile UI,
actual people, accessibility, autonomy, or bank/finance integrations.
"""
from __future__ import annotations

import copy
import csv
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "operating-system/projects/hisobchi-ai"
PROJECT = ROOT / "operating-system/projects/hisobchi-ai.json"
STAGES = ROOT / "operating-system/stages.json"

REQUIRED_CHECKS = {
    "S02-FLOW", "S02-FIN", "S02-VALID", "S02-RECOVERY",
    "S02-EDIT", "S02-DELETE", "S02-HISTORY", "S02-FILTER",
    "S02-DATE", "S02-EMPTY", "S02-TRUST", "S02-NAV", "S02-A11Y"
}


def require(condition: object, message: str) -> None:
    if not condition:
        raise ValueError(message)


def stage_and_source(p: dict, project: dict, stages: dict) -> None:
    require(p.get("project_id") == project.get("project_id") == "hisobchi-ai", "Project mismatch")
    require(p.get("mode") == project.get("mode") == "SIMULATED_BOARD_REVIEW",
            "Do not claim independent agents")
    require(p.get("source_repo") == "abdulazizganiyev255-ship-it/hisobchi-ai-mobile", "Wrong source repo")
    require(p.get("source_branch") == "design/splus-living-ledger-analytics-v03", "Wrong source branch")
    require(p.get("decision_status") == "APPROVED_BY_OWNER" and p.get("owner_approved") is True,
            "Required explicit owner decision missing")
    require(p.get("owner_approval_scope") == "FIRST_MVP_PRIMARY_JOB_ONLY", "Approval must be scoped")
    require(p.get("owner_approval_date") == "2026-11-23", "Approval date missing")
    approval_path = p.get("owner_approval_evidence", "")
    require(approval_path == project.get("owner_decision_record"), "Approval evidence mismatch")
    require((ROOT / approval_path).is_file(), "Owner decision record missing")
    approval_text = (ROOT / approval_path).read_text(encoding="utf-8")
    require("Hisobchi AI uchun A" in approval_text and "S02" in approval_text,
            "Cannot treat prior simulated board as Owner approval")

    statuses = project.get("stage_status", {})
    require(p.get("stage_S00") == statuses.get("S00") == "PASSED", "S00 scoped gate not passed")
    require(p.get("stage_S01") == statuses.get("S01") == "PASSED", "S01 first-job gate not passed")
    require(p.get("stage_S02") == statuses.get("S02") == "PASSED", "S02 spec gate not passed")
    require(p.get("stage_S03") == statuses.get("S03") == "IN_PROGRESS", "S03 must be in-progress")
    require(project.get("workflow_stage") == "S03", "Wrong current stage")
    require(all(statuses.get(f"S{i:02}") == "NOT_STARTED" for i in range(4, 13)),
            "Cannot skip S03 and start S04–S12")
    require(stages.get("stage_count") == 13, "Unexpected sequential design OS")
    require(stages["stages"][1]["depends_on"] == ["S00"], "S01 dependency missing")
    require(stages["stages"][2]["depends_on"] == ["S01"], "S02 dependency missing")
    require(stages["stages"][2]["review_required"] is True, "S02 Board review required")
    require(project.get("visual_target_approved") is False and
            project.get("production_release_approved") is False and
            project.get("visual_score") is None, "False design/release approval")

    segment = p.get("target_user_segment", {})
    require(segment.get("status") == "HYPOTHESIS" and segment.get("user_research_evidence") == [],
            "No first-hand user research available")
    job = p.get("first_mvp_job", {})
    require(job.get("id") == "A_RECORD_EXPENSE" and job.get("status") == "OWNER_APPROVED"
            and job.get("owner_selected") is True, "Wrong first MVP task")
    north = p.get("north_star_job", {})
    require(north.get("id") == "B_SAFE_TO_SPEND"
            and north.get("ready_for_live_claim") is False
            and north.get("status") == "NOT_IMPLEMENTED"
            and len(north.get("requirements", [])) >= 4,
            "Real Safe-to-Spend cannot be claimed")

    t = p.get("demo_truth", {})
    require(t.get("currency") == "UZS", "Currency mismatch")
    require(t.get("record_count_before") == 5 and t.get("record_count_after") == 6,
            "Unexpected demo record count")
    require(t.get("income_before") == 3_000_000 and t.get("expense_before") == 259_000,
            "Demo source fixture changed")
    require(t.get("example_added_expense") == 100_000, "Unexpected scenario")
    require(t.get("net_before") == t["income_before"] - t["expense_before"], "Bad before net")
    require(t.get("turnover_before") == t["income_before"] + t["expense_before"],
            "Bad before turnover")
    require(t.get("income_after") == t["income_before"], "Expense must not alter income")
    require(t.get("expense_after") == t["expense_before"] + t["example_added_expense"],
            "Bad expense arithmetic")
    require(t.get("net_after") == t["income_after"] - t["expense_after"], "Bad after net")
    require(t.get("turnover_after") == t["income_after"] + t["expense_after"], "Bad after turnover")
    require(t.get("fixed_sample_balance") == 12_850_000, "Demo balance altered")
    require(t.get("fixed_sample_safe_to_spend") == 145_000, "Demo allowance altered")
    require(t.get("fixed_sample_monthly_expense") == 3_840_000, "Demo month graph altered")

    for name in ("S03-lowfi-wireframes.md", "S03-board-review.md", "S03-gate-checklist.md"):
        target = BASE / name
        require(target.is_file() and target.read_text(encoding="utf-8").strip(), f"Missing S03 deliverable: {name}")
    require("IN_PROGRESS" in (BASE / "S03-board-review.md").read_text(encoding="utf-8"),
            "S03 review must remain in progress")

    quality = p.get("quality", {})
    require(quality.get("visual_total_score") is None, "No complete design score")
    require(quality.get("user_study_status") == "NOT_CONDUCTED", "No measured user study")
    require(quality.get("native_accessibility_status") == "NOT_TESTED", "Native a11y not tested")
    require(quality.get("ui_release_status") == "NOT_APPROVED", "No UI release")
    for label, rel in p.get("artifacts", {}).items():
        require(isinstance(rel, str) and (ROOT / rel).is_file(), f"Missing artifact {label}: {rel}")


def check_graph(g: dict) -> None:
    require(g.get("project_id") == "hisobchi-ai" and g.get("stage") == "S02",
            "Wrong IA graph")
    require(g.get("stage_status") == "PASSED", "S02 spec gate must pass before S03")
    require(g.get("board_spec_gate_passed") is True, "No Board spec pass record")
    require(g.get("owner_navigation_approved") is False, "Owner has not separately approved exact topology")
    require(bool(g.get("board_gate_evidence")) and (ROOT / g["board_gate_evidence"]).is_file(),
            "Board evidence missing")
    require(g.get("owner_job") == "A_RECORD_EXPENSE", "Graph ignores Owner job")
    require(g.get("board_mode") == "SIMULATED_BOARD_REVIEW", "Incorrect board mode")
    require(g.get("navigation_approved") is False and g.get("production_ready") is False,
            "Graph cannot approve itself")
    require(g.get("data_mode") == "LOCAL_DEMO_SESSION", "No live banking data")
    screens = g.get("screens", [])
    names = [x["id"] for x in screens]
    require(len(names) >= 7 and len(names) == len(set(names)), "Duplicate/too few screens")
    require({"HOME", "HISTORY", "ANALYTICS", "PROFILE", "EDITOR_NEW",
             "EDITOR_EDIT", "DATE_PICKER", "DELETE_CONFIRM"} <= set(names),
            "Missing required screen")
    transitions = g.get("transitions", [])
    ids = [x["id"] for x in transitions]
    require(len(ids) >= 25 and len(ids) == len(set(ids)), "Duplicate/too few transitions")
    by_id = {x["id"]: x for x in transitions}
    for edge in transitions:
        require(edge["from"] in names and edge["to"] in names,
                f"Broken edge: {edge['id']}")
        for key in ("event", "guard", "effect", "recovery"):
            require(isinstance(edge.get(key), str) and edge[key].strip(),
                    f"Missing {key} in {edge['id']}")
    path = g.get("primary_path", [])
    require(len(path) >= 3, "Primary task must include Home, Save, Analytics")
    prior = "HOME"
    for edge_id in path:
        require(edge_id in by_id and by_id[edge_id]["from"] == prior,
                f"Broken primary path at {edge_id}")
        prior = by_id[edge_id]["to"]
    require(prior == "ANALYTICS", "Primary flow must reach Analytics after saving")

    # Follow possible transitions from HOME and verify every required screen is reachable.
    found = {"HOME"}
    queue = deque(["HOME"])
    while queue:
        current = queue.popleft()
        for edge in transitions:
            if edge["from"] == current and edge["to"] not in found:
                found.add(edge["to"])
                queue.append(edge["to"])
    require(set(names) <= found, "Unreachable screen: " + repr(set(names) - found))

    # Explicit cancel or safe recovery from all overlays and both new/edit routes.
    for screen in ("EDITOR_NEW", "EDITOR_EDIT", "DATE_PICKER", "DELETE_CONFIRM", "RESET_CONFIRM"):
        if screen in names:
            require(any(e["from"] == screen and ("cancel" in e["event"] or
                    e["event"] in ("confirm", "save_valid")) for e in transitions),
                    f"No recoverable exit: {screen}")
    require(any(e["from"] == "EDITOR_NEW" and e["to"] == "HOME" and
                e["event"] == "cancel_origin_home" for e in transitions),
            "New expense cannot cancel to Home")
    require(any(e["from"] == "EDITOR_NEW" and e["to"] == "HISTORY" and
                e["event"] == "cancel_origin_history" for e in transitions),
            "New expense cannot cancel to History")
    require(any(e["from"] == "DELETE_CONFIRM" and e["to"] == "EDITOR_EDIT" and
                e["event"] == "cancel" for e in transitions),
            "Delete cancel does not preserve row")
    for source, event, dest in (("DATE_PICKER", "cancel_for_new", "EDITOR_NEW"),
                                ("DATE_PICKER", "cancel_for_edit", "EDITOR_EDIT")):
        require(any(e["from"] == source and e["event"] == event and
                    e["to"] == dest for e in transitions),
                "Calendar cancel path missing")

    cancel = g.get("cancel_paths", [])
    require(all(x in by_id for x in cancel), "Unknown cancel transition")
    require(all("no mutation" in by_id[x]["effect"] or
                "unchanged" in by_id[x]["effect"] for x in cancel),
            "Cancel path mutated financial data")

    truth = g.get("data_invariants", {})
    b, a, change = truth["before"], truth["after"], truth["action"]
    require(truth.get("fixture_scope") == "ALL_SEEDED_TRANSACTIONS", "Wrong fixture scope")
    require(b["income"] == a["income"] == 3_000_000, "Income unexpectedly changed")
    require(b["expense"] == 259_000 and a["expense"] == b["expense"] + change["amount"],
            "Expense not reconciled")
    require(a["count"] == b["count"] + 1, "Incorrect session record count")
    require(b["net"] == b["income"] - b["expense"]
            and a["net"] == a["income"] - a["expense"], "Bad net")
    require(b["turnover"] == b["income"] + b["expense"]
            and a["turnover"] == a["income"] + a["expense"], "Bad turnover")
    require(truth["unchanged_samples"]["safe_to_spend_demo"] == 145_000, "False live allowance")
    require(truth["unchanged_samples"]["balance"] == 12_850_000, "Sample balance mismatch")
    q = g.get("quality", {})
    require(q.get("visual_score") is None and q.get("owner_visual_approval") is False,
            "Cannot score unrendered visual")
    require(q.get("ux_user_testing") == "NOT_CONDUCTED"
            and q.get("native_qa") == "NOT_TESTED"
            and q.get("safe_to_spend_real_engine") == "NOT_IMPLEMENTED",
            "Unverified QA or finance claim")


def check_matrix() -> int:
    with (BASE / "S02-state-matrix.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    require(len(rows) >= 28 and len({x["id"] for x in rows}) == len(rows),
            "State matrix missing rows or duplicate IDs")
    require(REQUIRED_CHECKS <= {x["check_id"] for x in rows},
            "Missing test coverage in state matrix")
    for row in rows:
        require(row["screen"] and row["state"] and row["required_observable"]
                and row["recovery_or_next"] and row["data_truth"], "Incomplete state row")
    return len(rows)


def negative_tests(p: dict, project: dict, stages: dict, g: dict) -> None:
    cases = [
        ("fake_owner", lambda v: v.update(owner_approved=False), "proposal"),
        ("skip_s02", lambda v: v.update(stage_S02="NOT_STARTED"), "proposal"),
        ("skip_s03", lambda v: v.update(stage_S03="PASSED"), "proposal"),
        ("fake_study", lambda v: v["target_user_segment"].update(status="FACT"), "proposal"),
        ("live_safe_spend", lambda v: v["north_star_job"].update(ready_for_live_claim=True), "proposal"),
        ("wrong_net", lambda v: v["demo_truth"].update(net_after=100), "proposal"),
        ("fake_visual_score", lambda v: v["quality"].update(visual_total_score=99), "proposal"),
        ("broken_route", lambda v: v["transitions"][0].update(to="MISSING"), "graph"),
        ("calendar_cancel_missing",
         lambda v: v.update(transitions=[t for t in v["transitions"]
                 if t["event"] != "cancel_for_edit"]), "graph"),
        ("mutation_on_cancel", lambda v: v["transitions"][2].update(effect="mutated records"), "graph")
    ]
    for name, mutate, which in cases:
        if which == "proposal":
            altered = copy.deepcopy(p)
            mutate(altered)
            func = lambda: stage_and_source(altered, project, stages)
        else:
            altered = copy.deepcopy(g)
            mutate(altered)
            func = lambda: check_graph(altered)
        try:
            func()
        except ValueError:
            continue
        raise AssertionError(f"Invalid fixture accepted: {name}")


def main() -> None:
    p = json.loads((BASE / "S01-decision-proposal.json").read_text(encoding="utf-8"))
    project = json.loads(PROJECT.read_text(encoding="utf-8"))
    stages = json.loads(STAGES.read_text(encoding="utf-8"))
    graph = json.loads((BASE / "S02-navigation.json").read_text(encoding="utf-8"))
    stage_and_source(p, project, stages)
    check_graph(graph)
    rows = check_matrix()
    negative_tests(p, project, stages, graph)
    print("PASS: scoped S00/S01 Owner approvals, S02 spec pass and S03 in-progress dependency integrity.")
    print(f"PASS: {len(graph['screens'])} screens, {len(graph['transitions'])} routes, {rows} state checks.")
    print("PASS: finance arithmetic/provenance and 10 deliberately invalid fixtures rejected.")
    print("NOT VERIFIED: real mobile UI, native QA, user studies, visual S+ or real Safe-to-Spend.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, AssertionError, KeyError, OSError, TypeError, csv.Error) as e:
        print("FAIL:", e, file=sys.stderr)
        sys.exit(1)
