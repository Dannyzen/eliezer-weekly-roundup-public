# Daily Agent Research: 2026-09-30

Today's strongest implementation signal is that composability only helps when the harness, tool surface, and adversarial test surface are executable contracts. Popularity is secondary to inspectable interfaces, state checks, and replayable traces.

## Compose harnesses through explicit worker contracts

Raven treats each model and harness pair as a callable worker, then uses a host agent to decompose work, assign specialists, enforce dependency order, and retain artifacts for later handoffs. The public repository includes ACP, CLI, and OpenAI-compatible adapters plus presets for 13 external agents, including Hermes Agent. Hugging Face ranked Raven as its number one paper on September 30. The paper itself was submitted on September 27, so this is a fresh adoption signal rather than a strict 48-hour paper submission.

### Why it matters

A harness of harnesses makes the execution graph the unit of composition. Worker identity, accepted inputs, produced artifacts, dependency order, budget, and terminal proof have to survive across heterogeneous agents. This is more useful than routing one prompt to one general agent, but it also creates a larger coordination and authority surface.

### How it fits

Raven belongs in the orchestration and harness layers. Its Host Agent, registry, artifact ledger, and persistent archive are implementation references for composing specialized workers. The reusable lesson is to bind every worker edge to a typed handoff contract and keep the orchestrator separate from the worker's internal reasoning.

### Practical method

- model each worker as a versioned executor plus harness contract;
- express the run as a dependency graph with explicit input and artifact types;
- keep budgets, retries, receipts, and terminal state on the graph;
- admit third-party agents through read-only capability discovery before granting tools;
- validate the same task on a standalone worker and the composed graph.

Artifact status: `EverMind-AI/Raven` is public, Apache-2.0 licensed, has a populated `main` branch, 4,262 inspected blobs, and 4,912 stars at verification time. The repository and paper were inspected read-only. No installer or source code was executed. The report is company-authored and covers a broad system, so benchmark claims still need independent reproduction.

Tools and repositories worth exploring now: [Raven](https://github.com/EverMind-AI/Raven), ACP, explicit execution graphs, artifact ledgers, worker-contract validation

Implementability score: 0.68

Core sources: [Raven paper](https://arxiv.org/abs/2609.33439v1), [Raven repository](https://github.com/EverMind-AI/Raven)

## Make benchmark tool surfaces executable contracts

The executable-contract audit checks whether a benchmark tool's schema, documentation, return message, state mutation, and evaluator agree. Across 34 audited mutating tools in four benchmarks, the study confirmed seven tool defects and one evaluator property at pinned commits. Its clearest case reports a clinical write tool that claims success without changing state while the grader treats the success message as evidence.

### Why it matters

An agent benchmark can reward the correct payload even when the environment never applies the claimed effect. Model comparisons inherit that defect on every rerun. A benchmark needs contract tests below the model layer, not only task-level scores above it.

### How it fits

This belongs in the harness and evaluation layers. The tool contract is a release gate for the benchmark itself. Static checks can find likely mismatches, dynamic probes confirm effects, and provenance tracing identifies which reported scores depend on defective state.

### Practical method

- derive contracts from the tool schema, documentation, and returned messages;
- assert preconditions, state transitions, return values, and evaluator reads;
- pin every audited benchmark revision;
- retain a defect-to-score provenance map;
- run negative controls and injected defects against the checker itself;
- fail publication when the benchmark cannot prove the claimed state transition.

Evidence caveat: the checker missed most injected defects. In 29 of 33 scored misses, a contract clause covered the defect but no dynamic probe exposed it. Seven of eight findings were initially surfaced by hand, and benchmark selection was anchor-driven, so the paper does not establish ecosystem prevalence.

Artifact status: `rohithreddybc/tool-contract-conformance` is public, MIT licensed, has a populated `master` branch, 227 inspected blobs, 42 contracts, 25 test modules, and an offline reproduction path. It was inspected read-only and not executed.

Tools and repositories worth exploring now: [tool-contract-conformance](https://github.com/rohithreddybc/tool-contract-conformance), JSON Schema, state-transition assertions, mutation testing, evaluator provenance

Implementability score: 0.86

Core sources: [Executable-contract audit](https://arxiv.org/abs/2609.37315v1), [replication artifact](https://github.com/rohithreddybc/tool-contract-conformance)

## Turn prompt injection into a composable test matrix

pikit separates attack wording, delivery channel, defense, target agent, trace, and verdict. Its catalog contains 13 attacks, 16 carriers, 9 prevention strategies, 3 offline detection baselines, and 12 built-in agent scenarios. The public toolkit includes adapters for LangChain, OpenAI Agents SDK, PydanticAI, OpenClaw, and Hermes Agent.

### Why it matters

Single prompt-injection examples produce fragile security claims. An attack can fail because the payload never reached the agent, the carrier was unrealistic, the tool action was simulated incorrectly, or the verdict scored the wrong effect. A composable matrix makes those dimensions explicit and repeatable.

### How it fits

pikit belongs in the adversarial evaluation layer. It is strongest as a fixture generator and trace collector, not as a universal leaderboard. Teams still own the threat model, environment conformance, exact effect predicate, and release decision.

### Practical method

- freeze attack, channel, defense, target, model, and runtime versions per run;
- include clean controls and delivery receipts;
- use simulated consequential tools that record attempted effects without performing them;
- score full, partial, and unreached outcomes separately;
- preserve prompts, event traces, transcripts, and verdict records;
- test heuristic detectors for recall as well as precision.

Evidence caveat: the reported evaluation used one anonymized model with the pi coding agent in a production-like environment. Nine defenses produced a 71.8% relative reduction in attack success, while offline detectors had perfect precision and low recall. This does not establish general protection across models or real deployments.

Artifact status: the `Research/pikit` subtree in `Tencent/AI-Infra-Guard` is populated with 289 inspected entries, a CI workflow, datasets, framework adapters, demos, tests, and a subtree MIT license. The parent repository is public and Apache-2.0 licensed. It was inspected read-only and not executed.

Tools and repositories worth exploring now: [pikit](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/pikit), delivery receipts, exact-effect judges, paired clean and attacked fixtures

Implementability score: 0.88

Core sources: [pikit paper](https://arxiv.org/abs/2609.36817v1), [pikit repository](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/pikit)

## Working conclusion

Compose agents through explicit worker and artifact contracts. Test benchmark tools as state machines. Test adversarial inputs as a matrix with delivery and effect proof. These controls make a multi-agent stack inspectable before it becomes powerful.
