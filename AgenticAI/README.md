# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the daily analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-18

### Treat harness components as conditional policies

Summary: A 176-setting study across four models and two coding benchmarks found no universal best harness. Context management matters most under tight windows, deterministic elision should precede summarization, planning changes role with model capability, and tool richness should match shell proficiency.

Analysis: [daily analysis](2026-09-18/reasoning.md#treat-harness-components-as-conditional-policies)
Core source: [harness design study](https://arxiv.org/abs/2609.20804v1)
Tools and methodologies worth exploring now: controlled component ablations, context-window sweeps, deterministic elision, model-specific planning policies, structured-tool versus bash-only comparisons
Implementability score: 0.84

### Turn recorded incidents into cut-point regression tests

Summary: Chronicle records nondeterministic model, tool, and routing boundaries, then replays unchanged boundaries while executing selected code live. Across six incidents, full replay used zero model calls and stayed stable across 20 repetitions; selective tests caught every unsafe-action mutant while a fully stubbed baseline caught none.

Analysis: [daily analysis](2026-09-18/reasoning.md#turn-recorded-incidents-into-cut-point-regression-tests)
Durable deep dive: [Incident Replay Testing](incident-replay-testing/incident-replay-testing.md)
Core source: [Chronicle paper](https://arxiv.org/abs/2609.20625v1)
Tools and methodologies worth exploring now: [Chronicle](https://github.com/theagentplane/chronicle), immutable boundary envelopes, selective live boundaries, committed incident fixtures, OpenTelemetry spans
Implementability score: 0.93

### Profile intent across runs, not only spans within one run

Summary: AgentPProf projects agent traces onto stable semantic task stacks and emits pprof-compatible profiles. It reached 0.764 B3 F1 against human segmentation and improved localization MAP across three benchmarks, making cross-run token and failure hotspots visible.

Analysis: [daily analysis](2026-09-18/reasoning.md#profile-intent-across-runs-not-only-spans-within-one-run)
Core source: [AgentPProf paper](https://arxiv.org/abs/2609.20301v1)
Tools and methodologies worth exploring now: [AgentSight agentpprof](https://github.com/eunomia-bpf/agentsight/blob/master/docs/agentpprof.md), pprof, folded stacks, semantic operation paths, signed difference profiles, OpenTelemetry export
Implementability score: 0.80

## Current implication

Stop treating the harness and its traces as opaque glue. Tune components by measured conditions, turn incidents into replayable tests, and aggregate resource use by stable task intent.
