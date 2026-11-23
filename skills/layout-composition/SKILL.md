---
name: layout-composition
description: Design responsive spacing, grid and focal hierarchy according to real user content and editorial composition.
---

# layout-composition — Design Intelligence OS v0.3

**Stage:** S03, S05, S07. **Mode:** supervised ChatGPT role workflow; not an autonomous agent.

## Objective
Design responsive spacing, grid and focal hierarchy according to real user content and editorial composition.

## Inputs
task, wireframe, real content/locale, approved visual target where available, viewport set.

## Procedure
1. Define reading order before choosing card family or decorative treatments.
2. Specify max/min width, alignments, spacing rhythm and dense/comfortable sections.
3. Validate primary CTA placement at 320/390px with long labels and bottom navigation.
4. Check fold behavior: below-fold content is allowed; no fixed-height obstruction or horizontal clipping.
5. Compare screenshots at identical content/device and preserve stronger parts of approved target.

## Outputs
grid specification, spacing tokens, responsive notes and visual screenshot issue list.

## Acceptance / Quality gate
No horizontal overflow on target screens, primary action remains operable and hierarchy matches approved wireframe.

## Sources and caution
https://github.com/primer/react ; https://github.com/carbon-design-system/carbon

Link and extract principles with source provenance; do not import external code/skill text or claim tests that have not run. Every Board use logs four role positions with documented dissent.
