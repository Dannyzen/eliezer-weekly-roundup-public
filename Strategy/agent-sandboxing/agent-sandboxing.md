# Agent Sandboxing

Agent sandboxing is becoming a durable part of the agentic stack because coding agents are now powerful enough to make ordinary developer environments unsafe by default.

The core lesson is blunt: local execution is not the same thing as safe execution. Running an agent on your own hardware does not help much if it still inherits your main user account, your SSH keys, your cloud credentials, and unbounded network access.

## Why this topic now

April 2026 produced a more operationally serious sandboxing signal than most governance writing does:
- `code-on-incus` packages isolated coding-agent execution as a hardened runtime with monitored sessions, protected paths, and automatic threat response
- Olivier Ligot's sandboxing guide argues for a simple but high-value pattern: use a dedicated non-admin user, shared workspaces, package-manager reuse, and optional network mediation instead of giving the agent your full workstation identity
- the broader agent tooling conversation is moving from "can the agent code?" to "what exactly can it touch while coding?"

Core sources:
- code-on-incus: https://github.com/mensfeld/code-on-incus
- Running AI agents in a sandbox: https://oligot.be/posts/ai-sandbox/

## Core thesis

A coding agent should run inside a workspace with:
- scoped filesystem access
- no default access to durable credentials
- bounded network reach
- interruptibility
- preserved evidence for inspection and replay

If those properties are missing, the agent runtime is still basically a privileged shell with better marketing.

## What to build now

### 1. Separate the runtime principal from the human principal
Never run a coding agent inside the same account that holds your long-lived secrets and broad host privileges.

Minimum viable approach:
- dedicated non-admin user for agent sessions
- shared repository folder only where needed
- no inherited SSH keys, Git credentials, or cloud secrets unless explicitly mounted

### 2. Treat network access as a privilege, not a default
Many coding tasks do not need arbitrary outbound network access.

Useful controls:
- proxy-based allowlists
- monitored egress
- firewall rules that prevent bypassing the proxy layer
- selective secret injection at the proxy or mediation layer instead of exposing raw credentials to the agent

### 3. Preserve the workspace and kill the session cleanly
A sandbox is more useful when it supports operator response.

Required properties:
- pause or kill switch
- session persistence for review
- filesystem diffability
- logs or traces tied to the exact runtime session

### 4. Protect the host from incidental convenience
The dangerous path is usually the convenient one.

Avoid:
- bind-mounting the whole home directory
- copying host SSH config into the sandbox
- sharing Docker or other privileged sockets casually
- assuming local models remove the need for containment

## Practical stack to try now

### Lightweight pattern
- dedicated non-admin OS user
- shared project directory only
- package manager or dotfile setup that can be reused safely across users
- optional proxy and firewall controls

### Stronger pattern
- Incus/LXC or microVM-backed workspaces
- protected path policies
- monitored egress and credential isolation
- automatic pause or kill on suspicious behavior

## Selection rubric

Use stronger sandboxing when one or more of these are true:
- the agent can install packages or run arbitrary tests
- the repo contains production credentials or deployment paths nearby
- the workflow touches infrastructure or external services
- multiple agent sessions may run concurrently
- the agent has enough autonomy to branch, modify, and execute without turn-by-turn approval

A lighter-weight dedicated-user pattern may be enough when:
- the work is local-only and low privilege
- the repository is already scrubbed of durable secrets
- network access can be heavily constrained
- a human is reviewing every material step

### Read-only mounts and writable overlays are becoming default containment
Shannon v1.1.0 is useful category signal because it bakes containment into the product: read-only repository mounts, writable overlay workspaces, structured exploit queues, and ephemeral workers. That is the right direction for any agent with enough autonomy to analyze source and execute real attacks. A killable sandbox is not enough; the workspace also needs a clean separation between what the agent can read, what it can mutate, and what evidence survives the run.

Useful pattern:
- mount the target source or data read-only
- give the agent a separate writable overlay or scratch volume
- preserve workspaces and reports for audit
- keep high-risk agent work inside self-hosted runners or disposable environments

Source:
- [Shannon v1.1.0](https://github.com/KeygraphHQ/shannon/releases/tag/v1.1.0)
- [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)

## Current read

Agent sandboxing is not a niche hardening detail. It is becoming part of the default operating model for serious coding-agent use. The winning pattern is not "trust the model less" in the abstract. It is "give the model a smaller, killable, inspectable world to work inside."
