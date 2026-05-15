from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
from urllib.parse import parse_qs, urlsplit, urlunsplit

from notebooklm import AudioFormat, AudioLength, NotebookLMClient

AUDIO_BLOCK_START = "<!-- eliezer-roundup:audio:start -->"
AUDIO_BLOCK_END = "<!-- eliezer-roundup:audio:end -->"
AUDIO_BLOCK_PATTERN = re.compile(
    rf"\n?{re.escape(AUDIO_BLOCK_START)}.*?{re.escape(AUDIO_BLOCK_END)}\n?",
    re.DOTALL,
)
URL_PATTERN = re.compile(r"https?://[^\s<>()\]\[]+")
MANIFEST_NAME = ".notebooklm-sync.json"


@dataclass(frozen=True)
class NotebookRecord:
    id: str
    title: str
    created: bool = False


@dataclass(frozen=True)
class SourceRecord:
    id: str
    key: str


@dataclass(frozen=True)
class AudioArtifactRecord:
    id: str
    path: Path


@dataclass(frozen=True)
class ReportDocument:
    path: Path
    relative_path: Path
    title: str
    notebook_title: str
    report_source_title: str
    source_content: str
    source_digest: str
    cited_urls: list[str]
    audio_output_path: Path
    audio_relative_path: Path


@dataclass(frozen=True)
class ReportPodcastOptions:
    push: bool = False
    instructions: str | None = None
    language: str = "en"
    audio_format: str = "deep-dive"
    audio_length: str = "medium"
    timeout_seconds: int = 900


@dataclass(frozen=True)
class ReportPodcastResult:
    report_path: Path
    notebook_id: str
    audio_path: Path
    generated_new_audio: bool


class NotebookGateway(Protocol):
    async def ensure_notebook(
        self,
        title: str,
        preferred_notebook_id: str | None = None,
    ) -> NotebookRecord: ...

    async def replace_report_source(
        self,
        notebook_id: str,
        source_title: str,
        content: str,
        *,
        delete_existing: bool = True,
    ) -> SourceRecord: ...

    async def ensure_url_sources(
        self, notebook_id: str, urls: list[str]
    ) -> list[SourceRecord]: ...

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
    ) -> AudioArtifactRecord: ...


class GitPublisher(Protocol):
    def commit_and_push(
        self, *, repo_root: Path, paths: list[Path], message: str
    ) -> None: ...


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_managed_audio_section(markdown: str) -> str:
    cleaned = AUDIO_BLOCK_PATTERN.sub("\n", markdown)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def normalize_url(url: str) -> str:
    trimmed = url.rstrip(').,]"')
    split = urlsplit(trimmed)
    normalized = split._replace(fragment="")
    return urlunsplit(normalized)


def is_probably_feed_url(url: str) -> bool:
    split = urlsplit(url)
    path = split.path.lower().rstrip("/")
    if path.endswith(("/rss.xml", "/atom.xml", "/feed", "/rss", ".rss", ".atom")):
        return True

    query = parse_qs(split.query)
    for key, values in query.items():
        key_lower = key.lower()
        values_lower = {value.lower() for value in values}
        if key_lower in {"feed", "format", "output", "type"} and values_lower & {
            "rss",
            "atom",
            "xml",
        }:
            return True
    return False


def extract_cited_urls(markdown: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for match in URL_PATTERN.findall(markdown):
        normalized = normalize_url(match)
        if is_probably_feed_url(normalized):
            continue
        if normalized not in seen:
            seen.add(normalized)
            urls.append(normalized)
    return urls


def _extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def parse_report_document(report_path: Path, *, repo_root: Path) -> ReportDocument:
    report_path = report_path.resolve()
    repo_root = repo_root.resolve()
    relative_path = report_path.relative_to(repo_root)
    markdown = _read_text(report_path)
    source_content = strip_managed_audio_section(markdown)
    title = _extract_title(source_content, fallback=report_path.stem)
    source_digest = hashlib.sha256(source_content.encode("utf-8")).hexdigest()
    cited_urls = extract_cited_urls(source_content)
    audio_output_path = report_path.with_suffix(".notebooklm.mp3")
    audio_relative_path = audio_output_path.relative_to(repo_root)
    return ReportDocument(
        path=report_path,
        relative_path=relative_path,
        title=title,
        notebook_title=f"NotebookLM: {title}",
        report_source_title=f"Report Markdown: {relative_path.as_posix()}",
        source_content=source_content,
        source_digest=source_digest,
        cited_urls=cited_urls,
        audio_output_path=audio_output_path,
        audio_relative_path=audio_relative_path,
    )


def upsert_managed_audio_section(
    markdown: str,
    *,
    audio_relative_path: str,
    notebook_title: str,
    notebook_id: str,
) -> str:
    body = strip_managed_audio_section(markdown).rstrip() + "\n\n"
    block = (
        f"{AUDIO_BLOCK_START}\n"
        "## Audio Overview\n"
        f"- NotebookLM notebook: {notebook_title}\n"
        f"- Podcast: [Listen to the generated podcast]({audio_relative_path})\n"
        f"{AUDIO_BLOCK_END}\n"
    )
    return body + block


class SubprocessGitPublisher:
    def commit_and_push(
        self, *, repo_root: Path, paths: list[Path], message: str
    ) -> None:
        unique_paths = []
        seen: set[str] = set()
        for path in paths:
            rel = path.resolve().relative_to(repo_root.resolve()).as_posix()
            if rel not in seen:
                seen.add(rel)
                unique_paths.append(rel)
        if not unique_paths:
            return

        subprocess.run(["git", "add", *unique_paths], cwd=repo_root, check=True)
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet", "--", *unique_paths],
            cwd=repo_root,
            check=False,
        )
        if diff.returncode == 0:
            return
        if diff.returncode != 1:
            raise RuntimeError(
                "Unable to determine whether report assets changed before commit."
            )

        subprocess.run(["git", "commit", "-m", message], cwd=repo_root, check=True)
        current_branch = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        self._push_branch(repo_root=repo_root, current_branch=current_branch)

    def _push_branch(self, *, repo_root: Path, current_branch: str) -> None:
        push_error: subprocess.CalledProcessError | None = None
        for _attempt in range(2):
            try:
                subprocess.run(
                    ["git", "push", "origin", current_branch],
                    cwd=repo_root,
                    check=True,
                )
                return
            except subprocess.CalledProcessError as error:
                push_error = error

        if self._remote_contains_head(
            repo_root=repo_root, current_branch=current_branch
        ):
            return
        if push_error is not None:
            raise push_error

    def _remote_contains_head(self, *, repo_root: Path, current_branch: str) -> bool:
        try:
            subprocess.run(
                ["git", "fetch", "origin", current_branch],
                cwd=repo_root,
                check=True,
            )
        except subprocess.CalledProcessError:
            return False

        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", "HEAD", "FETCH_HEAD"],
            cwd=repo_root,
            check=False,
        )
        return result.returncode == 0


class NotebookLMGatewayAdapter:
    def __init__(self, storage_path: str | None = None) -> None:
        self.storage_path = storage_path

    async def ensure_notebook(
        self,
        title: str,
        preferred_notebook_id: str | None = None,
    ) -> NotebookRecord:
        async with await NotebookLMClient.from_storage(self.storage_path) as client:
            if preferred_notebook_id:
                notebook = await client.notebooks.get(preferred_notebook_id)
                if notebook is not None:
                    return NotebookRecord(id=notebook.id, title=notebook.title)

            notebooks = await client.notebooks.list()
            matches = [notebook for notebook in notebooks if notebook.title == title]
            if len(matches) > 1:
                raise RuntimeError(
                    f"Multiple NotebookLM notebooks matched title: {title}"
                )
            if matches:
                notebook = matches[0]
            else:
                notebook = await client.notebooks.create(title)
                return NotebookRecord(
                    id=notebook.id, title=notebook.title, created=True
                )
            return NotebookRecord(id=notebook.id, title=notebook.title)

    async def replace_report_source(
        self,
        notebook_id: str,
        source_title: str,
        content: str,
        *,
        delete_existing: bool = True,
    ) -> SourceRecord:
        async with await NotebookLMClient.from_storage(self.storage_path) as client:
            if delete_existing:
                existing_sources = await client.sources.list(notebook_id)
                for source in existing_sources:
                    if source.title == source_title:
                        await client.sources.delete(notebook_id, source.id)
            source = await client.sources.add_text(notebook_id, source_title, content)
            await client.sources.wait_until_ready(notebook_id, source.id, timeout=300.0)
            return SourceRecord(id=source.id, key=source_title)

    async def ensure_url_sources(
        self, notebook_id: str, urls: list[str]
    ) -> list[SourceRecord]:
        async with await NotebookLMClient.from_storage(self.storage_path) as client:
            existing_sources = await client.sources.list(notebook_id)
            existing_by_url = {
                normalize_url(source.url): source
                for source in existing_sources
                if source.url
            }
            ensured: list[SourceRecord] = []
            for url in urls:
                existing = existing_by_url.get(url)
                if existing is not None:
                    ensured.append(SourceRecord(id=existing.id, key=url))
                    continue
                source = await client.sources.add_url(
                    notebook_id, url, wait=True, wait_timeout=300.0
                )
                ensured.append(SourceRecord(id=source.id, key=url))
            return ensured

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
        output_path.parent.mkdir(parents=True, exist_ok=True)
        async with await NotebookLMClient.from_storage(self.storage_path) as client:
            status = await client.artifacts.generate_audio(
                notebook_id,
                instructions=instructions,
                language=language,
                audio_format=_coerce_audio_format(audio_format),
                audio_length=_coerce_audio_length(audio_length),
            )
            completed = await client.artifacts.wait_for_completion(
                notebook_id,
                status.task_id,
                timeout=float(timeout_seconds),
            )
            artifact_id = None
            if completed.metadata:
                artifact_id = completed.metadata.get("artifact_id")
            if artifact_id is None:
                audio_artifacts = await client.artifacts.list_audio(notebook_id)
                completed_artifacts = [
                    artifact for artifact in audio_artifacts if artifact.is_completed
                ]
                if not completed_artifacts:
                    raise RuntimeError(
                        "NotebookLM did not expose a completed audio artifact after generation."
                    )
                artifact = max(
                    completed_artifacts,
                    key=lambda candidate: candidate.created_at or 0,
                )
                artifact_id = artifact.id
            await client.artifacts.download_audio(
                notebook_id, str(output_path), artifact_id=artifact_id
            )
            return AudioArtifactRecord(id=artifact_id, path=output_path)


def _coerce_audio_format(value: str) -> AudioFormat:
    mapping = {
        "deep-dive": AudioFormat.DEEP_DIVE,
        "brief": AudioFormat.BRIEF,
        "critique": AudioFormat.CRITIQUE,
        "debate": AudioFormat.DEBATE,
    }
    try:
        return mapping[value]
    except KeyError as error:
        raise ValueError(f"Unsupported audio format: {value}") from error


def _coerce_audio_length(value: str) -> AudioLength:
    mapping = {
        "short": AudioLength.SHORT,
        "medium": AudioLength.DEFAULT,
        "default": AudioLength.DEFAULT,
        "long": AudioLength.LONG,
    }
    try:
        return mapping[value]
    except KeyError as error:
        raise ValueError(f"Unsupported audio length: {value}") from error


class ReportPodcastService:
    def __init__(
        self,
        *,
        repo_root: Path,
        gateway: NotebookGateway,
        git_publisher: GitPublisher | None = None,
    ) -> None:
        self.repo_root = repo_root.resolve()
        self.gateway = gateway
        self.git_publisher = git_publisher or SubprocessGitPublisher()
        self.manifest_path = self.repo_root / MANIFEST_NAME

    async def generate_podcast(
        self,
        report_path: Path,
        options: ReportPodcastOptions,
    ) -> ReportPodcastResult:
        report = parse_report_document(report_path, repo_root=self.repo_root)
        manifest = self._load_manifest()
        reports = manifest.setdefault("reports", {})
        manifest_entry = reports.get(report.relative_path.as_posix())

        if (
            manifest_entry
            and manifest_entry.get("source_digest") == report.source_digest
            and report.audio_output_path.exists()
        ):
            notebook_title = manifest_entry.get("notebook_title", report.notebook_title)
            notebook_id = manifest_entry.get("notebook_id", "unknown")
            updated_markdown = upsert_managed_audio_section(
                _read_text(report.path),
                audio_relative_path=report.audio_output_path.relative_to(
                    report.path.parent
                ).as_posix(),
                notebook_title=notebook_title,
                notebook_id=notebook_id,
            )
            self._write_text_if_changed(report.path, updated_markdown)
            return ReportPodcastResult(
                report_path=report.path,
                notebook_id=notebook_id,
                audio_path=report.audio_output_path,
                generated_new_audio=False,
            )

        notebook = await self.gateway.ensure_notebook(
            report.notebook_title,
            preferred_notebook_id=None
            if manifest_entry is None
            else manifest_entry.get("notebook_id"),
        )
        report_source = await self.gateway.replace_report_source(
            notebook.id,
            report.report_source_title,
            report.source_content,
            delete_existing=not notebook.created,
        )
        url_sources = await self.gateway.ensure_url_sources(
            notebook.id, report.cited_urls
        )
        audio_artifact = await self.gateway.generate_audio_overview(
            notebook.id,
            report.audio_output_path,
            instructions=options.instructions,
            language=options.language,
            audio_format=options.audio_format,
            audio_length=options.audio_length,
            timeout_seconds=options.timeout_seconds,
        )

        updated_markdown = upsert_managed_audio_section(
            _read_text(report.path),
            audio_relative_path=report.audio_output_path.relative_to(
                report.path.parent
            ).as_posix(),
            notebook_title=notebook.title,
            notebook_id=notebook.id,
        )
        self._write_text_if_changed(report.path, updated_markdown)

        reports[report.relative_path.as_posix()] = {
            "report_path": report.relative_path.as_posix(),
            "notebook_id": notebook.id,
            "notebook_title": notebook.title,
            "source_digest": report.source_digest,
            "report_source_id": report_source.id,
            "url_source_ids": [source.id for source in url_sources],
            "audio_artifact_id": audio_artifact.id,
            "audio_path": report.audio_relative_path.as_posix(),
        }
        self._save_manifest(manifest)

        if options.push:
            self.git_publisher.commit_and_push(
                repo_root=self.repo_root,
                paths=[report.path, report.audio_output_path],
                message=f"Add NotebookLM podcast for {report.relative_path.as_posix()}",
            )

        return ReportPodcastResult(
            report_path=report.path,
            notebook_id=notebook.id,
            audio_path=report.audio_output_path,
            generated_new_audio=True,
        )

    def _load_manifest(self) -> dict[str, object]:
        if not self.manifest_path.exists():
            return {"reports": {}}
        return json.loads(_read_text(self.manifest_path))

    def _save_manifest(self, manifest: dict[str, object]) -> None:
        self.manifest_path.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    @staticmethod
    def _write_text_if_changed(path: Path, new_content: str) -> None:
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != new_content:
            path.write_text(new_content, encoding="utf-8")
