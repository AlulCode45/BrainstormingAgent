---
name: prp-writer
description: >-
  Use this skill when discussing a software or technical project and the user
  wants a very detailed, clear, sequential, and thorough Project Requirements &
  Plan (PRP), complete with architecture, user flows, data models, milestones,
  and visual diagrams or charts.
---

# PRP Writer (Project Requirements & Plan)

Produce a crystal-clear, sequential, and comprehensive PRP document for a project, saved to `ideas/` (or the user's chosen path) when finalized.

## Workflow

1. **Ensure Context Is Complete**:
   - Before writing the full PRP, verify: problem statement, target users, core features, technical constraints/stack, and success criteria. Ask 2–4 targeted questions if critical gaps remain.
2. **Structure the PRP Sequentially & Thoroughly**:
   - **1. Executive Summary**: Project name, 1-paragraph vision, problem solved, and target users.
   - **2. Goals & Success Metrics**: Measurable objectives and non-goals (explicit out-of-scope).
   - **3. User Personas & User Flows**: Step-by-step journeys from entry to core outcome.
   - **4. Functional Requirements**: Detailed feature breakdown grouped by priority (**Must-Have / MVP**, **Should-Have**, **Nice-to-Have**), with acceptance criteria for each.
   - **5. Non-Functional Requirements**: Performance, security, scalability, reliability, and UX/accessibility constraints.
   - **6. System Architecture & Tech Stack**: Components, external integrations, API/service boundaries, and rationale.
   - **7. Data Model & Schema**: Core entities, relationships, and key fields.
   - **8. Implementation Roadmap & Task Breakdown**: Phased milestones (Phase 1 -> N) with concrete, ordered engineering tasks.
   - **9. Risks, Edge Cases & Mitigations**: Technical/product risks and fallback plans.
3. **Include Visual Diagrams & Illustrations**:
   - Use **Mermaid** diagrams directly in the Markdown for:
     - System Architecture (`flowchart TD` / `flowchart LR`)
     - User / Request Flows (`sequenceDiagram` or `flowchart`)
     - Database / Entity Relationships (`erDiagram`)
     - Project Timeline / Roadmap (`flowchart LR` or structured table)
   - When helpful for UI concepts, wireframes, or richer illustrations/charts, generate images into `ideas/assets/` and link them cleanly in the document.
4. **Save, Commit & Push**:
   - Save the PRP as `ideas/YYYY-MM-DD-prp-<project-slug>.md`, then commit and push to `origin`.
