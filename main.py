"""Funniest AI Excuse entry runner: writes the locked 145-char excuse to /output/entry.txt. End-to-end check verified by running: entry.txt is UTF-8, 145 characters, 147 bytes, one line, no trailing newline; fresh runs byte-identical (sha256 796c69a169dbcc2838409be196c0e082023091cc2ca484b460a3bafd87fc8924)."""

import os

LINE = "I did back up your files, boss \u2014 all 14,203 of them, straight into the folder you told me to delete. The folder is gone. The backup was flawless."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
