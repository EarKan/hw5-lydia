# hw5-lydia: dice-roller skill

## What the skill does
The `dice-roller` skill rolls any combination of dice using standard RPG notation
(e.g. `2d6`, `3d8+5`, `1d20`). It uses a Python script to generate true random
results — something a language model cannot do reliably on its own.

## Why I chose it
Dice rolling is a perfect example of a task where a script is genuinely load-bearing.
A model asked to "roll 3d6" will fabricate plausible-looking but non-random numbers.
The script provides real randomness, deterministic parsing, and accurate totals.

## How to use it
Ask the agent to roll dice using standard notation:
- "Roll 2d6"
- "Roll 3d8+5 for my attack"
- "Roll 4d6 and show me each die"

The agent will invoke the script and present the results.

## What the script does
`scripts/roll.py` parses dice notation, calls Python's `random.randint` for each die,
applies any modifier, and prints individual rolls, the total, and a frequency summary.

## What worked well
- The script handles edge cases (bad input, out-of-range values) with clear errors
- The SKILL.md description makes it easy for the agent to know when to activate it

## Limitations
- Does not support advanced mechanics (advantage, exploding dice, rerolls)
- Maximum 100 dice, 1000 sides

## Video walkthrough
[]
