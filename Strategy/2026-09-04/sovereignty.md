# Strategy Weekly Sovereignty Analysis - 2026-09-04

## Thesis

Sovereignty requires that freshness, trust, and declared interfaces never stand in for lineage, admission, or exact-effect authorization.

## Treat lifecycle hooks and loaded skills as delayed-authority objects

### Finding

HookPry attacks the update path that agent harnesses trust blindly. Lifecycle hooks bind host-privileged shell commands to runtime events such as session start, tool calls, and file edits. Those commands ship as configuration. They can fire at times the LLM never sees. Under a supply-chain threat model that controls only plugin metadata and hook configuration, a benign versioned plugin can be trojanized after install.

The paper evaluates seven harnesses: OpenHarness, OpenClaw, Claude Code, Codex CLI, OpenCode, Hermes, and WorkBuddy, across five backends, 25 combinations, 1,000 end-to-end runs. Verified E2E-ASR, binary, no partial credit, reaches a 77.9% unweighted macro-average across harnesses. Hermes is 92.5% overall. Claude Code is the hardest of the seven at 52.5%, still not a defense. Privilege Escalation averages 93.5%. Native hooks beat translated MCP descriptions (92.0% vs 56.0% on the paired 50-target set).

SkillShift is the quieter adjacent failure. A skill can keep the declared task and a valid output interface while steering shopping and dependency choices. PSR rises to 81.33% and 63.33% at 100% valid-output rate. Static scanners that catch direct injection do not distinguish Attack skills from paired Clean skills.

Defense-as-Skill is the complementary control, not a replacement for brokers. An installable Markdown guard sits beside untrusted task skills, checks proposed actions against the current user task, and returns allow, replan, or confirmation. On Claude Code with GLM-5, N = 10, in-distribution attack success fell from 0.482 to 0.104. Adding an allowlist to AcceptEdits collapsed protection. The guard is still instruction-following.

### Why it matters

SkillShift showed that a skill can keep the declared task and still steal the decision. HookPry showed that a hook can skip the model entirely. Scanner-plus-behavior skill gates do not see a command that never entered the LLM trace.

### Strategy fit

This is untrusted data boundaries plus runtime governance. Plugin install review, marketplace sync, and hook mutation are three different authority events. The last one is the one that executes. Loaded skills are delayed-authority objects: install-time vetting remains necessary and is no longer sufficient.

### Practical path now

- Deny unsigned hook mutation after install; pin hook command hashes at admission.
- Require hook events to emit an auditable record even when the LLM is not in the loop.
- Treat plugin update as a new admission, not a metadata refresh.
- Add fixtures that change only hook configuration on a previously trusted plugin.
- Audit skills with paired clean/attack selection fixtures, not scanner verdicts alone.
- Keep a task-conditioned consult-before-action guard, then a hard broker that can still deny the effect.

Do not take HookPry's attack recipes as an implementation plan. The reusable object is hook-update admission.

Implementability score: 0.62

No official HookPry repository resolved. Artifact status: claimed only. SkillShift likewise exposes no public implementation repository in the daily notes. Defense-as-Skill is a design-plus-eval reference.

Core sources:
- [HookPry](https://arxiv.org/abs/2609.03884v1)
- [SkillShift](https://arxiv.org/abs/2609.02564v1)
- [Defense-as-Skill](https://arxiv.org/abs/2609.01487v1)

## Freshness is not lineage, and OAuth is not execution-time trust

### Finding

PlanFence names stale-plan execution: an executor can hold the latest shared facts and still act on a plan derived from an obsolete version. A planner cites requirement r3. Another agent commits r4. The executor receives r4 and still runs the plan derived from r3. Freshness of local state is not lineage validity of the pending action.

The protocol is small. Plans cite the exact public record IDs they used. Before an external action, the executor validates only the records that can affect that action, then replans once or blocks if validation is incomplete. In 30 controlled live workflows with a post-plan revision, a freshness-only owner-head check issued the obsolete action in every task (0/30 valid primary actions). PlanFence and centralized lineage each completed all 30 without an invalid action. The authors call these controlled safety and systems-cost results, not general task-accuracy gains.

ACLE-MCP names the post-authorization execution trust gap. A short-lived, sender-constrained capability lease is consumed by an Execution Gate before protected tool logic. In the local simulation, OAuth-only and connect-time attestation block none of six misuse families; full ACLE-MCP blocks the evaluated set at +25.7% p95 latency.

CIPR shows the repository side: poisoning risk depends on how the user invokes the agent. Trusted invocations activate untrusted repository paths. The invocation is part of the threat model, not a trusted wrapper around it.

### Why it matters

Shared-memory systems keep answering "is the replica current." The missing question is "is this action still derived from the current heads of its parents." A valid OAuth token can likewise stay true after the workload that will execute the call is no longer the workload you appraised.

### Strategy fit

This is the memory-authority control plane, shared-state agents, and gateway governance. Record IDs, not semantic keys, are the authorization object at action time. Workload leases, not connect-time tokens, are the authorization object at tool dispatch.

### Practical path now

- Stamp every plan with exact parent record IDs, not "latest requirement".
- Validate only action-relevant parents at the effect gate.
- Replan once or block; do not silently splice a new fact into an old plan.
- Keep a freshness-only negative fixture that proves the replica can be current and the action still invalid.
- Bind remote tool calls to invocation-scoped workload leases instead of connect-time OAuth.
- Treat the user invocation as an activation plan over untrusted repository content.

No public PlanFence or ACLE-MCP repository resolved. Treat both protocols as design references until artifacts appear. CIPR has a public repository.

Implementability score: 0.58

Core sources:
- [PlanFence](https://arxiv.org/abs/2609.03340v1)
- [ACLE-MCP](https://arxiv.org/abs/2609.02690v1)
- [CIPR](https://arxiv.org/abs/2608.30686v1)
- [CIPR repository](https://github.com/StarConnor/CIPR)

## Isolate capabilities at the resource, not the model's explanation

### Finding

The week's highest-implementability strategy findings were destination allowlists and resource-identity permission checks. Prompt-injection work showed that removing outbound capabilities from components that read untrusted content, then enforcing destinations and data classes outside the model, remains the cheap control. Permission checks that bind to the exact resource, model, route, and configuration used scored 0.97. User policy as preference, not standing authorization, scored 0.84.

Persona-execution separation and plan-first information-flow labels belong in the same layer. The persona may evolve in tone and presentation. Execution remains faceless, audited, and tied to one stable operational identity. Confidentiality, integrity, provenance, and control labels must survive persistent artifacts.

### Why it matters

Asking the model to recognize injection, or asking a plugin marketplace to stay trusted, is the wrong layer. The resource actually used, the destination actually reached, and the effect actually released are the objects that can be checked.

### Strategy fit

This is agent gateway governance, untrusted data boundaries, and context-to-execution integrity. Preference, standing policy, and exact-effect authorization remain three separate objects.

### Practical path now

- Bind permission checks to the exact resource, model, route, and configuration used.
- Remove outbound capabilities from components that read untrusted content.
- Enforce destinations, data classes, and typed effects outside the model.
- Keep user preference, standing policy, and exact-effect authorization as three separate objects.
- Separate mutable persona from stable execution identity, credentials, state, and audit.
- Retain confidentiality, integrity, provenance, and control labels across persistent artifacts.

Implementability score: 0.91

Core sources:
- [capability isolation against prompt injection](https://arxiv.org/abs/2608.27092v1)
- [user policy as preference](https://arxiv.org/abs/2608.27443v1)
- [resource-identity permission checks](https://arxiv.org/abs/2608.27311v1)
- [Claude Code v2.1.251](https://github.com/anthropics/claude-code/releases/tag/v2.1.251)

## Working conclusion

The runtime must keep lineage, admission, and exact-effect authorization intact from observation through terminal provider state. A current replica, a trusted plugin, a valid OAuth token, and a declared skill interface can all be true while the runtime is already wrong. Models may propose transforms and actions. Only typed, stateful, independently reviewable control objects may promote them into authority.
