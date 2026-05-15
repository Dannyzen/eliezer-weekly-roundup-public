# Embeddable Agent Kernels

Embeddable agent kernels are becoming a better product shape than UI-locked agents.

## Core thesis

The important architectural split is between:
- the **agent kernel** that owns reasoning, permissions, task state, tools, subagents, and background execution
- the **client surface** that presents this capability inside an IDE, CLI, chat app, ticket system, or internal dashboard

If those two are fused, every new surface becomes a fresh agent implementation problem. If they are decoupled, new surfaces become integration work.

## Why this matters

Most coding agents still behave like vertically integrated products. That is fine for demos, but it breaks down in real organizations where the same reasoning core needs to appear in multiple places:
- IDE extensions
- terminal tools
- chat and messaging gateways
- internal workflow tools
- approval and review dashboards

A reusable kernel changes the economics. Permissions, background jobs, memory, Todo handling, MCP integration, and subagent orchestration can be implemented once and reused everywhere.

## What a good kernel should own

### 1. Task state
Plans, Todos, checkpoints, and task transitions should live in the kernel so every client sees the same ground truth.

### 2. Permissions
Approval flows and action scopes should not be reimplemented differently in each surface.

### 3. Tool and extension plumbing
MCP servers, plugins, and skills should bind to the kernel as extension surfaces.

### 4. Subagents and background work
Delegation and long-running jobs belong in the shared runtime, not in UI glue code.

### 5. Session continuity
The kernel should reconstruct sessions safely across surfaces and asynchronous events.

## What to build now

- expose the agent core as a library or service instead of a single locked application
- keep client layers thin and mostly presentation-focused
- push permissions, task state, and background execution into the shared runtime
- define typed integration points for tools, memory, and delegated workers
- design clients to be replaceable without changing the reasoning engine

## What to avoid

Avoid these traps:
- rebuilding the same orchestration logic in each interface
- letting each client invent its own permission semantics
- storing task state in UI-local objects instead of the kernel
- treating chat, IDE, and automation channels as separate agent products when they need the same core behavior

## Representative sources

- Sema Code paper: https://arxiv.org/abs/2604.11045
- sema-code-core repository: https://github.com/midea-ai/sema-code-core
- sema-code-vscode-extension repository: https://github.com/midea-ai/sema-code-vscode-extension

## New April 2026 addition

### Sema Code makes the kernel-first pattern explicit
Sema Code is useful because it says the architectural quiet part out loud. The same reasoning kernel can power both an IDE extension and a messaging gateway. Once that pattern is explicit, it becomes easier to reason about how agent products should be packaged: kernel once, clients many.

## Working conclusion

Embeddable agent kernels are likely to matter more than the next one-off coding assistant shell. The durable advantage is not just a nicer interface. It is a reusable agent runtime that can be dropped into every interface where work already happens.
