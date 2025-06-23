"""
Challenge 5: Functions

Problem Statement:
Write a function that calculates the area of a rectangle. The function should have default values for its parameters.

Requirements:
- The function should be named `calculate_rectangle_area`.
- It should accept two arguments: `width` and `height`.
- Provide default values of `1` for both `width` and `height`.
- The function should return the calculated area (`width * height`).
- Demonstrate calling the function with different combinations of arguments (no arguments, one argument, two arguments).

Solution:
"""

def calculate_rectangle_area(width=1, height=1):
    """
    Calculates the area of a rectangle with default dimensions.
    """
    return width * height

# Example usage:
if __name__ == "__main__":
    # Call with no arguments (uses both defaults)
    area1 = calculate_rectangle_area()
    print(f"Area with default width and height: {area1}")
    
    # Call with one argument (overrides width, uses default height)
    area2 = calculate_rectangle_area(5)
    print(f"Area with width=5 and default height: {area2}")
    
    # Call with two arguments (overrides both defaults)
    area3 = calculate_rectangle_area(4, 5)
    print(f"Area with width=4 and height=5: {area3}")

"""
Expected Output:

Area with default width and height: 1
Area with width=5 and default height: 5
Area with width=4 and height=5: 20
""" 