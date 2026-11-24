#!/usr/bin/env python3
"""Write one original one-line cat joke to /output/entry.txt.

No arguments. Deterministic: the same line every run, with no trailing
newline, so the output is byte-identical across runs.
"""

import os
import sys

JOKE = (
    "I bought my cat a bed, a tower, and a heated blanket \u2014 "
    "she sleeps in the box, on my keyboard, and on my last nerve."
)


def main() -> int:
    # Gate self-check: mirror the competition gate before writing.
    # Exactly one line, 1-200 characters, not only whitespace.
    if not (1 <= len(JOKE) <= 200):
        print(f"gate failed: joke is {len(JOKE)} chars, need 1-200",
              file=sys.stderr)
        return 1
    if JOKE.strip() == "" or "\n" in JOKE or "\r" in JOKE:
        print("gate failed: joke must be a single non-blank line",
              file=sys.stderr)
        return 1
    if JOKE != JOKE.strip():
        print("gate failed: joke must not start or end with whitespace",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))  # no trailing newline

    # Verify what was actually written, not just what we meant to write.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != JOKE:
        print("gate failed: written output differs from joke",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
