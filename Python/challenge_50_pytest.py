"""
Challenge 50: PyTest

Problem Statement:
Rewrite the unit tests from the `unittest` challenge using the `pytest` framework. `pytest` uses plain assert statements and simple function-based tests, which can be more concise.

Requirements:
1.  **The function to test:**
    -   You can reuse the `simple_math.py` file with the `add(a, b)` function.

2.  **The test file:**
    -   Create a separate file `test_math_pytest.py`.
    -   Import the `add` function.
    -   Write simple test functions (names must start with `test_`).
    -   Inside the functions, use the standard Python `assert` statement to check for correctness.

Solution:
"""
# Note: To run this, you need to have pytest installed (`pip install pytest`)

# Step 1: Create or reuse the file 'simple_math.py' with this content:
#
# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b


# Step 2: Create the file 'test_math_pytest.py' with this content:

# from simple_math import add # Uncomment if running as separate files

# --- For demonstration, we'll include the function in the same file ---
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
# --------------------------------------------------------------------


def test_add_positive_numbers():
    """Test that adding two positive numbers works correctly."""
    assert add(5, 10) == 15

def test_add_positive_and_negative():
    """Test adding a positive and a negative number."""
    assert add(-5, 10) == 5

def test_add_negative_numbers():
    """Test that adding two negative numbers works correctly."""
    assert add(-5, -10) == -15

"""
To run from the command line:
1. Make sure you are in the correct directory.
2. Run the command: pytest

Pytest will automatically discover and run the tests.

Expected Output (will vary slightly based on pytest version):

============================= test session starts ==============================
...
collected 3 items

test_math_pytest.py ...                                                  [100%]

============================== 3 passed in X.XXs ===============================
""" 