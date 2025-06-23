/*
Challenge 17: The Standard Template Library (STL) - std::map

Problem Statement:
Write a C++ program that uses `std::map` to store the inventory count of
different fruits. This demonstrates how to use a map for key-value storage,
insertion, lookup, and iteration.

Requirements:
1.  **Include Headers**: Include `<iostream>`, `<string>`, and `<map>`.
2.  **Initialization**: Create a `std::map` where keys are `std::string` (fruit name)
    and values are `int` (inventory count).
3.  **Inserting Elements**: Add several fruits and their counts to the map.
    Demonstrate two ways to insert: using `[]` and using `.insert()`.
4.  **Accessing Elements**: Retrieve and print the count of a specific fruit
    using its key.
5.  **Updating Elements**: Update the count of an existing fruit.
6.  **Checking for Existence**: Use the `.count()` or `.find()` method to check if a
    fruit exists in the map before trying to access it.
7.  **Iteration**: Use a range-based `for` loop to iterate through the map and
    print all key-value pairs.

*/

#include <iostream>
#include <string>
#include <map>

int main() {
    // 2. Create a map to store fruit inventory
    std::map<std::string, int> fruitInventory;

    // 3. Insert elements into the map
    fruitInventory["apples"] = 50;        // Using operator[]
    fruitInventory["bananas"] = 120;
    fruitInventory.insert(std::make_pair("oranges", 75)); // Using insert()

    std::cout << "--- Initial Inventory ---" << std::endl;
    // 7. Iterate and print all pairs
    for (const auto& pair : fruitInventory) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    // 4. Access an element
    std::cout << "\n--- Accessing & Updating ---" << std::endl;
    std::cout << "Initial count of apples: " << fruitInventory["apples"] << std::endl;
    
    // 5. Update an element
    fruitInventory["apples"] = 45; // Sold 5 apples
    std::cout << "Updated count of apples: " << fruitInventory["apples"] << std::endl;

    // 6. Check for the existence of a key
    std::cout << "\n--- Checking for Existence ---" << std::endl;
    std::string key = "pears";
    if (fruitInventory.count(key)) {
        std::cout << key << " are in stock." << std::endl;
    } else {
        std::cout << key << " are not in stock." << std::endl;
    }

    key = "bananas";
    if (fruitInventory.count(key)) {
        std::cout << key << " are in stock." << std::endl;
    } else {
        std::cout << key << " are not in stock." << std::endl;
    }

    return 0;
}

/*
Expected Output (maps are ordered by key):

--- Initial Inventory ---
apples: 50
bananas: 120
oranges: 75

--- Accessing & Updating ---
Initial count of apples: 50
Updated count of apples: 45

--- Checking for Existence ---
pears are not in stock.
bananas are in stock.
*/ 