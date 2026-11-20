---
name: prp-writer
description: >-
  Use this skill when discussing a software or technical project and the user
  wants a very detailed, clear, sequential, and thorough Project Requirements &
  Plan (PRP), complete with architecture, user flows, data models, milestones,
  and visual diagrams or charts stored in a structured project folder.
---

# PRP Writer (Project Requirements & Plan)

Produce a crystal-clear, sequential, and comprehensive PRP organized inside a dedicated folder under `prps/` so it is easy to read, navigate, and analyze.

## Folder Structure

Save every project PRP in its own folder:
`prps/YYYY-MM-DD-<project-slug>/`

```text
prps/YYYY-MM-DD-<project-slug>/
├── README.md                    # Index / Table of Contents + Quick Summary
├── 00-overview.md               # Executive Summary, Goals, Metrics & Non-Goals
├── 01-users-and-flows.md        # User Personas, Journeys & User Flow Diagrams
├── 02-requirements.md           # Functional (MoSCoW + Acceptance Criteria) & Non-Functional
├── 03-architecture.md           # System Architecture, Tech Stack & Sequence Diagrams
├── 04-data-model.md             # Data Model, ERD & Schema Definitions
├── 05-roadmap-and-tasks.md      # Phased Milestones & Actionable Task Breakdown
├── 06-risks-and-mitigation.md   # Risks, Edge Cases & Mitigation Plans
├── 07-market-research.md        # (market-researcher) Market, competitors, sources
├── 08-swot.md                   # (strategy-analyst) SWOT + TOWS
├── 09-opportunity-analysis.md   # (strategy-analyst) Opportunities, PESTEL, Five Forces
├── 10-management-plan.md        # (strategy-analyst) Team, operations, KPIs
├── 11-financial-plan.md         # (strategy-analyst) Costs, pricing, projections
├── 12-go-to-market-and-risk.md  # (strategy-analyst) Launch plan & risk register
├── 13-assumption-register.md    # (evidence-auditor) Assumptions, confidence, tests
├── 14-customer-discovery.md     # (customer-discovery) Interviews, JTBD, personas
├── 15-competitor-analysis.md    # (competitor-analyst) Matrix, review mining, ERRC
├── 16-compliance-and-legal.md   # (compliance-checker) Permits, tax, IP, data
├── 17-scorecard-and-decision.md # (decision-scorecard) Go/No-Go verdict
├── 18-executive-summary.md      # (executive-reporter) One-page summary
├── CHANGELOG.md                 # Version history (see templates/changelog.md)
├── decisions/                   # ADR-NNN-<slug>.md decision records
├── model/                       # inputs.json for financial-modeler
└── assets/                      # Generated illustrations, UI mockups, or charts
```

## Workflow

1. **Ensure Context Is Complete**:
   - Before writing the PRP, verify: problem statement, target users, core features, technical constraints/stack, and success criteria. Ask 2–4 targeted questions if critical gaps remain.
2. **Write Each Section Clearly & Sequentially**:
   - Keep each numbered file focused, well-formatted (tables, checklists, clear headings), and cross-linked from `README.md`.
   - Use **Mermaid** diagrams directly inside the relevant Markdown files (User Flows in `01`, System Architecture & Sequence Diagrams in `03`, ERD in `04`, Roadmap/Timeline in `05`).
   - When visual illustrations, charts, or UI mockups help clarify the concept, generate and save them inside `assets/` and embed them in the corresponding section.
3. **Commit & Push**:
   - After creating or updating the PRP folder, stage, commit, and push all files to `origin`.
