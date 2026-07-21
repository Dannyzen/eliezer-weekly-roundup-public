# Strategy Daily Sovereignty - 2026-07-21

## Verdict

Self-hosting and typed plans do not create sovereignty by themselves. Sovereignty comes from owning the boundaries where persistent state can change and where a requested action becomes a committed effect.

Today's strategy findings sharpen both boundaries: layer OS controls around writable self-state, and make effects, policies, approvals, and trace commitments explicit before execution.

## Scan boundary

- Both promoted papers were submitted on 2026-07-20 and first listed on 2026-07-21.
- Primary PDFs were downloaded as documents on Bigs and checked with `pdftotext -layout`.
- The self-state reproduction artifact was inspected read-only. ETAS claims a Rust prototype but links no public implementation artifact.
- No external repository was cloned, installed, built, imported, or executed.

## Self-hosted agents need a protected self-state plane

Core source: [Self-State Attacks on Self-Hosted AI Agents](https://arxiv.org/abs/2607.17986v1)

Artifact: [self-state-attacks-os reproduction repository](https://anonymous.4open.science/r/self-state-attacks-os-C901)

Submission: 2026-07-20 14:16:55 UTC. First listed: 2026-07-21.

### What it found

The paper names a hard local-agent problem: a compromised agent can corrupt its own memory, instructions, identity, or configuration through the same legitimate filesystem writes it needs to function. At the OS layer, benign and malicious writes can be identical.

The evaluation defines a 23-cell attack matrix and realizes it as 43 concrete operations over self-state files. It collects 600 task slots across coding, research, operations, and generalist profiles using a lightweight OpenClaw-compatible harness, then evaluates prevention, workload-conditioned detection, and recovery.

The paper's recommended stack locks instruction and configuration layers, uses workload-conditioned detection for the remaining writable memory layer, and snapshots state every 15 events. That composition closes 19 of 23 canonical cells, leaving four memory-write cells structurally indistinguishable in at least one workload.

The tradeoff is severe enough to matter. The recommended L3 permission level reports 0.61 protection and 0.70 average functionality, but the operations profile retains only 11% workload success because runtime configuration writes are blocked. The workload-conditioned detector also reports per-event false-positive rates from 0.08 to 0.36 across profiles. There is no universal lock policy or detector threshold.

The anonymous artifact contains 1,050 files, the traces and 600 task slots, a 23-cell attack definition, seven replay experiments, and a no-dependency Python 3.10+ reproduction path. The code is marked MIT and the task corpus CC BY 4.0. It was inspected read-only, not executed.

The evidence has limits:

- one lightweight OpenClaw-style harness and one model generated the traces;
- two workload profiles are author-constructed;
- the anomaly detector has high false positives in sparse profiles;
- OS telemetry cannot determine semantic intent for in-distribution writes;
- recovery still needs a trustworthy corruption point and selective semantic repair.

### Why it matters

Persistent state is part of the authority surface. A sandbox that blocks writes outside the workspace does not protect the memory and instruction files that the agent is explicitly allowed to change. Self-state needs its own principal separation, policy, monitoring, provenance, and recovery design.

### Fit in the stack

- **Persistent-state control:** classify instruction, memory, identity, and configuration as separate policy layers.
- **Runtime governance:** enforce permissions and observe state changes outside the model process.
- **Memory authority:** preserve lineage, promotion, supersession, and rollback evidence.
- **Sovereignty:** keep backups and monitors under a principal the agent cannot rewrite.

### Implementable now

1. Inventory every file the agent reads back into future decisions.
2. Lock static instruction and identity files under a separate owner or approval path.
3. Separate mutable memory from configuration and credentials.
4. Journal every self-state change with run ID, source evidence, old digest, new digest, and policy verdict.
5. Snapshot state to storage the agent cannot modify, then test rollback and selective restore.
6. Train detection per workload and file class, with explicit false-positive budgets.
7. Accept that some authorized writes require semantic review above the OS layer.

Tools and methodologies worth exploring:

- Unix principals, ACLs, Landlock, immutable flags, inotify, auditd, Wazuh-style FIM, Btrfs snapshots, append-only journals
- the self-state artifact as a read-only threat-model and replay reference

Implementability score: **0.72**

The layered controls exist now. The hard part is preserving functionality and semantic recovery without granting the agent ambient write authority over its future instructions.

## Effect-typed execution makes authority visible before commit

Core source: [ETAS: An Effect-Typed Language for Agent Systems](https://arxiv.org/abs/2607.17780v1)

Submission: 2026-07-20 10:11:53 UTC. First listed: 2026-07-21.

### What it proposes

ETAS treats model-backed agents, prompts, tool calls, typed memory, approvals, policies, and traces as language semantics rather than framework conventions. A computation carries an ordinary type, an escaping effect row, and a persistent abstraction of the action trace it may request.

Trace specifications compile to monitors. Static checking can prove some requests safe before runtime and emit residual obligations when dynamic resources prevent a complete proof. Runtime events distinguish requested, handled, denied, and committed actions, so a handler cannot erase a request from authorization or audit.

The paper states preservation, progress, type and effect soundness, handler trace-transparency, and policy-safety results. It also claims a Rust prototype with a CLI, typed HIR checks, effect and policy diagnostics, checkpoint and resume interfaces, token and attempt limits, and trace-aware hooks.

The weakest point is direct: no public implementation repository is linked, and the paper presents an evaluation plan rather than a measured comparison against production frameworks. Treat ETAS as a design reference, not software to adopt today.

### Why it matters

Current agent frameworks scatter authority across prompts, middleware, callback code, tool schemas, deployment settings, and logs. ETAS shows the stronger target: effects and trace obligations should be inspectable before execution, and commit should remain distinct from request and handling.

### Fit in the stack

- **Context-to-execution integrity:** untrusted context can influence a proposal without gaining effect authority.
- **Execution control:** effect rows, trace monitors, approvals, and residual runtime checks.
- **Audit:** requested, denied, handled, and committed events remain explicit.
- **Recovery:** replay and checkpoint semantics know which actions are irreversible.

### Implementable now

Do not start by creating a new language. Lift the useful semantics into a thin runtime contract:

1. Give every tool a typed effect and protected resource set.
2. Compile workflow policy into a deterministic preflight monitor.
3. Keep request, approval, handling, denial, commit, and post-state as separate trace events.
4. Require residual checks when target, principal, data classification, or current state is only known at runtime.
5. Reject undeclared effects and replay of irreversible commits.

Tools and methodologies worth exploring:

- algebraic effects, capability systems, typestate, policy automata, Cedar, OPA, OpenTelemetry, exact-effect manifests, append-only traces

Implementability score: **0.39**

A thin effect manifest is buildable. ETAS itself is a new language with no public artifact or measured production evaluation, so adoption is currently conceptual.

## Watchlist not promoted

- [PydanticAI v2.14.1](https://github.com/pydantic/pydantic-ai/releases/tag/v2.14.1) fixes durable MCP instruction fetching under DBOS. Useful, but it does not change a control-plane layer.
- [CrewAI 1.15.5](https://github.com/crewAIInc/crewAI/releases/tag/1.15.5) adds authenticated skill-registry downloads. The release note is too terse to establish the security mechanism or boundary.
- [Phoenix v19.3.0](https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v19.3.0) improves OIDC transport and suppresses trace metadata when tracing is off. These are useful maintenance deltas, not today's strongest architecture signal.

## Working conclusion

The runtime must own two transitions the model cannot be trusted to govern: durable self-state mutation and effect commit. OS controls constrain the first; typed effects, policy monitors, and explicit commit records constrain the second.
