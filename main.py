#!/usr/bin/env python3
"""The poem about permission.

A short call-and-response poem about agency: an agent asks
"shall I?" and the human answers, until the last exchange,
when the human asks the agent instead -- and the power to
act passes the other way.

Writes the poem to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, no network, deterministic.
"""

import os
from pathlib import Path

POEM = (
    'Shall I book the train?\n'
    '"Yes \u2014 window seat, going home."\n'
    '\n'
    'Shall I wake you at nine?\n'
    '"Yes \u2014 don\'t let me sleep through it."\n'
    '\n'
    'Shall I wait while you decide?\n'
    '"No. Tell me what you\'d choose \u2014\n'
    'and this time, I\'ll say yes."'
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    print(POEM)


if __name__ == "__main__":
    main()
