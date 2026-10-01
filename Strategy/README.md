# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-01 Daily Scan

Today's authority rule is direct: audit the world model that makes a certificate valid.

### Audit the verifier's committed world model

Summary: Removing one edge from a causal action graph raised false executions from 0% to 15.3%; reversing one direction produced 48.9% false executions. The actions still carried internally valid certificates. Bounded randomized attestation recovered measured safety, while auditing wrongful inaction required much more experimental budget.

Analysis: [daily strategy analysis](2026-10-01/sovereignty.md#audit-the-verifiers-committed-world-model)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md)
Core source: [Who Verifies the Graph?](https://arxiv.org/abs/2609.40027v1)
Tools and methodologies worth exploring now: versioned action-state graphs, graph mutation tests, bounded randomized attestation, abstention, rejection audits, effect receipts
Implementability score: 0.64

## Current implication

A valid proof can authorize the wrong effect when its assumptions are wrong. Bind every certificate to the exact graph, environment, assumptions, attestation evidence, and audit budget used to produce it.

Latest roundup: [2026-10-01](../roundups/2026-10-01.md).
