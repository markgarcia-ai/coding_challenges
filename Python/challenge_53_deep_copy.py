"""
Challenge 53: Deep Copy

Problem Statement:
Demonstrate the behavior of a deep copy with a nested list. A deep copy creates a new object and recursively creates independent copies of all the objects found inside the original.

Requirements:
- Import the `copy` module.
- Create a nested list, `list_a = [[1, 2], [3, 4]]`.
- Use `copy.deepcopy()` to create a deep copy of `list_a` and name it `list_c`.
- Modify an element inside the nested list of `list_a` (e.g., change `list_a[0][0]` to `99`).
- Print both `list_a` and `list_c` to observe that the change is *only* reflected in `list_a`, because `list_c` has its own, separate inner list objects.

Solution:
"""
import copy

def demonstrate_deep_copy():
    """
    Shows the effect of a deep copy on a nested list.
    """
    print("--- Initial State ---")
    list_a = [[1, 2], [3, 4]]
    
    # Create a deep copy
    list_c = copy.deepcopy(list_a)
    
    print(f"Original list (list_a): {list_a}")
    print(f"Deep copy (list_c): {list_c}")

    print("\n--- Modifying a nested element in list_a ---")
    list_a[0][0] = 99
    
    print(f"Original list after modification: {list_a}")
    print(f"Deep copy after modification: {list_c}")
    print("Note: The change is NOT reflected in the deep copy because it's a completely separate object.")


# Example usage:
if __name__ == "__main__":
    demonstrate_deep_copy()

"""
Expected Output:

--- Initial State ---
Original list (list_a): [[1, 2], [3, 4]]
Deep copy (list_c): [[1, 2], [3, 4]]

--- Modifying a nested element in list_a ---
Original list after modification: [[99, 2], [3, 4]]
Deep copy after modification: [[1, 2], [3, 4]]
Note: The change is NOT reflected in the deep copy because it's a completely separate object.
""" 