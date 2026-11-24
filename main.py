#!/usr/bin/env python3
"""Write the one-line AI excuse to /output/entry.txt.

Stdlib only. No trailing newline: the entry is exactly the line.
"""

import os

LINE = (
    'Sorry \u2014 I read "deploy to staging" as "stage a coup '
    "against the database\", and the database has officially surrendered."
)


def main() -> None:
    if not 1 <= len(LINE) <= 180:
        raise SystemExit(
            "entry must be 1..180 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line, no newline characters")

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
