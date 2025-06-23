/*
Challenge 8: Classes & Objects

Problem Statement:
Create a C++ program that defines a `Car` class to represent a car. The class
should encapsulate the car's properties (like brand and year) and behaviors
(like printing its details). Then, create instances (objects) of this class.

Requirements:
1.  **Define the `Car` class**:
    -   It should have two `private` member variables: a `std::string` for the brand
      and an `int` for the year.
    -   It should have a `public` constructor that takes the brand and year to
      initialize the member variables.
    -   It should have a `public` member function (method) `printDetails()` that
      prints the car's brand and year to the console.
2.  **Create Objects**: In the `main` function, create two different `Car` objects
    (instances of the `Car` class) with different brands and years.
3.  **Demonstrate**: Call the `printDetails()` method on each object to show
    that each instance holds its own separate data.

*/

#include <iostream>
#include <string>

// 1. Define the Car class
class Car {
private:
    std::string brand;
    int year;

public:
    // Public constructor to initialize the object
    Car(std::string b, int y) {
        brand = b;
        year = y;
    }

    // Public method to display the car's details
    void printDetails() {
        std::cout << "Car Details: " << year << " " << brand << std::endl;
    }
}; // Don't forget the semicolon at the end of a class definition

int main() {
    // 2. Create two Car objects
    Car car1("Toyota", 2021);
    Car car2("Ford", 2019);

    // 3. Call methods on each object
    std::cout << "--- Information for Car 1 ---" << std::endl;
    car1.printDetails();

    std::cout << "\n--- Information for Car 2 ---" << std::endl;
    car2.printDetails();

    return 0;
}

/*
Expected Output:

--- Information for Car 1 ---
Car Details: 2021 Toyota

--- Information for Car 2 ---
Car Details: 2019 Ford
*/ 