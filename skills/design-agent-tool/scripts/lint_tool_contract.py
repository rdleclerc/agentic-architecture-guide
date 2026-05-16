#!/usr/bin/env python3
"""Validate a JSON tool contract for agent-facing affordance basics."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED = [
    "name",
    "model_description",
    "purpose",
    "affordance_bought",
    "when_to_use",
    "when_not_to_use",
    "input_schema",
    "output_schema",
    "side_effect_class",
    "permission_level",
    "idempotency_policy",
    "source_authority_role",
    "error_codes",
    "trace_fields",
    "examples",
    "misuse_examples",
    "eval_cases",
]
SIDE_EFFECTS = {"none", "read", "write", "external_write", "destructive"}
WRITE_CLASSES = {"write", "external_write", "destructive"}


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def validate(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED:
        if key not in contract or not _nonempty(contract[key]):
            errors.append(f"missing_or_empty:{key}")

    side_effect = contract.get("side_effect_class")
    if side_effect not in SIDE_EFFECTS:
        errors.append(f"invalid_side_effect_class:{side_effect!r}")

    if side_effect in WRITE_CLASSES:
        policy = str(contract.get("idempotency_policy") or "").strip().lower()
        if policy in {"", "none", "n/a", "not applicable"}:
            errors.append("write_tool_requires_idempotency_policy")

    for schema_key in ("input_schema", "output_schema"):
        schema = contract.get(schema_key)
        if isinstance(schema, dict) and schema.get("type") != "object":
            errors.append(f"{schema_key}_should_be_object_schema")

    errors.extend(_validate_error_codes(contract.get("error_codes")))
    return errors


def _validate_error_codes(value: Any) -> list[str]:
    if not isinstance(value, list) or not value:
        return ["error_codes_must_be_nonempty_list"]
    errors: list[str] = []
    for idx, item in enumerate(value):
        if not isinstance(item, dict):
            errors.append(f"error_codes[{idx}]_not_object")
            continue
        for key in ("code", "meaning", "agent_next_action"):
            if not _nonempty(item.get(key)):
                errors.append(f"error_codes[{idx}]_missing_{key}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: lint_tool_contract.py <contract.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        contract = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001 - CLI should print concise parse failure.
        print(json.dumps({"status": "error", "errors": [f"invalid_json:{exc}"]}, indent=2))
        return 1
    if not isinstance(contract, dict):
        print(json.dumps({"status": "error", "errors": ["contract_must_be_object"]}, indent=2))
        return 1
    errors = validate(contract)
    status = "ok" if not errors else "error"
    print(json.dumps({"status": status, "errors": errors}, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
