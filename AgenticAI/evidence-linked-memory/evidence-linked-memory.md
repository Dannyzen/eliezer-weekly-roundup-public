# Evidence-linked memory

## Overview

A reusable agent lesson is a claim about what happened and what should happen next. It should remain linked to the execution that produced it.

WikiTrace is the strongest finding of the week ending 2026-11-11 because it isolates that design choice cleanly. The comparison gives agents the same compiled insights. One condition receives only the insights. WikiTrace also receives read-only access to the compilation and raw trajectory behind each insight, plus instructions to inspect that evidence when the lesson is incomplete, conflicting, or derived from failure.

Across five benchmarks and eight suites, WikiTrace averaged 90.2, compared with 87.0 for the same insights without source access and 79.5 with no memory. Its Regression rate, the share of tasks harmed relative to the no-memory baseline, fell from 6.5 percent to 4.5 percent. The result matters more than another retrieval improvement because it changes the contract of memory itself: compression may guide action, but source evidence remains available to challenge the compression.

## Core innovation

WikiTrace stores procedural memory as three linked layers:

1. **Insight:** a short reusable lesson shown to the agent.
2. **Compilation:** a diagnosis of why the source run succeeded or failed.
3. **Raw trajectory:** the original actions and observations, mounted read-only.

The agent starts with the insights and descends only when a lesson lacks a required detail, conflicts with another lesson, comes from a failed run, or stops matching the current task. Terminal tools expose the lower layers without forcing every raw trajectory into the prompt.

This is stronger than plain retrieval. Retrieval asks which memory looks relevant. Evidence descent asks whether the selected memory is justified and applicable.

## Why it matters

### Memory can create regressions

Average accuracy hides whether memory helps new tasks while breaking tasks the agent already solved. WikiTrace separates:

- **Gain:** failures without memory that become successes with memory.
- **Regression:** successes without memory that become failures with memory.

The paper found that 52 percent of analyzed memory-induced failures traced to a memory item the agent followed, usually a wrong one. WikiTrace achieved 4.5 percent Regression, compared with 6.5 percent for identical insights without source access and 9.7 percent for a fresh no-memory rerun baseline.

### Binary outcomes do not validate lessons

A successful run can contain bad actions, and a failed run can contain useful procedures. A success or failure label cannot identify which step caused the outcome. Compilers therefore produce interpretations, not verified truth.

Source links make that uncertainty recoverable. They allow a later agent to inspect the observations, revise the interpretation, and preserve useful information from failed runs without trusting the compiled lesson blindly.

### Selective verification is practical

WikiTrace descended more often on hard tasks, 44 percent of runs, than on easy tasks, 22 percent. In 43 percent of descending runs, evidence changed the plan by revising an insight, filling a missing detail, or adding a fact. Those runs led the insight-only condition by 8.3 points. Test-time cost averaged 1.17 times the insight-only condition.

The practical pattern is selective source checking, not constant replay.

## Fit in the agentic stack

Evidence-linked memory belongs in the memory and evaluation layers.

- **Trajectory store:** immutable source runs, outcomes, tool receipts, model and harness identity.
- **Memory compiler:** summaries, lessons, skills, and failure diagnoses derived from source runs.
- **Provenance index:** links from each compiled claim to exact trajectory spans and compiler versions.
- **Runtime memory interface:** concise lessons first, read-only source descent on defined triggers.
- **Evaluation layer:** paired no-memory and memory conditions with separate Gain and Regression measures.

Authority remains outside this layer. Source evidence can correct a lesson, but it does not grant permission to act. The action boundary still needs identity, policy, approval, and effect receipts.

## Implement now

1. **Bind every lesson to evidence.** Store source trajectory ID, outcome, task identity, model, harness version, compiler version, content hash, and cited turn range.
2. **Preserve raw runs immutably.** Mount them read-only and keep derived memory separately writable.
3. **Define descent triggers.** Start with conflict, missing operational detail, failed-source provenance, action failure, and current-state mismatch.
4. **Expose evidence through ordinary tools.** File search, line reads, and stable links are enough for an initial implementation.
5. **Refuse stale corpora.** Fingerprint prompts, configs, code revisions, and benchmark versions before reuse.
6. **Measure harm explicitly.** Report Gain and Regression against the same task set, alongside aggregate success.
7. **Keep decision receipts.** Record which lesson was used, whether evidence was opened, what changed, and the final outcome.

## Tools, repositories, and methodologies worth trying

### WikiTrace

The Apache-2.0 repository contains the memory store, citation and mounting code, compiler prompts, resumable experiment runner, five benchmark adapters, and Gain/Regression analysis. It requires Python 3.11, uv, Node 20, Docker, benchmark data, and model API access.

Use it first as a read-only design and evaluation reference. An isolated reproduction is feasible, but the full five-benchmark run carries meaningful setup and API cost.

Repository: https://github.com/yukyeongleee/wikitrace

### Minimal local pattern

A smaller implementation can use:

- JSONL or SQLite for memory metadata;
- immutable trajectory files in content-addressed storage;
- Markdown insight and compilation documents with stable source links;
- a read-only search tool over trajectories;
- a paired evaluation harness that computes Gain and Regression;
- OpenTelemetry or equivalent trace IDs to connect runtime decisions to source runs.

### Evaluation method

Keep the insight text identical between conditions. Compare:

1. no memory;
2. insights only;
3. insights plus source access.

Run repeated trials on the same tasks. Report aggregate success, Gain, Regression, evidence-open rate, plan-change rate, latency, and cost.

## Implementation complexity

A minimal source-linked memory layer is moderate engineering. Existing agent systems usually already have traces, summaries, and file tools. The missing work is stable identity, immutable storage, links, descent policy, and paired evaluation.

A production version is harder. It must handle access control, retention, private data in trajectories, corpus growth, retrieval before descent, stale evidence, compiler migration, and trace redaction without breaking provenance.

## Implementability score

**0.88**

The core pattern can be implemented now with ordinary storage and terminal-style tools. Full reproduction across all benchmark suites and a production-scale provenance store require more operational effort.

## What remains conceptual or unproven

- WikiTrace places every insight in the initial prompt. Retrieval over a large memory remains open.
- A source link enables checking, but does not verify the compiler's diagnosis.
- The main evaluation uses one agent harness and one model family, with a smaller three-suite replication on a second model.
- Descent behavior and degradation causes are partly labeled by LLM judges reading stated reasoning.
- The benchmarks do not prove privacy, authorization, or retention policy for production trajectories.
- The public repository has no tagged release yet, so pinning an exact commit is necessary for evaluation.

## Strategic implications

Danny's durable model should treat memory as an evidence-bearing projection over event history.

- Raw trajectories and receipts are the historical record.
- Summaries, skills, rules, and profile facts are projections that can be rebuilt or challenged.
- Compression improves usability and creates epistemic risk at the same time.
- High-confidence action should require a path from guidance to evidence and then through a separate authority gate.
- Memory quality means increasing useful transfer while preserving tasks that already work.

This reinforces a broader product principle: keep the interface concise, keep the evidence reachable, and keep authority separate.

## Why it won the week

Other strong findings improved persistent file workspaces, deliverable-level grading, production trace reuse, evidence sufficiency, and external action policy. WikiTrace connects those themes at a more basic layer. It shows that agent learning from experience becomes safer when the system preserves both the compressed lesson and the execution that can refute it. The same pattern applies to skills, rules, profiles, handoffs, and evaluation findings.

## Sources

- [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents, arXiv v1](https://arxiv.org/abs/2611.14320v1)
- [Immutable paper PDF, arXiv v1](https://arxiv.org/pdf/2611.14320v1)
- [WikiTrace repository](https://github.com/yukyeongleee/wikitrace)
- [WikiTrace memory implementation notes](https://github.com/yukyeongleee/wikitrace/blob/main/src/wikitrace/memory/README.md)
- [WikiTrace Gain and Regression analysis notes](https://github.com/yukyeongleee/wikitrace/blob/main/src/wikitrace/analysis/README.md)
