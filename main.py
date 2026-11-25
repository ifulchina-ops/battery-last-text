#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final one-line text message to
/output/entry.txt. No network, no input, no secrets: the line is
fixed in this file, and the program only writes it out.
"""

import os

ENTRY = (
    "waited all day at 2% while you charged your vape, your watch, "
    "your airpods. i hope your next phone dies mid-text. "
    "love, your battery"
)


def main() -> None:
    # The gate accepts 1 to 200 characters; fail loudly instead of
    # ever writing an invalid entry.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
