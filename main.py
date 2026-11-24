#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry.

Writes one original cat joke — a single line under 200 characters —
to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "My cat only cuddles me when I'm holding food — our whole "
    "relationship is a hostage negotiation, and I keep losing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
