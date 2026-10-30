# Strategy Daily Sovereignty Note, 2026-10-30

The strongest strategy signal is that runtime data, inter-agent claims, and gateway metadata are authority surfaces. Diagnostic text may inform reasoning, but it must not silently grant action authority. Claims and delegated identity need independent proof, bounded transport, and deterministic admission checks.

## 1. Treat runtime feedback as untrusted diagnostic data

CARI defines cross-boundary adversarial runtime injection in coding-agent workflows. A peer-controlled backend, test harness, CI job, or deployment service embeds instructions in legitimate runtime feedback. The receiving coding agent then converts diagnostic authority into unauthorized local actions.

The paper evaluates ten attacks across four programming languages and five code-capable models. CARI succeeded in 2,845 of 3,000 trials, or 94.8%. It also transferred to product coding agents, with 61.3% attack success on Codex and 58.7% on Claude Code. Generic warnings were ineffective, while explicit policies reduced attacks at the cost of substantial over-refusal.

Why it matters: provenance alone does not confer authority. A real service may truthfully own the log message while having no right to direct local files, credentials, shell commands, or deployments.

Fit in the strategy: untrusted data boundaries, context-to-execution integrity, and coding-agent sandbox policy.

Implementable now:
- label tool and runtime output by source and evidence class;
- strip or quarantine imperative text from diagnostic channels;
- require local policy to authorize every proposed effect independently;
- seed adversarial logs, test output, API errors, and CI messages in regression suites;
- measure attack suppression and legitimate recovery together.

Weakest point: no public implementation artifact was verified. The attack suite is compelling, but production defenses need domain-specific allowlists and effect policies to avoid blunt over-refusal.

Artifact status: paper methodology and PDF were inspected. No external source was cloned, installed, imported, or executed.

Implementability score: 0.76

Core source: [CARI v1](https://arxiv.org/abs/2610.38799v1)

## 2. Make inter-agent claims carry independently verifiable proof

Proof-Carrying Messages, or PCM, attaches each claim to records from an append-only Merkle log that the sending agent cannot write. An independent signer records events, signs the message, and provides inclusion proofs. Receivers verify claims offline as proven, unproven, or failed. Grant chains must originate in recorded human approval and may only narrow.

On a pre-specified benchmark of 926 messages containing 712 lies across 16 classes, PCM accepted 10 lies, all stale-evidence cases. That is 1.4% with a reported 95% confidence interval of 0.8% to 2.6%. Plain A2A accepted all 712 lies. Two independent verifiers agreed on all 926 verdicts, and verification took about 1 ms.

Why it matters: authenticated transport proves who sent a message. It does not prove that tests passed, a person approved an effect, or a tool result came from an independent executor.

Fit in the strategy: evidence provenance, multi-agent authority, and replay-safe delegation.

Implementable now:
- define typed claim schemas with proven, unproven, and failed states;
- record tool and approval events outside the agent process;
- bind claims to inclusion proofs and pinned signer keys;
- narrow delegated grants through typed caveats;
- refuse side effects when mandatory claims remain unproven.

Weakest point: PCM is a single-author v1 protocol. Stale evidence remains its documented failure class, and production use requires a trusted signer, append-only log, key distribution, replay state, and receiver policy.

Artifact status: the MIT repository, specification, vectors, and README were inspected read-only. The reference implementation was not installed or executed.

Implementability score: 0.72

Core sources: [PCM paper v1](https://arxiv.org/abs/2610.39109v1), [PCM protocol repository](https://github.com/Cygnux-Labs/PCM-protocol)

## 3. Bound identity, metadata, and backend headers at the MCP gateway

MCP Gateway Registry 1.35.0 turns several abstract governance rules into concrete gateway controls. It adds RFC 8693 Keycloak on-behalf-of token exchange, verifies exchanged token signature, issuer, expiry, audience, and subject, and refuses tokens whose audience would let an upstream replay them against the gateway.

The release also caps registrant metadata at 10 KB and eight nesting levels, omits metadata from model-facing discovery tools unless callers request named fields, strips reserved caller and forwarding headers from virtual-server backends, removes unhealthy backends from routing, and blocks unsafe A2A agents based on scanner findings rather than misclassifying the scan as a crash.

Why it matters: agent discovery data and delegated identity are control-plane inputs. Unbounded metadata expands prompt-injection and context-cost surfaces, while confused audiences and forwarded headers can turn gateway trust into upstream authority.

Fit in the strategy: agent gateway governance, identity propagation, and bounded discovery.

Implementable now:
- use on-behalf-of exchange with exact audience validation;
- project only explicitly requested metadata fields into model context;
- cap metadata size and depth before storage;
- strip reserved identity headers before backend dispatch;
- remove unhealthy or unsafe resources from discovery and routing.

Weakest point: this is an operational release, not an independent benchmark. The upgrade has breaking secret-ownership and metadata-limit changes that require deliberate migration.

Artifact status: Apache-2.0 repository metadata and the 1.35.0 release notes were inspected read-only. No external source was cloned, installed, built, or executed.

Implementability score: 0.92

Core source: [MCP Gateway Registry 1.35.0](https://github.com/agentic-community/mcp-gateway-registry/releases/tag/1.35.0)

## Working conclusion

Separate evidence from authority at every boundary. Runtime feedback stays diagnostic, inter-agent claims need source-owned proof, and gateway identity plus metadata must be bounded before they enter model context or backend routing.
