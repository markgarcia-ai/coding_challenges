"""
Challenge 49: Unit Test (unittest)

Problem Statement:
Write a simple function that adds two numbers and then write a set of unit tests for it using the `unittest` module to verify its correctness.

Requirements:
1.  **The function to test:**
    -   Create a standalone function `add(a, b)` that returns the sum of `a` and `b`. Save this in a file named `simple_math.py`.

2.  **The test file:**
    -   Create a separate file `test_simple_math.py`.
    -   Import the `unittest` module and the `add` function.
    -   Create a test class that inherits from `unittest.TestCase`.
    -   Write test methods inside the class (names must start with `test_`).
        -   A test for adding two positive numbers.
        -   A test for adding a positive and a negative number.
        -   A test for adding two negative numbers.
    -   Use assertion methods like `self.assertEqual()` to check the results.
    -   Include the standard `if __name__ == '__main__': unittest.main()` block to run the tests.

Solution:
"""

# Step 1: Create the file 'simple_math.py' with this content:

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b


# Step 2: Create the file 'test_simple_math.py' with this content:

import unittest
# from simple_math import add  # Uncomment this line if running as a separate file

# --- For demonstration, we'll include the function in the same file ---
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
# --------------------------------------------------------------------

class TestAddFunction(unittest.TestCase):
    """
    Test suite for the add function.
    """

    def test_add_positive_numbers(self):
        """Test that adding two positive numbers works correctly."""
        print("Running test_add_positive_numbers...")
        self.assertEqual(add(5, 10), 15)

    def test_add_positive_and_negative(self):
        """Test adding a positive and a negative number."""
        print("Running test_add_positive_and_negative...")
        self.assertEqual(add(-5, 10), 5)

    def test_add_negative_numbers(self):
        """Test that adding two negative numbers works correctly."""
        print("Running test_add_negative_numbers...")
        self.assertEqual(add(-5, -10), -15)

# This block allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""
To run from the command line (assuming two separate files):
python -m unittest test_simple_math.py

Expected Output:

Running test_add_negative_numbers...
.Running test_add_positive_and_negative...
.Running test_add_positive_numbers...
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
""" 