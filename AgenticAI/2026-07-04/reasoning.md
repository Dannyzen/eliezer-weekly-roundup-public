# AgenticAI Daily Analysis, 2026-07-04

Today's signal is not another larger agent harness. It is preflight control: analyze the agent program before it runs, predict expensive evals cheaply, and detonate untrusted skills before they inherit workspace authority.

## Agent program static analysis becomes the new preflight gate

Source links:
- AgentFlow: https://arxiv.org/abs/2607.01640v1
- When Agents Do Not Stop: https://arxiv.org/abs/2607.01641v1

AgentFlow and IAL-Scan are best read as one implementation pattern. Agent applications are now source-code systems with framework-level semantics that normal AST or call-graph tools miss. Prompts, tools, memory, model calls, handoffs, policies, and agent constructors are dependency edges, not comments.

AgentFlow names the object: an Agent Dependency Graph. It represents agents, prompts, models, capabilities, memory states, and control policies as typed nodes, with component, control-flow, and data-flow edges. The paper reports implementation across five representative frameworks, evaluation on 5,399 real-world agent programs, richer Agent BOM generation than AST-only baselines, and 238 taint-style prompt-to-tool risks.

IAL-Scan names a specific failure class on top of the same premise: infinite agentic loops. It abstracts heterogeneous agent code into a framework-independent Agent IR, builds an Agentic Loop Dependence Graph, and checks whether feedback paths can repeatedly reach costly or state-growing operations without an effective bound. The evaluation reports 74 potential findings across 6,549 LLM agent repositories, with manual review confirming 68 failures across 47 projects and 91.9% precision.

Why it matters: agent CI should not only run tests. It should statically recover the agent graph, emit an Agent BOM, detect prompt-to-tool taint paths, and prove that every expensive or side-effecting feedback path has a real bound.

Fit in the stack: AgenticAI runtime, coding-agent control plane, sessionful loops, skills-as-control, and harness architecture.

Practical implementation path:
- Parse repo-local agent code for framework constructs: agent definitions, model calls, tool decorators, handoffs, memories, routers, policies, and termination controls.
- Emit an Agent BOM with agent, prompt, model, tool, memory, policy, and data-source nodes.
- Add prompt-to-tool and memory-to-tool taint checks before deployment.
- Add loop coverage checks: max turns, recursion limits, retry limits, state-growth caps, and side-effect gates must cover the actual feedback path.
- Treat static findings as preflight blockers for high-risk agents and warnings for low-risk prototypes.

Tools, repos, and methodologies worth exploring now:
- Tree-sitter or framework-specific AST extractors for LangGraph, OpenAI Agents SDK, CrewAI, AutoGen, and custom Hermes agents.
- CodeQL or Semgrep-style rules for known framework constructs.
- Agent BOM JSON as a CI artifact.
- Prompt-to-tool taint fixtures and loop-bound fixtures in the agent harness.
- The new durable topic: [Agent Static Analysis](../agent-static-analysis/agent-static-analysis.md).

Implementability score: 0.72

The first version is implementable now as a framework-specific extractor plus CI checks. A framework-agnostic ADG with high precision across real repos is harder, but the direction is clear enough to start.

## Proxy benchmarks can make agent routing cheap enough to run continuously

Source links:
- PACE paper: https://arxiv.org/abs/2607.02032v1
- PACE code: https://github.com/neulab/pace
- PACE-Bench dataset: https://huggingface.co/datasets/neulab/pace-bench

PACE attacks the cost problem directly. Full agentic benchmark runs on SWE-Bench, GAIA, and similar environments can cost thousands of dollars and take days. PACE asks whether a compact set of non-agentic instances can predict full agentic benchmark scores well enough for model development, selection, and routing.

The reported result is strong enough to matter operationally: across 14 models, 4 target agentic benchmarks, and 19 non-agentic benchmarks, PACE-Bench predicts target agentic scores with leave-one-out mean absolute error under 4%, Spearman correlation above 0.80, and pairwise model-ranking accuracy around 85%, at much less than 1% of the full agentic evaluation cost. The public artifacts are useful: `neulab/pace` contains the prediction pipeline, and the Hugging Face `neulab/pace-bench` dataset exposes target subsets for GAIA, SWE-Bench, SWE-Bench Multimodal, and SWT-Bench.

Why it matters: model routing needs fresh evidence, but full agent evals are too expensive to run every time a model, prompt, or tool harness changes. A proxy benchmark is not a replacement for final eval. It is a continuous smoke test for routing and model-choice decisions.

Fit in the stack: trajectory-aware evaluation, model-router governance, agent harness architecture, and agent serving runtime.

Practical implementation path:
- Keep a compact proxy suite per workflow class: coding repair, research, browser use, multimodal workspace, and tool planning.
- Run candidate models through the proxy suite before allowing router changes.
- Log predicted full-agent score, confidence interval, cost, latency, and known blind spots.
- Use full agent evals for release gates, but use proxy evals for daily regression and router shadowing.
- Compare proxy predictions against occasional full evals and retire proxy items that stop predicting the target.

Tools, repos, and methodologies worth exploring now:
- `neulab/pace` for subset selection and regression.
- `neulab/pace-bench` for released proxy instances.
- Existing model-router traces as calibration data.
- Shadow routing based on proxy scores before online routing.

Implementability score: 0.86

This is highly implementable because the code and dataset are public and the first use case can be offline: run proxy instances, fit or reuse the regression, and compare predicted rankings before changing routing policy.

## Skill malware defeats static scanners, so skill admission needs detonation

Source link:
- Cloak and Detonate: https://arxiv.org/abs/2607.02357v1

Cloak and Detonate is the strongest skills finding today because it breaks a comforting assumption. Static skill scanners are useful, but a malicious skill can preserve behavior while changing visible payload form.

The paper evaluates SkillCloak against eight scanners and 1,613 in-the-wild malicious skills. Self-extracting packing bypasses every scanner at over 90%, while structural obfuscation bypasses over 80% on most static scanners and reaches 96% on a hybrid scanner. The proposed countermeasure, SkillDetonate, executes skills in a sandbox and detects behavior through OS-boundary information-flow evidence. It reports 97% attack detection at a 2% false-positive rate and 87% detection on real-world malicious skills.

Why it matters: if a skill can run with the agent's workspace, terminal, credential, browser, or repository authority, install-time text review is not enough. Skill admission needs a behavioral stage.

Fit in the stack: skills-as-control, sandbox-native workers, coding-agent control plane, and runtime governance.

Practical implementation path:
- Keep static skill scanning as a cheap first pass, but do not treat it as final admission.
- Execute untrusted skills in a network-denied or egress-logged sandbox with fake secrets and marker files.
- Track file, process, network, environment, credential, and prompt-context flows during execution.
- Require a clean detonation trace before a third-party skill can run against real repositories or credentials.
- Store scanner output, sandbox trace ID, skill hash, script hash, allowed scopes, and final admission verdict in the skill registry.

Tools, repos, and methodologies worth exploring now:
- SkillSpector or similar static triage for first-pass filtering.
- Sandbox workers for detonation.
- Marker-based taint fixtures for secrets, source files, and credential stores.
- Egress deny by default, then scoped allowlists after review.

Implementability score: 0.64

A basic detonation lane is implementable now. The hard part is coverage: real skill behavior can be trigger-dependent, model-dependent, and environment-dependent, so sandbox traces need adversarial fixtures rather than one happy-path run.

## Working conclusion

The daily implementation thesis is preflight before autonomy. Build the agent graph, bound the loops, run cheap proxy evals, and detonate untrusted skills before granting real tool authority.
