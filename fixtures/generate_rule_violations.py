import argparse
from pathlib import Path


def write_fixtures(output_dir: Path) -> None:
    """Create disposable files that violate common repository style limits."""
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "Bad-Names.py").write_text(
        "def findItem(searchItems):\n    return searchItems\n", encoding="utf-8"
    )
    (output_dir / "oversized_module.py").write_text(
        "".join(f"# generated line {line_number}\n" for line_number in range(501)),
        encoding="utf-8",
    )
    long_function = ["def function_too_long():\n", "    total = 0\n"]
    long_function.extend("    total += 1\n" for _ in range(81))
    long_function.append("    return total\n")
    (output_dir / "oversized_function.py").write_text(
        "".join(long_function), encoding="utf-8"
    )
    (output_dir / "overlong_line.py").write_text(
        "# " + "x" * 140 + "\n", encoding="utf-8"
    )
    (output_dir / "missing_final_newline.py").write_text(
        "value = 'intentionally missing final newline'", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", type=Path)
    write_fixtures(parser.parse_args().output_dir)


if __name__ == "__main__":
    main()
