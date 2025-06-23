/*
Challenge 12: Inheritance

Problem Statement:
Create a base class `Animal` and a derived class `Dog`. The `Animal` class
will have basic properties and methods common to all animals, and the `Dog`
class will inherit these and add its own specific behavior.

Requirements:
1.  **Base Class `Animal`**:
    -   It should have a `protected` member `std::string name`. (Protected is like
      private, but accessible to derived classes).
    -   It should have a `public` constructor to initialize the name.
    -   It should have a `public` method `eat()` that prints a generic message
      like "[name] is eating."
2.  **Derived Class `Dog`**:
    -   It should inherit `publicly` from `Animal`.
    -   It must call the `Animal` base class constructor from its own constructor's
      initializer list to properly initialize the `name`.
    -   It should have its own `public` method `bark()` that prints "Woof! Woof!".
3.  **Demonstrate**: In `main`, create a `Dog` object. Show that it can access
    both its own method (`bark()`) and the inherited method from the `Animal`
    class (`eat()`).

*/

#include <iostream>
#include <string>

// 1. Base Class
class Animal {
protected:
    std::string name;

public:
    // Base class constructor
    Animal(std::string n) : name(n) {
        std::cout << "Animal constructor called for " << name << std::endl;
    }

    void eat() {
        std::cout << name << " is eating." << std::endl;
    }
};

// 2. Derived Class
class Dog : public Animal {
public:
    // Derived class constructor
    // It calls the base class constructor using an initializer list.
    Dog(std::string name) : Animal(name) {
        std::cout << "Dog constructor called for " << name << std::endl;
    }

    // Dog-specific method
    void bark() {
        std::cout << name << " says: Woof! Woof!" << std::endl;
    }
};

int main() {
    // 3. Create a Dog object
    Dog myDog("Buddy");

    std::cout << "\n--- Calling Methods ---" << std::endl;
    
    // Call the inherited method from the Animal class
    myDog.eat();

    // Call the method specific to the Dog class
    myDog.bark();

    return 0;
}

/*
Expected Output:

Animal constructor called for Buddy
Dog constructor called for Buddy

--- Calling Methods ---
Buddy is eating.
Buddy says: Woof! Woof!
*/ 