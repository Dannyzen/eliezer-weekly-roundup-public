# Strategy

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Thursday, 2026-07-30

### Metadata-aware pre-action gates protect evidence the model cannot inspect

Summary: SARC-DQ finds that metadata-borne defects produce costly actions about 60 percent of the time across four model tiers, while explicit data-quality flags remain at zero and behavioral doubt stays at chance. A pre-action gate recovers covered defect classes and exposes uncovered predicate gaps.

Analysis: [dated sovereignty analysis](2026-07-30/sovereignty.md#metadata-aware-pre-action-gates-catch-evidence-defects-models-cannot-see)
Core sources: [paper](https://arxiv.org/abs/2607.26313v1), [MIT repository](https://github.com/besanson/dqSarc)
Implementable now:
- attach freshness, version, lineage, schema, and completeness metadata to high-impact records;
- run deterministic predicates immediately before side effects;
- remediate in a governed buffer, not by silently rewriting source systems;
- log evidence IDs, predicate versions, substitutions, uncovered gaps, and committed effects.
Tools, repositories, and methodologies:
- SARC-DQ, JSON Schema or Pydantic, data contracts, bitemporal versioning, Great Expectations or Soda, OPA or Cedar, OpenTelemetry evidence spans
Implementability score: 0.80

## Current implication

Model capability cannot compensate for evidence it never receives. Keep metadata-aware validation at the action boundary and preserve a receipt that binds admitted evidence to the committed effect.
