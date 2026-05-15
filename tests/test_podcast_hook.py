from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from eliezer_weekly_roundup.podcast_hook import (
    PodcastHookOptions,
    PodcastHookService,
    audio_profile_for_run,
    select_changed_roundup_reports,
)
from eliezer_weekly_roundup.report_podcast import ReportPodcastResult


@dataclass
class FakeGit:
    sha_before: str
    sha_after_generation: str
    changed: list[str]
    pulled: bool = False
    changed_files_calls: list[tuple[str, str]] | None = None
    current_sha_calls: int = 0

    def pull_ff_only(self) -> None:
        self.pulled = True

    def current_sha(self) -> str:
        self.current_sha_calls += 1
        if self.current_sha_calls >= 2:
            return self.sha_after_generation
        return self.sha_before

    def changed_files(self, since_sha: str, until_sha: str) -> list[str]:
        if self.changed_files_calls is None:
            self.changed_files_calls = []
        self.changed_files_calls.append((since_sha, until_sha))
        return self.changed


class FakePodcastGenerator:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def generate(
        self,
        report_path: Path,
        *,
        instructions: str,
        audio_length: str,
        timeout_seconds: int,
    ) -> ReportPodcastResult:
        self.calls.append(
            {
                "report_path": report_path,
                "instructions": instructions,
                "audio_length": audio_length,
                "timeout_seconds": timeout_seconds,
            }
        )
        audio_path = report_path.with_suffix(".notebooklm.mp3")
        audio_path.parent.mkdir(parents=True, exist_ok=True)
        audio_path.write_bytes(b"fake audio")
        return ReportPodcastResult(
            report_path=report_path,
            notebook_id="nb-1",
            audio_path=audio_path,
            generated_new_audio=True,
        )


def test_select_changed_roundup_reports_filters_markdown_reports_and_keeps_order() -> (
    None
):
    assert select_changed_roundup_reports(
        [
            "README.md",
            "roundups/2026-04-24.md",
            "roundups/2026-04-24.notebooklm.mp3",
            "AgenticAI/README.md",
            "roundups/2026-04-25.md",
        ]
    ) == [Path("roundups/2026-04-24.md"), Path("roundups/2026-04-25.md")]


def test_audio_profile_for_friday_after_synthesis_uses_long_weekly_audio() -> None:
    friday_after_synthesis = datetime(
        2026, 4, 24, 14, 30, tzinfo=ZoneInfo("America/New_York")
    )

    profile = audio_profile_for_run(friday_after_synthesis)

    assert profile.audio_length == "long"
    assert "weekly synthesis" in profile.instructions.lower()


def test_hook_generates_for_changed_roundup_after_successful_push_and_advances_state(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path
    report_path = repo_root / "roundups" / "2026-04-24.md"
    report_path.parent.mkdir(parents=True)
    report_path.write_text(
        "# Daily Scan: 2026-04-24\n\nhttps://example.com/source\n", encoding="utf-8"
    )
    state_path = tmp_path / "hook-state.json"
    state_path.write_text(json.dumps({"last_seen_sha": "old-sha"}), encoding="utf-8")
    git = FakeGit(
        sha_before="new-sha",
        sha_after_generation="podcast-sha",
        changed=["roundups/2026-04-24.md", "README.md"],
    )
    generator = FakePodcastGenerator()
    service = PodcastHookService(repo_root=repo_root, git=git, generator=generator)

    result = service.process(
        PodcastHookOptions(
            state_path=state_path,
            now=datetime(2026, 4, 23, 9, 45, tzinfo=ZoneInfo("America/New_York")),
        )
    )

    assert git.pulled is True
    assert git.changed_files_calls == [("old-sha", "new-sha")]
    assert result.generated_reports == [report_path]
    assert result.audio_paths == [report_path.with_suffix(".notebooklm.mp3")]
    assert generator.calls[0]["audio_length"] == "medium"
    assert (
        json.loads(state_path.read_text(encoding="utf-8"))["last_seen_sha"]
        == "podcast-sha"
    )


def test_hook_initializes_state_without_generating_when_no_prior_sha(
    tmp_path: Path,
) -> None:
    git = FakeGit(
        sha_before="current-sha",
        sha_after_generation="current-sha",
        changed=["roundups/2026-04-24.md"],
    )
    generator = FakePodcastGenerator()
    state_path = tmp_path / "state.json"
    service = PodcastHookService(repo_root=tmp_path, git=git, generator=generator)

    result = service.process(PodcastHookOptions(state_path=state_path))

    assert result.status == "initialized"
    assert generator.calls == []
    assert (
        json.loads(state_path.read_text(encoding="utf-8"))["last_seen_sha"]
        == "current-sha"
    )
