"""
Challenge 40: Walrus Operator (:=)

Problem Statement:
Write a function that processes a list of user inputs. The function should repeatedly ask the user for input until they enter "quit". It should then print all the collected inputs. Use the walrus operator to simplify the loop condition.

Requirements:
- Create a function named `collect_inputs`.
- Inside the function, use a `while` loop to gather input.
- The condition of the `while` loop must use the walrus operator (`:=`) to both get the user input and check if it is not "quit" in a single expression.
- Store the collected inputs in a list and print the list at the end.

Solution:
"""

def collect_inputs():
    """
    Collects user inputs until 'quit' is entered, using the walrus operator.
    
    NOTE: This example cannot be run in a non-interactive environment.
    The code below shows how it would work in an interactive session.
    """
    inputs = []
    # The walrus operator assigns the input to 'current_input' and then
    # the expression's value (the input string) is compared to 'quit'.
    while (current_input := input("Enter a value (or 'quit' to exit): ")) != "quit":
        inputs.append(current_input)
    
    print("\n--- Collected Inputs ---")
    print(inputs)

# Example usage in an interactive session:
if __name__ == "__main__":
    print("This script demonstrates the walrus operator for interactive input.")
    print("To test it, you would run the collect_inputs() function in a terminal.")
    # To run this for real, you would uncomment the line below:
    # collect_inputs()

"""
Example Interactive Session:

Enter a value (or 'quit' to exit): hello
Enter a value (or 'quit' to exit): world
Enter a value (or 'quit' to exit): 123
Enter a value (or 'quit' to exit): quit

--- Collected Inputs ---
['hello', 'world', '123']
""" 