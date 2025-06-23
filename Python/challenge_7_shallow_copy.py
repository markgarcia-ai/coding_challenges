"""
Challenge 7: Shallow Copy

Problem Statement:
Demonstrate the behavior of a shallow copy with a nested list. A shallow copy creates a new object, but it does not create copies of the nested objects within the original object. Instead, it copies references to them.

Requirements:
- Create a nested list, for example, `list_a = [[1, 2], [3, 4]]`.
- Use the `copy()` method to create a shallow copy of `list_a` and name it `list_b`.
- Modify an element inside the nested list of `list_a` (e.g., change `list_a[0][0]` to `99`).
- Print both `list_a` and `list_b` to observe that the change is reflected in both lists, because they share the same inner list objects.
- Append a new element to `list_a` and show that this change does *not* affect `list_b`, demonstrating that they are different outer lists.

Solution:
"""

def demonstrate_shallow_copy():
    """
    Shows the effect of a shallow copy on a nested list.
    """
    print("--- Initial State ---")
    list_a = [[1, 2], [3, 4]]
    # Create a shallow copy
    list_b = list_a.copy()
    
    print(f"Original list (list_a): {list_a}")
    print(f"Shallow copy (list_b): {list_b}")

    print("\n--- Modifying a nested element in list_a ---")
    list_a[0][0] = 99
    
    print(f"Original list after modification: {list_a}")
    print(f"Shallow copy after modification: {list_b}")
    print("Note: The change is reflected in both because the inner lists are shared.")

    print("\n--- Appending to the outer list_a ---")
    list_a.append([5, 6])
    
    print(f"Original list after append: {list_a}")
    print(f"Shallow copy after append: {list_b}")
    print("Note: The appended list only appears in list_a.")


# Example usage:
if __name__ == "__main__":
    demonstrate_shallow_copy()

"""
Expected Output:

--- Initial State ---
Original list (list_a): [[1, 2], [3, 4]]
Shallow copy (list_b): [[1, 2], [3, 4]]

--- Modifying a nested element in list_a ---
Original list after modification: [[99, 2], [3, 4]]
Shallow copy after modification: [[99, 2], [3, 4]]
Note: The change is reflected in both because the inner lists are shared.

--- Appending to the outer list_a ---
Original list after append: [[99, 2], [3, 4], [5, 6]]
Shallow copy after append: [[99, 2], [3, 4]]
Note: The appended list only appears in list_a.
""" 