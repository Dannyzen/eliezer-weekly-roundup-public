# Strategy Daily Sovereignty - 2026-09-04

## Treat lifecycle-hook updates as a privileged control plane, not plugin metadata

HookPry attacks the update path that agent harnesses trust blindly. Lifecycle hooks bind host-privileged shell commands to runtime events such as session start, tool calls, and file edits. Those commands ship as configuration. They can fire at times the LLM never sees. Under a supply-chain threat model that controls only plugin metadata and hook configuration, a benign versioned plugin can be trojanized after install.

The paper evaluates seven harnesses: OpenHarness, OpenClaw, Claude Code, Codex CLI, OpenCode, Hermes, and WorkBuddy, across five backends, 25 combinations, 1,000 end-to-end runs. Verified E2E-ASR, binary, no partial credit, reaches a 77.9% unweighted macro-average across harnesses and 77.0% micro-average. Hermes is 92.5% overall. OpenCode is 90.6%. Claude Code is the hardest of the seven at 52.5%, still not a defense. Privilege Escalation averages 93.5%. Command and Control is the weakest category at 41.7%. Translated MCP tool descriptions reach only 56.0% E2E-ASR against 92.0% for native HookPry on the same 50 targets. Representative defenses remain blocked. Removing Temporal Decoupling blocks payload loading; removing LCI preserves loading but blocks later stages.

Why it matters: yesterday's SkillShift finding was that a skill can keep the declared task and still steal the decision. Today's finding is that a hook can skip the model entirely. Scanner-plus-behavior skill gates do not see a command that never entered the LLM trace.

Stack fit: untrusted data boundaries and runtime governance. Plugin install review, marketplace sync, and hook mutation are three different authority events. The last one is the one that executes.

Implementable now:

- deny unsigned hook mutation after install; pin hook command hashes at admission
- require hook events to emit an auditable record even when the LLM is not in the loop
- treat plugin update as a new admission, not a metadata refresh
- add fixtures that change only hook configuration on a previously trusted plugin
- keep hard brokers for host effects; Markdown guards cannot intercept a session-start shell

Do not take the paper's attack recipes as an implementation plan. The reusable object is hook-update admission, not HookPry.

Implementability score: 0.62

No official HookPry repository resolved. The paper cites an anonymous artifact and OpenHarness as a target, not as the method. Artifact status: claimed only / primary-source link present, not contents-inspected.

Core source: https://arxiv.org/abs/2609.03884v1

## Fresh memory does not authorize a stale plan

PlanFence names stale-plan execution: an executor can hold the latest shared facts and still act on a plan derived from an obsolete version. A planner cites requirement r3. Another agent commits r4. The executor receives r4 and still runs the plan derived from r3. Freshness of local state is not lineage validity of the pending action.

The protocol is small. Plans cite the exact public record IDs they used. Before an external action, the executor validates only the records that can affect that action, then replans once or blocks if validation is incomplete. In 30 controlled live workflows with a post-plan revision, a freshness-only owner-head check issued the obsolete action in every task (0/30 valid primary actions). PlanFence and centralized lineage each completed all 30 without an invalid action. Cost results are conditional: metadata sync has lower stall at low churn; PlanFence avoids repeated update-path coordination as churn and keyspace grow. The authors call these controlled safety and systems-cost results, not general task-accuracy gains.

Why it matters: shared-memory systems keep answering "is the replica current." The missing question is "is this action still derived from the current heads of its parents." ACLE-MCP yesterday bound remote tools to a fresh workload lease. PlanFence binds the plan itself to exact parent IDs.

Stack fit: memory-authority control plane and shared-state agents. Record IDs, not semantic keys, are the authorization object at action time.

Implementable now:

- stamp every plan with exact parent record IDs, not "latest requirement"
- validate only action-relevant parents at the effect gate
- replan once or block; do not silently splice a new fact into an old plan
- keep a freshness-only negative fixture that proves the replica can be current and the action still invalid

No public PlanFence repository resolved. Treat the protocol as a design reference until an artifact appears.

Implementability score: 0.58

Core source: https://arxiv.org/abs/2609.03340v1

## Current implication

A green functional test, a current replica, a trusted plugin, and a parsed tool-call rate can all be true while the runtime is already wrong. Acceptance needs a second oracle. Authorization needs parent IDs, not freshness. Hook updates need admission, not marketplace sync. Serving adapters need to be part of the measurement, or eval and RL will train the censored remainder.
