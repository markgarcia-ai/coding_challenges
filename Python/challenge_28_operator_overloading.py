"""
Challenge 28: Operator Overloading

Problem Statement:
Create a `Vector` class that represents a 2D vector. Overload the addition (`+`) and subtraction (`-`) operators to perform vector addition and subtraction.

Requirements:
- Create a class named `Vector`.
- The constructor `__init__` should take `x` and `y` coordinates.
- Overload the `+` operator by implementing the `__add__` method. It should take another `Vector` object and return a *new* `Vector` object representing the sum.
- Overload the `-` operator by implementing the `__sub__` method. It should also return a new `Vector` object.
- Implement the `__repr__` method to provide a developer-friendly string representation of the vector (e.g., `Vector(x=2, y=3)`).

Solution:
"""

class Vector:
    """A 2D vector class that supports addition and subtraction."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloads the + operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        """Overloads the - operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __repr__(self):
        """Provides the official string representation."""
        return f"Vector(x={self.x}, y={self.y})"

# Example usage:
if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(5, 1)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    
    # Use the overloaded '+' operator
    v_sum = v1 + v2
    print(f"v1 + v2 = {v_sum}")
    
    # Use the overloaded '-' operator
    v_diff = v1 - v2
    print(f"v1 - v2 = {v_diff}")

"""
Expected Output:

Vector 1: Vector(x=2, y=3)
Vector 2: Vector(x=5, y=1)
v1 + v2 = Vector(x=7, y=4)
v1 - v2 = Vector(x=-3, y=2)
""" 