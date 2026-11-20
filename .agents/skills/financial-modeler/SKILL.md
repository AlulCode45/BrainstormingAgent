---
name: financial-modeler
description: >-
  Use this skill when the user needs a real, testable financial model for a
  project or business: three scenarios, unit economics (CAC, LTV, margin),
  break-even, cash runway, and sensitivity analysis, computed by script rather
  than described in prose.
---

# Financial Modeler

Numbers must be computed, not narrated.

## Workflow

1. **Collect inputs** (ask for missing ones; label guesses as assumptions and add them to the Assumption Register): price, unit variable cost, monthly fixed costs, starting cash, monthly customers or units in the base case, growth rate, churn or repeat rate, CAC.
2. **Write inputs** to `prps/<project>/model/inputs.json` (see [example](./scripts/example_inputs.json)).
3. **Run the model**:
   `python3 .agents/skills/financial-modeler/scripts/model.py prps/<project>/model/inputs.json`
   It prints a Markdown report with three scenarios (pessimistic, base, optimistic), 12-month cash, break-even month, runway, LTV/CAC, and a sensitivity table. Save the output to `prps/<project>/11-financial-plan.md` (append under "Model Output").
4. **Interpret**: explain which input changes the outcome most, and what must be true for the project to be viable.
5. **Sanity checks**: gross margin plausible for the industry, LTV/CAC above 3 is healthy, runway at least 6 months, and no scenario relies on unverified numbers without saying so.
6. **Checkpoint**: ask whether to continue.
