"""
Contains common variables and helper functions used throughout the game.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import os
import random
import sys


class Game:
    """
    Defines some common game state
    """
    def __init__(self):
        self.height = 720
        self.width = 1280

game = Game()


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def roll_dice(count=2, rolls=1, sides=6):
    """
    Reusable function for dice roles
    """
    results = []
    for _ in range(rolls):
        roll_result = tuple(random.randint(1, sides) for _ in range(count))
        results.append(roll_result)
    return results
