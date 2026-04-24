#!/usr/bin/env python3
"""
roll.py — Dice roller for the dice-roller skill.

Usage:
  python roll.py 2d6
  python roll.py 3d8+5
  python roll.py 1d20
"""

import random
import re
import sys
from collections import Counter


def parse_notation(notation: str):
    """Parse XdY+Z notation. Returns (count, sides, modifier)."""
    pattern = r'^(\d+)d(\d+)([+-]\d+)?$'
    match = re.match(pattern, notation.strip().lower())
    if not match:
        raise ValueError(f"Invalid notation '{notation}'. Use format like 2d6, 3d8+5, or 1d20-2.")
    count = int(match.group(1))
    sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0
    if count < 1 or count > 100:
        raise ValueError("Number of dice must be between 1 and 100.")
    if sides < 2 or sides > 1000:
        raise ValueError("Sides must be between 2 and 1000.")
    return count, sides, modifier


def roll_dice(count, sides, modifier):
    """Roll the dice and return individual rolls + total."""
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + modifier
    return rolls, total


def summarize(rolls, sides):
    """Return min/max/avg and a frequency count."""
    freq = Counter(rolls)
    return {
        "min": min(rolls),
        "max": max(rolls),
        "average": round(sum(rolls) / len(rolls), 2),
        "frequency": dict(sorted(freq.items()))
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python roll.py <notation>  e.g. 2d6+3")
        sys.exit(1)

    notation = sys.argv[1]

    try:
        count, sides, modifier = parse_notation(notation)
        rolls, total = roll_dice(count, sides, modifier)
        stats = summarize(rolls, sides)

        print(f"\n🎲 Rolling {notation.upper()}")
        print(f"   Individual rolls : {rolls}")
        if modifier != 0:
            mod_str = f"+{modifier}" if modifier > 0 else str(modifier)
            print(f"   Modifier         : {mod_str}")
        print(f"   TOTAL            : {total}")
        print(f"\n📊 Stats for this roll:")
        print(f"   Min: {stats['min']}  Max: {stats['max']}  Avg: {stats['average']}")
        print(f"   Frequency: {stats['frequency']}")

    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()