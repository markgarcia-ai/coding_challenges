"""
Challenge 47: Passing Objects to Functions

Problem Statement:
Create a `Robot` class and a standalone function that interacts with `Robot` objects. This will show how objects can be passed to functions as arguments, allowing the function to access the object's attributes and methods.

Requirements:
- Create a class named `Robot` with:
  - An `__init__` method that initializes a `name` and `position` (e.g., starting at 0).
  - A `move(self, distance)` method that updates the robot's position.
  - A `report_position(self)` method that prints the robot's name and current position.
- Create a standalone function `teleport_robot(robot_object, new_position)` that:
  - Takes a `Robot` object and a `new_position` as arguments.
  - Directly changes the robot's `position` attribute to the `new_position`.
  - Prints a message indicating the teleportation occurred.

Solution:
"""

class Robot:
    """Represents a simple robot."""
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, distance):
        self.position += distance
        print(f"{self.name} moved by {distance}.")

    def report_position(self):
        print(f"{self.name} is at position {self.position}.")

def teleport_robot(robot_object, new_position):
    """
    A standalone function that takes a Robot object and modifies its state.
    """
    print(f"--- Teleporting {robot_object.name} ---")
    robot_object.position = new_position
    print(f"{robot_object.name} has been teleported!")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Robot class
    r1 = Robot("R2-D2")
    r1.report_position()
    
    # Use the object's own method to change its state
    r1.move(10)
    r1.report_position()
    
    # Pass the robot object to the standalone function to change its state
    teleport_robot(r1, 100)
    r1.report_position()

"""
Expected Output:

R2-D2 is at position 0.
R2-D2 moved by 10.
R2-D2 is at position 10.
--- Teleporting R2-D2 ---
R2-D2 has been teleported!
R2-D2 is at position 100.
""" 