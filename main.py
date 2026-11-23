#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner describing a hilariously useless
superpower to /output/entry.txt. The line is fixed text: the whole entry
is the joke, so the program's only job is to deliver it byte-exact.
"""

import os
from pathlib import Path

LINE = "I can fly, but only downwards, and only once."


def validate(text: str) -> str:
    """Return the line if it passes the gate, else raise."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not cleaned.strip():
        raise ValueError("entry must not be only whitespace")
    return cleaned


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(validate(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
