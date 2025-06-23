/*
Challenge 18: The Standard Template Library (STL) - Algorithms

Problem Statement:
Write a C++ program that uses common algorithms from the `<algorithm>` library
to process a `std::vector` of integers. You will sort the vector and then
search for a specific element within it.

Requirements:
1.  **Include Headers**: `<iostream>`, `<vector>`, and `<algorithm>`.
2.  **Initialization**: Create a `std::vector` of integers with some unsorted values.
3.  **`std::sort`**: Use `std::sort` to sort the vector in ascending order.
    `std::sort` takes two iterators, `begin()` and `end()`, to define the
    range to be sorted.
4.  **`std::find`**: Use `std::find` to search for a specific value in the vector.
    `std::find` also takes `begin()` and `end()` iterators and a value to search for.
    It returns an iterator to the first occurrence of the value, or the `end()`
    iterator if the value is not found.
5.  **Demonstrate**: Print the vector before sorting, after sorting, and the
    result of the search.

*/

#include <iostream>
#include <vector>
#include <algorithm> // Required for std::sort and std::find

// Helper function to print a vector's contents
void printVector(const std::vector<int>& vec) {
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    // 2. Initialize a vector with unsorted data
    std::vector<int> numbers = {40, 10, 50, 30, 20};

    std::cout << "--- Initial Vector ---" << std::endl;
    printVector(numbers);

    // 3. Sort the vector
    std::sort(numbers.begin(), numbers.end());

    std::cout << "\n--- Sorted Vector ---" << std::endl;
    printVector(numbers);

    // 4. Search for a value in the vector
    std::cout << "\n--- Searching for a Value ---" << std::endl;
    int valueToFind = 30;
    
    // std::find returns an iterator
    auto it = std::find(numbers.begin(), numbers.end(), valueToFind);

    // 5. Check the result of the search
    if (it != numbers.end()) {
        // We found the value. 'it' points to it.
        std::cout << "Value " << valueToFind << " found in the vector." << std::endl;
        // We can find its index using std::distance
        auto index = std::distance(numbers.begin(), it);
        std::cout << "It is at index: " << index << std::endl;
    } else {
        // The iterator is at the end, meaning the value was not found
        std::cout << "Value " << valueToFind << " not found in the vector." << std::endl;
    }

    return 0;
}

/*
Expected Output:

--- Initial Vector ---
40 10 50 30 20 

--- Sorted Vector ---
10 20 30 40 50 

--- Searching for a Value ---
Value 30 found in the vector.
It is at index: 2
*/ 