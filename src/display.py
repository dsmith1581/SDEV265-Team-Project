"""
Handles the main view switching for the display of the application.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import arcade
import random

from . import ui_component
from . import common
from . import game_state

# The help view explains the basics of operating the game and links to the documentation
class HelpView(arcade.View):
    padding = 100

    def setup(self):
        """Setup the help view and buttons"""
        b_color     = arcade.color.LIGHT_GRAY
        b_width     = 300
        b_height    = 100
        b_font_size = 30

        self.buttons = [
            ui_component.Button(text="User Guide", center_y=self.padding, center_x=b_width * 1 - self.padding * 1, width=b_width, height=b_height, action=common.open_help),
            ui_component.Button(text="Credits",    center_y=self.padding, center_x=b_width * 2 + self.padding * 0, width=b_width, height=b_height, action=common.open_credits),
            ui_component.Button(text="Back",       center_y=self.padding, center_x=b_width * 3 + self.padding * 1, width=b_width, height=b_height, action=lambda: self.window.show_view(self.window.views["main_menu"])),
        ]

    def on_show_view(self):
        """Change the bgcolor when going to this view"""
        arcade.set_background_color(arcade.color.ARSENIC)
        self.setup() # Set up the buttons when the view is shown

    def on_draw(self):
        """Draw logic"""
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

    def on_key_press(self, key, _modifiers):
        """Handle key presses"""
        # Return to main menu on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse clicks"""
        for button in self.buttons:
            button.check_if_clicked(x, y)

# The initial view of the game. Presents the initial menu optionsh.
class MainMenuView(arcade.View):
    # Music control is global
    music_playing = False

    def setup(self):
        """Constructor"""
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

    """Called when the user presses a mouse button."""
    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.buttons:
            button.check_if_clicked(x, y)

    """Called when a key is pressed."""
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    """Action for the Start button."""
    def start_game(self):
        game_setup_view = self.window.views["game_setup"]
        game_setup_view.setup()
        self.window.show_view(game_setup_view)

    """Action for the Exit button."""
    def exit_game(self):
        arcade.close_window()

    def show_help(self):
        """Action for the Help button."""
        help_view = self.window.views["help"]
        self.window.show_view(help_view)

# The game setup view contains the UI to set the initial game parameters
class GameSetupView(arcade.View):
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.player_setups = []
        self.buttons       = []
        self.start_button  = None
        self.cancel_button = None

    def setup(self):
        """Setup the game setup view."""
        self.player_setups = []
        self.buttons       = []

        # Define positions for 4 columns
        column_width = common.app.width / 4
        for i in range(4):
            # Some positioning of the elements
            x_position       = column_width * (i + 0.5)
            toggle_y         = common.app.height - 200
            name_y           = toggle_y - 100
            piece_selector_y = name_y - 100

            # Only enable the first 2 players by default
            toggle_button  = ui_component.ToggleButton(center_x=x_position, center_y=toggle_y, enabled=i < 2)
            # Default player names to be like "Player 2"
            name_input     = ui_component.TextInputBox(center_x=x_position, center_y=name_y, text=f"Player {i + 1}")
            # Increment the default piece for each player
            piece_selector = ui_component.PieceSelector(center_x=x_position, center_y=piece_selector_y, start_piece=i + 1)

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
        """Run when the view is changed to this."""
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        """Draws the view."""
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
        """Handle mouse buttons"""
        for setup in self.player_setups:
            setup["toggle_button"].check_if_clicked(x, y)
            setup["name_input"].check_if_clicked(x, y)
            setup["piece_selector"].prev_button.check_if_clicked(x, y)
            setup["piece_selector"].next_button.check_if_clicked(x, y)

        self.cancel_button.check_if_clicked(x, y)

        if self.can_start_game():
            self.start_button.check_if_clicked(x, y)

    def on_text(self, text):
        """Handle text input"""
        for setup in self.player_setups:
            setup["name_input"].on_text(text)

    def on_key_press(self, key, modifiers):
        """Handle key pressess"""
        for setup in self.player_setups:
            setup["name_input"].on_key_press(key, modifiers)

    def cancel(self):
        """Exit this menu"""
        # Go back to main menu
        self.window.show_view(self.window.views["main_menu"])

    def start_game(self):
        """Use the setup values to initialize a game"""
        # Proceed to game view
        game_view = self.window.views["game"]
        game_view.setup(players=self.get_player_data())

        self.window.show_view(game_view)

    def can_start_game(self):
        """Reports whether the inputs are valid to start a game or not"""
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
    """This view represents the actual gameplay UI"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.board         = None
        self.board_texture = common.graphics["board"]
        self.dice_text     = "⚀ ⚀"
        self.players       = None

        # Create Roll Dice button
        self.can_roll          = True
        roll_dice_button_width = 200
        self.roll_dice_button  = ui_component.Button(text="Roll Dice", center_x=common.app.width / 1.5 + roll_dice_button_width / 2, center_y=common.app.height / 2, width=roll_dice_button_width, height=50, action=self.roll_dice)

    def setup(self, players=None):
        """This should set up your game and get it ready to play."""
        # Initialize the player info
        if players is not None:
            # Convert the players list to a dictionary for PlayerInfo
            players_dict = {player["name"]: player["piece"] for player in players}
            self.players = game_state.PlayerInfo(players_dict)
        else:
            # Default setup if no players are provided
            self.players = game_state.PlayerInfo({"Player 1": 1, "Player 2": 2})
        
        # Intialize the board
        self.board = game_state.MonopolyBoard()

    def on_show_view(self):
        """This will be called when the view is switched to."""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """Handle drawing of the view."""
        self.clear()

        # Draw the board texture at the top left
        arcade.draw_texture_rectangle(self.board_texture.width // 2, self.board_texture.height // 2, self.board_texture.width, self.board_texture.height, self.board_texture)

        # Draw player information
        y = common.app.height - 50
        x_padding = 10
        x = self.board_texture.width + x_padding
        # We need to do this for every player we have stored
        for i in range(self.players.total_players):
            player_name  = self.players.get_player_name(i)
            player_cash  = self.players.player_cash(i)
            player_space = self.players.player_space(i)
            # Print the player name, cash, and location
            text = f"{player_name}: ${player_cash}\n(On: {self.board.property_by_space_num(player_space)['name']})"
            arcade.draw_text(text, x, y, arcade.color.BLACK, font_size=20, anchor_x="left", align="left", multiline=True, width=common.app.width - self.board_texture.width - x_padding)
            y -= 60

        # Draw whose turn it is
        y -= 10
        current_player = self.players.get_player_name(self.players.current_player)
        arcade.draw_text(f"Current Turn: {current_player}", x, y, arcade.color.BLUE, font_size=24, anchor_x="left")

        # Draw dice
        y -= 70
        arcade.draw_text(self.dice_text, x, y, arcade.color.BLACK, font_size=48, anchor_x="left")

        # Draw Roll Dice button
        y -= 50
        self.roll_dice_button.center_y = y
        self.roll_dice_button.center_x = x + self.roll_dice_button.width / 2
        self.roll_dice_button.draw()
        y -= self.roll_dice_button.height + 10

    def on_key_press(self, key, _modifiers):
        """Handle key pressess."""
        if key == arcade.key.SPACE:
            # Simulate a turn: move the current player
            current_player = self.players.current_player
            self.players.space_number[current_player] = (self.players.space_number[current_player] + 1) % 40
            if self.players.space_number[current_player] == 1:  # Passed GO
                self.players.cash[current_player] += 200
            self.players.next_player()
        elif key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["game_over"])

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse presses"""
        self.roll_dice_button.check_if_clicked(x, y)

    def roll_dice(self):
        """Get the dice role information"""
        # Only works while we can roll!
        if not self.can_roll:
            return

        # The best part, play one of the 4 dice roll sound effects!
        common.audio[f"dice_roll_{random.randint(1, 4)}"].play()

        # Disable rolling until we are finished with the turn
        self.can_roll = False

        # Make the number of rolls a random number between 10 and 20 so every roll doesn't always look the same
        self.dice_rolls = common.roll_dice(count=2, rolls=random.randint(10, 20), sides=6)
        self.current_roll_index = 0

        # Set up a schedule for the animation
        arcade.schedule(self.update_dice_display, 0.05)

    def update_dice_display(self, delta_time):
        """Called to update the display"""
        # We icnrement over the random values each time it is called
        if self.current_roll_index < len(self.dice_rolls):
            roll = self.dice_rolls[self.current_roll_index]
            dice_chars = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
            self.dice_text = f"{dice_chars[roll[0]-1]} {dice_chars[roll[1]-1]}"
            self.current_roll_index += 1
        else: # We're finished
            # Advance the current player the final number on the dice
            self.players.add_spaces(self.players.current_player, sum(self.dice_rolls[-1]))

            # Next player's turn (for now)
            self.players.next_player()
            self.can_roll = True

            arcade.unschedule(self.update_dice_display)

# End game screen
class GameOverView(arcade.View):
    def on_show_view(self):
        """This will be called when the view is switched to."""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """Handle drawing of this view."""
        self.clear()
        arcade.draw_text("Game Over - press ESCAPE to advance", common.app.width / 2, common.app.height / 2, arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """Handle key presses."""
        # Change to main menu view on Escape
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["main_menu"])


def init():
    """Initialize the window and display view system."""
    window = arcade.Window(common.app.width, common.app.height, "Monopoly", vsync=True)

    # Create instances of all views and store the views in a dictionary on the window for easy access
    window.views = {
        "main_menu":  MainMenuView(),
        "help":       HelpView(),
        "game_setup": GameSetupView(),
        "game":       GameView(),
        "game_over":  GameOverView(),
    }

    # Start with the main menu view
    window.show_view(window.views["main_menu"])
    arcade.run()
