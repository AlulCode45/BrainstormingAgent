---
name: decision-scorecard
description: >-
  Use this skill when the user must decide between go, no-go, pivot, or choose
  among several ideas: weighted Go/No-Go scorecard, portfolio comparison
  matrix, automatic red-team review, and Decision Log (ADR) entries.
---

# Decision Scorecard

Make decisions auditable.

## Workflow

1. **Red-team first**: apply the `devils-advocate` method to the current analysis (assumptions, pre-mortem, top risks) before scoring.
2. **Score** using [the template](../../../templates/scorecard.md). Default criteria and weights (adjust with the user, weights sum to 100): Market demand 20, Evidence quality 15, Unit economics 20, Feasibility 15, Competitive edge 10, Risk and compliance 10, Founder fit 10. Score each 1-5 with a one-line justification linked to a PRP file.
3. **Verdict**: 4.0 and above = Go, 3.0-3.9 = Go with conditions (list them), below 3.0 = No-Go or Pivot. State what evidence would change the verdict.
4. **Compare ideas** (when several): one matrix, same criteria, ranked, with a sensitivity note (does the ranking change if weights shift 10 points?). Save to `ideas/<topic>/` or `prps/INDEX.md`.
5. **Log the decision** in `prps/<project>/decisions/ADR-NNN-<slug>.md` using [the ADR template](../../../templates/decision-log-adr.md), and save the scorecard as `prps/<project>/17-scorecard-and-decision.md`.
6. **Checkpoint**: ask the user to confirm the decision before proceeding.
