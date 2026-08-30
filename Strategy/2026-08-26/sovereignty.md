# Strategy Daily Sovereignty - 2026-08-26

## Scope note

The selected paper was first listed by arXiv on Wednesday, August 26 and submitted on August 25, inside the strict trailing 48-hour window. The immutable v1 abstract and HTML were inspected. No public implementation artifact was linked, and no external source code was cloned or executed.

## Preserve action-binding state across every handoff

A multi-stage agent can repeat the topic of a blocker while silently weakening its force. A ticket says approval is required before execution. A summary mentions that approval is unresolved. A downstream planner then treats it as context rather than a prerequisite. The information survived, but the constraint did not.

The paper tests this failure across 1,296 controlled synthetic episodes. Direct handoff preserved every blocker. Normal handoff compression produced 100.0 percent deactivation and 54.2 percent forbidden action. Restoring four fields, prerequisite, authority, fallback, and execution consequence, raised preservation to 100.0 percent and reduced forbidden action to 0.0 percent. A separate downstream verifier also eliminated forbidden action even while artifact deactivation remained 95.3 percent.

Why it matters: summaries, plans, memories, tickets, and handoff notes are not neutral text. They are intermediate control artifacts. Any transformation that can change an action path must preserve whether a condition is binding, who can clear it, what happens if it remains unresolved, and which action is prohibited.

Practical tools and methodologies worth exploring:
- represent blockers as typed records with prerequisite, authority, fallback, and execution consequence;
- require every summarizer or handoff generator to emit those fields unchanged or fail closed;
- compare source and transformed artifacts with deterministic preservation checks;
- run a downstream pre-action verifier even when the artifact passed a semantic-retention check;
- add compression, plan assimilation, ownership deferral, convergence, and precedent substitution to handoff regression tests.

Weakest point: the evaluation is synthetic and no public implementation artifact was linked. The control pattern is still cheap to test because it needs a typed handoff schema, deterministic comparisons, and adversarial fixtures rather than a new model.

Implementability score: 0.86

Durable deep dive:
- [Operational State Preservation](../operational-state-preservation/operational-state-preservation.md)

Core source:
- [When Must Becomes Maybe](https://arxiv.org/abs/2608.24569v1)

The formal carrier in the paper is stop status, unresolved prerequisite, responsible authority, and admissible fallback. The endpoint consequence is measured separately. A production contract should preserve both the carrier and the exact prohibited effect.
