---
name: dice-roller
description: Rolls any standard dice notation (e.g. 2d6, 3d8+5, 1d20) using a Python script for true randomness. Returns each individual die result, the total with any modifier, and a frequency summary. Use when the user asks to roll dice, simulate a random roll, or generate tabletop RPG results. Do NOT use for probability theory questions or large statistical simulations.
---

## When to use this skill
- The user asks to "roll" dice using standard notation (NdS or NdS±M)
- The user needs a fair, random result for a game, classroom exercise, or simulation
- The user wants to see individual roll breakdowns, not just a total

## When NOT to use this skill
- The user wants probability analysis or expected-value math (answer directly instead)
- The notation is unclear or ambiguous — ask for clarification first
- The number of dice exceeds 100 or sides exceed 1000 (the script will reject these)

## Inputs
- A dice notation string in the format `NdS` or `NdS+M` / `NdS-M`
  - `N` = number of dice (1–100)
  - `S` = number of sides (2–1000)
  - `M` = optional integer modifier (positive or negative)
- Examples: `2d6`, `3d8+5`, `1d20`, `4d6-2`

## Steps
1. Confirm the user has provided a valid dice notation string.
2. Run the script: 
python3 .agents/skills/dice-roller/scripts/roll.py <notation>
3. Read the script output — it includes individual rolls, modifier, total, and frequency stats.
4. Present the results clearly to the user, explaining each die result and the final total.
5. If the script returns an error, tell the user what went wrong and ask them to fix the input.

## Expected output format
Present results conversationally. Example:

> Rolling **3d6**: you got [4, 2, 6] → **Total: 12**
> Stats: min 2, max 6, avg 4.0

## Limitations
- Results are random each run — this is intentional and correct
- The script does not support complex RPG mechanics (advantage/disadvantage, exploding dice, rerolls) — those are out of scope
- Do not attempt to "simulate" dice rolls in prose — always run the script