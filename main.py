#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os

JOKE = "The printer jammed again on deadline day, so I printed my resignation: the only document it's ever run without a single complaint."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
