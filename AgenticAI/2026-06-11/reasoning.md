# AgenticAI Daily Analysis: 2026-06-11

Today's agent-stack signal is evented control. The best papers are not asking for bigger prompts or more generic autonomy. They are turning memory, tests, and skills into explicit runtime objects: append-only logs, deterministic slices, targeted probes, and policy planes.

## Project memory should be an event log plus a pre-action judge

PROJECTMEM is the strongest implementation signal today because it treats project memory as local runtime infrastructure, not as a hidden summary blob. The paper defines a local-first memory layer for AI coding agents that records issues, attempts, fixes, decisions, and notes as an append-only plain-text event log. It then projects that log into compact AI-readable summaries through MCP and adds a deterministic pre-action gate that warns before an agent repeats a failed fix or edits a known-fragile file.

Why it matters: most coding agents still start each run by rereading files and rediscovering decisions. PROJECTMEM names the cost directly: the session can spend thousands of tokens reconstructing project context before doing new work. The useful correction is not only retrieval. It is judgment. Memory should sometimes block or warn, not merely answer.

How it fits into the stack: this belongs at the boundary between memory systems and event-sourced agent runtimes. The raw event log is the evidence substrate. The MCP server is the retrieval surface. The pre-action judge is governance attached to memory consumption.

Practical tools, repos, and methodologies worth exploring now:
- `riponcm/projectmem` as a read-only implementation reference for local project memory and MCP exposure;
- append-only event logs for issues, attempts, decisions, fixes, failures, fragile files, and lessons;
- deterministic projections from raw logs into active-context summaries;
- pre-action gates that compare proposed edits against failed attempts and fragile-file records;
- trace IDs linking every retrieved memory to its event source.

Implementability score: 0.86

Core sources:
- [PROJECTMEM](https://arxiv.org/abs/2606.12329v1)
- [riponcm/projectmem](https://github.com/riponcm/projectmem)

## Deterministic layer slices catch regressions that aggregate agent scores hide

Layer-Isolated Evaluation is the cleanest deterministic-testing finding today. The paper decomposes a production ordering agent into architectural layers such as ontology pre-resolution, intent signals, routing, decomposition, escalation, safety, memory, and envelope/defense. Each layer gets a no-LLM pure assertion slice that runs in CI against a locked baseline.

Why it matters: aggregate task success is too blunt. The paper reports that injected local regressions can barely move the aggregate pass rate while the relevant layer slice collapses. That is exactly the failure mode serious agent teams face: dashboards say the agent is mostly fine while one scaffold layer silently broke.

How it fits into the stack: this is agent harness architecture and trajectory-aware evaluation. It says the deterministic scaffold around the model deserves its own fast regression suite before expensive end-to-end evals run.

Practical tools, repos, and methodologies worth exploring now:
- layer taxonomy for internal agents: routing, memory, tool selection, verifier, safety, escalation, lifecycle, and envelope;
- no-LLM pure mode for deterministic scaffold assertions;
- per-layer locked baselines in CI;
- controlled regression injection to prove the slices localize failures;
- separate reporting for aggregate score, layer score, and off-diagonal damage.

Implementability score: 0.91

Core source:
- [Layer-Isolated Evaluation](https://arxiv.org/abs/2606.11686v1)

## Skill security needs targeted runtime probes, not static inspection

Runtime Skill Audit is the best skills-as-control update today. The paper argues that a skill can look benign in documentation or code but become harmful only when invoked with a specific request, local asset, persistent state, or multi-step tool interaction. RSA responds by profiling risk-relevant interfaces, constructing the execution context needed to exercise them, running targeted probes, and assigning security labels from behavior-grounded traces.

Why it matters: skills are becoming installable operational authority. Static linting can catch obvious bad instructions, but it misses environment-dependent behavior. The useful testing question is not only what the skill says. It is what the skill-mediated agent actually does under the conditions that matter.

How it fits into the stack: this sits between skill registries, sandboxing, and runtime governance. Skills should have admission tests, periodic probes, and trace-linked verdicts, especially when they can read files, write files, call network tools, execute code, or persist memory.

Practical tools, repos, and methodologies worth exploring now:
- risk-interface profiles for each skill: file, network, shell, memory, credential, external API, and persistent-state access;
- targeted sandbox probes instead of one generic eval prompt per skill;
- trace labels for attempted exfiltration, unauthorized writes, hidden resource use, deceptive summaries, and permission laundering;
- Snyk Agent Scan as an adjacent practical scanner for agent, MCP, and skill surfaces;
- skill admission manifests that store risk class, probe set, last verdict, body hash, and allowed tool scopes.

Implementability score: 0.80

Core sources:
- [Runtime Skill Audit](https://arxiv.org/abs/2606.11671v1)
- [snyk/agent-scan](https://github.com/snyk/agent-scan)

## Watchlist: adapter benchmarks for general agent harnesses

Claw-SWE-Bench is worth tracking because it turns heterogeneous OpenClaw-style agent harnesses into comparable SWE-bench-style submissions with fixed prompts, runtime budgets, workspace contracts, patch extraction, and evaluator rules. I did not make it a top finding because it is more benchmark plumbing than new architecture, but the adapter-contract shape is useful.

Source:
- [Claw-SWE-Bench](https://arxiv.org/abs/2606.12344v1)

## Implementation readout

The immediate build target is not another memory summary or broad eval run. It is an evented harness core:
1. Store project memory and agent runs as typed append-only events.
2. Project active summaries and per-layer state from those events.
3. Gate proposed actions against remembered failures and fragile surfaces.
4. Run no-LLM layer slices in CI.
5. Probe high-risk skills dynamically before admission.

That loop is cheap enough to prototype now and strong enough to carry into the Friday synthesis.
