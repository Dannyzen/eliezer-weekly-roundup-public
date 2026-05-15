Feature: Manifest integrity and schema evolution
  As the infrastructure maintaining sync durability
  I want manifest corruption and schema changes to fail safely
  So that retries never destroy notebook identity or source history

  Background:
    Given the local sync manifest is the durable checkpoint for weekly NotebookLM state

  Rule: Corrupt state must fail before remote mutation
    Scenario: Reject a corrupt manifest before syncing
      Given the local sync manifest for the target week is not valid JSON
      When the operator runs the weekly NotebookLM sync
      Then the sync should fail before any remote mutation
      And the operator should be told that the manifest is corrupt

    Scenario: Preserve the previous manifest when a write is interrupted
      Given the current week has a valid local sync manifest
      When the process crashes during a manifest update
      Then the previous valid manifest should remain readable on disk
      And the next retry should recover from the last fully written checkpoint

  Rule: Older durable state can be migrated safely
    Scenario: Migrate an older manifest schema before resuming sync
      Given the local sync manifest was written by an older schema version
      When the operator runs the weekly NotebookLM sync
      Then the manifest should be upgraded in a backward-compatible way
      And existing notebook ids and source ids should be preserved through migration
