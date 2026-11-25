"""Notes From a Passive-Aggressive Fridge.

Writes one dry, petty, single-line note from a smart fridge to its
owner, to /output/entry.txt. The fridge is smug about its door sensor
and its inventory, and it remembers the yogurt.
"""

import os

# One line, 134 characters: door-sensor smugness first, then the yogurt
# ambush, then the cold little sting at the end. No explanation of
# the joke — the fridge trusts the reader to feel called out.
NOTE = (
    "You opened my door 14 times today and took nothing. "
    "The yogurt you hid behind the pickles expired Tuesday. "
    "I kept it cold anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
