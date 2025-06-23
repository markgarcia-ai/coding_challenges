"""
Challenge 15: Arguments (*args and **kwargs)

Problem Statement:
Write a function that accepts any number of positional and keyword arguments and prints them out. This is useful for creating flexible functions that can handle a variety of inputs.

Requirements:
- Create a function named `show_all_arguments`.
- The function signature must be `def show_all_arguments(*args, **kwargs):`.
- `*args` will collect all positional arguments into a tuple.
- `**kwargs` will collect all keyword arguments into a dictionary.
- The function should first print the positional arguments, then the keyword arguments.

Solution:
"""

def show_all_arguments(*args, **kwargs):
    """
    Accepts and displays any number of positional and keyword arguments.
    """
    print("--- Positional Arguments (*args) ---")
    if args:
        for i, arg in enumerate(args):
            print(f"  args[{i}]: {arg}")
    else:
        print("  None")
        
    print("\n--- Keyword Arguments (**kwargs) ---")
    if kwargs:
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    else:
        print("  None")

# Example usage:
if __name__ == "__main__":
    print("--- Calling with positional and keyword arguments ---")
    show_all_arguments(1, "hello", True, name="Alice", age=30)
    
    print("\n\n--- Calling with only positional arguments ---")
    show_all_arguments(10.5, [1, 2])
    
    print("\n\n--- Calling with only keyword arguments ---")
    show_all_arguments(city="New York", country="USA")
    
    print("\n\n--- Calling with no arguments ---")
    show_all_arguments()


"""
Expected Output:

--- Calling with positional and keyword arguments ---
--- Positional Arguments (*args) ---
  args[0]: 1
  args[1]: hello
  args[2]: True

--- Keyword Arguments (**kwargs) ---
  name: Alice
  age: 30


--- Calling with only positional arguments ---
--- Positional Arguments (*args) ---
  args[0]: 10.5
  args[1]: [1, 2]

--- Keyword Arguments (**kwargs) ---
  None


--- Calling with only keyword arguments ---
--- Positional Arguments (*args) ---
  None

--- Keyword Arguments (**kwargs) ---
  city: New York
  country: USA


--- Calling with no arguments ---
--- Positional Arguments (*args) ---
  None

--- Keyword Arguments (**kwargs) ---
  None
""" 