"""
Challenge 22: Instance Methods

Problem Statement:
Implement a `Dog` class that has instance methods to manage its state, such as its name and age.

Requirements:
- Create a class named `Dog`.
- The constructor `__init__` should accept `name` (a string) and `age` (an integer) and store them as instance attributes.
- Create an instance method `birthday()` that increments the dog's age by 1.
- Create an instance method `get_details()` that returns a string with the dog's name and current age, formatted as "Name: [name], Age: [age]".

Solution:
"""

class Dog:
    def __init__(self, name, age):
        """Initializes a new Dog instance."""
        self.name = name
        self.age = age

    def birthday(self):
        """Increments the dog's age."""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    def get_details(self):
        """Returns the dog's details."""
        return f"Name: {self.name}, Age: {self.age}"

# Example usage:
if __name__ == "__main__":
    my_dog = Dog("Rex", 3)
    print(my_dog.get_details())
    
    my_dog.birthday()
    
    print(my_dog.get_details())

"""
Expected Output:

Name: Rex, Age: 3
Happy Birthday, Rex! You are now 4 years old.
Name: Rex, Age: 4
""" 