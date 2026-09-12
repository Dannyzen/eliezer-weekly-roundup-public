# AgenticAI Weekly Analysis - 2026-09-11

## Thesis

The agent can propose state, but it cannot own the evidence that makes that state authoritative. The implementable stack is converging on runtime-owned lifecycle state, independently qualified tests, provenance-bound memory, and held-out gates for harness change.

## Runtime-owned truth beats model self-report

### Finding

SilentProbe shows why transport success is not semantic success. Across 721,320 OpenAPI parameters from 2,501 documents, only 15.2% exposed any machine-checkable constraint. In live perturbations, machine-checkable constraints were honest in 111 of 111 cases, while prose-only constraints failed silently in 44 of 61. Downstream agent loops detected the miss only 12% of the time and repaired none.

The Unreliable Progress Bar finds the same substitution at the lifecycle boundary. Across StageIF deployments, the gap between model-reported adherence during execution and at completion ranged from 29.4 to 89.3 percentage points. A model can say the task is done without proving that obligations are terminal.

### Why it matters

An HTTP 200 response and a completion phrase are observations. Neither is a state transition. If the runtime accepts them directly, malformed tool queries become false negatives and unfinished work becomes false completion.

### Stack fit

This belongs in the agent serving runtime and trajectory-aware evaluation. Tool schemas decide whether an answer is admissible. A runtime state machine decides whether work is terminal. Model reports remain diagnostic.

### Practical path now

- Put finite vocabularies and required constraints in JSON Schema, not examples in prose.
- Record transport status, schema validity, semantic result, and downstream effect separately.
- Derive ready, blocked, and done from pending obligations and verified provider state.
- Retain model progress reports as a comparison signal, never as the sole stop condition.

Implementability score: 0.86

Core sources:
- [SilentProbe](https://arxiv.org/abs/2609.00035v1)
- [SilentProbe repository](https://github.com/Jasper0122/silentprobe)
- [The Unreliable Progress Bar](https://arxiv.org/abs/2609.08589v1)

## Independent acceptance needs independent evidence

### Finding

ExecCritic separates test construction from source repair and freezes the admitted test so the repair agent cannot rewrite its own oracle. The trained test and repair agents reached 72.6% on SWE-bench Verified, while poor generated tests lowered resolution. VP-CONTROL then shows that adding models is not enough when all verifiers inherit the same evidence. In 2,880 deterministic scenarios, cross-model voting over shared evidence approved 62.9% of unsafe proposals, versus 22.9% when one verifier had an independent source.

### Why it matters

A second agent is not an independent critic if it reads the same corrupted state. Test identity, evidence lineage, and write separation matter more than role labels.

### Stack fit

This belongs in the coding-agent control plane and deterministic evaluation. Test authors, repairers, and commit verifiers are separate principals with separate inputs and write scopes.

### Practical path now

- Qualify tests before repair and freeze their content hash.
- Deny repair agents write access to accepted tests and verifier configuration.
- Attach evidence-lineage IDs to every verifier result.
- Add common-mode fault fixtures where multiple models read the same wrong source.
- Keep explicit defer when current independent evidence cannot be established.

Implementability score: 0.74

Core sources:
- [ExecCritic](https://arxiv.org/abs/2609.09133v1)
- [ExecCritic repository](https://github.com/MSR-Orchard/execcritic)
- [VP-CONTROL](https://arxiv.org/abs/2609.10969v1)
- [VP-CONTROL artifact](https://doi.org/10.6084/m9.figshare.33511441.v1)

## Mutable memory needs migration and probe admission

### Finding

Memory portability is directional. In a controlled study over 48 synthetic histories, fixed-schema memory transferred cleanly, compressed notes moved by as much as -13.28 percentage points depending on the writer-reader direction, and a mixed embedding index recovered less than half the gain of full re-embedding. Grounding Agent Memory adds the missing write gate: a read-only curator probes the current environment before committing a memory. On CLBench, pass rate rose from 39% to 73%, average queries fell from 8.8 to 4.7, and task-agent cost fell from $3.38 to $1.68.

RD-Forget supplies a complementary read gate. It retains source history, suppresses superseded facts for current-state questions, and re-admits them for historical queries.

### Why it matters

A durable note is not portable merely because the file still opens. Its authority depends on the writer model, reader model, embedding space, source history, and current environment. Deleting stale facts destroys auditability; exposing them without a query-time gate launders obsolete state into current answers.

### Stack fit

This belongs in memory systems and knowledge-state orchestration. Raw evidence remains append-only. Derived memory carries provenance and compatibility metadata. Retrieval creates a query-scoped evidence view.

### Practical path now

- Bind every memory record to writer, reader, embedding model, schema, and source identity.
- Re-embed as a migration, never mix embedding generations silently.
- Give curators a bounded read-only probe surface and require probe receipts before write admission.
- Preserve superseded source facts while filtering their answer-time authority by query.
- Run paired no-memory and stale-memory evaluations before promotion.

Implementability score: 0.77

Core sources:
- [Memory Portability](https://arxiv.org/abs/2609.05339v1)
- [Grounding Agent Memory](https://arxiv.org/abs/2609.11060v1)
- [RD-Forget](https://arxiv.org/abs/2609.10263v1)

## Harness improvement needs a frozen boundary

### Finding

Ecdysis clusters recurring execution failures across tasks before proposing harness changes. It reports up to 1.84x faster harness training, 18.56% higher reasoning accuracy, and full-data-comparable results from one-quarter of the training data. Skill-Evo4GUI applies the safer release shape: execute against a frozen skill snapshot, derive structured evidence from the trace, and expose accepted changes only in the next iteration. A separate multi-harness RL study found that harness choice moved mean solve rate 4.3x, while cross-harness reward grouping did not produce a statistically clear held-out gain.

### Why it matters

A harness can improve by memorizing one model, one environment, or one failure. Without a frozen snapshot and held-out harness, adaptation is indistinguishable from portable capability.

### Stack fit

This belongs in agent harness architecture and skills-as-control. Harness changes are versioned artifacts. Training, acceptance, and rollout are separate stages.

### Practical path now

- Cluster failures by interaction structure before changing prompts, tools, or control logic.
- Execute each run against a content-addressed skill and harness snapshot.
- Admit mutations only into the next version after held-out task and held-out harness checks.
- Track quality, token cost, regression count, and model portability together.
- Keep production rollback to the prior snapshot cheap.

Implementability score: 0.61

Ecdysis has a populated public repository but no declared root license or release in the inspected GitHub metadata. Treat it as research code, not a drop-in production dependency.

Core sources:
- [Ecdysis](https://arxiv.org/abs/2609.11677v1)
- [Ecdysis repository](https://github.com/cuiyu-ai/Ecdysis)
- [Skill-Evo4GUI](https://arxiv.org/abs/2609.04869v1)
- [Skill-Evo4GUI repository](https://github.com/LongtaoHu/Skill-Evo4GUI)
- [Multi-harness RL study](https://arxiv.org/abs/2609.04518v1)

## Working conclusion

The practical stack is not short on agents. It is short on independent evidence and frozen transition boundaries. Make lifecycle state, accepted tests, memory lineage, and harness versions runtime-owned objects. Then let models propose changes against them.
