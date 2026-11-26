#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — one-line entry.

Prints the diagnosis and writes it to entry.txt: in
$MAKEFUN_OUTPUT_DIR when set, otherwise next to this script.
Standard library only.
"""

import os

LINE = "Diagnosis: chronic passive-aggression \u2014 you wrote 'per my last email' three times today, and not one of them was your last email."


def main():
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
