# Agentic AI Research Analysis: 2026-09-18

## Freshness and evidence boundary

The harness study, Chronicle, and SkillAA were submitted as v1 on 17 September 2026 and first listed by arXiv on 18 September 2026. AgentPProf was submitted on 14 September and first listed in today's cs.AI batch, so it is current by listing date but outside a strict trailing 48-hour submission window. Primary abstract pages, HTML papers, PDFs, and linked repositories were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Treat harness components as conditional policies

### Finding

An Empirical Study of Harness Design for Coding Agents holds the execution loop fixed while varying planning, action space, and context management across four models, SWE-Bench Verified, Terminal-Bench 2.1, five context-management strategies, four context windows, and 176 matched settings.

The main result is not a universal best harness. Context management matters most at tight windows because it prevents overflow. Rule-based elision before summarization gives the strongest overall efficiency. Recoverable elision adds machinery that models rarely use and produces no accuracy gain. Planning helps weaker models reach correct solutions but mainly saves cost for stronger models. Predefined tools help models with weaker shell ability, while bash-capable models can be cheaper with a bash-only interface.

### Why it matters

Harness design should be calibrated to model capability, task shape, and budget. Adding every scaffold can increase cost and complexity without improving outcomes. The right unit of evaluation is a controlled component ablation, not a brand-level comparison between monolithic agents.

### Fit in the stack

This belongs in agent harness architecture, context economy, and model routing. Harness configuration is a policy chosen from measured task and model characteristics.

### Practical tools and methods worth exploring

- Reproduce a small component matrix across context budgets before standardizing a harness.
- Apply deterministic elision before paid summarization.
- Keep elided-content recall optional until traces show models use it.
- Compare structured tools with bash-only execution per model family and task type.
- Measure success, context overflow, token cost, stop location, and verification behavior together.

### Artifact status and caveat

No paper-specific public implementation repository was found on the primary paper pages. The paper supplies a detailed modular method and 176-setting evaluation, but the exact harness is not packaged for direct reuse. Results were measured on four models and two coding benchmarks, so transfer should be checked locally.

Implementability score: 0.84

Core source: https://arxiv.org/abs/2609.20804v1
PDF: https://arxiv.org/pdf/2609.20804v1

## Turn recorded incidents into cut-point regression tests

### Finding

Chronicle records model calls, tool calls, and routing decisions as immutable boundary envelopes. Full replay serves every recorded boundary. Cut-point replay serves the unchanged boundaries from the record while executing selected boundaries live with new code.

On six recorded failures with simulated model boundaries, recording added 23 microseconds per crossing, full replay issued zero model calls and stayed bit-stable across 20 repetitions, and cut-point tests rejected faulty code while accepting guarded and benign changes for all six incidents. Its mutation study caught every mutant that allowed the recorded unsafe action through. A baseline that stubbed every boundary caught none.

### Why it matters

A production failure should become a durable regression fixture. Re-running the whole agent is expensive and nondeterministic. Stubbing everything can hide the very behavior a fix must exercise. Selective replay keeps the real incident context while running only the changed control surface.

### Fit in the stack

This extends event-sourced runtimes, trajectory-aware evaluation, and CI. The test primitive is a recorded incident plus an explicit live boundary set.

### Practical tools and methods worth exploring

- Record immutable input, output, model, sampling, tool, and routing envelopes at nondeterministic boundaries.
- Redact secrets before storage and retain stable boundary names plus occurrence indexes.
- Run tool gates, routers, validators, or policy checks live while stubbing expensive model calls.
- Commit incident records and assertions as regression fixtures when privacy permits.
- Emit OpenTelemetry spans so replay tests and production traces share one vocabulary.

### Artifact status and caveat

The public MIT repository has a populated `main` branch, Python packaging, examples, fixtures, tests, CI, documentation, and published releases. It was inspected read-only and not executed. The empirical benchmark has only six incidents and simulated model boundaries, so the method is highly implementable but not yet broad evidence of production coverage.

Implementability score: 0.93

Core source: https://arxiv.org/abs/2609.20625v1
Artifact: https://github.com/theagentplane/chronicle

## Profile intent across runs, not only spans within one run

### Finding

AgentPProf compiles prompts, model calls, tool operations, and system effects into pprof-compatible semantic operation stacks. Instead of grouping only by timestamps or raw request tags, it segments trajectories into stable task-intent paths such as diagnose authentication, then aggregates tokens, time, files, or operation counts across runs.

Against human annotations on CodeTraceBench, recursive segmentation reached 0.764 B3 F1 versus 0.663 for a statistical baseline and 0.541 for raw actions. Across three localization benchmarks, the profile improved mean average precision by 0.031, 0.107, and 0.117. One profile-derived repair reduced agent tokens by 19 percent without degrading task quality. The study includes 41 long-horizon sessions, 440 web-agent runs, eight public benchmarks, and three real trajectory datasets.

### Why it matters

Tracing answers what happened in one run. Profiling answers where a fleet spends its time, tokens, and risk budget across many runs. Stable semantic paths are the missing aggregation key between user intent and low-level effects.

### Fit in the stack

This belongs in agent observability and fleet monitoring. OpenTelemetry spans remain useful, but a profiling layer must project them onto task intent and workflow phase.

### Practical tools and methods worth exploring

- Export trace events into a uniform operation schema with additive measures.
- Add stable semantic paths above raw agent and tool spans.
- Generate pprof, folded-stack, and flamegraph views for tokens, time, files, network, and operation count.
- Compare successful and failed runs with signed difference profiles.
- Keep previews off by default because semantic profiles can expose sensitive prompts and paths.

### Artifact status and caveat

The implementation is available inside the populated MIT AgentSight repository, with a dedicated agentpprof guide, Codex and Claude Code session support, pprof output, releases, and an optional non-LLM statistical segmenter. It was inspected read-only and not executed. Semantic segmentation still depends on model or statistical labeling quality, and the paper was submitted on 14 September rather than within the strict trailing 48-hour window.

Implementability score: 0.80

Core source: https://arxiv.org/abs/2609.20301v1
Artifact: https://github.com/eunomia-bpf/agentsight
Guide: https://github.com/eunomia-bpf/agentsight/blob/master/docs/agentpprof.md

## Practical next steps

1. Build one small harness ablation matrix around context compaction, planning, and action space.
2. Convert one known agent incident into a cut-point replay fixture.
3. Produce one semantic token flamegraph from a week of local agent traces.
