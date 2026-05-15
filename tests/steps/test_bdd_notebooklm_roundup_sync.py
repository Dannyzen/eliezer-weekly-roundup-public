from __future__ import annotations

import json
from pathlib import Path

import pytest

pytest.importorskip("pytest_bdd")
from pytest_bdd import given, parsers, scenario, then, when

pytestmark = pytest.mark.xfail(
    strict=True,
    reason=(
        "Future weekly NotebookLM sync contract. Keep strict xfail until each "
        "scenario is backed by real implementation steps."
    ),
)

FEATURE_WEEKLY_IDENTITY = "../bdd/weekly_notebook_identity.feature"
FEATURE_SOURCE_SYNC = "../bdd/source_sync_resilience.feature"
FEATURE_LOCKING = "../bdd/sync_locking_and_concurrency.feature"
FEATURE_AUTH = "../bdd/auth_and_account_boundaries.feature"
FEATURE_PUBLICATION = "../bdd/friday_audio_and_publication.feature"
FEATURE_BACKFILL = "../bdd/backfill_and_correction.feature"
FEATURE_DEGRADED = "../bdd/degraded_paths_and_auditability.feature"
FEATURE_OPERATOR_REVIEW = "../bdd/operator_review_and_dry_run.feature"
FEATURE_MANIFEST = "../bdd/manifest_integrity_and_schema_evolution.feature"
FEATURE_SOURCE_FINGERPRINTS = "../bdd/source_fingerprints_and_canonicalization.feature"
FEATURE_READER_EXPERIENCE = "../bdd/reader_experience_and_provenance.feature"
FEATURE_OBSERVABILITY = "../bdd/observability_and_recovery_reporting.feature"
FEATURE_SOURCE_READINESS = "../bdd/source_readiness_and_waiting.feature"
FEATURE_REMOTE_DRIFT = "../bdd/remote_drift_and_reconciliation.feature"
FEATURE_RETRY_BUDGETS = "../bdd/retry_budget_and_rate_limit_resilience.feature"
FEATURE_SESSION_EXPIRY = "../bdd/session_expiry_and_reauthentication.feature"
FEATURE_REMOTE_SIDE_EFFECTS = "../bdd/remote_side_effect_checkpoint_recovery.feature"
FEATURE_CALENDAR_BOUNDARIES = "../bdd/calendar_boundary_and_timezone_safety.feature"
FEATURE_INPUT_CONTRACTS = "../bdd/input_contracts_and_week_purity.feature"
FEATURE_AUTOMATION = "../bdd/automation_and_scheduler_safety.feature"
FEATURE_OPERATOR_OVERRIDE = "../bdd/operator_override_and_manual_repair.feature"
FEATURE_APPROVAL_FRESHNESS = "../bdd/approval_freshness_and_rollback_chain.feature"
FEATURE_PUBLICATION_BUNDLE = "../bdd/publication_bundle_consistency.feature"


@scenario(
    FEATURE_WEEKLY_IDENTITY, "Create the week's notebook from curated roundup artifacts"
)
def test_bdd_create_the_weeks_notebook_from_curated_roundup_artifacts() -> None:
    return None


@scenario(FEATURE_WEEKLY_IDENTITY, "Reuse the existing notebook on a later rerun")
def test_bdd_reuse_the_existing_notebook_on_a_later_rerun() -> None:
    return None


@scenario(
    FEATURE_WEEKLY_IDENTITY, "Stop when multiple candidate notebooks exist for one week"
)
def test_bdd_stop_when_multiple_candidate_notebooks_exist_for_one_week() -> None:
    return None


@scenario(FEATURE_SOURCE_SYNC, "Import roundup markdown and external cited URLs")
def test_bdd_import_roundup_markdown_and_external_cited_urls() -> None:
    return None


@scenario(FEATURE_SOURCE_SYNC, "Continue syncing when one cited URL is unreachable")
def test_bdd_continue_syncing_when_one_cited_url_is_unreachable() -> None:
    return None


@scenario(
    FEATURE_SOURCE_SYNC,
    "Resume after an interrupted sync without duplicate source uploads",
)
def test_bdd_resume_after_an_interrupted_sync_without_duplicate_source_uploads() -> (
    None
):
    return None


@scenario(FEATURE_LOCKING, "Allow only one same-week sync to mutate NotebookLM")
def test_bdd_allow_only_one_same_week_sync_to_mutate_notebooklm() -> None:
    return None


@scenario(FEATURE_LOCKING, "Reclaim a stale lock from a crashed sync")
def test_bdd_reclaim_a_stale_lock_from_a_crashed_sync() -> None:
    return None


@scenario(
    FEATURE_AUTH, "Abort before first write when no valid NotebookLM session exists"
)
def test_bdd_abort_before_first_write_when_no_valid_notebooklm_session_exists() -> None:
    return None


@scenario(FEATURE_AUTH, "Reject a valid session for the wrong account")
def test_bdd_reject_a_valid_session_for_the_wrong_account() -> None:
    return None


@scenario(FEATURE_AUTH, "Refuse to publish a mixed-sensitivity notebook")
def test_bdd_refuse_to_publish_a_mixed_sensitivity_notebook() -> None:
    return None


@scenario(FEATURE_PUBLICATION, "Keep the weekly notebook private before Friday")
def test_bdd_keep_the_weekly_notebook_private_before_friday() -> None:
    return None


@scenario(
    FEATURE_PUBLICATION,
    "Generate the Friday audio overview and publish the canonical notebook",
)
def test_bdd_generate_the_friday_audio_overview_and_publish_the_canonical_notebook() -> (
    None
):
    return None


@scenario(
    FEATURE_PUBLICATION, "Block publication when audio is stale after source changes"
)
def test_bdd_block_publication_when_audio_is_stale_after_source_changes() -> None:
    return None


@scenario(
    FEATURE_BACKFILL,
    "Backfill a previously missed week without altering the current week",
)
def test_bdd_backfill_a_previously_missed_week_without_altering_the_current_week() -> (
    None
):
    return None


@scenario(
    FEATURE_BACKFILL, "Correct a published week without creating a second share link"
)
def test_bdd_correct_a_published_week_without_creating_a_second_share_link() -> None:
    return None


@scenario(
    FEATURE_DEGRADED,
    "Fail safely when notebooklm-py returns an unexpected response shape",
)
def test_bdd_fail_safely_when_notebooklm_py_returns_an_unexpected_response_shape() -> (
    None
):
    return None


@scenario(
    FEATURE_DEGRADED,
    "Surface an ambiguous publish state when verification is unavailable",
)
def test_bdd_surface_an_ambiguous_publish_state_when_verification_is_unavailable() -> (
    None
):
    return None


@scenario(
    FEATURE_DEGRADED, "Preserve the local roundup when NotebookLM is fully unavailable"
)
def test_bdd_preserve_the_local_roundup_when_notebooklm_is_fully_unavailable() -> None:
    return None


@scenario(
    FEATURE_OPERATOR_REVIEW, "Preview the weekly sync plan without mutating NotebookLM"
)
def test_bdd_preview_the_weekly_sync_plan_without_mutating_notebooklm() -> None:
    return None


@scenario(
    FEATURE_OPERATOR_REVIEW, "Preview a Friday publication gate before running it"
)
def test_bdd_preview_a_friday_publication_gate_before_running_it() -> None:
    return None


@scenario(FEATURE_OPERATOR_REVIEW, "Require explicit approval before public sharing")
def test_bdd_require_explicit_approval_before_public_sharing() -> None:
    return None


@scenario(FEATURE_MANIFEST, "Reject a corrupt manifest before syncing")
def test_bdd_reject_a_corrupt_manifest_before_syncing() -> None:
    return None


@scenario(
    FEATURE_MANIFEST, "Preserve the previous manifest when a write is interrupted"
)
def test_bdd_preserve_the_previous_manifest_when_a_write_is_interrupted() -> None:
    return None


@scenario(FEATURE_MANIFEST, "Migrate an older manifest schema before resuming sync")
def test_bdd_migrate_an_older_manifest_schema_before_resuming_sync() -> None:
    return None


@scenario(
    FEATURE_SOURCE_FINGERPRINTS,
    "Deduplicate URLs that differ only by trailing punctuation and fragments",
)
def test_bdd_deduplicate_urls_that_differ_only_by_trailing_punctuation_and_fragments() -> (
    None
):
    return None


@scenario(
    FEATURE_SOURCE_FINGERPRINTS,
    "Ignore tracking-only URL variants when the canonical source is the same",
)
def test_bdd_ignore_tracking_only_url_variants_when_the_canonical_source_is_the_same() -> (
    None
):
    return None


@scenario(
    FEATURE_SOURCE_FINGERPRINTS, "Mark audio stale when the source fingerprint changes"
)
def test_bdd_mark_audio_stale_when_the_source_fingerprint_changes() -> None:
    return None


@scenario(
    FEATURE_READER_EXPERIENCE,
    "Publish a notebook with visible week identity and provenance",
)
def test_bdd_publish_a_notebook_with_visible_week_identity_and_provenance() -> None:
    return None


@scenario(
    FEATURE_READER_EXPERIENCE, "Keep one canonical share target per week for readers"
)
def test_bdd_keep_one_canonical_share_target_per_week_for_readers() -> None:
    return None


@scenario(
    FEATURE_READER_EXPERIENCE,
    "Revoke public sharing after a post-publish policy violation",
)
def test_bdd_revoke_public_sharing_after_a_post_publish_policy_violation() -> None:
    return None


@scenario(
    FEATURE_OBSERVABILITY,
    "Distinguish retryable failures from terminal policy failures",
)
def test_bdd_distinguish_retryable_failures_from_terminal_policy_failures() -> None:
    return None


@scenario(FEATURE_OBSERVABILITY, "Record the exact failing stage for a degraded run")
def test_bdd_record_the_exact_failing_stage_for_a_degraded_run() -> None:
    return None


@scenario(
    FEATURE_OBSERVABILITY,
    "Require manual verification before announcing a weakly verified publication",
)
def test_bdd_require_manual_verification_before_announcing_a_weakly_verified_publication() -> (
    None
):
    return None


@scenario(
    FEATURE_SOURCE_READINESS,
    "Time out waiting for a required source that never becomes ready",
)
def test_bdd_time_out_waiting_for_a_required_source_that_never_becomes_ready() -> None:
    return None


@scenario(
    FEATURE_SOURCE_READINESS,
    "Resume readiness polling after a crash without reattaching sources",
)
def test_bdd_resume_readiness_polling_after_a_crash_without_reattaching_sources() -> (
    None
):
    return None


@scenario(
    FEATURE_SOURCE_READINESS,
    "Block Friday publication while a required source is still processing",
)
def test_bdd_block_friday_publication_while_a_required_source_is_still_processing() -> (
    None
):
    return None


@scenario(
    FEATURE_REMOTE_DRIFT,
    "Fail closed when the recorded notebook id no longer exists remotely",
)
def test_bdd_fail_closed_when_the_recorded_notebook_id_no_longer_exists_remotely() -> (
    None
):
    return None


@scenario(FEATURE_REMOTE_DRIFT, "Reattach only sources that were removed out of band")
def test_bdd_reattach_only_sources_that_were_removed_out_of_band() -> None:
    return None


@scenario(
    FEATURE_REMOTE_DRIFT,
    "Detect out-of-band visibility changes before announcing publication",
)
def test_bdd_detect_out_of_band_visibility_changes_before_announcing_publication() -> (
    None
):
    return None


@scenario(FEATURE_RETRY_BUDGETS, "Back off and retry after a 429 during URL attachment")
def test_bdd_back_off_and_retry_after_a_429_during_url_attachment() -> None:
    return None


@scenario(
    FEATURE_RETRY_BUDGETS,
    "Mark retry-budget exhaustion as retryable rather than ambiguous",
)
def test_bdd_mark_retry_budget_exhaustion_as_retryable_rather_than_ambiguous() -> None:
    return None


@scenario(
    FEATURE_RETRY_BUDGETS, "Stop cleanly on quota exhaustion after partial progress"
)
def test_bdd_stop_cleanly_on_quota_exhaustion_after_partial_progress() -> None:
    return None


@scenario(
    FEATURE_SESSION_EXPIRY,
    "Session expires after notebook resolution but before source attachment",
)
def test_bdd_session_expires_after_notebook_resolution_but_before_source_attachment() -> (
    None
):
    return None


@scenario(
    FEATURE_SESSION_EXPIRY,
    "Reauthenticated retry resumes instead of recreating remote objects",
)
def test_bdd_reauthenticated_retry_resumes_instead_of_recreating_remote_objects() -> (
    None
):
    return None


@scenario(FEATURE_SESSION_EXPIRY, "Account identity changes before publication")
def test_bdd_account_identity_changes_before_publication() -> None:
    return None


@scenario(
    FEATURE_REMOTE_SIDE_EFFECTS,
    "Recover an existing share link after a crash before manifest write",
)
def test_bdd_recover_an_existing_share_link_after_a_crash_before_manifest_write() -> (
    None
):
    return None


@scenario(
    FEATURE_REMOTE_SIDE_EFFECTS,
    "Recover an audio artifact generated before a local crash",
)
def test_bdd_recover_an_audio_artifact_generated_before_a_local_crash() -> None:
    return None


@scenario(
    FEATURE_REMOTE_SIDE_EFFECTS,
    "Reconcile an uncertain source upload after a client timeout",
)
def test_bdd_reconcile_an_uncertain_source_upload_after_a_client_timeout() -> None:
    return None


@scenario(
    FEATURE_CALENDAR_BOUNDARIES,
    "Freeze the target week for a run that crosses midnight",
)
def test_bdd_freeze_the_target_week_for_a_run_that_crosses_midnight() -> None:
    return None


@scenario(
    FEATURE_CALENDAR_BOUNDARIES,
    "Evaluate Friday publication in the configured publishing timezone",
)
def test_bdd_evaluate_friday_publication_in_the_configured_publishing_timezone() -> (
    None
):
    return None


@scenario(
    FEATURE_CALENDAR_BOUNDARIES,
    "Do not auto-publish a historical backfill just because today is Friday",
)
def test_bdd_do_not_auto_publish_a_historical_backfill_just_because_today_is_friday() -> (
    None
):
    return None


@scenario(
    FEATURE_INPUT_CONTRACTS,
    "Fail closed when curated artifacts span multiple week keys",
)
def test_bdd_fail_closed_when_curated_artifacts_span_multiple_week_keys() -> None:
    return None


@scenario(
    FEATURE_INPUT_CONTRACTS,
    "Refuse sync when the curated roundup markdown for the target week is missing",
)
def test_bdd_refuse_sync_when_the_curated_roundup_markdown_for_the_target_week_is_missing() -> (
    None
):
    return None


@scenario(
    FEATURE_INPUT_CONTRACTS,
    "Refuse sync when the cited URL manifest week does not match the roundup markdown week",
)
def test_bdd_refuse_sync_when_the_cited_url_manifest_week_does_not_match_the_roundup_markdown_week() -> (
    None
):
    return None


@scenario(
    FEATURE_AUTOMATION,
    "Scheduled sync exits cleanly when a manual same-week run owns the lock",
)
def test_bdd_scheduled_sync_exits_cleanly_when_a_manual_same_week_run_owns_the_lock() -> (
    None
):
    return None


@scenario(
    FEATURE_AUTOMATION,
    "Repeated scheduled sync with an unchanged source fingerprint is a no-op",
)
def test_bdd_repeated_scheduled_sync_with_an_unchanged_source_fingerprint_is_a_no_op() -> (
    None
):
    return None


@scenario(
    FEATURE_AUTOMATION,
    "Missed Friday auto-publication requires explicit operator review",
)
def test_bdd_missed_friday_auto_publication_requires_explicit_operator_review() -> None:
    return None


@scenario(
    FEATURE_OPERATOR_OVERRIDE,
    "Resume from source readiness after the operator confirms attachment checkpoint",
)
def test_bdd_resume_from_source_readiness_after_the_operator_confirms_attachment_checkpoint() -> (
    None
):
    return None


@scenario(
    FEATURE_OPERATOR_OVERRIDE,
    "Require a reason when force-rebinding a week to a different notebook id",
)
def test_bdd_require_a_reason_when_force_rebinding_a_week_to_a_different_notebook_id() -> (
    None
):
    return None


@scenario(
    FEATURE_OPERATOR_OVERRIDE,
    "Refuse a force-publish override when auth or privacy checks are red",
)
def test_bdd_refuse_a_force_publish_override_when_auth_or_privacy_checks_are_red() -> (
    None
):
    return None


@scenario(
    FEATURE_APPROVAL_FRESHNESS,
    "Expire publication approval when the source fingerprint changes after approval",
)
def test_bdd_expire_publication_approval_when_the_source_fingerprint_changes_after_approval() -> (
    None
):
    return None


@scenario(
    FEATURE_APPROVAL_FRESHNESS,
    "Block reannouncement after rollback until a fresh publication succeeds",
)
def test_bdd_block_reannouncement_after_rollback_until_a_fresh_publication_succeeds() -> (
    None
):
    return None


@scenario(
    FEATURE_APPROVAL_FRESHNESS,
    "Require fresh approval when visibility drift is detected before publication",
)
def test_bdd_require_fresh_approval_when_visibility_drift_is_detected_before_publication() -> (
    None
):
    return None


@scenario(
    FEATURE_PUBLICATION_BUNDLE,
    "Build a publication bundle from one canonical week, share target, and audio artifact",
)
def test_bdd_build_a_publication_bundle_from_one_canonical_week_share_target_and_audio_artifact() -> (
    None
):
    return None


@scenario(
    FEATURE_PUBLICATION_BUNDLE,
    "Block bundle generation when the share target or local audio path is missing",
)
def test_bdd_block_bundle_generation_when_the_share_target_or_local_audio_path_is_missing() -> (
    None
):
    return None


@scenario(
    FEATURE_PUBLICATION_BUNDLE,
    "Invalidate a saved bundle when a correction changes the audio source revision",
)
def test_bdd_invalidate_a_saved_bundle_when_a_correction_changes_the_audio_source_revision() -> (
    None
):
    return None


@pytest.fixture
def context() -> dict[str, list[str] | str]:
    return {
        "repo_root": str(Path(__file__).resolve().parents[2]),
        "givens": [],
        "whens": [],
        "thens": [],
    }


def _remember(context: dict[str, list[str] | str], bucket: str, step: str) -> None:
    values = context[bucket]
    assert isinstance(values, list)
    values.append(step)


def _pending_message(
    context: dict[str, list[str] | str], failing_expectation: str
) -> str:
    payload = {
        "message": "Pending NotebookLM curated roundup sync implementation. This future BDD contract scenario is strict xfail until backed by real implementation steps.",
        "repo_root": context["repo_root"],
        "failing_expectation": failing_expectation,
        "givens": context["givens"],
        "whens": context["whens"],
        "thens": context["thens"],
    }
    return json.dumps(payload, indent=2)


@given(parsers.re(r"(?P<step>.+)"))
def record_given_step(context: dict[str, list[str] | str], step: str) -> None:
    _remember(context, "givens", step)


@when(parsers.re(r"(?P<step>.+)"))
def record_when_step(context: dict[str, list[str] | str], step: str) -> None:
    _remember(context, "whens", step)


@then(parsers.re(r"(?P<step>.+)"))
def fail_on_then_step(context: dict[str, list[str] | str], step: str) -> None:
    _remember(context, "thens", step)
    pytest.fail(_pending_message(context, step))
