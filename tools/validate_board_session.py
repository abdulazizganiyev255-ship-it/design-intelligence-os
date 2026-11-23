#!/usr/bin/env python3
"""Validate MVP-02 board-session JSON structure (not actual UX or visual quality).

Runs with Python standard library; no keys, inference services, or network.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "mvp-02" / "sessions"
ROLES = {"ux_researcher", "creative_director", "design_architect", "critical_reviewer"}
BASIS = {"FACT", "HYPOTHESIS", "DESIGN_JUDGMENT", "UNKNOWN"}
MODES = {"SIMULATED_BOARD_REVIEW", "MULTI_AGENT_REVIEW", "HUMAN_BOARD_REVIEW"}
DECISIONS = {
    "PROPOSED", "NEEDS_EVIDENCE", "REVISE", "ACCEPTED_FOR_PROTOTYPE",
    "REJECTED", "APPROVED_BY_OWNER", "SUPERSEDED"
}
EVIDENCE_TYPES = {
    "OWNER_STATEMENT", "SOURCE_DOCUMENT", "SCREENSHOT", "INTERACTION_RECORD",
    "CODE", "TEST_LOG", "REFERENCE"
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def check_session(s: dict) -> None:
    for key in ("session_id", "date", "mode", "artifact_kind", "project_id"):
        require(nonempty_string(s.get(key)), f"Missing {key}")
    require(s["mode"] in MODES, "Unknown review mode")
    require(s["artifact_kind"] in ("BASELINE_AUDIT", "CONCEPT_REVIEW"), "Unknown artifact kind")
    require(s["session_id"].startswith("BOARD-"), "Invalid session_id")

    sources = s.get("source_documents")
    require(isinstance(sources, list) and sources, "Need real source_documents")
    for source in sources:
        require(nonempty_string(source), "Blank source path")
        require((ROOT / source).is_file(), f"Missing source document: {source}")

    evidence = s.get("evidence")
    require(isinstance(evidence, list), "evidence must be array")
    ids = set()
    for item in evidence:
        require(isinstance(item, dict), "Evidence item must be object")
        eid = item.get("id")
        require(nonempty_string(eid) and eid.startswith("E-"), "Bad evidence id")
        require(eid not in ids, f"Duplicate evidence id: {eid}")
        require(item.get("type") in EVIDENCE_TYPES, f"Bad evidence type: {eid}")
        require(nonempty_string(item.get("source")), f"Missing evidence source: {eid}")
        require(nonempty_string(item.get("supports")), f"Missing evidence scope: {eid}")
        ids.add(eid)

    unknowns = s.get("unknowns")
    require(isinstance(unknowns, list), "Missing unknowns list")
    require(set(s.get("roles", {})) == ROLES, "Exactly four required role perspectives")
    for name, role in s["roles"].items():
        require(role.get("basis") in BASIS, f"{name}: bad basis")
        for key in ("position", "risk", "proposed_action"):
            require(nonempty_string(role.get(key)), f"{name}: missing {key}")
        refs = role.get("evidence_ids")
        require(isinstance(refs, list), f"{name}: bad evidence_ids")
        require(all(x in ids for x in refs), f"{name}: unknown E-ID")
        if role["basis"] == "FACT":
            require(bool(refs), f"{name}: FACT without evidence")

    options = s.get("options")
    require(isinstance(options, list) and len(options) >= 2, "Need two real alternatives")
    require(len({o.get("id") for o in options}) == len(options), "Duplicate option id")
    differences = []
    for option in options:
        for key in ("id", "title", "structural_difference", "strength", "risk"):
            require(nonempty_string(option.get(key)), f"Bad option {key}")
        differences.append(option["structural_difference"].strip().lower())
    require(len(set(differences)) > 1, "Alternatives only restate the same structure")

    objections = s.get("objections")
    require(isinstance(objections, list) and len(objections) >= 2, "Need at least two substantive objections")
    for objection in objections:
        require(objection.get("from") in ROLES and objection.get("to") in ROLES, "Unknown objection role")
        require(objection["from"] != objection["to"], "Role cannot object to itself")
        require(nonempty_string(objection.get("issue")), "Missing objection issue")
        require(nonempty_string(objection.get("response")), "Missing objection response")
        require(type(objection.get("resolved")) is bool, "Objection resolution must be Boolean")

    dissent = s.get("dissent")
    require(isinstance(dissent, list) and dissent, "Record disagreement or explicit dissent resolution")
    require(all(nonempty_string(d) for d in dissent), "Empty dissent entry")

    decision = s.get("decision", {})
    require(decision.get("status") in DECISIONS, "Invalid decision status")
    require(type(decision.get("owner_approved")) is bool, "Owner approval must be explicit Boolean")
    for key in ("scope", "proposal", "rationale"):
        require(nonempty_string(decision.get(key)), f"Missing decision {key}")
    if decision["status"] == "APPROVED_BY_OWNER":
        require(decision["owner_approved"], "Owner approval required for approval status")
    if not decision["owner_approved"]:
        require(decision["status"] != "APPROVED_BY_OWNER", "No approval without owner")
    if s["mode"] == "SIMULATED_BOARD_REVIEW":
        require(decision["scope"] != "PRODUCTION_RELEASE", "Simulation cannot authorize release")

    quality = s.get("quality", {})
    require(quality.get("score_status") in ("UNSCORED", "SCORED"), "Bad score status")
    score = quality.get("total_score")
    if quality["score_status"] == "UNSCORED":
        require(score is None, "UNSCORED must have null total_score")
    else:
        require(type(score) in (float, int) and 0 <= score <= 100, "Bad total score")
        # Scores must be backed by a separate evidence scorecard; this script does NOT verify one.
        require(nonempty_string(s.get("scorecard_path")), "Scored session needs scorecard path")
        require((ROOT / s["scorecard_path"]).is_file(), "Missing scorecard file")
    require(quality.get("acceptance_test") in ("NOT_TESTED", "PASS", "FAIL"), "Bad acceptance_test")
    blockers = quality.get("open_p0_p1")
    require(isinstance(blockers, list), "Missing blocker list")
    if blockers:
        require(decision["scope"] != "PRODUCTION_RELEASE", "P0/P1 must block release")
    if quality["acceptance_test"] == "PASS":
        require(bool(s.get("test_results")), "PASS requires observed test results")

    validation = s.get("validation_plan")
    require(isinstance(validation, list) and validation, "Missing validation plan")
    require(all(nonempty_string(v) for v in validation), "Empty validation step")
    require(s.get("learning_state") in ("REVIEW_PENDING", "VALIDATED_PATTERN"), "Bad learning status")
    if s["mode"] == "SIMULATED_BOARD_REVIEW":
        require(s["learning_state"] != "VALIDATED_PATTERN", "Simulation cannot itself validate a learned pattern")


def self_test(base: dict) -> None:
    check_session(base)
    changes = [
        lambda s: s["roles"].pop("critical_reviewer"),
        lambda s: s["quality"].update(total_score=93),
        lambda s: s["decision"].update(status="APPROVED_BY_OWNER"),
        lambda s: s.update(learning_state="VALIDATED_PATTERN"),
        lambda s: s["roles"]["ux_researcher"].update(evidence_ids=["E-FICTIONAL"]),
        lambda s: s["quality"].update(acceptance_test="PASS"),
        lambda s: s["options"][1].update(structural_difference=s["options"][0]["structural_difference"]),
    ]
    for i, mutate in enumerate(changes, 1):
        test = copy.deepcopy(base)
        mutate(test)
        try:
            check_session(test)
        except ValueError:
            continue
        raise AssertionError(f"Negative fixture {i} was incorrectly accepted")


def main() -> None:
    files = sorted(SESSIONS.glob("BOARD-*.json"))
    require(bool(files), "No session fixture found")
    for path in files:
        session = json.loads(path.read_text(encoding="utf-8"))
        check_session(session)
        require(path.stem == session["session_id"], f"Session ID/path mismatch: {path}")
        require((SESSIONS / (path.stem + ".md")).is_file(), f"Missing human-readable session: {path}")
        if path.name == "BOARD-002.json":
            self_test(session)
        print(f"PASS: {path.name} (structural only)")
    print(f"PASS: {len(files)} session(s); negative fixtures checked.")
    print("NOT VERIFIED: independent AI agents, UI visuals, task success, accessibility, S+ approval.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, OSError, KeyError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
