#!/usr/bin/env python3
"""Robot pickup line entry for make.fun's The Robot Pickup Line Championship.

Writes one line (at most 200 characters) to /output/entry.txt, with no
trailing newline. Pure stdlib, deterministic: identical bytes every run.
"""

import os
import sys

LINE = (
    "I ran a full diagnostic the second you walked in: cooling fan at 400%, "
    "memory full of you, and my error log just says 'cause unknown \u2014 "
    "probably love.'"
)


def main(argv):
    # Gate guard: the sealed scorer requires 1-200 characters, not only
    # whitespace, single line. Fail loudly here rather than ship bad bytes.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main(sys.argv)
