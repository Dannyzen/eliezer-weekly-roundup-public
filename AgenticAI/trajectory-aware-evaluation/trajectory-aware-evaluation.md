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

## Working conclusion

Trajectory-aware evaluation should become default infrastructure for any team building autonomous or semi-autonomous agents. If the run cannot be replayed, inspected, and scored across safety, robustness, parameter correctness, environment fidelity, runtime-specific harm dimensions, real-user collaboration traces, realistic workspace state, live workflow demand, cost, adversarial task quality, long-range state propagation, abstention, protocol conformance, tool-shortlist quality, environment-factory coverage, and quantitative goal persistence, improvement efforts will stay shallow and trust claims will stay unearned.
