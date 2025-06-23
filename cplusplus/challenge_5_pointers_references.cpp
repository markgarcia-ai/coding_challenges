/*
Challenge 5: Pointers & References

Problem Statement:
Write a C++ program that demonstrates the use of pointers and references.
The program should include functions that modify variables using both pointers
and references to show how they can alter data outside of their own scope.

Requirements:
1.  **Pointer Basics**: In `main`, declare an integer `num`. Create a pointer `pNum`
    that stores the memory address of `num`. Print the value of `num`, its
    memory address, the address stored in the pointer, and the value the
    pointer points to.
2.  **Modify via Pointer**: Create a `void` function `incrementWithPointer` that
    takes an integer pointer as an argument and uses it to increment the
    original variable's value.
3.  **Modify via Reference**: Create a `void` function `multiplyWithReference` that
    takes an integer reference as an argument and multiplies the original
    variable's value.
4.  **Demonstrate**: In `main`, call both functions and print the value of `num`
    after each call to show it has been modified.

*/

#include <iostream>

// Function that takes a pointer as an argument
void incrementWithPointer(int* ptr) {
    // Check for null pointer to be safe
    if (ptr != nullptr) {
        (*ptr)++; // Dereference the pointer and increment the value it points to
    }
}

// Function that takes a reference as an argument
void multiplyWithReference(int& ref) {
    ref *= 2; // Directly modify the original variable through the reference
}

int main() {
    int num = 10;

    // 1. Pointer Basics
    int* pNum = &num; // pNum now holds the memory address of num

    std::cout << "--- Initial State ---" << std::endl;
    std::cout << "Value of num: " << num << std::endl;
    std::cout << "Address of num (&num): " << &num << std::endl;
    std::cout << "Value of pointer (pNum): " << pNum << std::endl;
    std::cout << "Value pointed to by pNum (*pNum): " << *pNum << std::endl;

    // 2. Modify via Pointer
    incrementWithPointer(pNum);
    std::cout << "\n--- After incrementWithPointer ---" << std::endl;
    std::cout << "Value of num: " << num << std::endl;

    // 3. Modify via Reference
    multiplyWithReference(num);
    std::cout << "\n--- After multiplyWithReference ---" << std::endl;
    std::cout << "Value of num: " << num << std::endl;

    return 0;
}

/*
Expected Output (memory addresses will vary):

--- Initial State ---
Value of num: 10
Address of num (&num): 0x7ff7bfeff1ac
Value of pointer (pNum): 0x7ff7bfeff1ac
Value pointed to by pNum (*pNum): 10

--- After incrementWithPointer ---
Value of num: 11

--- After multiplyWithReference ---
Value of num: 22
*/ 