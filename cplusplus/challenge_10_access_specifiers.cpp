/*
Challenge 10: Access Specifiers

Problem Statement:
Create an `Employee` class that demonstrates the use of `public` and `private`
access specifiers. The class should store an employee's salary privately
to protect it from direct external modification, providing public methods
to interact with it safely.

Requirements:
1.  **Define the `Employee` class**:
    -   It should have a `private` member variable `double salary`.
    -   It should have a `public` constructor that initializes the `salary`.
    -   It should have a `public` method `getSalary()` that returns the salary.
    -   It should have a `public` method `giveRaise()` that accepts a percentage
      (e.g., 5.0 for 5%) and updates the salary, but only if the percentage
      is positive.
2.  **Demonstrate Encapsulation**:
    -   In `main`, create an `Employee` object.
    -   Show that you can access the public methods (`getSalary`, `giveRaise`).
    -   Include a commented-out line of code showing that you *cannot* access
      the private `salary` member directly, which would cause a compilation error.
      This enforces the controlled access.

*/

#include <iostream>
#include <iomanip>

// 1. Define the Employee class
class Employee {
private:
    // The salary is private, so it cannot be accessed directly from outside the class.
    double salary;

public:
    // Public constructor to initialize the private member
    Employee(double initialSalary) {
        salary = initialSalary > 0 ? initialSalary : 0;
    }

    // Public method to safely get the salary
    double getSalary() {
        return salary;
    }

    // Public method to safely modify the salary
    void giveRaise(double percentage) {
        if (percentage > 0) {
            salary *= (1.0 + percentage / 100.0);
            std::cout << "Success! Raise of " << percentage << "% applied." << std::endl;
        } else {
            std::cout << "Error: Raise percentage must be positive." << std::endl;
        }
    }
};

int main() {
    // 2. Create an Employee object
    Employee emp(50000.0);

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Initial salary: $" << emp.getSalary() << std::endl;

    // This line would cause a compilation error because salary is private:
    // emp.salary = 1000000.0; // ERROR: 'double Employee::salary' is private

    std::cout << "\n--- Attempting to give a raise ---" << std::endl;
    
    // Give a valid raise
    emp.giveRaise(5.0);
    std::cout << "New salary: $" << emp.getSalary() << std::endl;

    // Attempt an invalid raise
    emp.giveRaise(-2.0);
    std::cout << "Salary remains: $" << emp.getSalary() << std::endl;

    return 0;
}

/*
Expected Output:

Initial salary: $50000.00

--- Attempting to give a raise ---
Success! Raise of 5.00% applied.
New salary: $52500.00
Error: Raise percentage must be positive.
Salary remains: $52500.00
*/ 