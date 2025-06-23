/*
Challenge 15: The Standard Template Library (STL) - std::string

Problem Statement:
Write a C++ program that uses `std::string` to perform common string
manipulations. This demonstrates the power and safety of using the C++
standard string class over C-style character arrays.

Requirements:
1.  **Initialization**: Create two `std::string` objects.
2.  **Concatenation**: Combine the two strings into a third string using the
    `+` operator.
3.  **Accessing Characters**: Access and print the first character of the
    combined string.
4.  **Finding Substrings**: Use the `.find()` method to find the position of a
    substring.
5.  **Getting Length**: Use the `.length()` method to find the number of
    characters in the string.

*/

#include <iostream>
#include <string>

int main() {
    // 1. Initialization
    std::string firstName = "John";
    std::string lastName = "Doe";

    std::cout << "--- Initialization ---" << std::endl;
    std::cout << "First Name: " << firstName << std::endl;
    std::cout << "Last Name: " << lastName << std::endl;

    // 2. Concatenation
    std::string fullName = firstName + " " + lastName;
    std::cout << "\n--- Concatenation ---" << std::endl;
    std::cout << "Full Name: " << fullName << std::endl;

    // 3. Accessing Characters
    std::cout << "\n--- Character Access ---" << std::endl;
    if (!fullName.empty()) {
        std::cout << "The first initial is: " << fullName[0] << std::endl;
    }

    // 4. Finding Substrings
    std::cout << "\n--- Substring Search ---" << std::endl;
    std::string searchTerm = "Doe";
    size_t pos = fullName.find(searchTerm); // size_t is the type returned by find

    if (pos != std::string::npos) { // npos means "not found"
        std::cout << "'" << searchTerm << "' found at position: " << pos << std::endl;
    } else {
        std::cout << "'" << searchTerm << "' not found." << std::endl;
    }

    // 5. Getting Length
    std::cout << "\n--- String Length ---" << std::endl;
    std::cout << "The length of the full name is: " << fullName.length() << " characters." << std::endl;

    return 0;
}

/*
Expected Output:

--- Initialization ---
First Name: John
Last Name: Doe

--- Concatenation ---
Full Name: John Doe

--- Character Access ---
The first initial is: J

--- Substring Search ---
'Doe' found at position: 5

--- String Length ---
The length of the full name is: 8 characters.
*/ 