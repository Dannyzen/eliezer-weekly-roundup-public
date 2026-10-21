# AgenticAI Daily Analysis - 2026-10-21

This scan covers papers first listed by arXiv on 2026-10-21 and submitted on 2026-10-20. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Compress traces by phase and evidence value

TraceLite treats an agent trace as heterogeneous working state rather than one text stream. It keeps recent observations as text, renders older observations as images, removes overlap, and drops observation payloads after their phase expires. On 400 SWE-bench Verified tasks with GPT-5.6-Luna, it resolved 313 tasks, 78.25%, statistically comparable to the 78.00% full-trace baseline. Average input tokens fell 33.05%, API cost fell 21.30%, and compression added 0.438 seconds per observation.

The practical lesson is narrower than "turn history into images." The useful control is phase-aware retention: preserve high-fidelity evidence while it can still change the next decision, compact redundant history, and expire payloads after the workflow state makes them irrelevant. Token reduction without this evidence policy can damage task completion, as the paper's stronger-compression baselines did.

Implementable now:
- classify observations as recent, redundant, or phase-expired;
- keep authoritative outputs and active errors in text;
- evaluate compression against full-trace task success, tokens, cost, and latency;
- add rehydration for evidence needed by verification or review;
- start with shadow comparisons before changing production context.

Artifact status: the paper links a public repository whose default branch contains 48 files, including Python policies and rendering utilities. The repository was inspected read-only. The result is still paper-authored and concentrated on SWE agents, two backbone families, and selected benchmarks.

Implementability score: 0.84

Core sources:
- [TraceLite paper v1](https://arxiv.org/abs/2610.28612v1)
- [TraceLite repository](https://github.com/xjywhu/TraceLite)

## Turn business rules into executable agent tests

AgenTest mines rules from system prompts, tool definitions, and domain knowledge, refines them into Given-When-Then specifications, constructs a satisfying state and simulated user, runs the agent, then checks messages, tool calls, and state changes with a hybrid oracle. Across airline, retail, and telecom agents from tau2-bench, it produced 551 refined specifications. With two underlying models it found 89 and 121 violated specifications, 3.4 and 2.5 times the combined baselines.

The result that matters operationally is observability: about 60% of bug-triggering runs were invisible from final state alone. A successful-looking outcome can still include another user's data, a forbidden intermediate action, or an invalid tool argument. Agent acceptance therefore needs a workflow oracle, not only a final-state assertion.

Implementable now:
- mine candidate rules from prompts, schemas, support policy, and domain owners;
- review them into explicit Given-When-Then contracts;
- generate states that make each rule testable;
- assert over messages, tool calls, and state transitions;
- keep cross-user identity and resource ownership in the oracle.

Artifact status: the paper does not link a public implementation repository. The method is actionable with existing BDD, fixture, and trace tooling, but reproducing rule mining and hybrid oracles requires meaningful engineering. The evaluation covers three tau2-bench domains and two models.

Implementability score: 0.72

Core source:
- [AgenTest paper v1](https://arxiv.org/abs/2610.28116v1)

## Implementation implication

Context efficiency and agent correctness share one requirement: the harness must know which evidence and rules remain live at each step. Compress only after preserving authoritative evidence, and grade the full workflow against executable business contracts.
