# AgenticAI Daily Analysis - 2026-09-26

## Scope note

No new arXiv listing exists for Saturday, 26 September 2026. Category `recent` and `new` pages still show Friday, 25 September 2026 as the newest announcement batch. This note covers leftover Friday papers that the weekly synthesis did not promote, plus Saturday-visible official product evidence. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Compile skills into explicit state machines

HEXIS treats a skill document as source for a compiler, not as another prompt. The compiler maps clauses and tool interfaces onto an extended finite state machine: local instructions inside states, recorded intermediate results, and explicit transition conditions between operations. Updates are accepted only after static checks and replay of the current trace plus every previously accepted trace.

The measured lift is large enough to keep. Across four benchmarks and four executors, HEXIS improves success over Skill + ReAct by 16.1 percentage points on average. On Qwen3.8-27B, execution tokens fall 38.4 to 88.9 percent. The same Fable-compiled machines transfer to GLM-4.7-FlashX, Qwen3.5-9B, and Qwen3.8-27B without target-model recompilation. The test set is spreadsheet editing, LiveMath, InfiAgent data analysis, and SealQA long-context questions, with OpenCode among the executors.

Why it matters: reusable skills still fail when the model must rediscover control flow on every turn. Prescribed steps get skipped, and token cost is spent re-deriving the next legal operation. A compiled machine keeps reasoning inside a state while the runtime owns progress, data bindings, and legal continuations.

How it fits: this is the next control layer after skill admission. A SKILL.md remains the human-authored knowledge object. HEXIS compiles that object into an executable control graph with replay gates. SkillOpt-style document revision can still improve the source; the machine is what the executor is allowed to run.

Tools and methodologies worth exploring now:
- compile SKILL.md clauses into states, local instructions, and transition predicates;
- bind intermediate artifacts to named machine data slots;
- accept machine edits only after static checks and full-trace replay;
- transfer a compiled machine across models without rewriting it;
- keep OpenCode, Claude, or Hermes as the in-state executor, not as the control-flow owner.

Implementability score: 0.62

The pattern is clear and the evaluation is multi-benchmark. No paper-owned public repository resolved from the abstract, HTML, or PDF. Related cited repos such as OpenCode and SkillOpt are existing tools, not a HEXIS artifact. Treat this as an architecture reference until a compiler lands.

Core source: [HEXIS: Compiling Skills into Extended Finite State Machines](https://arxiv.org/abs/2609.30123v1)

## Scope memory to the family that certified it

Persistent skill memory can make a frozen model worse. On ProcStream-RSI, a 12-round code-repair stream, Orthogonal Regression Control already gates skill edits with execution evidence. Retrieving each accepted skill globally still dropped mean hidden trajectory utility to 0.713, below the static agent's 0.775, because locally valid edits interfered with unrelated families.

Matching retrieval scope to certification scope reverses that. Holding proposals and gate decisions fixed, family-scoped retrieval raised mean hidden trajectory utility from 0.713 to 0.816 and changed harmful deployments from six of eight streams to none. In 27 paired randomized-order streams, Scoped-ORC improved mean trajectory utility by 0.063 [0.037, 0.094] over Global-ORC, accepted 63 updates rather than 12, produced multiple accepted updates in 19 of 27 streams, and recorded 0 of 63 harmful acceptances.

Why it matters: an execution-grounded gate answers whether an edit is supported. It does not answer where that evidence authorizes later use. Global memory turns a locally proven skill into cross-family contamination.

How it fits: this is the retrieval counterpart to Friday's compaction rule. Compaction needs a durable carrier before context is deleted. Persistence needs a family, task, or repository scope before an accepted memory is eligible for later retrieval.

Tools and methodologies worth exploring now:
- store accepted skills with an originating family or repository identity;
- retrieve only memories whose certification scope matches the current task;
- keep a static or no-memory control beside global and scoped variants;
- count harmful accepts as checkpoint regressions, not as user complaints;
- prefer more scoped updates over fewer global ones.

Implementability score: 0.70

The intervention is cheap: namespaced memory keys and retrieval filters. The paper reports no public implementation repository, and ProcStream-RSI is a synthetic repair stream rather than a production coding agent.

Core source: [Scope Before You Persist](https://arxiv.org/abs/2609.29144v1)

## Working conclusion

Skills and memories become safer when the runtime owns their control graph and retrieval scope. Compile reusable procedures into replay-checked state machines, and load accepted memories only in the family that certified them.
