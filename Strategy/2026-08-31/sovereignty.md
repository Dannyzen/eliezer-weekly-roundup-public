# Strategy Daily Analysis - 2026-08-31

## Scope note

The Monday, August 31 arXiv listing is the first batch after the weekend. Recognition Without Enforcement and EvoUndo were submitted on August 28 and first listed on August 31. They are current listing signals, not strict trailing-48-hour submissions.

Primary pages and full-paper text were inspected. No external code was cloned, installed, built, imported, or executed. Recognition Without Enforcement exposes no public implementation repository. EvoUndo cites the public Cordis calculus paper repository as background, not an EvoUndo implementation artifact. NotebookLM remained disabled.

## Put tool authority behind an external reference monitor

### Finding

[Recognition Without Enforcement](https://arxiv.org/abs/2608.28502v1) distinguishes recognizing forged authority from enforcing a trust boundary. Models can linearly encode source-format features and verbally identify forged authority, yet some prompt-model configurations still emit the conflicting tool call.

The fleet study covers authority spoofing across 46 model endpoints from six vendors and memory conflict across 48 models. The paper reports average execution of 1.21 percent with a model-clustered 0.5 to 2.1 percent interval over 14,294 spoofed trials from 29 models, but failures concentrate in reproducible cells and shift by as much as 47 percentage points across deployment windows.

An external reference monitor combines authenticated source routing with capability-gated tool execution. It rejects all tested forged, tampered, replayed, and unsigned requests while preserving legitimate operations. A separate adaptive red team found one clock-skew admission flaw, which the authors patched, rather than a cryptographic bypass.

### Why it matters

Low average attack success is not a security boundary when one configuration fails deterministically. Model recognition is useful telemetry, but only an external monitor can bind authenticated source, exact capability, arguments, sequence, freshness, and replay state before an effect.

Prompt hardening still matters for usability and defense in depth. It cannot own authorization because its effectiveness shifts across models, prompts, and deployment windows.

### Strategy fit

This belongs in runtime governance and context-to-execution integrity:

1. authenticate the source outside the model;
2. convert approved intent into a capability-bound request;
3. validate tool, arguments, sequence, freshness, and replay state deterministically;
4. execute only the released request;
5. record the model proposal, monitor decision, actual effect, and receipt;
6. red-team the monitor implementation independently from the model.

### Practical path now

- Treat model instruction arbitration as a capability, not an authorization mechanism.
- Put tool execution behind an external reference monitor.
- Sign or otherwise authenticate authority-bearing requests.
- Add forged-source, tamper, replay, unsigned, and clock-skew fixtures.
- Re-run fingerprinted failures after model or prompt changes because vulnerability cells move.

The work is a single-author paper, its benchmark and implementation are paper-authored, and no public implementation artifact was exposed for independent inspection. The external-monitor pattern is implementable, but production cryptography, key lifecycle, freshness windows, and denial handling require real security engineering.

Implementability score: 0.72

Core source: [paper](https://arxiv.org/abs/2608.28502v1)

## Admit self-modification only with a verified recovery witness

### Finding

[EvoUndo](https://arxiv.org/abs/2608.28363v1) evaluates whether capability-improving changes to prompts, tools, middleware, resources, and harnesses can be safely reversed in counterfactual states. Among 600 unseen one-shot self-evolution tasks, 197 improving mutations fail recoverability verification.

Conventional repair strategies recover 0 of those 197 natural failures under the original recovery representation. Deterministic oracle analysis recovers 48 of 197 under the original language and 191 of 197 under an extended recovery calculus. Exact state-address grounding recovers 38 of 48 cases when the original language is sufficient. The richer language recovers 142 of 143 failures in its oracle-defined stratum, while one model-specific diagnostic interaction lowers the primary-backbone result to 133 of 143.

### Why it matters

A successful self-modification is not safe merely because an inverse exists in the state where the change was created. Recovery has to survive later state drift, name ambiguity, dependency changes, and missing recovery primitives.

The admission object should therefore include both the mutation and a verified recovery witness: exact state addresses, preconditions, inverse semantics, and evidence that the inverse works across bounded counterfactual states.

### Strategy fit

This belongs in agent self-improvement governance:

- generate mutation and recovery witness together;
- verify capability gain separately from reversibility;
- test recovery after bounded state drift;
- distinguish grounding failure from insufficient recovery-language expressivity;
- reject mutations whose effects cannot be addressed or inverted exactly;
- preserve recovery evidence beside the admitted change.

### Practical path now

- Require every harness mutation to declare affected state and an inverse.
- Test the inverse against copied counterfactual states before admission.
- Use stable object identities rather than inferred names or paths.
- Expand the recovery language only when the runtime can independently verify each primitive.
- Keep a human or deterministic rollback gate above model-generated repair attempts.

No paper-owned EvoUndo implementation repository was exposed. The PDF cites [Cordis](https://github.com/cordiverse/paper) as the background composability calculus, but that two-file repository is not an EvoUndo package. The study uses bounded one-shot tasks and two model backbones, so production generality is not established.

Implementability score: 0.63

Core source: [paper](https://arxiv.org/abs/2608.28363v1)
