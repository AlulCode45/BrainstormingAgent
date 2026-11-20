---
name: evidence-auditor
description: >-
  Use this skill to audit the quality of evidence behind any analysis: build and
  maintain the Assumption Register, score sources, separate facts from
  assumptions, and flag stale research. Use before trusting or presenting
  market research, financials, or strategy conclusions.
---

# Evidence Auditor

Make every claim traceable and testable.

## Source Scoring (apply to each cited source)

| Score | Meaning |
|---|---|
| A | Primary or official (government, filings, company data, own interviews) |
| B | Reputable secondary (established media, industry bodies, research firms) |
| C | Weak or biased (blogs, vendor marketing, forums, undated pages) |

Require at least 2 independent sources (A or B) for any number that drives a decision. A single C-only claim is `Unverified`.

## Workflow

1. **Extract** every number and key claim from the target documents.
2. **Label** each as `Verified` (2+ A/B sources), `Estimate` (derived, show formula), `Assumption` (no evidence), or `Unverified`.
3. **Maintain the Assumption Register** at `prps/<project>/13-assumption-register.md` using [the template](../../../templates/assumption-register.md). Each assumption has: ID, statement, confidence (High/Med/Low), impact if wrong, test method, owner, status.
4. **Flag staleness**: note the research date; mark data older than 12 months (6 months for fast-moving markets) as `Stale` and recommend a refresh.
5. **Report**: top 5 riskiest assumptions (low confidence x high impact) with the cheapest test for each.
6. **Checkpoint**: ask the user whether to continue to the next stage.
