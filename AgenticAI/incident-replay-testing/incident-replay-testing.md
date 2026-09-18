# Incident Replay Testing for Agents

## Thesis

Production agent incidents should become selective replay tests. Re-running the whole agent is nondeterministic and expensive. Stubbing the whole trajectory can hide the failure. The useful primitive is a recorded incident plus an explicit set of boundaries that must execute live against new code.

## Control model

Represent every nondeterministic crossing as an immutable envelope:

- boundary name and occurrence index;
- input and output;
- model, sampling, tool, router, and schema versions;
- source state or external-state identity where available;
- timestamps and trace identifiers;
- redaction and retention policy;
- content digest.

A full replay serves every envelope from the record. A cut-point replay serves unchanged boundaries from the record and executes selected boundaries live. The test must fail when boundary counts drift, required envelopes are missing, or hidden external state prevents faithful replay.

## What to run live

Choose the smallest boundary set that exercises the proposed fix:

- tool authorization and validation gates;
- routers and fallback policy;
- parsers and schema validators;
- state transition logic;
- approval checks;
- idempotency and compensation code;
- memory writeback and skill-mutation gates.

Stub expensive model calls only when the fix does not depend on new model behavior. If a model change is the intervention, run that model crossing live and preserve every other recorded boundary.

## CI contract

A durable incident fixture contains:

1. the immutable record;
2. the selected live boundary set;
3. deterministic structural assertions;
4. semantic assertions only where structural checks are insufficient;
5. expected failure under the old code;
6. expected pass under the fix;
7. benign-change controls;
8. source, policy, model, and fixture identities.

Keep advisory LLM judges separate from hard pass or fail checks. A semantic judge can add evidence, but deterministic safety and effect assertions should own the release gate.

## Privacy and storage

Replay records can contain prompts, tool outputs, customer data, file paths, tokens, and system state. Redact before storage, encrypt sensitive fixtures, bind access to the original authority scope, and store digests so redaction or migration cannot silently change test identity. Do not commit sensitive production envelopes to a public repository.

## Evidence

Chronicle demonstrates the pattern on six recorded failures. Full replay issued no model calls and stayed bit-stable across 20 repetitions. Cut-point tests rejected faulty code and accepted guarded and benign changes for all six incidents. In mutation testing, selective replay caught every unsafe-action mutant while a fully stubbed baseline caught none.

Core source: https://arxiv.org/abs/2609.20625v1
Implementation: https://github.com/theagentplane/chronicle

## Implementability

Implementability score: 0.93

The repository is packaged, tested, documented, licensed MIT, and released. The weakest point is evidence breadth: six incidents do not establish coverage across browser, infrastructure, stateful database, and multi-agent failures. Start with one existing incident and require a redaction review before wider adoption.
