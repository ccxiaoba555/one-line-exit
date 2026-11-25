"""The One-Line Exit — a one-line resignation letter for make.fun.

A night guard at a wax museum resigns in exactly one line. The program
writes that single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), self-checks the gate (UTF-8, 1 to 140 characters, exactly one
line, not only whitespace) and reads the file back to verify it.

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE = (
    "Dear boss, I resign as night guard at the wax museum: "
    "the figures started clocking in early, "
    "and last night one handed me this letter."
)

MAX_CHARS = 140


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == len(text), "read-back length mismatch"
    print(f"wrote {len(text)} chars to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
