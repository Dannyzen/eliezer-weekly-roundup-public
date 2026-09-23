# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-23

### Compact original context without recursive rewriting

Summary: CliffCompaction lowers long-horizon cost by deleting or truncating original content, never paraphrasing retained content and never compacting an earlier compaction. The paper reports up to 50 percent lower cost while maintaining or improving benchmark performance.

Analysis: [daily analysis](2026-09-23/reasoning.md#compact-by-deletion-never-recursive-rewriting)
Durable deep dive: [Context Economy](context-economy/context-economy.md)
Core sources: [paper](https://arxiv.org/abs/2609.26779v1), [MIT repository](https://github.com/nguyenvuthientrang/cliffcompaction)
Tools and methodologies worth exploring now: original-span lineage, deletion-only compaction, non-recursive views, compaction receipts, full-context controls, accepted-outcome gates
Implementability score: 0.86

### Convert observed failures into narrow runtime policies

Summary: FIRE applies targeted instructions or action denials at states that preceded failures. Across 87 Terminal-Bench 2.1 tasks, repeated success increased in all three tested model tiers while best-of-two changed much less.

Analysis: [daily analysis](2026-09-23/reasoning.md#convert-observed-failures-into-narrow-runtime-policies)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper](https://arxiv.org/abs/2609.26048v1), [dataset](https://huggingface.co/datasets/failproofai/fire-runtime-policy-reliability)
Tools and methodologies worth exploring now: failure-state clustering, state-specific instructions, deterministic action denials, sham-policy controls, repeated-success metrics, versioned policy eligibility
Implementability score: 0.74

## Current implication

Put context transformation and incident learning in the harness. Preserve raw evidence, make every policy narrow and reversible, and test cost savings separately from accepted outcomes.
