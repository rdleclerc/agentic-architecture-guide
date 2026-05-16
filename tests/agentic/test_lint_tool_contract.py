from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINTER = ROOT / "skills" / "design-agent-tool" / "scripts" / "lint_tool_contract.py"


def valid_contract() -> dict:
    return {
        "name": "read_source_artifact",
        "model_description": "Read a raw source artifact by id. Use for evidence inspection, not final editorial judgment.",
        "purpose": "Return raw source text and provenance for an existing artifact.",
        "affordance_bought": "Lets the agent inspect source evidence before synthesizing or deciding.",
        "when_to_use": ["Need raw source evidence"],
        "when_not_to_use": ["Need to decide whether to publish"],
        "input_schema": {"type": "object", "required": ["artifact_id"], "properties": {"artifact_id": {"type": "string"}}},
        "output_schema": {"type": "object", "required": ["artifact_id", "source_role"], "properties": {}},
        "side_effect_class": "read",
        "permission_level": "workspace read",
        "idempotency_policy": "read-only; no mutation",
        "source_authority_role": "raw_evidence",
        "error_codes": [{"code": "NOT_FOUND", "meaning": "No artifact exists", "agent_next_action": "ask for a valid artifact id or search artifacts"}],
        "trace_fields": ["tool_call_id", "actor", "artifact_id", "started_at", "duration_ms"],
        "examples": [{"input": {"artifact_id": "src_1"}, "output": {"artifact_id": "src_1"}, "why": "read evidence"}],
        "misuse_examples": [{"input": {"artifact_id": "src_1"}, "rejection": "does not decide publish", "why": "judgment belongs to agent/editor"}],
        "eval_cases": [{"name": "read raw evidence", "prompt": "inspect src_1", "expected_tool_call": {"artifact_id": "src_1"}}],
    }


def test_lint_tool_contract_accepts_complete_read_contract(tmp_path: Path) -> None:
    path = tmp_path / "contract.json"
    path.write_text(json.dumps(valid_contract()))
    result = subprocess.run([sys.executable, str(LINTER), str(path)], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["status"] == "ok"


def test_lint_tool_contract_rejects_write_without_idempotency(tmp_path: Path) -> None:
    contract = valid_contract()
    contract["side_effect_class"] = "external_write"
    contract["idempotency_policy"] = "none"
    path = tmp_path / "contract.json"
    path.write_text(json.dumps(contract))
    result = subprocess.run([sys.executable, str(LINTER), str(path)], text=True, capture_output=True, check=False)
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert "write_tool_requires_idempotency_policy" in payload["errors"]


def test_lint_tool_contract_rejects_unhelpful_error_codes(tmp_path: Path) -> None:
    contract = valid_contract()
    contract["error_codes"] = [{"code": "FAILED", "meaning": "failed"}]
    path = tmp_path / "contract.json"
    path.write_text(json.dumps(contract))
    result = subprocess.run([sys.executable, str(LINTER), str(path)], text=True, capture_output=True, check=False)
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert "error_codes[0]_missing_agent_next_action" in payload["errors"]
