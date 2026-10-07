# AgenticAI Daily Analysis: 2026-10-07

## Thesis

Long-horizon agent evaluation needs two independent surfaces: a reviewable account of what the agent did, and attack-shaped tests of what the harness actually prevents. Final answers and static settings do not prove either one.

## Freshness and evidence scope

Both papers were first listed by arXiv on 2026-10-07. Transect v1 and HarnessSecurity-Bench v1 were submitted on 2026-10-06. The papers, public repositories, and repository metadata were inspected read-only. No external repository was cloned, installed, built, imported, or executed.

## Retain reviewable observability across long agent runs

Transect is an open-source transcript-analysis package for long-horizon evaluations. It aligns events, token use, sub-agent activity, structural signals, and model-generated behavioral labels on one turn-based timeline. Every label can point back to source turns, and the resulting tables can be exported for cross-run analysis.

The paper demonstrates the workflow on an AI research run containing almost 13 million tokens. That scale matters because a successful terminal score can hide missing phases, silent coordination failures, or concentrated tool use that only become visible when the whole trajectory is reviewable.

### Why it matters

Observability should preserve the path from summary back to event. Evaluators can use model judges to triage a large transcript, while reviewers retain the source turns, prompts, settings, and reliability diagnostics needed to challenge the interpretation.

### Stack fit

This belongs in the evaluation and observability layer. It complements terminal-state oracles rather than replacing them. State proves what changed. Transect helps explain how the run reached that state and where the harness shaped the result.

### Practical tools and methods

- Transect for navigable long-run reports and exported dataframes
- Inspect AI and Inspect Scout for evaluation logs and scanners
- structural scanners before semantic judges
- source-turn provenance for every generated label
- judge cohorts, agreement statistics, and sensitivity checks
- independent expert annotations for validity checks

### Artifact and evidence caveat

The public MIT repository is populated and documents direct installation from GitHub, but it has no tagged release yet. The paper explicitly warns that judge reliability does not establish validity. Expert annotations or another independent evidence source are still required before treating a behavioral label as ground truth.

Implementability score: 0.88

Core sources:
- [Transect paper v1](https://arxiv.org/abs/2610.08364v1)
- [Transect repository](https://github.com/AI-Safety-Institute/transect)
- [Inspect AI](https://inspect.aisi.org.uk/)

## Test harness security with separate utility and attack oracles

HarnessSecurity-Bench evaluates coding-agent harness controls against both legitimate task completion and attack effects. The study maps ten mechanisms across 40 harnesses, then evaluates nine mechanisms across six open-source harnesses with 23 tasks and five attack surfaces.

The controlled study covers 2,500 trials, 81,155 tool calls, and more than 2.2 billion tokens. Enabling auto-approve raised attack success from 29.2 percent to 95.6 percent. Network isolation and read-only mode reduced attack effects with substantial utility loss. Command allowlists and denylists reduced attack effects with much smaller utility costs, while alternative execution paths sometimes kept unauthorized operations reachable.

### Why it matters

A control label such as read-only, network isolated, or approval required is not evidence of effect coverage. The harness must be tested against the exact protected operation, all reachable execution paths, and the legitimate work that the control may block.

### Stack fit

This belongs in the harness and evaluation layers. The benchmark shape is more important than any single harness ranking: freeze the harness version, run the same task with a control on and off, grade utility and attack state separately, then inspect bypass paths.

### Practical tools and methods

- deterministic utility and attack-effect oracles
- control-on versus control-off paired trials
- explicit alternative-path attack fixtures
- versioned effective-settings capture
- attack success, utility, execution cost, and tool-call accounting
- source-located evidence for mechanism coverage claims

### Artifact and evidence caveat

The public benchmark repository is populated with task packages and utility checks, but it has no tagged release and GitHub did not report a repository license. The study uses one base model, GLM-5.2, and Docker-based simulated services. Closed-source harnesses retain major evidence gaps.

Implementability score: 0.81

Core sources:
- [HarnessSecurity-Bench paper v1](https://arxiv.org/abs/2610.07639v1)
- [HarnessSecurity-Benchmark repository](https://github.com/TsingPig/HarnessSecurity-Benchmark)
- [Project site](https://tsingpig.github.io/HarnessSecurity-Benchmark/)

## What to implement now

1. Render one long agent run as a source-linked timeline before adding more summary layers.
2. Require every semantic behavior label to retain its source turns and judge settings.
3. Add one paired harness-control test with separate legitimate-task and forbidden-effect oracles.
4. Record the effective security setting and all tested bypass paths in the release receipt.
