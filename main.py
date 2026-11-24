#!/usr/bin/env python3
"""Charm the Commuter entry.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt, as the competition's program/v1
harness requires. No network, no input, no secrets: the line is fixed.
"""

import os

ENTRY = (
    "In Wobbleford, drizzle till nine, then bright sun \u2014 the 8:12 bus "
    "is on time, the pigeons applaud, and your umbrella finally gets a lie-in."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
