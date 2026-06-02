# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-02 Daily Scan

### SkillHarm makes skill security lifecycle-aware
Summary: SkillHarm shows that third-party skills can be attacked across installation, retrieval, execution, mutation, and reuse. The dangerous case is self-mutating poisoning: a benign-looking first run silently changes persistent skill content and defers harm to later tasks.

Analysis: [daily reasoning analysis](2026-06-02/reasoning.md#skillharm-makes-skill-security-lifecycle-aware)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core source: [SkillHarm](https://arxiv.org/abs/2606.02540v1)
Implementable now:
- make production-admitted skills immutable during execution;
- record skill source, version, body hash, manifest hash, and verification level;
- block skill self-modification outside reviewed patch paths;
- add lifecycle tests for install, retrieval, execution, update, reuse, quarantine, and rollback.
Tools, repos, and methodologies worth exploring:
- signed skill manifests, skill cards, semantic fuzzing, static risk scanners, file integrity checks, OPA/Cedar, OpenTelemetry trace fields, adversarial skill fixtures
Implementability score: 0.82

### Continual learning eval needs controlled transfer streams
Summary: AGENTCL argues that lifelong-agent evaluation should construct streams where earlier sub-solutions, evidence, or workflows are intentionally reusable later, then measure transfer gain and interference instead of rewarding raw memory stuffing.

Analysis: [daily reasoning analysis](2026-06-02/reasoning.md#continual-learning-eval-has-to-separate-transfer-from-memory-stuffing)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [AGENTCL](https://arxiv.org/abs/2606.02461v1)
Implementable now:
- create compositional task streams with known reusable pieces;
- run no-memory, raw-retrieval, summarized-memory, and promoted-skill baselines;
- score forward transfer, negative transfer, forgetting, retrieval precision, and cost;
- log which prior episode or workflow influenced later tasks.
Tools, repos, and methodologies worth exploring:
- compositional task streams, non-parametric memory ablations, transfer-gain metrics, trajectory replay, held-out transfer fixtures, skill promotion gates
Implementability score: 0.70

### Interactive agent evals must score process separately from outcome
Summary: ClinEnv builds staged inpatient simulations where models query specialist agents before committing to decisions. Its useful general lesson is that process quality and outcome quality can decouple; final-answer scoring hides redundant evidence gathering, poor sequencing, and weak late-stage management.

Analysis: [daily reasoning analysis](2026-06-02/reasoning.md#clinenv-shows-process-quality-and-outcome-quality-decouple-in-interactive-agent-benchmarks)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [ClinEnv](https://arxiv.org/abs/2606.02568v1)
Implementable now:
- build staged task environments with evidence-gathering checkpoints;
- label irreversible commitments and late-stage management actions;
- require evidence-query logs before final decisions;
- score redundant queries, missing evidence, bad sequencing, and unsupported commitments.
Tools, repos, and methodologies worth exploring:
- staged simulation harnesses, ontology-grounded matchers, specialist subagent mocks, trace-level process scoring, irreversible-decision labels, evidence-query budgets
Implementability score: 0.53

## Previous structured update

The prior daily scan for 2026-06-01 focused on verified skills, heterogeneous evolving memory evals, and deterministic retrieval oracles: [2026-06-01 roundup](../roundups/2026-06-01.md).
