# AgenticAI

This index tracks the most recent structured implementation research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-06

### HTTP 200 is not a tool-result

Summary: SilentProbe finds that 15.2% of 721,320 OpenAPI parameters declare any machine-checkable constraint, while 40.1% of documents put a constraint in prose only. Machine-checkable live perturbations were honest in 111/111 cases; prose-only failed silently in 44/61. Exemplified vocabularies were missed 88/88. Downstream loops repair 0% of those silent failures.

Analysis: [daily analysis](2026-09-06/reasoning.md#http-200-is-not-a-tool-result)
Core sources: [SilentProbe](https://arxiv.org/abs/2609.00035v1), [Jasper0122/silentprobe](https://github.com/Jasper0122/silentprobe)
Tools and methodologies worth exploring now: schema enumerations at tool admission, reject `e.g.`-only vocabs, treat HTTP 200 empty bodies as ambiguous, log silent-failure separately from tool-call success
Implementability score: 0.82

### A shared model name is not a frozen instrument

Summary: Two preregistered observer campaigns failed their instrument gates with execution records at ceiling. Same-window Spearman 0.400 vs required 0.90. Next-day replay 0.78 vs required 0.99. Waiting and switching providers did not restore a frozen instrument.

Analysis: [daily analysis](2026-09-06/reasoning.md#a-shared-model-name-is-not-a-frozen-instrument)
Core source: [Unstable Measurement](https://arxiv.org/abs/2609.04198v1)
Tools and methodologies worth exploring now: freeze instrument gates before task gates, log request hashes separately from verdicts, do not treat a shared model ID as a pinned observer
Implementability score: 0.58

### Graph structure is not a replay contract

Summary: DNative-Twin's typed decision graph cannot determine the consequence of an unobserved tool state. Unresolved-divergence recall rose from 0 to 0.667 with replay-contract state and to 1.0 with verification results on 300 injected instances.

Analysis: [daily analysis](2026-09-06/reasoning.md#graph-structure-is-not-a-replay-contract)
Core source: [DNative-Twin](https://arxiv.org/abs/2609.03787v1)
Tools and methodologies worth exploring now: put timeouts and verifier verdicts in the replay contract, score unresolved divergence, never default missing tool state to benign
Implementability score: 0.45

## Current implication

HTTP 200, a shared model name, and a decision graph are observations. Tool honesty needs a schema. Evaluation needs an instrument gate. Reconstruction needs tool state in the replay contract.
