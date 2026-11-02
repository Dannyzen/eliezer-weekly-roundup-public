# AgenticAI Daily Analysis: 2026-11-02

## Scope

The Monday, November 2 arXiv listing is live. Both selected v1 papers were submitted October 30 and first listed November 2. External repositories were inspected read-only; no external code was executed.

## 1. Recover from ambiguous tool outcomes with public evidence

Tool timeouts are uncertain effects. A write may have failed, committed, remained in flight, or partially completed while dependent work continued. Evidence-Guided Recovery models recovery as a partially observable control problem and preserves unresolved, handoff, and unknown-delay states instead of guessing success or retrying blindly.

The paper evaluates 20 authored mechanism templates across 37 latent-state combinations and five policies, producing 185 records. In a paired model study, planning assistance produced 30 certified safe completions in 58 episodes versus 9 of 58 for evidence prompting, a 36.2 percentage-point difference with p = 0.0078 under the registered family test. All 116 paired trajectories passed independent replay.

Why it matters: retries are side effects. A production runtime needs receipts, idempotency keys, dependency state, settlement evidence, and compensation safety before choosing retry, continue, compensate, hand off, or remain unresolved.

Fits into the stack: runtime recovery between tool execution and workflow orchestration.

Implementable now:
- assign stable operation IDs and idempotency keys before dispatch;
- persist intent, dispatch, acknowledgment, settlement, and verification separately;
- classify outcomes as failed, committed, pending, partial, or unresolved;
- query authoritative state before retry or compensation;
- preserve handoff and unknown as valid outcomes;
- replay delayed, duplicated, and partial effects in CI.

Evidence caveat: the workload is authored mechanism evidence, not a random sample of enterprise incidents. The model comparison uses one runtime and limited repeated samples. No dedicated public implementation repository was identified.

Implementability score: 0.83

Core source: [Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution](https://arxiv.org/abs/2610.41453v1)

## 2. Evaluate recursive memory for error persistence, not task score alone

KEEPER defines self-consistency bias as an incorrect claim persisting because each recursive update conditions on prior memory. Its key warning is operational: better task performance does not prove the memory corrected false history, while lower error persistence can hide destructive forgetting.

The paper compares reward preservation, predictive preservation, semantic anchoring, and update-stability objectives inside a shared recursive-memory interface on ScienceWorld and ALFWorld. Reward-related prediction is strongest among the evaluated post-RL conditions. A claim-level trajectory shows incorrect state persisting despite corrective observations.

Why it matters: memory quality needs separate correction and retention axes. End-task success proves neither.

Fits into the stack: memory update training, regression testing, and long-horizon control state.

Implementable now:
- represent memory claims with source event IDs and validity state;
- test contradiction, correction, omission, and recurrence across updates;
- score valid-information retention separately from error removal;
- compare updates before and after model or prompt changes;
- keep canonical events outside recursively rewritten summaries.

Evidence caveat: evaluation covers two backbones in one architecture, with the second tested only on ALFWorld. The claim-level analysis is qualitative and limited to one baseline trajectory. No public implementation artifact was identified.

Implementability score: 0.55

Core source: [KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.41482v1)

## Practical cut

Build the recovery ledger first. It is deployable with event sourcing, idempotency, provider queries, and replay fixtures. Use KEEPER's correction-versus-retention split as a memory quality gate now; defer training objectives until repeated failures justify model work.
