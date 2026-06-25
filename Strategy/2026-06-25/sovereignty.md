# Strategy daily scan, 2026-06-25

## Thesis

The strategic signal today is that serious agent safety has to sit outside the agent's own address space. Prompts, output filters, and in-runtime guardrails can request cooperation. They do not create architectural control when the agent can reach tools, APIs, memory, or self-modification seams.

## Execution-time safety kernels move alignment below prompts

Core source: https://arxiv.org/abs/2606.26057v1
Supporting empirical trust signal: https://arxiv.org/abs/2606.26028v1

The Unfireable Safety Kernel paper makes a hard governance claim: if the control lives inside the agent runtime, the agent or its inputs can reach it. The proposed alternative is execution-time alignment: an external authorization layer that every privileged action must pass before execution.

The paper names four properties for architectural control:

1. Process separation from the controlled agent.
2. Pre-action enforcement on a structurally only path.
3. Fail-closed behavior at both request and system levels.
4. External signed evidence verifiable outside the controlled system's trust boundary.

This is the same direction the repo has been tracking through runtime governance, authority manifests, execution brokers, and memory authority. The difference is emphasis. A safety kernel is not another agent instruction. It is the path privileged actions have to traverse.

The ERC-8004 empirical study is useful supporting evidence. It shows that decentralized agent identity and reputation registries are weak trust roots when registrations do not expose live service endpoints and reputation feedback is not grounded in verified interactions. The strategic lesson is the same: reputation and claims are not enough. Trust has to be tied to enforceable paths and verifiable evidence.

Why it matters: autonomous agents are becoming active principals. They run code, call APIs, move data, use credentials, and mutate workspaces. A policy that only appears in prompt text or in the same runtime that proposes the action is too soft for that surface area.

How it fits into the stack:

- Runtime governance: put a reference monitor before side-effecting tool calls.
- Agent authority manifests: compile declared authority into enforceable kernel policy.
- Agent gateway governance: make the gateway the only accepted mutation path for privileged tools.
- Evidence provenance: sign allow, deny, timeout, and fail-closed decisions into the trace.
- Sandbox and broker layers: remove standing mutation credentials from the agent process wherever possible.

Practical tools, repos, and methodologies worth exploring now:

- Start with a thin external reference monitor around high-risk tools instead of trying to build the full formal kernel first.
- Require side-effecting tools to accept requests only from the monitor, not directly from the agent process.
- Encode principal, workflow, resource, effect, policy version, approval state, and live-state hash in each decision.
- Fail closed on parse failure, policy timeout, missing scope, stale policy epoch, or missing approval artifact.
- Store signed policy verdicts or at least tamper-evident decision records in the same trace as tool calls.
- Run adversarial fixtures where the agent tries to bypass the monitor, call tools directly, reuse stale capability handles, or modify its own guardrail files.

Implementability score: 0.54

The architecture is implementable, but the fully formalized version is not a weekend patch. A thin reference monitor around dangerous tools is achievable now. Proving the only-path invariant across real infrastructure is the hard part.

## Working conclusion

The governance boundary is moving below the prompt. For serious agent systems, the question is not whether the model has been instructed to be safe. The question is which external path the action must cross, whether that path fails closed, and what evidence proves the policy fired before the world changed.
