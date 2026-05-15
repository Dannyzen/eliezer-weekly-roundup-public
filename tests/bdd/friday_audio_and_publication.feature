Feature: Friday audio generation and publication gates
  As the operator preparing the public weekly package
  I want audio generation and publication to respect readiness gates
  So that readers only receive a complete, current, and intentional weekly notebook

  Background:
    Given the week's notebook has been synchronized from curated roundup artifacts

  Rule: Midweek sync stays private
    Scenario: Keep the weekly notebook private before Friday
      Given today is not Friday
      When the operator runs the weekly NotebookLM sync
      Then the weekly notebook should remain private
      And no public share link should be emitted

  Rule: Friday publication requires current audio
    Scenario: Generate the Friday audio overview and publish the canonical notebook
      Given today is Friday
      And all required sources are ready
      And no audio overview exists for the current source set
      When the operator runs the Friday publication workflow
      Then an audio overview should be generated for the weekly notebook
      And the canonical weekly notebook should be published with one share link

    Scenario: Block publication when audio is stale after source changes
      Given an audio overview exists for the weekly notebook
      And the weekly sources changed after that audio overview was generated
      When the operator requests publication
      Then publication should be blocked until audio is regenerated
      And the operator should be told that the current audio artifact is stale
