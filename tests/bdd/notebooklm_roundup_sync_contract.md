# NotebookLM curated roundup sync BDD contract

This document captures the resilient contract that the new BDD suite is trying to protect.

## Scope

The system under test takes curated weekly roundup artifacts from this repo and synchronizes them into NotebookLM.

Planned responsibilities:
- find the current or requested week key
- locate curated markdown artifacts in this repo
- extract and dedupe external cited URLs
- get or create one canonical NotebookLM notebook for the target week
- attach markdown and URL sources
- wait for source readiness
- generate a Friday audio overview
- publish a single canonical share target when all gates pass
- persist durable local state for idempotency and recovery

## Primary actors

### Operator
The human who runs daily syncs, Friday publication, backfills, and corrections.

### Infrastructure
The sync runtime, its local manifest and locking layer, and the NotebookLM SDK integration.

### Reader
The external consumer who opens the shared weekly notebook and expects one current public entry point.

## Proposed durable local state

### Week key
A deterministic identifier for the weekly notebook lifecycle.

### Sync manifest
Suggested file: `.notebooklm-sync.json`

Suggested fields:
- `week_key`
- `notebook_id`
- `notebook_title`
- `share_url`
- `privacy_state`
- `audio_artifact_id`
- `audio_source_revision`
- `sources[]`
  - `kind` (`file` or `url`)
  - `local_path` or `url`
  - `checksum`
  - `remote_source_id`
  - `status` (`pending`, `ready`, `failed`)
  - `last_error`
  - `last_attempted_at`
- `lock`
  - `owner`
  - `acquired_at`
  - `expires_at`
- `last_run`
  - `status`
  - `stage`
  - `started_at`
  - `finished_at`

## Core invariants

### Identity invariants
- one week maps to one canonical notebook
- reruns must reuse the canonical notebook
- ambiguity must fail closed

### Source invariants
- roundup markdown is attached as a file source
- only external cited URLs are attached as URL sources
- duplicate sources are never reattached silently
- successful source uploads survive later failures

### Readiness invariants
- sync is not complete until required sources are ready
- retries resume from durable state instead of restarting blindly
- failed sources stay visible in local state

### Privacy invariants
- notebooks stay private by default
- weekday sync never publishes
- publication requires explicit operator intent and all readiness gates
- the system must not pretend that notebook-level sharing is source-level sharing

### Audio invariants
- audio is generated from the current source revision
- stale audio cannot satisfy Friday publish gates
- retrying audio must not duplicate source uploads

### Recovery invariants
- local curated content remains the source of record during external outages
- external SDK drift must fail safe
- partial progress must be checkpointed and resumable
- concurrent same-week sync must not corrupt notebook identity or manifest state

### Input invariants
- all selected target-week artifacts must agree on one week key
- missing required weekly artifacts block remote mutation before sync begins
- mixed-week local inputs fail closed instead of being guessed into one notebook

### Automation invariants
- scheduled reruns with an unchanged source fingerprint are safe no-ops
- unattended automation must honor existing locks and active manual runs
- a missed publication window requires explicit operator review before later publication

### Override and approval invariants
- manual repair must be scoped, auditable, and tied to an operator reason when destructive
- overrides cannot bypass approved-account checks or privacy gates
- publication approval is tied to the current weekly state and expires when that state changes
- rollback clears downstream trust until a fresh successful publication occurs

### Downstream package invariants
- one weekly package must reference one canonical share target for one week
- bundle metadata and audio artifacts must match the current weekly source revision
- missing downstream package components block packaging instead of producing a partial bundle

## Stage model for observability

Recommended stages:
- `auth.check`
- `week.resolve`
- `notebook.resolve`
- `manifest.load`
- `lock.acquire`
- `sources.extract`
- `sources.attach.files`
- `sources.attach.urls`
- `sources.wait_ready`
- `audio.generate`
- `publish.share`
- `publish.verify`
- `publish.package`
- `lock.release`

## Honest terminal states

Recommended run statuses:
- `succeeded`
- `succeeded_notebook_only`
- `published`
- `published_unverified_visibility`
- `degraded_retryable`
- `blocked_auth`
- `blocked_policy`
- `failed_dependency_compatibility`
- `failed_ambiguity`

## Test status

The report podcast MVP scenarios are executable pytest-bdd coverage backed by the real service surface, fake NotebookLM adapter, and real git publishing in a temporary repository.

The broader weekly sync scenarios are future contract coverage. They are collected by pytest-bdd as strict expected failures until each behavior has implementation-backed step definitions. The quality test suite validates that every scenario remains bound, focused, and structurally valid.

## Why this contract exists

These tests keep future code honest about:
- weekly notebook identity
- idempotent sync behavior
- privacy and publication boundaries
- recovery after interruptions
- resilience under dependency breakage
