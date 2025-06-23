/*
Challenge 16: The Standard Template Library (STL) - std::vector

Problem Statement:
Write a C++ program that uses `std::vector` to manage a list of scores.
This will demonstrate how to create a vector, add elements to it, access
elements, and iterate over its contents.

Requirements:
1.  **Include Headers**: Include `<iostream>` and `<vector>`.
2.  **Initialization**: Create an empty `std::vector` that can hold integers.
3.  **Adding Elements**: Use the `.push_back()` method to add several scores
    to the vector.
4.  **Accessing Elements**: Access an element by its index (e.g., `scores[1]`).
5.  **Iteration**: Use a range-based `for` loop to iterate through the vector
    and print all the scores.
6.  **Size**: Print the number of elements currently in the vector using the
    `.size()` method.

*/

#include <iostream>
#include <vector>

int main() {
    // 2. Create an empty vector of integers
    std::vector<int> scores;

    // 3. Add elements to the end of the vector
    scores.push_back(88);
    scores.push_back(95);
    scores.push_back(76);
    scores.push_back(100);

    std::cout << "--- Vector Contents ---" << std::endl;

    // 5. Iterate through the vector with a range-based for loop
    for (int score : scores) {
        std::cout << score << std::endl;
    }

    // 4. Access a specific element by index
    std::cout << "\n--- Element Access ---" << std::endl;
    std::cout << "The second score is: " << scores[1] << std::endl;

    // Modify an element
    scores[1] = 97;
    std::cout << "The second score after modification is: " << scores[1] << std::endl;

    // 6. Get the size of the vector
    std::cout << "\n--- Vector Size ---" << std::endl;
    std::cout << "The number of scores is: " << scores.size() << std::endl;

    return 0;
}

/*
Expected Output:

--- Vector Contents ---
88
95
76
100

--- Element Access ---
The second score is: 95
The second score after modification is: 97

--- Vector Size ---
The number of scores is: 4
*/ 