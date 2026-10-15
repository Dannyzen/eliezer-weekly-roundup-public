# AgenticAI Daily Analysis: 2026-10-14

## Thesis

Selection and verification fail when the model must infer hidden references while executing the task. Route skills explicitly, and derive expected tool arguments independently before judging a candidate call.

## Deep Dive Wednesday winner: skill routing is a control plane

Lost in Implicit Routing is the week's strongest finding because it exposes a system boundary that large skill catalogs currently leave inside the executor's hidden reasoning. The failure is measured at scale, can remain invisible in task-success metrics, and has a practical mitigation that uses ordinary retrieval and routing components.

The durable conclusion is stronger than “use RAG for skills.” Catalog admission, candidate generation, selection, loading, use, and final verification need separate evidence. Fixed preselection also needs a bounded reroute path because later execution evidence can reveal a missing capability.

Deep dive: [Skills as Control: make skill routing an explicit control plane](../skills-as-control/skills-as-control.md#october-14-2026-deep-dive-make-skill-routing-an-explicit-control-plane)

## Lost in Implicit Routing: preselect skills before task execution

Reusable skills save context only if the agent loads the right one. This study holds SkillsBench tasks and their golden skills fixed, then adds irrelevant skills. With 1,000 irrelevant skills, loaded-skill recall falls from 73.6% to 27.4%, while the zero-load rate rises from 9.3% to 51.6%. Explicit selection from the same library retains 73.9% recall.

The failure is primarily semantic interference from skill descriptions, not frequent substitution of one plausible skill for another. Masking irrelevant descriptions largely restores routing, while asking the executor to plan skill use still underperforms explicit preselection. Skill discovery and task execution should therefore be separate stages with separate evidence.

Why it matters: a large skill catalog can look available while the runtime silently behaves as if most skills do not exist. Success metrics alone hide whether the intended skill was loaded.

How it fits into the stack: capability discovery and context assembly. A deterministic or separately evaluated router should shortlist skills before the executor receives task instructions.

Tools and methodologies worth exploring now:
- explicit top-k skill preselection outside the executor prompt;
- loaded-skill recall, zero-load rate, substitution rate, latency, and task success as separate metrics;
- description ablations that isolate semantic interference;
- frozen skill-library snapshots and selection receipts;
- a no-skill baseline and a golden-skill upper bound.

Artifact status: the public repository has a populated 55-entry tree with manifests, routing experiments, reproducibility documentation, source indexes, and offline tests. No root license or tagged release was detected. It was inspected read-only and not executed.

Caveat: proprietary-model validation covers a 37-task subset, and field-level masking uses fewer tasks and repetitions than the main study. Preselection can omit a needed skill and adds retrieval latency.

Implementability score: **0.88**

Core sources:
- [paper v1](https://arxiv.org/abs/2610.18522v1)
- [official repository](https://github.com/jinlinll/lost-in-implicit-routing)

## DeRef: derive the expected argument before seeing the candidate

Tool-call judges accept correct values less often when the value's source is absent from their input. The failure appears for schema defaults, inferred values, and history truncated away from the judge. A controlled relocation test shows a stronger failure: judges can prefer a visible wrong reference over a correct value whose derivation is hidden.

DeRef separates derivation from judgment. One model reads the full history without seeing the candidate and writes the expected reference. The judge then compares the candidate against that reference. Across three benchmarks and seven judges, DeRef improves overall argument AUROC. On the controlled test, AUROC rises from chance or below to 98.40 through 99.59.

Why it matters: asking one judge to reconstruct missing evidence and score the candidate entangles two failure modes. A high score can reflect reference visibility rather than argument correctness.

How it fits into the stack: tool-call verification. The verifier needs a candidate-blind derivation record with source spans, schema defaults, transformations, and uncertainty before it sees the proposed argument.

Tools and methodologies worth exploring now:
- candidate-blind reference derivation;
- source-span and schema-default receipts for every derived value;
- separate derivation confidence and candidate-match scores;
- deterministic checks for types, ranges, identifiers, and exact external state;
- human review for high-impact arguments or ambiguous multiple-valid-value cases.

Artifact status: the public Apache-2.0 repository has a populated 106-entry tree with DeRef code, benchmark builders, prompts, inputs, and evaluation modules. It has no tagged release. It was inspected read-only and not executed.

Caveat: each benchmark item has one gold value even when multiple values could be valid. The paper reports 3% and 4% unresolved label uncertainty in two author-built wrong-value sets. The authors position DeRef as review support, not a replacement for deterministic or human checks.

Implementability score: **0.81**

Core sources:
- [paper v1](https://arxiv.org/abs/2610.18497v1)
- [Apache-2.0 implementation](https://github.com/SarielMa/DeRef_release)

## Practical implementation order

1. Log which skills were considered, selected, loaded, and used.
2. Add a separate skill-preselection stage with frozen catalog identity.
3. Build candidate-blind derivation records for consequential tool arguments.
4. Compare derivation, candidate, and final external-state receipt as distinct evidence.
5. Shadow both controls before allowing either to block production work.
