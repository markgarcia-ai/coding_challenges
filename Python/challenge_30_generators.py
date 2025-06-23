"""
Challenge 30: Generators

Problem Statement:
Create a generator function `even_numbers(max_val)` that yields all even numbers up to a given maximum value. Unlike a normal function that would build a list and return it, a generator yields values one at a time, which is more memory-efficient.

Requirements:
- Create a generator function named `even_numbers` that takes one argument, `max_val`.
- Inside the function, use a loop to iterate from 0 up to `max_val`.
- If a number is even, use the `yield` keyword to return it.
- Use the generator in a `for` loop to print the even numbers up to 10.

Solution:
"""

def even_numbers(max_val):
    """
    This is a generator function. It yields even numbers.
    The function's state is saved at each 'yield' statement.
    """
    print("--- Generator Started ---")
    for i in range(max_val + 1):
        if i % 2 == 0:
            yield i
    print("--- Generator Finished ---")

# Example usage:
if __name__ == "__main__":
    print("Using the generator in a for loop:")
    # The for loop works with generators just like with other iterables.
    for number in even_numbers(10):
        print(number)
        
    print("\nManually getting values from the generator:")
    even_gen = even_numbers(6)
    print(f"First value: {next(even_gen)}")
    print(f"Second value: {next(even_gen)}")
    print(f"Third value: {next(even_gen)}")

"""
Expected Output:

Using the generator in a for loop:
--- Generator Started ---
0
2
4
6
8
10
--- Generator Finished ---

Manually getting values from the generator:
--- Generator Started ---
First value: 0
Second value: 2
Third value: 4
""" 