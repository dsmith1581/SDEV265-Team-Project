"""
Contains some reusable UI components

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade

from . import common


class Button:
    def __init__(self, action=lambda: None, center_x=common.app.width / 2, center_y=common.app.height / 2, color=arcade.color.LIGHT_GRAY, font_color=arcade.color.BLACK, font_size=20, height=50, text="Button", width=200):
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
            common.audio["button"].play()
            self.action()


class ToggleButton:
    def __init__(self, action=lambda: None, center_x=0, center_y=0, width=150, height=50, enabled=True):
        self.action = action
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.enabled = enabled
        self.color_enabled = arcade.color.GREEN
        self.color_disabled = arcade.color.RED
        self.font_color = arcade.color.BLACK
        self.font_size = 20

    def draw(self):
        """Draw the toggle button."""
        color = self.color_enabled if self.enabled else self.color_disabled
        text = "Enabled" if self.enabled else "Disabled"
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, color)
        arcade.draw_text(text, self.center_x, self.center_y, self.font_color, font_size=self.font_size, anchor_x="center", anchor_y="center")

    def check_if_clicked(self, x, y):
        """Check if the toggle button is clicked."""
        if(self.center_x - self.width / 2 < x < self.center_x + self.width / 2) and (self.center_y - self.height / 2 < y < self.center_y + self.height / 2):
            common.audio["button"].play()
            self.enabled = not self.enabled
            self.action()


class TextInputBox:
    def __init__(self, center_x=0, center_y=0, width=300, height=50, text=""):
        self.center_x         = center_x
        self.center_y         = center_y
        self.width            = width
        self.height           = height
        self.text             = text
        self.active           = False
        self.font_color       = arcade.color.BLACK
        self.font_size        = 20
        self.border_color     = arcade.color.BLACK
        self.background_color = arcade.color.WHITE

    def draw(self):
        """Draw the text input box."""
        if self.active:
            border_color = arcade.color.BLUE
        else:
            border_color = self.border_color
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.background_color)
        arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width, self.height, border_color, 2)
        arcade.draw_text(self.text, self.center_x - self.width / 2 + 10, self.center_y - self.font_size / 2, self.font_color, font_size=self.font_size, anchor_x="left")

    def check_if_clicked(self, x, y):
        """Check if the text input box is clicked."""
        if(self.center_x - self.width / 2 < x < self.center_x + self.width / 2) and (self.center_y - self.height / 2 < y < self.center_y + self.height / 2):
            self.active = True
        else:
            self.active = False

    def on_text(self, text):
        """Handle text input."""
        if self.active:
            self.text += text

    def on_key_press(self, key, modifiers):
        """Handle backspace and other key presses."""
        if self.active:
            if key == arcade.key.BACKSPACE:
                self.text = self.text[:-1]


class PieceSelector:
    def __init__(self, center_x=0, center_y=0):
        self.center_x      = center_x
        self.center_y      = center_y
        self.width         = 64
        self.height        = 64
        self.current_index = 1
        self.total_images  = 6
        self.image         = common.graphics[f"piece{self.current_index}"]

        # Define buttons for changing to the previous or next piece
        self.prev_button = Button(text="Prev", center_x=self.center_x - self.width / 2 - 50, center_y=self.center_y, width=80, height=50, action=self.previous_image)
        self.next_button = Button(text="Next", center_x=self.center_x + self.width / 2 + 50, center_y=self.center_y, width=80, height=50, action=self.next_image)

    def draw(self):
        """Draw the image and the next/previous buttons."""
        arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.image)
        self.prev_button.draw()
        self.next_button.draw()

    def check_if_clicked(self, x, y):
        """Check if next or previous buttons are clicked."""
        self.prev_button.check_if_clicked(x, y)
        self.next_button.check_if_clicked(x, y)

    def previous_image(self):
        """Select the previous image."""
        self.current_index -= 1

        if self.current_index < 1:
            self.current_index = self.total_images

        self.image = common.graphics[f"piece{self.current_index}"]

    def next_image(self):
        """Select the next image."""
        self.current_index += 1

        if self.current_index > self.total_images:
            self.current_index = 1

        self.image = common.graphics[f"piece{self.current_index}"]
