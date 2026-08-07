# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-07

### TRAJDEBUG attributes earliest decisive errors

Summary: TRAJDEBUG builds multi-granularity trajectory views, then detects error triggers, classifies error state, and attributes the critical failure step. On 486 annotated failed trajectories from τ²-Bench and SWE-Bench Pro, diagnosis-guided re-execution improves success by about 10.80 percent on average.

Analysis: [daily analysis](2026-08-07/reasoning.md#trajdebug-turns-failed-trajectories-into-auditable-critical-error-evidence)
Core sources: [paper](https://arxiv.org/abs/2608.06346v1), [repo](https://github.com/THU-KEG/TrajDebug)
Implementable now:
- store multi-granularity trajectory views;
- separate error triggers from terminal failure;
- convert critical-error diagnoses into re-execution guidance;
- promote repeated patterns into failure memory with held-out checks.
Tools and repositories:
- THU-KEG/TrajDebug, SWE-Bench Pro failed traces, τ²-Bench, trajectory viewers, Hermes coding-lane receipts
Implementability score: 0.78

### Misleading history can flip known-good tool policies

Summary: When History Lies shows that structurally valid multi-turn tool history can hijack a policy the model already possesses under clean state. On Qwen3-1.7B, polluted history flips about 32.1 percent of otherwise correct decisions versus an Oracle State view.

Analysis: [daily analysis](2026-08-07/reasoning.md#misleading-multi-turn-history-can-flip-tool-decisions-the-model-already-knows)
Core source: [paper](https://arxiv.org/abs/2608.06057v1)
Implementable now:
- separate verified current state from raw multi-turn history;
- label tool traces as verified, superseded, failed-no-effect, or untrusted;
- evaluate polluted-history and oracle-state views;
- revalidate state before high-impact tool calls that depend on historical identifiers.
Tools and methodologies:
- session state ledgers, tool-trace authority labels, multi-turn tool-use fixtures, MCP conversation stores
Implementability score: 0.64

### Self-evolving skills need pre-commit gates

Summary: When Self-Evolution Backfires finds skill pools are not monotonically helpful. Past a critical size, new skills contaminate performance and post-hoc rollback recovers little. Verifier-as-Gatekeeper admits skills only before they enter runtime context.

Analysis: [daily analysis](2026-08-07/reasoning.md#self-evolving-skill-pools-need-pre-commit-gates-not-post-hoc-cleanup)
Core source: [paper](https://arxiv.org/abs/2608.05810v1)
Implementable now:
- split draft, admitted, and revoked skill states;
- require behavioral replay before skill load;
- block progressive disclosure of rejected skills;
- track pool growth against task regression.
Tools and methodologies:
- skill registries, replay harnesses, held-out suites, Skill-Use facet scoring, Hermes skill catalogs
Implementability score: 0.69

## Previous Structured Update: 2026-08-06

### Skill use needs progressive disclosure scores

Summary: Skill-Use grades trigger, compliance, and boundary separately when an agent sees only a skill name and short description before retrieving the full procedure. It covers 79 real skills and 177 sandbox tasks.

Analysis: [daily analysis](2026-08-06/reasoning.md#skill-use-separates-trigger-compliance-and-boundary-under-progressive-disclosure)
Core sources: [paper](https://arxiv.org/abs/2608.04828v1), [repo](https://github.com/JinyiHan99/Skill-Use-Bench)
Implementability score: 0.76

### Canary tools diagnose tool-selection failure modes

Summary: Canary Tools plants six trap types into MCP-style catalogs and turns wrong-tool outcomes into susceptibility profiles across 8,640 runs.

Analysis: [daily analysis](2026-08-06/reasoning.md#canary-tools-turn-wrong-tool-outcomes-into-a-failure-taxonomy)
Core source: [paper](https://arxiv.org/abs/2608.04719v1)
Implementability score: 0.60

### SuperScout routes after scout verification

Summary: SuperScout scouts a repository with a 7B searcher, strips failed reproduction claims, then routes among frontier fixers. On SWE-bench Pro Python-266 it matches the best solo solve rate at about one fifth the matched cost per solve.

Analysis: [daily analysis](2026-08-06/reasoning.md#superscout-routes-coding-agents-only-after-scouting-and-stripping-false-claims)
Core sources: [paper](https://arxiv.org/abs/2608.04804v1), [repo](https://github.com/TransformerOptimus/superscout)
Implementability score: 0.80

## Current implication

Retained text is a lead, not a grant. Failed trajectories need critical-error evidence. Session history needs authority labels. Skills need admission before they can load or self-expand.
