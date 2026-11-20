---
name: strategy-analyst
description: >-
  Use this skill when the user wants strategic analysis of a project or
  business: SWOT, opportunities and threats, PESTEL, Porter's Five Forces,
  management and operations planning, team, finance and unit economics, and
  go-to-market, ideally built on market research findings.
---

# Strategy Analyst

Run the analysis in stages. Each stage ends with a checkpoint question; never start the next stage without the user's approval.

## Stages

1. **SWOT** -> `08-swot.md`
   - Strengths, Weaknesses (internal); Opportunities, Threats (external).
   - Tie each point to evidence from `07-market-research.md`. Add a TOWS matrix (strategies from SO, WO, ST, WT).
2. **Opportunity & Environment** -> `09-opportunity-analysis.md`
   - Ranked opportunities (impact vs effort), PESTEL, Porter's Five Forces, differentiation and positioning.
3. **Management & Operations** -> `10-management-plan.md`
   - Team and roles, key hires, operations and processes, tools, partnerships, governance, KPIs/OKRs.
4. **Finance & Unit Economics** -> `11-financial-plan.md`
   - Cost structure, pricing, revenue projections (stated assumptions, 3 scenarios), break-even, funding needs.
5. **Go-to-Market & Risk** -> `12-go-to-market-and-risk.md`
   - Channels, launch plan, first 90 days, risk register with likelihood, impact, and mitigation.

## Rules

- If market research is missing, offer to run `market-researcher` first.
- Use tables and Mermaid charts (e.g., quadrant or flow) for clarity.
- Separate facts from assumptions; flag every assumption explicitly.
- Save files in `prps/<project>/` and link them from that folder's `README.md`.
- **Checkpoint after each stage**: summarize in 3–5 bullets, then ask "Lanjut ke tahap berikutnya: <nama tahap>?" with the options: lanjut, revisi tahap ini, atau berhenti.
