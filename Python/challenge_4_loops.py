"""
Challenge 4: Loops

Problem Statement:
Write a function that prints a simple pyramid pattern of a given height using asterisks (*).

Requirements:
- The function should be named `print_pyramid`.
- It should accept one argument: an integer `height`.
- Use a `for` loop to iterate from 1 to the given `height`.
- In each iteration, print a row with the correct number of leading spaces and asterisks.
- The top of the pyramid should have 1 asterisk, and the base should have `2 * height - 1` asterisks.

Solution:
"""

def print_pyramid(height):
    """
    Prints a pyramid pattern of a specified height.
    """
    # The width of the base of the pyramid
    base_width = 2 * height - 1
    
    for i in range(1, height + 1):
        # Calculate the number of asterisks for the current row
        num_asterisks = 2 * i - 1
        
        # Calculate the number of leading spaces for centering
        num_spaces = (base_width - num_asterisks) // 2
        
        # Construct the row string
        row = ' ' * num_spaces + '*' * num_asterisks
        print(row)

# Example usage:
if __name__ == "__main__":
    pyramid_height = 5
    print(f"Pyramid of height {pyramid_height}:")
    print_pyramid(pyramid_height)

"""
Expected Output:

Pyramid of height 5:
    *
   ***
  *****
 *******
*********
""" 