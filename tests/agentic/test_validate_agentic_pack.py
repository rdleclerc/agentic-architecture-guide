from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "scripts" / "validate_agentic_pack.py"
spec = importlib.util.spec_from_file_location("validate_agentic_pack", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def bundle_entry(path: str, payload: str) -> str:
    encoded = payload.encode("utf-8")
    sha = hashlib.sha256(encoded).hexdigest()
    trailing = "true" if payload.endswith("\n") else "false"
    return (
        f'<!-- AGENTIC_BUNDLE_FILE_START path="{path}" sha256="{sha}" '
        f'bytes="{len(encoded)}" trailing_newline="{trailing}" -->\n'
        "````````\n"
        f"{payload}"
        "````````\n"
        f'<!-- AGENTIC_BUNDLE_FILE_END path="{path}" -->\n'
    )


def write_minimal_valid_pack(root: Path) -> None:
    files = {
        "AGENTS.md": "# AGENTS\nLoad `docs/evals.md`.\n",
        "README.md": "# Pack\nSee `docs/evals.md`.\n",
        "CLAUDE.md": "# Adapter\nSee `docs/evals.md`.\n",
        ".github/pull_request_template.md": "- [ ] Ran `docs/evals.md` checks.\n",
        "docs/evals.md": "# Evals\n",
        ".agentic/skill_registry.yaml": (
            "canonical_root: skills\n"
            "adapter_roots:\n"
            "  claude: .claude/skills\n"
            "  codex: .codex/skills\n"
            "skills:\n"
            "  - name: build-agent-eval\n"
            "    description: Build evals.\n"
            "    path: skills/build-agent-eval/SKILL.md\n"
            "    adapter_paths:\n"
            "      claude: .claude/skills/build-agent-eval/SKILL.md\n"
            "      codex: .codex/skills/build-agent-eval/SKILL.md\n"
        ),
        ".agentic/eval_matrix.yaml": (ROOT / ".agentic" / "eval_matrix.yaml").read_text(encoding="utf-8"),
        "tests/agentic/behavior_fixtures.json": (ROOT / "tests" / "agentic" / "behavior_fixtures.json").read_text(encoding="utf-8"),
        "skills/build-agent-eval/SKILL.md": "# Build Agent Eval\n",
        ".claude/skills/build-agent-eval/SKILL.md": "# Build Agent Eval\n",
        ".codex/skills/build-agent-eval/SKILL.md": "# Build Agent Eval\n",
    }
    for rel_path, payload in files.items():
        out = root / rel_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
    bundle = "# Single-file test bundle\n\n" + "\n".join(bundle_entry(path, payload) for path, payload in files.items())
    (root / "agentic_architecture_singlefile.md").write_text(bundle, encoding="utf-8")


class ValidatorUnitTests(unittest.TestCase):
    def test_live_eval_matrix_covers_required_behavior_categories(self) -> None:
        cases = validator.parse_eval_cases(ROOT / ".agentic" / "eval_matrix.yaml")
        categories = {case.fields.get("category") for case in cases}
        self.assertTrue(validator.REQUIRED_COVERAGE_CATEGORIES <= categories)
        for case in cases:
            self.assertFalse(validator.REQUIRED_EVAL_FIELDS - case.fields.keys(), case.id)
            self.assertIsInstance(case.fields.get("expected"), dict)
            self.assertTrue(case.fields.get("expected"), case.id)

    def test_behavior_fixture_matches_eval_matrix_cases(self) -> None:
        matrix_case_ids = {case.id for case in validator.parse_eval_cases(ROOT / ".agentic" / "eval_matrix.yaml")}
        fixture = json.loads((ROOT / "tests" / "agentic" / "behavior_fixtures.json").read_text(encoding="utf-8"))
        fixture_ids = {case["id"] for case in fixture["cases"]}
        self.assertTrue(validator.REQUIRED_COVERAGE_CATEGORIES <= fixture_ids)
        for case in fixture["cases"]:
            self.assertIn(case["eval_matrix_case"], matrix_case_ids)
            self.assertTrue(case["expected_trace"])
            self.assertTrue(case["must_not"])

    def test_validator_passes_minimal_valid_pack(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_valid_pack(root)
            report = validator.validate(root)
            self.assertEqual(report.errors, [])

    def test_validator_fails_embedded_only_doc(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_valid_pack(root)
            hidden_doc = "# Hidden\n"
            single = root / "agentic_architecture_singlefile.md"
            single.write_text(single.read_text(encoding="utf-8") + bundle_entry("docs/hidden.md", hidden_doc), encoding="utf-8")
            report = validator.validate(root)
            self.assertTrue(any("embedded-only bundle docs" in error for error in report.errors))

    def test_validator_fails_missing_skill_registry_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_valid_pack(root)
            (root / "skills" / "build-agent-eval" / "SKILL.md").unlink()
            report = validator.validate(root)
            self.assertTrue(any("skill registry paths are missing" in error for error in report.errors))

    def test_validator_fails_skill_adapter_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_minimal_valid_pack(root)
            (root / ".claude" / "skills" / "build-agent-eval" / "SKILL.md").write_text("# Forked doctrine\n", encoding="utf-8")
            report = validator.validate(root)
            self.assertTrue(any("skill adapter paths drift" in error for error in report.errors))


if __name__ == "__main__":
    unittest.main()
