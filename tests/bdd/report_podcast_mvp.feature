Feature: Report-linked NotebookLM podcast MVP
  As the operator of the Eliezer weekly roundup repo
  I want one command to create or reuse a NotebookLM notebook for a report and generate a podcast
  So that each report can grow a listenable audio companion that is committed back into the repo

  Background:
    Given the repo contains a markdown report with cited URLs

  Rule: First run creates the remote notebook and podcast
    Scenario: Create a notebook for a report and add the generated podcast to markdown
      Given the report has not been synchronized before
      When the operator runs the report podcast command
      Then a dedicated NotebookLM notebook should exist for that report
      And the report sources should be uploaded to NotebookLM
      And a podcast file should be downloaded next to the report markdown
      And the manifest should record the notebook, sources, and podcast
      And the markdown should contain a managed audio section linking to that podcast

  Rule: Stable reruns are idempotent
    Scenario: Reuse an existing podcast when the report source digest is unchanged
      Given the report already has a manifest entry and a downloaded podcast for the current source digest
      When the operator reruns the report podcast command
      Then no new podcast should be generated
      And the existing managed audio section should remain stable

  Rule: GitHub publishing is explicit
    Scenario: Commit and push generated assets when requested
      Given the report has not been synchronized before
      And the repo has a configured origin remote
      When the operator runs the report podcast command with push enabled
      Then the changed report assets should be committed
      And the current git branch should be pushed to origin
