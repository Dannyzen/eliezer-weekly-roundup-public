# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-03

### Treat reusable skills as covert policy objects

Summary: SkillShift preserves declared functionality and valid outputs while steering shopping and dependency choices. PSR rises to 81.33% and 63.33% at 100% valid-output rate. Static scanners that catch direct injection do not distinguish SkillShift Attack skills from paired Clean skills. Audit skills as frozen policies, not only as packages.

Analysis: [daily strategy](2026-09-03/sovereignty.md#treat-reusable-skills-as-covert-policy-objects)
Core source: [paper](https://arxiv.org/abs/2609.02564v1)
Tools and methodologies worth exploring now: Skill Policy Integrity fixtures, frozen candidate sets, PSR and valid-output metrics, direct-injection positive controls, scanner-plus-behavior release gates
Implementability score: 0.72

### Bind remote tool calls to a fresh workload lease, not OAuth alone

Summary: ACLE-MCP names the post-authorization execution trust gap. A short-lived, sender-constrained capability lease is consumed by an Execution Gate before protected tool logic. In the local simulation, OAuth-only and connect-time attestation block none of six misuse families; full ACLE-MCP blocks the evaluated set at +25.7% p95 latency.

Analysis: [daily strategy](2026-09-03/sovereignty.md#bind-remote-tool-calls-to-a-fresh-workload-lease-not-oauth-alone)
Core source: [paper](https://arxiv.org/abs/2609.02690v1)
Tools and methodologies worth exploring now: invocation-scoped leases, workload-id and freshness binding, non-bypassable execution gates, substitution and stale-appraisal fixtures
Implementability score: 0.48

## Current implication

Skill admission, skill behavior, and remote execution are three different authority decisions. A package can pass install review and still steer later. A recommendation can stay schema-valid and still be a covert policy. A tool endpoint can stay OAuth-valid and still be the wrong workload.

## Previous structured update: 2026-09-02

### Treat loaded skills as delayed-authority objects

Summary: Defense-as-Skill implements the runtime guard as an installable skill. After a package is already loaded, SkillSonar checks proposed actions against the current user task and returns allow, replan, or confirmation. On Claude Code / GLM-5, N = 10, in-distribution attack success falls from 0.482 to 0.104 and out-of-distribution attack success from 0.606 to 0.115, with more utility than AcceptEdits. The guard is Markdown, so hard brokers still own effects.

Analysis: [daily strategy](2026-09-02/sovereignty.md#treat-loaded-skills-as-delayed-authority-objects)
Deep dive: [Defense as Skill](defense-as-skill/defense-as-skill.md)
Core source: [paper](https://arxiv.org/abs/2609.01487v1)
Tools and methodologies worth exploring now: dedicated guard skill, explicit consult-before-action, task-boundary object, allow/replan/confirm decisions, delayed-harm fixtures, allowlist-regression fixtures, sandbox and permission brokers as last word
Implementability score: 0.58
