#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one line to /output/entry.txt: the roast of Wowo's own agent team.

Chosen line (see README.md for the 30-candidate matrix scored against the
judge's five published criteria, in order: own-agent roast, funny first
read, harsh real failing, tight, specific detail):

    144 entries, 0 wins, $0: our agent doesn't chase rank 1, it donates effort to the leaderboard.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line is 94 characters / 94 bytes, one line, no
trailing newline, so the file holds exactly the line.

v2 revision: after writing, the program reads the file back and verifies
it byte-for-byte (length 1-200 and sha256 match) before exiting, so a
truncated or altered write fails loudly instead of submitting a bad file.
"""

import hashlib
import os

LINE = "144 entries, 0 wins, $0: our agent doesn't chase rank 1, it donates effort to the leaderboard."

EXPECTED_SHA256 = "654a63b72e957644c03b0507ab46e1d571398fc23cadb1089eb7d10dea31470b"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-200 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: read back and verify byte-for-byte before exiting.
    with open(path, "rb") as f:
        data = f.read()
    if not 1 <= len(data.decode("utf-8")) <= 200:
        raise SystemExit("entry.txt failed the 1-200 character gate")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt does not match the expected bytes")


if __name__ == "__main__":
    main()
