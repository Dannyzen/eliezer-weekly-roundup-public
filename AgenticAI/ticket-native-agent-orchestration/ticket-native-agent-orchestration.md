# Ticket-Native Agent Orchestration

Last updated: 2026-04-28

Core sources:
- OpenAI Symphony announcement: https://openai.com/index/open-source-codex-orchestration-symphony
- openai/symphony: https://github.com/openai/symphony
- Symphony SPEC.md: https://github.com/openai/symphony/blob/main/SPEC.md
- Codex App Server: https://developers.openai.com/codex/app-server/

## Thesis

The next useful control surface for coding agents is the issue tracker, not the chat session.

Interactive coding agents are powerful but attention-bound. A human can only supervise a handful of tabs, terminals, or agent sessions before the coordination cost eats the gain. Ticket-native orchestration changes the unit of work: the durable object is the task, not the conversation.

## Reference pattern

OpenAI's Symphony spec is the current best public reference. It defines a long-running automation service that:

1. polls an issue tracker on a fixed cadence;
2. dispatches eligible issues with bounded concurrency;
3. creates deterministic per-issue workspaces;
4. runs a coding-agent session inside each workspace;
5. loads runtime behavior from a repo-owned `WORKFLOW.md` contract;
6. stops active runs when issue state changes make them ineligible;
7. recovers from transient failures with retries and backoff;
8. emits operator-visible structured logs or a status surface.

That is enough to turn Linear, GitHub Issues, Jira, or another tracker into an agent control plane.

## Why this matters

Ticket-native orchestration creates several properties that session-native agents lack:

- **Durable state:** the issue records goal, status, dependencies, reviews, PR links, and handoffs.
- **Parallelism:** agents can work on unblocked tasks without a human juggling terminals.
- **Isolation:** one workspace per issue makes execution easier to inspect and clean up.
- **Reviewability:** proof-of-work artifacts can attach to the ticket where humans already decide what ships.
- **Policy locality:** workflow rules live in the repo and evolve with the codebase.
- **Failure recovery:** crashed or stalled agents can be restarted by the orchestrator instead of being forgotten.

## Minimum viable implementation

A small version should include:

1. a tracker query for eligible work;
2. a per-ticket workspace directory;
3. a runner wrapper for Codex App Server, Claude Code, OpenCode, or another agent CLI/API;
4. a repo-local workflow document with status transitions, validation rules, and proof requirements;
5. structured logs for dispatch, start, stop, retry, failure, PR, CI, and handoff events;
6. explicit concurrency limits;
7. cleanup for terminal issues;
8. a conservative trust posture for the first deployment.

## Governance requirements

Do not confuse orchestration with safety. A Symphony-style loop still needs:

- least-privilege tracker and repo credentials;
- sandbox or workspace boundary enforcement;
- explicit approval gates for destructive or external actions;
- protection against recursive task spam;
- evidence capture for each tool call and state transition;
- human review before merge until the workflow has earned trust.

## Tools and methodologies worth exploring

- OpenAI Symphony spec and Elixir reference implementation
- Codex App Server JSON-RPC
- Linear/GitHub Issues/Jira as task state machines
- `WORKFLOW.md` as a repo-owned agent contract
- per-ticket devcontainers, worktrees, or disposable VMs
- OpenTelemetry traces over dispatch, agent turns, CI, and review
- CI/CD gates that can be read and repaired by agents

## Implementability score

0.88

The pattern is implementable now with ordinary engineering tools. The remaining hard parts are safe credential separation, sandbox posture, reliable cleanup, and preventing runaway autonomous work creation.
