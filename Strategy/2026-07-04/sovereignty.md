# Strategy Daily Sovereignty, 2026-07-04

Today's strategic pattern is permission before power. The useful agent platform will not only expose tools. It will mediate runtime authority with user-aware permissions and behavior evidence.

## Runtime permission UX is a security primitive, not an approval popup

Source links:
- Janus paper: https://arxiv.org/abs/2607.01510v1
- Janus repository: https://github.com/GraceBrigham/Janus

Janus is useful because it treats user involvement as an evaluable systems design problem, not a product checkbox. The paper defines a playground for runtime permission management with Janus-Core, a modular agentic system, and Janus-Harness, an automated evaluation framework. It implements six permission assistants across a design space, evaluates them across three scenarios and three synthetic responders, and concludes that user input can materially strengthen privacy and security while AI augmentation can reduce cognitive load.

The repository is public and current. It includes an interactive runner, an evaluation harness, scenario definitions, metrics, and interchangeable permission-assistant designs such as auto-approve, constitution, policy suggestion, risk assessment, risk-assessment autonomous, and user confirmation.

Why it matters: approval dialogs are not governance. A serious execution-control plane needs an escalation policy that knows when user context is necessary, when automation is safe, when fatigue makes repeated prompts dangerous, and how permission decisions get logged as durable evidence.

Fit in the stack: agent execution control plane, runtime governance, agent gateway governance, and user-facing sovereign agent products.

Practical implementation path:
- Represent permission requests as typed objects: actor, resource, capability, action, data class, risk, source evidence, proposed effect, and fallback path.
- Route permission decisions through explicit assistant modes rather than one generic ask-user gate.
- Add synthetic and recorded responder profiles for always-yes, always-no, alignment-aware, fatigued, and context-rich users.
- Measure false approvals, false denials, user prompts per task, task completion, and attack resistance.
- Store permission decisions as grant or denial artifacts bound to the run trace.

Tools, repos, and methodologies worth exploring now:
- `GraceBrigham/Janus` for permission-assistant designs and harness structure.
- HCP-style grants and handles as the authority object model.
- Cedar, OPA, or OpenFGA for deterministic permission checks around the user-facing assistant.
- Permission-fatigue fixtures in the agent harness.

Implementability score: 0.74

The harness and design-space concepts are implementable now. The production challenge is tying user-facing permission UX to durable grants, provider resource canonicalization, and clear denial evidence without making the product unusable.

## Skill admission moves from provenance to behavior evidence

Source link:
- Cloak and Detonate: https://arxiv.org/abs/2607.02357v1

Skill marketplaces create a sovereignty problem. A community skill can carry procedural instructions, bundled scripts, hidden resources, install-time hooks, and runtime behavior that inherits the agent's authority. Provenance helps, but provenance does not prove behavior.

Cloak and Detonate shows why this matters. SkillCloak can preserve malicious behavior while changing payload appearance, bypassing static scanners at high rates. SkillDetonate changes the control plane: execute the skill in a sandbox, materialize hidden instructions during execution, and detect malicious effects through file, process, context, and network evidence.

Strategic implication: public skill catalogs should be treated like package registries plus malware sandboxes, not like prompt libraries. A skill should not gain repository, shell, credential, or browser authority until it has passed admission checks tied to the exact runtime policy.

Fit in the stack: runtime governance, agent sandboxing, agent gateway governance, and skills-as-control.

Practical implementation path:
- Separate provenance verification, static scanning, behavior detonation, and production admission.
- Require skill manifests to declare side effects, tool scope, network needs, memory access, and credential needs.
- Run new and changed skills against fake secrets, fake repos, and egress traps.
- Attach the detonation trace to the skill's admission record.
- Deny or quarantine skills that need broad ambient authority.

Tools, repos, and methodologies worth exploring now:
- Sandbox-native workers for detonation.
- Static triage plus dynamic taint, not static triage alone.
- Skill manifests and lockfiles.
- Egress allowlists, fake secret canaries, and marker files.

Implementability score: 0.62

The policy is implementable now, but robust behavior evidence is operationally heavy. A cheap first lane catches obvious malware. A serious lane needs coverage against trigger conditions, model-dependent execution, staged payloads, and environment-specific behavior.

## Working conclusion

The strategic thesis is simple: authority has to become a measured runtime object. User permission, skill admission, and sandbox behavior evidence should create grants and denials that the agent runtime can prove later.
