# Strategy

This index tracks the most recent structured research. Each finding includes a summary, a link into the detailed analysis, primary sources, practical implementation paths, and an implementability score from 0 to 1.

## Latest Structured Update: Saturday, 2026-07-25

### Gateways need independent model-identity audits

Summary: IRIS uses text-only random-generation probes to audit whole-stream substitution, backend attribution, routing dilution, and routing fraction. It reports 0.99 AUROC on a Qwen3 ladder and 0.85 mean power for 30 percent dilution on qualified OpenRouter pairs.

Analysis: [daily sovereignty analysis](2026-07-25/sovereignty.md#gateways-need-independent-model-identity-audits)
Core sources: [IRIS paper](https://arxiv.org/abs/2607.20860v1), [Photen/IRIS-audit](https://github.com/Photen/IRIS-audit)
Implementable now:
- enroll approved endpoints and freeze the audit budget before suspect queries;
- bind model, provider, quantization, probe set, and response digests;
- treat flags as private investigation triggers, not public proof.
Tools, repositories, and methodologies:
- IRIS-audit, gateway shadow traffic, model catalogs, provider attestations, calibrated sequential testing
Implementability score: 0.78

### Runtime lifecycle ownership must be explicit

Summary: NemoClaw v0.0.95 declares whether NemoClaw or an external systemd service owns the OpenShell gateway. Recovery and uninstall respect that owner. The same release adds atomic SQLite restore, immutable image checks, exact download verification, and executed-run E2E evidence.

Analysis: [daily sovereignty analysis](2026-07-25/sovereignty.md#runtime-lifecycle-ownership-must-be-explicit)
Core sources: [release notes](https://docs.nvidia.com/nemoclaw/user-guide/openclaw/release-notes/2026/7/24), [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)
Implementable now:
- declare one lifecycle owner per gateway;
- validate ownership and listeners before restart, recovery, or uninstall;
- stage and verify state restore before atomic replacement;
- reject skipped release gates as passing evidence.
Tools, repositories, and methodologies:
- NemoClaw, OpenShell, systemd, immutable digests, SQLite atomic replacement, E2E evidence ledgers
Implementability score: 0.90

## Current implication

Sovereignty requires independent identity and singular ownership. Verify what served the request, and let only the declared supervisor mutate the runtime.
