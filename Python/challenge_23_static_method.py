"""
Challenge 23: Static Method

Problem Statement:
Create a `MathUtils` class that contains a static method for calculating the area of a circle. A static method belongs to the class itself, not to any instance, and cannot modify class or instance state. It's like a regular function that is namespaced within the class.

Requirements:
- Create a class named `MathUtils`.
- Define a static method `circle_area(radius)` inside the class. You must use the `@staticmethod` decorator.
- The method should accept one argument, `radius`, and return the area of a circle (Area = π * r^2). You can use `3.14159` for π.
- Demonstrate that you can call this method directly on the class (`MathUtils.circle_area(...)`) without creating an instance of the class.

Solution:
"""
import math

class MathUtils:
    """A utility class for mathematical calculations."""
    
    @staticmethod
    def circle_area(radius):
        """
        Calculates the area of a circle.
        This is a static method because it doesn't need 'self' or 'cls'.
        """
        if radius < 0:
            return 0
        return math.pi * (radius ** 2)

# Example usage:
if __name__ == "__main__":
    # Call the static method directly on the class
    radius1 = 5
    area1 = MathUtils.circle_area(radius1)
    print(f"The area of a circle with radius {radius1} is: {area1:.2f}")

    radius2 = 10
    area2 = MathUtils.circle_area(radius2)
    print(f"The area of a circle with radius {radius2} is: {area2:.2f}")

"""
Expected Output:

The area of a circle with radius 5 is: 78.54
The area of a circle with radius 10 is: 314.16
""" 