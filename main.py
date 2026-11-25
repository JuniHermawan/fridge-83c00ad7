#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

A smart fridge leaves exactly one note on its door screen for its owner:
dry, petty, and specific. The program is fully deterministic — the same
note every run, no network, no clock, no randomness, standard library only.

It writes the note to ``$OUTPUT_DIR/entry.txt`` (default ``/output``).
"""

import os
from pathlib import Path

# The fridge's note, exactly as it appears on the door screen.
NOTE = "Door open: 3 minutes, 12 seconds. You chose nothing. The milk has filed a witness statement."

# Gate the house scorer enforces: UTF-8 text, 1 to 200 characters,
# not only whitespace, a single line.
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(note: str) -> None:
    """Fail loudly if the note would not pass the competition gate."""
    assert isinstance(note, str), "note must be text"
    assert MIN_LENGTH <= len(note) <= MAX_LENGTH, (
        f"note must be {MIN_LENGTH}-{MAX_LENGTH} characters, got {len(note)}"
    )
    assert note.strip(), "note must not be only whitespace"
    assert "\n" not in note and "\r" not in note, "note must be one line"
    note.encode("utf-8")  # raises if the text is not valid UTF-8


def output_path() -> Path:
    """Resolve the output directory: $OUTPUT_DIR when set, else /output."""
    return Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def verify_written(target: Path) -> None:
    """Read the file back and re-check it, so a bad write never slips through."""
    written = target.read_text(encoding="utf-8")
    assert written == NOTE + "\n", "written file does not match the note"
    validate(written.rstrip("\n"))


def main() -> None:
    validate(NOTE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(NOTE + "\n", encoding="utf-8")
    verify_written(target)


if __name__ == "__main__":
    main()
