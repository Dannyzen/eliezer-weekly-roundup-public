# Coding Agent Control Plane

Last updated: 2026-07-06

Coding-agent control planes are the missing governance layer between repo-local agent instructions and real file or shell authority.

## Core thesis

Agent rules files are not comments. They are executable-adjacent configuration that changes how an autonomous system reads, writes, tests, and invokes tools inside a repository. Treating those files as informal Markdown is now unsafe.

A serious coding-agent stack should manage agent configuration like a supply-chain object:
- canonical source definition
- content hash
- lockfile
- target-client compilation
- explicit permission profile
- policy checks before action
- drift detection
- trace evidence
- replayable conformance tests

## Why this topic now

The 2026-06-26 scan surfaced [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1), which studied 10,008 public GitHub repositories and 6,145 agent configuration files. Its key empirical finding is that agent configs propagate as undeclared shared components: 10.1% exact SHA-256 duplicates across independent repositories, 75.5% of clone pairs crossing organizational boundaries, rare revision, and almost no explicit permission boundaries.

That makes agent configuration a supply-chain surface. If a repo imports a GitHub Action, a package, or a Terraform module, teams know to check provenance and permissions. If a repo imports a copied agent rules file, most teams treat it as prose. That gap is now too large.

## Control-plane primitives

### 1. Canonical definition

Keep one canonical agent definition for a repo or product surface. Compile it into client-specific forms for Cursor, Claude Code, Copilot, OpenHands, Codex, IDE files, or custom harnesses.

### 2. Content addressing

Hash the canonical definition and compiled target files. Store the active hash in a lockfile. Log the hash with every agent run.

### 3. Permission profile

Declare allowed file scopes, shell commands, network access, memory writes, external sends, and approval requirements. Do not rely on instruction prose to imply permissions.

### 4. Policy gate

Route side-effecting actions through a deterministic policy layer such as Cedar, OPA, or a custom broker. The model can propose. The control plane decides.

### 5. Drift detection

Fail CI or require review when compiled target files drift from the canonical definition, when copied configs lack provenance, or when permissions change without review.

### 6. Trace binding

Record agent config hash, target client, permission profile, policy version, allowed tools, denied tools, touched files, and test evidence in the trajectory.

## Practical implementation path

1. Inventory all repo-local agent instruction files: `AGENTS.md`, `.cursor/rules`, Claude Code instructions, Copilot instructions, OpenHands config, and custom skill files.
2. Add a canonical `agent-control-plane.yaml` or equivalent typed source.
3. Generate client-specific files from that canonical source.
4. Hash generated outputs and store a lockfile.
5. Add CI that fails on ungenerated drift or missing permission declarations.
6. Add trace fields for config hash, permission profile, policy version, and target client.
7. Put one privileged action path behind a deterministic policy gate.
8. Add conformance tests for blocked commands, write-scope violations, missing tests, and stale config hashes.

## Tools, repos, and methodologies worth exploring

- Cedar or OPA for deterministic action policy
- OpenTelemetry for config-hash and policy-verdict spans
- SLSA-style provenance ideas for agent config packages
- git hooks or CI workflows for drift detection
- config compilers that generate client-specific instruction files
- replay packs tying requirement, file, test, and policy verdict
- static scanners for copied agent config and embedded prompt-injection patterns

## Implementability score

0.64

A useful first version is straightforward: inventory, hash, generate, lint, trace, and gate one high-risk action. A mature version is harder because agent clients have inconsistent instruction formats and inconsistent runtime permission controls.

## Core source links

- A Deterministic Control Plane for LLM Coding Agents: https://arxiv.org/abs/2606.26924v1
- Autoformalization of Agent Instructions into Policy-as-Code: https://arxiv.org/abs/2606.26649v1
- Sondera Harness Python: https://github.com/sondera-ai/sondera-harness-python

## June 29 update: repository outcomes are part of the coding-agent control plane

Govern the Repository, Not the Agent and NOVA extend this topic from configuration governance into outcome governance. The control plane should not only know which rules file guided the agent. It should know whether agent work increased repository friction, whether architecture mutations passed verifier cascades, and whether failed attempts became reusable diagnostics.

Practical lesson:
- attach agent run ID, config hash, policy profile, and verifier version to pull requests;
- track merge delay, review churn, CI retries, conflicts, rollbacks, and post-merge defects by repository and component;
- require verifier cascades for architecture-changing patches;
- store proposal, diagnostics, metric delta, promotion decision, and human override in the trajectory;
- expand autonomy only where repository-level outcomes justify it.

Sources:
- [Govern the Repository, Not the Agent](https://arxiv.org/abs/2606.28235v1)
- [NOVA](https://arxiv.org/abs/2606.27243v2)

## July 6 update: coding chats need regression gates and constrained substrates

Regression Accumulation and Steerability via constraints extend this topic from repo-config governance into turn-by-turn coding authority. A coding-agent session creates commitments. Later turns should not be accepted unless they preserve earlier behavior. A coding-agent workspace also needs substrate constraints so the agent has fewer unsafe paths and reviewers have better evidence.

Practical lesson:
- store accepted requirements as session contracts;
- convert prior requirements into replayable tests, assertions, or invariants;
- run old and new checks on every later turn, then rollback and retry on regression;
- treat cross-turn conflict as a first-class failure label;
- default coding agents into constrained file, network, dependency, and command surfaces;
- expose local docs, architecture rules, and code maps to reviewer agents.

Sources:
- [Regression Accumulation in Multi-Turn LLM Programming Conversations](https://arxiv.org/abs/2607.01855v1)
- [Steerability via constraints](https://arxiv.org/abs/2607.02389v1)

## July 17 update: package installation needs exact artifact admission

Setup Complete, Now You Are Compromised extends the coding-agent control plane below rules files and commands. Documentation can propose dependencies, but the runtime should resolve exact package identity, registry origin, version policy, lockfile state, and known risk before any installer runs.

Practical lesson:
- intercept `pip`, `uv`, `npm`, `cargo`, and system-package commands before execution;
- resolve namespace, publisher, registry, version, lockfile, and vulnerability policy;
- reject alternate sources unless a reviewed policy allows them;
- treat install-then-flag as a compromise, not a detection;
- store instruction source, resolved artifact, policy verdict, command, and effect evidence under one install ID.

Artifact caveat: the repository URL printed in the paper did not resolve during the scan, so the deterministic gate is an implementation pattern rather than a reproduced package.

Source:
- [Setup Complete, Now You Are Compromised](https://arxiv.org/abs/2607.15143v1)

## July 21 update: passing tests do not prove an agent tested its diff

Test Coverage Analysis of Agentic Pull Requests adds a release gate below test success. The control plane should prove that the agent's changed executable lines were exercised and identify whether that evidence came from existing tests or tests the agent added.

Practical lesson:
- compute base-to-head executable-line changes;
- map normal coverage output back to the diff;
- require stronger review for uncovered error handling, auth, persistence, and side-effect paths;
- record coverage provenance and uncovered syntax classes under the agent run and pull request;
- follow line coverage with branch, assertion-quality, or mutation evidence where risk justifies it.

Evidence caveat: the coverage subset is limited to merged repositories that built and instrumented successfully, the Java subset skews smaller than the source population, and line coverage is not behavioral correctness. The replication repository is populated and tagged, but GitHub exposes no license metadata.

Sources:
- [Test Coverage Analysis of Agentic Pull Requests](https://arxiv.org/abs/2607.18057v1)
- [SageSELab replication repository](https://github.com/SageSELab/Agentic-Pull-Request-Test-Coverage)
- [Zenodo 1.0.0](https://doi.org/10.5281/zenodo.21419686)
