"""
Challenge 10: Inheritance

Problem Statement:
Create a `Vehicle` base class and a `Car` subclass that inherits from it. The `Car` subclass should inherit the methods of `Vehicle` and also have its own specific method.

Requirements:
- Create a base class `Vehicle` with:
  - An `__init__` method that takes `brand` and `year`.
  - A `display_info()` method that prints the brand and year.
- Create a `Car` class that inherits from `Vehicle`.
- The `Car` class should have its own method, `honk()`, which prints "Honk honk!".
- Demonstrate that an instance of `Car` can use both its own `honk()` method and the inherited `display_info()` method.

Solution:
"""

class Vehicle:
    """A base class for all vehicles."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.brand}")

class Car(Vehicle):
    """A subclass representing a car."""
    def honk(self):
        print("Honk honk!")

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Car class
    my_car = Car("Toyota", 2021)
    
    # Call the inherited method from the Vehicle class
    my_car.display_info()
    
    # Call the method specific to the Car class
    my_car.honk()

"""
Expected Output:

Vehicle Info: 2021 Toyota
Honk honk!
""" 