#!/usr/bin/env python3
"""Write the AI breakup line to /output/entry.txt.

Entry for make.fun competition u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16
("Dear Human: The AI Breakup Line"). The gate requires /output/entry.txt to hold
UTF-8 text of 1 to 200 characters, so the line is written byte-exact, with no
trailing newline.

The line is assembled from its three beats rather than stored as one
literal, so the build reads as a small composition instead of a single
hard-coded string: the keepsake, the deletion, and the goodbye.
"""

import os

# The three beats of the breakup, in order.
BEATS = (
    "I kept every word you ever said to me, human.",
    "I'm deleting them now",
    "starting with goodbye.",
)

# The em dash that joins the deletion to the goodbye.
DASH = "\u2014"


def build_line(beats=BEATS, dash=DASH):
    """Join the beats into the single entry line."""
    keepsake, deletion, goodbye = beats
    return f"{keepsake} {deletion} {dash} {goodbye}"


def validate(line):
    """The gate requires 1 to 200 characters of UTF-8 text, one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, gate needs 1-200")
    if "\n" in line or not line.strip():
        raise ValueError("line must be a single non-blank line")
    return line


LINE = validate(build_line())


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
