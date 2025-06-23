"""
Challenge 9: Methods

Problem Statement:
Create a `Calculator` class with methods to perform basic arithmetic operations: addition, subtraction, multiplication, and division. Methods are functions that belong to an object.

Requirements:
- Create a class named `Calculator`.
- The `__init__` method should initialize a `current_value` attribute, starting at 0.
- Create an `add(self, number)` method that adds a number to `current_value`.
- Create a `subtract(self, number)` method that subtracts a number from `current_value`.
- Create a `multiply(self, number)` method that multiplies `current_value` by a number.
- Create a `get_value(self)` method that returns the `current_value`.

Solution:
"""

class Calculator:
    """A simple calculator class to demonstrate methods."""
    def __init__(self):
        self.current_value = 0

    def add(self, number):
        """Method to add a number to the current value."""
        self.current_value += number

    def subtract(self, number):
        """Method to subtract a number from the current value."""
        self.current_value -= number

    def multiply(self, number):
        """Method to multiply the current value by a number."""
        self.current_value *= number
        
    def get_value(self):
        """Method to get the current value."""
        return self.current_value

# Example usage:
if __name__ == "__main__":
    # Create an instance (object) of the Calculator class
    calc = Calculator()
    
    print(f"Initial value: {calc.get_value()}")
    
    # Call the methods on the object
    calc.add(10)
    print(f"After adding 10: {calc.get_value()}")
    
    calc.subtract(3)
    print(f"After subtracting 3: {calc.get_value()}")
    
    calc.multiply(5)
    print(f"After multiplying by 5: {calc.get_value()}")

"""
Expected Output:

Initial value: 0
After adding 10: 10
After subtracting 3: 7
After multiplying by 5: 35
""" 