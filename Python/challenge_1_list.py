"""
Challenge 1: Lists

Problem Statement:
Write a function that takes a list of numbers and returns a new list containing only the even numbers from the original list, sorted in ascending order.

Requirements:
- The function should be named `filter_and_sort_evens`.
- It should accept one argument: a list of integers.
- It should return a new list, leaving the original list unmodified.
- Use a list comprehension to filter the even numbers.

Solution:
"""

def filter_and_sort_evens(numbers):
    """
    Filters a list of numbers to keep only even values and sorts them.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort()
    return even_numbers

# Example usage:
if __name__ == "__main__":
    my_list = [4, 1, 8, 3, 6, 9, 2, 7]
    filtered_sorted_list = filter_and_sort_evens(my_list)
    print(f"Original list: {my_list}")
    print(f"Filtered and sorted list of evens: {filtered_sorted_list}")

"""
Expected Output:

Original list: [4, 1, 8, 3, 6, 9, 2, 7]
Filtered and sorted list of evens: [2, 4, 6, 8]
""" 