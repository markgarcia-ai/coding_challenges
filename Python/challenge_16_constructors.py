"""
Challenge 16: Constructors (__init__)

Problem Statement:
Create a `Player` class for a game. The constructor (`__init__` method) should set up the initial state of each player object, such as their name and starting health.

Requirements:
- Create a class named `Player`.
- The `__init__` method should be the constructor.
- The constructor should accept a `name` as an argument.
- Inside the constructor, it should initialize two instance attributes:
  - `self.name` should be set to the `name` argument.
  - `self.health` should be set to a default value of `100`.
- Create a `show_info()` method to display the player's name and health.

Solution:
"""

class Player:
    """Represents a player in a game."""
    
    # This is the constructor method.
    def __init__(self, name):
        """
        This method is called automatically when a new Player object is created.
        It initializes the object's attributes.
        """
        print(f"A new player, '{name}', has joined the game!")
        self.name = name
        self.health = 100  # Default starting health

    def show_info(self):
        """Displays the player's current status."""
        print(f"Player: {self.name}, Health: {self.health}")

# Example usage:
if __name__ == "__main__":
    # When we create an instance, the __init__ method is called automatically.
    player1 = Player("KnightRider")
    player2 = Player("ShadowFox")
    
    # Each player instance has its own name and health, set by the constructor.
    player1.show_info()
    player2.show_info()

"""
Expected Output:

A new player, 'KnightRider', has joined the game!
A new player, 'ShadowFox', has joined the game!
Player: KnightRider, Health: 100
Player: ShadowFox, Health: 100
""" 