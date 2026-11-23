#!/usr/bin/env python3
"""Design Intelligence OS v0.3 structural checks: no AI/API/browser involved.

This checks documentation, dependency order, source registry, skills and
example project state. It DOES NOT check visual taste, live UX, security,
licensing eligibility or independent agent operation.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"ux-researcher", "creative-director", "design-architect", "critical-reviewer"}
STAGE_STATUSES = {"NOT_STARTED", "IN_PROGRESS", "NEEDS_EVIDENCE", "REVISE", "PASSED", "BLOCKED"}
NEW_SKILLS = [
    "ux-psychology", "information-architecture", "wireframing", "taste-critique",
    "typography-system", "color-system", "layout-composition", "design-tokens",
    "component-contract", "interaction-motion", "frontend-implementation",
    "accessibility-qa", "visual-regression", "knowledge-curation"
]
REQUIRED = [
    "operating-system/README.md", "operating-system/stages.json",
    "operating-system/projects/hisobchi-ai.json",
    "operating-system/projects/hisobchi-ai-stage-S00-review.md",
    "operating-system/board-stage-contract.md", "operating-system/stage-questions.md",
    "operating-system/templates/stage-review.md", "operating-system/audit-v2.md",
    "operating-system/efficiency-dashboard.md", "operating-system/launch-prompt.md",
    "design-system/README.md", "design-system/foundations.md",
    "design-system/component-contract.md", "design-system/component-inventory.csv",
    "design-system/tokens/example.tokens.json",
    "knowledge/source-registry.csv", "knowledge/research-policy.md",
    "knowledge/upstream-audits.md", "knowledge/ux-psychology-checklist.md",
    "knowledge/pattern-record.template.md",
    ".github/workflows/validate-design-os.yml",
    "tools/validate_operating_system.py"
]


def require(condition: object, detail: str) -> None:
    if not condition:
        raise ValueError(detail)


def inspect_stages(data: dict) -> list[str]:
    stages = data.get("stages", [])
    require(data.get("mode") == "CHATGPT_SIMULATED_BOARD", "Do not claim independent agents")
    require(len(stages) == data.get("stage_count") == 13, "Expected exactly 13 stages")
    ids = []
    for index, stage in enumerate(stages):
        stage_id = f"S{index:02}"
        require(stage.get("id") == stage_id and stage.get("order") == index, f"Bad order: {stage}")
        require(set(stage.get("board_review", [])) == ROLES, f"{stage_id}: missing Board perspectives")
        require(stage.get("review_required") is True, f"{stage_id}: Board review required")
        require(stage.get("lead") in ROLES, f"{stage_id}: unknown lead")
        require(type(stage.get("owner_gate")) is bool, f"{stage_id}: invalid owner gate")
        for key in ("name", "gate"):
            require(isinstance(stage.get(key), str) and stage[key].strip(), f"{stage_id}: empty {key}")
        for key in ("inputs", "outputs", "skills"):
            require(isinstance(stage.get(key), list) and stage[key], f"{stage_id}: empty {key}")
        required_deps = [] if index == 0 else [ids[-1]]
        require(stage.get("depends_on") == required_deps, f"{stage_id}: invalid dependency")
        for skill in stage["skills"]:
            require((ROOT / "skills" / skill / "SKILL.md").is_file(), f"{stage_id}: missing skill {skill}")
        ids.append(stage_id)
    return ids


def inspect_skills() -> None:
    for name in NEW_SKILLS:
        skill_path = ROOT / "skills" / name / "SKILL.md"
        require(skill_path.is_file(), f"Missing skill: {name}")
        data = skill_path.read_text(encoding="utf-8")
        require(data.startswith("---\n") and data.count("---") >= 2, f"Broken frontmatter: {name}")
        require(f"name: {name}\n" in data, f"Wrong name: {name}")
        require("description:" in data and "## Inputs" in data and "## Outputs" in data, f"Incomplete skill: {name}")
        require("## Acceptance" in data and "## Procedure" in data, f"No testable procedure: {name}")
        require("not an autonomous agent" in data, f"Missing scope disclosure: {name}")


def inspect_sources(valid_ids: list[str]) -> int:
    file_path = ROOT / "knowledge/source-registry.csv"
    with file_path.open(encoding="utf-8", newline="") as fh:
        sources = list(csv.DictReader(fh))
    require(len(sources) >= 18, "Insufficient source catalog coverage")
    require(len({x["id"] for x in sources}) == len(sources), "Duplicate source ID")
    require(len({x["url"] for x in sources}) == len(sources), "Duplicate source URL")
    for x in sources:
        require(x["url"].startswith("https://"), f"Non-https source: {x['id']}")
        require(x["review_status"], f"Source needs honest review scope: {x['id']}")
        require(x["license_policy"] == "CHECK_LICENSE_AND_PIN_VERSION_BEFORE_CODE_COPY", f"License guard missing: {x['id']}")
        for stage in x["stages"].split("/"):
            require(stage in valid_ids, f"Unknown source stage: {x['id']} {stage}")
    taste = next((x for x in sources if "taste-skill" in x["source"]), None)
    require(taste is not None and taste["classification"] == "ADAPT_ONLY", "Website taste skill must not be installed blindly")
    require("NOT dashboards" in taste["caution"], "Must flag taste-skill dashboard mismatch")
    return len(sources)


def inspect_components(valid_ids: list[str]) -> int:
    with (ROOT / "design-system/component-inventory.csv").open(encoding="utf-8", newline="") as fh:
        items = list(csv.DictReader(fh))
    require(len(items) >= 25, "Component inventory too small")
    ids = {row["id"] for row in items}
    require(len(ids) == len(items), "Duplicate component IDs")
    for item in items:
        require(item["stage"] in valid_ids, f"Bad component stage {item['id']}")
        require(item["required_states"], f"Missing states {item['id']}")
        for dep in item["depends_on"].split("/"):
            require(dep in ids or dep in valid_ids, f"Missing component dependency {item['id']} -> {dep}")
    return len(items)


def inspect_project(valid_ids: list[str]) -> None:
    project = json.loads((ROOT / "operating-system/projects/hisobchi-ai.json").read_text(encoding="utf-8"))
    require(project["workflow_stage"] in valid_ids, "Unknown active stage")
    statuses = project.get("stage_status", {})
    require(set(statuses) == set(valid_ids), "Project must explicitly track every stage")
    require(all(x in STAGE_STATUSES for x in statuses.values()), "Unknown project stage status")
    require(statuses[project["workflow_stage"]] in {"IN_PROGRESS", "NEEDS_EVIDENCE", "REVISE", "BLOCKED"}, "Current stage cannot be a claimed final success without proof")
    require(project["visual_target_approved"] is False, "Do not infer owner visual selection")
    require(project["production_release_approved"] is False, "No production approval")
    require(project["visual_score"] is None, "Missing evidence must be UNSCORED")
    require((ROOT / project["latest_baseline"]).is_file(), "Referenced actual baseline missing")


def inspect_example_tokens() -> None:
    path = ROOT / "design-system/tokens/example.tokens.json"
    tokens = json.loads(path.read_text(encoding="utf-8"))
    meta = tokens.get("$extensions", {}).get("design-intelligence-os", {})
    require(meta.get("status") == "EXAMPLE_NOT_APPROVED", "Example must not be mistaken for approved design")
    for group in ("color", "space"):
        for name, token in tokens[group].items():
            require("$type" in token and "$value" in token, f"Bad token sample: {group}.{name}")


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    require(not missing, "Missing documents: " + ", ".join(missing))
    require(all((ROOT / p).read_text(encoding="utf-8").strip() for p in REQUIRED), "One required file is empty")
    data = json.loads((ROOT / "operating-system/stages.json").read_text(encoding="utf-8"))
    valid_ids = inspect_stages(data)
    inspect_skills()
    source_count = inspect_sources(valid_ids)
    component_count = inspect_components(valid_ids)
    inspect_project(valid_ids)
    inspect_example_tokens()

    # Deliberately wrong dependency must fail: prevention of stage-skipping.
    altered = json.loads(json.dumps(data))
    altered["stages"][4]["depends_on"] = ["S07"]
    try:
        inspect_stages(altered)
    except ValueError:
        pass
    else:
        raise AssertionError("Dependency-cycle negative fixture was wrongly accepted")

    print(f"PASS: {len(valid_ids)} ordered stages, {len(NEW_SKILLS)} new skills, {component_count} components, {source_count} sources.")
    print("PASS: Four Board perspectives and owner gates specified; stage dependency negative fixture rejected.")
    print("NOT VERIFIED: real agent autonomy, visual taste, UI runtime, real RAG retrieval, external license rights, user study, S+.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, AssertionError, KeyError, OSError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
