# Strategy Daily Analysis: 2026-05-13

Today's strategy signal is that agent authorization is moving out of chat policy and into tool-path infrastructure. MCP and browser agents need scoped consent, policy refinement, and live indirect-prompt-injection testing on the same surfaces attackers use in production.

## MCP and browser agents need scoped consent plus live indirect-injection tests

The Options, Not Clicks paper is useful because it treats MCP consent as a policy-design problem, not a UX checkbox. Broad "always allow" toggles are too coarse, and opaque LLM-only decisions are too hard to audit. The proposed Conleash middleware puts a risk lattice on the client side: safe calls inside known boundaries can be auto-permitted, risky argument combinations are escalated, user-defined invariants are enforced by policy, and repeated user decisions are refined into reusable rules. The paper reports 98.2% accuracy, 99.4% escalation capture, and 8.2 ms policy-verification overhead on 984 real-world traces.

IPI-proxy adds the browser-agent red-team counterpart. Enterprise browser agents often operate under domain allowlists, but allowlists do not protect against hidden instructions inside pages served by approved domains. IPI-proxy rewrites real HTTP responses from whitelisted domains in flight, injecting payloads from a deduplicated library of 820 attack strings across several published benchmarks, then tracks exfiltration callbacks. That is the right testing surface: not a mock page, not a model API probe, but the retrieved content stream the agent actually consumes.

The deeper strategy point is that MCP consent and browser retrieval are both tool-path governance problems. The runtime has to know which principal authorized the action, which arguments crossed a boundary, which retrieved content was untrusted, which policy fired, and which trace evidence proves the decision. Prompt-only warnings are not enough once a browser page or MCP tool call can drive side effects.

A related Microsoft Research signal reinforces the evaluation side: SocialReasoning-Bench finds that frontier agents often complete calendar or marketplace tasks while leaving value on the table for the user. It measures outcome optimality and due diligence, not only task completion. I am treating it as a supporting signal rather than today's core governance finding: the implementation move is still the same, but one layer higher. Delegated agents need explicit user-interest policies, not just success flags.

Why it matters: agent sovereignty depends on keeping authority legible. A user should not have to approve every harmless MCP call, but the system must escalate when arguments cross data, money, file, identity, browser, or external-communication boundaries. Browser agents should not be declared safe because they only visit approved domains; approved domains can still carry hostile content.

How it fits into the stack or strategy: this belongs in runtime governance, agent gateways, browser-agent safety, and MCP client design. The control plane should sit before action execution and before retrieved content becomes instruction-like context.

Implementable now:
- classify MCP tools by boundary: read-only, local file, network, credential, money, external communication, durable memory, and destructive action;
- define argument-level policies instead of only tool-level allow/deny lists;
- convert repeated user approvals into scoped rules with expiry and trace evidence;
- add indirect prompt-injection tests that rewrite real fetched pages from allowed domains before the browser agent reads them;
- log policy decisions, content rewrites, callbacks, approved scopes, denials, and overrides in the same trace as the tool action.

Tools, repos, and methodologies worth exploring:
- Conleash-style risk lattices and client-side MCP middleware: https://arxiv.org/abs/2605.11360v1
- IPI-proxy-style intercepting proxy tests: https://arxiv.org/abs/2605.11868v1
- SocialReasoning-Bench-style outcome/due-diligence metrics: https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/
- Open Policy Agent, Cedar, deterministic argument validators, browser proxy injection, exfiltration callback trackers, and trace-linked consent artifacts

Implementability score: 0.74

Core source links:
- https://arxiv.org/abs/2605.11360v1
- https://arxiv.org/abs/2605.11868v1
- https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/
