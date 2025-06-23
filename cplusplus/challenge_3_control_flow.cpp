/*
Challenge 3: Control Flow

Problem Statement:
Write a C++ program that demonstrates conditional logic and looping. The program
should check a user's grade and provide a corresponding remark. It should then
use a loop to print a countdown.

Requirements:
1.  **Conditional Logic**: Use an `if`, `else if`, and `else` structure to check
    a character variable `grade`.
    - If the grade is 'A', print "Excellent!".
    - If the grade is 'B', print "Good job!".
    - If the grade is 'C', print "You passed.".
    - For any other grade, print "Please see your instructor.".
2.  **Looping**: Use a `for` loop to print a countdown from 5 down to 1,
    followed by "Liftoff!".

*/

#include <iostream>

int main() {
    // 1. Conditional Logic (if/else if/else)
    char grade = 'B';
    std::cout << "--- Grade Evaluation ---" << std::endl;
    std::cout << "Your grade is: " << grade << std::endl;
    
    if (grade == 'A') {
        std::cout << "Remark: Excellent!" << std::endl;
    } else if (grade == 'B') {
        std::cout << "Remark: Good job!" << std::endl;
    } else if (grade == 'C') {
        std::cout << "Remark: You passed." << std::endl;
    } else {
        std::cout << "Remark: Please see your instructor." << std::endl;
    }

    // 2. Looping (for loop)
    std::cout << "\n--- Countdown ---" << std::endl;
    for (int i = 5; i > 0; --i) {
        std::cout << i << "..." << std::endl;
    }
    std::cout << "Liftoff!" << std::endl;

    return 0;
}

/*
Expected Output:

--- Grade Evaluation ---
Your grade is: B
Remark: Good job!

--- Countdown ---
5...
4...
3...
2...
1...
Liftoff!
*/ 