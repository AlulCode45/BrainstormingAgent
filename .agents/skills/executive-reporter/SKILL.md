---
name: executive-reporter
description: >-
  Use this skill to turn a finished or in-progress PRP into decision-ready
  output: a one-page executive summary, decision memo, consistent charts, and
  an exportable report or pitch outline for investors, mentors, or partners.
---

# Executive Reporter

Busy readers need the answer first.

## Workflow

1. **Read** the whole `prps/<project>/` folder. Do not invent anything not in it; flag gaps instead.
2. **Executive summary** (max one page) at `prps/<project>/18-executive-summary.md` from [the template](../../../templates/executive-summary.md): recommendation, problem, solution, market, evidence quality, economics, top risks, ask and next steps.
3. **Charts** (Mermaid in Markdown, or images saved in `assets/`): market funnel (TAM/SAM/SOM), scenario cash curves from the model, risk heat map, roadmap. Use the same labels and units everywhere.
4. **Consistency check**: numbers in the summary match the detailed files; every number carries its label (Verified, Estimate, Assumption).
5. **Export** (on request): pitch deck outline (10-12 slides) or a PDF/HTML via available tools; save under `prps/<project>/assets/`.
6. **Update** `prps/INDEX.md` status and the project `CHANGELOG.md`.
