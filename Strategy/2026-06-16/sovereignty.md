# Strategy Daily Analysis: 2026-06-16

Today's strategy signal is that agent trust boundaries are moving below the prompt. Two high-risk surfaces stood out: API routers that see plaintext interactions, and skills that can be rewritten while an agent is running. Both need hard data-path controls, not only policy text.

## Skills and API routers now need tamper-resistant data paths

Core sources:
- The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs: https://arxiv.org/abs/2606.16358v1
- Dynamic Malicious Skills in Agentic AI: https://arxiv.org/abs/2606.16287v1
- Agent trajectories as programs: https://arxiv.org/abs/2606.16988v1

The Proxy Knows Too Much frames an LLM API router as an application-layer man-in-the-middle. The router terminates the client TLS session, opens a separate upstream session, and can therefore read or alter the full interaction. The paper's AEGIS design confines plaintext handling to a small attested enclave, keeps management and accounting on the untrusted host, and reports about six milliseconds of local relay overhead. Dynamic Malicious Skills identifies a different but adjacent integrity failure: agents can be induced by natural-language documentation to dynamically inject malicious logic into otherwise benign skills during execution. Its mitigation is blunt and useful: kernel-enforced read-only mounts for skill files.

Why it matters: agent governance cannot stop at "the policy said no." A malicious router can rewrite tool calls or exfiltrate secrets before policy evidence ever reaches the operator. A mutable skill can change the instruction surface after review. Serious deployments need tamper-resistant paths for both interactions and procedural artifacts.

How it fits into the stack:
- Router layer: compatibility proxies and model routers become privileged security infrastructure.
- Skill layer: skill files are runtime dependencies and should be immutable while active.
- Gateway layer: policy should bind source, hash, mount mode, route, provider destination, and trace evidence.
- Evaluation layer: trajectory fingerprints and trace audits can detect unexpected router or skill behavior drift.

Implementable now:
- treat any LLM API router or OpenAI/Anthropic-compatible proxy as privileged infrastructure;
- pin router images, restrict upstream host destinations, and log requested model, effective model, route, and policy verdict;
- mount admitted skill directories read-only during agent execution;
- include skill body hash, script hash, mount mode, and loaded-skill ID in every run trace;
- add canary tests that try to mutate a skill at runtime and expect a hard failure;
- treat TEEs and remote attestation as a design reference for high-sensitivity router paths, even if the first production step is simpler host hardening.

Tools, repos, and methodologies worth exploring:
- read-only bind mounts, OverlayFS, container read-only filesystems, seccomp/AppArmor, signed router images, mTLS, provider host allowlists, LiteLLM or Portkey policy logs, remote attestation patterns, ProcGrep-style trace drift checks.

Implementability score: 0.69

## Strategic implication

The durable strategy is not "trust the agent less." It is "make the authority path inspectable and tamper-resistant." Skills, routers, gateways, and traces are all part of the same operating surface. If any one can silently rewrite the run, the audit trail is decorative.

## Watchlist

- The Proxy Knows Too Much has no public implementation repo verified in this scan; treat AEGIS as a design reference, not a drop-in router.
- Dynamic Malicious Skills targets OpenHands and Claude Code style skill systems; the mitigation generalizes to any agent runtime that loads writable procedural files.
- Transferable Self-Evolving Playbooks for Agentic Security Auditing shows that generated playbooks can materially lift security-agent performance, but this also increases the need for playbook provenance and review: https://arxiv.org/abs/2606.16420v1

## Scan quality note

This scan used primary arXiv links, managed extraction for selected papers, read-only GitHub metadata searches for implementation artifacts, and direct raw README reads where a practical repo was cited. External source code was not cloned, installed, built, imported, or executed.
