"""
Challenge 12: Method Overriding

Problem Statement:
Create a base class `Animal` with a method `speak()`. Then, create two subclasses, `Dog` and `Cat`, that override the `speak()` method to provide their own specific implementation.

Requirements:
- Create a base class `Animal` with a method `speak()` that returns a generic sound like "Some animal sound".
- Create a `Dog` class that inherits from `Animal` and overrides `speak()` to return "Woof!".
- Create a `Cat` class that inherits from `Animal` and overrides `speak()` to return "Meow!".
- Write a function that takes a list of `Animal` objects and prints the sound each animal makes.

Solution:
"""

class Animal:
    """Base class for all animals."""
    def speak(self):
        return "Some animal sound"

class Dog(Animal):
    """Dog subclass that overrides the speak method."""
    def speak(self):
        return "Woof!"

class Cat(Animal):
    """Cat subclass that overrides the speak method."""
    def speak(self):
        return "Meow!"

def print_animal_sounds(animals):
    """Takes a list of animal objects and prints their sounds."""
    for animal in animals:
        print(f"A {type(animal).__name__} says: {animal.speak()}")

# Example usage:
if __name__ == "__main__":
    animal_list = [
        Animal(),
        Dog(),
        Cat()
    ]
    
    print_animal_sounds(animal_list)

"""
Expected Output:

A Animal says: Some animal sound
A Dog says: Woof!
A Cat says: Meow!
""" 