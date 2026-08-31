# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-31

### Put tool authority behind an external reference monitor

Summary: Recognition Without Enforcement shows that models can recognize forged authority yet still emit the conflicting tool call in reproducible configurations. External authenticated routing and capability-gated execution reject all tested forged, tampered, replayed, and unsigned requests.

Analysis: [daily strategy](2026-08-31/sovereignty.md#put-tool-authority-behind-an-external-reference-monitor)
Core source: [paper](https://arxiv.org/abs/2608.28502v1)
Tools and methodologies worth exploring now: authenticated source routing, capability-bound requests, exact argument and sequence validation, replay protection, freshness windows, clock-skew fixtures, external reference monitors
Implementability score: 0.72

### Admit self-modification only with a verified recovery witness

Summary: EvoUndo finds 197 capability-improving but unrecoverable mutations among 600 one-shot self-evolution tasks. Exact state addressing and a richer recovery calculus recover most oracle-defined failures, while conventional repair under the original representation recovers none.

Analysis: [daily strategy](2026-08-31/sovereignty.md#admit-self-modification-only-with-a-verified-recovery-witness)
Core source: [paper](https://arxiv.org/abs/2608.28363v1)
Tools and methodologies worth exploring now: mutation manifests, stable state identities, inverse semantics, counterfactual rollback fixtures, recovery witnesses, independent recovery verification, fail-closed admission
Implementability score: 0.63

## Current implication

Models may propose instructions and self-modifications, but they should not own authority or rollback proof. Tool execution belongs behind an external reference monitor, and every admitted mutation should carry an independently verified recovery witness.
