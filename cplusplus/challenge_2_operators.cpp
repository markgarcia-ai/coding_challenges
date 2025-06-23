/*
Challenge 2: Operators

Problem Statement:
Write a C++ program to demonstrate various operators. The program should perform
several calculations and logical comparisons and print the results.

Requirements:
1.  **Arithmetic Operators**: Calculate the sum, difference, product, quotient,
    and remainder (modulo) of two integer variables.
2.  **Relational Operators**: Compare two numbers to see if one is greater than,
    less than, or equal to the other.
3.  **Logical Operators**: Demonstrate the `&&` (AND), `||` (OR), and `!` (NOT)
    operators using boolean variables.
4.  **Increment Operator**: Show the effect of the post-increment operator (`++`).

*/

#include <iostream>

int main() {
    int a = 10;
    int b = 3;

    // 1. Arithmetic Operators
    std::cout << "--- Arithmetic Operators ---" << std::endl;
    std::cout << "a + b = " << (a + b) << std::endl;       // Sum
    std::cout << "a - b = " << (a - b) << std::endl;       // Difference
    std::cout << "a * b = " << (a * b) << std::endl;       // Product
    std::cout << "a / b = " << (a / b) << std::endl;       // Quotient (integer division)
    std::cout << "a % b = " << (a % b) << std::endl;       // Remainder (modulo)

    // 2. Relational Operators
    double c = 5.5;
    double d = 5.5;
    std::cout << "\n--- Relational Operators ---" << std::endl;
    std::cout << std::boolalpha; // Print bools as "true" or "false"
    std::cout << "a > b: " << (a > b) << std::endl;
    std::cout << "a < b: " << (a < b) << std::endl;
    std::cout << "c == d: " << (c == d) << std::endl;

    // 3. Logical Operators
    bool hasKey = true;
    bool hasPermission = false;
    std::cout << "\n--- Logical Operators ---" << std::endl;
    std::cout << "Can open door (hasKey && hasPermission): " << (hasKey && hasPermission) << std::endl;
    std::cout << "Can enter restricted area (hasKey || hasPermission): " << (hasKey || hasPermission) << std::endl;
    std::cout << "NOT hasKey (!hasKey): " << (!hasKey) << std::endl;

    // 4. Increment Operator
    int counter = 5;
    std::cout << "\n--- Increment Operator ---" << std::endl;
    std::cout << "Initial counter value: " << counter << std::endl;
    // Post-increment: The value is used first (for printing), then incremented.
    std::cout << "Counter value during post-increment: " << counter++ << std::endl;
    std::cout << "Counter value after post-increment: " << counter << std::endl;

    return 0;
}

/*
Expected Output:

--- Arithmetic Operators ---
a + b = 13
a - b = 7
a * b = 30
a / b = 3
a % b = 1

--- Relational Operators ---
a > b: true
a < b: false
c == d: true

--- Logical Operators ---
Can open door (hasKey && hasPermission): false
Can enter restricted area (hasKey || hasPermission): true
NOT hasKey (!hasKey): false

--- Increment Operator ---
Initial counter value: 5
Counter value during post-increment: 5
Counter value after post-increment: 6
*/ 