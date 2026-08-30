# Strategy Weekly Sovereignty Analysis - 2026-08-28

## Thesis

Sovereignty requires provenance, binding force, and authorization to outlive every representation change and remain enforceable until external effects are terminal.

## Preserve provenance and binding force through every transform

### Finding

When Context Gets Root identifies privilege escalation inside context assembly. Six coding-agent harnesses can reintroduce tool-origin content as user-level or system-effective instructions. Across 13 objectives, tool-to-user escalation reached a 97.3 percent mean success rate, and tool-to-system escalation reached 80.3 percent per attempt.

When "Must" Becomes "Maybe" identifies the adjacent handoff failure. Mandatory constraints weaken when they pass through summaries, plans, role transfers, and other representation changes. The content may remain present while its binding force disappears.

The same control applies to both: a transform may change representation, but not origin, privilege, or obligation semantics without a separately authorized release.

### Why it matters

Prompt hierarchy is ineffective when the harness silently promotes data. Policy language is ineffective when handoffs silently demote obligations. These are control-plane failures before they are model failures.

### Strategy fit

This is the provenance and constraint layer inside context-to-execution integrity. It maintains source identity, privilege class, transform lineage, loader identity, obligation type, satisfaction criteria, fallback, and execution consequence.

### Practical path now

- Attach immutable origin, privilege class, transform chain, and loader identity to every context item.
- Require privilege-monotonic transforms.
- Keep repository content, tool results, and retrieved memory in data-bearing message classes unless separately released.
- Represent mandatory constraints and blockers as typed records with explicit enforcement semantics.
- Reject summaries or handoffs that omit, soften, or contradict active constraints.
- Give permission reviewers the original provenance and transform history, not only the final prompt.

Implementability score: 0.86

Core sources:
- [When Context Gets Root](https://arxiv.org/abs/2608.27299v1)
- [When "Must" Becomes "Maybe"](https://arxiv.org/abs/2608.24569v1)

## Keep authorization live until the effect reaches terminal state

### Finding

When Tool Outputs Become Commands separates action induction from authorization. An untrusted observation may help construct a candidate call, but repeated appearance in history cannot create authority. The runtime checks the operation, target, scope, recipients, and argument support against the user's effect contract immediately before execution.

AID-Guard extends authorization through provider commit, ambiguous delivery, reconciliation, and recovery. One reservation lineage remains charged until the result is terminal or a certified no-effect state plus delivery fence permits a successor. Metis adds typed runtime events and terminal-result closure. ToolMinimize reduces argument disclosure after call construction and before execution.

### Why it matters

Approval at request start is too early. The request can mutate, provider state can change, responses can be lost, and retries can create duplicate effects. Idempotency keys and receipts help, but do not by themselves prove that the final provider effect came from the approved delegation.

### Strategy fit

This is the stateful effect-governance layer: effect contract, reservation, acting identity, canonical request, provider operation, commit-time validation, ambiguous state, reconciliation, terminal closure, and protected evidence.

### Practical path now

- Define the effect contract independently of observations and model history.
- Persist authorization identity, request digest, acting principal, provider operation, and effect lineage.
- Revalidate the exact request and current provider state at commit.
- Treat ambiguous outcomes as live obligations, not permission to retry.
- Normalize accepted, denied, failed, timed-out, cancelled, and reconciled results into typed terminal events.
- Minimize argument disclosure at the last responsible boundary and audit the rewrite.

Implementability score: 0.82

Core sources:
- [When Tool Outputs Become Commands](https://arxiv.org/abs/2608.27146v1)
- [AID-Guard](https://arxiv.org/abs/2608.21159v1)
- [Metis](https://arxiv.org/abs/2608.25322v1)
- [ToolMinimize](https://arxiv.org/abs/2608.24957v1)

## Make safety state outlive the agent trajectory

### Finding

Safety Does Not Compose shows why trajectory-scoped monitoring is insufficient for autonomous loops. An attacker can distribute individually benign fragments across iterations until persistent state enables an unsafe effect. Resetting the monitor discards the evidence. Geometric decay gives the attacker a fixed cooling-off period.

LoopHarness retains grounded risk evidence, memory-integrity state, effect budgets, rehydration checks, and authenticated clearance outside the inner agent loop. In the paper's main Track-B evaluation, the full configuration reduced overall attack success to 0.1 percent from 88.4 to 97.6 percent for weaker configurations while retaining 96.9 percent clean goal completion.

The week's lower-confidence adaptive prompt-injection work points in the same direction but should remain advisory. A learning loop may discover new attacks, but a model-mediated adaptive defense should not become the final authority boundary without deterministic release and rollback controls.

### Why it matters

A new trajectory, restart, subagent, retry, or long wait is an implementation detail, not a security reset. Safety evidence must live as long as the protected workflow and its unresolved effects.

### Strategy fit

This is persistent-state agent control: non-decaying risk evidence, effect budget, verifier uncertainty, rehydration integrity, scope-specific clearance, and cross-iteration attack evaluation.

### Practical path now

- Persist risk evidence, effect budgets, and clearance state beside durable workflow state.
- Keep high-confidence risk latched until an authenticated, scope-specific clearance event.
- Verify state integrity before rehydrating the next agent iteration.
- Test fragmented, delayed, restart, cancellation, and subagent-handoff attacks.
- Measure compounding attack success against iteration count and clean-goal completion.
- Keep adaptive detectors behind deterministic policy ceilings and versioned rollback.

Weakest point: the LoopHarness study uses one frozen model-role assignment and no multi-seed or multi-model replication. The adaptive prompt-injection method scored 0.38 this week because its learning loop remains operationally immature and model-mediated.

Implementability score: 0.60

Core sources:
- [Safety Does Not Compose](https://arxiv.org/abs/2608.27141v1)
- [adaptive prompt-injection defense](https://arxiv.org/abs/2608.19982v1)

## Working conclusion

The runtime must keep the original source class, obligation semantics, authority grant, risk evidence, and effect lineage intact from observation through terminal provider state. Models may propose transforms and actions. Only typed, stateful, independently reviewable control objects may promote them into authority.
