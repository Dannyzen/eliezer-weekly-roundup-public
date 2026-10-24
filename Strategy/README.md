# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-24

### Admit effects through explicit consumable state

Summary: A formal execution supervisor can represent approvals, budgets, capabilities, and spent grants outside model reasoning. The design is compelling, but no verified public implementation was identified.

Analysis: [certified execution admission](2026-10-24/sovereignty.md#1-put-a-certified-admission-layer-between-reasoning-and-action)

Core source: [Certified Execution Harness for Agentic AI](https://arxiv.org/abs/2610.31376v1)

Implementable now:
- type every side-effecting transition;
- bind grants to principal, resource, and effect;
- consume one-use approvals;
- retain admitted and refused transition receipts.

Implementability score: 0.56

### Keep an explicit cannot-determine release state

Summary: Matched safe and harmful lifecycles can expose identical offline evidence. Release decisions therefore need fresh deployment outcomes, subgroup denominators, and a valid undecided state.

Analysis: [post-audit identifiability](2026-10-24/sovereignty.md#2-treat-offline-audits-as-incomplete-without-deployment-identifying-evidence)

Core source: [Post-Audit Mirage](https://arxiv.org/abs/2610.31130v1)

Implementable now:
- define the audit observation boundary;
- preserve deploy, hold, cannot determine, and unsupported;
- bind canary rollout to fresh outcome evidence;
- stop when relevant harm is not identifiable.

Implementability score: 0.76

### Govern agent interfaces independently

Summary: AAIF now hosts Agent Skills, Open Responses, OpenEnv, and OpenSandbox. The strategic value is a portable seam across capability packaging, model exchange, evaluation episodes, and execution environments.

Analysis: [neutral governance across four agent interfaces](2026-10-24/sovereignty.md#3-neutral-governance-now-spans-four-adjacent-agent-interfaces)

Core source: [AAIF project announcement](https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects)

Implementable now:
- contract-test each interface independently;
- keep model interoperability separate from tool authorization;
- keep sandbox lifecycle separate from model and skill selection.

Implementability score: 0.82

## Previous Structured Update: Week Ending 2026-10-23

### Reauthorize persistent state when it resurfaces

Summary: Memory and scheduled tasks are delayed execution channels. Stored evidence may persist, while authority must be re-established when it enters planning and again before an effect.

Analysis: [reauthorize persistent state when it resurfaces](2026-10-23/sovereignty.md#1-reauthorize-persistent-state-when-it-resurfaces)

Core sources: [CarryoverBench](https://arxiv.org/abs/2610.28425v1), [public repository](https://github.com/igloomatics/CarryoverBench)

Implementable now:
- attach origin, purpose, expiry, and revocation to writes;
- quarantine instructions from untrusted sources;
- reauthorize scheduled and memory-derived effects;
- test planting and triggering separately.

Implementability score: 0.78

### Enforce capability below declared tool intent

Summary: Tool schemas describe intent. Filesystem, credential, process, and network authority need sandbox and host enforcement below the tool server.

Analysis: [enforce capability below declared tool intent](2026-10-23/sovereignty.md#2-enforce-capability-below-declared-tool-intent)

Core sources: [My Credentials, Please](https://arxiv.org/abs/2610.22301v1), [Arcade dynamic tool discovery](https://arxiv.org/abs/2610.23707v1)

Implementable now:
- run tool servers under exact roots and dedicated identities;
- deny ambient credential access;
- fail startup when containment is unavailable;
- filter eligible tools before ranking.

Implementability score: 0.86

### Make effects and diagnoses replayable

Summary: Normalize tool lifecycles into canonical events, bind claims to recorded evidence, and reuse deterministic world-state checks for audit, evaluation, and release.

Analysis: [make effects and diagnoses replayable](2026-10-23/sovereignty.md#3-make-effects-and-diagnoses-replayable)

Core sources: [AgentTriage](https://arxiv.org/abs/2610.30738v1), [Apache-2.0 repository](https://github.com/AsnGs/agenttriage-open-source), [ThinkingBox Training](https://huggingface.co/blog/microsoft/thinkingbox-training)

Implementable now:
- define canonical ingress, intent, result, and effect events;
- distinguish native from synthesized identity;
- version overlays and policy oracles;
- abstain when mandatory evidence is absent.

Implementability score: 0.84

### Bind approval to the exact effect path

Summary: Keep sandbox lifecycle, egress policy, and recovery outside the guest. Bind high-risk approval to the exact template, destination, socket, expiry, and use.

Analysis: [bind approval to the exact effect path](2026-10-23/sovereignty.md#4-bind-approval-to-the-exact-effect-path)

Core sources: [SPACE](https://www.perplexity.ai/hub/blog/open-sourcing-space), [Connection Escrow](https://arxiv.org/abs/2610.26501v1)

Implementable now:
- bind creates to template digests and egress profiles;
- retain host-side lifecycle receipts;
- use single-use effect grants;
- test fail-closed controller recovery.

Implementability score: 0.58

## Current implication

Evidence can inform authority. It cannot silently become authority through persistence, compaction, retrieval, tool discovery, or guest execution.
