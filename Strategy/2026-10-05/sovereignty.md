# Strategy Daily Analysis: 2026-10-05

Today's control-plane rule is simple: historical constraints and security filters must be evaluated at the action boundary. Context presence and benchmark scores are weak proxies for execution safety.

## Restore historical constraints before every consequential action

GHOST measures benign long-horizon failures where an agent violates a safety constraint stated many turns earlier. The paper reports an 11.5% occurrence rate on GPT-5.5. Its STAR-Guard design restores relevant historical constraints before proposal and then applies a deterministic pre-execution audit. The authors observed no GHOST events under their reported GPT-5.5 setup, which is promising evidence rather than a universal guarantee.

Why it matters: safety rules that live only in conversational context decay as the trajectory grows. Consequential actions need a compact, durable constraint register and a deterministic release check.

Strategy fit: runtime governance, context-to-execution integrity, agent execution control plane.

Tools and methodologies worth exploring now:
- an append-only constraint register with source-turn provenance;
- applicability matching before each consequential action;
- exact-effect manifests checked against restored constraints;
- deterministic vetoes outside the proposing model;
- regression journeys that move a constraint far back in history.

Artifact status: method-first paper; no public implementation repository was exposed on the paper page.

Implementability score: 0.81

Core source: [GHOST paper v1](https://arxiv.org/abs/2610.02664v1)

## Evaluate prompt-injection detectors on deployed tool outputs

The detector study shows poor ranking transfer from public prompt-injection benchmarks to agent workloads. At a 1% false-positive rate, the best detector on BIPIA caught 2% of AgentDojo injections. A detector that caught 72% on AgentDojo caught 15% on tau-bench. False-positive rates on real tool outputs ranged from zero to over 90%. The paper's practical rule is stronger than choosing a benchmark leader: replay the agent's own tool outputs, measure at a low false-positive operating point, and audit training-data shape.

Why it matters: a detector is part of the deployed gateway, so its unit of evidence is the actual tool-output distribution. Generic benchmark accuracy can hide both missed attacks and blocked legitimate work.

Strategy fit: agent gateway governance, untrusted data boundaries, evaluation containment control plane.

Tools and methodologies worth exploring now:
- the [benign-instruction-bench repository](https://github.com/lzwhehe/benign-instruction-bench);
- benign tool-output replay from real agent traces;
- differential replay for injected variants;
- detection curves at fixed low false-positive rates;
- blocked-task accounting and training-data provenance audits.

Artifact status: public paper scripts and scores are available in the repository.

Implementability score: 0.91

Core source: [prompt-injection detector paper v1](https://arxiv.org/abs/2610.03448v1)

## Current strategy call

Move both controls to execution time: restore applicable constraints before effect release, and qualify security detectors on the exact data plane they govern.
