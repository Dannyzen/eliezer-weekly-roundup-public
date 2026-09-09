# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-09

### Independent tests must be frozen before repair

Summary: ExecCritic separates behavior-test construction from source repair, qualifies each test bundle in a fail-closed harness, and prevents the Repair agent from changing the test. Poor generated tests lowered resolution from 61.2% to 57.3%, while the trained pair reached 72.6% on SWE-bench Verified.

Analysis: [daily analysis](2026-09-09/reasoning.md#independent-tests-must-be-frozen-before-repair)
Core sources: [paper](https://arxiv.org/abs/2609.09133v1), [MSR-Orchard/execcritic](https://github.com/MSR-Orchard/execcritic)
Tools and methodologies worth exploring now: independent test and repair principals, behavior contracts, clean-base-failure gates, frozen test bundles, held-out verification
Implementability score: 0.72

### Runtime state must own progress and completion

Summary: The Unreliable Progress Bar finds stage-dependent lifecycle-reporting gaps across deployed model configurations. Six of seven primary deployments had significant nonterminal-to-terminal gaps from 29.4 to 89.3 points, and post-done false reporting reached 90% to 100% for most deployments.

Analysis: [daily analysis](2026-09-09/reasoning.md#runtime-state-must-own-progress-and-completion)
Core source: [The Unreliable Progress Bar](https://arxiv.org/abs/2609.08589v1)
Tools and methodologies worth exploring now: runtime-owned lifecycle state, pending-obligation checks, separate report and task-success metrics, pre-action and post-completion fixtures
Implementability score: 0.90

### Procedural knowledge should be an editable graph

Summary: Procedural Graphs turns tool order, preconditions, and verification steps into a versioned transition graph. It ranked first or tied first in 21 of 24 model-benchmark cells and admits offline edits only after held-out validation.

Analysis: [daily analysis](2026-09-09/reasoning.md#procedural-knowledge-should-be-an-editable-graph-not-a-flat-note)
Core source: [Procedural Graphs](https://arxiv.org/abs/2609.09153v1)
Tools and methodologies worth exploring now: typed procedure nodes, precondition edges, bounded neighborhood guidance, frozen run snapshots, rejected-edit memory
Implementability score: 0.61

## Current implication

Agent loops need external truth surfaces. Freeze tests before repair, derive progress from durable runtime state, and evolve procedural guidance only through held-out admission.
