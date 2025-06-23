/*
Challenge 20: Smart Pointers (std::unique_ptr)

Problem Statement:
Write a C++ program that uses `std::unique_ptr` to manage the memory of a
dynamically allocated object. This demonstrates the concept of RAII (Resource
Acquisition Is Initialization) and ownership, where the smart pointer is
responsible for deleting the object when its managing smart pointer goes out of scope.

Requirements:
1.  **Include Headers**: `<iostream>`, `<string>`, and `<memory>`.
2.  **Create a Simple Class**: Define a simple `Resource` class with a
    constructor that prints a "Resource created" message and a destructor that
    prints a "Resource destroyed" message.
3.  **Use `std::unique_ptr`**:
    -   Inside a function or a limited scope in `main`, create an instance of
      `Resource` on the heap using `new`.
    -   Manage this instance with a `std::unique_ptr` using `std::make_unique`.
    -   Call a method on the object using the smart pointer's `->` operator.
4.  **Observe Automatic Cleanup**: When the `unique_ptr` goes out of scope,
    its destructor will be called automatically, which in turn will `delete`
    the `Resource` object, invoking its destructor. You don't need to manually
    call `delete`.

*/

#include <iostream>
#include <string>
#include <memory> // Required for smart pointers

// 2. A simple class to demonstrate lifecycle management
class Resource {
private:
    std::string name;
public:
    Resource(std::string n) : name(n) {
        std::cout << "Resource '" << name << "' created." << std::endl;
    }
    ~Resource() {
        std::cout << "Resource '" << name << "' destroyed." << std::endl;
    }
    void use() {
        std::cout << "Using resource '" << name << "'." << std::endl;
    }
};

void manageResource() {
    std::cout << "\n--- Entering manageResource scope ---" << std::endl;
    
    // 3. Create a Resource managed by a unique_ptr.
    // std::make_unique is the recommended way to create unique_ptrs.
    auto uniqueRes = std::make_unique<Resource>("MyUniqueResource");
    
    // Use the resource via the smart pointer
    uniqueRes->use();

    // No need to call delete. The unique_ptr will do it for us.
    std::cout << "--- Exiting manageResource scope ---" << std::endl;
} // uniqueRes goes out of scope here, and its destructor is called.

int main() {
    std::cout << "--- Program Start ---" << std::endl;
    manageResource();
    std::cout << "--- Program End ---" << std::endl;
    return 0;
}

/*
Expected Output:

--- Program Start ---

--- Entering manageResource scope ---
Resource 'MyUniqueResource' created.
Using resource 'MyUniqueResource'.
--- Exiting manageResource scope ---
Resource 'MyUniqueResource' destroyed.
--- Program End ---
*/ 