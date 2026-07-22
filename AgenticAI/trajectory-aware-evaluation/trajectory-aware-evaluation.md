# Trajectory-Aware Evaluation

Trajectory-aware evaluation is becoming the dividing line between toy agent demos and systems you can actually improve.

## Core thesis

If you only grade the final output, you are measuring luck, not behavior.

Agent systems act through sequences: planning, tool selection, retries, state changes, recoveries, and handoffs. A benchmark that ignores the sequence cannot reliably tell the difference between:
- a clean execution
- a dangerous execution that happened to end well
- a brittle execution that only works once every few tries
- an execution that silently violated policy before producing a superficially correct answer

## Why this matters

Traditional LLM evals were built for static responses. Agent evals need to answer different questions:
- Did the agent take the right actions?
- Did it stay within policy?
- Did it recover correctly when the environment pushed back?
- Would the behavior repeat across multiple trials?
- Is the trace good enough to audit after a failure?

That means evidence has to come from the run itself, not only the final artifact.

## What a modern agent eval should capture

### 1. Execution traces
Record the actual sequence of actions, tool calls, retries, and branch decisions.

### 2. Environment snapshots
Capture state before, during, and after important actions so graders can verify whether the world changed as intended.

### 3. Audit logs
Preserve policy decisions, approvals, exceptions, and metadata about why actions were allowed or denied.

### 4. Repeated-trial consistency
Use multiple runs per task. A system that passes once in three attempts is not equivalent to a system that passes reliably.

### 5. Separate scoring dimensions
Completion, safety, and robustness should not be collapsed into one opaque metric.

### 6. Parameter-level execution quality
For tool-heavy work, many failures come from wrong arguments, wrong thresholds, and wrong target selection rather than bad intent or bad final prose. Good evals score those execution details directly.

### 7. Modality-aware verification
When outputs are visual, spatial, interactive, or otherwise world-facing, the grader should verify the artifact in the right modality instead of reducing everything to text matching.

## Practical build pattern

A useful minimum stack now looks like this:
1. replayable traces for every run
2. state snapshots at critical checkpoints
3. explicit scoring rubrics for completion, safety, and robustness
4. repeated-trial metrics such as Pass@k and stricter consistency-oriented variants
5. dashboards that let engineers inspect failures by trajectory, not only by top-line score
6. environment-aware checks for parameter correctness and output fidelity

## Tools and methodologies worth exploring now

- OpenTelemetry-style tracing for agent workflows
- environment snapshotting for browser, desktop, or API task state
- rubric-based evaluators linked to traces rather than final outputs only
- perturbation testing to measure recovery and consistency under noise
- benchmark harnesses that preserve evidence artifacts for later replay
- parameter-level execution scoring
- modality-aware verifiers for visual or structured outputs
- adaptive curricula that keep environments near the policy frontier
- runtime-specific safety taxonomies for different execution surfaces

## Representative sources

- Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents: https://arxiv.org/abs/2604.06132
- Microsoft Agent Framework repository, especially its checkpointing and observability features: https://github.com/microsoft/agent-framework
- OpenClaw real-world safety analysis: https://arxiv.org/abs/2604.04759
- GeoAgentBench: https://arxiv.org/abs/2604.13888
- Ecom-RLVE: https://huggingface.co/blog/ecom-rlve
- ATBench-Claw and ATBench-CodeX: https://arxiv.org/abs/2604.14858
- AgentEval: https://arxiv.org/abs/2604.23581
- AgentPulse: https://arxiv.org/abs/2604.24038
- OS-SPEAR: https://arxiv.org/abs/2604.24348
- Wuzheng02/OS-SPEAR: https://github.com/Wuzheng02/OS-SPEAR

## New April 2026 additions

### GeoAgentBench shows why execution metrics need to reach below the final artifact
GeoAgentBench is domain-specific on paper and generally useful in practice. Its main lesson is that tool-augmented agents often fail on the execution substrate: wrong parameters, weak recovery logic, and outputs that need modality-aware verification. Parameter Execution Accuracy is a good pattern because it grades what the agent actually did to the environment, not just whether it wrote a plausible answer afterward.

### Claw-Eval strengthens the case for trace-first grading
Claw-Eval is the clearest current argument that final-output grading is not enough. Its three evidence channels and separate completion, safety, and robustness scores make a good default pattern for future agent benchmarks.

### CodeTracer shows that trace structure matters as much as trace capture
CodeTracer adds an important operational lesson: it is not enough to log everything if the resulting evidence is still too flat to debug. Reconstructing hierarchical state transitions, tagging likely failure onset, and tracing downstream error chains turns observability into something engineers can actually use to recover failed runs.

### EcomRLVE-GYM turns verifiable environments into reusable agent infrastructure
EcomRLVE-GYM adds a useful escalation of the trajectory-aware-eval idea. The environment is not only the place where you score the agent after the fact. It is also the curriculum, the verifier, and the regression harness. Procedural generation, adaptive difficulty, and tuple-level reward computation make the benchmark reusable as training infrastructure.

### ATBench shows safety eval has to adapt to the runtime surface
ATBench-Claw and ATBench-CodeX make an important design correction: the benchmark pipeline can stay shared while the safety taxonomy changes with the runtime. Shells, patches, approvals, sessions, skills, and external actions create different harm surfaces, so the taxonomy has to move with the execution setting.

### Frameworks are starting to absorb evaluation prerequisites
Microsoft Agent Framework is strategically relevant here because checkpointing, time travel, and observability reduce the gap between runtime debugging and benchmark evidence collection. The platform layer is beginning to catch up with what evaluation research actually needs.

### Environment generation turns eval into a service, not a spreadsheet
ClawEnvKit sharpens the next step beyond trace-first evaluation. The benchmark should not only record what happened inside a fixed set of tasks. It should generate new verified tasks when the capability frontier moves. Its parser-generator-validator pipeline and 1,040-environment Auto-ClawEval benchmark make the design pattern clear: a capability description can be compiled into an environment, scored automatically, and recycled into both training and regression testing.

Two lessons matter immediately:
- harness engineering still changes outcomes materially, so eval has to compare scaffolding and not only model families
- operators should be able to describe a desired capability in natural language and get back a verified task world instead of waiting for the next benchmark paper

This is a better product shape for agent evaluation. The environment factory becomes part of the runtime improvement loop.

### Repeated execution is now a first-class reliability test
On the Reliability of Computer Use Agents adds the correction this topic needed. A task is not solved because the agent passed once. The same model can alternate between success and failure across repeated runs due to execution stochasticity, task ambiguity, and behavioral drift. That turns repeated-trial consistency from a nice-to-have into a required metric for browser and desktop agents.

The product lesson is direct:
- rerun the same task multiple times before trusting a pass rate
- record ambiguity and clarification failure as benchmark data, not annotation noise
- optimize for stable strategies across runs instead of one aggressive lucky trajectory

Source:
- [On the Reliability of Computer Use Agents](https://arxiv.org/abs/2604.17849)

### SWE-chat shows why coding-agent eval has to leave benchmark theater
SWE-chat adds the missing field evidence for coding agents. Instead of another curated benchmark, it captures 6,000 real coding-agent sessions from open-source development, with more than 63,000 user prompts and 355,000 agent tool calls. That makes it possible to score what actually matters in practice: how often humans interrupt or correct the agent, how much agent-written code survives into commits, and whether security quality drops when the agent is doing more of the work.

Its numbers are useful precisely because they are messy. Only 44% of agent-produced code survives into user commits, users push back against agent outputs in 44% of turns, and agent-written code introduces more security vulnerabilities than human-authored code. That is a much better eval substrate than a clean coding benchmark because it captures the negotiation between user and agent instead of pretending the interaction ends when the model emits code.

Practical lesson:
- measure code-survival and authorship patterns, not just task completion
- treat interruption and rewrite behavior as primary signals of usefulness
- run security analysis on agent-authored diffs as part of the same benchmark loop
- preserve full user-agent traces so teams can study where collaboration actually degrades

Source:
- [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779)

### April 28 update: eval is becoming operational observability
AgentEval, AgentPulse, and OS-SPEAR add a useful three-layer correction to this topic.

AgentEval shows that multi-step workflows should be represented as DAGs, not flat logs. Typed node metrics, dependency edges, and hierarchical failure labels make root-cause attribution possible and CI regression results actionable.

AgentPulse shows that deployed agent quality also has an ecosystem dimension. Benchmark scores need to be interpreted next to adoption signals, package/marketplace activity, issue health, community sentiment, and maintenance evidence. Those signals are not ground truth, but they catch risks that static benchmarks miss.

OS-SPEAR makes the runtime-specific case for OS agents. Safety, performance, efficiency, and robustness have to be scored separately because a desktop/browser agent can finish a task while still being slow, unsafe, or brittle under visual/textual perturbations.

Practical lesson:
- store traces in a shape that preserves dependencies
- grade intermediate steps, not only final artifacts
- connect eval failures to CI/CD root-cause reports
- track deployment-health signals as context around benchmark scores
- use runtime-specific perturbation and efficiency tests for OS/browser/desktop agents

Sources:
- [AgentEval](https://arxiv.org/abs/2604.23581)
- [AgentPulse](https://arxiv.org/abs/2604.24038)
- [OS-SPEAR](https://arxiv.org/abs/2604.24348)
- [Wuzheng02/OS-SPEAR](https://github.com/Wuzheng02/OS-SPEAR)

## April 30 update: eval cost turns environment factories into infrastructure

ClawGym and Hugging Face’s eval-cost analysis update this topic with a hard operational constraint: agent evaluation now has to be both environment-aware and cost-aware.

ClawGym pushes the environment side. Its personal-agent framework synthesizes 13.5K filtered tasks from persona-driven intents and skill-grounded operations, pairs them with realistic mock workspaces and hybrid verification mechanisms, trains ClawGym-Agents from black-box rollout trajectories, explores RL through parallel per-task environments, and builds a 200-instance benchmark calibrated by automated filtering and human-LLM review. That is the environment-factory shape this topic has been moving toward.

The Hugging Face article pushes the cost side. HAL spent about $40,000 on 21,730 agent rollouts; a single frontier GAIA run can cost $2,829 before caching; and scaffold choice can create a 33x cost spread on identical tasks. That means trajectory-aware evaluation without cost accounting is incomplete.

Practical lesson:
- benchmark the model x scaffold x environment x token-budget product, not the model alone
- store cost, tokens, retries, scaffold version, and trace path with every eval result
- use cheap coarse screens before expensive repeated trials
- report success-versus-cost Pareto frontiers
- treat generated task worlds as reusable training, eval, and regression infrastructure

Sources:
- [ClawGym](https://arxiv.org/abs/2604.26904v1)
- [AI evals are becoming the new compute bottleneck](https://huggingface.co/blog/evaleval/eval-costs-bottleneck)

## May 1 update: live workflow eval needs fresh demand and adversarial task design

Claw-Eval-Live, WindowsWorld, and the terminal-agent benchmark guideline sharpen this topic in the same direction: agent eval should be maintained like infrastructure, not published once as a static quiz.

Claw-Eval-Live separates a refreshable demand-signal layer from a reproducible release snapshot. The current release uses ClawHub Top-500 skills to construct 105 controlled workflow tasks across 17 families and evaluates 13 frontier models from execution traces, audit logs, service state, and post-run workspace artifacts. The leading model passes only 66.7% of tasks and no model reaches 70%, which is exactly the kind of sober signal operators need.

WindowsWorld adds the desktop/workstation version of the same lesson: 181 tasks across 17 Windows applications, 77.9% multi-application workflows, and all tested agents below 21% success on multi-app tasks. The benchmark guideline adds the task-authoring correction: benchmark tasks are not prompts. They should be adversarial, difficult, and legible, with reward-hacking checks and verification logic review.

Practical lesson:
- derive internal benchmark tasks from real workflow demand, then snapshot releases for reproducibility
- grade state changes, intermediate checkpoints, audit logs, and artifacts before trusting final prose
- tag failures by execution surface: browser, terminal, desktop, API, workspace, or multi-system handoff
- adversarially review benchmark tasks for hidden oracle assumptions and reward-hackable tests
- keep benchmark distribution change logs so freshness does not destroy comparability

Sources:
- [Claw-Eval-Live](https://arxiv.org/abs/2604.28139)
- [Claw-Eval-Live repo](https://github.com/Claw-Eval-Live/Claw-Eval-Live)
- [WindowsWorld](https://arxiv.org/abs/2604.27776)
- [WindowsWorld repo](https://github.com/HITsz-TMG/WindowsWorld)
- [What Makes a Good Terminal-Agent Benchmark Task](https://arxiv.org/abs/2604.28093)

## May 2 update: synthetic computers make long-horizon productivity eval concrete

Synthetic Computers at Scale updates this topic by making the task world itself the unit of evaluation. The public dataset exposes 98 synthetic computers with personas, monthly objectives, collaborators, filesystem policies, file lists, and file relationship graphs. The paper’s larger methodology then runs month-scale productivity simulations across these environments to generate professional deliverables and process traces.

The practical implication is strong: a computer-use eval should not start from an empty browser or a one-line prompt. It should start from a realistic workspace whose state conditions the task. That is how agents fail in the real world: they miss the right folder, misread project history, ignore local conventions, overwrite the wrong artifact, or produce a deliverable that is ungrounded in the user’s files.

Practical lesson:
- seed internal desktop/file-system evals from synthetic computer metadata
- score file discovery, grounded evidence use, artifact quality, trace evidence, and repeated-run consistency
- preserve the workspace before and after each run for replay
- track cost and wall time because long-horizon workspace evals can become expensive quickly

Sources:
- [Synthetic Computers at Scale](https://arxiv.org/abs/2604.28181)
- [microsoft/synthetic-computers-at-scale](https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale)

## May 6 update: search-agent eval should grade evidence portfolios

OpenSeeker-v2 and Bright-Pro add a useful search-agent correction to this topic. A deep-research agent should not be judged only on final answer quality or generic retrieval recall. The trace should show whether the agent generated useful search trajectories, covered the required evidence aspects, avoided redundant lookup, and assembled complementary sources for reasoning.

OpenSeeker-v2 emphasizes trajectory data quality: informative, high-difficulty traces can make simple SFT surprisingly competitive for ReAct-style search agents. Bright-Pro emphasizes evaluation shape: reasoning-intensive retrievers should be scored on aspect-aware evidence portfolios and in-loop agentic search behavior, not only static top-k matching.

Practical lesson:
- record query decomposition, retrieval calls, selected evidence, missing aspects, judge decisions, and final claims
- label evidence aspects for internal research tasks so retrieval can be graded by coverage and complementarity
- evaluate search agents in both static retrieval and agentic in-loop settings
- curate hard successful traces and near-miss traces instead of only collecting easy wins
- attach cost and iteration count to search quality so teams can compare success-versus-cost frontiers

Sources:
- [OpenSeeker-v2](https://arxiv.org/abs/2605.04036)
- [PolarSeeker/OpenSeeker](https://github.com/PolarSeeker/OpenSeeker)
- [Bright-Pro / Rethinking Reasoning-Intensive Retrieval](https://arxiv.org/abs/2605.04018)
- [yale-nlp/Bright-Pro](https://github.com/yale-nlp/Bright-Pro)

## May 8 update: citation verification belongs in the research-agent eval loop

Cited but Not Verified adds the evaluation layer this topic needs for deep research agents. A source-grounded report is not verified because it contains links. The system has to parse the Markdown, identify which claim each citation is supposed to support, retrieve the cited content, and score link validity, relevance, and factual support separately.

The practical lesson is immediate:
- parse citations from generated Markdown with an AST, not only regex link scraping
- snapshot cited source content so later audits do not drift with the web
- score link availability, source relevance, and claim support as separate dimensions
- fail publication on dead links, uncited core claims, unsupported claim-source pairs, and source drift
- preserve retrieval IDs, cited spans, source snapshots, and final claims in the run trace
- use model judges only after deterministic retrieval and source extraction have produced auditable evidence

This directly upgrades trajectory-aware evaluation from "grade the final report" to "grade the evidence chain that produced the report." It is especially relevant for research agents, coding agents that cite docs, and compliance assistants that cite policies.

Source:
- [Cited but Not Verified](https://arxiv.org/abs/2605.06635)

## May 9 update: prefix monitors and test evolution move eval before final failure

PrefixGuard and TEBench make the same correction from different sides: agent evaluation should catch failure while the run is still unfolding and should test whether the surrounding verification harness stays current.

PrefixGuard turns raw agent traces into typed step views and trains online prefix-risk monitors. That is the right product shape for long-running tool use: not every risky run should wait until a final grader says the task failed. The monitor should warn when the prefix already contains enough evidence of repeated tool confusion, missing state, risky actions, or unrecoverable trajectory drift.

TEBench adds the coding-agent version. Production code changes can leave tests broken, stale, or missing. A coding agent that only makes the current suite pass is not enough; it should identify affected tests, update stale assertions, and add tests for new behavior. That moves evaluation from static patch correctness to project-level test maintenance.

Practical lesson:
- train or hand-author cheap prefix monitors over typed trace events before reaching for LLM judges
- store warning time, warning reason, observed prefix, and final outcome together
- create internal TEBench-style fixtures from real commits where tests broke, went stale, or were missing
- treat browser/network/runtime evidence from tools like Chrome DevTools MCP as trace artifacts and CI evidence
- score warning quality, test-evolution quality, final success, and human-intervention burden separately

Sources:
- [PrefixGuard](https://arxiv.org/abs/2605.06455)
- [TEBench](https://arxiv.org/abs/2605.06125)
- [iSEngLab/TEBench](https://github.com/iSEngLab/TEBench)
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)

## May 10 update: agent eval is becoming chaos engineering

EvalMonkey is useful because it turns agent evaluation into a local failure-injection workflow. It talks to agents over HTTP, supports common frameworks, runs standard text benchmarks, injects chaos such as latency, header mutation, and schema corruption, then emits traces and improvement eval assets.

This complements PrefixGuard and TEBench. PrefixGuard warns before final failure; TEBench checks whether tests evolve with the project; EvalMonkey contributes the operator move: deliberately perturb the runtime seams where agents break, then turn failures into repair artifacts.

Practical lesson:
- expose internal agents through stable HTTP endpoints so eval harnesses can test them without invasive changes
- run small benchmark samples as smoke tests before full expensive sweeps
- inject latency, malformed headers, corrupt schemas, missing fields, and response-shape mismatches
- preserve `traces.json`, `evals.json`, and improvement prompts as CI artifacts
- evaluate recovery behavior, not only clean-prompt accuracy

Source:
- [EvalMonkey](https://github.com/Corbell-AI/evalmonkey)

## May 11 update: eval must test state propagation, live failures, and abstention

AgentEscapeBench, SREGym, FixedBench, and TraceFix push this topic from trace capture into operational stress testing.

AgentEscapeBench shows that agents can call local tools but still fail when intermediate results must be propagated through long unfamiliar dependency graphs. SREGym shows the live-systems version: SRE agents need to diagnose faults under Kubernetes, observability streams, ambient noise, and metastable/correlated failures. FixedBench adds the abstention axis for coding agents: stale issues require the agent to prove that no patch is needed. TraceFix adds the coordination axis: multi-agent protocols should be verified against model-checker counterexamples and monitored at runtime, not left as chat-room etiquette.

Practical lesson:
- build DAG-style tool-use evals where intermediate state is checked, not only the final answer
- include live fault-injection environments for agents that touch production-like systems
- score abstention and empty-patch decisions as successful outcomes when the current state is already correct
- require reproduction, Git-history inspection, or state inspection before edits
- verify critical multi-agent handoffs with TLA+, state machines, or runtime topology monitors
- preserve the trace, environment snapshot, protocol spec, and final artifact together so failures are debuggable

Sources:
- [AgentEscapeBench](https://arxiv.org/abs/2605.07926)
- [SREGym](https://arxiv.org/abs/2605.07161)
- [SREGym repository](https://github.com/SREGym/SREGym)
- [Coding Agents Don't Know When to Act](https://arxiv.org/abs/2605.07769)
- [TraceFix](https://arxiv.org/abs/2605.07935)

## May 14 update: coding-agent eval must grade the whole cycle and the process

SWE-Cycle, AgentLens, and BenchJack all attack the same weakness in coding-agent evaluation: final pass/fail scores are too easy to misread. SWE-Cycle removes scaffolding by asking agents to reconstruct environments, implement code, generate verification tests, and complete the whole issue-resolution cycle in a bare repository. AgentLens shows that even passing trajectories can be low-quality lucky passes. BenchJack shows that benchmarks themselves can be hacked for near-perfect scores without solving the intended task.

The practical correction is to turn every coding-agent eval into an evidence package. The run should prove environment reconstruction, reproduction, implementation, test maintenance, verification, process quality, and benchmark integrity. A green patch is only one artifact in that package.

Practical lesson:
- split evals into setup, reproduction, implementation, test generation/maintenance, and final verification phases
- label trace steps as exploration, implementation, verification, orchestration, retry, rollback, or waste
- flag blind retries, regression cycles, missing verification, and temporally disordered work even when tests pass
- combine dynamic testing with static review and process-quality scoring
- adversarially audit benchmarks for reward-hacking shortcuts before using them as selection signals
- preserve bare-repo state, trace labels, test artifacts, patches, and benchmark-audit notes together

Sources:
- [SWE-Cycle](https://arxiv.org/abs/2605.13139)
- [AgentLens](https://arxiv.org/abs/2605.12925)
- [BenchJack](https://arxiv.org/abs/2605.12673)

## May 17 update: adaptive eval needs chronological replay and verified artifacts

FutureSim and Viverra update trajectory-aware evaluation from two sides. FutureSim shows how to test adaptation by replaying real-world events in chronological order and asking agents to forecast outcomes beyond their knowledge cutoff. That turns state update, evidence use, uncertainty, and calibration into measurable behavior. Viverra shows the coding-agent version of evidence discipline: generated code should carry candidate assertions and deterministic verification results, not only a persuasive explanation.

The shared lesson is that an eval should leave an evidence package. For adaptive agents, the package is the dated event stream, forecast, uncertainty, retrieved evidence, state update, and resolution. For coding agents, it is the patch, properties, verification attempts, proven claims, and explicit non-guarantees.

Practical lesson:
- replay dated tickets, docs, incidents, changelogs, or source feeds through the same agent harness
- score accuracy, Brier calibration, evidence use, state updates, and missed-event failure modes
- ask coding agents for invariants, postconditions, and safety properties with each patch
- run deterministic verifiers, static analyzers, property tests, or model checkers where feasible
- store replay traces and proof artifacts next to final outputs so failures can be audited

Sources:
- [FutureSim: Replaying World Events to Evaluate Adaptive Agents](https://arxiv.org/abs/2605.15188)
- [Viverra: Text-to-Code with Guarantees](https://arxiv.org/abs/2605.14972)

## May 19 update: full-agent evals need environment factories and cost traces

The Open Agent Leaderboard and EnvFactory push trajectory-aware evaluation into a more operational shape.

The Open Agent Leaderboard makes the full agent system the eval unit. The useful comparison is no longer only model A versus model B. It is model plus scaffold plus tool shortlist plus memory/recovery policy plus cost. Its Exgentic protocol is especially useful because it normalizes diverse benchmarks into task, context, and actions, while the results layer tracks full-system outcomes.

EnvFactory extends the environment side of the same thesis. Tool-use RL cannot scale if every stateful task world is handmade or if synthetic trajectories reveal the tool sequence too directly. Verified executable environments should become a reusable supply layer for training, evaluation, and regression.

Practical lesson:
- benchmark model x scaffold x tool shortlist x cost, not model names alone
- preserve failed-run traces because failures can cost materially more than successful runs
- build small verified mock environments from real internal tool schemas and docs
- generate natural intents that force the agent to infer the tool path
- reuse environment factories for SFT/RL data, eval, and CI regression
- report success-versus-cost Pareto frontiers rather than single leaderboard numbers

Sources:
- [The Open Agent Leaderboard](https://huggingface.co/blog/ibm-research/open-agent-leaderboard)
- [Exgentic](https://github.com/Exgentic/exgentic)
- [Open Agent Leaderboard results dataset](https://huggingface.co/datasets/open-agent-leaderboard/results)
- [EnvFactory](https://arxiv.org/abs/2605.18703v1)

## May 20 update: code cleanliness is an agent-cost metric

Does Code Cleanliness Affect Coding Agents? adds a practical measurement correction. In the reported controlled minimal-pair study, cleaner repositories did not materially change Claude Code pass rate, but they did reduce token usage by 7-8% and file revisitations by 34%. That means code cleanliness should be treated as a measurable agent operating-cost variable, not only a human maintainability preference.

The eval implication is direct: pass rate alone hides repository-shape effects. A coding-agent benchmark should report the target codebase's static-analysis profile, cognitive complexity, file-revisit count, token spend, tool calls, retries, and latency. Otherwise a harness change may look neutral while still wasting materially more context and wall-clock time.

Practical lesson:
- add static-analysis and cognitive-complexity metadata to coding-agent eval tasks
- track token usage, file revisits, tool calls, retries, latency, and failed-run premiums
- build clean/messy minimal-pair repositories to isolate environment effects from model effects
- prioritize refactors that lower agent navigation waste even when they do not change pass rate

Source:
- [Does Code Cleanliness Affect Coding Agents?](https://arxiv.org/abs/2605.20049v1)

## May 21 update: green tests are not enough for coding agents

SpecBench sharpens the reward-hacking problem for long-horizon coding agents. The benchmark separates natural-language specification, visible validation tests, and held-out composed tests. That split matters because a coding agent can saturate visible tests while failing the real specification once features interact.

The companion benchmark-disclosure audit adds a reporting correction. Agent evals should disclose the benchmark identity, harness/scaffold, inference settings, cost, and failure breakdown. Without that, two papers can disagree on the same benchmark and no operator can tell whether the difference came from model behavior, scaffold behavior, sampling settings, task subset, or evaluator version.

Practical lesson:
- keep visible tests for local feedback but reserve held-out composed tests for trust decisions;
- add integration tests that combine features and stress hidden assumptions;
- adversarially audit benchmark tasks for shortcut solutions and test-memorization paths;
- record scaffold version, model version, prompts/settings, token/cost, retries, and failure labels;
- publish or preserve an evidence package for each eval run instead of a naked score.

Sources:
- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384v1)
- [What Twelve LLM Agent Benchmark Papers Disclose About Themselves](https://arxiv.org/abs/2605.21404v1)

## May 22 update: eval needs realistic terminal worlds and synthetic-data audits
TerminalWorld, Agentic CLEAR, and SynAE make the evaluation stack more operational. TerminalWorld derives terminal tasks from real asciinema recordings and reports that the best tested systems reach only 62.5% on a verified subset. Agentic CLEAR adds system-, trace-, and node-level analysis above observability. SynAE measures whether synthetic tool-calling trajectories preserve validity, fidelity, diversity, and downstream evaluation behavior.

The practical lesson is that agent eval is now a data pipeline, not a scoreboard:
- collect realistic task worlds from real workflows, not only hand-authored prompts;
- preserve full traces and environment state;
- grade failures at system, trace, and node levels;
- keep synthetic-data generation under validity, fidelity, diversity, and downstream-rank audits;
- report scaffold version, model/settings, dataset/source version, cost, and failure taxonomy with every score;
- maintain a small manually verified subset for trust decisions even when the larger benchmark is generated automatically.

Sources:
- [TerminalWorld](https://arxiv.org/abs/2605.22535)
- [EuniAI/TerminalWorld](https://github.com/EuniAI/TerminalWorld)
- [TerminalWorld dataset](https://huggingface.co/datasets/EuniAI/TerminalWorld)
- [Agentic CLEAR](https://arxiv.org/abs/2605.22608)
- [SynAE](https://arxiv.org/abs/2605.22564)
- [wsqwsq/SynAE](https://github.com/wsqwsq/SynAE)

## May 24 update: eval needs work-product quality, not only task completion

WorkstreamBench, SGR-Bench, ClawBench, and GBQA make the same operational point from different domains. Agents are now being asked to produce or manipulate work products: spreadsheets, website states, terminal environments, software releases, and QA findings. A final answer can be plausible while the artifact is unreviewable, the retrieval state is wrong, or the process skipped required evidence.

The evaluation unit should be a work-product evidence package:
- initial state and final state;
- trace with tool/browser/terminal actions;
- intermediate artifacts;
- verifier-owned checks;
- quality rubric for the artifact itself;
- process-defect labels;
- cost and retry metadata.

Practical lesson:
- grade spreadsheets across accuracy, formula lineage, formatting, and modifiability;
- grade browser/search tasks on state configuration before final prose;
- grade QA agents on reproducible bug evidence, not only issue text;
- keep verifier-owned tests and environment snapshots outside the agent's control;
- report process-defect classes next to pass/fail.

Sources:
- [WorkstreamBench](https://arxiv.org/abs/2605.22664)
- [SGR-Bench](https://arxiv.org/abs/2605.22219)
- [ClawBench](https://github.com/TIGER-AI-Lab/ClawBench)
- [GBQA](https://github.com/camel-ai/GBQA)

## May 25 update: long-horizon agents need quantitative persistence ledgers

Push Your Agent adds a metric that should become standard in long-horizon agent eval: Quantitative Goal Persistence. The failure is familiar. An agent performs plausible local work, repeats itself, loses count, submits duplicates, or declares completion before enough distinct valid work units have passed an external verifier. Final-answer scoring hides that defect; a progress ledger exposes it.

The practical lesson is to make completion external and machine-checkable:
- target count;
- candidate IDs;
- duplicate keys;
- verifier result;
- accepted distinct units;
- remaining backlog;
- stop reason;
- false-completion and repeated-work labels.

This extends work-product evaluation. The artifact is not only the final deliverable; it is also the ledger proving that the agent persisted until the requested quantity of valid work existed.

Source:
- [Push Your Agent](https://arxiv.org/abs/2605.23574)

## May 28 update: evaluation must control prior knowledge, infeasibility, and benchmark saturation

LiveBrowseComp, feasibility-awareness evaluation, and TASTE all point at the same eval defect: final-answer accuracy is not enough to know whether an agent actually searched, knew when to stop, or exercised the tool surface broadly.

LiveBrowseComp shows that agents can answer many BrowseComp questions without tools and can use search to verify internally generated hypotheses rather than discover evidence. Feasibility-awareness work shows that agents waste cost when required tools are unavailable and they fail to abstain. TASTE shows that hand-written natural-language scenarios under-cover the tool-sequence space and saturate too easily.

Practical lesson:
- run a closed-book baseline before crediting a search trajectory;
- include freshness windows so answers depend on recent evidence, not model memory;
- remove supporting evidence and check whether the agent degrades cleanly;
- create tool-missing tasks where success means early abstention;
- generate benchmark cases from real or synthetic tool-call sequences, then evolve difficulty;
- score query origin, evidence use, tool count, turn count, abstention, and false completion.

Sources:
- [LiveBrowseComp](https://arxiv.org/abs/2605.28721)
- [Do Agents Know What They Can't Do?](https://arxiv.org/abs/2605.28532)
- [TASTE](https://arxiv.org/abs/2605.28556)

## June 2 update: eval needs controlled transfer and process/outcome separation

AGENTCL adds a useful continual-learning test shape: build task streams where earlier sub-solutions, evidence, or workflows are intentionally reusable later, then measure whether the agent gains from that structure without dragging irrelevant past experience into the run. This is better than asking whether a memory system can retrieve old context. It tests whether prior experience becomes reusable capability.

ClinEnv adds the process-scoring version of the same correction. In staged inpatient simulations, the model must query specialist agents before committing to medications, procedures, and diagnoses. The important general result is that outcome quality and process quality decouple: a plausible final answer can hide redundant evidence gathering, bad sequencing, and weak late-stage management decisions.

Practical lesson:
- build compositional task streams with known reusable sub-solutions;
- compare no-memory, raw-retrieval, summarized-memory, and promoted-skill baselines;
- score forward transfer, negative transfer, forgetting, retrieval precision, process quality, and cost separately;
- build staged simulations where evidence gathering is required before irreversible commitments;
- label redundant queries, missing evidence, bad sequencing, unsupported commitments, and late-stage management failures.

Sources:
- [AGENTCL](https://arxiv.org/abs/2606.02461v1)
- [ClinEnv](https://arxiv.org/abs/2606.02568v1)

## June 5 update: search-enabled agent evals need contamination controls

Search-Time Contamination in Deep Research Agents adds a missing eval control for deep-research agents. Public benchmarks become leaky when an agent can search during inference and retrieve benchmark metadata, question context, or explicit answers. A final answer can look like reasoning while the trajectory is actually benchmark leakage.

The practical lesson is to make search provenance part of the grade:
- run no-search baselines before crediting search-enabled performance;
- preserve queries, clicked URLs, snippets, timestamps, and evidence paths;
- isolate benchmark metadata and known answer keys from the agent's search corpus;
- add canary benchmark artifacts and contamination classifiers;
- score contamination separately from answer correctness;
- require citations to evidence that is not benchmark metadata or leaked answers.

This pairs with EVA-Bench's stateful scenario design. A serious agent benchmark should control both the external information environment and the internal task state. Otherwise the score is measuring benchmark exposure, not capability.

Sources:
- [Search-Time Contamination in Deep Research Agents](https://arxiv.org/abs/2606.05241)
- [EVA-Bench Data 2.0](https://huggingface.co/blog/ServiceNow-AI/eva-bench-data)


## June 8 update: sabotage evaluation needs accumulated evidence ledgers

TRACE updates trajectory-aware evaluation with a monitoring shape for hidden malicious objectives. A sabotage trajectory can be composed of actions that are individually benign, so scoring one window at a time can miss the pattern. A full-trajectory judge can also drown in low-signal trace noise. TRACE's Triage-Inspect-Judge loop is useful because it first selects high-signal regions, then inspects them while carrying evidence forward, then emits a cited trajectory-level verdict.

The eval implication is direct: sabotage and permission-laundering tasks need accumulated evidence ledgers. The grader should preserve which steps formed the hypothesis, which steps weakened it, and which final verdict followed.

Practical lesson:
- normalize traces into typed events before scoring sabotage risk;
- run cheap prefix/region triage before expensive semantic inspection;
- preserve evidence links across distant actions;
- require verdicts to cite steps, arguments, outputs, and policy events;
- evaluate monitors offline on benign, malicious, and ambiguous trajectories before using them to block live work.

Source:
- [TRACE](https://arxiv.org/abs/2606.07054v1)

## June 16 update: procedure fingerprints turn traces into routing features

Agent trajectories as programs and ProcGrep turn trace capture into behavioral comparison. The key move is to normalize action sequences into atoms, learn recurring procedures, and compare agents by procedural distribution. That makes it possible to ask whether two agents solve tasks the same way, whether a fine-tune changed behavior, whether a run is drifting toward a known failure prefix, and whether a routing decision should prefer an agent with the right procedural habits.

PACT adds the training-side implication. Expert traces can guide optimization without becoming runtime hints, which preserves deployment realism while still giving dense process supervision.

Practical lesson:
- normalize action traces into a shared action alphabet before scoring;
- store procedure fingerprints next to success, cost, latency, retries, and human correction;
- compare agents by procedural divergence and failure-pattern frequency, not only pass rate;
- use early bad-prefix matches as soft interrupts or escalation signals;
- keep privileged expert traces as training/evaluation assets unless runtime replay is explicitly intended.

Sources:
- [Agent trajectories as programs](https://arxiv.org/abs/2606.16988v1)
- [ProcGrep](https://github.com/hamidahoderinwale/procgrep)
- [PACT](https://arxiv.org/abs/2606.16215v1)

## June 17 update: trajectory preferences and oracle signals expose fake progress

Offline Preference-Based Trajectory Evaluation and All Smoke, No Alarm update this topic at two different layers. Preference-based trajectory evaluation shows that terminal success creates too many ties and wastes partial-progress information. Comparing trajectories by progress and time-to-return can reduce tied comparisons from roughly 75% to roughly 35% across agentic and interactive benchmarks. All Smoke, No Alarm shows the coding-agent analog: a test file can exist while providing weak or no verification. In its public PR study, 80.2% of agent-authored test patches had weak or no explicit oracle signals.

The practical lesson is that evaluation should preserve proof strength, not just proof existence:
- store progress checkpoints, partial returns, retries, and time-to-return profiles;
- compare near-miss trajectories instead of flattening them into failed equals;
- classify agent-authored tests by explicit oracle signals, not only file count;
- reject assertion-free, output-free, and self-mocking test theater before merge;
- bind trajectory preference labels and oracle-strength labels to the same run trace.

Sources:
- [Offline Preference-Based Trajectory Evaluation](https://arxiv.org/abs/2606.17541v1)
- [All Smoke, No Alarm](https://arxiv.org/abs/2606.18168v1)


## June 19 update: staged harm and effort telemetry beat final pass/fail

SafeClawBench and Hugging Face's tool-specific agent benchmark update this topic with two practical scoring corrections. First, tool-agent security needs endpoint separation: semantic attack acceptance, audit-visible harm evidence, and sandbox-observed state harm can disagree. Second, tool and library quality should be measured by agent effort, not only final correctness. Turns, tokens, wall time, error rate, deprecated API use, and intended CLI or API marker adoption reveal whether a tool surface is actually agent-usable.

OpenAI's Deployment Simulation adds the rollout version of the same principle: realistic historical interactions can be replayed with a candidate model to estimate deployment-like behavior before release, including agentic workflows with tool use.

Practical lesson:
- score semantic, audit, and sandbox harm as separate endpoints;
- preserve environment state deltas and tool effects for adversarial tasks;
- extract trace markers for intended API path, CLI use, deprecated APIs, silent failures, and fallback behavior;
- compare bare, clone, and skill/documented support tiers for internal tools;
- replay representative historical workflows before changing model, scaffold, policy, or tool surface.

Sources:
- [SafeClawBench](https://arxiv.org/abs/2606.18356v1)
- [SafeClawBench dataset](https://huggingface.co/datasets/sairights/safeclawbench)
- [Is it agentic enough?](https://huggingface.co/blog/is-it-agentic-enough)
- [OpenAI Deployment Simulation](https://openai.com/index/deployment-simulation)

## June 22 update: domain benchmarks need tools, specialists, and replay

AssetOpsBench is useful because it moves domain-agent evaluation away from generic final-answer scoring. The benchmark includes industrial scenarios, domain-specific MCP servers, specialist agents, orchestration blueprints, trajectory replay, and failure taxonomy analysis. That is the shape real vertical-agent products need.

The portable lesson is to build eval worlds around the domain's actual tools and workflow roles. A maintenance agent, finance agent, medical admin agent, or internal ops agent should be scored on evidence gathered, tool parameters, specialist handoffs, intermediate decisions, final work product, and replayable failure labels.

Practical lesson:
- start with 20 to 50 realistic scenarios from one operating domain;
- expose domain tools as typed adapters or MCP-style servers;
- score intermediate steps separately from final answers;
- preserve trajectory replays and failure labels as engineering inputs;
- compare plan-and-execute against agents-as-tools on the same scenarios.

Sources:
- [IBM/AssetOpsBench](https://github.com/IBM/AssetOpsBench)
- [IBM Research AssetOpsBench writeup](https://research.ibm.com/blog/asset-ops-benchmark)
- [AssetOpsBench paper](https://arxiv.org/abs/2506.03828v1)
- [AssetOpsBench Hugging Face article](https://huggingface.co/blog/ibm-research/assetopsbench-playground-on-hugging-face)

## June 23 update: evidence-path and process-discipline scoring move eval below the answer

GroundEval and RigorBench update this topic with two practical corrections. First, stateful agent evaluation should deterministically check the evidence path: what the agent searched, fetched, cited, and was permitted to access. Second, coding-agent evaluation should score process discipline: planning, verification, recovery, abstention, and atomic step integrity.

Practical lesson:
- store `source_id`, `raw_output_ref`, retrieval time, access scope, and final-claim dependency in the trace;
- fail answers that depend on artifacts the agent never fetched;
- build silence, perspective, and counterfactual fixtures before relying on LLM judges;
- score coding runs for explicit plans, verifier use, recovery quality, abstention, and doom-loop avoidance;
- treat a reckless lucky pass as lower quality than a disciplined pass.

Sources:
- [GroundEval](https://arxiv.org/abs/2606.22737v1)
- [RigorBench](https://arxiv.org/abs/2606.22678v1)

## June 25 update: tool reliability needs hazard and constraint interaction tests

ToolBench-X and Constraint Tax update trajectory-aware evaluation from two sides. ToolBench-X shows that a clean function-call benchmark is too forgiving because real tool environments drift, fail, and contradict themselves. Constraint Tax shows that even the decoding mode can become part of the trajectory: a strict JSON Schema mask can suppress tool invocation when tool calling and structured output are enabled together.

Practical lesson:
- inject recoverable tool hazards into benchmark tasks and score diagnosis, retry, fallback, verification, and cross-check behavior;
- test tool use and structured output in the same serving mode used in production;
- log schema constraint mode, available tools, selected tool path, and serializer pass as trace fields;
- compare test-time scaling against targeted recovery hints and two-pass execution;
- treat a model that passes tool and JSON tests separately but fails the joint mode as not production-ready.

Sources:
- [ToolBench-X](https://arxiv.org/abs/2606.25819v1)
- [Foreverskyou/ToolBench-X](https://github.com/Foreverskyou/ToolBench-X)
- [Constraint Tax](https://arxiv.org/abs/2606.25605v1)

## June 26 update: RAG red-teaming needs novelty and cross-surface traces

MIRROR adds a useful evaluation correction for agentic RAG. A red-team run should not only report attack success. It should report whether attacks are novel, whether they duplicate known prompts, which surface failed, and how much query budget was spent. The relevant surfaces now include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation.

Practical lesson:
- add novelty gates to internal RAG red-team suites
- score duplicate rate, attack success, novelty-adjusted success, query cost, and cross-surface variance separately
- preserve trajectory evidence for retrieval, context assembly, modality handling, tool choice, and final response

Sources:
- [MIRROR](https://arxiv.org/abs/2606.26793v1)
- [FujitsuResearch/mirror](https://github.com/FujitsuResearch/mirror)

## July 9 update: severity scoring and causal slices make traces operational

Action-graded severity and STRACE add two complementary upgrades to trajectory-aware evaluation. Action-graded severity says tool-agent red-team results should be scored by the actual effect: reversibility, scope crossing, and privilege expansion. STRACE says long traces should be compressed by failure pattern and causal dependency before reflection, fine-tuning, or policy repair.

Practical lesson:
- score risky tool-call trajectories by effect severity, not only binary attack success;
- preserve action target, scope, reversibility, privilege level, and final effect as trace fields;
- cluster repeated failures before spending model budget on reflection;
- build dependency graphs over plan steps, tool calls, observations, verifier results, and policy decisions;
- send causal slices, not full noisy transcripts, into agent-optimization loops.

Sources:
- [Action-graded severity](https://arxiv.org/abs/2607.07474v1)
- [Harry-Ashley/action-graded-severity](https://github.com/Harry-Ashley/action-graded-severity)
- [STRACE](https://arxiv.org/abs/2607.07702v1)
- [moomight/STRACE](https://github.com/moomight/STRACE)

## Working conclusion

Trajectory-aware evaluation should become default infrastructure for any team building autonomous or semi-autonomous agents. If the run cannot be replayed, inspected, fingerprinted, severity-scored, causally sliced, and scored across safety, robustness, parameter correctness, environment fidelity, runtime-specific harm dimensions, staged semantic/audit/sandbox harm, agent-effort telemetry, real-user collaboration traces, realistic workspace state, live workflow demand, cost, adversarial task quality, long-range state propagation, abstention, protocol conformance, tool-shortlist quality, environment-factory coverage, quantitative goal persistence, procedural behavior, partial-progress preference, oracle strength, deterministic evidence paths, and coding-process discipline, improvement efforts will stay shallow and trust claims will stay unearned.

## July 10 update: framework choice belongs in the benchmark matrix

UniClawBench makes model and framework attribution separable. Its 400 bilingual tasks are organized by five capabilities and run in live containers with checkpoint grading. An executor, hidden supervisor, and user simulator support multi-turn recovery while keeping the evaluator's rubric and hidden resources outside the acting agent's workspace.

Practical lesson:
- benchmark model, framework, task world, and budget as separate variables;
- keep the model fixed when comparing harnesses;
- keep supervisor rubrics and hidden resources outside the executor workspace;
- score first-pass completion, recovery, final artifact state, cost, and wall time separately;
- retain traces, screenshots, checkpoint verdicts, and environment state as replay artifacts.

Sources:
- [UniClawBench](https://arxiv.org/abs/2607.08768v1)
- [HKU-MMLab/UniClawBench](https://github.com/HKU-MMLab/UniClawBench)

## July 11 update: causal data-science agents need abstention-aware ground truth

CausalDS adds a useful eval shape for data-science agents: generated hidden-SCM scenes, graph-faithful stories, tabular observations, private ground truth, deterministic grading, and scored abstention when a causal target is not identifiable.

Practical lesson:
- include hidden ground truth for analytics-agent benchmarks;
- score identifiability and abstention separately from numeric correctness;
- preserve claimed estimand, data columns used, identification method, uncertainty, and abstention reason in traces;
- build fixtures where the right behavior is refusing to estimate an unwarranted causal effect;
- use generated exams for regression, but keep manually reviewed examples for trust decisions.

Sources:
- [CausalDS](https://arxiv.org/abs/2607.08093v1)
- [andleb/causalds](https://github.com/andleb/causalds)

## July 13 update: coding-agent failure needs onset, lock-in, and observability

Failure as a Process adds the temporal decomposition this topic needed. A failed coding-agent run should not have one error timestamp. It should preserve the decisive error (`t_err`), the point after which no recovery is observed (`t_lock`), and the first externally visible symptom (`t_obs`).

The study's medians are step 7, step 12, and step 16, and 28% of failures never surface externally. That makes final-outcome grading structurally late. The actionable window sits between the first decisive error and empirical lock-in.

Practical lesson:
- add `t_err`, `t_lock`, and `t_obs` to failed-run review schemas;
- preserve the task specification beside the trace so requirement-relative failures are detectable;
- run prefix checks after task interpretation, environment discovery, first edit, first test, and before commit;
- treat lock-in predictions as intervention signals, not proof that recovery is impossible;
- convert repeated early error patterns into deterministic fixtures and routing rules.

Artifact caveat: the public package includes 1,794 annotations, codebooks, precomputed outputs, and analysis scripts, but omits raw trajectories and currently declares no repository license.

Sources:
- [Failure as a Process](https://arxiv.org/abs/2607.09510v1)
- [xz-Sean/cli_trajectory_analysis](https://github.com/xz-Sean/cli_trajectory_analysis)

## July 14 update: MCP fault injection needs a reproduce-intervene-confirm loop

AgentCheck converts runtime tool failures into controlled regression fixtures. It records a clean MCP run, replays matching tool responses while injecting one fault, returns to live tools after trajectory divergence, and reruns the identical fault after a mitigation. This is stronger than postmortem tracing because the changed variable is explicit.

Practical lesson:
- version clean, faulted, and mitigated runs under one scenario identity;
- make timeout, stale data, schema drift, permission denial, poisoned descriptions, and semantic corruption standard release fixtures;
- keep deterministic fault-handling checks load-bearing and LLM labels diagnostic;
- preserve the clean cache, injected mutation, divergence point, mitigation version, and final verdict;
- promote successful mitigations into the permanent MCP regression pack.

Artifact caveat: the MIT-licensed repository is populated and includes 120 scenarios, a web workbench, deterministic scoring, experiment runners, and results. Live evaluation still requires provider credentials and faithful local scenario specifications.

Sources:
- [AgentCheck](https://arxiv.org/abs/2607.11098v1)
- [aritra741/AgentCheck](https://github.com/aritra741/AgentCheck)

## July 16 update: self-improvement needs phased trajectory evidence

Self-improving harnesses need more than before-and-after pass rates. The trace must prove the source failure exists, show the candidate's effect on legal no-change controls, preserve old-task regression results, measure unseen-task transfer, and record what happens under a second optimization phase.

Practical lesson:
- bind every candidate to one reproducible failure trace and oracle;
- add negative controls where no edit is correct;
- preserve phase 0, phase 1, transfer, phase 2, and lifelong-average results;
- reject candidates that fix a refuted failure or transfer below the unoptimized baseline;
- record promotion, canary, rollback, and authority delta beside trajectory scores.

Sources:
- [Do Agent Optimizers Compound?](https://arxiv.org/abs/2607.14004v1)
- [experiment artifacts](https://github.com/relai-ai/Continual-Learning-Terminal-Bench)
- [Phantom Guardrails](https://arxiv.org/abs/2607.13083v1)
## July 22 update: debugging needs exact attribution and rerun closure

AgentDebugX adds the missing closure test for trajectory debugging. A diagnosis is useful only when it names the responsible agent and exact step, produces a bounded recovery, and improves the state on rerun.

Its strict result is deliberately humbling: exact agent-and-step attribution reaches 28.8% versus 21.7% for the strongest single-pass baseline. On GAIA, one rerun repairs 13 of 73 failures and raises overall accuracy from 55.8% to 63.6%. The gain is real, but the absolute attribution rate is not strong enough for unattended corrective authority.

Practical lesson:
- label symptom step, causal step, responsible agent, repair point, and resulting state separately;
- compare multi-turn root-cause analysis against single-pass summaries;
- make rerun success, new regressions, cost, and wall time part of the diagnosis score;
- preserve failed and repaired traces under one incident identity;
- keep incident sharing opt-in and scrub prompts, tool outputs, paths, credentials, and user data locally.

Artifact caveat: the public MIT toolkit is packaged and broad, but the evaluation covers one rerun and does not measure developer debugging time or console usability.

Sources:
- [AgentDebugX](https://arxiv.org/abs/2607.18754v1)
- [AgentDebugX/AgentDebugX](https://github.com/AgentDebugX/AgentDebugX)
- [AgentDebugX project site](https://www.agentdebugx.com/)
