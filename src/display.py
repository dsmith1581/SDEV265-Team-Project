"""
Handles the main view switching for the display of the application.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade

from .       import ui_component
from .common import *


class HelpView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Help - press ESCAPE to return to the main menu", game.width / 2, game.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        # Return to main menu on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(MainMenuView())

class MainMenuView(arcade.View):
    def setup(self):
        """ Setup the main menu view and buttons. """
        # Create buttons for the main menu
        b_color     = arcade.color_from_hex_string("#7F8C8D")
        b_width     = 400
        b_height    = 100
        b_font_size = 30

        self.buttons = [
            ui_component.Button(text="Start", center_y=game.height / 2 + 150, width=b_width, height=b_height, action=self.start_game),
            ui_component.Button(text="Exit",  center_y=game.height / 2 + 0,   width=b_width, height=b_height, action=self.exit_game),
            ui_component.Button(text="Help",  center_y=game.height / 2 - 150, width=b_width, height=b_height, action=self.show_help)
        ]

    def on_show_view(self):
        """ This is run once when we switch to this view. """
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()  # Set up the buttons when the view is shown

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        for button in self.buttons:
            button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        for button in self.buttons:
            button.check_if_clicked(x, y)

    def on_key_press(self, key, _modifiers):
        """ Called when a key is pressed. """
        # Exit on escape
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def start_game(self):
        """ Action for the Start button. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def exit_game(self):
        """ Action for the Exit button. """
        arcade.close_window()

    def show_help(self):
        """ Action for the Help button. """
        help_view = HelpView()
        self.window.show_view(help_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game - press SPACE to advance", game.width / 2, game.height / 2, arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.SPACE:
            self.window.show_view(GameOverView())


class GameOverView(arcade.View):
    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over - press ESCAPE to advance", game.width / 2, game.height / 2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        # Change to main menu view on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(MainMenuView())

def init():
    """ Startup """
    window = arcade.Window(game.width, game.height, "Monopoly", vsync=True)
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()