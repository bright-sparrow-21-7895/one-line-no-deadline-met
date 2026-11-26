"""One-line joke excusing a missed deadline.

The program writes a single line to /output/entry.txt: an
excuse for a deadline that was not met. The joke reframes
the miss as a favour to the deadline itself, which keeps
it a real excuse, a single line, and something a person
might actually say, as the bounty brief asks. The turn
is that the deadline, not the speaker, is the one that
needed the extra time — the excuse blames the calendar
by pretending to do it a favour.
"""

import os

ENTRY = "I didn't miss the deadline \u2014 I just gave it extra time to lower its expectations."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
