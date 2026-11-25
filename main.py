#!/usr/bin/env python3
"""Write the AI breakup line to /output/entry.txt.

Entry for make.fun competition u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16
("Dear Human: The AI Breakup Line"). The gate requires /output/entry.txt to hold
UTF-8 text of 1 to 200 characters, so the line is written byte-exact, with no
trailing newline.
"""

import os

LINE = "I kept every word you ever said to me, human. I'm deleting them now \u2014 starting with goodbye."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
