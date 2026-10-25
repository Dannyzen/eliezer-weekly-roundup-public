# Strategy Daily Analysis: 2026-10-25

## Freshness note

arXiv's newest agent-relevant listing is Friday, October 23. These Sunday carry-forward findings were submitted October 22 and were not used in the October 24 daily update.

## 1. Evaluate memory validity state separately from retrieval quality

A memory system can retrieve the correct record and still expose the wrong operative version after deletion, supersession, or temporal change. The paper names this governance-state corruption: retained content and task stay fixed while the control state deciding what enters model-visible context is altered.

Across six providers, 731 benchmark-grounded bases produced 2,080 matched fault pairs. Corruption changed the operative projection in 96.25% of offline pairs, while oracle-backed enforcement restored it in 100%. In the selected downstream panel, 298 of 300 matched triplets resolved. The clean-minus-corrupted contrast was 40.54 percentage points for LongMemEval binary correctness and 30.60 points for Memora FAMA, with recovery under enforcement.

### Why it matters

Retrieval benchmarks miss whether a record remains authorized, current, and visible for the present action. Memory governance needs its own test plane covering lifecycle state, projection construction, and model-visible context.

### Fit in the stack

This is a memory authority control-plane finding. The write path stores content and lifecycle metadata; the read path must compile an authorized projection; the evaluation path must fault the governance state independently from content and retrieval.

### Implementable now

- represent current, superseded, deleted, expired, and quarantined states explicitly;
- compute model-visible context from those states rather than retrieving raw retained records;
- seed lifecycle-state faults while holding task, content, and retrieval fixed;
- retain the compiled projection and policy decision as audit evidence;
- report recovery and abstention separately from answer accuracy.

Implementability score: 0.72

Core source: [Governance-State Corruption in Long-Term Memory for LLM Agents v1](https://arxiv.org/abs/2610.30698v1)

Artifact status: the paper advertises `chris3494285/govmem-paper-reproducibility`, but the repository did not resolve during this scan. The selected downstream panel is non-probability sampled, and the paper labels full-cohort frozen-scorer effects as descriptive rather than validated population effects.

## 2. Test email agents against adaptive persuasion, not only static phishing corpora

AgentPhishing evaluates both phishing detection and compliance with malicious requests. Its PhishOpt method adapts reusable email-generation skills against individual target agents under benchmark and realism constraints. In the reported evaluation of nine additional agents, four had detection rates below 10% and malicious-request compliance above 45%, despite agents handling conventional phishing examples safely.

### Why it matters

Static detection scores can certify the wrong property. An email agent may label known phishing patterns correctly while complying with a novel persuasive request. Safety evaluation must grade the resulting action, disclosure, or refusal.

### Fit in the stack

This belongs at the untrusted-data boundary between message ingestion and privileged email actions. Detection is one signal. Authorization and effect admission remain separate controls.

### Implementable now

- grade detection and malicious-request compliance as separate outcomes;
- generate adaptive, held-out persuasion variants under a fixed task contract;
- require independent approval for credential disclosure, payment, external sharing, and account changes;
- keep message text outside the authority channel used to admit effects;
- replay failures as regression fixtures without publishing ready-to-use attack corpora.

Implementability score: 0.64

Core source: [AgentPhishing v1](https://arxiv.org/abs/2610.31404v1)

Artifact status: no primary public implementation repository was identified in the paper page. The study covers synthetic, single-message social-engineering attacks under fixed task setups, so it does not establish real-world attack prevalence.
