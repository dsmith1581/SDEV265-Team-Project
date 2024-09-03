"""
Handles the main view switching for the display of the application.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade

from . import ui_component
from . import common


class HelpView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Help - press ESCAPE to return to the main menu", common.app.width / 2, common.app.height / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        # Return to main menu on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])


class MainMenuView(arcade.View):
    music_playing = False

    def setup(self):
        """Setup the main menu view and buttons."""
        b_color     = arcade.color_from_hex_string("#7F8C8D")
        b_width     = 400
        b_height    = 100
        b_font_size = 30

        self.buttons = [
            ui_component.Button(text="Start", center_y=common.app.height / 2 + 150, width=b_width, height=b_height, action=self.start_game),
            ui_component.Button(text="Exit",  center_y=common.app.height / 2 + 0,   width=b_width, height=b_height, action=self.exit_game),
            ui_component.Button(text="Help",  center_y=common.app.height / 2 - 150, width=b_width, height=b_height, action=self.show_help)
        ]

        if not self.music_playing:
            common.audio["bg_music"].play(loop=True)
            self.music_playing = True;

    def on_show_view(self):
        """This is run once when we switch to this view."""
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup()  # Set up the buttons when the view is shown

    def on_draw(self):
        """Render the screen."""
        self.clear()
        for button in self.buttons:
            button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button."""
        for button in self.buttons:
            button.check_if_clicked(x, y)

    def on_key_press(self, key, _modifiers):
        """Called when a key is pressed."""
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def start_game(self):
        """Action for the Start button."""
        game_view = self.window.views["game"]
        game_view.setup()
        self.window.show_view(game_view)

    def exit_game(self):
        """Action for the Exit button."""
        arcade.close_window()

    def show_help(self):
        """Action for the Help button."""
        help_view = self.window.views["help"]
        self.window.show_view(help_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """This should set up your game and get it ready to play"""
        pass

    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game - press SPACE to advance", common.app.width / 2, common.app.height / 2, arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.SPACE:
            self.window.show_view(self.window.views["game_over"])


class GameOverView(arcade.View):
    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over - press ESCAPE to advance", common.app.width / 2, common.app.height / 2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        # Change to main menu view on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])


def init():
    """Startup"""
    window = arcade.Window(common.app.width, common.app.height, "Monopoly", vsync=True)

    # Create instances of all views
    main_menu_view = MainMenuView()
    help_view = HelpView()
    game_view = GameView()
    game_over_view = GameOverView()

    # Store views in a dictionary on the window for easy access
    window.views = {
        "main_menu": main_menu_view,
        "help":      help_view,
        "game":      game_view,
        "game_over": game_over_view
    }

    # Start with the main menu view
    window.show_view(main_menu_view)
    arcade.run()
