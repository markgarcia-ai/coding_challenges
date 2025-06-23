/*
Challenge 14: Operator Overloading

Problem Statement:
Create a `Vector2D` class representing a 2D vector. Overload the `+` operator
to perform vector addition and the `<<` operator to allow easy printing of
the vector's contents to an output stream like `std::cout`.

Requirements:
1.  **`Vector2D` Class**:
    -   It should have `public` members `x` and `y` of type `double`.
    -   A constructor to initialize `x` and `y`.
2.  **Overload the `+` Operator**:
    -   Create a member function `Vector2D operator+(const Vector2D& other) const`.
    -   This function should take another `Vector2D` object and return a *new*
      `Vector2D` object representing the sum of the two vectors.
3.  **Overload the `<<` Operator**:
    -   Create a non-member function `std::ostream& operator<<(std::ostream& stream, const Vector2D& vec)`.
    -   This function will format the vector's output (e.g., "(x, y)") and
      write it to the provided output stream.
4.  **Demonstrate**: In `main`, create two `Vector2D` objects, add them together
    using the `+` operator, and print all three vectors using `std::cout`.

*/

#include <iostream>

class Vector2D {
public:
    double x, y;

    // Constructor
    Vector2D(double x_val = 0.0, double y_val = 0.0) : x(x_val), y(y_val) {}

    // 2. Overload the + operator as a member function
    Vector2D operator+(const Vector2D& other) const {
        // Create a new Vector2D that is the sum of this vector and the other
        return Vector2D(this->x + other.x, this->y + other.y);
    }
};

// 3. Overload the << operator as a non-member function
// It needs to be a non-member to have std::ostream as its left-hand operand.
std::ostream& operator<<(std::ostream& stream, const Vector2D& vec) {
    stream << "(" << vec.x << ", " << vec.y << ")";
    return stream;
}

int main() {
    // 4. Demonstrate the overloaded operators
    Vector2D v1(2.5, 3.0);
    Vector2D v2(1.5, 4.5);

    // Use the overloaded + operator
    Vector2D v_sum = v1 + v2;

    // Use the overloaded << operator with std::cout
    std::cout << "Vector v1: " << v1 << std::endl;
    std::cout << "Vector v2: " << v2 << std::endl;
    std::cout << "Sum of v1 and v2: " << v_sum << std::endl;

    return 0;
}

/*
Expected Output:

Vector v1: (2.5, 3)
Vector v2: (1.5, 4.5)
Sum of v1 and v2: (4, 7.5)
*/ 