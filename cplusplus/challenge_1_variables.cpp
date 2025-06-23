/*
Challenge 1: Variables & Data Types

Problem Statement:
Write a C++ program that declares and initializes variables of different
fundamental data types (`int`, `double`, `char`, `bool`). The program should
then print the value of each variable along with a descriptive message.
Additionally, it should demonstrate the use of a `const` qualifier and
display the memory size of each data type using the `sizeof()` operator.

Requirements:
1.  Declare an integer variable for age.
2.  Declare a double-precision floating-point variable for an account balance.
3.  Declare a character variable for a grade (e.g., 'A', 'B').
4.  Declare a boolean variable to indicate if a user is active.
5.  Declare a constant integer for the number of months in a year.
6.  Print the value of each variable.
7.  Print the size in bytes of each data type using the `sizeof()` operator.
*/

#include <iostream>
#include <iomanip> // For std::fixed and std::setprecision

int main() {
    // 1. Declare and initialize an integer for age
    int userAge = 30;

    // 2. Declare and initialize a double for balance
    double accountBalance = 1250.75;

    // 3. Declare and initialize a character for a grade
    char grade = 'A';

    // 4. Declare and initialize a boolean for user status
    bool isUserActive = true;

    // 5. Declare a constant integer
    const int MONTHS_IN_YEAR = 12;
    // The line below would cause a compile-time error because constants cannot be changed.
    // MONTHS_IN_YEAR = 13;

    // 6. Print the value of each variable
    std::cout << "--- Variable Values ---" << std::endl;
    std::cout << "User Age: " << userAge << std::endl;
    // Use iomanip to format the double to two decimal places
    std::cout << "Account Balance: $" << std::fixed << std::setprecision(2) << accountBalance << std::endl;
    std::cout << "Final Grade: " << grade << std::endl;
    // std::boolalpha makes the bool print as "true" or "false" instead of 1 or 0
    std::cout << "Is User Active? " << std::boolalpha << isUserActive << std::endl;
    std.cout << "Months in a year: " << MONTHS_IN_YEAR << std::endl;

    // 7. Print the size of each data type
    std::cout << "\n--- Data Type Sizes ---" << std::endl;
    std::cout << "Size of int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Size of double: " << sizeof(double) << " bytes" << std::endl;
    std::cout << "Size of char: " << sizeof(char) << " byte" << std::endl;
    std::cout << "Size of bool: " << sizeof(bool) << " byte" << std::endl;

    return 0;
}

/*
Expected Output:

--- Variable Values ---
User Age: 30
Account Balance: $1250.75
Final Grade: A
Is User Active? true
Months in a year: 12

--- Data Type Sizes ---
Size of int: 4 bytes
Size of double: 8 bytes
Size of char: 1 byte
Size of bool: 1 byte
*/ 