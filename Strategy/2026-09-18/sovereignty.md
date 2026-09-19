# Strategy Weekly Sovereignty Analysis - 2026-09-18

## Thesis

Sovereignty requires an unbroken trust chain from discovery to effect. Registry presence, stable names, compliant messages, visible interfaces, and local guardrails are representations. The runtime must independently bind identity, authority, policy, resulting state, and accountability.

## Build a continuous trust chain from registry to effect

### Finding

A probability sample of 400 MCP servers found that only 48.8% initialized without repair. A separate census of 21,643 registry servers found that 40.58% of multi-version servers changed meaning or destination under stable identifiers and 4.16% redirected endpoint hosts. OATS then showed that package review does not establish action permission: 34.7% of 144 live-agent commands carried a consequence class absent from documentation code blocks.

The final boundary is transactional. Eight tool-effect anomalies show how retries, speculation, concurrency, and partial failure can leave duplicate, missing, provisional, or aborted state while every individual call reports success. A separate compositional-policy result shows why local compliance is insufficient: cumulative limits, separation of duty, and context-dependent policy must be recomputed over the whole trace.

### Why it matters

Trust decays at every translation: registry to package, package to runtime, runtime to command, command to effect, and local step to workflow. If any translation inherits trust automatically, an approved label can authorize changed or incomplete behavior.

### Strategy fit

This is the agent gateway and execution control plane. Admission manifests, action-time permission, transaction contracts, and trace-level policy form one continuous chain.

### Practical path now

- Probe startup and schema behavior before catalog admission.
- Pin package digest, source revision, schema hash, transport, endpoint origin, and approved authority.
- Reauthorize each side-effecting operator against current state.
- Require effect IDs, outcome lookup, idempotency keys, compensation preconditions, and visibility state.
- Evaluate cumulative and separation-of-duty policy over raw provenance before commit.

Implementability score: 0.86

Core sources:
- [Random MCP registry sample](https://arxiv.org/abs/2609.10962v1)
- [mcp-probe](https://github.com/itguruhaseeb/mcp-probe)
- [MCP silent-drift census](https://arxiv.org/abs/2609.14119v1)
- [Scan the Skill, Govern the Action](https://arxiv.org/abs/2609.12001v1)
- [OATS repository](https://github.com/pheo-ai/open-agent-trust-system)
- [Agent-tool effect anomalies](https://arxiv.org/abs/2609.15397v1)
- [Compositional policy](https://arxiv.org/abs/2609.18820v1)

## Keep binding constraints outside mutable context

### Finding

Across 1,800 trajectories in The Missing Boundary, restoring the original control boundary cut loss of control to zero. In the compaction ablation, preserving constraints also yielded zero while omitting them yielded 87%. Interaction-contract work adds the lifecycle shape: bind task revisions, referenced objects, role authority, control transitions, postconditions, evidence, dependency versions, and controller epochs.

### Why it matters

A model summary, compacted context, or handoff can omit the rule that made an action safe. Asking an old controller to stop is not the same as proving its authority can no longer admit new work.

### Strategy fit

This is context-to-execution integrity and operational state preservation. Binding constraints live in runtime-owned policy objects, and every action references the exact policy and controller epoch that authorized it.

### Practical path now

- Store binding constraints outside free-form summaries.
- Attach policy version and controller epoch to every queued action.
- Recheck constraints at tool admission and effect commit.
- Revoke old epochs before a new controller begins.
- Test compaction, cancellation, reconnect, retry, and handoff as authority transitions.

Implementability score: 0.87

Core sources:
- [The Missing Boundary](https://arxiv.org/abs/2609.11024v1)
- [Agent-Integrated Software](https://arxiv.org/abs/2609.11381v1)

## Put cross-principal communication behind a social harness

### Finding

Across 600 released scheduling runs, capable agents with basic messaging did not reliably produce satisfactory coordination across principals. Honest agents degraded under scale and concurrency, while faulty agents could stall or steer outcomes. The proposed social harness separates identity, ordered communication, personal firewalls, task-specific norms, and accountability from the underlying transport.

### Why it matters

A valid message proves only that a transport moved bytes. It does not prove who the end principal is, whether the transition is allowed, whether local authority permits the resulting effect, or who can investigate a violation.

### Strategy fit

This belongs above A2A or MCP connectivity and below local execution authority. It complements, rather than replaces, per-principal capabilities and exact-effect gates.

### Practical path now

- Sign envelopes with principal identity, task state, expiry, sequence, and allowed transition.
- Keep each principal's effect gate local and non-delegable.
- Encode one bounded workflow as a deterministic state machine.
- Append decision and violation receipts to an auditable log.
- Use released traces as fixtures before generalizing norms across task families.

Implementability score: 0.68

The public repository contains paper material and released traces, not a production social-harness runtime. General norms and consequence institutions remain conceptual.

Core sources:
- [Agentic Societies Need a Social Harness](https://arxiv.org/abs/2609.17527v1)
- [Social harness artifact](https://github.com/social-harness/social-harness-paper)

## Bind approval to the agent's actual observation

### Finding

Across 546 mobile tasks, 13 apps, five frameworks, and three models, UI-desynchronization attacks produced 77.9% static and 66.9% dynamic misleading rates. Affora's controlled studies support a concrete response: declare shared control identity, relationships, state, error, recovery, and terminal semantics for both human and machine readers. Its primary comparison improved task completion by about 23 percentage points over baseline.

### Why it matters

A user can approve one visible representation while the agent acts on a different accessibility tree, hidden control, stale target, or ambiguous state. Approval without observation parity is interface theater.

### Strategy fit

This is context-to-execution integrity at the browser and device boundary. The approval object must bind the exact observation, target identity, proposed action, and expected effect.

### Practical path now

- Capture screenshot, accessibility tree, target identity, and relevant state in one observation digest.
- Show the same target and effect semantics on the approval surface.
- Reject stale approvals when any bound observation changes.
- Add executable interface checks for identity, relationships, errors, recovery, and terminal success.
- Preserve before and after state receipts for consequential actions.

Implementability score: 0.66

Core sources:
- [UI desynchronization attacks](https://arxiv.org/abs/2609.16732v1)
- [Affora](https://arxiv.org/abs/2609.19125v1)

## Working conclusion

The weekly sovereignty rule is simple: no representation should authorize the next layer by itself. Registries, names, messages, summaries, local checks, and visible screens become trustworthy only when the runtime binds them to exact identity, current authority, global policy, resulting state, and durable receipts.
