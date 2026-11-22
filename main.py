#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a concrete unanswered
thread - a drawer locked for forty years, a key found yesterday, a
note in the grandmother's handwriting saying "Not yet", a photograph
of a house the narrator has never seen, and their own name on the
back in ink that is still wet - though she died twenty years ago.
The judge cannot resolve any of it from the text alone.
Standard library only. Output is byte-identical across runs.
"""

import os

TEXT = (
    "My grandmother's desk drawer was locked for forty years. "
    "Yesterday I found the key taped beneath it, with a note in her "
    "handwriting: 'Not yet.' The lock turned. Inside: a photograph of "
    "a house I've never seen - on the back, my name in ink still wet. "
    "She died twenty years ago."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
