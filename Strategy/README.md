# Strategy

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Tuesday, 2026-07-21

### Self-hosted agents need a protected self-state plane

Summary: a compromised local agent can corrupt its own memory, instructions, identity, or configuration through legitimate writes. OS defenses reduce the surface but cannot distinguish every malicious write from normal adaptation.

Analysis: [daily sovereignty analysis](2026-07-21/sovereignty.md#self-hosted-agents-need-a-protected-self-state-plane)
Durable topic: [Persistent-State Agent Control](persistent-state-agent-control/persistent-state-agent-control.md#july-21-update-writable-self-state-needs-layered-os-controls-and-semantic-recovery)
Core sources: [paper](https://arxiv.org/abs/2607.17986v1), [reproduction artifact](https://anonymous.4open.science/r/self-state-attacks-os-C901)
Implementable now:
- separate instruction, identity, configuration, credential, and memory policy layers;
- move monitors and backups under a principal the agent cannot rewrite;
- journal every self-state mutation with source, digest, run, and policy evidence;
- tune detection per workload and preserve a semantic review path for in-distribution writes.
Tools, repositories, and methodologies:
- Unix principals, ACLs, Landlock, immutable flags, inotify, auditd, Wazuh-style FIM, Btrfs snapshots, the reproduction artifact
Implementability score: 0.72

### Effect-typed execution makes authority visible before commit

Summary: model requests, tool effects, approvals, policies, and traces should be explicit semantics. Request, handling, denial, and commit must remain distinct events.

Analysis: [daily sovereignty analysis](2026-07-21/sovereignty.md#effect-typed-execution-makes-authority-visible-before-commit)
Durable topic: [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md#july-21-update-effect-types-make-requested-actions-visible-before-commit)
Core source: [ETAS](https://arxiv.org/abs/2607.17780v1)
Implementable now:
- give every tool a typed effect and protected resource set;
- compile policy into deterministic preflight and residual runtime checks;
- preserve request, approval, denial, handling, commit, and post-state separately;
- reject undeclared effects and replay of irreversible commits.
Tools, repositories, and methodologies:
- algebraic effects, capability systems, typestate, policy automata, Cedar, OPA, OpenTelemetry
Implementability score: 0.39

## Current implication

Local execution is not sovereign when the agent can rewrite its own authority state or turn untyped requests directly into effects. Protect self-state outside the model process, then require explicit policy evidence at commit.
