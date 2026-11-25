#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Word for Your Wi-Fi — writes the entry word to /output/entry.txt.

The word is "Connected-ish": the phone proudly says Connected while
nothing loads — the most recognisable home Wi-Fi moment there is.
"""

import os

WORD = "Connected-ish"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(word: str) -> None:
    """Fail loudly rather than emit an entry the sealed gate would refuse."""
    assert word == word.strip() and word, "word must be non-blank"
    assert " " not in word, "entry must be a single word"
    assert 1 <= len(word) <= 20, "gate allows 1 to 20 characters"


def main() -> None:
    check_gate(WORD)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
