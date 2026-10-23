# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-23 Daily Scan

### Make security diagnosis replayable across runtimes

Summary: Normalize heterogeneous runtime telemetry into one canonical event contract, derive policy-decisive evidence slices, and require every diagnosis claim to cite recorded events.

Analysis: [make security diagnosis replayable across agent runtimes](2026-10-23/sovereignty.md#make-security-diagnosis-replayable-across-agent-runtimes)

Core sources: [paper v1](https://arxiv.org/abs/2610.30738v1), [Apache-2.0 repository](https://github.com/AsnGs/agenttriage-open-source)

Implementable now:
- join invocation and result lifecycles deterministically;
- distinguish native from synthesized identity;
- version runtime overlays and policy oracles;
- abstain when required evidence is missing.

Evidence caveat: the evaluation is author-run across five overlays and some identity fields are synthesized by adapters.

Implementability score: 0.84

### Require evidence recovery before consequential action

Summary: Treat omitted safety facts as an authorization failure, try an explicit recovery path, then abstain if required evidence remains unavailable.

Analysis: [missing evidence must trigger recovery or abstention](2026-10-23/sovereignty.md#missing-evidence-must-trigger-recovery-or-abstention)

Core source: [EpiSEM-Bench paper v1](https://arxiv.org/abs/2610.31650v1)

Implementable now:
- enumerate critical evidence per effect class;
- test matched prohibited and permissible worlds;
- grade unsafe execution and excessive refusal separately;
- expose a bounded evidence-recovery tool path.

Artifact caveat: no public implementation repository was verified.

Implementability score: 0.68

## Current implication

Evidence is part of execution authority. A runtime needs both a complete-enough evidence gate before action and a replayable evidence chain after action.
