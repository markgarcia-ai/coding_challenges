"""
Challenge 27: Destructors (__del__)

Problem Statement:
Create a `FileHandler` class that opens a file in its constructor and, to demonstrate the concept, prints a message in its destructor (`__del__`) when the object is destroyed.

Requirements:
- Create a class named `FileHandler`.
- The `__init__` constructor should take a `filename` and print a message that the file is being "opened".
- The `__del__` destructor should print a message that the object is being "closed" or cleaned up.
- Note: The exact timing of `__del__` is not guaranteed in Python. It's called when an object's reference count drops to zero. We will use `del` to trigger it explicitly for this demonstration.

Solution:
"""

class FileHandler:
    """A class to demonstrate the __del__ method."""
    def __init__(self, filename):
        print(f"CONSTRUCTOR: Opening file '{filename}'.")
        self.filename = filename

    def __del__(self):
        """
        This is the destructor. It's called when the object is garbage collected.
        """
        print(f"DESTRUCTOR: Cleaning up and closing file '{self.filename}'.")

def manage_file():
    print("Entering manage_file function...")
    handler = FileHandler("my_document.txt")
    print("...handler object created.")
    print("Exiting manage_file function...")
    # The 'handler' object goes out of scope here, and __del__ will be called.

# Example usage:
if __name__ == "__main__":
    print("--- Scenario 1: Object goes out of scope ---")
    manage_file()
    
    print("\n--- Scenario 2: Explicitly deleting an object ---")
    handler2 = FileHandler("another_file.log")
    print("Deleting handler2 now...")
    del handler2 # This triggers the __del__ method.

"""
Expected Output:

--- Scenario 1: Object goes out of scope ---
Entering manage_file function...
CONSTRUCTOR: Opening file 'my_document.txt'.
...handler object created.
Exiting manage_file function...
DESTRUCTOR: Cleaning up and closing file 'my_document.txt'.

--- Scenario 2: Explicitly deleting an object ---
CONSTRUCTOR: Opening file 'another_file.log'.
Deleting handler2 now...
DESTRUCTOR: Cleaning up and closing file 'another_file.log'.
""" 