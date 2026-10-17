# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-17 Daily Scan

### Sandbox the server effect, not the tool description

Summary: MCP approval can authorize a process with ambient host permissions. Tool contracts need process-level filesystem enforcement.

Analysis: [sandbox the server effect, not the tool description](2026-10-17/sovereignty.md#sandbox-the-server-effect-not-the-tool-description)

Core source: [My Credentials, Please paper v1](https://arxiv.org/abs/2610.22301v1)

Implementable now:
- launch servers with explicit read-only and read-write roots;
- remove ambient credential and home-directory access;
- canonicalize paths after symlink expansion;
- bind roots to server revision and tool identity;
- test exploit, benign, and containment cases;
- fail closed when containment is unavailable.

Implementability score: 0.86

## Current implication

Capability governance belongs below model narration. Bind server identity, process permissions, path policy, sandbox health, and observed effects before approval can authorize execution.
