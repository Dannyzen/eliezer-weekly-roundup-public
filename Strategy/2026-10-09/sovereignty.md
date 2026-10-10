# Strategy Weekly Analysis: 2026-10-09

## Thesis

The strategic primitive is an evidence-bearing authority boundary. Agent proposals become authorized only when the runtime can identify the capability, mediate the effect path, supervise the live run, verify terminal obligations, and justify the chosen topology.

## Completion authority belongs to terminal state

ThinkingBox shows that repeated stateful success is far weaker than single-run success. ObligationGuard shows that safe actions can still produce an unsafe ending when required work remains undone.

The governance implication is direct: completion authority should require both achieved state and fulfilled obligations. A final answer, progress bar, or green subtask status cannot substitute for backend predicates, cleanup evidence, verification, rollback readiness, and handoff.

Implementable now: terminal-state contracts, positive obligation registers, repeated trials, failure snapshots, and unresolved-obligation gates.

Implementability score: 0.88

Core sources: [ThinkingBox article](https://huggingface.co/blog/microsoft/thinkingbox), [ThinkingBox paper v4](https://arxiv.org/abs/2608.19741v4), [ObligationGuard paper v1](https://arxiv.org/abs/2610.11773v1)

## Approval must mediate the protected effect

HarnessSecurity-Bench demonstrates that nominal controls can leave alternate execution paths open. The governance object should therefore name the protected effect, approved path, denied paths, utility oracle, attack oracle, and exact harness version.

The unflattering fact is that the public task repository does not include the full evaluation runner and has no detected license. The control-effect contract remains implementable because it can be built from local incident and acceptance fixtures without depending on the research code.

Implementable now: paired utility and attack fixtures, alternate-path enumeration, deterministic effect oracles, and versioned release receipts.

Implementability score: 0.81

Core sources: [HarnessSecurity-Bench paper v1](https://arxiv.org/abs/2610.07639v1), [task repository](https://github.com/TsingPig/HarnessSecurity-Benchmark)

## Runtime owns time, observation, and intervention

Transect makes long runs reviewable through a shared timeline. AgentTime shows that duration following depends on the model and harness, and that apparent on-time behavior may include artificial sleeping after work is done. OnTrack suggests that trajectory structure can support early warnings and selective abort.

The governance implication is that the scheduler, not the model, should own deadlines, active versus idle time, cancellation, recovery, and intervention policy. All of those decisions should share one event identity and receipt model.

The weakest evidence is automatic abort. OnTrack interrupted six runs, so the deployment sequence should be shadow, warn, human-approved pause, then narrow automatic abort for reversible cases.

Implementable now: normalized event streams, scheduler-owned deadlines, recovery checkpoints, shadow intervention, and intervention receipts.

Implementability score: 0.76

Core sources: [Transect paper v1](https://arxiv.org/abs/2610.08364v1), [AgentTime paper v1](https://arxiv.org/abs/2610.09944v1), [OnTrack paper v1](https://arxiv.org/abs/2610.12375v1)

## Catalog governance and action governance must converge

One Skill Too Many shows that capability selection can silently remove normative behavior while task completion remains green. NOMOS shows how written policy can become typed, statically checked gates around state-changing calls.

The combined governance object should carry capability identity, catalog precedence, conflict evidence, first-read receipt, policy source, compiled rule version, schema report, replay result, and effect receipt. This creates a trace from what the runtime intended to load to what it allowed to change.

The unflattering fact is that NOMOS withholds its compiler and runtime gate, and the skill-conflict repository has no detected license. A clean-room narrow policy compiler is feasible, while general policy compilation needs meaningful architecture and validation.

Implementable now: overlap scans, namespaces, first-read hooks, typed policy IR, schema validation, replay preflight, and deterministic state-change gates.

Implementability score: 0.70

Core sources: [One Skill Too Many paper v1](https://arxiv.org/abs/2610.11647v1), [replication package](https://github.com/ltroin/conflict), [NOMOS paper v1](https://arxiv.org/abs/2610.11030v1), [artifact repository](https://github.com/iamupd/NOMOS)

## Scale-out needs topology authority

The dynamic-concurrency study finds that parallel sub-agents usually cost more time and can reduce task success. The strategic error is to treat parallelism as an intelligence multiplier rather than a topology choice with coordination cost.

A topology authority should approve concurrency only when decomposition quality, write ownership, integration cost, budget, and benchmark evidence support it. Serial execution remains the safe default for tightly coupled repository work.

Implementable now: task-shape classification, single-writer boundaries, explicit merge stages, serial-versus-parallel trials, and workload-specific routing rules.

Implementability score: 0.86

Core sources: [dynamic-concurrency paper v1](https://arxiv.org/abs/2610.10263v1), [trajectory artifact](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)

## Strategic conclusion

The lifecycle needs one chain of authority: selected capability, compiled policy, mediated effect, supervised execution, verified terminal state, and justified topology. Break any link and the system can remain persuasive while becoming ungoverned.
