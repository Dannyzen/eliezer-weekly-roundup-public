# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-18

### Make capability changes pass owned evals

Summary: GitHub Copilot Evals adds repeatable behavioral tests for skills, custom agents, and MCP tools, with approval and before-and-after comparison built into the workflow.

Analysis: [Daily strategy](2026-11-18/sovereignty.md#1-make-capability-changes-pass-owned-evals)

Core source: [GitHub Copilot Evals public preview](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/)

Implementable now:
- owned evals for high-impact capabilities
- exact configuration and fixture version binding
- separate outcome, trajectory, and authority checks
- explicit approval for side-effecting runs
- replayable promotion receipts

Implementability score: 0.92

## Current strategic model

1. Admit capabilities through approved provenance channels.
2. Bind runtime permissions to exact principals and effects.
3. Require owned evals for every high-impact capability.
4. Re-run the same eval after model, harness, prompt, skill, agent, or MCP changes.
5. Fail closed when required behavioral proof is missing or stale.

## Browse

- [Daily roundup](../roundups/2026-11-18.md)
- [Daily strategy](2026-11-18/sovereignty.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Agent gateway governance](agent-gateway-governance/agent-gateway-governance.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
