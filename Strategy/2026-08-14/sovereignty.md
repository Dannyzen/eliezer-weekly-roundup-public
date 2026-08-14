# Strategy Daily Sovereignty Analysis, 2026-08-14

## Thesis

A green result is not authority. Side effects and automated repairs need conjunctive acceptance: the requested outcome must hold, the exact change must stay inside its grant, the execution path must preserve intent, and previously valid properties must remain valid.

## CAPRI: acceptance must combine correctness with change authorization

### Finding

CAPRI treats an LLM proof repair as an untrusted patch. Isabelle checks whether the theory builds, while an independent checker enforces a machine-readable edit contract over protected text, the permitted proof region, forbidden commands, and build configuration. A repair is accepted only when both predicates hold.

Across 180 runs on 12 failed proofs, 144 terminal candidates were accepted by Isabelle. Six of those had modified protected text. A proof-body-only interface produced 29 of 36 valid repairs with no contract violations, compared with 31 of 36 for the corresponding full-theory workflow. The narrow interface gives up two repairs while removing observed authority violations.

### Why it matters

This is the exact shape of a safe agent release gate. A successful build, API response, or validator result proves one predicate. It does not prove that the agent changed only what the principal authorized. The effect boundary needs an independent frame condition.

### Fit into the strategy stack

Primary layer: context-to-execution integrity and execution control.

The reusable pattern is:

`Accept = OutcomeValid AND ChangeAuthorized AND ForbiddenEffectsAbsent`

The contract, original state, candidate state, verifier output, policy verdict, and hashes should be retained together. The agent may propose a patch, but it must not define its own authority boundary.

### Practical tools, repositories, and methodologies worth exploring

- Express editable files, byte ranges, declarations, resources, fields, and effect classes as a machine-readable contract.
- Run the normal build or business validator independently from the contract checker.
- Reject candidates that pass the outcome check but cross the edit boundary.
- Prefer narrow proof-body, patch, field, or typed-operation interfaces over whole-artifact rewrites.
- Preserve original and candidate hashes, diff, contract, verdicts, and execution receipts.
- Treat the contract checker as part of the trusted computing base and test it separately.

Implementability score: 0.84

Artifact status: the arXiv listing says a reproducibility artifact is available on Zenodo, but this scan did not resolve an exact artifact URL. The paper and PDF were inspected; no artifact was executed.

Weakest point: the benchmark has 12 tasks from four developments maintained by the authors, three replicates per condition, and one hosted model configuration. The checker is conservative, does not judge proof quality inside the authorized region, and is not formally verified.

Submission: 2026-08-13 16:43:44 UTC. First listed: 2026-08-14.

Core source:
- https://arxiv.org/abs/2608.13459v1

## QuoteBench: the execution path belongs inside the authority boundary

### Finding

QuoteBench shows that a downstream parser can damage the same generated command by 55.4 to 73.2 percentage points. Contract disclosure can then make the model compensate, causing matched-path scores to hide the transport defect.

### Why it matters

A model’s generated intent is not the executed effect. Serializers, wrappers, SSH hops, container shells, CI steps, and operating-system parsing all transform the action. Governance that approves only the model-visible command misses the actual path to effect.

### Practical tools, repositories, and methodologies worth exploring

- Bind approval to the exact decoded command or typed action manifest.
- Record every transport transform and the executor input.
- Replay fixed actions through production wrappers before release.
- Remove extra parser boundaries where possible.
- Require final-state receipts after execution.

Implementability score: 0.92

Core sources:
- https://arxiv.org/abs/2608.13547v1
- https://github.com/LeonardNJU/quoteBench

## Iterative repair needs monotonic property authority

### Finding

The IaC regression study shows that cumulative-best security metrics can improve while raw per-iteration security regresses. The defensible strict regression rate is 3.3 percent of scenarios, with higher churn and volatility around regressing transitions.

### Why it matters

The runtime must remember not only what still fails, but what has already earned protection. Once a property passes, a later repair should need explicit authority to invalidate it. Best-so-far dashboards are not sufficient because they hide the state being proposed for release.

### Practical tools, repositories, and methodologies worth exploring

- Convert passing checks into preservation obligations for the next iteration.
- Distinguish the best observed candidate from the candidate currently proposed for release.
- Require explicit waivers for intentional property removal.
- Preserve per-iteration property vectors, diffs, and policy receipts.

Implementability score: 0.88

Core source:
- https://arxiv.org/abs/2608.13404v1

## Current implication

Use conjunctive release gates. Outcome validity, authority conformance, path fidelity, and property preservation are separate predicates. No single green check can stand in for all four.
