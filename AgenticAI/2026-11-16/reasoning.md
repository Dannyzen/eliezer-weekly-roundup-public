# AgenticAI Daily Analysis: 2026-11-16

The strongest implementation signal is that the harness is becoming an executable state machine. It should evolve from evidence, checkpoint work at meaningful boundaries, and prove replay before promotion.

## 1. Learn harness programs from typed trajectories

ModHarness-RL represents an agent interaction as typed blocks for reasoning, tool calls, tool results, and guidance. Compression and Steering are executable programs over that state. Candidate programs are proposed from recent trajectories, executed for validation, replayed over past trajectories, and admitted only when they improve held-out behavior as the model changes.

Why it matters: prompt and memory scaffolds are usually fixed configuration. This work treats them as versioned software that can be learned, tested, replayed, and retired. The durable pattern applies beyond RL: store typed trajectory state, derive small candidate transforms, replay them against a frozen corpus, and promote only evidence-bearing changes.

Implementable now:
- store reasoning, calls, results, and guidance as typed trajectory blocks;
- express compression and steering as deterministic programs rather than free-form prompt rewrites;
- replay every candidate against historical trajectories before admission;
- retire guidance when the underlying failure declines;
- measure task score, context use, latency, and regression shape separately.

Evidence and caveat: on CodeSearch, ModHarness-RL improves over the fixed harness by 14 to 24 percent and by 5 to 12 percent over the strongest comparison baseline. Compression or Steering improves seven of eight ALFWorld and BIRD SQL settings. The public repository currently contains documentation rather than an implementation, has no detected license, and was inspected read-only.

Artifact status: project page and public repository inspected read-only. No source was cloned or executed.

Implementability score: 0.62

Core source: [ModHarness-RL v1](https://arxiv.org/abs/2611.18533v1)

Project evidence: [project page](https://zlhe0.github.io/ModHarness-RL/), [repository](https://github.com/ZLHe0/ModHarness-RL)

## 2. Checkpoint coding-agent setup at semantic boundaries

HerAgent divides environment setup into functional blocks such as system packages, language runtime, and project dependencies. Each block has its own validation boundary and checkpoint. Repairs must replay from the previous valid checkpoint, and suspected earlier faults trigger rollback to the responsible block rather than a one-command retry or full reset. The final setup is replayed in a clean container.

Why it matters: long setup trajectories fail because command-level recovery preserves polluted state while whole-script recovery discards good work. A semantic block is a better unit for validation, rollback, cost accounting, and durable receipts.

Implementable now:
- compile setup into ordered blocks with explicit preconditions and validation commands;
- checkpoint only after a block passes;
- bound local repair and require replay from the prior checkpoint;
- relocate root cause to an earlier block when current repair cannot validate;
- replay the accepted sequence in a fresh environment before using it as evidence.

Evidence and caveat: against six prior agents on four datasets, HerAgent reports setup gains from 52.0 to 85.0 percent on Installamatic-Bench and 46.3 to 70.4 percent on SetupBench, with cost reduction up to 94.5 percent. The public artifact predates this paper and has no detected license in GitHub metadata, so the architecture is stronger evidence than immediate package readiness.

Artifact status: repository and paper inspected read-only. No source was cloned or executed.

Implementability score: 0.84

Core source: [HerAgent v1](https://arxiv.org/abs/2611.18443v1)

Public artifact: [BeeuniLab/pheragent](https://github.com/BeeuniLab/pheragent)

## Working conclusion

Treat harness changes and environment setup as stateful software. Typed state, semantic checkpoints, replay, and bounded promotion are the path from plausible agent behavior to reproducible work.
