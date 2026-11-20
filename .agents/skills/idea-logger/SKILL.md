---
name: idea-logger
description: >-
  Use this skill when the user wants to save, document, archive, or summarize a
  brainstorming session, decision, or idea into a structured Markdown file in
  the `ideas/` directory.
---

# Idea Logger

Persist brainstorming outcomes as clean, searchable Markdown files in `ideas/`.

## Workflow

1. **Determine Filename**:
   - Never save files directly in `ideas/`. Group every note in a topic folder: `ideas/<topic-slug>/YYYY-MM-DD-<note>.md` (lowercase, hyphenated, e.g., `ideas/saas-umkm-kasir/2026-11-21-validasi.md`).
   - Reuse the existing topic folder if the idea already has one; otherwise create it. Add an `assets/` subfolder inside it for images.
   - Check the folder first so existing files are not accidentally overwritten unless updating the same note.
2. **Use Structured Template**:
   ```markdown
   # <Idea / Topic Title>

   - **Date**: YYYY-MM-DD
   - **Category**: Project | Business | Task | Decision
   - **Status**: Exploring | Validating | Scoped | Parked

   ## Context & Goal
   <1–3 sentences summarizing what we are trying to solve>

   ## Key Ideas / Options Explored
   - **Option A**: ...
   - **Option B**: ...

   ## Risks & Open Questions
   - ...

   ## Decision & Next Steps
   - [ ] <Concrete next action>
   ```
3. **Commit & Push**:
   - After writing the file, stage, commit, and push the changes to `origin` as required by `AGENTS.md`.
