# Daily Strategy Research: 2026-10-01

The strongest governance finding is direct: a correct verifier can produce valid certificates for harmful actions when its committed world model is wrong.

## Audit the verifier's committed world model

Who Verifies the Graph red-teams CIVeX, a causal action verifier that gates state-changing tool calls against a committed action-state graph. The author changes only that graph.

On 1,050-action cells across seven seeds, omitting one bidirected edge raises false executions from 0% to 15.3% at the published confounding strength. Of the resulting executions, 91% are harmful, and utility falls from +2.27 to +0.35. Reversing one arrowhead produces 48.9% false executions and no correct executions. Every harmful execution still carries an internally valid certificate.

A bounded randomized attestation step detects both attacks. Refusing actions that fail or cannot be tested produces zero false executions in the measured settings, with two false alarms among 555 executions on a truthful graph. The cost is material: safety recovery uses 127 experiments per 1,050 actions. Recovering the lost beneficial actions needs 614 more experiments because the misspecified graph rejects them before attestation runs.

### Why it matters

A proof is only as sound as the committed model it proves against. Certificate validity, policy syntax, or a zero-false-execution benchmark cannot authorize effects unless the graph, schema, environment identity, and assumptions are also tested.

The paper exposes two separate failure classes:

- wrongful action, which execution attestation can detect;
- wrongful inaction, which requires auditing refusals and costs much more.

### Fit in the strategy stack

The action-state graph is a policy-bearing runtime object. It needs source lineage, versioning, mutation tests, challenge probes, and an owner distinct from the acting agent. A verifier should be allowed to abstain when the model is untrusted or untestable.

### Practical methods worth exploring

- version and hash action-state graphs beside each certificate;
- generate edge-deletion, edge-direction, omitted-confounder, and stale-state mutation tests;
- use bounded randomized interventions for high-impact certified executions;
- audit a sample of rejections to measure wrongful inaction;
- separate certificate validity from world-model validity in dashboards and release gates;
- fail closed when the graph identity, environment identity, or attestation budget is missing.

Evidence caveat: this is a synthetic causal tool-use benchmark, and the single author is red-teaming his own earlier verifier. No paper-owned public implementation artifact was resolved. The reported mechanism is useful, but it does not establish production prevalence or deployed safety.

Implementability score: 0.64

Core source: [Who Verifies the Graph?](https://arxiv.org/abs/2609.40027v1)

## Working conclusion

Verification must cover the assumptions and world model behind the certificate. Audit both harmful executions and beneficial actions that a misspecified verifier suppresses.
