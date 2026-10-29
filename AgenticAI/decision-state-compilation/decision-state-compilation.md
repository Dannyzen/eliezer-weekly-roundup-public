# Decision-State Compilation for Agent Memory

## Overview

Agent memory should not hand facts directly to a decision-maker. It should compile the facts, their source-linked governing conditions, and the actions those conditions permit into explicit decision state.

SciValidityBench makes this distinction executable. A remembered result can be accurate while its use is invalid. A p-value of 0.03 can support confirmation when the outcome and stopping rule were fixed in advance, yet support exploration only when the outcome was selected after inspecting twenty results. The fact is identical. The governing state changes the legal decision.

This is the strongest finding of the week because it closes the gap between three themes already present in this repository: provenance, memory authority, and executable evaluation. Other strong findings measured workload scheduling, evolving teams, instruction-stack drift, and workload-owned identity. Those improve a subsystem. Decision-state compilation defines the contract that decides whether retained evidence may influence an action at all.

Primary layer: AgenticAI memory systems and trajectory-aware evaluation.

Adjacent strategic layer: evidence provenance and context-to-execution integrity. Compiled state is evidence for a decision, not authority by itself. A separate execution-control layer must still bind the decision to a permitted effect.

## Core innovation

SciValidityBench couples five elements that are often evaluated separately:

1. A deterministic event history.
2. A state contract that names decision-governing variables.
3. A compiler that derives source-linked state from distributed events.
4. A programmatic oracle over legal actions.
5. Controlled interventions that test whether the reader uses the decisive state.

The benchmark contains 64 TaskSpecs across five validity modules and six domains: machine learning, A/B testing, clinical research, bioinformatics, systems, and causal inference. It compares raw events, BM25 retrieval, a generic Event Graph, a flat compiled-state view, and a typed scientific-state ledger.

Across four locked model families, compiled state improved TaskSpec-balanced valid decision-making by 9.2 to 18.8 percentage points over a generic Event Graph. BM25 retrieval did not reproduce the cross-family gain. Content-identical flat and typed views showed that exposing governing state mattered more than a specific graph serialization. Exact repair of missing target state exceeded edit-matched irrelevant repair by 18.6 validity points on average.

The decisive innovation is the diagnostic design. Counterfactual pairs hold non-target information fixed while changing one governing state value. Corruption removes oracle-required state. Exact and irrelevant repairs separate genuine state use from answer preference, formatting effects, and generic text perturbation.

## Why it matters

Retrieval benchmarks ask whether the agent can find the record. Operational agents need a stricter question: should this record influence this decision now?

That distinction appears across the agentic stack:

- A customer status may be accurate but stale after a later cancellation.
- A test result may be real but ineligible for release because the environment or acceptance contract changed.
- A remembered approval may be authentic but scoped to a different resource, time window, or effect.
- A prior tool result may be correct but superseded by a newer source-of-truth observation.
- A successful historical procedure may be irrelevant after a dependency or policy revision.

A source citation alone cannot answer these questions. The system needs state variables such as validity interval, scope, supersession, selection procedure, missingness, comparability, and relevance. It then needs an oracle or policy that maps those variables to legal decisions.

This reframes memory architecture. The memory store preserves episodes and facts. A domain compiler derives decision state. A reader consumes that state. An execution gate checks authority and effect scope. Keeping these layers separate makes failures localizable.

## Fit in the agentic stack

### 1. Evidence layer

Preserve immutable source episodes, event identity, actor, time, and lineage. Do not replace the evidence with the compiled view.

### 2. State-compilation layer

Derive named decision variables from distributed evidence. Every compiled field should retain its source references, derivation version, and as-of time.

### 3. Decision layer

Expose legal actions and a deterministic or policy-backed oracle. An agent may explain the choice, while the admissible action set remains external to free-form reasoning.

### 4. Evaluation layer

Use counterfactual pairs, required-state corruption, exact repair, and matched irrelevant repair. Score valid decision-making separately from retrieval, state fidelity, and final-answer preference.

### 5. Execution-control layer

Treat a valid decision as a candidate action. Recheck identity, authority, current state, budget, and exact effect before mutation. Scientific validity does not grant operational permission.

## Practical tools, repositories, and methods to try now

### SciValidityBench

The public Apache 2.0 repository contains the 64-TaskSpec catalog, deterministic generators, five memory views, state compilers, reader protocol, counterfactual and corruption operators, deterministic scoring, examples, and release tests. The tree was inspected read-only. It was not cloned, installed, imported, or executed during this research run.

Repository: https://github.com/SciValidityBench/SciValidityBench

Project site: https://scivaliditybench.github.io/SciValidityBench/

### A bounded implementation spike

Start with one real workflow where an agent currently retrieves historical facts before a decision. Good candidates are release approval, client-record status, expense classification, or task handoff.

Define one TaskSpec-like contract:

- `events`: immutable source records;
- `state`: decisive variables with source references;
- `legal_actions`: explicit outcomes such as proceed, explore, abstain, or escalate;
- `oracle`: deterministic mapping from state to legal actions;
- `counterfactual`: one changed state variable that must change the legal action;
- `corruption`: one missing required field that must force abstention;
- `receipt`: compiler version, evidence IDs, state, decision, and timestamp.

Then compare four views on the same cases: raw history, retrieval-only excerpts, generic event graph, and compiled decision state. The point is to measure decision validity, not to prove that one storage format is universally best.

### Methodologies worth adopting

- Contract-first TaskSpecs for every high-impact decision class.
- Event sourcing for immutable evidence and reproducible state derivation.
- JSON Schema or Pydantic models for typed state and legal actions.
- Property-based tests that vary one governing condition at a time.
- Mutation testing for missing, stale, or incorrectly scoped state.
- Provenance receipts that link each compiled field to source events.
- Abstention as the required outcome when oracle-required state is absent.

## What is implementable now

A single workflow can adopt this pattern with ordinary engineering effort:

1. Preserve source events.
2. Name governing variables.
3. Compile a typed state object.
4. Define legal actions and an oracle.
5. Generate counterfactual and corruption fixtures.
6. Gate decisions on complete state.
7. Retain the decision receipt.

The repository provides usable contracts and examples, and its deterministic mechanics require no external model service. Teams can borrow the pattern without adopting the scientific domains.

## What remains architecture-heavy

The difficult work is authoring trustworthy state contracts and oracles for open-ended business domains. Scientific tasks have comparatively crisp validity rules. Client operations, compliance, and organizational decisions often contain disputed policy, incomplete sources, exception paths, and human judgment.

A production compiler also needs:

- schema versioning and migrations;
- conflict and supersession handling;
- current-source refresh rules;
- field-level provenance and confidence;
- clear ownership for oracle changes;
- separation between decision validity and execution authority;
- review paths when the state contract is incomplete.

The paper is a two-author preprint evaluated on generated deterministic histories and four model families. Its public artifact is fresh, with one GitHub star and no tagged release at inspection time. The measured gains establish a strong mechanism inside the benchmark, not independent production replication.

## Implementation complexity

Complexity: medium for one bounded workflow, high for a general platform.

The data structures and tests are straightforward. The hard part is deciding which conditions govern a decision and keeping those conditions current across policy changes. A poor state contract can make an invalid decision look formally justified.

Implementability score: 0.76

The score reflects a runnable reference implementation and a clear bounded adoption path, reduced by domain-modeling cost, preprint maturity, and the absence of independent production validation.

## Strategic implications for Danny's worldview and product thinking

The product primitive is not better memory retrieval. It is inspectable decision state.

This supports a consistent architecture for Danny's agentic systems:

- raw interactions and source records remain evidence;
- memory stores facts without silently promoting them to authority;
- domain compilers produce visible, source-linked state;
- decision contracts expose what actions the state licenses;
- humans can inspect and amend the contract;
- execution control binds a valid decision to one approved effect;
- receipts make the result replayable and contestable.

This is especially useful for co-created systems. Customers retain ownership of the governing definitions and exception rules. The agent handles evidence assembly and state compilation. Product quality becomes visible in the state object, counterfactual tests, and receipts instead of being hidden inside a prompt.

The strategic claim is simple: durable agents need a compiler between memory and action.

## Core sources

- [The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory, arXiv v1](https://arxiv.org/abs/2610.34767v1)
- [SciValidityBench reference implementation](https://github.com/SciValidityBench/SciValidityBench)
- [SciValidityBench project site](https://scivaliditybench.github.io/SciValidityBench/)
