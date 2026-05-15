Feature: Input contracts, week purity, and required artifact presence
  As the infrastructure choosing what belongs in one weekly notebook
  I want target-week inputs to agree with each other before any remote mutation
  So that the system never mixes weeks or syncs from incomplete local state

  Background:
    Given the target week is resolved before any remote mutation begins

  Rule: Selected artifacts must agree on one week
    Scenario: Fail closed when curated artifacts span multiple week keys
      Given the selected roundup markdown resolves to one week key
      And a cited URL manifest or companion artifact resolves to a different week key
      When the operator runs the weekly NotebookLM sync
      Then the sync should fail closed before any remote mutation
      And the operator should be told that the selected artifacts do not agree on one target week

  Rule: Required weekly artifacts must exist before sync
    Scenario: Refuse sync when the curated roundup markdown for the target week is missing
      Given no curated roundup markdown exists for the requested week
      When the operator runs the weekly NotebookLM sync
      Then the sync should fail before notebook resolution
      And the operator should be told which required artifact is missing

    Scenario: Refuse sync when the cited URL manifest week does not match the roundup markdown week
      Given the roundup markdown exists for the requested week
      And the cited URL manifest points at a different week key
      When the operator runs the weekly NotebookLM sync
      Then the sync should fail before source extraction
      And no sources should be attached for either week
