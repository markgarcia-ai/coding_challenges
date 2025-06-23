"""
Challenge 18: self

Problem Statement:
Create a `Person` class to demonstrate the use of `self`. The `self` keyword is used to refer to the instance of the class, allowing you to access its attributes and methods.

Requirements:
- Create a class named `Person`.
- The `__init__` method should take a `name` and store it in an instance attribute, `self.name`.
- Create an instance method `introduce()` that uses `self.name` to print an introduction message like "Hi, my name is [name]".
- Create another instance method `change_name(self, new_name)` that uses `self` to modify the instance's `name` attribute.

Solution:
"""

class Person:
    """A class to demonstrate the use of self."""
    def __init__(self, name):
        # 'self' refers to the specific instance being created.
        # We are attaching the 'name' to this instance.
        self.name = name
        print(f"'{self.name}' has been created.")

    def introduce(self):
        # Here, 'self' gives us access to the 'name' attribute
        # that was set in the constructor for this specific instance.
        print(f"Hi, my name is {self.name}.")

    def change_name(self, new_name):
        # 'self' allows us to modify the state of this instance.
        self.name = new_name
        print(f"My name has been changed to {self.name}.")

# Example usage:
if __name__ == "__main__":
    # Create the first instance of Person. 'self' inside the methods will refer to p1.
    p1 = Person("Alice")
    p1.introduce()
    
    # Create a second instance. 'self' will now refer to p2 for this object's calls.
    p2 = Person("Bob")
    p2.introduce()
    
    # Change the name of the first instance. This only affects p1.
    p1.change_name("Alicia")
    p1.introduce()
    p2.introduce() # p2's name remains unchanged.

"""
Expected Output:

'Alice' has been created.
Hi, my name is Alice.
'Bob' has been created.
Hi, my name is Bob.
My name has been changed to Alicia.
Hi, my name is Alicia.
Hi, my name is Bob.
""" 