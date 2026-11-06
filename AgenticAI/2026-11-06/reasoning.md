# AgenticAI Daily Analysis: 2026-11-06

All four shortlisted papers were submitted on November 5, 2026. External repositories were inspected read-only. No external source code was cloned, installed, built, imported, or executed.

## 1. Treat benchmarks as maintained software

Terminal-Bench 2.1 shows that a benchmark can be carefully reviewed at release and still accumulate measurement debt. A continuous audit of Terminal-Bench 2.0 found issues in roughly 30 percent of the benchmark. Repairs changed measured accuracy by more than 10 percentage points and moved leaderboard positions by as many as three ranks. Resource policy mattered too: longer time limits closed a 20 point harness gap on GPT 5.4 and shrank a 30 point gap on GPT 5.4 mini to 5 points.

Why it matters: benchmark tasks, verifiers, infrastructure, and budgets are one versioned measurement system. A frozen task set with drifting infrastructure or stale oracles produces precise but unreliable scores.

Stack fit: trajectory-aware evaluation and harness release engineering.

Implementable now:
- version tasks, verifiers, sandbox images, timeouts, compute limits, and retry policy together;
- accept community reports as candidate defects, then reproduce them against stored trajectories;
- run automated oracle checks and human-gated repairs before publishing revised scores;
- retain old and repaired grades with machine-readable reasons;
- compare leaderboard sensitivity across resource budgets before claiming a harness advantage.

Artifact status: [Terminal-Bench 2.1](https://github.com/harbor-framework/terminal-bench-2-1) is a populated public repository with repaired tasks and leaderboard workflow. It was inspected read-only.

Evidence caveat: the audit is one benchmark family. The maintenance workflow generalizes more strongly than the exact defect rate.

Implementability score: 0.92

Core source: [Benchmarks as Software v1](https://arxiv.org/abs/2611.08417v1)

## 2. Build MCP tests around structural failure triggers

MCPHallu turns four failure mechanisms into task construction rules: Branch Collapse, Unreachable Goal, Tool Misuse, and Context Forgetting. Across 358 tasks, 36 production MCP servers, 14 models, and 5,012 trajectories, Unreachable Goal was the hardest subtype. Its mean score was 0.458 and only 23.2 percent of runs passed. Model rankings moved by an average of 6.9 of 13 positions across subtypes, so one aggregate MCP score hides materially different failure profiles.

Why it matters: an agent that cannot recognize an impossible goal may keep issuing calls or falsely claim completion. Aggregate success rates cannot isolate that behavior from tool-selection or memory failures.

Stack fit: MCP harness design, trajectory diagnosis, and release regression testing.

Implementable now:
- add infeasible tasks whose available tool inventory cannot satisfy the goal;
- create near-pair tools that differ in one consequential semantic property;
- retain intermediate values across multi-step calls and test later dependence;
- score structural trajectory checks separately from judge-based assessment;
- report subtype profiles and false-completion rates beside aggregate task success.

Artifact status: [J1zz/mcp_hallu](https://github.com/J1zz/mcp_hallu) is populated with canonical tasks, scoring modules, recorded results, and container infrastructure. It was inspected read-only.

Evidence caveat: parts of the score still use an LLM judge, although structural checks carry most of the weight for Tool Misuse and Unreachable Goal.

Implementability score: 0.84

Core source: [MCPHallu v1](https://arxiv.org/abs/2611.07689v1)

## 3. Validate compressed memory at near and far scales

The LAQ paper shows that nearest-neighbor preservation alone can hide global distortion. At 96 bytes per passage, rescored binary codes retained local fidelity of 0.97 while moving 10.1 percent of passages to another theme. LAQ adds a far-rank hinge objective to OPQ codebook training. It improved global fidelity in all 52 held-out runs while preserving the same byte budget and query-time interface.

Why it matters: retrieval uses the near end of memory geometry, while consolidation, clustering, deletion, deduplication, and theme maps also depend on medium and far relationships. A compression accepted only on recall can silently corrupt those operations.

Stack fit: vector-memory storage, consolidation, and migration qualification.

Implementable now:
- measure local neighbor fidelity and global rank fidelity before a compression cutover;
- preserve full-precision source vectors or source records for rollback and audit;
- compare consolidation and clustering outcomes, not only retrieval recall;
- qualify new encoders and quantizers on the actual memory distribution;
- treat codec, encoder, and training recipe as one versioned memory artifact.

Artifact status: [hank08819/LAQ](https://github.com/hank08819/LAQ) is a populated public research implementation with OPQ-compatible codecs, fidelity metrics, and tests. It was inspected read-only.

Evidence caveat: this is a new single-author method. The package is experimental and its far-fidelity metrics need independent replication on production memory distributions.

Implementability score: 0.68

Core source: [Enhancing Local and Global Structure in Compressed AI Agent Memory v1](https://arxiv.org/abs/2611.08341v1)
