# Strategy Daily Analysis: 2026-11-02

## Scope

The Monday, November 2 arXiv listing is live. Both selected v1 papers were submitted October 30 and first listed November 2. External repositories were inspected read-only only.

## 1. Authorize effects across every interface, then bind the decision to commit state

Cross-Interface Authorization argues that a policy decision can be interface-invariant while executable authorization is route-specific. The same effect may be reachable through GUI clicks, CLI commands, APIs, scripts, or MCP tools, each with different defaults, parsers, identities, and durable sinks.

The proposed profile-bounded protocol inventories effect-bearing routes and sinks, normalizes routes into effect semantics, issues route-bound witnesses, rechecks mutable state at commit, and requires a matching receipt. Its fixed-deployment evidence includes an independent checker accepting 3,464 retained traces and rejecting 26 of 26 semantic regressions, 48 of 48 instrumented adapter calls committing, and 15 of 15 unbound cases failing closed.

Why it matters: approving a GUI action does not safely authorize an equivalent shell or API call unless the runtime proves the same bounded effect. Discovery filtering alone is insufficient because another client can bypass it.

Fits into strategy: execution control below interfaces and above durable side effects.

Implementable now:
- enumerate GUI, CLI, API, script, and MCP routes for consequential effects;
- normalize route inputs into one typed effect manifest;
- bind grants to principal, route, effect, version, expiry, and state;
- revalidate mutable preconditions immediately before commit;
- require sink receipts that match the authorized effect;
- test bypass, stale-state, alternate-route, and default-value mutants.

Evidence caveat: guarantees are profile-bounded to fixed, versioned deployments. Adapter evidence is not a theorem about future upstream changes. No dedicated public implementation repository was identified.

Implementability score: 0.64

Core source: [Cross-Interface Authorization for AI Computer-Use Agents](https://arxiv.org/abs/2610.41397v1)

## 2. Treat tool-call traces as sensitive behavioral data

PrivacyTrace shows that protocol-visible tool names, arguments, returned results, and cross-session linkage can reveal user attributes without conversation access. Across 1,000 synthetic profiles, 4,000 trajectories, four domains, and real interactions with tools from 25 MCP servers, the default attack reached 26.25% profile-inference success versus 17.97% from prior-only guessing. Four attacker models ranged from 25.29% to 28.32%.

Why it matters: traces are operational evidence and a privacy side channel. Centralized observability, debugging exports, vendor telemetry, and shared evaluation corpora can expose behavior beyond prompts or final responses.

Fits into strategy: telemetry governance, data minimization, and untrusted-data boundaries.

Implementable now:
- classify tool arguments and results as sensitive before logging;
- separate operational receipts from payload captures;
- redact identifiers and high-signal attributes at collection time;
- restrict cross-session joins by purpose, principal, and retention window;
- keep trace stores tenant-isolated and short-lived;
- run profile-inference audits against exported telemetry.

Evidence caveat: profiles and scenarios are synthetic. The public repository is newly released, has no formal release, and its license is unspecified.

Artifact status: contents inspected read-only. The repo includes generation, attack, evaluation, MCP-server, data-card, documentation, and test surfaces.

Implementability score: 0.78

Core source: [How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces](https://arxiv.org/abs/2610.41885v1)

Read-only artifact: [AI45Lab/PrivacyTrace](https://github.com/AI45Lab/PrivacyTrace)

## Strategic cut

Make effect identity route-independent and authorization route-bound. Collect the smallest receipt that proves the effect. Full tool traces should be exceptional debug artifacts with explicit purpose, access, and retention controls.
