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
