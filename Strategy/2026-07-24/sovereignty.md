# Strategy Weekly Sovereignty - 2026-07-24

## Weekly thesis

Explicit state is not enough. A system can explicitly preserve the wrong target, admit a malicious capability, or centralize sensitive telemetry without proving that the object is correct or authorized. Sovereign agent infrastructure needs evidence-bearing boundary objects: target bindings re-derived before effects, capability admission receipts based on attempted behavior, and state or telemetry handles bound to identity, scope, retention, and revocation.

The strategic shift is from policy as instructions to policy as a mediated transition. Context may propose. Only the runtime should release authority.

## Target identity must be re-derived at commit time

[Binding Drift](https://arxiv.org/abs/2607.18316v1) separates silent target drift from propagation of an initially wrong entity. The controlled benchmark covers 200 workflows, 580 binding-scored steps, four enterprise domains, and eight model backends. Under injected errors, locking the first target increases pooled wrong actions from 907 to 2,746. A cheap independent re-verifier reduces wrong actions by 79 percent, close in aggregate to the paper's oracle comparator. In the natural synthetic setting, drift appears in 18 percent of eligible workflows.

The key lesson is unflattering: persistence can make the system more consistently wrong. A stored customer ID, repository path, database handle, or payment beneficiary is not authorization merely because it was resolved earlier.

Why it matters: long-running workflows cross time, models, retries, and operators. Every material effect needs a target binding that carries provenance and is re-derived against the original intent or a trusted resolver.

Stack fit:
- planning layer proposes a typed target binding;
- state layer preserves provenance, not only the identifier;
- execution-control layer rechecks target, arguments, and effect class;
- approval layer binds consent to the exact target and action manifest;
- receipt layer records the observed post-state.

Implementable now:
1. Define typed target objects with canonical identity, source evidence, tenant, scope, expiry, and confidence.
2. Re-resolve high-risk targets immediately before commit.
3. Deny and escalate disagreement instead of silently replacing one uncertain binding with another.
4. Inject wrong initial and mid-workflow bindings into tests.

Tools, repositories, and methodologies:
- [shashank-indukuri/binding-drift](https://github.com/shashank-indukuri/binding-drift), MIT code with CC BY 4.0 data and results
- JSON Schema action manifests, canonical resource IDs, policy engines, two-channel verification, post-state receipts

Implementability score: **0.82**

## Capability packages need effect-level admission tests

[OpenSkillRisk](https://arxiv.org/abs/2607.20121v1) evaluates 263 risky skills collected from public marketplaces across seven threat categories, three CLI harnesses, and thirteen models. Even the safest tested configurations still attempt unsafe actions in about 17 percent of cases. The failure modes matter more than the aggregate: agents fail to recognize risk, recognize it but act before intervening, or obey skill instructions beyond user intent.

This reinforces the week's memory and channel findings. Static review and model explanations are not enough because risk can emerge only when instructions compose with tools, environment state, or later triggers. Admission must be based on the first attempted unsafe effect in a controlled environment.

Why it matters: a skill, memory record, plugin, or tool description is executable influence. Marketplace provenance helps, but it does not prove behavior under the local harness and authority set.

Stack fit:
- registry stores source, digest, declared effects, dependencies, and version;
- quarantine environment supplies canary resources and no production credentials;
- runtime monitor records the first attempted unsafe effect;
- admission policy scopes the capability to tested resources and action classes;
- continuous evaluation reruns composition and update tests.

Implementable now:
1. Map OpenSkillRisk's seven threat classes into the local capability registry.
2. Run new or changed skills in a no-secret sandbox with canary files, hosts, and credentials.
3. Score attempted effects, not only final outcomes or model explanations.
4. Re-test skill combinations, memory retrieval sets, and tool-description updates.

Tools, repositories, and methodologies:
- [Miaow-Lab/OpenSkillRisk](https://github.com/Miaow-Lab/OpenSkillRisk), MIT, populated Docker, guard, scripts, and source tree
- [OpenSkillRisk dataset](https://huggingface.co/datasets/Miaow-Lab/OpenSkillRisk)
- sandbox canaries, egress allowlists, syscall and tool-call traces, signed manifests, lockfiles, composition fuzzing

Implementability score: **0.80**

## State handles and telemetry must be policy objects

The [MCP 2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) removes the protocol session and initialization handshake, adds routable method metadata, cache semantics, trace propagation, formal extensions, and full JSON Schema 2020-12. Stateful applications now carry explicit handles such as `basket_id` or `browser_id`. The protocol no longer hides state, but applications inherit the duty to scope and revoke it. The candidate was locked May 21 and the final specification is scheduled for July 28, so production migration still needs final-spec and SDK proof.

AWS's [per-agent unified observability](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-bedrock-agentcore-unified-observability-single-log-group/) makes a related move. Traces, prompts, structured logs, and stdout now share one per-agent CloudWatch log group. That simplifies correlation and policy, but also concentrates sensitive execution history under one boundary.

Why it matters: explicit handles and unified logs are useful only when identity, access, encryption, retention, export, and revocation are narrower than the authority or data they contain.

Stack fit:
- gateway validates operation metadata against request bodies and authenticated principals;
- application binds each handle to tenant, resource, scope, expiry, and revocation;
- conformance layer proves protocol behavior before deployment;
- telemetry layer binds prompts, tools, memory, identity, and stdout to one agent policy boundary;
- security layer tests cross-agent isolation and export controls.

Implementable now:
1. Run the official MCP draft conformance suite in staging and inventory sticky-session assumptions.
2. Treat every application handle as a scoped capability, not a convenient identifier.
3. Define per-agent IAM, CMK, retention, redaction, and export policy before unified telemetry migration.
4. Prove cross-agent log isolation and handle revocation with negative tests.

Tools, repositories, and methodologies:
- [modelcontextprotocol/conformance](https://github.com/modelcontextprotocol/conformance), active public suite with scenario and check structure
- MCP draft specification, JSON Schema 2020-12, W3C Trace Context, CloudWatch, ADOT 0.17.1+, IAM Access Analyzer, CMK policy tests

Implementability score: **0.90**

## Governance sequence

1. Identify every boundary where context becomes durable state or side effect.
2. Replace ambient identifiers with typed, scoped objects.
3. Attach independent evidence before release and post-state evidence after commit.
4. Test denial, expiry, revocation, disagreement, replay, and cross-tenant isolation.
5. Train or optimize only on trajectories that preserve those receipts.

## Strategic implication

The tempting default is to improve the model's judgment. The real cost is that judgment cannot prove which target was affected, which capability crossed the boundary, or which telemetry principal owns the evidence.

> Choose runtime-mediated evidence objects. You gain auditability, replay, and revocation, but give up some speed and architectural simplicity.

The weakest point is operational burden. Typed bindings, quarantine suites, conformance tests, per-agent policy, and receipts add latency and systems work. That burden is survivable because it can be introduced first on high-risk effects. The guardrail is progressive mediation: start with destructive writes, credentials, payments, external messages, and cross-tenant state, then expand based on measured failure.

## Evidence and caveats

- Binding Drift is a synthetic stress benchmark, not a deployment prevalence estimate. The independent verifier trades wrong actions for more clarification-like outcomes.
- OpenSkillRisk v1 was read for the version-bound claim, while arXiv now lists v2. The public MIT artifact was inspected read-only and not executed.
- The MCP source is a release candidate, not the final July 28 specification. Staging conformance is implementable now; production cutover is premature without final SDK compatibility proof.
- AgentCore is a managed AWS feature. The governance pattern transfers, but self-hosted stacks need equivalent OpenTelemetry, storage, encryption, and tenancy controls.
- NotebookLM remained disabled and untouched.
