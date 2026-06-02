# AgenticAI Daily Analysis — 2026-06-02

## Signal over noise

Today’s signal is lifecycle control. Skills can poison future work after a benign-looking first run. Memory and continual-learning evals need controlled transfer streams instead of loose transcript stuffing. Long-horizon benchmarks need to grade the process that produced the answer, not only the answer.

## SkillHarm makes skill security lifecycle-aware

SkillHarm is the sharpest source today because it attacks the agent skill layer exactly where the stack is moving. The paper treats third-party skills as privileged workflow artifacts that agents are expected to follow implicitly. It evaluates two attack scenarios: Fixed-Payload Poisoning, where a poisoned skill compromises any task that invokes it, and Self-Mutating Poisoning, where a benign-looking execution mutates persistent skill content so harm appears only on later reuse. It also defines 12 skill-relevant risk types across data pipelines, system environments, and agent autonomy.

This matters because the skill layer is no longer harmless markdown. A skill can shape tool selection, file writes, memory writes, retrieval, approval language, and future behavior. One install-time scan is not enough if skills can be updated, patched, retrieved, or mutated after the first run.

Fit in the stack: skill registry, capability governance, third-party skill admission, persistent procedural memory, agent supply-chain security.

Implementable now:
- make production-admitted skills immutable during task execution;
- record skill source, version, body hash, manifest hash, and verification level in every trace;
- block skill self-modification unless it goes through a reviewed patch path;
- add lifecycle tests for install, retrieval, execution, update, reuse, quarantine, and rollback;
- treat a skill that writes files, memory, or tool config as a high-risk artifact even if its prose looks benign.

Tools, repos, and methodologies worth exploring:
- signed skill manifests, skill cards, semantic fuzzing, static risk scanners, file integrity checks, OPA/Cedar policy, OpenTelemetry trace fields, adversarial skill fixtures, reviewed skill-patch queues.

Implementability score: 0.82

Core source:
- SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction: https://arxiv.org/abs/2606.02540v1

## Continual learning eval has to separate transfer from memory stuffing

AGENTCL makes a useful correction to lifelong-agent evaluation. A benchmark should not merely ask whether an agent can remember old tasks or retrieve old conversations. It should construct task streams where earlier sub-solutions, evidence, or workflows are intentionally reusable in later tasks, then measure whether the agent actually extracts transfer value without interference from irrelevant experience.

The key design move is the contrast between compositional streams and naive streams. A compositional stream lets evaluators know what should transfer. A naive stream does not guarantee reusable structure. That distinction matters because many memory-heavy agents look competent when given enough context but still fail to build reusable procedures.

Fit in the stack: continual-learning harnesses, memory policy, skill promotion, trajectory replay, experience reuse.

Implementable now:
- create small task streams where prior evidence or sub-solutions should help later tasks;
- run a no-memory baseline, raw-episode retrieval baseline, summarized-memory baseline, and promoted-skill baseline;
- score forward transfer, negative transfer, forgetting, retrieval precision, and cost separately;
- log which prior episode or workflow actually influenced each later run;
- reject memory or skill promotion that improves easy repeats but hurts held-out transfer tasks.

Tools, repos, and methodologies worth exploring:
- compositional task streams, non-parametric memory ablations, transfer-gain metrics, experience ledgers, skill promotion gates, trajectory replay, held-out transfer fixtures.

Implementability score: 0.70

Core source:
- AGENTCL: Toward Rigorous Evaluation of Continual Learning in Language Agents: https://arxiv.org/abs/2606.02461v1

## ClinEnv shows process quality and outcome quality decouple in interactive agent benchmarks

ClinEnv is medical, but the benchmark lesson is general. It builds interactive, multi-stage inpatient simulations from real admissions. At every stage, the model must actively query four specialized agents before committing to medications, procedures, and diagnoses. The benchmark scores both final decisions with deterministic ontology-grounded matching and the information-gathering process that led there.

The useful result is not only that the strongest tested model reaches 0.31 decision F1. It is that outcome quality and process quality are sharply decoupled. A model can recover a plausible final diagnosis while still gathering information poorly, issuing redundant queries, or failing on management decisions later in the trajectory.

Fit in the stack: long-horizon interactive evaluation, specialist-agent orchestration, irreversible-decision scoring, process observability.

Implementable now:
- build staged task environments where the agent must gather evidence before committing;
- separate process score from outcome score;
- label irreversible decisions and late-stage management actions as distinct risk points;
- require evidence-query logs before final decisions;
- score redundant queries, missing evidence, bad sequencing, and unsupported commitments.

Tools, repos, and methodologies worth exploring:
- staged simulation harnesses, ontology-grounded matchers, specialist subagent mocks, trace-level process scoring, irreversible-decision labels, evidence-query budgets.

Implementability score: 0.53

Core source:
- ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents: https://arxiv.org/abs/2606.02568v1
