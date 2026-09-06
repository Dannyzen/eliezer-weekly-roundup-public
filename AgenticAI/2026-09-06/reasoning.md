# AgenticAI Daily Analysis - 2026-09-06

No new Sunday arXiv listing. Category recent pages still open with Friday, 4 Sep 2026 as the newest heading. The papers below were submitted 29 Aug and 3 Sep 2026 UTC, first listed in that Friday batch, and were not used in the 2026-09-04 synthesis or the 2026-09-05 daily. Do not describe them as "new today."

## HTTP 200 is not a tool-result

An agent calling a production API cannot tell a true empty match from a query the server did not understand. Both return HTTP 200 with a parsable body. There is no exception to catch and no field to branch on. SilentProbe measures that gap instead of treating it as model failure.

The static audit is the cheap part. Across 721,320 parameters in 2,501 independently published OpenAPI documents, 7.5% declare an enumeration and 15.2% declare any machine-checkable constraint. 40.1% of documents state at least one constraint in prose that the schema does not encode. Constraint form, not vendor identity, predicts honesty on live calls. Machine-checkable constraints yielded an honest error in 111 of 111 schema-derived perturbations. Prose-only constraints failed silently in 44 of 61 (`p = 2e-13`). A vocabulary that the description merely exemplifies was missed by every one of twelve models on 88 of 88 attempts. Vocabularies written out in full were used correctly. Downstream, in full agent loops, models detected the silent failure in 12% of cases, repaired it in 0%, asserted a false negative to the user in 41%, and invented a figure in 12%.

The practical rule in the repository README is sharper than the paper title: `e.g.` is more dangerous than an incomplete closed list. An example invites invention. A closed list keeps the model inside the documented set even when that set is incomplete. Promoting the vocabulary into the schema removes the silent path.

Why it matters: tool-using agents treat HTTP 200 plus JSON as success. That is the same cheap-check failure as a green functional test or a crash-free PoC. The environment has misled the model by omission. Self-repair cannot converge on a vocabulary it was never shown.

Fit in the stack: this belongs in trajectory-aware evaluation and gateway governance. The tool schema is the first oracle. The HTTP status is not.

Practical tools and methodologies worth exploring now:
- put enumerations and numeric bounds in the machine-readable schema, not only in prose;
- reject `e.g.`-only vocabularies at tool admission;
- treat HTTP 200 empty or partial bodies as ambiguous until a schema-valid error or an explicit no-match field exists;
- log silent-failure, false-negative, and fabricated-figure rates separately from tool-call success;
- keep a run identifier on every tool call so a single perturbation can be re-fetched.

Artifact status: [Jasper0122/silentprobe](https://github.com/Jasper0122/silentprobe) resolves, MIT, populated `master`, 115 tree entries, created 2026-08-28. README, `data/`, and `out/` are present. Inspected read-only via GitHub API and raw README. Nothing was cloned, installed, or executed. Live measurements used Monid as an aggregation layer in front of 27 vendors. Replicating those live calls is a separate procurement step.

Evidence caveat: executed perturbations cover endpoints reachable through one aggregator. The 12% / 0% / 41% / 12% downstream rates are from the v1 PDF and the repository README, not an independent rerun.

Implementability score: 0.82

Core sources:
- [SilentProbe, arXiv:2609.00035v1](https://arxiv.org/abs/2609.00035v1)
- [Jasper0122/silentprobe](https://github.com/Jasper0122/silentprobe)

## A shared model name is not a frozen instrument

Language-model judges now gate training data, score generations, and drive leaderboards. That stack assumes the same request, sent to the same model name, reads the same tomorrow. Two preregistered campaigns audited that assumption with every threshold frozen in advance. Neither campaign got past validating its instrument.

Across 52,988 audited request attempts, same-window repeat rankings agreed at Spearman 0.400 against a required 0.90, and byte-identical next-day replays agreed at 0.78 against a required 0.99. Execution records were at ceiling. The analyses rest on 31 valid task groups, 100 replay pairs, ten windows per supplementary arm, and 3,060 constructed-error judgments. Three mechanisms explain the gap: a label-to-meaning mapping that biased readouts as strongly as the signal; candidate gaps seven orders of magnitude below the instrument's own noise floor; and byte-identical inputs returning different rankings. Waiting did not help on the days sampled (0.805 same-day versus 0.800 cross-day). Switching providers did not help: four providers in three jurisdictions share the floor (medians 0.74 to 0.88). Self-hosting on batch-invariant kernels helped only while the server was quiet; concurrent load raised disagreement 8.4-fold, back to shared-endpoint magnitude.

Why it matters: yesterday's dual-oracle work still needs a stable observer. If the judge itself fails a preregistered reliability gate, SWE-Gate, PatchBench, and every LLM-as-judge leaderboard are measuring a moving instrument. A model name on a shared endpoint is not a frozen measurement device.

Fit in the stack: this belongs in trajectory-aware evaluation as an instrument layer above the task oracle. Measure the observer before freezing any gate on it.

Practical tools and methodologies worth exploring now:
- freeze instrument gates before an eval campaign: same-window rank agreement and next-day byte-identical replay;
- log request hashes, schema validity, and execution records separately from scientific verdicts;
- do not treat a shared OpenAI-compatible model ID as a pinned instrument;
- if you must use a hosted judge, report the instrument-gate miss instead of a task score;
- self-hosting is not a free repair under concurrent load.

Artifact status: no public implementation repository resolved from the v1 abstract, HTML, or PDF. The paper ships a public-layer per-window ledger and authorisation ledger as part of the writeup. Treat the method as specified and the code as claimed-only.

Evidence caveat: observer work used temperature 0.0 one-token exact-label readouts on a shared OpenAI-compatible Chat Completions endpoint (DashScope compatible mode). Results are about black-box hosted observers, not about every local deterministic decoder.

Implementability score: 0.58

Core source: [Clean Engineering, Unstable Measurement, arXiv:2609.04198v1](https://arxiv.org/abs/2609.04198v1)

## Graph structure is not a replay contract

A final agent output cannot show which evidence, tool state, rule, authorization, or action path produced it. DNative-Twin records a committed agentic decision as a typed trajectory and re-executes the decision mechanism under declared conditions. The graph links the state the agent observed, the path it followed, and the authority behind the resulting action.

The measured failure is specific. Graph structure localizes represented changes but cannot determine the consequence of an unobserved tool state. In a three-condition controlled experiment with 300 injected instances, unresolved-divergence recall increased from 0 to 0.667 when replay-contract state was added and to 1.0 when verification results were also available. The held-out set contained no critical-class instance. In all 40 unobserved tool-timeout cases, graph-only reconstruction treated the timeout as benign. Replay-contract state recovered 60 of 90 aligned trajectories in the three-condition experiment. Experiments used public process logs plus controlled replay suites.

Why it matters: an event log without a replay contract is a diagram of what was stored, not a test of what would happen if a tool timed out, a budget call failed, or an authorization was missing. Reconstructability is an execution property.

Fit in the stack: this belongs in the event-sourced agent runtime and the evidence-provenance control plane. Typed trajectories are necessary. They are not sufficient until tool state and verification results are in the replay contract.

Practical tools and methodologies worth exploring now:
- store observed state, chosen path, and authority grant as separate typed nodes;
- put tool-call results, timeouts, and verifier verdicts into the replay contract, not only into the graph;
- score unresolved-divergence recall as a first-class metric;
- do not call a decision reconstructable if an unobserved timeout would have been labelled benign;
- keep replay in isolation from the live effect path.

Artifact status: no public GitHub, Hugging Face, or project URL resolved from the v1 abstract, HTML, or PDF. Treat the paper as the verified source and the implementation as claimed-only. Do not add a live markdown link to an unresolved artifact.

Evidence caveat: 300 injected instances plus public process-log probes. The held-out set had no critical-class instance, so the 1.0 recall figure does not cover that class. No independent reproduction.

Implementability score: 0.45

Core source: [DNative-Twin, arXiv:2609.03787v1](https://arxiv.org/abs/2609.03787v1)

## Working conclusion

Sunday did not add a new listing batch. It added unused Friday papers that change the cheap-check thesis. HTTP 200, a shared model name, and a decision graph can all look complete while the tool lied by omission, the judge failed its own gate, or an unobserved timeout was labelled benign. Put vocabularies in schemas. Measure the observer. Put tool state in the replay contract.
