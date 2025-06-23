/*
Challenge 6: C-Style Arrays and Strings

Problem Statement:
Write a C++ program to demonstrate the use of basic C-style arrays and
null-terminated strings.

Requirements:
1.  **Integer Array**: Declare and initialize an integer array with 5 numbers.
    Use a loop to iterate through the array and print each element.
2.  **C-Style String**: Declare and initialize a character array (a C-style string)
    with a sample word.
3.  **String Traversal**: Write a function `printCString` that takes a `const char*`
    as an argument and prints the string character by character using a `while`
    loop that checks for the null terminator (`\0`).

*/

#include <iostream>
#include <cstring> // For strlen

// Function to print a C-style string
void printCString(const char* cstr) {
    std::cout << "Printing C-string character by character: ";
    // Loop until we find the null terminator character
    while (*cstr != '\0') {
        std::cout << *cstr;
        cstr++; // Move the pointer to the next character
    }
    std::cout << std::endl;
}

int main() {
    // 1. Integer Array
    int grades[] = {85, 92, 78, 95, 88};
    int numGrades = sizeof(grades) / sizeof(grades[0]); // A common way to get array size

    std::cout << "--- Integer Array ---" << std::endl;
    for (int i = 0; i < numGrades; ++i) {
        std::cout << "Grade " << i + 1 << ": " << grades[i] << std::endl;
    }

    // 2. C-Style String (a character array ending with '\0')
    char greeting[] = "Hello"; // The compiler automatically adds the null terminator

    std::cout << "\n--- C-Style String ---" << std::endl;
    std::cout << "The full string is: " << greeting << std::endl;
    std::cout << "The length of the string (using strlen) is: " << strlen(greeting) << std::endl;

    // 3. String Traversal with a function
    printCString(greeting);
    
    return 0;
}

/*
Expected Output:

--- Integer Array ---
Grade 1: 85
Grade 2: 92
Grade 3: 78
Grade 4: 95
Grade 5: 88

--- C-Style String ---
The full string is: Hello
The length of the string (using strlen) is: 5
Printing C-string character by character: Hello
*/ 