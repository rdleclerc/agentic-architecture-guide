from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "openclaw-agentic-skill-creator" / "SKILL.md"


class OpenClawSkillCreatorContractTests(unittest.TestCase):
    def test_keeps_production_contract_and_privacy_boundary(self) -> None:
        body = SKILL.read_text(encoding="utf-8")

        self.assertIn("## OpenClaw Production Contract", body)
        self.assertIn("smallest useful non-skill check", body)
        self.assertIn("direct answer, source note, typed tool, source-lane contract, deterministic script", body)
        self.assertIn("should-trigger, should-not-trigger, and near-neighbor prompts", body)
        self.assertIn(
            "required source lanes, tools, memory/context packets, permissions, and live-data access",
            body,
        )
        self.assertIn("live-safe OpenClaw proof receipts", body)
        self.assertIn("source-authority boundary", body)
        self.assertIn("side-effect boundary", body)
        self.assertIn("rollback/idempotency rule", body)
        self.assertIn("Scaffold", body)
        self.assertIn("Production", body)
        self.assertIn("Library", body)
        self.assertIn("Governed", body)
        self.assertIn("metadata-only and local-first", body)
        self.assertIn("Do not store raw prompts", body)

        section = body.split("## OpenClaw Production Contract", 1)[1].split("## Affordance And Proof Rules", 1)[0]
        self.assertLess(len(section.encode("utf-8")), 3000)
        self.assertNotIn("```python", section)
        self.assertNotIn("```sh", section)
        self.assertNotIn("```bash", section)
        self.assertNotIn("```js", section)
        self.assertNotIn("subprocess", section)
        self.assertNotIn("sqlite", section.lower())


if __name__ == "__main__":
    unittest.main()
