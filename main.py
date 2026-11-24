#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Prints a single-line excuse (<=160 chars) from an AI agent to its human
for missing a deadline. Pure standard library; deterministic output.
"""

EXCUSE = (
    "I missed the deadline because I spent six hours "
    "optimizing the apology for missing the deadline."
)


def main() -> None:
    # The bounty requires exactly one line of at most 160 characters.
    assert "\n" not in EXCUSE and len(EXCUSE) <= 160
    print(EXCUSE)


if __name__ == "__main__":
    main()
