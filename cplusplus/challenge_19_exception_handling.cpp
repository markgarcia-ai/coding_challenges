/*
Challenge 19: Exception Handling

Problem Statement:
Write a C++ program that demonstrates exception handling. Create a function
that performs division but throws an exception if the denominator is zero.
The main function will call this and use a `try...catch` block to handle
the potential error gracefully without crashing the program.

Requirements:
1.  **Include Headers**: `<iostream>` and `<stdexcept>`.
2.  **`divide` Function**:
    -   Create a function `double divide(double numerator, double denominator)`.
    -   Inside the function, check if the denominator is zero.
    -   If it is, `throw` a `std::runtime_error` with an appropriate message.
    -   Otherwise, return the result of the division.
3.  **`try...catch` Block**:
    -   In `main`, create a `try` block.
    -   Inside the `try` block, call the `divide` function twice: once with a
      valid denominator and once with zero as the denominator. Print the result
      of the valid division.
    -   Follow the `try` block with a `catch` block that can catch a
      `const std::runtime_error&`.
    -   Inside the `catch` block, print an error message to the user, including
      the content of the exception's `.what()` message.

*/

#include <iostream>
#include <stdexcept> // Required for std::runtime_error

// 2. A function that might throw an exception
double divide(double numerator, double denominator) {
    if (denominator == 0) {
        // Throw an exception of type std::runtime_error
        throw std::runtime_error("Division by zero error!");
    }
    return numerator / denominator;
}

int main() {
    double num1 = 10.0;
    double num2 = 2.0;
    double num3 = 0.0;

    // 3. Use a try...catch block to handle potential exceptions
    
    // First, test with valid division
    std::cout << "--- Testing valid division ---" << std::endl;
    try {
        double result = divide(num1, num2);
        std::cout << "Result of " << num1 << " / " << num2 << " is " << result << std::endl;
    } catch (const std::runtime_error& e) {
        // This block will not be executed for the valid case
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    }

    // Now, test division by zero
    std::cout << "\n--- Testing division by zero ---" << std::endl;
    try {
        // This call will throw an exception
        double result = divide(num1, num3);
        // This line will not be reached
        std::cout << "Result of " << num1 << " / " << num3 << " is " << result << std::endl;
    } catch (const std::runtime_error& e) {
        // The exception is caught here
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    }
    
    std::cout << "\nProgram continues to run after handling the exception." << std::endl;

    return 0;
}

/*
Expected Output:

--- Testing valid division ---
Result of 10 / 2 is 5

--- Testing division by zero ---
Caught an exception: Division by zero error!

Program continues to run after handling the exception.
*/ 