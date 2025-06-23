"""
Challenge 6: Recursion

Problem Statement:
Write a recursive function to calculate the factorial of a non-negative integer. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers up to `n`.

Requirements:
- The function should be named `factorial`.
- It should accept one argument: a non-negative integer `n`.
- The function must call itself to solve the problem (i.e., it must be recursive).
- The base case for the recursion is when `n` is 0, in which case the factorial is 1.
- For any other `n`, the factorial is `n` multiplied by the factorial of `n-1`.

Solution:
"""

def factorial(n):
    """
    Calculates the factorial of a number using recursion.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    num = 5
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
    
    num = 0
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
    
    num = 7
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

"""
Expected Output:

The factorial of 5 is: 120
The factorial of 0 is: 1
The factorial of 7 is: 5040
""" 