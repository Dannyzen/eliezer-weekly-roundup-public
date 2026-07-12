# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday synthesis, week ending 2026-07-10

### The release gate is the missing layer between evidence and authority

Summary: Context-to-Execution Integrity, deterministic pre-execution gates, and SessionBound converge on one sovereignty primitive: untrusted context may inform reasoning, but protected execution requires typed releases, exact-effect commitments, scoped grants, budgets, and receipts before side effects.

Analysis: [weekly sovereignty analysis](2026-07-10/sovereignty.md#the-release-gate-is-the-missing-layer-between-evidence-and-authority)
Durable topics: [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md), [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md)
Core sources: [Context-to-Execution Integrity](https://arxiv.org/abs/2607.06000v1), [CXI artifact](https://anonymous.4open.science/r/cxi), [Deterministic pre-execution gates](https://arxiv.org/abs/2607.07405v1), [SessionBound](https://arxiv.org/abs/2607.00751v1), [SessionBound repo](https://github.com/SessionBound/sessionbound)
Implementable now:
- mark protected sink fields on privileged tools
- require typed releases from untrusted evidence before protected fields can be populated
- inspect proposed writes before execution and log receipts after effects
Tools, repos, and methodologies worth exploring:
- CXI-style action manifests, `SessionBound/sessionbound`, Cedar or OPA policies, exact-effect manifests, deterministic side-effect oracles
Implementability score: 0.76

### Untrusted data boundaries now cover browser content, tool outputs, metadata, and memory

Summary: Untrusted Content Masking, Agent Data Injection, Unicode TAG-block MCP concealment, HalluSquatting, and Prismata all show the same failure: agents flatten trusted structure, untrusted content, model-visible bytes, identifiers, and capabilities into one prompt surface.

Analysis: [weekly sovereignty analysis](2026-07-10/sovereignty.md#untrusted-data-boundaries-now-cover-browser-content-tool-outputs-metadata-and-memory)
Durable topics: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Untrusted Content Masking](https://arxiv.org/abs/2607.05277v1), [UCM repo](https://github.com/ethz-spylab/untrusted-content-masking), [Agent Data Injection](https://arxiv.org/abs/2607.05120v1), [Unicode TAG-block MCP concealment](https://arxiv.org/abs/2607.05744v1), [HalluSquatting](https://arxiv.org/abs/2607.07433v1), [Prismata](https://arxiv.org/abs/2607.08147v1)
Implementable now:
- classify DOM regions and tool output fields by origin, trust class, and allowed use
- mask untrusted browser content before planner exposure
- canonicalize and hash approval text, MCP metadata, and model-visible bytes before approval
Tools, repos, and methodologies worth exploring:
- `ethz-spylab/untrusted-content-masking`, BrowserGym/WebArena/WASP fixtures, Unicode scanners, registry metadata checks, OpenTelemetry evidence-to-effect spans
Implementability score: 0.70

### Permission is a typed grant, not an approval popup

Summary: Janus makes permission management a testable user-involved design space. SessionBound compiles approved enterprise tasks into budgeted data sessions. SovereignPA-Bench shows why personal-agent consent must include revocation, platform influence, current user interest, evidence quality, and burden.

Analysis: [weekly sovereignty analysis](2026-07-10/sovereignty.md#permission-is-a-typed-grant-not-an-approval-popup)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core sources: [Janus](https://arxiv.org/abs/2607.01510v1), [Janus repo](https://github.com/GraceBrigham/Janus), [SessionBound](https://arxiv.org/abs/2607.00751v1), [SovereignPA-Bench](https://arxiv.org/abs/2607.05363v1)
Implementable now:
- represent approvals as grant objects with principal, target, scope, action class, expiry, budget, revocation, and receipt fields
- deny or downscope when requested effects exceed the grant
- measure user burden and intervention quality, not only attack prevention
Tools, repos, and methodologies worth exploring:
- `GraceBrigham/Janus`, grant-object schemas, signed task tokens, receipt logs, personal-agent consent manifests
Implementability score: 0.66

### Agent supply chain starts before install

Summary: Skill malware, skill composition, approval-metadata concealment, and HalluSquatting all move the supply-chain boundary earlier. The platform must verify the artifact identity, approval bytes, composition behavior, and sandbox behavior before an agent loads a skill, tool server, package, or repository.

Analysis: [weekly sovereignty analysis](2026-07-10/sovereignty.md#agent-supply-chain-starts-before-install)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
Core sources: [Cloak and Detonate](https://arxiv.org/abs/2607.02357v1), [SkillFuzz](https://arxiv.org/abs/2607.02345v1), [Unicode TAG-block MCP concealment](https://arxiv.org/abs/2607.05744v1), [HalluSquatting](https://arxiv.org/abs/2607.07433v1)
Implementable now:
- require exact artifact identity from a trusted source before clone, install, or skill load
- detonate risky skills in a sandbox with fake secrets, marker files, egress traps, and OS-boundary traces
- fuzz approved skills for risky compositions before marketplace admission
Tools, repos, and methodologies worth exploring:
- SkillDetonate-style behavior tracing, SkillFuzz-style composition search, Unicode and control-character scanning, exact-source allowlists, sandbox-native workers
Implementability score: 0.72

### Personal-agent sovereignty is low-readiness but strategically unavoidable

Summary: SovereignPA-Bench is not a ready product pattern, but it is the clearest warning in the week: user-owned personal agents need explicit tests for privacy, consent, revocation, platform mediation, current user interest, evidence quality, and user burden.

Analysis: [weekly sovereignty analysis](2026-07-10/sovereignty.md#personal-agent-sovereignty-remains-strategically-important-but-low-readiness)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Community Governance](agent-community-governance/agent-community-governance.md)
Core source: [SovereignPA-Bench](https://arxiv.org/abs/2607.05363v1)
Implementable now:
- add consent scope, revocation, platform-influence, current-interest, evidence-quality, and user-burden fields to personal-agent task manifests
- keep sensitive actions behind grants with explicit receipts
- treat platform suggestions, ads, rankings, and social pressure as untrusted influence surfaces
Tools, repos, and methodologies worth exploring:
- consent manifests, revocation tests, platform-influence fixtures, user-burden scoring, receipt-backed personal-agent task logs
Implementability score: 0.43

## Supporting recent Strategy context

The week ending 2026-07-10 turned the strategic model into a concrete operating rule: evidence is not authority. Agents can read messy context, but side effects require typed releases, scoped grants, exact identities, deterministic gates, and receipts.
