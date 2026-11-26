#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun bounty entry.

Writes one funny text message from your future self to /output/entry.txt.

The joke: a future self reporting back that the present self finally fixed
one annoying habit (replying "haha" to everything) only to replace it with
a worse one (voice notes). Good-news / bad-news structure, a specific
voice, and a punchline that lands on the last word — no setup needed,
and no broke-or-tired cliche. Kept to 140 chars — stricter than the
kit's 200-char gate — so every word earns its place.
"""

import os

ENTRY = "It's future you. Good news: you stopped replying 'haha' to everything. Bad news: now you only send voice notes. Everyone hates it. Stop."

MAX_CHARS = 140


def validate_entry(text: str) -> str:
    """Check the entry fits the gate: 1-140 chars, one line, no padding."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
