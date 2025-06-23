"""
Challenge 21: Decorators

Problem Statement:
Create a decorator that logs the execution time of a function. The decorator should print a message indicating how long the function took to run.

Requirements:
- Create a decorator named `timer`.
- When a function decorated with `@timer` is called, it should:
  1. Record the time before the function executes.
  2. Execute the function.
  3. Record the time after the function executes.
  4. Print the time difference in a user-friendly format (e.g., "Function 'my_function' executed in 0.002 seconds").
- The decorator should work on any function, regardless of its arguments.

Solution:
"""

import time
import functools

def timer(func):
    """A decorator that prints the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {run_time:.4f} seconds")
        return value
    return wrapper

@timer
def example_function(delay):
    """A simple function that pauses for a given duration."""
    time.sleep(delay)
    return f"Slept for {delay} seconds."

# Example usage:
if __name__ == "__main__":
    result = example_function(0.5)
    print(result)
    
    result2 = example_function(1)
    print(result2)

"""
Expected Output:

Function 'example_function' executed in 0.50XX seconds
Slept for 0.5 seconds.
Function 'example_function' executed in 1.00XX seconds
Slept for 1 seconds.
""" 