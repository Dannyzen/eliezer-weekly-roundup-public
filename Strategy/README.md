# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-06

### A parsable success is not an honest tool

Summary: A 200 JSON body can be an answer to a different question when the schema never named the legal values. SilentProbe's downstream loops then assert false negatives or invent figures. The contract is the authority object.

Analysis: [daily strategy](2026-09-06/sovereignty.md#a-parsable-success-is-not-an-honest-tool)
Core sources: [paper](https://arxiv.org/abs/2609.00035v1), [silentprobe](https://github.com/Jasper0122/silentprobe)
Tools and methodologies worth exploring now: schema-validate arguments and results, fail closed on exemplified-only vocabularies, treat silent-failure rate as a gateway SLO
Implementability score: 0.82

### Hosted judges are not a sovereign measurement plane

Summary: A preregistered black-box observer on a shared endpoint failed Spearman 0.90 same-window and 0.99 next-day replay. Switching providers did not restore a frozen instrument. Self-hosting failed again under concurrent load.

Analysis: [daily strategy](2026-09-06/sovereignty.md#hosted-judges-are-not-a-sovereign-measurement-plane)
Core source: [Unstable Measurement](https://arxiv.org/abs/2609.04198v1)
Tools and methodologies worth exploring now: instrument gates before task gates, local or batch-invariant observers, publish request hashes with eval results
Implementability score: 0.58

### Replay without tool state is unauthorized reconstruction

Summary: Graph-only reconstruction labelled unobserved tool timeouts as benign. Replay-contract state and verification results are what moved unresolved-divergence recall off zero. Missing evidence is not a safe default.

Analysis: [daily strategy](2026-09-06/sovereignty.md#replay-without-tool-state-is-unauthorized-reconstruction)
Core source: [DNative-Twin](https://arxiv.org/abs/2609.03787v1)
Tools and methodologies worth exploring now: refuse reconstructability claims without tool results and verifier verdicts, treat missing tool state as unresolved divergence
Implementability score: 0.45

## Current implication

A 200, a model name, and a decision graph are observations. Honesty needs a schema. Measurement needs an instrument gate. Reconstruction needs tool state. Missing evidence is not a safe default.
