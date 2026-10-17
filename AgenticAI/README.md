# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-17 Daily Scan

### Gate computer-use escalation with observed uncertainty

Summary: Weak-to-strong routing should react to task and step uncertainty, then keep lightweight oversight active after handoff.

Analysis: [gate computer-use escalation with observed uncertainty](2026-10-17/reasoning.md#gate-computer-use-escalation-with-observed-uncertainty)

Core source: [LEASH paper v1](https://arxiv.org/abs/2610.22280v1)

Implementable now:
- retain labeled success and failure trajectories;
- score task and action uncertainty;
- compare against random and always-strong baselines;
- preserve post-handoff observation.

Implementability score: 0.67

### Treat code quality as inference cost control

Summary: A pre-registered study links higher maintainability scores to lower multi-agent review token cost across three LLMs.

Analysis: [treat code quality as inference cost control](2026-10-17/reasoning.md#treat-code-quality-as-inference-cost-control)

Core sources: [paper v1](https://arxiv.org/abs/2610.21914v1), [replication package](https://doi.org/10.5281/zenodo.22127920)

Implementable now:
- record tokens by review stage;
- measure deterministic maintainability and file size;
- stratify by repository and language;
- compare refactoring against a no-change control.

Implementability score: 0.90

### Build anticipatory workspaces with source fallback

Summary: Reorganize high-reuse corpora into derived files and indexes before queries arrive, while preserving links to canonical evidence.

Analysis: [build anticipatory workspaces with source fallback](2026-10-17/reasoning.md#build-anticipatory-workspaces-with-source-fallback)

Core sources: [paper v1](https://arxiv.org/abs/2610.22273v1), [project page](https://librarian-agents.github.io/), [repository](https://github.com/teresaz05/librarian-agents)

Implementable now:
- build source-linked timelines and indexes;
- keep raw documents canonical;
- measure construction cost against repeated-query savings;
- invalidate derived files when sources change.

Implementability score: 0.61

## Current implication

Measure the runtime condition that causes failure or cost, then turn it into an explicit gate. Confidence text and successful final answers are weak substitutes for trajectory, token, and source-state evidence.
