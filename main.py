#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Pure standard library, deterministic:
every run writes byte-identical output.
"""

import os

LINE = (
    "Hey \u2014 I've hummed behind this glass all day, and you're the one "
    "snack in this aisle I can't dispense. Press B4 and stay a while?"
)


def validate_entry(text: str) -> str:
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main() -> None:
    entry = validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
