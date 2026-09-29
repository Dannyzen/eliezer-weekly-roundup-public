# Strategy Daily Sovereignty Analysis - 2026-09-29

Today's governance signal is that evidence and intervention must be independently measurable. A control plane cannot infer safety from a tool name, a halted run, or a compressed transcript.

## Make evaluation evidence delivery-complete and effect-complete

Silent Failures shows how an agent-security benchmark can report plausible results when attack payloads never arrive, arguments are ignored, and environment mismatch is counted as model incapacity. Re-scoring identical traces changed measured attack success from 21.7% to 1.2%.

### Strategic implication

Treat benchmark stimuli, policy inputs, and tool effects as governed records. The runtime needs proof that the tested input was delivered and that the scorer inspected the exact arguments and resulting state.

### Control pattern

- Bind each scenario to an environment identity and payload-delivery receipt.
- Preserve exact tool arguments and post-action state.
- Separate refusal, incapacity, transport failure, and policy enforcement.
- Reject aggregate scores that cannot be replayed from retained evidence.

Tools and methodologies worth exploring now: machine-checkable delivery receipts, effect predicates, replayable security traces, environment conformance tests

Implementability score: 0.94

Core source: [Silent Failures in Agentic Security Evaluation](https://arxiv.org/abs/2609.32691v1)

## Govern validators by net utility, not halt count

Maat's deterministic handoff contracts reduced cost when they caught attributable defects, yet 37% of reviewed halts were false alarms. DebateLedger found a similar failure in debate control: one freeze rule prevented 29 collapses and lost 108 corrections.

### Strategic implication

Deterministic controls deserve trust only when their own errors are measured. A validator needs versioning, paired replay, false-alarm accounting, and a signed intervention ledger before it can become an authority boundary.

### Control pattern

- Version contracts, validators, and scoring definitions together.
- Record prevented defects, false alarms, lost corrections, and preserved corrections.
- Require paired governed and ungoverned replay before promotion.
- Roll back policies whose net intervention utility is negative.
- Keep human override and audit paths outside the validator itself.

Tools and repositories worth exploring now: [Maat benchmarks](https://github.com/Lorelys/maat-benchmarks), [DebateLedger](https://github.com/LiXin97/DebateLedger), signed intervention utility, paired trajectory replay

Artifact caveat: the linked repositories are public and populated, but GitHub metadata exposed no detected SPDX license during this scan.

Implementability score: 0.86

Core sources: [Maat](https://arxiv.org/abs/2609.34017v1), [Measuring Collapse and Correction in Homogeneous-Panel LLM Debate](https://arxiv.org/abs/2609.35279v1)

## Working conclusion

A governed runtime proves input delivery, scores exact effects, and measures the cost of blocking useful work. Controls become authority only after their own error surface is visible.
