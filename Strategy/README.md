# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-14

### Acceptance must combine correctness with change authorization

Summary: CAPRI evaluates 180 proof-repair runs. Six of 144 Isabelle-accepted candidates modified protected text. A separate machine-readable edit contract detects these false successes, while a proof-body-only interface removes observed violations at a small repair cost.

Analysis: [daily strategy](2026-08-14/sovereignty.md#capri-acceptance-must-combine-correctness-with-change-authorization)
Core source: [CAPRI](https://arxiv.org/abs/2608.13459v1)
Tools and methodologies worth exploring now: editable-region contracts, independent conformance checkers, forbidden-effect lists, proof-body or patch-only interfaces, original and candidate hashes, dual verdict receipts
Implementability score: 0.84

### The execution path belongs inside the authority boundary

Summary: QuoteBench shows that downstream parsers can damage a generated action even when the model reply is fixed. Approving only the model-visible command does not approve the actual executed effect.

Analysis: [daily strategy](2026-08-14/sovereignty.md#quotebench-the-execution-path-belongs-inside-the-authority-boundary)
Core sources: [paper](https://arxiv.org/abs/2608.13547v1), [public artifact](https://github.com/LeonardNJU/quoteBench)
Tools and methodologies worth exploring now: exact action manifests, transform logs, production-wrapper replay, parser-boundary removal, final-state receipts
Implementability score: 0.92

### Previously passing properties need monotonic authority

Summary: Cumulative-best IaC security metrics improve while raw trajectories regress. Once a property passes, a later repair should need explicit authority to invalidate it.

Analysis: [daily strategy](2026-08-14/sovereignty.md#iterative-repair-needs-monotonic-property-authority)
Core source: [Does Fixing Break Security?](https://arxiv.org/abs/2608.13404v1)
Tools and methodologies worth exploring now: preservation obligations, best-candidate versus release-candidate separation, explicit waivers, per-iteration property vectors, diff-bound policy receipts
Implementability score: 0.88

## Current implication

Use conjunctive release gates. Outcome validity, authority conformance, path fidelity, and property preservation are separate predicates.
