"""
Challenge 26: Abstract Classes

Problem Statement:
Create an abstract base class `Shape` that defines a common interface for all shapes. Then, create concrete subclasses `Circle` and `Rectangle` that implement the interface. Abstract classes ensure that subclasses implement required methods.

Requirements:
- Use the `abc` module to create an abstract class.
- The `Shape` class should be an abstract base class (inherit from `ABC`).
- `Shape` should have an abstract method named `area()`.
- Create two concrete classes, `Circle` and `Rectangle`, that inherit from `Shape`.
- Both `Circle` and `Rectangle` must implement the `area()` method.
  - `Circle` will need a `radius` and its area is `pi * r^2`.
  - `Rectangle` will need `width` and `height`, and its area is `w * h`.
- Attempting to instantiate `Shape` directly should raise a `TypeError`.

Solution:
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for geometric shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

# Example usage:
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]
    
    for shape in shapes:
        # Note: The type of shape is not checked. We just call area().
        print(f"The area of a {type(shape).__name__} is {shape.area():.2f}")
        
    # This line should raise a TypeError because Shape is abstract
    try:
        abstract_shape = Shape()
    except TypeError as e:
        print(f"\nError trying to instantiate Shape: {e}")

"""
Expected Output:

The area of a Circle is 78.54
The area of a Rectangle is 24.00

Error trying to instantiate Shape: Can't instantiate abstract class Shape with abstract method area
""" 