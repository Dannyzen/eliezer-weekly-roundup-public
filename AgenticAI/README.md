# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-06

### Skill use needs progressive disclosure scores

Summary: Skill-Use grades trigger, compliance, and boundary separately when an agent sees only a skill name and short description before retrieving the full procedure. It covers 79 real skills and 177 sandbox tasks.

Analysis: [daily analysis](2026-08-06/reasoning.md#skill-use-separates-trigger-compliance-and-boundary-under-progressive-disclosure)
Core sources: [paper](https://arxiv.org/abs/2608.04828v1), [repo](https://github.com/JinyiHan99/Skill-Use-Bench)
Implementable now:
- score skill runs on trigger, compliance, and boundary;
- require explicit skill retrieval before full procedure injection;
- keep trajectory rubrics with skill identity and hash.
Tools and repositories:
- Skill-Use-Bench, Docker sandbox fixtures, progressive disclosure loaders, Hermes skill catalogs
Implementability score: 0.76

### Canary tools diagnose tool-selection failure modes

Summary: Canary Tools plants six trap types into MCP-style catalogs and turns wrong-tool outcomes into susceptibility profiles across 8,640 runs.

Analysis: [daily analysis](2026-08-06/reasoning.md#canary-tools-turn-wrong-tool-outcomes-into-a-failure-taxonomy)
Core source: [paper](https://arxiv.org/abs/2608.04719v1)
Implementable now:
- generate schema-derived canaries beside real tools;
- log canary type with selected tool and task success;
- block catalog promotion when susceptibility exceeds budget.
Tools and methodologies:
- MCP registries, decoy generators, gateway allowlists, trajectory labels
Implementability score: 0.60

### SuperScout routes after scout verification

Summary: SuperScout scouts a repository with a 7B searcher, strips failed reproduction claims, then routes among frontier fixers. On SWE-bench Pro Python-266 it matches the best solo solve rate at about one fifth the matched cost per solve.

Analysis: [daily analysis](2026-08-06/reasoning.md#superscout-routes-coding-agents-only-after-scouting-and-stripping-false-claims)
Core sources: [paper](https://arxiv.org/abs/2608.04804v1), [repo](https://github.com/TransformerOptimus/superscout), [model](https://huggingface.co/SuperAGI/SuperScout-7B)
Implementable now:
- scout before model selection;
- sandbox-verify handoff claims;
- keep paired solo and routed cost or solve receipts.
Tools and repositories:
- SuperScout, verify-then-strip gates, frozen routers, SWE-bench receipts
Implementability score: 0.80

## Current implication

Names are leads, not authority. Skill catalogs, tool descriptions, and issue text should unlock work only after retrieval, traps, or verified local scout evidence make the next action defensible.
