# Board checkpoint questions — all 13 stages

At each stage ask all four **simulated perspectives** (UX, Creative, Architect, Reviewer) to answer the stage-specific question in addition to the general contract. Provide evidence IDs/UNKNOWN, risk, readiness 0–5/null and actionable correction for each. Rating is *readiness* not scientific visual quality.

| Stage | UX Researcher | Creative Director | Design Architect | Critical Reviewer | Hard gate |
|---|---|---|---|---|---|
| S00 Baseline | What task is unknown? | What exactly was rejected? | What existing behavior must be preserved? | What is observed vs assumed? | Honest evidence scope |
| S01 Strategy | Who and why? | What product personality fits the job? | Any constraints? | Which claims lack data? | Owner approves task |
| S02 IA | Can user locate and recover? | Is grouping meaningful? | Complete states? | Missing branches? | End-to-end flow |
| S03 Wireframe | CTA and info clear unstyled? | Does composition hold in grayscale? | Reflow/content? | What remains untestable? | Hierarchy locked |
| S04 Art direction | Does aesthetic serve core task? | Distinctiveness of A vs B? | Can both scale? | Fake quality numbers? | Owner selects/rejects visual |
| S05 Foundations | Contrast/readability/semantic copy? | Type/color coherent to brand? | Valid tokens/modes? | Contrast/locale evidence? | Semantic system approved |
| S06 Components | Actions/error recovery intuitive? | Component family consistent? | All states/props covered? | No dead controls? | Component contract complete |
| S07 Screen design | Is task findable across screens? | Does rendered craft match target? | 320/390 states and content? | Overlap/clip/source truth? | Owner visual checkpoint |
| S08 Prototype | Real task steps and recovery? | Motion serves meaning? | Events/state persistence? | Test logs or guesses? | Observed task check |
| S09 Implementation | No flow regression? | Fidelity to approved visual? | Build/tests/data contract? | Unsafe code claims? | Implementation PR verified |
| S10 QA | Actual task success? | Actual rendered polish? | A11y/native/device evidence? | P0/P1 and full rubric? | 100-point score or UNSCORED |
| S11 Release | Clear user promise? | Brand consistency? | Rollback/security? | Scope/approvals recorded? | Human owner and hard gates |
| S12 Learning | Does lesson help future user? | What design rule generalized? | How indexed with version? | Could it be false outside context? | Only verified knowledge |

### Blocking escalation

When evidence unavailable, do not replace it with invented scores. Stage can be `NEEDS_EVIDENCE`; owner gives actual task/screenshot. Two revisions with no progress → reopen earliest wrong assumption rather than color adjustments. Strong Creative–UX disagreements require concrete alternative and user test; consensus by model role-play alone doesn't count as external proof.
