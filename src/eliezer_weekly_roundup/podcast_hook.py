from __future__ import annotations

import asyncio
import json
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Protocol
from zoneinfo import ZoneInfo

from .report_podcast import (
    NotebookLMGatewayAdapter,
    ReportPodcastOptions,
    ReportPodcastResult,
    ReportPodcastService,
)

DEFAULT_STATE_PATH = (
    Path.home() / ".hermes" / "state" / "eliezer-weekly-roundup-podcast-hook.json"
)
PUBLISHING_TZ = ZoneInfo("America/New_York")


@dataclass(frozen=True)
class AudioProfile:
    audio_length: str
    instructions: str


@dataclass(frozen=True)
class PodcastHookOptions:
    state_path: Path = DEFAULT_STATE_PATH
    now: datetime | None = None
    timeout_seconds: int = 2400
    max_reports: int = 3


@dataclass(frozen=True)
class PodcastHookResult:
    status: str
    generated_reports: list[Path] = field(default_factory=list)
    reused_reports: list[Path] = field(default_factory=list)
    audio_paths: list[Path] = field(default_factory=list)
    start_sha: str | None = None
    final_sha: str | None = None


class GitHookClient(Protocol):
    def pull_ff_only(self) -> None: ...

    def current_sha(self) -> str: ...

    def changed_files(self, since_sha: str, until_sha: str) -> list[str]: ...


class PodcastGenerator(Protocol):
    def generate(
        self,
        report_path: Path,
        *,
        instructions: str,
        audio_length: str,
        timeout_seconds: int,
    ) -> ReportPodcastResult: ...


class SubprocessGitHookClient:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root

    def pull_ff_only(self) -> None:
        subprocess.run(["git", "pull", "--ff-only"], cwd=self.repo_root, check=True)

    def current_sha(self) -> str:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def changed_files(self, since_sha: str, until_sha: str) -> list[str]:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{since_sha}..{until_sha}"],
            cwd=self.repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]


class ReportPodcastGenerator:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root

    def generate(
        self,
        report_path: Path,
        *,
        instructions: str,
        audio_length: str,
        timeout_seconds: int,
    ) -> ReportPodcastResult:
        gateway = NotebookLMGatewayAdapter()
        service = ReportPodcastService(repo_root=self.repo_root, gateway=gateway)
        return asyncio.run(
            service.generate_podcast(
                report_path,
                ReportPodcastOptions(
                    push=True,
                    instructions=instructions,
                    audio_format="deep-dive",
                    audio_length=audio_length,
                    timeout_seconds=timeout_seconds,
                ),
            )
        )


def select_changed_roundup_reports(changed_paths: list[str]) -> list[Path]:
    reports: list[Path] = []
    seen: set[str] = set()
    for changed_path in changed_paths:
        path = Path(changed_path)
        if len(path.parts) != 2:
            continue
        if path.parts[0] != "roundups":
            continue
        if path.suffix != ".md":
            continue
        key = path.as_posix()
        if key in seen:
            continue
        seen.add(key)
        reports.append(path)
    return reports


def audio_profile_for_run(now: datetime | None = None) -> AudioProfile:
    resolved_now = now or datetime.now(PUBLISHING_TZ)
    if resolved_now.tzinfo is None:
        resolved_now = resolved_now.replace(tzinfo=PUBLISHING_TZ)
    local_now = resolved_now.astimezone(PUBLISHING_TZ)
    if local_now.weekday() == 4 and local_now.hour >= 14:
        return AudioProfile(
            audio_length="long",
            instructions=(
                "Create a full NotebookLM-style weekly synthesis podcast for the operator. "
                "Make it conversational, source-grounded, opinionated, and practical. "
                "Emphasize the week's strongest agent-stack themes, implementation moves, "
                "unresolved risks, and one provocative strategic question."
            ),
        )
    return AudioProfile(
        audio_length="medium",
        instructions=(
            "Create a NotebookLM-style deep-dive podcast for the operator. Be clear, "
            "source-grounded, opinionated, and practical. Highlight the agent-stack "
            "implications, implementation moves, and strategic questions."
        ),
    )


class PodcastHookService:
    def __init__(
        self,
        *,
        repo_root: Path,
        git: GitHookClient | None = None,
        generator: PodcastGenerator | None = None,
    ) -> None:
        self.repo_root = repo_root.resolve()
        self.git = git or SubprocessGitHookClient(self.repo_root)
        self.generator = generator or ReportPodcastGenerator(self.repo_root)

    def process(self, options: PodcastHookOptions) -> PodcastHookResult:
        self.git.pull_ff_only()
        current_sha = self.git.current_sha()
        state = self._load_state(options.state_path)
        last_seen_sha = state.get("last_seen_sha")
        if not last_seen_sha:
            self._save_state(options.state_path, current_sha)
            return PodcastHookResult(
                status="initialized", start_sha=current_sha, final_sha=current_sha
            )
        if last_seen_sha == current_sha:
            return PodcastHookResult(
                status="no_changes", start_sha=current_sha, final_sha=current_sha
            )

        changed_paths = self.git.changed_files(str(last_seen_sha), current_sha)
        report_paths = select_changed_roundup_reports(changed_paths)[
            : options.max_reports
        ]
        if not report_paths:
            self._save_state(options.state_path, current_sha)
            return PodcastHookResult(
                status="no_roundup_changes",
                start_sha=last_seen_sha,
                final_sha=current_sha,
            )

        profile = audio_profile_for_run(options.now)
        generated_reports: list[Path] = []
        reused_reports: list[Path] = []
        audio_paths: list[Path] = []
        for relative_report_path in report_paths:
            report_path = self.repo_root / relative_report_path
            if not report_path.exists():
                continue
            result = self.generator.generate(
                report_path,
                instructions=profile.instructions,
                audio_length=profile.audio_length,
                timeout_seconds=options.timeout_seconds,
            )
            audio_paths.append(result.audio_path)
            if result.generated_new_audio:
                generated_reports.append(report_path)
            else:
                reused_reports.append(report_path)

        final_sha = self.git.current_sha()
        self._save_state(options.state_path, final_sha)
        status = "generated" if generated_reports else "reused"
        return PodcastHookResult(
            status=status,
            generated_reports=generated_reports,
            reused_reports=reused_reports,
            audio_paths=audio_paths,
            start_sha=str(last_seen_sha),
            final_sha=final_sha,
        )

    @staticmethod
    def _load_state(state_path: Path) -> dict[str, object]:
        if not state_path.exists():
            return {}
        return json.loads(state_path.read_text(encoding="utf-8"))

    @staticmethod
    def _save_state(state_path: Path, last_seen_sha: str) -> None:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(
            json.dumps({"last_seen_sha": last_seen_sha}, indent=2, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
