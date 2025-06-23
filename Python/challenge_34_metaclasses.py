"""
Challenge 34: Metaclasses

Problem Statement:
Create a simple metaclass that automatically adds a `created_at` attribute to any class that uses it. This attribute should record the time the class was defined.

Requirements:
- Create a metaclass named `TimestampedMeta`.
- This metaclass should inherit from Python's built-in `type` metaclass.
- Implement the `__new__` method in the metaclass. The `__new__` method is called when a class is being created.
- Inside `__new__`, add an attribute named `created_at` to the class being created. The value should be the current timestamp.
- Create a simple class `MyExampleClass` that uses `TimestampedMeta` as its metaclass.
- Verify that `MyExampleClass` has the `created_at` attribute without it being explicitly defined in the class body.

Solution:
"""
import time

# Define the metaclass
class TimestampedMeta(type):
    """A metaclass that adds a 'created_at' timestamp to a class."""
    def __new__(cls, name, bases, attrs):
        # 'cls' is the metaclass itself (TimestampedMeta)
        # 'name' is the name of the class being created ("MyExampleClass")
        # 'bases' is a tuple of the parent classes
        # 'attrs' is a dictionary of the class's attributes and methods
        
        # Add the new attribute to the class's dictionary
        attrs['created_at'] = time.ctime()
        
        # Create the new class by calling the parent's __new__ method
        return super().__new__(cls, name, bases, attrs)

# Create a class using the metaclass
class MyExampleClass(metaclass=TimestampedMeta):
    """An example class that will be timestamped by its metaclass."""
    pass

# Example usage:
if __name__ == "__main__":
    print(f"MyExampleClass was created at: {MyExampleClass.created_at}")

    # The attribute is part of the class, not the instance
    instance = MyExampleClass()
    # print(instance.created_at) # This also works

"""
Expected Output:

MyExampleClass was created at: [Current Date and Time]
(e.g., MyExampleClass was created at: Tue Dec 19 10:30:00 2023)
""" 