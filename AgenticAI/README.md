# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-25 Daily Scan

### Quantitative goal persistence is the missing long-horizon agent metric
Summary: PushBench turns a common long-horizon failure into a measurable defect: agents stop before an external verifier confirms enough distinct valid work units. The practical fix is an explicit progress ledger and verifier-owned completion gate outside model memory.

Analysis: [daily reasoning analysis](2026-05-25/reasoning.md#quantitative-goal-persistence-is-the-missing-long-horizon-agent-metric)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [Push Your Agent](https://arxiv.org/abs/2605.23574)
Implementable now:
- add target-count, accepted-item, duplicate-key, verifier-result, and remaining-backlog fields to long-horizon tasks;
- reject self-reported completion until verifier-owned criteria pass;
- label false completion, duplicate submission, repeated work, and progress drift separately.
Tools, repos, and methodologies worth exploring:
- verifier-owned work-unit ledgers, task-state machines, duplicate-key normalization, external completion validators, trajectory labels for repeated work
Implementability score: 0.76

### Operations agents need falsifiable fault-injection harnesses
Summary: The agent-breakage paper argues that autonomous Kubernetes operations claims need controlled faults, ground-truth scoring, agent-disabled baselines, and outcome-labeled state/action tuples. Ops agents need the same kind of falsification substrate that tests gave coding agents.

Analysis: [daily reasoning analysis](2026-05-25/reasoning.md#operations-agents-need-falsifiable-fault-injection-harnesses)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [agentic Kubernetes measurement paper](https://arxiv.org/abs/2605.23058), [agent-breakage repo](https://github.com/odmarkj/agent-breakage)
Implementable now:
- build a small disposable fault catalog for staging infrastructure;
- compare autonomous agents against agent-disabled baselines;
- score diagnosis, action correctness, recovery, and side effects separately;
- store `(state, action, outcome)` tuples for regression and future training.
Tools, repos, and methodologies worth exploring:
- Kubernetes staging clusters, chaos engineering, OpenTelemetry, pre-registered scoring, agent-disabled baselines, `odmarkj/agent-breakage` as a read-only pattern
Implementability score: 0.63

### Skill systems are becoming trainable and auditable state
Summary: SkillOpt treats a skill document as external trainable state with bounded edits, held-out validation, and rejected-edit memory. OpenSkillEval adds ecosystem-level skill auditing against realistic artifact-generation tasks. Skills need validation and rollback, not just more files.

Analysis: [daily reasoning analysis](2026-05-25/reasoning.md#skill-systems-are-becoming-trainable-and-auditable-state)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [SkillOpt](https://arxiv.org/abs/2605.23904), [OpenSkillEval](https://arxiv.org/abs/2605.23657), [OpenSkillEval project](https://yingjiahao14.github.io/OpenSkillEval-Web/)
Implementable now:
- add validation fixtures to high-value skills;
- require proposed skill edits to list expected gains and at-risk regressions;
- accept patches only after held-out tasks improve or review approves the tradeoff;
- log loaded skill hashes and validation status in traces.
Tools, repos, and methodologies worth exploring:
- git-backed skills, held-out validation tasks, artifact graders, skill hash logging, Pydantic skill contracts, OpenSkillEval-style task categories
Implementability score: 0.68

## Previous structured update

The prior daily scan for 2026-05-24 focused on terminal-coded browser workspaces, API/MCP skill compilation, schedulable tool waits, and stateful work-product evaluation: [2026-05-24 reasoning](2026-05-24/reasoning.md).
