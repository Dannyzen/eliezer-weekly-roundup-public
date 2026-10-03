# AgenticAI Weekly Analysis: 2026-10-02

This week’s strongest implementation signal is that reliable agent systems are becoming executable evidence pipelines. Stable workflow structure belongs in code, evaluation must vary the deployed configuration rather than the model alone, and memory policy must expose the evidence-selection process before it optimizes retention.

## Compile recurring multi-agent work into code

GitHub Dynamic Workflows let a Copilot extension define deterministic commands, tool calls, sequential or parallel agent stages, structured handoffs, review checkpoints, resume behavior, schedules, and run limits. HEXIS reaches the same architectural boundary from the research side by compiling SKILL.md procedures into extended finite state machines, leaving local judgment to the model while the runtime owns progress and allowed transitions.

### Why it matters

Prompt-only orchestration asks the model to remember both the task and the procedure. Coded orchestration makes the execution graph inspectable, replayable, and resumable. It also gives cost limits, checkpoints, and structured joins a real enforcement surface.

### Fit in the stack

This belongs in orchestration and harness architecture. The practical route is GitHub’s public preview or an equivalent Temporal, LangGraph, or explicit state-machine implementation. HEXIS is a design reference because no paper-owned public compiler resolved during this scan.

### Practical tools and methodologies worth exploring

- GitHub Copilot Dynamic Workflows with typed stage outputs and explicit joins
- Temporal or LangGraph for durable waits, retries, and resumable state
- finite-state or statechart compilation for stable skill procedures
- versioned workflow definitions, review checkpoints, and run-budget limits
- replay tests that assert allowed states, transitions, and terminal receipts

Implementability score: 0.90

Core sources: [GitHub Dynamic Workflows release](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app/), [GitHub operating documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows), [HEXIS](https://arxiv.org/abs/2609.30123v1)

## Evaluate the model, harness, tools, and budget as one system

Agents Are Systems, Not Models studies complete configurations across four scientific coding tasks. Repeated runs of the same configuration account for about 54 percent of outcome variance. Task information mattered more than model size or time budget, and a dedicated verification tool changed behavior more than a self-verification prompt. The executable-contract audit adds the missing lower layer: across 34 mutating tools in four benchmarks, the authors found seven tool defects and one evaluator property that could let a benchmark report success without the intended state transition.

### Why it matters

A model leaderboard cannot predict a deployed agent when instructions, tools, budgets, harness behavior, and repeated-run variance materially change the outcome. A benchmark score also cannot certify anything when the environment contract is wrong.

### Fit in the stack

The deployment unit is the model plus harness plus tools plus context plus budget plus evaluator. Evaluation needs repeated factorial cells above the tool layer and executable state-transition contracts below it.

### Practical tools and methodologies worth exploring

- factorial configuration sweeps with repeated cells and variance decomposition
- dedicated verification tools instead of self-verification prompts alone
- contract schemas for tool preconditions, state transitions, returns, and evaluator reads
- dynamic probes and mutation tests for benchmark tools and scorers
- trajectory taxonomies that separate model, harness, environment, and evaluator failures

Implementability score: 0.82

Core sources: [Agents Are Systems, Not Models](https://arxiv.org/abs/2610.01618v1), [public trajectory repository](https://github.com/lusxvr/rethinking-agent-evaluation), [Executable-Contract Audit](https://arxiv.org/abs/2609.37315v1), [MIT-licensed audit artifact](https://github.com/rohithreddybc/tool-contract-conformance)

## Make security evaluation a composable evidence matrix

pikit separates attack wording, delivery carrier, prevention strategy, target agent, trace, and verdict. Its public toolkit includes 13 attacks, 16 carriers, 9 prevention strategies, and runtime adapters for OpenClaw and Hermes Agent. This matters because an audited prompt-injection harness changed measured attack success from 21.7 percent to 1.2 percent after correcting payload delivery and tool-argument scoring.

### Why it matters

Security evaluation is invalid when the payload never reaches the model or the grader checks the wrong effect. A composable matrix makes the delivery path and verdict predicate explicit, so new defenses can be compared against the same evidence contract.

### Fit in the stack

This belongs in trajectory-aware evaluation and the harness test layer. It should sit beside environment-specific delivery receipts, exact tool-argument predicates, and realized-effect checks.

### Practical tools and methodologies worth exploring

- pikit as a fixture generator and trace collector
- delivery receipts for browser, document, memory, MCP, and tool-output carriers
- exact argument and realized-effect predicates
- paired defended and undefended replays against the same payload corpus
- regression matrices keyed by attack, carrier, defense, agent, and verdict version

Implementability score: 0.88

Core sources: [pikit paper](https://arxiv.org/abs/2609.36817v1), [pikit in AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/pikit), [Auditing Agent Security Benchmarks](https://arxiv.org/abs/2609.32691v1)

## Intervene on retrieval and gate shared-memory admission

Causal Memory Policy shows that store-level utility estimates fail when retrieval never exposes the memory. The paper reports identification failure for 54 percent of required LongMemEval memories and 67 percent on LoCoMo, then improves discrimination with randomized retrieval slots and known propensities. The shared-memory admission benchmark finds a related failure: uncontested false beliefs were repeated in 0.97 to 0.99 of probes, while a declared-source-type gate reduced false adoption to 0.06 to 0.09.

### Why it matters

A memory can look useless because retrieval never surfaced it, and a repeated claim can look corroborated when every copy descends from one source. Retention and admission decisions need controlled exposure plus lineage, not frequency alone.

### Fit in the stack

Memory is an evidence-selection system. Retrieval policy, provenance roots, source classes, contest state, and retention policy must be observable and separately testable.

### Practical tools and methodologies worth exploring

- bounded randomized retrieval slots with propensity logging
- reversible demotion and no-delete controls while utility is unidentified
- provenance-root collapse before corroboration counts
- source-class admission gates, contest state, and temporal supersession
- replay tests that vary retrieval exposure while holding the task fixed

Implementability score: 0.68

Core sources: [Causal Memory Policy](https://arxiv.org/abs/2610.02070v1), [Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1), [public benchmark artifact](https://github.com/lxy1134/iclr_2027)

## Weekly implication

Treat the workflow program, full deployed configuration, evidence-selection policy, and evaluator contract as one inspectable system. Optimization comes after the trace can show which program path ran, which evidence was available, what effect occurred, and which component deserves credit or blame.
