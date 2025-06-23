"""
Challenge 13: Composition (Has-A Relationship)

Problem Statement:
Model a car using composition. A `Car` "has-a" `Engine`. The `Engine` is an essential part of the `Car`, and its lifecycle is managed by the `Car` class.

Requirements:
- Create an `Engine` class with a `start()` method that returns "Engine started".
- Create a `Car` class.
- In the `Car` class's `__init__` method, create an instance of the `Engine` class and store it as an attribute (e.g., `self.engine`). This demonstrates composition.
- The `Car` class should have a `start()` method that delegates the action to its `engine` object.

Solution:
"""

class Engine:
    """A simple Engine class for a car."""
    def start(self):
        return "Engine started... Vroom!"

class Car:
    """A Car class that contains an Engine object."""
    def __init__(self, model):
        self.model = model
        # The Engine is created when the Car is created.
        self.engine = Engine()

    def start(self):
        """Starts the car by starting its engine."""
        print(f"Starting the {self.model}...")
        engine_status = self.engine.start()
        print(engine_status)

# Example usage:
if __name__ == "__main__":
    my_car = Car("Tesla Model S")
    my_car.start()
    
    # Note that the Engine object is part of the Car object.
    # If my_car is destroyed, its engine instance is also destroyed.

"""
Expected Output:

Starting the Tesla Model S...
Engine started... Vroom!
""" 