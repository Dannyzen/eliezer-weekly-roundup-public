# Strategy Daily Sovereignty, 2026-07-30

## Verdict

A more capable model cannot detect evidence that never enters its context. The controlling architecture is a metadata-aware pre-action gate that checks freshness, lineage, completeness, and consistency before a costly side effect.

## Scan boundary

SARC-DQ was submitted as v1 on Tuesday, 2026-07-28 and first listed on Thursday, 2026-07-30. The PDF and public artifact were inspected read-only. The repository is populated, MIT-licensed, and explicitly labels itself an alpha research artifact. No external source code was cloned, installed, built, imported, or executed.

## Metadata-aware pre-action gates catch evidence defects models cannot see

### What it found

SARC-DQ separates record payload from metadata and tests whether a competent purchasing agent turns silent evidence defects into monetary loss. Across four model tiers spanning roughly 15x in inference price and eight defect classes, metadata-borne defects produced costly actions about 60 percent of the time. Explicit data-quality flags remained at zero and behavioral doubt stayed at chance, AUC at or below 0.50.

A metadata-aware gate placed immediately before action fully recovered losses for defect classes covered by its predicates and failed on classes outside that coverage. The analytical oracle tracked observed rates with mean absolute error 0.015, Pearson r = 0.876, and interval coverage in 15 of 16 cells.

### Why it matters

Model intelligence is not evidence access. A stale price, superseded record, broken lineage, or missing provenance can remain invisible if the tool returns only a plausible payload. Asking the model to be more skeptical cannot repair an information boundary it cannot observe.

The important design choice is enforcement placement. Data-quality checks belong where the runtime still has source metadata and before the action becomes externally costly.

### Fit in the stack

Primary layer: evidence provenance and execution control.

The gate is downstream-only. It quarantines or substitutes evidence in a governed buffer and leaves source systems unchanged. This avoids turning an agent-side remediation into an unauthorized source write.

### Implementable now

- attach freshness, source, version, lineage, schema, and completeness metadata to every high-impact evidence record;
- evaluate deterministic predicates immediately before the side effect;
- keep repair in a governed buffer and never silently rewrite the source of record;
- log admitted evidence IDs, predicate versions, substitutions, uncovered gaps, action intent, and committed effect;
- pair every corrupted run with a same-seed clean counterfactual and price the resulting action delta;
- start in shadow mode on one workflow before blocking production actions.

Tools, repositories, and methodologies:
- SARC-DQ, JSON Schema or Pydantic, data contracts, bitemporal versioning, Great Expectations or Soda, OPA or Cedar, governed buffers, OpenTelemetry evidence spans

Implementability score: 0.80

Artifact status: the public repository contains deterministic tests, frozen results, claim-consistency checks, and a zero-cost replay path. The GitHub license metadata is unset, but the repository contains an MIT license file. The evidence is still a single-author, narrow replenishment benchmark. Two declared defect classes remain uncovered, and one high-magnitude uncovered class dominates the remaining recoverable loss.

Sources:
- [SARC-DQ paper](https://arxiv.org/abs/2607.26313v1)
- [SARC-DQ repository](https://github.com/besanson/dqSarc)

## Adjacent control surfaces from today's scan

Three implementation findings reinforce the same strategy:

- AgentGUI shows that operator supervision needs live state and explicit intervention receipts rather than transcript archaeology.
- MemSecBench shows that persistent memory needs write, consequence, repair, and benign-preservation evidence under one configuration identity.
- CAM-DF shows that tool catalogs are authority surfaces. Ranking relevance is not enough; the gateway must decide how much exposure the task receives.

Sources:
- [AgentGUI](https://arxiv.org/abs/2607.26300v1)
- [MemSecBench](https://arxiv.org/abs/2607.27080v1)
- [Scores Are Not Decisions](https://arxiv.org/abs/2607.27083v1)

## Working conclusion

> Put evidence-quality checks at the last point where metadata is visible and before authority becomes effect. A stronger model is not a substitute for a better gate.
