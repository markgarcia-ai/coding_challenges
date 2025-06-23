"""
Challenge 41: Enumerate Function

Problem Statement:
Write a function that finds the index of all occurrences of a specific item in a list.

Requirements:
- The function should be named `find_all_indices`.
- It should accept two arguments: a list to search in (`search_list`) and the item to search for (`item_to_find`).
- Use the `enumerate` function to get both the index and the value during iteration.
- Return a list of indices where the item was found. If the item is not found, return an empty list.

Solution:
"""

def find_all_indices(search_list, item_to_find):
    """
    Finds all indices of a given item in a list using enumerate.
    """
    indices = []
    for index, value in enumerate(search_list):
        if value == item_to_find:
            indices.append(index)
    return indices

# Example usage:
if __name__ == "__main__":
    my_letters = ['a', 'b', 'c', 'a', 'd', 'a', 'e']
    item = 'a'
    indices = find_all_indices(my_letters, item)
    print(f"List to search: {my_letters}")
    print(f"Indices of '{item}': {indices}")

    item = 'f'
    indices = find_all_indices(my_letters, item)
    print(f"Indices of '{item}': {indices}")

"""
Expected Output:

List to search: ['a', 'b', 'c', 'a', 'd', 'a', 'e']
Indices of 'a': [0, 3, 5]
Indices of 'f': []
""" 