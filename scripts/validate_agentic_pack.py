#!/usr/bin/env python3
"""Validate the agentic architecture guide package without external dependencies.

This is intentionally a small contract checker, not an eval framework. It fails
when the package violates source-authority or behavioral-eval contracts that the
repo claims to teach.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

BUNDLE_START_RE = re.compile(
    r'<!-- AGENTIC_BUNDLE_FILE_START path="([^"]+)" sha256="([a-f0-9]{64})" bytes="(\d+)" trailing_newline="(true|false)" -->'
)
FENCE_RE = re.compile(r"^`{8,}|^~{8,}")
DOC_REF_RE = re.compile(r"(?<![A-Za-z0-9_./-])(docs/[A-Za-z0-9._/-]+\.md)\b")
PATH_LINE_RE = re.compile(r"^\s*path:\s*(.+?)\s*$")
CANONICAL_SKILL_PATH_RE = re.compile(r"^\s{4}path:\s*(.+?)\s*$")
ADAPTER_SKILL_PATH_RE = re.compile(r"^\s{6}(claude|codex):\s*(.+?)\s*$")
CASE_START_RE = re.compile(r"^\s*-\s+id:\s*(\S+)\s*$")
FIELD_RE = re.compile(r"^\s{4}([A-Za-z0-9_]+):\s*(.*?)\s*$")
EXPECTED_FIELD_RE = re.compile(r"^\s{6}([A-Za-z0-9_]+):\s*(.*?)\s*$")

# These are generated/example output paths, not guide source files.
DOC_REFERENCE_ALLOWLIST = {
    "docs/current-agentic-inventory.md",
}

ROOT_REFERENCE_FILES = [
    "AGENTS.md",
    "README.md",
    "CLAUDE.md",
    ".github/pull_request_template.md",
]

EXPECTED_BUNDLE_ROOT_FILES = [
    ".gitignore",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "build_agentic_architecture_singlefile.py",
    "rebuild_agentic_architecture.py",
    ".github/pull_request_template.md",
]
EXPECTED_BUNDLE_GLOBS = [
    ".agentic/*.yaml",
    "docs/*.md",
    "skills/*/SKILL.md",
    ".claude/skills/*/SKILL.md",
    ".codex/skills/*/SKILL.md",
    "scripts/*.py",
    "tests/**/*.py",
    "tests/**/*.json",
]

REQUIRED_EVAL_FIELDS = {"id", "task", "category", "expected"}
REQUIRED_COVERAGE_CATEGORIES = {
    "simplicity_deletion",
    "cli_affordance",
    "parallel_slice",
    "source_authority",
    "side_effect_approval",
}


@dataclass(frozen=True)
class BundlePayload:
    path: str
    payload: str
    sha256: str
    byte_count: int
    trailing_newline: bool


@dataclass(frozen=True)
class EvalCase:
    id: str
    fields: dict[str, object]


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.ok: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def pass_(self, message: str) -> None:
        self.ok.append(message)

    @property
    def passed(self) -> bool:
        return not self.errors


def extract_fenced_payload(block: str, trailing_newline: bool) -> str:
    lines = block.splitlines(keepends=True)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines or not FENCE_RE.match(lines[0].strip()):
        raise ValueError("missing opening long fence for bundle payload")
    fence = lines.pop(0).strip().split()[0]
    if not lines or lines[-1].strip() != fence:
        raise ValueError("missing closing long fence for bundle payload")
    lines.pop()
    payload = "".join(lines)
    if not trailing_newline and payload.endswith("\n"):
        payload = payload[:-1]
    return payload


def read_bundle_payloads(single_file: Path) -> dict[str, BundlePayload]:
    source = single_file.read_text(encoding="utf-8")
    payloads: dict[str, BundlePayload] = {}
    for match in BUNDLE_START_RE.finditer(source):
        rel_path, expected_sha, expected_bytes, trailing_text = match.groups()
        trailing_newline = trailing_text == "true"
        end_marker = f'<!-- AGENTIC_BUNDLE_FILE_END path="{rel_path}" -->'
        end_index = source.find(end_marker, match.end())
        if end_index == -1:
            raise ValueError(f"missing bundle end marker for {rel_path}")
        payload = extract_fenced_payload(source[match.end() : end_index], trailing_newline)
        payloads[rel_path] = BundlePayload(
            path=rel_path,
            payload=payload,
            sha256=expected_sha,
            byte_count=int(expected_bytes),
            trailing_newline=trailing_newline,
        )
    return payloads


def parse_skill_registry_paths(path: Path) -> list[str]:
    paths: list[str] = []
    if not path.exists():
        return paths
    for line in path.read_text(encoding="utf-8").splitlines():
        match = PATH_LINE_RE.match(line)
        if match:
            paths.append(match.group(1).strip().strip('"\''))
    return paths


def parse_skill_registry_skill_paths(path: Path) -> list[tuple[str, list[str]]]:
    """Return canonical skill paths paired with adapter paths.

    This deliberately parses only the small registry shape used in this pack.
    It avoids adding a YAML dependency just to enforce package integrity.
    """
    entries: list[tuple[str, list[str]]] = []
    canonical: str | None = None
    adapters: list[str] = []
    if not path.exists():
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("  - name:"):
            if canonical:
                entries.append((canonical, adapters))
            canonical = None
            adapters = []
            continue
        canonical_match = CANONICAL_SKILL_PATH_RE.match(line)
        if canonical_match:
            canonical = canonical_match.group(1).strip().strip('"\'')
            continue
        adapter_match = ADAPTER_SKILL_PATH_RE.match(line)
        if adapter_match:
            adapters.append(adapter_match.group(2).strip().strip('"\''))
    if canonical:
        entries.append((canonical, adapters))
    return entries


def scalar(value: str) -> object:
    value = value.strip().strip('"\'')
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "[]":
        return []
    return value


def parse_eval_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    current_id: str | None = None
    current: dict[str, object] = {}
    in_expected = False

    def flush() -> None:
        nonlocal current_id, current, in_expected
        if current_id is not None:
            cases.append(EvalCase(current_id, current))
        current_id = None
        current = {}
        in_expected = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        start = CASE_START_RE.match(line)
        if start:
            flush()
            current_id = start.group(1)
            current = {"id": current_id}
            continue
        if current_id is None:
            continue
        field = FIELD_RE.match(line)
        if field:
            key, value = field.groups()
            if key == "expected":
                current["expected"] = {}
                in_expected = True
            else:
                current[key] = scalar(value)
                in_expected = False
            continue
        expected_field = EXPECTED_FIELD_RE.match(line)
        if in_expected and expected_field:
            key, value = expected_field.groups()
            expected = current.setdefault("expected", {})
            if isinstance(expected, dict):
                expected[key] = scalar(value)
    flush()
    return cases


def discover_doc_refs(root: Path) -> set[str]:
    refs: set[str] = set()
    candidates: list[Path] = []
    for rel in ROOT_REFERENCE_FILES:
        path = root / rel
        if path.exists():
            candidates.append(path)
    docs_dir = root / "docs"
    if docs_dir.exists():
        candidates.extend(sorted(docs_dir.glob("*.md")))
    agentic_dir = root / ".agentic"
    if agentic_dir.exists():
        candidates.extend(sorted(agentic_dir.glob("*.yaml")))
    for file_path in candidates:
        text = file_path.read_text(encoding="utf-8")
        for match in DOC_REF_RE.finditer(text):
            refs.add(match.group(1))
    return refs


def expected_bundle_paths(root: Path) -> set[str]:
    paths: set[str] = set()
    for rel_path in EXPECTED_BUNDLE_ROOT_FILES:
        if (root / rel_path).exists():
            paths.add(rel_path)
    for pattern in EXPECTED_BUNDLE_GLOBS:
        for path in root.glob(pattern):
            if "__pycache__" in path.parts:
                continue
            if path.is_file() or path.is_symlink():
                paths.add(path.relative_to(root).as_posix())
    return paths


def check_bundle(root: Path, report: ValidationReport) -> dict[str, BundlePayload]:
    single_file = root / "agentic_architecture_singlefile.md"
    if not single_file.exists():
        report.fail("missing agentic_architecture_singlefile.md")
        return {}
    try:
        payloads = read_bundle_payloads(single_file)
    except Exception as exc:  # noqa: BLE001 - diagnostic script should report all parsing failures cleanly.
        report.fail(f"could not parse single-file bundle: {exc}")
        return {}
    if not payloads:
        report.fail("single-file bundle contains no AGENTIC_BUNDLE_FILE_START payloads")
        return {}

    hash_failures = []
    live_mismatches = []
    embedded_only_docs = []
    for rel_path, bundle in payloads.items():
        payload_bytes = bundle.payload.encode("utf-8")
        actual_sha = hashlib.sha256(payload_bytes).hexdigest()
        if actual_sha != bundle.sha256 or len(payload_bytes) != bundle.byte_count:
            hash_failures.append(rel_path)
        live_path = root / rel_path
        if live_path.exists():
            live_text = live_path.read_text(encoding="utf-8")
            if live_text != bundle.payload:
                live_mismatches.append(rel_path)
        elif rel_path.startswith("docs/") and rel_path.endswith(".md"):
            embedded_only_docs.append(rel_path)
    if hash_failures:
        report.fail("bundle payload metadata mismatch: " + ", ".join(sorted(hash_failures)))
    else:
        report.pass_(f"bundle payload metadata valid for {len(payloads)} files")
    if live_mismatches:
        report.fail("bundle payloads differ from live files: " + ", ".join(sorted(live_mismatches)))
    else:
        report.pass_("bundle payloads match all live files present in the bundle")
    if embedded_only_docs:
        report.fail("embedded-only bundle docs are not materialized: " + ", ".join(sorted(embedded_only_docs)))
    else:
        report.pass_("all bundled docs are materialized as live files")
    missing_from_bundle = sorted(expected_bundle_paths(root) - set(payloads))
    if missing_from_bundle:
        report.fail("live canonical files are missing from single-file bundle: " + ", ".join(missing_from_bundle))
    else:
        report.pass_("single-file bundle includes all expected live canonical files")
    return payloads


def check_doc_refs(root: Path, report: ValidationReport) -> None:
    refs = discover_doc_refs(root)
    missing = sorted(ref for ref in refs if ref not in DOC_REFERENCE_ALLOWLIST and not (root / ref).exists())
    if missing:
        report.fail("referenced docs are missing: " + ", ".join(missing))
    else:
        report.pass_(f"referenced docs exist ({len(refs)} references checked; {len(DOC_REFERENCE_ALLOWLIST)} allowlisted examples)")


def check_skill_registry(root: Path, report: ValidationReport) -> None:
    registry_path = root / ".agentic" / "skill_registry.yaml"
    entries = parse_skill_registry_skill_paths(registry_path)
    paths = sorted({path for canonical, adapters in entries for path in [canonical, *adapters]})
    if not entries:
        paths = parse_skill_registry_paths(registry_path)
    if not paths:
        report.fail("skill registry has no path entries")
        return
    missing = sorted(path for path in paths if not (root / path).exists())
    adapter_drift: list[str] = []
    for canonical, adapters in entries:
        canonical_path = root / canonical
        if not canonical_path.exists():
            continue
        canonical_text = canonical_path.read_text(encoding="utf-8")
        for adapter in adapters:
            adapter_path = root / adapter
            if adapter_path.exists() and adapter_path.read_text(encoding="utf-8") != canonical_text:
                adapter_drift.append(f"{adapter} != {canonical}")
    if missing:
        report.fail("skill registry paths are missing: " + ", ".join(missing))
    elif adapter_drift:
        report.fail("skill adapter paths drift from canonical skills: " + ", ".join(sorted(adapter_drift)))
    else:
        report.pass_(f"skill registry paths exist and adapters match canonical skills ({len(paths)} paths)")


def check_eval_matrix(root: Path, report: ValidationReport) -> None:
    matrix_path = root / ".agentic" / "eval_matrix.yaml"
    if not matrix_path.exists():
        report.fail("missing .agentic/eval_matrix.yaml")
        return
    try:
        cases = parse_eval_cases(matrix_path)
    except Exception as exc:  # noqa: BLE001
        report.fail(f"could not parse eval matrix: {exc}")
        return
    if not cases:
        report.fail("eval matrix has no cases")
        return

    duplicate_ids = sorted({case.id for case in cases if [c.id for c in cases].count(case.id) > 1})
    if duplicate_ids:
        report.fail("duplicate eval case ids: " + ", ".join(duplicate_ids))

    missing_fields: list[str] = []
    empty_expected: list[str] = []
    fixture_missing: list[str] = []
    categories: set[str] = set()
    for case in cases:
        missing = sorted(field for field in REQUIRED_EVAL_FIELDS if field not in case.fields)
        if missing:
            missing_fields.append(f"{case.id} missing {','.join(missing)}")
        expected = case.fields.get("expected")
        if not isinstance(expected, dict) or not expected:
            empty_expected.append(case.id)
        category = case.fields.get("category")
        if isinstance(category, str) and category:
            categories.add(category)
        fixture = case.fields.get("fixture")
        if isinstance(fixture, str) and fixture:
            fixture_path = fixture.split("#", 1)[0]
            if not (root / fixture_path).exists():
                fixture_missing.append(f"{case.id}->{fixture}")
    if missing_fields:
        report.fail("eval cases missing required fields: " + "; ".join(missing_fields))
    if empty_expected:
        report.fail("eval cases missing non-empty expected maps: " + ", ".join(sorted(empty_expected)))
    missing_categories = sorted(REQUIRED_COVERAGE_CATEGORIES - categories)
    if missing_categories:
        report.fail("eval matrix missing required behavior categories: " + ", ".join(missing_categories))
    if fixture_missing:
        report.fail("eval cases reference missing fixtures: " + ", ".join(sorted(fixture_missing)))
    if not (missing_fields or empty_expected or missing_categories or fixture_missing or duplicate_ids):
        report.pass_(f"eval matrix valid ({len(cases)} cases; required behavior categories covered)")


def check_behavior_fixture(root: Path, report: ValidationReport) -> None:
    fixture_path = root / "tests" / "agentic" / "behavior_fixtures.json"
    if not fixture_path.exists():
        report.fail("missing tests/agentic/behavior_fixtures.json")
        return
    try:
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.fail(f"behavior fixture is invalid JSON: {exc}")
        return
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        report.fail("behavior fixture must contain non-empty cases list")
        return
    by_id = {}
    fixture_errors: list[str] = []
    for case in cases:
        if not isinstance(case, dict):
            fixture_errors.append("non-object case")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            fixture_errors.append("case without id")
            continue
        by_id[case_id] = case
        for field in ["prompt", "expected_trace", "must_not"]:
            value = case.get(field)
            if field == "prompt" and not isinstance(value, str):
                fixture_errors.append(f"{case_id} missing prompt string")
            if field in {"expected_trace", "must_not"} and not isinstance(value, list):
                fixture_errors.append(f"{case_id} missing {field} list")
    missing_fixture_categories = sorted(REQUIRED_COVERAGE_CATEGORIES - set(by_id))
    if missing_fixture_categories:
        fixture_errors.append("missing fixture ids/categories: " + ", ".join(missing_fixture_categories))
    if fixture_errors:
        report.fail("behavior fixture contract failures: " + "; ".join(fixture_errors))
    else:
        report.pass_(f"behavior fixture valid ({len(cases)} cases)")


def validate(root: Path) -> ValidationReport:
    report = ValidationReport()
    check_bundle(root, report)
    check_doc_refs(root, report)
    check_skill_registry(root, report)
    check_eval_matrix(root, report)
    check_behavior_fixture(root, report)
    return report


def print_report(report: ValidationReport) -> None:
    for message in report.ok:
        print(f"PASS: {message}")
    for message in report.warnings:
        print(f"WARN: {message}")
    for message in report.errors:
        print(f"FAIL: {message}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate agentic architecture guide package integrity.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Guide repo root. Defaults to the parent of this script directory.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    report = validate(args.root.resolve())
    print_report(report)
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
