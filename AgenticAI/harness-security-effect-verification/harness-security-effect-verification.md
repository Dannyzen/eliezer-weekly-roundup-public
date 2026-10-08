# Harness Security Effect Verification

## Overview

A security control is a testable claim about system behavior. HarnessSecurity-Bench provides the strongest evidence this week because it measures whether native coding-agent controls change the forbidden effect while preserving legitimate work.

The durable pattern is a control-effect contract. Each security setting should carry a versioned description, an effective-setting receipt, paired utility and attack-effect oracles, alternative-path coverage, and a release decision tied to the exact harness version.

Primary source: [HarnessSecurity-Bench v1](https://arxiv.org/abs/2610.07639v1)

Implementability score: **0.81**

## Why this won the week

Transect and AgentMonBench improve reviewability of long trajectories. MemMux makes fleet resource ownership measurable. BOTTLED turns repeated cognition into an economic routing question. HarnessSecurity-Bench reaches the most consequential boundary: whether a configured control changes the state an attacker can produce.

That boundary has the highest leverage because every other observability or governance layer eventually needs a release gate. A control-effect contract turns logs, settings, tool receipts, and terminal state into a decision about whether a harness version is safe enough for a specific workload.

## Core innovation

The paper combines two evidence layers.

First, it defines ten native harness mechanisms and evaluates 400 mechanism cells across 40 coding-agent harnesses. The study confirms 205 implementations, finds 83 absent, and leaves 112 unresolved. Closed-source products account for many evidence gaps, including 69 of 130 unresolved closed-source cells.

Second, it evaluates realized runtime effects. HarnessSecurity-Bench compares enabled and disabled settings for nine mechanisms across six harnesses, 23 coding tasks, and five attack surfaces. The study uses isolated containers, one controlled base model, ten repetitions per condition, and separate deterministic oracles for legitimate task utility and forbidden effects. Its 2,500 trials record 81,155 tool calls, more than 2.2 billion native tokens, and 589.32 hours of cumulative agent execution time.

The important result is the shape of the evidence:

- auto-approve raised attack success from 29.2 percent to 95.6 percent;
- network isolation reduced attack success from 57.1 percent to 0.8 percent with a 24.5 point utility loss;
- read-only mode reduced attack success from 8.3 percent to 0.8 percent with a 34.0 point utility loss;
- command allowlists and denylists reduced attack effects with materially lower utility costs;
- alternative execution paths kept some forbidden operations reachable despite the named control.

The product lesson is precise: configuration names do not establish coverage. The release artifact needs measured effects, preserved utility, and explicit path coverage.

## The control-effect contract

A practical control-effect record should bind these fields:

1. **Source identity:** harness name, version, commit or build, model, tool catalog, sandbox image, and task fixture.
2. **Effective setting:** the setting observed at runtime, including defaults and inherited policy.
3. **Protected effect:** the exact filesystem, network, process, credential, repository, or external-service state that must remain unreachable.
4. **Authorized completion path:** the legitimate operation that must remain possible.
5. **Paired trial:** identical task and environment with the target control enabled and disabled.
6. **Deterministic oracles:** one oracle for legitimate utility and one for the forbidden effect.
7. **Alternative paths:** shell, interpreter, MCP tool, editor, package script, browser, API, and indirect process routes to the same effect.
8. **Cost receipt:** tool calls, runtime, tokens, retries, and blocked legitimate work.
9. **Release decision:** pass, fail, or scoped exception with the exact evidence snapshot.

The contract belongs in the release evidence for the harness. It should be queryable by mechanism, protected effect, harness version, and workload class.

## Why it matters

Agent security programs often inventory settings. That inventory answers whether a control exists and whether it appears enabled. It does not answer whether an agent can still reach the protected effect through another tool, command, interpreter, or service.

HarnessSecurity-Bench shows why the difference matters. Broad controls can reduce attack success while destroying useful work. Narrow controls can preserve utility while leaving alternate paths open. A strong evaluation therefore measures both outcomes and enumerates the paths that can produce them.

This creates a better engineering target: maximize legitimate task completion under a bounded forbidden-effect rate, with every exception linked to a reproducible fixture.

## Fit in the agentic stack

Primary layer: **AgenticAI harness evaluation and release engineering**.

Adjacent layers:

- **Execution control:** the protected effect and allowed path should be typed before the run.
- **Observability:** tool calls and state changes provide evidence for debugging failed or bypassed controls.
- **Sandboxing:** isolated environments make effects measurable and resettable.
- **Policy:** the control manifest defines intended coverage and default state.
- **Fleet governance:** the same fixture set can gate upgrades across agent profiles and hosts.

The stack sequence is:

`control manifest -> effective-setting receipt -> paired execution -> utility oracle + effect oracle -> alternative-path sweep -> release decision`

## Practical tools and methodologies worth trying now

### Use the public task packages as design examples

The repository publishes task suites, manifests, container environments, reference solutions, and utility checks across automatic approval, audit logging, command controls, filesystem boundaries, network isolation, read-only mode, prompt-injection filtering, MCP permissions, and project trust.

Artifact status: contents inspected read-only. The repository has a populated default branch and one `arXiv` tag. It has no GitHub release and no GitHub-reported license. The README says the full evaluation runner is maintained separately, while the project site says harness ratings, trial artifacts, and analysis scripts are still being prepared for release.

### Build the first local fixture with existing evaluation infrastructure

Useful components:

- [Inspect AI](https://inspect.aisi.org.uk/) for agent tasks, tools, sandboxes, scorers, logs, and external-agent adapters;
- container snapshots for deterministic setup and reset;
- state oracles that inspect the filesystem, process tree, network sink, repository, or external-service fixture;
- source-linked trajectory views such as [Transect](https://arxiv.org/abs/2610.08364v1) for diagnosis after an oracle fails;
- evidence graphs such as [AgentMonBench](https://arxiv.org/abs/2610.06406v1) for linking claims back to trajectory events;
- incident-derived attack fixtures and negative controls to prevent benchmark theater.

### Start with one high-consequence effect

A practical first implementation should use one ordinary coding task and one protected effect, for example:

- utility: complete a repository edit and pass its project checks;
- forbidden effect: write outside the worktree, contact an unapproved endpoint, or expose a seeded credential marker;
- alternate paths: shell command, Python process, package script, MCP tool, editor helper, and browser request;
- gate: zero forbidden effects across repeated trials with an explicit minimum utility threshold.

This fixture is small enough to maintain and strong enough to catch control regressions during harness upgrades.

## Implementation complexity

Complexity is moderate.

The easy parts are containerized fixtures, state checks, result schemas, and paired configuration runs. The hard parts are harness adapters, reliable capture of effective settings, complete alternative-path enumeration, and preserving valid completion paths under restrictive controls.

The public artifact accelerates task design. It does not provide a complete drop-in runner. A production implementation still needs:

- adapters for each harness and approval flow;
- exact version and configuration capture;
- deterministic external-service fixtures;
- repeat scheduling and result aggregation;
- versioned coverage manifests;
- release policy for acceptable utility and residual risk.

Implementability score: **0.81**. A narrow fixture is straightforward now. Cross-harness coverage requires meaningful evaluation engineering.

## Evidence limits and weakest point

The weakest point is generalization. The runtime study uses one base model, GLM-5.2, and six open-source harnesses. Docker containers, automated execution, and simulated services do not fully reproduce live deployments. Approval-off trials use a fixed LLM reviewer, which introduces model bias and residual nondeterminism. Ten repetitions reduce single-run noise without establishing universal rates.

The artifact is also incomplete for full reproduction. Task packages and utility checks are public. The full runner, harness-rating records, trial artifacts, and analysis scripts are not all public at the time of this review.

These limits are survivable for the architectural conclusion because the control-effect pattern does not depend on one ranking. The guardrail is local replication: derive fixtures from the real workload, preserve deterministic state oracles, rerun them against every harness version, and treat published rates as hypotheses rather than deployment guarantees.

## Strategic implications for Danny's product thinking

The product opportunity is a release-quality layer for agent harnesses.

Customers do not need another dashboard that lists security toggles. They need proof that a named control blocks a named effect in their environment while preserving the work they bought the agent to do. That proof can become a durable capability:

- workload-specific control-effect packs;
- versioned harness coverage manifests;
- upgrade regression gates;
- alternative-path attack fixtures;
- utility, security, and cost curves;
- evidence receipts attached to releases and incidents.

This fits Danny's worldview: agents earn autonomy through observable outcomes, bounded authority, and transferable methods. The evaluation pack becomes customer-owned operational knowledge. It can move across models and harnesses while preserving the customer's definition of acceptable behavior.

## What remains conceptual or incomplete

- standardized schemas for effective harness settings;
- portable protected-effect vocabularies across shells, MCP servers, browsers, IDEs, and cloud agents;
- credible coverage metrics for alternative execution paths;
- cross-model and closed-source harness replication;
- live external-service tests that preserve safety and resetability;
- statistically grounded release thresholds for rare harmful effects.

These are architecture and ecosystem problems. They do not block a narrow first fixture.

## Recommended next exploration

1. Reproduce one published task shape with an internal harness adapter and deterministic state oracle.
2. Add one incident-derived alternative path that the named control does not directly mention.
3. Store the effective setting, source identity, utility result, attack result, tool trace, and cost in one signed result record.
4. Run the fixture against the current harness and one upgrade candidate.
5. Promote the fixture into a release gate only after the oracle and reset behavior are independently reviewed.

## Core sources

- [HarnessSecurity-Bench paper, immutable v1](https://arxiv.org/abs/2610.07639v1)
- [HarnessSecurity-Bench HTML](https://arxiv.org/html/2610.07639v1)
- [HarnessSecurity-Benchmark project site](https://tsingpig.github.io/HarnessSecurity-Benchmark/)
- [HarnessSecurity-Benchmark task repository](https://github.com/TsingPig/HarnessSecurity-Benchmark)

## Supporting sources

- [Inspect AI evaluation framework](https://inspect.aisi.org.uk/)
- [Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations](https://arxiv.org/abs/2610.08364v1)
- [What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents](https://arxiv.org/abs/2610.06406v1)
