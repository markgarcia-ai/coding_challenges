"""
Challenge 37: Properties (@property)

Problem Statement:
Create a `Temperature` class that stores a temperature in Celsius. Use the `@property` decorator to create a getter for a `fahrenheit` attribute that dynamically converts the Celsius temperature to Fahrenheit. This allows you to access `temp.fahrenheit` as if it were an attribute, but it's calculated on the fly.

Requirements:
- Create a class named `Temperature`.
- The `__init__` constructor should take a temperature in `celsius`.
- Create a method `fahrenheit(self)` and decorate it with `@property`.
- This method should calculate and return the temperature in Fahrenheit using the formula: `F = C * 9/5 + 32`.
- Demonstrate that you can access `fahrenheit` like an attribute.

Solution:
"""

class Temperature:
    """A class to represent temperature, with a property for Fahrenheit conversion."""
    def __init__(self, celsius):
        self._celsius = celsius  # Use a "private" attribute

    @property
    def fahrenheit(self):
        """
        This is the property. It acts like a getter method.
        It's accessed like an attribute: temp.fahrenheit
        """
        return (self._celsius * 9/5) + 32

# Example usage:
if __name__ == "__main__":
    t1 = Temperature(0)
    t2 = Temperature(25)
    t3 = Temperature(100)
    
    # Access the fahrenheit property as if it were a stored attribute
    print(f"0 degrees Celsius is {t1.fahrenheit:.1f} degrees Fahrenheit.")
    print(f"25 degrees Celsius is {t2.fahrenheit:.1f} degrees Fahrenheit.")
    print(f"100 degrees Celsius is {t3.fahrenheit:.1f} degrees Fahrenheit.")

"""
Expected Output:

0 degrees Celsius is 32.0 degrees Fahrenheit.
25 degrees Celsius is 77.0 degrees Fahrenheit.
100 degrees Celsius is 212.0 degrees Fahrenheit.
""" 