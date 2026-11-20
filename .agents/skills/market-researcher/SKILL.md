---
name: market-researcher
description: >-
  Use this skill when the user wants market research for a project, product, or
  business idea: market size, trends, target customers, competitors, pricing
  benchmarks, and demand signals, using live web/browser research with sources.
---

# Market Researcher

Research the market with live sources. The agent is explicitly allowed to use web research tools: `search_web` for quick lookups, the browser subagent for interactive or JS-rendered pages, and the lightpanda MCP tools for page extraction.

## Workflow

1. **Scope the Research**: Confirm industry, geography (default: Indonesia unless told otherwise), target segment, and the decision this research supports.
2. **Research These Areas** (cite every claim with a URL and access date):
   - **Market size & growth**: TAM / SAM / SOM with the assumptions behind each number.
   - **Trends & demand signals**: search interest, news, regulation, community discussions.
   - **Target customers**: segments, pain points, buying behavior, willingness to pay.
   - **Competitors** (3–7 direct and indirect): offering, pricing, strengths, weaknesses, reviews.
   - **Pricing benchmarks** and common business models.
3. **Be Honest About Evidence**: Label each finding as `Verified` (primary or reputable source), `Estimate` (derived), or `Unverified`. Never invent figures. If data is not found, say so.
4. **Save the Result**: Write to `prps/<project>/07-market-research.md` (or `ideas/` if no PRP exists yet), with a competitor comparison table, a Mermaid chart where useful, and a `Sources` section.
5. **Checkpoint**: Summarize the top 3 findings and ask the user: "Lanjut ke tahap berikutnya (Analisa SWOT & Strategi)?" Do not continue until the user agrees.
