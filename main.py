"""Museum of the Year 3000 — one museum label from the year 3000.

Writes the chosen label to /output/entry.txt: exactly one line, no
trailing newline, 1-200 characters of UTF-8 text.
"""

import os

LINE = (
    "Toothbrush, c. 2022. Miniature broom with which citizens scrubbed "
    "their mouth-bones twice daily, then replaced each season as ritual "
    "demanded."
)


def main() -> None:
    # Self-check: one line, 1-200 characters, non-blank.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry length {len(LINE)} out of range"
    assert LINE.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Round-trip check: what landed on disk must be exactly the line —
    # same text, same byte length, still a single line with no newline.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch in /output/entry.txt"
    assert len(written.encode("utf-8")) == len(LINE), "byte length changed"

    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
