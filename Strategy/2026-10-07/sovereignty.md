# Strategy Daily Analysis: 2026-10-07

## Thesis

Agent economics and agent sovereignty meet at the runtime boundary. The operator needs proof that each agent owns and releases its resource tree correctly, and proof that expensive general capability can be converted into cheaper reusable artifacts before scaling a repetitive workload.

## Freshness and evidence scope

MemMux v1 and BOTTLED v1 were first listed by arXiv on 2026-10-07 after submission on 2026-10-05 and 2026-10-06. The papers, public repositories, release metadata, and README claims were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Make agent-fleet resource ownership checkable at runtime

MemMux treats parallel coding-agent resource control as a runtime-verification problem. It attributes process trees to agents, checks descendant cleanup, surfaces escaped children, enforces a memory admission budget, and reports its own monitoring cost.

Under a 7.5 GiB binding budget, the paper reports zero swap while ungoverned launchers used twice the budget and spilled about 2 GiB to swap. MemMux reclaimed 100 percent of a terminated process subtree where the raw baseline stranded half of it, and it detected all 10 injected escaped children. The 1 Hz attribution scanner reached 2.7 percent CPU at ten agents, above the paper's 2 percent target.

### Why it matters

A fleet manager that only displays terminals cannot prove whether a stopped agent is actually gone, whether a child escaped its boundary, or whether overcommit will destroy uncommitted work. Resource ownership and cleanup are control-plane facts, not interface details.

### Strategic fit

This belongs in the sovereign runtime and fleet-monitoring layers. Every agent should receive a durable task identity, a bounded resource envelope, an owned process subtree, and a verifiable termination receipt.

### Practical tools and methods

- Linux cgroup v2 or equivalent process-group ownership
- per-agent proportional-set-size attribution
- admission control before process launch
- descendant cleanup verification after stop or failure
- escaped-process detection and quarantine
- host-stamped benchmark artifacts for attribution, cleanup, budget, and overhead

### Artifact and evidence caveat

The public MIT repository is populated and publishes prerelease binaries through v0.9.0. Most benchmark load is synthetic. The live check covers three Claude Code sessions, and larger live fleets plus live overcommit and escape tests remain future work. The monitoring-overhead target is not yet met.

Implementability score: 0.84

Core sources:
- [MemMux paper v1](https://arxiv.org/abs/2610.07257v1)
- [MemMux repository](https://github.com/sumanyumuku98/MemMux)

## Bottle repeated cognition before routing millions of calls

BOTTLED asks whether an agent can spend a fixed budget once to produce a reusable program or small model for a large repetitive workload. Across ten models, three tasks, and 60 runs, 48 runs fell below the lower bound of their model's zero-shot performance interval, and 31 underperformed the stronger same-budget distillation baseline.

The counterexample is useful. On one query-product relevance task, Opus 5 retained about 82 percent of zero-shot macro-F1 at roughly 657 times lower reported cost. The result shows that artifactization can create real leverage, while also showing that strong zero-shot capability does not predict the ability to build a cheap reusable solution.

### Why it matters

The default scaling move is to route every item to a general model. For repeated workloads, the router should first ask whether a bounded investment can produce a verified artifact with lower marginal cost. This is a separate capability from per-query accuracy.

### Strategic fit

This belongs in model-router governance and agent economics. The routing decision becomes build, validate, and reuse versus call a general model per item. The artifact must carry dataset, budget, quality, cost, and drift receipts.

### Practical tools and methods

- a fixed build budget before full-workload execution
- zero-shot and same-budget distillation controls
- workload-level quality and marginal-cost accounting
- held-out artifact validation before scale-out
- explicit fallback to general inference when artifact quality misses the gate
- drift tests that trigger rebuild or retirement

### Artifact and evidence caveat

The benchmark uses three tasks, one OpenCode harness, ten-hour runs, five million weighted tokens, and an NVIDIA A100 per run. The public MIT repository is populated but has no release, and its README says some result-processing and convenience code will be added later. The 657-times figure is a reported result for one task, not a general cost guarantee.

Implementability score: 0.61

Core sources:
- [BOTTLED paper v1](https://arxiv.org/abs/2610.08775v1)
- [BOTTLED repository](https://github.com/aktsonthalia/bottled)

## What to implement now

1. Give each local agent a resource envelope and an owned process tree.
2. Require stop receipts that prove descendant cleanup and zero escaped processes.
3. Add an artifactization branch to one high-volume classifier or extractor.
4. Compare reusable-artifact quality and cost against zero-shot and distillation controls before scaling.
