from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "openclaw-agentic-skill-creator" / "SKILL.md"


class OpenClawSkillCreatorContractTests(unittest.TestCase):
    def test_keeps_production_contract_and_privacy_boundary(self) -> None:
        body = SKILL.read_text(encoding="utf-8")

        self.assertIn("OpenClaw production contract", body)
        self.assertIn("Keep this contract inline because it is short, safety-critical active context", body)
        self.assertIn("non-skill check", body)
        self.assertIn("direct answer, source note, deterministic script, typed tool", body)
        self.assertIn("should-trigger, should-not-trigger, and near-neighbor prompts", body)
        self.assertIn("required source lanes, tools, memory/context packets, and permissions", body)
        self.assertIn("OpenClaw parity proof receipts", body)
        self.assertIn("source-authority boundary, side-effect boundary, rollback/idempotency rule", body)
        self.assertIn("Scaffold", body)
        self.assertIn("Production", body)
        self.assertIn("Library", body)
        self.assertIn("Governed", body)
        self.assertIn("verification command or OpenClaw session receipt", body)
        self.assertIn("metadata-only and local-first", body)
        self.assertIn("Do not store raw prompts", body)

        section = body.split("> ## OpenClaw production contract", 1)[1].split(
            "A skill for creating new OpenClaw skills", 1
        )[0]
        self.assertLess(len(section.encode("utf-8")), 3000)
        self.assertNotIn("```python", section)
        self.assertNotIn("```sh", section)
        self.assertNotIn("```bash", section)
        self.assertNotIn("```js", section)
        self.assertNotIn("subprocess", section)
        self.assertNotIn("sqlite", section.lower())


if __name__ == "__main__":
    unittest.main()
