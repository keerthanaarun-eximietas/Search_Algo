import tempfile
import unittest
from pathlib import Path

from fixtures.generate_rule_violations import write_fixtures


class RuleViolationFixtureTests(unittest.TestCase):
    def test_generator_creates_each_requested_violation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            write_fixtures(output_dir)

            self.assertTrue((output_dir / "Bad-Names.py").exists())
            oversized_module = (output_dir / "oversized_module.py").read_text(
                encoding="utf-8"
            )
            self.assertGreater(len(oversized_module.splitlines()), 500)
            long_function = (output_dir / "oversized_function.py").read_text(
                encoding="utf-8"
            )
            self.assertGreater(long_function.count("\n"), 80)
            overlong_line = (output_dir / "overlong_line.py").read_text(
                encoding="utf-8"
            )
            self.assertGreater(len(overlong_line.splitlines()[0]), 120)
            missing_newline = (output_dir / "missing_final_newline.py").read_bytes()
            self.assertFalse(missing_newline.endswith(b"\n"))


if __name__ == "__main__":
    unittest.main()
