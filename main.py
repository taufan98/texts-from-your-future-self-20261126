#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun bounty entry.

Writes one funny text message from your future self to /output/entry.txt.
"""

import os

ENTRY = "It's future you. Good news: you stopped replying 'haha' to everything. Bad news: now you only send voice notes. Everyone hates it. Stop."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
