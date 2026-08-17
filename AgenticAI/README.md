# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-17

### Skills work mainly as procedural anchors

Summary: Across 8,135 normalized trials, skills beat matched workflow memory by 6.06 points. Procedural anchoring dominated coded cases, while actual-use precision collapsed as candidate pools grew.

Analysis: [daily analysis](2026-08-17/reasoning.md#skills-work-mainly-as-procedural-anchors)
Core source: [Demystifying Agent Skills](https://arxiv.org/abs/2608.14036v1)
Tools and methodologies worth exploring now: matched trace-memory-skill arms, procedural compatibility labels, actual-use parsing, held-out promotion tests, cross-harness verification
Implementability score: 0.90

### Recovery needs aligned context and environment checkpoints

Summary: AgentRewind restores both model context and controlled environment state. It improved success across three harnesses and recovered 30.0% of paired failed endpoints versus 8.0% for continued repair.

Analysis: [daily analysis](2026-08-17/reasoning.md#recovery-needs-aligned-context-and-environment-checkpoints)
Core sources: [AgentRewind](https://arxiv.org/abs/2608.14380v1), [runtime repository](https://github.com/Futuresis/replay-agent-recorder), [MettleBench](https://github.com/Kelvin-Coffee/MettleBench)
Tools and methodologies worth exploring now: aligned checkpoint IDs, controlled environment snapshots, rewind memory, restore-point validators, Continue-versus-restart-versus-rewind tests
Implementability score: 0.84

### Computer-use acceptance must grade atomic failure

Summary: LegacyWorld separates useful completion, safe failure, and persistent damage across 28 Windows workflows and six computer-use agents. Task success and state safety produced materially different rankings.

Analysis: [daily analysis](2026-08-17/reasoning.md#computer-use-acceptance-must-grade-atomic-failure)
Core sources: [LegacyWorld paper](https://arxiv.org/abs/2608.14131v1), [LegacyWorld repository](https://github.com/ThiloReintjes/LegacyWorld)
Tools and methodologies worth exploring now: fresh VM runs, allowed and forbidden state deltas, post-run validators, four-way outcome labels, atomicity-aware acceptance tests
Implementability score: 0.88

### Message correctness does not determine trajectory value

Summary: Fixed-pool leave-one-out replay found wrong-helpful messages in every tested benchmark-model combination. Correctness and downstream contribution are separate properties.

Analysis: [daily analysis](2026-08-17/reasoning.md#message-correctness-does-not-determine-trajectory-value)
Core sources: [Wrong but Useful](https://arxiv.org/abs/2608.14375v1), [reproducibility artifact](https://arxiv.org/src/2608.14375v1/anc/anonymous_reproducibility/README.md)
Tools and methodologies worth exploring now: immutable message pools, leave-one-out replay, repeated effect labels, context-bound contribution data, conservative keep-or-remove policies
Implementability score: 0.78

## Current implication

Treat procedures, checkpoints, persistent state, and peer messages as testable runtime objects. Reliability appears when the harness can inspect, restore, validate, and replay them.
