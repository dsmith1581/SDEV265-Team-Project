"""
Contains helper functions used throughout the game.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import random

def roll_dice(count=2, rolls=1, sides=6):
    results = []
    for _ in range(rolls):
        roll_result = tuple(random.randint(1, sides) for _ in range(count))
        results.append(roll_result)
    return results