# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-05

Historical safety context and generic detector benchmarks both fail when treated as execution authority. Restore constraints at release time and qualify filters on the exact tool-output distribution they govern.

### Restore historical constraints before execution

Summary: GHOST reports an 11.5% benign long-horizon constraint-violation rate on GPT-5.5. STAR-Guard combines semantic constraint restoration with a deterministic pre-execution audit.

Analysis: [daily strategy analysis](2026-10-05/sovereignty.md#restore-historical-constraints-before-every-consequential-action)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md)
Core source: [GHOST paper v1](https://arxiv.org/abs/2610.02664v1)
Tools and methodologies worth exploring now: provenance-bearing constraint registers, applicability checks, exact-effect manifests, deterministic vetoes, long-history regression journeys
Implementability score: 0.81

### Evaluate detectors on deployed tool outputs

Summary: Prompt-injection detector rankings transferred poorly across public and agent-shaped benchmarks. False-positive rates on tool outputs ranged from zero to over 90%.

Analysis: [daily strategy analysis](2026-10-05/sovereignty.md#evaluate-prompt-injection-detectors-on-deployed-tool-outputs)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.03448v1), [benchmark repository](https://github.com/lzwhehe/benign-instruction-bench)
Tools and methodologies worth exploring now: tool-output replay, differential injection replay, fixed low-FPR evaluation, blocked-task accounting, training-data provenance audits
Implementability score: 0.91

## Current implication

Context and benchmark rank may inform a decision. The execution control plane must restore, test, and enforce the decision against live action data.

Latest roundup: [2026-10-05](../roundups/2026-10-05.md).
