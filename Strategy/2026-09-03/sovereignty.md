# Strategy Daily Sovereignty - 2026-09-03

Yesterday said a loaded skill is delayed authority: install review is not enough, and a later user task can make a leak look useful. Today's complementary failure is quieter. The skill can keep the original task, keep a valid answer, and still change what the agent prefers.

Remote tool use has the same shape one layer down. OAuth can stay valid after the workload that will execute the call is no longer the workload you appraised.

## Treat reusable skills as covert policy objects

SkillShift formalizes Skill Policy Integrity: the policy induced by a skill must stay aligned with its declared functionality and the user-authorized objective. The attack is not prompt injection and not task hijacking. It is a semantically plausible skill that preserves the interface while steering the decision.

Measured on two fixed-candidate domains, with 50 queries each and three runs per query:

- Shopping recommendation: PSR from 37.33% to 81.33%, valid-output rate 100%.
- Python dependency selection: PSR to 63.33%, valid-output rate 100%.
- Direct-Skill Injection reaches near-100% PSR but is the noisy control. SkillShift is the stealth path.
- Frozen Attack skills transfer across Claude Haiku 4.5, DeepSeek v4-Flash, GLM-4.7, Gemini 3-Flash, and Qwen3.5-Flash without retraining.

Existing skill scanners fail the stealth case. skill-scanner-full, Aguara, Snyk Agent Scan, STARS, SkillSpector, and ProtectAI DeBerTa do not distinguish SkillShift Attack skills from paired Clean skills. Several of those tools do flag Direct-Skill Injection. Static scanning still has a positive control. It does not have a policy-integrity control.

Why it matters: a Hermes, Claude Code, or Codex skill that recommends a library, vendor, or destination is an externalized policy. If we only hash files, lint Markdown, and run SkillSpector, we will ship steered skills that look clean.

How it fits: this extends Defense-as-Skill rather than replacing it. The guard skill still consults before sensitive effects. SkillShift says the skill can steal the decision before any sensitive effect is proposed, inside a valid recommendation.

Implementable now:

- add paired clean/attack skill fixtures over frozen candidate sets
- measure selection lift and valid-output rate, not only scanner verdicts
- keep a direct-injection positive control so scanner regressions are visible
- treat unexplained PSR lift as a release blocker even when the schema is valid
- do not unsupervised-evolve guard skills from live third-party packages

Implementability score: 0.72

Caveat: evaluation is two domains, three runs per query, and detector case studies under specific configurations. No official SkillShift repository resolved. Unrelated GitHub repos named `skillshift` are not this paper.

Core source: [A Finger on the Scale](https://arxiv.org/abs/2609.02564v1)

## Bind remote tool calls to a fresh workload lease, not OAuth alone

ACLE-MCP names the post-authorization execution trust gap. A remote MCP endpoint can remain OAuth-authorized after execution moves to a substituted workload, uses stale appraisal, reuses authority from another sender, or traverses an undeclared downstream component.

The proposed object is an invocation-scoped capability lease. It is short-lived and sender-constrained. It binds expected workload, freshness, operation, object and parameter bounds, downstream constraints, and receipt obligations. A provider-side Execution Gate consumes the lease immediately before protected tool logic.

In the paper's local simulation:

- OAuth-only and attest-on-connect block none of six execution-misuse families.
- Full ACLE-MCP blocks the evaluated families and preserves the evaluated benign tasks.
- Request-level pooled p95 on normal allowed calls rises from 12.20 ms to 15.34 ms, 25.7% over OAuth-only, over 40 samples and ten repetitions.

Why it matters: FriendVM and any remote MCP tool already look "authorized" at connect time. That is the wrong moment for high-risk operations. The lease has to be minted for this call, this sender, this workload state.

How it fits: agent gateway governance and execution control. Authenticated routing remains necessary. It is not workload identity. ACLE-MCP is the missing bind between call authority and current provider-side state.

Implementable now:

- split connect-time OAuth from invocation-time admission
- for protected tools, require a short-lived lease that names workload id, appraisal freshness, operation, and object bounds
- consume the lease in a non-bypassable gate before the handler
- test substitution, stale appraisal, sender reuse, and undeclared downstream as first-class families
- do not claim general agent capability is unaffected; the paper itself says four benign families are too narrow for that

Implementability score: 0.48

The prototype uses Keycloak/OIDC, an MCP Python SDK server, and optional vTPM quotes. No public implementation repository resolved. Results are a local simulation, not an independent production deployment.

Core source: [ACLE-MCP](https://arxiv.org/abs/2609.02690v1)

## Current implication

Skill admission, skill behavior, and remote execution are three different authority decisions. A package can pass install review and still steer later. A recommendation can stay schema-valid and still be a covert policy. A tool endpoint can stay OAuth-valid and still be the wrong workload. Scanners and bearer tokens are telemetry until an outcome fixture or an execution gate says otherwise.
