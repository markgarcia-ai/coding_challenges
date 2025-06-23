/*
Challenge 9: Constructors & Destructors

Problem Statement:
Create a `Logger` class that demonstrates the object lifecycle. The constructor
should announce the creation of a `Logger` object, and the destructor should
announce its destruction. This is a fundamental concept in C++ for resource
management, often called RAII (Resource Acquisition Is Initialization).

Requirements:
1.  **Define the `Logger` class**:
    -   It should have a `private` member `std::string loggerName`.
    -   The `public` constructor should accept a name, store it, and print a
      message like "[name] Logger created."
    -   The `public` destructor (`~Logger`) should print a message like
      "[name] Logger destroyed."
2.  **Demonstrate Lifecycle**:
    -   In `main`, create a `Logger` object inside a specific scope (e.g., curly
      braces `{}`).
    -   Observe that the constructor is called upon creation.
    -   When the program execution leaves the scope, observe that the destructor
      is automatically called.

*/

#include <iostream>
#include <string>

// 1. Define the Logger class
class Logger {
private:
    std::string loggerName;

public:
    // Constructor: Called when an object is created
    Logger(std::string name) {
        loggerName = name;
        std::cout << "[" << loggerName << "] Logger created." << std::endl;
    }

    // Destructor: Called when an object is destroyed
    ~Logger() {
        std::cout << "[" << loggerName << "] Logger destroyed." << std::endl;
    }

    void logMessage(std::string message) {
        std::cout << "[" << loggerName << "] " << message << std::endl;
    }
};

// A function to demonstrate object scope
void someFunction() {
    std::cout << "--- Entering someFunction ---" << std::endl;
    Logger functionLogger("FunctionScopeLogger");
    functionLogger.logMessage("This logger exists only inside someFunction.");
    std::cout << "--- Exiting someFunction ---" << std::endl;
    // functionLogger is destroyed here as it goes out of scope
}

int main() {
    std::cout << "--- Program Start ---" << std::endl;

    Logger mainLogger("MainScopeLogger");
    mainLogger.logMessage("This logger exists throughout main.");

    someFunction();

    std::cout << "--- Back in main, after someFunction call ---" << std::endl;
    
    std::cout << "--- Program End ---" << std::endl;
    // mainLogger is destroyed here as main finishes
    return 0;
}

/*
Expected Output:

--- Program Start ---
[MainScopeLogger] Logger created.
[MainScopeLogger] This logger exists throughout main.
--- Entering someFunction ---
[FunctionScopeLogger] Logger created.
[FunctionScopeLogger] This logger exists only inside someFunction.
--- Exiting someFunction ---
[FunctionScopeLogger] Logger destroyed.
--- Back in main, after someFunction call ---
--- Program End ---
[MainScopeLogger] Logger destroyed.
*/ 