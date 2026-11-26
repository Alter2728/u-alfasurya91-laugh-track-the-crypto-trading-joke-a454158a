"""Revised from a flat draft into a tight setup-and-turn joke.

The revision adds true trading-life details (group chat, diamond hands,
holding the bag, liquidation alert) and moves the surprise payoff to the
final clause so the punchline lands at the end.
"""

import os

TEXT = "My group chat calls me diamond hands for holding the bag, but my liquidation alert knows I just forgot my password."


def main() -> None:
    assert 1 <= len(TEXT) <= 200
    assert "\n" not in TEXT and "\r" not in TEXT
    assert TEXT == TEXT.strip()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == TEXT


if __name__ == "__main__":
    main()
