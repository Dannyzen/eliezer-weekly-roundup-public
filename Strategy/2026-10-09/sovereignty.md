# Daily Strategy Analysis: 2026-10-09

## Thesis

Agent governance needs control over four moments: the live trajectory, terminal obligations, capability selection, and state-changing tool calls. Evidence that arrives after execution is useful for learning and insufficient for authority.

All four papers were submitted on 2026-10-08 and first listed on 2026-10-09.

## Make intervention a runtime-owned capability

OnTrack shows that trajectory structure can support warnings or aborts before a run completes. The strategic pattern is a monitor outside the model loop that consumes normalized events, compares partial execution with known trajectories, and applies a separately governed intervention policy.

The strongest objection is the small abort sample: only six runs were interrupted. That makes the 83% precision estimate fragile. The survivable path is shadow monitoring first, then warnings, then human-approved pause, with automatic abort reserved for high-confidence and reversible conditions.

Implementable now: streaming event schemas, reference-trajectory stores, warn and pause thresholds, intervention receipts, and false-positive review.

Implementability score: 0.62

Core source: [OnTrack paper v1](https://arxiv.org/abs/2610.12375v1)

## Treat missing obligations as safety failures

ObligationGuard identifies required safety actions that never occurred. Its benchmark shows that omission risk can exceed explicit forbidden-action risk. A task can be operationally unsafe even when every individual action was permitted.

The strategic consequence is direct: completion authority should require proof of required cleanup, verification, rollback, disclosure, and handoff. These obligations belong in the task contract and final gate, not in a model's implicit memory.

The public benchmark is useful but narrow, with 240 trajectories in three domains. Use its schema as a starting method, then build domain-specific obligation sets from incidents and operating procedures.

Implementable now: positive obligations in action manifests, terminal-state checks, unresolved-obligation reports, and approval gates for incomplete cleanup.

Implementability score: 0.78

Core sources: [ObligationGuard paper v1](https://arxiv.org/abs/2610.11773v1), [public repository](https://github.com/THU-Agent/ObligationGuard)

## Treat skill selection as authority routing

The skill-conflict study shows that one overlapping skill can silently displace another while the task still passes. Installation location influences selection, first-read order locks in behavior, and final responses rarely disclose the substitution.

This makes skill loading an authority event. A runtime should identify overlap, bind normative requirements to the intended skill, intercept the first read, and issue a selection receipt. Catalog size without conflict control expands ambiguity and weakens policy fidelity.

The replication package is inspectable and the mitigation is small. The main deployment constraint is governance: teams need ownership for skill identity, precedence, and conflict adjudication.

Implementable now: similarity scans, namespace and precedence rules, first-read hooks, selected-skill receipts, and exclusive-function regression tests.

Implementability score: 0.90

Core sources: [One Skill Too Many paper v1](https://arxiv.org/abs/2610.11647v1), [replication package](https://github.com/ltroin/conflict)

## Compile policy before granting tool authority

NOMOS turns written policy into deterministic tool-call gates and rejects rules that do not fit the tool schema. The combination of compilation, static checks, replay preflight, and microsecond runtime decisions is a credible control-plane shape.

The unflattering fact is that the public package excludes the compiler and runtime gate. It supports audit of rule artifacts and reported numbers, not reproduction of the system. The method remains implementable as a clean-room pattern, with a meaningful engineering and validation burden.

A production design should keep authored policy, compiled rules, static-check reports, preflight results, active rule version, block receipts, and benign-utility measurements as one release object.

Implementable now: typed rule IR, schema validation, good-transcript replay, deterministic state-change gates, versioned policy bundles, and dual safety plus utility metrics.

Implementability score: 0.58

Core sources: [NOMOS paper v1](https://arxiv.org/abs/2610.11030v1), [public artifact repository](https://github.com/iamupd/NOMOS), [Zenodo v1.0 record](https://zenodo.org/records/22123420)

## Strategic conclusion

The shared control-plane pattern is early and explicit authority. Monitor before failure completes, require obligations before completion, resolve skill conflicts before capability use, and compile policy before state-changing calls.
