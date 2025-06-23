"""
Challenge 39: List Comprehensions

Problem Statement:
Use list comprehensions to perform three common list creation tasks:
1. Create a list of the squares of numbers from 0 to 9.
2. Create a list of uppercase versions of words from another list.
3. Create a list of only the even numbers from a given list of integers.

Requirements:
- For each task, create the new list using a single line of code (a list comprehension).
- Print each resulting list with a descriptive message.

Solution:
"""

# Example usage:
if __name__ == "__main__":
    # Task 1: Create a list of squares
    squares = [x**2 for x in range(10)]
    print(f"Squares of numbers from 0 to 9: {squares}")
    
    # Task 2: Uppercase words
    words = ["hello", "world", "python", "is", "awesome"]
    uppercase_words = [word.upper() for word in words]
    print(f"Uppercase words: {uppercase_words}")
    
    # Task 3: Filter for even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers from the list: {even_numbers}")

"""
Expected Output:

Squares of numbers from 0 to 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Uppercase words: ['HELLO', 'WORLD', 'PYTHON', 'IS', 'AWESOME']
Even numbers from the list: [2, 4, 6, 8, 10]
""" 