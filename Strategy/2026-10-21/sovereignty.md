# Strategy Daily Sovereignty Analysis - 2026-10-21

This scan covers papers first listed by arXiv on 2026-10-21 and submitted on 2026-10-20. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Treat persistent state as delayed execution authority

CarryoverBench measures prompt injections that survive the original session through memory files or scheduled wake-ups. It includes 12 personal-assistant scenarios and 101 attack tasks across same-turn, scheduled, and memory-resurfaced channels. Across five frontier models, planted payloads showed no measurable decay over five trigger rounds. A port of 36 latent variants to Hermes reduced attack success but did not remove it; reported Hermes attack success ranged from 2.8% to 27.8% depending on model.

The strategic mistake is treating memory and cron as passive storage. A write can become a future execution path after the attacker has disappeared and the user is absent. Admission, persistence, resurfacing, and action need separate gates and separate receipts.

Implementable now:
- quarantine instructions derived from webpages and tool results;
- attach origin, principal, scope, and authority to every persistent write;
- scan scheduled wake-ups as fresh authority requests;
- test planting and triggering as independent stages across clean sessions;
- revoke or expire untrusted state before it can re-enter action context.

Artifact status: the paper links a public CarryoverBench repository with 435 files, including tasks, payloads, benchmark code, and a Dockerfile. It was inspected read-only and not executed. The evaluation is benchmark-shaped, and the Hermes transfer covers only the latent channel and 36 variants.

Implementability score: 0.78

Core sources:
- [Carryover attacks paper v1](https://arxiv.org/abs/2610.28425v1)
- [CarryoverBench repository](https://github.com/igloomatics/CarryoverBench)

## Monitor policy across executions, not only actions

Local Allow, Global Deny formalizes compositional authorization failures: each tool call can pass its local guard while the sequence, or a comparison between executions, violates policy for purpose, provenance, consent, or delegation. The paper proves that relational purpose violations are 2-safety properties with no single-trace locus of blame. A zero-false-alarm per-action monitor detects none of them. Across nine LLM judges, isolated witnesses were approved almost universally, while showing the paired executions exposed the violation.

This changes the control-plane unit. The authorization object cannot stop at one request and one tool call. It must include workflow purpose, prior executions, principal, data lineage, delegated authority, and the relation the policy intends to preserve.

Implementable now:
- bind each workflow to a declared purpose and principal;
- retain a policy projection of prior executions;
- compare disclosures and effects across runs for the same purpose;
- use SAT, SMT, or property-based synthesis to generate minimal relational witnesses;
- make false-alarm tolerance explicit when full cross-execution visibility is unavailable.

Artifact status: the paper names the public `al-synth` repository, but GitHub reports that it has no default branch and no populated tree. The formal method and witness pattern are usable as a design reference; the advertised implementation is not ready to inspect or run.

Implementability score: 0.56

Core sources:
- [Local Allow, Global Deny paper v1](https://arxiv.org/abs/2610.27620v1)
- [al-synth repository, currently empty](https://github.com/anmolpandey299/al-synth)

## Strategic implication

Agent authority must survive two dimensions: time and relation. Persistent state can trigger future effects, and individually permitted actions can combine into a forbidden workflow. Govern writes as delayed authority and evaluate policy across executions.
