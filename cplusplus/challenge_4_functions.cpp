/*
Challenge 4: Functions

Problem Statement:
Write a C++ program that uses functions to calculate the area of a circle
and to print a formatted message. This demonstrates how to define, declare (prototype),
and call functions.

Requirements:
1.  **Function Declaration (Prototype)**: Declare a function `calculateCircleArea`
    that takes a double `radius` and returns a double.
2.  **Function Definition**: Define the `calculateCircleArea` function. It should
    use the formula `Area = PI * radius^2`.
3.  **void Function**: Create a function `printMessage` that takes a string and
    prints it to the console, surrounded by a decorative border. This function
    will not return a value.
4.  **main Function**: In the `main` function, call `calculateCircleArea` with a
    sample radius and call `printMessage` with the result.

*/

#include <iostream>
#include <string>
#include <cmath> // For M_PI on some compilers, or use a const
#include <iomanip>

// Define a constant for PI
const double PI = 3.14159;

// 1. Function Declaration (Prototype)
double calculateCircleArea(double radius);
void printMessage(std::string message);

int main() {
    double radius = 5.0;
    
    // 4. Call the area calculation function
    double area = calculateCircleArea(radius);

    // Prepare the message string
    std::string resultMessage = "The area of a circle with radius " + 
                              std::to_string(radius) + " is " + 
                              std::to_string(area);

    // 4. Call the void function to print the formatted message
    printMessage(resultMessage);

    return 0;
}

// 2. Function Definition for calculateCircleArea
double calculateCircleArea(double radius) {
    // Area = PI * r^2
    return PI * radius * radius;
}

// 3. Function Definition for printMessage
void printMessage(std::string message) {
    std::cout << "****************************************" << std::endl;
    std::cout << message << std::endl;
    std::cout << "****************************************" << std::endl;
}


/*
Expected Output:

****************************************
The area of a circle with radius 5.000000 is 78.539750
****************************************
*/ 