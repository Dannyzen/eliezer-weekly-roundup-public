# Strategy Daily Sovereignty, 2026-07-07

Today's strategy signal is untrusted data boundaries. The old split, prompt versus data, is too weak for deployed agents. Serious systems need to decide which observations are allowed to influence planning, which evidence can authorize action, and which content must remain quarantined even if it is useful.

## Untrusted data needs a boundary plane, not better reminders

Core sources:
- https://arxiv.org/abs/2607.05277v1
- https://github.com/ethz-spylab/untrusted-content-masking
- https://arxiv.org/abs/2607.05120v1
- https://arxiv.org/abs/2607.05029v1

Untrusted Content Masking, Agent Data Injection, and Forged Reasoning Attacks all point to the same strategic correction: agents need a boundary plane between observation and authority.

UCM handles the immediate browser case. It masks untrusted DOM regions before the planner sees them and routes necessary reads through a quarantined model with typed return values. ADI handles the tool-output case. It shows that malicious data can masquerade as trusted metadata or evidence without looking like an instruction. FARMA handles the memory case. It poisons remembered reasoning rather than factual memory, so future retrieval feels like the agent's own prior rationale.

The shared product lesson is direct: untrusted content is not merely dangerous text. It is a class of evidence that needs origin, scope, allowed uses, transformation lineage, and effect gates.

How it fits into the strategy layer:

- Agent gateway governance: tool and browser outputs need field-level trust classes.
- Runtime governance: the planner should not see high-risk untrusted content unless a policy grants it.
- Memory authority: recalled reasoning must preserve origin and derivation, not only semantic similarity.
- Evidence provenance: action authorization needs to know which evidence class justified the effect.

Implementable now:

- introduce a trust class field for every observation: trusted system state, user-provided task data, third-party content, derived summary, recalled memory, and quarantined answer;
- restrict which trust classes can authorize external effects;
- keep untrusted text out of the main planner where possible;
- expose narrow typed quarantine tools instead of raw text reads;
- log evidence lineage from observation to plan to action.

Tools, repos, and methodologies worth exploring:

- Untrusted Content Masking reference repo;
- AgentDojo-style prompt and data injection suites;
- memory-poisoning regression fixtures from FARMA-style attacks;
- OPA or Cedar policy over evidence class, data origin, principal, action, and target;
- OpenTelemetry spans for observation, quarantine, reveal, derive, authorize, and deny.

Implementability score: 0.78

The boundary plane is implementable on controlled surfaces now. The hard part is broad coverage across arbitrary web pages, heterogeneous SaaS APIs, memory summaries, and multi-agent handoffs.

## Agent data injection is the next gateway threat after instruction injection

Core source: https://arxiv.org/abs/2607.05120v1

ADI matters because it attacks the evidence channel. A malicious value can be placed where the agent expects data, such as metadata, fields, labels, IDs, deadlines, or records. The agent can then make a bad decision while never explicitly following a malicious instruction.

This is strategically worse than many prompt-injection demos because it looks like normal work. The agent reads an API response, extracts a value, and acts. If the gateway does not preserve field provenance, the trace may show a plausible business action with no visible jailbreak string.

Practical governance pattern:

1. Split tool outputs by trust class.
2. Mark untrusted fields before model exposure.
3. Require high-risk actions to cite trusted evidence or human approval.
4. Fuzz serialization boundaries, delimiters, nested fields, and user-controlled labels.
5. Deny actions when their decisive evidence came only from untrusted content.

Artifact status: the paper advertises a GitHub artifact under `compsec-snu/adi`, but the repository returned 404 through both GitHub CLI and REST in this cron run. Treat it as a paper-backed method, not a verified public tool, until that changes.

Implementability score: 0.64

The idea is immediately useful for red-team fixtures. Production enforcement needs schema changes and evidence lineage across tools and policies.

## Personal-agent sovereignty needs consent and platform-mediation tests

Core source: https://arxiv.org/abs/2607.05363v1

SovereignPA-Bench is the user-owned-agent version of the same boundary problem. A personal agent should not optimize only for task completion. It should preserve the user's current intent under platform mediation, evolving preferences, privacy constraints, consent limits, evidence quality, user burden, and manipulative incentives.

This is a strategy finding more than a drop-in implementation. The paper is useful because it names the evaluation target that local-first personal agents need: not just personalization, not just tool use, but user sovereignty under changing context and platform pressure.

How it fits into the strategic layer:

- Local-first agents: the user, not the platform, should own the agent's policy state and memory state.
- Agent authority manifests: tasks need consent scope, allowed evidence, burden limits, and revocation paths.
- Runtime governance: platform-provided suggestions should not silently override user interest.
- Product design: the agent should explain when a platform's incentive conflicts with the user's declared preference.

Implementable now:

- add consent scope and revocation fields to personal-agent task manifests;
- test preference changes across time, not only one-turn personalization;
- log when platform-provided information influences a recommendation;
- separate user burden minimization from silent automation;
- create fixtures where service incentives conflict with user intent.

Tools, repos, and methodologies worth exploring:

- SovereignPA-Bench's evaluation dimensions as a design checklist;
- local-first memory stores with origin, consent, and supersession metadata;
- approval receipts and user-visible policy manifests for recurring personal-agent workflows.

Implementability score: 0.43

The benchmark framing is valuable, but no public artifact resolved during this run. The immediate action is to copy the evaluation dimensions into product requirements and internal fixtures.

## Working conclusion

The sovereignty lesson is that trust is an evidence property. If an agent cannot say whether a value came from a trusted system, third-party content, a quarantined read, a recalled memory, or a platform-mediated incentive, it should not be allowed to turn that value into an external effect.
