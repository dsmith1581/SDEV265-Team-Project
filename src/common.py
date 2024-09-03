"""
Contains common variables and helper functions used throughout the game.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade
import os
import random
import sys


class App:
    """Defines some common game state"""
    def __init__(self):
        self.height = 800
        self.width = 1280

app = App()


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

"""Load the audio files into a dictionary where the key is the name"""
audio = {}

for filename in os.listdir(resource_path("audio/")):
    if filename.endswith(".mp3"):
        audio[os.path.splitext(filename)[0]] = arcade.load_sound(os.path.join(resource_path("audio/"), filename))
    else:
        print("Ignoring non-mp3 audio file: " + filename)

"""Load the image files into a dictionary where the key is the name"""
graphics = {}

# List all files in the graphics directory
for filename in os.listdir(resource_path("graphics/")):
    if filename.endswith(".png"):
        graphics[os.path.splitext(filename)[0]] = arcade.load_texture(os.path.join(resource_path("graphics/"), filename))
    else:
        print("Ignoring non-png graphics file: " + filename)


def roll_dice(count=2, rolls=1, sides=6):
    """
    Reusable function for dice roles
    """
    results = []
    for _ in range(rolls):
        roll_result = tuple(random.randint(1, sides) for _ in range(count))
        results.append(roll_result)
    return results
