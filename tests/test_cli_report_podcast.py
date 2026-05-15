from __future__ import annotations

from pathlib import Path

import pytest

from eliezer_weekly_roundup import cli
from eliezer_weekly_roundup.cli import build_parser


def test_build_parser_parses_generate_podcast_command(tmp_path: Path) -> None:
    parser = build_parser()

    args = parser.parse_args(
        [
            "generate-podcast",
            str(tmp_path / "roundups" / "2026-04-21.md"),
            "--push",
            "--instructions",
            "make it engaging",
            "--language",
            "en",
            "--audio-format",
            "brief",
            "--audio-length",
            "long",
            "--timeout-seconds",
            "900",
        ]
    )

    assert args.command == "generate-podcast"
    assert args.push is True
    assert args.instructions == "make it engaging"
    assert args.language == "en"
    assert args.audio_format == "brief"
    assert args.audio_length == "long"
    assert args.timeout_seconds == 900


def test_build_parser_parses_process_podcast_hook_command(tmp_path: Path) -> None:
    parser = build_parser()

    args = parser.parse_args(
        [
            "process-podcast-hook",
            "--state-path",
            str(tmp_path / "state.json"),
            "--timeout-seconds",
            "1800",
            "--max-reports",
            "2",
        ]
    )

    assert args.command == "process-podcast-hook"
    assert args.state_path == tmp_path / "state.json"
    assert args.timeout_seconds == 1800
    assert args.max_reports == 2


def test_main_returns_actionable_message_when_notebooklm_auth_is_missing(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    tmp_path: Path,
) -> None:
    async def fake_run_generate_podcast(args: object) -> int:
        raise FileNotFoundError(
            "Storage file not found: /tmp/notebooklm/storage_state.json"
        )

    monkeypatch.setattr(cli, "_run_generate_podcast", fake_run_generate_podcast)
    monkeypatch.setattr(
        cli,
        "build_parser",
        lambda: build_parser(),
    )
    monkeypatch.setattr(
        "sys.argv",
        [
            "eliezer-roundup",
            "generate-podcast",
            str(tmp_path / "roundups" / "2026-04-21.md"),
        ],
    )

    exit_code = cli.main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "notebooklm login" in captured.err
    assert "storage_state.json" in captured.err
