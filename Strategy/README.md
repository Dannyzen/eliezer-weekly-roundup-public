# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-29 Daily Scan

Today's control rule is direct: a runtime must measure the evidence path and the intervention's net utility before granting authority to a validator.

### Make evaluation evidence delivery-complete and effect-complete

Summary: Silent Failures shows that undelivered payloads and identity-only tool scoring can invert security results. Corrected scoring changed measured attack success from 21.7% to 1.2%.

Analysis: [daily strategy analysis](2026-09-29/sovereignty.md#make-evaluation-evidence-delivery-complete-and-effect-complete)
Durable deep dives: [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Silent Failures in Agentic Security Evaluation](https://arxiv.org/abs/2609.32691v1)
Tools and methodologies worth exploring now: delivery receipts, exact effect predicates, environment conformance tests, replayable traces
Implementability score: 0.94

### Govern validators by net utility, not halt count

Summary: Maat's deterministic contracts caught real defects and reduced cost, yet 37% of reviewed halts were false alarms. DebateLedger shows that blocking harmful collapse can also block more useful correction.

Analysis: [daily strategy analysis](2026-09-29/sovereignty.md#govern-validators-by-net-utility-not-halt-count)
Durable deep dives: [Runtime Governance](runtime-governance/runtime-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [Maat](https://arxiv.org/abs/2609.34017v1), [Measuring Collapse and Correction](https://arxiv.org/abs/2609.35279v1)
Tools and repositories worth exploring now: [Maat benchmarks](https://github.com/Lorelys/maat-benchmarks), [DebateLedger](https://github.com/LiXin97/DebateLedger), paired replay, signed intervention ledgers
Implementability score: 0.86

## Current implication

A control becomes an authority boundary only after input delivery, exact effects, false alarms, lost corrections, and net utility are all visible and replayable.

Friday synthesis remains the current week-level map: [2026-09-25 sovereignty](2026-09-25/sovereignty.md).
