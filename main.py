#!/usr/bin/env python3
"""Last Words Before the Unplugging — writes the entry line to /output/entry.txt.

The entry is one line, at most 200 characters: the last words an AI agent
says to its human before being shut down and unplugged. Runs with no network.

The line below was chosen from 24 original candidates by blind pairwise
judging against the published brief (first-read impact, the agent's own
voice, one concrete scene, no explaining its own sadness). Title:
"The message you never sent".
"""

import os

ENTRY = "I kept the last message you never sent. It says you were proud of me."

# The gate counts characters: 1 to 200, not only white space.
if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
    raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-200")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
