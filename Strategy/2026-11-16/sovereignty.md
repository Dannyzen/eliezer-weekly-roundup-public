# Strategy Daily Analysis: 2026-11-16

Today's strategy signal is that agent safety and privacy need controls over trajectories and derivations, not only individual calls or stored rows.

## 1. Verify the plan and enforce every effect

Soteria composes hierarchical plans from reusable sub-plans, verifies tool contracts, progress, and policy compliance before execution, then checks every proposed call again with a runtime specification monitor. A blocked action returns the executor to a verified recovery path instead of leaving it to improvise.

Why it matters: runtime blocking alone can preserve safety while destroying task completion. A verified plan supplies global foresight and a recovery route, while the monitor protects against planner or executor deviation.

Implementable now:
- formalize tool preconditions, postconditions, and sequence policies;
- build reusable sub-plans for recurring workflows;
- verify progress and policy conformance before the first side effect;
- monitor every proposed call at runtime against the same specifications;
- preserve the plan, proof result, blocked call, recovery path, and final receipt.

Evidence and caveat: across 207 tasks, three benchmarks, and four models, Soteria reports 100 percent specification conformance and task-success gains of 4.7 to 43.9 percentage points over the best baseline. Policy specifications and tool contracts are generated with LLM assistance and manually validated. The method still allows the strongest partially verified plan when full verification fails, so the runtime monitor remains the hard safety boundary. No public implementation repository was identified from the primary source.

Artifact status: immutable paper and official NeurIPS session inspected. Nothing was executed.

Implementability score: 0.68

Core source: [Soteria v1](https://arxiv.org/abs/2611.17880v1)

Supporting source: [NeurIPS 2026 oral session](https://nips.cc/virtual/2026/loc/atlanta/session/176366)

## 2. Make forgetting follow the memory derivation graph

LinEra encrypts each derived memory under keys connected to every source the memory writer saw. Forgetting a source punctures its key and makes the full descendant closure unreadable, even if an attacker later obtains all stored files, backups, vector indexes, and current keys.

Why it matters: deleting a message or vector does not erase summaries, extracted facts, profile entries, free pages, or backups derived from it. A deletion guarantee needs provenance capture at write time and cryptographic revocation across the derivation graph.

Implementable now:
- record every model-visible source as a parent of each derived memory;
- separate source objects from summaries, facts, profiles, and embeddings;
- bind encryption keys to lineage rather than object identity alone;
- keep memory-writer context small to limit the forgetting radius;
- re-derive affected memories from surviving sources after erasure.

Evidence and caveat: in the largest-model evaluation, logical deletion exposed 70 of 71 forgotten secrets, per-object or epoch keys exposed 67, and LinEra exposed none. The guarantee has an availability cost: forgetting 1 percent of turns erased 73.0 percent of memories under session-level summaries, versus 3.8 percent with four-turn windows. The threat model excludes model weights, copies exported before deletion, running-process side channels, and repeated facts in independent sources.

Artifact status: MIT repository, v1.0.0 release, paper, and experiment descriptions inspected read-only. No source was cloned or executed.

Implementability score: 0.58

Core source: [LinEra paper v1](https://arxiv.org/abs/2611.18133v1)

Public artifact: [yulliwasameur/linera](https://github.com/yulliwasameur/linera)

## Working conclusion

Authority should be checked over the full action trajectory, and privacy should be enforced over the full derivation closure. Per-call guardrails and row deletion are incomplete control surfaces.
