"""
Handles the main view switching for the display of the application.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade

from . import ui_component
from . import common


class HelpView(arcade.View):
    padding = 100

    def setup(self):
        """Setup the main menu view and buttons."""
        b_color     = arcade.color.LIGHT_GRAY
        b_width     = 300
        b_height    = 100
        b_font_size = 30

        self.buttons = [
            ui_component.Button(text="User Guide", center_y=self.padding, center_x=b_width * 1 - self.padding * 1, width=b_width, height=b_height, action=common.open_help),
            ui_component.Button(text="Credits",    center_y=self.padding, center_x=b_width * 2 + self.padding * 0, width=b_width, height=b_height, action=common.open_credits),
            ui_component.Button(text="Back",       center_y=self.padding, center_x=b_width * 3 + self.padding * 1, width=b_width, height=b_height, action=lambda: self.window.show_view(self.window.views["main_menu"])),
        ]

    """Change the bgcolor when going to this view"""
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ARSENIC)
        self.setup() # Set up the buttons when the view is shown

    """Draw logic"""
    def on_draw(self):
        self.clear()

        help_text = """Welcome to the game of Monopoly!

The game can be started from the main menu. The "Start" button will launch a setup wizard to configure the game. Note: For all enabled players the names and pieces chosen must be unique. Disabled players are ignored.

The full user guide can be accessed by clicking the "User Guide" button below. This will open the full HTML help manual in your local browser. If the installer was used, this documentation is also made available offline in the installation directory.

Credits for various images, sounds, and other assets in this game can be found by clicking the "Credits" button. The credits will open in the system's default text editor. If the installer was used, this documentation is also made available offline in the installation directory.

Authors: Bo Tang, Dan Smith, and Nate Spriggs
            """

        arcade.draw_text(help_text, color=arcade.color.WHITE, start_x=self.padding / 2, start_y=common.app.height - self.padding, font_size=20, width=common.app.width - self.padding, align="left", multiline=True)

        # Draw the buttons
        for button in self.buttons:
            button.draw()

    """Handle the escape key"""
    def on_key_press(self, key, _modifiers):
        # Return to main menu on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])

    """Handle mouse clicks"""
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.buttons:
            button.check_if_clicked(x, y)


class MainMenuView(arcade.View):
    music_playing = False

    def setup(self):
        """Setup the main menu view and buttons."""
        b_width     = 400
        b_height    = 100
        b_font_size = 30

        # A list of all buttons on the page so we can batch process them
        self.buttons = [
            ui_component.Button(text="Start", center_y=common.app.height / 2 + 50,  width=b_width, height=b_height, action=self.start_game),
            ui_component.Button(text="Help",  center_y=common.app.height / 2 - 100, width=b_width, height=b_height, action=self.show_help),
            ui_component.Button(text="Exit",  center_y=common.app.height / 2 - 250, width=b_width, height=b_height, action=self.exit_game)
        ]

        # Make sure we kick off the music if it wasn't already started before!
        if not self.music_playing:
            common.audio["bg_music"].play(loop=True)
            self.music_playing = True;

        # Draw the logo from the preloaded graphics in common.py
        self.logo_texture = common.graphics["logo"]
        self.logo_x       = common.app.width / 2
        self.logo_y       = common.app.height - self.logo_texture.height / 2 - 20

    def on_show_view(self):
        """This is run once when we switch to this view."""
        arcade.set_background_color(arcade.color.AMAZON)
        self.setup() # Set up the buttons when the view is shown

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw the logo
        arcade.draw_texture_rectangle(self.logo_x, self.logo_y, self.logo_texture.width, self.logo_texture.height, self.logo_texture)

        # Draw the buttons
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
        game_setup_view = self.window.views["game_setup"]
        game_setup_view.setup()
        self.window.show_view(game_setup_view)

    def exit_game(self):
        """Action for the Exit button."""
        arcade.close_window()

    def show_help(self):
        """Action for the Help button."""
        help_view = self.window.views["help"]
        self.window.show_view(help_view)


class GameSetupView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_setups = []
        self.buttons = []
        self.start_button = None
        self.cancel_button = None

    def setup(self):
        """Setup the game setup view."""
        self.player_setups = []
        self.buttons       = []

        # Define positions for 4 columns
        column_width = common.app.width / 4
        for i in range(4):
            x_position = column_width * (i + 0.5)

            toggle_y         = common.app.height - 200
            name_y           = toggle_y - 100
            piece_selector_y = name_y - 100

            toggle_button  = ui_component.ToggleButton(center_x=x_position, center_y=toggle_y)
            name_input     = ui_component.TextInputBox(center_x=x_position, center_y=name_y, text="Player Name")
            piece_selector = ui_component.PieceSelector(center_x=x_position, center_y=piece_selector_y)

            # Store components together
            self.player_setups.append(
            {
                "toggle_button":  toggle_button,
                "name_input":     name_input,
                "piece_selector": piece_selector
            })

        # Create Cancel and Start buttons
        self.cancel_button = ui_component.Button(text="Cancel", center_x=common.app.width / 2 - 150, center_y=50, width=200, height=50, action=self.cancel)
        self.start_button  = ui_component.Button(text="Start",  center_x=common.app.width / 2 + 150, center_y=50, width=200, height=50, action=self.start_game)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        # Draw player setups
        for setup in self.player_setups:
            setup["toggle_button"].draw()
            setup["name_input"].draw()
            setup["piece_selector"].draw()

        # Draw buttons
        self.cancel_button.draw()
        # Determine if start button is usable
        if self.can_start_game():
            self.start_button.color = arcade.color.LIGHT_GRAY
        else:
            self.start_button.color = arcade.color.DARK_GRAY
        self.start_button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for setup in self.player_setups:
            setup["toggle_button"].check_if_clicked(x, y)
            setup["name_input"].check_if_clicked(x, y)
            setup["piece_selector"].prev_button.check_if_clicked(x, y)
            setup["piece_selector"].next_button.check_if_clicked(x, y)

        self.cancel_button.check_if_clicked(x, y)

        if self.can_start_game():
            self.start_button.check_if_clicked(x, y)

    def on_text(self, text):
        for setup in self.player_setups:
            setup["name_input"].on_text(text)

    def on_key_press(self, key, modifiers):
        for setup in self.player_setups:
            setup["name_input"].on_key_press(key, modifiers)

    def cancel(self):
        # Go back to main menu
        self.window.show_view(self.window.views["main_menu"])

    def start_game(self):
        # Proceed to game view
        game_view = self.window.views["game"]
        game_view.setup(players=self.get_player_data())

        self.window.show_view(game_view)

    # Reports whether the inputs are valid to start a game or not
    def can_start_game(self):
        enabled_players = [setup for setup in self.player_setups if setup["toggle_button"].enabled]
        
        # At least 2 players must be enabled
        if len(enabled_players) < 2:
            return False

        # All enabled players must have names set
        player_names = [setup["name_input"].text.strip() for setup in enabled_players]
        for name in player_names:
            if not name:
                return False

        # Check that none of the enabled players have the same name (case insensitive)
        lowercased_names = [name.lower() for name in player_names]
        if len(lowercased_names) != len(set(lowercased_names)):
            return False

        # None of the enabled players can have the same piece selected
        selected_pieces = [setup["piece_selector"].current_index for setup in enabled_players]
        if len(selected_pieces) != len(set(selected_pieces)):
            return False
        
        return True

    def get_player_data(self):
        """Return the player data needed to start the game."""
        players = []

        for setup in self.player_setups:
            if setup["toggle_button"].enabled:
                player = {
                    "name":  setup["name_input"].text,
                    "piece": setup["piece_selector"].current_index
                }
                players.append(player)

        return players


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.players = []
        self.board_texture = common.graphics["board"]

    def setup(self, players=None):
        """This should set up your game and get it ready to play"""
        if players is not None:
            self.players = players
        pass

    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()

        # Draw the board texture at the top left
        arcade.draw_texture_rectangle(self.board_texture.width // 2, self.board_texture.height // 2, self.board_texture.width, self.board_texture.height, self.board_texture)

        # For now, draw some temporary text and info
        arcade.draw_text("SPACE to advance", common.app.width / 1.5, common.app.height / 2, arcade.color.BLACK, font_size=30, anchor_x="left")
        y = common.app.height / 2 - 50
        for player in self.players:
            text = f"Player: {player['name']}, Piece: {player['piece']}"
            arcade.draw_text(text, common.app.width / 1.5, y, arcade.color.BLACK, font_size=20, anchor_x="left")
            y -= 30

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.SPACE:
            self.window.show_view(self.window.views["game_over"])


class GameOverView(arcade.View):
    # This will be called when the view is switched to
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over - press ESCAPE to advance", common.app.width / 2, common.app.height / 2, arcade.color.WHITE, 30, anchor_x="center")

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
    game_setup_view = GameSetupView()
    game_view = GameView()
    game_over_view = GameOverView()

    # Store views in a dictionary on the window for easy access
    window.views = {
        "main_menu": main_menu_view,
        "help": help_view,
        "game_setup": game_setup_view,
        "game": game_view,
        "game_over": game_over_view
    }

    # Start with the main menu view
    window.show_view(main_menu_view)
    arcade.run()
