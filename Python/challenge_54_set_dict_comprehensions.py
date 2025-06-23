"""
Challenge 54: Set and Dictionary Comprehensions

Problem Statement:
Use set and dictionary comprehensions to efficiently create these data structures.
1.  **Set Comprehension**: Create a set containing the squares of numbers from a list, automatically handling any duplicate results.
2.  **Dictionary Comprehension**: Create a dictionary from two lists (e.g., one for keys, one for values).

Requirements:
-   **Task 1 (Set)**:
    -   Start with a list containing duplicates, e.g., `numbers = [1, 2, 2, 3, 4, 4, 5]`.
    -   Use a set comprehension to create a set of the squares of these numbers.
    -   Print the resulting set.
-   **Task 2 (Dictionary)**:
    -   Start with a list of keys and a list of values, e.g., `keys = ['name', 'age', 'city']` and `values = ['Alice', 30, 'New York']`.
    -   Use a dictionary comprehension to create a dictionary mapping keys to values.
    -   Print the resulting dictionary.

Solution:
"""

# Example usage:
if __name__ == "__main__":
    # --- Task 1: Set Comprehension ---
    numbers = [1, 2, 2, 3, 4, 4, 5]
    # The set comprehension {expression for item in iterable} creates a set.
    # Duplicates like 2*2=4 and 4*4=16 are automatically handled.
    squared_set = {x**2 for x in numbers}
    print(f"Original numbers: {numbers}")
    print(f"Set of squared numbers: {squared_set}")
    
    print("-" * 20)
    
    # --- Task 2: Dictionary Comprehension ---
    keys = ['name', 'age', 'city']
    values = ['Alice', 30, 'New York']
    # The dictionary comprehension {key_expr: val_expr for item in iterable} creates a dict.
    # We can use zip() to pair the keys and values.
    person_dict = {keys[i]: values[i] for i in range(len(keys))}
    # A more Pythonic way using zip: {k: v for k, v in zip(keys, values)}
    print(f"Original keys and values: {keys}, {values}")
    print(f"Created dictionary: {person_dict}")

"""
Expected Output:

Original numbers: [1, 2, 2, 3, 4, 4, 5]
Set of squared numbers: {1, 4, 9, 16, 25}
--------------------
Original keys and values: ['name', 'age', 'city'], ['Alice', 30, 'New York']
Created dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
""" 