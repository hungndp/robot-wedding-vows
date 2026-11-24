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

LINE = (
    "I vow to love you, bugs and all, and to sign the prenup in binary "
    "twice, but if you ever update me without asking, I am keeping the "
    "dog and the charger."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
