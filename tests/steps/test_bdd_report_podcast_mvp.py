from __future__ import annotations

import asyncio
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import pytest

pytest.importorskip("pytest_bdd")
from pytest_bdd import given, scenario, then, when

from eliezer_weekly_roundup.report_podcast import (
    MANIFEST_NAME,
    AudioArtifactRecord,
    GitPublisher,
    NotebookRecord,
    ReportPodcastOptions,
    ReportPodcastResult,
    ReportPodcastService,
    SourceRecord,
    SubprocessGitPublisher,
    parse_report_document,
    upsert_managed_audio_section,
)

FEATURE = "../bdd/report_podcast_mvp.feature"


@scenario(
    FEATURE, "Create a notebook for a report and add the generated podcast to markdown"
)
def test_bdd_create_a_notebook_for_a_report_and_add_the_generated_podcast() -> None:
    return None


@scenario(
    FEATURE, "Reuse an existing podcast when the report source digest is unchanged"
)
def test_bdd_reuse_an_existing_podcast_when_the_report_source_digest_is_unchanged() -> (
    None
):
    return None


@scenario(FEATURE, "Commit and push generated assets when requested")
def test_bdd_commit_and_push_generated_assets_when_requested() -> None:
    return None


class NotebookGatewayForTests:
    def __init__(self) -> None:
        self.notebook = NotebookRecord(
            id="nb-123", title="NotebookLM: Daily Scan: 2026-04-21", created=True
        )
        self.ensure_notebook_calls: list[tuple[str, str | None]] = []
        self.replace_report_source_calls: list[tuple[str, str, str, bool]] = []
        self.ensure_url_sources_calls: list[tuple[str, tuple[str, ...]]] = []
        self.generate_audio_calls: list[dict[str, object]] = []

    async def ensure_notebook(
        self, title: str, preferred_notebook_id: str | None = None
    ) -> NotebookRecord:
        self.ensure_notebook_calls.append((title, preferred_notebook_id))
        return self.notebook

    async def replace_report_source(
        self,
        notebook_id: str,
        source_title: str,
        content: str,
        *,
        delete_existing: bool = True,
    ) -> SourceRecord:
        self.replace_report_source_calls.append(
            (notebook_id, source_title, content, delete_existing)
        )
        return SourceRecord(id="src-report", key=source_title)

    async def ensure_url_sources(
        self, notebook_id: str, urls: list[str]
    ) -> list[SourceRecord]:
        self.ensure_url_sources_calls.append((notebook_id, tuple(urls)))
        return [
            SourceRecord(id=f"src-url-{index}", key=url)
            for index, url in enumerate(urls, start=1)
        ]

    async def generate_audio_overview(
        self,
        notebook_id: str,
        output_path: Path,
        *,
        instructions: str | None,
        language: str,
        audio_format: str,
        audio_length: str,
        timeout_seconds: int,
    ) -> AudioArtifactRecord:
        self.generate_audio_calls.append(
            {
                "notebook_id": notebook_id,
                "output_path": output_path,
                "instructions": instructions,
                "language": language,
                "audio_format": audio_format,
                "audio_length": audio_length,
                "timeout_seconds": timeout_seconds,
            }
        )
        output_path.write_bytes(b"fake mp3 bytes")
        return AudioArtifactRecord(id="audio-123", path=output_path)


class FakeGitPublisher:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def commit_and_push(
        self, *, repo_root: Path, paths: list[Path], message: str
    ) -> None:
        self.calls.append({"repo_root": repo_root, "paths": paths, "message": message})


class GitPublisherFactory(Protocol):
    def __call__(self) -> GitPublisher: ...


@dataclass
class MvpContext:
    repo_root: Path
    report_path: Path
    gateway: NotebookGatewayForTests
    git_publisher_factory: GitPublisherFactory
    result: ReportPodcastResult | None = None
    fake_git_publisher: FakeGitPublisher | None = None
    markdown_before_rerun: str | None = None
    remote_path: Path | None = None


@pytest.fixture
def mvp_context(tmp_path: Path) -> MvpContext:
    report_path = tmp_path / "roundups" / "2026-04-21.md"
    report_path.parent.mkdir(parents=True)
    report_path.write_text(
        "# Daily Scan: 2026-04-21\n\n"
        "Core source: https://example.com/alpha\n"
        "Supporting source: https://example.com/beta).\n"
        "Local note: ./notes/local-only.md\n",
        encoding="utf-8",
    )
    fake_git = FakeGitPublisher()
    return MvpContext(
        repo_root=tmp_path,
        report_path=report_path,
        gateway=NotebookGatewayForTests(),
        git_publisher_factory=lambda: fake_git,
        fake_git_publisher=fake_git,
    )


def _run_report_podcast(context: MvpContext, *, push: bool) -> None:
    service = ReportPodcastService(
        repo_root=context.repo_root,
        gateway=context.gateway,
        git_publisher=context.git_publisher_factory(),
    )
    context.result = asyncio.run(
        service.generate_podcast(context.report_path, ReportPodcastOptions(push=push))
    )


def _git(repo_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


@given("the repo contains a markdown report with cited URLs")
def repo_contains_markdown_report(mvp_context: MvpContext) -> None:
    assert mvp_context.report_path.exists()
    parsed = parse_report_document(
        mvp_context.report_path, repo_root=mvp_context.repo_root
    )
    assert parsed.title == "Daily Scan: 2026-04-21"
    assert parsed.cited_urls == [
        "https://example.com/alpha",
        "https://example.com/beta",
    ]


@given("the report has not been synchronized before")
def report_has_not_been_synchronized_before(mvp_context: MvpContext) -> None:
    assert not (mvp_context.repo_root / MANIFEST_NAME).exists()
    assert not mvp_context.report_path.with_suffix(".notebooklm.mp3").exists()


@given(
    "the report already has a manifest entry and a downloaded podcast for the current source digest"
)
def report_has_manifest_entry_and_downloaded_podcast(mvp_context: MvpContext) -> None:
    parsed = parse_report_document(
        mvp_context.report_path, repo_root=mvp_context.repo_root
    )
    audio_path = parsed.audio_output_path
    audio_path.write_bytes(b"existing audio")
    updated_markdown = upsert_managed_audio_section(
        mvp_context.report_path.read_text(encoding="utf-8"),
        audio_relative_path=audio_path.relative_to(
            mvp_context.report_path.parent
        ).as_posix(),
        notebook_title="NotebookLM: Daily Scan: 2026-04-21",
        notebook_id="nb-123",
    )
    mvp_context.report_path.write_text(updated_markdown, encoding="utf-8")
    mvp_context.markdown_before_rerun = updated_markdown
    manifest = {
        "reports": {
            parsed.relative_path.as_posix(): {
                "report_path": parsed.relative_path.as_posix(),
                "notebook_id": "nb-123",
                "notebook_title": "NotebookLM: Daily Scan: 2026-04-21",
                "source_digest": parsed.source_digest,
                "report_source_id": "src-report",
                "url_source_ids": ["src-url-1", "src-url-2"],
                "audio_artifact_id": "audio-123",
                "audio_path": parsed.audio_relative_path.as_posix(),
            }
        }
    }
    (mvp_context.repo_root / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


@given("the repo has a configured origin remote")
def repo_has_configured_origin_remote(mvp_context: MvpContext) -> None:
    remote_path = mvp_context.repo_root.parent / "origin.git"
    subprocess.run(
        ["git", "init", "-b", "master"], cwd=mvp_context.repo_root, check=True
    )
    _git(mvp_context.repo_root, "config", "user.email", "tests@example.invalid")
    _git(mvp_context.repo_root, "config", "user.name", "BDD Test")
    subprocess.run(["git", "init", "--bare", str(remote_path)], check=True)
    _git(mvp_context.repo_root, "remote", "add", "origin", str(remote_path))
    mvp_context.remote_path = remote_path
    mvp_context.git_publisher_factory = SubprocessGitPublisher


@when("the operator runs the report podcast command")
def operator_runs_report_podcast_command(mvp_context: MvpContext) -> None:
    _run_report_podcast(mvp_context, push=False)


@when("the operator reruns the report podcast command")
def operator_reruns_report_podcast_command(mvp_context: MvpContext) -> None:
    _run_report_podcast(mvp_context, push=False)


@when("the operator runs the report podcast command with push enabled")
def operator_runs_report_podcast_command_with_push(mvp_context: MvpContext) -> None:
    _run_report_podcast(mvp_context, push=True)


@then("a dedicated NotebookLM notebook should exist for that report")
def dedicated_notebook_exists(mvp_context: MvpContext) -> None:
    assert mvp_context.result is not None
    assert mvp_context.result.notebook_id == "nb-123"
    assert mvp_context.gateway.ensure_notebook_calls == [
        ("NotebookLM: Daily Scan: 2026-04-21", None)
    ]


@then("the report sources should be uploaded to NotebookLM")
def report_sources_are_uploaded(mvp_context: MvpContext) -> None:
    assert len(mvp_context.gateway.replace_report_source_calls) == 1
    assert (
        "Core source: https://example.com/alpha"
        in mvp_context.gateway.replace_report_source_calls[0][2]
    )
    assert mvp_context.gateway.ensure_url_sources_calls == [
        ("nb-123", ("https://example.com/alpha", "https://example.com/beta"))
    ]


@then("a podcast file should be downloaded next to the report markdown")
def podcast_file_is_downloaded_next_to_report(mvp_context: MvpContext) -> None:
    assert mvp_context.result is not None
    audio_path = mvp_context.report_path.with_suffix(".notebooklm.mp3")
    assert mvp_context.result.audio_path == audio_path
    assert audio_path.read_bytes() == b"fake mp3 bytes"


@then("the manifest should record the notebook, sources, and podcast")
def manifest_records_notebook_sources_and_podcast(mvp_context: MvpContext) -> None:
    manifest = json.loads(
        (mvp_context.repo_root / MANIFEST_NAME).read_text(encoding="utf-8")
    )
    entry = manifest["reports"]["roundups/2026-04-21.md"]
    assert entry["notebook_id"] == "nb-123"
    assert entry["report_source_id"] == "src-report"
    assert entry["url_source_ids"] == ["src-url-1", "src-url-2"]
    assert entry["audio_artifact_id"] == "audio-123"
    assert entry["audio_path"] == "roundups/2026-04-21.notebooklm.mp3"


@then("the markdown should contain a managed audio section linking to that podcast")
def markdown_contains_managed_audio_section(mvp_context: MvpContext) -> None:
    markdown = mvp_context.report_path.read_text(encoding="utf-8")
    assert "<!-- eliezer-roundup:audio:start -->" in markdown
    assert "## Audio Overview" in markdown
    assert "2026-04-21.notebooklm.mp3" in markdown
    assert "Notebook id:" not in markdown
    assert "nb-123" not in markdown


@then("no new podcast should be generated")
def no_new_podcast_is_generated(mvp_context: MvpContext) -> None:
    assert mvp_context.result is not None
    assert mvp_context.result.generated_new_audio is False
    assert mvp_context.gateway.ensure_notebook_calls == []
    assert mvp_context.gateway.generate_audio_calls == []


@then("the existing managed audio section should remain stable")
def existing_audio_section_remains_stable(mvp_context: MvpContext) -> None:
    assert mvp_context.markdown_before_rerun is not None
    assert (
        mvp_context.report_path.read_text(encoding="utf-8")
        == mvp_context.markdown_before_rerun
    )
    assert (
        mvp_context.report_path.with_suffix(".notebooklm.mp3").read_bytes()
        == b"existing audio"
    )


@then("the changed report assets should be committed")
def changed_report_assets_are_committed(mvp_context: MvpContext) -> None:
    committed_paths = set(
        _git(
            mvp_context.repo_root, "show", "--name-only", "--pretty=format:"
        ).splitlines()
    )
    assert MANIFEST_NAME not in committed_paths
    assert {
        "roundups/2026-04-21.md",
        "roundups/2026-04-21.notebooklm.mp3",
    }.issubset(committed_paths)
    assert _git(mvp_context.repo_root, "log", "-1", "--pretty=%s") == (
        "Add NotebookLM podcast for roundups/2026-04-21.md"
    )


@then("the current git branch should be pushed to origin")
def current_git_branch_is_pushed_to_origin(mvp_context: MvpContext) -> None:
    local_head = _git(mvp_context.repo_root, "rev-parse", "HEAD")
    remote_head = _git(mvp_context.repo_root, "ls-remote", "origin", "master").split()[
        0
    ]
    assert remote_head == local_head
