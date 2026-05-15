Feature: Weekly notebook identity and notebook reuse
  As the operator curating Eliezer's weekly AI roundup
  I want one canonical NotebookLM notebook per week
  So that reruns stay deterministic and resilient

  Background:
    Given the curated roundup pipeline writes the week's markdown outputs
    And the sync system can derive the week key from the roundup date

  Rule: One week maps to one notebook
    Scenario: Create the week's notebook from curated roundup artifacts
      Given no notebook has been recorded for the current week
      And the week's cited URL manifest exists
      When the operator runs the weekly NotebookLM sync
      Then a NotebookLM notebook should be created for that week
      And the notebook should be recorded as the canonical notebook for that week

    Scenario: Reuse the existing notebook on a later rerun
      Given the week already has a recorded NotebookLM notebook id
      And the roundup markdown changed since the last sync
      When the operator reruns the weekly NotebookLM sync
      Then the existing notebook should be reused
      And no second notebook should be created for the same week

  Rule: Ambiguity fails closed
    Scenario: Stop when multiple candidate notebooks exist for one week
      Given two remote notebooks appear to match the same week key
      When the operator runs the weekly NotebookLM sync
      Then the sync should fail closed before mutating NotebookLM
      And the operator should be told that notebook identity is ambiguous
