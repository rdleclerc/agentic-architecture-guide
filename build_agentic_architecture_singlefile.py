#!/usr/bin/env python3
"""Build the single-file handoff from the canonical live multifile guide.

The live repo is the source of truth. This script regenerates only the
repo-tree, bundle-manifest, and embedded-payload sections of
agentic_architecture_singlefile.md while preserving the architecture prose and
reference-source sections around them.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_SINGLE_FILE = ROOT / "agentic_architecture_singlefile.md"
FENCE = "````````"

ROOT_FILES = [
    ".gitignore",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "build_agentic_architecture_singlefile.py",
    "rebuild_agentic_architecture.py",
    ".github/pull_request_template.md",
]

GLOB_PATTERNS = [
    ".agentic/*.yaml",
    "docs/*.md",
    "skills/*/SKILL.md",
    ".claude/skills/*/SKILL.md",
    ".codex/skills/*/SKILL.md",
    "scripts/*.py",
    "tests/**/*.py",
    "tests/**/*.json",
]

SKIP_NAMES = {"__pycache__"}


def canonical_bundle_paths(root: Path = ROOT) -> list[str]:
    paths: set[str] = set()
    for rel in ROOT_FILES:
        if (root / rel).exists():
            paths.add(rel)
    for pattern in GLOB_PATTERNS:
        for path in root.glob(pattern):
            if any(part in SKIP_NAMES for part in path.parts):
                continue
            if path.is_file() or path.is_symlink():
                paths.add(path.relative_to(root).as_posix())
    return sorted(paths)


def read_payload(path: Path) -> str:
    # read_text follows symlinks. That is intentional: runtime-specific adapter
    # skill files are derived surfaces; the bundle may reconstruct them as
    # copies if the target filesystem cannot preserve symlinks.
    return path.read_text(encoding="utf-8")


def file_metadata(payload: str) -> tuple[int, str, bool]:
    encoded = payload.encode("utf-8")
    return len(encoded), hashlib.sha256(encoded).hexdigest(), payload.endswith("\n")


def render_tree(paths: list[str]) -> str:
    lines = ["## Repository tree", "", "```text", "."]
    for rel in paths:
        lines.append(f"├── {rel}")
    lines.extend(["```", ""])
    return "\n".join(lines)


def render_manifest(root: Path, paths: list[str]) -> str:
    lines = ["## Bundle manifest", "", "```yaml", "files:"]
    for rel in paths:
        payload = read_payload(root / rel)
        byte_count, sha, trailing_newline = file_metadata(payload)
        lines.extend(
            [
                f"  - path: {rel}",
                f"    bytes: {byte_count}",
                f"    sha256: {sha}",
                f"    trailing_newline: {str(trailing_newline).lower()}",
            ]
        )
    lines.extend(["```", ""])
    return "\n".join(lines)


def render_payloads(root: Path, paths: list[str]) -> str:
    chunks = ["## Embedded file payloads", ""]
    for rel in paths:
        payload = read_payload(root / rel)
        byte_count, sha, trailing_newline = file_metadata(payload)
        chunks.extend(
            [
                f"### File: `{rel}`",
                "",
                (
                    f'<!-- AGENTIC_BUNDLE_FILE_START path="{rel}" sha256="{sha}" '
                    f'bytes="{byte_count}" trailing_newline="{str(trailing_newline).lower()}" -->'
                ),
                FENCE,
                payload.rstrip("\n") if trailing_newline else payload,
                FENCE,
                f'<!-- AGENTIC_BUNDLE_FILE_END path="{rel}" -->',
                "",
            ]
        )
    return "\n".join(chunks).rstrip() + "\n"


def replace_between(source: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    return source[:start] + replacement + source[end:]


def build(source: str, root: Path) -> str:
    paths = canonical_bundle_paths(root)
    generated_middle = render_tree(paths) + "\n" + render_manifest(root, paths) + "\n"

    research_start = source.index("## Research boundary:")
    payload_start = source.index("## Embedded file payloads")
    if research_start < payload_start:
        research_block = source[research_start:payload_start].strip() + "\n"
        source_without_research = source[:research_start] + source[payload_start:]
    else:
        reference_start = source.index("## Reference sources used")
        research_block = source[research_start:reference_start].strip() + "\n"
        source_without_research = source[:research_start] + source[reference_start:]

    before_payload = replace_between(
        source_without_research,
        "## Repository tree",
        "## Embedded file payloads",
        generated_middle,
    )
    payload_index = before_payload.index("## Embedded file payloads")
    return before_payload[:payload_index] + render_payloads(root, paths) + "\n" + research_block


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate agentic_architecture_singlefile.md from live guide files.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Guide repo root.")
    parser.add_argument("--single-file", type=Path, default=DEFAULT_SINGLE_FILE, help="Single-file markdown to update.")
    parser.add_argument("--check", action="store_true", help="Fail if the single-file would change.")
    args = parser.parse_args()

    root = args.root.resolve()
    single_file = args.single_file.resolve()
    source = single_file.read_text(encoding="utf-8")
    rebuilt = build(source, root)
    if args.check:
        if rebuilt != source:
            print(f"{single_file} is not up to date")
            return 1
        print(f"{single_file} is up to date")
        return 0
    single_file.write_text(rebuilt, encoding="utf-8")
    print(f"Regenerated {single_file} with {len(canonical_bundle_paths(root))} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
