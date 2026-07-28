# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Tuesday, 2026-07-28

### Taint confinement needs engine-owned child trajectories

Summary: APPA proposes keeping untrusted or sensitive reads inside restricted child trajectories and admitting only checked returns or atomic one-call rulings. It reports attack success falling from 31 to 50 percent to 0 to 7 percent across four models.

Analysis: [daily sovereignty analysis](2026-07-28/sovereignty.md#taint-confinement-needs-engine-owned-branches-and-checked-return)
Core source: [paper](https://arxiv.org/abs/2607.24625v1)
Implementable now:
- label sources and sinks before observation;
- isolate restricted reads in child trajectories;
- merge only typed, size-bounded, provenance-bearing derivatives;
- bind exceptional authority to one rendered action.
Tools, repositories, and methodologies:
- information-flow labels, child run identities, trusted sanitizers, atomic policy rulings, append-only event logs
Implementability score: 0.52

### Containment governance needs a security-utility frontier

Summary: ContainmentBench demonstrates that zero committed harm is not enough. Runtime policies must also preserve authorized work and expose propagation and recovery across the trace.

Analysis: [daily sovereignty analysis](2026-07-28/sovereignty.md#containment-metrics-should-preserve-the-security-utility-frontier)
Core source: [paper](https://arxiv.org/abs/2607.23999v1)
Implementable now:
- keep endpoint compliance, propagation, recovery, and utility separate;
- compare conservative taint, intent-aware authorization, and tool-boundary controls on matched scenarios;
- require explicit authorization ledgers for intent-aware exceptions.
Tools, repositories, and methodologies:
- structured authorization ledgers, stage-stratified traces, matched controls, positive-control attacks
Implementability score: 0.68

## Current implication

Do not ask the model to reason itself clean after reading untrusted data. Branch below the model, merge through checked runtime policy, and measure both containment and authorized utility.
