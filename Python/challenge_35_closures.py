"""
Challenge 35: Closures

Problem Statement:
Create a "factory" function that generates and returns a new function. The returned function should be a multiplier that multiplies any number by a factor that was defined when the factory was called. This demonstrates a closure, where the inner function "remembers" the `factor` from its enclosing scope.

Requirements:
- Create a function `create_multiplier(factor)`. This is the outer function.
- Inside `create_multiplier`, define a nested function `multiplier(x)`.
- The `multiplier` function should take one argument `x` and return `x * factor`.
- The `create_multiplier` function should return the `multiplier` function itself (not the result of calling it).
- Demonstrate that you can create different multiplier functions (e.g., one for doubling, one for tripling) and that they work correctly.

Solution:
"""

def create_multiplier(factor):
    """
    This is the outer function (the factory). It creates a closure.
    'factor' is the "free variable" that will be remembered by the inner function.
    """
    def multiplier(x):
        """
        This is the inner function. It has access to 'factor'
        from its enclosing scope, even after create_multiplier has finished.
        """
        return x * factor
    
    return multiplier

# Example usage:
if __name__ == "__main__":
    # Create a function that doubles a number
    double = create_multiplier(2)
    
    # Create a function that triples a number
    triple = create_multiplier(3)
    
    # Use the new functions. Notice how each one "remembers" its factor.
    print(f"Using the 'double' function (factor=2):")
    print(f"double(5) = {double(5)}")
    print(f"double(10) = {double(10)}")
    
    print(f"\nUsing the 'triple' function (factor=3):")
    print(f"triple(5) = {triple(5)}")
    print(f"triple(10) = {triple(10)}")

"""
Expected Output:

Using the 'double' function (factor=2):
double(5) = 10
double(10) = 20

Using the 'triple' function (factor=3):
triple(5) = 15
triple(10) = 30
""" 