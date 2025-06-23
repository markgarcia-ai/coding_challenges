"""
Challenge 44: yield (Generators)

Problem Statement:
Write a generator function that yields a sequence of even numbers up to a specified limit. Generators are a simple way to create iterators using the `yield` keyword.

Requirements:
- The function should be named `even_number_generator`.
- It should accept one argument: an integer `limit`.
- Use a `for` loop and the `yield` keyword to produce even numbers one at a time.
- The generator should yield even numbers starting from 0 up to (and including) `limit`.

Solution:
"""

def even_number_generator(limit):
    """
    A generator that yields even numbers up to a given limit.
    """
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

# Example usage:
if __name__ == "__main__":
    max_limit = 10
    print(f"Even numbers up to {max_limit}:")
    
    # Create the generator object
    evens = even_number_generator(max_limit)
    
    # Iterate through the generator and print each number
    for num in evens:
        print(num)

"""
Expected Output:

Even numbers up to 10:
0
2
4
6
8
10
""" 