# Strategy Daily Sovereignty Analysis - 2026-08-18

## Scope

The strategy finding comes from an immutable arXiv v1 submission inside the strict 48-hour window and first listed on 2026-08-18. The paper and PDF were inspected as primary sources. No external repository was cloned or executed.

## Delegation must narrow authority and close over prior actions

Bounded Agents argues that static per-call permissions are structurally insufficient for multi-agent systems. An action can be individually allowed and still complete a prohibited sequence. A subagent can also inherit more authority than its delegated task needs unless the chain narrows scope, budgets, and composition rules at every hop.

The proposed Agentic Principal Chain evaluates six authorization conditions against accumulated session state and enforces the decision outside the model. Across 3,154 benchmark instances, the reported AgentDojo exfiltration rate fell from a 75% to 100% range down to 0% across four domains, and all 544 InjecAgent data-stealing cases were blocked. Intent binding reduced destructive outcomes from 38.6% to 4.0% and manipulation from 90.5% to 12.1%. The paper reports 0.24 ms p99 authorization latency on an idle host, but utility fell by 8.6 and 13.9 percentage points in two AgentDojo settings.

Why it matters: authority is a session object, not a list of allowed tool names. The control plane needs to know who delegated what, the remaining budget, which action combinations are forbidden, and whether an approval token binds the exact action instance.

Practical paths:
- create a signed authorization envelope at session start;
- narrow resources, actions, data classes, budgets, and expiration at every delegation hop;
- evaluate prohibited compositions over the action history before admission;
- bind approvals to action type, target, parameters, session, and single-use nonce;
- fail closed when policy, evidence sink, or budget state is unavailable;
- measure both attack blocking and utility loss before strict rollout.

Caveat: this is a single-author paper. It reports a reference implementation and public evaluation material, but the exact artifact URL was not resolved from the primary arXiv page during this scan. The utility cost is material, and composition soundness depends on a complete restriction set and serialized admission.

Implementability score: 0.76

Core source:
- https://arxiv.org/abs/2608.15888v1

## Working conclusion

Delegation safety is not inherited trust. Every hop should attenuate authority, every action should be checked against accumulated state, and every approval should authorize one exact effect.
