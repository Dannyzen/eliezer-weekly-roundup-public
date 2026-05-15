# Sandbox-Native Agent Workers

## Overview

The strongest finding from the last 7 days is that the execution substrate itself is becoming a first-class product surface for serious agents.

The clearest shipped proof point is OpenAI's April 15 update to the Agents SDK. The official announcement frames it as native sandbox execution plus a model-native harness. The `v0.14.0` release turns that into concrete runtime primitives: `SandboxAgent`, `Manifest`, `SandboxRunConfig`, persistent isolated workspaces, snapshots, resume support, sandbox memory, and local, Docker, or hosted sandbox backends.

That is more important than a normal feature release because it changes what the default agent should be. The new primitive is not just an LLM with tools. It is a bounded worker with a filesystem, mounts, resumable state, and an explicit execution backend.

## Core innovation

The innovation is not merely that the agent can run shell commands.

The real innovation is packaging long-horizon execution as a first-class worker abstraction:
- the workspace is declared through a manifest instead of being improvised at run time
- the execution boundary is explicit and backend-selectable
- state can be snapshotted and resumed instead of disappearing with the process
- memory becomes a workspace capability instead of hidden prompt residue
- the same agent model can run against local, containerized, or hosted sandboxes without changing the orchestration shape

This compresses several recent agentic-stack ideas into one shipped surface: artifact-first workspaces, harness architecture, isolation, and resumability.

## Why it matters

This matters because most agents still smuggle execution through an untyped shell tool and hope the rest works out. That is fine for short demos and bad for real work.

A serious agent needs:
- an execution boundary you can reason about
- durable state that survives across runs
- a clean way to mount repos, files, and object storage
- explicit backend choice for local, container, or hosted execution
- a worker model that can be paused, resumed, inspected, and replayed

OpenAI's SDK release does not solve every governance problem, but it moves the center of gravity in the right direction. Runtime design is leaving the appendix and entering the product surface.

## How it fits into the agentic stack

### Execution layer
The worker is no longer an implicit side effect of tool calls. It becomes a real runtime object with an explicit sandbox client and manifest.

### State layer
The workspace is durable state, not just scratch space. Snapshots and resume paths turn files, mounts, and generated artifacts into part of the system contract.

### Memory layer
Sandbox memory pushes learning from prior runs into the workspace itself. That is a better product shape than invisible context accumulation because it is scoped to the worker and can be managed explicitly.

### Security and governance layer
Isolation, run-as defaults, backend selection, and mount strategies make containment part of the runtime shape. That is a better foundation than bolting approvals onto an otherwise omnipotent shell loop.

### Orchestration layer
The outer orchestrator can stay thinner when long-running execution sits inside a bounded worker abstraction. This is exactly the direction implied by [File-as-Bus Workspaces](../file-as-bus-workspaces/file-as-bus-workspaces.md) and [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md).

## What is implementable now

You can apply this immediately:
- model long-running tasks as bounded workers with manifests instead of free-floating tool loops
- use `UnixLocalSandboxClient` for fast local iteration and `DockerSandboxClient` when you need cleaner isolation
- snapshot and resume runs instead of forcing every non-trivial task back into one uninterrupted session
- mount repositories, synthetic files, and remote storage deliberately rather than letting state sprawl into ad hoc temp paths
- keep worker memory explicit and scoped to the sandboxed workflow
- separate the outer orchestrator from the worker runtime so coordination stays thin and execution stays inspectable

## What remains conceptual

Several pieces still need stronger conventions:
- portable policy layers for credentials, network access, and approvals across sandbox providers
- better cross-provider guarantees so local, Docker, and hosted backends behave similarly enough for serious replay
- stronger audit trails that connect workspace diffs, traces, approvals, and final outputs into one evidence plane
- a less vendor-specific abstraction for sandbox-native workers across frameworks
- clearer defaults for when memory should stay inside a worker versus promote into a broader system memory service

## Practical tools, repos, or methodologies worth trying now

### Tools and repos
- [OpenAI Agents SDK repo](https://github.com/openai/openai-agents-python)
- [OpenAI Agents SDK v0.14.0 release](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0)
- [Sandbox Agents documentation](https://openai.github.io/openai-agents-python/sandbox_agents/)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

### Methodologies
- manifest-declared workspaces
- sandbox-native worker abstractions
- snapshot-and-resume execution
- thin orchestration over bounded workers
- explicit mount strategies for repos, files, and object stores
- cross-runtime scorecards from [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md)

## Implementation complexity

Medium.

The primitives are shipped and usable now, but the surrounding operational discipline still matters: mount design, backend choice, resume semantics, audit expectations, and policy boundaries.

## Implementability score

0.95

## Strategic implications for this stack

This strengthens a useful worldview update: the moat is moving lower in the stack.

Implications:
- serious agent products will compete on runtime design, not only on prompt quality or model access
- the important boundary is becoming the worker substrate: what it can mount, where it runs, what state it preserves, and how safely it resumes
- file-as-bus coordination and harness scorecards were not isolated ideas; mainstream frameworks are starting to ship the same assumptions
- sovereignty becomes more practical when backend choice is explicit instead of hidden inside a hosted black box
- long-horizon products should be designed around resumability, inspectability, and execution boundaries before chasing more autonomous behavior

## Core source links

- OpenAI announcement: https://openai.com/index/the-next-evolution-of-the-agents-sdk
- OpenAI news RSS item describing the release: https://openai.com/news/rss.xml
- OpenAI Agents SDK v0.14.0 release: https://github.com/openai/openai-agents-python/releases/tag/v0.14.0
- OpenAI Agents SDK repo: https://github.com/openai/openai-agents-python
- Sandbox Agents docs: https://openai.github.io/openai-agents-python/sandbox_agents/

## Especially useful secondary sources

- [File-as-Bus Workspaces](../file-as-bus-workspaces/file-as-bus-workspaces.md)
- [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md)
- Microsoft Agent Framework python-1.1.0: https://github.com/microsoft/agent-framework/releases/tag/python-1.1.0

## Working conclusion

The new default primitive is not an agent with one more tool. It is a resumable worker with a bounded computer.