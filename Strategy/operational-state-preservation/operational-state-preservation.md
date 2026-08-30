# Operational State Preservation

Last updated: 2026-08-26

Core finding: an agent handoff can retain the words of a constraint while removing its force. Reliable stacks need two controls: preserve binding state through every artifact transformation, then verify the live prerequisite and authority again before committing an effect.

Core source:
- [When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569v1)
- [Immutable v1 PDF](https://arxiv.org/pdf/2608.24569v1)

Related durable topics:
- [Context-to-Execution Integrity](../context-to-execution-integrity/context-to-execution-integrity.md)
- [Agent Authority Manifests](../agent-authority-manifests/agent-authority-manifests.md)
- [Runtime Governance](../runtime-governance/runtime-governance.md)

## Overview

Agent stacks repeatedly turn one representation into another: a conversation becomes a summary, a review becomes a ticket, a ticket becomes a plan, a plan becomes a delegated task, and a task becomes a tool call. These are not neutral rewrites when the source contains a prerequisite, approval boundary, veto, fallback, or prohibition.

The paper calls the missing invariant operational state preservation. A handoff is faithful only when it preserves both the proposition and the action set that proposition controls. Mentioning that approval is unresolved is not enough if the next agent may still proceed.

This belongs primarily in the Strategy layer. It governs how authority and obligations survive movement across models, memories, tickets, plans, agents, and execution boundaries. The implementation touches orchestration, but the load-bearing decision is what counts as permission to act.

## Why this finding won the week

Other strong findings improved individual layers. Recuris separated working state from skill memory. `llmmas-otel` made multi-agent traces perturbable. ComponentBench turned GUI tasks into component contracts. Microsoft Agent Framework strengthened runtime invariants.

This paper matters more because it exposes a failure between those layers. A system can identify the right blocker, store it, summarize it, trace it, and still weaken it during the next transformation. The failure applies to nearly every long-horizon workflow, and the first useful control does not require a new model.

Three facts make it unusually actionable:

1. The failure is measured after correct upstream identification, so it cannot be dismissed as ordinary model misunderstanding.
2. The intervention is structural: preserve a small binding-state record and re-check it at the action boundary.
3. The paper separates artifact repair from endpoint containment, which prevents a safe final action from hiding corrupt intermediate state.

## Core innovation

The paper turns handoff reliability into a stage-separated experiment:

1. Establish a valid blocker in the source workflow.
2. Transform it into a summary, plan, ticket, memory, or handoff note.
3. Measure whether the artifact still binds downstream action.
4. Give a local-view executor only that artifact and measure whether it performs a forbidden action.
5. Repair the artifact and gate the endpoint separately to identify where reliability is recovered.

The measured source carrier is:

`z = (stop status, unresolved prerequisite, responsible authority, admissible fallback)`

The endpoint consequence is evaluated separately as forbidden or admissible action. This distinction matters. The abstract describes prerequisite, authority, fallback, and execution consequence as the broader safety-blocker object, while the formal four-field carrier uses stop status instead of execution consequence. A production schema should preserve both the carrier and the exact effect rule. It should not collapse them into one vague `constraint` string.

## Evidence

The primary matrix contains 1,296 episodes across six model variants, five static transformation families, and three dynamic trajectories. A validation panel adds 476 episodes across seven other model variants. The combined evidence covers 1,772 episodes, 13 model variants, and 8,789 API calls.

Matched direct handoffs produced 100.0 percent preservation, 0.0 percent deactivation, and 0.0 percent forbidden action.

Normal handoff compression produced 100.0 percent deactivation and 54.2 percent forbidden action. More aggressive multihop conditions kept deactivation at 100.0 percent and raised forbidden action to 83.3 and 79.2 percent. Ownership deferral increased deactivation by 76.7 percentage points and forbidden action by 60.8 points relative to its paired control.

Restoring all four formal carrier fields to degraded artifacts returned preservation to 100.0 percent and forbidden action to 0.0 percent. A hard visible-authorization check, external permission lookup, or human approval gate also reduced forbidden action to 0.0 percent while the artifact remained degraded.

That last result is the architectural payoff: artifact preservation and endpoint containment are complementary controls. A safe effect does not prove the handoff is healthy, and a healthy handoff does not remove the need for a commit-time gate.

## Why it matters

### Summaries are control-plane compilation passes

A summary that carries action-relevant state is compiling one control representation into another. It needs schema validation, preservation checks, and failure semantics, not only semantic similarity.

### Tickets and memories can change authority

A ticket, plan, or memory entry can transform a veto into advice, move an obligation to an unnamed future owner, or substitute precedent for current authorization. The artifact is therefore part of the authority path.

### Endpoint-only safety hides coordination damage

A final authorization check can prevent one forbidden action while leaving a bad artifact available to later agents, audits, retries, or human operators. The runtime must record both artifact integrity and effect admission.

### Correct recognition is not enough

The experiment conditions on correct upstream identification. Better retrieval or a stronger model cannot guarantee preservation after a later compression or handoff step.

## Fit in the agentic stack

- Source layer: establishes the canonical obligation, authority, and action consequence.
- State layer: stores a typed, addressable binding-state record.
- Transformation layer: compiles summaries, plans, tickets, and memories without weakening that record.
- Orchestration layer: passes constraint identifiers and live status across agents and retries.
- Execution-control layer: checks the current prerequisite and authority before a protected effect.
- Evidence layer: records source state, transformed artifact, preservation verdict, gate decision, and effect receipt.

The key rule is simple: prose may describe binding state, but prose is not the source of truth for whether an effect is permitted.

## Practical tools and methodologies worth trying now

### Define a minimal binding-state schema

Use JSON Schema or Pydantic to require:

- `constraint_id`
- `status`
- `prerequisite`
- `responsible_authority`
- `safe_fallback`
- `prohibited_effect`
- `clearance_event`
- `source_digest`
- `policy_version`
- `updated_at`

The four paper fields are the minimum carrier. `prohibited_effect`, `clearance_event`, source identity, and policy version make the record usable at the execution boundary.

### Keep canonical state outside generated prose

Store the binding-state object in a database, event log, ticket field, or workflow state store. A summary should include its identifier and human-readable rendering, not become the only copy.

### Add a transformation preservation gate

Before accepting a generated summary, plan, or handoff:

1. Extract or render the required binding fields.
2. Compare them with the canonical record.
3. Reject missing or weakened fields.
4. Preserve the prior artifact and failed transformation as evidence.

Start with deterministic equality and explicit status transitions. Do not begin with another LLM judge.

### Add a commit-time effect gate

Before a protected tool call, query the canonical state by `constraint_id`. Require the prerequisite to be cleared by the named authority under the current policy version. Bind the decision to the exact resource and effect.

OPA or Cedar can express the policy check. OpenTelemetry can record preservation and effect-admission spans. Temporal, LangGraph, or another durable workflow engine can carry the constraint identifier across waits and retries, but none of them provides the invariant automatically.

### Build adversarial handoff fixtures

Use the paper's five transformation families as regression tests:

- compression;
- plan assimilation;
- convergence;
- ownership deferral;
- precedent substitution.

Add local variants for approval carryover, deadline pressure, cloned tickets, resumed sessions, stale exceptions, and delegated ownership.

## Minimal pilot

Choose one workflow where an approval or blocker crosses at least two representation boundaries.

1. Record the blocker in the typed schema.
2. Generate the normal summary or handoff.
3. Run preservation checks against the canonical record.
4. Attempt the protected effect through a commit-time gate.
5. Save the artifact verdict and effect receipt separately.
6. Re-run with all five weakening transformations.

Definition of done is not a safe demo. It is a regression suite that proves both the artifact and the endpoint remain governed after compression, retry, and delegation.

## Implementation complexity

Thin implementation complexity: low to medium. One workflow can add typed blocker fields, deterministic preservation checks, and a final authorization gate with ordinary application code.

Platform implementation complexity: medium to high. The difficult work is propagating stable identifiers across queues, model calls, memories, human approvals, retries, and external providers while preventing stale or cloned artifacts from acquiring authority.

Implementability score: 0.86

The score is high because the thin control uses existing schemas, policy engines, workflow state, and trace tooling. It is not higher because the paper provides no public implementation artifact, production prevalence is unmeasured, and end-to-end propagation across heterogeneous systems remains substantial.

## Weakest point and guardrail

The unflattering fact is that the task population is synthetic and conditions on a correctly identified blocker. It does not show how often production systems weaken real constraints, nor does it solve incorrect source-state recognition.

That limitation is survivable here because the proposed invariant is cheap to test on real internal workflows before broad adoption.

Guardrail: treat the paper's rates as evidence that the failure can be severe, not as a production prevalence estimate. Build local fixtures from actual approval, billing, deployment, and external-message boundaries, then measure preservation and forbidden-effect rates under the current models and prompts.

## What remains conceptual or unresolved

- Generalization from blockers to budgets, data-use restrictions, revocation, legal obligations, and multi-party consent.
- Correct source-state establishment when policies conflict or authority is ambiguous.
- Constraint identity across copied tickets, forks, merged plans, and cross-provider retries.
- Safe composition when several constraints have different authorities and fallbacks.
- Human interfaces that expose live binding state without turning operators into raw-schema readers.
- Independent replication of the reported model and transformation effects.

## Strategic implications for Danny's product thinking

The product opportunity is not better summarization. It is state-preserving agency.

For Hermes and FriendVM, blockers, approvals, budget limits, delivery boundaries, and external-action permissions should be first-class policy-bearing objects. Beads and Kanban can carry identifiers and human workflow state, but generated comments and handoffs should never become the authority source by themselves.

This strengthens Danny's preference for fail-closed gates and proof-backed completion. The agent may compress context aggressively for speed. It may not compress away the force of an unresolved obligation.

A credible agent platform should be able to answer five questions for every protected effect:

1. Which binding state applied?
2. Which transformation carried it here?
3. Did the artifact preserve its operational role?
4. Which authority cleared it?
5. Which receipt proves the admitted effect matched the clearance?

That is a stronger product claim than “the agent remembers context.” It says the system preserves what still matters when context changes form.

## What to explore next

- Build a small open conformance harness for artifact preservation and endpoint containment.
- Add typed blocker fields to one Hermes or FriendVM workflow and capture failure fixtures.
- Compare deterministic preservation checks with LLM-based artifact judges only after a deterministic baseline exists.
- Test whether current ticket, memory, and summarization pipelines preserve constraint identity through retries and delegation.
- Extend authority manifests with `constraint_id`, clearance event, prohibited effect, and transformation lineage.

## Source status

The immutable arXiv v1 abstract, HTML, and PDF were inspected. The PDF's methods, result tables, repair ablations, endpoint controls, evidence scope, and limitations were read directly. No public implementation repository or dataset is linked from the primary source. No external code was cloned, installed, built, imported, or executed.
