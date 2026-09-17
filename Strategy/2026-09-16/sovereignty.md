# AI Strategy and Sovereignty Analysis: 2026-09-16

## Freshness and evidence boundary

A real Wednesday arXiv batch was first listed September 16. Both selected v1 papers were submitted September 15. Primary HTML papers and linked public repositories were inspected read-only. No external source was cloned or executed.

## Make skill admission evidence-bearing, not popularity-bearing

### Finding

A longitudinal study of the OpenClaw skill ecosystem shows why registry metadata cannot carry safety authority. The observable stock grew from 33,399 to 65,175 listings in 91 days. Among readable skills, 85.06 percent contained privilege evidence, while 77.86 percent had no stars and no comments. Three scanners disagreed on 23,702 of the 61,990 skills they all covered, and human-adjudicated weighted sensitivity ranged from 21.67 to 61.06 percent.

### Why it matters

Downloads, stars, continued listing, and scanner consensus are weak proxies for review or safety. A skill is a policy-bearing artifact that can direct shell, network, credential, file, and process actions even when it contains little executable code. Registry presence should trigger admission work, not satisfy it.

### Fit in the strategy

This belongs in skill-admission control and agent-community governance. Authority must be attached by the host after provenance, privilege, static findings, behavioral probes, and operator policy are evaluated together.

### Practical methods worth exploring

- content-address every skill version and bind it to a declared privilege manifest
- preserve scanner outputs separately, including unknown and disagreement states
- require human review evidence for privileged capabilities rather than inferring review from stars or comments
- run scoped behavioral probes before promotion and after dependency or host-policy changes
- quarantine unmaintained or unresolved artifacts without pretending scanner majority vote is ground truth

### Evidence caveat

The study measures one fast-growing registry during a boom-and-crest period. Privilege evidence is text-derived and does not prove runtime exploitability. The operational lesson is about weak governance signals, not a claim that 85.06 percent of skills are malicious.

Implementability score: 0.84

Core source: https://arxiv.org/abs/2609.17274v1
Registry source: https://github.com/openclaw/clawhub
Specification source: https://github.com/agentskills/agentskills

## Put cross-principal communication behind a social harness

### Finding

Agents acting for different principals need controls above basic messaging. In 600 released meeting-scheduling runs, the study found that honest agents can fail as participants and concurrent tasks increase, while faulty or malicious agents can stall progress or steer outcomes. The authors propose a five-layer social harness spanning identity, reliable ordered communication, action guardrails, task-specific communication norms, and post-hoc accountability.

### Why it matters

A2A-style connectivity does not solve cross-principal authority, protocol validity, conflicts, or accountability. Personal agent harnesses protect one principal. Multi-party work needs a separate shared control plane that can reject invalid messages, detect violations in-band, and retain enough evidence for later investigation.

### Fit in the strategy

This belongs in agent-community governance and execution control. The social harness should own the inter-agent protocol and evidence, while each personal agent retains its principal's private state and approval policy.

### Practical methods worth exploring

- bind every message to sender identity, principal, task, protocol state, and expiry
- use ordered, replayable envelopes with idempotency and duplicate suppression
- compile task-specific communication norms into deterministic transition checks
- keep private calendars and credentials local while exchanging bounded claims or commitments
- record violation evidence and consequence hooks without granting the shared harness unrestricted principal authority

### Artifact status and caveat

The MIT-licensed companion repository contains the 600 experiment traces, result summaries, and a trace viewer. It does not provide a production social-harness implementation. The evidence comes from meeting scheduling and ten-run cells, so the five-layer stack is a strong design reference, not a universal validated architecture.

Implementability score: 0.68

Core source: https://arxiv.org/abs/2609.17527v1
Artifact: https://github.com/social-harness/social-harness-paper

## Deep Dive Wednesday: make the social harness a separate control plane

This is the week's strongest finding because it identifies a missing control plane rather than only improving a model, benchmark, scanner, or protocol. Transport can deliver messages, but it cannot decide whether a cross-principal message is valid in the active workflow, whether the recipient may act on it, or what evidence must survive for later investigation.

The architecture should keep each principal's private memory, credentials, tools, and final effect authority inside a personal harness. A separate social harness should own verified identities, signed ordered envelopes, task-specific state transitions, violation evidence, and replay. The shared layer may validate a message transition, but the receiving principal's execution-control gate must still release the exact local side effect.

A narrow prototype is implementable now: use A2A or another transport, CloudEvents-style message identity, a JSON Schema state machine, OPA-style policy checks, append-only receipts, and the released 600-run trace corpus as adversarial fixtures. The hard parts are task-specific norms, privacy-preserving evidence exchange, and post-hoc institutional ownership.

Durable deep dive: [Agent Community Governance](../agent-community-governance/agent-community-governance.md)

Implementability score: 0.68

## Practical next steps

1. Require a privilege manifest and explicit review evidence before a skill can receive shell, network, credential, file, or process authority.
2. Prototype a signed inter-agent envelope with principal identity, task state, expiry, idempotency key, and allowed next messages.
3. Use the released social-harness traces as read-only fixtures for protocol validation, not as proof that the proposed stack is production-ready.
