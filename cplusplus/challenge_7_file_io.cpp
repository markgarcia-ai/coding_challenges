/*
Challenge 7: Basic File I/O

Problem Statement:
Write a C++ program that performs basic file input and output operations.
The program will first write a short message to a file named `notes.txt`.
Then, it will read the content back from the same file and print it to the
console.

Requirements:
1.  **Writing to a File**:
    -   Include the `<fstream>` header.
    -   Create an `std::ofstream` (output file stream) object.
    -   Open the file `notes.txt`.
    -   Check if the file opened successfully.
    -   Write a few lines of text to the file.
    -   Close the file stream.
2.  **Reading from a File**:
    -   Create an `std::ifstream` (input file stream) object.
    -   Open the same `notes.txt` file.
    -   Check if the file opened successfully.
    -   Read the file line by line using `std::getline` and print each line
      to the console.
    -   Close the file stream.

*/

#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::string filename = "notes.txt";

    // 1. Writing to a file
    std::cout << "--- Writing to file: " << filename << " ---" << std::endl;
    // Create and open an output file stream
    std::ofstream outFile(filename);

    if (outFile.is_open()) {
        outFile << "Hello from C++!" << std::endl;
        outFile << "This is the second line." << std::endl;
        outFile << "File I/O is essential." << std::endl;
        outFile.close(); // Close the file
        std::cout << "Successfully wrote to the file." << std::endl;
    } else {
        std::cerr << "Error: Could not open the file for writing." << std::endl;
        return 1; // Return an error code
    }

    // 2. Reading from a file
    std::cout << "\n--- Reading from file: " << filename << " ---" << std::endl;
    // Create and open an input file stream
    std::ifstream inFile(filename);
    std::string line;

    if (inFile.is_open()) {
        // Read the file line by line until the end
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close(); // Close the file
    } else {
        std::cerr << "Error: Could not open the file for reading." << std::endl;
        return 1; // Return an error code
    }

    return 0;
}

/*
Expected Output:

--- Writing to file: notes.txt ---
Successfully wrote to the file.

--- Reading from file: notes.txt ---
Hello from C++!
This is the second line.
File I/O is essential.
*/ 