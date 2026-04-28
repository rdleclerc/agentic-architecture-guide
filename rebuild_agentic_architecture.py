#!/usr/bin/env python3
"""
Rebuild the multifile agentic architecture pack from the single Markdown source.

Usage:
  python rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack
  python rebuild_agentic_architecture.py agentic_architecture_singlefile.md ./agentic_architecture_pack --overwrite
"""
from pathlib import Path
import argparse
import hashlib
import re

START_RE = re.compile(
    r'<!-- AGENTIC_BUNDLE_FILE_START path="([^"]+)" sha256="([a-f0-9]{64})" bytes="(\d+)" trailing_newline="(true|false)" -->'
)
DIR_RE = re.compile(r'<!-- AGENTIC_BUNDLE_DIR path="([^"]+)" -->')
FENCE_RE = re.compile(r'^`{8,}|^~{8,}')


def extract_fenced_payload(block: str, trailing_newline: bool) -> str:
    lines = block.splitlines(keepends=True)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines or not FENCE_RE.match(lines[0].strip()):
        raise ValueError("Missing opening long fence for payload")
    fence = lines.pop(0).strip().split()[0]
    if not lines or lines[-1].strip() != fence:
        raise ValueError("Missing closing long fence for payload")
    lines.pop()
    payload = "".join(lines)
    if not trailing_newline and payload.endswith("\n"):
        payload = payload[:-1]
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("single_file", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    source = args.single_file.read_text(encoding="utf-8")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for match in DIR_RE.finditer(source):
        (args.out_dir / match.group(1)).mkdir(parents=True, exist_ok=True)

    count = 0
    for match in START_RE.finditer(source):
        path = match.group(1)
        expected_sha = match.group(2)
        expected_bytes = int(match.group(3))
        trailing_newline = match.group(4) == "true"
        end_marker = f'<!-- AGENTIC_BUNDLE_FILE_END path="{path}" -->'
        end_index = source.find(end_marker, match.end())
        if end_index == -1:
            raise ValueError(f"Missing end marker for {path}")
        payload = extract_fenced_payload(source[match.end():end_index], trailing_newline)
        actual_bytes = len(payload.encode("utf-8"))
        actual_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        if actual_bytes != expected_bytes or actual_sha != expected_sha:
            raise ValueError(
                f"Payload mismatch for {path}: bytes {actual_bytes}/{expected_bytes}, sha {actual_sha}/{expected_sha}"
            )
        out_path = args.out_dir / path
        if out_path.exists() and not args.overwrite:
            raise FileExistsError(f"Refusing to overwrite existing file: {out_path}")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
        count += 1

    print(f"Rebuilt {count} files into {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
