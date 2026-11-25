#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line deadline excuse to /output/entry.txt."""

ENTRY = "The Wi-Fi died, the backup died, and my deadline died of natural causes \u2014 I was just the witness."


def main() -> None:
    # Gate: 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
