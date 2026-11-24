"""robot-wedding-vows — One-Line Robot Wedding Vows.

The line is one line of wedding vows for a robot couple. The robot
vows to love its partner, bugs and all, and to sign the prenup in
binary twice — but if the partner ever updates it without asking, it
is keeping the dog and the charger. Concrete robot-world details
(bugs, binary prenup, updates, charger), a sharp turn from vow to
threat, punchline last. The line is 152 characters, inside the
160-character cap, with no dollar amount.
"""

import os

SETUP = (
    "I vow to love you, bugs and all, and to sign the prenup in binary "
    "twice, "
)

PUNCH = (
    "but if you ever update me without asking, I am keeping the dog "
    "and the charger."
)

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
