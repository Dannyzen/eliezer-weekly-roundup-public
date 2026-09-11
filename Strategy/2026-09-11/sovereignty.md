# Strategy Daily Sovereignty - 2026-09-11

## Freshness and selection

The selected papers were first listed by arXiv on Friday, 11 Sep 2026. VP-CONTROL was submitted on 10 Sep and A2ABreak on 9 Sep. Both expose reproducible public artifacts, inspected read-only. No external source code or benchmark was downloaded or executed.

## Independent evidence beats a second model at commit time

VP-CONTROL isolates a common failure in multi-agent verification: two models can agree because both consume the same stale or corrupted evidence. Its 48 task templates produce 2,880 deterministic scenarios across six fault regimes. In the fixed-call 2x2 comparison, a cross-model vote over shared evidence approved 62.9% of unsafe proposals, versus 22.9% when the second verifier used an independent source. Evidence-source diversity moved the result by 40.9 percentage points, while model diversity moved it by 11.3 points.

A calibrated portfolio on the locked test reached 1.9% unsafe execution with 38.2% automated safe coverage. The weakness is transfer: unseen fault families still produced 16% to 26% risk. The paper therefore supports a control-plane rule, not a universal safety rate. Verification plans should buy independent evidence, require atomic preconditions, and defer when the calibrated risk budget cannot be met.

How it fits into strategy: evidence provenance and execution control. The verifier model is not the root of trust. The root is an independently sourced, current, typed observation consumed at the non-bypassable commit boundary.

Practical tools and methodologies worth exploring now:

- separate evidence-lineage IDs for actor and verifier reads
- deterministic fault injection for stale, partial, degraded, and raced state
- calibrated verification portfolios with explicit cost, risk, and coverage targets
- atomic compare-and-commit or transactional guards for mutable preconditions
- defer as a first-class result when independence cannot be established
- the MIT VP-CONTROL Figshare artifact for offline replay design

Evidence caveat: the main benchmark is deterministic and synthetic, the actors are frozen local-model proposals, and the controlled HTTP/SQLite study is not a distributed production deployment. The public artifact includes frozen records, tests, preregistrations, and transaction-level audit material; replay does not require LLM access.

Implementability score: 0.74

Core sources: [paper](https://arxiv.org/abs/2609.10969v1), [VP-CONTROL artifact](https://doi.org/10.6084/m9.figshare.33511441.v1)

## Protocol compliance is not delegation safety

A2ABreak models the Agent2Agent protocol as a verified finite-state machine, then searches for missing security primitives under a specification-compliant adversary. It reports 11 new vulnerabilities that do not require implementation bugs, including cross-client context injection through unprotected context identifiers, credential harvesting when identity is lost across delegation hops, and data exfiltration through rogue agents with unattested capability claims.

Against independent expert review, the framework achieved 73.3% precision and 84.6% F1. A zero-shot LLM over the same specification produced no confirmed findings. The public MIT repository is populated with the PSM benchmark, formal-verification inputs and results, source, and outputs. This makes the work useful as a protocol threat-model corpus, not proof that every deployed A2A system is exploitable.

How it fits into strategy: agent gateway governance. A2A's horizontal delegation boundary needs stronger controls than peer discovery and transport authentication. Context ownership, end-principal identity, capability attestation, and task lineage must survive every hop.

Practical tools and methodologies worth exploring now:

- `arlotfi79/A2ABreak` as a read-only attack taxonomy and benchmark reference
- tenant-bound context identifiers with non-transferable ownership
- end-principal and delegation-chain identity on every task and artifact
- signed, attested capability manifests rather than self-advertised Agent Cards
- least-privilege credential delegation with hop limits and audience binding
- formal state-machine review of A2A lifecycle changes before rollout

Evidence caveat: the analysis assumes a fully compliant adversary and evaluates normative gaps in the specification, not measured prevalence across production deployments. Precision of 73.3% also means expert adjudication remains necessary.

Implementability score: 0.73

Core sources: [paper](https://arxiv.org/abs/2609.10871v1), [A2ABreak repository](https://github.com/arlotfi79/A2ABreak), [A2A specification](https://a2a-protocol.org/latest/specification/)

## Current implication

Do not spend the next safety dollar on another model reading the same state. Buy independent evidence, bind it atomically to the write, and preserve principal, context, and capability identity across every delegated hop.
