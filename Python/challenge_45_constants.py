"""
Challenge 45: Constants

Problem Statement:
Create a file to store application-wide constants. Then, create a simple program that uses these constants to perform a calculation. This pattern is useful for managing "magic numbers" and configuration values in a single, easy-to-manage location.

Requirements:
1.  Create a file named `constants.py`.
    -   In this file, define two constants:
        -   `PI` with a value of `3.14159`.
        -   `GRAVITY` (Earth's gravity in m/s^2) with a value of `9.81`.
2.  Create a main script file.
    -   Import the constants from `constants.py`.
    -   Create a function `calculate_circle_area(radius)` that uses the `PI` constant.
    -   Create a function `calculate_fall_time(height)` that uses the `GRAVITY` constant (formula: t = sqrt(2h/g)).
    -   Use these functions and print the results.

Solution:
"""

# ============== constants.py ==============
# In a real scenario, this would be in a separate file.

PI = 3.14159
GRAVITY = 9.81

# ============ main_script.py ============
# In a real scenario, this would be in your main application file.

# from constants import PI, GRAVITY  <- This is how you would import
import math

def calculate_circle_area(radius):
    """Calculates the area of a circle using the imported PI constant."""
    return PI * (radius ** 2)

def calculate_fall_time(height):
    """Calculates the time for an object to fall from a certain height."""
    return math.sqrt((2 * height) / GRAVITY)

# Example usage:
if __name__ == "__main__":
    circle_radius = 5
    fall_height = 100
    
    area = calculate_circle_area(circle_radius)
    time = calculate_fall_time(fall_height)
    
    print(f"Using PI = {PI}")
    print(f"Area of a circle with radius {circle_radius}: {area:.2f}")
    
    print(f"\nUsing GRAVITY = {GRAVITY}")
    print(f"Time for an object to fall from {fall_height} meters: {time:.2f} seconds")

"""
Expected Output:

Using PI = 3.14159
Area of a circle with radius 5: 78.54

Using GRAVITY = 9.81
Time for an object to fall from 100 meters: 4.52 seconds
""" 