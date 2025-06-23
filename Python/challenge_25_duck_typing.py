"""
Challenge 25: Duck Typing

Problem Statement:
Create a function that can make any object "speak" by calling its `speak()` method, regardless of the object's class. This demonstrates duck typing, where the suitability of an object is determined by the presence of certain methods and properties, rather than its class.

Requirements:
- Create two unrelated classes, `Dog` and `Person`.
- Both classes must have a method named `speak()` that returns a string.
  - `Dog.speak()` should return "Woof!".
  - `Person.speak()` should return "Hello!".
- Create a function `make_it_speak(obj)` that takes any object and prints the result of its `speak()` method.
- The function should not check the type of `obj`. It should just assume the object has a `speak()` method.

Solution:
"""

class Dog:
    def speak(self):
        return "Woof!"

class Person:
    def speak(self):
        return "Hello!"

def make_it_speak(obj):
    """
    Calls the speak() method of any object that has one.
    "If it walks like a duck and quacks like a duck, it must be a duck."
    """
    print(obj.speak())

# Example usage:
if __name__ == "__main__":
    dog_instance = Dog()
    person_instance = Person()
    
    print("Making the dog speak:")
    make_it_speak(dog_instance)
    
    print("Making the person speak:")
    make_it_speak(person_instance)

"""
Expected Output:

Making the dog speak:
Woof!
Making the person speak:
Hello!
""" 