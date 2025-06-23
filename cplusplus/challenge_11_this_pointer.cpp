/*
Challenge 11: The `this` Pointer

Problem Statement:
Create a `Box` class to demonstrate the use of the `this` pointer. The
constructor will have parameters with the same names as the member variables,
requiring `this` to disambiguate them. Also, create a method that returns
a reference to the current object to enable method chaining.

Requirements:
1.  **Define the `Box` class**:
    -   It should have `private` member variables for `width`, `height`, and `depth`.
    -   The constructor's parameters should also be named `width`, `height`, and
      `depth`. Use the `this` pointer to correctly assign the parameter values
      to the member variables (e.g., `this->width = width;`).
2.  **Method Chaining**:
    -   Create a method `setDimensions` that takes new dimensions, updates the
      object's state, and returns a reference to the current object (`*this`).
    -   Create a `printVolume` method that calculates and prints the volume.
3.  **Demonstrate**: In `main`, create a `Box` object and use method chaining
    to set new dimensions and then print the volume in a single statement.

*/

#include <iostream>

class Box {
private:
    double width;
    double height;
    double depth;

public:
    // 1. Constructor using 'this' to disambiguate members from parameters
    Box(double width, double height, double depth) {
        std::cout << "Constructor called. Initializing dimensions." << std::endl;
        this->width = width;
        this->height = height;
        this->depth = depth;
    }

    // 2. Method that returns a reference to the current object
    Box& setDimensions(double width, double height, double depth) {
        this->width = width;
        this->height = height;
        this->depth = depth;
        return *this; // Return the current object by reference
    }

    void printVolume() {
        double volume = width * height * depth;
        std::cout << "The volume of the box is: " << volume << std::endl;
    }
};

int main() {
    // Create an initial box
    Box myBox(10.0, 5.0, 2.0);
    std::cout << "--- Initial Box ---" << std::endl;
    myBox.printVolume();

    // 3. Demonstrate method chaining
    std::cout << "\n--- Updating Box and Chaining Methods ---" << std::endl;
    // setDimensions returns the object, so we can immediately call another method on it.
    myBox.setDimensions(8.0, 4.0, 3.0).printVolume();

    return 0;
}

/*
Expected Output:

Constructor called. Initializing dimensions.
--- Initial Box ---
The volume of the box is: 100

--- Updating Box and Chaining Methods ---
The volume of the box is: 96
*/ 