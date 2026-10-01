# Composable Agent Harnesses

Updated: 2026-09-30

## Overview

Treat the model and its harness as one deployable worker. Raven is the strongest signal from the last seven days because it turns this idea into a broad, inspectable system: a registry of model-harness pairs, protocol adapters, dependency-graph planning, artifact handoffs, persistent experience, and bounded harness evolution.

The week also produced strong work on executable benchmark contracts, prompt-injection matrices, and typed tool authorization. Those findings improve individual controls. Raven changes the unit that the stack composes. That architectural leverage makes it the Deep Dive Wednesday winner.

Raven was submitted to arXiv on September 27, 2026 and surfaced as the number one Hugging Face paper on September 30. The public `EverMind-AI/Raven` repository is Apache-2.0 licensed, has a populated `main` branch, and exposed 4,268 blobs at verification time. Its README documents ACP, CLI, and OpenAI-compatible adapters plus presets for 13 third-party agents, including Hermes Agent.

## Core innovation

Raven treats each executable model-harness pair as a callable worker with its own tools, execution policy, and domain strengths. A Host Agent decomposes the goal, selects registered specialists, emits a directed acyclic graph, validates the plan, dispatches ready nodes, preserves artifacts, and integrates the deliverable.

Five primitives matter:

1. **Worker as deployment unit.** The capability is the model plus the surrounding prompt policy, tools, runtime, memory, and configuration.
2. **Registry as discovery plane.** The orchestrator chooses among explicit worker capabilities instead of assuming one universal agent.
3. **Graph as run contract.** Nodes identify workers and edges identify required artifact dependencies.
4. **Artifact ledger as handoff truth.** Workers exchange durable outputs instead of relying on conversational summaries alone.
5. **Evaluation-gated adaptation.** Harness changes are proposed, screened, frozen, and tested with the task model held fixed.

The formal claim is narrower than the product language. Composition can expand reliable task coverage when local capabilities are complementary, handoffs are compatible, planning and execution errors are bounded, and the total resource budget includes coordination cost. These are useful design conditions. They do not prove that arbitrary agent composition improves outcomes.

## Evidence

Raven introduces the Multi-Agent Orchestration Benchmark with 140 occupational requests and reference graphs over four specialists. Under matched backbones, Raven reported:

- Qwen3.8-27B Node F1 of 0.923 versus 0.776 for the strongest baseline;
- Qwen3.8-27B exact graph match of 0.711 versus 0.607;
- DeepSeek-V4-Flash-0731 exact graph match of 0.867 versus 0.762;
- exact-match gains of 10.4 and 10.5 percentage points across the two tested backbones.

This is meaningful evidence for specialist selection and dependency prediction. It is incomplete evidence for end-to-end product reliability. The benchmark grades proposed graphs before worker execution, and the paper evaluates planning, specialist performance, harness evolution, and skill reuse as separate layers.

The weakest point is source independence. EverMind authored the paper and implementation. The repository was inspected read-only; no installer, source, or benchmark was executed for this research asset. Independent reproduction remains necessary.

## Why it matters

Agent products are moving from one general agent with a large prompt toward fleets of specialized workers. The hard problem shifts to interface integrity:

- Which worker version actually ran?
- What authority did it receive?
- Which inputs and artifacts crossed the boundary?
- Which dependency made the node ready?
- What budget, retry policy, and deadline governed execution?
- Which receipt proves the claimed terminal state?

Raven makes the execution graph visible. A production stack must make every graph edge enforceable. Without typed worker and artifact contracts, composition multiplies ambiguity, authority, and failure propagation.

## Fit in the agentic stack

| Layer | Job | Raven signal | Required production control |
| --- | --- | --- | --- |
| Model | Generate decisions or artifacts | Backbones remain replaceable | Bind every run to exact provider, model, and parameters |
| Worker harness | Turn a model into an executor | Model-harness pair is the callable unit | Version prompt policy, tools, runtime, memory, and configuration together |
| Registry | Advertise available workers | Capabilities guide assignment | Verify identity, health, cost envelope, and authority scope before admission |
| Orchestrator | Build and schedule the graph | Host Agent emits and runs a DAG | Compile plans through deterministic admission and budget checks |
| Artifact plane | Carry work across nodes | Edges identify artifact dependencies | Use immutable artifact IDs, schemas, lineage, and acceptance checks |
| Evidence plane | Prove what happened | Runtime records artifacts and status | Keep append-only events, external-state receipts, and terminal proofs outside worker custody |
| Memory and skills | Reuse experience | EverOS and Skill Forge support continuity | Separate evidence, procedures, and preferences; preserve source and audience scope |
| Execution control | Authorize side effects | Raven exposes a broad orchestration surface | Bind every node to an authority manifest and exact effect capabilities |

The primary home is AgenticAI because the central contribution is an executable composition architecture. The strategic consequence is direct: orchestration must never become an authority shortcut.

## Practical tools, repositories, and methodologies worth trying now

### 1. Define a worker contract

Start with a small, versioned schema:

```yaml
worker_id: hermes-researcher
harness_version: 1.0.0
protocol: acp
capabilities:
  - sourced_research
accepted_inputs:
  - research_brief.v1
produced_artifacts:
  - research_report.v1
resource_envelope:
  max_runtime_seconds: 1800
  max_cost_usd: 5
allowed_effects:
  - read_public_web
terminal_receipt: worker_run_receipt.v1
```

Add health state, model identity, sandbox profile, network policy, retry class, and artifact size limits before any consequential deployment.

### 2. Compile plans before dispatch

Represent the proposed run as a DAG. Reject unknown workers, cycles, missing producers, schema-incompatible edges, unbounded budgets, and unauthorized effects before the first worker starts.

### 3. Make artifacts first-class

Address artifacts by immutable ID and content hash. Record producer, consumer, schema version, source run, acceptance result, and supersession. Pass references across worker boundaries; keep raw evidence available for review.

### 4. Separate orchestration from authority

Let the host propose worker assignments and dependencies. Let a runtime-owned policy service decide which workers, credentials, networks, tools, and effects may be released. A graph edge carries data dependency. It does not grant authority.

### 5. Evaluate the composition delta

Run the same task through the best standalone worker and the composed graph. Measure outcome quality, cost, latency, retries, handoff failures, evidence completeness, and intervention utility. Promote composition only when its net gain survives the coordination cost.

### 6. Use Raven as a reference implementation

Inspect the Raven registry, adapters, graph runtime, artifact flow, and Hermes preset. Keep any experiment isolated and read-only until the trust boundary, install path, outbound network behavior, secret access, and cleanup procedure are reviewed. Do not adopt self-evolution or shared group memory as a first step.

## Implementation complexity

| Work item | Complexity | Reason |
| --- | --- | --- |
| Versioned worker contract | Medium | Schema design and adapters are ordinary engineering |
| Capability registry | Medium | Discovery is easy; trust, health, and version truth are harder |
| DAG planner and scheduler | High | Retries, cancellation, partial failure, budgets, and resume semantics interact |
| Artifact and evidence ledger | Medium to high | Identity, lineage, retention, and external-state receipts must stay consistent |
| Authority isolation | High | Credentials, tool scopes, networks, and exact effects require runtime enforcement |
| Harness self-evolution | Very high | Search can optimize the wrong objective and silently expand the attack surface |
| Cross-device collaboration network | Conceptual | The paper lists it as future work and supplies no production proof |

## Implementability score

**0.68**

A bounded prototype is implementable now with existing schemas, DAG engines, artifact stores, ACP or CLI adapters, and policy gates. Production deployment requires substantial work in cancellation, recovery, authority isolation, evidence custody, version truth, and independent evaluation. Raven self-evolution and the cross-device network should remain deferred until the static composition path is measurable and safe.

## What remains conceptual or unproven

- End-to-end gains from graph planning across independently operated workers need independent reproduction.
- The paper reports that the group-memory layer is disabled by default and was not evaluated.
- EverOS records have an owner field without a separate author field, and extraction can rewrite text. Raven compensates with a host-side append-only ledger, while worker-native writes remain outside that group policy.
- The All-Domain Collaboration Network is future work.
- Cross-worker authorization, secret boundaries, network containment, cancellation, and rollback need stronger treatment than registry capability descriptions.
- Automated harness evolution has held-out evaluation, yet it still needs security regression gates and an explicit authority ceiling.

## Strategic implications for Danny’s worldview and product thinking

The model becomes a replaceable component. The durable product is the governed worker contract and the evidence-bearing runtime around it.

For Hermes and FriendVM, each node can expose bounded capabilities through an explicit adapter while retaining its own local policy, memory, and tools. A host can compose those nodes without collapsing their authority domains. Bigs or another private control plane can own registry truth, artifact identity, run events, and receipts while personal nodes keep local data and final approval boundaries.

For client systems, the transferable asset is the operating method: worker definitions, artifacts, policies, evaluation fixtures, and run evidence. Customers retain their data, domain judgment, and release authority. Models and specialist agents can change without replacing the control plane.

The design verdict is simple: compose workers only after their contracts are typed, their artifacts are durable, their authority is bounded, and their terminal claims are externally provable.

## Core sources

- Raven paper, immutable v1 abstract: https://arxiv.org/abs/2609.33439v1
- Raven paper, immutable v1 PDF: https://arxiv.org/pdf/2609.33439v1
- Raven HTML paper: https://arxiv.org/html/2609.33439v1
- Raven repository: https://github.com/EverMind-AI/Raven
- Raven project page: https://raven.evermind.ai/
- Hugging Face paper page: https://huggingface.co/papers/2609.33439

## Supporting source

- ToolFence, a complementary typed-authorization design for the effect boundary: https://arxiv.org/abs/2609.37196v1
