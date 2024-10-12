"""
Code which handles information and logic related to the board itself.

Authors: Daniel Smith, Bo Tang, and Nathan Spriggs
"""

import random


class MonopolyBoard:
    """Initialization data and logic for the board of the game itself"""
    def __init__(self):
        # Initialize the board with properties
        self.properties = [
            {"houses": None, "group": None, "space_num": 1,    "name": "Go",                   "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": 0,    "group": 1,    "space_num": 2,    "name": "Mediterranean Avenue", "owner": None, "price": 60,   "rent-t0.1": 2,    "rent-t0.2": 4,    "rent-t0.3": None, "rent-t0.4": None, "rent-t1": 10,   "rent-t2": 30,   "rent-t3": 90,   "rent-t4": 160,  "rent-t5": 250,  "type": "property"},
            {"houses": None, "group": None, "space_num": 3,    "name": "Community Chest",      "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 1,    "space_num": 4,    "name": "Baltic Avenue",        "owner": None, "price": 60,   "rent-t0.1": 4,    "rent-t0.2": 8,    "rent-t0.3": None, "rent-t0.4": None, "rent-t1": 20,   "rent-t2": 60,   "rent-t3": 180,  "rent-t4": 320,  "rent-t5": 450,  "type": "property"},
            {"houses": None, "group": None, "space_num": 5,    "name": "Income Tax",           "owner": 0,    "price": None, "rent-t0.1": 200,  "rent-t0.2": 200,  "rent-t0.3": 200,  "rent-t0.4": 200,  "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": None, "group": 9,    "space_num": 6,    "name": "Reading Railroad",     "owner": None, "price": 200,  "rent-t0.1": 25,   "rent-t0.2": 50,   "rent-t0.3": 100,  "rent-t0.4": 200,  "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "railroad"},
            {"houses": 0,    "group": 2,    "space_num": 7,    "name": "Oriental Avenue",      "owner": None, "price": 100,  "rent-t0.1": 6,    "rent-t0.2": 6,    "rent-t0.3": 12,   "rent-t0.4": None, "rent-t1": 30,   "rent-t2": 90,   "rent-t3": 270,  "rent-t4": 400,  "rent-t5": 550,  "type": "property"},
            {"houses": None, "group": None, "space_num": 8,    "name": "Chance",               "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 2,    "space_num": 9,    "name": "Vermont Avenue",       "owner": None, "price": 100,  "rent-t0.1": 6,    "rent-t0.2": 6,    "rent-t0.3": 12,   "rent-t0.4": None, "rent-t1": 30,   "rent-t2": 90,   "rent-t3": 270,  "rent-t4": 400,  "rent-t5": 550,  "type": "property"},
            {"houses": 0,    "group": 2,    "space_num": 10,   "name": "Connecticut Avenue",   "owner": None, "price": 120,  "rent-t0.1": 8,    "rent-t0.2": 8,    "rent-t0.3": 16,   "rent-t0.4": None, "rent-t1": 40,   "rent-t2": 100,  "rent-t3": 300,  "rent-t4": 450,  "rent-t5": 600,  "type": "property"},
            {"houses": None, "group": None, "space_num": 11,   "name": "Jail",                 "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": 0,    "group": 3,    "space_num": 12,   "name": "St. Charles Place",    "owner": None, "price": 140,  "rent-t0.1": 10,   "rent-t0.2": 10,   "rent-t0.3": 20,   "rent-t0.4": None, "rent-t1": 50,   "rent-t2": 150,  "rent-t3": 450,  "rent-t4": 625,  "rent-t5": 750,  "type": "property"},
            {"houses": None, "group": 10,   "space_num": 13,   "name": "Electric Company",     "owner": None, "price": 50,   "rent-t0.1": 100,  "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "utility" },
            {"houses": 0,    "group": 3,    "space_num": 14,   "name": "States Avenue",        "owner": None, "price": 140,  "rent-t0.1": 10,   "rent-t0.2": 10,   "rent-t0.3": 20,   "rent-t0.4": None, "rent-t1": 50,   "rent-t2": 150,  "rent-t3": 450,  "rent-t4": 625,  "rent-t5": 750,  "type": "property"},
            {"houses": 0,    "group": 3,    "space_num": 15,   "name": "Virginia Avenue",      "owner": None, "price": 160,  "rent-t0.1": 12,   "rent-t0.2": 12,   "rent-t0.3": 24,   "rent-t0.4": None, "rent-t1": 60,   "rent-t2": 180,  "rent-t3": 500,  "rent-t4": 700,  "rent-t5": 900,  "type": "property"},
            {"houses": None, "group": 9,    "space_num": 16,   "name": "Pennsylvania Railroad","owner": None, "price": 200,  "rent-t0.1": 25,   "rent-t0.2": 50,   "rent-t0.3": 100,  "rent-t0.4": 200,  "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "railroad"},
            {"houses": 0,    "group": 4,    "space_num": 17,   "name": "St. James Place",      "owner": None, "price": 180,  "rent-t0.1": 14,   "rent-t0.2": 14,   "rent-t0.3": 28,   "rent-t0.4": None, "rent-t1": 70,   "rent-t2": 200,  "rent-t3": 550,  "rent-t4": 750,  "rent-t5": 950,  "type": "property"},
            {"houses": None, "group": None, "space_num": 18,   "name": "Community Chest",      "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 4,    "space_num": 19,   "name": "Tennessee Avenue",     "owner": None, "price": 180,  "rent-t0.1": 14,   "rent-t0.2": 14,   "rent-t0.3": 28,   "rent-t0.4": None, "rent-t1": 70,   "rent-t2": 200,  "rent-t3": 550,  "rent-t4": 750,  "rent-t5": 950,  "type": "property"},
            {"houses": 0,    "group": 4,    "space_num": 20,   "name": "New York Avenue",      "owner": None, "price": 200,  "rent-t0.1": 16,   "rent-t0.2": 16,   "rent-t0.3": 32,   "rent-t0.4": None, "rent-t1": 80,   "rent-t2": 220,  "rent-t3": 600,  "rent-t4": 800,  "rent-t5": 1000, "type": "property"},
            {"houses": None, "group": None, "space_num": 21,   "name": "Free Parking",         "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": 0,    "group": 5,    "space_num": 22,   "name": "Kentucky Avenue",      "owner": None, "price": 220,  "rent-t0.1": 18,   "rent-t0.2": 18,   "rent-t0.3": 26,   "rent-t0.4": None, "rent-t1": 90,   "rent-t2": 250,  "rent-t3": 700,  "rent-t4": 875,  "rent-t5": 1050, "type": "property"},
            {"houses": None, "group": None, "space_num": 23,   "name": "Chance",               "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 5,    "space_num": 24,   "name": "Indiana Avenue",       "owner": None, "price": 220,  "rent-t0.1": 18,   "rent-t0.2": 18,   "rent-t0.3": 36,   "rent-t0.4": None, "rent-t1": 90,   "rent-t2": 250,  "rent-t3": 700,  "rent-t4": 875,  "rent-t5": 1050, "type": "property"},
            {"houses": 0,    "group": 5,    "space_num": 25,   "name": "Illinois Avenue",      "owner": None, "price": 240,  "rent-t0.1": 20,   "rent-t0.2": 20,   "rent-t0.3": 40,   "rent-t0.4": None, "rent-t1": 100,  "rent-t2": 300,  "rent-t3": 750,  "rent-t4": 925,  "rent-t5": 1100, "type": "property"},
            {"houses": None, "group": 9,    "space_num": 26,   "name": "B. & O. Railroad",     "owner": None, "price": 200,  "rent-t0.1": 25,   "rent-t0.2": 50,   "rent-t0.3": 100,  "rent-t0.4": 200,  "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "railroad"},
            {"houses": 0,    "group": 6,    "space_num": 27,   "name": "Atlantic Avenue",      "owner": None, "price": 260,  "rent-t0.1": 22,   "rent-t0.2": 22,   "rent-t0.3": 44,   "rent-t0.4": None, "rent-t1": 110,  "rent-t2": 330,  "rent-t3": 800,  "rent-t4": 975,  "rent-t5": 1150, "type": "property"},
            {"houses": 0,    "group": 6,    "space_num": 28,   "name": "Ventor Avenue",        "owner": None, "price": 260,  "rent-t0.1": 22,   "rent-t0.2": 22,   "rent-t0.3": 44,   "rent-t0.4": None, "rent-t1": 110,  "rent-t2": 330,  "rent-t3": 800,  "rent-t4": 975,  "rent-t5": 1150, "type": "property"},
            {"houses": None, "group": 10,   "space_num": 29,   "name": "Water Works",          "owner": None, "price": 50,   "rent-t0.1": 40,   "rent-t0.2": 100,  "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "utility" },
            {"houses": None, "group": 6,    "space_num": 30,   "name": "Marvin Gardens",       "owner": None, "price": 280,  "rent-t0.1": 24,   "rent-t0.2": 24,   "rent-t0.3": 48,   "rent-t0.4": None, "rent-t1": 120,  "rent-t2": 360,  "rent-t3": 850,  "rent-t4": 1025, "rent-t5": 1200, "type": "property"},
            {"houses": None, "group": None, "space_num": 31,   "name": "Go to Jail",           "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": 0,    "group": 7,    "space_num": 32,   "name": "Pacific Avenue",       "owner": None, "price": 300,  "rent-t0.1": 26,   "rent-t0.2": 26,   "rent-t0.3": 52,   "rent-t0.4": None, "rent-t1": 130,  "rent-t2": 390,  "rent-t3": 900,  "rent-t4": 1100, "rent-t5": 1275, "type": "property"},
            {"houses": 0,    "group": 7,    "space_num": 33,   "name": "North Carolina Avenue","owner": None, "price": 300,  "rent-t0.1": 26,   "rent-t0.2": 26,   "rent-t0.3": 52,   "rent-t0.4": None, "rent-t1": 130,  "rent-t2": 390,  "rent-t3": 900,  "rent-t4": 1100, "rent-t5": 1275, "type": "property"},
            {"houses": None, "group": None, "space_num": 34,   "name": "Community Chest",      "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 7,    "space_num": 35,   "name": "Pennsylvania Avenue",  "owner": None, "price": 320,  "rent-t0.1": 28,   "rent-t0.2": 28,   "rent-t0.3": 56,   "rent-t0.4": None, "rent-t1": 150,  "rent-t2": 450,  "rent-t3": 1000, "rent-t4": 1200, "rent-t5": 1400, "type": "property"},
            {"houses": None, "group": 9,    "space_num": 36,   "name": "Short Line Railroad",  "owner": None, "price": 200,  "rent-t0.1": 25,   "rent-t0.2": 50,   "rent-t0.3": 100,  "rent-t0.4": 200,  "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "railroad"},
            {"houses": None, "group": None, "space_num": 37,   "name": "Chance",               "owner": 0,    "price": None, "rent-t0.1": 0,    "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "card"    },
            {"houses": 0,    "group": 8,    "space_num": 38,   "name": "Park Place",           "owner": None, "price": 350,  "rent-t0.1": 35,   "rent-t0.2": 70,   "rent-t0.3": None, "rent-t0.4": None, "rent-t1": 175,  "rent-t2": 500,  "rent-t3": 1100, "rent-t4": 1300, "rent-t5": 1500, "type": "property"},
            {"houses": None, "group": None, "space_num": 39,   "name": "Luxury Tax",           "owner": 0,    "price": None, "rent-t0.1": 75,   "rent-t0.2": None, "rent-t0.3": None, "rent-t0.4": None, "rent-t1": None, "rent-t2": None, "rent-t3": None, "rent-t4": None, "rent-t5": None, "type": "special" },
            {"houses": 0,    "group": 8,    "space_num": 40,   "name": "Boardwalk",            "owner": None, "price": 400,  "rent-t0.1": 50,   "rent-t0.2": 100,  "rent-t0.3": None, "rent-t0.4": None, "rent-t1": 200,  "rent-t2": 600,  "rent-t3": 1400, "rent-t4": 1700, "rent-t5": 2000, "type": "property"},
        ]

    def property_by_space_num(self, space_num):
        """Get the property at the given space_num."""
        # Allows indexing by space_num instead of dictionary order
        for property in self.properties:
            if property["space_num"] == space_num:
                return property

        # If it's not found raise an error
        raise ValueError("Invalid space number")

    def properties_by_group(self, group):
        """Get all properties in the given group."""
        return [prop for prop in self.properties if prop.get("group") == group]

    def set_owner(self, space_num, player_number):
        """Set the owner of the property at the given space_num."""
        prop = self.property_by_space_num(space_num)
        if prop:
            prop["owner"] = player_number

            return

        # If it's not found raise an error
        raise ValueError("Invalid space number")

    def add_house(self, space_num):
        """Add a house to all properties in the group of the property at the given space_num. This will ensure that houses are built evenly across the group. Does nothing if any property already has 5 houses."""
        prop = self.property_by_space_num(space_num)
        if not prop:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        # If property is not part of a group or can't have houses, return
        group = prop.get("group")
        if group is None or prop.get("houses") is None:
            return

        group_properties = self.properties_by_group(group)

        # Can't upgrade past 5 houses
        if any(p["houses"] >= 5 for p in group_properties):
            return

        # Add a house to each property
        for p in group_properties:
            p["houses"] += 1

    def land_action(self, player_number, space_num):
        """Return what type of action needs to happen."""
        # Look up the space and bail if it's not found
        space = self.property_by_space_num(space_num)
        if not space:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        space_type = space["type"]
        owner = space.get("owner")

        # If the player already owns the space, no action is needed
        if owner == player_number:
            return "no_action"

        # Different space types will need different actions
        match space_type:
            # Spaces where ownership and rent apply
            case "property" | "railroad" | "utility":
                # Check if it's buyable
                if owner == 0:
                    return "buy_space_option"
                # Already checked if player owns space so otherwise some form of rent is due
                return "pay_rent"
            case "card":
                # Only 2 known types of cards to draw
                if space["name"] == "Chance":
                    return "draw_chance_card"
                if space["name"] == "Community Chest":
                    return "draw_community_chest_card"
                return "unknown_card"
            # Special are permanently board owned spaces like Go or Free Parking
            case "special":
                match space["name"]:
                    case "Income Tax" | "Luxury Tax":
                        return "pay_tax"
                    case "Go to Jail":
                        return "move_to_jail"
                    case _:
                        return "do_nothing"
            case _:
                return "unknown_action"

    def full_group(self, space_num):
        """Check if a player owns all properties of the group."""
        # Only works for valid space numbers
        space = self.property_by_space_num(space_num)
        if not space:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        # Unpurchaseable or unpurchased spaces can't form a group
        owner = space["owner"]
        if owner == 0 or owner is None:
            return False

        # Not all spaces are in a group
        group = space["group"]
        if group is None:
            return False

        # Otherwise, we can check if all spaces are owned by the same ownper
        group_spaces = self.properties_by_group(group)
        return all(p["owner"] == owner for p in group_spaces)

    def house_count(self, space_num):
        """Gets the number of houses for the property at the given space_num."""
        prop = self.property_by_space_num(space_num)
        if not prop:
            # If it's not found raise an error
            raise ValueError("Invalid space number")
        return prop.get("houses", 0) if prop else 0

    def group_property_count(self, group):
        """Helper function to return the number of properties in a group."""
        return len(self.properties_by_group(group))

    def can_buy_houses(self, space_num, cash):
        """Determine if the current space can have houses bought given the amount of cash."""
        # Only works for valid spaces
        prop = self.property_by_space_num(space_num)
        if not prop:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        # Can only buy houses on property spaces
        if prop.get("type") != "property":
            return False

        # Can't buy more than 5 houses. None means a property where houses can't be purchased, 0 is no houses but can be.
        houses = prop.get("houses")
        if houses is None or houses >= 5:
            return False

        # Can only buy houses on properties in group
        group = prop.get("group")
        if group is None:
            return False

        # Can only buy houses when it's a full group
        if not self.full_group(space_num):
            return False

        # Check we have enough money to buy houses for every place in the group
        house_cost = 50 * self.group_property_count(group)
        return cash >= house_cost

    def can_buy_space(self, space_num, cash):
        """Determine if the current space is purchasable given the amount of cash."""
        # Must be a valid space
        prop = self.property_by_space_num(space_num)
        if not prop:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        # Can only buy spaces owned by the board that are sellable (i.e. not None or other players)
        if prop.get("owner") != 0:
            return False

        return cash >= prop.get("price")

    def rent_cost(self, space_num, player_number):
        """Determine the cost of rent for the given player landing on the space space_num."""
        # must be a valid space
        prop = self.property_by_space_num(space_num)
        if not prop:
            # If it's not found raise an error
            raise ValueError("Invalid space number")

        # Players don't pay their own rent
        owner = prop.get("owner")
        if owner == player_number:
            return 0
        # Or rent to beyable spaces
        if owner == 0:
            return 0

        # Houses factor in
        houses = prop.get("houses", 0)
        if houses == 0:
            # When 0 houses the group size matters
            group = prop.get("group")
            if group is None:
                rent_key = "rent-t0.1"
            else:
                group_properties = self.properties_by_group(group)
                owned_properties = sum(1 for p in group_properties if p.get("owner") == owner)
                rent_key = f"rent-t0.{owned_properties}"
        else:
            # when > 0 houses the number of houses matters
            rent_key = f"rent-t{houses}"

        return prop.get(rent_key)


board = MonopolyBoard();


def draw_card(type):
    """Draw a random card based on the type"""
    chance = [
        "Advance to Boardwalk.",
        "Advance to Go (Collect $200).",
        "Advance to Illinois Avenue. If you pass Go, collect $200.",
        "Advance to St. Charles Place. If you pass Go, collect $200.",
        "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled.",
        "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled.",
        "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
        "Bank pays you dividend of $50.",
        "Get Out of Jail Free.",
        "Go Back 3 Spaces.",
        "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200.",
        "Make general repairs on all your property. For each house pay $25. For each hotel pay $100.",
        "Speeding fine $15.",
        "Take a trip to Reading Railroad. If you pass Go, collect $200.",
        "You have been elected Chairman of the Board. Pay each player $50.",
        "Your building loan matures. Collect $150",
    ]

    community = [
        "Community Chest",
        "Advance to Go (Collect $200)",
        "Bank error in your favor. Collect $200",
        "Doctor’s fee. Pay $50",
        "From sale of stock you get $50",
        "Get Out of Jail Free",
        "Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
        "Holiday fund matures. Receive $100",
        "Income tax refund. Collect $20",
        "It is your birthday. Collect $10 from every player",
        "Life insurance matures. Collect $100",
        "Pay hospital fees of $100",
        "Pay school fees of $50",
        "Receive $25 consultancy fee",
        "You are assessed for street repair. $40 per house. $115 per hotel",
        "You have won second prize in a beauty contest. Collect $10",
        "You inherit $100",
    ]

    # 2 types of cards so we try to leniently match which based on the type argument
    if(type.lower() == "chance"):
        return random.choice(chance)
    if(type.lower() == "community chest" or type.lower() == "community" or type.lower() == "chest"):
        return random.choice(community)

    raise ValueError("Invalid card type")

class PlayerInfo:
    """Initialization data and logic for the board of the game itself"""
    def __init__(self, count):
        self.validate_count(count)
        self.total_players = count
        self.current_player = 1
        self.space_number = {i: 1 for i in range(1, count + 1)}
        self.cash = {i: 1500 for i in range(1, count + 1)}

    def validate_count(self, count):
        if not isinstance(count, int):
            raise TypeError("Player count must be an integer")
        if count < 2 or count > 4:
            raise ValueError("Player count must be between 2 and 4")

    def next_player(self):
        self.current_player = self.current_player % self.total_players + 1
        return self.current_player

    def player_cash(self, player_number):
        self.validate_player_number(player_number)
        return self.cash[player_number]

    def player_space(self, player_number):
        self.validate_player_number(player_number)
        return self.space_number[player_number]

    def validate_player_number(self, player_number):
        if not isinstance(player_number, int):
            raise TypeError("Player number must be an integer")
        if player_number < 1 or player_number > self.total_players:
            raise ValueError(f"Player number must be between 1 and {self.total_players}")
