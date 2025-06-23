/*
Challenge 21: Lambda Expressions

Problem Statement:
Write a C++ program that uses a lambda expression with the `std::for_each`
algorithm to process elements in a `std::vector`. This will show how to define
and use a simple, inline anonymous function.

Requirements:
1.  **Include Headers**: `<iostream>`, `<vector>`, and `<algorithm>`.
2.  **Initialization**: Create a `std::vector` of integers.
3.  **`std::for_each` with a Lambda**:
    -   Call `std::for_each`, providing the vector's `begin()` and `end()` iterators.
    -   For the third argument, provide a lambda expression.
    -   The lambda should take a single integer argument and print its value
      followed by a space.
4.  **Lambda with Capture**:
    -   Declare an integer `multiplier` in `main`.
    -   Use a second `std::for_each` call with a new lambda that "captures" the
      `multiplier` variable from its surrounding scope.
    -   The lambda should print the result of each element in the vector
      multiplied by the captured value.

*/

#include <iostream>
#include <vector>
#include <algorithm> // for std::for_each

int main() {
    // 2. Initialize a vector
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // 3. Use a simple lambda to print each element
    std::cout << "--- Printing elements using a simple lambda ---" << std::endl;
    std::for_each(numbers.begin(), numbers.end(),
        // This is the lambda expression:
        [](int n) {
            std::cout << n << " ";
        }
    );
    std::cout << std::endl;

    // 4. Use a lambda that captures a local variable
    int multiplier = 3;
    std::cout << "\n--- Multiplying elements using a lambda with capture ---" << std::endl;
    std::for_each(numbers.begin(), numbers.end(),
        // [=] captures all local variables by value. [multiplier] would also work.
        [=](int n) {
            std::cout << (n * multiplier) << " ";
        }
    );
    std::cout << std::endl;

    return 0;
}

/*
Expected Output:

--- Printing elements using a simple lambda ---
1 2 3 4 5 

--- Multiplying elements using a lambda with capture ---
3 6 9 12 15 
*/ 