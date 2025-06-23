"""
Challenge 20: Wrappers (Decorators)

Problem Statement:
Create a simple decorator (a wrapper) that prints a message before and after a function is called. This is a fundamental pattern for logging, timing, or adding setup/teardown logic.

Requirements:
- Create a function named `simple_wrapper` that will act as a decorator.
- This decorator should take a function as its argument.
- It should define and return a new function (the "wrapper function").
- When the wrapper function is executed, it should:
  1. Print "Function is about to be called."
  2. Call the original function.
  3. Print "Function has been called."
- Apply this decorator to a simple function to demonstrate its effect.

Solution:
"""
import functools

def simple_wrapper(func):
    """A simple decorator that wraps a function with print statements."""
    @functools.wraps(func) # Preserves the original function's metadata
    def wrapper_function(*args, **kwargs):
        print("Function is about to be called.")
        result = func(*args, **kwargs)
        print("Function has been called.")
        return result
    return wrapper_function

@simple_wrapper
def say_hello(name):
    """A function that prints a greeting."""
    print(f"Hello, {name}!")

# Example usage:
if __name__ == "__main__":
    say_hello("World")

"""
Expected Output:

Function is about to be called.
Hello, World!
Function has been called.
""" 