"""
Contains common variables and helper functions used throughout the game.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import random


class Game:
    """
    Defines some common game state
    """
    def __init__(self):
        self.height = 720
        self.width = 1280

game = Game()


def roll_dice(count=2, rolls=1, sides=6):
    """
    Reusable function for dice roles
    """
    results = []
    for _ in range(rolls):
        roll_result = tuple(random.randint(1, sides) for _ in range(count))
        results.append(roll_result)
    return results
