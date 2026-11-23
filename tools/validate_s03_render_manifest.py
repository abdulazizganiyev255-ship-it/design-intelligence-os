#!/usr/bin/env python3
"""Audit S03 source/manifest integrity. Does not run Chromium or real UX tests."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"operating-system/projects/hisobchi-ai"
DOC=BASE/"S03-browser-qa.json"
PROJECT=ROOT/"operating-system/projects/hisobchi-ai.json"
SCREENS=("home","editor","history","analytics")
STATES=(("home","default"),("editor","default"),("history","default"),
        ("analytics","default"),("editor","error"),("history","empty"),
        ("analytics","empty"))
SIZES=((320,640),(390,844))

def require(test:bool, message:str)->None:
    if not test: raise ValueError(message)

def validate(d:dict,p:dict)->None:
    require(d.get("project_id")=="hisobchi-ai" and d.get("stage")=="S03","Wrong project/stage")
    require(d.get("stage_status")=="IN_PROGRESS" and p.get("workflow_stage")=="S03","S03 not in progress")
    require(p["stage_status"]["S02"]=="PASSED" and p["stage_status"]["S03"]=="IN_PROGRESS",
            "Invalid stage progression")
    require(all(p["stage_status"][f"S{i:02}"]=="NOT_STARTED" for i in range(4,13)),
            "S04+ must not start without S03 pass")
    require(d.get("owner_visual_approval") is False and d.get("quality_total_score") is None,
            "No unsupported visual approval/score")
    relative=d.get("artifacts_source")
    require(relative=="operating-system/projects/hisobchi-ai/S03-wireframe-render.html",
            "Unexpected render source")
    html=(ROOT/relative).read_bytes()
    require(hashlib.sha256(html).hexdigest()==d.get("source_sha256"),"Wireframe HTML differs from captured source")
    text=html.decode("utf-8")
    for name in SCREENS:
        require(f"const {name}=" in text, f"Missing screen {name}")
    for term in ("2 741 000 so‘m","259 000 so‘m","3 000 000 so‘m",
                 "DEMO","Xarajat qo‘shish","Mos operatsiya topilmadi"):
        require(term in text, f"Missing truthful content: {term}")
    require("145 000" not in text and "92/100" not in text,
            "Unsupported budget or quality score in UI")
    expected={f"{screen}_{state}_{w}x{h}.png" for w,h in SIZES for screen,state in STATES}
    cases=d.get("cases",[])
    require(len(cases)==14 and {c.get("file") for c in cases}==expected,
            "Expected exactly 14 unique cases")
    for case in cases:
        require(case.get("viewport_css") in ([320,640],[390,844]),"Unknown viewport")
        w,h=case["viewport_css"]
        require(case.get("png_pixels")==[w*2,h*2],"Bad DPR=2 screenshot size")
        require(case.get("horizontal_overflow") is False,"Reported horizontal overflow")
        require(case.get("geometry_assertions")=="PASS","Missing observed geometry check")
        require(case.get("runtime_task_test")=="NOT_TESTED","Must not invent runtime task pass")
    totals=d.get("totals",{})
    require(totals.get("pass")==14 and totals.get("fail")==0,
            "Manifest must reflect inspected 14 geometry screenshots")
    require(d.get("board_decision","").startswith("S03 REVISE_TARGETED"),
            "Do not auto-pass S03 from geometry-only checks")
    require(len(d.get("limitations",[]))>=5,"Missing limitations")

def main()->None:
    report=json.loads(DOC.read_text(encoding="utf-8"))
    project=json.loads(PROJECT.read_text(encoding="utf-8"))
    validate(report,project)
    invalid=[
        lambda x:x.update(source_sha256="0"*64),
        lambda x:x.update(stage_status="PASSED"),
        lambda x:x.update(owner_visual_approval=True),
        lambda x:x["cases"][0].update(geometry_assertions="FAIL"),
        lambda x:x["cases"][0].update(runtime_task_test="PASS"),
    ]
    for i,mutate in enumerate(invalid,1):
        bad=copy.deepcopy(report);mutate(bad)
        try: validate(bad,project)
        except ValueError: continue
        raise AssertionError(f"Invalid fixture {i} accepted")
    print("PASS: S03 exact HTML source digest, 14 case manifest, honesty and stage integrity.")
    print("PASS: 5 deliberate bad fixtures rejected.")
    print("NOT VERIFIED: screenshots independently reproduced by this script, touch UX, native accessibility, S+.")

if __name__=="__main__":
    try: main()
    except (ValueError,AssertionError,OSError,KeyError,TypeError,UnicodeError) as exc:
        print("FAIL:",exc,file=sys.stderr);sys.exit(1)
