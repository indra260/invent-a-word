"""Invent a Word We Need — entry program.

Writes the competition entry, one newly coined English word with a
one-line definition of at most 140 characters, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set, for
local testing). Python 3.13 standard library only; deterministic,
no network access, no randomness.

The entry is written with no trailing newline, so the file holds
exactly the entry text and nothing else — the gate counts characters,
and a stray newline would count against the 140-character limit.
"""

import os
import sys

ENTRY_TEXT = (
    "pocketpat (n.) the frantic pat-down of every pocket for phone, keys "
    "and wallet before you can leave the house."
)
MAX_CHARS = 140


def main() -> int:
    text = ENTRY_TEXT
    if not text or not text.strip():
        print("entry text must not be empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"entry is {len(text)} characters, over the {MAX_CHARS}-character gate",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
