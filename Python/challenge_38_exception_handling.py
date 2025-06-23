"""
Challenge 38: Exception Handling

Problem Statement:
Write a function that attempts to divide two numbers. The function should gracefully handle potential errors, such as division by zero or receiving non-numeric input, using a `try...except...finally` block.

Requirements:
- Create a function named `safe_divide(numerator, denominator)`.
- Use a `try` block to perform the division `numerator / denominator`.
- Include an `except` block for `ZeroDivisionError` to handle cases where the denominator is zero.
- Include an `except` block for `TypeError` to handle cases where inputs are not numbers.
- Use a `finally` block to print a message indicating that the division attempt has finished, regardless of whether it was successful or not.
- The function should return the result of the division or `None` if an error occurred.

Solution:
"""

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.
    """
    result = None
    try:
        result = numerator / denominator
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
    finally:
        print("Division attempt finished.")
    return result

# Example usage:
if __name__ == "__main__":
    print("--- Test Case 1: Valid division ---")
    safe_divide(10, 2)
    
    print("\n--- Test Case 2: Division by zero ---")
    safe_divide(10, 0)
    
    print("\n--- Test Case 3: Invalid input type ---")
    safe_divide(10, "a")

"""
Expected Output:

--- Test Case 1: Valid division ---
Result of division: 5.0
Division attempt finished.

--- Test Case 2: Division by zero ---
Error: Cannot divide by zero.
Division attempt finished.

--- Test Case 3: Invalid input type ---
Error: Both numerator and denominator must be numbers.
Division attempt finished.
""" 