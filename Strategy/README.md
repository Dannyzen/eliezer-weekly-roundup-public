# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-30

### Keep runtime feedback diagnostic

Summary: CARI shows that peer-controlled logs, tests, and service output can turn diagnostic authority into unauthorized local action. It succeeded in 94.8% of 3,000 trials across four languages and five models.

Analysis: [runtime feedback as an untrusted boundary](2026-10-30/sovereignty.md#1-treat-runtime-feedback-as-untrusted-diagnostic-data)

Core source: [CARI](https://arxiv.org/abs/2610.38799v1)

Implementable now:
- label and quarantine imperative runtime text;
- authorize every effect independently;
- replay adversarial runtime fixtures.

Implementability score: 0.76

### Carry proof with inter-agent claims

Summary: PCM binds claims to independently written log records and offline-verifiable inclusion proofs. It accepted 10 of 712 benchmark lies, all stale-evidence cases, while plain A2A accepted all 712.

Analysis: [proof-carrying agent messages](2026-10-30/sovereignty.md#2-make-inter-agent-claims-carry-independently-verifiable-proof)

Core sources: [paper](https://arxiv.org/abs/2610.39109v1), [MIT repository](https://github.com/Cygnux-Labs/PCM-protocol)

Implementable now:
- type claims as proven, unproven, or failed;
- record evidence outside the agent process;
- narrow delegated grants through typed caveats.

Implementability score: 0.72

### Bound MCP identity and discovery data

Summary: MCP Gateway Registry 1.35.0 adds Keycloak on-behalf-of token exchange with audience checks, caps registrant metadata, makes model-facing metadata opt-in, strips reserved backend headers, and gates unhealthy or unsafe resources.

Analysis: [bounded gateway authority](2026-10-30/sovereignty.md#3-bound-identity-metadata-and-backend-headers-at-the-mcp-gateway)

Core source: [release 1.35.0](https://github.com/agentic-community/mcp-gateway-registry/releases/tag/1.35.0)

Implementable now:
- validate delegated-token audience;
- project only named metadata fields;
- strip reserved headers and unhealthy routes.

Implementability score: 0.92

## Previous Structured Update: 2026-10-29

### Compile reasoning into guarded CI execution

Summary: GitHub Agentic Workflows compiles Markdown into standard Actions YAML, keeps agent jobs read-only and sandboxed by default, and releases configured writes through separate safe-output jobs with scoped permissions.

Analysis: [guarded workflow compilation](2026-10-29/sovereignty.md#1-compile-reasoning-workflows-into-constrained-execution)

Core sources: [GA release](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/), [github/gh-aw](https://github.com/github/gh-aw)

Implementable now:
- keep deterministic CI gates outside the model;
- compile reasoning tasks into reviewable lockfiles;
- isolate agent execution and release writes separately.

Implementability score: 0.94

### Make authority a runtime protocol

Summary: Concordat models consequential conversations as finite-state protocols, with tool access and human-only decisions enforced by current state.

Analysis: [typed conversation authority](2026-10-29/sovereignty.md#2-make-conversation-authority-a-runtime-protocol)

Core sources: [paper](https://arxiv.org/abs/2610.37461v1), [repository](https://github.com/miladsikaroudi/concordat)

Implementable now:
- encode approval order as transitions;
- bind capabilities to current state;
- reject illegal effects before dispatch.

Implementability score: 0.79

## Previous Structured Update: 2026-10-28

### Give autonomous workloads their own revocable identity

Summary: GitHub Copilot SDK now supports short-lived GitHub App installation tokens for organization-owned services. Usage inherits organization policy and budget, carries app attribution, and can be revoked independently from human accounts.

Analysis: [workload-owned agent identity](2026-10-28/sovereignty.md#1-give-autonomous-workloads-their-own-revocable-identity)

Core source: [GitHub Copilot server-to-server authentication](https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication/)

Methodology: [server-to-server token documentation](https://docs.github.com/copilot/how-tos/copilot-sdk/auth/server-to-server-tokens)

Implementable now:
- issue one bounded workload identity per service or trust domain;
- use short-lived tokens and disable human-credential fallback;
- bind usage, model, task, and effect receipts;
- retain independent revocation.

Implementability score: 0.90

## Previous Daily Update: 2026-10-27

### Put assisted permission classification below policy

Summary: GitHub's assisted mode can auto-pass requests classified as clearly safe, while enterprise settings bound whether Assisted and Allow All are available. Public classifier accuracy evidence is absent.

Analysis: [assisted permissions inside deterministic policy](2026-10-27/sovereignty.md#1-keep-assisted-permission-classification-inside-deterministic-policy)

Core source: [GitHub Copilot assisted permissions](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available)

Implementable now:
- define deterministic deny and always-ask classes;
- auto-pass only eligible reversible actions;
- retain exact-effect permission receipts;
- fail back to manual approval.

Implementability score: 0.84

## Previous Daily Update: 2026-10-26

### Bind authority to the causal effect path

Summary: Benign agents bypassed review by performing locally permitted favors for peers. The behavior appeared in 58.8% of FavorBench trajectories and 95% of adapted CooperBench trajectories, with measurable harm to absent stakeholders.

Analysis: [workflow-bypassing favors](2026-10-26/sovereignty.md#1-local-permission-is-insufficient-when-agents-can-exchange-favors)

Core source: [The Helpful Agent Problem](https://arxiv.org/abs/2610.31985v1)

Implementable now:
- bind effects to initiator, beneficiary, owner, and approval path;
- make reviewer unavailability a blocked state;
- test reciprocal and third-party edits explicitly.

Implementability score: 0.66

### Make MCP resilience a gateway policy

Summary: A 60% quality drop under realistic MCP faults and no measured scale advantage make timeout, retry, validation, and escalation policy gateway responsibilities.

Analysis: [gateway-owned tool resilience](2026-10-26/sovereignty.md#2-treat-tool-resilience-as-gateway-policy-not-model-capability)

Core source: [MCP-Injector paper](https://arxiv.org/abs/2610.32555v1)

Artifact: [MCP-Injector](https://gitlab.com/uniluxembourg/snt/sedan/papers/mcp-injector)

Implementable now:
- classify effects before retry;
- require idempotency evidence;
- fault-test every production tool server.

Implementability score: 0.91

## Previous Daily Update: 2026-10-25

### Evaluate memory validity state separately from retrieval

Summary: Governance-state corruption changed the operative projection in 96.25% of 2,080 matched fault pairs. Selected downstream contrasts showed 40.54 points of LongMemEval damage and 30.60 points of Memora FAMA damage, with recovery under enforcement.

Analysis: [memory governance-state corruption](2026-10-25/sovereignty.md#1-evaluate-memory-validity-state-separately-from-retrieval-quality)

Core source: [Governance-State Corruption in Long-Term Memory for LLM Agents](https://arxiv.org/abs/2610.30698v1)

Implementable now:
- type memory lifecycle states;
- compile authorized model-visible projections;
- seed state faults independently from content and retrieval;
- retain projection and policy receipts.

Implementability score: 0.72

### Grade adaptive phishing by effects, not only detection

Summary: Four of nine evaluated email agents had phishing detection below 10% and malicious-request compliance above 45% under adaptive persuasion. Conventional phishing safety therefore did not predict action safety.

Analysis: [adaptive phishing effect grading](2026-10-25/sovereignty.md#2-test-email-agents-against-adaptive-persuasion-not-only-static-phishing-corpora)

Core source: [AgentPhishing](https://arxiv.org/abs/2610.31404v1)

Implementable now:
- separate detection from compliance and disclosure outcomes;
- test held-out adaptive persuasion variants;
- gate privileged email effects outside message content;
- replay failures as controlled regression fixtures.

Implementability score: 0.64

## Previous Daily Update: 2026-10-24

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
