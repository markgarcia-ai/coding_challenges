/*
Challenge 13: Polymorphism

Problem Statement:
Demonstrate polymorphism by creating a base `Shape` class and two derived
classes, `Circle` and `Rectangle`. We will use a base class pointer to hold
objects of derived classes and call a common virtual function, which will
behave differently depending on the object's actual type.

Requirements:
1.  **Base Class `Shape`**:
    -   Should have a `virtual` method `draw()` that prints a generic shape message.
      The `virtual` keyword is essential for polymorphism.
    -   Should have a `virtual` destructor to ensure proper cleanup when deleting
      a derived object through a base class pointer.
2.  **Derived Classes `Circle` and `Rectangle`**:
    -   Both should inherit from `Shape`.
    -   Each should `override` the `draw()` method to print a message specific
      to that shape (e.g., "Drawing a Circle.").
3.  **Demonstrate Polymorphism**:
    -   In `main`, create a `Circle` object and a `Rectangle` object.
    -   Create a `Shape*` (a pointer to a Shape).
    -   First, point the `Shape*` to the `Circle` object and call `draw()`.
    -   Second, point the `Shape*` to the `Rectangle` object and call `draw()`.
      Observe that the same function call produces different behavior.

*/

#include <iostream>

// 1. Base Class
class Shape {
public:
    // virtual function, enabling polymorphism
    virtual void draw() {
        std::cout << "Drawing a generic shape." << std::endl;
    }
    // virtual destructor for safe cleanup
    virtual ~Shape() {}
};

// 2. Derived Classes
class Circle : public Shape {
public:
    // Override the base class method
    void draw() override {
        std::cout << "Drawing a Circle." << std::endl;
    }
};

class Rectangle : public Shape {
public:
    // Override the base class method
    void draw() override {
        std::cout << "Drawing a Rectangle." << std::endl;
    }
};

int main() {
    // 3. Demonstrate Polymorphism
    Circle circle;
    Rectangle rectangle;
    
    Shape* shapePtr; // A pointer to the base class

    std::cout << "--- Using a Shape pointer to call draw() ---" << std::endl;

    // Point to a Circle object
    shapePtr = &circle;
    std::cout << "Pointer points to a Circle: ";
    shapePtr->draw(); // Calls Circle::draw()

    // Point to a Rectangle object
    shapePtr = &rectangle;
    std::cout << "Pointer points to a Rectangle: ";
    shapePtr->draw(); // Calls Rectangle::draw()

    return 0;
}

/*
Expected Output:

--- Using a Shape pointer to call draw() ---
Pointer points to a Circle: Drawing a Circle.
Pointer points to a Rectangle: Drawing a Rectangle.
*/ 