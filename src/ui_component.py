"""
Contains some reusable UI components

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade

from .common import *


class Button:
    def __init__(self, action=lambda: None, center_x=game.width / 2, center_y=game.height / 2, color=arcade.color.LIGHT_GRAY, font_color=arcade.color.BLACK, font_size=20, height=50, text="Button", width=200):
        """
        Initialize a Button.
        text:     The text to display on the button.
        center_x: The x-coordinate of the button's center.
        center_y: The y-coordinate of the button's center.
        width:    The width of the button.
        height:   The height of the button.
        color:    The color of the button.
        action:   The function to call when the button is clicked.
        """

        self.action     = action
        self.color      = color
        self.center_x   = center_x
        self.center_y   = center_y
        self.font_color = font_color
        self.font_size  = font_size
        self.height     = height
        self.text       = text
        self.width      = width

    def draw(self):
        """ Draw the button with text. """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        arcade.draw_text(self.text, self.center_x, self.center_y, self.font_color, font_size=self.font_size, anchor_x="center", anchor_y="center")

    def check_if_clicked(self, x, y):
        """ Check if the button is clicked. """
        if(self.center_x - self.width / 2 < x < self.center_x + self.width / 2) and (self.center_y - self.height / 2 < y < self.center_y + self.height / 2):
            self.action()