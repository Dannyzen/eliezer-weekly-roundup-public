# Strategy Daily Analysis - 2026-06-23

Today's strategic signal is that agent governance is becoming an artifact problem. The serious control surface is not a policy paragraph saying an agent should be safe. It is a machine-readable record of what the agent can access, remember, change, delegate, and prove, plus runtime mechanics that revoke authority when the justifying subtask ends.

## AgentRiskBOM makes agent authority a machine-readable artifact

AgentRiskBOM names the gap left by SBOM, AIBOM, and MLBOM work. Those artifacts help document dependencies, model metadata, and training provenance, but they do not say enough about deployed agent authority: autonomy level, tool permissions, memory scope, credential scope, approval gates, audit signals, inter-agent communication rules, and external action capability.

The paper proposes AgentRiskBOM as an additive risk-scoping artifact over existing BOM layers. The useful part is not only the schema. It is the deployment discipline: produce a JSON-schema compliant artifact, score risk scenarios, detect deployment mutations, map controls, and generate reports before the system fails in production.

The evaluation is directionally strong. The authors test 13 open-source agentic systems across coding, RAG, and multi-agent archetypes, model 52 risk scenarios across 14 categories, report 100% schema validation over corpus artifacts, 14/16 native-equivalent capability coverage, and 100% detection of 33 structured authority-drift mutations. Risk thresholds still need human calibration, but that is acceptable. The artifact gives operators a place to calibrate.

Why it matters: agent platforms cannot govern what they cannot enumerate. A security review that says "this agent has tools and memory" is too vague. The deployable unit needs an authority bill of materials.

Strategic fit: runtime governance, agent gateway governance, evidence provenance, compliance, operational readiness, procurement review.

Implementable now:
- define a compact authority manifest for each agent workflow;
- include autonomy level, allowed tools, credential scopes, memory write paths, approval gates, delegation rights, external effects, and audit evidence fields;
- diff manifests across deployments and block unreviewed authority expansion;
- map each high-risk capability to a control: policy check, approval, sandbox, rate limit, or logging requirement;
- store the authority manifest next to code, config, and traces so review covers what the agent can actually do.

Tools, repos, and methodologies worth exploring:
- JSON Schema for authority manifests;
- CycloneDX or SPDX adjacency for linking SBOMs to agent authority artifacts;
- OPA, Cedar, or OpenFGA for control mapping;
- OpenTelemetry spans for authority decisions;
- CI checks that fail on new tools, credentials, memory scopes, or external effects without review.

Implementability score: 0.82

Core source: https://arxiv.org/abs/2606.21877v1

## PORTICO closes the lingering-authority gap with revocable capabilities

Lingering Authority identifies the next failure after a workflow gets a permission: the agent keeps authority after the subgoal that justified it is over. Coding agents often receive broad access for the whole task, even when a file, network, git, or write capability is needed only for one episode.

The PORTICO design is a reference monitor for revocable resource-and-effect capabilities. It compiles an explicit task contract into initial capabilities, grant rules, trusted closure predicates, and global deny rules. Capability expansions become opaque, epoch-bound handles tied to a specific task episode. When the episode closes, those handles disappear from the planner interface and stale replay is rejected before side effects occur.

The evaluation makes the control point concrete: in comparator tests, PORTICO rejects 10/10 post-closure capability reuses while a non-revoking baseline permits all 10/10. In a stale-write audit, PORTICO records 0/6 executed forbidden effects while the comparator records 6/6. The paper also reports validation across scripted traces and 6 live model traces covering file writes, git mutation, and network egress.

Why it matters: least-privilege is not static. An agent can need permission at turn 7 and become dangerous with the same permission at turn 12. Serious platforms need time-bounded and episode-bounded authority.

Strategic fit: agent gateway governance, runtime governance, least privilege, coding-agent safety, policy-as-code, capability attenuation.

Implementable now:
- model tasks as contracts with named subgoals and closure predicates;
- issue opaque capability handles instead of exposing raw credentials or broad tool access;
- bind each handle to principal, workflow, tool, resource, effect, and epoch;
- remove closed handles from the next planner context;
- reject stale handle replay before execution, not after logging;
- preserve grant, invoke, close, deny, and stale-replay events in the trace.

Tools, repos, and methodologies worth exploring:
- reference monitor in front of privileged coding tools;
- typed tool catalog with effect labels;
- OPA or Cedar policies over task stage and capability epoch;
- git and filesystem sandboxes with scoped write grants;
- OpenTelemetry spans for grant, invoke, closure, and denial events.

Implementability score: 0.76

Core source: https://arxiv.org/abs/2606.22504v1
