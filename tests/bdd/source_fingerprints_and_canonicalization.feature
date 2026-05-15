Feature: Source fingerprints, canonicalization, and stale artifact detection
  As the sync engine protecting weekly notebook correctness
  I want source identity to be canonical and content-aware
  So that dedupe, retries, and publication gates stay trustworthy

  Background:
    Given the system computes canonical source identities and source-set fingerprints for each week

  Rule: Equivalent URLs are deduped consistently
    Scenario: Deduplicate URLs that differ only by trailing punctuation and fragments
      Given the roundup contains the same external URL with trailing punctuation or a removable fragment
      When the operator runs the weekly NotebookLM sync
      Then those URLs should collapse into one canonical URL source
      And the canonical URL should be the only URL stored in the manifest

    Scenario: Ignore tracking-only URL variants when the canonical source is the same
      Given the roundup cites the same source once directly and once with tracking query parameters
      When the operator runs the weekly NotebookLM sync
      Then the system should attach only one canonical URL source for that article
      And the manifest should record the canonicalized URL identity

  Rule: Downstream artifacts must reflect the current source set
    Scenario: Mark audio stale when the source fingerprint changes
      Given the current week already has a generated audio overview
      And the source-set fingerprint changes because the roundup content changed
      When the operator reruns the weekly NotebookLM sync
      Then the existing audio artifact should be marked stale
      And publication should require a regenerated audio overview for the new fingerprint
